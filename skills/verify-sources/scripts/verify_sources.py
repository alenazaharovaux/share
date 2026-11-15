"""Проверка источников программой: каждая цитата ищется в самом источнике.

Запуск:  python verify_sources.py claims.json
Итог:    verification.md и verification.json рядом с claims.json.

Только стандартная библиотека Python. Интернет нужен.
Формат claims.json — references/claims-format.md.
"""
import html
import html.parser
import json
import pathlib
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/140.0 Safari/537.36 verify-sources/1.0")
TIMEOUT = 25
SHINGLE = 5          # слов в куске при нечётком поиске цитаты
PARTIAL_OK = 0.8     # доля кусков цитаты, найденных в источнике


# ---------- сеть ----------

def fetch_raw(url, accept=None):
    """Вернуть (код ответа, байты, тип содержимого, конечный адрес, кодировка). Код 0 — сеть недоступна."""
    headers = {"User-Agent": UA, "Accept-Language": "ru,en;q=0.8"}
    if accept:
        headers["Accept"] = accept
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            return (r.status, r.read(20_000_000), r.headers.get("Content-Type", ""), r.geturl(),
                    r.headers.get_content_charset() or "utf-8")
    except urllib.error.HTTPError as e:
        return e.code, b"", e.headers.get("Content-Type", "") if e.headers else "", url, "utf-8"
    except Exception as e:  # noqa: BLE001 — любая сетевая ошибка значит «не открылся»
        return 0, f"{type(e).__name__}: {e}".encode(), "", url, "utf-8"


def fetch(url, accept=None):
    """Вернуть (код ответа, текст, тип содержимого, конечный адрес). Код 0 — сеть недоступна."""
    code, raw, ctype, final, charset = fetch_raw(url, accept)
    return code, raw.decode(charset, errors="replace"), ctype, final


def pdf_to_text(raw):
    """Текст PDF через pypdf или PyMuPDF, если установлены. Пустая строка — прочитать не удалось."""
    import io
    try:
        import pypdf
        return " ".join((p.extract_text() or "") for p in pypdf.PdfReader(io.BytesIO(raw)).pages)
    except Exception:  # noqa: BLE001
        pass
    try:
        import fitz
        with fitz.open(stream=raw, filetype="pdf") as doc:
            return " ".join(page.get_text() for page in doc)
    except Exception:  # noqa: BLE001
        return ""


class TextExtractor(html.parser.HTMLParser):
    SKIP = {"script", "style", "noscript", "svg", "template"}

    def __init__(self):
        super().__init__()
        self.parts, self.skip = [], 0

    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP:
            self.skip += 1

    def handle_endtag(self, tag):
        if tag in self.SKIP and self.skip:
            self.skip -= 1

    def handle_data(self, data):
        if not self.skip:
            self.parts.append(data)


def html_to_text(s):
    p = TextExtractor()
    try:
        p.feed(s)
    except Exception:  # noqa: BLE001 — битая разметка: берём что успели
        pass
    return " ".join(p.parts)


# ---------- нормализация ----------

DOI_RE = re.compile(r"10\.\d{4,9}/[^\s\"<>]+", re.I)


def clean_doi(s):
    m = DOI_RE.search(urllib.parse.unquote(s or ""))
    if not m:
        return None
    doi = m.group(0)
    # хвост URL после DOI — частая ошибка парсинга
    doi = re.sub(r"/(full|abstract|pdf|epdf|html)$", "", doi, flags=re.I)
    doi = re.sub(r"v\d+$", "", doi) if doi.startswith("10.1101/") else doi
    return doi.rstrip(".,;)")


def norm(s):
    # NFKC раскладывает лигатуры PDF (ﬂ → fl, ﬁ → fi) и полноширинные знаки
    s = unicodedata.normalize("NFKC", html.unescape(s or "")).lower().replace("ё", "е")
    s = re.sub(r"[«»“”„\"‟″]", '"', s)
    s = re.sub(r"[‘’‚‛′`]", "'", s)
    s = re.sub(r"[‐‑‒–—―−]", "-", s)
    s = s.replace("­", "").replace("​", "")
    s = re.sub(r"(\d)[·⋅∙](\d)", r"\1.\2", s)                # 1·2 (Lancet) → 1.2
    s = re.sub(r"(\d)[\s  ](\d{3})", r"\1\2", s)   # 1 234 → 1234
    s = re.sub(r"\s+", " ", s)
    return s.strip()


NUM_RE = re.compile(r"(?<![\w.])-?\d+(?:[.,]\d+)?")


def numbers(s):
    out = []
    for n in NUM_RE.findall(norm(s)):
        n = n.replace(",", ".")
        if n not in out:
            out.append(n)
    return out


def number_in(n, text_norm):
    variants = {n, n.replace(".", ",")}
    return any(re.search(r"(?<![\d.,])" + re.escape(v) + r"(?![\d])", text_norm) for v in variants)


def loose(s):
    """Без знаков препинания: цитаты часто расходятся только кавычками и точкой внутри них."""
    s = re.sub(r"(?<=\d)[.,](?=\d)", "DECIMAL", s)
    s = re.sub(r"[^\w\s]", " ", s)
    return re.sub(r"\s+", " ", s.replace("DECIMAL", ".")).strip()


def quote_found(quote, text_norm, text_loose=None):
    q = norm(quote).strip(" \"'.,;:")
    if not q:
        return "нет цитаты", 0.0
    if q in text_norm:
        return "найдена", 1.0
    text_loose = text_loose if text_loose is not None else loose(text_norm)
    q_loose = loose(q)
    if q_loose and q_loose in text_loose:
        return "найдена", 1.0
    words = q_loose.split()
    text_norm = text_loose
    if len(words) < SHINGLE:
        return "не найдена", 0.0
    shingles = [" ".join(words[i:i + SHINGLE]) for i in range(len(words) - SHINGLE + 1)]
    share = sum(1 for sh in shingles if sh in text_norm) / len(shingles)
    if share >= PARTIAL_OK:
        return "найдена частично", share
    return "не найдена", share


# ---------- источники ----------

def load_doi(doi):
    """Текст для сверки по DOI: метаданные + аннотация Europe PMC + страница издателя, если открылась."""
    info = {"doi": doi, "texts": [], "notes": []}
    code, body, _, _ = fetch(f"https://doi.org/api/handles/{urllib.parse.quote(doi)}")
    try:
        exists = json.loads(body).get("responseCode") == 1
    except Exception:  # noqa: BLE001
        exists = False
    info["code"] = code
    info["exists"] = exists
    if not exists:
        info["notes"].append("DOI не зарегистрирован в doi.org")
        return info
    code, body, _, _ = fetch(f"https://doi.org/{doi}", accept="application/vnd.citationstyles.csl+json")
    if code == 200:
        try:
            meta = json.loads(body)
            info["title"] = (meta.get("title") or "")
            info["year"] = ((meta.get("issued") or {}).get("date-parts") or [[None]])[0][0]
            info["journal"] = meta.get("container-title") or ""
            info["authors"] = [a.get("family", "") for a in meta.get("author", [])][:6]
            info["texts"].append(info["title"])
        except Exception:  # noqa: BLE001
            pass
    _, _, abstract = europepmc_abstract(f'DOI:"{doi}"')
    if abstract:
        info["texts"].append(abstract)
        info["notes"].append("аннотация из Europe PMC")
    code, body, ctype, final = fetch(f"https://doi.org/{doi}")
    info["publisher_code"] = code
    info["full_text"] = False
    if code == 200 and "html" in ctype:
        info["texts"].append(html_to_text(body))
        info["notes"].append("страница издателя открылась")
        info["full_text"] = True
    elif code == 403:
        info["notes"].append("страница издателя: 403 (защита от роботов, ссылка живая)")
    return info


def fetch_json(url):
    """JSON с повтором на 429 (Semantic Scholar и Crossref ограничивают частоту)."""
    for attempt in range(3):
        code, body, _, _ = fetch(url, accept="application/json")
        if code == 429:
            time.sleep(5 * (attempt + 1))
            continue
        if code != 200:
            return None
        try:
            return json.loads(body)
        except Exception:  # noqa: BLE001
            return None
    return None


def other_abstracts(doi):
    """Аннотации из OpenAlex, Crossref и Semantic Scholar: {база: текст}."""
    out, q = {}, urllib.parse.quote(doi)
    j = fetch_json(f"https://api.openalex.org/works/doi:{q}")
    if j and j.get("abstract_inverted_index"):
        pos = {p: w for w, ps in j["abstract_inverted_index"].items() for p in ps}
        out["OpenAlex"] = " ".join(pos[i] for i in sorted(pos))
    j = fetch_json(f"https://api.crossref.org/works/{q}")
    if j and (j.get("message") or {}).get("abstract"):
        out["Crossref"] = html_to_text(j["message"]["abstract"])
    j = fetch_json(f"https://api.semanticscholar.org/graph/v1/paper/DOI:{q}?fields=abstract")
    if j and j.get("abstract"):
        out["Semantic Scholar"] = j["abstract"]
    time.sleep(0.3)
    return out


def europepmc_abstract(query):
    q = urllib.parse.quote(query)
    code, body, _, _ = fetch(f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?query={q}&resultType=core&format=json")
    try:
        res = json.loads(body).get("resultList", {}).get("result", [])
    except Exception:  # noqa: BLE001
        return code, "", ""
    if not res:
        return code, "", ""
    return code, res[0].get("title", ""), html_to_text(res[0].get("abstractText", ""))


def load_url(url):
    info = {"url": url, "texts": [], "notes": []}
    m = re.search(r"pubmed\.ncbi\.nlm\.nih\.gov/(\d+)", url)
    if m:
        # страница PubMed отдаёт капчу роботам — берём аннотацию из Europe PMC
        code, title, abstract = europepmc_abstract(f"EXT_ID:{m.group(1)} AND SRC:MED")
        info["code"] = code
        if abstract:
            info["title"] = title
            info["texts"] += [title, abstract]
            info["notes"].append("PubMed: аннотация из Europe PMC")
        else:
            info["notes"].append("PubMed: аннотация в Europe PMC не найдена")
        return info
    code, raw, ctype, final, charset = fetch_raw(url)
    body = raw.decode(charset, errors="replace")
    info["code"] = code
    info["final_url"] = final
    if code == 200:
        if "pdf" in ctype.lower() or raw[:5] == b"%PDF-":
            text = pdf_to_text(raw)
            if text.strip():
                info["texts"].append(text)
                info["notes"].append("PDF прочитан программой")
            else:
                info["notes"].append("PDF: текст не извлёкся (скан или нет pypdf), сверить новой сессией")
        else:
            info["texts"].append(html_to_text(body) if "html" in ctype.lower() or "<html" in body[:500].lower() else body)
    elif code == 0:
        info["notes"].append(body)
    elif code == 403:
        info["notes"].append("403: сайт закрыт от роботов, ссылка может быть живой")
    return info


# ---------- проверка ----------

def check(claims):
    cache, results = {}, []
    for i, c in enumerate(claims, 1):
        cid = str(c.get("id") or i)
        src = (c.get("doi") or c.get("source") or c.get("url") or "").strip()
        r = {"id": cid, "claim": c.get("claim", ""), "source": src, "quote": c.get("quote", ""),
             "location": c.get("location", "")}
        if c.get("data"):
            # число из таблицы или файла: цитаты в тексте нет, сверяет новая сессия по сохранённому файлу
            r["status"] = "число из файла"
            r["data"] = c["data"]
            results.append(r)
            continue
        if not src:
            r["status"] = "нет источника"
            results.append(r)
            continue
        doi = clean_doi(src)
        key = doi or src
        if key not in cache:
            cache[key] = load_doi(doi) if doi else load_url(src)
        info = cache[key]
        r["code"] = info.get("code")
        r["notes"] = list(info.get("notes", []))
        if doi and not info.get("exists"):
            r["status"] = "DOI не существует"
            results.append(r)
            continue
        text = norm(" ".join(info["texts"]))
        verdict, share = ("не найдена", 0.0)
        if text:
            if "loose" not in info:
                info["loose"] = loose(text)
            verdict, share = quote_found(r["quote"], text, info["loose"])
        if doi and verdict != "найдена" and r["quote"] and "abstracts" not in info:
            # второй проход: аннотации из других баз, один раз на DOI
            info["abstracts"] = other_abstracts(doi)
            if info["abstracts"]:
                info["texts"] += list(info["abstracts"].values())
                info["notes"].append("аннотации: " + ", ".join(info["abstracts"]))
                text = norm(" ".join(info["texts"]))
                info["loose"] = loose(text)
                verdict, share = quote_found(r["quote"], text, info["loose"])
                r["notes"] = list(info["notes"])
        if not text:
            r["status"] = "источник не прочитан"
            results.append(r)
            continue
        r["quote_check"] = verdict
        r["quote_share"] = round(share, 2)
        claim_nums = numbers(r["claim"])
        r["numbers_not_in_quote"] = [n for n in claim_nums if not number_in(n, norm(r["quote"]))]
        r["numbers_not_in_source"] = [n for n in claim_nums if not number_in(n, text)]
        if verdict == "нет цитаты":
            r["status"] = "нет цитаты"
        elif verdict == "не найдена" and doi and not info.get("full_text"):
            r["status"] = "нет в аннотации, полный текст не прочитан"
        elif verdict == "не найдена":
            r["status"] = "цитата не найдена в источнике"
        elif r["numbers_not_in_source"] or r["numbers_not_in_quote"]:
            r["status"] = "число не подтверждено"
        else:
            r["status"] = "подтверждено" if verdict == "найдена" else "подтверждено частично"
        results.append(r)
    return results, cache


SECTIONS = [
    ("Подтверждено", {"подтверждено"}),
    ("Подтверждено частично — цитата найдена с расхождениями в словах", {"подтверждено частично"}),
    ("Число не подтверждено — число из утверждения нет в цитате или в источнике", {"число не подтверждено"}),
    ("Цитата не найдена в источнике", {"цитата не найдена в источнике"}),
    ("Нет в аннотации, полный текст не прочитан — сверить по полному тексту новой сессией",
     {"нет в аннотации, полный текст не прочитан"}),
    ("Источник не прочитан программой — сверить новой сессией", {"источник не прочитан"}),
    ("Число из файла — сверить новой сессией по сохранённому файлу", {"число из файла"}),
    ("DOI не существует", {"DOI не существует"}),
    ("Без источника или без цитаты", {"нет источника", "нет цитаты"}),
]


def report(results, cache, path):
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    total = len(results)
    ok = sum(1 for r in results if r["status"] == "подтверждено")
    lines = [f"# Проверка источников — {now}", "",
             f"Проверено программой `verify_sources.py`. Утверждений: {total}. Подтверждено полностью: {ok}.", "",
             "Подтверждено = цитата дословно найдена в тексте источника, и каждое число из утверждения есть и в цитате, и в источнике.", ""]
    for title, statuses in SECTIONS:
        rows = [r for r in results if r["status"] in statuses]
        lines.append(f"## {title} — {len(rows)}")
        lines.append("")
        if not rows:
            lines += ["нет", ""]
            continue
        for r in rows:
            lines.append(f"- **[{r['id']}]** {r['claim']}")
            if r.get("source"):
                lines.append(f"  - источник: {r['source']} · код ответа: {r.get('code')}")
            if r.get("data"):
                lines.append(f"  - данные: {r['data']}")
            if r.get("location"):
                lines.append(f"  - место: {r['location']}")
            if r.get("quote"):
                lines.append(f"  - цитата: «{r['quote'][:300]}» · поиск в источнике: {r.get('quote_check')} ({r.get('quote_share')})")
            if r.get("numbers_not_in_quote"):
                lines.append(f"  - числа из утверждения, которых нет в цитате: {', '.join(r['numbers_not_in_quote'])}")
            if r.get("numbers_not_in_source"):
                lines.append(f"  - числа из утверждения, которых нет в источнике: {', '.join(r['numbers_not_in_source'])}")
            for n in r.get("notes", []):
                lines.append(f"  - {n}")
        lines.append("")
    lines += ["## Источники", "", "| Источник | Код | Что прочитано |", "|---|---|---|"]
    for key, info in cache.items():
        title = f" — {info['title'][:80]}" if info.get("title") else ""
        lines.append(f"| {key}{title} | {info.get('code')} | {'; '.join(info.get('notes', [])) or 'текст страницы'} |")
    lines += ["", "Списки «не найдена» и «не прочитан» не значат «выдумано». Их сверяет новая сессия, которая сама открывает источник."]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    if len(sys.argv) < 2:
        print("Запуск: python verify_sources.py claims.json")
        sys.exit(2)
    src = pathlib.Path(sys.argv[1])
    claims = json.loads(src.read_text(encoding="utf-8"))
    if isinstance(claims, dict):
        claims = claims.get("claims", [])
    results, cache = check(claims)
    md = src.with_name("verification.md")
    report(results, cache, md)
    src.with_name("verification.json").write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    counts = {}
    for r in results:
        counts[r["status"]] = counts.get(r["status"], 0) + 1
    summary = ", ".join(f"{k}: {v}" for k, v in counts.items())
    sys.stdout.buffer.write(f"OK {md}\n{summary}\n".encode("utf-8"))


if __name__ == "__main__":
    main()
