# -*- coding: utf-8 -*-
"""Kapitel-Metadaten, Grafik-Zuordnung, interaktive Widgets und Quizfragen."""

# (nummer, md-datei, ausgabedatei, kurztitel, icon, kurzbeschreibung, gruppe)
CHAPTERS = [
    (1, "Kapitel_01_Einfuehrung_und_Grundlagen.md", "kapitel-01.html", "Einführung & Grundlagen", "🎧",
     "Schall, Frequenz, Pegel, Signalfluss – das Fundament.", "A"),
    (2, "Kapitel_02_Kabel_Anschluesse_Hardware.md", "kapitel-02.html", "Kabel, Anschlüsse & Hardware", "🔌",
     "XLR, Klinke, Speakon, symmetrisch vs. unsymmetrisch.", "A"),
    (3, "Kapitel_03_Mikrofone.md", "kapitel-03.html", "Mikrofone", "🎤",
     "Dynamisch, Kondensator, Richtcharakteristik, Mikrofonierung.", "A"),
    (4, "Kapitel_04_Analoge_Mischpulte.md", "kapitel-04.html", "Analoge Mischpulte", "🎚️",
     "Kanalzug, Gain, EQ, Aux, Fader, Gain Staging.", "A"),
    (5, "Kapitel_05_Lautsprecher_und_Monitoring.md", "kapitel-05.html", "Lautsprecher & Monitoring", "🔊",
     "PA, Tops & Subs, Monitore, In-Ear, Feedback.", "A"),
    (6, "Kapitel_06_Hoeren_lernen.md", "kapitel-06.html", "Hören lernen", "👂",
     "Kritisches Hören, Frequenztraining, Dynamik, Hall.", "A"),
    (7, "Kapitel_07_Live-Mixing_Grundlagen.md", "kapitel-07.html", "Live-Mixing Grundlagen", "🎛️",
     "Soundcheck, Vocals, Balance, Fehlerdiagnose.", "A"),
    (8, "Kapitel_08_Equalizer_und_Dynamikbearbeitung.md", "kapitel-08.html", "Equalizer & Dynamik", "📊",
     "EQ-Arten, Kompressor, Gate, De-Esser.", "A"),
    (9, "Kapitel_09_Digitale_Mischpulte.md", "kapitel-09.html", "Digitale Mischpulte", "💻",
     "Layer, Routing, Szenen, DCAs, Remote Mixing.", "B"),
    (10, "Kapitel_10_Recording_und_DAWs.md", "kapitel-10.html", "Recording & DAWs", "🎙️",
     "DAW, Interface, Aufnahme, Plugins, Export.", "B"),
    (11, "Kapitel_11_Fortgeschrittene_Live-Technik.md", "kapitel-11.html", "Fortgeschrittene Live-Technik", "📡",
     "Digitalsnake, Dante, Funk, RF, Phase, Delay.", "B"),
    (12, "Kapitel_12_Soft_Skills_und_Arbeitsweise.md", "kapitel-12.html", "Soft Skills & Arbeitsweise", "🤝",
     "Ruhe, Kommunikation, Verantwortung, Auftreten.", "C"),
    (13, "Kapitel_13_Praktische_Uebungen.md", "kapitel-13.html", "Praktische Übungen", "🏋️",
     "Konkrete Übungen vom Vocal-Mix bis Mini-Gig.", "C"),
    (14, "Kapitel_14_Typische_Anfaengerfehler.md", "kapitel-14.html", "Typische Anfängerfehler", "⚠️",
     "Die 6 häufigsten Fallen – und wie du sie vermeidest.", "C"),
    (15, "Kapitel_15_Weiterfuehrende_Themen.md", "kapitel-15.html", "Weiterführende Themen", "🚀",
     "Akustik, LUFS, Broadcast, Immersive Audio, Zukunft.", "C"),
    (16, "Kapitel_16_Eigene_Notizen_und_Erfahrungswerte.md", "kapitel-16.html", "Eigene Notizen", "📓",
     "Dein persönliches Tontechnik-Tagebuch & Tracker.", "C"),
]

GROUPS = [
    ("A", "Fundament & Analog-Handwerk"),
    ("B", "Digitale Welt & Aufnahme"),
    ("C", "Praxis, Haltung & Vertiefung"),
]

# Grafik-Zuordnung: kapitel -> { überschrift-teilstring: (dateiname, bildunterschrift) }
IMAGES = {
    1: {"1.7 Signalfluss": ("G1_1_signalfluss.png", "Abb. 1.1 – Signalfluss von der Schallquelle bis zum Publikum"),
        "1.4 Frequenz": ("G1_2_frequenzspektrum.png", "Abb. 1.2 – Das hörbare Frequenzspektrum (20 Hz – 20 kHz)")},
    2: {"2.1 XLR": ("G2_1_kabeltypen.png", "Abb. 2.1 – Die wichtigsten Kabel- und Steckertypen im Überblick"),
        "2.7 Symmetrisch": ("G2_2_symmetrisch.png", "Abb. 2.2 – Symmetrische Übertragung: Störungen werden herausgerechnet")},
    3: {"3.3 Richtcharakteristiken": ("G3_1_richtcharakteristiken.png", "Abb. 3.1 – Richtcharakteristiken im Vergleich"),
        "3.7 Mikrofonierung von Gitarrenamps": ("G3_3_gitarrenamp_mikro.png", "Abb. 3.3 – SM57 am Gitarrenamp: Mitte vs. Rand"),
        "3.8 Mikrofonierung von Schlagzeug": ("G3_2_drum_mikrofonierung.png", "Abb. 3.2 – Typisches Drum-Mikrofonierungs-Setup")},
}

# Interaktive Widget-Blöcke pro Kapitel. Platzhalter %LEAD% wird ersetzt; window.PAGE_INIT initialisiert.
def _section(lead, widgets, init_calls):
    inner = "".join(
        '<div class="widget"><h3>%s</h3><p class="audiohint">🔊 Web-Audio: bitte zuerst leise stellen / Kopfhörer. '
        'Der Button „🔇 Ton stoppen” oben bricht jederzeit ab.</p><div id="%s"></div></div>'
        % (title, wid) if needs_audio else
        '<div class="widget"><h3>%s</h3><div id="%s"></div></div>' % (title, wid)
        for (title, wid, needs_audio) in widgets
    )
    return ('<section class="interaktiv"><h2>🎧 Zum Ausprobieren</h2>'
            '<p class="lead">%s</p>%s<script>window.PAGE_INIT=function(){%s};</script></section>'
            % (lead, inner, init_calls))


WIDGETS = {
    1: _section("Begreife Signalweg, Frequenzen, Lautstärke und Panorama – zum Anfassen und Anhören.",
                [("Signalfluss erkunden", "w-flow", False),
                 ("Frequenz-Explorer (20 Hz – 20 kHz)", "w-freq", True),
                 ("Wie viel ist 1 dB? – Lautheit erfahren", "w-db", True),
                 ("Panorama: links / Mitte / rechts", "w-pan", True)],
                "signalFlow('w-flow');freqExplorer('w-freq');dbDemo('w-db');panDemo('w-pan');"),
    2: _section("Ordne die Steckertypen ihrem Einsatzzweck zu.",
                [("Stecker-Memory: Was gehört wohin?", "w-match", False)],
                "matchGame('w-match',[['XLR','Mikrofon → Mischpult (symmetrisch)'],"
                "['Klinke TS','Gitarre / Instrument (unsymmetrisch)'],"
                "['Speakon','Endstufe → Lautsprecher'],['Cinch / RCA','Consumer- & DJ-Geräte'],"
                "['MIDI','Steuerdaten – keine Audiodaten'],['USB','Audiointerface → Computer']],"
                "'Stecker','Einsatzzweck');"),
    3: _section("Verändere den Winkel der Schallquelle und höre, wie die Richtcharakteristik den Pegel bestimmt.",
                [("Richtcharakteristik-Simulator", "w-polar", True)],
                "polarDemo('w-polar');"),
    4: _section("Bediene einen kompletten Kanalzug – mit echtem Test-Signal – und erlebe Clipping.",
                [("Virtueller Kanalzug", "w-strip", True),
                 ("Sauber vs. übersteuert (Clipping)", "w-clip", True)],
                "channelStrip('w-strip');clipDemo('w-clip');"),
    5: _section("Erlebe Feedback kontrolliert und höre den Unterschied von Tops und Subwoofer.",
                [("Feedback-Simulator", "w-fb", True),
                 ("Tops vs. Subwoofer", "w-split", True)],
                "feedbackDemo('w-fb');splitDemo('w-split');"),
    6: _section("Das Kernkapitel zum Mitmachen: trainiere dein Gehör mit echtem Ton.",
                [("Frequenz-Hörtrainer", "w-ear", True),
                 ("Hall hören: dezent bis übertrieben", "w-rev", True)],
                "earTrainer('w-ear');reverbDemo('w-rev');"),
    7: _section("Bringe den Ablauf eines Gigs in die richtige Reihenfolge.",
                [("Workflow-Reihenfolge", "w-order", False)],
                "orderGame('w-order',['Aufbau & Einschalten (PA zuletzt)','Line Check',"
                "'Gain Staging','Monitor-Mix','FOH-Balance aufbauen','Konzert – aufmerksam bleiben']);"),
    8: _section("Stelle einen Kompressor ein und sieh + höre, was Threshold, Ratio, Attack und Release bewirken.",
                [("Kompressor-Visualizer", "w-comp", True)],
                "compViz('w-comp');"),
    9: _section("So bedienen Digitalpulte viele Kanäle mit wenigen Fadern.",
                [("Layer-Umschalter", "w-layer", False)],
                "layerDemo('w-layer');"),
    10: _section("Welches Audioformat wofür?",
                 [("Format-Wähler", "w-fmt", False)],
                 "formatWidget('w-fmt');"),
    11: _section("Rechne Laufzeiten für Delay-Speaker und Effekt-Delays aus.",
                 [("Delay-/Laufzeit-Rechner", "w-delay", False)],
                 "delayCalc('w-delay');"),
    12: _section("Übersetze typische Musiker-Aussagen in konkrete Handgriffe am Pult.",
                 [("Musiker-Übersetzer", "w-trans", False)],
                 "translator('w-trans');"),
    13: _section("Übe den Zeitdruck eines Soundchecks – die Checklisten oben kannst du dauerhaft abhaken.",
                 [("Soundcheck-Timer (15 Min)", "w-timer", False)],
                 "timerWidget('w-timer');"),
    14: _section("Höre den Unterschied zwischen sauberem Mix und typischen Fehlern.",
                 [("Fehler hören: A/B-Vergleich", "w-spot", True)],
                 "spotError('w-spot');"),
    15: _section("Lautheit im Vergleich: So unterschiedlich „laut” mischen die Plattformen.",
                 [("Lautheitsnormen (LUFS)", "w-loud", False)],
                 "loudnessWidget('w-loud');"),
    16: _section("Dein persönliches Logbuch – wird automatisch in deinem Browser gespeichert.",
                 [("Schnellnotizen", "w-notes", False)],
                 "notesWidget('w-notes','kap16_schnellnotizen');"),
}


# Quizfragen: q=Frage, o=Optionen, a=Index der richtigen Antwort, e=Erklärung
QUIZ = {
1: [
 {"q":"Was ist die zentrale Aufgabe eines Tontechnikers?","o":["Möglichst viele Effekte einsetzen","Dafür sorgen, dass das Publikum die Band gut hört","Die lauteste mögliche Lautstärke erreichen","Die Instrumente stimmen"],"a":1,"e":"Der Tontechniker sorgt dafür, dass das Publikum die Band bestmöglich hört – am besten unauffällig."},
 {"q":"In welcher Einheit wird die Frequenz gemessen?","o":["Dezibel (dB)","Watt (W)","Hertz (Hz)","Volt (V)"],"a":2,"e":"Frequenz = Schwingungen pro Sekunde, gemessen in Hertz (Hz). dB ist die Einheit für Pegel/Lautstärke."},
 {"q":"Was passiert bei Clipping?","o":["Das Signal wird leiser","Der obere Teil der Wellenform wird abgeschnitten und verzerrt","Der Ton wird höher","Die Frequenz verdoppelt sich"],"a":1,"e":"Ist ein Signal zu laut, wird die Wellenform abgeschnitten – das klingt kratzig und unangenehm."},
 {"q":"Welche Reihenfolge beschreibt den grundlegenden Signalfluss?","o":["Lautsprecher → Mischpult → Mikrofon","Mikrofon → Kabel → Mischpult → Endstufe → Lautsprecher","Mischpult → Mikrofon → Publikum","Endstufe → Mikrofon → Kabel"],"a":1,"e":"Schallquelle → Mikrofon → Kabel → Mischpult → Endstufe → Lautsprecher → Publikum."},
 {"q":"Warum lernt man die Tontechnik zuerst analog?","o":["Analoge Geräte sind teurer","Weil man den Signalfluss direkt und greifbar versteht","Digitale Geräte sind verboten","Analog rauscht weniger"],"a":1,"e":"Analog hat jeder Regler eine klare Funktion – dieses Grundwissen überträgt sich direkt auf digitale Pulte."},
 {"q":"Wo gehören tiefe Frequenzen (Bass, Kick) im Live-Panorama meist hin?","o":["Ganz links","Ganz rechts","In die Mitte","Wechselnd L/R"],"a":2,"e":"Tiefe Frequenzen sind kaum ortbar – in der Mitte bilden sie ein stabiles Fundament."},
 {"q":"Ab welchem Dauerpegel kann das Gehör geschädigt werden?","o":["ab 40 dB","ab 60 dB","ab 85 dB","erst ab 130 dB"],"a":2,"e":"Dauerhafter Lärm ab ca. 85 dB kann das Gehör schädigen – Gehörschutz ist Pflicht."},
],
2: [
 {"q":"Welches Kabel überträgt symmetrisch und ist Standard für Mikrofone?","o":["TS-Klinke","XLR","Cinch","Speakon"],"a":1,"e":"XLR überträgt symmetrisch (3 Pins) und ist dadurch unempfindlich gegen Brummen/Einstreuung."},
 {"q":"Wofür ist das Speakon-Kabel gedacht?","o":["Mikrofon → Mischpult","Endstufe → Lautsprecher","Gitarre → Amp","Laptop → Interface"],"a":1,"e":"Speakon ist stromfest und verriegelbar – für die Verbindung Endstufe → Lautsprecher."},
 {"q":"Was überträgt ein MIDI-Kabel?","o":["Audiosignale","Lautsprechersignale","Steuerdaten (z. B. welche Note, wie laut)","Strom"],"a":2,"e":"MIDI überträgt keine Klänge, sondern Steuerdaten wie Note, Velocity und Programmwechsel."},
 {"q":"Warum ist ein symmetrisches Kabel störungsärmer?","o":["Es ist dicker","Das Signal wird doppelt mit umgekehrter Polarität geführt und Störungen werden herausgerechnet","Es hat Goldkontakte","Es ist kürzer"],"a":1,"e":"Common Mode Rejection: Die identische Störung auf beiden Adern hebt sich bei der Differenzbildung auf."},
 {"q":"Welche Wickeltechnik verhindert Kabel-Drall?","o":["Möglichst stramm aufrollen","Over-Under (Überhand/Unterhand)","Um den Arm wickeln","Knoten machen"],"a":1,"e":"Over-Under verhindert, dass das Kabel einen Drall bekommt und sich beim Abwickeln verdreht."},
 {"q":"Ein TS-Klinkenkabel (Gitarre) ist …","o":["symmetrisch","unsymmetrisch","digital","ein Lautsprecherkabel"],"a":1,"e":"TS hat nur zwei Leiter (Signal + Masse) – unsymmetrisch und anfällig für Einstreuungen."},
],
3: [
 {"q":"Welcher Mikrofontyp ist robust und braucht KEINE Phantomspannung?","o":["Kondensatormikrofon","Dynamisches Mikrofon","Bändchenmikrofon","USB-Mikrofon"],"a":1,"e":"Dynamische Mikrofone (z. B. SM58) arbeiten nach dem Induktionsprinzip und brauchen keinen Strom."},
 {"q":"Welche Spannung brauchen Kondensatormikrofone?","o":["+12V","+48V Phantomspannung","230V","Keine"],"a":1,"e":"Kondensatormikrofone benötigen +48V Phantomspannung über das XLR-Kabel."},
 {"q":"Welche Richtcharakteristik ist Standard für Live-Gesang?","o":["Kugel (Omni)","Niere (Cardioid)","Acht","Keine"],"a":1,"e":"Die Niere nimmt von vorne auf und blendet hinten aus – gut gegen Feedback auf der Bühne."},
 {"q":"Was beschreibt der Nahbesprechungseffekt?","o":["Höhen werden lauter, je näher man spricht","Bässe werden betont, je näher die Quelle am Mikro ist","Das Mikro rauscht stärker","Die Lautstärke sinkt"],"a":1,"e":"Bei Nieren-/Supernieren-Mikros nehmen die Bässe mit geringerem Abstand zu."},
 {"q":"Welches Mikrofon darf man NIEMALS mit Phantomspannung betreiben?","o":["SM57","Großmembran-Kondensator","Bändchenmikrofon (Ribbon)","USB-Mikrofon"],"a":2,"e":"Bändchenmikrofone können durch +48V zerstört werden."},
 {"q":"Warum dreht man bei Snare oben/unten eine Phase?","o":["Damit es lauter wird","Weil die Membranen gegenläufig sind und sich der Bass sonst auslöscht","Zur Feedback-Unterdrückung","Wegen der Phantomspannung"],"a":1,"e":"Die untere Membran schwingt gegenläufig – ohne Phasendrehung löschen sich tiefe Frequenzen aus."},
 {"q":"Was ist der Standard zur Abnahme eines Gitarrenamps?","o":["Großmembran-Kondensator weit weg","SM57 nah am Lautsprecher","Kugelmikrofon","DI-Box"],"a":1,"e":"Das robuste SM57 direkt am Gitter (Mitte = hell, Rand = wärmer) ist der Klassiker."},
],
4: [
 {"q":"Welcher Regler steht ganz am Anfang des Kanalzugs und muss zuerst stimmen?","o":["Fader","Pan","Gain (Preamp)","Mute"],"a":2,"e":"Gain hebt das schwache Mic-Signal auf Line-Level. „Garbage in, garbage out”."},
 {"q":"Wann aktivierst du den High-Pass-Filter (HPF)?","o":["Nie","Bei fast jedem Kanal außer Bassinstrumenten","Nur beim Bass","Nur beim Master"],"a":1,"e":"Der HPF filtert Trittschall/Rumoren – an bei allem außer Kick, Bass & Co."},
 {"q":"Welche EQ-Strategie gilt als professioneller?","o":["Möglichst viel boosten","Subtraktiv: lieber absenken als anheben","Immer alle Höhen anheben","EQ gar nicht nutzen"],"a":1,"e":"„If in doubt, cut.” Absenken hält den Pegel stabil und klingt oft natürlicher."},
 {"q":"Monitorwege stellt man auf … ?","o":["Post-Fader","Pre-Fader","Mute","Solo"],"a":1,"e":"Pre-Fader: Der Monitor-Mix bleibt unabhängig vom FOH-Fader. Effekte dagegen Post-Fader."},
 {"q":"Was bedeutet die 0-dB-Position (Unity) am Fader?","o":["Kein Ton","Der ideale Arbeitspunkt ohne Verstärkung/Absenkung","Maximale Lautstärke","Stummschaltung"],"a":1,"e":"Bei korrektem Gain Staging sitzt der Fader meist nahe Unity (0 dB)."},
 {"q":"Wofür dient eine Subgruppe (Group)?","o":["Einzelne Kanäle stummschalten","Mehrere Kanäle (z. B. alle Drums) mit einem Fader gemeinsam regeln","Den Master ersetzen","Phantomspannung verteilen"],"a":1,"e":"Auf eine Gruppe geroutet, regelst du z. B. das ganze Schlagzeug mit einem Fader."},
 {"q":"Wie gehst du beim Gain Staging vor?","o":["Von unten (Fader) nach oben","Von oben (Gain) nach unten (Fader, Master)","Nur den Master einstellen","Alles gleichzeitig"],"a":1,"e":"Erst Gain richtig einpegeln, dann mit den Fadern den Mix formen."},
],
5: [
 {"q":"Wofür steht „PA”?","o":["Power Amplifier","Public Address (Beschallung des Publikums)","Phantom Audio","Pan Adjust"],"a":1,"e":"PA = Public Address, das System, das das Publikum beschallt."},
 {"q":"Was ist für Einsteiger einfacher zu handhaben?","o":["Passive Lautsprecher mit externer Endstufe","Aktive Lautsprecher (Endstufe eingebaut)","Beide gleich","Nur Subwoofer"],"a":1,"e":"Aktive Boxen haben die passende Endstufe eingebaut – weniger Kabel, einfacher Aufbau."},
 {"q":"Welche Frequenzen geben Subwoofer wieder?","o":["Höhen","Mitten","Tiefe Bassfrequenzen (ca. 30–80 Hz)","Alles"],"a":2,"e":"Subs übernehmen den Tiefbass; Tops machen Mitten/Höhen (ab ca. 80–100 Hz)."},
 {"q":"Wie entsteht Feedback?","o":["Durch zu wenig Gain","Schall aus dem Lautsprecher geht ins Mikrofon und wird immer wieder verstärkt","Durch ein defektes Kabel","Durch Phantomspannung"],"a":1,"e":"Eine Rückkopplungsschleife schaukelt sich auf, bis es pfeift."},
 {"q":"Was ist die schnellste Sofortmaßnahme bei Feedback?","o":["PA ausschalten","Gain des betroffenen Kanals runter / Kanal muten","Mehr Hall geben","Master aufdrehen"],"a":1,"e":"Gain runter bzw. Kanal muten stoppt das Feedback sofort, dann Ursache suchen."},
 {"q":"Was ist ein großer Vorteil von In-Ear-Monitoring?","o":["Es ist billiger","Keine offenen Lautsprecher → keine Feedback-Gefahr","Mehr Bühnenlärm","Man braucht keinen Mix"],"a":1,"e":"Ohne offenen Wedge gibt es keine Rückkopplung; zudem besserer Gehörschutz und sauberere Bühne."},
],
6: [
 {"q":"Was bedeutet „kritisches Hören”?","o":["Musik nur genießen","Aktiv und analytisch hören: Was fehlt? Was ist zu viel?","Möglichst laut hören","Nur auf den Bass achten"],"a":1,"e":"Du analysierst den Sound in Echtzeit statt nur emotional zu genießen."},
 {"q":"Welche Technik hilft, eine Problemfrequenz zu finden?","o":["Alles boosten","Sweep & Cut: schmal boosten, Frequenz suchen, dann dort senken","Master runter","Phantom an"],"a":1,"e":"Mit einem schmalen Boost die Problemstelle aufspüren und dort gezielt absenken."},
 {"q":"Wonach klingt der Bereich um 250–400 Hz, wenn zu viel davon da ist?","o":["Zischig","„Matschig” / „boxig”","Dünn","Luftig"],"a":1,"e":"Zu viel 250–400 Hz lässt den Mix matschig/boxig wirken."},
 {"q":"Was ist beim Hall (Reverb) der typische Anfängerfehler?","o":["Zu wenig Hall","Zu viel Hall auf allem","Falscher Pre-Delay","Kein Stereo"],"a":1,"e":"Zu viel Hall macht den Mix undurchsichtig und kostet Verständlichkeit – weniger ist mehr."},
 {"q":"Wofür ist der Pre-Delay beim Hall gut?","o":["Macht den Hall länger","Trennt das klare Direktsignal vom Nachhall","Erhöht die Lautstärke","Senkt die Bässe"],"a":1,"e":"Ein Pre-Delay von 20–40 ms lässt den Direktsound zuerst klar durch, dann erst den Hall."},
 {"q":"Welcher Frequenzbereich bestimmt die Verständlichkeit/Präsenz von Gesang besonders?","o":["20–60 Hz","100 Hz","2–6 kHz","unter 100 Hz"],"a":2,"e":"In den oberen Mitten (2–6 kHz) sitzt die Silbenverständlichkeit/Präsenz."},
],
7: [
 {"q":"In welcher Reihenfolge schaltet man ein?","o":["Lautsprecher zuerst, Mischpult zuletzt","Mischpult zuerst, Lautsprecher zuletzt","Egal","Alles gleichzeitig"],"a":1,"e":"„Last on, first off”: Lautsprecher zuletzt an, zuerst aus – schützt vor Knackgeräuschen."},
 {"q":"Was prüfst du beim Line Check?","o":["Den Geschmack des Sounds","Ob auf jedem Kanal überhaupt ein Signal ankommt","Die Lichtanlage","Den Hall"],"a":1,"e":"Line Check = kanalweise prüfen, ob Kabel/Verbindungen Signal liefern."},
 {"q":"Womit beginnt ein klassischer Soundcheck der Einzelkanäle?","o":["Gesang","Kick Drum / Fundament","Gitarre","Keyboard"],"a":1,"e":"Man baut von unten auf: Kick, Snare, … bis hoch zum Gesang."},
 {"q":"Was machst du laut Best Practice ZUERST – Monitor oder FOH?","o":["FOH-Mix","Monitor-Mix","Effekte","Aufnahme"],"a":1,"e":"Zufriedene Musiker, die sich hören, spielen besser – das ist dein bester FOH-Helfer."},
 {"q":"Du hast nur 10 Minuten. Was hat Priorität?","o":["Feine EQ-Justage","Kick + Snare + Bass + Gesang + Monitore","Effekte und Hall","Perfekte Stereobreite"],"a":1,"e":"Pflicht vor Kür: Fundament, Gesang und Monitoring zuerst."},
 {"q":"Wie diagnostizierst du „kein Ton auf einem Kanal”?","o":["Sofort Kabel kaufen","Systematisch: Mute? Fader? Gain? Kabel? Phantom? Routing?","Master aufdrehen","Pult neu starten"],"a":1,"e":"Systematisch dem Signalfluss folgen – meist liegt es an Mute, Gain oder Kabel."},
],
8: [
 {"q":"Was macht ein Kompressor?","o":["Macht leise Stellen lauter, Schluss","Verringert die Lautstärke über dem Threshold → gleichmäßigeres Signal","Filtert Frequenzen","Erzeugt Hall"],"a":1,"e":"Über dem Threshold drückt er den Pegel – das Signal wird gleichmäßiger."},
 {"q":"Der Threshold bestimmt …","o":["wie stark komprimiert wird","ab welchem Pegel der Kompressor eingreift","wie schnell er reagiert","den Ausgangspegel"],"a":1,"e":"Threshold = Schwelle. Darüber arbeitet der Kompressor, darunter nicht."},
 {"q":"Welcher Attack erhält den Punch einer Kick Drum?","o":["Sehr schneller Attack","Langsamer Attack (Transiente kommt zuerst durch)","Threshold ganz hoch","Ratio ∞:1"],"a":1,"e":"Langsamer Attack lässt den Anschlag durch, dann greift der Kompressor – mehr Punch."},
 {"q":"Was ist ein Gate?","o":["Ein EQ","Lässt Signal nur durch, wenn es laut genug ist","Ein Halleffekt","Ein Limiter"],"a":1,"e":"Das Gate öffnet erst über dem Threshold – klassisch zum Entfernen von Übersprechen bei Drums."},
 {"q":"Worauf reagiert ein De-Esser?","o":["Auf Bässe","Auf Zischlaute (ca. 6–10 kHz)","Auf die Kick","Auf Feedback"],"a":1,"e":"Der De-Esser ist ein Kompressor für sibilante S-/Sch-Laute bei 6–10 kHz."},
 {"q":"Welcher Gain-Reduction-Wert ist im Live-Sound oft ausreichend?","o":["–20 bis –30 dB","–3 bis –6 dB","0 dB","–15 dB dauerhaft"],"a":1,"e":"–3 bis –6 dB GR reichen meist; mehr klingt schnell „totgequetscht”."},
],
9: [
 {"q":"Was bleibt beim Wechsel von analog zu digital gleich?","o":["Nichts","Die Konzepte: Signalfluss, Gain, EQ, Aux, Fader","Nur das Gehäuse","Nur die Farbe"],"a":1,"e":"Das analoge Denken ist 100 % übertragbar – digital ist nur die „Verpackung”."},
 {"q":"Was ist ein Layer?","o":["Ein Effekt","Eine Schicht, die festlegt, welche Kanäle gerade auf den Fadern liegen","Ein Kabel","Ein Mikrofontyp"],"a":1,"e":"Mit Layern steuern wenige physische Fader viele Kanäle (z. B. 1–16, dann 17–32)."},
 {"q":"Was ist ein DCA?","o":["Ein echter Mix-Bus","Eine Fernbedienung für eine Kanalgruppe ohne Signalzusammenlegung","Ein Kompressor","Ein Reverb"],"a":1,"e":"Ein DCA steuert die Pegel mehrerer Kanäle gemeinsam, ohne ihre Signale zusammenzulegen."},
 {"q":"Was ist der größte Vorteil digitaler Pulte?","o":["Sie rauschen mehr","Szenen/Snapshots speichern alle Einstellungen","Sie haben keine Latenz","Sie brauchen keinen Strom"],"a":1,"e":"Komplette Zustände lassen sich speichern und abrufen – ideal z. B. beim Bandwechsel."},
 {"q":"Was ist beim Remote Mixing per Tablet ein Risiko?","o":["Zu guter Klang","Verbindungsabbrüche / Latenz – jemand muss zur Not ans Pult","Keine Farben","Zu wenig Kanäle"],"a":1,"e":"WLAN kann abbrechen; im Notfall muss jemand am physischen Pult sein."},
 {"q":"Wie debuggst du Routing-Fehler am besten?","o":["Pult zurücksetzen","Systematisch von vorne: Signal am Eingang? im L/R-Bus? am Ausgang?","Neue Szene laden","Gain erhöhen"],"a":1,"e":"Schritt für Schritt dem Weg folgen – Routing-Fehler sind häufig nach dem Laden alter Szenen."},
],
10: [
 {"q":"Was ist eine DAW?","o":["Ein Mikrofon","Die Software zum Aufnehmen/Mischen am Computer","Ein Kabeltyp","Ein Lautsprecher"],"a":1,"e":"DAW = Digital Audio Workstation, z. B. Reaper, Logic, Cubase."},
 {"q":"Wozu dient ein Audiointerface?","o":["Strom liefern","Analoge Signale in digitale wandeln und umgekehrt (Verbindung Mikro ↔ Computer)","Hall erzeugen","Kabel testen"],"a":1,"e":"Das Interface wandelt (ADC/DAC) und verbindet Mikrofone/Instrumente mit dem Rechner."},
 {"q":"Welcher Eingangspegel ist beim Aufnehmen anzustreben?","o":["0 dBFS (Vollausschlag)","–6 bis –3 dBFS, nicht clippen","möglichst rot","möglichst leise"],"a":1,"e":"Etwas Headroom (–6 bis –3 dBFS) lassen, damit nichts clippt."},
 {"q":"Welches Format eignet sich für die Archivierung/Master?","o":["MP3","WAV (verlustfrei)","AAC","Nur Streaming"],"a":1,"e":"WAV ist verlustfrei (z. B. 24 Bit/48 kHz); MP3 nutzt man zum Teilen."},
 {"q":"Wohin darf der Clicktrack NIEMALS?","o":["In den Monitor des Schlagzeugers","In die FOH-PA","In die DAW","Ins In-Ear"],"a":1,"e":"Der Klick ist nur fürs Timing der Band – nie ins Publikum (FOH)."},
],
11: [
 {"q":"Was ersetzt eine Digitalsnake?","o":["Das Mischpult","Das analoge Multicore-Kabel","Die Lautsprecher","Die Mikrofone"],"a":1,"e":"Statt dickem Multicore überträgt ein schlankes Netzwerk-/Glasfaserkabel die Signale digital."},
 {"q":"Was ist der Vorteil von Dante (Audio-over-IP)?","o":["Nur 2 Kanäle möglich","Hunderte Kanäle über ein Netzwerkkabel, geräteunabhängig","Es ist analog","Keine Konfiguration nötig"],"a":1,"e":"Dante ist ein herstellerübergreifender Standard für sehr viele Kanäle über Ethernet."},
 {"q":"Worauf musst du bei Funkmikrofonen besonders achten?","o":["Auf die Kabelfarbe","Batteriezustand und störungsfreie Frequenz-Koordinierung","Auf den Hall","Auf die Phantomspannung"],"a":1,"e":"Frische Akkus und koordinierte, sich nicht störende Frequenzen sind entscheidend."},
 {"q":"Woran erkennst du ein Phasenproblem?","o":["Zu viele Höhen","Dünner, „hohler” Klang; Bass verschwindet bei zwei Mikros","Zu viel Hall","Clipping"],"a":1,"e":"Gegenläufige Signale löschen sich teilweise aus – Test: Phase eines Kanals drehen."},
 {"q":"Ein Delay-Speaker 20 m hinter der Haupt-PA braucht ca. wie viel Delay?","o":["6 ms","58 ms","580 ms","kein Delay"],"a":1,"e":"20 m ÷ 343 m/s ≈ 58 ms, damit beide Signale gleichzeitig ankommen."},
 {"q":"Wie löst man eine Masseschleife (Brummen 50/100 Hz)?","o":["Mehr Gain","DI-Box mit Ground-Lift","Mehr Hall","Phantom ausschalten"],"a":1,"e":"Der Ground-Lift trennt die Masseverbindung des Audiosignals und unterbricht die Schleife."},
],
12: [
 {"q":"Was ist die wichtigste Haltung im stressigen Livebetrieb?","o":["Hektisch alles gleichzeitig lösen","Ruhe bewahren – ein Problem nach dem anderen","Sofort die Band beschuldigen","Das Pult neu starten"],"a":1,"e":"Atmen, eine Sache nach der anderen – ruhige Analyse ist schneller als Hektik."},
 {"q":"Ein Musiker sagt „mehr Ich”. Was meint er?","o":["Mehr Hall","Sein eigenes Instrument im Monitor lauter","Mehr Bass im FOH","Lauteres Schlagzeug"],"a":1,"e":"„Mehr Ich” = mehr vom eigenen Instrument/der eigenen Stimme im Monitor."},
 {"q":"Wie kommunizierst du gut mit Musikern?","o":["Von oben herab, du weißt es besser","Zuhören, nachfragen, klar und auf Augenhöhe","Möglichst kompliziert","Gar nicht"],"a":1,"e":"Erst verstehen, was wirklich gebraucht wird – dann klar und respektvoll handeln."},
 {"q":"Was bedeutet professionelles Auftreten u. a.?","o":["Handy am Pult checken","Pünktlich sein, kein Getränk aufs Pult, fokussiert bleiben","Möglichst auffallen","Fehler verschweigen für immer"],"a":1,"e":"Pünktlichkeit, Fokus, Ordnung und Verlässlichkeit zeichnen Profis aus."},
 {"q":"Was gehört zur Verantwortung eines Technikers?","o":["Fehler vertuschen","Fehler zugeben, Equipment pflegen, pünktlich sein","Nur das Pult bedienen","Geräte selbst öffnen"],"a":1,"e":"Verantwortung heißt: zu Fehlern stehen, Material pflegen und zuverlässig sein."},
],
13: [
 {"q":"Womit solltest du laut Übung 13.1 zuerst üben?","o":["Das ganze Schlagzeug","Nur den Gesangskanal vollständig einstellen","Den Master-Bus","Effekte"],"a":1,"e":"Erst einen Gesangskanal komplett (Gain, HPF, EQ, Kompressor) beherrschen."},
 {"q":"Wie spürst du beim „Ringing Out” Feedback-Frequenzen auf?","o":["Master aufdrehen","Mit schmalem Boost suchen, dann an der Stelle absenken","Alle Höhen senken","Phantom an"],"a":1,"e":"Boost zum Finden, dann Cut – so machst du den Monitor lauter ohne Feedback."},
 {"q":"Was trainiert „Blindes Hören”?","o":["Schnelles Kabelwickeln","Frequenzen/Effekte ohne Hinsehen erkennen","Lötkenntnisse","Notenlesen"],"a":1,"e":"Jemand verändert etwas, du beschreibst es nur nach Gehör – das schult das analytische Ohr."},
 {"q":"Welche Übung ist „die beste Schule überhaupt”?","o":["Nur Theorie lesen","Einen echten Mini-Livegig eigenständig betreuen","YouTube schauen","Das Handbuch auswendig lernen"],"a":1,"e":"Echte Verantwortung bei einem kleinen Gig bringt am meisten – inkl. Selbstreflexion danach."},
 {"q":"Was solltest du nach jedem Gig tun?","o":["Sofort heimgehen","Kurze schriftliche Selbstreflexion (was lief gut/schlecht?)","Nichts","Die Band kritisieren"],"a":1,"e":"15 Minuten Reflexion festigen das Gelernte und zeigen Verbesserungspunkte."},
],
14: [
 {"q":"Wie vermeidest du „zu viel Gain”?","o":["Beim leisesten Moment einstellen","Beim lautesten Spielmoment einstellen, nie dauerhaft rot","Gain ganz aufdrehen","Fader statt Gain nutzen"],"a":1,"e":"Beim lautesten Moment einpegeln – lieber etwas zu wenig Gain als Clipping."},
 {"q":"Was ist die beste Maßnahme gegen einen matschigen, basslastigen Mix?","o":["Bass überall boosten","HPF auf allen Nicht-Bass-Kanälen aktivieren","Mehr Hall","Master runter"],"a":1,"e":"Bass kommt nicht vom Boost, sondern von subtraktivem EQ/HPF auf den anderen Kanälen."},
 {"q":"Was gilt für Hall im Livebetrieb?","o":["Viel hilft viel","Weniger ist meist besser; kurze Decay-Zeiten","Immer maximaler Decay","Hall auf jeden Kanal"],"a":1,"e":"Der Raum hallt ohnehin – zu viel künstlicher Hall verwäscht den Mix."},
 {"q":"Woran erkennst du übermäßige Kompression?","o":["Viel Dynamik","Flacher, „toter” Sound ohne Punch; GR-Meter dauerhaft tief","Mehr Bass","Mehr Höhen"],"a":1,"e":"Wenn alles gleich laut klingt und der Punch fehlt, ist zu stark komprimiert."},
 {"q":"Warum sind schlechte Monitorwege so problematisch?","o":["Sie kosten Strom","Musiker hören sich nicht → spielen unsicher, Feedback-Teufelskreis","Sie sehen schlecht aus","Sie brauchen Phantom"],"a":1,"e":"Zuerst individuelle Monitor-Mixe machen – sonst leiden Spiel und Feedback-Situation."},
 {"q":"Was hilft gegen unsauberes Routing?","o":["Routing ignorieren","Routing-Check vor jedem Soundcheck, Kanäle solo prüfen","Alte Szene blind laden","Mehr Gain"],"a":1,"e":"Kanäle einzeln solieren und Labels prüfen – besonders nach dem Laden alter Szenen."},
],
15: [
 {"q":"Was bewirken Bassfallen (Bass Traps)?","o":["Höhen schlucken","Tiefe Frequenzen in Raumecken absorbieren","Schall streuen","Den Raum lauter machen"],"a":1,"e":"Bassfallen sind große Absorber für tiefe Frequenzen, typischerweise in Ecken."},
 {"q":"Was misst LUFS?","o":["Spitzenpegel","Die wahrgenommene Lautheit","Die Frequenz","Die Latenz"],"a":1,"e":"LUFS misst die empfundene Lautheit – Grundlage der Streaming-Normalisierung."},
 {"q":"Auf welchen Zielwert normalisiert Spotify etwa?","o":["–23 LUFS","–14 LUFS","0 LUFS","+6 LUFS"],"a":1,"e":"Spotify/YouTube zielen auf ca. –14 LUFS, Film/TV auf –23 LUFS."},
 {"q":"Was kennzeichnet einen Broadcast-Mix?","o":["Mehr Hall","Weniger Hall, mehr Kompression, normiert, sehr verständlich","Lauter als alles","Kein Gesang"],"a":1,"e":"Für TV/Streaming wird kontrollierter und verständlicher gemischt und normiert."},
 {"q":"Was bleibt laut Kapitel trotz aller Technik entscheidend?","o":["Die teuerste Hardware","Das Gehör, das Urteilsvermögen und der Umgang mit Menschen","Die Anzahl der Kanäle","Reine Automatik/KI"],"a":1,"e":"Kein Algorithmus ersetzt Ohr, Urteilsvermögen und Teamfähigkeit."},
],
16: [
 {"q":"Wofür ist dieses Kapitel gedacht?","o":["Als Prüfung","Als persönliches Tagebuch für eigene Erfahrungen","Als Werbung","Als Vertrag"],"a":1,"e":"Eigene Erfahrungen bleiben am besten hängen – nutze das Logbuch aktiv."},
 {"q":"Was solltest du dir bei einem analogen Pult unbedingt notieren?","o":["Die Farbe der Fader","Gain-Werte und gute EQ-Einstellungen pro Kanal","Das Wetter","Die Uhrzeit"],"a":1,"e":"Notierte Gain-/EQ-Werte sparen beim nächsten Mal viel Zeit."},
 {"q":"Was ist ein guter Lern-Tipp aus dem Schlusswort?","o":["Nie Fehler machen","So viele Proben/Gigs wie möglich machen und aus Fehlern lernen","Nur lesen","Allein arbeiten"],"a":1,"e":"Praxis, Beobachten, Fragen stellen und keine Angst vor Fehlern – so wächst du."},
 {"q":"Was solltest du beim Üben/Experimentieren beachten?","o":["Immer beim wichtigen Konzert testen","Neues lieber bei der Probe ausprobieren, nicht beim Gig","Gar nicht experimentieren","Ohne Plan ändern"],"a":1,"e":"Experimente gehören in die Probe – beim Konzert zählt Verlässlichkeit."},
],
}
