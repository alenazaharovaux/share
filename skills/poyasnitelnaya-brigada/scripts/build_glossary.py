"""Собирает HTML-страницу глоссария «Пояснительная бригада» из файла terminy.md.

Запуск:
  python -I build_glossary.py [--data ПАПКА] [--out ПАПКА] [--open]

--data  папка с данными человека, по умолчанию ~/poyasnitelnaya-brigada
        (там nastrojki.md и terminy.md; если папки нет, она создаётся с пустыми файлами)
--out   куда положить страницу, по умолчанию ~/Downloads (если её нет, то папка данных)
--open  открыть страницу в браузере после сборки

Страница всегда называется poyasnitelnaya-brigada.html: её можно переслать одним файлом.
На странице есть слой комментариев. Кнопка «Сохранить комментарии» скачивает
poyasnitelnaya-brigada-<дата-время>.json, его читает read_comments.py.
"""
import argparse
import hashlib
import html
import json
import re
import sys
import webbrowser
from datetime import datetime
from pathlib import Path

PAGE_NAME = "poyasnitelnaya-brigada"

NASTROJKI_TEMPLATE = """# Настройки «Пояснительной бригады»

- стиль:

## Знаю эти слова
<!-- слова, которые человек отметил как знакомые; в списках из транскриптов их не предлагать -->
"""

TERMINY_TEMPLATE = """# Глоссарий
<!-- Новые термины добавляй сверху, сразу под этой строкой. Формат — в references/primer-termina.md -->
"""


# ---------- данные ----------

def ensure_data(data: Path) -> None:
    data.mkdir(parents=True, exist_ok=True)
    (data / "kommentarii").mkdir(exist_ok=True)
    if not (data / "nastrojki.md").exists():
        (data / "nastrojki.md").write_text(NASTROJKI_TEMPLATE, encoding="utf-8")
    if not (data / "terminy.md").exists():
        (data / "terminy.md").write_text(TERMINY_TEMPLATE, encoding="utf-8")


def read_style(data: Path) -> str:
    text = (data / "nastrojki.md").read_text(encoding="utf-8-sig")
    m = re.search(r"^-\s*стиль:\s*(.*)$", text, re.M)
    return m.group(1).strip() if m else ""


SECTIONS = {"история": "story", "просто": "plain", "пример": "example", "вопросы": "qa"}


def parse_terms(md: str):
    md = re.sub(r"<!--.*?-->", "", md, flags=re.S)
    terms = []
    for chunk in re.split(r"^## ", md, flags=re.M)[1:]:
        lines = chunk.splitlines()
        t = {"title": lines[0].strip(), "id": "", "дата": "", "сфера": "Разное", "стиль": "",
             "источник": "", "story": "", "plain": "", "example": "", "qa": ""}
        section = None
        buf = []

        def flush():
            if section:
                t[section] = "\n".join(buf).strip()

        for line in lines[1:]:
            h = re.match(r"^###\s+(.+?)\s*$", line)
            if h:
                flush()
                section = SECTIONS.get(h.group(1).strip().lower())
                buf = []
                continue
            if section is None:
                m = re.match(r"^-\s*([^:]+):\s*(.*)$", line)
                if m and m.group(1).strip().lower() in t:
                    t[m.group(1).strip().lower()] = m.group(2).strip()
                continue
            buf.append(line)
        flush()
        if not t["id"]:
            t["id"] = re.sub(r"[^a-z0-9а-яё]+", "-", t["title"].lower()).strip("-")
        terms.append(t)
    # свежие сверху; при одинаковой дате — порядок файла
    order = {id(t): i for i, t in enumerate(terms)}
    terms.sort(key=lambda t: (t["дата"], -order[id(t)]), reverse=True)
    return terms


# ---------- разметка ----------

def inline(text: str) -> str:
    s = html.escape(text, quote=False)
    s = re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", r'<a href="\2" target="_blank" rel="noopener">\1</a>', s)
    s = re.sub(r"(?<![\"'>=])(https?://[^\s<]+)", r'<a href="\1" target="_blank" rel="noopener">\1</a>', s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<!\*)\*(?!\s)(.+?)(?<!\s)\*(?!\*)", r"<em>\1</em>", s)
    return s


def blocks(text: str) -> str:
    out = []
    for para in re.split(r"\n\s*\n", text.strip()):
        lines = [l for l in para.splitlines() if l.strip()]
        if not lines:
            continue
        if all(re.match(r"^\s*[-*]\s+", l) for l in lines):
            out.append("<ul>" + "".join(f"<li>{inline(re.sub(r'^\s*[-*]\s+', '', l))}</li>" for l in lines) + "</ul>")
        else:
            out.append(f"<p>{inline(' '.join(l.strip() for l in lines))}</p>")
    return "\n".join(out)


def qa_blocks(text: str) -> str:
    out = []
    for part in re.split(r"^####\s+", text, flags=re.M):
        part = part.strip()
        if not part:
            continue
        q, _, a = part.partition("\n")
        out.append(f'<div class="qa-item"><h4>{inline(q.strip())}</h4>{blocks(a)}</div>')
    return "\n".join(out)


def fmt_date(d: str) -> str:
    try:
        return datetime.strptime(d, "%Y-%m-%d").strftime("%d.%m.%Y")
    except ValueError:
        return html.escape(d)


def sources(src: str) -> str:
    urls = re.findall(r"https?://\S+", src)
    if not urls:
        return f'<p class="src">Источник: {inline(src)}</p>' if src else ""
    links = " · ".join(
        f'<a href="{html.escape(u)}" target="_blank" rel="noopener">{html.escape(re.sub(r"^https?://(www\.)?", "", u).rstrip("/"))}</a>'
        for u in urls)
    return f'<p class="src">Источник: {links}</p>'


def term_html(t) -> str:
    style = t["стиль"]
    story_label = f"В стиле «{html.escape(style)}»" if style else "История"
    parts = [f'<article class="term" id="t-{html.escape(t["id"])}" data-term="{html.escape(t["id"])}" '
             f'data-sphere="{html.escape(t["сфера"])}">',
             f'<h2>{inline(t["title"])}</h2>',
             f'<div class="meta"><span class="chip">{html.escape(t["сфера"])}</span>'
             f'<span>{fmt_date(t["дата"])}</span></div>']
    if t["story"]:
        parts.append(f'<section class="story"><h3>{story_label}</h3>{blocks(t["story"])}</section>')
    if t["plain"]:
        parts.append(f'<section class="plain"><h3>Просто</h3>{blocks(t["plain"])}</section>')
    if t["example"]:
        parts.append(f'<section class="example"><h3>Пример</h3>{blocks(t["example"])}</section>')
    if t["qa"]:
        parts.append(f'<section class="qa"><h3>Вопросы и ответы</h3>{qa_blocks(t["qa"])}</section>')
    parts.append(sources(t["источник"]))
    parts.append("</article>")
    return "\n".join(parts)


CSS = """
:root{--bg:#f7f3ec;--card:#fff;--ink:#1f2328;--muted:#5f6670;--line:#e4ddd0;--accent:#7c2d12;--accent2:#c2410c;--soft:#fff4e6;--plain:#eef6f0;--plainline:#2f7d4f}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--ink);font:17px/1.55 -apple-system,"Segoe UI",Roboto,Arial,sans-serif}
.wrap{max-width:820px;margin:0 auto;padding:0 16px}
header.top{padding:32px 0 8px}
header.top h1{font-size:30px;line-height:1.15;margin:0 0 6px;color:var(--accent)}
header.top .sub{color:var(--muted);margin:0 0 16px}
.tools{position:sticky;top:0;z-index:50;background:var(--bg);padding:10px 0 12px;border-bottom:1px solid var(--line)}
.tools input{width:100%;font:16px -apple-system,"Segoe UI",Roboto,Arial,sans-serif;padding:10px 12px;border:1px solid var(--line);border-radius:10px;background:#fff}
.chips{display:flex;flex-wrap:wrap;gap:6px;margin-top:10px}
.chips button{font:14px -apple-system,"Segoe UI",Roboto,Arial,sans-serif;border:1px solid var(--line);background:#fff;color:var(--ink);border-radius:999px;padding:5px 12px;cursor:pointer}
.chips button.on{background:var(--accent);border-color:var(--accent);color:#fff}
main{padding:16px 0 40px}
.term{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:18px 20px;margin:0 0 16px;box-shadow:0 1px 2px rgba(0,0,0,.04)}
.term h2{margin:0 0 6px;font-size:24px;line-height:1.2}
.meta{display:flex;flex-wrap:wrap;gap:10px;align-items:center;color:var(--muted);font-size:14px;margin-bottom:12px}
.chip{background:var(--soft);color:var(--accent);border-radius:999px;padding:2px 10px;font-weight:600}
.term h3{font-size:13px;text-transform:uppercase;letter-spacing:.06em;color:var(--muted);margin:14px 0 6px}
.term p{margin:0 0 10px}
.story{border-left:3px solid var(--accent2);padding-left:14px}
.story p{font-style:italic}
.plain{background:var(--plain);border-left:3px solid var(--plainline);border-radius:8px;padding:4px 14px 2px}
.plain p{font-weight:600}
.qa-item{border-top:1px dashed var(--line);padding-top:8px;margin-top:8px}
.qa-item h4{margin:0 0 4px;font-size:16px}
.src{font-size:14px;color:var(--muted);margin:12px 0 0}
.src a{color:var(--accent2);word-break:break-all}
.empty{color:var(--muted);text-align:center;padding:40px 0}
.hidden{display:none}
footer{color:var(--muted);font-size:13px;padding:0 0 100px}
@media (max-width:520px){header.top h1{font-size:25px}.term{padding:14px}.term h2{font-size:21px}}
"""

FILTER_JS = """
<script>
(function(){
const q=document.getElementById("q"),chips=[...document.querySelectorAll(".chips button")],terms=[...document.querySelectorAll(".term")];
let sphere="";
function apply(){const s=q.value.trim().toLowerCase();let n=0;
  terms.forEach(t=>{const ok=(!sphere||t.dataset.sphere===sphere)&&(!s||t.innerText.toLowerCase().includes(s));t.classList.toggle("hidden",!ok);if(ok)n++;});
  document.getElementById("none").classList.toggle("hidden",n>0||!terms.length);
  window.dispatchEvent(new Event("resize"));}
q.addEventListener("input",apply);
chips.forEach(b=>b.addEventListener("click",()=>{chips.forEach(x=>x.classList.remove("on"));b.classList.add("on");sphere=b.dataset.sphere;apply();}));
})();
</script>
"""


def page_html(terms, style: str) -> str:
    spheres = []
    for t in terms:
        if t["сфера"] not in spheres:
            spheres.append(t["сфера"])
    chips = '<button class="on" data-sphere="">Все</button>' + "".join(
        f'<button data-sphere="{html.escape(s)}">{html.escape(s)}</button>' for s in spheres)
    style_line = f"Сейчас объясняю в стиле «{html.escape(style)}». " if style else ""
    body = "\n".join(term_html(t) for t in terms) if terms else (
        '<p class="empty">Пока пусто. Скажи агенту: «бригада, что такое …»</p>')
    return f"""<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Пояснительная бригада</title>
<style>{CSS}</style>
</head>
<body>
<div class="wrap">
<header class="top">
<h1>Пояснительная бригада</h1>
<p class="sub">{style_line}Терминов: {len(terms)}. Свежие сверху. Выделите слово, фразу или наведите на блок и нажмите «+ комментарий»: задайте вопрос или напишите «удали».</p>
</header>
<div class="tools">
<input id="q" type="search" placeholder="Поиск по глоссарию">
<div class="chips">{chips}</div>
</div>
<main>
{body}
<p id="none" class="empty hidden">Ничего не нашлось.</p>
</main>
<footer>Собрано {datetime.now().strftime("%d.%m.%Y %H:%M")}.</footer>
</div>
{FILTER_JS}
</body>
</html>
"""


# ---------- слой комментариев (из навыка «Понятный текст», плюс поле term) ----------

LAYER = r"""
<style id="cm-style">
.cm-bar{position:fixed;bottom:16px;right:16px;z-index:9000;display:flex;gap:8px;font:14px/1.3 -apple-system,"Segoe UI",Roboto,Arial,sans-serif}
.cm-bar button,.cm-pop button,.cm-panel button{font:14px -apple-system,"Segoe UI",Roboto,Arial,sans-serif;border:1px solid #d8d3c8;background:#fff;color:#1f2328;border-radius:8px;padding:7px 12px;cursor:pointer;box-shadow:0 1px 3px rgba(0,0,0,.08)}
.cm-bar .cm-main,.cm-pop .cm-main{background:#c2410c;border-color:#c2410c;color:#fff}
.cm-t{position:relative;cursor:text}
.cm-t:hover{outline:2px solid rgba(194,65,12,.25);outline-offset:3px;border-radius:4px}
.cm-t.cm-has{outline:2px solid #c2410c;outline-offset:3px;border-radius:4px}
.cm-add{position:absolute;z-index:8000;font:12px -apple-system,"Segoe UI",Roboto,Arial,sans-serif;background:#c2410c;color:#fff;border:0;border-radius:999px;padding:3px 10px;cursor:pointer;display:none;box-shadow:0 1px 3px rgba(0,0,0,.2)}
.cm-badge{position:absolute;z-index:7000;font:12px/1 -apple-system,"Segoe UI",Roboto,Arial,sans-serif;background:#c2410c;color:#fff;border-radius:999px;padding:4px 8px;cursor:pointer}
.cm-pop{position:absolute;z-index:9100;width:min(420px,calc(100vw - 32px));background:#fff;color:#1f2328;border:2px solid #c2410c;border-radius:12px;padding:12px;box-shadow:0 8px 24px rgba(0,0,0,.18);font:15px/1.45 -apple-system,"Segoe UI",Roboto,Arial,sans-serif}
.cm-pop .cm-q{color:#5f6670;font-style:italic;margin-bottom:8px}
.cm-pop textarea{width:100%;min-height:100px;box-sizing:border-box;font:16px/1.45 -apple-system,"Segoe UI",Roboto,Arial,sans-serif;border:1px solid #d8d3c8;border-radius:8px;padding:8px}
.cm-pop .cm-row{display:flex;gap:8px;margin-top:8px}
.cm-panel{position:fixed;top:0;right:0;bottom:0;z-index:9200;width:min(400px,100vw);background:#fff;color:#1f2328;border-left:1px solid #d8d3c8;box-shadow:-8px 0 24px rgba(0,0,0,.12);padding:16px;overflow:auto;display:none;font:15px/1.45 -apple-system,"Segoe UI",Roboto,Arial,sans-serif}
.cm-panel.on{display:block}
.cm-panel h3{margin:0 0 12px;font-size:18px;display:flex;justify-content:space-between;align-items:center}
.cm-item{border-left:3px solid #c2410c;background:#fff4e6;border-radius:6px;padding:8px 10px;margin:0 0 10px;cursor:pointer}
.cm-item .cm-q{color:#5f6670;font-style:italic;margin-bottom:4px}
.cm-item .cm-acts{display:flex;gap:6px;margin-top:6px}
.cm-item .cm-acts button{font-size:12px;padding:3px 8px}
.cm-toast{position:fixed;bottom:72px;left:50%;transform:translateX(-50%);z-index:9300;background:#1f2328;color:#fff;padding:8px 14px;border-radius:8px;font:14px -apple-system,"Segoe UI",Roboto,Arial,sans-serif;opacity:0;transition:opacity .2s;pointer-events:none}
.cm-toast.on{opacity:1}
.cm-flash{animation:cmflash 1.2s}
@keyframes cmflash{0%{background:rgba(194,65,12,.25)}100%{background:transparent}}
</style>
<div class="cm-bar"><button id="cm-open">Комментарии: 0</button><button class="cm-main" id="cm-save">Сохранить комментарии</button></div>
<button class="cm-add" id="cm-add">+ комментарий</button>
<div class="cm-panel" id="cm-panel"><h3>Комментарии <button id="cm-close">Закрыть</button></h3><div id="cm-list"></div></div>
<div class="cm-toast" id="cm-toast"></div>
<script>
(function(){
const SOURCE=__SOURCE__, KEY="kommentarii:"+SOURCE+":"+__VERSION__, JSONNAME=__JSONNAME__;
const root=document.querySelector("main")||document.body;
const targets=[...root.querySelectorAll("h1,h2,h3,h4,p,li")].filter(el=>!el.closest(".cm-bar,.cm-panel,.cm-pop")&&!el.classList.contains("empty"));
targets.forEach((el,i)=>{el.classList.add("cm-t");el.dataset.cmId="b"+String(i+1).padStart(3,"0");});
const byId=id=>targets.find(t=>t.dataset.cmId===id);
const termOf=el=>{const a=el.closest("[data-term]");return a?{term:a.dataset.term,term_title:(a.querySelector("h2")||{innerText:""}).innerText.trim()}:{term:"",term_title:""};};
let notes=[]; try{notes=JSON.parse(localStorage.getItem(KEY)||"[]");}catch(e){notes=[];}
const esc=s=>s.replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
const txt=el=>el.innerText.replace(/\s+/g," ").trim();
function toast(t){const el=document.getElementById("cm-toast");el.textContent=t;el.classList.add("on");setTimeout(()=>el.classList.remove("on"),1800);}
function store(){try{localStorage.setItem(KEY,JSON.stringify(notes));}catch(e){} render();}
function pos(el){const r=el.getBoundingClientRect();return{top:r.top+scrollY,left:r.left+scrollX,right:r.right+scrollX,bottom:r.bottom+scrollY};}
function render(){
  document.querySelectorAll(".cm-badge").forEach(b=>b.remove());
  targets.forEach(t=>{const n=notes.filter(x=>x.block===t.dataset.cmId).length;t.classList.toggle("cm-has",n>0);
    if(n&&t.offsetParent!==null){const p=pos(t),b=document.createElement("span");b.className="cm-badge";b.textContent=n;b.style.top=(p.top-12)+"px";b.style.left=(Math.min(p.right,document.documentElement.clientWidth+scrollX-40)-6)+"px";b.onclick=()=>openPanel(t.dataset.cmId);document.body.appendChild(b);}});
  document.getElementById("cm-open").textContent="Комментарии: "+notes.length;
  const order=targets.map(t=>t.dataset.cmId);
  const sorted=[...notes].sort((a,b)=>order.indexOf(a.block)-order.indexOf(b.block)||a.time.localeCompare(b.time));
  document.getElementById("cm-list").innerHTML=sorted.length?sorted.map(n=>`<div class="cm-item" data-t="${n.time}" data-b="${n.block}">${n.term_title?`<div><b>${esc(n.term_title)}</b></div>`:""}${n.quote?`<div class="cm-q">«${esc(n.quote)}»</div>`:`<div class="cm-q">${esc(n.block_text.slice(0,90))}${n.block_text.length>90?"…":""}</div>`}<div>${esc(n.comment)}</div><div class="cm-acts"><button data-act="edit">Изменить</button><button data-act="del">Удалить</button></div></div>`).join(""):"<p>Пока нет комментариев. Выделите фразу или наведите на абзац и нажмите «+ комментарий».</p>";
}
let pop=null;
function closePop(){if(pop){pop.remove();pop=null;}}
function openPop(el,quote,existing){
  closePop(); addBtn.style.display="none";
  pop=document.createElement("div");pop.className="cm-pop";
  pop.innerHTML=`<div class="cm-q">${esc(quote?"«"+quote+"»":(t=>t.length>140?t.slice(0,t.lastIndexOf(" ",140))+"…":t)(txt(el)))}</div><textarea placeholder="Вопрос, «удали», «знаю это слово» — что угодно"></textarea><div class="cm-row"><button class="cm-main" data-act="ok">Сохранить</button><button data-act="cancel">Отмена</button></div>`;
  document.body.appendChild(pop);
  const p=pos(el),w=pop.offsetWidth,maxL=document.documentElement.clientWidth+scrollX-w-16;
  pop.style.top=(p.bottom+8)+"px";pop.style.left=Math.max(16,Math.min(p.left,maxL))+"px";
  const ta=pop.querySelector("textarea");if(existing)ta.value=existing.comment;ta.focus();
  pop.addEventListener("click",ev=>{const a=ev.target.dataset.act;if(!a)return;
    if(a==="ok"){const t=ta.value.trim();if(t){if(existing)existing.comment=t;else notes.push(Object.assign({block:el.dataset.cmId,kind:el.tagName.toLowerCase(),block_text:txt(el),quote:quote||"",comment:t,time:new Date().toISOString()},termOf(el)));store();toast("Комментарий сохранён");}}
    closePop();});
}
const addBtn=document.getElementById("cm-add");let hoverEl=null;
root.addEventListener("mouseover",ev=>{const t=ev.target.closest(".cm-t");if(!t||pop)return;
  const inner=[...t.querySelectorAll(".cm-t")].find(x=>x.contains(ev.target));hoverEl=inner||t;
  const p=pos(hoverEl);addBtn.style.display="block";addBtn.style.top=(p.top-10)+"px";addBtn.style.left=Math.max(8,p.right-110)+"px";});
addBtn.addEventListener("click",()=>{if(hoverEl)openPop(hoverEl,"");});
document.addEventListener("mouseup",ev=>{if(ev.target.closest(".cm-pop,.cm-bar,.cm-panel,.cm-add,.cm-badge,.tools"))return;
  const sel=getSelection(),q=sel?sel.toString().replace(/\s+/g," ").trim():"";if(!q)return;
  const node=sel.anchorNode&&(sel.anchorNode.nodeType===1?sel.anchorNode:sel.anchorNode.parentElement);const el=node&&node.closest(".cm-t");if(el)openPop(el,q);});
document.addEventListener("keydown",ev=>{if(ev.key==="Escape"){closePop();document.getElementById("cm-panel").classList.remove("on");}});
function openPanel(id){document.getElementById("cm-panel").classList.add("on");if(id){const it=document.querySelector(`.cm-item[data-b="${id}"]`);if(it)it.scrollIntoView({block:"center"});}}
document.getElementById("cm-open").onclick=()=>openPanel();
document.getElementById("cm-close").onclick=()=>document.getElementById("cm-panel").classList.remove("on");
document.getElementById("cm-list").addEventListener("click",ev=>{const it=ev.target.closest(".cm-item");if(!it)return;const n=notes.find(x=>x.time===it.dataset.t),el=byId(it.dataset.b);
  if(ev.target.dataset.act==="del"){notes=notes.filter(x=>x!==n);store();return;}
  if(ev.target.dataset.act==="edit"){document.getElementById("cm-panel").classList.remove("on");el.scrollIntoView({block:"center"});openPop(el,n.quote,n);return;}
  el.scrollIntoView({block:"center",behavior:"smooth"});el.classList.add("cm-flash");setTimeout(()=>el.classList.remove("cm-flash"),1300);});
function payload(){const order=targets.map(t=>t.dataset.cmId);const s=[...notes].sort((a,b)=>order.indexOf(a.block)-order.indexOf(b.block)||a.time.localeCompare(b.time));return JSON.stringify({source:SOURCE,saved:new Date().toISOString(),count:s.length,comments:s},null,2);}
document.getElementById("cm-save").onclick=()=>{const a=document.createElement("a");a.href=URL.createObjectURL(new Blob([payload()],{type:"application/json"}));a.download=JSONNAME;document.body.appendChild(a);a.click();a.remove();toast("Файл "+JSONNAME+" скачан");};
addEventListener("resize",render);
render();
})();
</script>
"""


def add_layer(page: str) -> str:
    stamp = datetime.now().strftime("%Y-%m-%d-%H%M")
    jsonname = f"{PAGE_NAME}-{stamp}.json"
    version = hashlib.sha1(page.encode("utf-8")).hexdigest()[:10]
    layer = (LAYER.replace("__SOURCE__", json.dumps(PAGE_NAME))
             .replace("__VERSION__", json.dumps(version))
             .replace("__JSONNAME__", json.dumps(jsonname)))
    idx = page.lower().rfind("</body>")
    return page[:idx] + layer + page[idx:]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--data", type=Path, default=Path.home() / "poyasnitelnaya-brigada")
    ap.add_argument("--out", type=Path, default=None)
    ap.add_argument("--open", action="store_true")
    args = ap.parse_args()
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass

    ensure_data(args.data)
    out_dir = args.out or (Path.home() / "Downloads")
    if not out_dir.exists():
        out_dir = args.data
    terms = parse_terms((args.data / "terminy.md").read_text(encoding="utf-8-sig"))
    page = add_layer(page_html(terms, read_style(args.data)))
    out = out_dir / f"{PAGE_NAME}.html"
    out.write_text(page, encoding="utf-8")
    print(f"{out}  (терминов: {len(terms)})")
    if args.open:
        webbrowser.open(out.resolve().as_uri())


if __name__ == "__main__":
    sys.exit(main())
