# -*- coding: utf-8 -*-
"""Gemeinsames Studio-/Konsolen-Theme (dunkel). Wird in jede HTML-Datei inline kopiert."""

CSS = r"""
:root{
  --bg:#0e1116; --bg2:#161b22; --panel:#1c232d; --panel2:#232c38;
  --line:#2d3744; --txt:#e6edf3; --muted:#9aa7b4; --dim:#6b7785;
  --accent:#ff7a1a; --accent2:#27c2a0; --blue:#3b9dff;
  --green:#37d67a; --yellow:#ffd23f; --red:#ff5c5c; --purple:#b98cff;
  --radius:14px; --radius-s:9px; --shadow:0 6px 24px rgba(0,0,0,.35);
  --mono:'SFMono-Regular',ui-monospace,Consolas,'Liberation Mono',Menlo,monospace;
  --sans:'Segoe UI',system-ui,-apple-system,Roboto,Helvetica,Arial,sans-serif;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{
  margin:0;background:linear-gradient(180deg,#0c0f14,#0e1116 240px);color:var(--txt);
  font-family:var(--sans);font-size:17px;line-height:1.65;-webkit-font-smoothing:antialiased;
}
a{color:var(--blue);text-decoration:none}
a:hover{text-decoration:underline}

/* ---------- Topbar ---------- */
.topbar{
  position:sticky;top:0;z-index:50;display:flex;align-items:center;gap:14px;
  padding:10px 18px;background:rgba(14,17,22,.86);backdrop-filter:blur(8px);
  border-bottom:1px solid var(--line);
}
.topbar .home{display:flex;align-items:center;gap:8px;font-weight:600;color:var(--txt)}
.topbar .home:hover{color:var(--accent);text-decoration:none}
.topbar .crumb{color:var(--muted);font-size:14px}
.topbar .spacer{flex:1}
.btn{
  font-family:var(--sans);font-size:14px;font-weight:600;cursor:pointer;
  border:1px solid var(--line);background:var(--panel);color:var(--txt);
  padding:7px 14px;border-radius:999px;transition:.15s;
}
.btn:hover{border-color:var(--accent);color:var(--accent)}
.btn.warnstop{border-color:#5a2b2b;color:#ffb3b3}
.btn.warnstop:hover{background:#3a1d1d;border-color:var(--red);color:#fff}
.btn.primary{background:var(--accent);border-color:var(--accent);color:#160a02}
.btn.primary:hover{filter:brightness(1.08);color:#160a02}
.btn:disabled{opacity:.4;cursor:not-allowed}

/* ---------- Layout ---------- */
main{max-width:880px;margin:0 auto;padding:34px 22px 90px}
h1{font-size:2.05rem;line-height:1.2;margin:.2em 0 .1em;letter-spacing:-.5px}
h2{font-size:1.5rem;margin:1.9em 0 .5em;padding-top:.3em;border-top:1px solid var(--line)}
h2:first-of-type{border-top:none}
h3{font-size:1.18rem;margin:1.5em 0 .4em;color:#f2f6fb}
h4{font-size:1.02rem;margin:1.2em 0 .3em;color:var(--muted);text-transform:uppercase;letter-spacing:.04em}
p{margin:.7em 0}
ul,ol{margin:.6em 0;padding-left:1.4em}
li{margin:.28em 0}
strong{color:#fff}
hr{border:none;border-top:1px dashed var(--line);margin:1.6em 0}
code{font-family:var(--mono);background:#10151c;border:1px solid var(--line);
  padding:.08em .4em;border-radius:6px;font-size:.88em;color:#ffcaa0}
pre.ascii{
  background:#0b0e13;border:1px solid var(--line);border-left:3px solid var(--accent);
  border-radius:var(--radius-s);padding:14px 16px;overflow-x:auto;margin:1.1em 0;
}
pre.ascii code{background:none;border:none;padding:0;color:#bcd2e6;font-size:.86em;line-height:1.5;white-space:pre}

/* ---------- Tables ---------- */
.tablewrap{overflow-x:auto;margin:1.1em 0}
table{border-collapse:collapse;width:100%;font-size:.95rem;background:var(--panel);
  border-radius:var(--radius-s);overflow:hidden}
th,td{padding:9px 13px;text-align:left;border-bottom:1px solid var(--line);vertical-align:top}
th{background:var(--panel2);color:#fff;font-weight:600;font-size:.86rem;text-transform:uppercase;letter-spacing:.03em}
tr:last-child td{border-bottom:none}
tbody tr:hover{background:#202935}

/* ---------- Callouts ---------- */
.callout{margin:1.2em 0;padding:14px 16px 14px 50px;border-radius:var(--radius-s);position:relative;
  border:1px solid var(--line);background:var(--panel)}
.callout::before{position:absolute;left:14px;top:13px;font-size:1.25rem;line-height:1}
.callout.tip{background:rgba(39,194,160,.08);border-color:rgba(39,194,160,.4)}
.callout.tip::before{content:"💡"}
.callout.warn{background:rgba(255,92,92,.08);border-color:rgba(255,92,92,.42)}
.callout.warn::before{content:"⚠️"}
.callout.note{background:var(--panel);padding-left:16px}
.callout.note::before{content:""}
.callout p:first-child{margin-top:0}
.callout p:last-child{margin-bottom:0}

/* intro box under H1 */
.intro{background:linear-gradient(135deg,rgba(255,122,26,.12),rgba(59,157,255,.08));
  border:1px solid var(--line);border-left:4px solid var(--accent);
  padding:16px 18px;border-radius:var(--radius-s);margin:1em 0 1.4em;font-size:1.03rem}
.intro p:first-child{margin-top:0}.intro p:last-child{margin-bottom:0}

/* term cards (Begriffs-Abbildungen mit Foto-Link) */
.termcards{display:flex;flex-wrap:wrap;gap:12px;margin:1.1em 0}
.termcard{display:flex;gap:13px;align-items:center;background:var(--panel);border:1px solid var(--line);
  border-radius:var(--radius-s);padding:12px 14px;flex:1 1 250px;min-width:240px}
.termcard .termsvg{flex:none;width:84px;height:84px;display:flex;align-items:center;justify-content:center;
  background:#0b0e13;border:1px solid var(--line);border-radius:8px}
.termcard .termsvg svg{width:74px;height:74px}
.termcard .termmeta{display:flex;flex-direction:column;gap:3px;min-width:0}
.termcard .termmeta b{color:#fff;font-size:.97rem}
.termcard .termmeta span{color:var(--muted);font-size:.82rem;line-height:1.4}
.termcard a.photo{font-size:.82rem;font-weight:600;margin-top:3px}

/* figures */
figure{margin:1.4em 0;text-align:center}
figure img{max-width:100%;height:auto;border-radius:var(--radius-s);
  background:#fff;padding:8px;box-shadow:var(--shadow)}
figcaption{color:var(--muted);font-size:.88rem;margin-top:.5em;font-style:italic}

/* checklists (from markdown - [ ]) */
ul.checklist{list-style:none;padding-left:0}
ul.checklist li{display:flex;gap:10px;align-items:flex-start;padding:6px 10px;border-radius:8px}
ul.checklist li:hover{background:#1a212b}
ul.checklist input{margin-top:5px;width:17px;height:17px;accent-color:var(--accent);flex:none;cursor:pointer}
ul.checklist li.done label{color:var(--dim);text-decoration:line-through}
ul.checklist label{cursor:pointer}

/* ---------- Interactive section & widgets ---------- */
.interaktiv{margin:2.4em 0 1em;padding:20px 20px 24px;border-radius:var(--radius);
  background:radial-gradient(120% 120% at 0% 0%,rgba(59,157,255,.10),transparent),var(--bg2);
  border:1px solid var(--line)}
.interaktiv>h2{border:none;margin-top:0;display:flex;align-items:center;gap:10px}
.interaktiv .lead{color:var(--muted);margin-top:-.3em}
.widget{background:var(--panel);border:1px solid var(--line);border-radius:var(--radius-s);
  padding:16px;margin:16px 0}
.widget h3{margin-top:0;font-size:1.05rem}
.audiohint{font-size:.8rem;color:var(--dim);display:flex;align-items:center;gap:6px;margin:.4em 0}
.row{display:flex;flex-wrap:wrap;gap:10px;align-items:center;margin:10px 0}
.chips{display:flex;flex-wrap:wrap;gap:8px}
.chip{cursor:pointer;border:1px solid var(--line);background:var(--panel2);color:var(--txt);
  padding:8px 13px;border-radius:999px;font-size:.9rem;transition:.12s;font-weight:600;font-family:var(--sans)}
.chip:hover{border-color:var(--blue);transform:translateY(-1px)}
.chip.active{background:var(--blue);border-color:var(--blue);color:#04121f}
.chip.correct{background:var(--green);border-color:var(--green);color:#062012}
.chip.wrong{background:var(--red);border-color:var(--red);color:#fff}
label.fld{display:flex;flex-direction:column;gap:4px;font-size:.82rem;color:var(--muted);min-width:120px}
label.fld b{color:var(--txt);font-family:var(--mono);font-size:.95rem}
input[type=range]{width:100%;accent-color:var(--accent);height:22px}
select,input[type=number]{font-family:var(--sans);background:#10151c;color:var(--txt);
  border:1px solid var(--line);border-radius:8px;padding:7px 10px;font-size:.95rem}
.readout{font-family:var(--mono);font-size:.95rem;color:var(--accent2)}
canvas{max-width:100%;background:#0b0e13;border:1px solid var(--line);border-radius:8px;display:block}

/* meter */
.meter{height:16px;border-radius:6px;background:#0b0e13;border:1px solid var(--line);overflow:hidden;position:relative}
.meter>span{position:absolute;left:0;top:0;bottom:0;width:0%;
  background:linear-gradient(90deg,var(--green) 0%,var(--green) 60%,var(--yellow) 80%,var(--red) 100%);
  transition:width .05s linear}
.lr{display:flex;gap:6px;align-items:center}.lr b{font-family:var(--mono);width:14px;color:var(--muted)}

.feedbackline{font-size:.92rem;margin-top:10px;padding:10px 12px;border-radius:8px;display:none}
.feedbackline.show{display:block}
.feedbackline.ok{background:rgba(55,214,122,.12);border:1px solid rgba(55,214,122,.4);color:#a9f0c6}
.feedbackline.no{background:rgba(255,92,92,.12);border:1px solid rgba(255,92,92,.4);color:#ffc2c2}

/* ---------- Quiz ---------- */
.quiz{margin-top:2.6em;padding:22px;border-radius:var(--radius);
  background:linear-gradient(135deg,rgba(255,122,26,.07),transparent),var(--bg2);border:1px solid var(--line)}
.quiz h2{border:none;margin:0 0 .2em;display:flex;align-items:center;gap:10px}
.quiz .qmeta{color:var(--muted);font-size:.9rem;margin-bottom:1em}
.qcard{background:var(--panel);border:1px solid var(--line);border-radius:var(--radius-s);
  padding:16px 18px;margin:14px 0}
.qcard .qnum{color:var(--accent);font-family:var(--mono);font-size:.8rem}
.qcard .qtext{font-weight:600;margin:.2em 0 .8em;font-size:1.05rem}
.qopt{display:block;width:100%;text-align:left;cursor:pointer;border:1px solid var(--line);
  background:var(--panel2);color:var(--txt);padding:11px 14px;border-radius:9px;margin:7px 0;
  font-size:.98rem;font-family:var(--sans);transition:.12s}
.qopt:hover:not(:disabled){border-color:var(--blue)}
.qopt:disabled{cursor:default}
.qopt.sel{border-color:var(--blue)}
.qopt.correct{background:rgba(55,214,122,.16);border-color:var(--green)}
.qopt.wrong{background:rgba(255,92,92,.16);border-color:var(--red)}
.qexpl{display:none;margin-top:10px;padding:11px 13px;border-radius:8px;font-size:.93rem;
  background:#10151c;border:1px solid var(--line)}
.qexpl.show{display:block}
.qexpl b{color:var(--accent2)}
.quizresult{margin-top:18px;padding:18px;border-radius:var(--radius-s);text-align:center;
  background:var(--panel);border:1px solid var(--line);display:none}
.quizresult.show{display:block}
.quizresult .score{font-size:2.2rem;font-weight:800;font-family:var(--mono)}
.badge{display:inline-block;padding:3px 10px;border-radius:999px;font-size:.8rem;font-weight:700;margin-left:8px}
.badge.gold{background:var(--yellow);color:#241c00}
.badge.ok{background:var(--green);color:#062012}
.badge.try{background:var(--panel2);color:var(--muted);border:1px solid var(--line)}

/* ---------- Chapter nav ---------- */
.chapnav{display:flex;justify-content:space-between;gap:12px;margin-top:42px}
.chapnav a{flex:1;padding:14px 16px;border:1px solid var(--line);border-radius:var(--radius-s);
  background:var(--panel);transition:.15s;display:flex;flex-direction:column;gap:2px}
.chapnav a:hover{border-color:var(--accent);text-decoration:none;background:var(--panel2)}
.chapnav a .dir{font-size:.78rem;color:var(--muted)}
.chapnav a .ttl{color:var(--txt);font-weight:600}
.chapnav a.next{text-align:right}
.chapnav a.disabled{opacity:.35;pointer-events:none}

footer{border-top:1px solid var(--line);color:var(--dim);font-size:.85rem;
  text-align:center;padding:26px 18px 40px}

/* ---------- Index hub ---------- */
.hero{max-width:980px;margin:0 auto;padding:46px 22px 8px;text-align:center}
.hero h1{font-size:2.5rem}
.hero p.sub{color:var(--muted);font-size:1.12rem;max-width:680px;margin:.4em auto 1.2em}
.progresswrap{max-width:620px;margin:18px auto;background:var(--panel);border:1px solid var(--line);
  border-radius:999px;height:26px;overflow:hidden;position:relative}
.progresswrap>span{position:absolute;left:0;top:0;bottom:0;width:0%;
  background:linear-gradient(90deg,var(--accent),var(--accent2));transition:width .6s ease}
.progresswrap em{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;
  font-style:normal;font-size:.82rem;font-weight:700;color:#fff;text-shadow:0 1px 2px rgba(0,0,0,.6)}
.hubgrid{max-width:980px;margin:8px auto;padding:10px 22px 40px;display:grid;
  grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:16px}
.sectionhead{max-width:980px;margin:30px auto 0;padding:0 22px;color:var(--accent);
  font-size:.85rem;font-weight:700;text-transform:uppercase;letter-spacing:.12em}
.card{display:flex;flex-direction:column;gap:6px;padding:18px;border-radius:var(--radius);
  background:var(--panel);border:1px solid var(--line);transition:.16s;position:relative;overflow:hidden}
.card:hover{transform:translateY(-3px);border-color:var(--accent);text-decoration:none;box-shadow:var(--shadow)}
.card .knum{font-family:var(--mono);font-size:.78rem;color:var(--muted)}
.card .kicon{font-size:1.7rem}
.card .ktitle{font-size:1.12rem;font-weight:700;color:var(--txt);line-height:1.25}
.card .kdesc{font-size:.88rem;color:var(--muted)}
.card .kstatus{margin-top:8px;font-size:.8rem;font-weight:700;display:flex;align-items:center;gap:6px}
.card .kstatus.done{color:var(--green)}
.card .kstatus.part{color:var(--yellow)}
.card .kstatus.todo{color:var(--dim)}
.card.bonus{background:linear-gradient(135deg,rgba(185,140,255,.14),var(--panel));border-color:rgba(185,140,255,.4)}
.tools{max-width:980px;margin:0 auto 40px;padding:0 22px;display:flex;gap:10px;justify-content:center;flex-wrap:wrap}

@media (max-width:560px){
  body{font-size:16px}
  main{padding:22px 15px 80px}
  h1{font-size:1.7rem}.hero h1{font-size:2rem}
  .chapnav{flex-direction:column}
}
"""
