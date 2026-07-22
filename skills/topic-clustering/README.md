# Topic Clustering

Cluster large volumes of text into semantic topics with BERTopic, without touching a terminal. You bring a Telegram export, a chat history, a set of transcripts or a pile of posts; Claude flattens it into a common format, installs what is missing, runs the clustering, and reports the topics in chat. Each topic is a real list of documents rather than a summary, so nothing is invented and coverage is not lost.

## Installation

**macOS / Linux:**
```bash
cp -r topic-clustering ~/.claude/skills/topic-clustering
```

**Windows:**
```powershell
Copy-Item -Recurse topic-clustering $env:USERPROFILE\.claude\skills\topic-clustering
```

## Usage

Say any of these to Claude Code:

- "what are these messages about?"
- "group my Telegram export by topic"
- "cluster these transcripts by meaning"
- "what topics are in this dump of posts?"
- "run BERTopic on this table"

The skill reads whatever you bring, flattens it into an intermediate `docs.json`, runs the clustering, and shows topics with their keywords and example documents.

## What it does

BERTopic turns each text into a meaning vector, groups the semantically close ones into clusters, and derives keywords for each cluster with class-based TF-IDF. The result is a set of topics where every topic points at the actual documents that belong to it. This is what makes it different from asking a chat model "what are the themes here": it does not fit into a context window, it does not hallucinate topics, and it does not quietly cover only part of the corpus.

| Step | What happens |
|------|--------------|
| Input | Any format — Telegram export, chat history, transcripts, spreadsheet, pasted text |
| Flatten | Reduced to `docs.json`: an array of `{text, label}`, parsed for the actual data |
| Cluster (layer A) | `scripts/cluster_topics.py` runs BERTopic and tags each text into a topic → `topics.json` |
| Read (layer B) | `scripts/render_clusters.py` renders a readable HTML of what the algorithm clustered — keywords, counts, sample quotes |
| Synthesize (layer C) | Only if you say yes: Claude groups the topics into clear threads and writes takeaways, reviewable and editable |

The line matters: BERTopic only tags texts into topics and gives keywords and counts (layers A and B, the machine). Naming the threads and writing takeaways is a separate step done by Claude reading the actual texts (layer C) — the skill keeps them apart and never passes synthesis off as the algorithm's own output.

## Dependencies

Claude installs this on first use, so there is nothing to set up in advance:

- `bertopic` (pulls in `sentence-transformers`, `scikit-learn`, `umap-learn`, `hdbscan`)

The first run downloads a multilingual embedding model of several hundred megabytes. That happens once and is then cached by Hugging Face.

## Reproducibility

BERTopic's dimensionality-reduction step (UMAP) is stochastic, so the same input yields slightly different topics across runs. The skill fixes this by default (`--seed 42`): the same input gives the same result. That matters when you need to repeat an analysis and get exactly the same output. Pass `--no-seed` to turn the fix off and let the model search for groups afresh each time. On different input data the seed makes no difference — new data gives new topics either way.

## Speed and volume

Embeddings are computed on the CPU. A large corpus — tens of thousands of documents — takes hours rather than minutes. With a lot of data, run it in the background, or first run on a meaningful subsample (substantial documents, not every one-word reply) to see the picture quickly. Under roughly 50 documents, topics come out fragmented and the skill warns you the result is raw.

## Language support

The default embedding model is multilingual (`paraphrase-multilingual-MiniLM-L12-v2`) and handles Russian, Serbian and English. The clustering script also carries bundled stopword lists for those three languages, which keeps topic labels readable instead of filling them with function words. Add your language to the `STOPWORDS` list at the top of `cluster_topics.py`.

## Credits

By [Alena Zakharova](https://github.com/alenazaharovaux) (MIT).

Built on [BERTopic](https://github.com/MaartenGr/BERTopic) by Maarten Grootendorst (MIT), which in turn uses [sentence-transformers](https://www.sbert.net/), UMAP, HDBSCAN and scikit-learn. Embedding models are downloaded from the Hugging Face Hub and carry their own licenses.

---

# Topic Clustering (RU)

Кластеризует большие объёмы текста по смысловым темам через BERTopic, не заставляя лезть в терминал. Ты приносишь экспорт Telegram, историю переписки, набор транскриптов или гору постов; Claude сплющивает это в общий формат, доставляет недостающие пакеты, запускает кластеризацию и показывает темы в чате. Каждая тема — это реальный список документов, а не пересказ, поэтому ничего не выдумывается и охват не теряется.

## Установка

**macOS / Linux:**
```bash
cp -r topic-clustering ~/.claude/skills/topic-clustering
```

**Windows:**
```powershell
Copy-Item -Recurse topic-clustering $env:USERPROFILE\.claude\skills\topic-clustering
```

## Как пользоваться

Скажи Claude Code что-нибудь из этого:

- «о чём эти сообщения?»
- «сгруппируй выгрузку из телеграма по темам»
- «кластеризуй эти транскрипты по смыслу»
- «какие темы в этой куче постов?»
- «запусти BERTopic на этой таблице»

Скилл читает то, что ты принесла, сплющивает это в промежуточный `docs.json`, запускает кластеризацию и показывает темы с ключевыми словами и примерами документов.

## Что он делает

BERTopic превращает каждый текст в вектор смысла, собирает близкие по смыслу в кластеры и выводит для каждого кластера ключевые слова через class-based TF-IDF. На выходе — набор тем, где за каждой темой стоят конкретные документы, которые в неё попали. Этим он и отличается от вопроса чат-модели «какие тут темы»: он не упирается в контекстное окно, не выдумывает темы и не охватывает молча только часть корпуса.

| Шаг | Что происходит |
|-----|----------------|
| Вход | Любой формат — экспорт Telegram, переписка, транскрипты, таблица, вставленный текст |
| Сплющивание | Сводится к `docs.json`: массив `{text, label}`, разбор под конкретные данные |
| Кластеризация (слой A) | `scripts/cluster_topics.py` запускает BERTopic и тегирует каждый текст в тему → `topics.json` |
| Чтение (слой B) | `scripts/render_clusters.py` рисует читаемый HTML того, что накластеризовал алгоритм — ключевые слова, числа, примеры цитат |
| Синтез (слой C) | Только по твоему согласию: Claude группирует темы в понятные сюжеты и пишет выводы, всё ревьюится и правится |

Граница важна: BERTopic только тегирует тексты по темам и даёт ключевые слова и числа (слои A и B, машина). Назвать сюжеты и написать выводы — отдельный шаг, который делает Claude, читая сами тексты (слой C); скилл держит их порознь и никогда не выдаёт синтез за результат самого алгоритма.

## Зависимости

Claude ставит их сам при первом запуске, заранее готовить ничего не нужно:

- `bertopic` (подтягивает `sentence-transformers`, `scikit-learn`, `umap-learn`, `hdbscan`)

Первый запуск скачивает многоязычную модель эмбеддингов на несколько сотен мегабайт. Это происходит один раз, дальше она лежит в кэше Hugging Face.

## Скорость и объём

Эмбеддинги считаются на процессоре. Большой массив — десятки тысяч документов — это часы, а не минуты. Если данных много, запускай в фоне или сначала прогони на осмысленной подвыборке (содержательные документы, а не каждую однословную реплику), чтобы быстро увидеть картину. Меньше примерно 50 документов — темы получаются дробными, и скилл предупреждает, что результат сырой.

## Языки

Модель эмбеддингов по умолчанию многоязычная (`paraphrase-multilingual-MiniLM-L12-v2`), берёт русский, сербский и английский. В скрипте кластеризации вшиты списки стоп-слов для этих трёх языков — они держат названия тем читаемыми, а не набитыми служебными словами. Свой язык добавь в список `STOPWORDS` в начале `cluster_topics.py`.

## Благодарности

Автор: [Алена Захарова](https://github.com/alenazaharovaux) (MIT).

Построено на [BERTopic](https://github.com/MaartenGr/BERTopic) Маартена Грутендорста (MIT), который использует [sentence-transformers](https://www.sbert.net/), UMAP, HDBSCAN и scikit-learn. Модели эмбеддингов скачиваются с Hugging Face Hub и имеют собственные лицензии.
