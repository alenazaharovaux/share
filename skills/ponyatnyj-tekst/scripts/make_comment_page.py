"""Собирает из md-файла HTML-страницу для комментариев голосом.

Запуск:  python -I make_comment_page.py <файл.md> [папка-вывода]
По умолчанию кладёт kommentarii-<имя>.html в папку «Загрузки» (~/Downloads).
Комментарии хранятся в браузере (localStorage), кнопка «Сохранить комментарии»
скачивает kommentarii-<имя>.json: блок, текст блока, выделенная фраза, комментарий.
"""
import hashlib
import html
import json
from datetime import datetime
import re
import sys
from pathlib import Path

DEFAULT_OUT = Path.home() / "Downloads"


def inline(text: str) -> str:
    t = html.escape(text, quote=False)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)",
               lambda m: f'<a href="{html.escape(m.group(2))}" target="_blank" rel="noopener">{m.group(1)}</a>', t)
    return t


def plain(text: str) -> str:
    t = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    return t.replace("**", "").replace("`", "")


def parse(md: str):
    """Возвращает список блоков: (kind, raw_text). kind: h1/h2/h3/p/li/oli."""
    lines = md.splitlines()
    if lines and lines[0].strip() == "---":
        end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
        if end is not None:
            lines = lines[end + 1:]
    blocks, para = [], []

    def flush():
        if para:
            blocks.append(("p", " ".join(s.strip() for s in para)))
            para.clear()

    code, table = None, None
    for line in lines:
        s = line.rstrip()
        if code is not None:
            if s.strip().startswith("```"):
                blocks.append(("pre", "\n".join(code))); code = None
            else:
                code.append(s)
            continue
        if s.strip().startswith("```"):
            flush(); code = []; continue
        if s.strip().startswith("|"):
            flush()
            if table is None:
                table = []
            if not re.match(r"^\s*\|[\s|:-]+\|\s*$", s):
                table.append([c.strip() for c in s.strip().strip("|").split("|")])
            continue
        if table is not None:
            blocks.append(("table", json.dumps(table, ensure_ascii=False))); table = None
        if not s.strip():
            flush(); continue
        m = re.match(r"^(#{1,3})\s+(.*)", s)
        if m:
            flush(); blocks.append((f"h{len(m.group(1))}", m.group(2))); continue
        m = re.match(r"^\s*[-*]\s+(.*)", s)
        if m:
            flush(); blocks.append(("li", m.group(1))); continue
        m = re.match(r"^\s*(\d+)\.\s+(.*)", s)
        if m:
            flush(); blocks.append(("oli", f"{m.group(1)}. {m.group(2)}")); continue
        para.append(s)
    flush()
    if table is not None:
        blocks.append(("table", json.dumps(table, ensure_ascii=False)))
    if code is not None:
        blocks.append(("pre", "\n".join(code)))
    return blocks


PAGE = """<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Комментарии: __TITLE__</title>
<style>
:root{--bg:#faf9f6;--fg:#1d1d1b;--muted:#77756f;--line:#e4e1d8;--accent:#c2410c;--note:#fff4e6;--card:#fff}
@media (prefers-color-scheme:dark){:root{--bg:#171715;--fg:#ecebe6;--muted:#9a978e;--line:#33322e;--accent:#fb923c;--note:#2a2118;--card:#1f1f1c}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);font:18px/1.6 Georgia,"Times New Roman",serif}
header{position:sticky;top:0;z-index:5;background:var(--bg);border-bottom:1px solid var(--line);padding:10px 16px;display:flex;gap:10px;align-items:center;flex-wrap:wrap;font:14px/1.3 system-ui,sans-serif}
header .count{color:var(--muted);margin-right:auto}
button{font:14px system-ui,sans-serif;border:1px solid var(--line);background:var(--card);color:var(--fg);border-radius:8px;padding:7px 12px;cursor:pointer}
button.main{background:var(--accent);border-color:var(--accent);color:#fff}
main{max-width:760px;margin:0 auto;padding:16px 16px 120px}
.hint{font:14px/1.5 system-ui,sans-serif;color:var(--muted);border:1px dashed var(--line);border-radius:10px;padding:10px 14px;margin:8px 0 24px}
.blk{position:relative;padding:4px 8px 4px 44px;margin:0 -8px;border-radius:8px;cursor:text}
.blk:hover{background:rgba(194,65,12,.05)}
.blk .num{position:absolute;left:6px;top:6px;font:12px system-ui,sans-serif;color:var(--muted);cursor:pointer;user-select:none}
.blk.has .num{color:var(--accent);font-weight:700}
.blk h1,.blk h2,.blk h3{font-family:system-ui,sans-serif;line-height:1.25;margin:.6em 0 .3em}
.blk h1{font-size:30px}.blk h2{font-size:23px}.blk h3{font-size:19px}
.blk p{margin:.35em 0}
.blk.li p{padding-left:18px;text-indent:-14px}
.blk.li p::before{content:"•  "}
code{font-size:.85em;background:rgba(127,127,127,.15);padding:1px 4px;border-radius:4px}
pre{font:13.5px/1.5 Consolas,Menlo,monospace;background:rgba(127,127,127,.12);border-radius:8px;padding:10px 12px;margin:.4em 0;white-space:pre-wrap;word-break:break-word}
table{border-collapse:collapse;width:100%;font:15px/1.4 system-ui,sans-serif;margin:.4em 0}
th,td{border:1px solid var(--line);padding:6px 8px;text-align:left;vertical-align:top}
th{background:rgba(127,127,127,.1)}
a{color:var(--accent)}
.notes{margin:4px 0 10px;font:15px/1.45 system-ui,sans-serif}
.note{background:var(--note);border-left:3px solid var(--accent);border-radius:6px;padding:8px 10px;margin:6px 0}
.note .q{color:var(--muted);font-style:italic;margin-bottom:4px}
.note .acts{margin-top:6px;display:flex;gap:6px}
.note .acts button{font-size:12px;padding:3px 8px}
.editor{background:var(--card);border:1px solid var(--accent);border-radius:8px;padding:8px;margin:6px 0 12px;font:15px system-ui,sans-serif}
.editor .q{color:var(--muted);font-style:italic;margin-bottom:6px}
.editor textarea{width:100%;min-height:90px;font:16px/1.45 system-ui,sans-serif;border:1px solid var(--line);border-radius:6px;padding:8px;background:var(--bg);color:var(--fg)}
.editor .row{display:flex;gap:8px;margin-top:6px;flex-wrap:wrap}
.toast{position:fixed;bottom:16px;left:50%;transform:translateX(-50%);background:var(--fg);color:var(--bg);padding:8px 14px;border-radius:8px;font:14px system-ui,sans-serif;opacity:0;transition:opacity .2s;pointer-events:none}
.toast.on{opacity:1}
</style>
</head>
<body>
<header>
  <span class="count" id="count">Комментариев: 0</span>
  <button id="copy">Скопировать всё</button>
  <button class="main" id="save">Сохранить комментарии</button>
</header>
<main>
  <div class="hint">Выделите фразу или нажмите на номер абзаца слева — появится поле. Поставьте в него курсор и диктуйте через программу диктовки. Каждый комментарий сохраняется в браузере сам. В конце нажмите «Сохранить комментарии»: файл <b>__JSONNAME__</b> ляжет в Загрузки.</div>
  <div id="doc">__BLOCKS__</div>
</main>
<div class="toast" id="toast"></div>
<script>
const SOURCE = __SOURCE__;
const KEY = "kommentarii:" + SOURCE + ":" + __VERSION__;
const JSONNAME = __JSONNAMEJS__;
let notes = [];
try { notes = JSON.parse(localStorage.getItem(KEY) || "[]"); } catch (e) { notes = []; }
function store(){ try { localStorage.setItem(KEY, JSON.stringify(notes)); } catch (e) {} render(); }
function toast(t){ const el=document.getElementById("toast"); el.textContent=t; el.classList.add("on"); setTimeout(()=>el.classList.remove("on"),1800); }
function esc(s){ return s.replace(/[&<>]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;"}[c])); }

function render(){
  document.querySelectorAll(".blk").forEach(b=>{
    const id=b.dataset.id, mine=notes.filter(n=>n.block===id);
    b.classList.toggle("has", mine.length>0);
    const box=b.querySelector(".notes");
    box.innerHTML = mine.map(n=>`<div class="note" data-t="${n.time}">${n.quote?`<div class="q">«${esc(n.quote)}»</div>`:""}<div>${esc(n.comment)}</div><div class="acts"><button data-act="edit">Изменить</button><button data-act="del">Удалить</button></div></div>`).join("");
  });
  document.getElementById("count").textContent = "Комментариев: " + notes.length;
}

function openEditor(blk, quote, existing){
  document.querySelectorAll(".editor").forEach(e=>e.remove());
  const ed=document.createElement("div"); ed.className="editor";
  ed.innerHTML = `${quote?`<div class="q">«${esc(quote)}»</div>`:`<div class="q">Комментарий к абзацу ${blk.dataset.id}</div>`}<textarea placeholder="Диктуйте сюда"></textarea><div class="row"><button class="main" data-act="ok">Сохранить</button><button data-act="cancel">Отмена</button></div>`;
  const ta=ed.querySelector("textarea"); if(existing) ta.value=existing.comment;
  blk.querySelector(".notes").after(ed); ta.focus();
  const draftKey = KEY+":draft";
  ta.addEventListener("input",()=>{ try{localStorage.setItem(draftKey,JSON.stringify({block:blk.dataset.id,quote,text:ta.value}));}catch(e){} });
  ed.addEventListener("click",ev=>{
    const act=ev.target.dataset.act; if(!act) return;
    if(act==="ok"){
      const text=ta.value.trim();
      if(text){
        if(existing){ existing.comment=text; }
        else notes.push({block:blk.dataset.id, kind:blk.dataset.kind, block_text:blk.dataset.text, quote:quote||"", comment:text, time:new Date().toISOString()});
        store(); toast("Комментарий сохранён");
      }
    }
    try{localStorage.removeItem(draftKey);}catch(e){}
    ed.remove();
  });
}

document.getElementById("doc").addEventListener("mouseup", ev=>{
  if(ev.target.closest(".editor,.note,a")) return;
  const blk=ev.target.closest(".blk"); if(!blk) return;
  const sel=window.getSelection(); const q=sel?sel.toString().trim():"";
  if(ev.target.classList.contains("num")) { openEditor(blk,""); return; }
  if(q) openEditor(blk,q.replace(/\\s+/g," "));
});
document.getElementById("doc").addEventListener("click", ev=>{
  const b=ev.target.closest(".note button"); if(!b) return;
  const t=b.closest(".note").dataset.t, n=notes.find(x=>x.time===t), blk=b.closest(".blk");
  if(b.dataset.act==="del"){ notes=notes.filter(x=>x!==n); store(); }
  if(b.dataset.act==="edit"){ openEditor(blk,n.quote,n); }
});

function payload(){
  const order=[...document.querySelectorAll(".blk")].map(b=>b.dataset.id);
  const sorted=[...notes].sort((a,b)=>order.indexOf(a.block)-order.indexOf(b.block)||a.time.localeCompare(b.time));
  return JSON.stringify({source:SOURCE, saved:new Date().toISOString(), count:sorted.length, comments:sorted}, null, 2);
}
document.getElementById("save").onclick=()=>{
  const blob=new Blob([payload()],{type:"application/json"}); const a=document.createElement("a");
  a.href=URL.createObjectURL(blob); a.download=JSONNAME; document.body.appendChild(a); a.click(); a.remove();
  toast("Файл "+JSONNAME+" скачан");
};
document.getElementById("copy").onclick=async()=>{
  try{ await navigator.clipboard.writeText(payload()); toast("Скопировано"); }catch(e){ toast("Не получилось скопировать"); }
};
render();
</script>
</body>
</html>
"""


def build(src: Path, out_dir: Path) -> Path:
    md = src.read_text(encoding="utf-8")
    title = next((t for k, t in parse(md) if k == "h1"), src.stem)
    parts = []
    for i, (kind, raw) in enumerate(parse(md), 1):
        bid = f"b{i:03d}"
        cls = "li" if kind in ("li", "oli") else kind
        text_for_data = plain(raw)
        if kind.startswith("h"):
            inner = f"<{kind}>{inline(raw)}</{kind}>"
        elif kind == "pre":
            inner = f"<pre>{html.escape(raw)}</pre>"
        elif kind == "table":
            rows = json.loads(raw)
            head = "".join(f"<th>{inline(c)}</th>" for c in rows[0])
            body = "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in rows[1:])
            inner = f"<table><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table>"
            text_for_data = "\n".join(" | ".join(plain(c) for c in r) for r in rows)
        else:
            inner = f"<p>{inline(raw)}</p>"
        parts.append(
            f'<div class="blk {cls}" data-id="{bid}" data-kind="{kind}" data-text="{html.escape(text_for_data)}">'
            f'<span class="num" title="Комментарий к абзацу">{i}</span>{inner}<div class="notes"></div></div>')
    stamp = datetime.now().strftime("%Y-%m-%d-%H%M")
    version = hashlib.sha1(md.encode("utf-8")).hexdigest()[:10]
    name = f"{src.stem}-{stamp}"
    jsonname = f"kommentarii-{name}.json"
    page = (PAGE.replace("__TITLE__", html.escape(plain(title)))
            .replace("__VERSION__", json.dumps(version))
            .replace("__JSONNAMEJS__", json.dumps(jsonname))
            .replace("__JSONNAME__", html.escape(jsonname))
            .replace("__SOURCE__", json.dumps(str(src).replace("\\", "/"), ensure_ascii=False))
            .replace("__BLOCKS__", "\n".join(parts)))
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / f"kommentarii-{name}.html"
    out.write_text(page, encoding="utf-8")
    return out


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    src = Path(sys.argv[1])
    out_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else DEFAULT_OUT
    print(build(src, out_dir))
