---
name: bert-family
description: >
  Runs BERT-family tools on the user's own text: named entity recognition (NER) and topic
  clustering (BERTopic). Use this ALWAYS when the user brings any textual material (interview
  transcript, Telegram chat export, spreadsheet, data dump, articles) and asks either to LIST
  the specific entities mentioned in it (banks, companies, brands, people, places, amounts) or
  to GROUP the texts by topic. Triggers: "run BERT", "BERTopic", "which banks/companies are
  mentioned", "pull out the names / entities / brands", "who is mentioned", "group these by
  topic", "cluster this", "split into themes", "what are these texts about". Works with any
  language the underlying models cover. Claude handles the technical side (installing packages,
  running scripts) — the user stays in chat and never touches a terminal.
---

# BERT Family

One umbrella skill for two tasks from the BERT family. It is **deterministic**: the branch is
chosen mechanically by what the user wants as output, NOT by judging "which tool is better".
Do not offer alternatives (an LLM and so on) unless asked — the user picked BERT, so run BERT.

## Step 0 — Configuration (first run)

Read `config.md` from this skill's directory.

If the file does not exist, ask the user the two questions below, one at a time. Each question
can be skipped — if skipped, write `skip` as the value and use the default described.

1. **Interface language.** "Which language should I use when I talk to you about results?"
   Default when skipped: match the language the user writes in.
2. **Default NER model.** "What language are your texts mostly in? I will pick a default NER
   model for it." Map the answer to a Hugging Face model id (see the model notes below).
   Default when skipped: `yqelz/xml-roberta-large-ner-russian`, which is XLM-RoBERTa based and
   covers Russian, Serbian and English acceptably.

Write the answers to `config.md` next to this file:

```
language: English
ner_model: yqelz/xml-roberta-large-ner-russian
```

Everything below works with or without the config — a skipped setting only means the default
applies. Never ask these questions again once `config.md` exists.

## The fork: which tool to run

Look at the **object of the request — what the output should be**, not at the verb:

| The user wants to… | Branch | Script |
|---|---|---|
| list the concrete things mentioned: banks, companies, brands, people, places, amounts, products | **NER** | `scripts/extract_entities.py` |
| sort the texts themselves into topics, "what is this even about", group or cluster them | **BERTopic** | `scripts/cluster_topics.py` |

Worked examples:
- "which banks are mentioned in these interviews" → list entities → **NER**
- "pull all the brands out of this transcript" → **NER**
- "group my chat history by topic" → **BERTopic**
- "what are these 200 posts about" → **BERTopic**

If the phrasing is genuinely ambiguous (a bare "run BERT" with no object), ask ONE clarifying
question: "list the entities mentioned, or group the texts by topic?" — and wait for the answer.
Do not guess.

## Step 1 — Normalize any input into one format

The user may bring anything: a `.docx`/`.txt` transcript, a Telegram export (`.json`/`.html`),
a spreadsheet (`.csv`/`.xlsx`), ready-made JSON, or text pasted straight into chat. Your job is
to read it and flatten it into an intermediate `docs.json`: an array of objects, each with a
`text` field (required) and a `label` field (optional — a source marker such as a group or
respondent name, so it stays visible where a fragment came from).

```json
[
  {"text": "full text of the message or utterance", "label": "Group name / Respondent 03"},
  {"text": "next fragment", "label": "..."}
]
```

Flattening rules:
- One unit of meaning = one array element (one post, one utterance, one spreadsheet row).
- Parse the format against what was actually given — do not rely on a schema you assume in
  advance. Look at the file structure first, then write the parsing code.
- Empty and very short fragments (under 15 characters) can be dropped as noise.
- If the user asked to exclude something (a particular group, say), leave it out of `docs.json`.

Save `docs.json` to a working folder (a scratch directory or the project folder).

## Step 2 — Make sure the packages are installed

Check that the required package imports; install it if it does not. Claude installs, the user
does nothing.

- NER: `python -c "import transformers"` → on error, `python -m pip install transformers torch`
- BERTopic: `python -c "import bertopic"` → on error, `python -m pip install bertopic`

The first run of either branch also downloads a model (hundreds of MB). That is expected and
happens once.

## Step 3 — Run the right script

**NER (list the entities):**
```
python scripts/extract_entities.py --docs docs.json --out entities.json
```
The model comes from `ner_model` in `config.md`; pass it with `--model` when it differs from the
script default. Entity types: ORG (organizations, companies, banks), PER (people), LOC (places),
MISC (other). Look for banks and companies under ORG.

IMPORTANT — verify the model against THESE data, do not treat the choice as settled:
- On every new dataset, skim the output: is it shredding entities into subwords (`Ti`, `##nk`,
  `##off`), confusing types, picking up the right language?
- If quality is poor for the language mix at hand, swap the model: `--model <hf-id>`. Candidates
  worth trying: `Babelscape/wikineural-multilingual-ner` (multilingual, weaker on Cyrillic),
  `surdan/LaBSE_ner_nerel` (Russian, NEREL), `dslim/bert-base-NER` (English).
  For an unfamiliar language mix, run two or three models over a sample and compare — measure on
  the data rather than guessing.
- Data differ every time, so one good run on one sample guarantees nothing for the next dataset.
  Verifying against the data is part of the job, not a one-off action.

**BERTopic (group by topic):**
```
python scripts/cluster_topics.py --docs docs.json --out topics.json
```
The default embedding model is multilingual (`paraphrase-multilingual-MiniLM-L12-v2`). The script
picks `min_topic_size` from the corpus size on its own; override it with `--min-topic-size N`.

## Step 4 — Show the result in chat

The scripts print a human-readable summary AND save the full result to JSON. Put the summary in
chat (topics with their posts, or entities with frequencies) and leave the full JSON in the file
for reference. Do not retell raw JSON line by line. Use the language from `config.md`.

- NER → a list or table of "type → entity → count" (Organizations: Tinkoff ×12, Sber ×8).
- BERTopic → "topic (keywords) → sample posts with their source labels".

## Notes

- Small corpora for BERTopic (under roughly 50 texts) produce fragmented, unstable topics. The
  script lowers `min_topic_size` to compensate, but warn the user that results from a handful of
  documents are raw.
- Multilingual models are mandatory for mixed-language data. An English-only default breaks on
  Cyrillic and on Serbian diacritics.
- The scripts carry built-in stopword lists for Russian, English and Serbian so that topic labels
  stay readable. Add your own language to `STOPWORDS` in `cluster_topics.py` if topic keywords
  come back full of function words.
- The scripts are the stable core. Input parsing (Step 1) is written fresh for each dataset and
  is deliberately not baked into them.
