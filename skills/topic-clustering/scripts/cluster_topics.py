"""
BERTopic branch of the bert-family skill: grouping texts by topic.

Input  : docs.json — an array of [{"text": "...", "label": "..."}]
Output : topics.json (full result) + a human-readable summary on stdout.

The embedding model is multilingual. min_topic_size is scaled to the size of the corpus so that
small samples do not end up entirely in the outlier bucket.
"""

import argparse
import json
import sys
from pathlib import Path

# Windows: stdout defaults to cp1252 and dies on non-Latin text — force utf-8.
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

# Stopwords are bundled so that topic labels come out meaningful. Russian + English + a Serbian
# minimum. Add your own language here if topic keywords come back full of function words.
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
    ap.add_argument("--docs", required=True, help="JSON: array of {text, label?}")
    ap.add_argument("--out", default="topics.json")
    ap.add_argument("--model", default="paraphrase-multilingual-MiniLM-L12-v2")
    ap.add_argument("--min-topic-size", type=int, default=None)
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
    print(f"Documents in scope: {n}")
    if n < 5:
        print("Too few documents to cluster (about 5 is the minimum).")
        sys.exit(2)

    from bertopic import BERTopic
    from sentence_transformers import SentenceTransformer
    from sklearn.feature_extraction.text import CountVectorizer

    # min_topic_size scaled to corpus size: with little data, lower the threshold, otherwise
    # everything drifts into topic -1.
    mts = args.min_topic_size or (2 if n < 60 else 3 if n < 300 else 10)

    embed = SentenceTransformer(args.model)

    # Stopwords come from the list above rather than nltk, which is unreliable to fetch at
    # runtime. This keeps topic labels readable instead of "the/of/and/to".
    vectorizer = CountVectorizer(stop_words=STOPWORDS)

    topic_model = BERTopic(
        embedding_model=embed,
        vectorizer_model=vectorizer,
        min_topic_size=mts,
        language="multilingual",
        verbose=False,
    )
    topics, _ = topic_model.fit_transform(texts)

    # Orphan documents (topic -1) get reassigned to their nearest topic.
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

    print(f"\nTopics found: {len(result)} -> {args.out}\n")
    for r in result:
        print(f"=== TOPIC {r['topic_id']} ({r['size']} docs): {', '.join(r['keywords'])} ===")
        for m in r["messages"][:3]:
            lab = f"[{m['label']}] " if m["label"] else ""
            print(f"  - {lab}{m['text'][:90]}")
        if r["size"] > 3:
            print(f"  ... and {r['size'] - 3} more")
        print()


if __name__ == "__main__":
    main()
