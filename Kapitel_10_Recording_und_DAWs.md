# Kapitel 10: Recording & DAWs

> **Von der Bühne ins Studio.**
> Nicht alles, was ein Tontechniker tut, passiert live. Aufnahmen, Proberaum-Mitschnitte, Click-Tracks für die Band – all das ist Teil des Jobs. In diesem Kapitel lernst du die Grundlagen des Aufnehmens mit einem Computer.

---

## 10.1 Grundlagen von DAWs

**DAW** steht für *Digital Audio Workstation* – das ist die Software auf deinem Computer, mit der du Musik aufnimmst, bearbeitest und abmischst.

### Was kann eine DAW?

- Mehrere Spuren gleichzeitig aufnehmen (Multitrack-Recording)
- Aufnahmen anhören, schneiden, arrangieren
- EQ, Kompressor, Reverb und viele andere Effekte als Plugins hinzufügen
- Fertige Mischung als MP3 oder WAV exportieren

### Bekannte DAWs:

| DAW | Betriebssystem | Preis | Einsatz |
|-----|---------------|-------|---------|
| **Reaper** | Windows / Mac | günstig (~60€) | Sehr beliebt, flexibel |
| **GarageBand** | Mac / iOS | Kostenlos | Einsteiger auf Apple |
| **Logic Pro** | Mac | ~230€ | Professionell, Apple |
| **Cubase** | Windows / Mac | mittel–teuer | Studio, professionell |
| **Ableton Live** | Windows / Mac | mittel–teuer | Elektronische Musik, Live-Performance |
| **Pro Tools** | Windows / Mac | teuer (Abo) | Industrie-Standard im Studio |

**Für den Anfang empfohlen:** GarageBand (kostenlos auf Mac) oder Reaper (günstig, sehr mächtig).

### Die Grundoberfläche einer DAW:

```
┌─────────────────────────────────────────────────────┐
│  Transport (Play / Stop / Record / Rewind)          │
├─────────────────────────────────────────────────────┤
│  Spur 1: Kick     ████░░░░████░░░░████░░░░          │ ← Audio-Wellenform
│  Spur 2: Snare    ░░██░░░░░░██░░░░░░██░░░░          │
│  Spur 3: Gesang   ░░░░████████████████░░░░          │
│  Spur 4: Gitarre  ████████████████████████          │
├─────────────────────────────────────────────────────┤
│  Mixer (Fader, EQ, Insert, Send für jede Spur)     │
└─────────────────────────────────────────────────────┘
```

---

## 10.2 Audiointerfaces

Ein **Audiointerface** ist das Bindeglied zwischen Mikrofonen/Instrumenten und dem Computer. Es wandelt das analoge Audiosignal in digitale Daten um (ADC) und umgekehrt (DAC).

### Was macht ein Audiointerface?

- **Eingang:** XLR/Klinke → Analog-Digital-Wandlung → Computer (USB/Thunderbolt)
- **Ausgang:** Computer → Digital-Analog-Wandlung → Monitorlautsprecher / Kopfhörer

### Wichtige Merkmale:

- **Anzahl der Eingänge:** 2-Kanal-Interface für einfache Aufnahmen; 8+ Kanäle für Multitrack-Aufnahme einer ganzen Band
- **Preamp-Qualität:** Das Interface verstärkt das Mikrofonsignal – Qualität des Preamps beeinflusst den Sound
- **Phantomspannung:** Für Kondensatormikrofone
- **Latenz:** Je niedriger, desto besser (besonders beim Einspielen – du willst dich ohne spürbare Verzögerung hören)

### Beliebte Einsteiger-Interfaces:

| Modell | Eingänge | Preis (ca.) |
|--------|---------|------------|
| Focusrite Scarlett 2i2 | 2 | ~150€ |
| Focusrite Scarlett 4i4 | 4 | ~200€ |
| Behringer UMC404HD | 4 | ~80€ |
| SSL 2+ | 2 | ~200€ |

---

## 10.3 Spuren aufnehmen

Das Aufnehmen in der DAW folgt einem klaren Ablauf.

### Schritt-für-Schritt: Aufnahme starten

**1. Interface verbinden und konfigurieren**
- Interface per USB/Thunderbolt an den Computer
- DAW öffnen
- In den DAW-Einstellungen das Interface als Audio-Gerät auswählen

**2. Neue Spur erstellen**
- In der DAW: "Neue Spur" (New Track) → "Audio-Spur"
- Eingangs-Quelle auswählen (z.B. "Input 1" für Mikrofon an Buchse 1)

**3. Monitoring einstellen**
- "Input Monitoring" aktivieren → du hörst dich beim Spielen/Singen in Echtzeit
- Vorsicht: Wenn Lautsprecher offen sind, kann Feedback entstehen

**4. Pegel prüfen**
- Musiker spielen/singen, Eingang prüfen: Pegelanzeige soll –6 bis –3 dBFS erreichen, nicht clippen

**5. Aufnahme starten (Record)**
- Record-Arm (Aufnahme-bereit) für die Spur aktivieren (rote Taste)
- Gesamte Aufnahme mit dem Transport-Regler starten

**6. Abhören**
- Aufnahme stoppen, sofort anhören
- Gibt es Probleme? Nochmal aufnehmen.

### Mehrspur-Aufnahme

Wenn du mehrere Spuren gleichzeitig aufnimmst (z.B. Drums mit 8 Mikrofonen):
- Du brauchst ein Interface mit genug Eingängen (oder ein Mischpult mit USB-Multitrack-Ausgang)
- Jedes Mikrofon = eine Spur in der DAW
- Alle Spuren gleichzeitig auf Record-Arm setzen

---

## 10.4 Editing

Nachdem du aufgenommen hast, bearbeitest du die Aufnahmen (Editing).

### Typische Editing-Aufgaben:

**Schneiden (Cutting/Trimming)**
Überflüssige Stellen (z.B. Rauschen vor dem Einsatz) herausschneiden. In der DAW: Schnitt-Werkzeug (Schere) wählen, klicken.

**Verschieben**
Aufnahme-Clips an die richtige Zeitposition schieben. Wichtig für Timing-Korrekturen.

**Fade In / Fade Out**
Anfang und Ende einer Aufnahme sanft ein- bzw. ausblenden. Verhindert Knackgeräusche.

**Normalisieren**
Den lautesten Punkt einer Aufnahme auf 0 dBFS bringen. Macht leise Aufnahmen lauter.

**Comp-Editing (Comping)**
Du nimmst mehrere Takes (Durchläufe) auf und wählst die besten Passagen aus verschiedenen Takes aus und kombinierst sie zu einem "Comp-Take".

### Sauberes Editing = halbe Arbeit beim Mischen

Je sauberer und sorgfältiger du editierst, desto einfacher wird es, den Mix zu erstellen. Rauschen, unnötige Frequenzen, schlechte Aufnahmen – alles kostet Zeit beim Mixen.

---

## 10.5 Plugins

**Plugins** sind Software-Werkzeuge, die du in der DAW auf einzelne Spuren oder den Gesamtmix anwendest. Sie entsprechen den Hardware-Geräten aus der analogen Welt.

### Arten von Plugins:

| Plugin-Typ | Funktion | Analoges Äquivalent |
|-----------|---------|-------------------|
| EQ-Plugin | Klangformung | Analoger EQ |
| Kompressor-Plugin | Dynamikbearbeitung | Analoger Kompressor |
| Reverb-Plugin | Hall-Effekt | Hallgerät |
| Delay-Plugin | Echo-Effekt | Delay-Gerät |
| Gate-Plugin | Noise Gate | Analoges Gate |
| De-Esser-Plugin | Zischlaut-Kontrolle | De-Esser |
| Limiter-Plugin | Schutz vor Clipping | Limiter |
| Chorus/Flanger | Modulationseffekte | Effektgerät |

### Einbindung in die DAW:

Plugins werden als **Insert** direkt in den Signalfluss einer Spur eingebunden (Signal geht durch das Plugin) oder als **Send/Return** (Signal wird anteilig auf einen Effektbus geschickt).

**Gratis-Plugins für den Anfang:**

- **TDR Nova** (EQ, parametrisch – kostenlos)
- **MCompressor** von MeldaProduction (kostenlos)
- **Valhalla Supermassive** (Reverb – kostenlos, sehr gut!)
- **OJI Audio** (verschiedene kostenlose Tools)

---

## 10.6 Export & Formate

Wenn der Mix fertig ist, exportierst du ihn als Audio-Datei.

### Typische Formate:

| Format | Qualität | Dateigröße | Einsatz |
|--------|---------|-----------|--------|
| **WAV** | Verlustfrei (lossless) | Groß | Master, Archivierung |
| **AIFF** | Verlustfrei | Groß | Mac-Standard, wie WAV |
| **MP3** | Verlustbehaftet | Klein | Online, Streaming, Sharing |
| **FLAC** | Verlustfrei, komprimiert | Mittel | Archivierung, qualitätsbewusste Hörer |
| **AAC** | Verlustbehaftet | Klein | Apple, Streaming |

### Empfohlene Export-Einstellungen:

**Für Archivierung (Mastering-Qualität):**
- Format: WAV
- Auflösung: 24 Bit
- Sample Rate: 48.000 Hz (48 kHz)

**Für Sharing / Online:**
- Format: MP3
- Bitrate: 320 kbps
- Sample Rate: 44.100 Hz (44.1 kHz – CD-Standard)

### Was bedeuten Bit und Sample Rate?

- **Sample Rate (Abtastrate):** Wie oft pro Sekunde das Signal "abgetastet" wird. 44.1 kHz = 44.100 mal pro Sekunde. Mehr = bessere Qualität, aber größere Datei.
- **Bit-Tiefe:** Wie genau jede Abtastung gemessen wird. 16 Bit = CD-Qualität, 24 Bit = Studio-Qualität.

---

## 10.7 Clicktracks & Playbacks

Beim Live-Sound werden zunehmend **Clicktracks** und **Playbacks** eingesetzt. Als Tontechniker musst du wissen, was das ist und wie du damit umgehst.

### Clicktrack (Metronom-Klick)

Ein **Clicktrack** ist ein elektronisches Metronom-Signal, das der Schlagzeuger (und manchmal andere Musiker) über In-Ear-Monitore hört.

**Warum Clicktrack?**
- Band spielt im Takt zusammen, auch bei großen Bühnen
- Ermöglicht das Einspielen von Playbacks (Hintergrundspuren)
- Professionelleres, stabiles Tempo

**Deine Aufgabe:** Den Clicktrack aus der DAW oder einem dedizierten Gerät (z.B. Ableton Live, MIDI-Drumcomputer) in den Monitor-Aux-Weg des Schlagzeugers einspielen. Er darf **niemals** in die FOH-PA kommen!

### Playbacks / Backing Tracks

**Playbacks** sind vorproduzierte Spuren, die beim Live-Konzert als Hintergrund eingespielt werden. Das können sein:

- Synthesizer-Teppiche und Streicher (die live nicht vorhanden sind)
- Chor-Harmonien
- Percussion-Elemente
- Geräuschkulissen und Intros

**Wie werden Playbacks abgespielt?**

- In der Regel über einen Laptop mit Ableton Live oder einer ähnlichen Software
- Der Laptop sendet Audio in das Mischpult (via Interface oder direktem Ausgang)
- Auf einem Kanal landet der Stereo-Playback-Mix, der in den FOH-Mix gemischt wird

**Wichtige Regel:** Immer eine Backup-Lösung haben (zweiter Laptop, USB-Stick). Wenn der Playback-Laptop abstürzt, ist das Konzert in Gefahr.

---

## 10.8 Einfacher Livemitschnitt

Du kannst ein Konzert mit deinem Mischpult direkt auf einen Laptop aufnehmen – das nennt sich **Livemitschnitt** (Live Recording).

### Wie geht das?

**Option 1: Stereo-Aufnahme vom Master-Ausgang**

Das einfachste: Ein Kabel vom "Rec Out" oder "Main Out" des Mischpults geht in ein Audiointerface, und du nimmst in der DAW eine Stereo-Spur auf.

Ergebnis: Du hast die Aufnahme genau so, wie du sie gemischt hast. Kein Nachbearbeiten einzelner Spuren möglich.

**Option 2: Multitrack-Aufnahme**

Viele digitale Mischpulte können über USB direkt als Interface dienen – jeder Eingangskanal wird als separate Spur aufgenommen.

```
Mischpult → USB → Laptop → DAW (32 Spuren gleichzeitig)
```

Danach kannst du die Spuren nachbearbeiten und einen eigenen Mix erstellen.

**Option 3: Dedizierter Recorder**

Ein Hardware-Multitrack-Recorder (z.B. TASCAM, Zoom) nimmt alle Spuren auf eigene Festplatte auf – ohne Computer.

### Vorbereitung eines Livemitschnitts:

- [ ] Genug Speicherplatz? (1 Stunde, 32 Spuren, 24 Bit = ca. 10–15 GB)
- [ ] Sample Rate stimmt überein (Mischpult und DAW: beide 48 kHz)
- [ ] Testaufnahme vor dem Soundcheck machen
- [ ] Pegelcheck: Eingänge sollen nicht clippen

---

## Zusammenfassung Kapitel 10

- Eine **DAW** ist das Software-Mischpult und Aufnahmegerät auf dem Computer
- Ein **Audiointerface** verbindet Mikrofone/Instrumente mit dem Computer
- Aufnahme-Ablauf: Interface → Neue Spur → Pegel prüfen → Record
- **Editing** = Schneiden, Verschieben, Faden nach der Aufnahme
- **Plugins** sind Software-EQs, Kompressoren, Halls usw.
- **WAV** für Archivierung, **MP3** für Sharing
- **Clicktrack** hört nur der Schlagzeuger – nie in die PA!
- **Livemitschnitt**: Stereo (einfach) oder Multitrack (flexibler)

---

*Weiter geht es in Kapitel 11: Fortgeschrittene Live-Technik*
