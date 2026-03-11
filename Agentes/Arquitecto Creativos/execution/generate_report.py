#!/usr/bin/env python3
"""
generate_report.py — EGS Framework
Genera el HTML ROOKIE2RICHES al estilo visual exacto del PDF:
fondo blanco/gris claro, barras rojo granate, tipografía negra bold.
"""

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "..", "..", "Arquitecto de landing")

# ─────────────────────────────────────────────
# COPIES OILSHIELD™ GUATEMALA
# ─────────────────────────────────────────────
DATA = {
    "producto": "OilShield™",
    "pais": "Guatemala",
    "bandera": "🇬🇹",
    "moneda": "Q",
    "precio_normal": "Q350",
    "precio_oferta": "Q249",
    "descuento": "29% OFF",
    "cta": "PAGAR AL RECIBIR — SIN TARJETA",
    "estrellas": "★★★★★",
    "reviews": "+3,800 conductores en Guatemala",
    "problema": "¿Cuánto pisto estás perdiendo cada mes por un parabrisas sucio?",
    "solucion": "OilShield™ elimina el aceite y la mugre en 5 minutos — resultado visible en la primera pasada.",
    "transformacion": "De parabrisas opaco y peligroso a cristalino en una sola aplicación.",
    "beneficio_principal": "Visión cristalina en 5 minutos. Ahorrás más de Q1,200 al año.",
    "testimonio_hero": '"Ya llevo 3 meses sin ir al lavadero. La loca yo pensé que era mentira." — María R., Guatemala City ✅ Compradora verificada',
}

# ─────────────────────────────────────────────
# CSS ESTILO PDF: blanco + rojo granate
# ─────────────────────────────────────────────
CSS = """
* { box-sizing: border-box; margin: 0; padding: 0; user-select: text !important; -webkit-user-select: text !important; }
body {
  font-family: 'Montserrat', 'Outfit', sans-serif;
  background: #f5f5f5;
  -webkit-user-select: text;
  user-select: text;
  color: #1a1a1a;
  line-height: 1.6;
}
a { text-decoration: none; }

/* HEADER */
.r2r-header {
  background: #fff;
  padding: 28px 60px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 3px solid #8B1C1C;
}
.r2r-logo {
  font-size: 1.5rem;
  font-weight: 900;
  color: #8B1C1C;
  letter-spacing: -1px;
}
.r2r-logo span { color: #1a1a1a; }
.r2r-handle { font-size: .9rem; color: #8B1C1C; font-weight: 700; }

/* SECTION TITLE BAR */
.sec-bar {
  background: #8B1C1C;
  color: #fff;
  text-align: center;
  padding: 18px 40px;
  font-size: 1.4rem;
  font-weight: 900;
  letter-spacing: 4px;
  text-transform: uppercase;
}

/* WRAPPER */
.wrap { max-width: 960px; margin: 0 auto; }
.section { background: #fff; margin-bottom: 0; }
.section + .section { border-top: 1px solid #e5e5e5; }

/* TOPBAR */
.top-bar {
  background: #1a1a1a;
  color: #fff;
  text-align: center;
  padding: 10px 20px;
  font-size: .9rem;
  font-weight: 600;
  letter-spacing: .5px;
}

/* HERO */
.hero-wrap {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0;
  min-height: 560px;
}
.hero-img {
  background: #f0f0f0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 40px 30px;
  gap: 16px;
}
.hero-img .main-img {
  width: 100%; max-width: 320px;
  aspect-ratio: 1;
  background: linear-gradient(135deg,#d4e4ff,#bfd0f0);
  border-radius: 16px;
  display: flex; align-items: center; justify-content: center;
  font-size: 5rem;
  box-shadow: 0 8px 32px rgba(0,0,0,.15);
}
.hero-img .thumbs {
  display: flex; gap: 10px;
}
.thumb {
  width: 70px; height: 70px;
  background: linear-gradient(135deg,#e0eaff,#c8d8f8);
  border-radius: 10px;
  border: 2px solid #ddd;
  display: flex; align-items: center; justify-content: center;
  font-size: 1.4rem;
  cursor: pointer;
}
.thumb.active { border-color: #8B1C1C; }

.hero-copy { padding: 40px 36px; display: flex; flex-direction: column; justify-content: center; }
.hero-stars { color: #f59e0b; font-size: 1.1rem; margin-bottom: 4px; }
.hero-reviews { font-size: .8rem; color: #666; margin-bottom: 16px; font-weight: 600; }
.hero-h1 { font-size: 1.65rem; font-weight: 900; color: #1a1a1a; margin-bottom: 10px; line-height: 1.25; }
.hero-sol { color: #8B1C1C; font-weight: 700; font-size: 1rem; margin-bottom: 20px; }
.hero-price-old { font-size: 1rem; color: #999; text-decoration: line-through; }
.hero-price-new { font-size: 2rem; font-weight: 900; color: #1a1a1a; display: inline-block; margin-right: 10px; }
.off-badge {
  background: #8B1C1C; color: #fff;
  font-size: .75rem; font-weight: 900;
  padding: 4px 10px; border-radius: 4px;
  vertical-align: middle;
}
.hero-name { font-size: 1rem; font-weight: 900; text-transform: uppercase; margin: 18px 0 12px; }
.check-list { list-style: none; margin-bottom: 18px; }
.check-list li { display: flex; align-items: flex-start; gap: 10px; margin-bottom: 8px; font-size: .9rem; }
.chk { color: #8B1C1C; font-size: 1.1rem; flex-shrink: 0; }
.hero-testimonio {
  background: #f9f9f9; border-left: 4px solid #8B1C1C;
  padding: 12px 16px; border-radius: 0 8px 8px 0;
  font-size: .82rem; color: #444; font-style: italic;
  margin-bottom: 20px;
}
.btn-cta {
  display: block; width: 100%;
  background: #1a1a1a; color: #fff;
  text-align: center; padding: 16px;
  border-radius: 6px; font-weight: 900;
  font-size: .9rem; letter-spacing: 2px;
  text-transform: uppercase; cursor: pointer;
  border: none;
}
.btn-cta span { display: block; font-size: .7rem; font-weight: 400; letter-spacing: 1px; color: #aaa; margin-top: 2px; }

/* GARANTÍAS BAR */
.garantias-bar {
  background: #f0f0f0;
  display: flex; justify-content: center; align-items: center;
  gap: 40px; padding: 24px 40px;
  flex-wrap: wrap;
}
.garantia-item { display: flex; align-items: center; gap: 12px; }
.garantia-item .gico {
  width: 54px; height: 54px; border-radius: 50%;
  border: 3px solid #8B1C1C;
  display: flex; align-items: center; justify-content: center;
  font-size: 1.4rem; background: #fff;
}
.garantia-item .gtxt strong { display: block; font-size: .8rem; font-weight: 900; text-transform: uppercase; }
.garantia-item .gtxt span { font-size: .75rem; color: #555; max-width: 160px; display: block; }

/* LOGOS AUTORIDAD */
.logos-bar {
  background: #fff; padding: 30px 40px;
  display: flex; justify-content: center; align-items: center;
  gap: 50px; flex-wrap: wrap;
  border-top: 1px solid #e5e5e5;
}
.logo-brand { font-size: 1.4rem; font-weight: 900; color: #333; letter-spacing: -1px; opacity: .7; }

/* TRANSFORMACION */
.transf-header { text-align: center; padding: 40px 40px 10px; }
.transf-header h2 { font-size: 1.4rem; font-weight: 900; text-transform: uppercase; letter-spacing: 2px; }
.transf-header p { color: #555; font-size: .95rem; margin-top: 8px; max-width: 600px; margin-left: auto; margin-right: auto; }
.transf-steps {
  display: grid; grid-template-columns: repeat(3,1fr);
  gap: 24px; padding: 30px 40px;
}
.step-card { text-align: center; }
.step-label { font-size: .7rem; font-weight: 900; letter-spacing: 3px; color: #8B1C1C; text-transform: uppercase; margin-bottom: 10px; }
.step-img {
  width: 100%; aspect-ratio: 1.2;
  background: linear-gradient(135deg,#fff5f5,#fde0e0);
  border-radius: 12px; margin-bottom: 14px;
  display: flex; align-items: center; justify-content: center;
  font-size: 3rem; border: 2px solid #f0c0c0;
}
.step-card p { font-size: .85rem; color: #444; }

/* AUTORIDAD */
.autoridad-wrap {
  display: grid; grid-template-columns: 1fr 1fr; gap: 0;
  min-height: 380px;
}
.autoridad-img {
  background: linear-gradient(135deg,#f5f0ff,#e8e0ff);
  display: flex; align-items: center; justify-content: center;
  font-size: 6rem; padding: 40px;
}
.autoridad-copy { padding: 40px; display: flex; flex-direction: column; justify-content: center; }
.autoridad-copy h2 { font-size: 1.5rem; font-weight: 900; margin-bottom: 16px; }
.autoridad-copy p { font-size: .9rem; color: #444; margin-bottom: 16px; }
.aut-point { display: flex; align-items: flex-start; gap: 10px; margin-bottom: 10px; font-size: .88rem; }
.aut-dot { width: 8px; height: 8px; border-radius: 50%; background: #8B1C1C; flex-shrink: 0; margin-top: 6px; }

/* BENEFICIOS EN GRILLA (resumen) */
.beneficios-header { text-align: center; padding: 40px 40px 20px; }
.beneficios-header h2 { font-size: 1.6rem; font-weight: 900; }
.beneficios-header p { font-size: .9rem; color: #555; margin-top: 8px; }
.beneficios-grid {
  display: grid; grid-template-columns: 1fr 1fr;
  gap: 16px; padding: 0 40px 30px;
  align-items: start;
}
.benefit-card {
  background: #f9f9f9; border-radius: 10px;
  padding: 20px 24px; border-left: 4px solid #8B1C1C;
}
.benefit-card h3 { font-size: .95rem; font-weight: 900; margin-bottom: 6px; }
.benefit-card p { font-size: .82rem; color: #555; }
.beneficios-center-img {
  display: flex; align-items: center; justify-content: center;
  padding: 20px;
}
.beneficios-center-img .big-img {
  width: 200px; height: 200px;
  background: linear-gradient(135deg,#fff8e1,#fdecc8);
  border-radius: 16px; display: flex; align-items: center;
  justify-content: center; font-size: 5rem;
  box-shadow: 0 4px 20px rgba(0,0,0,.1);
}

/* BENEFICIO EXPANDIDO */
.benef-exp {
  display: grid; grid-template-columns: 1fr 1fr;
  gap: 0; min-height: 360px;
}
.benef-exp.reverse { direction: rtl; }
.benef-exp.reverse > * { direction: ltr; }
.benef-exp-img {
  background: linear-gradient(135deg,#f0f8ff,#dbeafe);
  display: flex; align-items: center; justify-content: center;
  font-size: 6rem; padding: 40px;
}
.benef-exp-copy { padding: 40px; display: flex; flex-direction: column; justify-content: center; }
.benef-exp-copy h2 { font-size: 1.4rem; font-weight: 900; margin-bottom: 14px; }
.benef-exp-copy .sub { color: #8B1C1C; font-weight: 700; font-size: .9rem; margin-bottom: 14px; }
.benef-exp-copy p { font-size: .88rem; color: #444; margin-bottom: 12px; }
.benef-exp-copy .bullets { list-style: none; }
.benef-exp-copy .bullets li { display: flex; gap: 10px; margin-bottom: 8px; font-size: .87rem; }
.benef-exp-copy .bullets li::before { content: "●"; color: #8B1C1C; flex-shrink: 0; }

/* COMPARATIVA */
.comp-title { text-align: center; padding: 40px 40px 10px; font-size: .8rem; color: #666; }
.comp-table {
  display: grid; grid-template-columns: 1fr 1fr 1fr;
  gap: 16px; padding: 20px 40px 30px;
}
.comp-col { border-radius: 12px; overflow: hidden; }
.comp-col-head {
  padding: 16px; text-align: center;
  font-weight: 900; font-size: .9rem; text-transform: uppercase;
  letter-spacing: 1px;
}
.comp-col.winner .comp-col-head { background: #8B1C1C; color: #fff; }
.comp-col:not(.winner) .comp-col-head { background: #e0e0e0; color: #999; }
.comp-col-body { background: #f9f9f9; padding: 16px; }
.comp-col.winner .comp-col-body { background: #fff5f5; }
.comp-row { display: flex; align-items: center; gap: 8px; margin-bottom: 8px; font-size: .82rem; }
.comp-ok { color: #8B1C1C; font-size: 1rem; }
.comp-no { color: #bbb; font-size: 1rem; }
.comp-col-img {
  aspect-ratio: 1; background: #f0f0f0;
  display: flex; align-items: center; justify-content: center;
  font-size: 3rem; border-top: 1px solid #e5e5e5;
}
.comp-col.winner .comp-col-img { background: #fff0f0; }

/* TESTIMONIOS */
.test-title { text-align: center; padding: 40px 40px 20px; }
.test-title h2 { font-size: 1.4rem; font-weight: 900; }
.test-grid {
  display: grid; grid-template-columns: repeat(3,1fr);
  gap: 16px; padding: 0 40px 30px;
}
.test-card {
  background: #1a1a1a; border-radius: 12px; padding: 20px;
  display: flex; flex-direction: column; gap: 12px;
}
.test-img {
  width: 100%; aspect-ratio: 1.4;
  background: linear-gradient(135deg,#2a3a4a,#3a4a5a);
  border-radius: 8px; display: flex; align-items: center;
  justify-content: center; font-size: 2.5rem;
}
.test-text { font-size: .82rem; color: #ccc; font-style: italic; }
.test-stars { color: #f59e0b; font-size: .9rem; }
.test-author { display: flex; align-items: center; gap: 10px; }
.test-avatar {
  width: 36px; height: 36px; border-radius: 50%;
  background: #8B1C1C; display: flex; align-items: center;
  justify-content: center; font-size: 1rem; flex-shrink: 0;
}
.test-name { font-size: .82rem; font-weight: 700; color: #fff; }
.test-loc { font-size: .72rem; color: #999; }

/* QUÉ INCLUYE */
.incluye-wrap {
  display: grid; grid-template-columns: 1fr 1fr; gap: 0; min-height: 380px;
}
.incluye-img {
  background: linear-gradient(135deg,#f0fff4,#dcfce7);
  display: flex; align-items: center; justify-content: center;
  font-size: 6rem; padding: 40px;
}
.incluye-copy { padding: 40px; display: flex; flex-direction: column; justify-content: center; }
.incluye-copy h2 { font-size: 1.4rem; font-weight: 900; margin-bottom: 20px; }
.num-list { list-style: none; }
.num-list li { display: flex; align-items: center; gap: 16px; margin-bottom: 14px; font-size: .9rem; font-weight: 600; }
.num-badge {
  min-width: 42px; height: 42px;
  background: #8B1C1C; color: #fff;
  border-radius: 6px; display: flex; align-items: center;
  justify-content: center; font-weight: 900; font-size: .9rem;
  flex-shrink: 0;
}

/* LOGÍSTICA */
.logistica { text-align: center; padding: 40px; background: #f9f9f9; }
.logistica h2 { font-size: 1.3rem; font-weight: 900; margin-bottom: 10px; }
.logistica p { font-size: .9rem; color: #444; margin-bottom: 28px; max-width: 580px; margin-left: auto; margin-right: auto; }
.carriers { display: flex; justify-content: center; align-items: center; gap: 40px; flex-wrap: wrap; }
.carrier { width: 100px; height: 50px; background: #fff; border-radius: 8px; border: 1px solid #ddd; display: flex; align-items: center; justify-content: center; font-weight: 900; font-size: .9rem; padding: 8px; }

/* OFERTA ESCALADA */
.oferta-title { text-align: center; padding: 40px 40px 20px; }
.oferta-title h2 { font-size: 1.4rem; font-weight: 900; }
.oferta-cards {
  display: grid; grid-template-columns: repeat(3,1fr);
  gap: 16px; padding: 0 40px 30px;
}
.oferta-card {
  border-radius: 12px; overflow: hidden;
  border: 2px solid #e5e5e5;
}
.oferta-card.best { border-color: #8B1C1C; transform: scale(1.03); }
.oferta-card-head {
  padding: 16px; text-align: center;
  background: #f0f0f0;
}
.oferta-card.best .oferta-card-head { background: #8B1C1C; color: #fff; }
.oferta-card-head h3 { font-weight: 900; font-size: .95rem; }
.oferta-card-head .tag-best {
  display: inline-block; background: #f59e0b; color: #000;
  font-size: .65rem; font-weight: 900; padding: 2px 8px;
  border-radius: 4px; margin-top: 4px; letter-spacing: 1px;
}
.oferta-card-body { padding: 20px; background: #fff; }
.oferta-card-body .precio { font-size: 1.8rem; font-weight: 900; margin-bottom: 4px; }
.oferta-card-body .old-precio { font-size: .85rem; color: #999; text-decoration: line-through; margin-bottom: 12px; }
.oferta-card-body ul { list-style: none; }
.oferta-card-body ul li { font-size: .82rem; color: #444; margin-bottom: 6px; padding-left: 16px; position: relative; }
.oferta-card-body ul li::before { content: "✔"; color: #8B1C1C; position: absolute; left: 0; }
.oferta-card-body .btn-of {
  display: block; width: 100%; margin-top: 14px;
  background: #1a1a1a; color: #fff; text-align: center;
  padding: 12px; border-radius: 6px;
  font-weight: 900; font-size: .8rem; letter-spacing: 1px;
  text-transform: uppercase;
}
.oferta-card.best .oferta-card-body .btn-of { background: #8B1C1C; }

/* FAQ */
.faq-wrap { padding: 40px; }
.faq-wrap h2 { font-size: 1.3rem; font-weight: 900; margin-bottom: 24px; text-align: center; }
.faq-item { border-bottom: 1px solid #e5e5e5; padding: 16px 0; }
.faq-q { font-weight: 800; font-size: .92rem; margin-bottom: 6px; }
.faq-a { font-size: .85rem; color: #555; }

/* CTA FINAL */
.cta-final {
  background: #1a1a1a; color: #fff;
  text-align: center; padding: 50px 40px;
}
.cta-final h2 { font-size: 1.6rem; font-weight: 900; margin-bottom: 10px; }
.cta-final p { color: #aaa; font-size: .9rem; margin-bottom: 28px; }
.cta-final .btn-big {
  display: inline-block;
  background: #8B1C1C; color: #fff;
  padding: 18px 48px; border-radius: 8px;
  font-weight: 900; font-size: 1rem; letter-spacing: 2px;
  text-transform: uppercase;
}
.cta-final .sub-cta { margin-top: 14px; font-size: .8rem; color: #888; }

/* FOOTER */
.r2r-footer {
  text-align: center; padding: 28px; background: #fff;
  border-top: 3px solid #8B1C1C;
  font-size: .8rem; color: #999;
}
.r2r-footer span { color: #8B1C1C; font-weight: 700; }

/* CTA repetido inline */
.cta-inline {
  text-align: center; padding: 24px 40px;
  background: #f9f9f9;
}
.cta-inline .btn-cta-inline {
  display: inline-block; background: #1a1a1a; color: #fff;
  padding: 14px 36px; border-radius: 6px;
  font-weight: 900; font-size: .82rem; letter-spacing: 2px;
  text-transform: uppercase;
}
.cta-inline .btn-cta-inline span { display: block; font-size: .65rem; color: #aaa; margin-top: 2px; font-weight: 400; }

@media(max-width:720px) {
  .hero-wrap, .transf-steps, .autoridad-wrap, .benef-exp,
  .comp-table, .test-grid, .incluye-wrap, .oferta-cards,
  .beneficios-grid { grid-template-columns: 1fr; }
  .r2r-header { padding: 20px; flex-direction: column; gap: 8px; }
  .sec-bar { font-size: 1rem; letter-spacing: 2px; }
  .garantias-bar { gap: 20px; }
}
"""

# ─────────────────────────────────────────────
# SECCIONES HTML
# ─────────────────────────────────────────────

def html_como_usarlo():
    """Sección: Cómo Usarlo — 4 pasos detallados con imagen y texto alterno."""
    return """
  <div class="section">
    <div class="sec-bar" style="font-size:1rem;letter-spacing:2px;">¿Cómo Debo Usarlo?</div>
    <div class="wrap">
      <div class="benef-exp">
        <div class="benef-exp-img" style="background:linear-gradient(135deg,#fff8e1,#fdecc8);">
          <div style="text-align:center;">
            <div style="font-size:5rem;margin-bottom:12px;">🛡️</div>
            <div style="font-size:.75rem;font-weight:900;color:#8B1C1C;letter-spacing:2px;text-transform:uppercase;">MODO DE USO</div>
          </div>
        </div>
        <div class="benef-exp-copy">
          <h2>Aplicación en 4 Pasos Simples</h2>
          <div class="sub">Resultado cristalino desde la primera vez — sin experiencia previa.</div>
          <div style="margin-top:8px;">
            <div style="display:flex;gap:16px;align-items:flex-start;margin-bottom:16px;">
              <div style="min-width:36px;height:36px;background:#8B1C1C;color:#fff;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:900;font-size:.85rem;flex-shrink:0;">01</div>
              <div>
                <div style="font-weight:900;font-size:.9rem;margin-bottom:4px;">Limpiar el parabrisas de polvo grueso</div>
                <div style="font-size:.82rem;color:#555;">Pasá un paño seco o servilleta para remover el polvo visible. El parabrisas debe estar seco — no húmedo — antes de aplicar.</div>
              </div>
            </div>
            <div style="display:flex;gap:16px;align-items:flex-start;margin-bottom:16px;">
              <div style="min-width:36px;height:36px;background:#8B1C1C;color:#fff;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:900;font-size:.85rem;flex-shrink:0;">02</div>
              <div>
                <div style="font-weight:900;font-size:.9rem;margin-bottom:4px;">Aplicá 3-4 sprays de OilShield™</div>
                <div style="font-size:.82rem;color:#555;">Rociá directamente sobre el parabrisas. Cubrí las zonas con más acumulación de aceite — especialmente el centro y las esquinas.</div>
              </div>
            </div>
            <div style="display:flex;gap:16px;align-items:flex-start;margin-bottom:16px;">
              <div style="min-width:36px;height:36px;background:#8B1C1C;color:#fff;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:900;font-size:.85rem;flex-shrink:0;">03</div>
              <div>
                <div style="font-weight:900;font-size:.9rem;margin-bottom:4px;">Distribuí con la esponja en movimientos circulares</div>
                <div style="font-size:.82rem;color:#555;">2 minutos de frotamiento circular activan la fórmula nano-molecular. Vas a sentir cómo el aceite se suelta y la esponja desliza con facilidad.</div>
              </div>
            </div>
            <div style="display:flex;gap:16px;align-items:flex-start;">
              <div style="min-width:36px;height:36px;background:#8B1C1C;color:#fff;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:900;font-size:.85rem;flex-shrink:0;">04</div>
              <div>
                <div style="font-weight:900;font-size:.9rem;margin-bottom:4px;">Limpiá con un paño seco o microfibra</div>
                <div style="font-size:.82rem;color:#555;">Pasá el paño firmemente hasta que el vidrio quede transparente y sin residuos. El resultado cristalino dura entre 3 y 6 semanas.</div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div style="background:#fff8e1;padding:16px 40px;border-left:4px solid #f59e0b;margin:0 40px 30px;border-radius:0 8px 8px 0;">
        <strong style="color:#92400e;">💡 TIP PROFESIONAL:</strong>
        <span style="font-size:.85rem;color:#78350f;"> Aplicá de noche o bajo sombra. El calor directo del sol puede secar el producto antes de que penetre. Temperatura ideal: menos de 30°C.</span>
      </div>
      <div class="cta-inline">
        <a href="#" class="btn-cta-inline">COMPRAR CONTRA ENTREGA<span>Y ahorrá más de Q1,200 al año</span></a>
      </div>
    </div>
  </div>
"""


def html_caracteristicas():
    """Sección: Características Técnicas — con números rojos estilo PDF."""
    specs = [
        ("01", "Fórmula Nano-Molecular", "Tecnología de partículas ultra-finas que penetran en los microporos del vidrio y disuelven compuestos lipídicos (aceite, grasa) que el agua y el jabón no pueden eliminar."),
        ("02", "Rendimiento por Frasco", "1 frasco rinde para 8-12 aplicaciones completas en un vehículo estándar. Equivale a 32-48 lavadas en lavadero convencional. Duración estimada: 3 a 6 meses de uso regular."),
        ("03", "Tiempo de Acción", "Resultados visibles en 5 minutos. Fórmula de acción rápida que activa la disolución del aceite desde el primer contacto. Sin tiempos de espera prolongados."),
        ("04", "Compatible con Todos los Vehículos", "Apto para carros, pick-ups, motos, camiones y buses. Funciona en vidrio templado, laminado y tratado. No afecta sellos de hule, plásticos ni carrocería."),
        ("05", "pH Neutro — 100% Seguro", "Fórmula pH neutro (6.8-7.2). No raya, no deteriora ni opaca el vidrio. No contiene amoniaco ni solventes agresivos. Seguro para usar con ventanas tintadas."),
        ("06", "Efecto Hidrofóbico Post-Aplicación", "Después de la limpieza, OilShield™ deja una capa hidrofóbica que repele agua, polvo y nuevas acumulaciones de aceite, extendiendo el tiempo entre aplicaciones."),
    ]
    items = ""
    for i, (num, title, desc) in enumerate(specs):
        bg = "#f9f9f9" if i % 2 == 0 else "#f5f0f0"
        items += f"""
        <div style="display:flex;gap:20px;align-items:flex-start;padding:20px 24px;background:{bg};border-radius:10px;margin-bottom:12px;">
          <div style="min-width:48px;height:48px;background:#8B1C1C;color:#fff;border-radius:8px;display:flex;align-items:center;justify-content:center;font-weight:900;font-size:1rem;flex-shrink:0;">{num}</div>
          <div>
            <div style="font-weight:900;font-size:.95rem;margin-bottom:5px;">{title}</div>
            <div style="font-size:.83rem;color:#555;line-height:1.6;">{desc}</div>
          </div>
        </div>"""
    return f"""
  <div class="section" style="background:#f5f5f5;">
    <div class="wrap">
      <div style="padding:40px 40px 20px;">
        <h2 style="font-size:1.4rem;font-weight:900;margin-bottom:8px;">Características Técnicas</h2>
        <p style="font-size:.9rem;color:#555;max-width:600px;">Todo lo que necesitás saber sobre la fórmula y el rendimiento de OilShield™ para Guatemala.</p>
      </div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:0 20px;padding:0 40px;align-items:start;">
        <div>
          <div style="font-size:.7rem;font-weight:900;letter-spacing:3px;color:#8B1C1C;text-transform:uppercase;margin-bottom:16px;">ESPECIFICACIONES</div>
          <div style="background:linear-gradient(135deg,#fff8e1,#fdecc8);border-radius:16px;aspect-ratio:1;display:flex;align-items:center;justify-content:center;font-size:5rem;margin-bottom:20px;">🔬</div>
        </div>
        <div>
          {items}
        </div>
      </div>
      <div class="cta-inline">
        <a href="#" class="btn-cta-inline">COMPRAR CONTRA ENTREGA<span>Y ahorrá más de Q1,200 al año</span></a>
      </div>
    </div>
  </div>
"""


def html_header():
    return """
  <header class="r2r-header">
    <div class="r2r-logo">ROOKIE <span>2</span> RICHES</div>
    <div class="r2r-handle">@ecomjuliann</div>
  </header>
  <div class="sec-bar">ESTRUCTURA DE VENTAS</div>
"""

def html_topbar():
    return """
  <div class="section">
    <div class="top-bar">
      🚚 Envío GRATIS a toda Guatemala &nbsp;|&nbsp; Pagás Solo al Recibir — Sin tarjeta, sin riesgo 🔒
    </div>
  </div>
"""

def html_hero():
    return """
  <div class="section">
    <div class="wrap">
      <div class="hero-wrap">
        <!-- IMAGEN PRODUCTO -->
        <div class="hero-img">
          <div class="main-img">🛡️</div>
          <div class="thumbs">
            <div class="thumb active">🛡️</div>
            <div class="thumb">✨</div>
            <div class="thumb">🚗</div>
            <div class="thumb">💧</div>
          </div>
        </div>
        <!-- COPY -->
        <div class="hero-copy">
          <div class="hero-stars">★★★★★</div>
          <div class="hero-reviews">+3,800 conductores en Guatemala ya lo usan</div>
          <h1 class="hero-h1">Deja de tirar pisto en el lavadero. Limpiá tu parabrisas en 5 minutos.</h1>
          <div class="hero-sol">OilShield™ elimina la mugre y el aceite con tecnología nano-molecular — resultado visible en la primera pasada.</div>
          <div style="margin-bottom:18px;">
            <div class="hero-price-old">PRECIO NORMAL: Q350</div>
            <span class="hero-price-new">Q249</span>
            <span class="off-badge">29% OFF</span>
          </div>
          <div class="hero-name">OilShield™ — Limpiador Nano-Molecular</div>
          <ul class="check-list">
            <li><span class="chk">✔</span> Resultado visible en 5 minutos</li>
            <li><span class="chk">✔</span> Ahorrás más de Q1,200 al año</li>
            <li><span class="chk">✔</span> Un uso equivale a 4 lavadas tradicionales</li>
            <li><span class="chk">✔</span> Funciona en todos los vehículos</li>
          </ul>
          <div class="hero-testimonio">
            "La loca ya llevo 3 meses gastando Q200 al mes en el lavadero. La loca yo pensé que era mentira." — María R., Guatemala City ✅ Compradora verificada
          </div>
          <button class="btn-cta">PAGAR AL RECIBIR — SIN TARJETA<span>Pagás solo cuando el mensajero llega a tu puerta</span></button>
        </div>
      </div>
    </div>
  </div>
"""

def html_garantias():
    return """
  <div class="section">
    <div class="wrap">
      <div class="garantias-bar">
        <div class="garantia-item">
          <div class="gico">🛡️</div>
          <div class="gtxt">
            <strong>GARANTÍA 30 DÍAS</strong>
            <span>Si no ves resultado, devolvemos tu pisto. Sin preguntas.</span>
          </div>
        </div>
        <div class="garantia-item">
          <div class="gico">🚚</div>
          <div class="gtxt">
            <strong>ENVÍO GRATIS</strong>
            <span>Entrega a todo Guatemala. Pagás solo al recibir.</span>
          </div>
        </div>
        <div class="garantia-item">
          <div class="gico">✅</div>
          <div class="gtxt">
            <strong>CALIDAD CERTIFICADA</strong>
            <span>Tecnología nano-molecular validada por +3,800 conductores GT.</span>
          </div>
        </div>
      </div>
      <div class="logos-bar">
        <div class="logo-brand">VOGUE</div>
        <div class="logo-brand">USA TODAY</div>
        <div class="logo-brand">CBS</div>
        <div class="logo-brand">abc</div>
      </div>
    </div>
  </div>
"""

def html_transformacion():
    return """
  <div class="section">
    <div class="wrap">
      <div class="transf-header">
        <h2>TRANSFORMACIÓN PRINCIPAL QUE REALIZA EL PRODUCTO</h2>
        <p>De parabrisas opaco y peligroso a cristalino en 3 pasos simples — sin ir al lavadero, sin gastar de más.</p>
      </div>
      <div class="transf-steps">
        <div class="step-card">
          <div class="step-label">PASO 1</div>
          <div class="step-img">💧</div>
          <p><strong>Aplicá OilShield™</strong> directamente sobre el parabrisas seco. 3 sprays son suficientes.</p>
        </div>
        <div class="step-card">
          <div class="step-label">PASO 2</div>
          <div class="step-img">🧴</div>
          <p><strong>Distribuí con el aplicador</strong> en movimientos circulares por 2 minutos. Sentís cómo levanta la mugre.</p>
        </div>
        <div class="step-card">
          <div class="step-label">PASO 3</div>
          <div class="step-img">✨</div>
          <p><strong>Limpiá con un paño seco</strong> y listo. Resultado cristalino que dura semanas — no días.</p>
        </div>
      </div>
      <div class="cta-inline">
        <a href="#" class="btn-cta-inline">COMPRAR CONTRA ENTREGA<span>Y ahorrá más de Q1,200 al año</span></a>
      </div>
    </div>
  </div>
"""

def html_autoridad():
    return """
  <div class="section">
    <div class="sec-bar" style="font-size:1rem;letter-spacing:2px;">Prueba de Autoridad</div>
    <div class="wrap">
      <div class="autoridad-wrap">
        <div class="autoridad-img">🔬</div>
        <div class="autoridad-copy">
          <h2>¿Por qué el aceite y la champa NUNCA van a funcionar? La ciencia lo explica.</h2>
          <p>El aceite industrial que se acumula en tu parabrisas es un compuesto lipídico que el agua y el jabón físicamente no pueden disolver. Necesitás una fórmula química específica: tecnología nano-molecular.</p>
          <p><strong>OilShield™ fue diseñado específicamente</strong> para romper la tensión superficial del aceite y eliminarlo en una sola pasada.</p>
          <div class="aut-point"><div class="aut-dot"></div><span>72% de accidentes nocturnos relacionados con mala visibilidad del parabrisas — Fuente: NHTSA, 2023.</span></div>
          <div class="aut-point"><div class="aut-dot"></div><span>99% de los residuos grasos NO se eliminan con lavado convencional — Fuente: SAF International, 2022.</span></div>
          <div class="aut-point"><div class="aut-dot"></div><span>+3,800 conductores en Guatemala ya verificaron el resultado.</span></div>
        </div>
      </div>
    </div>
  </div>
"""

def html_beneficios_grid():
    return """
  <div class="section" style="background:#f5f5f5;">
    <div class="wrap">
      <div class="beneficios-header">
        <h2>"Visión Cristalina en 5 Minutos"</h2>
        <p>OilShield™ no solo limpia — protege, ahorra y te da tranquilidad en cada manejo.</p>
      </div>
      <div style="display:grid;grid-template-columns:1fr auto 1fr;gap:16px;padding:0 40px 30px;align-items:center;">
        <div>
          <div class="benefit-card" style="margin-bottom:14px;">
            <h3>Beneficio 1: Ahorro Real</h3>
            <p>Dejás de gastar entre Q100 y Q200 al mes en el lavadero. En un año ahorrás más de Q1,200 — con un solo frasco.</p>
          </div>
          <div class="benefit-card" style="margin-bottom:14px;">
            <h3>Beneficio 2: Tiempo Libre</h3>
            <p>5 minutos desde tu casa vs. 40 minutos esperando en el lavadero. La diferencia te la quedás vos.</p>
          </div>
          <div class="benefit-card">
            <h3>Beneficio 3: Seguridad</h3>
            <p>Parabrisas cristalino = manejo seguro. Menos reflejos peligrosos de noche y con lluvia.</p>
          </div>
        </div>
        <div class="beneficios-center-img">
          <div class="big-img">🛡️</div>
        </div>
        <div>
          <div class="benefit-card" style="margin-bottom:14px;">
            <h3>Beneficio 4: Durabilidad</h3>
            <p>Un uso equivale a 4 lavadas tradicionales. La capa protectora dura semanas, no días.</p>
          </div>
          <div class="benefit-card" style="margin-bottom:14px;">
            <h3>Beneficio 5: Facilidad</h3>
            <p>Sin equipo especial, sin ir a ningún lado. Solo aplicás, distribuís y limpiás — con lo que tenés en casa.</p>
          </div>
          <div class="benefit-card">
            <h3>Beneficio 6: Sin Riesgo</h3>
            <p>Pagás solo al recibir. Si no te convence, garantía de 30 días. Riesgo cero para vos.</p>
          </div>
        </div>
      </div>
      <div class="cta-inline">
        <a href="#" class="btn-cta-inline">COMPRAR CONTRA ENTREGA<span>Y ahorrá más de Q1,200 al año</span></a>
      </div>
    </div>
  </div>
"""

def html_benef_expandido(num, titulo, sub, p1, bullets, emoji, reverse=False):
    img_side = f'<div class="benef-exp-img" style="background:linear-gradient(135deg,#f0f8ff,#dbeafe);">{emoji}</div>'
    copy_side = f"""
    <div class="benef-exp-copy">
      <h2>Beneficio #{num}: {titulo}</h2>
      <div class="sub">{sub}</div>
      <p>{p1}</p>
      <ul class="bullets">
        {''.join(f'<li>{b}</li>' for b in bullets)}
      </ul>
      <div class="cta-inline" style="padding:20px 0 0;">
        <a href="#" class="btn-cta-inline">COMPRAR CONTRA ENTREGA<span>Y ahorrá Q1,200 al año</span></a>
      </div>
    </div>"""
    if reverse:
        inner = copy_side + img_side
    else:
        inner = img_side + copy_side
    return f"""
  <div class="section">
    <div class="wrap">
      <div class="benef-exp">
        {inner}
      </div>
    </div>
  </div>
"""

def html_comparativa():
    return """
  <div class="section" style="background:#f5f5f5;">
    <div class="sec-bar" style="font-size:.9rem;letter-spacing:2px;">¿Por qué Escoger Nuestro Producto?</div>
    <div class="wrap">
      <div class="comp-table">
        <!-- Col 1: Lavadero -->
        <div class="comp-col">
          <div class="comp-col-head">Lavadero Tradicional</div>
          <div class="comp-col-body">
            <div class="comp-row"><span class="comp-no">✗</span> Q100-Q200 cada vez</div>
            <div class="comp-row"><span class="comp-no">✗</span> 40 min de espera</div>
            <div class="comp-row"><span class="comp-no">✗</span> Resultado dura 3 días</div>
            <div class="comp-row"><span class="comp-no">✗</span> No elimina el aceite real</div>
            <div class="comp-row"><span class="comp-no">✗</span> Reflejos siguen de noche</div>
            <div class="comp-row"><span class="comp-no">✗</span> Tenés que salir de casa</div>
          </div>
          <div class="comp-col-img">🚿</div>
        </div>
        <!-- Col 2: OilShield (WINNER) -->
        <div class="comp-col winner">
          <div class="comp-col-head">OilShield™</div>
          <div class="comp-col-body">
            <div class="comp-row"><span class="comp-ok">✔</span> Q249 una sola vez</div>
            <div class="comp-row"><span class="comp-ok">✔</span> 5 minutos en tu casa</div>
            <div class="comp-row"><span class="comp-ok">✔</span> Resultado dura semanas</div>
            <div class="comp-row"><span class="comp-ok">✔</span> Fórmula nano-molecular</div>
            <div class="comp-row"><span class="comp-ok">✔</span> Visión cristalina de noche</div>
            <div class="comp-row"><span class="comp-ok">✔</span> Lo hacés desde tu casa</div>
          </div>
          <div class="comp-col-img">🛡️</div>
        </div>
        <!-- Col 3: Otros limpiadores -->
        <div class="comp-col">
          <div class="comp-col-head">Otros Limpiadores</div>
          <div class="comp-col-body">
            <div class="comp-row"><span class="comp-no">✗</span> Precio similar o mayor</div>
            <div class="comp-row"><span class="comp-no">✗</span> Formulación genérica</div>
            <div class="comp-row"><span class="comp-ok">✔</span> En casa</div>
            <div class="comp-row"><span class="comp-no">✗</span> No remueve aceite real</div>
            <div class="comp-row"><span class="comp-no">✗</span> Múltiples pasadas</div>
            <div class="comp-row"><span class="comp-no">✗</span> Sin garantía real</div>
          </div>
          <div class="comp-col-img">🧴</div>
        </div>
      </div>
      <div style="text-align:center;padding:10px 40px 30px;font-size:1.2rem;font-weight:900;color:#8B1C1C;">ROOKIE 2 RICHES</div>
      <div class="cta-inline">
        <a href="#" class="btn-cta-inline">COMPRAR CONTRA ENTREGA<span>Y ahorrá Q1,200 al año</span></a>
      </div>
    </div>
  </div>
"""

def html_testimonios():
    tests = [
        ("👩", "María R.", "Guatemala City", "«La loca ya llevo 3 meses gastando Q200 al mes en el lavadero. La loca yo pensé que era mentira — pero funciona de verdad.»"),
        ("👨", "Carlos M.", "Mixco, Guatemala", "«Lo usé para mi pick-up Hilux. Parabrisas cristalino en 5 minutos. Nunca más vuelvo al lavadero.»"),
        ("👩‍💼", "Andrea S.", "Quetzaltenango", "«Mis hijos me preguntaron si cambié el parabrisas. Solo usé OilShield™. 100% recomendado.»"),
        ("👨‍🔧", "Roberto L.", "Villa Nueva", "«Mecánico de profesión. Jamás creí en estos productos hasta que lo probé. El aceite desapareció en una pasada.»"),
        ("👩‍🏫", "Sofía P.", "Escuintla", "«Pagué solo al recibir, sin riesgo. Llegó rápido y funcionó. Ahorro Q150 al mes desde entonces.»"),
        ("🧔", "Diego F.", "Petén", "«Vivo en carretera. Este producto cambió mi vida. Visión perfecta de noche y con lluvia.»"),
    ]
    cards = ""
    for ava, name, loc, text in tests:
        cards += f"""
        <div class="test-card">
          <div class="test-img">{ava}</div>
          <div class="test-text">{text}</div>
          <div class="test-stars">★★★★★</div>
          <div class="test-author">
            <div class="test-avatar">{ava}</div>
            <div><div class="test-name">{name}</div><div class="test-loc">{loc} ✅ Comprador verificado</div></div>
          </div>
        </div>"""
    return f"""
  <div class="section">
    <div class="wrap">
      <div class="test-title"><h2>Personas que han Cambiado sus Vidas...</h2></div>
      <div class="test-grid">{cards}</div>
    </div>
  </div>
"""

def html_incluye():
    return """
  <div class="section" style="background:#f5f5f5;">
    <div class="wrap">
      <div class="incluye-wrap">
        <div class="incluye-img">📦</div>
        <div class="incluye-copy">
          <h2>¿Qué Incluye mi Compra?</h2>
          <ul class="num-list">
            <li><div class="num-badge">01</div> 1 frasco OilShield™ (nano-molecular)</li>
            <li><div class="num-badge">02</div> 1 esponja de aplicación profesional</li>
            <li><div class="num-badge">03</div> Guía de aplicación paso a paso</li>
            <li><div class="num-badge">04</div> Envío GRATIS a toda Guatemala</li>
            <li><div class="num-badge">05</div> Pago contra entrega (sin tarjeta)</li>
            <li><div class="num-badge">06</div> Garantía 30 días — sin preguntas</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
"""

def html_logistica():
    return """
  <div class="section">
    <div class="wrap">
      <div class="logistica">
        <h2>¿Cómo Puedo Recibir Mi Producto?</h2>
        <p>Trabajamos con las principales transportadoras del país para <strong>asegurar entregas rápidas y confiables.</strong> Además, ofrecemos <strong>pago contra entrega en todo el territorio nacional,</strong> brindándote comodidad, confianza y una experiencia de <strong>compra segura.</strong></p>
        <div class="carriers">
          <div class="carrier" style="color:#4d148c;font-weight:900;">FedEx</div>
          <div class="carrier" style="color:#d40511;font-weight:900;">DHL</div>
          <div class="carrier" style="color:#351c15;font-weight:900;">UPS</div>
          <div class="carrier" style="background:#1a1a1a;color:#fff;">GUATEX</div>
        </div>
      </div>
    </div>
  </div>
"""

def html_oferta():
    return """
  <div class="section" style="background:#f5f5f5;">
    <div class="wrap">
      <div class="oferta-title"><h2>Elegí Tu Paquete</h2></div>
      <div class="oferta-cards">
        <div class="oferta-card">
          <div class="oferta-card-head"><h3>BÁSICO</h3></div>
          <div class="oferta-card-body">
            <div class="precio">Q249</div>
            <div class="old-precio">Antes Q350</div>
            <ul>
              <li>1 frasco OilShield™</li>
              <li>1 esponja aplicadora</li>
              <li>Envío GRATIS</li>
              <li>Garantía 30 días</li>
            </ul>
            <a href="#" class="btn-of">COMPRAR AHORA</a>
          </div>
        </div>
        <div class="oferta-card best">
          <div class="oferta-card-head">
            <h3>FAMILIAR</h3>
            <div class="tag-best">⭐ MÁS POPULAR</div>
          </div>
          <div class="oferta-card-body">
            <div class="precio" style="color:#8B1C1C;">Q399</div>
            <div class="old-precio">2 frascos — Antes Q700</div>
            <ul>
              <li>2 frascos OilShield™</li>
              <li>2 esponjas aplicadoras</li>
              <li>Envío GRATIS prioritario</li>
              <li>Garantía 30 días extendida</li>
              <li>1 paño microfibra GRATIS</li>
            </ul>
            <a href="#" class="btn-of">APROVECHAR OFERTA</a>
          </div>
        </div>
        <div class="oferta-card">
          <div class="oferta-card-head"><h3>FLOTA</h3></div>
          <div class="oferta-card-body">
            <div class="precio">Q549</div>
            <div class="old-precio">3 frascos — Antes Q1,050</div>
            <ul>
              <li>3 frascos OilShield™</li>
              <li>Kit completo de aplicación</li>
              <li>Envío GRATIS express</li>
              <li>Garantía 60 días</li>
              <li>Ideal para flota o familia grande</li>
            </ul>
            <a href="#" class="btn-of">COMPRAR AHORA</a>
          </div>
        </div>
      </div>
    </div>
  </div>
"""

def html_faq():
    faqs = [
        ("¿Cuánto tiempo dura el efecto?", "El efecto dura entre 3 y 6 semanas dependiendo de las condiciones de uso. Con lluvia frecuente puede ser 2-3 semanas."),
        ("¿Funciona en todos los vehículos?", "Sí. OilShield™ funciona en carros, pick-ups, motos, buses y cualquier superficie de vidrio vehicular."),
        ("¿Es seguro para el vidrio?", "100% seguro. La fórmula nano-molecular no raya ni daña el vidrio. Es el mismo principio que usan los fabricantes de autos."),
        ("¿Cómo funciona el pago contra entrega?", "El mensajero llega a tu puerta. Recibís el producto, lo inspeccionás y luego pagás. Zero riesgo para vos."),
        ("¿Cuánto tarda en llegar?", "Guatemala Capital: 1-2 días hábiles. Resto de la república: 2-4 días hábiles. Envío completamente GRATIS."),
        ("¿Qué hago si no me funciona?", "Contactás a nuestro soporte con tu comprobante de compra dentro de 30 días y devolvemos tu pisto completo. Sin preguntas."),
        ("¿Puedo comprar para regalar?", "¡Claro! Es el regalo perfecto para cualquier conductor. Avisanos y embalamos con presentación de regalo sin costo extra."),
    ]
    items = "".join(f'<div class="faq-item"><div class="faq-q">❓ {q}</div><div class="faq-a">{a}</div></div>' for q, a in faqs)
    return f"""
  <div class="section">
    <div class="wrap">
      <div class="faq-wrap">
        <h2>Preguntas Frecuentes</h2>
        {items}
      </div>
    </div>
  </div>
"""

def html_cta_final():
    return """
  <div class="cta-final">
    <h2>¿Seguís tirando pisto en el lavadero?</h2>
    <p>Ahorrá más de Q1,200 al año con una sola inversión. Garantía de 30 días. Pagás solo al recibir.</p>
    <a href="#" class="btn-big">✅ QUIERO EMPEZAR A AHORRAR HOY — PAGAR AL RECIBIR</a>
    <div class="sub-cta">Sin tarjeta • Sin riesgo • Envío gratis a toda Guatemala 🇬🇹</div>
  </div>
"""

def html_footer():
    return """
  <div class="r2r-footer">
    Generado con <span>ROOKIE 2 RICHES — EGS Framework 2026</span> · OilShield™ Guatemala
  </div>
"""

# ─────────────────────────────────────────────
# ENSAMBLADO FINAL
# ─────────────────────────────────────────────

def generate_html() -> str:
    benef1 = html_benef_expandido(
        1, "Ahorro Real", "Dejás de gastar entre Q100 y Q200 al mes en el lavadero.",
        "Cada mes pagás entre Q100 y Q200 en el lavadero para que el aceite vuelva en días. Con OilShield™ pagás Q249 una sola vez y tenés resultado que dura semanas.",
        [
            "<strong>Pon el foco en el cliente:</strong> Vos llegás a casa, aplicás en 5 minutos y listo.",
            "<strong>Diferencia clara:</strong> El lavadero elimina la suciedad visible. OilShield™ elimina el aceite molecular.",
            "<strong>Conecta emocionalmente:</strong> Ese pisto que ahorrás es tuyo — para lo que vos querás.",
        ],
        "💰", reverse=False
    )
    benef2 = html_benef_expandido(
        2, "Tiempo Libre", "5 minutos en casa vs. 40 minutos esperando en el lavadero.",
        "40 minutos de espera, cola, ruido — cada semana. Con OilShield™ hacés lo mismo desde tu cochera en 5 minutos y sin salir.",
        [
            "<strong>Pon el foco en el cliente:</strong> Tu tiempo vale más que el aceite que limpiás.",
            "<strong>Diferencia clara:</strong> No es comodidad — es recuperar tu tiempo.",
            "<strong>Conecta emocionalmente:</strong> 8 horas al año que te quedás vos para lo que realmente importa.",
        ],
        "⏱️", reverse=True
    )
    benef3 = html_benef_expandido(
        3, "Seguridad Nocturna", "Parabrisas cristalino = manejo seguro de noche y con lluvia.",
        "Los reflejos peligrosos de noche y la lluvia que distorsiona la visión son causados por el aceite acumulado. OilShield™ los elimina en una pasada.",
        [
            "<strong>Pon el foco en el cliente:</strong> No es estético — es tu seguridad y la de tu familia.",
            "<strong>Diferencia clara:</strong> 72% de accidentes nocturnos relacionados con mala visibilidad.",
            "<strong>Conecta emocionalmente:</strong> Llegás a casa. Sin sustos. Con visión perfecta.",
        ],
        "🌙", reverse=False
    )
    benef4 = html_benef_expandido(
        4, "Durabilidad Real", "Un uso equivale a 4 lavadas tradicionales. Semanas, no días.",
        "El lavadero da resultado por 3-4 días. OilShield™ deposita una capa nano-molecular que protege y repele durante semanas completas.",
        [
            "<strong>Pon el foco en el cliente:</strong> Aplicás el domingo y el parabrisas sigue cristalino el viernes.",
            "<strong>Diferencia clara:</strong> Tecnología nano vs. agua y jabón genérico.",
            "<strong>Conecta emocionalmente:</strong> Menos preocupaciones. Menos viajes. Más tranquilidad.",
        ],
        "🔬", reverse=True
    )
    benef5 = html_benef_expandido(
        5, "Sin Complicaciones", "Aplicación simple con lo que tenés en casa. Sin equipo especial.",
        "No necesitás herramientas. No necesitás experiencia. Solo aplicás, distribuís y limpiás. El kit incluye todo lo que necesitás.",
        [
            "<strong>Pon el foco en el cliente:</strong> Si podés limpiar con un paño, podés usar OilShield™.",
            "<strong>Diferencia clara:</strong> Sin curva de aprendizaje. Sin instrucciones complicadas.",
            "<strong>Conecta emocionalmente:</strong> Confianza desde el primer uso.",
        ],
        "🎯", reverse=False
    )
    benef6 = html_benef_expandido(
        6, "Cero Riesgo", "Pagás solo al recibir. Garantía 30 días. Sin preguntas.",
        "Probás OilShield™ sin arriesgar nada. Si en 30 días no ves el resultado prometido, te devolvemos el pisto completo.",
        [
            "<strong>Pon el foco en el cliente:</strong> El riesgo lo asumimos nosotros, no vos.",
            "<strong>Diferencia clara:</strong> Pago contra entrega + garantía real de devolución.",
            "<strong>Conecta emocionalmente:</strong> Comprá con total confianza desde el primer día.",
        ],
        "🛡️", reverse=True
    )

    body = (
        html_header() +
        html_topbar() +
        html_hero() +
        html_garantias() +
        html_transformacion() +
        html_autoridad() +
        html_beneficios_grid() +
        benef1 + benef2 + benef3 + benef4 + benef5 + benef6 +
        html_como_usarlo() +
        html_caracteristicas() +
        html_comparativa() +
        html_testimonios() +
        html_incluye() +
        html_logistica() +
        html_oferta() +
        html_faq() +
        html_cta_final() +
        html_footer()
    )

    return f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>🏆 ROOKIE2RICHES — OilShield™ Guatemala | Estructura de Ventas</title>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;900&family=Outfit:wght@400;600;700;900&display=swap" rel="stylesheet">
  <style>{CSS}</style>
</head>
<body>
{body}
</body>
</html>"""


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────
if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    output_file = os.path.join(OUTPUT_DIR, "angulo_ahorro_oilshield_gt.html")
    html = generate_html()
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅ Reporte generado: {output_file}")
