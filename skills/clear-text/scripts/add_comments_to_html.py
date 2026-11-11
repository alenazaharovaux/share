"""Adds a comment layer to a finished HTML page and keeps its design.

Usage:  python -I add_comments_to_html.py <page.html> [output-folder]
Writes comments-<name>-<date-time>.html to the Downloads folder (~/Downloads).
Headings, paragraphs and list items inside <main> (or <body> if there is no <main>) can be commented.
Comments are kept in the browser; the "Save comments" button downloads a .json file in the same format
as make_comment_page.py, which read_comments.py reads.
"""
import hashlib
import json
import sys
from datetime import datetime
from pathlib import Path

DEFAULT_OUT = Path.home() / "Downloads"

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
body{padding-bottom:80px}
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
<div class="cm-bar"><button id="cm-open">Comments: 0</button><button class="cm-main" id="cm-save">Save comments</button></div>
<button class="cm-add" id="cm-add">+ comment</button>
<div class="cm-panel" id="cm-panel"><h3>Comments <button id="cm-close">Close</button></h3><div id="cm-list"></div></div>
<div class="cm-toast" id="cm-toast"></div>
<script>
(function(){
const SOURCE=__SOURCE__, KEY="comments:"+SOURCE+":"+__VERSION__, JSONNAME=__JSONNAME__;
const root=document.querySelector("main")||document.body;
const targets=[...root.querySelectorAll("h1,h2,h3,h4,p,li")].filter(el=>!el.closest(".cm-bar,.cm-panel,.cm-pop"));
targets.forEach((el,i)=>{el.classList.add("cm-t");el.dataset.cmId="b"+String(i+1).padStart(3,"0");});
const byId=id=>targets.find(t=>t.dataset.cmId===id);
let notes=[]; try{notes=JSON.parse(localStorage.getItem(KEY)||"[]");}catch(e){notes=[];}
const esc=s=>s.replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
const txt=el=>el.innerText.replace(/\s+/g," ").trim();
function toast(t){const el=document.getElementById("cm-toast");el.textContent=t;el.classList.add("on");setTimeout(()=>el.classList.remove("on"),1800);}
function store(){try{localStorage.setItem(KEY,JSON.stringify(notes));}catch(e){} render();}
function pos(el){const r=el.getBoundingClientRect();return{top:r.top+scrollY,left:r.left+scrollX,right:r.right+scrollX,bottom:r.bottom+scrollY};}
function render(){
  document.querySelectorAll(".cm-badge").forEach(b=>b.remove());
  targets.forEach(t=>{const n=notes.filter(x=>x.block===t.dataset.cmId).length;t.classList.toggle("cm-has",n>0);
    if(n){const p=pos(t),b=document.createElement("span");b.className="cm-badge";b.textContent=n;b.style.top=(p.top-12)+"px";b.style.left=(Math.min(p.right,document.documentElement.clientWidth+scrollX-40)-6)+"px";b.onclick=()=>openPanel(t.dataset.cmId);document.body.appendChild(b);}});
  document.getElementById("cm-open").textContent="Comments: "+notes.length;
  const order=targets.map(t=>t.dataset.cmId);
  const sorted=[...notes].sort((a,b)=>order.indexOf(a.block)-order.indexOf(b.block)||a.time.localeCompare(b.time));
  document.getElementById("cm-list").innerHTML=sorted.length?sorted.map(n=>`<div class="cm-item" data-t="${n.time}" data-b="${n.block}">${n.quote?`<div class="cm-q">“${esc(n.quote)}”</div>`:`<div class="cm-q">${esc(n.block_text.slice(0,90))}${n.block_text.length>90?"…":""}</div>`}<div>${esc(n.comment)}</div><div class="cm-acts"><button data-act="edit">Edit</button><button data-act="del">Delete</button></div></div>`).join(""):"<p>No comments yet. Select a phrase, or hover over a paragraph and press “+ comment”.</p>";
}
let pop=null;
function closePop(){if(pop){pop.remove();pop=null;}}
function openPop(el,quote,existing){
  closePop(); addBtn.style.display="none";
  pop=document.createElement("div");pop.className="cm-pop";
  pop.innerHTML=`<div class="cm-q">${esc(quote?"“"+quote+"”":(t=>t.length>140?t.slice(0,t.lastIndexOf(" ",140))+"…":t)(txt(el)))}</div><textarea placeholder="Type or dictate here"></textarea><div class="cm-row"><button class="cm-main" data-act="ok">Save</button><button data-act="cancel">Cancel</button></div>`;
  document.body.appendChild(pop);
  const p=pos(el),w=pop.offsetWidth,maxL=document.documentElement.clientWidth+scrollX-w-16;
  pop.style.top=(p.bottom+8)+"px";pop.style.left=Math.max(16,Math.min(p.left,maxL))+"px";
  const ta=pop.querySelector("textarea");if(existing)ta.value=existing.comment;ta.focus();
  pop.addEventListener("click",ev=>{const a=ev.target.dataset.act;if(!a)return;
    if(a==="ok"){const t=ta.value.trim();if(t){if(existing)existing.comment=t;else notes.push({block:el.dataset.cmId,kind:el.tagName.toLowerCase(),block_text:txt(el),quote:quote||"",comment:t,time:new Date().toISOString()});store();toast("Comment saved");}}
    closePop();});
}
const addBtn=document.getElementById("cm-add");let hoverEl=null;
root.addEventListener("mouseover",ev=>{const t=ev.target.closest(".cm-t");if(!t||pop)return;
  const inner=[...t.querySelectorAll(".cm-t")].find(x=>x.contains(ev.target));hoverEl=inner||t;
  const p=pos(hoverEl);addBtn.style.display="block";addBtn.style.top=(p.top-10)+"px";addBtn.style.left=Math.max(8,p.right-110)+"px";});
addBtn.addEventListener("click",()=>{if(hoverEl)openPop(hoverEl,"");});
document.addEventListener("mouseup",ev=>{if(ev.target.closest(".cm-pop,.cm-bar,.cm-panel,.cm-add,.cm-badge"))return;
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
document.getElementById("cm-save").onclick=()=>{const a=document.createElement("a");a.href=URL.createObjectURL(new Blob([payload()],{type:"application/json"}));a.download=JSONNAME;document.body.appendChild(a);a.click();a.remove();toast("File "+JSONNAME+" downloaded");};
addEventListener("resize",render);
render();
})();
</script>
"""


def build(src: Path, out_dir: Path) -> Path:
    page = src.read_text(encoding="utf-8")
    stamp = datetime.now().strftime("%Y-%m-%d-%H%M")
    name = f"{src.stem}-{stamp}"
    jsonname = f"comments-{name}.json"
    version = hashlib.sha1(page.encode("utf-8")).hexdigest()[:10]
    layer = (LAYER.replace("__SOURCE__", json.dumps(str(src).replace("\\", "/"), ensure_ascii=False))
             .replace("__VERSION__", json.dumps(version))
             .replace("__JSONNAME__", json.dumps(jsonname)))
    idx = page.lower().rfind("</body>")
    page = page[:idx] + layer + page[idx:] if idx != -1 else page + layer
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / f"comments-{name}.html"
    out.write_text(page, encoding="utf-8")
    return out


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    src = Path(sys.argv[1])
    out_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else DEFAULT_OUT
    print(build(src, out_dir))
