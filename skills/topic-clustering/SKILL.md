---
name: topic-clustering
description: >
  Cluster and organize large volumes of text into semantic topics with BERTopic. Use this
  ALWAYS when the user brings a lot of text (a Telegram export, a chat history, a dump of
  posts, a set of transcripts, a table of messages, hundreds of rows) and wants to know what
  it is about, sort it into topics, group it by meaning, or see the main threads. Triggers:
  "group these by topic", "what are these messages about", "cluster this", "split into
  themes", "what topics are here", "BERTopic", "separate by meaning", "main threads". Works
  with any language the embedding model covers. Claude handles the technical side (installing
  packages, running the script) — the user stays in chat and never touches a terminal.
---

# Topic Clustering with BERTopic

This skill groups large volumes of text into semantic topics with **BERTopic**. It takes a
pile of texts, turns each into a meaning vector, gathers the semantically close ones into
clusters, and returns keywords and example documents for each cluster. This is the thing
that is hard to do by reading: sort tens of thousands of messages into topics without losing
coverage and without making things up, because each topic is a real list of documents rather
than a summary.

## When this skill, and when not

- A lot of texts, the question is "what are these about" and "what topics are here" → **this skill**.
- You need to pull specific entities (companies, names, places) out of the text → that is a
  separate NER task, and it is not part of this skill.
- A handful of documents you could just read → BERTopic is not needed, read them yourself.

## Step 1 — Normalize any input into one format

The user may bring anything: a Telegram export (`.json`/`.html`), a chat history, a table
(`.csv`/`.xlsx`), ready-made JSON, a set of transcripts, or text pasted into chat. Your job
is to read it and flatten it into an intermediate `docs.json`: an array of objects, each with
a `text` field (required) and a `label` field (optional — a source marker such as a group,
author or respondent name, so it stays visible where a fragment came from).

```json
[
  {"text": "full text of the message or utterance", "label": "Group name / Respondent 03"},
  {"text": "next fragment", "label": "..."}
]
```

Flattening rules:
- One unit of meaning = one array element (one post, one utterance, one table row).
- Parse the format against what was actually given — do not rely on a schema you assume in
  advance. Look at the file structure first, then write the parsing code. For large exports,
  write the parsing as a separate script rather than pulling all the text into context.
- Very short fragments (under 15 characters) can be dropped as noise. For chats with short
  replies, raise the threshold: fragments like "ok", "+", "thanks" produce junk topics. If
  the goal is meaningful threads rather than chat noise, keep only substantial messages
  (say, 200+ characters).
- If the user asked to exclude something (a particular group, say), leave it out of `docs.json`.

Save `docs.json` to a working folder (a scratch directory or the project folder).

## Step 2 — Make sure the package is installed

Check the import; install it if it is missing. Claude installs, the user does nothing.

`python -c "import bertopic"` → on error, `python -m pip install bertopic`

The first run also downloads an embedding model (hundreds of MB). That is expected and
happens once.

## Step 3 — Run the script

```
python scripts/cluster_topics.py --docs docs.json --out topics.json
```

The default embedding model is multilingual (`paraphrase-multilingual-MiniLM-L12-v2`). The
script picks `min_topic_size` from the corpus size on its own; override it with
`--min-topic-size N`.

**Reproducibility.** The dimensionality-reduction step (UMAP) inside BERTopic is stochastic
by nature: the same input produces slightly different topics on different runs (~15% drift).
The script fixes this by default via `--seed 42` — the same input gives the same result,
which matters when you need to repeat a run and get exactly the same output (e.g. show a
client, then re-run; compare "before/after" on the same data). If you do not want the fix and
prefer the model to search for groups afresh each time, add `--no-seed`. On DIFFERENT input
data the seed changes nothing — new data gives new topics regardless.

On volume and speed, honestly: embeddings are computed on the CPU, and a large corpus (tens
of thousands of documents) takes real time — hours rather than minutes. With a lot of data,
either warn the user and run it in the background, or first run on a meaningful subsample
(substantial documents, not everything) to see the picture quickly.

## Step 4 — Show the result in chat

The script prints a human-readable summary AND saves the full result to `topics.json`. Put
the summary in chat — topics with keywords and example documents (with their source labels) —
and leave the full JSON in the file for reference. Do not retell raw JSON line by line.

Summary format: "topic (keywords) → how many documents → 2-3 examples with labels".

## Notes

- Small corpora (under roughly 50 texts): topics come out fragmented and unstable. The script
  lowers `min_topic_size` to compensate, but warn the user that results from a handful of
  documents are raw.
- A multilingual embedding model is mandatory for mixed-language data. An English-only model
  breaks on Cyrillic and on Serbian diacritics.
- The script carries built-in stopword lists for Russian, English and Serbian so that topic
  labels stay readable instead of "the/of/and/to". Add your own language to `STOPWORDS` in
  `cluster_topics.py`.
- Orphan documents (topic -1) are reassigned to their nearest topic via `reduce_outliers`.
- The script is the stable core. Input parsing (Step 1) is written fresh for each dataset and
  is deliberately not baked into it.
