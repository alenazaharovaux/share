"""Механический поиск мест, где у читателя может возникнуть вопрос.

Запуск:  python -I check_text.py <файл.md> [<отчёт.md>]
Отчёт пишется в файл (по умолчанию рядом: <файл>.check.md), в консоль — только число находок.
Программа ищет приметы. Каждую находку человек или агент проверяет глазами по references/voprosy.md.
Регулярные выражения с кириллицей работают в Python; в grep классы [А-Я] не работают.
"""
import re
import sys
from pathlib import Path

CHECKS = [
    ("противопоставление «не X, а Y»", r",\s+а\s+не\s|\bне\s[^.!?]{1,40},\s+а\s"),
    ("слово-подпорка", r"\b(то есть|дело в том|на самом деле|стоит отметить|важно отметить|практический вывод|отсюда следует|по простой причине|вот пример)\b"),
    ("номер строки без цитаты рядом", None),
    ("предложение начинается с указательного слова (вопрос 1: о ком это?)",
     r"^(Это|Этот|Эта|Эти|Так|Такой|Такая|Такие|Такое|Тот|Та|Те|Другой|Другая|Второй|Вторая|Его|Её|Ее|Их|Он|Она|Оно|Они)\b"),
    ("короткое предложение — понятно ли без соседних? (вопрос 3)", None),
    ("длинное предложение, больше 40 слов", None),
    ("сокращение — расшифровано при первом упоминании? (вопрос 2)", None),
]
ABBR_OK = {"ИИ", "HTML", "PDF", "URL", "API", "JSON", "ID"}


def strip_md(md: str):
    """Убирает шапку, блоки кода и таблицы; возвращает пары (номер строки, текст)."""
    lines = md.splitlines()
    start = 0
    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                start = i + 1
                break
    out, in_code = [], False
    for n, l in enumerate(lines[start:], start + 1):
        if l.strip().startswith("```"):
            in_code = not in_code
            continue
        if in_code or l.strip().startswith("|") or not l.strip():
            continue
        out.append((n, l))
    return out


def sentences(text: str):
    t = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    t = re.sub(r"^\s*([-•]|\d+(\.\d+)*\.)\s+", "", t)      # маркер списка и нумерация «3.1.»
    t = re.sub(r"^\s*\*\*[^*]{1,80}\*\*\s*", "", t)          # жирный подзаголовок в начале абзаца
    t = re.sub(r"«[^«»]*»", "«…»", t)                         # чужая речь в кавычках не проверяется
    t = re.sub(r"[*`#>]", "", t)
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+(?=[«\"A-ZА-ЯЁ])", t) if s.strip() and s.strip() != "«…»"]


def run(path: Path):
    md = path.read_text(encoding="utf-8")
    found = []
    seen_abbr = set()
    for n, line in strip_md(md):
        is_heading = line.lstrip().startswith("#")
        is_list = bool(re.match(r"^\s*([-*]|\d+\.)\s", line))
        for s in sentences(line):
            words = len(s.split())
            for name, rx in CHECKS:
                if rx and re.search(rx, s, flags=re.IGNORECASE if "подпорка" in name else 0):
                    found.append((n, name, s))
            if re.search(r"строк[аеиу]\s+\d+", s, re.IGNORECASE) and "«" not in s:
                found.append((n, CHECKS[2][0], s))
            if not is_heading and not is_list and words <= 5 and not s.endswith(":"):
                found.append((n, CHECKS[4][0], s))
            if words > 40:
                found.append((n, CHECKS[5][0], s))
            for ab in re.findall(r"\b[A-ZА-ЯЁ]{2,6}\b", s):
                if ab in ABBR_OK or ab in seen_abbr:
                    continue
                seen_abbr.add(ab)
                if not re.search(re.escape(ab) + r"\s*[(—–-]|\(\s*" + re.escape(ab), s):
                    found.append((n, CHECKS[6][0], f"{ab}: {s}"))
    return found


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    src = Path(sys.argv[1])
    rep = Path(sys.argv[2]) if len(sys.argv) > 2 else src.with_suffix(".check.md")
    found = run(src)
    by = {}
    for n, name, s in found:
        by.setdefault(name, []).append((n, s))
    out = [f"# Проверка понятности: {src.name}", f"Находок: {len(found)}. Каждую проверь глазами по references/voprosy.md.", ""]
    for name, items in by.items():
        out.append(f"## {name} — {len(items)}")
        out += [f"- строка {n}: {s}" for n, s in items]
        out.append("")
    rep.write_text("\n".join(out), encoding="utf-8")
    print(len(found), rep)


if __name__ == "__main__":
    main()
