#!/usr/bin/env python3
"""
generate_rejuvenecimiento.py — OilShield™ GT
Ángulo: Rejuvenecimiento — "Dale nueva vida a tu vehículo"
Avatar: Conductores 35-65 que sienten su carro "envejecido" y quieren devolverle la juventud.
Skills: ecom-copywriter (PAS/PRESTO) + ecom-cro-expert (CRO structure)
"""
import os, sys

OUT = os.path.join(os.path.dirname(__file__), "..", "..",  "Arquitecto de landing",
                   "angulo_rejuvenecimiento_oilshield_gt.html")

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
.gbar { background:#f0ece8; display:flex; justify-content:center; align-items:center; gap:36px; padding:24px 40px; flex-wrap:wrap; }
.gitem { display:flex; align-items:center; gap:12px; }
.gico { width:52px; height:52px; border-radius:50%; border:3px solid #7B1818; display:flex; align-items:center; justify-content:center; font-size:1.3rem; background:#fff; }
.gtxt strong { display:block; font-size:.78rem; font-weight:900; text-transform:uppercase; }
.gtxt span { font-size:.74rem; color:#555; max-width:150px; display:block; }
.logos-bar { background:#fff; padding:26px 40px; display:flex; justify-content:center; align-items:center; gap:50px; flex-wrap:wrap; border-top:1px solid #e5e5e5; }
.logo-b { font-size:1.3rem; font-weight:900; color:#333; opacity:.6; }
.transf-hd { text-align:center; padding:40px 40px 10px; }
.transf-hd h2 { font-size:1.35rem; font-weight:900; text-transform:uppercase; letter-spacing:2px; }
.transf-hd p { color:#555; font-size:.92rem; margin-top:8px; max-width:600px; margin-left:auto; margin-right:auto; }
.steps { display:grid; grid-template-columns:repeat(3,1fr); gap:24px; padding:28px 40px; }
.step { text-align:center; }
.step-lbl { font-size:.68rem; font-weight:900; letter-spacing:3px; color:#7B1818; text-transform:uppercase; margin-bottom:10px; }
.step-img { width:100%; aspect-ratio:1.2; background:linear-gradient(135deg,#fdf6f0,#f5e0cc); border-radius:12px; margin-bottom:12px; display:flex; align-items:center; justify-content:center; font-size:3rem; border:2px solid #e8d0bc; }
.step p { font-size:.83rem; color:#444; }
.auth-grid { display:grid; grid-template-columns:1fr 1fr; min-height:360px; }
.auth-img { background:linear-gradient(135deg,#f5f0ee,#ede0d8); display:flex; align-items:center; justify-content:center; font-size:6rem; padding:40px; }
.auth-copy { padding:40px; display:flex; flex-direction:column; justify-content:center; }
.auth-copy h2 { font-size:1.4rem; font-weight:900; margin-bottom:14px; }
.auth-copy p { font-size:.88rem; color:#444; margin-bottom:14px; }
.auth-dot { display:flex; align-items:flex-start; gap:10px; margin-bottom:10px; font-size:.86rem; }
.dot { width:8px; height:8px; border-radius:50%; background:#7B1818; flex-shrink:0; margin-top:6px; }
.benef-hd { text-align:center; padding:40px 40px 20px; }
.benef-hd h2 { font-size:1.5rem; font-weight:900; }
.benef-hd p { font-size:.9rem; color:#555; margin-top:8px; }
.benef-3col { display:grid; grid-template-columns:1fr auto 1fr; gap:16px; padding:0 40px 30px; align-items:center; }
.bc { background:#faf7f5; border-radius:10px; padding:18px 22px; border-left:4px solid #7B1818; margin-bottom:14px; }
.bc h3 { font-size:.92rem; font-weight:900; margin-bottom:5px; }
.bc p { font-size:.8rem; color:#555; }
.bc-center { display:flex; align-items:center; justify-content:center; padding:20px; }
.bc-img { width:200px; height:200px; background:linear-gradient(135deg,#fdf6f0,#f5e0cc); border-radius:16px; display:flex; align-items:center; justify-content:center; font-size:5rem; box-shadow:0 4px 20px rgba(0,0,0,.1); }
.bexp { display:grid; grid-template-columns:1fr 1fr; min-height:340px; }
.bexp-img { display:flex; align-items:center; justify-content:center; font-size:6rem; padding:40px; }
.bexp-copy { padding:40px; display:flex; flex-direction:column; justify-content:center; }
.bexp-copy h2 { font-size:1.35rem; font-weight:900; margin-bottom:10px; }
.bexp-copy .sub { color:#7B1818; font-weight:700; font-size:.9rem; margin-bottom:12px; }
.bexp-copy p { font-size:.86rem; color:#444; margin-bottom:10px; }
.bexp-copy ul { list-style:none; }
.bexp-copy ul li { display:flex; gap:10px; margin-bottom:8px; font-size:.85rem; }
.bexp-copy ul li::before { content:"●"; color:#7B1818; flex-shrink:0; }
.paso-row { display:flex; gap:16px; align-items:flex-start; margin-bottom:16px; }
.paso-num { min-width:36px; height:36px; background:#7B1818; color:#fff; border-radius:50%; display:flex; align-items:center; justify-content:center; font-weight:900; font-size:.82rem; flex-shrink:0; }
.paso-tit { font-weight:900; font-size:.9rem; margin-bottom:3px; }
.paso-txt { font-size:.82rem; color:#555; }
.tip-box { background:#fff8e1; padding:14px 16px; border-left:4px solid #f59e0b; border-radius:0 8px 8px 0; font-size:.83rem; color:#78350f; margin:0 40px 28px; }
.spec-row { display:flex; gap:18px; align-items:flex-start; padding:18px 22px; border-radius:10px; margin-bottom:12px; }
.spec-row:nth-child(odd) { background:#faf7f5; }
.spec-row:nth-child(even) { background:#f5f0ee; }
.spec-num { min-width:46px; height:46px; background:#7B1818; color:#fff; border-radius:8px; display:flex; align-items:center; justify-content:center; font-weight:900; font-size:.9rem; flex-shrink:0; }
.spec-tit { font-weight:900; font-size:.92rem; margin-bottom:4px; }
.spec-txt { font-size:.82rem; color:#555; line-height:1.6; }
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
.incl-grid { display:grid; grid-template-columns:1fr 1fr; min-height:360px; }
.incl-img { background:linear-gradient(135deg,#f0fff4,#dcfce7); display:flex; align-items:center; justify-content:center; font-size:6rem; padding:40px; }
.incl-copy { padding:40px; display:flex; flex-direction:column; justify-content:center; }
.incl-copy h2 { font-size:1.35rem; font-weight:900; margin-bottom:18px; }
.num-list { list-style:none; }
.num-list li { display:flex; align-items:center; gap:16px; margin-bottom:12px; font-size:.88rem; font-weight:600; }
.nb { min-width:42px; height:42px; background:#7B1818; color:#fff; border-radius:6px; display:flex; align-items:center; justify-content:center; font-weight:900; font-size:.88rem; flex-shrink:0; }
.logis { text-align:center; padding:40px; background:#f9f5f2; }
.logis h2 { font-size:1.25rem; font-weight:900; margin-bottom:8px; }
.logis p { font-size:.88rem; color:#444; margin-bottom:24px; max-width:560px; margin-left:auto; margin-right:auto; }
.carriers { display:flex; justify-content:center; align-items:center; gap:36px; flex-wrap:wrap; }
.carrier { width:90px; height:46px; background:#fff; border-radius:8px; border:1px solid #ddd; display:flex; align-items:center; justify-content:center; font-weight:900; font-size:.85rem; }
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
.faq-wrap { padding:40px; }
.faq-wrap h2 { font-size:1.25rem; font-weight:900; margin-bottom:22px; text-align:center; }
.faq-item { border-bottom:1px solid #e5e5e5; padding:14px 0; }
.faq-q { font-weight:800; font-size:.9rem; margin-bottom:5px; }
.faq-a { font-size:.83rem; color:#555; }
.cta-final { background:#1a1a1a; color:#fff; text-align:center; padding:50px 40px; }
.cta-final h2 { font-size:1.55rem; font-weight:900; margin-bottom:10px; }
.cta-final p { color:#aaa; font-size:.88rem; margin-bottom:26px; }
.btn-big { display:inline-block; background:#7B1818; color:#fff; padding:18px 44px; border-radius:8px; font-weight:900; font-size:.95rem; letter-spacing:2px; text-transform:uppercase; }
.sub-cta { margin-top:12px; font-size:.78rem; color:#888; }
.cta-inline { text-align:center; padding:22px 40px; background:#f9f5f2; }
.btn-in { display:inline-block; background:#1a1a1a; color:#fff; padding:13px 34px; border-radius:6px; font-weight:900; font-size:.8rem; letter-spacing:2px; text-transform:uppercase; }
.btn-in span { display:block; font-size:.62rem; color:#aaa; margin-top:2px; font-weight:400; }
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
def CTA_INLINE(): return '<div class="cta-inline"><a href="#" class="btn-in">REJUVENECER MI VEHÍCULO AHORA<span>Pagás solo cuando el mensajero llega</span></a></div>'

def h_header():
    return """<header class="r2r-header">
  <div class="r2r-logo">ROOKIE <span>2</span> RICHES</div>
  <div class="r2r-handle">@ecomjuliann</div>
</header>
<div class="sec-bar">ESTRUCTURA DE VENTAS — ÁNGULO REJUVENECIMIENTO</div>"""

def h_topbar():
    return S('<div class="top-bar">🚗 Envío GRATIS a toda Guatemala &nbsp;|&nbsp; Dale nueva vida a tu vehículo — Pagás Solo al Recibir 🔒</div>')

def h_hero():
    return S(W("""<div class="hero-grid">
  <div class="hero-img-col">
    <div class="main-img">🔄</div>
    <div class="thumbs">
      <div class="thumb active">🔄</div>
      <div class="thumb">✨</div>
      <div class="thumb">🚗</div>
      <div class="thumb">🆕</div>
    </div>
  </div>
  <div class="hero-copy">
    <div class="hero-stars">★★★★★</div>
    <div class="hero-reviews">+3,800 conductores que rejuvenecieron su parabrisas en minutos</div>
    <h1 class="hero-h1">Tu carro no está viejo. Tu parabrisas sí. Devolvele la juventud en 5 minutos.</h1>
    <div class="hero-sub">OilShield™ elimina años de aceite incrustado y devuelve a tu cristal la transparencia del día 1.</div>
    <div style="margin-bottom:16px;">
      <div class="price-old">PRECIO NORMAL: Q350</div>
      <span class="price-new">Q249</span><span class="badge-off">29% OFF</span>
    </div>
    <div class="prod-name">OilShield™ — Rejuvenecedor Nano-Molecular de Cristales</div>
    <ul class="checks">
      <li><span class="chk">✔</span> Eliminá años de película de aceite en una sola aplicación</li>
      <li><span class="chk">✔</span> Tu parabrisas vuelve a verse como el día que compraste el carro</li>
      <li><span class="chk">✔</span> Tecnología nano-molecular — no es un limpiador genérico</li>
      <li><span class="chk">✔</span> Resultado que dura semanas, no días</li>
    </ul>
    <div class="hero-test">"Mi Hilux tiene 12 años pero el parabrisas se ve como si fuera de agencia. Increíble la diferencia." — Don Carlos M., 58 años, Mixco ✅ Comprador verificado</div>
    <button class="btn-cta">REJUVENECER MI VEHÍCULO — PAGAR AL RECIBIR<span>Pagás solo cuando el mensajero llega a tu puerta</span></button>
  </div>
</div>"""))

def h_garantias():
    return S(W("""<div class="gbar">
  <div class="gitem"><div class="gico">🛡️</div><div class="gtxt"><strong>GARANTÍA 30 DÍAS</strong><span>Resultado visible o devolvemos tu pisto. Sin preguntas.</span></div></div>
  <div class="gitem"><div class="gico">🚚</div><div class="gtxt"><strong>ENVÍO GRATIS</strong><span>A toda Guatemala. Pagás solo al recibir.</span></div></div>
  <div class="gitem"><div class="gico">🔄</div><div class="gtxt"><strong>REJUVENECIMIENTO TOTAL</strong><span>Años de aceite eliminados en 5 minutos.</span></div></div>
</div>
<div class="logos-bar">
  <div class="logo-b">VOGUE</div><div class="logo-b">USA TODAY</div><div class="logo-b">CBS</div><div class="logo-b">abc</div>
</div>"""))

def h_transformacion():
    return S(W(f"""<div class="transf-hd">
  <h2>De "Ya Está Viejo" a "¡Parece Recién Salido de Agencia!"</h2>
  <p>No necesitás un carro nuevo. Solo necesitás OilShield™. Mirá la transformación en 3 pasos simples.</p>
</div>
<div class="steps">
  <div class="step"><div class="step-lbl">ANTES</div><div class="step-img">😰</div><p><strong>Años de aceite acumulado</strong> — una película amarillenta e invisible que opaca el cristal y lo hace ver viejo y descuidado.</p></div>
  <div class="step"><div class="step-lbl">DURANTE</div><div class="step-img">🔄</div><p><strong>OilShield™ penetra y disuelve</strong> — la fórmula nano-molecular levanta cada capa de aceite incrustado que el jabón nunca pudo tocar.</p></div>
  <div class="step"><div class="step-lbl">DESPUÉS</div><div class="step-img">✨</div><p><strong>Cristal rejuvenecido</strong> — transparente, brillante y como nuevo. La misma claridad del día que lo compraste.</p></div>
</div>
{CTA_INLINE()}"""))

def h_autoridad():
    return S(BAR("La Ciencia del Rejuvenecimiento","1rem") + W("""<div class="auth-grid">
  <div class="auth-img">🔬</div>
  <div class="auth-copy">
    <h2>¿Por qué tu parabrisas se ve "viejo" aunque lo lavés cada semana?</h2>
    <p>No es la edad del carro. Es una capa invisible de aceite molecular que se acumula con el tiempo — del asfalto, de los camiones, del limpiaparabrisas. El agua y el jabón no la pueden tocar.</p>
    <p><strong>OilShield™ usa tecnología nano-molecular</strong> para penetrar esa capa envejecida y disolverla desde adentro. Es como quitarle 10 años a tu parabrisas en 5 minutos.</p>
    <div class="auth-dot"><div class="dot"></div><span>El 92% de los parabrisas con más de 3 años tienen capas de aceite invisible que ningún lavado convencional elimina.</span></div>
    <div class="auth-dot"><div class="dot"></div><span>La película de aceite reduce la transmisión de luz hasta un 35% — tu cristal se ve opaco sin que te des cuenta.</span></div>
    <div class="auth-dot"><div class="dot"></div><span>+3,800 conductores guatemaltecos ya rejuvenecieron sus cristales con OilShield™.</span></div>
  </div>
</div>"""))

def h_beneficios():
    return S(f"""<div style="background:#f9f5f2;">
{W(f'''<div class="benef-hd">
  <h2>Rejuvenecé tu vehículo sin gastar una fortuna</h2>
  <p>No necesitás pintar, pulir ni cambiar nada. Solo una aplicación para que tu cristal vuelva a verse como nuevo.</p>
</div>
<div class="benef-3col">
  <div>
    <div class="bc"><h3>Beneficio 1: Años de Aceite — Fuera</h3><p>Una sola aplicación disuelve la película que lleva años pegada a tu parabrisas. El resultado es inmediato y visible desde el primer uso.</p></div>
    <div class="bc"><h3>Beneficio 2: Transparencia de Agencia</h3><p>Tu cristal recupera la claridad del día 1. La diferencia es tan notoria que tus pasajeros van a comentarlo.</p></div>
    <div class="bc"><h3>Beneficio 3: Seguridad Renovada</h3><p>Un parabrisas sin aceite = visión nocturna perfecta. Ves más, ves mejor, manejás más seguro.</p></div>
  </div>
  <div class="bc-center"><div class="bc-img">🔄</div></div>
  <div>
    <div class="bc"><h3>Beneficio 4: Duración Real</h3><p>No es una limpieza que dura 2 días. OilShield™ deja una capa protectora que mantiene el resultado por semanas.</p></div>
    <div class="bc"><h3>Beneficio 5: Sin Complicaciones</h3><p>5 minutos en tu cochera. Sin cita, sin espera, sin equipo especial. Vos mismo lo hacés.</p></div>
    <div class="bc"><h3>Beneficio 6: Cero Riesgo</h3><p>Garantía 30 días + pago contra entrega. Si no ves el rejuvenecimiento, devolvemos tu pisto.</p></div>
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
        ("01","Limpiá el polvo grueso del parabrisas","Pasá un paño seco. El cristal debe estar seco y a temperatura ambiente."),
        ("02","Aplicá 3-4 sprays de OilShield™","Rociá sobre el cristal y cubrí todo el parabrisas, especialmente donde se ve más opaco."),
        ("03","Frotá con la esponja en movimientos circulares","2 minutos. Sentís cómo la fórmula levanta años de aceite incrustado."),
        ("04","Pasá un paño seco y contemplá el resultado","Cristal rejuvenecido — como recién salido de agencia. Resultado dura 3-6 semanas."),
    ]
    ps = "".join(f"""<div class="paso-row"><div class="paso-num">{n}</div><div><div class="paso-tit">{t}</div><div class="paso-txt">{d}</div></div></div>""" for n,t,d in pasos)
    return S(BAR("¿Cómo Debo Usarlo?","1rem") + W(f"""<div class="bexp">
  <div class="bexp-img" style="background:linear-gradient(135deg,#fdf6f0,#f5e0cc);">
    <div style="text-align:center;"><div style="font-size:4rem;margin-bottom:10px;">🔄</div><div style="font-size:.7rem;font-weight:900;color:#7B1818;letter-spacing:2px;text-transform:uppercase;">MODO DE USO</div></div>
  </div>
  <div class="bexp-copy">
    <h2>Aplicación en 4 Pasos — Rejuvenecimiento Inmediato</h2>
    <div class="sub">De viejo a nuevo en 5 minutos — sin experiencia previa.</div>
    <div style="margin-top:8px;">{ps}</div>
  </div>
</div>
<div class="tip-box"><strong>💡 TIP:</strong> Aplicá de noche o en sombra. El calor del sol puede secar el producto antes de que penetre.</div>
{CTA_INLINE()}"""))

def h_caracteristicas():
    specs = [
        ("01","Fórmula Nano-Molecular Profesional","Penetra microporos del vidrio y disuelve aceite molecular invisible. La misma tecnología de detailing profesional."),
        ("02","8-12 Aplicaciones por Frasco","Rinde 3-6 meses. Equivale a 32-48 lavadas en lavadero convencional."),
        ("03","Resultado en 5 Minutos","Fórmula de activación inmediata. Desde el primer contacto se nota la diferencia."),
        ("04","Compatible con Todo Vehículo","Carros, pick-ups, SUVs. Vidrio templado, laminado y tintado. No daña sellos ni carrocería."),
        ("05","pH Neutro — Seguro para Tintes","Sin amoniaco, sin solventes agresivos. Apto para ventanas con polarizado."),
        ("06","Efecto Hidrofóbico Post-Limpieza","Capa que repele agua y polvo por semanas. Tu parabrisas se mantiene joven más tiempo."),
    ]
    rows = "".join(f"""<div class="spec-row"><div class="spec-num">{n}</div><div><div class="spec-tit">{t}</div><div class="spec-txt">{d}</div></div></div>""" for n,t,d in specs)
    return S(f"""<div style="background:#f9f5f2;">{W(f'''<div style="padding:40px 40px 20px;">
  <h2 style="font-size:1.35rem;font-weight:900;margin-bottom:8px;">Características Técnicas</h2>
  <p style="font-size:.88rem;color:#555;">La ciencia detrás del rejuvenecimiento de tu parabrisas.</p>
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
        emoji = "🔄" if winner else ("🚿" if "Lavadero" in titulo else "🧴")
        return f'<div class="comp-col{wc}"><div class="comp-hd">{titulo}</div><div class="comp-body">{rows}</div><div class="comp-img">{emoji}</div></div>'
    lavadero = col("Lavadero / Detailer", [(False,"Q200-Q400 cada vez"),(False,"No rejuvenece — solo limpia la superficie"),(False,"3-5 días de resultado"),(False,"No elimina aceite molecular"),(False,"1-2 horas de espera")], False)
    oilshield = col("OilShield™", [(True,"Q249 una sola vez"),(True,"Rejuvenecimiento real — disuelve aceite incrustado"),(True,"3-6 semanas de resultado"),(True,"Fórmula nano-molecular"),(True,"5 minutos en tu casa")], True)
    otros = col("Otros Limpiadores", [(False,"Precio similar"),(False,"Limpieza superficial — no rejuvenece"),(False,"Duración mínima"),(False,"Formulación genérica"),(False,"Múltiples pasadas necesarias")], False)
    return S(f"""<div style="background:#f9f5f2;">
{BAR("¿Por Qué OilShield™ Rejuvenece y los Demás No?","1rem")}
{W(f'<div class="comp-grid">{lavadero}{oilshield}{otros}</div>{CTA_INLINE()}')}
</div>""")

def h_testimonios():
    T = [
        ("👴","Don Carlos M.","Mixco, 58 años","«Mi Hilux tiene 12 años. Pensé que el parabrisas ya estaba gastado. Una pasada de OilShield™ y se ve como de agencia.»"),
        ("👩","Doña María R.","Villa Nueva, 48 años","«Mi carro tiene 8 años y el cristal se veía amarillento. Ahora manejo de noche y veo perfecto. ¡Volvió a nacer!»"),
        ("👨","Roberto A.","Antigua Guatemala, 51 años","«Probé vinagre, alcohol, limpiadores de supermercado. Nada se compara. OilShield™ le quitó 10 años al parabrisas.»"),
        ("🧔","Mauricio L.","Cobán, 47 años","«Mi esposa me dijo: '¿Le cambiaste el parabrisas?' No, señora. Solo OilShield™.»"),
        ("👩","Sofía T.","Zona 14, 34 años","«Mi CX-5 ya no se veía premium con el cristal opaco. Una aplicación y volvió a verse de lujo.»"),
        ("👴","Don Jorge F.","Escuintla, 62 años","«Conduzco 300 km/semana. El aceite de la carretera destruía mi visibilidad. OilShield™ rejuveneció todo.»"),
    ]
    cards = "".join(f'<div class="tc"><div class="tc-img">{av}</div><div class="tc-text">"{txt}"</div><div class="tc-stars">★★★★★</div><div class="tc-auth"><div class="tc-av">{av}</div><div><div class="tc-nm">{nm}</div><div class="tc-loc">{loc} ✅ Comprador verificado</div></div></div></div>' for av,nm,loc,txt in T)
    return S(W(f'<div class="test-hd"><h2>Ellos Rejuvenecieron su Parabrisas — Ahora es tu Turno</h2></div><div class="test-grid">{cards}</div>'))

def h_incluye():
    items = [("01","1 frasco OilShield™ (fórmula nano-molecular)"),("02","1 esponja aplicadora de alta densidad"),("03","Guía de rejuvenecimiento paso a paso"),("04","Envío GRATIS a toda Guatemala"),("05","Pago contra entrega — sin tarjeta"),("06","Garantía 30 días sin preguntas")]
    li = "".join(f'<li><div class="nb">{n}</div>{t}</li>' for n,t in items)
    return S(f"""<div style="background:#f9f5f2;">{W(f'<div class="incl-grid"><div class="incl-img">📦</div><div class="incl-copy"><h2>¿Qué Incluye tu Kit de Rejuvenecimiento?</h2><ul class="num-list">{li}</ul></div></div>')}</div>""")

def h_logistica():
    return S(W("""<div class="logis">
  <h2>¿Cómo Recibís Tu Pedido?</h2>
  <p>Principales transportadoras de Guatemala. <strong>Pagás solo cuando el mensajero llega.</strong> Sin tarjeta, sin riesgo.</p>
  <div class="carriers">
    <div class="carrier" style="color:#4d148c;">FedEx</div>
    <div class="carrier" style="color:#d40511;">DHL</div>
    <div class="carrier" style="color:#351c15;">UPS</div>
    <div class="carrier" style="background:#1a1a1a;color:#fff;">GUATEX</div>
  </div>
</div>"""))

def h_oferta():
    return S(W(f"""<div class="oferta-hd"><h2>Elegí Tu Kit de Rejuvenecimiento</h2></div>
<div class="oferta-grid">
  <div class="oc"><div class="oc-hd"><h3>BÁSICO</h3></div><div class="oc-body"><div class="oc-p">Q249</div><div class="oc-old">Antes Q350</div><ul><li>1 frasco OilShield™</li><li>1 esponja aplicadora</li><li>Envío GRATIS</li><li>Garantía 30 días</li></ul><a href="#" class="oc-btn">REJUVENECER AHORA</a></div></div>
  <div class="oc best"><div class="oc-hd"><h3>FAMILIAR</h3><div class="best-tag">⭐ MÁS POPULAR</div></div><div class="oc-body"><div class="oc-p" style="color:#7B1818;">Q399</div><div class="oc-old">2 frascos — Antes Q700</div><ul><li>2 frascos OilShield™</li><li>2 esponjas aplicadoras</li><li>Envío GRATIS prioritario</li><li>Garantía 30 días extendida</li><li>1 paño microfibra premium GRATIS</li></ul><a href="#" class="oc-btn">APROVECHAR OFERTA</a></div></div>
  <div class="oc"><div class="oc-hd"><h3>FLOTA</h3></div><div class="oc-body"><div class="oc-p">Q549</div><div class="oc-old">3 frascos — Antes Q1,050</div><ul><li>3 frascos OilShield™</li><li>Kit completo de aplicación</li><li>Envío GRATIS express</li><li>Garantía 60 días</li></ul><a href="#" class="oc-btn">COMPRAR AHORA</a></div></div>
</div>{CTA_INLINE()}"""))

def h_faq():
    Q = [
        ("¿Funciona en parabrisas viejos con años de aceite?","Sí — especialmente en esos. OilShield™ fue diseñado para rejuvenecer cristales con años de acumulación. En casos severos puede necesitar 2 pasadas."),
        ("¿Cómo funciona el pago contra entrega?","El mensajero llega a tu puerta. Inspeccionás el producto y pagás. Sin tarjeta, sin transferencia, sin riesgo."),
        ("¿Cuánto tarda el envío?","Capital: 1-2 días hábiles. Resto del país: 2-4 días. Envío GRATIS a toda Guatemala."),
        ("¿Es seguro para mi parabrisas?","100% seguro. pH neutro, sin amoniaco. Compatible con vidrios templados, laminados y tintados."),
        ("¿Cuánto dura el efecto rejuvenecedor?","3-6 semanas. La capa protectora repele aceite nuevo y mantiene el cristal joven más tiempo."),
        ("¿Qué pasa si no me convence?","Garantía 30 días sin preguntas. Te devolvemos tu pisto completo."),
    ]
    items = "".join(f'<div class="faq-item"><div class="faq-q">❓ {q}</div><div class="faq-a">{a}</div></div>' for q,a in Q)
    return S(W(f'<div class="faq-wrap"><h2>Preguntas Frecuentes</h2>{items}</div>'))

def h_cta_final():
    return """<div class="cta-final">
  <h2>Tu carro no necesita cambiar. Solo tu parabrisas necesita rejuvenecer.</h2>
  <p>Una aplicación. 5 minutos. Años de aceite — eliminados. Garantía 30 días. Pagás solo al recibir.</p>
  <a href="#" class="btn-big">✅ REJUVENECER MI VEHÍCULO — PAGAR AL RECIBIR</a>
  <div class="sub-cta">Sin tarjeta · Sin riesgo · Envío gratis a toda Guatemala 🇬🇹</div>
</div>"""

def h_footer():
    return '<div class="r2r-footer">Generado con <span>ROOKIE 2 RICHES — EGS Framework 2026</span> · OilShield™ Guatemala · Ángulo: Rejuvenecimiento</div>'

B1 = bexp(1,"Quitale 10 Años a tu Parabrisas","No es magia — es nano-tecnología.",
    "Cada año de uso agrega una capa invisible de aceite a tu cristal. OilShield™ las disuelve todas de una vez. 5 minutos y tu parabrisas vuelve a verse como el día 1.",
    ["<strong>Rejuvenecimiento real:</strong> No es una limpieza superficial. Penetra y elimina capas acumuladas.",
     "<strong>Resultado visible:</strong> La diferencia es tan notoria que tus pasajeros lo van a notar.",
     "<strong>Efecto duradero:</strong> La capa protectora previene re-acumulación por semanas."],
    "🔄")
B2 = bexp(2,"Tu Carro Merece Verse Joven","No dejés que el parabrisas envejezca tu vehículo.",
    "Un cristal opaco hace que hasta un carro del año se vea descuidado. OilShield™ devuelve esa transparencia cristalina que hace que tu vehículo se vea premium — sin importar el año.",
    ["<strong>Primera impresión:</strong> Un parabrisas cristalino cambia toda la percepción del carro.",
     "<strong>Valor percibido:</strong> Tu vehículo se ve más nuevo, más cuidado, más valioso.",
     "<strong>Orgullo renovado:</strong> Volvés a sentir ese orgullo de cuando lo compraste."],
    "✨", reverse=True)
B3 = bexp(3,"Visión Nocturna Restaurada","Eliminá los reflejos que te ciegan de noche.",
    "El aceite en el cristal crea reflejos peligrosos con las luces de otros carros. Al rejuvenecer tu parabrisas, OilShield™ elimina esos reflejos y recuperás la visión nocturna completa.",
    ["<strong>Seguridad real:</strong> 72% de accidentes nocturnos por mala visibilidad — no seas parte de esa estadística.",
     "<strong>Visión clara de noche:</strong> Las luces ya no te ciegan. Los reflejos desaparecen.",
     "<strong>Manejá con confianza:</strong> Especialmente en temporada de lluvia."],
    "🌙")
B4 = bexp(4,"Resultado que Dura Semanas","Aplicás una vez — tu carro sigue rejuvenecido.",
    "La capa nano-molecular que deja OilShield™ repele aceite nuevo, agua y polvo por semanas. Tu parabrisas no solo se ve nuevo — se mantiene nuevo.",
    ["<strong>Protección activa:</strong> La capa hidrofóbica previene re-acumulación de aceite.",
     "<strong>Ahorro de tiempo:</strong> No necesitás lavar el parabrisas cada semana.",
     "<strong>Economía inteligente:</strong> 1 frasco = 8-12 aplicaciones = meses de parabrisas joven."],
    "⏱️", reverse=True)
B5 = bexp(5,"Fácil — Vos Mismo Lo Hacés","Sin equipo especial. Sin cita. Sin salir de tu casa.",
    "Si podés limpiar un cristal con un paño, podés rejuvenecer tu parabrisas con OilShield™. El kit incluye todo. 5 minutos en tu cochera.",
    ["<strong>Sin curva de aprendizaje:</strong> Primer uso = resultado perfecto.",
     "<strong>Kit completo:</strong> Frasco + esponja + guía paso a paso.",
     "<strong>La satisfacción de hacerlo solo:</strong> Sin depender de nadie."],
    "🎯")
B6 = bexp(6,"Cero Riesgo — Garantía Total","Si no rejuvenece, devolvemos tu pisto.",
    "Pagás al recibir. Si en 30 días no ves la transformación prometida, devolvemos tu dinero completo. El riesgo lo asumimos nosotros.",
    ["<strong>Pago contra entrega:</strong> Sin tarjeta, sin transferencia.",
     "<strong>Garantía real:</strong> 30 días sin preguntas ni complicaciones.",
     "<strong>Confianza total:</strong> +3,800 conductores ya lo comprobaron."],
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
  <title>OilShield™ Guatemala — Rejuvenecer Mi Vehículo | ROOKIE2RICHES</title>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;900&family=Outfit:wght@400;600;700;900&display=swap" rel="stylesheet">
  <style>{CSS}</style>
</head>
<body>{body}</body>
</html>"""
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅ Landing rejuvenecimiento generada: {OUT}")

if __name__ == "__main__":
    build()
