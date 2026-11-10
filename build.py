#!/usr/bin/env python3
"""Baut aus regelbuch/*.md eine statische Website (nur relative Links).

Aufruf:  python build.py [Zielordner]      (Standard: _site)

Die Markdown-Dateien bleiben unverändert (Obsidian-Syntax). Umgewandelt werden
erst beim Build: Wiki-Links [[Seite#Anker|Text]]. Nicht auflösbare Links
(z. B. Kapitel, die noch nicht veröffentlicht sind) erscheinen als Text.
Alle Seiten liegen auf einer Ebene, alle Links sind relativ und funktionieren
daher unter jedem Unterpfad (GitHub-Pages-Projektseite).
"""
import html
import json
import re
import shutil
import sys
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "regelbuch"
SITE = ROOT / "site"
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "_site"

SITE_TITLE = "Nasus Nasus – Regelbuch"
FRONT_RE = re.compile(r"\A---\n(.*?)\n---\n", re.S)
WIKI_RE = re.compile(r"\[\[([^\]|#\n]*?)(#[^\]|\n]*?)?\\?(\|[^\]\n]*)?\]\]")
FENCE_RE = re.compile(r"^\s*(```|~~~)")
CODE_SPLIT = re.compile(r"(`[^`\n]+`)")
TERM_RE = re.compile(r"^\*\*(.+?)(?: \(|\.\*\*)")


def slug(value, sep="-"):
    s = re.sub(r"[^\w\- ]", "", value.strip().lower())
    return re.sub(r"[\s_-]+", sep, s)


def parse_front(text):
    m = FRONT_RE.match(text)
    meta = {}
    if not m:
        return meta, text
    for line in m.group(1).split("\n"):
        k, _, v = line.partition(":")
        v = v.strip()
        if k.strip() == "aliases":
            meta["aliases"] = [x.strip().strip("\"'") for x in v.strip("[]").split(",") if x.strip()]
        else:
            meta[k.strip()] = v.strip("\"'")
    return meta, text[m.end():]


def lines_with_fence_state(body):
    in_fence = False
    for line in body.split("\n"):
        if FENCE_RE.match(line):
            in_fence = not in_fence
            yield line, True
        else:
            yield line, in_fence


def main():
    nav = json.loads((SRC / "nav.json").read_text(encoding="utf-8"))
    order = [p for t in nav["parts"] for p in t["pages"]]
    pages = {}
    for stem in order:
        meta, body = parse_front((SRC / f"{stem}.md").read_text(encoding="utf-8"))
        meta.setdefault("title", stem)
        heads, terms = set(), {}
        for line, code in lines_with_fence_state(body):
            if code:
                continue
            h = re.match(r"^#{1,6}\s+(.*?)\s*#*\s*$", line)
            if h:
                heads.add(slug(h.group(1)))
        for line, code in lines_with_fence_state(body):
            t = None if code else TERM_RE.match(line)
            if t and slug(t.group(1)) not in heads:
                terms.setdefault(slug(t.group(1)), t.group(1))
        pages[stem] = {"meta": meta, "body": body, "heads": heads, "terms": terms}

    targets = {}
    for stem in order:
        targets.setdefault(stem.lower(), stem)
    for stem in order:
        targets.setdefault(pages[stem]["meta"]["title"].lower(), stem)
    for stem in order:
        for a in pages[stem]["meta"].get("aliases", []):
            targets.setdefault(a.lower(), stem)

    stats = {"links": 0, "offen": 0, "anker_ohne_treffer": 0}
    offen = {}

    def wiki(match, own):
        stats["links"] += 1
        ziel, anker, label = match.group(1).strip(), match.group(2), match.group(3)
        stem = targets.get(ziel.lower()) if ziel else own
        text = label[1:].strip() if label else (ziel or pages[own]["meta"]["title"])
        if stem is None:
            stats["offen"] += 1
            offen[ziel] = offen.get(ziel, 0) + 1
            return f'<span class="offen" title="Dieses Kapitel ist noch nicht veröffentlicht.">{html.escape(text)}</span>'
        href = f"{stem}.html"
        if anker:
            a = slug(anker[1:])
            if a in pages[stem]["heads"] or a in pages[stem]["terms"]:
                href += f"#{a}"
            else:
                stats["anker_ohne_treffer"] += 1
        return f"[{text}]({href})"

    md_html = {}
    for stem, p in pages.items():
        out = []
        for line, code in lines_with_fence_state(p["body"]):
            if code:
                out.append(line)
                continue
            parts = CODE_SPLIT.split(line)
            for i in range(0, len(parts), 2):
                parts[i] = WIKI_RE.sub(lambda m, s=stem: wiki(m, s), parts[i])
            line = "".join(parts)
            t = TERM_RE.match(line)
            if t and slug(t.group(1)) in p["terms"]:
                line = f'<a id="{slug(t.group(1))}"></a>' + line
            out.append(line)
        md = markdown.Markdown(
            extensions=["tables", "fenced_code", "toc", "nl2br"],
            extension_configs={"toc": {"slugify": slug, "toc_depth": "2-3"}},
        )
        body_html = md.convert("\n".join(out))
        body_html = body_html.replace("<table>", '<div class="tw"><table>').replace("</table>", "</table></div>")
        md_html[stem] = (body_html, md.toc_tokens)

    def nav_html(current):
        out = []
        for part in nav["parts"]:
            opened = " open" if current in part["pages"] else ""
            items = "".join(
                f'<li><a href="{s}.html"{" aria-current=page" if s == current else ""}>{html.escape(pages[s]["meta"]["title"])}</a></li>'
                for s in part["pages"]
            )
            out.append(f"<details{opened}><summary>{html.escape(part['title'])}</summary><ul>{items}</ul></details>")
        return "".join(out)

    shell = (SITE / "template.html").read_text(encoding="utf-8")

    def render(filename, title, content, current=None, pager=""):
        page = (shell.replace("{{TITLE}}", html.escape(title))
                .replace("{{SITE_TITLE}}", html.escape(SITE_TITLE))
                .replace("{{NAV}}", nav_html(current))
                .replace("{{CONTENT}}", content)
                .replace("{{PAGER}}", pager))
        (OUT / filename).write_text(page, encoding="utf-8", newline="\n")

    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    shutil.copy(SITE / "style.css", OUT / "style.css")
    if (SRC / "assets").is_dir():
        shutil.copytree(SRC / "assets", OUT / "assets")

    for i, stem in enumerate(order):
        meta = pages[stem]["meta"]
        badge = f'<p class="status">Status: {html.escape(meta["status"])}</p>' if meta.get("status") else ""
        prev_l = f'<a rel="prev" href="{order[i-1]}.html">← {html.escape(pages[order[i-1]]["meta"]["title"])}</a>' if i else "<span></span>"
        next_l = f'<a rel="next" href="{order[i+1]}.html">{html.escape(pages[order[i+1]]["meta"]["title"])} →</a>' if i + 1 < len(order) else "<span></span>"
        content = md_html[stem][0]
        content = re.sub(r"(</h1>)", r"\1" + badge, content, count=1) if "</h1>" in content else badge + content
        render(f"{stem}.html", f'{meta["title"]} – {SITE_TITLE}', content, stem, f'<nav class="pager" aria-label="Weiter">{prev_l}{next_l}</nav>')

    intro = [f"<h1>{html.escape(SITE_TITLE)}</h1>", "<p>Regelwerk für private Spielrunden. Der Text ist im Arbeitsstand; Kapitel mit dem Status „entwurf“ können sich noch ändern.</p>"]
    for part in nav["parts"]:
        intro.append(f"<h2>{html.escape(part['title'])}</h2><ul>")
        intro += [f'<li><a href="{s}.html">{html.escape(pages[s]["meta"]["title"])}</a></li>' for s in part["pages"]]
        intro.append("</ul>")
    render("index.html", SITE_TITLE, "\n".join(intro))

    rights = ROOT / "RIGHTS.md"
    if rights.exists():
        r = markdown.markdown(rights.read_text(encoding="utf-8"), extensions=["nl2br"])
        render("RIGHTS.html", f"Rechtevorbehalt – {SITE_TITLE}", r)

    # Selbsttest: alle internen Links und Anker müssen existieren.
    fehler = []
    ids = {}
    for f in OUT.glob("*.html"):
        ids[f.name] = set(re.findall(r'id="([^"]+)"', f.read_text(encoding="utf-8")))
    for f in OUT.glob("*.html"):
        for href in re.findall(r'href="([^"]+)"', f.read_text(encoding="utf-8")):
            if re.match(r"^(https?:|mailto:|#)", href):
                continue
            seite, _, anker = href.partition("#")
            if seite and not (OUT / seite).exists() or (anker and anker not in ids.get(seite or f.name, set())):
                fehler.append(f"{f.name}: {href}")
    if fehler:
        print("FEHLER: kaputte interne Links:", *fehler[:20], sep="\n  ", file=sys.stderr)
        sys.exit(1)

    print(f"Build ok: {len(order)} Kapitel, {stats['links']} Wiki-Links, "
          f"{stats['offen']} auf noch nicht veröffentlichte Kapitel (als Text), "
          f"{stats['anker_ohne_treffer']} Anker ohne Treffer (Link auf Seitenanfang)")
    if offen:
        print("Noch nicht veröffentlichte Ziele:", ", ".join(f"{k} ({v})" for k, v in sorted(offen.items())))


if __name__ == "__main__":
    main()
