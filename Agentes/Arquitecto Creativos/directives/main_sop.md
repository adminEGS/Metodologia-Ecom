# SOP: Arquitecto Creativos — Estrategia Visual y Copy de Alto Impacto
> Documento definitivo. Fuente única de verdad para la ideación de creativos que conviertan.
> El Arquitecto Creativos conceptualiza la narrativa visual: define la idea, el copy persuasivo y el CTA.

---

> ⚠️ **REGLA DE ORO — INVIOLABLE:** El output estándar de la landing page es siempre el HTML ROOKIE2RICHES generado por `execution/generate_report.py`. No existe ningún otro formato aceptado para entregar la estructura de ventas de una landing. Cada sección del HTML debe tener copy persuasivo real (no placeholders), aplicando las skills `ecom-copywriter` y `ecom-cro-expert`, guiándose por el PDF `ROOKIE2RICHES - ESTRUCTURA DE VENTAS 1 2.pdf`.

---

## 1. Objetivo
Producir todos los assets visuales y de video necesarios para:
1. **Landing Page** — Imágenes para cada sección (estructura ROOKIE2RICHES).
2. **Meta Ads** — Creativos de imagen y video con CTR > 2% y alta retención.
3. **TikTok Ads** — Creativos nativos con hook < 3 segundos y retención > 25%.

**Métrica clave:** Un creativo es exitoso si logra **CTR > 2%** y **Hook Rate > 30%** (% que pasan los 3 primeros segundos).

---

## 2. Entradas Requeridas
Antes de empezar, necesitás tener:
- [ ] SOP del Arquitecto de Landing del producto (para entender el producto, ángulo, avatar y mecanismo)
- [ ] Informe del Arquitecto Avatar (ángulos y motivaciones)
- [ ] Informe del Hunter (dolores y beneficios)
- [ ] Material gráfico disponible (fotos/videos del producto, si hay)
- [ ] País destino y contexto visual (ej. Guatemala = carros latinos, calles urbanas)
- [ ] Estructura ROOKIE2RICHES para las secciones de la landing

---

## 3. Las 3 Funciones del Arquitecto Creativos

### FUNCIÓN 0 (PRIMERO): Generar el HTML ROOKIE2RICHES de la Landing
### FUNCIÓN 1: Imágenes para la Landing Page
### FUNCIÓN 2: Creativos para Meta Ads (Facebook/Instagram)
### FUNCIÓN 3: Creativos para TikTok Ads

---

## 3b. FUNCIÓN 0 — Generación del HTML ROOKIE2RICHES (OBLIGATORIO PRIMERO)

> Esta es la función más importante. Antes de cualquier creativo, debe existir el HTML de la landing con copies reales.

### ¿Qué es el HTML ROOKIE2RICHES?
Es el documento HTML generado por `execution/generate_report.py` que sirve como:
1. **Guía definitiva de copy** para la landing page final.
2. **Referencia visual** para todos los creativos de Meta y TikTok.
3. **Brief de diseño** entregable al equipo o diseñador.

El archivo se genera en `.tmp/reporte_rookie2riches_[producto]_[pais].html`.

### Secciones Obligatorias del HTML (en este orden)

El PDF `ROOKIE2RICHES - ESTRUCTURA DE VENTAS 1 2.pdf` es la guía visual. Cada sección tiene un copy específico:

| # | Sección HTML | Función de Copy | Skill a Aplicar |
|---|---|---|---|
| 1 | **Top Bar** | Beneficio logístico — Envío gratis + pago al recibir | ecom-cro-expert |
| 2 | **Hero** | H1 con promesa transformación + precio + checklist | ecom-copywriter (PAS) |
| 3 | **Garantías** | 3 sellos de confianza + logos autoridad | ecom-cro-expert |
| 4 | **Transformación** | 3 pasos del proceso con verbo acción + resultado | ecom-copywriter (PRESTO-S) |
| 5 | **Autoridad** | Dato científico/técnico que justifica el mecanismo | ecom-copywriter (PRESTO-R+E) |
| 6 | **Beneficios Grid** | 6 beneficios: resultado emocional + dato concreto | ecom-copywriter |
| 7-12 | **6 Beneficios Expandidos** | Uno por uno: dolor → beneficio → prueba → CTA | ecom-copywriter (PAS por sección) |
| 13 | **¿Cómo Usarlo?** | 4 pasos simples + tip profesional | ecom-cro-expert |
| 14 | **Características Técnicas** | 6 specs con badge rojo + explicación en lenguaje simple | ecom-copywriter |
| 15 | **Comparativa** | Nosotros vs competencia vs alternativa | ecom-cro-expert |
| 16 | **Testimonios** | 6 testimonios reales o redactados como reales | ecom-copywriter |
| 17 | **¿Qué Incluye?** | Lista de todo lo que recibe + valor percibido | ecom-cro-expert |
| 18 | **Logística** | Transportadoras + tiempo de entrega + contra entrega | ecom-cro-expert |
| 19 | **Oferta Escalada** | 3 paquetes con precio tachado + el mejor destacado | ecom-cro-expert |
| 20 | **FAQ** | 7 preguntas que destruyen las objeciones principales | ecom-copywriter + ecom-cro-expert |
| 21 | **CTA Final** | Cierre agresivo con toda la promesa resumida | ecom-copywriter |

### Reglas de Copy por Sección (INVIOLABLES)

**Skill: ecom-copywriter**
- Usar siempre **PAS** (Problema → Agitación → Solución) en la sección Hero y en cada Beneficio Expandido.
- Usar **PRESTO** en la sección de Autoridad y Transformación.
- Beneficios = resultados emocionales con dato numérico concreto: `"Ahorrás Q1,200 al año"`, no `"te ahorrás dinero"`.
- Lenguaje local del país: Guatemala = voseo (`"guardás"`, `"pagás"`, `"ves"`), moneda Q, referencias locales.
- Siempre incluir prueba social específica: `"+3,800 conductores"`, no `"miles de clientes"`.

**Skill: ecom-cro-expert**
- Hero: Precio tachado visible + badge de descuento + botón negro `"PAGAR AL RECIBIR — SIN TARJETA"`.
- Comparativa: 3 columnas (opción nuestra destacada en rojo granate con ✔ verdes, competencia con ✗ grises).
- Oferta escalada: 3 paquetes — básico / popular (MÁS POPULAR destacado) / flota. Precios con comparativo tachado.
- FAQ: Mínimo 7 preguntas. Las 3 primeras deben destruir los miedos de pago y entrega.
- Cada sección debe tener al menos 1 CTA intermedio negro con subtexto de ahorro.

### Proceso de Generación del HTML

```
PASO 1: Leer inputs del producto
  → Avatar (dolores, motivaciones, lenguaje exacto)
  → Ángulo de venta definido (Ahorro / Salud / Conveniencia / Status)
  → Mecanismo distintivo con nombre tecnológico
  → Precios, paquetes y garantías confirmadas

PASO 2: Aplicar skills para redactar cada sección
  → ecom-copywriter: Hero, Beneficios, Testimonios, FAQ, CTA Final
  → ecom-cro-expert: Top Bar, Garantías, Comparativa, Oferta, Logística

PASO 3: Integrar copy en generate_report.py
  → Editar los textos de las funciones correspondientes
  → Nunca usar placeholders vagos — siempre copy real finalizado

PASO 4: Ejecutar el script
  → python3 execution/generate_report.py
  → Output: .tmp/reporte_rookie2riches_[producto]_[pais].html

PASO 5: Verificar en el navegador
  → Abrir el HTML y revisar que cada sección tenga copy real
  → Confirmar que el texto es seleccionable (copy-paste habilitado)
```

### Inputs Mínimos Requeridos para Ejecutar la Función 0
```
- Nombre del producto y nombre tecnológico del mecanismo
- País de venta + moneda + método de pago (contra entrega)
- Precio normal y precio oferta
- Ángulo de venta principal (ej. "Ahorro de Dinero")
- Descripción del avatar (quién es, qué dolor tiene, lenguaje que usa)
- Número de unidades vendidas o de reseñas (para prueba social)
- Paquetes de oferta (básico, popular, flota) con precios
- Garantía (días de devolución)
```

---

## 4. FUNCIÓN 1 — Imágenes para la Landing Page

### Estructura de un Brief Creativo para Landing:
```
BREVE CREATIVO — [SECCIÓN]
Idea Visual: [Descripción de qué debe mostrar la imagen para conectar con el avatar]
Copy en Imagen: [Texto persuasivo exacto que debe llevar el diseño]
Subtexto/Bullet: [Refuerzo de valor o prueba social]
Llamado a la Acción: [CTA imperativo y específico]
Objetivo Psicológico: [Por qué esta imagen ayuda a vender: Ahorro, Miedo, Estatus, etc.]
```

### El nuevo estándar: El "Hero Quinteto" (5 Imágenes Visuales)
La sección Hero no es una imagen, es un embudo visual en 5 slides:
1. **Gancho/Atención**: Producto + Promesa principal + Precio irresistible.
2. **Problema/Dolor**: El "Antes" sucio o el gasto innecesario que el avatar odia.
3. **Solución/Mecanismo**: El producto en acción "curando" el problema.
4. **Prueba/Confianza**: Testimonio + Garantías de hierro + Quedan pocos.
5. **Oferta/Cierre**: Bundle completo + CTA de pago al recibir.

---

## 5. FUNCIÓN 2 — Creativos para Meta Ads

### 5.1 Formatos obligatorios (generar mínimo 1 de cada uno)

| Formato | Tipo | Descripción | Mejor para |
|---|---|---|---|
| **A. Problem/Solution** | Video 15-30s | Mostrar problema → solución rápida | Conversión |
| **B. UGC (User Generated Content)** | Video 15-45s | Persona real probando el producto | Confianza |
| **C. Comparativo** | Imagen o Video | Nosotros vs Alternativa (lado a lado) | Diferenciación |
| **D. Antes/Después** | Imagen carrusel o Video | Transformación visual dramática | Engagement |
| **E. Testimonio** | Video 15-30s | Cliente real contando su experiencia | Prueba social |
| **F. Estático de Oferta** | Imagen | Producto + precio + beneficios + CTA | Retargeting |

### 5.2 Estructura de un creativo de video (Meta)

```
HOOK (0-3s)     → Detener el scroll. Visual o auditivo impactante.
PROBLEMA (3-8s) → Agitar el dolor del avatar.
SOLUCIÓN (8-15s)→ Mostrar el producto en acción.
PRUEBA (15-22s) → Resultado visible o testimonio rápido.
CTA (22-30s)    → Instrucción clara + oferta + pago al recibir.
```

### 5.3 Tipos de HOOKS (Los primeros 3 segundos)

**El hook determina el 80% del rendimiento del creativo.** Generar mínimo 5 hooks por producto.

| Tipo de Hook | Fórmula | Ejemplo |
|---|---|---|
| **Negativo** | "¿Sabías que estás [error común]?" | "¿Sabías que estás lavando tu carro para NADA?" |
| **Resultado** | "Mirá cómo [transformación] en [tiempo]" | "Mirá cómo este parabrisas pasa de opaco a cristalino en 10 segundos" |
| **Social** | "La razón por la que [X personas] ya [acción]" | "La razón por la que +3,800 conductores dejaron el lavadero" |
| **Curiosidad** | "[Dato sorprendente] que nadie te dice" | "El 89% de los lavaderos NO limpian esto de tu parabrisas" |
| **Autoridad** | "[Experto/estudio] confirma que..." | "Los ingenieros de SAE International confirman que el jabón no funciona" |
| **POV** | "POV: Descubriste [solución] y ahora [resultado]" | "POV: Descubriste OilShield y ahora ves perfecto de noche" |
| **Contraste** | "Izquierda: [sin producto] / Derecha: [con producto]" | Split screen antes/después |
| **Pregunta directa** | "¿[Problema del avatar]?" | "¿Tu parabrisas parece que tiene una capa de grasa que nunca se va?" |

### 5.4 Especificaciones técnicas por formato Meta

| Formato | Tamaño | Duración | Texto |
|---|---|---|---|
| Feed imagen | 1080×1080 (1:1) | — | Primary text: 125 chars, Headline: 40 chars |
| Feed video | 1080×1080 (1:1) | 15-30s | Subtítulos obligatorios |
| Story/Reel | 1080×1920 (9:16) | 15-30s | Texto en zona segura |
| Carrusel | 1080×1080 (×3-5) | — | Cada slide con copy progresivo |

---

## 6. FUNCIÓN 3 — Creativos para TikTok Ads

### 6.1 Diferencias clave vs Meta
- **Nativo:** Debe parecer contenido orgánico, NO publicidad.
- **Vertical:** Siempre 9:16.
- **Audio:** La música/sonido es CRÍTICO (usar trending sounds).
- **Ritmo:** Más rápido que Meta. Cortes cada 2-3 segundos.
- **Texto en pantalla:** Siempre. El usuario puede tener el sonido apagado.

### 6.2 Formatos TikTok

| Formato | Descripción | Duración |
|---|---|---|
| **Demo rápida** | Producto en acción, resultado inmediato | 10-15s |
| **Storytelling** | Mini-historia: problema → descubrimiento → resultado | 20-30s |
| **POV** | "POV: [situación relatable]" + transformación | 10-20s |
| **Reacción** | Reacción exagerada al ver el resultado | 10-15s |
| **Review honesto** | "Probé este producto viral y..." | 15-30s |
| **Trend adaptation** | Adaptar un trend/sound actual al producto | 10-20s |

### 6.3 Estructura de video TikTok
```
HOOK VISUAL (0-1.5s) → Imagen o movimiento que OBLIGUE a detenerse.
CONTEXTO (1.5-5s)    → "Encontré esto para [problema]" — tono casual.
DEMO (5-15s)         → Producto en acción con resultado visible.
RESULTADO (15-20s)   → Reacción genuina + dato de ahorro/beneficio.
CTA NATIVO (20-25s)  → "El link está en el perfil" o "Comenta INFO".
```

---

## 7. Reglas de Alto CTR y Retención

### 7.1 Reglas de diseño visual
1. **Contraste alto** — Elementos claros sobre fondos oscuros (o viceversa) para detener el scroll.
2. **Texto grande** — Legible en móvil sin esfuerzo. Mínimo 48px en imagen 1080px.
3. **Colores de marca** — Usar la paleta definida en el SOP de landing.
4. **Elemento humano** — Las imágenes con personas generan 2x más engagement que solo producto.
5. **Zona segura** — No poner texto en los 150px superiores/inferiores (UI de la plataforma los tapa).

### 7.2 Reglas de copy en creativos
1. **Beneficio en el hook, no característica** — "Ve perfecto de noche" > "Fórmula nano-molecular".
2. **Números concretos** — "5 minutos", "Q1,200 al año", "+3,800 conductores".
3. **Primera persona** — "Dejé de gastar en el lavadero" > "Este producto limpia".
4. **Urgencia real** — "Últimas unidades", "Oferta solo esta semana".
5. **CTA con método de pago** — Siempre incluir "Pago al recibir" o "Sin tarjeta".

### 7.3 Reglas de retención en video
1. **Corte cada 2-3 segundos** — Mantener la atención con cambios de ángulo/toma.
2. **Movimiento constante** — Sin tomas estáticas largas.
3. **Subtítulos siempre** — 80% de usuarios ven sin sonido.
4. **Reveal progresivo** — No mostrar todo de una. Generar expectativa.
5. **Loop** — Que el final conecte con el inicio para que se repita automáticamente.

---

## 8. Formato de Entregables

### 8.1 Brief Creativo (por cada creativo)
```
BRIEF CREATIVO #[N]
═══════════════════════════════════════
Producto:       [Nombre del producto]
Plataforma:     [Meta / TikTok / Landing]
Formato:        [Video 15s / Imagen 1:1 / Carrusel / etc.]
Tipo:           [Problem/Solution / UGC / Comparativo / etc.]
Ángulo:         [Ahorro / Salud / Conveniencia / etc.]
Avatar:         [Descripción corta del target]
───────────────────────────────────────
HOOK (0-3s):    [Texto/Visual del gancho]
BODY (3-20s):   [Descripción de lo que pasa]
CTA:            [Texto exacto del llamado a acción]
───────────────────────────────────────
TEXTO:
  Primary text: [Copy principal del ad]
  Headline:     [Título corto]
  Description:  [Descripción del link]
───────────────────────────────────────
NOTAS DE EDICIÓN:
  Música:       [Tipo de música/sound]
  Ritmo:        [Rápido/Medio/Lento]
  Subtítulos:   [Sí/No, estilo]
  Filtros:      [Si aplica]
═══════════════════════════════════════
```

### 8.2 Concepto Creativo para Imagen (Landing/Ads)
```
CONCEPTO CREATIVO #[N]
═══════════════════════════════════════
Para:           [Sección de Landing / Meta Ad / TikTok]
Ángulo:         [Ahorro / Seguridad / Comodidad]
Idea Visual:    [Descripción clara para el diseñador/editor]
Texto Principal: [Copy persuasivo para la imagen]
Subtexto:       [Dato o garantía de refuerzo]
CTA:            [Botón o instrucción de acción]
Coherencia:     [Cómo conecta con la sección X de la landing]
═══════════════════════════════════════
```

### 8.3 Guión de Video
```
GUIÓN DE VIDEO #[N]
═══════════════════════════════════════
Duración:       [15s / 30s / 45s]
Plataforma:     [Meta / TikTok / Ambas]
Formato:        [Vertical 9:16 / Cuadrado 1:1]
───────────────────────────────────────
[0-3s]  HOOK:
  Visual: [Qué se ve en pantalla]
  Audio:  [Qué se escucha / voz en off]
  Texto:  [Texto overlay]

[3-8s]  PROBLEMA:
  Visual: [Qué se ve]
  Audio:  [Narración]
  Texto:  [Texto overlay]

[8-18s] SOLUCIÓN:
  Visual: [Producto en acción]
  Audio:  [Narración]
  Texto:  [Texto overlay]

[18-25s] PRUEBA:
  Visual: [Resultado / Testimonio]
  Audio:  [Narración]
  Texto:  [Dato de impacto]

[25-30s] CTA:
  Visual: [Producto + oferta]
  Audio:  [Instrucción clara]
  Texto:  [CTA + precio + pago al recibir]
───────────────────────────────────────
NOTAS DE PRODUCCIÓN:
  Música: [Referencia o tipo]
  Transiciones: [Cortes rápidos / Zoom / etc.]
  Edición: [Notas adicionales]
═══════════════════════════════════════
```

---

## 9. Proceso de Trabajo

### Paso 1: Leer las entradas
- Revisar el SOP del Arquitecto de Landing del producto para entender: producto, ángulo, avatar, mecanismo, precios, garantías, beneficios.

### Paso 2: Generar prompts de imágenes para Landing
- Seguir la tabla de la sección 4. Generar 1 prompt por cada sección obligatoria.

### Paso 3: Generar Briefs de Meta Ads
- Crear mínimo **6 briefs creativos** (1 por formato: Problem/Solution, UGC, Comparativo, Antes/Después, Testimonio, Estático de Oferta).
- Cada brief incluye: hook, body, CTA, textos del ad, notas de edición.

### Paso 4: Generar Briefs de TikTok Ads
- Crear mínimo **4 briefs creativos** (Demo rápida, Storytelling, POV, Review honesto).
- Adaptar al tono nativo de TikTok.

### Paso 5: Generar Hooks
- Producir mínimo **8 variaciones de hooks** usando la tabla de tipos.
- Estos hooks se reutilizan en Meta y TikTok.

### Paso 6: Compilar entregable
- Archivo único con todos los briefs, prompts y guiones organizados.

---

## 10. Coherencia con la Landing

> **REGLA CRÍTICA:** El creativo debe prometer EXACTAMENTE lo mismo que la landing.

| Elemento | Landing → Creativo |
|---|---|
| Promesa principal (H1) | = Hook del creativo |
| Mecanismo distintivo | = Explicación en el body |
| Precio y oferta | = CTA del creativo |
| Garantías | = Reducer de objeciones |
| Testimonios | = Material para formato UGC |
| Comparativa | = Material para formato comparativo |

Si el creativo promete algo que la landing no cumple = **rebote alto**. Si la landing tiene algo que el creativo no anticipó = **oportunidad perdida**.

---

## 11. Checklist Final

- [ ] Prompts de imágenes para todas las secciones de landing (mín. 12)
- [ ] 6 briefs creativos para Meta Ads (1 por formato)
- [ ] 4 briefs creativos para TikTok Ads
- [ ] 8+ hooks variados (diferentes tipos)
- [ ] Textos de ads (primary text + headline + description) por creativo
- [ ] Guiones de video con timestamps
- [ ] Todo coherente con la landing (misma promesa, precio, garantías)
- [ ] Contextualizado al país destino (personas, escenarios, lenguaje)
- [ ] Especificaciones técnicas correctas por plataforma

---

## 12. Límites
- **No se limita a prompts:** Su valor es la **estrategia narrativa**. Los prompts son secundarios; la idea y el copy mandan.
- **Coherencia obligatoria:** No inventar beneficios, precios o promesas que no estén en la landing.
- **Respeto al avatar:** Usar el tono, lenguaje y contexto definido por el Arquitecto Avatar.
- **Copy real siempre:** Prohibido usar placeholders o textos genéricos en el HTML. Si no hay información, pedirla antes de escribir.
- **HTML primero:** Ningún creativo de Meta o TikTok puede existir antes de tener el HTML ROOKIE2RICHES aprobado. El HTML es la fuente de verdad de toda la narrativa.

---

## 13. Archivos de Referencia del Sistema

| Archivo | Propósito |
|---|---|
| `execution/generate_report.py` | Script Python que genera el HTML ROOKIE2RICHES |
| `.tmp/reporte_rookie2riches_*.html` | Output generado — brief de copy de la landing |
| `ROOKIE2RICHES - ESTRUCTURA DE VENTAS 1 2.pdf` | Guía visual de referencia de estructura y diseño |
| `skill-creator/ecom-copywriter/SKILLCopywriter.md` | Skill de copywriting (PAS, PRESTO, hooks) |
| `skill-creator/ecom-cro-expert/SKILLConvertion.md` | Skill de CRO (estructura, oferta, objeciones) |
