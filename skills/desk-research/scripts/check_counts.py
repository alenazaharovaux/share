"""Признаки имитации: сверяет числа, которые должны совпасть.

Запуск:
    python check_counts.py <папка desk или справки> <файл выводов> [<файл выводов> ...]

Пары:
1. Источники, на которые ссылаются выводы, и источники в claims.json.
2. Источники в claims.json и источники, которые программа открыла, плюс помеченные «недоступен».
Третью пару (запросы в поисковом следе и вызовы поиска агента) сверяет человек по итогу агента.
"""
import glob
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
DOI = re.compile(r"\b10\.\d{4,9}/[^\s|\]>,;«»\"`)]+")
URL = re.compile(r"https?://[^\s|)\]>,;«»\"`]+")
NOT_READ = {"источник не прочитан", "DOI не существует", "нет источника", "число из файла"}


def keys(text):
    out = {d.rstrip(".,:").lower() for d in DOI.findall(text)}
    out |= {u.rstrip(".").lower() for u in URL.findall(text) if "doi.org/" not in u}
    return out


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    folder = os.path.abspath(sys.argv[1])
    claims = json.load(open(os.path.join(folder, "claims.json"), encoding="utf-8"))
    in_claims = {(c.get("doi") or c.get("source") or "").lower() for c in claims} - {""}

    cited = set()
    for f in sys.argv[2:]:
        cited |= keys(open(f, encoding="utf-8").read())
    print("1. Источники в выводах:", len(cited), "| в claims.json:", len(in_claims))
    extra = sorted(cited - in_claims)
    if extra:
        print("   В выводах, но нет в claims.json (нет проверенной цитаты):")
        for x in extra:
            print("   -", x)

    registry = set()
    for path in glob.glob(os.path.join(folder, "sources", "*-istochniki.md")):
        for line in open(path, encoding="utf-8"):
            if re.match(r"^\|\s*\d+\s*\|", line):
                registry |= keys(line)
    if registry:
        print("   Для справки: источников в реестрах", len(registry), "| из них с фактами", len(registry & in_claims))
    vpath = os.path.join(folder, "verification.json")
    if os.path.exists(vpath):
        v = json.load(open(vpath, encoding="utf-8"))
        opened = {(x.get("source") or "").lower() for x in v if x.get("status") not in NOT_READ} - {""}
        unavailable = {(c.get("doi") or c.get("source") or "").lower() for c in claims if c.get("unconfirmed")}
        rpath = os.path.join(folder, "review.md")
        if os.path.exists(rpath):
            # источники, которые открыла сверка: id из раздела «Совпали» и «Не совпали»
            review = open(rpath, encoding="utf-8").read().split("## Источник открыть не удалось")[0]
            by_id = {str(c.get("id")): (c.get("doi") or c.get("source") or "").lower() for c in claims}
            opened |= {src for cid, src in by_id.items() if src and re.search(r"(?<![\w-])" + re.escape(cid) + r"(?![\w-])", review)}
        print("2. Источники в claims.json:", len(in_claims), "| открыты программой, сверкой или помечены «недоступен»:", len(in_claims & (opened | unavailable)))
        missing = sorted(in_claims - opened - unavailable)
        if missing:
            print("   Не открыт программой и не помечен «недоступен» — открыть руками:")
            for x in missing:
                print("   -", x)
    else:
        print("2. Пропущено: нет verification.json, сначала запусти программу verify-sources.")
    print("3. Сверь руками: число запросов в поисковом следе и число вызовов поиска в итоге агента.")


if __name__ == "__main__":
    main()
