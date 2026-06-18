# -*- coding: utf-8 -*-
"""Schlanker Markdown->HTML-Konverter für die Kurs-Kapitel (keine externen Abhängigkeiten).
   Unterstützt: Überschriften, Absätze, **fett**/*kursiv*/`code`, Tabellen (GFM),
   Codeblöcke (```), Blockquotes inkl. 💡/⚠️-Callouts, Listen, Checklisten (- [ ]), ---."""
import re
import html as _html


def _inline(text):
    text = _html.escape(text, quote=False)
    # inline code
    codes = []
    def _c(m):
        codes.append(m.group(1))
        return "\x00%d\x00" % (len(codes) - 1)
    text = re.sub(r"`([^`]+)`", _c, text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", text)
    text = re.sub(r"\x00(\d+)\x00", lambda m: "<code>%s</code>" % _html.escape(codes[int(m.group(1))], quote=False), text)
    return text


def _table(rows):
    # rows: list of raw "| a | b |" lines (header, sep, body...)
    def cells(line):
        line = line.strip()
        if line.startswith("|"):
            line = line[1:]
        if line.endswith("|"):
            line = line[:-1]
        return [c.strip() for c in line.split("|")]
    header = cells(rows[0])
    body = [cells(r) for r in rows[2:]]
    out = ['<div class="tablewrap"><table><thead><tr>']
    out += ["<th>%s</th>" % _inline(h) for h in header]
    out.append("</tr></thead><tbody>")
    for r in body:
        out.append("<tr>" + "".join("<td>%s</td>" % _inline(c) for c in r) + "</tr>")
    out.append("</tbody></table></div>")
    return "".join(out)


def convert(md, page_id="p", image_map=None, drop_first_h1=True):
    """image_map: dict {heading_substring: (data_uri, caption)} -> figure nach passender Überschrift."""
    image_map = dict(image_map or {})
    lines = md.replace("\r\n", "\n").split("\n")
    html_out = []
    title = None
    chk_counter = [0]
    i = 0
    n = len(lines)

    def emit_image_for(heading_text):
        for key in list(image_map.keys()):
            if key.lower() in heading_text.lower():
                uri, cap = image_map.pop(key)
                html_out.append(
                    '<figure><img src="%s" alt="%s" loading="lazy">'
                    '<figcaption>%s</figcaption></figure>' % (uri, _html.escape(cap, quote=True), _inline(cap))
                )

    while i < n:
        line = lines[i]
        striped = line.strip()

        # skip trailing nav italics like *Weiter geht es...* / *Ende...*
        if re.match(r"^\*(Weiter geht es|Ende des|Verwandt:)", striped):
            i += 1
            continue

        # fenced code
        if striped.startswith("```"):
            buf = []
            i += 1
            while i < n and not lines[i].strip().startswith("```"):
                buf.append(lines[i])
                i += 1
            i += 1  # closing fence
            html_out.append('<pre class="ascii"><code>%s</code></pre>'
                            % _html.escape("\n".join(buf), quote=False))
            continue

        # headings
        m = re.match(r"^(#{1,4})\s+(.*)$", striped)
        if m:
            level = len(m.group(1))
            txt = m.group(2).strip()
            if level == 1:
                if title is None and drop_first_h1:
                    title = txt
                    i += 1
                    continue
                html_out.append("<h1>%s</h1>" % _inline(txt))
            else:
                html_out.append("<h%d>%s</h%d>" % (level, _inline(txt), level))
                emit_image_for(txt)
            i += 1
            continue

        # horizontal rule
        if re.match(r"^---+$", striped):
            html_out.append("<hr>")
            i += 1
            continue

        # table (current line has |, next line is separator)
        if "|" in striped and i + 1 < n and re.match(r"^\s*\|?[\s:|-]*-[-\s:|]*\|?\s*$", lines[i + 1]) and "|" in lines[i + 1]:
            rows = []
            while i < n and "|" in lines[i] and lines[i].strip():
                rows.append(lines[i])
                i += 1
            html_out.append(_table(rows))
            continue

        # blockquote
        if striped.startswith(">"):
            buf = []
            while i < n and lines[i].strip().startswith(">"):
                buf.append(re.sub(r"^\s*>\s?", "", lines[i]))
                i += 1
            content = "\n".join(buf).strip()
            cls = "note"
            if content.startswith("💡"):
                cls = "tip"
            elif content.startswith("⚠️") or content.startswith("⚠"):
                cls = "warn"
            paras = [p for p in re.split(r"\n\s*\n", content) if p.strip()]
            inner = "".join("<p>%s</p>" % _inline(p.replace("\n", " ")) for p in paras)
            html_out.append('<div class="callout %s">%s</div>' % (cls, inner))
            continue

        # checklist / unordered list
        if re.match(r"^[-*]\s+", striped):
            is_check = bool(re.match(r"^[-*]\s+\[[ xX]\]", striped))
            items = []
            while i < n and re.match(r"^\s*[-*]\s+", lines[i]):
                raw = re.sub(r"^\s*[-*]\s+", "", lines[i])
                cm = re.match(r"^\[([ xX])\]\s*(.*)$", raw)
                if cm:
                    checked = cm.group(1).lower() == "x"
                    chk_counter[0] += 1
                    items.append(
                        '<li class="%s"><label><input type="checkbox" data-persist="%s_%d"%s> %s</label></li>'
                        % ("done" if checked else "", page_id, chk_counter[0],
                           " checked" if checked else "", _inline(cm.group(2)))
                    )
                else:
                    items.append("<li>%s</li>" % _inline(raw))
                i += 1
            tag = '<ul class="checklist">' if is_check else "<ul>"
            html_out.append(tag + "".join(items) + "</ul>")
            continue

        # ordered list
        if re.match(r"^\d+\.\s+", striped):
            items = []
            while i < n and re.match(r"^\s*\d+\.\s+", lines[i]):
                items.append("<li>%s</li>" % _inline(re.sub(r"^\s*\d+\.\s+", "", lines[i])))
                i += 1
            html_out.append("<ol>" + "".join(items) + "</ol>")
            continue

        # blank line
        if not striped:
            i += 1
            continue

        # paragraph (gather until blank / block start)
        buf = [striped]
        i += 1
        while i < n:
            nxt = lines[i].strip()
            if (not nxt or nxt.startswith(("#", ">", "```", "- ", "* ", "|"))
                    or re.match(r"^\d+\.\s+", nxt) or re.match(r"^---+$", nxt)):
                break
            buf.append(nxt)
            i += 1
        html_out.append("<p>%s</p>" % _inline(" ".join(buf)))

    return title, "\n".join(html_out)
