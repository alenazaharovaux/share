"""
Скилл topic-clustering: группировка текстов по темам через BERTopic.

Вход  : docs.json — массив [{"text": "...", "label": "..."}]
Выход : topics.json (полный результат) + человекочитаемая сводка в stdout.

Модель эмбеддингов многоязычная (русский/сербский/английский). min_topic_size
подбирается под объём данных, чтобы на малых выборках не уносить всё в «мусор».

Воспроизводимость: шаг снижения размерности (UMAP) по своей природе случайный,
поэтому один и тот же вход даёт немного разные темы при каждом прогоне. Чтобы
результат был стабильным (тот же вход -> тот же результат), UMAP фиксируется
через random_state=--seed (по умолчанию 42). Это нужно, когда разбор надо
повторить и получить точь-в-точь то же самое. Если фиксация не нужна и хочется,
чтобы модель каждый раз искала группы заново, передай --no-seed.
"""

import argparse
import json
import sys
from pathlib import Path

# Windows: stdout по умолчанию cp1252 и падает на кириллице — принудительно utf-8.
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

# Стоп-слова вшиты, чтобы названия тем были осмысленными. RU + EN + сербский минимум.
_RU_STOP = (
    "и в во не что он на я с со как а то все она так его но да ты к у же вы за бы по "
    "только ее мне было вот от меня еще нет о из ему теперь когда даже ну вдруг ли если "
    "уже или ни быть был него до вас нибудь опять уж вам ведь там потом себя ничего ей "
    "может они тут где есть надо ней для мы тебя их чем была сам чтоб без будто чего раз "
    "тоже себе под будет ж кто этот того потому этого какой совсем ним здесь этом один "
    "почти мой тем чтобы нее сейчас были куда зачем всех никогда можно при наконец два об "
    "другой хоть после над больше тот через эти нас про всего них какая много разве три "
    "эту моя впрочем хорошо свою этой перед иногда лучше чуть том нельзя такой им более "
    "всегда конечно всю между это все своих также этих очень нашего нужно свои весь так же "
    "который которые нашей просто нам он-то тем-то этом-то нибудь-то нашими"
).split()
_EN_STOP = (
    "the a an and or but if then of to in on for with at by from as is are was were be "
    "been this that these those it its i you he she they we not no yes do does did will "
    "would can could should have has had my your our their his her me us them so just very"
).split()
_SR_STOP = "je su da se na za od koji koja koje sam smo ste ili ali kao sa u i o li ne".split()
STOPWORDS = sorted(set(_RU_STOP) | set(_EN_STOP) | set(_SR_STOP))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--docs", required=True, help="JSON: массив {text, label?}")
    ap.add_argument("--out", default="topics.json")
    ap.add_argument("--model", default="paraphrase-multilingual-MiniLM-L12-v2")
    ap.add_argument("--min-topic-size", type=int, default=None)
    ap.add_argument("--seed", type=int, default=42,
                    help="фиксирует UMAP -> один вход даёт один и тот же результат")
    ap.add_argument("--no-seed", action="store_true",
                    help="выключить фиксацию: каждый прогон ищет группы заново")
    args = ap.parse_args()

    docs_raw = json.loads(Path(args.docs).read_text(encoding="utf-8"))
    texts, labels = [], []
    for d in docs_raw:
        t = (d.get("text") or "").strip()
        if len(t) < 15:
            continue
        texts.append(t)
        labels.append(d.get("label", ""))

    n = len(texts)
    print(f"Документов в работе: {n}")
    if n < 5:
        print("Слишком мало документов для кластеризации (нужно хотя бы ~5).")
        sys.exit(2)

    from bertopic import BERTopic
    from sentence_transformers import SentenceTransformer
    from sklearn.feature_extraction.text import CountVectorizer
    from umap import UMAP

    # min_topic_size под объём: мало данных -> меньше порог, иначе всё уедет в тему -1.
    mts = args.min_topic_size or (2 if n < 60 else 3 if n < 300 else 10)

    embed = SentenceTransformer(args.model)

    # Стоп-слова вшиты в скрипт (не тянем nltk на рантайме — это ненадёжно), чтобы
    # названия тем были читаемыми, а не «не/то/что/на». Русский + английский + сербский минимум.
    vectorizer = CountVectorizer(stop_words=STOPWORDS)

    # UMAP явно, чтобы зафиксировать random_state. Параметры — дефолты BERTopic
    # (n_neighbors=15, n_components=5, min_dist=0.0, cosine). random_state=seed делает
    # результат воспроизводимым; --no-seed убирает фиксацию (random_state=None).
    seed = None if args.no_seed else args.seed
    umap_model = UMAP(n_neighbors=15, n_components=5, min_dist=0.0,
                      metric="cosine", random_state=seed)
    if seed is not None:
        print(f"Фиксация включена (seed={seed}): один и тот же вход даст один результат.")
    else:
        print("Фиксация выключена (--no-seed): темы могут отличаться между прогонами.")

    topic_model = BERTopic(
        embedding_model=embed,
        umap_model=umap_model,
        vectorizer_model=vectorizer,
        min_topic_size=mts,
        language="multilingual",
        verbose=False,
    )
    topics, _ = topic_model.fit_transform(texts)

    # «Ничьи» посты (тема -1) раскидываем по ближайшим темам.
    try:
        topics = topic_model.reduce_outliers(texts, topics)
    except Exception:
        pass

    result = []
    for _, row in topic_model.get_topic_info().iterrows():
        tid = int(row["Topic"])
        if tid == -1:
            continue
        keywords = [w for w, _ in topic_model.get_topic(tid)[:6]]
        members = [
            {"text": texts[i], "label": labels[i]}
            for i, t in enumerate(topics)
            if t == tid
        ]
        result.append(
            {"topic_id": tid, "keywords": keywords, "size": len(members), "messages": members}
        )
    result.sort(key=lambda x: x["size"], reverse=True)

    Path(args.out).write_text(
        json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    print(f"\nНайдено тем: {len(result)} -> {args.out}\n")
    for r in result:
        print(f"=== ТЕМА {r['topic_id']} ({r['size']} шт): {', '.join(r['keywords'])} ===")
        for m in r["messages"][:3]:
            lab = f"[{m['label']}] " if m["label"] else ""
            print(f"  - {lab}{m['text'][:90]}")
        if r["size"] > 3:
            print(f"  ... ещё {r['size'] - 3}")
        print()


if __name__ == "__main__":
    main()
