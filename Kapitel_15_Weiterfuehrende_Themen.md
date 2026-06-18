# Kapitel 15: Weiterführende Themen

> **Wenn du die Grundlagen wirklich beherrschst.**
> Dieses Kapitel gibt dir einen Ausblick auf Themen, die über den normalen Band-Tontechniker-Job hinausgehen. Du musst das nicht sofort verstehen – aber es zeigt dir, in welche Richtungen sich Audiotechnik entwickelt.

---

## 15.1 Studioakustik

**Raumakustik** im Studio ist eine eigene Wissenschaft. Ohne akustisch behandelten Raum klingt jede Aufnahme anders als geplant.

### Warum ist Raumakustik wichtig?

Schall reflektiert an Wänden, Boden und Decke. In einem unbehandelten Raum entstehen:

- **Frühe Reflexionen:** Der direkte Schall und sein Echo kommen fast gleichzeitig an → klingt verwaschen
- **Stehende Wellen (Raummoden):** Bestimmte Frequenzen werden durch Raumgeometrie sehr stark verstärkt oder ausgelöscht → bestimmte Töne klingen viel lauter oder leiser als sie sind
- **Nachhall (Reverberation):** Zu viel Nachhall macht Aufnahmen unklar

### Akustische Behandlung:

| Maßnahme | Funktion |
|---------|---------|
| **Absorber** (Schaumstoff, Mineral-wolle) | Schlucken Schall, reduzieren Nachhall |
| **Diffusoren** (unregelmäßige Oberflächen) | Streuen Schall, vermeiden Reflexionen ohne den Raum "tot" klingen zu lassen |
| **Bassfallen** (Bass Traps) | Große Absorber für tiefe Frequenzen in Raumecken |

**Ein weit verbreiteter Irrtum:** Eierkartons behandeln Raumakustik effektiv. Sie absorbieren nur sehr hohe Frequenzen minimal – und sind als Akustikbehandlung nahezu wirkungslos.

### Reflexionspunkte:

Die wichtigsten Stellen, die akustisch behandelt werden sollten:
- **Seitenwände** auf Ohrhöhe (erste Reflexionen von den Lautsprechern)
- **Decke** zwischen Lautsprechern und Hörposition
- **Hintere Wand** hinter dem Hörplatz
- **Ecken** (für Bassfallen)

---

## 15.2 Raumakustik bei Liveveranstaltungen

Jeder Raum ist anders. Eine wichtige Fähigkeit von Profi-Tontechnikern ist es, einen Raum schnell zu "lesen" und den Mix entsprechend anzupassen.

### Wie beeinflusst der Raum den Sound?

**Große, hallende Räume (Kirchen, Hallen):**
- Sehr langer Nachhall (RT60 > 2 Sekunden)
- Bass häuft sich an
- Sprache/Musik klingt verwaschen
- Lösung: Wenig bis kein künstlicher Hall, viel HPF, langsames Tempo bevorzugen

**Kleine, trockene Räume (Proberäume, kleine Clubs):**
- Kurzer Nachhall
- Bässe häufen sich in Ecken
- Reflexionen von nahen Wänden
- Lösung: Etwas mehr Hall kann helfen, um Natürlichkeit zu erzeugen

**Freigelände:**
- Kein Nachhall
- Schall verteilt sich nach allen Seiten → PA muss lauter sein
- Wind kann Schall ablenken
- Lösung: Mehr PA-Leistung, keine künstlichen Raumeffekte nötig

### Einmessen eines PA-Systems:

Professionelle Tontechniker nutzen **Room Measurement Software** (z.B. Smaart, REW) mit einem Messmikrofon, um den Raum akustisch zu analysieren und die PA per DSP anzupassen.

---

## 15.3 Lautheitsnormen

**Lautstärke** ist nicht nur eine Frage des persönlichen Geschmacks – es gibt gesetzliche Regelungen und Industrie-Standards.

### Warum Lautheitsnormen?

Früher gab es im Radio und Streaming einen "Lautheits-Krieg": Jeder wollte lauter klingen als der andere. Das Ergebnis war komprimierter, ermüdender Sound.

Moderne Plattformen (Spotify, YouTube, Apple Music) normalisieren die Lautstärke auf einen Zielwert. Zu laute Tracks werden leiser abgespielt.

### LUFS – Loudness Units Full Scale:

**LUFS** (Loudness Units relative to Full Scale) ist die Maßeinheit für wahrgenommene Lautstärke, nicht nur Spitzenpegel.

Zielwerte verschiedener Plattformen:

| Plattform | Zielwert |
|-----------|---------|
| Spotify | –14 LUFS |
| Apple Music | –16 LUFS |
| YouTube | –14 LUFS |
| CD | –9 bis –6 LUFS (sehr laut) |
| Film | –23 LUFS |

### Für Live-Sound:

Bei Live-Veranstaltungen gibt es oft **Lautstärkebegrenzungen** (SPL-Limits) durch den Veranstalter oder Behörden:

- Typisch in Deutschland: 85–100 dB(A) gemessen am FOH-Platz oder an definierten Messpunkten
- Als Tontechniker musst du innerhalb dieser Grenzen bleiben
- Manchmal gibt es automatische Limiter-Systeme, die eingreifen wenn der Grenzwert überschritten wird

---

## 15.4 Broadcast-Audio

**Broadcast** bedeutet: Audio für Fernseher, Radio oder Live-Streaming. Das ist eine eigene Welt mit eigenen Anforderungen.

### Unterschiede zu normalem Live-Sound:

| Merkmal | Live-Sound | Broadcast |
|---------|-----------|---------|
| Zielgruppe | Anwesende | Zuschauer/Zuhörer zuhause |
| Lautheit | Flexibel | Normiert (–23 LUFS für TV) |
| Sprach-verständlichkeit | Wichtig | Kritisch |
| Dynamik | Groß möglich | Kontrolliert und komprimiert |
| Hörumgebung | Konzertsaal | Wohnzimmer, Kopfhörer, TV-Lautsprecher |

### Broadcast-Mix vs. FOH-Mix:

Beim Live-Konzert für TV oder Streaming wird oft ein **separater Broadcast-Mix** erstellt:

- Weniger Hall (klingt auf TV-Lautsprechern sonst matschig)
- Mehr Kompression (dynamischer TV-Lautsprecher ist begrenzt)
- Mehr Verständlichkeit des Gesangs
- Normiert auf Broadcast-Lautstärkewerte

---

## 15.5 Immersive Audio

**Immersive Audio** (auch: 3D-Audio, Spatial Audio) ist die nächste Entwicklung in der Audiotechnik. Statt Stereo (links/rechts) gibt es einen dreidimensionalen Klangraum.

### Formate:

- **Dolby Atmos:** Film-Standard, auch für Musik. Objekte können im 3D-Raum platziert werden.
- **Sony 360 Reality Audio:** Für Musik-Streaming
- **Ambisonics:** Für VR und 360°-Video

### In der Live-Technik:

- **L-ISA (L-Acoustics):** System für immersiven Live-Sound mit vielen Lautsprechern
- **d&b Soundscape:** Ähnliches System für immersive Live-Beschallung
- **Meyer Sound LEOPARD mit Spacemap Go:** Weitere Lösung

### Grundprinzip:

Statt zwei Lautsprecher (links/rechts) gibt es viele Lautsprecher um das Publikum herum – vorne, seitlich, hinten, über dem Publikum. Instrumente können im Raum bewegt werden.

Für die meisten kleinen Bands und Venues ist das noch Zukunftsmusik – aber in großen Venues und Events ist Immersive Audio bereits Standard.

---

## 15.6 Zukunft der Audiotechnik

Die Audiotechnik entwickelt sich schnell. Ein Blick, wohin die Reise geht:

### KI und Machine Learning in Audio:

**Automatische Mischsysteme:**
Es gibt bereits KI-basierte Systeme (z.B. Wizdom Music JamOrigin, Soundcraft Notepad-Serie mit Auto-Mix), die automatisch Kanäle muten und Pegel anpassen. Der menschliche Tontechniker wird zunächst ergänzt, nicht ersetzt.

**KI-basiertes Mastering:**
Tools wie LANDR oder iZotope Ozone nutzen KI, um Mischungen automatisch zu mastern. Gut als Ausgangspunkt, aber kein Ersatz für menschliches Urteilsvermögen.

**Noise Suppression:**
KI kann Hintergrundgeräusche in Echtzeit entfernen – nützlich für Sprache in Konferenzschaltungen (z.B. NVIDIA RTX Voice).

### Remote Monitoring und Fernwartung:

Digitale Systeme können über das Internet überwacht werden. Ein Techniker in einer anderen Stadt kann das System eines Live-Gigs überwachen.

### Netzwerk-Audio (DANTE, AVB, AES67):

Immer mehr Systeme kommunizieren über Ethernet. Die Grenze zwischen IT und Audiotechnik verschwimmt. Tontechniker der Zukunft müssen auch Netzwerk-Grundkenntnisse haben.

### Kleinere, leistungsfähigere Hardware:

Digitale Mischpulte werden kleiner, leichter und günstiger – und klingen dabei besser als früher teure Profi-Geräte. Ein iPad kann ein vollständiges Mischpult sein.

### Was bleibt?

Trotz aller Technologie: Das Gehör, das Urteilsvermögen und die Fähigkeit, mit Menschen umzugehen – das bleibt die wichtigste Qualität eines Tontechnikers. Kein Algorithmus kann entscheiden, was in einer bestimmten Situation gut klingt.

---

## Zusammenfassung Kapitel 15

- **Studioakustik:** Absorbtion, Diffusion und Bassfallen für einen korrekten Abhörraum
- **Raumakustik Live:** Jeder Raum ist anders – lerne, einen Raum schnell zu "lesen"
- **Lautheitsnormen:** LUFS als Messeinheit; Streaming-Plattformen normalisieren Lautstärke
- **Broadcast:** Separater Mix für TV/Radio/Streaming mit anderen Anforderungen als FOH
- **Immersive Audio:** 3D-Audio mit vielen Lautsprechern – Zukunft im professionellen Live-Bereich
- **Zukunft:** KI, Netzwerk-Audio, kleinere Hardware – aber das Gehör und der Mensch bleiben entscheidend

---

*Weiter geht es in Kapitel 16: Eigene Notizen & Erfahrungswerte*
