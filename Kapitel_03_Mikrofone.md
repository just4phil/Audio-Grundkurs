# Kapitel 3: Mikrofone

> **Warum ist das wichtig?**
> Das Mikrofon ist das erste Glied in der Signalkette. Wenn hier etwas nicht stimmt, hilft dir auch das teuerste Mischpult nichts mehr. Ein gutes Verständnis von Mikrofonen ist der Schlüssel zu einem guten Live-Sound.

---

## 3.1 Dynamische Mikrofone

Das **dynamische Mikrofon** ist das Arbeitspferd der Live-Tontechnik. Robust, günstig und für die meisten Anwendungen auf der Bühne ideal.

### Wie funktioniert es?

Im Inneren sitzt eine dünne Membran, die mit einer Spule verbunden ist. Diese Spule hängt in einem Magnetfeld. Wenn Schall die Membran bewegt, bewegt sich die Spule im Magnetfeld – und erzeugt so elektrischen Strom (**Induktionsprinzip**).

### Eigenschaften:

- **Robust** – verträgt Stöße, Feuchtigkeit, laute Schalldruckpegel
- **Braucht keine Phantomspannung** (wichtig: mehr dazu in 3.5)
- **Gut für laute Quellen** – Gitarrenamp, Snare, Gesang auf der Bühne
- **Weniger empfindlich bei sehr hohen Frequenzen** (klingt etwas dunkler als Kondensatormikrofone)

### Klassiker:

- **Shure SM58** – das meistverkaufte Gesangsmikrofon der Welt
- **Shure SM57** – für Instrumente (Snare, Gitarrenamp)
- **Sennheiser e835, e845**

> 💡 **Tipp:** Das SM57 und SM58 sind so robust, dass sie Jahrzehnte halten. Wenn du ein zuverlässiges Mikrofon für den Anfang brauchst, bist du damit goldrichtig.

---

## 3.2 Kondensatormikrofone

Das **Kondensatormikrofon** ist empfindlicher und klingt detailreicher als das dynamische Mikrofon. Es wird vor allem für Overhead (Schlagzeug), Akustikgitarren, Chöre und Aufnahmen verwendet.

### Wie funktioniert es?

Hier ist die Membran eine dünne Metallfolie, die sich gegenüber einer festen Platte befindet – zusammen bilden sie einen **Kondensator**. Wenn Schall die Membran bewegt, ändert sich der Abstand zur Gegenplatte, und damit die elektrische Kapazität. Diese winzige Änderung wird verstärkt.

### Eigenschaften:

- **Sehr empfindlich** – nimmt auch leise Details auf
- **Braucht Phantomspannung (+48V)** – ohne Strom geht gar nichts
- **Klingt klarer, luftiger** – mehr Höhen, mehr Details
- **Weniger robust** – nicht auf laute Impulse direkt ausrichten (z.B. Snare direkt vor dem Mikrofon)
- **Empfindlich gegenüber Feuchtigkeit** – bei schlechtem Wetter oder Schweißtropfen vorsichtig sein

### Varianten:

- **Großmembran-Kondensator** – klassisches Studio-Mikrofon, große runde Kapsel
- **Kleinmembran-Kondensator** – schlanker Stift, sehr präzise Richtcharakteristik, gut für Overhead und Akustikgitarre

### Klassiker:

- **Shure SM81** – Kleinmembran, sehr beliebt für Overhead
- **AKG C414** – Großmembran, vielseitig
- **Rode NT5** – günstiger Einstieg für Kleinmembran

---

## 3.3 Richtcharakteristiken

Die **Richtcharakteristik** beschreibt, aus welchen Richtungen ein Mikrofon Schall aufnimmt. Das ist extrem wichtig beim Live-Sound, weil es bestimmt, wie gut das Mikrofon den gewünschten Sound aufnimmt und wie stark es Störgeräusche und Feedback unterdrückt.

### Kugel (Omnidirektional)

Das Mikrofon nimmt Schall aus **allen Richtungen** gleichmäßig auf.

- **Vorteil:** Kein Nahbesprechungseffekt, klingt natürlich
- **Nachteil:** Keine Rückkopplungsunterdrückung – auf der Bühne kaum verwendbar

### Niere (Cardioid)

Die häufigste Charakteristik bei Live-Mikrofonen. Nimmt Schall **von vorne** auf, blendet Schall **von hinten** aus.

- **Vorteil:** Gute Trennung von Schallquellen, Feedback-Unterdrückung
- **Nachteil:** Starker Nahbesprechungseffekt

```
        VORNE
        (gut)
         ↑
Links ←  ●  → Rechts
(mittel)   (mittel)
         ↓
       HINTEN
       (kaum)
```

### Superniere / Hyperniere

Noch enger als die Niere, noch besser in der Frontalaufnahme, aber mit einem kleinen Bereich auch **direkt hinten** empfindlich.

- **Einsatz:** Drumoverhead, Sprachübertragung in lauter Umgebung

### Acht (Bidirektional)

Nimmt Schall **von vorne und hinten** auf, blendet Schall **von der Seite** aus.

- **Einsatz:** Selten beim Live-Sound, öfter im Studio (z.B. Stereo-Techniken)

> 💡 **Merke für die Bühne:** Bei fast allen Gesangsmikrofonen auf der Bühne willst du eine **Niere oder Superniere**. Richtung und Abstand stimmen – Feedback bleibt draußen.

---

## 3.4 Nahbesprechungseffekt

Der **Nahbesprechungseffekt** (englisch: *Proximity Effect*) ist ein physikalisches Phänomen: Je näher du ein Nieren- oder Supernieren-Mikrofon an die Schallquelle hältst, desto mehr Bässe werden betont.

### Praxisbeispiel:

- Sänger hält das Mikrofon weit weg → dünner, heller Klang
- Sänger hält das Mikrofon direkt an den Mund → voller, bassiger Klang

### Praktische Nutzung:

- Ein dünner Sänger kann näher ans Mikrofon gehen für mehr Wärme
- Radio-DJs nutzen den Nahbesprechungseffekt für ihre tiefe, warme Stimme
- Bei zu viel Nähe kann der Bass übertrieben werden → mit High-Pass-Filter (HPF) gegensteuern

> ⚠️ **Problem:** Wenn Sänger mit dem Mikrofon "rumspielen" (mal nah, mal weit weg), schwankt der Klang stark. Als Tontechniker musst du das mit Gain und EQ ausgleichen.

---

## 3.5 Phantomspannung

**Phantomspannung** (+48V) ist eine Gleichspannung, die das Mischpult über das XLR-Kabel zum Mikrofon schickt. Kondensatormikrofone brauchen diese Spannung, um zu funktionieren.

### Wichtige Regeln:

1. **Aktiviere Phantomspannung nur für Kondensatormikrofone** – dynamische Mikrofone brauchen sie nicht, aber in der Regel werden sie davon auch nicht beschädigt
2. **Bändchenmikrofone (Ribbon) können durch Phantomspannung zerstört werden** – niemals +48V an ein Bändchenmikrofon!
3. **Schalte Phantomspannung ein, bevor du den Kanal aufmachst** – bzw. erst Phantom an, dann Fader hochziehen, um Knackgeräusche zu vermeiden
4. Am Mischpult erkennst du den Schalter mit **"48V"** oder **"Phantom Power"**

### Was passiert ohne Phantomspannung?

Das Kondensatormikrofon gibt kein oder extrem wenig Signal aus. Es klingt nicht kaputt – es liefert einfach kein Signal.

> 💡 **Tipp:** Wenn ein Kondensatormikrofon keinen Ton macht und du alles andere gecheckt hast – prüf als erstes, ob Phantomspannung eingeschaltet ist!

---

## 3.6 Mikrofonierung von Gesang

Gesang ist die wichtigste Schallquelle beim Live-Sound. Der Sänger muss für das Publikum klar und verständlich zu hören sein.

### Grundregeln für Gesangsmikrofone:

- **Abstand:** 5–15 cm vom Mund – zu nah gibt Nahbesprechung und Plosive ("P", "B"), zu weit gibt Rauschen und dünnen Klang
- **Winkel:** Leicht schräg halten (ca. 45°) reduziert Plosive und Zischlaute
- **Niere-Richtung:** Die Vorderseite des Mikrofons zeigt auf den Mund

### Häufige Probleme:

| Problem | Ursache | Lösung |
|---------|---------|--------|
| Zu dumpfer, bassiger Sound | Zu nah am Mund, Nahbesprechung | High-Pass-Filter, etwas Abstand |
| Zischende S-Laute | Sibilanz, Mikrofon direkt auf Mund | Winkel ändern, De-Esser |
| Knacken bei "P" und "B" (Plosive) | Luftstoß direkt auf Kapsel | Mikrofon schräg halten, Pop-Filter |
| Feedback (Pfeifen) | Mikrofon zu nah am Monitor | Monitor-Winkel ändern, Gain reduzieren |

### Mikrofontypen für Gesang:

- **Live:** Shure SM58, Sennheiser e835, AKG D5 (dynamisch, robust)
- **Studio:** Großmembran-Kondensator (AKG C414, Neumann U87)

---

## 3.7 Mikrofonierung von Gitarrenamps

Ein Gitarrenamp klingt auf der Bühne anders als der Sound, der das Publikum erreicht – deshalb wird er mit einem Mikrofon abgenommen.

### Die Grundposition: SM57 auf der Lautsprechermembran

Das Shure SM57 ist der absolute Standard für Gitarrenamps. Es ist robust, verträgt hohe Schalldruckpegel und klingt gut.

**Positionierung:**

```
     Amp-Lautsprecher
     ┌─────────────┐
     │    ┌───┐    │
     │    │   │    │   ← Mitte der Membran (hell, viel Höhen)
     │    └───┘    │   ← Rand der Membran (wärmer, mehr Tiefe)
     └─────────────┘
           ↑
          SM57
```

- **Mittig auf den Konus zeigen:** Mehr Höhen, brillanter Klang, schärfer
- **Auf den Rand zeigen:** Wärmer, weniger Zischhöhen
- **Abstand:** Direkt auf dem Gitter des Amps bis ca. 5 cm davor

### Tipps:

- Starte mit dem Mikrofon **direkt auf dem Gitter** in der Mitte des Lautsprechers
- Höre dir den Sound an und verändere dann die Position minimal
- Kleine Positionsveränderungen haben große Auswirkungen – probiere verschiedene Positionen aus

> 💡 **Praxistipp:** Was aus dem Amp kommt, ist der Sound des Gitarristen. Deine Aufgabe ist es, diesen Sound möglichst originalgetreu einzufangen, nicht zu verändern. Mikrofonposition vor EQ!

---

## 3.8 Mikrofonierung von Schlagzeug

Das Schlagzeug ist die komplexeste Schallquelle beim Live-Sound. Es besteht aus vielen Elementen, die alle unterschiedlich behandelt werden.

### Übersicht: Typisches Drum-Mikrofonie-Setup

| Teil | Mikrofon | Position |
|------|---------|----------|
| Kick (Bassdrum) | Dynamisch mit Großmembran (z.B. AKG D112, Shure Beta 52) | Im Loch der Resonanzfell-Seite, auf den Schläger gerichtet |
| Snare (oben) | SM57 | 2–5 cm über Rand, auf Fell gerichtet |
| Snare (unten) | SM57 oder ähnlich | Unter dem Fell (Schnarrteppich), Phase beachten! |
| Hi-Hat | Kleines Kondensatormikrofon | 10–15 cm über den Becken |
| Tom 1, Tom 2 | Kleine Clip-Mikrofone (e.g. Sennheiser e604) | Am Rand der Toms |
| Floor Tom | Clip-Mikrofon oder SM57 | Am Rand |
| Overhead L/R | Kleinmembran-Kondensator (z.B. SM81) | 40–60 cm über den Becken, symmetrisch |

### Besonderheiten:

**Kick Drum:**
Die Bassdrum braucht ein spezielles Mikrofon, das hohe Schalldruckpegel und tiefe Frequenzen gut verträgt. Das Mikrofon wird durch ein Loch im Resonanzfell in die Trommel eingeführt.

**Phasenproblem bei Snare oben/unten:**
Wenn du oben und unten ein Mikrofon an der Snare hast, sind die Membranen entgegengesetzt – das Signal von unten hat deshalb umgekehrte Polarität. Du musst eines der Mikrofone **umpolen (Phase drehen)** am Mischpult, sonst hören sich Bässe gegenseitig auf (Auslöschung)!

**Overhead-Mikrofone:**
Die Overhead-Mikrofone fangen die Becken und einen Gesamteindruck des Schlagzeugs ein. Sie sollen symmetrisch über dem Kit platziert sein, damit das Stereo-Bild stimmt.

---

## 3.9 Mikrofonierung von Bass & Akustikinstrumenten

### E-Bass

Der E-Bass kann auf zwei Arten abgenommen werden:

**1. DI-Box (Direct Injection)**

Die DI-Box wandelt das unsymmetrische Instrument-Signal in ein symmetrisches XLR-Signal um, das direkt ins Mischpult geht.

- **Vorteile:** Sauberer, definierter Bass-Sound; kein Mikrofon nötig; weniger Feedback
- **Nachteile:** Du hörst den "trockenen" Sound des Basses ohne den Charakter des Amps

**2. Mikrofon am Bassamp**

Gleiche Technik wie beim Gitarrenamp (SM57 oder Großmembran-Dynamik).

- **Vorteile:** Charakterklang des Amps wird mit übertragen
- **Nachteile:** Mehr Feedback-Potenzial; braucht guten Amp-Sound

**Profi-Tipp:** Viele Tontechniker kombinieren DI-Box (für das Fundament) + Mikrofon am Amp (für den Charakter) und mischen beides im Mischpult.

### Akustikgitarre

**Option 1: Pickup/DI-Box**
Wenn die Gitarre einen eingebauten Tonabnehmer hat, geht das Signal über DI-Box ins Mischpult.

**Option 2: Kondensatormikrofon**
- Kleinmembran-Kondensator (SM81, Rode NT5) auf den Klangkörper
- Position: Zwischen Schalloch und 12. Bund – nicht direkt ins Schalloch (zu viel Bass)
- Problem: Hohe Feedback-Gefahr bei lautem Bühnenpegel

**Option 3: Kombination**
DI + Mikrofon gemixt = natürlichster Sound.

### Keyboards / Synthesizer

Keyboards werden fast immer über **DI-Box** abgenommen (stereo: zwei DI-Boxen oder eine Stereo-DI).

- Keyboard → DI-Box L und R → XLR ins Mischpult (zwei Kanäle, Links und Rechts)

### Akustik-Instrumente allgemein (Geige, Cajon, usw.)

- Kondensatormikrofon in 20–60 cm Abstand vom Resonanzbereich des Instruments
- Nicht zu nah (Feedback, zu viel Direktschall), nicht zu weit (zu viel Raumklang)
- Niere für Bühne, Kugel nur im Proberaum/Studio

---

## Zusammenfassung Kapitel 3

**Die wichtigsten Mikrofontypen:**

| Typ | Beispiel | Einsatz |
|-----|---------|---------|
| Dynamisch | SM58, SM57 | Gesang, Gitarrenamp, Snare – robust, live |
| Kondensator | SM81, AKG C414 | Overhead, Akustikinstrumente – empfindlich, studio |

**Die wichtigsten Richtcharakteristiken:**

| Charakteristik | Form | Einsatz |
|---------------|------|---------|
| Kugel | Kreis | Studio, keine Bühne |
| Niere | Herz | Standard für Live |
| Superniere | Enger Kegel | Laute Umgebungen |

**Goldene Regeln:**
- Kondensatormikrofone brauchen +48V Phantomspannung
- Bändchenmikrofone NIEMALS Phantomspannung
- Snare oben/unten: Phase drehen!
- Mikrofonposition vor EQ: erst positionieren, dann korrigieren

---

*Weiter geht es in Kapitel 4: Analoge Mischpulte*
