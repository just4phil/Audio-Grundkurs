# Kapitel 2: Kabel, Anschlüsse & Hardware

> **Warum ist das wichtig?**
> Bevor du auch nur einen Regler anfasst, musst du wissen, was du womit verbindest. Falsche Verbindungen können Equipment beschädigen oder einfach keinen Ton erzeugen – das kostet Zeit und Nerven.

---

## 2.1 XLR

Das **XLR-Kabel** ist der Standard für professionelles Audio. Es ist das Kabel mit dem runden 3-poligen Stecker, den du an jedem Mikrofon siehst.

**Aufbau eines XLR-Steckers (3 Pins):**

| Pin | Funktion |
|-----|----------|
| Pin 1 | Masse (Ground / Shield) |
| Pin 2 | Signal + (positiv) |
| Pin 3 | Signal – (negativ) |

**Männlich vs. Weiblich:**

- **XLR männlich (male):** Stecker mit Pins → kommt aus dem Mikrofon oder aus einem Ausgang
- **XLR weiblich (female):** Buchse mit Löchern → geht in einen Eingang (z.B. Mischpult)

> 💡 **Eselsbrücke:** "Mikrofone sind weiblich" – der Stecker am Mikrofon ist female (Eingang), und der Stecker vom Kabel, der ins Mikrofon geht, ist male.

**Warum XLR und nicht irgendwas anderes?**

XLR überträgt das Signal **symmetrisch** (mehr dazu in Abschnitt 2.7). Das macht es widerstandsfähig gegen Einstreuungen (Brummen, Rauschen) – ideal für lange Kabelwege auf der Bühne.

**Typische Einsatzbereiche:**

- Mikrofon → Mischpult
- Mischpult → Endstufe
- Stagebox → Mischpult (Multicore)
- Di-Box → Mischpult

---

## 2.2 Klinke (TS / TRS)

Klinkenstecker (auch "Jack" genannt) kommen in verschiedenen Größen und Varianten.

### TS – Mono (Tip/Sleeve)

Der **TS-Stecker** hat zwei Abschnitte (Tip = Spitze, Sleeve = Hülse) und überträgt ein **unsymmetrisches** Mono-Signal.

**Einsatzbereiche:**
- Gitarren- und Bassinstrumentkabel (6,3 mm)
- Effektpedal-Verbindungen
- Manche Kopfhörer (3,5 mm TS)

### TRS – Stereo oder symmetrisch (Tip/Ring/Sleeve)

Der **TRS-Stecker** hat drei Abschnitte (Tip, Ring, Sleeve) und kann:

- Ein **Stereo-Signal** übertragen (z.B. Kopfhörer)
- Ein **symmetrisches Mono-Signal** übertragen (z.B. Insert-Kabel, symmetrierte Line-Verbindungen)

**Größen:**

| Größe | Typischer Einsatz |
|-------|------------------|
| 6,3 mm (¼ Zoll) | Instrumente, Mischpult-Eingang, Endstufen |
| 3,5 mm (Mini-Jack) | Smartphones, Laptops, Consumer-Geräte |

> ⚠️ **Achtung:** Ein Gitarrenkabel (TS) in einen Kopfhörerausgang (TRS) zu stecken funktioniert – aber du hörst nur einen Kanal! Verwende für Kopfhörer immer TRS.

---

## 2.3 Speakon

Das **Speakon-Kabel** wurde von Neutrik entwickelt und ist speziell für die Verbindung zwischen Endstufe und Lautsprecher gedacht.

**Warum Speakon statt Klinke?**

- Viel höhere Stromfestigkeit – Lautsprecher brauchen viel mehr Strom als Mikrofone
- Verpolungssicher – Stecker rastet ein und kann nicht versehentlich rausfallen
- Sicherer – bei hohen Lautstärken können Klinkenstecker Funken schlagen

**Typen:**

- **NL2** (2-polig): Für einfache mono Lautsprecher
- **NL4** (4-polig): Für Bi-Amping (getrennte Ansteuerung von Tieftöner und Hochtöner)

**Erkennungszeichen:** Runder, schwarzer Stecker mit einer Arretierung (Lock), der durch Drehen einrastet.

> ⚠️ **Niemals** ein Mikrofon- oder Instrumentensignal über ein Speakon-Kabel schicken – das sind zwei völlig unterschiedliche Signalstärken!

---

## 2.4 Cinch / RCA

Der **Cinch-Stecker** (auch RCA genannt) ist der runde, farbige Stecker, den du vielleicht von Stereo-Anlagen zu Hause kennst.

**Charakteristik:**

- Überträgt ein **unsymmetrisches** Signal
- Immer paarweise (Rot = Rechts, Weiß/Schwarz = Links)
- Eher im Consumer-Bereich (Heimkino, DJ-Pult)

**In der Live-Tontechnik:**

Cinch findet man beim Live-Sound eher selten, aber manchmal:
- DJ-Pult → Mischpult
- Zuspielgeräte (CD-Player, Laptop mit Adapter)
- Subwoofer-Ausgänge mancher Systeme

> 💡 **Tipp:** Wenn du ein Gerät mit Cinch-Ausgang an ein Mischpult mit Klinke anschließen willst, brauchst du einen Adapter oder ein Adapterkabel (Cinch auf Klinke).

---

## 2.5 MIDI

**MIDI** steht für *Musical Instrument Digital Interface*. Es ist kein Audiokabel – es überträgt keine Klänge, sondern **Steuerdaten**.

**Was überträgt MIDI?**

- Welche Note wird gespielt (z.B. "C4")
- Wie laut (Velocity / Anschlagstärke)
- Welches Instrument / welcher Kanal
- Programmwechsel, Controller-Daten (z.B. Pedalposition)

**MIDI-Anschlüsse:**

- **MIDI IN:** Eingang – empfängt Befehle
- **MIDI OUT:** Ausgang – sendet Befehle
- **MIDI THRU:** Leitet das Signal unverändert weiter (für Geräte in Serie)

**Modernes MIDI:**

Klassisches MIDI nutzt 5-polige DIN-Stecker (die runden großen Stecker). Heute wird MIDI oft über **USB** oder sogar über Netzwerk übertragen.

**Relevanz für den Live-Tontechniker:**

- Digitale Mischpulte können per MIDI Szenen wechseln
- Effektgeräte können per MIDI ferngesteuert werden
- Keyboards und Drumcomputer kommunizieren per MIDI

---

## 2.6 USB & digitale Verbindungen

### USB

**USB-Verbindungen** kommen in der Audiotechnik vor bei:

- Audiointerfaces (Mikrofon oder Mischpult → Computer)
- USB-Mikrofone (direkt ans Laptop)
- Firmware-Updates für digitale Mischpulte
- Abspielen von USB-Sticks auf Mischpulten

**USB-Typen:** USB-A, USB-B, USB-C, Micro-USB – je nach Gerät. Merke dir einfach, welches Kabel welches Gerät braucht.

### AES/EBU

Eine professionelle digitale Audioverbindung, die wie XLR aussieht, aber digitale Daten überträgt. Wird bei professionellen Stagebox-Systemen und Verbindungen zwischen Profi-Geräten genutzt.

### S/PDIF

Consumer-digitale Verbindung, entweder über Cinch (koaxial) oder Lichtleiter (TOSLINK). Kommt beim Live-Sound selten vor, eher im Heimstudio.

### Ethernet / Dante

Moderne Bühnen nutzen oft **Audio-over-IP** (Dante, AVB, AES67) – dabei wird Audio digital über normale Netzwerkkabel (Ethernet/CAT) übertragen. Ein Kabel kann dabei hunderte Audiokanäle tragen. Dazu mehr in Kapitel 11.

---

## 2.7 Symmetrisch vs. unsymmetrisch

Das ist ein Konzept, das du wirklich verstehen musst – es erklärt, warum manche Kabel Brummen und Rauschen einsammeln und andere nicht.

### Unsymmetrisches Signal (Unbalanced)

Ein unsymmetrisches Kabel hat **zwei Leiter**: Signal und Masse. Das Signal liegt offen da.

**Problem:** Auf dem Weg durch das Kabel können sich elektromagnetische Störungen einschleichen (Brummen vom Stromnetz, Einstreuungen von Lichtdimmern, Handyantennen usw.).

**Typische Kabel:** TS-Klinkenkabel (Gitarrenkabel), Cinch

### Symmetrisches Signal (Balanced)

Ein symmetrisches Kabel hat **drei Leiter**: Signal+, Signal– und Masse.

**Das Trick dabei:** Das gleiche Signal wird mit umgekehrter Polarität ein zweites Mal übertragen. Am Eingang des Empfängers werden die Störungen, die sich auf beide Signale aufaddiert haben, wieder herausgerechnet (die Differenz der beiden Signale eliminiert den Störanteil). Das nennt sich **Common Mode Rejection**.

**Ergebnis:** Auch bei langen Kabelwegen kein Brummen, kein Rauschen.

**Typische Kabel:** XLR, TRS (wenn symmetrisch verwendet)

> 💡 **Faustregel:** Für Bühnenverkabelung immer symmetrisch (XLR) verwenden, sobald die Kabelwege länger als 3–5 Meter sind.

---

## 2.8 Stagebox & Multicore

### Was ist eine Stagebox?

Eine **Stagebox** (auch: Bühnenbox, Splitter) ist eine Anschlussbox, die auf der Bühne steht. Alle Mikrofone und Instrumente werden dort eingesteckt. Von der Stagebox läuft dann nur **ein dickes Kabel** zum Mischpult – das **Multicore**.

**Vorteile:**

- Statt 20 einzelnen Kabeln liegt nur ein Kabel durch den Saal
- Saubere, übersichtliche Bühnenverkabelung
- Weniger Kabelsalat im Publikumsbereich

### Wie ist eine Stagebox aufgebaut?

- **Eingänge (Ins):** XLR-Buchsen für Mikrofone (female) – oft 16 bis 32 Stück
- **Ausgänge (Returns):** XLR-Buchsen oder Klinke für Monitorwege – oft 4 bis 8 Stück

### Das Multicore-Kabel

Das **Multicore** (auch "Snake") ist ein Kabelbaum, der viele Kanäle in einem gemeinsamen Mantel führt. Am Ende hat es einen Steckverbinder zur Stagebox und am anderen Ende entweder:

- Einzelne XLR-Stecker (Fan-out) die direkt ins Mischpult gehen
- Einen Stecker in eine weitere Box (z.B. digitale Stage-Box)

> ⚠️ **Achtung beim Aufwickeln:** Ein Multicore mit 20 Kanälen und 30 Meter Länge kann sehr schwer sein – lass es dir am Anfang zeigen, wie es richtig gewickelt und getragen wird.

---

## 2.9 Kabelpflege & Wickeltechniken

Gute Tontechniker pflegen ihr Kabel. Ein kaputtes Kabel beim Soundcheck kostet Zeit und Nerven. Kabelpflege ist also kein Luxus – es ist professionelle Vorsorge.

### Die Over-Under-Methode (Overhand/Underhand)

Die professionellste Wickeltechnik für XLR und andere flexible Kabel ist **Over-Under** (auch: Überhand-Unterhand). Sie verhindert, dass sich das Kabel beim Abwickeln verdreht.

**So geht's:**

1. Nimm das Kabelende in die linke Hand
2. Erste Schlaufe: Wickle das Kabel **normal über** die Hand (Überhand)
3. Zweite Schlaufe: Drehe die nächste Schlaufe **leicht nach innen** und leg sie **unter** die erste (Unterhand)
4. Abwechseln: über – unter – über – unter
5. Am Ende mit einem Klettverschluss oder Kabelbinder sichern

**Warum so kompliziert?**

Ein Kabel, das immer in die gleiche Richtung gewickelt wird, bekommt einen "Drall" – es dreht sich beim Abwickeln und macht Knoten. Over-Under verhindert das.

### Wichtige Regeln für Kabelpflege:

- **Niemals** knicken oder stark biegen – die Adern im Inneren brechen
- **Nie** mit dem Fuß draufstehen oder überrollen lassen (mit Fahrzeugen)
- Stecker immer sauber halten – dreckige Stecker machen Kontaktprobleme
- Nach dem Einsatz: Abwischen, prüfen, ordentlich aufwickeln
- Kabel regelmäßig testen – ein Kabeltester kostet wenig und spart viel Ärger

### Kabelbeschriftung

Beschrifte deine Kabel! Klebeband mit einem Stift, Schrumpfschlauch oder Kabelmarkierer. So weißt du bei einem Problem sofort, welches Kabel wohin geht.

### Kabeltester – dein bester Freund

Ein einfacher Kabeltester (kostet 10–30 Euro) zeigt dir:

- Ob alle Leitungen durchgehen
- Ob das Kabel einen Kurzschluss hat
- Ob Masse und Signal vertauscht sind (Polverwechslung)

> 💡 **Profi-Tipp:** Teste neue Kabel, bevor du sie einsetzt. Und wenn du einen Fehler nicht findest – check zuerst das Kabel. Kabelprobleme sind der häufigste Fehler beim Live-Sound.

---

## Zusammenfassung Kapitel 2

| Kabel/Stecker | Verwendung | Symmetrisch? |
|---------------|-----------|--------------|
| XLR | Mikrofone, professionelles Audio | Ja |
| Klinke TS | Gitarren, Instrumente | Nein |
| Klinke TRS | Kopfhörer, symmetrierte Line-Verbindungen | Ja/Nein (je nach Verwendung) |
| Speakon | Endstufe → Lautsprecher | Sonderfall |
| Cinch/RCA | Consumer-Geräte, DJ | Nein |
| MIDI | Steuerdaten (keine Audiodaten!) | – |
| USB | Audiointerfaces, digitale Mischpulte | – |

**Goldene Regeln:**
- Mikrofone und professionelle Geräte → XLR (symmetrisch)
- Lautsprecher → Speakon (nie Mikrokabel!)
- Kabel pflegen, testen, beschriften
- Over-Under-Wickeltechnik lernen und immer anwenden

---

*Weiter geht es in Kapitel 3: Mikrofone*
