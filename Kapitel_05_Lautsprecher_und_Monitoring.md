# Kapitel 5: Lautsprecher & Monitoring

> **Warum ist das wichtig?**
> Du kannst den besten Mix am Pult haben – wenn das Lautsprechersystem schlecht eingestellt ist oder die Musiker sich auf der Bühne nicht hören können, scheitert das Konzert. Lautsprecher und Monitoring sind das Ende der Signalkette. Hier kommt die Arbeit heraus.

---

## 5.1 PA-Systeme

**PA** steht für *Public Address* – also das Beschallungssystem, das das Publikum beschallt. Ein PA-System besteht aus Lautsprechern, Endstufen, und oft auch Signalprozessoren.

### Aufgabe des PA-Systems

Das PA-System soll:
- Den Sound gleichmäßig und laut genug ins Publikum bringen
- Alle Frequenzen sauber und verzerrrungsfrei wiedergeben
- Das gesamte Publikum möglichst gleich laut und qualitativ hochwertig beschallen

### Typische Komponenten eines PA-Systems:

```
Mischpult (Ausgang L/R)
        ↓
Systemcontroller / DSP (Laufzeiten, EQ, Limitierung)
        ↓
Endstufe (Verstärker)
        ↓
Lautsprecher (Tops + Subwoofer)
```

### Kleine vs. große PA

| Größe | Typischer Einsatz | Beispiel |
|-------|-----------------|---------|
| Kleine PA | Probe, kleiner Club | 2× Tops, kein Sub |
| Mittlere PA | Kleinere Live-Gigs | 2× Tops, 1–2× Sub |
| Größere PA | Festivals, Hallen | Line-Array links/rechts + viele Subs |

---

## 5.2 Aktiv vs. Passiv

Lautsprecher gibt es in zwei Varianten – aktiv und passiv. Für den Einsteiger ist es wichtig, den Unterschied zu kennen.

### Passive Lautsprecher

Ein **passiver Lautsprecher** hat keine eigene Elektronik. Er braucht ein separates **Verstärkergerät (Endstufe)**, das das Signal verstärkt bevor es in den Lautsprecher geht.

```
Mischpult → Endstufe → Passiver Lautsprecher
```

**Vorteile:**
- Endstufen können separat gewählt und ausgetauscht werden
- Endstufen laufen oft kühler und sind robuster
- Flexibler im Aufbau

**Nachteile:**
- Mehr Kabel (Speakon-Kabel zwischen Endstufe und Lautsprecher)
- Mehr Geräte = mehr Fehlerquellen
- Schwerer aufzubauen für Einsteiger

### Aktive Lautsprecher

Ein **aktiver Lautsprecher** hat die Endstufe bereits **eingebaut**. Du steckst direkt das Line-Signal (XLR) an.

```
Mischpult → Aktiver Lautsprecher (Endstufe intern)
```

**Vorteile:**
- Einfacher Aufbau, weniger Kabel
- Endstufe ist auf den Lautsprecher abgestimmt
- Ideal für mobile Systeme und Einsteiger

**Nachteile:**
- Wenn der Lautsprecher kaputt geht, ist Endstufe und Lautsprecher gleichzeitig weg
- Schwerer (Endstufe im Gehäuse)

> 💡 **Für den Anfang:** Aktive Lautsprecher sind einfacher zu handhaben. Die meisten modernen Systeme für kleine Bands sind aktiv.

---

## 5.3 Tops & Subwoofer

Ein vollständiges PA-System besteht aus zwei Lautsprechertypen, die zusammen das gesamte Frequenzspektrum abdecken:

### Tops (Fullrange-Lautsprecher)

**Tops** reproduzieren Mitten und Höhen – also alles oberhalb von ca. 80–100 Hz. Sie werden auf Stative gestellt (oder auf die Subs) und zeigen ins Publikum.

- Typische Frequenz: ca. 80 Hz – 20 kHz
- Enthält oft Hochtöner (HF) + Mittel-/Tiefmitteltöner (LF)
- Beispiel: RCF Art 735, QSC K12.2

### Subwoofer (Subs)

**Subwoofer** reproduzieren nur die tiefen Bassfrequenzen, die ein normaler Fullrange-Lautsprecher nicht kann.

- Typische Frequenz: 30–80 Hz (manchmal bis 120 Hz)
- Stehen auf dem Boden (Bässe sind omnidirektional)
- Geben dem Sound das physische Fundament – den "Druck" im Bauch

### Frequenzweiche (Crossover)

Damit Tops und Subs nur die Frequenzen bekommen, die sie wiedergeben sollen, gibt es eine **Frequenzweiche** (Crossover):

- **Tiefpassfilter** für den Sub: Lässt nur Tiefen durch
- **Hochpassfilter** für die Tops: Lässt nur Mitten/Höhen durch
- Die **Trennfrequenz** (Crossover-Punkt) liegt meist bei 80–100 Hz

Bei aktiven Systemen ist die Frequenzweiche oft bereits im System-DSP integriert.

> ⚠️ **Achtung:** Nie ein Fullrange-Signal auf einen Subwoofer geben, der keine eigene Frequenzweiche hat – der Hochtöner im Sub (falls vorhanden) kann kaputtgehen.

---

## 5.4 Monitorlautsprecher

**Monitorlautsprecher** (kurz: Wedges, Wedge-Monitor oder Floor-Monitor) stehen auf der Bühne und zeigen zu den Musikern hin. Sie geben den Musikern ihr eigenes Mix zurück, damit sie sich beim Spielen hören können.

### Warum brauchen Musiker Monitoring?

Auf einer lauten Bühne mit PA-Sound von vorne und den eigenen Instrumenten hinter sich kann ein Musiker sich selbst oft kaum hören. Ohne Monitoring spielen sie falsch, kommen aus dem Rhythmus oder singen schief.

### Aufbau auf der Bühne

Typisches einfaches Monitoring-Setup:

```
Sänger         Gitarrist      Schlagzeuger
  ▲                ▲
[Monitor 1]  [Monitor 2]    [Monitor 3]

Aux 1 → Monitor 1 (viel Gesang, etwas Gitarre)
Aux 2 → Monitor 2 (seine Gitarre, Gesang, etwas Drums)
Aux 3 → Monitor 3 (Klick/Click-Track, etwas Bass und Gesang)
```

### Keilmonitor vs. Sidefill

- **Keilmonitor (Wedge):** Liegt flach auf dem Boden, typische Keilform, zeigt von unten auf den Musiker
- **Sidefill:** Größerer Lautsprecher seitlich der Bühne, für Sänger, die sich viel bewegen

### Wichtige Eigenschaft: Feedback-Unterdrückung

Da Monitorlautsprecher direkt in die Mikrofone strahlen (können), ist Feedback-Gefahr groß. Deshalb:
- Nieren-Charakteristik nutzen (Mikrofon von hinten = von Monitor wegzeigend)
- HPF nutzen
- Gain im Monitor-Aux nicht zu hoch

---

## 5.5 In-Ear-Monitoring

**In-Ear-Monitoring (IEM)** ist die Alternative zum klassischen Wedge-Monitor: Der Musiker trägt kleine Ohrhörer (ähnlich wie Kopfhörer) und bekommt seinen Mix direkt ins Ohr.

### Vorteile von In-Ear:

- **Keine Feedback-Gefahr** – kein offener Lautsprecher auf der Bühne
- **Bessere Lautstärkekontrolle** – Musiker hört seinen Mix leise und klar
- **Gehörschutz** – richtig angewendet schützt IEM das Gehör besser als Wedge
- **Sauberer Bühnenklang** – weniger Bühnenlärm, bessere Mischsituation für FOH

### Nachteile:

- **Teurer** als Wedge-System (besonders kabellose Systeme)
- **Fühlt sich unnatürlich an** für manche Musiker ("tot" im Ohr, kein Raumgefühl)
- **Kabelgebunden vs. Funk:** Kabel kann stören, Funkstrecke ist teurer

### Aufbau:

```
Mischpult Aux-Ausgang → In-Ear-Sender (rack) → IEM-Empfänger (am Gürtel) → Ohrhörer
```

Bei kabelgebundenem IEM: Aux-Ausgang → Kopfhörerverstärker → Kabel → Ohrhörer

> 💡 **Für die Band:** In-Ear ist der nächste Schritt nach einem guten Wedge-System. Wenn die Bühne sauberer und ruhiger werden soll – IEM ist die Lösung.

---

## 5.6 Feedback / Rückkopplungen

**Feedback** (Rückkopplung) ist das gefürchtete Pfeifen, das entsteht, wenn der Schall aus einem Lautsprecher wieder in ein Mikrofon geht und dann verstärkt wird – und wieder in den Lautsprecher geht – und so weiter. Eine Endlosschleife.

### Wie entsteht Feedback?

```
Mikrofon → Mischpult → Lautsprecher → [Schall geht zurück ins Mikrofon] → Mischpult → Lautsprecher → ...
```

Die Schleife verstärkt sich jedes Mal, bis eine bestimmte Frequenz so laut wird, dass man das typische Pfeifen oder Heulen hört.

### Warum pfeift es gerade bei bestimmten Frequenzen?

Jede Frequenz verhält sich im Raum anders. Bestimmte Frequenzen werden durch Reflexionen an Wänden und Boden besonders stark zurückgeworfen. Das Mikrofon, der Raum und die Lautsprecher-Position bestimmen gemeinsam, welche Frequenz zuerst Feedback erzeugt.

### Was tun bei Feedback?

**Sofort-Maßnahmen:**

1. **Gain des Kanals schnell runter** → Feedback stoppt sofort
2. Kanal muten
3. Sänger bittet, das Mikrofon weg vom Monitor zu halten

**Dauerhafte Lösung:**

- Mikrofon-Position und Monitor-Position überprüfen
- Gain senken
- Die Feedback-Frequenz mit einem engen EQ-Cut senken (mehr dazu in 5.7)
- Monitore nie direkt vor das Mikrofon stellen

---

## 5.7 Feedbackfrequenzen erkennen

Das Erkennen von Feedbackfrequenzen ist eine wichtige Fähigkeit – und sie lässt sich trainieren.

### Methode 1: Systematisches Soundcheck-Vorgehen (Ringing Out)

Beim "Ringing Out" eines Monitor-Mixes geht man wie folgt vor:

1. Aux-Master für den Monitor langsam hochziehen
2. Warten bis das System kurz vor dem Feedback ist (es "klingelt" leise)
3. Die Frequenz am Mischpult oder Grafik-EQ identifizieren und etwas absenken
4. Wieder etwas hochziehen – nächste Frequenz absenken
5. So lange, bis der Monitor laut genug für den Musiker ist ohne zu feedbacken

**Wichtig:** Grafik-EQ (31-Band-EQ) ist ideal dafür – viele Monitor-Auxe laufen durch einen Grafik-EQ, bevor sie zum Monitor gehen.

### Methode 2: Feedback-Frequenz hören

Mit Übung kannst du eine Feedback-Frequenz hören und ihr Bereich grob einschätzen:

| Klingt nach... | Ungefähre Frequenz |
|---------------|-------------------|
| Tiefes Wummern / Grollen | 80–200 Hz |
| Mittiges Heulen | 500 Hz – 2 kHz |
| Hohes Pfeifen | 2–8 kHz |
| Sehr hohes, spitzes Pfeifen | 8–16 kHz |

### Grafik-EQ als Feedback-Werkzeug

Am Monitor-Ausgang sitzt oft ein **31-Band Grafik-EQ**. Hier kannst du Frequenzen sehr gezielt in kleinen Schritten (je 1/3 Oktave) absenken.

```
63  125  250  500  1k  2k  4k  8k  16k Hz
 |   |    |    |   |   |   |   |   |
 0   0   -2    0   0  -3   0   0  -2  dB  (Beispiel: Feedback bei 2 kHz und 250 Hz gesenkt)
```

> 💡 **Tipp:** Lieber mehrere Frequenzen minimal absenken (–1 bis –3 dB) als eine einzige Frequenz stark (–10 dB). Starke Einschnitte klingen unnatürlich.

---

## 5.8 Lautsprecherpositionierung

Wo ein Lautsprecher steht, hat genauso viel Einfluss auf den Sound wie der Mix selbst. Schlechte Positionierung kann auch den besten Mix ruinieren.

### Grundregeln für die Top-Platzierung:

**1. Lautsprecher zeigen ins Publikum, nicht in die Luft oder an die Wand.**

- Optimal: Lautsprecher auf Stativen, leicht nach unten geneigt, auf das mittlere Publikum gerichtet
- Fehler: Lautsprecher stehen auf dem Boden und strahlen nach oben

**2. Abstand zum Mikrofon vergrößern.**

- Je mehr Abstand zwischen Lautsprecher und Mikrofon, desto weniger Feedback-Gefahr
- Tops möglichst weit vorne aufstellen (nicht hinter den Musikern)

**3. Lautsprecher-Abdeckwinkel (Coverage Angle) beachten.**

Jeder Lautsprecher hat einen horizontalen und vertikalen Abstrahlwinkel. Der Bereich, der gut beschallt wird, ist der **Coverage Angle**. Außerhalb des Winkels fällt der Pegel stark ab.

```
         Lautsprecher
              /
Publikum [====]
              \
```
Typisch: 90° horizontal × 60° vertikal.

### Subwoofer-Positionierung:

- Subs stehen auf dem Boden – tiefe Frequenzen profitieren vom Bodenpresswing (Grenzflächeneffekt)
- Subs möglichst in der Mitte oder symmetrisch links/rechts aufstellen
- Nicht in Ecken stellen (Überhöhungen von Raummoden)

### Delay-Speaker / Fill-Speaker:

Bei großen Venues (Hallen, Freigelände) reicht das Haupt-PA nicht, um weit entfernte Bereiche zu versorgen. Hier kommen **Delay-Speaker** zum Einsatz:

- Kleinere Lautsprecher, die tiefer im Publikumsbereich aufgestellt werden
- Mit einer **Laufzeitverzögerung (Delay)** versehen, damit der Schall zeitlich zur Haupt-PA passt
- Ohne Delay würde man zuerst den Delay-Speaker hören und dann (mit Nachhall) die Haupt-PA

> ⚠️ **Wichtige Sicherheitsregel:** Lautsprecher auf Stativen müssen korrekt gesichert sein. Ein kippendes Stativ kann Leben gefährden. Immer die Stative prüfen, Standplatten verwenden, Kabel fixieren.

---

## Zusammenfassung Kapitel 5

- Das PA-System beschallt das Publikum: Tops für Mitten/Höhen, Subs für den Bass
- Aktive Lautsprecher (Endstufe eingebaut) sind einfacher für den Anfang
- Monitore geben den Musikern ihren eigenen Mix – unabhängig vom FOH-Mix
- In-Ear-Monitoring ist die moderne, sauberere Alternative zu Wedge-Monitoren
- Feedback entsteht, wenn Schall aus dem Lautsprecher zurück ins Mikrofon geht
- Feedbackfrequenzen erkennen und am EQ senken ist eine wichtige Fähigkeit
- Lautsprecherpositionierung beeinflusst den Sound genauso wie der Mix

---

*Weiter geht es in Kapitel 6: Hören lernen*
