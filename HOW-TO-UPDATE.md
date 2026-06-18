# 🛠️ Anleitung: Kurs aktualisieren & veröffentlichen

Diese Datei erklärt **vollständig**, wie du den interaktiven Tontechnik-Grundkurs änderst,
neu baust und online aktualisierst – auch wenn du länger nicht reingeschaut hast.

---

## 1. Wie funktioniert das Projekt? (Das Wichtigste zuerst)

Die fertigen HTML-Seiten im Ordner **`docs/`** sind **automatisch generiert** –
**du bearbeitest sie NICHT direkt!** (Änderungen dort würden beim nächsten Bauen überschrieben.)

Der Ablauf ist:

```
1. Quelldateien bearbeiten   (Markdown-Kapitel oder Dateien in kurs_build/)
2. Hochladen: git add / commit / push
3. → Eine GitHub Action baut den Kurs automatisch und veröffentlicht ihn.
```

> 💡 **Merksatz:** Markdown ändern → `git push` → fertig. Den Ordner `docs/` nie von Hand editieren.

**Du musst NICHT mehr selbst bauen.** Eine GitHub Action (`.github/workflows/deploy.yml`)
führt `python build_kurs.py` bei jedem Push automatisch in der Cloud aus und stellt das Ergebnis
online. Lokal `python build_kurs.py` zu laufen ist nur noch **optional** – nämlich dann, wenn du
Änderungen vorher im Browser ansehen willst (siehe Abschnitt 4).

---

## 2. Voraussetzungen (einmalig)

- **Python 3** muss installiert sein. Test im Terminal: `python --version`
  (zeigt z. B. `Python 3.9.6`). Es werden **keine Zusatzpakete** gebraucht.
- **Git** zum Hochladen. Test: `git --version`
- (Optional) **Node.js** – nur falls du JavaScript-Änderungen automatisch prüfen willst. Nicht nötig zum Bauen.

Es ist **kein** Internet, keine Datenbank und kein Server nötig – der Kurs läuft komplett offline
(nur die „📷 Echtes Foto ansehen“-Links zeigen ins Netz).

---

## 3. Projektstruktur

```
Audio-Grundkurs/
├─ Kapitel_01_*.md … Kapitel_16_*.md   ← INHALT der Kapitel (hier Text ändern)
├─ Best_Practices_Live_Mixing.md       ← Inhalt der Bonus-Seite
├─ inhaltsverzeichnis.md               ← (nur Quelle, wird nicht gebaut)
├─ Grafiken/                           ← große PNG-Abbildungen (Signalfluss etc.)
│
├─ build_kurs.py                       ← das Bau-Skript (startest du)
├─ kurs_build/                         ← Bausteine des Generators:
│   ├─ assets_css.py                   ← Design / Farben / Theme
│   ├─ assets_js.py                    ← Audio-Engine, Quiz-Logik, alle Widgets
│   ├─ mdconv.py                       ← wandelt Markdown → HTML (selten anzufassen)
│   ├─ content.py                      ← Kapitel-Liste, QUIZFRAGEN, Widget-Zuordnung
│   └─ termfigs.py                     ← SVG-Abbildungen + Foto-Links (XLR, SM58 …)
│
└─ docs/                               ← AUSGABE (generiert!) – das, was online geht
    ├─ index.html  (Startseite)
    ├─ kapitel-01.html … kapitel-16.html
    └─ best-practices.html
```

---

## 4. Bauen (immer gleich)

Im Projektordner ein Terminal öffnen und ausführen:

```bash
python build_kurs.py
```

Ausgabe sollte enden mit `Fertig: 16 Kapitel + Best Practices + Index.`
Danach liegen alle aktualisierten Dateien in **`docs/`**.

**Zum lokalen Anschauen** vor dem Hochladen: `docs/index.html` einfach im Browser öffnen
(Doppelklick). Tipp: vorher den Browser-Cache umgehen (Strg+F5), damit Änderungen sicher sichtbar sind.

---

## 5. Häufige Änderungen – Schritt für Schritt

### 5.1 Text eines Kapitels ändern
1. Die passende Datei `Kapitel_XX_*.md` öffnen und den Text bearbeiten (normales Markdown).
2. `python build_kurs.py` ausführen.
- Überschriften `## 4.2 …`, Tabellen `| … |`, Listen `- …`, Hinweisboxen mit `> 💡` bzw. `> ⚠️`
  werden automatisch ins richtige Design übersetzt.

### 5.2 Eine Quizfrage ändern oder hinzufügen
Datei: **`kurs_build/content.py`**, Abschnitt `QUIZ = { … }`. Jede Frage sieht so aus:

```python
{"q":"Deine Frage?",
 "o":["Antwort A","Antwort B","Antwort C","Antwort D"],
 "a":1,                       # Index der richtigen Antwort (0 = erste!)
 "e":"Kurze Erklärung, die nach dem Antworten erscheint."},
```
Neue Frage einfach als weiteren Eintrag in die Liste des Kapitels (`1: [ … ]`, `2: [ … ]` …) einfügen.

> ⚠️ **Wichtige Falle:** Für deutsche Anführungszeichen **immer „typografisch“** schreiben (`„…“`),
> **niemals** das gerade `"` – das gerade `"` beendet sonst den Python-Text und der Build bricht ab.
> Tipp: gar keine Anführungszeichen im Text verwenden, dann kann nichts schiefgehen.

### 5.3 Eine große Grafik (PNG) einbauen
1. Bild nach `Grafiken/` legen (z. B. `G4_1_kanalzug.png`).
2. In **`kurs_build/content.py`** im Block `IMAGES` eintragen, unter welcher Überschrift es erscheinen soll:
   ```python
   4: {"4.1 Aufbau eines Kanalzugs": ("G4_1_kanalzug.png", "Abb. 4.1 – Aufbau eines Kanalzugs")},
   ```
   (Der Text vor dem Doppelpunkt muss ein Stück der Kapitel-Überschrift sein.)
3. Bauen. Das PNG wird automatisch **als Base64 eingebettet** – bleibt also offline.

### 5.4 Eine Begriffs-Abbildung (SVG-Karte mit Foto-Link) hinzufügen
Datei: **`kurs_build/termfigs.py`**. Drei kleine Schritte:
1. **`SVG`**: eine neue Zeichnung als `"key": '<svg …>…</svg>'` ergänzen (oder eine bestehende kopieren).
2. **`META`**: `"key": ("Name", "Ein-Satz-Beschreibung", "https://commons.wikimedia.org/…")`.
3. **`TERMS`**: festlegen, in welchem Kapitel/unter welcher Überschrift die Karte erscheint, z. B.
   ```python
   4: {"4.1 Aufbau eines Kanalzugs": ["key"]},
   ```
4. Bauen.

### 5.5 Aussehen / Farben ändern
Datei: **`kurs_build/assets_css.py`**. Die Farben stehen oben unter `:root{ --bg … --accent … }`.
Einfach Werte anpassen und neu bauen.

### 5.6 Ein interaktives Widget ändern/ergänzen
- Die Bausteine (Frequenz-Explorer, Kanalzug, Kompressor … ) stehen in **`kurs_build/assets_js.py`**.
- Welche Widgets in welchem Kapitel erscheinen, steht in **`kurs_build/content.py`** unter `WIDGETS`.
- Das ist der technisch anspruchsvollste Teil – für reine Inhalts-Updates nicht nötig.

---

## 6. Veröffentlichen (Online-Update) – automatisch per GitHub Action

Du änderst nur die Quelle (z. B. ein `Kapitel_XX.md`) und lädst hoch:

```bash
git add -A
git commit -m "Kurs aktualisiert: <kurz was geändert wurde>"
git push
```

Danach läuft **automatisch** die GitHub Action `.github/workflows/deploy.yml`:
sie baut den Kurs (`python build_kurs.py`) in der Cloud und veröffentlicht ihn.
Fortschritt sichtbar unter **Repo → Reiter „Actions“**. Nach ~1–2 Minuten ist die neue Version live:

**https://just4phil.github.io/Audio-Grundkurs/**

> **Einmalige Einrichtung (nur beim allerersten Mal):**
> GitHub-Repo → **Settings → Pages** → unter **„Source“** **„GitHub Actions“** auswählen.
> (Vorher stand dort „Deploy from a branch /docs“ – das wird durch die Action ersetzt.)

> 💡 Du brauchst Python jetzt **nur noch lokal**, wenn du vor dem Push selbst eine Vorschau bauen willst.
> Für ein reines Inhalts-Update reicht: Markdown ändern → committen → pushen.

---

## 7. Schnell-Checkliste für ein Update

```
[ ] Quelle bearbeitet (Kapitel_XX.md  oder  Datei in kurs_build/)
[ ] (optional) python build_kurs.py + docs/index.html im Browser ansehen
[ ] git add -A
[ ] git commit -m "…"
[ ] git push
[ ] Repo → Reiter „Actions“: läuft grün durch?
[ ] ~1–2 Min warten, dann Live-Seite prüfen
```

---

## 8. Wenn etwas schiefgeht

| Problem | Ursache / Lösung |
|--------|------------------|
| Build bricht mit `SyntaxError` ab | Meist ein gerades `"` in `content.py`. Stattdessen `„…“` nutzen oder Anführungszeichen weglassen. |
| `python` nicht gefunden | Python 3 installieren bzw. stattdessen `py build_kurs.py` versuchen. |
| Änderung nicht sichtbar | Neu gebaut? Browser mit **Strg+F5** neu laden (Cache). Online: ~1 Min Wartezeit für GitHub Pages. |
| `docs/` fehlt nach Bau | Wird automatisch angelegt. Sicherstellen, dass `python build_kurs.py` ohne Fehler durchlief. |
| Bilder/Quiz weg auf der Live-Seite | Wurde `docs/` mit committet und gepusht? `git status` prüfen. |
| Foto-Link tot | Wikimedia-Kategorie wurde umbenannt – in `kurs_build/termfigs.py` (`META`) URL anpassen. |

---

*Kurz: **Quelle ändern → `python build_kurs.py` → `git push`.** Den Ordner `docs/` nie von Hand bearbeiten.*
