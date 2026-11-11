"""Comments from a comment page, turned into a readable list.

Usage:  python -I read_comments.py <comments-*.json> <list.md>
The list is written to a UTF-8 file: the Windows console can garble non-Latin text.
"""
import json
import sys
from pathlib import Path

if len(sys.argv) < 3:
    sys.exit(__doc__)
data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
out = [f"# Comments: {data.get('source', '')}", f"Saved: {data.get('saved', '')}, total {data.get('count', 0)}", ""]
for i, c in enumerate(data.get("comments", []), 1):
    out.append(f"## {i}. Block {c['block']} ({c.get('kind', '')})")
    out.append(f"Block text: {c['block_text']}")
    if c.get("quote"):
        out.append(f"Selected phrase: \"{c['quote']}\"")
    out.append(f"Comment: {c['comment']}")
    out.append("")
Path(sys.argv[2]).write_text("\n".join(out), encoding="utf-8")
print(len(data.get("comments", [])))
