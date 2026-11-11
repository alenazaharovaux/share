"""Комментарии со страницы make_comment_page.py — в читаемый список.

Запуск:  python -I read_comments.py <kommentarii-*.json> <список.md>
Список пишется в файл в UTF-8: консоль Windows портит кириллицу.
"""
import json
import sys
from pathlib import Path

if len(sys.argv) < 3:
    sys.exit(__doc__)
data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
out = [f"# Комментарии: {data.get('source', '')}", f"Сохранено: {data.get('saved', '')}, всего {data.get('count', 0)}", ""]
for i, c in enumerate(data.get("comments", []), 1):
    out.append(f"## {i}. Блок {c['block']} ({c.get('kind', '')})")
    out.append(f"Текст блока: {c['block_text']}")
    if c.get("quote"):
        out.append(f"Выделенная фраза: «{c['quote']}»")
    out.append(f"Комментарий: {c['comment']}")
    out.append("")
Path(sys.argv[2]).write_text("\n".join(out), encoding="utf-8")
print(len(data.get("comments", [])))
