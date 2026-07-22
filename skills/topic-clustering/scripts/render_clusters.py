"""
render_clusters.py — «слой B» скилла topic-clustering.

Берёт topics.json (сырой результат BERTopic) и рисует читаемый HTML, где по-человечески
видно, ЧТО накластеризовал алгоритм: каждая тема — ключевые слова, число реплик и несколько
реальных цитат с метками источника. Это отображение ДО синтеза: никакой интерпретации,
названий и выводов здесь нет — только то, что реально дала машина.

Запуск:
    python scripts/render_clusters.py --topics topics.json --out clusters.html [--title "..."]

Выход — самодостаточный HTML (без внешних зависимостей), который можно открыть в браузере.
"""

import argparse
import html
import json
import re
from pathlib import Path


def clean(s: str) -> str:
    return re.sub(r"\s+", " ", s or "").strip()


def sample_quotes(messages, k=4, maxlen=240):
    """Несколько разнообразных цитат: раскидываем по списку, режем по длине."""
    subst = [m for m in messages if len(clean(m.get("text", ""))) >= 120] or messages
    if not subst:
        return []
    step = max(1, len(subst) // k)
    picked = subst[::step][:k]
    out = []
    for m in picked:
        t = clean(m.get("text", ""))
        if len(t) > maxlen:
            t = t[:maxlen].rsplit(" ", 1)[0] + "…"
        out.append({"text": t, "label": clean(m.get("label", ""))})
    return out


CSS = """
:root{--bg:#F6F5F2;--card:#fff;--ink:#232a30;--mut:#727d86;--faint:#9aa4ac;
--accent:#3B6FB0;--soft:#ECF1F8;--line:#e6e3db;
--mono:ui-monospace,"Cascadia Code",Consolas,monospace;
--sans:system-ui,"Segoe UI",Roboto,Arial,sans-serif;}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--sans);line-height:1.55;font-size:16px}
.wrap{max-width:880px;margin:0 auto;padding:40px 22px 80px}
.head{border-bottom:2px solid var(--line);padding-bottom:20px;margin-bottom:8px}
.eyebrow{font-family:var(--mono);font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:var(--accent)}
h1{font-size:26px;margin:12px 0 6px;font-weight:700}
.sub{color:var(--mut);font-size:14.5px}
.note{background:var(--soft);border-radius:10px;padding:12px 16px;margin:18px 0 26px;color:#3a4650;font-size:14px}
.topic{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:18px 20px;margin-bottom:14px}
.trow{display:flex;align-items:baseline;gap:12px;flex-wrap:wrap;margin-bottom:6px}
.tid{font-family:var(--mono);font-size:12px;color:var(--faint)}
.kw{font-size:18px;font-weight:700;letter-spacing:-.01em}
.cnt{margin-left:auto;font-family:var(--mono);font-size:13px;color:var(--mut);white-space:nowrap}
.cnt b{color:var(--ink)}
.bar{height:6px;border-radius:3px;background:var(--soft);overflow:hidden;margin:8px 0 14px}
.bar>i{display:block;height:100%;background:var(--accent);border-radius:3px}
.q{border-left:3px solid var(--line);padding:2px 0 2px 14px;margin:10px 0;color:#3c464e;font-size:14.5px}
.q .who{font-family:var(--mono);font-size:12px;color:var(--accent)}
.q .who::before{content:"@ ";color:var(--faint)}
.foot{margin-top:30px;color:var(--faint);font-family:var(--mono);font-size:12px}
@media (prefers-color-scheme:dark){
:root{--bg:#15191d;--card:#1c2228;--ink:#e6ebef;--mut:#9aa5ad;--faint:#6b757d;--soft:#1e2836;--line:#2a333c}
}
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--topics", required=True)
    ap.add_argument("--out", default="clusters.html")
    ap.add_argument("--title", default="Что накластеризовал BERT")
    ap.add_argument("--quotes", type=int, default=4, help="сколько цитат на тему")
    args = ap.parse_args()

    topics = json.loads(Path(args.topics).read_text(encoding="utf-8"))
    topics = sorted(topics, key=lambda t: -t.get("size", 0))
    total = sum(t.get("size", 0) for t in topics) or 1
    maxsize = max((t.get("size", 0) for t in topics), default=1) or 1

    def esc(s):
        return html.escape(str(s))

    cards = []
    for t in topics:
        size = t.get("size", 0)
        share = round(100 * size / total)
        w = max(4, round(100 * size / maxsize))
        kw = ", ".join(t.get("keywords", []))
        quotes = "".join(
            f'<div class="q">{esc(q["text"])}'
            + (f'<div class="who">{esc(q["label"])}</div>' if q["label"] else "")
            + "</div>"
            for q in sample_quotes(t.get("messages", []), k=args.quotes)
        )
        cards.append(
            '<div class="topic">'
            f'<div class="trow"><span class="tid">тема {t.get("topic_id")}</span>'
            f'<span class="kw">{esc(kw)}</span>'
            f'<span class="cnt"><b>{size}</b> реплик · {share}%</span></div>'
            f'<div class="bar"><i style="width:{w}%"></i></div>'
            f"{quotes}</div>"
        )

    page = (
        "<!DOCTYPE html><html lang=\"ru\"><head><meta charset=\"utf-8\">"
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        f"<title>{esc(args.title)}</title><style>{CSS}</style></head><body><div class=\"wrap\">"
        '<div class="head"><div class="eyebrow">BERTopic · сырой результат</div>'
        f"<h1>{esc(args.title)}</h1>"
        f'<div class="sub">{len(topics)} тем · {total} реплик в работе</div></div>'
        '<div class="note">Это то, что нашёл алгоритм: реплики сгруппированы по смысловой '
        "близости, для каждой группы — частотные слова, число реплик и несколько реальных "
        "цитат. Названий тем и выводов здесь нет — это машинное тегирование до интерпретации.</div>"
        + "".join(cards)
        + '<div class="foot">topic-clustering · слой B (до синтеза)</div>'
        "</div></body></html>"
    )
    Path(args.out).write_text(page, encoding="utf-8")
    print(f"Слой B готов: {args.out} ({len(topics)} тем)")


if __name__ == "__main__":
    main()
