# Best Practices: Live Mixing

> **Dieses Dokument ist dein Spickzettel.**
> Hier findest du bewährte Startwerte und Grundmuster, die bei fast jedem Gig funktionieren. Sie sind kein Gesetz – aber ein zuverlässiger Ausgangspunkt. Von dort aus hörst du und passt an.

---

## 1. Der goldene Workflow – immer in dieser Reihenfolge

```
1. Aufbau & Einschalten (Lautsprecher immer zuletzt!)
2. Line Check (kommt Signal auf jedem Kanal an?)
3. Gain Staging (Kanal für Kanal, lauteste Stelle)
4. HPF aktivieren (auf allen Nicht-Bass-Kanälen)
5. Monitor-Mix (ZUERST – Musiker müssen sich hören)
6. EQ grob (nur was wirklich stört)
7. Kompressoren (wo nötig, sanft)
8. FOH-Mix Balance aufbauen (von unten: Kick → Bass → Rest → Vocals)
9. Feintuning: EQ, Effekte, Details
10. Konzert – aufmerksam bleiben und reagieren
```

> **Merke:** Schritt 5 (Monitor) vor Schritt 8 (FOH). Zufriedene Musiker spielen besser. Das ist dein bester FOH-Mix-Helfer.

---

## 2. Gain Staging – Grundregel

| Signal | Ziel-Pegelanzeige |
|--------|-----------------|
| Eingangskanal (bei lautester Stelle) | Gelb, kurz orange – NIE dauerhaft rot |
| Aux-Ausgänge | Grün bis gelb |
| Master L/R | –6 bis –3 dBFS (nicht in den Rot-Bereich) |
| Endstufe / Aktive Box | So, dass bei Vollaussteuerung des Mischpults kein Clip entsteht |

**Faustregel:** Fader auf 0 dB stellen, dann den Gain so wählen, dass der Pegel stimmt. Den Fader danach zum Feinmischen nutzen.

---

## 3. HPF (High-Pass-Filter / Low-Cut) – wann und wo

**Aktiviere den HPF auf JEDEM Kanal, der kein Bassinstrument ist.** Das ist die einfachste und wirkungsvollste Maßnahme gegen einen matschigen Mix.

| Kanal | HPF aktivieren? | Empfohlene Grenzfrequenz |
|-------|---------------|--------------------------|
| Kick Drum | Nein | – |
| Snare | Ja | 80–120 Hz |
| Hi-Hat | Ja | 200–400 Hz |
| Tom | Ja | 60–80 Hz |
| Overhead | Ja | 80–120 Hz |
| Bassgitarre | Nein / sehr tief | evtl. 40 Hz (Sub-Rumpel) |
| E-Gitarre | Ja | 80–100 Hz |
| Akustikgitarre | Ja | 100–120 Hz |
| Keyboard (Bass-Lage) | Nein | – |
| Keyboard (Pad, Lead) | Ja | 80–150 Hz |
| Gesang | Ja | 80–120 Hz |
| Sprache / Moderation | Ja | 120–150 Hz |

> **Warum?** Tiefe Frequenzen aus Mikrofonen kommen meist von Trittschall, Bühnenvibrationen, Atemluft und dem Nahbesprechungseffekt – nicht von der eigentlichen Schallquelle. Der HPF filtert genau diesen Müll heraus.

---

## 4. EQ – Startwerte und typische Eingriffe

### Grundsatz: Erst hören, dann eingreifen. Subtraktiv vor additiv.

Wenn der Sound ohne EQ-Eingriff gut klingt – lass die Finger weg.

### Gesang:

| Problem | Eingriff |
|---------|---------|
| Dumpf, undeutlich | +2–3 dB bei 2–4 kHz (Präsenz) |
| Nasal, "durch die Nase" | –2–3 dB bei 500–800 Hz |
| Zu scharf, aggressiv | –2–3 dB bei 3–5 kHz |
| Zischende S-Laute | De-Esser oder –3 dB (schmal) bei 7–9 kHz |
| Zu viel Körper/Wärme | –2–3 dB bei 200–300 Hz |
| Plosive (P/B-Knacken) | HPF höher ansetzen (bis 150 Hz) |

**Typischer Gesangs-EQ-Start:**
- HPF: 100 Hz
- Low-Mid: –2 dB bei 300 Hz (Boxigkeit reduzieren)
- Mid: +2 dB bei 3 kHz (Verständlichkeit)
- High Shelf: +1–2 dB bei 10 kHz (Luft)

---

### Kick Drum:

| Ziel | Eingriff |
|------|---------|
| Mehr Punch / Fundament | +3–4 dB bei 80–100 Hz |
| Mehr Anschlag / "Klick" | +2–3 dB bei 4–6 kHz |
| Weniger Matsch | –3 dB bei 200–400 Hz |
| Weniger Dröhnen | –3 dB bei 500–800 Hz |

**Typischer Kick-EQ-Start:**
- HPF: 40–60 Hz (Sub-Rumpel weg)
- +3 dB bei 80 Hz (Punch)
- –3 dB bei 300 Hz (Matsch weg)
- +3 dB bei 5 kHz (Klick/Anschlag)

---

### Snare:

| Ziel | Eingriff |
|------|---------|
| Mehr Körper / Dicke | +3 dB bei 150–200 Hz |
| Mehr Crack | +3 dB bei 5–8 kHz |
| Schnarrteppich betonen | +2 dB bei 5–8 kHz |
| Weniger Näseln | –3 dB bei 400–600 Hz |

**Typischer Snare-EQ-Start:**
- HPF: 100 Hz
- +2 dB bei 200 Hz (Körper)
- –2 dB bei 400 Hz (Boxigkeit)
- +3 dB bei 6 kHz (Crack)

---

### E-Gitarre:

| Ziel | Eingriff |
|------|---------|
| Mehr Wärme | +2 dB bei 150–200 Hz |
| Weniger Matsch | –3 dB bei 200–400 Hz |
| Mehr Präsenz / Durchsetzung | +2 dB bei 2–3 kHz |
| Weniger scharf | –2 dB bei 3–5 kHz |

**Typischer Gitarren-EQ-Start:**
- HPF: 80–100 Hz
- –2 dB bei 300 Hz (Matsch weg)
- +2 dB bei 2,5 kHz (Präsenz)

---

### Bassgitarre (DI):

| Ziel | Eingriff |
|------|---------|
| Mehr Fundament | +3 dB bei 80–100 Hz |
| Mehr Anschlag / Knurren | +2–3 dB bei 700 Hz – 1 kHz |
| Weniger Dröhnen | –3 dB bei 200–400 Hz |

**Typischer Bass-EQ-Start:**
- HPF: 40 Hz (Sub-Rumpel)
- +2 dB bei 80 Hz (Fundament)
- –2 dB bei 250 Hz (Matsch)
- +2 dB bei 800 Hz (Knurren / Definition)

---

## 5. Kompressor – Startwerte nach Instrument

**Grundsatz:** Komprimiere nur, wenn es ein echtes Problem gibt (zu viel Dynamik, unkontrollierte Peaks). Nicht auf jedem Kanal ist ein Kompressor nötig.

| Instrument | Ratio | Threshold | Attack | Release | GR-Ziel |
|-----------|-------|-----------|--------|---------|---------|
| Gesang | 3:1–4:1 | –20 bis –15 dBFS | 10–20 ms | 60–100 ms | –3 bis –6 dB |
| Bassgitarre | 4:1–6:1 | –20 bis –15 dBFS | 20–40 ms | 80–150 ms | –4 bis –8 dB |
| Kick Drum | 4:1–6:1 | –15 bis –10 dBFS | 30–50 ms (langsam!) | 80–150 ms | –3 bis –6 dB |
| Snare | 4:1 | –15 dBFS | 5–15 ms | 60–100 ms | –3 bis –5 dB |
| Akustikgitarre | 3:1–4:1 | –18 dBFS | 15–30 ms | 80 ms | –3 bis –4 dB |
| E-Gitarre | Meist kein Kompressor | – | – | – | – |
| Overhead | 2:1–3:1 (sanft) | –20 dBFS | 30–50 ms | 100–200 ms | –2 bis –3 dB |
| Master-Bus | 2:1 | –6 bis –3 dBFS | 30–50 ms | Auto | –1 bis –2 dB |

### Entscheidungshilfe: Brauche ich hier einen Kompressor?

```
Klingt das Instrument sehr ungleichmäßig laut?
        │
       JA → Kompressor sinnvoll
        │
       NEIN → Finger weg, lieber nichts tun
```

### Attack-Faustregel:

- **Langsamer Attack** (30–50 ms): Transiente kommt durch → mehr Punch → gut für Drums
- **Schneller Attack** (1–10 ms): Transiente wird abgefangen → gleichmäßiger → gut für Vocals

---

## 6. Gate – Startwerte

Gates werden hauptsächlich auf Schlagzeug verwendet.

| Instrument | Threshold | Attack | Hold | Release |
|-----------|-----------|--------|------|---------|
| Kick | –30 bis –20 dBFS | 1 ms | 200–400 ms | 100 ms |
| Snare | –25 bis –15 dBFS | 1–2 ms | 150–300 ms | 80–100 ms |
| Tom 1 | –30 bis –20 dBFS | 1 ms | 200–300 ms | 80 ms |
| Tom 2 | –30 bis –20 dBFS | 1 ms | 200–300 ms | 80 ms |

**Tipp:** Lieber Threshold etwas tiefer setzen, damit keine Schläge abgehackt werden. Range auf –30 bis –40 dB statt –∞, damit es natürlicher klingt.

---

## 7. Reverb – Startwerte und Regeln

### Die wichtigste Reverb-Regel:

> **Weniger ist mehr. Im Zweifel: halbiere die Reverb-Menge.**

Live-Räume hallen bereits von Natur aus. Zusätzlicher künstlicher Hall macht den Mix schnell undurchsichtig.

### Standardeinstellungen Gesangs-Reverb (Live):

| Parameter | Empfehlung |
|-----------|-----------|
| Typ | Room oder Short Hall |
| Pre-Delay | 20–40 ms (trennt Direktsignal vom Nachhall) |
| Decay / RT60 | 0,8–1,5 Sekunden |
| Diffusion | 50–70% |
| Dry/Wet | 15–25% Wet (als Send/Return: Aux-Return auf –15 bis –10 dB) |
| HPF im Reverb | 150–200 Hz (Bässe aus dem Hall heraushalten) |

**Warum Pre-Delay?** Mit einem Pre-Delay von 20–40 ms hörst du erst den trockenen Direktsound (klar, verständlich), dann erst den Nachhall. Ohne Pre-Delay "verschmieren" Direktsignal und Hall ineinander.

### Typische Reverb-Typen und ihr Einsatz:

| Reverb-Typ | Klingt wie | Passt zu |
|-----------|-----------|---------|
| Room | Kleiner Raum, kurz (0,3–0,8 s) | Drums, Snare, natürlicher Klang |
| Hall (Concert Hall) | Große Halle, lang (1,5–3 s) | Gesang (sparingly!), Streicher |
| Plate | Metallische Platte, mittellang (1–2 s) | Snare, klassischer Pop-Gesang |
| Spring | Federhall, charakteristisch | Gitarre (Vintage-Sound) |

### Reverb als Send, nicht als Insert:

Reverb gehört auf einen **Aux-Weg (Send/Return)**, nicht als Insert direkt in den Kanal:

```
Kanal → Aux-Send (Post-Fader) → Reverb-Gerät / Plugin → Return-Kanal
```

So kannst du von jedem Kanal individuell bestimmen, wie viel Reverb er bekommt – statt das Reverb auf jeden Kanal separat einzustecken.

---

## 8. Delay – Startwerte

Delay kommt im Live-Sound hauptsächlich auf Gesang (für Tiefe) oder als atmosphärischer Effekt.

| Parameter | Empfehlung |
|-----------|-----------|
| Typ | Tape Delay oder Digital Delay |
| Zeit | Im Takt des Songs (Quarter Note oder Eighth Note) |
| Feedback | 15–30% (2–4 Echos, dann ausblenden) |
| Dry/Wet | 10–20% Wet |
| HPF im Delay | 200 Hz (dumpfere Echos klingen natürlicher) |

### Delay-Zeit im Takt berechnen:

```
Delay (ms) = 60.000 ÷ BPM
```

Beispiel: Song mit 120 BPM → 60.000 ÷ 120 = **500 ms** (Quarter Note Delay)
- Half Note: 1000 ms
- Eighth Note: 250 ms
- Dotted Eighth Note: 375 ms (sehr beliebt für atmosphärischen Sound)

---

## 9. Panorama – Standardverteilung

| Instrument | Pan-Position |
|-----------|-------------|
| Kick Drum | Mitte (12 Uhr) |
| Snare | Mitte |
| Hi-Hat | 10–11 Uhr (leicht links) |
| Tom 1 | 10 Uhr |
| Tom 2 | 2 Uhr |
| Floor Tom | 3 Uhr |
| Overhead L | 9 Uhr |
| Overhead R | 3 Uhr |
| Bassgitarre | Mitte |
| Lead Gesang | Mitte |
| Backing Vocal L | 9–10 Uhr |
| Backing Vocal R | 2–3 Uhr |
| Gitarre 1 | 9 Uhr |
| Gitarre 2 | 3 Uhr |
| Keyboard L | 9 Uhr |
| Keyboard R | 3 Uhr |

**Merke:** Bässe (Kick, Snare, Bass, Lead Vocal) immer in die Mitte. Sie bilden das Fundament – das muss stabil und zentriert sein.

---

## 10. Monitor-Mix – Best Practices

### Grundsatz: Jeder Musiker bekommt seinen eigenen Mix.

| Musiker | Was er meistens braucht |
|---------|----------------------|
| Sänger | Viel eigener Gesang, etwas Gitarre, Kick und Snare zum Zeitgefühl |
| Gitarrist | Seine eigene Gitarre klar, Lead-Gesang, Kick |
| Bassist | Kick Drum stark, seinen Bass (etwas tiefer im Pegel), Gesang |
| Schlagzeuger | Klick-Track (falls vorhanden), Bassgitarre, Gesang – meist kein eigenes Schlagzeug nötig |
| Keyboarder | Seinen Sound, Gesang, Bass und Kick |

### Grundeinstellungen für Monitor-Aux:

- **Pre-Fader:** Immer! (Musiker-Mix unabhängig vom FOH-Mix)
- **HPF am Aux-Ausgang:** 100–120 Hz (weniger Feedback-Risiko, mehr Klarheit)
- **Grafik-EQ am Monitor-Weg:** Feedback-Frequenzen kontrolliert herausnehmen
- **Grundlautstärke:** So leise wie möglich, damit Musiker sich hören können – nicht lauter

### Feedback in Monitoren vermeiden:

1. Aux-Send-Pegel möglichst niedrig halten
2. HPF auf dem Kanal und am Aux-Ausgang aktivieren
3. Monitor nicht direkt auf das Mikrofon gerichtet
4. Gain des Kanals nicht zu hoch
5. Feedback-Frequenzen am Grafik-EQ herausnehmen (Ringing Out)

---

## 11. Checkliste: Schnell-Soundcheck (unter 15 Minuten)

```
□ PA läuft, alle Lautsprecher aktiv
□ Alle Kanäle: HPF an, Gain auf Minimum, Fader auf 0 dB
□ Line Check: Kanal für Kanal solieren, Signal vorhanden?

□ Kick → Gain, HPF, EQ grob
□ Snare → Gain, HPF, EQ grob
□ Bass → Gain, HPF, EQ grob
□ Gitarre → Gain, HPF, EQ grob
□ Gesang → Gain, HPF, EQ grob

□ Monitor-Mix: Jeder Musiker einmal fragen "Kannst du dich hören?"
□ Grober FOH-Mix: Balance zwischen allen Instrumenten

□ Kompressoren (falls nötig): Gesang, Bass
□ Reverb: Gesang, Snare – sparsam

□ Nochmal Gesamtmix abhören, letzte Korrekturen
□ Go!
```

---

## 12. Häufige Probleme und sofortige Lösung

| Problem | Erste Maßnahme |
|---------|--------------|
| Kein Ton auf einem Kanal | Mute? Gain? Kabel? Phantom? |
| Mix klingt matschig | HPF auf allen Nicht-Bass-Kanälen aktivieren |
| Feedback | Gain des Kanals runter, dann Ursache suchen |
| Gesang zu leise im Mix | Fader hoch, dann Gain prüfen, dann EQ (2–4 kHz) |
| Bass überwältigt alles | HPF auf anderen Kanälen, Bass-Fader reduzieren |
| Schlagzeug klingt flach | Gate prüfen, EQ (Kick: 80 Hz + 5 kHz; Snare: 200 Hz + 6 kHz) |
| Zu viel Brummen (50/100 Hz) | Masseschleife: Ground-Lift an DI-Box |
| Mix klingt verwaschen | Reverb reduzieren (oder ausschalten zum Test) |
| Alles klingt gleich laut / flach | Zu viel Kompression, Ratio/Threshold zurücknehmen |
| Zischende S-Laute | De-Esser oder –3 dB schmal bei 7–9 kHz |

---

> **Das wichtigste Werkzeug bist du – deine Ohren und deine Ruhe. Technik und Startwerte sind der Ausgangspunkt. Was du hörst, ist das Ziel.**

---

*Verwandt: Kapitel 4 (Mischpult), Kapitel 6 (Hören lernen), Kapitel 7 (Live-Mixing), Kapitel 8 (EQ & Dynamik)*
