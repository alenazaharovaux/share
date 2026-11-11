"""Mechanical search for spots where a reader may have a question.

Usage:  python -I check_text.py <file.md> [<report.md>]
The report goes to a file (default: next to the input, <file>.check.md); the console shows only the number of findings.
The script looks for signs. A person or an agent checks every finding by eye against references/questions.md.
"""
import re
import sys
from pathlib import Path

CHECKS = [
    ("\"not X but Y\" contrast", r"\bnot\s[^.!?]{1,40},?\s+but\s|,\s+not\s+\w+[^.!?]{0,30}[.!?]?$|\bisn't just\b|\bnot just\b"),
    ("filler phrase", r"\b(that is to say|the thing is|in fact|actually|it is worth noting|it's worth noting|it is important to note|importantly|the practical takeaway|it follows that|for a simple reason|here is an example|let's dive|needless to say)\b"),
    ("line number without a quote nearby", None),
    ("sentence starts with a pointing word (question 1: who is this about?)",
     r"^(This|That|These|Those|Such|It|Its|He|She|They|Their|His|Her|The other|The second|The latter|The former)\b"),
    ("short sentence: does it make sense without its neighbours? (question 3)", None),
    ("long sentence, more than 35 words", None),
    ("abbreviation: explained when first used? (question 2)", None),
]
ABBR_OK = {"AI", "HTML", "PDF", "URL", "API", "JSON", "ID", "OK", "UI", "CSS", "USA", "UK", "EU"}


def strip_md(md: str):
    """Drops front matter, code blocks and tables; returns (line number, text) pairs."""
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
    t = re.sub(r"^\s*([-•]|\d+(\.\d+)*\.)\s+", "", t)      # list marker and numbering like "3.1."
    t = re.sub(r"^\s*\*\*[^*]{1,80}\*\*\s*", "", t)          # bold lead-in at the start of a paragraph
    t = re.sub(r"[\"“][^\"“”]*[\"”]", "\"…\"", t)            # quoted speech is not checked
    t = re.sub(r"[*`#>]", "", t)
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+(?=[\"“A-Z])", t) if s.strip() and s.strip() != "\"…\""]


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
                if rx and re.search(rx, s, flags=re.IGNORECASE if name == "filler phrase" else 0):
                    found.append((n, name, s))
            if re.search(r"\blines?\s+\d+", s, re.IGNORECASE) and "\"" not in s and "“" not in s:
                found.append((n, CHECKS[2][0], s))
            if not is_heading and not is_list and words <= 5 and not s.endswith(":"):
                found.append((n, CHECKS[4][0], s))
            if words > 35:
                found.append((n, CHECKS[5][0], s))
            for ab in re.findall(r"\b[A-Z]{2,6}\b", s):
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
    out = [f"# Clarity check: {src.name}", f"Findings: {len(found)}. Check each one by eye against references/questions.md.", ""]
    for name, items in by.items():
        out.append(f"## {name} — {len(items)}")
        out += [f"- line {n}: {s}" for n, s in items]
        out.append("")
    rep.write_text("\n".join(out), encoding="utf-8")
    print(len(found), rep)


if __name__ == "__main__":
    main()
