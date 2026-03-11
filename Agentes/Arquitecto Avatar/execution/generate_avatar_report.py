#!/usr/bin/env python3
"""
generate_avatar_report.py — Arquitecto Avatar
Genera el HTML con el análisis profundo de avatares para un producto.
Estilo visual ROOKIE2RICHES (Montserrat, granate, cards premium).
Output: Arquitecto Avatar/reporte_avatares_<producto>_<pais>.html
"""
import os, re

def md_bold(text):
    """Convert **bold** markdown to <strong> HTML tags."""
    return re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)

BASE = os.path.dirname(os.path.abspath(__file__))
OUT  = os.path.join(BASE, "..", "reporte_avatares_oilshield_gt.html")

# ─────────────────────────────────────────────
# CSS
# ─────────────────────────────────────────────
CSS = """
* { box-sizing:border-box; margin:0; padding:0;
    user-select:text!important; -webkit-user-select:text!important; }
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800;900&family=Outfit:wght@400;500;600;700&display=swap');

:root {
  --bg: #f5f3f0;
  --white: #ffffff;
  --dark: #1a1a1a;
  --granate: #7a1f1f;
  --granate-light: #9b3333;
  --gold: #d4a03c;
  --gold-light: #f0d080;
  --text: #333333;
  --text-light: #666666;
  --green: #2d8a4e;
  --blue: #2563eb;
  --orange: #e67e22;
  --purple: #7c3aed;
  --border: #e0dcd7;
  --shadow: 0 4px 24px rgba(0,0,0,.08);
  --radius: 16px;
}
body { font-family:'Outfit',sans-serif; background:var(--bg); color:var(--text); line-height:1.6; }
.container { max-width:1100px; margin:0 auto; padding:0 24px; }

/* ── HEADER ── */
.header { background:var(--white); border-bottom:3px solid var(--granate); padding:16px 0; }
.header-inner { display:flex; justify-content:space-between; align-items:center; }
.header h1 { font-family:'Montserrat',sans-serif; font-size:1.5rem; font-weight:900;
             letter-spacing:2px; color:var(--dark); }
.header span { font-size:.9rem; color:var(--granate); font-weight:600; }

/* ── TOP BAR ── */
.top-bar { background:var(--granate); color:#fff; text-align:center; padding:14px 0;
           font-family:'Montserrat',sans-serif; font-weight:700; letter-spacing:4px;
           text-transform:uppercase; font-size:1rem; }

/* ── SECTION generic ── */
section { padding:48px 0; }
section:nth-child(even) { background:var(--white); }
.section-title { font-family:'Montserrat',sans-serif; font-weight:800;
                 font-size:1.8rem; color:var(--dark); text-align:center;
                 margin-bottom:12px; }
.section-sub { text-align:center; color:var(--text-light); font-size:1.05rem;
               max-width:700px; margin:0 auto 40px; }

/* ── RESUMEN EJECUTIVO ── */
.exec-grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
             gap:20px; margin-bottom:40px; }
.exec-card { background:var(--white); border-radius:var(--radius); padding:28px;
             box-shadow:var(--shadow); border-top:4px solid var(--granate);
             text-align:center; }
.exec-card .number { font-family:'Montserrat',sans-serif; font-size:2.5rem;
                     font-weight:900; color:var(--granate); }
.exec-card .label { font-size:.85rem; color:var(--text-light); margin-top:4px;
                    text-transform:uppercase; letter-spacing:1px; font-weight:600; }

/* ── AVATAR CARD ── */
.avatar-section { margin-bottom:56px; }
.avatar-header { display:flex; align-items:center; gap:20px; margin-bottom:28px;
                 padding:24px 32px; border-radius:var(--radius);
                 color:#fff; position:relative; overflow:hidden; }
.avatar-header::before { content:''; position:absolute; top:0; left:0; right:0; bottom:0;
                         background:linear-gradient(135deg,rgba(0,0,0,.15),transparent); }
.avatar-header * { position:relative; z-index:1; }
.avatar-header .emoji { font-size:3rem; }
.avatar-header h3 { font-family:'Montserrat',sans-serif; font-weight:800; font-size:1.4rem; }
.avatar-header .quote { font-style:italic; opacity:.9; margin-top:4px; font-size:1rem; }

.av-color-1 { background:linear-gradient(135deg,var(--granate),#4a1010); }
.av-color-2 { background:linear-gradient(135deg,var(--green),#1a5c32); }
.av-color-3 { background:linear-gradient(135deg,var(--blue),#1a3a8c); }
.av-color-4 { background:linear-gradient(135deg,var(--purple),#4c1d95); }
.av-color-5 { background:linear-gradient(135deg,#c0392b,#922b21); }
.av-color-6 { background:linear-gradient(135deg,#16a085,#0e6655); }

.profile-grid { display:grid; grid-template-columns:1fr 1fr; gap:20px; margin-bottom:28px; }
@media(max-width:768px) { .profile-grid { grid-template-columns:1fr; } }
.profile-card { background:var(--white); border-radius:12px; padding:24px;
                box-shadow:0 2px 12px rgba(0,0,0,.05); border-left:4px solid var(--border); }
.profile-card h4 { font-family:'Montserrat',sans-serif; font-weight:700; font-size:1rem;
                   margin-bottom:10px; color:var(--dark); display:flex; align-items:center; gap:8px; }
.profile-card ul { list-style:none; padding:0; }
.profile-card li { padding:5px 0; border-bottom:1px solid #f0eeeb; font-size:.95rem; }
.profile-card li:last-child { border:none; }
.profile-card li strong { color:var(--dark); }

/* ── ÁNGULOS TABLE ── */
.angles-table { width:100%; border-collapse:collapse; border-radius:12px; overflow:hidden;
                box-shadow:var(--shadow); margin-bottom:28px; }
.angles-table thead { background:var(--dark); color:#fff; }
.angles-table th { font-family:'Montserrat',sans-serif; font-weight:700; padding:14px 16px;
                   text-align:left; font-size:.85rem; text-transform:uppercase; letter-spacing:1px; }
.angles-table td { padding:14px 16px; border-bottom:1px solid var(--border); font-size:.93rem;
                   background:var(--white); }
.angles-table tr:last-child td { border:none; }
.angles-table .badge { display:inline-block; padding:3px 10px; border-radius:20px;
                       font-size:.75rem; font-weight:600; }
.badge-ugc { background:#e8f5e9; color:#2d8a4e; }
.badge-testi { background:#e3f2fd; color:#1565c0; }
.badge-compar { background:#fce4ec; color:#c62828; }
.badge-demo { background:#fff3e0; color:#e65100; }
.badge-emocional { background:#f3e5f5; color:#6a1b9a; }

/* ── MATRIZ ── */
.matrix-table { width:100%; border-collapse:collapse; border-radius:12px; overflow:hidden;
                box-shadow:var(--shadow); }
.matrix-table th, .matrix-table td { padding:12px 14px; text-align:center; font-size:.88rem; }
.matrix-table thead th { background:var(--dark); color:#fff; font-family:'Montserrat',sans-serif;
                         font-weight:700; text-transform:uppercase; letter-spacing:1px; }
.matrix-table tbody th { background:var(--granate); color:#fff; font-weight:600; text-align:left;
                         padding-left:16px; }
.matrix-table td { background:var(--white); border:1px solid var(--border); }
.cell-high { background:#e8f5e9!important; color:#2d8a4e; font-weight:700; }
.cell-mid  { background:#fff3e0!important; color:#e65100; font-weight:600; }
.cell-low  { background:#fafafa!important; color:#999; }

/* ── RECOMENDACIÓN ── */
.reco-box { background:linear-gradient(135deg,var(--granate),#4a1010); color:#fff;
            border-radius:var(--radius); padding:40px; text-align:center; }
.reco-box h3 { font-family:'Montserrat',sans-serif; font-size:1.6rem; font-weight:800;
               margin-bottom:16px; }
.reco-box p { max-width:700px; margin:0 auto; font-size:1.05rem; line-height:1.7; opacity:.92; }
.reco-priorities { display:flex; justify-content:center; gap:32px; margin-top:28px; flex-wrap:wrap; }
.reco-pill { background:rgba(255,255,255,.15); border:1px solid rgba(255,255,255,.3);
             border-radius:40px; padding:12px 28px; font-weight:700;
             font-family:'Montserrat',sans-serif; font-size:1rem; }
.reco-pill.gold { background:var(--gold); color:var(--dark); border-color:var(--gold); }

/* ── FOOTER ── */
footer { background:var(--dark); color:rgba(255,255,255,.6); text-align:center;
         padding:24px 0; font-size:.85rem; }
"""

# ─────────────────────────────────────────────
# AVATARES DATA
# ─────────────────────────────────────────────

PRODUCTO = "OilShield™"
PAIS = "Guatemala"
FECHA = "10 de Marzo, 2026"

avatares = [
    {
        "nombre": "Don Carlos — El Guardián del Orgullo",
        "emoji": "🏆",
        "quote": "Mi carro es mi carta de presentación. Si no brilla, no salgo.",
        "color": "av-color-1",
        "tipo": "Autorrealización / Emocional",
        "perfil": {
            "Edad y Perfil": "Hombre, 50-65 años. Padre de familia consolidado. Profesional, comerciante o jubilado activo. Vive en zonas urbanas (Mixco, Villa Nueva, Zona 10-14).",
            "Estilo de Vida": "Rutina ordenada: iglesia los domingos, reuniones familiares, paseos con la esposa. El carro es parte de su identidad — lo lava él mismo los sábados.",
            "Ingreso Mensual": "Q8,000 – Q20,000. No es rico, pero tiene para cuidar lo suyo. Gasta con criterio.",
            "Vehículo Típico": "Toyota Corolla 2012-2018, Nissan Sentra o Hyundai Tucson. Más de 5 años pero 'parece nuevo' porque lo cuida."
        },
        "psicografia": {
            "Valores Profundos": [
                "**Disciplina y orden** — Un hombre que no cuida su carro no cuida su vida",
                "**Herencia y ejemplo** — Quiere que sus hijos vean que las cosas se cuidan, no se desechan",
                "**Independencia** — 'No necesito pagar a nadie para esto. Yo me las arreglo solo'",
                "**Orgullo silencioso** — No lo dice, pero le encanta cuando le preguntan: '¿Acabás de comprar ese carro?'"
            ],
            "Motivaciones Emocionales (Neuroventas)": [
                "**Reconocimiento** — Que los vecinos, la familia y los colegas noten que su carro está impecable",
                "**Control** — Sentir que el deterioro del tiempo NO le gana",
                "**Satisfacción del 'DIY'** — La gratificación de hacerlo con sus propias manos",
                "**Nostalgia** — Recuperar la sensación de carro nuevo, de cuando lo sacó de la agencia"
            ],
            "Miedos y Bloqueos": [
                "Que el producto raye el vidrio (miedo #1 — necesita garantía explícita)",
                "Que sea solo 'agua con jabón caro' (necesita ver la ciencia/mecanismo)",
                "Pagar online — prefiere Pago Contra Entrega",
                "Que no funcione y haber 'perdido el pisto' frente a su esposa"
            ],
            "Comportamiento de Compra": [
                "Busca en Facebook, NO en Google — ve anuncios en su feed mientras descansa",
                "Lee comentarios y testimonios de gente como él (50+ años, guatemaltecos)",
                "Necesita ver un 'antes y después' para convencerse",
                "Compra por impulso emocional pero justifica con lógica ('me ahorro el lavadero')"
            ]
        },
        "angulos": [
            ("El Reflejo", "Tu carro dice mucho de vos. ¿Qué dice el tuyo ahora mismo?", "Orgullo / Identidad", "UGC Testimonio", "Empático, masculino, respetuoso"),
            ("Rejuvenecimiento", "Recuperá la transparencia de cuando lo sacaste de la agencia — en 5 minutos.", "Nostalgia / Satisfacción", "Demo Antes/Después", "Aspiracional, enfocado en resultado"),
            ("El Estándar", "Los hombres que cuidan lo suyo no dejan sus vidrios opacos.", "Masculinidad / Estándar", "Comparativo", "Directo, retador"),
            ("Hazlo Vos Mismo", "Sin lavaderos. Sin esperar. Sin pagar de más. Vos y 5 minutos.", "Independencia / Control", "UGC DIY", "Práctico, empoderador"),
            ("La Pregunta", "¿Cuánto llevas manejando con vidrios que no te dejan ver bien?", "Preocupación / Seguridad", "Emocional", "Provocador, reflexivo")
        ]
    },
    {
        "nombre": "Don Jorge — El Administrador Eficiente",
        "emoji": "💰",
        "quote": "Pisto ahorrado es pisto ganado. Y yo no boto el pisto.",
        "color": "av-color-2",
        "tipo": "Racional / Ahorro",
        "perfil": {
            "Edad y Perfil": "Hombre, 45-60 años. Trabajador asalariado o microempresario. Pragmático, calculador. Vive en zonas comerciales o periurbanas.",
            "Estilo de Vida": "Madrugador. Usa el carro para trabajar (repartidor, vendedor, transportista). El carro es herramienta, no lujo — pero lo cuida porque es su inversión.",
            "Ingreso Mensual": "Q5,000 – Q12,000. Cada quetzal cuenta. Odia los gastos 'invisibles' que no dan resultado.",
            "Vehículo Típico": "Pick-up Toyota Hilux, Nissan Frontier o sedan económico. El carro tiene polvo, grasa de carretera y aceite industrial."
        },
        "psicografia": {
            "Valores Profundos": [
                "**Eficiencia** — Busca el máximo resultado con el mínimo gasto",
                "**Desconfianza inteligente** — Asume que todo es 'caro para lo que es' hasta que pruebe lo contrario",
                "**Autosuficiencia** — 'Si puedo hacerlo yo, ¿para qué pago?'",
                "**Responsabilidad familiar** — El pisto que ahorra es pisto para la familia"
            ],
            "Motivaciones Emocionales (Neuroventas)": [
                "**Ahorro tangible** — Necesita ver el número: 'Te ahorrás Q150 por lavada'",
                "**Frustración resuelta** — Está HARTO de pagar lavaderos que no quitan la grasa real",
                "**Durabilidad** — Un producto que dura semanas, no horas, lo vuelve loco de felicidad",
                "**Inteligencia de compra** — Sentirse 'vivo' por encontrar algo bueno y barato"
            ],
            "Miedos y Bloqueos": [
                "Que sea un producto 'gringo caro' que no se adapta a Guatemala",
                "Que no funcione en el tipo de grasa de las carreteras centroamericanas",
                "Que tenga que comprar accesorios adicionales para que funcione",
                "Que las 'ofertas' sean solo trucos para cobrar más"
            ],
            "Comportamiento de Compra": [
                "Compara precios mentalmente — siempre calcula 'cuántas lavadas me ahorro'",
                "Lee las preguntas frecuentes antes de comprar",
                "Se convence con testimonios de gente trabajadora como él, no influencers",
                "Necesita la opción de Pago Contra Entrega — cero riesgo"
            ]
        },
        "angulos": [
            ("Costo por Lavada", "Dejá de regalar Q200 al lavadero cada mes. Hacélo vos por Q8 la aplicación.", "Ahorro / Lógica", "Comparativo de costos", "Directo, con números"),
            ("La Cuenta", "Un lavadero = Q150. OilShield = 30+ lavadas por Q249. Hacé la cuenta.", "Inteligencia financiera", "Infografía", "Práctico, calculador"),
            ("Frustración", "¿Pagaste Q200 y tu vidrio sigue con grasa? No sos vos, es el lavadero.", "Frustración / Validación", "UGC Testimonio", "Empático, agitador"),
            ("Triple Duración", "Una aplicación que dura 3-6 semanas. No horas, SEMANAS.", "Durabilidad / Eficiencia", "Demo con timer", "Enfático, impactante"),
            ("Inversión Inteligente", "Q249 que te ahorran más de Q1,800 al año en lavaderos. Eso sí es negocio.", "ROI / Pisto inteligente", "Testimonio + cálculo", "Calculador, convincente")
        ]
    },
    {
        "nombre": "Andrés — El Padre Protector",
        "emoji": "🛡️",
        "quote": "Bajo la lluvia de Guatemala, mi único miedo es no poder ver el camino.",
        "color": "av-color-3",
        "tipo": "Emocional / Seguridad",
        "perfil": {
            "Edad y Perfil": "Hombre, 35-50 años. Padre de hijos pequeños o adolescentes. Profesional de oficina o emprendedor. Maneja diario por la ciudad y carreteras.",
            "Estilo de Vida": "Rutina familiar intensa: llevar a los hijos al colegio, recoger a la esposa, viajes los fines de semana a Antigua, Panajachel o la costa. El carro es el 'refugio móvil' de la familia.",
            "Ingreso Mensual": "Q10,000 – Q25,000. Suficiente para invertir en la seguridad de su familia sin pensarlo dos veces.",
            "Vehículo Típico": "SUV familiar: RAV4, CRV, Tucson o Kia Sportage. Lo usa para todo — del colegio a la carretera."
        },
        "psicografia": {
            "Valores Profundos": [
                "**La familia primero** — Todo lo que hace es por proteger a los suyos",
                "**Prevención** — Prefiere gastar Q249 hoy que arriesgarse a un accidente",
                "**Responsabilidad silenciosa** — No dice 'tengo miedo', pero toma acción para eliminar riesgos",
                "**Modernidad práctica** — Está abierto a productos nuevos si resuelven un problema real"
            ],
            "Motivaciones Emocionales (Neuroventas)": [
                "**Paz mental** — Saber que va a VER bien la carretera aunque llueva fuerte",
                "**Protección activa** — Sentir que hizo algo concreto para proteger a su familia",
                "**Eliminación de ansiedad nocturna** — Las luces de noche en vidrios grasosos son su pesadilla",
                "**Confianza al volante** — Manejar relajado, no tenso y agarrado del timón"
            ],
            "Miedos y Bloqueos": [
                "Un accidente donde no pudo ver a tiempo — este es el miedo existencial",
                "Que el producto sea 'cosmético' y no mejore realmente la visibilidad",
                "No saber aplicarlo bien y dañar algo del vidrio",
                "Que sus hijos vayan atrás y él no pueda ver bien por la lluvia"
            ],
            "Comportamiento de Compra": [
                "Investiga un poco pero decide rápido si toca la fibra emocional correcta",
                "Le convence más un video de lluvia real que un testimonial de texto",
                "Compra por WhatsApp sin problema — está acostumbrado al e-commerce",
                "Si el producto promete seguridad para su familia, el precio es secundario"
            ]
        },
        "angulos": [
            ("El Aguacero", "El próximo aguacero no avisa. ¿Estás seguro que vas a ver el camino?", "Miedo / Anticipación", "Video lluvia real", "Urgente, provocador"),
            ("Cero Reflejos", "Eliminá el peligroso 'efecto espejo' que las luces de noche causan en vidrios grasosos.", "Miedo nocturno", "Demo noche", "Técnico, serio"),
            ("El Trayecto", "Del colegio a la casa, de la casa al trabajo. Tus hijos van atrás. ¿Ves bien?", "Responsabilidad", "Emocional familia", "Íntimo, paternal"),
            ("Prevención", "Q249 vs una consulta al mecánico por un golpe que pudiste evitar.", "Costo de NO actuar", "Comparativo emocional", "Lógico-emocional"),
            ("Tecnología Activa", "No es un limpiador. Es una capa nano-molecular que repele agua y aceite por semanas.", "Innovación / Confianza", "Demo técnica", "Científico, de autoridad")
        ]
    },
    {
        "nombre": "Kevin — El Detailer Amateur",
        "emoji": "✨",
        "quote": "Si no brilla, no es mío. Mis vidrios tienen que verse HD.",
        "color": "av-color-4",
        "tipo": "Aspiracional / Estética",
        "perfil": {
            "Edad y Perfil": "Joven, 22-35 años. Soltero o recién casado. Trabaja en ventas, servicio al cliente o tiene su propio negocio. Activo en redes sociales.",
            "Estilo de Vida": "Amante de los carros, sigue cuentas de detailing en Instagram y TikTok. Va a 'Car Meets' los fines de semana. Le importa lo que piensan los demás de su carro.",
            "Ingreso Mensual": "Q4,000 – Q10,000. No gana mucho pero prioriza su carro sobre otras cosas.",
            "Vehículo Típico": "Civic, Mazda 3, Golf o pickup modificada. El carro puede ser viejo pero está 'tuneado' o al menos super limpio."
        },
        "psicografia": {
            "Valores Profundos": [
                "**Imagen y estatus** — Tu carro habla por vos antes de que abrás la boca",
                "**Comunidad** — Pertenecer al grupo de los que 'sí cuidan su carro'",
                "**Knowledge** — Le encanta saber de productos, técnicas, hacks de limpieza",
                "**Perfeccionismo** — Un detalle sucio le arruina todo. Los vidrios opacos son inaceptables"
            ],
            "Motivaciones Emocionales (Neuroventas)": [
                "**Reconocimiento social** — Que le pidan consejos: '¿Qué le echás a tus vidrios?'",
                "**Efecto 'WOW'** — Que la gente se quede viendo su carro cuando pasa",
                "**Superioridad visual** — Tener los vidrios más limpios del parking o del Meet",
                "**Content Creation** — Quiere un resultado tan bueno que valga la pena filmarlo"
            ],
            "Miedos y Bloqueos": [
                "Que el producto sea 'de señor' y no sea cool compartirlo",
                "Que no se vea la diferencia en video/fotos — necesita resultado visual viral",
                "Que haya un producto mejor que él no conoce (FOMO inverso)",
                "Precio alto vs su presupuesto limitado — necesita la opción de 1 unidad"
            ],
            "Comportamiento de Compra": [
                "Compra desde TikTok o Instagram — casi nunca desde Facebook",
                "Se convence con reviews de otros 'detailers' o entusiastas, no con autoridades",
                "Le atraen los empaques premium y las marcas que 'se ven pro'",
                "Compra rápido si el hook visual es potente — menos de 3 segundos para decidir"
            ]
        },
        "angulos": [
            ("Full HD", "Dale a tus cristales un acabado Full HD. Los vidrios más limpios del Meet.", "Estatus / Perfección", "Demo satisfactorio", "Dinámico, informal, 'cool'"),
            ("El Hack", "El producto secreto que los detailers PRO no te cuentan. Ahora es tuyo.", "Exclusividad / Conocimiento", "UGC revelación", "Misterioso, insider"),
            ("Car Meet Ready", "Antes del Meet, una pasada de OilShield. Vidrios de showroom en 5 min.", "Comunidad / Preparación", "Lifestyle Meet", "Energético, comunitario"),
            ("Antes y Después Viral", "El 'before & after' más satisfactorio que vas a ver hoy. Mirá esto.", "Viralidad / WOW", "Video satisfactorio", "Hook viral, rápido"),
            ("Nivel PRO", "Dejá de usar productos de supermercado. Subí al nivel nano-molecular.", "Upgrade / Aspiración", "Comparativo productos", "Aspiracional, técnico")
        ]
    },
    {
        "nombre": "Doña María — La Madre Vigilante",
        "emoji": "👩‍👧‍👦",
        "quote": "Yo manejo con mis hijos. No puedo darme el lujo de no ver bien.",
        "color": "av-color-5",
        "tipo": "Seguridad / Maternal",
        "perfil": {
            "Edad y Perfil": "Mujer, 35-55 años. Madre de familia. Ama de casa activa, profesional o comerciante. Maneja diario para llevar a sus hijos al colegio, hacer mandados y trabajar.",
            "Estilo de Vida": "Rutina intensa: colegio, supermercado, reuniones. El carro es su herramienta de vida — lo usa más que nadie en la familia. Prefiere resolver sola antes que depender de otros.",
            "Ingreso Mensual": "Q6,000 – Q18,000 (propio o familiar). Administra el presupuesto del hogar con criterio. Gasta en lo que protege a su familia.",
            "Vehículo Típico": "Hatchback o sedan familiar: Yaris, Aveo, Hyundai Accent. O la SUV del esposo cuando llueve. Carro funcional, no de lujo."
        },
        "psicografia": {
            "Valores Profundos": [
                "**Protección maternal** — Sus hijos van atrás. Punto. No negocia la seguridad",
                "**Autonomía** — 'Yo puedo resolver esto sin pedirle a nadie'",
                "**Practicidad extrema** — Si no es fácil de usar, no le interesa",
                "**Responsabilidad del hogar** — Ella administra, ella decide, ella cuida"
            ],
            "Motivaciones Emocionales (Neuroventas)": [
                "**Tranquilidad al volante** — Manejar sin ansiedad cuando llueve de noche",
                "**Orgullo silencioso** — Mantener el carro limpio sin depender del esposo o del lavadero",
                "**Protección activa** — Sentir que hizo algo concreto por la seguridad de su familia",
                "**Eficiencia** — Una sola aplicación que dure semanas = menos cosas en su lista de pendientes"
            ],
            "Miedos y Bloqueos": [
                "Que sea difícil de aplicar — necesita ser simple, sin herramientas especiales",
                "Que raye o dañe el vidrio — miedo a estropear algo",
                "Que sea un 'producto de hombres' y no se sienta identificada",
                "Que tenga químicos fuertes o tóxicos — preocupación por los niños en el carro"
            ],
            "Comportamiento de Compra": [
                "Ve anuncios en Facebook e Instagram mientras descansa en la noche",
                "Le convencen los testimonios de otras mamás o mujeres que manejan",
                "Compra por WhatsApp o Pago Contra Entrega — cero riesgo",
                "Decide rápido si el producto resuelve un dolor real y es fácil de usar"
            ]
        },
        "angulos": [
            ("Mamá al Volante", "Llevás a tus hijos al cole todos los días. ¿Estás segura que ves bien cuando llueve?", "Miedo maternal / Protección", "UGC Testimonio mamá", "Empático, maternal, cercano"),
            ("Fácil y Rápido", "5 minutos. Sin herramientas. Sin ayuda. Vos sola podés hacerlo.", "Autonomía / Practicidad", "Demo tutorial", "Empoderador, directo, femenino"),
            ("Lluvia de Noche", "Esas luces que te ciegan en la noche + lluvia + vidrio grasoso = PELIGRO.", "Miedo nocturno / Seguridad", "Video lluvia real", "Urgente, serio, protector"),
            ("Sin Lavadero", "Dejá de esperar al fin de semana para limpiar tus vidrios. Hacélo vos en 5 min.", "Independencia / Eficiencia", "Demo antes/después", "Práctico, empoderador"),
            ("Carro Familiar Seguro", "Tu carro lleva lo más importante: tu familia. Que se vea y se sienta seguro.", "Seguridad / Valor familiar", "Emocional familia", "Emotivo, aspiracional")
        ]
    },
    {
        "nombre": "Sofía — La Profesional Moderna",
        "emoji": "💼",
        "quote": "Mi carro refleja quién soy. Limpio, ordenado y profesional.",
        "color": "av-color-6",
        "tipo": "Imagen / Profesional",
        "perfil": {
            "Edad y Perfil": "Mujer, 25-40 años. Profesional activa, emprendedora o ejecutiva. Soltera o casada sin hijos (o hijos pequeños). Vive en zonas urbanas (Zona 10-14, Carretera a El Salvador).",
            "Estilo de Vida": "Agenda ocupada: oficina, gym, reuniones, eventos sociales. El carro es extensión de su imagen profesional. Le importa la estética y el detalle.",
            "Ingreso Mensual": "Q12,000 – Q30,000. Tiene recursos para invertir en calidad. No busca lo más barato, busca lo mejor.",
            "Vehículo Típico": "Mazda CX-5, Kia Seltos, VW Tiguan o sedan moderno. Carro en buenas condiciones porque es parte de su imagen."
        },
        "psicografia": {
            "Valores Profundos": [
                "**Imagen profesional** — Su carro es su primera impresión ante clientes y colegas",
                "**Eficiencia** — Todo lo que ahorre tiempo es bienvenido. Su agenda no perdona",
                "**Calidad sobre precio** — Prefiere pagar más por algo que realmente funcione",
                "**Independencia** — No espera a que alguien le resuelva. Ella se encarga"
            ],
            "Motivaciones Emocionales (Neuroventas)": [
                "**Imagen impecable** — Llegar a una reunión con el carro brillante dice mucho de ella",
                "**Eficiencia de tiempo** — Una solución que dura semanas = una cosa menos en su agenda",
                "**Satisfacción personal** — El placer de tener todo bajo control y bien presentado",
                "**Seguridad vial** — Manejar con visibilidad perfecta, especialmente de noche"
            ],
            "Miedos y Bloqueos": [
                "Que sea un producto 'masculino' o feo — le importa el empaque y la presentación",
                "Que sea complicado o requiera fuerza — necesita ser fácil y elegante",
                "Que no se note la diferencia — necesita resultado visible para justificar la compra",
                "Que deje residuos o manchas — el vidrio debe quedar perfecto, no 'medio limpio'"
            ],
            "Comportamiento de Compra": [
                "Compra desde Instagram — sigue marcas premium y lifestyle",
                "Le convencen reviews de mujeres profesionales y videos de resultado satisfactorio",
                "Paga online sin problema — tarjeta de crédito, no necesita COD",
                "Investiga poco pero decide por calidad percibida: empaque, presentación, reviews"
            ]
        },
        "angulos": [
            ("Primera Impresión", "Tu carro habla antes que vos. ¿Qué dice con los vidrios opacos?", "Imagen / Profesionalismo", "Lifestyle profesional", "Sofisticado, aspiracional"),
            ("Sin Tiempo", "Agenda llena, cero tiempo para lavaderos. 5 minutos y vidrios perfectos por semanas.", "Eficiencia / Tiempo", "Demo rápida", "Directo, práctico, moderno"),
            ("Calidad Premium", "No es un limpiador genérico. Es tecnología nano-molecular para quien exige más.", "Calidad / Exclusividad", "Comparativo premium", "Elegante, de autoridad"),
            ("Noche Segura", "Reuniones de noche, carretera oscura, vidrios grasosos. OilShield elimina el riesgo.", "Seguridad nocturna", "Demo noche", "Serio, protector, directo"),
            ("Self-Care Automotriz", "Cuidás tu piel, tu pelo, tu ropa. ¿Por qué no cuidás tus vidrios?", "Self-care / Identidad", "UGC femenino", "Cercano, lifestyle, moderno")
        ]
    }
]

# ─────────────────────────────────────────────
# HTML GENERATORS
# ─────────────────────────────────────────────

def h_header():
    return f"""
    <header class="header">
      <div class="container header-inner">
        <h1>ROOKIE 2 RICHES</h1>
        <span>@ecomjuliann</span>
      </div>
    </header>
    <div class="top-bar">ARQUITECTO AVATAR — MAPA ESTRATÉGICO DE AUDIENCIAS</div>
    """

def h_resumen():
    cards = f"""
    <div class="exec-grid">
      <div class="exec-card">
        <div class="number">6</div>
        <div class="label">Avatares Identificados</div>
      </div>
      <div class="exec-card">
        <div class="number">30</div>
        <div class="label">Ángulos de Venta</div>
      </div>
      <div class="exec-card">
        <div class="number">♂♀</div>
        <div class="label">Tipos Psicográficos</div>
      </div>
      <div class="exec-card">
        <div class="number">🏹</div>
        <div class="label">Producto: {PRODUCTO}</div>
      </div>
    </div>
    <div style="background:var(--white);border-radius:var(--radius);padding:24px 32px;
                box-shadow:var(--shadow);max-width:800px;margin:0 auto;">
      <p style="font-size:1.05rem;line-height:1.8;color:var(--text);">
        <strong>Producto:</strong> {PRODUCTO} — Limpiador Nano-molecular de Película de Aceite<br>
        <strong>Mercado:</strong> {PAIS} (COD – Pago Contra Entrega)<br>
        <strong>Fecha de Análisis:</strong> {FECHA}<br>
        <strong>Metodología:</strong> Validación en mercados sofisticados (BR, USA, DE) + perfilamiento psicográfico
        con neuroventas + ángulos de venta por framework PAS/PRESTO.
      </p>
    </div>
    """
    return f"""
    <section>
      <div class="container">
        <h2 class="section-title">Resumen Ejecutivo</h2>
        <p class="section-sub">Análisis profundo de 6 perfiles psicográficos (4 masculinos + 2 femeninos) para {PRODUCTO} en {PAIS},
           con 5 ángulos de venta por avatar.</p>
        {cards}
      </div>
    </section>
    """

def h_avatar(av):
    # Profile cards
    profile_html = ""
    for k, v in av["perfil"].items():
        profile_html += f"""
        <div class="profile-card">
          <h4>📋 {k}</h4>
          <p style="font-size:.93rem;">{v}</p>
        </div>"""

    # Psychographic cards
    psico_html = ""
    icons = {"Valores Profundos": "💎", "Motivaciones Emocionales (Neuroventas)": "🧠",
             "Miedos y Bloqueos": "😰", "Comportamiento de Compra": "🛒"}
    for k, items in av["psicografia"].items():
        icon = icons.get(k, "📌")
        lis = "".join(f"<li>{md_bold(it)}</li>" for it in items)
        psico_html += f"""
        <div class="profile-card" style="border-left-color:var(--granate);">
          <h4>{icon} {k}</h4>
          <ul>{lis}</ul>
        </div>"""

    # Angles table
    badge_map = {"UGC": "badge-ugc", "Demo": "badge-demo", "Comparativ": "badge-compar",
                 "Testimon": "badge-testi", "Emocional": "badge-emocional",
                 "Infograf": "badge-demo", "Lifestyle": "badge-ugc", "Video": "badge-demo"}
    rows = ""
    for i, (name, hook, emo, fmt, tono) in enumerate(av["angulos"], 1):
        badge_cls = "badge-ugc"
        for key, cls in badge_map.items():
            if key.lower() in fmt.lower():
                badge_cls = cls
                break
        rows += f"""
        <tr>
          <td style="font-weight:700;">{i}. {name}</td>
          <td><em>"{hook}"</em></td>
          <td>{emo}</td>
          <td><span class="badge {badge_cls}">{fmt}</span></td>
          <td>{tono}</td>
        </tr>"""

    return f"""
    <div class="avatar-section">
      <div class="avatar-header {av['color']}">
        <div class="emoji">{av['emoji']}</div>
        <div>
          <h3>{av['nombre']}</h3>
          <div class="quote">"{av['quote']}"</div>
          <div style="margin-top:6px;font-size:.85rem;opacity:.8;">Tipo: {av['tipo']}</div>
        </div>
      </div>

      <h4 style="font-family:'Montserrat',sans-serif;font-weight:700;font-size:1.1rem;
                 margin-bottom:16px;color:var(--dark);">📋 Perfil Demográfico</h4>
      <div class="profile-grid">{profile_html}</div>

      <h4 style="font-family:'Montserrat',sans-serif;font-weight:700;font-size:1.1rem;
                 margin-bottom:16px;color:var(--dark);">🧠 Perfil Psicográfico</h4>
      <div class="profile-grid">{psico_html}</div>

      <h4 style="font-family:'Montserrat',sans-serif;font-weight:700;font-size:1.1rem;
                 margin-bottom:16px;color:var(--dark);">🎯 Ángulos de Venta (5)</h4>
      <table class="angles-table">
        <thead><tr>
          <th>Ángulo</th><th>Hook Sugerido</th><th>Emoción</th><th>Formato</th><th>Tono</th>
        </tr></thead>
        <tbody>{rows}</tbody>
      </table>
    </div>
    """

def h_matriz():
    rows = ""
    combos = [
        ("Autorrealización / Orgullo", "⭐⭐⭐", "⭐⭐", "⭐⭐", "⭐⭐⭐", "⭐", "⭐⭐⭐"),
        ("Ahorro / Eficiencia", "⭐⭐", "⭐⭐⭐", "⭐", "⭐", "⭐⭐⭐", "⭐"),
        ("Seguridad Familiar", "⭐⭐", "⭐", "⭐⭐⭐", "⭐", "⭐⭐⭐", "⭐⭐"),
        ("Estética / Estatus", "⭐⭐⭐", "⭐", "⭐", "⭐⭐⭐", "⭐", "⭐⭐⭐"),
        ("DIY / Independencia", "⭐⭐⭐", "⭐⭐⭐", "⭐⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐"),
        ("Imagen Profesional", "⭐⭐", "⭐", "⭐", "⭐⭐", "⭐", "⭐⭐⭐"),
        ("Protección Maternal", "⭐", "⭐", "⭐⭐⭐", "⭐", "⭐⭐⭐", "⭐⭐"),
    ]
    for ang, c1, c2, c3, c4, c5, c6 in combos:
        def cell(s):
            n = s.count("⭐")
            cls = "cell-high" if n >= 3 else ("cell-mid" if n == 2 else "cell-low")
            return f'<td class="{cls}">{s}</td>'
        rows += f"<tr><th>{ang}</th>{cell(c1)}{cell(c2)}{cell(c3)}{cell(c4)}{cell(c5)}{cell(c6)}</tr>"

    return f"""
    <section>
      <div class="container">
        <h2 class="section-title">Matriz Avatar × Ángulo</h2>
        <p class="section-sub">Cruza cada ángulo de venta con los 6 avatares para identificar
           la combinación de mayor impacto. ⭐⭐⭐ = Alta afinidad.</p>
        <table class="matrix-table">
          <thead><tr>
            <th>Ángulo de Venta</th>
            <th>🏆 Don Carlos<br><small>Orgullo</small></th>
            <th>💰 Don Jorge<br><small>Ahorro</small></th>
            <th>🛡️ Andrés<br><small>Protección</small></th>
            <th>✨ Kevin<br><small>Estética</small></th>
            <th>👩‍👧‍👦 Doña María<br><small>Maternal</small></th>
            <th>💼 Sofía<br><small>Profesional</small></th>
          </tr></thead>
          <tbody>{rows}</tbody>
        </table>
      </div>
    </section>
    """

def h_recomendacion():
    return """
    <section style="background:var(--bg);">
      <div class="container">
        <div class="reco-box">
          <h3>📌 Recomendación Estratégica de Lanzamiento</h3>
          <p>Para el lanzamiento inicial de OilShield™ en Guatemala, priorizar los
             <strong>Avatares 1 y 2</strong> (Don Carlos y Don Jorge, 45-65 años) —
             mayor poder adquisitivo, decisión de compra autónoma y afinidad natural
             con el producto. <strong>Doña María</strong> (Madre Vigilante) es el avatar
             femenino de mayor impacto — combina urgencia emocional con decisión de compra
             autónoma. <strong>Sofía</strong> (Profesional Moderna) es ideal para Instagram
             y audiencias de mayor ingreso. El <strong>Avatar 3</strong> (Padre Protector)
             y Doña María son ideales para campañas de temporada lluviosa (mayo-octubre).
             <strong>Kevin</strong> funciona como amplificador orgánico en TikTok.</p>
          <div class="reco-priorities">
            <div class="reco-pill gold">🥇 Don Carlos — PRIORIDAD 1</div>
            <div class="reco-pill gold">🥈 Don Jorge — PRIORIDAD 2</div>
            <div class="reco-pill gold">🥉 Doña María — PRIORIDAD 3</div>
            <div class="reco-pill">4° Andrés — Temporada Lluvia</div>
            <div class="reco-pill">5° Sofía — Instagram Premium</div>
            <div class="reco-pill">6° Kevin — Amplificador TikTok</div>
          </div>
        </div>
      </div>
    </section>
    """

def h_footer():
    return f"""
    <footer>
      <p>Arquitecto Avatar — {PRODUCTO} {PAIS} — Generado automáticamente | ROOKIE2RICHES Framework</p>
    </footer>
    """

# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────
def generate():
    avatares_html = ""
    for av in avatares:
        avatares_html += h_avatar(av)

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Arquitecto Avatar — {PRODUCTO} {PAIS}</title>
<style>{CSS}</style>
</head>
<body>
{h_header()}
{h_resumen()}
<section>
  <div class="container">
    <h2 class="section-title">Análisis Profundo de Avatares</h2>
    <p class="section-sub">6 perfiles psicográficos (4 masculinos + 2 femeninos) con motivaciones, miedos, comportamiento de compra
       y ángulos de venta específicos para {PRODUCTO} en {PAIS}.</p>
    {avatares_html}
  </div>
</section>
{h_matriz()}
{h_recomendacion()}
{h_footer()}
</body>
</html>"""
    return html

if __name__ == "__main__":
    html = generate()
    os.makedirs(os.path.dirname(OUT) or ".", exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅ Reporte de Avatares generado: {os.path.abspath(OUT)}")
