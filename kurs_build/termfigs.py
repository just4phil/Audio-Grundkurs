# -*- coding: utf-8 -*-
"""Schematische SVG-Abbildungen für Fachbegriffe (Stecker, Mikrofone, …) + Link auf echtes Foto.
   Inline eingebettet -> Kurs bleibt offline; nur der Foto-Link braucht Internet."""

# --- SVG-Zeichnungen (schematisch, dunkles Theme) ---------------------------
_B = '#7fb4ff'   # blau
_G = '#27c2a0'   # grün
_O = '#ffcaa0'   # orange/pins
_M = '#c9d6e3'   # metall
_D = '#3a4654'   # dunkel

SVG = {
"xlr": (
 '<svg viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg">'
 '<circle cx="60" cy="58" r="44" fill="#10151c" stroke="%s" stroke-width="3"/>'
 '<circle cx="60" cy="58" r="34" fill="none" stroke="%s" stroke-width="1.5"/>'
 '<circle cx="60" cy="42" r="6" fill="%s"/><circle cx="46" cy="68" r="6" fill="%s"/>'
 '<circle cx="74" cy="68" r="6" fill="%s"/>'
 '<text x="60" y="34" fill="%s" font-size="8" text-anchor="middle">2</text>'
 '<rect x="52" y="100" width="16" height="18" rx="3" fill="%s"/>'
 '</svg>' % (_B,_D,_O,_O,_O,_M,_D)),

"klinke": (
 '<svg viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg">'
 '<rect x="8" y="50" width="40" height="20" rx="4" fill="%s"/>'
 '<rect x="48" y="54" width="46" height="12" fill="%s"/>'
 '<rect x="66" y="54" width="3.5" height="12" fill="#10151c"/>'
 '<rect x="80" y="54" width="3.5" height="12" fill="#10151c"/>'
 '<path d="M94 54 q14 6 0 12 z" fill="%s"/>'
 '<text x="60" y="92" fill="%s" font-size="11" text-anchor="middle">T R S</text>'
 '</svg>' % (_D,_M,_M,_M)),

"speakon": (
 '<svg viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg">'
 '<circle cx="60" cy="58" r="44" fill="#10151c" stroke="%s" stroke-width="3"/>'
 '<path d="M60 22 a36 36 0 0 1 30 18" fill="none" stroke="%s" stroke-width="4" stroke-linecap="round"/>'
 '<rect x="40" y="44" width="12" height="28" rx="3" fill="%s"/>'
 '<rect x="68" y="44" width="12" height="28" rx="3" fill="%s"/>'
 '<text x="60" y="100" fill="%s" font-size="10" text-anchor="middle">NL4 · Lock</text>'
 '</svg>' % (_B,_O,_M,_M,_M)),

"cinch": (
 '<svg viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg">'
 '<rect x="20" y="40" width="40" height="40" rx="6" fill="#b03a3a"/>'
 '<rect x="58" y="50" width="36" height="20" rx="3" fill="%s"/>'
 '<line x1="94" y1="60" x2="110" y2="60" stroke="%s" stroke-width="5" stroke-linecap="round"/>'
 '<text x="40" y="100" fill="%s" font-size="10" text-anchor="middle">RCA · L/R</text>'
 '</svg>' % (_M,_O,_M)),

"midi": (
 '<svg viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg">'
 '<circle cx="60" cy="58" r="44" fill="#10151c" stroke="%s" stroke-width="3"/>'
 '<path d="M30 58 a30 30 0 0 1 60 0" fill="none" stroke="%s" stroke-width="2"/>'
 '<circle cx="36" cy="62" r="4.5" fill="%s"/><circle cx="48" cy="44" r="4.5" fill="%s"/>'
 '<circle cx="60" cy="38" r="4.5" fill="%s"/><circle cx="72" cy="44" r="4.5" fill="%s"/>'
 '<circle cx="84" cy="62" r="4.5" fill="%s"/>'
 '<text x="60" y="104" fill="%s" font-size="10" text-anchor="middle">5-pol DIN</text>'
 '</svg>' % (_B,_D,_O,_O,_O,_O,_O,_M)),

"usb": (
 '<svg viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg">'
 '<rect x="34" y="30" width="52" height="60" rx="4" fill="#10151c" stroke="%s" stroke-width="3"/>'
 '<rect x="44" y="44" width="32" height="10" rx="2" fill="%s"/>'
 '<rect x="44" y="62" width="32" height="14" rx="2" fill="%s"/>'
 '<text x="60" y="108" fill="%s" font-size="10" text-anchor="middle">USB-A</text>'
 '</svg>' % (_B,_M,_D,_M)),

"mic_dyn": (
 '<svg viewBox="0 0 90 130" xmlns="http://www.w3.org/2000/svg">'
 '<circle cx="45" cy="32" r="26" fill="#1a2230" stroke="%s" stroke-width="2.5"/>'
 '<line x1="25" y1="24" x2="65" y2="24" stroke="%s" stroke-width="1.2"/>'
 '<line x1="22" y1="32" x2="68" y2="32" stroke="%s" stroke-width="1.2"/>'
 '<line x1="25" y1="40" x2="65" y2="40" stroke="%s" stroke-width="1.2"/>'
 '<line x1="38" y1="10" x2="38" y2="54" stroke="%s" stroke-width="1.2"/>'
 '<line x1="52" y1="10" x2="52" y2="54" stroke="%s" stroke-width="1.2"/>'
 '<rect x="30" y="54" width="30" height="66" rx="9" fill="#2a3340" stroke="%s" stroke-width="2.5"/>'
 '<rect x="32" y="74" width="26" height="3" fill="%s"/>'
 '</svg>' % (_B,_D,_D,_D,_D,_D,_B,_D)),

"sm58": (
 '<svg viewBox="0 0 90 130" xmlns="http://www.w3.org/2000/svg">'
 '<circle cx="45" cy="30" r="25" fill="#15324a" stroke="%s" stroke-width="2.5"/>'
 '<line x1="24" y1="30" x2="66" y2="30" stroke="%s" stroke-width="1.2"/>'
 '<line x1="27" y1="22" x2="63" y2="22" stroke="%s" stroke-width="1.2"/>'
 '<line x1="27" y1="38" x2="63" y2="38" stroke="%s" stroke-width="1.2"/>'
 '<rect x="31" y="52" width="28" height="64" rx="9" fill="#1b242f" stroke="%s" stroke-width="2.5"/>'
 '<text x="45" y="88" fill="%s" font-size="9" text-anchor="middle" font-weight="bold">SM58</text>'
 '</svg>' % (_G,_G,_G,_G,_M,_M)),

"mic_cond": (
 '<svg viewBox="0 0 90 130" xmlns="http://www.w3.org/2000/svg">'
 '<rect x="26" y="8" width="38" height="86" rx="16" fill="#2a3340" stroke="%s" stroke-width="2.5"/>'
 '<rect x="32" y="16" width="26" height="40" rx="11" fill="#10151c" stroke="%s" stroke-width="1.5"/>'
 '<line x1="36" y1="22" x2="36" y2="50" stroke="%s"/><line x1="42" y1="20" x2="42" y2="52" stroke="%s"/>'
 '<line x1="48" y1="20" x2="48" y2="52" stroke="%s"/><line x1="54" y1="22" x2="54" y2="50" stroke="%s"/>'
 '<rect x="38" y="94" width="14" height="28" fill="#2a3340" stroke="%s" stroke-width="2"/>'
 '</svg>' % (_G,_D,_D,_D,_D,_D,_G)),

"dibox": (
 '<svg viewBox="0 0 120 110" xmlns="http://www.w3.org/2000/svg">'
 '<rect x="24" y="24" width="72" height="62" rx="6" fill="#2a3340" stroke="%s" stroke-width="2.5"/>'
 '<circle cx="42" cy="44" r="6" fill="#10151c" stroke="%s"/>'
 '<circle cx="78" cy="44" r="6" fill="#10151c" stroke="%s"/>'
 '<rect x="52" y="60" width="16" height="9" rx="2" fill="%s"/>'
 '<text x="60" y="100" fill="%s" font-size="10" text-anchor="middle">DI · Ground-Lift</text>'
 '</svg>' % (_B,_O,_M,_O,_M)),

"wedge": (
 '<svg viewBox="0 0 130 100" xmlns="http://www.w3.org/2000/svg">'
 '<path d="M14 84 L40 30 L116 30 L116 84 Z" fill="#2a3340" stroke="%s" stroke-width="2.5"/>'
 '<circle cx="74" cy="58" r="20" fill="#10151c" stroke="%s" stroke-width="2"/>'
 '<circle cx="74" cy="58" r="9" fill="%s"/>'
 '<circle cx="48" cy="44" r="6" fill="#10151c" stroke="%s"/>'
 '</svg>' % (_B,_O,_D,_O)),

"iem": (
 '<svg viewBox="0 0 120 110" xmlns="http://www.w3.org/2000/svg">'
 '<path d="M70 30 a30 30 0 0 0 -30 40 q-4 12 8 14 q14 2 16 -12 a18 18 0 0 1 18 -22 q10 -2 6 -14 q-6 -8 -18 -6 z" '
 'fill="#2a3340" stroke="%s" stroke-width="2.5"/>'
 '<circle cx="52" cy="62" r="9" fill="%s"/>'
 '<path d="M86 32 q18 6 14 30" fill="none" stroke="%s" stroke-width="3" stroke-linecap="round"/>'
 '<text x="60" y="100" fill="%s" font-size="10" text-anchor="middle">In-Ear (IEM)</text>'
 '</svg>' % (_G,_O,_M,_M)),
}

# --- Name, Kurzbeschreibung, Link auf echtes Foto (Wikimedia Commons) -------
META = {
"xlr":     ("XLR-Stecker", "3-polig, symmetrisch – Standard für Mikrofone.",
            "https://commons.wikimedia.org/wiki/Category:XLR_connectors"),
"klinke":  ("Klinke (TS / TRS)", "6,3 mm „Jack“ – Instrumente (TS) & symmetrisch/Stereo (TRS).",
            "https://commons.wikimedia.org/wiki/Category:Phone_connectors_(audio)"),
"speakon": ("Speakon", "Verriegelbar & stromfest – Endstufe → Lautsprecher.",
            "https://commons.wikimedia.org/wiki/Category:Speakon_connectors"),
"cinch":   ("Cinch / RCA", "Unsymmetrisch, paarweise (rot/weiß) – Consumer & DJ.",
            "https://commons.wikimedia.org/wiki/Category:RCA_connectors"),
"midi":    ("MIDI (5-pol DIN)", "Überträgt Steuerdaten, keine Audiodaten.",
            "https://commons.wikimedia.org/wiki/Category:MIDI"),
"usb":     ("USB", "Digitale Verbindung – Audiointerface → Computer.",
            "https://commons.wikimedia.org/wiki/Category:USB_connectors"),
"mic_dyn": ("Dynamisches Mikrofon", "Robust, braucht keine Phantomspannung – Bühnen-Arbeitspferd.",
            "https://commons.wikimedia.org/wiki/Category:Dynamic_microphones"),
"sm58":    ("Shure SM58", "Das meistverkaufte Gesangsmikrofon – dynamisch, sehr robust.",
            "https://commons.wikimedia.org/wiki/Category:Shure_SM58"),
"mic_cond":("Kondensatormikrofon", "Empfindlich & detailreich, braucht +48 V – z. B. Overhead.",
            "https://commons.wikimedia.org/wiki/Category:Condenser_microphones"),
"dibox":   ("DI-Box", "Wandelt unsymmetrisch → symmetrisch; Ground-Lift gegen Brummen.",
            "https://commons.wikimedia.org/wiki/Category:DI_units"),
"wedge":   ("Monitor (Wedge)", "Keilförmiger Bühnenmonitor – zeigt zum Musiker.",
            "https://commons.wikimedia.org/wiki/Category:Stage_monitors"),
"iem":     ("In-Ear-Monitor", "Ohrhörer statt Wedge – keine Feedback-Gefahr.",
            "https://commons.wikimedia.org/wiki/Category:In-ear_monitors"),
}

# --- Platzierung: kapitel -> { überschrift-teilstring: [term-keys] } --------
TERMS = {
2: {"2.1 XLR": ["xlr"], "2.2 Klinke": ["klinke"], "2.3 Speakon": ["speakon"],
    "2.4 Cinch": ["cinch"], "2.5 MIDI": ["midi"], "2.6 USB": ["usb"]},
3: {"3.1 Dynamische": ["mic_dyn", "sm58"], "3.2 Kondensator": ["mic_cond"],
    "3.9 Mikrofonierung von Bass": ["dibox"]},
5: {"5.4 Monitorlautsprecher": ["wedge"], "5.5 In-Ear": ["iem"]},
}


def card(key):
    name, desc, url = META[key]
    return ('<div class="termcard"><div class="termsvg">%s</div>'
            '<div class="termmeta"><b>%s</b><span>%s</span>'
            '<a class="photo" href="%s" target="_blank" rel="noopener">📷 Echtes Foto ansehen ↗</a>'
            '</div></div>' % (SVG[key], name, desc, url))


def cards_html(keys):
    return '<div class="termcards">%s</div>' % "".join(card(k) for k in keys)
