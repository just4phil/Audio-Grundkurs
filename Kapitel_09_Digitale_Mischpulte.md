# Kapitel 9: Digitale Mischpulte

> **Der nächste Schritt.**
> Du hast das analoge Handwerk gelernt. Jetzt betrittst du die digitale Welt. Vieles bleibt gleich – Signalfluss, EQ, Kompressor, Aux-Wege – aber die Bedienung ist anders. Und es gibt Möglichkeiten, die analog schlicht nicht existieren.

---

## 9.1 Unterschiede zu Analogpulten

Ein digitales Mischpult macht im Kern dasselbe wie ein analoges – aber auf eine völlig andere Art.

### Was bleibt gleich?

- Gain, EQ, Kompressor, Gate, Aux-Wege, Fader, Pan, Mute – alle diese Konzepte existieren genauso
- Signalfluss-Denken ist identisch
- Gain Staging bleibt wichtig

### Was ist anders?

| Merkmal | Analog | Digital |
|---------|--------|---------|
| Bedienung | Jeder Regler hat eine eigene Funktion | Ein Regler = viele Funktionen (je nach Layer) |
| Einstellungen speichern | Nicht möglich | Szenen / Snapshots speicherbar |
| Routing | Fest verdrahtet | Frei konfigurierbar |
| Kanalanzahl | Physisch begrenzt | Viele Kanäle auf wenig Platz |
| Remote Control | Nicht möglich | Tablet / Laptop als Mischpult |
| Latenz | Keine | Kleine Verzögerung (1–5 ms) |
| Fehler | Ein Regler kaputt = ein Kanal kaputt | Software-Absturz = alles weg |
| Bedienungsphilosophie | Direkt, sichtbar | Menüs, Layer, Bildschirme |

### Der wichtigste Unterschied: Oberfläche vs. Funktion

Bei einem analogen Pult siehst du jeden Regler, der funktioniert. Bei einem digitalen Pult kann ein einziger Bildschirm und ein paar Encoder hunderte Parameter steuern – je nachdem, welchen Layer oder welches Menü du gerade geöffnet hast.

> 💡 **Merke:** Das Wissen aus Kapitel 1–8 ist 100% übertragbar. Der digitale Weg ist nur die Verpackung. Lerne zuerst das analoge Denken, dann ist Digital logisch.

---

## 9.2 Layer & Kanalverwaltung

Das Herzstück der digitalen Bedienung sind **Layer** (Schichten). Da ein digitales Pult oft mehr Kanäle hat als physische Fader, werden Kanäle in Schichten organisiert.

### Was ist ein Layer?

Stell dir vor, du hast 32 Mikrofon-Kanäle, aber nur 16 Fader auf dem Pult. Mit dem **Layer-Button** wechselst du zwischen zwei Seiten:

- **Layer 1:** Kanal 1–16 liegt auf den Fadern
- **Layer 2:** Kanal 17–32 liegt auf denselben Fadern

Durch Drücken des Layer-Buttons wechselst du sofort, welche Kanäle du gerade bedienst.

### Typische Layer-Einteilung:

| Layer | Kanäle |
|-------|--------|
| Layer 1 | Inputs 1–8 (z.B. Drums) |
| Layer 2 | Inputs 9–16 (z.B. Gitarren, Bass) |
| Layer 3 | Inputs 17–24 (z.B. Vocals, Keyboard) |
| Layer 4 | Aux-Master / DCA-Gruppen |

### Was ist ein DCA?

**DCA** steht für *Digitally Controlled Amplifier*. Es ist eine Art Master-Regler für eine Gruppe von Kanälen – ähnlich wie eine Gruppe beim analogen Pult, aber ohne dass das Signal wirklich zusammengelegt wird.

Wenn du z.B. alle Drum-Kanäle einem DCA zuweist, kannst du mit einem einzigen DCA-Fader alle Drums gleichzeitig lauter oder leiser machen – ohne die relativen Verhältnisse zueinander zu verändern.

---

## 9.3 Routing

**Routing** bedeutet beim digitalen Pult: Du entscheidest, welches Signal wohin geht. Das ist viel flexibler als analog.

### Typische Routing-Aufgaben:

**Eingangs-Routing:**
- Welcher physische Eingang (XLR 1 am Stagebox) landet auf welchem Kanal im Pult?
- Beim analogen Pult: fest verdrahtet (Kanal 1 = Buchse 1)
- Digital: Du kannst Eingang 5 auf Kanal 12 legen wenn du willst

**Ausgangs-Routing:**
- Welcher Aux-Weg geht auf welche physische Ausgangsbuchse?
- Welcher Ausgang geht auf welchen Monitor?

**Matrix-Routing:**
Manche Pulte haben eine **Matrix** – ein weiteres Routing-Netz, das nach dem Haupt-Mix sitzt. Damit kann man z.B. einen separaten Mix für eine Aufnahme erstellen, der unabhängig vom FOH-Mix ist.

### Typischer Routing-Plan für eine Band:

```
Stagebox-Eingang  →  Mischpult-Kanal
───────────────────────────────────
XLR 1 (Kick)     →  Kanal 1
XLR 2 (Snare)    →  Kanal 2
XLR 3 (HiHat)    →  Kanal 3
XLR 4 (Tom 1)    →  Kanal 4
XLR 5 (Tom 2)    →  Kanal 5
XLR 6 (OH L)     →  Kanal 6
XLR 7 (OH R)     →  Kanal 7
XLR 8 (Bass DI)  →  Kanal 8
XLR 9 (Gitarre)  →  Kanal 9
XLR 10 (Gesang)  →  Kanal 10

Aux-Ausgang  →  Stagebox-Return  →  Monitor
───────────────────────────────────────────
Aux 1        →  Return 1         →  Monitor Sänger
Aux 2        →  Return 2         →  Monitor Gitarrist
Aux 3        →  Return 3         →  Monitor Schlagzeuger
```

> 💡 **Tipp:** Schreibe deinen Routing-Plan immer auf! Beim nächsten Aufbau sparst du viel Zeit, wenn du weißt, was wo hängt.

---

## 9.4 Szenen & Presets

Das mächtigste Feature digitaler Mischpulte: **Du kannst alle Einstellungen speichern und wieder abrufen.**

### Was ist eine Szene?

Eine **Szene** (auch: Snapshot, Scene, Show File) speichert den kompletten Zustand des Mischpults:

- Alle Gain-Einstellungen
- Alle EQ-Einstellungen auf allen Kanälen
- Kompressor, Gate, De-Esser
- Aux-Sends und Monitor-Mixes
- Routing
- Fader-Positionen
- Mute-Zustände

### Anwendungsbeispiele:

**Zwischen Bands wechseln:**
Beim Festival spielt Band A, dann Band B. Du speicherst für jede Band eine Szene. Wenn Band B auf die Bühne kommt, rufst du ihre Szene auf – und alle Einstellungen sind sofort da.

**Soundcheck und Show:**
Du machst beim Soundcheck alles fertig und speicherst eine Szene. Wenn während des Konzerts etwas durcheinandergerät, kannst du jederzeit auf die Soundcheck-Szene zurückgehen.

**Szene pro Song:**
Manche Techniker speichern für jeden Song eine Szene – bestimmte Songs brauchen z.B. mehr Reverb, andere weniger.

### Presets:

**Presets** sind vorgefertigte Einstellungen für einzelne Kanäle oder Prozessoren:

- Preset "Gesang Niere" → EQ und Kompressor für typischen Gesangskanal
- Preset "Kick Drum" → fertige Einstellung für Kickdrum-Kanal
- Preset "Akustikgitarre DI" → Grundeinstellung für akustische Gitarre über DI

Du kannst eigene Presets erstellen und für kommende Gigs verwenden.

---

## 9.5 Busse & DCAs

Wir kennen Gruppen schon vom analogen Pult. Digital gibt es mehr Möglichkeiten.

### Mix-Busse

Ein **Mix-Bus** ist wie eine Gruppe beim analogen Pult: Mehrere Kanäle werden auf einen gemeinsamen Weg geroutet, und dieser Weg hat seinen eigenen Fader und eigenen EQ/Kompressor.

Typische Mix-Busse:
- **Drum-Bus:** Alle Drum-Kanäle, darauf ein Kompressor für den "Drum-Bus-Crunch"
- **Vocal-Bus:** Alle Vocals zusammen, darauf ein Kompressor und Reverb-Send
- **Guitar-Bus:** Alle Gitarren
- **L/R Master-Bus:** Das Hauptsignal

### DCAs (Digitally Controlled Amplifiers)

DCAs sind keine echten Signalwege – sie sind nur **Fernbedienungen** für Gruppen von Kanälen.

```
DCA 1 (Drums):
  - Kanal 1 (Kick) ─────┐
  - Kanal 2 (Snare) ────┤→ DCA 1-Fader steuert alle gleichzeitig
  - Kanal 3 (HiHat) ────┤   (aber Signal läuft separat weiter)
  - Kanal 6 (OH L) ─────┘
```

**Vorteil gegenüber Mix-Bus:** Jeder Kanal bleibt im Master-Bus separat hörbar und klingbar. Du hast mehr Kontrolle – und kannst z.B. trotzdem die Kick alleine im Master-Bus solieren.

---

## 9.6 Effekte & interne Prozessoren

Digitale Mischpulte haben viele Effekte intern eingebaut – du brauchst keine externen Geräte mehr.

### Typisch eingebaute Effekte:

| Effekt-Typ | Funktion |
|-----------|---------|
| Reverb | Hall – Room, Hall, Plate, Spring |
| Delay | Echo-Effekt, rhythmisch oder atmosphärisch |
| Chorus | Verdickung des Signals |
| Pitch-Shifter | Tonhöhenveränderung |
| Multi-Band Kompressor | Kompressor mit separaten Frequenzbändern |
| Grafik-EQ | 31-Band EQ auf Aux-Wegen |
| Limiter | Schutz vor Übersteuerung |
| De-Esser | Zischlaut-Kontrolle |

### Effekte auf Aux-Wegen (Send/Return):

Wie beim analogen Pult gibst du Effekte über Aux-Sends und empfängst sie auf Return-Kanälen:

```
Kanal (Gesang) → Aux 5 (FX-Send Post-Fader) → Interner Reverb → Return auf Kanal 31/32
```

Der Vorteil: Du kannst von jedem Kanal individuell bestimmen, wie viel in den Reverb geht.

---

## 9.7 Remote Mixing

Einer der größten Vorteile digitaler Mischpulte: Du kannst das Pult **fernbedienen** – mit einem Tablet oder Laptop.

### Typische Remote-Szenarien:

**Tablet am FOH:**
Du stehst im Publikum und mischst über ein iPad. Das Pult steht irgendwo anders (z.B. in einem Rack auf der Bühne). Du bist freier in der Bewegung.

**Monitor-Mixing vom Tablet:**
Der Gitarrist oder Sänger kann seinen eigenen Monitor-Mix selbst einstellen – über eine App auf seinem Smartphone. Du gibst ihm Zugriff auf seinen Aux-Weg.

**Zwei-Mann-Team:**
Einer mischt FOH am Pult, der andere macht Monitor-Mix vom Tablet auf der Bühne.

### Beliebte Remote-Apps:

- **Behringer X32/M32:** "Mixing Station X32" (Android/iOS), "X32-Q"
- **Allen & Heath SQ:** "SQ MixPad"
- **Yamaha:** "StageMix"

### Voraussetzungen:

- Mischpult und Tablet im selben WLAN-Netzwerk
- Stabiler WLAN-Router (kein Consumer-Router für Live-Einsatz – lieber professionelle Lösung)

> ⚠️ **Achtung:** Remote Mixing klingt toll, hat aber Risiken: Verbindungsabbrüche, Latenz, versehentliche Veränderungen. Im Notfall muss jemand am physischen Pult stehen.

---

## 9.8 Typische Routingfehler

Routing-Fehler sind die häufigsten Probleme bei digitalen Mischpulten – und oft schwer zu finden, wenn man nicht weiß, wo man sucht.

### Die häufigsten Routing-Fehler:

**Falscher Eingang zugewiesen:**
Kanal 3 im Pult ist dem Stagebox-Eingang 5 zugewiesen, aber das Gesangsmikrofon steckt in Eingang 3. Resultat: kein Ton auf dem Gesangskanal.

**Lösung:** Eingangs-Routing im Pult prüfen und anpassen.

**Aux-Ausgang geht auf falschen Monitor:**
Monitor für den Sänger spielt den Mix des Gitarristen.

**Lösung:** Ausgangs-Routing der Aux-Wege prüfen.

**Kanal ist nicht im Master-Bus:**
Ein Kanal wurde versehentlich aus dem L/R-Bus herausgeroutet – Signal geht nirgendwo hin.

**Lösung:** Routing des Kanals zum L/R-Bus prüfen.

**Phasendrehung vergessen:**
Beim digitalen Pult kann man die Phase (Polarität) mit einem Klick umdrehen. Wenn du es vergisst (z.B. nach dem Laden einer Szene), gibt es Auslöschungen.

**Diagnosetipp:** Bei Routing-Problemen immer von vorne anfangen:
1. Kommt Signal am Eingang an? (PFL/Solo des Kanals prüfen)
2. Ist Kanal im L/R-Bus?
3. Geht der L/R-Bus zum Ausgang?
4. Geht der Ausgang zur Endstufe/Lautsprecher?

---

## 9.9 Strukturierte Showfiles erstellen

Ein **Showfile** ist die Datei, in der alle Einstellungen für eine Show gespeichert sind – Routing, alle Szenen, Presets, Labels. Es ist dein digitales "Mischpult-Gedächtnis".

### Gutes Showfile-Struktur:

**1. Kanäle beschriften (Labels)**
Gib jedem Kanal einen Namen: "Kick", "Snare", "Gesang 1", "Bass DI" usw. So weißt du sofort, was was ist – auch wenn du das Pult nach Monaten wieder aufmachst.

**2. Farben zuweisen**
Moderne digitale Pulte erlauben Farben für Kanäle:
- Drums: Rot
- Bass: Blau
- Gitarren: Grün
- Vocals: Gelb

**3. Sinnvolle Layer-Einteilung**
Erstelle Layer so, dass zusammengehörige Instrumente immer auf einem Layer liegen.

**4. Szenen anlegen:**
- "Szene 1: Soundcheck"
- "Szene 2: Show Start"
- "Szene 3: Akustik-Set" (falls die Band auch einen ruhigen Teil hat)

**5. Backup erstellen:**
Showfile immer auf USB-Stick sichern! Wenn das Pult abstürzt oder du ein anderes Pult nutzen musst, hast du deine Einstellungen dabei.

---

## Zusammenfassung Kapitel 9

- Digitale Mischpulte machen dasselbe wie analoge – aber flexibler und mit mehr Funktionen
- **Layer:** Viele Kanäle auf wenig Fadern durch Schichtung
- **DCA:** Fernbedienung für Kanalgruppen, kein echter Signal-Zusammenschluss
- **Routing:** Frei konfigurierbar – Eingang auf beliebigen Kanal, Ausgang auf beliebige Buchse
- **Szenen:** Vollständige Speicherung aller Einstellungen → riesiger Vorteil gegenüber analog
- **Remote Mixing:** Tablet steuert das Pult – mehr Flexibilität, aber Risiken beachten
- **Routing-Fehler** sind häufig → systematisch von vorne nach hinten debuggen
- **Showfile-Hygiene:** Kanäle benennen, Farben vergeben, Backup auf USB

---

*Weiter geht es in Kapitel 10: Recording & DAWs*
