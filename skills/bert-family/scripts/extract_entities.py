"""
NER branch of the bert-family skill: extracting named entities.

Input  : docs.json — an array of [{"text": "...", "label": "..."}]
Output : entities.json (entities by type, with counts) + a summary on stdout.

The default model is yqelz/xml-roberta-large-ner-russian. It was picked empirically on a sample
of Russian bank names, where it was the only candidate that returned them whole instead of
shredding them into subwords, and it also handles Serbian and English because the XLM-RoBERTa
backbone is multilingual. Override it with --model for other language mixes.
Types: ORG (organizations, companies, banks), PER (people), LOC (places), MISC (other).
"""

import argparse
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

# Windows: stdout defaults to cp1252 and dies on non-Latin text — force utf-8.
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

CHUNK = 1500  # characters per chunk (rough bound for the model's input limit)

TYPE_LABELS = {
    "ORG": "Organizations / companies / banks",
    "PER": "People",
    "PERSON": "People",
    "LOC": "Places",
    "MISC": "Other",
}

DEFAULT_MODEL = "yqelz/xml-roberta-large-ner-russian"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--docs", required=True, help="JSON: array of {text, label?}")
    ap.add_argument("--out", default="entities.json")
    ap.add_argument("--model", default=DEFAULT_MODEL,
                    help="any other Hugging Face NER model id")
    args = ap.parse_args()

    docs_raw = json.loads(Path(args.docs).read_text(encoding="utf-8"))
    texts = [(d.get("text") or "").strip() for d in docs_raw]
    texts = [t for t in texts if t]
    print(f"Documents: {len(texts)}  |  model: {args.model}")

    from transformers import pipeline
    ner = pipeline("ner", model=args.model, aggregation_strategy="simple")

    by_type = defaultdict(Counter)
    for t in texts:
        for i in range(0, len(t), CHUNK):
            for ent in ner(t[i:i + CHUNK]):
                word = ent["word"].strip()
                if len(word) < 2:
                    continue
                by_type[ent["entity_group"]][word] += 1

    result = {grp: cnt.most_common() for grp, cnt in by_type.items()}
    Path(args.out).write_text(
        json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    print(f"\nExtracted -> {args.out}\n")
    for grp, items in result.items():
        print(f"=== {TYPE_LABELS.get(grp, grp)} ===")
        for word, c in items[:30]:
            print(f"  {word}  x{c}")
        print()


if __name__ == "__main__":
    main()
