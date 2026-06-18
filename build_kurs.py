# -*- coding: utf-8 -*-
"""Generator für den interaktiven Tontechnik-Grundkurs.
   Erzeugt self-contained HTML-Dateien (CSS+JS inline, Grafiken als Base64) in Kurs_HTML/.
   Aufruf:  python build_kurs.py
"""
import os
import sys
import json
import base64

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "kurs_build"))

from assets_css import CSS              # noqa: E402
from assets_js import JS                # noqa: E402
from mdconv import convert              # noqa: E402
from content import CHAPTERS, GROUPS, IMAGES, WIDGETS, QUIZ  # noqa: E402
import termfigs  # noqa: E402

SRC = HERE
GFX = os.path.join(SRC, "Grafiken")
OUT = os.path.join(SRC, "Kurs_HTML")

# ---------------------------------------------------------------- helpers
def read(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def write(path, text):
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

_IMG_CACHE = {}
def data_uri(filename):
    if filename not in _IMG_CACHE:
        with open(os.path.join(GFX, filename), "rb") as f:
            b64 = base64.b64encode(f.read()).decode("ascii")
        _IMG_CACHE[filename] = "data:image/png;base64," + b64
    return _IMG_CACHE[filename]

def _figure_html(fname, caption):
    return ('<figure><img src="%s" alt="%s" loading="lazy"><figcaption>%s</figcaption></figure>'
            % (data_uri(fname), caption.replace('"', "&quot;"), caption))

def build_after_map(num):
    """Kombiniert große Grafiken (PNG) und Term-Karten (SVG) je Überschrift."""
    out = {}
    for key, (fname, caption) in IMAGES.get(num, {}).items():
        out[key] = _figure_html(fname, caption)
    for key, keys in termfigs.TERMS.get(num, {}).items():
        block = termfigs.cards_html(keys)
        out[key] = (out[key] + block) if key in out else block
    return out

# ---------------------------------------------------------------- templates
def page(title, num_label, body, *, widgets="", quiz_json=None, quiz_key="",
         nav="", body_class="", crumb=None, footer=None):
    quiz_block = ""
    quiz_tail = ""
    if quiz_json is not None:
        quiz_block = (
            '<section class="quiz"><h2>📝 Prüfungsfragen</h2>'
            '<p class="qmeta">Beantworte alle Fragen – du bekommst sofort Feedback mit Erklärung. '
            'Dein Ergebnis wird gespeichert und in der Kurs-Übersicht angezeigt.</p>'
            '<div id="quiz-cards"></div></section>'
        )
        quiz_tail = ('<script>window.QUIZ=%s;window.QUIZ_KEY=%s;</script>'
                     % (json.dumps(quiz_json, ensure_ascii=False), json.dumps(quiz_key)))
    crumb_html = ('<span class="crumb">%s</span>' % crumb) if crumb else ""
    foot = footer or ("Ausbildung Tontechniker · interaktiver Grundkurs")
    html = (
        "<!DOCTYPE html>\n<html lang=\"de\"><head>\n"
        "<meta charset=\"utf-8\">\n"
        "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">\n"
        "<title>%TITLE%</title>\n"
        "<style>%CSS%</style>\n</head>\n"
        "<body class=\"%BODYCLASS%\">\n"
        "<header class=\"topbar\">\n"
        " <a class=\"home\" href=\"index.html\">🎚️ Kurs-Übersicht</a>\n"
        " %CRUMB%\n <span class=\"spacer\"></span>\n"
        " <button id=\"audioStop\" class=\"btn warnstop\" disabled title=\"Alle Töne sofort stoppen\">🔇 Ton stoppen</button>\n"
        "</header>\n"
        "<main>\n%BODY%\n%WIDGETS%\n%QUIZ%\n%NAV%\n</main>\n"
        "<footer>%FOOT%</footer>\n"
        "<script>%JS%</script>\n%QUIZTAIL%\n"
        "</body></html>\n"
    )
    repl = {
        "%TITLE%": title, "%CSS%": CSS, "%JS%": JS, "%BODY%": body,
        "%WIDGETS%": widgets, "%QUIZ%": quiz_block, "%QUIZTAIL%": quiz_tail,
        "%NAV%": nav, "%BODYCLASS%": body_class, "%CRUMB%": crumb_html, "%FOOT%": foot,
    }
    for k, v in repl.items():
        html = html.replace(k, v)
    return html

def chapter_nav(idx):
    """idx = position in CHAPTERS (0-based)."""
    parts = []
    if idx > 0:
        p = CHAPTERS[idx - 1]
        parts.append('<a class="prev" href="%s"><span class="dir">← Vorheriges Kapitel</span>'
                     '<span class="ttl">%d. %s</span></a>' % (p[2], p[0], p[3]))
    else:
        parts.append('<a class="prev disabled"><span class="dir">Start</span><span class="ttl">—</span></a>')
    if idx < len(CHAPTERS) - 1:
        n = CHAPTERS[idx + 1]
        parts.append('<a class="next" href="%s"><span class="dir">Nächstes Kapitel →</span>'
                     '<span class="ttl">%d. %s</span></a>' % (n[2], n[0], n[3]))
    else:
        parts.append('<a class="next" href="best-practices.html"><span class="dir">Bonus →</span>'
                     '<span class="ttl">Best Practices Spickzettel</span></a>')
    return "".join(parts)

# ---------------------------------------------------------------- build chapters
def build_chapters():
    for idx, (num, mdfile, outfile, short, icon, desc, grp) in enumerate(CHAPTERS):
        md = read(os.path.join(SRC, mdfile))
        title, body = convert(md, page_id="kap%d" % num, after_heading=build_after_map(num))
        title = title or short
        full_body = '<h1>%s %s</h1>\n%s' % (icon, _escape(title.split(":", 1)[-1].strip() if ":" in title else title), body)
        html = page(
            "%s · Tontechnik-Grundkurs" % title,
            num, full_body,
            widgets=WIDGETS.get(num, ""),
            quiz_json=QUIZ.get(num),
            quiz_key="tt_quiz_%d" % num,
            nav='<nav class="chapnav">%s</nav>' % chapter_nav(idx),
            crumb="Kapitel %d / 16 · %s" % (num, short),
            footer="Ausbildung Tontechniker · Kapitel %d von 16 · %s" % (num, short),
        )
        write(os.path.join(OUT, outfile), html)
        print("  ✓ %s" % outfile)

def _escape(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

# ---------------------------------------------------------------- best practices
def build_best_practices():
    md = read(os.path.join(SRC, "Best_Practices_Live_Mixing.md"))
    title, body = convert(md, page_id="bp", after_heading={})
    title = title or "Best Practices: Live Mixing"
    full_body = '<h1>🧾 %s</h1>\n%s' % (_escape(title), body)
    nav = ('<nav class="chapnav">'
           '<a class="prev" href="kapitel-16.html"><span class="dir">← Zurück</span>'
           '<span class="ttl">16. Eigene Notizen</span></a>'
           '<a class="next" href="index.html"><span class="dir">→</span>'
           '<span class="ttl">Zur Kurs-Übersicht</span></a></nav>')
    html = page("Best Practices · Tontechnik-Grundkurs",
                "Bonus", full_body, nav=nav,
                crumb="Bonus · Spickzettel",
                footer="Ausbildung Tontechniker · Bonus: Best-Practices-Spickzettel")
    write(os.path.join(OUT, "best-practices.html"), html)
    print("  ✓ best-practices.html")

# ---------------------------------------------------------------- index hub
def build_index():
    cards_by_group = {g: [] for g, _ in GROUPS}
    for (num, mdfile, outfile, short, icon, desc, grp) in CHAPTERS:
        cards_by_group[grp].append(
            '<a class="card" href="%s" data-quizkey="tt_quiz_%d">'
            '<span class="knum">Kapitel %d</span>'
            '<span class="kicon">%s</span>'
            '<span class="ktitle">%s</span>'
            '<span class="kdesc">%s</span>'
            '<span class="kstatus todo">○ noch offen</span></a>'
            % (outfile, num, num, icon, _escape(short), _escape(desc))
        )
    sections = []
    for g, label in GROUPS:
        sections.append('<div class="sectionhead">%s</div>' % label)
        sections.append('<div class="hubgrid">%s</div>' % "".join(cards_by_group[g]))
    # bonus card
    sections.append('<div class="sectionhead">Bonus</div>')
    sections.append('<div class="hubgrid">'
                    '<a class="card bonus" href="best-practices.html">'
                    '<span class="knum">Spickzettel</span><span class="kicon">🧾</span>'
                    '<span class="ktitle">Best Practices: Live Mixing</span>'
                    '<span class="kdesc">Bewährte Startwerte für EQ, Kompressor, Gates, Reverb, Pan & Monitor.</span>'
                    '<span class="kstatus todo">Nachschlagewerk</span></a></div>')

    body = (
        '<section class="hero">'
        '<h1>🎚️ Ausbildung Tontechniker</h1>'
        '<p class="sub">Dein interaktiver Grundkurs – Schritt für Schritt vom analogen Handwerk '
        'in die digitale Welt. Mit echtem Ton zum Ausprobieren und Quiz am Ende jedes Kapitels.</p>'
        '<div class="progresswrap" id="hubbar"><span></span><em>Fortschritt wird geladen …</em></div>'
        '</section>'
        + "".join(sections) +
        '<div class="tools">'
        '<a class="btn primary" href="kapitel-01.html">▶ Mit Kapitel 1 starten</a>'
        '<button class="btn" onclick="resetProgress()">↺ Fortschritt zurücksetzen</button>'
        '</div>'
    )
    html = page("Ausbildung Tontechniker · Interaktiver Grundkurs",
                None, body, body_class="hub",
                footer="Interaktiver Grundkurs · läuft komplett offline · Fortschritt wird lokal im Browser gespeichert")
    # Hub braucht keine Topbar-Crumb/Home-Link auf sich selbst -> entferne Home-Link doppelung nicht nötig
    write(os.path.join(OUT, "index.html"), html)
    print("  ✓ index.html")

# ---------------------------------------------------------------- main
def main():
    if not os.path.isdir(OUT):
        os.makedirs(OUT)
    print("Baue Kurs nach %s" % OUT)
    build_chapters()
    build_best_practices()
    build_index()
    print("Fertig: %d Kapitel + Best Practices + Index." % len(CHAPTERS))

if __name__ == "__main__":
    main()
