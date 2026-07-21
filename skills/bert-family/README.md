# BERT Family

Run two BERT-family tools on your own text without touching a terminal. The skill either pulls out the entities mentioned in your material (banks, companies, brands, people, places) or groups the texts themselves into topics. You bring a transcript, a chat export, a spreadsheet or a pile of posts; Claude flattens it into a common format, installs what is missing, runs the right script, and reports the result in chat.

## Installation

**macOS / Linux:**
```bash
cp -r bert-family ~/.claude/skills/bert-family
```

**Windows:**
```powershell
Copy-Item -Recurse bert-family $env:USERPROFILE\.claude\skills\bert-family
```

## First run

The first time you use the skill it asks two questions and saves the answers to `config.md` inside the skill folder. Both questions can be skipped.

| Question | Why it asks | Example answer |
|----------|-------------|----------------|
| Which language should I use when reporting results? | Summaries in chat come back in that language | `English` |
| What language are your texts mostly in? | Sets the default NER model for that language | `Russian and Serbian` |

Skipping the first question means Claude replies in whatever language you write in. Skipping the second leaves the default model, `yqelz/xml-roberta-large-ner-russian`, which is built on multilingual XLM-RoBERTa and handles Russian, Serbian and English.

## Usage

Say any of these to Claude Code:

- "which banks are mentioned in these interviews?"
- "pull all the brands out of this transcript"
- "group my Telegram export by topic"
- "what are these 200 posts about?"
- "run BERTopic on this spreadsheet"

The fork between the two branches is mechanical, based on what you want as output: asking to list the things that appear in the text runs NER, while asking to sort the texts themselves into groups runs BERTopic. On a bare "run BERT" with no object, the skill asks one clarifying question rather than guessing.

## The two branches

| Branch | Script | What you get |
|--------|--------|--------------|
| NER | `scripts/extract_entities.py` | Entities by type with frequencies: ORG (organizations, companies, banks), PER (people), LOC (places), MISC (other) |
| BERTopic | `scripts/cluster_topics.py` | Topics with keywords, sizes and member documents, each tagged with its source label |

Both scripts save a full JSON result and print a readable summary. Input parsing is written fresh for each dataset rather than baked into the scripts, so odd export formats are handled case by case.

## Dependencies

Claude installs these on first use, so there is nothing to set up in advance:

- NER branch: `transformers`, `torch`
- BERTopic branch: `bertopic` (pulls in `sentence-transformers` and `scikit-learn`)

The first run of either branch downloads a model of several hundred megabytes. That happens once and is then cached by Hugging Face.

## Check the default model against your own data

The default NER model was chosen on a small sample and works well there. It is documented in the skill as a starting point that needs checking against each new dataset: whether entities come back whole rather than shredded into subwords, whether types are assigned correctly, whether the model picks up the right language. When quality drops, swap the model with `--model <hf-id>`. Candidates worth trying are `Babelscape/wikineural-multilingual-ner`, `surdan/LaBSE_ner_nerel` and `dslim/bert-base-NER`.

Topic clustering has its own limit: under roughly 50 documents, topics come out fragmented and unstable. The script lowers `min_topic_size` to compensate and the skill warns you when the corpus is that small.

## Adding your own language

`cluster_topics.py` carries bundled stopword lists for Russian, English and Serbian, which keeps topic labels readable instead of filling them with function words. If your topic keywords come back full of articles and prepositions, add your language to the `STOPWORDS` list at the top of the script.

## Credits

By [Alena Zakharova](https://github.com/alenazaharovaux) (MIT).

Built on [BERTopic](https://github.com/MaartenGr/BERTopic) by Maarten Grootendorst (MIT) and the [Transformers](https://github.com/huggingface/transformers) library by Hugging Face (Apache 2.0). Models are downloaded from the Hugging Face Hub and carry their own licenses.

---

# BERT Family (RU)

Запускает два инструмента семейства BERT на твоих текстах, не заставляя лезть в терминал. Скилл либо вытаскивает упомянутые в материале сущности (банки, компании, бренды, людей, места), либо раскладывает сами тексты по темам. Ты приносишь транскрипт, выгрузку переписки, таблицу или гору постов; Claude сплющивает это в общий формат, доставляет недостающие пакеты, запускает нужный скрипт и показывает результат в чате.

## Установка

**macOS / Linux:**
```bash
cp -r bert-family ~/.claude/skills/bert-family
```

**Windows:**
```powershell
Copy-Item -Recurse bert-family $env:USERPROFILE\.claude\skills\bert-family
```

## Первый запуск

При первом обращении скилл задаёт два вопроса и сохраняет ответы в `config.md` внутри своей папки. Оба вопроса можно пропустить.

| Вопрос | Зачем | Пример ответа |
|--------|-------|---------------|
| На каком языке докладывать результаты? | На этом языке будут сводки в чате | `Русский` |
| На каком языке твои тексты? | Подбирает дефолтную NER-модель под этот язык | `Русский и сербский` |

Если пропустить первый вопрос, Claude отвечает на том языке, на котором пишешь ты. Если пропустить второй, останется модель по умолчанию `yqelz/xml-roberta-large-ner-russian` — она построена на многоязычном XLM-RoBERTa и берёт русский, сербский и английский.

## Как пользоваться

Скажи Claude Code что-нибудь из этого:

- «какие банки упоминаются в этих интервью?»
- «вытащи все бренды из транскрипта»
- «сгруппируй выгрузку из телеграма по темам»
- «о чём эти 200 постов?»
- «запусти BERTopic на этой таблице»

Развилка между ветками механическая и зависит от того, что нужно на выходе: если надо перечислить упомянутые в тексте штуки, запускается NER, а если разложить сами тексты по группам, то BERTopic. На голое «запускай BERT» без объекта скилл задаёт один уточняющий вопрос вместо того, чтобы гадать.

## Две ветки

| Ветка | Скрипт | Что на выходе |
|-------|--------|---------------|
| NER | `scripts/extract_entities.py` | Сущности по типам с частотами: ORG (организации, компании, банки), PER (люди), LOC (места), MISC (прочее) |
| BERTopic | `scripts/cluster_topics.py` | Темы с ключевыми словами, размерами и составом документов, каждый с меткой источника |

Оба скрипта сохраняют полный результат в JSON и печатают читаемую сводку. Разбор входного формата пишется заново под каждый набор данных, а не зашивается в скрипты, так что странные выгрузки разбираются по месту.

## Зависимости

Claude ставит их сам при первом запуске, заранее готовить ничего не нужно:

- Ветка NER: `transformers`, `torch`
- Ветка BERTopic: `bertopic` (подтягивает `sentence-transformers` и `scikit-learn`)

Первый запуск любой ветки скачивает модель на несколько сотен мегабайт. Это происходит один раз, дальше она лежит в кэше Hugging Face.

## Проверяй дефолтную модель на своих данных

Дефолтная NER-модель выбрана на маленькой пробе и на ней работает хорошо. В скилле она описана как стартовая точка, которую надо проверять на каждом новом наборе: приходят ли сущности целиком, а не покрошенными на подслова, верно ли расставлены типы, берёт ли модель нужный язык. Когда качество проседает, модель меняется через `--model <hf-id>`. Стоит попробовать `Babelscape/wikineural-multilingual-ner`, `surdan/LaBSE_ner_nerel` и `dslim/bert-base-NER`.

У кластеризации своё ограничение: примерно до 50 документов темы получаются дробными и нестабильными. Скрипт понижает `min_topic_size`, чтобы это компенсировать, а скилл предупреждает, когда выборка такая маленькая.

## Как добавить свой язык

В `cluster_topics.py` вшиты списки стоп-слов для русского, английского и сербского — они держат названия тем читаемыми, а не набитыми служебными словами. Если ключевые слова тем приходят забитыми предлогами и союзами, добавь свой язык в список `STOPWORDS` в начале скрипта.

## Благодарности

Автор: [Алена Захарова](https://github.com/alenazaharovaux) (MIT).

Построено на [BERTopic](https://github.com/MaartenGr/BERTopic) Маартена Грутендорста (MIT) и библиотеке [Transformers](https://github.com/huggingface/transformers) от Hugging Face (Apache 2.0). Модели скачиваются с Hugging Face Hub и имеют собственные лицензии.
