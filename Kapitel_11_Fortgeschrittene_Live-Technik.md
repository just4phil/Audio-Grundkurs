# Kapitel 11: Fortgeschrittene Live-Technik

> **Wenn du die Grundlagen beherrschst, kommt das hier.**
> Dieses Kapitel behandelt Technologien und Konzepte, die du im professionellen Live-Bereich antreffen wirst. Du brauchst das nicht sofort zu können – aber du solltest wissen, was es ist und wie es funktioniert.

---

## 11.1 Digitalsnakes

Eine **Digitalsnake** ersetzt das klassische analoge Multicore-Kabel. Statt vieler analoger Signale wird ein digitales Signal über ein einziges Kabel übertragen.

### Wie funktioniert eine Digitalsnake?

```
Bühne                              Mischpult
┌────────────────┐                ┌──────────────┐
│  Stage Box     │────────────────│  FOH-Rack    │
│  (32 XLR-In)   │  1× CAT/AES   │  (digital)   │
│  (16 XLR-Out)  │               │              │
└────────────────┘               └──────────────┘
```

Statt eines dicken, schweren Multicore-Kabels mit 32 Kupferadern liegt nur ein schlankes Netzwerkkabel oder Glasfaserkabel auf dem Boden.

### Vorteile:

- Viel leichter und handlicher
- Kein Qualitätsverlust über lange Distanzen (digital bleibt digital)
- Oft integrierter Stagebox-Preamp → sehr gute Vorverstärkung direkt auf der Bühne

### Bekannte Systeme:

- **Allen & Heath dSNAKE** – für A&H-Mischpulte
- **Yamaha Rio** – für Yamaha-Pulte (CL/QL-Serie)
- **Behringer S16** – für X32/M32

> ⚠️ **Wichtig:** Digitalsnakes sind herstellergebunden. Du kannst eine Yamaha-Stage-Box in der Regel nicht an einem Allen & Heath Pult betreiben. Ausnahme: Standard-Protokolle wie Dante (mehr in 11.2).

---

## 11.2 Dante & Audio-over-IP

**Dante** ist ein Standard für Audio-over-IP – das Übertragen von Audio über normale Netzwerkkabel (Ethernet). Es ist die professionellste und flexibelste Lösung.

### Was kann Dante?

- Bis zu **512 Kanäle** über ein einziges Netzwerkkabel
- Jedes Gerät, das Dante unterstützt, kann mit jedem anderen kommunizieren
- Routing über Software (Dante Controller) – kein physisches Umstecken nötig

### Typisches Dante-Setup:

```
Stagebox (Dante) ────┐
Mischpult (Dante) ───┤── Ethernet-Switch ──── andere Dante-Geräte
Recording-PC (Dante) ┘
```

Alle Geräte sind im selben Netzwerk. Du kannst in der Dante-Controller-Software frei bestimmen, welches Signal von welchem Gerät auf welches andere geht.

### Dante vs. analoge Stagebox:

| | Analoge Stagebox | Dante |
|--|-----------------|-------|
| Kabel | Dickes Multicore | Normales Netzwerkkabel |
| Kanalanzahl | Begrenzt (max. ca. 64) | Hunderte möglich |
| Geräte-Kompatibilität | Herstellerspezifisch | Geräteunabhängig (alle Dante-Geräte) |
| Einrichtung | Plug and Play | Erfordert Konfiguration |
| Kosten | Einstieg günstig | Teure Einstiegshürde |

---

## 11.3 Funkmikrofone

**Funkmikrofone** (Wireless-Systeme) ermöglichen das Singen und Spielen ohne Kabel. Der Sänger kann sich frei auf der Bühne bewegen.

### Aufbau eines Funksystems:

```
Mikrofon/Sender (Transmitter)  →  [Funk]  →  Empfänger (Receiver)  →  Mischpult
```

- **Handsender:** Mikrofon mit integriertem Sender (Batterie im Griffstück)
- **Bodypack-Sender:** Kleines Gerät am Gürtel, das Headset oder Lavalier-Mikrofon sendet
- **Empfänger:** Gerät im Rack, das das Funksignal empfängt und als XLR-Signal ausgibt

### Frequenzbänder:

Funkmikrofone arbeiten in bestimmten Frequenzbändern (UHF, VHF). In Deutschland ist nicht jede Frequenz frei nutzbar – manche Frequenzbereiche sind für Behörden oder Mobilfunk reserviert.

**Wichtig:** Verwende nur Systeme, die für Deutschland zugelassen sind (UHF-Bereich: 470–694 MHz ist aktuell für Funkmikrofone nutzbar, aber sich verändernder Rechtslage – immer prüfen!).

### Worauf du achten musst:

- **Batteriezustand:** Funkmikrofone brauchen Strom. Immer vor dem Konzert frische Batterien oder geladene Akkus einsetzen. Niemals alte Batterien riskieren.
- **Frequenz-Koordinierung:** Mehrere Systeme gleichzeitig dürfen sich nicht gegenseitig stören. Jedes System braucht eine eigene Frequenz.
- **Latenz:** Funkmikrofone haben eine kleine Verzögerung (2–5 ms) – meist nicht hörbar.
- **Dropout:** Wenn Sender und Empfänger sich nicht mehr "sehen", gibt es kurze Tonaussetzer. Antennen richtig positionieren!

### Antennenpositionen:

- Antennen des Empfängers sollen möglichst in Sichtlinie zum Sender stehen
- Nicht hinter Metallstrukturen verstecken
- Bei großen Bühnen: Antennen-Splitter mit aktiven Antennen auf der Bühne platzieren

---

## 11.4 RF-Grundlagen

**RF** steht für *Radio Frequency* – also Funkfrequenz. Für den Umgang mit Funkmikrofonen solltest du Grundbegriffe kennen.

### Wichtige Begriffe:

**Frequenz (MHz/GHz):** Auf welcher Frequenz sendet das Funkmikrofon? Verschiedene Systeme brauchen verschiedene Frequenzen.

**Intermodulation:** Wenn mehrere Funksysteme gleichzeitig betrieben werden, können durch Wechselwirkungen neue, störende Frequenzen entstehen. Professionelle Koordinierungs-Software berechnet störungsfreie Frequenzkombinationen.

**Diversity:** Gute Funksysteme haben zwei Antennen und wählen automatisch das bessere Signal aus (Diversity-Empfänger). Das reduziert Dropouts.

**RSSI (Received Signal Strength Indicator):** Die Signalstärke zwischen Sender und Empfänger. Am Empfänger als Balken angezeigt. Je voller der Balken, desto stabiler die Verbindung.

### Koordinierung mehrerer Funksysteme:

Wenn du 4 Funkmikrofone gleichzeitig nutzt, musst du sicherstellen, dass sich die Frequenzen nicht gegenseitig stören. Software wie **Sennheiser Wireless Systems Manager** oder **Shure Wireless Workbench** hilft dabei, störungsfreie Frequenzkombinationen zu berechnen.

---

## 11.5 Stromversorgung & Sicherheit

Strom ist die Grundlage von allem. Probleme mit der Stromversorgung können das Konzert ruinieren oder im schlimmsten Fall gefährlich sein.

### Grundlagen:

**Sicherung (Fuse):** Jeder Stromkreis hat eine Sicherung. Wenn zu viele Geräte an einem Stromkreis hängen und zu viel Strom fließt, löst die Sicherung aus. Das schützt die Kabel vor Überhitzung.

**Wie viel Strom verbraucht mein Equipment?**

Auf jedem Gerät steht: Leistungsaufnahme in Watt (W). Ein Stromkreis liefert in der Regel 16 Ampere bei 230 Volt = 3.680 Watt. Teile die gesamten Watt aller Geräte durch 3.680 – wenn mehr als 80% ausgenutzt sind, lieber auf zwei Kreise aufteilen.

**Verteilerdosen und Strom-Management:**

- Profi-Stromverteiler (PDU = Power Distribution Unit) haben eigene Sicherungen pro Ausgang
- Nie zu viele Geräte auf einen Verteiler – Überlastung ist Brandgefahr
- Strom-Kabel von Audio-Kabeln getrennt verlegen (Einstreuungen!)

### Sicherheitsregeln:

> ⚠️ **Das folgende ist ernst gemeint:**

- **Defekte Kabel und Geräte sofort aus dem Betrieb nehmen** – defekte Isolation = Lebensgefahr
- **Keine nassen Hände an Stecker** – Strom und Feuchtigkeit ist lebensgefährlich
- **Geräte nicht öffnen** – selbst wenn sie kaputt sind. Das ist Sache von Fachleuten.
- **Schutzerdung (PE) nicht überbrücken** – der Schutzleiter (gelb-grünes Kabel) schützt dich bei einem Kurzschluss
- **Im Notfall: Strom abschalten** – kein Gerät ist es wert, jemanden zu verletzen

### Masseschleifen (Ground Loops):

Wenn zwei Geräte aus verschiedenen Steckdosen (oder verschiedenen Phasen) Strom beziehen und miteinander verbunden sind, kann ein Brummen entstehen (50 Hz oder 100 Hz). Das heißt **Ground Loop** (Masseschleife).

**Lösung:** DI-Box mit Ground-Lift verwenden. Der Ground-Lift trennt die Masseverbindung des Audiosignals und unterbricht die Schleife.

---

## 11.6 Phasenprobleme

**Phase** (Polarität) beschreibt, ob eine Schallwelle oder ein elektrisches Signal in die "richtige" oder "umgekehrte" Richtung schwingt.

### Wie entstehen Phasenprobleme?

Wenn zwei Mikrofone dasselbe Signal aufnehmen (z.B. Snare oben und unten), aber eines ist umgekehrt verdrahtet, heben sich die Signale teilweise auf. Der Bass wird dünn, das Signal klingt "hohl".

### Wann treten Phasenprobleme auf?

- **Snare-Mikrofon oben/unten** – klassischer Fall (immer Phase drehen bei einem der beiden)
- **Zwei Mikrofone auf einem Amp** – wenn sie unterschiedlich weit entfernt sind, kommt der Schall zu verschiedenen Zeiten an
- **DI + Amp gleichzeitig** – Phase kann sich canceln
- **Defektes Kabel** (Pin 2 und 3 vertauscht) – Signal ist phasenverdreht

### Phasenprobleme erkennen:

- Der Bass "verschwindet" wenn du zwei Mikrofone zusammen öffnest
- Sound klingt "dünn", "hohl", "weit weg"
- Wenn du ein Mikrofon muted, klingt der Rest besser

**Test:** Schalte die Phase (Polarity) eines der beiden Kanäle um. Wenn es besser klingt – Problem gefunden!

### Laufzeit-Phase (Time Alignment):

Wenn zwei Lautsprecher unterschiedlich weit von einem Mikrofon entfernt sind, kommt der Schall aus dem entfernteren Lautsprecher etwas später an. Das erzeugt auch Phasenproblem.

**Lösung:** Den entfernteren Lautsprecher mit einem Delay versehen, damit beide Signale gleichzeitig ankommen.

---

## 11.7 Delay & Laufzeiten

**Laufzeit** (Time Delay) ist die Zeit, die Schall braucht, um von einem Ort zum anderen zu gelangen. Schall bewegt sich mit 343 m/s.

### Warum ist das für den Tontechniker wichtig?

**Beispiel:** Du hast Hauptlautsprecher links/rechts der Bühne und Delay-Speaker 20 Meter weiter hinten im Publikum.

```
Haupt-PA    Delay-Speaker
(Bühne)     (20m dahinter)
  ↓              ↓
Publikum    Publikum (hinten)
```

Wenn beide Lautsprecher gleichzeitig spielen, hört das hintere Publikum den Delay-Speaker zuerst und dann (ca. 58 ms später) den Schall von der Haupt-PA. Das klingt falsch – wie ein Echo.

**Lösung:** Den Delay-Speaker um 58 ms verzögern (20m ÷ 343 m/s ≈ 58 ms). Jetzt kommen beide Signale gleichzeitig an.

### Delay berechnen:

```
Delay (ms) = Abstand (m) × 1000 ÷ 343
```

Beispiel: 15 m Abstand → 15 × 1000 ÷ 343 ≈ 44 ms Delay

**Tipp:** Haas-Effekt (kurzes Delay bis 40 ms) lässt den Schall so wirken, als käme er von der früheren Quelle. Nutze dieses Wissen für natürlich klingende Delay-Speaker.

---

## 11.8 Systemverkabelung

Bei professionellen Live-Gigs gibt es viel mehr Verkabelung als beim Bandauftritt. Hier lernst du, wie ein professionelles System strukturiert ist.

### Typisches Systemdiagramm für einen mittleren Gig:

```
BÜHNE
┌─────────────────────────────────────────────────────────────────────┐
│  Stage Box         Monitorverstärker       Effekte
│  (Stagebox)        (Mon-Amp)               (Rack)
│   ↑ ↑               ↑ ↑                     ↑
│  XLR-In            Aux 1–4                  Aux 5–6
│  (Mikrofone)        ↓ ↓                      ↓
│                    Wedge-Monitore          Reverb → Return
│
│              Multicore / Digitalsnake
└──────────────────────┬──────────────────────────────────────────────┘
                       ↓
PUBLIKUMSBEREICH
┌─────────────────────────────────────────────────────────────────────┐
│  Mischpult (FOH)
│   ↓ L/R
│  Systemcontroller / DSP
│   ↓ HF   ↓ LF
│  HF-Amp  LF-Amp
│   ↓        ↓
│  Tops    Subwoofer
└─────────────────────────────────────────────────────────────────────┘
```

### Rack-System (Rack = Einschubrahmen für Geräte):

Professionelle Geräte werden in **19-Zoll-Racks** eingebaut. Ein Rack enthält:
- Systemcontroller / DSP (Frequenzweiche, EQ, Limiter, Delay)
- Endstufen
- Strom-Verteiler (PDU)
- Patchbay (alle Verbindungen zentral)

### Wichtige Kabel-Tipps für den Aufbau:

- **Strom und Audio trennen** – Stromkabel nicht neben Audiokabel verlegen
- **Kabel sichern** – Klettverschlüsse, keine losen Kabel auf dem Boden (Stolperfalle!)
- **Beschriftung** – Jedes Kabel beschriften, dann ist Fehlersuche einfach
- **Sicherheitsreserven** – Genug Kabellänge, damit kein Kabel straff gespannt ist

---

## Zusammenfassung Kapitel 11

- **Digitalsnake:** Ersetzt das analoge Multicore durch ein digitales Netzwerkkabel
- **Dante:** Hersteller-unabhängiges Audio-over-IP-Protokoll für bis zu hunderte Kanäle
- **Funkmikrofone:** Sender + Empfänger, Batteriepflege, Frequenz-Koordination
- **RF:** Signalstärke, Diversity, Intermodulation – Grundbegriffe für Funk-Management
- **Strom:** Sicherheitsregeln ernst nehmen, Masseschleifen mit Ground-Lift lösen
- **Phase:** Polarity-Taste nutzen, Phasenprobleme erkennst du am "hohlen" Klang
- **Delay:** Schallgeschwindigkeit = 343 m/s; Delay-Speaker brauchen Laufzeitkorrektur
- **Systemverkabelung:** Trennung von Strom und Audio, sauberes Rack-System

---

*Weiter geht es in Kapitel 12: Soft Skills & Arbeitsweise*
