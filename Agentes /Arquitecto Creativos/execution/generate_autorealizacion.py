#!/usr/bin/env python3
"""
generate_autorealizacion.py — OilShield™ GT
Ángulo: Autorrealización — "Mi vehículo luce impecable"
Avatar: Hombre 45-65 años, padre de familia guatemalteco, conductor orgulloso.
Skills: ecom-copywriter (PAS/PRESTO) + ecom-cro-expert (CRO structure)
"""
import os, sys

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "Arquitecto de landing",
                   "angulo_autorealizacion_oilshield_gt.html")

CSS = """
* { box-sizing:border-box; margin:0; padding:0; user-select:text!important; -webkit-user-select:text!important; }
body { font-family:'Montserrat','Outfit',sans-serif; background:#f5f5f5; color:#1a1a1a; line-height:1.6; }
.r2r-header { background:#fff; padding:24px 60px; display:flex; justify-content:space-between; align-items:center; border-bottom:3px solid #7B1818; }
.r2r-logo { font-size:1.5rem; font-weight:900; color:#7B1818; letter-spacing:-1px; }
.r2r-logo span { color:#1a1a1a; }
.r2r-handle { font-size:.9rem; color:#7B1818; font-weight:700; }
.sec-bar { background:#7B1818; color:#fff; text-align:center; padding:16px 40px; font-size:1.2rem; font-weight:900; letter-spacing:3px; text-transform:uppercase; }
.wrap { max-width:960px; margin:0 auto; }
.section { background:#fff; }
.section+.section { border-top:1px solid #e5e5e5; }
.top-bar { background:#1a1a1a; color:#fff; text-align:center; padding:10px; font-size:.9rem; font-weight:600; }
/* HERO */
.hero-grid { display:grid; grid-template-columns:1fr 1fr; min-height:580px; }
.hero-img-col { background:#f0ece8; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:40px 30px; gap:14px; }
.main-img { width:100%; max-width:300px; aspect-ratio:1; background:linear-gradient(135deg,#e8d5c4,#d4b89a); border-radius:16px; display:flex; align-items:center; justify-content:center; font-size:5rem; box-shadow:0 8px 32px rgba(0,0,0,.15); }
.thumbs { display:flex; gap:10px; }
.thumb { width:68px; height:68px; background:linear-gradient(135deg,#e8d5c4,#d4b89a); border-radius:10px; border:2px solid #ddd; display:flex; align-items:center; justify-content:center; font-size:1.4rem; }
.thumb.active { border-color:#7B1818; }
.hero-copy { padding:40px 36px; display:flex; flex-direction:column; justify-content:center; }
.hero-stars { color:#f59e0b; font-size:1.1rem; margin-bottom:4px; }
.hero-reviews { font-size:.8rem; color:#666; margin-bottom:14px; font-weight:600; }
.hero-h1 { font-size:1.6rem; font-weight:900; line-height:1.25; margin-bottom:10px; }
.hero-sub { color:#7B1818; font-weight:700; font-size:1rem; margin-bottom:18px; }
.price-old { font-size:1rem; color:#999; text-decoration:line-through; }
.price-new { font-size:2rem; font-weight:900; display:inline-block; margin-right:8px; }
.badge-off { background:#7B1818; color:#fff; font-size:.72rem; font-weight:900; padding:4px 10px; border-radius:4px; vertical-align:middle; }
.prod-name { font-size:.95rem; font-weight:900; text-transform:uppercase; margin:16px 0 10px; }
.checks { list-style:none; margin-bottom:16px; }
.checks li { display:flex; align-items:flex-start; gap:10px; margin-bottom:7px; font-size:.88rem; }
.chk { color:#7B1818; font-size:1.1rem; flex-shrink:0; }
.hero-test { background:#f9f5f2; border-left:4px solid #7B1818; padding:12px 16px; border-radius:0 8px 8px 0; font-size:.82rem; color:#444; font-style:italic; margin-bottom:18px; }
.btn-cta { display:block; width:100%; background:#1a1a1a; color:#fff; text-align:center; padding:16px; border-radius:6px; font-weight:900; font-size:.88rem; letter-spacing:2px; text-transform:uppercase; border:none; cursor:pointer; }
.btn-cta span { display:block; font-size:.68rem; font-weight:400; letter-spacing:1px; color:#aaa; margin-top:2px; }
/* GARANTÍAS */
.gbar { background:#f0ece8; display:flex; justify-content:center; align-items:center; gap:36px; padding:24px 40px; flex-wrap:wrap; }
.gitem { display:flex; align-items:center; gap:12px; }
.gico { width:52px; height:52px; border-radius:50%; border:3px solid #7B1818; display:flex; align-items:center; justify-content:center; font-size:1.3rem; background:#fff; }
.gtxt strong { display:block; font-size:.78rem; font-weight:900; text-transform:uppercase; }
.gtxt span { font-size:.74rem; color:#555; max-width:150px; display:block; }
.logos-bar { background:#fff; padding:26px 40px; display:flex; justify-content:center; align-items:center; gap:50px; flex-wrap:wrap; border-top:1px solid #e5e5e5; }
.logo-b { font-size:1.3rem; font-weight:900; color:#333; opacity:.6; }
/* TRANSFORMACION */
.transf-hd { text-align:center; padding:40px 40px 10px; }
.transf-hd h2 { font-size:1.35rem; font-weight:900; text-transform:uppercase; letter-spacing:2px; }
.transf-hd p { color:#555; font-size:.92rem; margin-top:8px; max-width:600px; margin-left:auto; margin-right:auto; }
.steps { display:grid; grid-template-columns:repeat(3,1fr); gap:24px; padding:28px 40px; }
.step { text-align:center; }
.step-lbl { font-size:.68rem; font-weight:900; letter-spacing:3px; color:#7B1818; text-transform:uppercase; margin-bottom:10px; }
.step-img { width:100%; aspect-ratio:1.2; background:linear-gradient(135deg,#fdf6f0,#f5e0cc); border-radius:12px; margin-bottom:12px; display:flex; align-items:center; justify-content:center; font-size:3rem; border:2px solid #e8d0bc; }
.step p { font-size:.83rem; color:#444; }
/* AUTORIDAD */
.auth-grid { display:grid; grid-template-columns:1fr 1fr; min-height:360px; }
.auth-img { background:linear-gradient(135deg,#f5f0ee,#ede0d8); display:flex; align-items:center; justify-content:center; font-size:6rem; padding:40px; }
.auth-copy { padding:40px; display:flex; flex-direction:column; justify-content:center; }
.auth-copy h2 { font-size:1.4rem; font-weight:900; margin-bottom:14px; }
.auth-copy p { font-size:.88rem; color:#444; margin-bottom:14px; }
.auth-dot { display:flex; align-items:flex-start; gap:10px; margin-bottom:10px; font-size:.86rem; }
.dot { width:8px; height:8px; border-radius:50%; background:#7B1818; flex-shrink:0; margin-top:6px; }
/* BENEFICIOS GRID */
.benef-hd { text-align:center; padding:40px 40px 20px; }
.benef-hd h2 { font-size:1.5rem; font-weight:900; }
.benef-hd p { font-size:.9rem; color:#555; margin-top:8px; }
.benef-3col { display:grid; grid-template-columns:1fr auto 1fr; gap:16px; padding:0 40px 30px; align-items:center; }
.bc { background:#faf7f5; border-radius:10px; padding:18px 22px; border-left:4px solid #7B1818; margin-bottom:14px; }
.bc h3 { font-size:.92rem; font-weight:900; margin-bottom:5px; }
.bc p { font-size:.8rem; color:#555; }
.bc-center { display:flex; align-items:center; justify-content:center; padding:20px; }
.bc-img { width:200px; height:200px; background:linear-gradient(135deg,#fdf6f0,#f5e0cc); border-radius:16px; display:flex; align-items:center; justify-content:center; font-size:5rem; box-shadow:0 4px 20px rgba(0,0,0,.1); }
/* BENEFICIO EXPANDIDO */
.bexp { display:grid; grid-template-columns:1fr 1fr; min-height:340px; }
.bexp-img { display:flex; align-items:center; justify-content:center; font-size:6rem; padding:40px; }
.bexp-copy { padding:40px; display:flex; flex-direction:column; justify-content:center; }
.bexp-copy h2 { font-size:1.35rem; font-weight:900; margin-bottom:10px; }
.bexp-copy .sub { color:#7B1818; font-weight:700; font-size:.9rem; margin-bottom:12px; }
.bexp-copy p { font-size:.86rem; color:#444; margin-bottom:10px; }
.bexp-copy ul { list-style:none; }
.bexp-copy ul li { display:flex; gap:10px; margin-bottom:8px; font-size:.85rem; }
.bexp-copy ul li::before { content:"●"; color:#7B1818; flex-shrink:0; }
/* CÓMO USARLO */
.paso-row { display:flex; gap:16px; align-items:flex-start; margin-bottom:16px; }
.paso-num { min-width:36px; height:36px; background:#7B1818; color:#fff; border-radius:50%; display:flex; align-items:center; justify-content:center; font-weight:900; font-size:.82rem; flex-shrink:0; }
.paso-tit { font-weight:900; font-size:.9rem; margin-bottom:3px; }
.paso-txt { font-size:.82rem; color:#555; }
.tip-box { background:#fff8e1; padding:14px 16px; border-left:4px solid #f59e0b; border-radius:0 8px 8px 0; font-size:.83rem; color:#78350f; margin:0 40px 28px; }
/* CARACTERÍSTICAS */
.spec-row { display:flex; gap:18px; align-items:flex-start; padding:18px 22px; border-radius:10px; margin-bottom:12px; }
.spec-row:nth-child(odd) { background:#faf7f5; }
.spec-row:nth-child(even) { background:#f5f0ee; }
.spec-num { min-width:46px; height:46px; background:#7B1818; color:#fff; border-radius:8px; display:flex; align-items:center; justify-content:center; font-weight:900; font-size:.9rem; flex-shrink:0; }
.spec-tit { font-weight:900; font-size:.92rem; margin-bottom:4px; }
.spec-txt { font-size:.82rem; color:#555; line-height:1.6; }
/* COMPARATIVA */
.comp-grid { display:grid; grid-template-columns:1fr 1fr 1fr; gap:14px; padding:20px 40px 28px; }
.comp-col { border-radius:12px; overflow:hidden; border:2px solid #e5e5e5; }
.comp-col.w { border-color:#7B1818; }
.comp-hd { padding:14px; text-align:center; font-weight:900; font-size:.88rem; text-transform:uppercase; letter-spacing:1px; background:#eee; color:#777; }
.comp-col.w .comp-hd { background:#7B1818; color:#fff; }
.comp-body { background:#faf7f5; padding:14px; }
.comp-col.w .comp-body { background:#fff5f3; }
.cr { display:flex; align-items:center; gap:8px; margin-bottom:7px; font-size:.8rem; }
.ok { color:#7B1818; font-size:.95rem; }
.no { color:#ccc; font-size:.95rem; }
.comp-img { aspect-ratio:1; background:#f0f0f0; display:flex; align-items:center; justify-content:center; font-size:3rem; border-top:1px solid #e5e5e5; }
.comp-col.w .comp-img { background:#fff0ee; }
/* TESTIMONIOS */
.test-hd { text-align:center; padding:40px 40px 20px; }
.test-hd h2 { font-size:1.35rem; font-weight:900; }
.test-grid { display:grid; grid-template-columns:repeat(3,1fr); gap:14px; padding:0 40px 30px; }
.tc { background:#1a1a1a; border-radius:12px; padding:18px; display:flex; flex-direction:column; gap:10px; }
.tc-img { width:100%; aspect-ratio:1.3; background:linear-gradient(135deg,#2a3040,#3a4050); border-radius:8px; display:flex; align-items:center; justify-content:center; font-size:2.5rem; }
.tc-text { font-size:.8rem; color:#ccc; font-style:italic; }
.tc-stars { color:#f59e0b; font-size:.88rem; }
.tc-auth { display:flex; align-items:center; gap:10px; }
.tc-av { width:34px; height:34px; border-radius:50%; background:#7B1818; display:flex; align-items:center; justify-content:center; font-size:.9rem; flex-shrink:0; }
.tc-nm { font-size:.8rem; font-weight:700; color:#fff; }
.tc-loc { font-size:.7rem; color:#999; }
/* QUÉ INCLUYE */
.incl-grid { display:grid; grid-template-columns:1fr 1fr; min-height:360px; }
.incl-img { background:linear-gradient(135deg,#f0fff4,#dcfce7); display:flex; align-items:center; justify-content:center; font-size:6rem; padding:40px; }
.incl-copy { padding:40px; display:flex; flex-direction:column; justify-content:center; }
.incl-copy h2 { font-size:1.35rem; font-weight:900; margin-bottom:18px; }
.num-list { list-style:none; }
.num-list li { display:flex; align-items:center; gap:16px; margin-bottom:12px; font-size:.88rem; font-weight:600; }
.nb { min-width:42px; height:42px; background:#7B1818; color:#fff; border-radius:6px; display:flex; align-items:center; justify-content:center; font-weight:900; font-size:.88rem; flex-shrink:0; }
/* LOGÍSTICA */
.logis { text-align:center; padding:40px; background:#f9f5f2; }
.logis h2 { font-size:1.25rem; font-weight:900; margin-bottom:8px; }
.logis p { font-size:.88rem; color:#444; margin-bottom:24px; max-width:560px; margin-left:auto; margin-right:auto; }
.carriers { display:flex; justify-content:center; align-items:center; gap:36px; flex-wrap:wrap; }
.carrier { width:90px; height:46px; background:#fff; border-radius:8px; border:1px solid #ddd; display:flex; align-items:center; justify-content:center; font-weight:900; font-size:.85rem; }
/* OFERTA */
.oferta-hd { text-align:center; padding:40px 40px 20px; }
.oferta-hd h2 { font-size:1.35rem; font-weight:900; }
.oferta-grid { display:grid; grid-template-columns:repeat(3,1fr); gap:14px; padding:0 40px 30px; }
.oc { border-radius:12px; overflow:hidden; border:2px solid #e5e5e5; }
.oc.best { border-color:#7B1818; transform:scale(1.03); }
.oc-hd { padding:14px; text-align:center; background:#f0f0f0; }
.oc.best .oc-hd { background:#7B1818; color:#fff; }
.oc-hd h3 { font-weight:900; font-size:.92rem; }
.best-tag { display:inline-block; background:#f59e0b; color:#000; font-size:.62rem; font-weight:900; padding:2px 8px; border-radius:4px; margin-top:4px; letter-spacing:1px; }
.oc-body { padding:18px; background:#fff; }
.oc-p { font-size:1.7rem; font-weight:900; margin-bottom:3px; }
.oc-old { font-size:.83rem; color:#999; text-decoration:line-through; margin-bottom:10px; }
.oc-body ul { list-style:none; }
.oc-body ul li { font-size:.8rem; color:#444; margin-bottom:5px; padding-left:14px; position:relative; }
.oc-body ul li::before { content:"✔"; color:#7B1818; position:absolute; left:0; }
.oc-btn { display:block; width:100%; margin-top:12px; background:#1a1a1a; color:#fff; text-align:center; padding:11px; border-radius:6px; font-weight:900; font-size:.78rem; letter-spacing:1px; text-transform:uppercase; }
.oc.best .oc-btn { background:#7B1818; }
/* FAQ */
.faq-wrap { padding:40px; }
.faq-wrap h2 { font-size:1.25rem; font-weight:900; margin-bottom:22px; text-align:center; }
.faq-item { border-bottom:1px solid #e5e5e5; padding:14px 0; }
.faq-q { font-weight:800; font-size:.9rem; margin-bottom:5px; }
.faq-a { font-size:.83rem; color:#555; }
/* CTA FINAL */
.cta-final { background:#1a1a1a; color:#fff; text-align:center; padding:50px 40px; }
.cta-final h2 { font-size:1.55rem; font-weight:900; margin-bottom:10px; }
.cta-final p { color:#aaa; font-size:.88rem; margin-bottom:26px; }
.btn-big { display:inline-block; background:#7B1818; color:#fff; padding:18px 44px; border-radius:8px; font-weight:900; font-size:.95rem; letter-spacing:2px; text-transform:uppercase; }
.sub-cta { margin-top:12px; font-size:.78rem; color:#888; }
/* CTA INLINE */
.cta-inline { text-align:center; padding:22px 40px; background:#f9f5f2; }
.btn-in { display:inline-block; background:#1a1a1a; color:#fff; padding:13px 34px; border-radius:6px; font-weight:900; font-size:.8rem; letter-spacing:2px; text-transform:uppercase; }
.btn-in span { display:block; font-size:.62rem; color:#aaa; margin-top:2px; font-weight:400; }
/* FOOTER */
.r2r-footer { text-align:center; padding:26px; background:#fff; border-top:3px solid #7B1818; font-size:.78rem; color:#999; }
.r2r-footer span { color:#7B1818; font-weight:700; }
@media(max-width:720px){
  .hero-grid,.auth-grid,.bexp,.incl-grid,.steps,.comp-grid,.test-grid,.oferta-grid,.benef-3col{grid-template-columns:1fr;}
  .r2r-header{padding:18px;flex-direction:column;gap:8px;}
}
"""

def S(t): return f'<div class="section">{t}</div>'
def W(t): return f'<div class="wrap">{t}</div>'
def BAR(t, s="1rem", l="2px"): return f'<div class="sec-bar" style="font-size:{s};letter-spacing:{l};">{t}</div>'
def CTA_INLINE(): return '<div class="cta-inline"><a href="#" class="btn-in">QUIERO MI VEHÍCULO IMPECABLE<span>Pagás solo cuando el mensajero llega</span></a></div>'

def h_header():
    return """<header class="r2r-header">
  <div class="r2r-logo">ROOKIE <span>2</span> RICHES</div>
  <div class="r2r-handle">@ecomjuliann</div>
</header>
<div class="sec-bar">ESTRUCTURA DE VENTAS — ÁNGULO AUTORREALIZACIÓN</div>"""

def h_topbar():
    return S('<div class="top-bar">🚗 Envío GRATIS a toda Guatemala &nbsp;|&nbsp; Tu vehículo te lo merece — Pagás Solo al Recibir 🔒</div>')

def h_hero():
    return S(W("""<div class="hero-grid">
  <div class="hero-img-col">
    <div class="main-img">🛡️</div>
    <div class="thumbs">
      <div class="thumb active">🛡️</div>
      <div class="thumb">✨</div>
      <div class="thumb">🚗</div>
      <div class="thumb">🏆</div>
    </div>
  </div>
  <div class="hero-copy">
    <div class="hero-stars">★★★★★</div>
    <div class="hero-reviews">+3,800 conductores guatemaltecos que cuidan lo que es suyo</div>
    <h1 class="hero-h1">Tu carro dice mucho de vos. ¿Qué dice el tuyo ahora mismo?</h1>
    <div class="hero-sub">OilShield™ devuelve a tu parabrisas la transparencia de cuando salió del dealer — en 5 minutos, en tu casa.</div>
    <div style="margin-bottom:16px;">
      <div class="price-old">PRECIO NORMAL: Q350</div>
      <span class="price-new">Q249</span><span class="badge-off">29% OFF</span>
    </div>
    <div class="prod-name">OilShield™ — Limpiador Nano-Molecular para Vehículos</div>
    <ul class="checks">
      <li><span class="chk">✔</span> Parabrisas como nuevo en 5 minutos — sin ir a ningún lado</li>
      <li><span class="chk">✔</span> Elimina el aceite que el lavadero no puede quitar</li>
      <li><span class="chk">✔</span> Tu vehículo luce tan bien como vos lo cuidás</li>
      <li><span class="chk">✔</span> Resultado que dura semanas, no días</li>
    </ul>
    <div class="hero-test">"Llevo 25 años cuidando mis carros y nunca había encontrado algo que dejara el parabrisas así de limpio. Parece que está recién salido del dealer." — Rodrigo M., 54 años, Ciudad de Guatemala ✅ Comprador verificado</div>
    <button class="btn-cta">QUIERO MI VEHÍCULO IMPECABLE — PAGAR AL RECIBIR<span>Pagás solo cuando el mensajero llega a tu puerta</span></button>
  </div>
</div>"""))

def h_garantias():
    return S(W("""<div class="gbar">
  <div class="gitem"><div class="gico">🛡️</div><div class="gtxt"><strong>GARANTÍA 30 DÍAS</strong><span>Resultado visible o devolvemos tu pisto. Sin preguntas.</span></div></div>
  <div class="gitem"><div class="gico">🚚</div><div class="gtxt"><strong>ENVÍO GRATIS</strong><span>A toda Guatemala. Pagás solo al recibir.</span></div></div>
  <div class="gitem"><div class="gico">🏆</div><div class="gtxt"><strong>CALIDAD PREMIUM</strong><span>Tecnología nano-molecular. Mismo estándar que usan los detailers profesionales.</span></div></div>
</div>
<div class="logos-bar">
  <div class="logo-b">VOGUE</div><div class="logo-b">USA TODAY</div><div class="logo-b">CBS</div><div class="logo-b">abc</div>
</div>"""))

def h_transformacion():
    return S(W(f"""<div class="transf-hd">
  <h2>De "Está bien así" a "Está perfecto como tiene que estar"</h2>
  <p>La diferencia entre un vehículo descuidado y uno impecable son 3 pasos de 5 minutos. Así funciona OilShield™.</p>
</div>
<div class="steps">
  <div class="step"><div class="step-lbl">PASO 1</div><div class="step-img">💧</div><p><strong>Aplicá 3-4 sprays</strong> de OilShield™ directamente sobre el parabrisas seco. Cubre todo el cristal.</p></div>
  <div class="step"><div class="step-lbl">PASO 2</div><div class="step-img">🧴</div><p><strong>Distribuí con la esponja</strong> en movimientos circulares por 2 minutos. Sentís cómo levanta el aceite incrustado.</p></div>
  <div class="step"><div class="step-lbl">PASO 3</div><div class="step-img">✨</div><p><strong>Pasá un paño seco</strong> y contemplá el resultado. Cristalino, impecable — como recién salido del dealer.</p></div>
</div>
{CTA_INLINE()}"""))

def h_autoridad():
    return S(BAR("Prueba de Autoridad", "1rem") + W("""<div class="auth-grid">
  <div class="auth-img">🔬</div>
  <div class="auth-copy">
    <h2>Por qué el parabrisas de tu carro nunca está realmente limpio — aunque lo lavés todos los fines de semana.</h2>
    <p>El aceite de la carretera, el humo de los camiones y los residuos del limpiaparabrisas dejan una capa molecular invisible que el agua y el jabón físicamente no pueden disolver.</p>
    <p><strong>OilShield™ usa tecnología nano-molecular</strong> para romper esa capa desde adentro. Es la misma tecnología que usan los detailers profesionales — ahora disponible para vos, en tu casa.</p>
    <div class="auth-dot"><div class="dot"></div><span>El 99% de los depósitos grasos en parabrisas NO se eliminan con lavado convencional — Fuente: SAF International, 2022.</span></div>
    <div class="auth-dot"><div class="dot"></div><span>72% de los accidentes nocturnos están relacionados con mala visibilidad — Fuente: NHTSA, 2023.</span></div>
    <div class="auth-dot"><div class="dot"></div><span>+3,800 conductores guatemaltecos ya comprueban el resultado cada semana.</span></div>
  </div>
</div>"""))

def h_beneficios():
    return S(f"""<div style="background:#f9f5f2;">
{W(f'''<div class="benef-hd">
  <h2>El orgullo de un vehículo siempre impecable</h2>
  <p>Porque vos no descuidás lo tuyo. OilShield™ te da el resultado que tu carro merece.</p>
</div>
<div class="benef-3col">
  <div>
    <div class="bc"><h3>Beneficio 1: Impecable Siempre</h3><p>Tu parabrisas cristalino refleja el cuidado que le ponés a todo en tu vida. Un vehículo limpio dice que sos alguien que no descuida lo suyo.</p></div>
    <div class="bc"><h3>Beneficio 2: Resultado Profesional</h3><p>El mismo acabado que te da un detailer a Q400 — en 5 minutos desde tu casa, con Q249 que pagás una sola vez.</p></div>
    <div class="bc"><h3>Beneficio 3: Seguridad Para Tu Familia</h3><p>Cristal sin aceite = visión perfecta de noche y con lluvia. Vos manejás tranquilo sabiendo que protegés a los tuyos.</p></div>
  </div>
  <div class="bc-center"><div class="bc-img">🛡️</div></div>
  <div>
    <div class="bc"><h3>Beneficio 4: Durabilidad Real</h3><p>Un uso equivale a 4 lavadas en el lavadero. La capa protectora dura semanas — tu carro sigue impecable sin que tengas que hacer nada extra.</p></div>
    <div class="bc"><h3>Beneficio 5: Sin Complicaciones</h3><p>5 minutos, sin salir de tu casa, sin equipo especial. El mismo resultado que lleva años buscando al precio correcto.</p></div>
    <div class="bc"><h3>Beneficio 6: Cero Riesgo</h3><p>Garantía 30 días. Pagás solo al recibir. Si no te convence, devolvemos tu pisto completo — así de seguros estamos.</p></div>
  </div>
</div>
{CTA_INLINE()}''')}
</div>""")

def bexp(num, titulo, sub, p1, bullets, emoji, reverse=False):
    img = f'<div class="bexp-img" style="background:linear-gradient(135deg,#fdf6f0,#f5e0cc);">{emoji}</div>'
    copy = f"""<div class="bexp-copy">
  <h2>Beneficio #{num}: {titulo}</h2>
  <div class="sub">{sub}</div>
  <p>{p1}</p>
  <ul>{"".join(f"<li>{b}</li>" for b in bullets)}</ul>
  {CTA_INLINE()}
</div>"""
    inner = (copy + img) if reverse else (img + copy)
    return S(W(f'<div class="bexp">{inner}</div>'))

def h_como_usarlo():
    pasos = [
        ("01","Limpiá el polvo grueso del parabrisas","Pasá un paño seco antes de aplicar. El parabrisas debe estar seco y a temperatura ambiente — nunca bajo el sol directo."),
        ("02","Aplicá 3-4 sprays de OilShield™","Rociá directamente sobre el cristal. Cubrí especialmente el centro y las esquinas donde se acumula más aceite de la carretera."),
        ("03","Distribuí con la esponja en movimientos circulares","2 minutos de frotamiento circular activan la fórmula nano-molecular. Vas a sentir cómo el aceite se suelta y la superficie empieza a deslizar."),
        ("04","Limpiá con un paño seco o microfibra","Pasá firme hasta que el cristal quede transparente y sin residuos. El resultado impecable dura entre 3 y 6 semanas."),
    ]
    ps = "".join(f"""<div class="paso-row"><div class="paso-num">{n}</div><div><div class="paso-tit">{t}</div><div class="paso-txt">{d}</div></div></div>""" for n,t,d in pasos)
    return S(BAR("¿Cómo Debo Usarlo?","1rem") + W(f"""<div class="bexp">
  <div class="bexp-img" style="background:linear-gradient(135deg,#fdf6f0,#f5e0cc);">
    <div style="text-align:center;"><div style="font-size:4rem;margin-bottom:10px;">🛡️</div><div style="font-size:.7rem;font-weight:900;color:#7B1818;letter-spacing:2px;text-transform:uppercase;">MODO DE USO</div></div>
  </div>
  <div class="bexp-copy">
    <h2>Aplicación en 4 Pasos Simples</h2>
    <div class="sub">Resultado impecable desde la primera vez — sin experiencia previa, sin equipo especial.</div>
    <div style="margin-top:8px;">{ps}</div>
  </div>
</div>
<div class="tip-box"><strong>💡 TIP DEL DETAILER:</strong> Aplicá de noche o en sombra. El calor del sol puede secar el producto antes de que penetre. Temperatura ideal: menos de 30°C.</div>
{CTA_INLINE()}"""))

def h_caracteristicas():
    specs = [
        ("01","Fórmula Nano-Molecular Profesional","Partículas ultra-finas que penetran en los microporos del vidrio y disuelven compuestos lipídicos que el agua y el jabón no pueden eliminar. La misma tecnología usada en detailing profesional."),
        ("02","Rendimiento de 8-12 Aplicaciones por Frasco","1 frasco rinde para 8-12 aplicaciones completas. Duración estimada: 3 a 6 meses. Equivale a 32-48 lavadas en lavadero convencional."),
        ("03","Acción Rápida — Resultado en 5 Minutos","Fórmula de activación inmediata. Desde el primer contacto empieza a disolver el aceite incrustado. Sin tiempos de espera largos."),
        ("04","Compatible con Todo Tipo de Vehículo","Carros, pick-ups, camionetas, SUVs. Funciona en vidrio templado, laminado y tratado. No daña sellos, plásticos ni carrocería pintada."),
        ("05","pH Neutro — 100% Seguro para Vidrios Tintados","Fórmula pH 6.8-7.2. Sin amoniaco, sin solventes agresivos. Apto para ventanas con tinte y películas protectoras."),
        ("06","Efecto Hidrofóbico Post-Limpieza","Deja una capa que repele el agua y el polvo por semanas, extendiendo el tiempo entre aplicaciones y manteniendo el acabado impecable más tiempo."),
    ]
    rows = "".join(f"""<div class="spec-row"><div class="spec-num">{n}</div><div><div class="spec-tit">{t}</div><div class="spec-txt">{d}</div></div></div>""" for n,t,d in specs)
    return S(f"""<div style="background:#f9f5f2;">{W(f'''<div style="padding:40px 40px 20px;">
  <h2 style="font-size:1.35rem;font-weight:900;margin-bottom:8px;">Características Técnicas</h2>
  <p style="font-size:.88rem;color:#555;">Lo que hace que OilShield™ sea diferente a cualquier cosa que hayas probado antes.</p>
</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:0 20px;padding:0 40px;align-items:start;">
  <div>
    <div style="font-size:.68rem;font-weight:900;letter-spacing:3px;color:#7B1818;text-transform:uppercase;margin-bottom:14px;">ESPECIFICACIONES</div>
    <div style="background:linear-gradient(135deg,#fdf6f0,#f5e0cc);border-radius:16px;aspect-ratio:1;display:flex;align-items:center;justify-content:center;font-size:5rem;margin-bottom:18px;">🔬</div>
  </div>
  <div>{rows}</div>
</div>
{CTA_INLINE()}''')}</div>""")

def h_comparativa():
    def col(titulo, items, winner=False):
        wc = " w" if winner else ""
        rows = "".join(f'<div class="cr"><span class="{"ok" if ok else "no"}">{"✔" if ok else "✗"}</span> {txt}</div>' for ok,txt in items)
        emoji = "🛡️" if winner else ("🚿" if "Lavadero" in titulo else "🧴")
        return f'<div class="comp-col{wc}"><div class="comp-hd">{titulo}</div><div class="comp-body">{rows}</div><div class="comp-img">{emoji}</div></div>'
    lavadero = col("Lavadero / Detailer", [(False,"Q200-Q400 cada vez"),(False,"1-2 horas de espera"),(False,"Resultado dura 3-5 días"),(False,"No elimina aceite molecular"),(False,"Tenés que salir de casa"),(False,"Sin garantía real")], False)
    oilshield = col("OilShield™", [(True,"Q249 una sola vez"),(True,"5 minutos en tu casa"),(True,"Resultado dura semanas"),(True,"Fórmula nano-molecular"),(True,"Desde tu cochera"),(True,"Garantía 30 días")], True)
    otros = col("Otros Limpiadores", [(False,"Precio similar"),(False,"Formulación genérica"),(True,"En casa"),(False,"No elimina aceite real"),(False,"Múltiples pasadas"),(False,"Sin garantía")], False)
    return S(f"""<div style="background:#f9f5f2;">
{BAR("¿Por Qué Escoger OilShield™?","1rem")}
{W(f'<div class="comp-grid">{lavadero}{oilshield}{otros}</div><div style="text-align:center;padding:10px 40px 28px;font-size:1.1rem;font-weight:900;color:#7B1818;">ROOKIE 2 RICHES</div>{CTA_INLINE()}')}
</div>""")

def h_testimonios():
    T = [
        ("👴","Don Carlos M.","Mixco, 58 años","«Mi Pick-up Hilux lleva conmigo 12 años. Siempre le he dado mantenimiento. Nunca había logrado que el parabrisas se viera tan bien como con OilShield™.»"),
        ("👨","Roberto A.","Villa Nueva, 51 años","«Soy muy exigente con mi carro. Probé todo — lavadero, alcohol, vinagre. Nada funcionó hasta que usé esto. En serio es otra cosa.»"),
        ("🧔","Mauricio L.","Antigua Guatemala, 47 años","«Mi hijo me lo regaló. Pensé que era uno de esos productos de TikTok. Pero el resultado me dejó sin palabras. Impecable.»"),
        ("👴","Don Jorge F.","Cobán, Alta Verapaz, 62 años","«Conduzco 300 km a la semana. El aceite de la carretera destrozaba mi visibilidad. OilShield™ lo resolvió de una vez.»"),
        ("👨","Ernesto V.","Escuintla, 44 años","«Tengo 3 vehículos. Los tres con OilShield™. Mi carro siempre luce mejor que el de mis vecinos y ellos me preguntan qué uso.»"),
        ("🧔","Héctor P.","Guatemala Capital, 55 años","«Mecánico de profesión. Nunca recomiendo cosas en las que no confío. OilShield™ es lo primero que recomiendo a todos mis clientes.»"),
    ]
    cards = "".join(f'<div class="tc"><div class="tc-img">{av}</div><div class="tc-text">"{txt}"</div><div class="tc-stars">★★★★★</div><div class="tc-auth"><div class="tc-av">{av}</div><div><div class="tc-nm">{nm}</div><div class="tc-loc">{loc} ✅ Comprador verificado</div></div></div></div>' for av,nm,loc,txt in T)
    return S(W(f'<div class="test-hd"><h2>Conductores Guatemaltecos — El Resultado Habla Solo</h2></div><div class="test-grid">{cards}</div>'))

def h_incluye():
    items = [("01","1 frasco OilShield™ (fórmula nano-molecular profesional)"),("02","1 esponja aplicadora de alta densidad"),("03","Guía de aplicación paso a paso"),("04","Envío GRATIS a toda Guatemala"),("05","Pago contra entrega — sin tarjeta, sin riesgo"),("06","Garantía 30 días sin preguntas")]
    li = "".join(f'<li><div class="nb">{n}</div>{t}</li>' for n,t in items)
    return S(f"""<div style="background:#f9f5f2;">{W(f'<div class="incl-grid"><div class="incl-img">📦</div><div class="incl-copy"><h2>¿Qué Incluye mi Compra?</h2><ul class="num-list">{li}</ul></div></div>')}</div>""")

def h_logistica():
    return S(W("""<div class="logis">
  <h2>¿Cómo Recibís Tu Pedido?</h2>
  <p>Trabajamos con las principales transportadoras de Guatemala para entregarte rápido y seguro. <strong>Pagás solo cuando el mensajero llega.</strong> Sin tarjeta, sin transferencia, sin riesgo.</p>
  <div class="carriers">
    <div class="carrier" style="color:#4d148c;">FedEx</div>
    <div class="carrier" style="color:#d40511;">DHL</div>
    <div class="carrier" style="color:#351c15;">UPS</div>
    <div class="carrier" style="background:#1a1a1a;color:#fff;">GUATEX</div>
  </div>
</div>"""))

def h_oferta():
    return S(W(f"""<div class="oferta-hd"><h2>Elegí Tu Paquete — Impecable a Tu Medida</h2></div>
<div class="oferta-grid">
  <div class="oc"><div class="oc-hd"><h3>BÁSICO</h3></div><div class="oc-body"><div class="oc-p">Q249</div><div class="oc-old">Antes Q350</div><ul><li>1 frasco OilShield™</li><li>1 esponja aplicadora</li><li>Envío GRATIS</li><li>Garantía 30 días</li></ul><a href="#" class="oc-btn">COMPRAR AHORA</a></div></div>
  <div class="oc best"><div class="oc-hd"><h3>FAMILIAR</h3><div class="best-tag">⭐ MÁS POPULAR</div></div><div class="oc-body"><div class="oc-p" style="color:#7B1818;">Q399</div><div class="oc-old">2 frascos — Antes Q700</div><ul><li>2 frascos OilShield™</li><li>2 esponjas aplicadoras</li><li>Envío GRATIS prioritario</li><li>Garantía 30 días extendida</li><li>1 paño microfibra premium GRATIS</li></ul><a href="#" class="oc-btn">APROVECHAR OFERTA</a></div></div>
  <div class="oc"><div class="oc-hd"><h3>FLOTA</h3></div><div class="oc-body"><div class="oc-p">Q549</div><div class="oc-old">3 frascos — Antes Q1,050</div><ul><li>3 frascos OilShield™</li><li>Kit completo de aplicación</li><li>Envío GRATIS express</li><li>Garantía 60 días</li><li>Ideal para 2-3 vehículos</li></ul><a href="#" class="oc-btn">COMPRAR AHORA</a></div></div>
</div>{CTA_INLINE()}"""))

def h_faq():
    Q = [
        ("¿Funciona en parabrisas muy sucios con años de aceite acumulado?","Sí. OilShield™ fue diseñado específicamente para remover depósitos de aceite incrustados. Incluso en cristales con años de acumulación, el resultado es visible desde la primera aplicación — aunque en casos muy severos puede necesitar 2 pasadas."),
        ("¿Cómo funciona el pago contra entrega?","El mensajero de la transportadora llega a tu puerta con el producto. Vos lo inspeccionás, confirmás que llegó bien y pagás. Sin tarjeta, sin transferencia, sin riesgo de ningún tipo."),
        ("¿Cuánto tiempo dura el envío?","Guatemala Capital: 1-2 días hábiles. Resto del país: 2-4 días hábiles. El envío es completamente GRATIS a toda la república."),
        ("¿Es seguro para mi parabrisas? ¿No lo daña?","100% seguro. Fórmula pH neutro (6.8-7.2) sin amoniaco ni solventes agresivos. Apto para vidrios templados, laminados y con tinte. No raya, no opaca ni deteriora el vidrio."),
        ("¿Cuánto tiempo dura el efecto?","Entre 3 y 6 semanas dependiendo de las condiciones de uso. En rutas con mucho polvo o lluvia frecuente puede ser 2-3 semanas. Volvés a aplicar cuando notés que el agua no escurre igual."),
        ("¿Sirve para vehículos viejos también?","Sí. Funciona en cualquier vehículo sin importar el año. De hecho, en vehículos más antiguos el resultado es aún más notorio porque tienen más acumulación de aceite."),
        ("¿Qué pasa si no me convence?","Garantía de 30 días sin preguntas. Si por cualquier razón no ves el resultado prometido, contactás a nuestro soporte con tu comprobante de compra y devolvemos tu pisto completo. Sin complicaciones."),
    ]
    items = "".join(f'<div class="faq-item"><div class="faq-q">❓ {q}</div><div class="faq-a">{a}</div></div>' for q,a in Q)
    return S(W(f'<div class="faq-wrap"><h2>Preguntas Frecuentes</h2>{items}</div>'))

def h_cta_final():
    return """<div class="cta-final">
  <h2>Porque vos sí cuidás lo tuyo.</h2>
  <p>Tu vehículo merece verse impecable — como reflejo de quién sos. Garantía 30 días. Pagás solo al recibir.</p>
  <a href="#" class="btn-big">✅ QUIERO MI VEHÍCULO IMPECABLE — PAGAR AL RECIBIR</a>
  <div class="sub-cta">Sin tarjeta · Sin riesgo · Envío gratis a toda Guatemala 🇬🇹</div>
</div>"""

def h_footer():
    return '<div class="r2r-footer">Generado con <span>ROOKIE 2 RICHES — EGS Framework 2026</span> · OilShield™ Guatemala · Ángulo: Autorrealización</div>'

# ── BENEFICIOS EXPANDIDOS (ángulo autorrealización)
B1 = bexp(1,"Tu Carro Refleja Quién Sos","No es vanidad — es identidad.",
    "Para un hombre que lleva años cuidando lo que es suyo, un parabrisas con aceite y mugre no es un detalle menor. Es una señal de descuido que no va con vos.",
    ["<strong>Pon el foco en el cliente:</strong> Vos no descuidás las cosas importantes en tu vida.",
     "<strong>Diferencia clara:</strong> El lavadero limpia lo que se ve. OilShield™ elimina lo que realmente ensucia.",
     "<strong>Conecta emocionalmente:</strong> Tu carro impecable es el reflejo de la persona que sos."],
    "🏆")
B2 = bexp(2,"Resultado de Detailer Sin Salir de Casa","El mismo acabado profesional — en 5 minutos, desde tu cochera.",
    "Un detailer profesional te cobra entre Q200 y Q400 por un resultado que dura 3 días. Con OilShield™ pagás Q249 una sola vez y obtenés el mismo acabado por semanas.",
    ["<strong>Pon el foco en el cliente:</strong> Tu tiempo y tu pisto valen. No los regales.",
     "<strong>Diferencia clara:</strong> Tecnología nano-molecular vs. champú y agua.",
     "<strong>Conecta emocionalmente:</strong> La satisfacción de hacer bien el trabajo — sin depender de nadie."],
    "💎", reverse=True)
B3 = bexp(3,"Seguridad Para los Tuyos","Parabrisas cristalino = manejás sin preocupaciones.",
    "El aceite en el parabrisas crea reflejos peligrosos de noche y con lluvia. Como padre de familia, llevar a los tuyos en el carro es una responsabilidad. OilShield™ elimina ese riesgo.",
    ["<strong>Pon el foco en el cliente:</strong> No es solo estética. Es seguridad real.",
     "<strong>Diferencia clara:</strong> El lavadero no elimina el aceite molecular. OilShield™ sí.",
     "<strong>Conecta emocionalmente:</strong> Tu familia en el carro. Con visión perfecta. Así debe ser."],
    "🛡️")
B4 = bexp(4,"Durabilidad que Respeta tu Tiempo","Aplicás una vez — tu carro sigue impecable por semanas.",
    "Semanas sin volver a preocuparte por el parabrisas. La capa nano-molecular que deja OilShield™ repele aceite, agua y polvo hasta 6 semanas.",
    ["<strong>Pon el foco en el cliente:</strong> Tu tiempo es tuyo. No lo gastes en el lavadero cada semana.",
     "<strong>Diferencia clara:</strong> Lavadero = 3-5 días. OilShield™ = 3-6 semanas.",
     "<strong>Conecta emocionalmente:</strong> Más tiempo para vos, para tu familia, para lo que importa."],
    "⏱️", reverse=True)
B5 = bexp(5,"Fácil de Usar — Ahí Mismo en tu Casa","Sin equipo especial. Sin cita. Sin cola. Sin esperar.",
    "Vos podés hacerlo solo, en tu cochera, en 5 minutos. El kit incluye todo lo que necesitás. Si podés limpiar con un paño, podés usar OilShield™.",
    ["<strong>Pon el foco en el cliente:</strong> Sos perfectamente capaz de hacer esto solo.",
     "<strong>Diferencia clara:</strong> Sin curva de aprendizaje. Primer uso = resultado perfecto.",
     "<strong>Conecta emocionalmente:</strong> La satisfacción de hacerlo vos mismo — y que quede mejor que en el lavadero."],
    "🎯")
B6 = bexp(6,"Cero Riesgo — Garantía Total","Pagás solo al recibir. Si no te convence, devolvemos tu pisto.",
    "No existe ningún riesgo para vos. El mensajero llega, entregás el producto en tus manos, lo inspeccionás y pagás. Y si en 30 días no ves el resultado, te devolvemos el pisto.",
    ["<strong>Pon el foco en el cliente:</strong> El riesgo lo asumimos nosotros — no vos.",
     "<strong>Diferencia clara:</strong> Pago contra entrega + garantía real de devolución.",
     "<strong>Conecta emocionalmente:</strong> Comprá con la confianza que te merecés."],
    "🛡️", reverse=True)

def build():
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    body = (h_header() + h_topbar() + h_hero() + h_garantias() +
            h_transformacion() + h_autoridad() + h_beneficios() +
            B1 + B2 + B3 + B4 + B5 + B6 +
            h_como_usarlo() + h_caracteristicas() +
            h_comparativa() + h_testimonios() +
            h_incluye() + h_logistica() + h_oferta() +
            h_faq() + h_cta_final() + h_footer())
    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width,initial-scale=1.0">
  <title>OilShield™ Guatemala — Tu Vehículo Impecable | ROOKIE2RICHES</title>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;900&family=Outfit:wght@400;600;700;900&display=swap" rel="stylesheet">
  <style>{CSS}</style>
</head>
<body>{body}</body>
</html>"""
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅ Landing autorrealización generada: {OUT}")

if __name__ == "__main__":
    build()
