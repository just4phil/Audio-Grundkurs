# -*- coding: utf-8 -*-
"""Gemeinsames JavaScript: Audio-Helper, Quiz-Engine, Persistenz, Widget-Bibliothek.
   Wird in jede HTML-Datei inline kopiert (self-contained, keine externen Requests)."""

JS = r"""
//============================ Helpers ============================
function q(id){return document.getElementById(id);}
function flash(el){el.classList.add('active');setTimeout(()=>el.classList.remove('active'),250);}
function sliderField(o){
  const w=document.createElement('label');w.className='fld';
  const t=document.createElement('span');t.textContent=o.label;
  const b=document.createElement('b');
  const i=document.createElement('input');i.type='range';i.min=o.min;i.max=o.max;i.step=o.step;i.value=o.val;
  const fmt=o.fmt||(v=>v+(o.unit||''));b.textContent=fmt(+o.val);
  i.oninput=()=>{b.textContent=fmt(+i.value);o.on&&o.on(+i.value);};
  w.appendChild(t);w.appendChild(i);w.appendChild(b);w._input=i;w._read=b;return w;
}
function btn(label,cls){const b=document.createElement('button');b.type='button';
  b.className='btn'+(cls?' '+cls:'');b.textContent=label;return b;}

//============================ Audio engine ============================
const Snd={
  ctx:null,master:null,active:new Set(),_nb:null,
  init(){const C=window.AudioContext||window.webkitAudioContext;
    if(!this.ctx){this.ctx=new C();this.master=this.ctx.createGain();
      this.master.gain.value=0.28;this.master.connect(this.ctx.destination);}
    if(this.ctx.state==='suspended')this.ctx.resume();
    document.querySelectorAll('.js-audio-on').forEach(e=>e.classList.add('on'));
    const sb=q('audioStop');if(sb)sb.disabled=false;
    return this.ctx;},
  reg(n){this.active.add(n);return n;},
  osc(freq,type){this.init();const c=this.ctx,o=c.createOscillator(),g=c.createGain();
    o.type=type||'sine';o.frequency.value=freq;g.gain.value=0;o.connect(g);g.connect(this.master);
    o.start();g.gain.setTargetAtTime(0.9,c.currentTime,0.015);
    const n={o,g,node:g,setFreq:f=>o.frequency.setTargetAtTime(f,c.currentTime,0.03),
      setGain:v=>g.gain.setTargetAtTime(v,c.currentTime,0.03),
      stop:()=>{try{g.gain.setTargetAtTime(0,c.currentTime,0.05);o.stop(c.currentTime+0.14);}catch(e){}this.active.delete(n);}};
    return this.reg(n);},
  beep(freq,dur,type){const n=this.osc(freq,type);setTimeout(()=>n.stop(),(dur||0.6)*1000);return n;},
  noiseBuf(){if(!this._nb){const c=this.init(),len=c.sampleRate*2,b=c.createBuffer(1,len,c.sampleRate),d=b.getChannelData(0);
    let last=0;for(let i=0;i<len;i++){const w=Math.random()*2-1;last=(last+0.02*w)/1.02;d[i]=last*3.2;}this._nb=b;}return this._nb;},
  noise(){this.init();const s=this.ctx.createBufferSource();s.buffer=this.noiseBuf();s.loop=true;
    const g=this.ctx.createGain();g.gain.value=0;s.connect(g);s.start();
    g.gain.setTargetAtTime(0.6,this.ctx.currentTime,0.02);
    const n={src:s,g,node:g,setGain:v=>g.gain.setTargetAtTime(v,this.ctx.currentTime,0.03),
      stop:()=>{try{g.gain.setTargetAtTime(0,this.ctx.currentTime,0.05);s.stop(this.ctx.currentTime+0.15);}catch(e){}this.active.delete(n);}};
    return this.reg(n);},
  impulse(seconds,decay){const c=this.init(),len=c.sampleRate*seconds,b=c.createBuffer(2,len,c.sampleRate);
    for(let ch=0;ch<2;ch++){const d=b.getChannelData(ch);
      for(let i=0;i<len;i++)d[i]=(Math.random()*2-1)*Math.pow(1-i/len,decay);}return b;},
  stopAll(){this.active.forEach(n=>{try{n.stop()}catch(e){}});this.active.clear();
    document.querySelectorAll('.js-audio-on').forEach(e=>e.classList.remove('on'));
    document.querySelectorAll('[data-toggle]').forEach(b=>{b.dataset.toggle='';b.classList.remove('primary');
      if(b.dataset.onlabel)b.textContent=b.dataset.offlabel||b.textContent;});}
};
function toggleBtn(b,onLabel,offLabel,start,stop){
  b.dataset.offlabel=offLabel;b.textContent=offLabel;
  b.onclick=()=>{if(b.dataset.toggle){b.dataset.toggle='';b.classList.remove('primary');b.textContent=offLabel;stop();}
    else{b.dataset.toggle='1';b.classList.add('primary');b.textContent=onLabel;start();}};
}

//============================ Quiz engine ============================
function initQuiz(){
  const data=window.QUIZ,key=window.QUIZ_KEY,host=q('quiz-cards');if(!data||!host)return;
  const st={ans:0,cor:0};
  data.forEach((item,qi)=>{
    const card=document.createElement('div');card.className='qcard';
    const num=document.createElement('div');num.className='qnum';num.textContent='Frage '+(qi+1)+' / '+data.length;
    const txt=document.createElement('div');txt.className='qtext';txt.textContent=item.q;
    card.appendChild(num);card.appendChild(txt);
    const opts=[];
    item.o.forEach((opt,oi)=>{const b=document.createElement('button');b.type='button';b.className='qopt';b.textContent=opt;
      b.onclick=()=>{if(card.dataset.done)return;card.dataset.done='1';st.ans++;
        const ok=oi===item.a;if(ok)st.cor++;
        opts.forEach((bb,bi)=>{bb.disabled=true;if(bi===item.a)bb.classList.add('correct');if(bi===oi&&!ok)bb.classList.add('wrong');});
        ex.classList.add('show');if(st.ans===data.length)finish();};
      opts.push(b);card.appendChild(b);});
    const ex=document.createElement('div');ex.className='qexpl';
    const eb=document.createElement('b');eb.textContent='Erklärung: ';ex.appendChild(eb);ex.appendChild(document.createTextNode(item.e));
    card.appendChild(ex);host.appendChild(card);
  });
  const res=document.createElement('div');res.className='quizresult';res.id='quiz-result';host.parentNode.appendChild(res);
  function finish(){const pct=Math.round(st.cor/data.length*100);let badge='try',word='Weiter üben!';
    if(pct===100){badge='gold';word='Perfekt! 🏆';}else if(pct>=70){badge='ok';word='Bestanden! ✅';}
    res.innerHTML='<div class="score">'+st.cor+' / '+data.length+'</div><div>richtig beantwortet '+
      '<span class="badge '+badge+'">'+word+'</span></div>';
    res.classList.add('show');res.scrollIntoView({behavior:'smooth',block:'center'});
    try{localStorage.setItem(key,JSON.stringify({c:st.cor,t:data.length,ts:Date.now()}));}catch(e){}}
}

//============================ Persistence (checklists, notes) ============================
function initPersist(){
  document.querySelectorAll('input[type=checkbox][data-persist]').forEach(cb=>{
    const k='ttchk_'+cb.dataset.persist;
    if(localStorage.getItem(k)==='1'){cb.checked=true;const li=cb.closest('li');if(li)li.classList.add('done');}
    cb.addEventListener('change',()=>{localStorage.setItem(k,cb.checked?'1':'0');
      const li=cb.closest('li');if(li)li.classList.toggle('done',cb.checked);});});
  document.querySelectorAll('textarea[data-persist]').forEach(ta=>{
    const k='ttnotes_'+ta.dataset.persist,v=localStorage.getItem(k);if(v!=null)ta.value=v;
    ta.addEventListener('input',()=>localStorage.setItem(k,ta.value));});
}

//============================ Index hub ============================
function initHub(){
  const cards=document.querySelectorAll('.card[data-quizkey]');let done=0,total=0;
  cards.forEach(c=>{total++;const st=c.querySelector('.kstatus');let r=null;
    try{r=JSON.parse(localStorage.getItem(c.dataset.quizkey));}catch(e){}
    if(r&&r.t){const pct=Math.round(r.c/r.t*100);
      if(pct>=70){done++;st.className='kstatus done';st.textContent='✓ Quiz: '+r.c+'/'+r.t;}
      else{st.className='kstatus part';st.textContent='◐ Quiz: '+r.c+'/'+r.t+' – nochmal?';}}
    else{st.className='kstatus todo';st.textContent='○ noch offen';}});
  const bar=q('hubbar');if(bar){const pct=total?Math.round(done/total*100):0;
    bar.querySelector('span').style.width=pct+'%';
    bar.querySelector('em').textContent=done+' von '+total+' Kapiteln geschafft ('+pct+'%)';}
}
function resetProgress(){if(!confirm('Wirklich den gesamten Lernfortschritt (Quiz-Ergebnisse & Häkchen) löschen?'))return;
  Object.keys(localStorage).filter(k=>k.startsWith('tt_quiz_')||k.startsWith('ttchk_')||k.startsWith('ttnotes_'))
    .forEach(k=>localStorage.removeItem(k));location.reload();}

//============================ WIDGETS ============================
// 1) Frequenz-Explorer ------------------------------------------------
function freqExplorer(id){const host=q(id);if(!host)return;
  const bands=[[40,'Sub-Bass · 40 Hz'],[80,'Bass · 80 Hz'],[160,'Tiefe Mitten · 160 Hz'],
    [400,'Untere Mitten · 400 Hz'],[1000,'Mitten · 1 kHz'],[3000,'Präsenz · 3 kHz'],
    [6500,'Höhen · 6,5 kHz'],[12000,'Brillanz · 12 kHz']];
  const chips=document.createElement('div');chips.className='chips';
  bands.forEach(([f,l])=>{const c=document.createElement('button');c.className='chip';c.textContent=l;
    c.onclick=()=>{flash(c);Snd.beep(f,0.9,'sine');};chips.appendChild(c);});
  host.appendChild(chips);
  let tone=null;const tb=btn('▶ Dauerton','');
  const sl=sliderField({label:'Frequenz',min:Math.log10(20),max:Math.log10(20000),step:0.001,val:Math.log10(440),
    fmt:v=>{const f=Math.round(Math.pow(10,v));return f>=1000?(f/1000).toFixed(1)+' kHz':f+' Hz';},
    on:v=>{if(tone)tone.setFreq(Math.pow(10,v));}});
  toggleBtn(tb,'⏹ Stop','▶ Dauerton (Slider bewegen)',
    ()=>{tone=Snd.osc(Math.pow(10,+sl._input.value),'sine');},()=>{if(tone){tone.stop();tone=null;}});
  const row=document.createElement('div');row.className='row';row.appendChild(tb);row.style.marginTop='8px';
  host.appendChild(sl);host.appendChild(row);
}

// 2) Pan-Demo ----------------------------------------------------------
function panDemo(id){const host=q(id);if(!host)return;
  let osc=null,pan=null,lr=null;
  const meter=document.createElement('div');meter.className='row';
  meter.innerHTML='<div class="lr" style="flex:1"><b>L</b><div class="meter" style="flex:1"><span id="'+id+'-l"></span></div></div>'+
                  '<div class="lr" style="flex:1"><b>R</b><div class="meter" style="flex:1"><span id="'+id+'-r"></span></div></div>';
  const sl=sliderField({label:'Panorama',min:-1,max:1,step:0.01,val:0,
    fmt:v=>Math.abs(v)<0.05?'Mitte':(v<0?'L '+Math.round(-v*100)+'%':'R '+Math.round(v*100)+'%'),
    on:v=>{if(pan)pan.pan.setTargetAtTime(v,Snd.ctx.currentTime,0.02);upd(v);}});
  function upd(v){const l=Math.round(Math.cos((v+1)/2*Math.PI/2)*100),r=Math.round(Math.sin((v+1)/2*Math.PI/2)*100);
    const L=q(id+'-l'),R=q(id+'-r');if(L)L.style.width=l+'%';if(R)R.style.width=r+'%';}
  const b=btn('▶ Ton abspielen','');
  toggleBtn(b,'⏹ Stop','▶ Ton abspielen',()=>{Snd.init();osc=Snd.ctx.createOscillator();
    pan=Snd.ctx.createStereoPanner();const g=Snd.ctx.createGain();g.gain.value=0.5;
    osc.type='triangle';osc.frequency.value=330;osc.connect(g);g.connect(pan);pan.connect(Snd.master);osc.start();
    pan.pan.value=+sl._input.value;upd(+sl._input.value);
    const n={node:g,stop:()=>{try{g.gain.setTargetAtTime(0,Snd.ctx.currentTime,0.05);osc.stop(Snd.ctx.currentTime+0.12);}catch(e){}}};Snd.reg(n);},
    ()=>{Snd.stopAll();});
  host.appendChild(meter);host.appendChild(sl);const r=document.createElement('div');r.className='row';r.appendChild(b);host.appendChild(r);
  upd(0);
}

// 3) dB-Demo -----------------------------------------------------------
function dbDemo(id){const host=q(id);if(!host)return;
  const p=document.createElement('p');p.className='audiohint';p.textContent='Höre, wie sich dB-Stufen anfühlen – jeweils derselbe Ton, nur leiser.';host.appendChild(p);
  const chips=document.createElement('div');chips.className='chips';
  [[0,'0 dB (Referenz)'],[-3,'–3 dB (kaum leiser)'],[-6,'–6 dB (etwas leiser)'],[-10,'–10 dB (≈ halb so laut)'],[-20,'–20 dB (viel leiser)']]
    .forEach(([db,l])=>{const c=document.createElement('button');c.className='chip';c.textContent=l;
      c.onclick=()=>{flash(c);const n=Snd.osc(440,'sine');n.setGain(0.9*Math.pow(10,db/20));setTimeout(()=>n.stop(),800);};
      chips.appendChild(c);});
  host.appendChild(chips);
}

// 4) Signalfluss klickbar ---------------------------------------------
function signalFlow(id){const host=q(id);if(!host)return;
  const steps=[['Schallquelle','Stimme oder Instrument erzeugt Schallwellen (Luftdruck-Schwankungen).'],
    ['Mikrofon','Wandelt Schall in eine schwache elektrische Wechselspannung (Mic-Level).'],
    ['Kabel (XLR)','Transportiert das schwache Signal – symmetrisch, damit kein Brummen einstreut.'],
    ['Mischpult','Gain hebt das Signal auf Line-Level, dann EQ, Aux, Pan, Fader → Master.'],
    ['Endstufe','Verstärkt das Line-Signal auf Lautsprecher-Level (viel Leistung).'],
    ['Lautsprecher','Wandelt Strom zurück in Schall.'],
    ['Publikum','Hört das Ergebnis deiner Arbeit.']];
  const flow=document.createElement('div');flow.className='chips';
  const out=document.createElement('div');out.className='feedbackline show ok';out.style.display='block';
  out.textContent='Tippe auf eine Station, um zu sehen, was dort passiert.';
  steps.forEach(([n,d],i)=>{const c=document.createElement('button');c.className='chip';c.textContent=(i+1)+'. '+n;
    c.onclick=()=>{flow.querySelectorAll('.chip').forEach(x=>x.classList.remove('active'));c.classList.add('active');
      out.className='feedbackline show ok';out.innerHTML='<b>'+n+':</b> '+d;};flow.appendChild(c);});
  host.appendChild(flow);host.appendChild(out);
}

// 5) Polar / Richtcharakteristik --------------------------------------
function polarDemo(id){const host=q(id);if(!host)return;
  const pats={'Kugel (Omni)':a=>1,'Niere (Cardioid)':a=>0.5+0.5*Math.cos(a),
    'Superniere':a=>0.37+0.63*Math.cos(a),'Acht (Bidirektional)':a=>Math.abs(Math.cos(a))};
  const sel=document.createElement('select');Object.keys(pats).forEach(k=>{const o=document.createElement('option');o.textContent=k;sel.appendChild(o);});
  const cv=document.createElement('canvas');cv.width=300;cv.height=300;cv.style.margin='10px auto';
  const ctx=cv.getContext('2d');let angle=0,tone=null;
  const sl=sliderField({label:'Winkel der Schallquelle',min:0,max:360,step:1,val:0,unit:'°',on:v=>{angle=v*Math.PI/180;draw();updTone();}});
  const read=document.createElement('div');read.className='readout';
  function gain(){return pats[sel.value](angle);}
  function updTone(){if(tone)tone.setGain(0.9*Math.max(0.02,gain()));read.textContent='Empfindlichkeit: '+Math.round(gain()*100)+'%  ('+(gain()>0.001?(20*Math.log10(gain())).toFixed(1):'-∞')+' dB)';}
  function draw(){const f=pats[sel.value],cx=150,cy=150,R=120;ctx.clearRect(0,0,300,300);
    ctx.strokeStyle='#2d3744';for(let r=0.25;r<=1;r+=0.25){ctx.beginPath();ctx.arc(cx,cy,R*r,0,7);ctx.stroke();}
    ctx.beginPath();ctx.strokeStyle='#27c2a0';ctx.lineWidth=2;
    for(let a=0;a<=360;a++){const rad=(a-90)*Math.PI/180;const g=Math.max(0,f(a*Math.PI/180));const r=R*g;
      const x=cx+Math.sin(a*Math.PI/180)*r,y=cy-Math.cos(a*Math.PI/180)*r;a?ctx.lineTo(x,y):ctx.moveTo(x,y);}ctx.closePath();ctx.stroke();
    // source dot
    const sx=cx+Math.sin(angle)*R,sy=cy-Math.cos(angle)*R;
    ctx.fillStyle='#ff7a1a';ctx.beginPath();ctx.arc(sx,sy,7,0,7);ctx.fill();
    ctx.fillStyle='#9aa7b4';ctx.font='12px sans-serif';ctx.textAlign='center';ctx.fillText('vorne',cx,18);ctx.fillText('hinten',cx,295);}
  sel.onchange=()=>{draw();updTone();};
  const b=btn('▶ Hörbar machen','');
  toggleBtn(b,'⏹ Stop','▶ Hörbar machen',()=>{tone=Snd.osc(330,'sawtooth');updTone();},()=>{if(tone){tone.stop();tone=null;}});
  const r1=document.createElement('div');r1.className='row';r1.appendChild(sel);r1.appendChild(b);
  host.appendChild(r1);host.appendChild(cv);host.appendChild(sl);host.appendChild(read);
  draw();
}

// 6) Virtueller Kanalzug ----------------------------------------------
function channelStrip(id){const host=q(id);if(!host)return;
  let chain=null;
  const state={gain:0,hpf:false,low:0,mid:0,high:0,pan:0,fader:0};
  function build(){Snd.init();const c=Snd.ctx;const src=Snd.ctx.createBufferSource();src.buffer=Snd.noiseBuf();src.loop=true;
    const pre=c.createGain();const shaper=c.createWaveShaper();shaper.curve=clipCurve();
    const hpf=c.createBiquadFilter();hpf.type='highpass';hpf.frequency.value=20;
    const low=c.createBiquadFilter();low.type='lowshelf';low.frequency.value=120;
    const mid=c.createBiquadFilter();mid.type='peaking';mid.frequency.value=1500;mid.Q.value=1;
    const high=c.createBiquadFilter();high.type='highshelf';high.frequency.value=8000;
    const pan=c.createStereoPanner();const fader=c.createGain();const an=c.createAnalyser();an.fftSize=512;
    src.connect(pre);pre.connect(shaper);shaper.connect(hpf);hpf.connect(low);low.connect(mid);mid.connect(high);
    high.connect(pan);pan.connect(fader);fader.connect(an);an.connect(Snd.master);src.start();
    chain={src,pre,hpf,low,mid,high,pan,fader,an,buf:new Uint8Array(an.frequencyBinCount),
      stop:()=>{try{fader.gain.setTargetAtTime(0,c.currentTime,0.05);src.stop(c.currentTime+0.15);}catch(e){}}};
    Snd.reg(chain);apply();meterLoop();}
  function clipCurve(){const n=1024,c=new Float32Array(n);for(let i=0;i<n;i++){const x=i/n*2-1;c[i]=Math.tanh(x*1.2);}return c;}
  function apply(){if(!chain)return;const c=Snd.ctx,t=c.currentTime;
    chain.pre.gain.setTargetAtTime(Math.pow(10,state.gain/20),t,0.02);
    chain.hpf.frequency.setTargetAtTime(state.hpf?120:20,t,0.02);
    chain.low.gain.setTargetAtTime(state.low,t,0.02);chain.mid.gain.setTargetAtTime(state.mid,t,0.02);
    chain.high.gain.setTargetAtTime(state.high,t,0.02);chain.pan.pan.setTargetAtTime(state.pan,t,0.02);
    chain.fader.gain.setTargetAtTime(0.5*Math.pow(10,state.fader/20),t,0.02);}
  const clip=document.createElement('div');clip.className='readout';clip.style.marginLeft='auto';clip.textContent='Pegel: –';
  function meterLoop(){if(!chain)return;chain.an.getByteTimeDomainData(chain.buf);let peak=0;
    for(let i=0;i<chain.buf.length;i++){const v=Math.abs(chain.buf[i]-128)/128;if(v>peak)peak=v;}
    const m=q(id+'-m');if(m)m.style.width=Math.min(100,peak*120)+'%';
    clip.textContent=peak>0.98?'⚠ CLIPPING':(peak>0.8?'Pegel: hoch':'Pegel: ok');
    clip.style.color=peak>0.98?'var(--red)':(peak>0.8?'var(--yellow)':'var(--green)');
    requestAnimationFrame(meterLoop);}
  const grid=document.createElement('div');grid.className='row';grid.style.alignItems='stretch';
  grid.appendChild(sliderField({label:'Gain',min:-6,max:24,step:1,val:0,unit:' dB',on:v=>{state.gain=v;apply();}}));
  const hpfBtn=btn('HPF: aus','');hpfBtn.onclick=()=>{state.hpf=!state.hpf;hpfBtn.textContent='HPF: '+(state.hpf?'an (120 Hz)':'aus');hpfBtn.classList.toggle('primary',state.hpf);apply();};
  const hpfWrap=document.createElement('label');hpfWrap.className='fld';hpfWrap.appendChild(Object.assign(document.createElement('span'),{textContent:'Low-Cut'}));hpfWrap.appendChild(hpfBtn);
  grid.appendChild(hpfWrap);
  grid.appendChild(sliderField({label:'EQ Bass',min:-12,max:12,step:1,val:0,unit:' dB',on:v=>{state.low=v;apply();}}));
  grid.appendChild(sliderField({label:'EQ Mitten',min:-12,max:12,step:1,val:0,unit:' dB',on:v=>{state.mid=v;apply();}}));
  grid.appendChild(sliderField({label:'EQ Höhen',min:-12,max:12,step:1,val:0,unit:' dB',on:v=>{state.high=v;apply();}}));
  grid.appendChild(sliderField({label:'Pan',min:-1,max:1,step:0.05,val:0,fmt:v=>Math.abs(v)<0.05?'Mitte':(v<0?'L':'R'),on:v=>{state.pan=v;apply();}}));
  grid.appendChild(sliderField({label:'Fader',min:-30,max:6,step:1,val:0,unit:' dB',on:v=>{state.fader=v;apply();}}));
  const meter=document.createElement('div');meter.className='row';
  meter.innerHTML='<span style="font-size:.8rem;color:var(--muted)">Kanal-Pegel</span><div class="meter" style="flex:1"><span id="'+id+'-m"></span></div>';
  meter.appendChild(clip);
  const b=btn('▶ Test-Signal (Rauschen)','');
  toggleBtn(b,'⏹ Stop','▶ Test-Signal (Rauschen)',build,()=>{if(chain){chain.stop();chain=null;}});
  const r=document.createElement('div');r.className='row';r.appendChild(b);
  const hint=document.createElement('p');hint.className='audiohint';hint.textContent='Dreh Gain hoch bis „CLIPPING" erscheint – genau das willst du im echten Kanal vermeiden.';
  host.appendChild(r);host.appendChild(hint);host.appendChild(meter);host.appendChild(grid);
}

// 7) Clipping A/B ------------------------------------------------------
function clipDemo(id){const host=q(id);if(!host)return;const chips=document.createElement('div');chips.className='chips';
  const mk=(label,drive)=>{const c=document.createElement('button');c.className='chip';c.textContent=label;
    c.onclick=()=>{flash(c);Snd.init();const o=Snd.ctx.createOscillator();o.type='sine';o.frequency.value=220;
      const g=Snd.ctx.createGain();g.gain.value=drive;const sh=Snd.ctx.createWaveShaper();
      const n=1024,cv=new Float32Array(n);for(let i=0;i<n;i++){const x=i/n*2-1;cv[i]=Math.max(-1,Math.min(1,x));}sh.curve=cv;
      const out=Snd.ctx.createGain();out.gain.value=0.5;o.connect(g);g.connect(sh);sh.connect(out);out.connect(Snd.master);o.start();
      const node={node:out,stop:()=>{try{out.gain.setTargetAtTime(0,Snd.ctx.currentTime,0.05);o.stop(Snd.ctx.currentTime+0.12);}catch(e){}}};Snd.reg(node);
      setTimeout(()=>node.stop(),900);};return c;};
  chips.appendChild(mk('✅ Sauberer Pegel',0.8));chips.appendChild(mk('⚠️ Übersteuert (Clipping)',4));host.appendChild(chips);
}

// 8) Feedback-Demo (simuliert) ----------------------------------------
function feedbackDemo(id){const host=q(id);if(!host)return;let osc=null,base=600;
  const p=document.createElement('p');p.className='audiohint';p.textContent='Simulation: Dreh den Monitor-Pegel hoch – ab einer Schwelle „kippt" das System ins Pfeifen. Stop-Button bricht sofort ab.';
  const sl=sliderField({label:'Monitor-Pegel',min:0,max:100,step:1,val:0,unit:' %',on:v=>{if(!osc)return;
    const g=v<60?v/100*0.2:0.12+(v-60)/40*0.8;osc.setGain(Math.min(0.9,g));
    osc.setFreq(base*(1+(v>70?(v-70)/30*0.04*Math.sin(Date.now()/40):0)));
    out.textContent=v>72?'🔴 FEEDBACK! Sofort Gain runter oder Kanal muten!':(v>60?'🟡 Es klingelt – kurz vor Feedback (jetzt EQ-Cut setzen).':'🟢 stabil');}});
  const out=document.createElement('div');out.className='readout';out.textContent='—';
  const b=btn('▶ Monitor an','');
  toggleBtn(b,'⏹ Not-Stop','▶ Monitor an',()=>{osc=Snd.osc(base,'sine');osc.setGain(0.001);},()=>{if(osc){osc.stop();osc=null;}sl._input.value=0;sl._read.textContent='0 %';out.textContent='—';});
  const r=document.createElement('div');r.className='row';r.appendChild(b);
  host.appendChild(p);host.appendChild(r);host.appendChild(sl);host.appendChild(out);
}

// 9) Tops/Sub Split ----------------------------------------------------
function splitDemo(id){const host=q(id);if(!host)return;const chips=document.createElement('div');chips.className='chips';
  const play=(label,type,freq)=>{const c=document.createElement('button');c.className='chip';c.textContent=label;
    c.onclick=()=>{flash(c);Snd.init();const s=Snd.ctx.createBufferSource();s.buffer=Snd.noiseBuf();s.loop=true;
      const f=Snd.ctx.createBiquadFilter();const g=Snd.ctx.createGain();g.gain.value=0.5;
      if(type==='full'){f.type='allpass';}else{f.type=type;f.frequency.value=freq;f.Q.value=0.7;}
      s.connect(f);f.connect(g);g.connect(Snd.master);s.start();
      const n={node:g,stop:()=>{try{g.gain.setTargetAtTime(0,Snd.ctx.currentTime,0.05);s.stop(Snd.ctx.currentTime+0.15);}catch(e){}}};Snd.reg(n);setTimeout(()=>n.stop(),1300);};return c;};
  chips.appendChild(play('🔊 Fullrange (alles)','full'));chips.appendChild(play('🔈 Nur Tops (>100 Hz)','highpass',100));
  chips.appendChild(play('🔉 Nur Sub (<90 Hz)','lowpass',90));host.appendChild(chips);
}

// 10) Ear-Trainer ------------------------------------------------------
function earTrainer(id){const host=q(id);if(!host)return;
  const bands=[100,250,500,1000,2500,5000,10000];const labels={100:'100 Hz',250:'250 Hz',500:'500 Hz',1000:'1 kHz',2500:'2,5 kHz',5000:'5 kHz',10000:'10 kHz'};
  let target=null,src=null,filt=null,score=0,rounds=0;
  const info=document.createElement('p');info.className='audiohint';info.textContent='Ein Frequenzband im Rauschen ist angehoben (+10 dB). Welches? Erst abspielen, dann tippen.';
  const playBtn=btn('▶ Sound abspielen','primary');
  function play(){Snd.stopAll();target=bands[Math.floor(Math.random()*bands.length)];Snd.init();
    src=Snd.ctx.createBufferSource();src.buffer=Snd.noiseBuf();src.loop=true;
    filt=Snd.ctx.createBiquadFilter();filt.type='peaking';filt.frequency.value=target;filt.Q.value=2.5;filt.gain.value=11;
    const g=Snd.ctx.createGain();g.gain.value=0.45;src.connect(filt);filt.connect(g);g.connect(Snd.master);src.start();
    const n={node:g,stop:()=>{try{g.gain.setTargetAtTime(0,Snd.ctx.currentTime,0.05);src.stop(Snd.ctx.currentTime+0.15);}catch(e){}}};Snd.reg(n);
    chips.querySelectorAll('.chip').forEach(c=>{c.className='chip';c.disabled=false;});out.className='feedbackline';}
  playBtn.onclick=play;
  const chips=document.createElement('div');chips.className='chips';
  bands.forEach(f=>{const c=document.createElement('button');c.className='chip';c.textContent=labels[f];
    c.onclick=()=>{if(target==null)return;chips.querySelectorAll('.chip').forEach(x=>x.disabled=true);
      rounds++;const ok=f===target;if(ok){score++;c.classList.add('correct');}else{c.classList.add('wrong');
        chips.querySelectorAll('.chip').forEach(x=>{if(x.textContent===labels[target])x.classList.add('correct');});}
      out.className='feedbackline show '+(ok?'ok':'no');
      out.textContent=(ok?'✅ Richtig! ':'❌ Es war '+labels[target]+'. ')+'Score: '+score+' / '+rounds;
      target=null;};chips.appendChild(c);});
  const out=document.createElement('div');out.className='feedbackline';
  const r=document.createElement('div');r.className='row';r.appendChild(playBtn);
  host.appendChild(info);host.appendChild(r);host.appendChild(chips);host.appendChild(out);
}

// 11) Reverb-Demo ------------------------------------------------------
function reverbDemo(id){const host=q(id);if(!host)return;let loop=null,wetG=null;
  const sl=sliderField({label:'Hall-Anteil (Dry/Wet)',min:0,max:100,step:1,val:25,unit:' %',on:v=>{if(wetG)wetG.gain.setTargetAtTime(v/100*1.5,Snd.ctx.currentTime,0.05);}});
  const b=btn('▶ Gesangs-Simulation','');
  function start(){Snd.init();const c=Snd.ctx;const conv=c.createConvolver();conv.buffer=Snd.impulse(2.2,3);
    wetG=c.createGain();wetG.gain.value=+sl._input.value/100*1.5;const dry=c.createGain();dry.gain.value=0.8;
    const out=c.createGain();out.gain.value=0.6;conv.connect(wetG);wetG.connect(out);dry.connect(out);out.connect(Snd.master);
    let i=0;const seq=[392,440,494,440];
    function note(){if(!loop)return;const o=c.createOscillator();const g=c.createGain();o.type='triangle';
      o.frequency.value=seq[i%seq.length];i++;g.gain.value=0;o.connect(g);g.connect(dry);g.connect(conv);o.start();
      g.gain.setTargetAtTime(0.5,c.currentTime,0.02);g.gain.setTargetAtTime(0,c.currentTime+0.35,0.1);o.stop(c.currentTime+0.7);}
    loop={node:out,timer:setInterval(note,700),stop:()=>{clearInterval(loop.timer);try{out.gain.setTargetAtTime(0,c.currentTime,0.1);}catch(e){}}};Snd.reg(loop);note();}
  toggleBtn(b,'⏹ Stop','▶ Gesangs-Simulation',start,()=>{if(loop){loop.stop();loop=null;}});
  const r=document.createElement('div');r.className='row';r.appendChild(b);
  const p=document.createElement('p');p.className='audiohint';p.textContent='Schiebe von 0 % (trocken) bis 100 % (Kirche). Faustregel live: lieber zu wenig als zu viel.';
  host.appendChild(p);host.appendChild(r);host.appendChild(sl);
}

// 12) Kompressor-Visualizer -------------------------------------------
function compViz(id){const host=q(id);if(!host)return;
  const st={th:-24,ratio:4,attack:10,release:120};let comp=null,pulse=null;
  const cv=document.createElement('canvas');cv.width=300;cv.height=220;const ctx=cv.getContext('2d');
  function draw(){ctx.clearRect(0,0,300,220);ctx.strokeStyle='#2d3744';
    for(let i=0;i<=4;i++){const x=20+i/4*260;ctx.beginPath();ctx.moveTo(x,10);ctx.lineTo(x,190);ctx.stroke();
      const y=190-i/4*180;ctx.beginPath();ctx.moveTo(20,y);ctx.lineTo(280,y);ctx.stroke();}
    // 1:1 reference
    ctx.strokeStyle='#3a4654';ctx.setLineDash([4,4]);ctx.beginPath();ctx.moveTo(20,190);ctx.lineTo(280,10);ctx.stroke();ctx.setLineDash([]);
    // transfer curve (dB -60..0)
    ctx.strokeStyle='#ff7a1a';ctx.lineWidth=2.5;ctx.beginPath();
    for(let dbi=-60;dbi<=0;dbi++){const out=dbi<st.th?dbi:st.th+(dbi-st.th)/st.ratio;
      const x=20+(dbi+60)/60*260,y=190-(out+60)/60*180;dbi===-60?ctx.moveTo(x,y):ctx.lineTo(x,y);}ctx.stroke();
    ctx.fillStyle='#9aa7b4';ctx.font='11px sans-serif';ctx.fillText('Eingang →',120,210);
    ctx.save();ctx.translate(12,120);ctx.rotate(-Math.PI/2);ctx.fillText('Ausgang →',0,0);ctx.restore();
    // threshold marker
    const tx=20+(st.th+60)/60*260;ctx.strokeStyle='#27c2a0';ctx.beginPath();ctx.moveTo(tx,10);ctx.lineTo(tx,190);ctx.stroke();
    ctx.fillStyle='#27c2a0';ctx.fillText('Threshold',tx-24,22);}
  function apply(){if(!comp)return;const t=Snd.ctx.currentTime;comp.threshold.setTargetAtTime(st.th,t,0.01);
    comp.ratio.setTargetAtTime(st.ratio,t,0.01);comp.attack.setTargetAtTime(st.attack/1000,t,0.01);comp.release.setTargetAtTime(st.release/1000,t,0.01);}
  const gr=document.createElement('div');gr.className='readout';gr.textContent='Gain Reduction: 0 dB';
  function start(){Snd.init();const c=Snd.ctx;comp=c.createDynamicsCompressor();comp.knee.value=6;apply();
    const out=c.createGain();out.gain.value=0.8;comp.connect(out);out.connect(Snd.master);
    function hit(){if(!pulse)return;const o=c.createOscillator();const g=c.createGain();o.type='sine';o.frequency.value=140;
      g.gain.value=0;o.connect(g);g.connect(comp);o.start();g.gain.setTargetAtTime(0.9,c.currentTime,0.005);
      g.gain.setTargetAtTime(0,c.currentTime+0.18,0.06);o.stop(c.currentTime+0.5);}
    pulse={node:out,timer:setInterval(hit,500),stop:()=>{clearInterval(pulse.timer);try{out.gain.setTargetAtTime(0,c.currentTime,0.1);}catch(e){}}};Snd.reg(pulse);hit();
    (function loop(){if(!comp)return;gr.textContent='Gain Reduction: '+comp.reduction.toFixed(1)+' dB';requestAnimationFrame(loop);})();}
  const b=btn('▶ Beat durch Kompressor','');
  toggleBtn(b,'⏹ Stop','▶ Beat durch Kompressor',start,()=>{if(pulse){pulse.stop();pulse=null;}comp=null;gr.textContent='Gain Reduction: 0 dB';});
  const grid=document.createElement('div');grid.className='row';
  grid.appendChild(sliderField({label:'Threshold',min:-50,max:0,step:1,val:st.th,unit:' dB',on:v=>{st.th=v;apply();draw();}}));
  grid.appendChild(sliderField({label:'Ratio',min:1,max:20,step:1,val:st.ratio,fmt:v=>v+':1',on:v=>{st.ratio=v;apply();draw();}}));
  grid.appendChild(sliderField({label:'Attack',min:1,max:100,step:1,val:st.attack,unit:' ms',on:v=>{st.attack=v;apply();}}));
  grid.appendChild(sliderField({label:'Release',min:20,max:400,step:10,val:st.release,unit:' ms',on:v=>{st.release=v;apply();}}));
  const r=document.createElement('div');r.className='row';r.appendChild(b);r.appendChild(gr);
  host.appendChild(cv);host.appendChild(r);host.appendChild(grid);draw();
}

// 13) Delay-/Laufzeit-Rechner -----------------------------------------
function delayCalc(id){const host=q(id);if(!host)return;
  const wrap=document.createElement('div');wrap.className='widget';wrap.style.margin='0';
  wrap.innerHTML='<h3>📏 Laufzeit-Rechner (Delay-Speaker)</h3>';
  const r1=document.createElement('div');r1.className='row';
  const dist=document.createElement('input');dist.type='number';dist.value=20;dist.min=0;dist.step=1;dist.style.width='90px';
  const o1=document.createElement('div');o1.className='readout';
  function calc(){const d=+dist.value||0;o1.textContent=d+' m  →  '+Math.round(d*1000/343)+' ms Delay  (Schall: 343 m/s)';}
  dist.oninput=calc;r1.appendChild(Object.assign(document.createElement('span'),{textContent:'Abstand:'}));r1.appendChild(dist);
  r1.appendChild(Object.assign(document.createElement('span'),{textContent:'m'}));r1.appendChild(o1);
  const h2=document.createElement('h3');h2.textContent='🎵 Delay-Effekt im Takt';h2.style.marginTop='14px';
  const r2=document.createElement('div');r2.className='row';const bpm=document.createElement('input');bpm.type='number';bpm.value=120;bpm.min=40;bpm.style.width='90px';
  const o2=document.createElement('div');o2.className='readout';
  function calc2(){const b=+bpm.value||120;const q=60000/b;o2.innerHTML='1/4: '+Math.round(q)+' ms · 1/8: '+Math.round(q/2)+' ms · 1/8 punktiert: '+Math.round(q*0.75)+' ms';}
  bpm.oninput=calc2;r2.appendChild(Object.assign(document.createElement('span'),{textContent:'Tempo:'}));r2.appendChild(bpm);
  r2.appendChild(Object.assign(document.createElement('span'),{textContent:'BPM'}));r2.appendChild(o2);
  wrap.appendChild(r1);wrap.appendChild(h2);wrap.appendChild(r2);host.appendChild(wrap);calc();calc2();
}

// 14) Zuordnungsspiel (Kabel) -----------------------------------------
function matchGame(id,pairs,leftTitle,rightTitle){const host=q(id);if(!host)return;let sel=null,solved=0;
  const grid=document.createElement('div');grid.className='row';grid.style.alignItems='flex-start';
  const colA=document.createElement('div');colA.style.flex='1';colA.innerHTML='<h4>'+leftTitle+'</h4>';
  const colB=document.createElement('div');colB.style.flex='1';colB.innerHTML='<h4>'+rightTitle+'</h4>';
  const rights=pairs.map((p,i)=>({t:p[1],i})).sort(()=>Math.random()-0.5);
  const out=document.createElement('div');out.className='feedbackline show ok';out.textContent='Tippe links einen Begriff an, dann rechts die passende Antwort.';
  pairs.forEach((p,i)=>{const c=document.createElement('button');c.className='chip';c.style.display='block';c.style.margin='6px 0';c.style.width='100%';
    c.textContent=p[0];c.dataset.i=i;c.onclick=()=>{if(c.classList.contains('correct'))return;
      colA.querySelectorAll('.chip').forEach(x=>x.classList.remove('active'));c.classList.add('active');sel=i;};colA.appendChild(c);});
  rights.forEach(r=>{const c=document.createElement('button');c.className='chip';c.style.display='block';c.style.margin='6px 0';c.style.width='100%';
    c.textContent=r.t;c.dataset.i=r.i;c.onclick=()=>{if(sel==null||c.classList.contains('correct'))return;
      if(+c.dataset.i===sel){c.classList.add('correct');colA.querySelector('.chip.active').classList.add('correct');
        colA.querySelector('.chip.active').classList.remove('active');solved++;
        out.className='feedbackline show ok';out.textContent='✅ Richtig! ('+solved+' / '+pairs.length+')'+(solved===pairs.length?' – alles gelöst! 🎉':'');}
      else{c.classList.add('wrong');out.className='feedbackline show no';out.textContent='❌ Passt nicht – versuch es nochmal.';setTimeout(()=>c.classList.remove('wrong'),500);}
      sel=null;colA.querySelectorAll('.chip').forEach(x=>x.classList.remove('active'));};colB.appendChild(c);});
  grid.appendChild(colA);grid.appendChild(colB);host.appendChild(grid);host.appendChild(out);
}

// 15) Reihenfolge-Spiel (Soundcheck) ----------------------------------
function orderGame(id,correctSteps){const host=q(id);if(!host)return;let next=0;
  const shuffled=correctSteps.map((s,i)=>({s,i})).sort(()=>Math.random()-0.5);
  const out=document.createElement('div');out.className='feedbackline show ok';out.textContent='Tippe die Schritte in der richtigen Reihenfolge an (von zuerst nach zuletzt).';
  const chips=document.createElement('div');chips.className='chips';chips.style.flexDirection='column';
  shuffled.forEach(o=>{const c=document.createElement('button');c.className='chip';c.style.textAlign='left';c.textContent=o.s;c.dataset.i=o.i;
    c.onclick=()=>{if(c.disabled)return;if(+c.dataset.i===next){c.classList.add('correct');c.disabled=true;c.textContent=(next+1)+'. '+o.s;next++;
        out.className='feedbackline show ok';out.textContent=next===correctSteps.length?'✅ Perfekte Reihenfolge! 🎉':'✅ Richtig – weiter geht\'s.';}
      else{c.classList.add('wrong');out.className='feedbackline show no';out.textContent='❌ Noch nicht – welcher Schritt kommt jetzt dran?';setTimeout(()=>c.classList.remove('wrong'),500);}};
    chips.appendChild(c);});
  host.appendChild(chips);host.appendChild(out);
}

// 16) Layer-Umschalter (Digitalpult) ----------------------------------
function layerDemo(id){const host=q(id);if(!host)return;
  const layers=[['Kick','Snare','HiHat','Tom1','Tom2','OH-L','OH-R','Bass'],
    ['Git 1','Git 2','Keys-L','Keys-R','Lead-Voc','BV 1','BV 2','Talk'],
    ['Aux 1','Aux 2','Aux 3','Aux 4','FX 1','FX 2','DCA Drums','DCA Voc']];
  let cur=0;const names=['Layer 1 · Inputs 1–8','Layer 2 · Inputs 9–16','Layer 3 · Aux / DCA'];
  const head=document.createElement('div');head.className='readout';
  const faders=document.createElement('div');faders.className='row';faders.style.alignItems='flex-end';faders.style.minHeight='90px';
  function render(){head.textContent='▸ '+names[cur];faders.innerHTML='';
    layers[cur].forEach(n=>{const f=document.createElement('div');f.style.textAlign='center';f.style.flex='1';f.style.minWidth='54px';
      f.innerHTML='<div style="height:60px;width:8px;margin:0 auto;background:linear-gradient(#37d67a,#1c232d);border-radius:4px"></div>'+
        '<div style="font-size:.7rem;color:var(--muted);margin-top:4px">'+n+'</div>';faders.appendChild(f);});}
  const b=btn('🔀 Layer wechseln','primary');b.onclick=()=>{cur=(cur+1)%layers.length;render();};
  const p=document.createElement('p');p.className='audiohint';p.textContent='Dieselben 8 physischen Fader steuern je nach Layer andere Kanäle – so passen 24+ Kanäle auf wenige Fader.';
  const r=document.createElement('div');r.className='row';r.appendChild(b);r.appendChild(head);
  host.appendChild(p);host.appendChild(r);host.appendChild(faders);render();
}

// 17) Musiker-Übersetzer ----------------------------------------------
function translator(id){const host=q(id);if(!host)return;
  const pairs=[['„Mehr Ich"','Eigenes Instrument im Monitor lauter machen.'],
    ['„Mehr Druck"','Mehr Bässe / mehr Lautstärke.'],['„Schärfer"','Mehr Höhen/Präsenz (2–5 kHz).'],
    ['„Wärmer"','Mehr Bässe, weniger Höhen.'],['„Ich höre mich nicht"','Erst Gain prüfen, dann Aux-Lautstärke.'],
    ['„Zu viel Hall"','Reverb-Anteil im Monitor reduzieren.']];
  const out=document.createElement('div');out.className='feedbackline show ok';out.textContent='Was meinen Musiker damit? Tippe eine Aussage an.';
  const chips=document.createElement('div');chips.className='chips';
  pairs.forEach(([k,v])=>{const c=document.createElement('button');c.className='chip';c.textContent=k;
    c.onclick=()=>{chips.querySelectorAll('.chip').forEach(x=>x.classList.remove('active'));c.classList.add('active');
      out.className='feedbackline show ok';out.innerHTML='<b>'+k+'</b> → '+v;};chips.appendChild(c);});
  host.appendChild(chips);host.appendChild(out);
}

// 18) Format-Wähler ----------------------------------------------------
function formatWidget(id){const host=q(id);if(!host)return;
  const data={'WAV':['Verlustfrei','Groß','Master & Archivierung','24 Bit / 48 kHz'],
    'MP3 320':['Verlustbehaftet','Klein','Online & Sharing','320 kbps / 44,1 kHz'],
    'FLAC':['Verlustfrei (komprimiert)','Mittel','Archiv für Hörer','24 Bit'],
    'AAC':['Verlustbehaftet','Klein','Apple / Streaming','256 kbps']};
  const sel=document.createElement('select');Object.keys(data).forEach(k=>{const o=document.createElement('option');o.textContent=k;sel.appendChild(o);});
  const out=document.createElement('div');out.className='feedbackline show ok';
  function upd(){const d=data[sel.value];out.innerHTML='<b>'+sel.value+'</b> · Qualität: '+d[0]+' · Größe: '+d[1]+' · Einsatz: '+d[2]+' · Typisch: '+d[3];}
  sel.onchange=upd;const r=document.createElement('div');r.className='row';
  r.appendChild(Object.assign(document.createElement('span'),{textContent:'Format wählen:'}));r.appendChild(sel);
  host.appendChild(r);host.appendChild(out);upd();
}

// 19) Loudness-Vergleich ----------------------------------------------
function loudnessWidget(id){const host=q(id);if(!host)return;
  const rows=[['Film / TV',-23],['Apple Music',-16],['Spotify / YouTube',-14],['CD (laut)',-8]];
  const wrap=document.createElement('div');
  rows.forEach(([n,l])=>{const pct=(l+30)/30*100;const row=document.createElement('div');row.className='row';
    row.innerHTML='<span style="width:150px;font-size:.85rem">'+n+'</span>'+
      '<div class="meter" style="flex:1"><span style="width:'+pct+'%"></span></div>'+
      '<b class="readout" style="width:80px;text-align:right">'+l+' LUFS</b>';wrap.appendChild(row);});
  const p=document.createElement('p');p.className='audiohint';p.textContent='Je weiter rechts, desto lauter (höherer LUFS-Wert). Streaming normalisiert lautere Tracks wieder herunter.';
  host.appendChild(p);host.appendChild(wrap);
}

// 20) Spot-the-error A/B ----------------------------------------------
function spotError(id){const host=q(id);if(!host)return;
  function abPlay(make){Snd.stopAll();const c=Snd.init();const node=make(c);setTimeout(()=>{try{node.stop()}catch(e){}},1400);}
  function noiseChain(filterFn){const c=Snd.ctx;const s=c.createBufferSource();s.buffer=Snd.noiseBuf();s.loop=true;
    const g=c.createGain();g.gain.value=0.45;let last=s;if(filterFn){last=filterFn(c,s);}last.connect(g);g.connect(Snd.master);s.start();
    const n={node:g,stop:()=>{try{g.gain.setTargetAtTime(0,c.currentTime,0.05);s.stop(c.currentTime+0.15);}catch(e){}}};return Snd.reg(n);}
  const cases=[
    ['🎚️ Bass: korrekt vs. zu viel',
      ()=>noiseChain((c,s)=>{const f=c.createBiquadFilter();f.type='highpass';f.frequency.value=120;s.connect(f);return f;}),
      ()=>noiseChain((c,s)=>{const f=c.createBiquadFilter();f.type='lowshelf';f.frequency.value=200;f.gain.value=15;s.connect(f);return f;})],
    ['💧 Hall: dezent vs. zu viel',
      ()=>{const c=Snd.ctx;const o=c.createOscillator();o.type='triangle';o.frequency.value=440;const g=c.createGain();g.gain.value=0.4;o.connect(g);g.connect(Snd.master);o.start();return Snd.reg({node:g,stop:()=>{g.gain.setTargetAtTime(0,c.currentTime,0.05);o.stop(c.currentTime+0.12);}});},
      ()=>{const c=Snd.ctx;const o=c.createOscillator();o.type='triangle';o.frequency.value=440;const cv=c.createConvolver();cv.buffer=Snd.impulse(2.5,2);const w=c.createGain();w.gain.value=1.4;const out=c.createGain();out.gain.value=0.4;o.connect(cv);cv.connect(w);w.connect(out);o.connect(out);out.connect(Snd.master);o.start();return Snd.reg({node:out,stop:()=>{out.gain.setTargetAtTime(0,c.currentTime,0.1);o.stop(c.currentTime+0.2);}});}]
  ];
  cases.forEach(([title,good,bad])=>{const w=document.createElement('div');w.style.margin='10px 0';
    const h=document.createElement('div');h.style.fontWeight='600';h.style.marginBottom='6px';h.textContent=title;
    const chips=document.createElement('div');chips.className='chips';
    const a=document.createElement('button');a.className='chip';a.textContent='✅ richtig';a.onclick=()=>{flash(a);abPlay(good);};
    const b=document.createElement('button');b.className='chip';b.textContent='⚠️ Fehler';b.onclick=()=>{flash(b);abPlay(bad);};
    chips.appendChild(a);chips.appendChild(b);w.appendChild(h);w.appendChild(chips);host.appendChild(w);});
}

// 21) Soundcheck-Timer -------------------------------------------------
function timerWidget(id){const host=q(id);if(!host)return;let t=null,sec=900;
  const disp=document.createElement('div');disp.className='readout';disp.style.fontSize='2rem';
  function show(){const m=Math.floor(Math.abs(sec)/60),s=Math.abs(sec)%60;disp.textContent=(sec<0?'-':'')+m+':'+(s<10?'0':'')+s;
    disp.style.color=sec<=0?'var(--red)':(sec<180?'var(--yellow)':'var(--green)');}
  const start=btn('▶ 15-Min-Soundcheck','primary');const reset=btn('↺ Reset','');
  start.onclick=()=>{if(t){clearInterval(t);t=null;start.textContent='▶ Weiter';}else{start.textContent='⏸ Pause';t=setInterval(()=>{sec--;show();},1000);}};
  reset.onclick=()=>{clearInterval(t);t=null;sec=900;start.textContent='▶ 15-Min-Soundcheck';show();};
  const r=document.createElement('div');r.className='row';r.appendChild(start);r.appendChild(reset);
  host.appendChild(disp);host.appendChild(r);show();
}

// 22) Notiz-Feld -------------------------------------------------------
function notesWidget(id,pkey){const host=q(id);if(!host)return;
  const ta=document.createElement('textarea');ta.setAttribute('data-persist',pkey);ta.rows=6;
  ta.style.cssText='width:100%;background:#10151c;color:var(--txt);border:1px solid var(--line);border-radius:8px;padding:10px;font-family:var(--sans);font-size:.95rem';
  ta.placeholder='Tippe hier deine Schnellnotizen … (wird automatisch in deinem Browser gespeichert)';
  host.appendChild(ta);initPersist();
}

//============================ Boot ============================
document.addEventListener('DOMContentLoaded',function(){
  const sb=q('audioStop');if(sb){sb.onclick=()=>Snd.stopAll();}
  initQuiz();initPersist();
  if(window.PAGE_INIT)try{window.PAGE_INIT();}catch(e){console.error(e);}
  if(document.body.classList.contains('hub'))initHub();
});
"""
