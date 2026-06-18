# Kapitel 4: Analoge Mischpulte

> **Das Herzstück der Tontechnik.**
> Das Mischpult ist das wichtigste Werkzeug des Tontechnikers. Hier läuft alles zusammen – alle Mikrofone, alle Instrumente. Du regelst, was das Publikum hört. In diesem Kapitel lernst du, jeden Regler zu verstehen.

---

## 4.1 Aufbau eines Kanalzugs

Ein analoges Mischpult besteht aus vielen identischen **Kanalzügen** (auch: Kanalstreifen). Jeder Kanal kann eine Signalquelle aufnehmen (z.B. ein Mikrofon). Alle Kanäle laufen am Ende in den **Master-Bus** zusammen.

### Der Weg durch einen Kanalzug (von oben nach unten):

```
┌─────────────────────────┐
│  EINGANG (XLR / Klinke) │  ← Hier steckst du Mikrofon oder Instrument ein
├─────────────────────────┤
│  GAIN (Preamp)          │  ← Wie empfindlich ist der Eingang?
├─────────────────────────┤
│  HIGH-PASS FILTER (HPF) │  ← Tiefe Störgeräusche ausblenden
├─────────────────────────┤
│  EQUALIZER (EQ)         │  ← Klangformung (Bässe, Mitten, Höhen)
├─────────────────────────┤
│  AUX-SENDS              │  ← Signal auf Monitore oder Effekte schicken
├─────────────────────────┤
│  PAN                    │  ← Links/Rechts-Position
├─────────────────────────┤
│  SOLO / MUTE            │  ← Kanal allein hören oder stumm schalten
├─────────────────────────┤
│  FADER                  │  ← Lautstärke des Kanals im Gesamtmix
└─────────────────────────┘
          ↓
     MASTER-BUS
```

Das Wichtigste: **Das Signal durchläuft alle diese Stufen von oben nach unten.** Ein Fehler am Anfang (z.B. falscher Gain) zieht sich durch alle folgenden Stufen.

---

## 4.2 Gain / Vorverstärkung

Der **Gain-Regler** (auch: Trim, Sensitivity, Preamp) ist der erste und wichtigste Regler in jedem Kanalzug. Er bestimmt, wie stark das eingehende Signal verstärkt wird.

### Warum ist Gain so wichtig?

Ein Mikrofonsignal ist extrem schwach (wenige Millivolt). Das Mischpult braucht ein stärkeres Signal, um damit zu arbeiten. Der Gain-Regler verstärkt das Mikrofonsignal auf **Line-Pegel**.

### Die goldene Regel: Gain Staging

Der Gain sollte so eingestellt sein, dass das Signal im Kanal **ausreichend stark, aber nicht übersteuert** ist.

**Pegelanzeige beim Soundcheck:**

- Spieler spielt normal, Gain so einstellen, dass die Pegelanzeige (Meter) im **grünen bis leicht orangen Bereich** ist
- Bei Spitzenpegeln (lauteste Stelle) sollte der Meter **nie in den roten Bereich** kommen

**Zu niedriger Gain:**
- Signal ist zu leise
- Du musst den Fader sehr weit aufziehen
- Signal-Rausch-Abstand verschlechtert sich (mehr Rauschen)

**Zu hoher Gain:**
- Signal clippt (verzerrt)
- Clipping klingt kratzig, unangenehm
- Alle nachfolgenden Stufen (EQ, Aux, Fader) verarbeiten ein schlechtes Signal

> 💡 **Merke:** "Garbage in, garbage out" – wenn das Signal schon am Gain-Regler verzerrt, kann kein EQ oder Effekt das reparieren.

### Wie stellst du den Gain ein?

1. Fader auf 0 dB (die markierte Nullposition auf dem Fader, meist ca. ¾ oben)
2. Bitte den Musiker, sein Instrument laut zu spielen (wie beim echten Konzert)
3. Drehe den Gain langsam hoch, bis der Pegel im grünen Bereich ist
4. Prüfe, ob bei Spitzenpegeln rot aufleuchtet – wenn ja, Gain etwas zurücknehmen

---

## 4.3 High Pass Filter (HPF)

Der **High Pass Filter** (HPF, auch: Tiefensperre, Low-Cut) ist ein Filter, der tiefe Frequenzen unterhalb einer bestimmten Grenzfrequenz abschneidet und hohe Frequenzen passieren lässt (daher: High Pass = Hochpassfilter = lässt Höhen durch).

### Wann nutze ich den HPF?

Aktiviere den HPF bei **fast jedem Kanal**, der kein Bassinstrument ist:

| Kanal | HPF aktivieren? | Grenzfrequenz (ca.) |
|-------|----------------|---------------------|
| Gesang | Ja | 80–120 Hz |
| Gitarrenamp | Ja | 80–100 Hz |
| Snare | Ja | 100–150 Hz |
| Hi-Hat | Ja | 200–400 Hz |
| Tom | Ja | 60–80 Hz |
| Overhead | Ja | 80–120 Hz |
| Bassgitarre | Nein / vorsichtig | – |
| Kick Drum | Nein | – |
| Keyboard (Bass-Range) | Nein | – |

### Warum ist der HPF so nützlich?

- **Trittschall und Körperschall:** Wenn jemand auf der Bühne läuft, überträgt sich das als tiefes Rumoren auf alle Mikrofone → HPF filtert das heraus
- **Wind und Atemgeräusche:** Bei Gesangsmikrofonen gibt es tiefes Rauschen durch Atemluft → HPF hilft
- **Klarheit im Mix:** Wenn alle Kanäle unnötige Bässe haben, wird der Gesamtmix matschig und überladen

> 💡 **Faustregel:** Schalte bei jedem Kanal den HPF an. Nur bei Bassinstrumenten bleibst du vorsichtig.

---

## 4.4 Equalizer (EQ)

Der **Equalizer** (EQ) ermöglicht es dir, bestimmte Frequenzbereiche zu verstärken (+) oder abzusenken (–). Das ist das mächtigste Werkzeug zur Klangformung.

### Arten von EQ-Bändern am Mischpult:

**High Shelf (Höhenregler):**
Verstärkt oder senkt **alle Frequenzen oberhalb** eines bestimmten Punktes.
- Typische Frequenz: 10–12 kHz
- +3 dB → mehr Brillanz, Luft
- –3 dB → dumpfer, weniger scharf

**Mid (Mitten):**
Verstärkt oder senkt einen **mittleren Frequenzbereich**. Oft mit einem zusätzlichen Frequenzwahlregler (parametrisch oder semi-parametrisch).
- Typische Frequenz: 1–4 kHz
- Sehr wichtig für Verständlichkeit von Gesang und Instrumenten

**Low Shelf (Bassregler):**
Verstärkt oder senkt **alle Frequenzen unterhalb** eines bestimmten Punktes.
- Typische Frequenz: 80–100 Hz
- +3 dB → mehr Wärme, mehr Druck
- –3 dB → schlankerer Klang

### Parametrischer EQ

Ein **parametrischer EQ** gibt dir drei Parameter für jedes Band:

1. **Frequenz (Hz):** Wo greifst du ein?
2. **Gain (dB):** Wie stark verstärkst/senkst du?
3. **Q (Güte/Bandwidth):** Wie breit oder eng ist der Eingriff?

- **Breite Q:** Sanfter, musikalischer Eingriff über viele Frequenzen
- **Schmale Q:** Chirurgischer Eingriff auf eine sehr spezifische Frequenz (gut zum Entfernen von Problemfrequenzen)

### Boost vs. Cut: Die wichtigste EQ-Regel

**Subtraktiver EQ ist besser als additiver EQ:**

- Senke lieber ab, als zu boosten
- Wenn etwas fehlt, liegt es oft daran, dass etwas anderes zu viel ist
- Zu viele Boosts können das Signal übersteuern und klingen unnatürlich

> 💡 **Merkregel:** "If in doubt, cut." – Im Zweifel: senken statt boosten.

### Typische EQ-Eingriffe beim Live-Sound:

| Problem | Eingriff |
|---------|---------|
| Gesang klingt dumpf | +2–3 dB bei 2–4 kHz |
| Zu viel "Matsch" im Mix | –3 dB bei 200–400 Hz |
| Kick drum fehlt Punch | +3 dB bei 80 Hz, +2 dB bei 4–5 kHz |
| Gitarre sticht zu sehr | –3 dB bei 3–4 kHz |
| Zu viel Rauschen/Zischen | –3 dB bei 8–12 kHz |
| Feedback-Frequenz | Schmaler Cut an der Feedback-Frequenz |

---

## 4.5 Aux-Wege

**Aux-Wege** (Auxiliary) sind zusätzliche Ausgänge, die unabhängig vom Hauptmix geregelt werden. Sie haben zwei Hauptverwendungen:

### 1. Monitor-Mixes (Bühnenmonitore)

Die Musiker auf der Bühne brauchen ihren eigenen Mix, damit sie sich hören können. Jeder Aux-Weg kann einen eigenen Monitor-Mix steuern.

- **Aux 1:** Monitor für Sänger → viel Gesang, etwas Gitarre, wenig Drums
- **Aux 2:** Monitor für Gitarrist → seine Gitarre, etwas Bass, Schlagzeug
- **Aux 3:** Monitor für Schlagzeuger → Bassdrum-Klick, Gesang, Bass

Jeder Kanal hat für jeden Aux-Weg einen kleinen Regler (Aux-Send). Du regelst damit, wie viel von diesem Kanal auf diesem Monitor-Mix landet.

### 2. Effektwege (FX-Send)

Aux-Wege können auch auf Effektgeräte (Hall, Delay) geschickt werden.

- Signal geht raus aus dem Mischpult → ins Effektgerät → zurück in einen Kanal des Mischpults
- Typisch: Aux 5 → Hallgerät → Rückgabe auf Kanal 31/32

### Pre-Fader vs. Post-Fader

Ein wichtiger Unterschied bei Aux-Sends:

- **Pre-Fader:** Das Signal auf dem Aux-Weg ist **unabhängig vom Fader** des Kanals. Wenn du den Fader runterzieht, ändert sich der Monitor-Mix nicht. Das willst du für **Monitorwege** – der Musiker hört sich immer gleich, egal was du im FOH-Mix machst.

- **Post-Fader:** Das Signal auf dem Aux-Weg ist **abhängig vom Fader**. Wenn du den Kanal leiser machst, wird auch der Aux-Send leiser. Das willst du für **Effektwege** – wenn du ein Instrument leiser machst, soll auch der Hall dazu leiser werden.

> ⚠️ **Wichtig:** Monitorwege immer auf **Pre-Fader** einstellen. Effektwege auf **Post-Fader**.

---

## 4.6 Panorama (Pan)

Der **Pan-Regler** (Panorama) bestimmt die Position des Kanals im Stereobild.

- **Linksanschlag (L):** Signal nur im linken Lautsprecher
- **Mitte (C):** Signal gleichmäßig in beiden Lautsprechern
- **Rechtsanschlag (R):** Signal nur im rechten Lautsprecher

### Typische Panoramapositionen beim Live-Band-Mix:

| Instrument | Pan |
|-----------|-----|
| Kick Drum | Mitte |
| Snare | Mitte |
| Bassgitarre | Mitte |
| Lead-Gesang | Mitte |
| Hi-Hat | Leicht links (10–11 Uhr) |
| Tom 1 | Leicht links |
| Tom 2 | Leicht rechts |
| Floor Tom | Rechts |
| Gitarre 1 | Links (9 Uhr) |
| Gitarre 2 | Rechts (3 Uhr) |
| Keyboard | Etwas links, etwas rechts |

### Warum Bässe in die Mitte?

Tiefe Frequenzen sind kaum richtbar – das Gehör kann nicht genau lokalisieren, woher tiefe Töne kommen. Bässe in der Mitte sorgen für ein stabiles, ausgeglichenes Fundament.

> 💡 **Tipp:** Beim Live-Sound ist die Pan-Nutzung oft konservativer als im Studio. Wenn das Publikum weit links steht, hört es sonst nur die linke Seite des Mixes.

---

## 4.7 Mute & Solo / PFL

### Mute

Der **Mute-Button** schaltet einen Kanal **stumm** – das Signal wird unterbrochen und geht nicht mehr in den Master-Bus.

**Wann nützlich:**

- Ein Instrument pausiert → Kanal muten, damit kein Rauschen oder Nebengeräusche durchkommen
- Feedback-Notfall → Kanal sofort muten
- Aufbau- und Umbauphase → Kein Mikrofon ohne Musiker offen lassen

> ⚠️ **Falle:** Vergiss nicht, den Kanal wieder zu un-muten, wenn der Musiker wieder spielt!

### Solo / PFL (Pre-Fader Listen)

Der **Solo-Button** oder **PFL-Button** schickt den Kanal auf den **Kopfhörerausgang** des Mischpults – du kannst diesen Kanal isoliert abhören, ohne dass der Hauptmix beeinflusst wird.

**PFL (Pre-Fader Listen):**
Du hörst das Signal **vor dem Fader** – ideal zum Einstellen des Gains und Überprüfen des Kanals.

**AFL (After-Fader Listen):**
Du hörst das Signal **nach dem Fader** – so wie es im Mix ist.

**Wann nutze ich Solo?**

- Einen bestimmten Kanal überprüfen (Kabel check, Klang check)
- Gain einstellen ohne störende andere Kanäle
- Feedback-Frequenz orten

> ⚠️ **Achtung:** Solo/PFL beeinflusst nicht den Master-Ausgang – das Publikum hört weiter den normalen Mix. Aber manche Pulte haben einen "Solo in Place"-Modus, der den Master beeinflusst. Kenne dein Mischpult!

---

## 4.8 Fader

Der **Fader** ist der große Schieberegler am unteren Ende des Kanalzugs. Er regelt die Lautstärke des Kanals **im Hauptmix**.

### Nullposition (0 dB)

Die **0-dB-Position** (oft mit einer Markierung oder "U" für Unity) ist der ideale Arbeitspunkt. Wenn du alle Gain-Stages richtig eingestellt hast, sollte der Fader meistens in der Nähe dieser Position sein.

```
      +10
       +5
        0  ← Nullposition (Unity)
       -5
      -10
      -20
      -∞  (unten = kein Ton)
```

### Wie benutze ich den Fader?

- **Soundcheck:** Fader auf 0 dB stellen, dann den Gain einstellen
- **Mixphase:** Fader bewegen, um relative Lautstärke zu regeln
- **Feine Korrekturen:** Meist nur wenige dB rauf oder runter

### Fader vs. Gain – der Unterschied:

| | Gain | Fader |
|--|------|-------|
| Position im Signalfluss | Ganz oben (erster Regler) | Ganz unten (letzter Regler) |
| Funktion | Grundpegel / Eingangsempfindlichkeit | Lautstärke im Mix |
| Wann einstellen? | Beim Soundcheck, einmalig | Während des Mixes, laufend |
| Beeinflusst Aux-Sends? | Ja (alle) | Nur Post-Fader Auxe |

---

## 4.9 Gruppen & Busse

### Was ist ein Bus?

Ein **Bus** ist eine Sammelleitung, auf die mehrere Kanäle gleichzeitig geroutet werden können.

**Master-Bus (L/R):** Alle Kanäle landen im Master-Bus und gehen als Gesamtmix aus dem Mischpult raus.

### Gruppen-Busse (Subgruppen)

Manche Mischpulte haben **Gruppen** (Subgruppen, Groups). Du kannst mehrere Kanäle auf eine Gruppe routen und dann die Gruppe als Ganzes regeln.

**Beispiel: Schlagzeug-Gruppe**

Statt alle Drum-Kanäle einzeln zu regeln, routest du sie auf Gruppe 1. Jetzt kannst du mit einem einzigen Fader das komplette Schlagzeug lauter oder leiser machen.

```
Kick  ──┐
Snare ──┤
Tom 1 ──┤→ GRUPPE 1 (Drums) → Master L/R
Tom 2 ──┤
OH L  ──┤
OH R  ──┘
```

**Typische Gruppen:**

| Gruppe | Kanäle |
|--------|--------|
| Gruppe 1 | Alle Drums |
| Gruppe 2 | Alle Vocals |
| Gruppe 3 | Alle Gitarren |
| Gruppe 4 | Bass |

**Vorteil:** Wenn der Schlagzeuger zu laut spielt, drückst du nur einen Fader (Gruppe 1) statt 6 einzelne Drum-Fader.

### Master-Bus

Der **Master-Fader** regelt die Gesamtlautstärke des Hauptmixes. Er sollte **immer** auf 0 dB stehen. Du regelst die Lautstärke mit den einzelnen Kanälen, nicht mit dem Master-Fader.

> 💡 **Ausnahme:** Wenn du beim Konzert schnell leiser werden musst (z.B. Pause, Moderationsansage), kannst du kurz den Master-Fader drücken.

---

## 4.10 Gain Staging

**Gain Staging** ist das gezielte Einstellen aller Pegel in der Signalkette, damit das Signal immer im optimalen Bereich ist – weder zu laut (Clipping) noch zu leise (Rauschen).

### Das Konzept der Pegeltreppe

Stell dir vor, das Signal muss eine Treppe hinuntergehen. Bei jedem Schritt (Gerät, Stufe im Signalfluss) gibt es einen idealen Pegel. Wenn du überall richtig einstellst, läuft das Signal glatt die Treppe hinunter.

```
Mikrofonsignal (sehr leise)
        ↓ GAIN (anhebt auf Line-Level)
EQ / Compressor (sollte nicht übergesteuert sein)
        ↓ Fader (verfeinert den Pegel)
Master-Bus (soll ebenfalls gut ausgesteuert sein)
        ↓ Master-Fader (auf 0 dB)
Endstufe (sollte voll ausgesteuert werden)
        ↓
Lautsprecher
```

### Richtwerte:

- **Eingangs-Pegelanzeige (Kanalzug):** Spitzenpegel sollte –6 bis –3 dBFS (digital) oder "gelb" (analog) sein
- **Master-Bus:** Sollte ebenfalls nicht in den roten Bereich kommen, –6 dBFS oder weniger
- **Aux-Master:** Je nach Endstufe – oft bis zum grünen/gelben Bereich aussteuern

### Schritt-für-Schritt: Gain Staging beim Soundcheck

1. **Alle Fader auf 0 dB** (Nullposition)
2. **Alle Gain-Regler auf Minimum** (links anschlag oder ganz runter)
3. **Musiker spielen** wie im Konzert (laut, normal)
4. **Gain langsam hochdrehen** bis Pegelanzeige grün bis leicht orange zeigt
5. **Alle Kanäle so einstellen**, dann den Gesamtmix mit den Fadern formen
6. **Master-Fader** prüfen: Läuft er auch nicht in den roten Bereich?

### Typische Gain-Staging-Fehler:

| Fehler | Folge |
|--------|-------|
| Gain zu hoch | Kanal clippt, Verzerrung |
| Gain zu niedrig, Fader hochgezogen | Rauschen, schlechter Klang |
| Master zu weit oben | Endstufe wird übersteuert |
| Endstufe zu laut eingestellt | System clippt am Ende der Kette |

> 💡 **Goldene Regel:** Starte immer von oben (Gain) und arbeite dich nach unten (Fader, Master). Nicht umgekehrt.

---

## Zusammenfassung Kapitel 4

**Der Weg durch den Kanalzug:**

```
Eingang → Gain → HPF → EQ → Aux-Send → Pan → Mute/Solo → Fader → Master
```

**Die wichtigsten Merksätze:**

- **Gain** bestimmt den Grundpegel – er muss als erstes richtig eingestellt werden
- **HPF** immer anschalten – außer bei Bassinstrumenten
- **EQ:** Erst subtraktiv (senken), dann additiv (boosten) – weniger ist mehr
- **Aux Pre-Fader** für Monitore, **Aux Post-Fader** für Effekte
- **Pan:** Bässe in die Mitte, Instrumente links/rechts verteilen
- **Mute** ist dein Freund – unnötige offene Mikrofone schließen
- **Fader auf 0 dB** als Ausgangspunkt, dann feinjustieren
- **Gain Staging** = sicherstellen, dass das Signal überall im optimalen Bereich ist

---

*Weiter geht es in Kapitel 5: Lautsprecher & Monitoring*
