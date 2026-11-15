"""Собирает claims.json из файлов фактов для программы verify-sources.

Запуск:
    python raw_to_claims.py <папка desk или справки>

Читает <папка>/_raw/*.md (или <папка>/fakty.md в справке) и реестры <папка>/sources/0N-istochniki.md.
Формат строк — references/raw-format.md. Строки, которые не разобрал, печатает списком: их надо поправить руками.
"""
import collections
import glob
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

DOI = re.compile(r"\b10\.\d{4,9}/[^\s|\]>,;«»\"`]+")
URL = re.compile(r"https?://[^\s|)\]>,;«»\"`]+")
QUOTE = re.compile(r"^-\s*«([^«»]{15,})»\s*—\s*(.+)$")
DATA = re.compile(r"^-\s*данные:\s*(.+?)\s*—\s*(.+)$")
REF = re.compile(r"^\[(\d+)-(\d+)\]")


def clean_doi(d):
    d = re.sub(r"\.pdf$", "", d.rstrip(".,:`"), flags=re.I)
    while d.endswith(")") and d.count(")") > d.count("("):
        d = d[:-1].rstrip(".,:`")
    return d


def find_source(text):
    d = DOI.search(text)
    if d:
        return "doi", clean_doi(d.group(0))
    u = [x.rstrip(".") for x in URL.findall(text) if "doi.org/" not in x]
    if u:
        return "source", u[0]
    return None


def fields(tail):
    """'[1-12] · место: X · текст: полный · против' -> (ref, {поле: значение}, {метки})"""
    parts = [p.strip() for p in tail.split("·")]
    head, out, marks = parts[0], {}, set()
    for p in parts[1:]:
        if ":" in p:
            k, v = p.split(":", 1)
            out[k.strip().lower()] = v.strip()
        elif p:
            marks.add(p.lower())
    return head, out, marks


def load_registries(folder):
    reg = {}
    for path in glob.glob(os.path.join(folder, "sources", "*-istochniki.md")):
        block = re.match(r"(\d+)", os.path.basename(path))
        if not block:
            continue
        b = str(int(block.group(1)))
        for line in open(path, encoding="utf-8"):
            m = re.match(r"^\|\s*(\d+)\s*\|", line)
            if m:
                s = find_source(line)
                if s:
                    reg[(b, m.group(1))] = s
    return reg


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    folder = os.path.abspath(sys.argv[1])
    files = sorted(glob.glob(os.path.join(folder, "_raw", "*.md")))
    if not files and os.path.exists(os.path.join(folder, "fakty.md")):
        files = [os.path.join(folder, "fakty.md")]
    if not files:
        print("Нет файлов фактов: ни _raw/*.md, ни fakty.md в", folder)
        sys.exit(1)
    reg = load_registries(folder)

    claims, bad, stats = [], [], collections.Counter()
    for path in files:
        name = os.path.basename(path)
        section, skip = "", False
        for ln, line in enumerate(open(path, encoding="utf-8").read().split("\n"), 1):
            if line.startswith("## "):
                section = line[3:].strip()
                skip = section.lower().startswith(("чего не нашли", "что не искали", "поисковый след"))
                continue
            s = line.strip()
            if skip or not s.startswith("-"):
                continue
            mq, md = QUOTE.match(s), DATA.match(s)
            if not mq and not md:
                if "«" in s:
                    bad.append(f"{name}:{ln} — строка с цитатой не по формату")
                continue
            body, tail = (mq or md).group(1), (mq or md).group(2)
            head, f, marks = fields(tail)
            src = None
            r = REF.match(head)
            if r:
                src = reg.get((str(int(r.group(1))), r.group(2)))
                if not src:
                    bad.append(f"{name}:{ln} — номер [{r.group(1)}-{r.group(2)}] не найден в реестре или у строки реестра нет DOI и ссылки")
            else:
                src = find_source(head)
            loc = "; ".join(x for x in (f"{name}:{ln}", section, f.get("место", ""), f.get("текст", "")) if x)
            c = {"id": f"{name.split('-')[0].split('.')[0]}-{ln}", "location": loc}
            if mq:
                c["claim"] = c["quote"] = body
                stats["цитата"] += 1
            else:
                c["claim"] = body
                c["quote"] = ""
                c["data"] = body
                stats["данные из файла"] += 1
            if src:
                c[src[0]] = src[1]
            else:
                c["source"] = ""
                stats["без источника"] += 1
            for k in ("дата", "период"):
                if k in f:
                    c[k] = f[k]
            if "против" in marks:
                c["against"] = True
            if "не подтверждено" in marks:
                c["unconfirmed"] = True
            claims.append(c)

    out = os.path.join(folder, "claims.json")
    json.dump(claims, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("Записано:", out)
    print("Утверждений:", len(claims), dict(stats))
    print("Источников:", len({c.get("doi") or c.get("source") for c in claims if c.get("doi") or c.get("source")}))
    if bad:
        print(f"\nНе разобрано или без источника — {len(bad)}:")
        for b in bad:
            print(" ", b)


if __name__ == "__main__":
    main()
