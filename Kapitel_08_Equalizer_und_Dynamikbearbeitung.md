# Kapitel 8: Equalizer & Dynamikbearbeitung

> **Die Werkzeuge der Klangformung.**
> EQ und Kompressor sind die zwei wichtigsten Bearbeitungswerkzeuge nach dem Gain. In diesem Kapitel lernst du, wie du sie richtig einsetzt – und vor allem, wann du sie am besten in Ruhe lässt.

---

## 8.1 Grundlagen von EQs

Du hast in Kapitel 4.4 bereits das Grundprinzip des EQs kennengelernt. Jetzt gehen wir tiefer.

### EQ-Arten im Überblick:

**Shelving EQ (Regal-EQ)**

Verstärkt oder senkt alle Frequenzen oberhalb (High Shelf) oder unterhalb (Low Shelf) einer Grenzfrequenz. Wie eine Schranke, ab der alles rauf- oder runtergeregelt wird.

- Typisch für Höhen und Bässe am Mischpult-Kanalzug

**Peak / Bell EQ**

Verstärkt oder senkt einen Bereich um eine Mittenfrequenz, in Form einer "Glocke" (Bell). Die Breite dieser Glocke wird durch den **Q-Faktor** bestimmt.

- Niedriger Q = breite, sanfte Glocke
- Hoher Q = schmale, chirurgische Glocke

**High-Pass / Low-Pass Filter**

- **HPF (High Pass Filter):** Lässt Höhen durch, schneidet Tiefen ab
- **LPF (Low Pass Filter):** Lässt Tiefen durch, schneidet Höhen ab
- Die **Flankensteilheit** (Slope) bestimmt, wie steil der Filter abschneidet: 12 dB/Oktave, 24 dB/Oktave usw.

**Parametrischer EQ**

Kombiniert mehrere Bänder (HPF, mehrere Bell-Bänder, Shelving, LPF) in einem Gerät. Der Standard für professionelle Mischpulte und DAW-Plugins.

**Grafik-EQ (Graphic EQ)**

Hat viele Bänder in festen Abständen (1/3 Oktave = 31 Bänder). Jedes Band hat einen Regler. Man sieht sofort, wie der EQ-Verlauf aussieht. Typisch für Monitore und Systemcontroller.

---

## 8.2 Frequenzbereiche in der Praxis

Hier vertiefst du, was du in Kapitel 6.3 begonnen hast – jetzt mit konkreten Hinweisen, wann du wo eingreifst.

### Sub-Bass (20–60 Hz)

- Kaum hörbar, aber spürbar
- Zu viel: Macht den Mix "wummrig", überlastet die PA
- Eingriff: Bei den meisten Kanälen per HPF abschneiden; nur Kick und Bass dürfen hier etwas haben

### Bass (60–120 Hz)

- Fundament des Sounds, Wärme
- Kick Drum: ca. 80 Hz ist der "Punch"
- Bassgitarre: ca. 100 Hz ist das Fundament
- Zu viel auf allen Kanälen: Matschiger, unklarer Mix

### Tiefe Mitten / Obere Bässe (120–250 Hz)

- "Wärme" von Instrumenten (Gitarren, Stimmen)
- Zu viel: "Muffig", "boxig", undefiniert
- Oft sinnvoll: Bei Gitarren und Keyboards leicht absenken

### Untere Mitten (250–500 Hz)

- Körper von Instrumenten, Nasalität
- Zu viel: Klingt "nasal", "honkig"
- Kritischer Bereich – hier gibt es viele Konflikte zwischen Instrumenten

### Mitten (500 Hz – 2 kHz)

- Verständlichkeit, Durchsetzungsvermögen
- Gesang: Dieser Bereich bestimmt, ob man ihn versteht
- Gitarre: Hier liegt der "Crunch" und Charakter
- Zu viel auf allem: Mix klingt aggressiv und anstrengend

### Obere Mitten (2–6 kHz)

- Präsenz, Brillanz, "Schneidigkeit"
- Gesang: Hier sitzt die Silbenverständlichkeit
- 3–4 kHz: Sehr empfindlicher Bereich für das Gehör – Eingriffe wirken stark
- Zu viel: Aggressiv, anstrengend, ermüdend

### Höhen (6–12 kHz)

- Luftigkeit, Glanz, Helligkeit
- Becken: Hauptbereich
- Zu viel: Schrill und unangenehm
- Zu wenig: Mix klingt dumpf und stumpf

### Ultra-Höhen (12–20 kHz)

- "Seide", Luft
- Nur mit einem High-Shelf sanft geregelt
- Bei Vocals manchmal leicht boosten für Frische

---

## 8.3 Subtraktiver EQ

**Subtraktiver EQ** bedeutet: Du senkst Frequenzen ab, anstatt sie zu boosten. Das ist die professionellere und musikalischere Herangehensweise.

### Warum subtraktiv?

- Boosten kann das Signal übersteuern (vor allem bei vielen Kanälen gleichzeitig)
- Wenn etwas zu viel ist, klingt das Absenken besser als das "Gegenteil" zu boosten
- Subtraktiver EQ hält den Gesamtpegel stabiler

### Die "Sweep and Cut"-Technik:

1. Nimm ein Bell-Band mit hohem Gain (+12 dB) und hohem Q (schmal)
2. Bewege die Frequenz langsam durch das Spektrum
3. Höre, bei welcher Frequenz das Problem am schlimmsten klingt
4. Dort: Gain auf –3 bis –6 dB, Q anpassen
5. Ergebnis: Das Problem ist gezielt entfernt

### Wann dann doch boosten?

Boosten ist okay, wenn:
- Du einen Charakter hinzufügen willst (mehr Wärme, mehr Brillanz)
- Der Boost moderat ist (maximal +3 bis +5 dB)
- Du mit dem Gesamtpegel aufpasst

---

## 8.4 Kompressoren

Ein **Kompressor** verringert automatisch die Lautstärke, wenn ein Signal einen definierten Pegel überschreitet. Er macht laute Stellen leiser – und dadurch klingt das Signal insgesamt gleichmäßiger.

### Was macht ein Kompressor?

Stell dir vor, du sitzt am Fader und passt die Lautstärke mit der Hand an:

```
Sänger singt leise → du ziehst Fader hoch
Sänger singt laut  → du drückst Fader runter
```

Genau das macht ein Kompressor – nur automatisch, schneller und präziser.

### Analogie: Kompressor als "sanfter Assistent am Fader"

- Wenn die Stimme zu laut wird, drückt der Kompressor sanft nach unten
- Wenn sie wieder leiser ist, lässt er sie wieder normal
- Du regelst, wie stark und schnell er reagiert

### Wo setzt man einen Kompressor ein?

| Kanal | Warum Kompressor? |
|-------|------------------|
| Gesang | Sehr hohe Dynamik, Gleichmäßigkeit |
| Bass | Dynamik von Finger- vs. Plektrumanschlag |
| Kick Drum | Punchy, kontrollierter Anschlag |
| Snare | Gleichmäßiger Charakter |
| Gitarren | Sustain verlängern, Peaks kontrollieren |

---

## 8.5 Threshold, Ratio, Attack & Release

Das sind die vier Hauptparameter eines Kompressors. Wenn du diese verstehst, kannst du jeden Kompressor bedienen.

### Threshold (Schwelle)

Der **Threshold** bestimmt, ab welchem Pegel der Kompressor anfängt zu arbeiten.

- Signal **unter dem Threshold:** Keine Kompression, Signal bleibt unverändert
- Signal **über dem Threshold:** Kompressor greift ein

Beispiel: Threshold bei –20 dBFS → Immer wenn das Signal lauter als –20 dB ist, wird es komprimiert.

**Faustformel:** Je niedriger der Threshold, desto mehr wird komprimiert.

### Ratio (Verhältnis)

Das **Ratio** bestimmt, wie stark das Signal über dem Threshold komprimiert wird.

| Ratio | Bedeutung |
|-------|----------|
| 2:1 | Für jede 2 dB über dem Threshold kommt 1 dB raus → sanft |
| 4:1 | Für jede 4 dB über dem Threshold kommt 1 dB raus → moderat |
| 8:1 | Für jede 8 dB → stark |
| ∞:1 (Limiter) | Alles über dem Threshold wird hart begrenzt |

**Faustregel:**
- Gesang: 3:1 – 4:1 (sanft)
- Bass: 4:1 – 6:1 (moderat)
- Limiter für PA-Schutz: ∞:1

### Attack (Einsatz)

Der **Attack** bestimmt, wie schnell der Kompressor reagiert, wenn das Signal den Threshold überschreitet.

- **Schneller Attack (1–5 ms):** Kompressor greift sofort ein → Transiente (Anschlag) wird weichgemacht
- **Langsamer Attack (30–100 ms):** Der Anschlag des Instruments kommt zuerst durch, dann erst greift der Kompressor ein → Mehr Punch, Transienten bleiben erhalten

**Beispiel:**
- Kick Drum mit langsamem Attack: Der harte Anschlag ("Klick") bleibt erhalten, nur der Körper wird komprimiert
- Gesang mit schnellem Attack: Peaks werden sofort abgefangen, klingt gleichmäßiger

### Release (Abklingen)

Der **Release** bestimmt, wie schnell der Kompressor aufhört zu komprimieren, wenn das Signal wieder unter den Threshold fällt.

- **Schneller Release:** Kompressor hört schnell auf → kann "Pumpen" erzeugen
- **Langsamer Release:** Kompressor bleibt länger aktiv → gleichmäßiger, aber Gefahr von zu viel Kompression

### Makeup Gain

Wenn du viel komprimierst, wird das Signal insgesamt leiser. Der **Makeup Gain** (auch: Output Gain) hebt den Ausgangspegel wieder an, um den Pegelverlust auszugleichen.

### Gain Reduction Meter

Das **Gain Reduction Meter** (GR) zeigt dir, wie viel der Kompressor gerade eingreift.

- 0 dB GR: Kein Eingriff
- –3 dB GR: Kompressor reduziert gerade um 3 dB
- –10 dB GR: Starke Kompression

**Richtwerte:** Im Live-Sound sind –3 bis –6 dB GR typisch. Mehr als –10 dB klingt oft "totgequetscht".

---

## 8.6 Gates

Ein **Gate** (Noise Gate) ist das Gegenteil eines Kompressors: Es lässt das Signal nur durch, wenn es **laut genug** ist.

### Wie funktioniert ein Gate?

```
Signal leise (unter Threshold) → Gate schließt → kein Ton
Signal laut (über Threshold)  → Gate öffnet  → Signal durch
```

### Wofür nutzt man Gates?

**Schlagzeug** ist der klassische Einsatzbereich:

- Snare-Gate: Lässt nur den echten Snare-Schlag durch, nicht das Übersprechen von anderen Drums
- Tom-Gate: Zwischen Fills hörst du kein Rauschen oder Übersprechen
- Kick-Gate: Sauberer Kick, kein Raumhall dazwischen

### Gate-Parameter:

- **Threshold:** Wie laut muss das Signal sein, damit das Gate öffnet?
- **Attack:** Wie schnell öffnet das Gate? (sehr kurz für Drums)
- **Hold:** Wie lange bleibt das Gate offen, auch wenn Signal wieder leiser ist?
- **Release:** Wie schnell schließt das Gate?
- **Range:** Wie weit schließt das Gate? (–20 dB = wird leiser, nicht stumm; –∞ = komplett stumm)

### Typische Einstellung für Snare-Gate:

- Threshold: So, dass nur die Snare öffnet, nicht das Hi-Hat-Übersprechen
- Attack: 1–5 ms
- Hold: 100–200 ms
- Release: 50–100 ms

> ⚠️ **Falle:** Ein Gate, das zu aggressiv eingestellt ist, frisst den Anfang von Noten ab oder "pumpt" unangenehm. Lieber etwas zu sanft als zu hart einstellen.

---

## 8.7 De-Esser

Ein **De-Esser** ist ein spezieller Kompressor, der nur auf **sibilante Frequenzen** (Zischlaute: "S", "Sch", "Z") reagiert.

### Das Problem: Zischende S-Laute

Manche Sänger produzieren sehr starke Zischlaute bei 6–10 kHz. Das kann auf der Bühne und besonders bei Mikrofonen sehr unangenehm sein – es klingt, als würde man in die Kapsel stechen.

### Wie funktioniert ein De-Esser?

Er analysiert laufend die Frequenzanteile des Signals. Wenn bei 6–10 kHz zu viel Energie ist (S-Laut), drückt er kurz die Lautstärke in diesem Bereich – und zwar nur dort und nur kurz.

Das Ergebnis: Die S-Laute werden weicher, ohne dass der Gesamtklang der Stimme beeinflusst wird.

### Einstellung:

- **Frequenz:** 6–10 kHz (je nach Sänger variiert der Sibilanz-Bereich)
- **Threshold:** So, dass nur die stärksten Zischlaute aktiviert werden
- **Split-Modus oder Wideband-Modus:** Split ist präziser (nur diese Frequenz wird beeinflusst)

### Wann brauche ich keinen De-Esser?

- Wenn der Sänger keine ausgeprägte Sibilanz hat
- Wenn das Mikrofon nicht besonders empfindlich bei Höhen ist (z.B. SM58)
- Wenn der Raum die Höhen sowieso dämpft

---

## 8.8 Typische Fehler bei Dynamikbearbeitung

### Fehler 1: Zu viel Kompression

Der Mix klingt "flach", "tot", ohne Energie. Alles ist auf einem Level – keine Spannung mehr.

**Lösung:** Ratio reduzieren, Threshold erhöhen, Makeup Gain prüfen. Weniger ist mehr.

### Fehler 2: Gate schnappt falsch zu

Das Gate schließt, bevor der Ton fertig ist – der Anfang oder das Ende eines Schlags wird abgehackt.

**Lösung:** Attack verlängern, Hold erhöhen, Threshold leicht senken.

### Fehler 3: Kompressor "pumpt"

Der gesamte Mix atmet mit der Kick Drum mit – wenn die Kick schlägt, wird alles andere leiser. Das klingt wie "pumpa pumpa pumpa".

**Lösung:** Release verlängern (langsamer), Threshold erhöhen, Ratio reduzieren. Alternativ: Kompressor nur auf den Master-Bus nehmen, nicht auf einzelne Kanäle.

### Fehler 4: EQ und Kompressor in falscher Reihenfolge

**EQ vor Kompressor:** Du formst den Klang, dann wird er komprimiert (Standard)
**Kompressor vor EQ:** Kompressor reagiert auf das ungefilterte Signal, dann EQ danach

Für Live-Sound ist EQ vor Kompressor die Standardreihenfolge. Wenn du Problemfrequenzen vor der Kompression entfernst (z.B. Bassüberhang bei Gesang per HPF), komprimiert der Kompressor sauberer.

### Fehler 5: Kompressor auf allem und ohne Grund

Nicht jeder Kanal braucht einen Kompressor. Instrumente mit wenig Dynamik (z.B. Keyboard mit konstantem Sound) brauchen oft keinen.

**Faustregel:** Kompressor dort einsetzen, wo die Dynamik ein echtes Problem ist.

### Fehler 6: Zu starker EQ-Boost ohne Pegel-Check

Mehrere Kanäle mit +6 dB Boost können den Master-Bus zum Übersteuern bringen.

**Lösung:** Nach EQ-Eingriffen den Gesamtpegel am Master-Bus prüfen.

---

## Zusammenfassung Kapitel 8

**EQ:**
- Subtraktiv vor additiv: Lieber senken als boosten
- HPF immer aktivieren (außer bei Bassinstrumenten)
- Sweep-Technik: Boost → Position finden → Cut setzen
- Grafik-EQ für Monitor-Feedback, parametrischer EQ für Klangformung

**Kompressor:**
- Threshold: Ab wann reagiert er?
- Ratio: Wie stark greift er ein?
- Attack: Wie schnell (langsam = mehr Punch)
- Release: Wie lange greift er ein?
- –3 bis –6 dB Gain Reduction ist oft ausreichend

**Gate:**
- Schließt das Signal, wenn es zu leise ist
- Klassisch für Drums (Snare, Tom, Kick)
- Nicht zu aggressiv einstellen

**De-Esser:**
- Spezieller Kompressor für Zischlaute
- Frequenz: 6–10 kHz
- Nur wenn wirklich nötig

**Goldene Regel:** Jedes dieser Werkzeuge kann helfen – aber zu viel Bearbeitung klingt schlechter als zu wenig. Vertraue deinen Ohren.

---

*Weiter geht es in Kapitel 9: Digitale Mischpulte*
