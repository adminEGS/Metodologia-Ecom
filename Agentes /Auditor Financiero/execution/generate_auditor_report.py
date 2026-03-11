#!/usr/bin/env python3
"""
generate_auditor_report.py — Auditor Financiero
Genera el HTML con el análisis de viabilidad financiera.
Output: Auditor Financiero/reporte_auditor_oilshield_gt.html
"""
import os

BASE = os.path.dirname(os.path.abspath(__file__))
OUT  = os.path.join(BASE, "..", "reporte_auditor_oilshield_gt.html")

CSS = """
* { box-sizing:border-box; margin:0; padding:0;
    user-select:text!important; -webkit-user-select:text!important; }
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800;900&family=Outfit:wght@400;500;600;700&display=swap');
:root {
  --bg:#f5f3f0; --white:#fff; --dark:#1a1a1a; --granate:#7a1f1f;
  --gold:#d4a03c; --green:#2d8a4e; --red:#c62828; --text:#333; --text-light:#666;
  --border:#e0dcd7; --shadow:0 4px 24px rgba(0,0,0,.08); --radius:16px;
}
body { font-family:'Outfit',sans-serif; background:var(--bg); color:var(--text); line-height:1.6; }
.container { max-width:1100px; margin:0 auto; padding:0 24px; }
.header { background:var(--white); border-bottom:3px solid var(--granate); padding:16px 0; }
.header-inner { display:flex; justify-content:space-between; align-items:center; }
.header h1 { font-family:'Montserrat',sans-serif; font-size:1.5rem; font-weight:900;
             letter-spacing:2px; color:var(--dark); }
.header span { font-size:.9rem; color:var(--granate); font-weight:600; }
.top-bar { background:var(--granate); color:#fff; text-align:center; padding:14px 0;
           font-family:'Montserrat',sans-serif; font-weight:700; letter-spacing:4px;
           text-transform:uppercase; font-size:1rem; }
section { padding:48px 0; }
section:nth-child(even) { background:var(--white); }
.section-title { font-family:'Montserrat',sans-serif; font-weight:800; font-size:1.8rem;
                 color:var(--dark); text-align:center; margin-bottom:12px; }
.section-sub { text-align:center; color:var(--text-light); font-size:1.05rem;
               max-width:700px; margin:0 auto 40px; }
.exec-grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(200px,1fr));
             gap:20px; margin-bottom:40px; }
.exec-card { background:var(--white); border-radius:var(--radius); padding:28px;
             box-shadow:var(--shadow); border-top:4px solid var(--granate); text-align:center; }
.exec-card .number { font-family:'Montserrat',sans-serif; font-size:2rem;
                     font-weight:900; color:var(--granate); }
.exec-card .label { font-size:.8rem; color:var(--text-light); margin-top:4px;
                    text-transform:uppercase; letter-spacing:1px; font-weight:600; }
.cost-table { width:100%; border-collapse:collapse; border-radius:12px; overflow:hidden;
              box-shadow:var(--shadow); margin:20px 0; }
.cost-table thead { background:var(--dark); color:#fff; }
.cost-table th { font-family:'Montserrat',sans-serif; font-weight:700; padding:14px 16px;
                 text-align:left; font-size:.85rem; text-transform:uppercase; letter-spacing:1px; }
.cost-table td { padding:14px 16px; border-bottom:1px solid var(--border);
                 font-size:.93rem; background:var(--white); }
.cost-table tr:last-child td { border:none; }
.cost-table .total-row td { background:#fef3c7; font-weight:700; border-top:2px solid var(--gold); }
.cost-table .profit-row td { background:#d1fae5; font-weight:700; color:var(--green);
                              border-top:2px solid var(--green); }
.scenario-grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(300px,1fr));
                 gap:24px; margin:20px 0; }
.scenario-card { background:var(--white); border-radius:var(--radius); box-shadow:var(--shadow);
                 overflow:hidden; }
.scenario-card .head { padding:16px 24px; font-family:'Montserrat',sans-serif; font-weight:700;
                       color:#fff; font-size:1rem; }
.scenario-card .body { padding:24px; }
.scenario-card .body ul { list-style:none; padding:0; }
.scenario-card .body li { padding:6px 0; border-bottom:1px solid #f0eeeb; font-size:.93rem; }
.scenario-card .body li:last-child { border:none; }
.head-ideal { background:var(--green); }
.head-real { background:var(--gold); }
.head-max { background:var(--red); }
.verdict-box { border-radius:var(--radius); padding:40px; text-align:center; color:#fff;
               background:linear-gradient(135deg,var(--green),#1a5c32); }
.verdict-box h2 { font-family:'Montserrat',sans-serif; font-size:1.8rem; font-weight:900;
                  margin-bottom:12px; }
.verdict-box p { font-size:1.05rem; opacity:.92; max-width:700px; margin:8px auto;
                 line-height:1.7; }
.rule-box { background:#fef3c7; border-left:4px solid var(--gold); border-radius:8px;
            padding:20px 28px; margin:24px 0; }
.rule-box h4 { font-family:'Montserrat',sans-serif; font-weight:700; color:var(--dark);
               margin-bottom:8px; }
footer { background:var(--dark); color:rgba(255,255,255,.6); text-align:center;
         padding:24px 0; font-size:.85rem; }
"""

PRODUCTO = "OilShield™"
PAIS = "Guatemala"

def generate():
    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Auditor Financiero — {PRODUCTO} {PAIS}</title>
<style>{CSS}</style>
</head>
<body>
<header class="header">
  <div class="container header-inner">
    <h1>ROOKIE 2 RICHES</h1>
    <span>@ecomjuliann</span>
  </div>
</header>
<div class="top-bar">AUDITOR FINANCIERO — VIABILIDAD ECONÓMICA</div>

<!-- RESUMEN -->
<section>
  <div class="container">
    <h2 class="section-title">Resumen de Viabilidad</h2>
    <p class="section-sub">Análisis financiero completo para {PRODUCTO} en {PAIS} — modelo COD.</p>
    <div class="exec-grid">
      <div class="exec-card" style="border-top-color:var(--green);">
        <div class="number" style="color:var(--green);">✅</div>
        <div class="label">Viable Financieramente</div>
      </div>
      <div class="exec-card">
        <div class="number">Q249</div>
        <div class="label">PV Aprobado (1 unidad)</div>
      </div>
      <div class="exec-card">
        <div class="number">40%</div>
        <div class="label">Margen Neto Estimado</div>
      </div>
      <div class="exec-card">
        <div class="number">Q99</div>
        <div class="label">CPA Máximo Permitido</div>
      </div>
    </div>
  </div>
</section>

<!-- DESGLOSE DE COSTOS -->
<section>
  <div class="container">
    <h2 class="section-title">Desglose de Costos por Unidad</h2>
    <p class="section-sub">Cada concepto desglosado para transparencia total.</p>
    <table class="cost-table">
      <thead><tr>
        <th>Concepto</th><th style="text-align:right;">Monto (Q)</th>
        <th style="text-align:right;">USD aprox.</th><th>Notas</th>
      </tr></thead>
      <tbody>
        <tr><td>Costo de Producto</td><td style="text-align:right;">Q45</td>
            <td style="text-align:right;">$5.50</td><td>Incluye empaque</td></tr>
        <tr><td>Flete Nacional (GT)</td><td style="text-align:right;">Q35</td>
            <td style="text-align:right;">$4.50</td><td>Promedio a zonas urbanas y rurales</td></tr>
        <tr><td>CPA Estimado (Meta Ads)</td><td style="text-align:right;">Q40</td>
            <td style="text-align:right;">$5.00</td><td>Base CPA $5 USD</td></tr>
        <tr><td>Provisión Devoluciones (12%)</td><td style="text-align:right;">Q30</td>
            <td style="text-align:right;">$3.85</td><td>Tasa GT: 12%. Incluye re-envío</td></tr>
        <tr class="total-row">
            <td>COSTO TOTAL POR UNIDAD</td><td style="text-align:right;">Q150</td>
            <td style="text-align:right;">$18.85</td><td>Base para cálculo de margen</td></tr>
        <tr class="profit-row">
            <td>GANANCIA NETA (PV Q249)</td><td style="text-align:right;">Q99</td>
            <td style="text-align:right;">$12.65</td><td>Margen: 39.8%</td></tr>
      </tbody>
    </table>
  </div>
</section>

<!-- PRECIOS APROBADOS -->
<section>
  <div class="container">
    <h2 class="section-title">Precios de Venta Aprobados</h2>
    <p class="section-sub">Estructura de precios por paquete — optimizada para AOV.</p>
    <table class="cost-table">
      <thead><tr>
        <th>Paquete</th><th style="text-align:center;">Unidades</th>
        <th style="text-align:right;">PV</th><th style="text-align:right;">PV/Unidad</th>
        <th style="text-align:right;">Margen</th><th style="text-align:right;">Margen %</th>
      </tr></thead>
      <tbody>
        <tr><td>Básico</td><td style="text-align:center;">1</td>
            <td style="text-align:right;">Q249</td><td style="text-align:right;">Q249</td>
            <td style="text-align:right;">Q99</td><td style="text-align:right;">39.8%</td></tr>
        <tr style="background:#d1fae5;">
            <td style="font-weight:700;">⭐ Familiar (Recomendado)</td><td style="text-align:center;">2</td>
            <td style="text-align:right;font-weight:700;">Q399</td><td style="text-align:right;">Q199.50</td>
            <td style="text-align:right;font-weight:700;color:var(--green);">Q249</td>
            <td style="text-align:right;font-weight:700;color:var(--green);">62.4%</td></tr>
        <tr><td>Flota</td><td style="text-align:center;">3</td>
            <td style="text-align:right;">Q549</td><td style="text-align:right;">Q183</td>
            <td style="text-align:right;">Q399</td><td style="text-align:right;">72.7%</td></tr>
      </tbody>
    </table>
    <div class="rule-box">
      <h4>⚖️ Regla de Oro del Auditor</h4>
      <p>Ningún agente puede modificar estos precios sin aprobación del Auditor Financiero.
         El paquete <strong>Familiar (x2)</strong> es el objetivo principal de conversión por su
         balance entre accesibilidad y margen.</p>
    </div>
  </div>
</section>

<!-- ESCENARIOS -->
<section>
  <div class="container">
    <h2 class="section-title">Escenarios de Rentabilidad</h2>
    <p class="section-sub">Tres escenarios según el CPA real obtenido en campaña.</p>
    <div class="scenario-grid">
      <div class="scenario-card">
        <div class="head head-ideal">🟢 ESCENARIO IDEAL — CPA Q30</div>
        <div class="body">
          <ul>
            <li><strong>CPA:</strong> Q30 ($3.85 USD)</li>
            <li><strong>Costo total:</strong> Q140</li>
            <li><strong>Ganancia/unidad:</strong> Q109</li>
            <li><strong>Margen:</strong> 43.8%</li>
            <li><strong>100 ventas/mes:</strong> Q10,900 de ganancia</li>
            <li><strong>Veredicto:</strong> Escalar agresivamente</li>
          </ul>
        </div>
      </div>
      <div class="scenario-card">
        <div class="head head-real">🟡 ESCENARIO REAL — CPA Q40</div>
        <div class="body">
          <ul>
            <li><strong>CPA:</strong> Q40 ($5.00 USD)</li>
            <li><strong>Costo total:</strong> Q150</li>
            <li><strong>Ganancia/unidad:</strong> Q99</li>
            <li><strong>Margen:</strong> 39.8%</li>
            <li><strong>100 ventas/mes:</strong> Q9,900 de ganancia</li>
            <li><strong>Veredicto:</strong> Saludable — optimizar creativos</li>
          </ul>
        </div>
      </div>
      <div class="scenario-card">
        <div class="head head-max">🔴 ESCENARIO MÁXIMO — CPA Q80</div>
        <div class="body">
          <ul>
            <li><strong>CPA:</strong> Q80 ($10.25 USD)</li>
            <li><strong>Costo total:</strong> Q190</li>
            <li><strong>Ganancia/unidad:</strong> Q59</li>
            <li><strong>Margen:</strong> 23.7%</li>
            <li><strong>100 ventas/mes:</strong> Q5,900 de ganancia</li>
            <li><strong>Veredicto:</strong> Ajustado — revisar audiencia y creativos</li>
          </ul>
        </div>
      </div>
    </div>
    <div class="rule-box">
      <h4>🚫 Punto de Detención</h4>
      <p>Si el CPA supera <strong>Q99</strong>, la operación deja de ser rentable. A partir de Q80,
         se recomienda pausar, revisar creativos y optimizar antes de continuar invirtiendo.</p>
    </div>
  </div>
</section>

<!-- VEREDICTO -->
<section style="background:var(--bg);">
  <div class="container">
    <div class="verdict-box">
      <h2>VEREDICTO FINANCIERO</h2>
      <h2 style="font-size:2.5rem;margin-top:8px;">✅ VIABLE — APROBADO PARA LANZAMIENTO</h2>
      <p>OilShield™ presenta un margen neto saludable del 40% en escenario base, con un CPA máximo
         de Q99 antes de break-even. La estructura de paquetes por cantidad (x2 Familiar) optimiza
         el AOV y lleva el margen a +62%. Se aprueba el lanzamiento bajo los precios establecidos.</p>
    </div>
  </div>
</section>

<footer>
  <p>Auditor Financiero — {PRODUCTO} {PAIS} — Generado automáticamente | ROOKIE2RICHES Framework</p>
</footer>
</body>
</html>"""
    return html

if __name__ == "__main__":
    html = generate()
    os.makedirs(os.path.dirname(OUT) or ".", exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅ Reporte Auditor generado: {os.path.abspath(OUT)}")
