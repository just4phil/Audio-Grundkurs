# Kapitel 7: Live-Mixing Grundlagen

> **Von der Theorie in die Praxis.**
> Jetzt kommt alles zusammen. Du weißt, wie Mikrofone funktionieren, wie das Mischpult aufgebaut ist, und wie man hört. In diesem Kapitel lernst du den Ablauf eines echten Live-Gigs – von der Vorbereitung bis zur letzten Note.

---

## 7.1 Vorbereitung einer Probe

Eine gute Vorbereitung ist die halbe Miete. Ein Tontechniker, der unvorbereitet zur Probe erscheint, kostet die ganze Band Zeit.

### Checkliste vor der Probe:

**Technische Vorbereitung:**
- [ ] Mischpult eingeschaltet und überprüft
- [ ] Alle Kabel liegen auf den richtigen Wegen
- [ ] Stagebox verbunden, Multicore ausgelegt
- [ ] Mikrofone auf Ständern, in richtiger Position
- [ ] Endstufen / PA-Boxen eingeschaltet (in richtiger Reihenfolge!)
- [ ] Monitore aufgestellt und verkabelt
- [ ] Kopfhörer am Pult angesteckt (für Solo/PFL)

**Einschaltreihenfolge – sehr wichtig!**

Die korrekte Einschaltreihenfolge verhindert laute Knackgeräusche und schützt Lautsprecher:

```
EINSCHALTEN:
1. Mischpult
2. Effektgeräte / Systemcontroller
3. Endstufen / aktive Lautsprecher   ← als letztes!

AUSSCHALTEN:
1. Endstufen / aktive Lautsprecher   ← als erstes!
2. Effektgeräte / Systemcontroller
3. Mischpult
```

> ⚠️ **Merksatz:** "Last on, first off" – Die Lautsprecher kommen zuletzt an und gehen zuerst aus.

**Vorbereitung des Mischpultes:**
- Alle Fader auf 0 dB (Nullposition)
- Alle EQ-Regler zurücksetzen (flach)
- Gain-Regler auf Minimum
- Alle Aux-Sends auf Null
- Phantomspannung aus (bis Mikrofone angeschlossen)

---

## 7.2 Line Check

Bevor die Musiker auf der Bühne sind, machst du einen **Line Check** – du überprüfst, ob alle Kabel und Verbindungen funktionieren.

### Wie läuft ein Line Check ab?

1. **Kanal für Kanal überprüfen** – solo-abhören, ob Signal ankommt
2. **Nicht drauf klopfen!** – Auf ein Mikrofon zu hauen, um es zu testen, ist ein Ammenmärchen und schlecht für die Kapsel. Einfach sanft reinblasen oder sprechen.
3. **Phantom an den richtigen Stellen aktivieren**
4. **Stumme Kanäle überprüfen** – manchmal ist der Mute-Button versehentlich aktiv

### Typische Probleme beim Line Check:

| Problem | Ursache | Lösung |
|---------|---------|--------|
| Kein Signal auf Kanal 3 | Kabel defekt, Stagebox-Kanal falsch | Kabel tauschen, Routing prüfen |
| Brummen auf Kanal 7 | Masseschleife | Ground-Lift an DI-Box aktivieren |
| Signal sehr leise | Gain zu niedrig, falscher Eingang | Gain hochdrehen, Eingangstyp prüfen (Mic/Line) |
| Alle Kanäle kein Ton | Master-Fader unten, PA aus | Master prüfen, PA einschalten |

---

## 7.3 Soundcheck

Der **Soundcheck** ist die wichtigste Phase vor dem Konzert. Hier stellst du alles ein, damit das Konzert gut klingt.

### Reihenfolge beim Soundcheck:

**1. Einzeln einpegeln (Instrument für Instrument)**

Starte mit dem Instrument, das das Fundament des Sounds bildet:

```
1. Kick Drum → Gain einstellen, EQ grob
2. Snare
3. Hi-Hat
4. Toms
5. Overhead
6. Bass (DI oder Mikrofon)
7. Gitarre(n)
8. Keyboard / Sonstige
9. Gesang(smikrofone)
```

**2. Gruppen-Check**

Höre alle Drums zusammen – klingt das kohärent? Dann Bass dazu. Dann alles zusammen.

**3. Monitor-Mix einstellen**

Frage jeden Musiker, was er braucht:
- "Was willst du lauter/leiser?"
- "Fehlst dir etwas im Monitor?"

Gehe dabei ruhig und geduldig vor. Jeder Musiker hat andere Bedürfnisse.

**4. Gesamtmix abhören**

Höre alle Kanäle zusammen. Jetzt geht es um das Gesamtbild:
- Ist die Band ausgewogen? (Drums, Bass, Gitarre, Vocals)
- Versteht man den Gesang?
- Klingt es im Raum gut?

### Goldene Soundcheck-Regeln:

- **Lautsprecher-Check zuerst**, bevor du irgendwas einstellst – PA muss laufen
- **Musiker spielen wie beim Konzert** – wenn die Gitarre beim Soundcheck leise gespielt wird, passt der Mix beim Konzert nicht mehr
- **Monitor-Mix zuerst, bevor du FOH-Mix machst** – glückliche Musiker spielen besser
- **Notizen machen** – schreibe auf, was du eingestellt hast (besonders Gain-Werte)

---

## 7.4 Vocals verständlich mischen

Der Gesang ist in den meisten Bands das Wichtigste im Mix. Das Publikum will den Sänger hören und verstehen. Gesang muss immer oben im Mix "sitzen".

### Das Problem: Gesang kämpft gegen alles

Gitarren, Keyboards, Schlagzeug – alle belegen Frequenzen, die auch der Gesang braucht (Mitten und Obere Mitten). Dieser Kampf um Frequenzraum ist die Hauptherausforderung beim Mischen.

### Techniken für verständlichen Gesang:

**1. Platz schaffen ("Schnitt")**

Senke bei anderen Instrumenten die Frequenzen, die der Gesang braucht (2–5 kHz), leicht ab. Besonders bei Gitarren.

**2. Gesang in den Vordergrund EQen**

- Kleiner Boost bei 2–4 kHz: Verständlichkeit, Präsenz
- HPF aktivieren (ca. 100 Hz): Tiefes Plosivgeräusch und Bühnengrollen entfernen
- Bei nasalem Klang: Leichter Cut bei 500–800 Hz

**3. Kompression auf dem Gesang**

Gesang hat eine sehr hohe Dynamik. Ein sanfter Kompressor (Ratio 3:1–4:1) sorgt dafür, dass laute und leise Passagen gleichmäßiger klingen.

**4. Etwas Hall / Delay**

Ein kurzes Room-Reverb oder Pre-Delay macht den Gesang runder und lässt ihn weniger "nackt" klingen. Nicht zu viel!

**5. Pan: Mitte**

Lead-Gesang immer in die Mitte. Ausnahmen (z.B. Backing-Vocals) können leicht links/rechts gesetzt werden.

### Typische Gesangs-Probleme:

| Problem | Lösung |
|---------|--------|
| Zu undeutlich/leise | Gain prüfen, 2–4 kHz leicht boosten |
| Zu dominant/schrill | 3–5 kHz senken |
| Zu "dumpf" | HPF an, 2–4 kHz etwas boosten |
| Zischende S-Laute | De-Esser oder manuellen Cut bei 7–9 kHz |
| "Ploppt" bei P und B | HPF oder Mikrofon-Winkel ändern |

---

## 7.5 Balance im Bandmix

Eine gute **Balance** bedeutet: Alle Instrumente haben ihren Platz im Mix und keines übertönt das andere unnötig.

### Die Hierarchie im Mix

Es gibt Instrumente, die wichtiger sind als andere:

```
Priorität 1 (wichtigste):  Lead-Gesang
Priorität 2:               Kick Drum, Snare, Bass
Priorität 3:               Gitarren, Keyboard
Priorität 4:               Hi-Hat, Overhead, Percussion
```

Stelle die wichtigsten Elemente zuerst ein und füge dann die anderen drum herum.

### Schritt-für-Schritt Balance einstellen:

1. Alle Fader auf –∞ (ganz unten)
2. Kick Drum auf einen angenehmen Pegel ziehen
3. Snare dazu – so, dass sie zur Kick passt
4. Bass dazu – Fundament aufbauen
5. Drums und Bass zusammen beurteilen
6. Gesang dazu – deutlich hörbar, Hauptfokus
7. Gitarren dazu – Füllung ohne zu übertönen
8. Alle anderen Instrumente dazu

### Häufige Balance-Fehler:

- **Zu viel Bass/Kick:** Mix klingt wummrig, undeutlich
- **Zu wenig Gesang:** Das Wichtigste geht unter
- **Gitarre übertönt alles:** Besonders bei Bands mit lauten Gitarristen
- **Alle Fader voll oben:** Dann kannst du bei Bedarf nichts mehr lauter machen

> 💡 **Trick:** Stelle dir vor, der Mix ist ein Gemälde. Der Gesang ist das Motiv in der Mitte (Vordergrund), die Instrumente sind der Hintergrund. Alles muss zusammenpassen – nichts darf "rausspringen" außer dem Gesang.

---

## 7.6 Arbeiten unter Zeitdruck

Live-Sound bedeutet Zeitdruck. Ein Soundcheck hat 20 Minuten, es gibt technische Probleme, und der Sänger kommt zu spät. Das ist normal – du musst damit umgehen können.

### Prioritäten setzen beim Schnell-Soundcheck:

Wenn du nur 10 Minuten hast:

1. **Kick + Snare + Bass** → Rhythmisches Fundament (3 Minuten)
2. **Gesang** → Das Wichtigste für das Publikum (3 Minuten)
3. **Monitore** → Musiker müssen sich hören (3 Minuten)
4. **Rest** → Gitarren, Overhead, Sonstiges schnell einpegeln (1 Minute)

Was du weglässt: Feine EQ-Justierungen, perfekte Balance, Effekte. Das kommt, wenn Zeit ist.

### Ruhe bewahren

Unter Zeitdruck machen viele Anfänger Fehler, weil sie hektisch werden:
- Mehrere Dinge gleichzeitig versuchen
- Kabel ohne Nachdenken einstecken
- Regler verstellen, ohne zu wissen, warum

**Lösung:** Atmen. Einen Schritt nach dem anderen. Ein Problem nach dem anderen lösen.

> 💡 **Profi-Tipp:** Lerne, den Soundcheck immer in derselben Reihenfolge zu machen. Eine feste Routine hilft dir, auch unter Druck systematisch zu bleiben.

---

## 7.7 Fehlerdiagnose im Livebetrieb

Während des Konzerts kann immer etwas schiefgehen. Kein Ton, plötzliches Feedback, Brummen – das muss du schnell und ruhig lösen.

### Diagnose-Schema: Kein Ton auf einem Kanal

```
Kein Ton?
    │
    ├── Kanal gemuted?  → Mute aufheben
    │
    ├── Fader unten?  → Fader hochziehen
    │
    ├── Gain auf Null?  → Gain einstellen
    │
    ├── Kabel defekt?  → Kabel tauschen
    │
    ├── Phantomspannung an? (wenn Kondensatormikrofon) → +48V aktivieren
    │
    └── Eingang richtig konfiguriert? (Mic vs. Line) → Eingang prüfen
```

### Diagnose-Schema: Plötzliches Brummen

```
Brummen?
    │
    ├── Neues Kabel gerade eingesteckt? → Kabel auf Masseschleife prüfen
    │
    ├── Gerät gerade angeschaltet? → Ground-Lift an DI-Box probieren
    │
    ├── Lichtsystem verändert? → Dimmer erzeugen oft Einstreuungen
    │
    └── Kabel nahe Stromkabeln? → Kabel verlegen
```

### Diagnose-Schema: Feedback

```
Feedback?
    │
    ├── Kanal muten / Gain runter → sofortige Lösung
    │
    ├── Mikrofon zu nah am Monitor? → Abstand vergrößern
    │
    ├── Monitor-Mix zu laut? → Aux-Master senken
    │
    └── Bestimmte Frequenz? → Am EQ senken
```

### Während du ein Problem löst:

- **Kommuniziere mit der Band** – kurzes Handzeichen "einen Moment"
- **Panic nicht** – ruhige Analyse ist schneller als hektisches Probieren
- **Notfall-Plan:** Wenn du es nicht schnell lösen kannst, den Kanal muten und später in Ruhe lösen

---

## 7.8 Notfallmanagement

Manche Probleme sind größer als ein defektes Kabel. Hier sind Szenarien und was du tun kannst.

### Szenario: Kompletter Ausfall eines PA-Zweigs

Wenn ein Lautsprecher plötzlich ausfällt:
1. Überprüfe Kabel und Stecker
2. Überprüfe Endstufe (Clip-LED, Schutzschaltung?)
3. Notbetrieb: Restliches System lauter stellen
4. Wenn möglich: Ersatzlautsprecher

### Szenario: Mischpult-Ausfall / Stromausfall

1. Ruhig bleiben – Panik hilft nicht
2. Strom prüfen (Sicherungen, Verteiler)
3. Wenn Mischpult ausgefallen: War es ein Überhitzungsproblem? Kurz abwarten.
4. Notbetrieb: Direkte Verbindung Instrument → Lautsprecher (ohne Mischpult) – limitiert, aber Konzert kann weitergehen

### Szenario: Mikrofon fällt aus (Funkmikrofon / technisches Problem)

1. Ersatzmikrofon bereithalten (immer!)
2. Schnell tauschen
3. Kanal-Einstellungen merken (Gain, EQ) – diese sind auf das spezifische Mikrofon abgestimmt, aber als Ausgangspunkt gut

### Vorbereitung ist das beste Notfallmanagement

- **Ersatzkabel** bereithalten (mindestens 2 XLR-Kabel)
- **Ersatzmikrofon** griffbereit
- **Kabeltester** immer dabei
- **Notebook** mit allen wichtigen Einstellungen
- **Werkzeug** (Schraubenzieher, Multimeter) in der Tasche

> 💡 **Profi-Mentalität:** Ein Problem ist nicht die Frage "ob" – sondern "wann". Sei vorbereitet. Ein gut vorbereiteter Tontechniker löst 80% der Probleme, bevor sie das Publikum bemerkt.

---

## Zusammenfassung Kapitel 7

**Der Ablauf eines Live-Gigs:**

```
Aufbau → Line Check → Soundcheck (Instrumente) → Monitor-Mix → FOH-Mix → Konzert → Abbau
```

**Wichtigste Merksätze:**

- Einschalten: Mischpult zuerst, Lautsprecher zuletzt. Ausschalten umgekehrt.
- Soundcheck: Immer in der gleichen Reihenfolge – von unten (Kick) nach oben (Vocals)
- Gesang ist König: Er muss immer verständlich und klar vorne sitzen
- Balance: Zuerst Kick + Snare + Bass + Vocals, dann der Rest drum herum
- Unter Zeitdruck: Prioritäten setzen – Pflicht vor Kür
- Fehlerdiagnose: Systematisch von vorne nach hinten im Signalfluss denken
- Notfall: Ruhig bleiben, vorbereitet sein, einen Schritt nach dem anderen

---

*Weiter geht es in Kapitel 8: Equalizer & Dynamikbearbeitung*
