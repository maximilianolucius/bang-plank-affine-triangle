# Auditoría Ronda 3 — higiene, paper (`affine-plank-triangle.tex`), `notes/47` + Órdenes Ronda 4
> Auditor / Jefe de research: Claude. Fecha: 2026-07-01.
> Alcance: R3-3 (higiene), R3-1 (paper), R3-2 (`notes/47`). Método: referee + ejecución de scripts.

---

## Veredicto global

R3-3 y R3-2 **impecables**. El paper (R3-1) es **honesto y bien estructurado**, pero como
referee **lo rechazaría en la forma actual por un error de prueba** (Teorema faceta-paralelo,
§4) y varias correcciones de bibliografía/rigor. Nada de esto toca los resultados (son
ciertos); es la **redacción de una prueba** la que está mal. Detalle abajo.

---

## R3-3 (higiene) — VERIFICADO ✓

- **Scripts archivados** en `experiments/` (cierra la 3ª reincidencia de fuente efímera):
  `median_rigidity_enumeration.py`, `median_rigidity_centroid.py`, `median_tiling_gridsearch.py`,
  `median_generic_linsolve.py`, `bang_Nc_nogo_chord.py`, `median_edgetilings_independent.py`.
- **Corrí la enumeración simbólica** (`median_rigidity_enumeration.py`): exhaustiva sobre los
  27 patrones de cruce × todos los órdenes de trazas, resuelta exacto con `sympy`. Salida:
  **exactamente 3 soluciones** `{[0,⅓]³, [⅓,⅔]³, [⅔,1]³}`. **El `[PROVED]` de rigidez está
  genuinamente respaldado.** ✓
- **Enumeración independiente** (`median_edgetilings_independent.py`, método distinto, sin
  sympy): corrí D=6,12,18 → mismas 3. Doble verificación real. ✓
- `notes/36` cerrada sin contradicción (status + cola). ✓

## R3-2 (`notes/47`) — ACEPTADO, downgrade honesto ✓

Verifiqué la parte que va al paper: las medianas cíclicas de `Δ^d` tienen filas de `V` con
suma `(d+1)/2` ⟹ `V·centroide=½·1` ⟹ concurren en el centroide ∀d ⟹ satisfacen la
condición necesaria `1ᵀV⁻¹1=2`. **Correcto y dim-agnóstico.** El negativo (la medida del
perímetro NO da marginal uniforme en `d≥3`, dev 3.16) y el downgrade ("no es la extensión
limpia; solo la caracterización generaliza") son **honestos y correctos**. Sin overclaim.
Buen juicio: no forzó un teorema inexistente.

## R3-1 (el paper `affine-plank-triangle.tex`) — buen draft, PERO con defectos de referee

**Lo bueno:** alcance honesto ejemplar (Scope + Remark 1.2 sobre `2N−1`, "we claim no proof
of the conjecture"); estructura clara; el no-go (Thm G) y la rigidez de medianas (centerpiece)
bien presentados; abstract preciso. Supersede los `.tex` de la era tórica muerta. Compila.

### ⚠ ERROR DE PRUEBA (bloqueante) — Teorema faceta-paralelo (§4, `thm:facet`)
La prueba dice: *"along the edge from vertex $j$ to vertex $k$ each coordinate $\lambda_i$ is
affine onto $[0,1]$…"*. **Es FALSO.** En la arista `j→k`, solo `λ_j` y `λ_k` varían; para
`i∉{j,k}`, `λ_i≡0` (no es "onto `[0,1]`"). Una sola arista ve **2** coordenadas, no las `d+1`;
no puede dar `Σ_i|I_i|≥1` sobre todas las facetas. Además `"1∈∪_i I_i+(the sumset)"` es
notación corrupta.
**El teorema es cierto**, pero la prueba correcta es la de `notes/30`/`PROMPT-TWO-WALLS §2`:
punto libre `⟺ ∃λ∈Δ` con `λ_i∈F_i:=[0,1]\U_i` (`U_i`=unión de intervalos de planks ⊥ faceta
`i`); por **Brunn–Minkowski 1-D / sumset**, `1∈F_1+…+F_{d+1}` es lo que hay que negar, y
`1∉ΣF_i ⟹ ΣLeb F_i ≤ d ⟹ Σrw≥1`. **Reescribir la prueba** con este argumento (no la arista).

### Correcciones de rigor / bibliografía (referee)
1. **Rigidez "verified symbolically" (§5):** para publicación, o (a) prueba a mano de "exactamente
   3 edge-tilings", o (b) enunciarlo como **lema asistido por computador** citando el script
   archivado (`experiments/median_rigidity_enumeration.py`) + la verificación independiente. El
   caso genérico ya está a mano (`l_i=⅓`); faltan los patrones L/R a mano o como computer-assisted
   documentado. (No es error; es estándar de rigor.)
2. **`\bibitem{Bang53}`** "On covering by parallel-strips (two-plank case)" — **cita incompleta
   y vaga** (sin revista/año). Conseguir la referencia real de Bang 1953 o reformular la frase
   del intro sin citarla como ítem.
3. **`\bibitem{Verreault}`** título/fecha incorrectos: es *"Plank theorems and their applications:
   a survey"*, arXiv:2203.05540**v2 (2025)** (no "A survey of the plank problem", 2022).
4. **`\bibitem{Ambrus}`**: "manuscript, 2010" — correcto que es inédito; añadir la URL de Rényi.
5. Autor vacío (`\author{}`) — placeholder, ok para draft.

### Verificaciones que SÍ pasan (no tocar)
- Thm `1/d` (§2): prueba correcta (la verifiqué en rondas previas; pico marginal = `d/w` por
  BM). ✓
- Thm 3-facetas+1 (§3): prueba por fibras, **la audité línea a línea antes**, correcta. ✓
- Thm medianas (§5) cota (transporte) + rigidez (3 edge-tilings + centroide): **verificada**
  (enumeración corrida). ✓
- Prop concurrencia (§5, `prop:concur`): `Vp=½1`, correcta y dim-agnóstica (row-sum `(d+1)/2`
  verificado). ✓
- Thm no-go (§6): correcto; núcleo (presupuesto = cuerda más larga) verificado numéricamente. ✓

**Veredicto del paper:** contenido sólido y honesto; **1 prueba a reescribir (faceta-paralelo)**
+ hardening de la rigidez + limpieza de biblio. Tras eso, es un mid-tier sólido.

═══════════════════════════════════════════════════════════════════════
# ÓRDENES DE TRABAJO — RONDA 4
═══════════════════════════════════════════════════════════════════════

Contexto: el paper es el deliverable primario y está casi listo. El objetivo primario
"avanzar la conjetura / batir SOTA" solo tiene ya dos vías, ambas de investigación:
**(A) suficiencia de concurrencia** (tratable, template de Gardner, y **fortalece el paper**),
y **(B) certificado de acoplamiento** (moonshot, única vía a batir B-Y tras el no-go).

## R4-1 (OBLIGATORIO, rápido) — arreglar la prueba faceta-paralelo del paper
Reescribir `thm:facet` con el argumento correcto de sumset/BM-1D (`notes/30`), no el de la
arista. **Hecho:** prueba válida en el `.tex`.

## R4-2 (cierre paper) — hardening de rigidez + bibliografía
- Rigidez: prueba a mano de los patrones L/R **o** enunciar el lema como computer-assisted con
  cita al script archivado + la enumeración independiente.
- Corregir `Bang53`, `Verreault`, `Ambrus` (arriba). Rellenar autor/acks cuando corresponda.
**Hecho:** paper sin huecos de referee.

## R4-3 (referee pass completo) — una pasada final adversarial
Revisar cada prueba, notación y afirmación del `.tex` como referee hostil (todo `[PROVED]`
airtight; ningún uso de un `Problem/Conjecture` como probado). **Hecho:** checklist de referee.

## R4-4 (RESEARCH #1, tratable + fortalece el paper) — suficiencia de la familia de concurrencia
**El mayor upgrade real disponible.** Probar que `1ᵀV⁻¹1=2` + `p` interior ⟹ existe una medida
de marginal uniforme ⟹ `Σrw≥1` para **toda la familia de concurrencia** (positivo-dimensional,
incluye direcciones **genéricas no-faceta**). Eso convierte la Prop. de "necesaria" a **iff** y
da un teorema **nuevo y fuerte** (Bang para una familia genérica), muy por encima de "solo
medianas".
- **Template concreto:** la prueba de **Gardner Thm 1** (2 direcciones) construye la medida por
  múltiplos de Lebesgue lineal sobre segmentos (`refs/gardner1988`, `notes/43-P3`). Intentar
  extenderla a **3 direcciones concurrentes** (`cond=2`): la medida del perímetro (medianas) es
  el caso simétrico; buscar la construcción general por segmentos para `p` interior genérico.
- Backend exacto (no grid: el LP de suficiencia es grid-inestable, `notes/38/47`); usar dualidad
  de Kellerer analítica o construcción explícita.
**Entregable:** teorema "Σrw≥1 para la familia de concurrencia (d=2)", o reducción a un lema
nombrado. **Riesgo:** medio-alto (es el hueco finito de Gardner), pero **con template** y **alto
valor para el paper**. **Prioridad de investigación #1.**

## R4-5 (RESEARCH #2, moonshot) — certificado de acoplamiento (batir B-Y)
Única vía a la SOTA tras el no-go de `notes/44`. Testigo que NO sea el punto del sistema de
Bang: certificado de **celdas de escape + Farkas** (`notes/30 §8.5`), semilla = 6 celdas mixtas
(`notes/33 §6`); nugget = estabilidad transversal en el collar `R=1`. Anti-fabricación:
identidad SOS/Farkas exacta o intervalos certificados en TODO el collar. **Riesgo:** muy alto,
sin ruta conocida. Solo con capacidad sobrante.

---

## Prioridad
1. **R4-1 → R4-2 → R4-3** (cerrar el paper: es el entregable seguro y ya casi está).
2. **R4-4** (suficiencia de concurrencia): la mejor apuesta de investigación — tratable con el
   template de Gardner y **sube el techo del paper** de "medianas" a "familia genérica".
3. **R4-5** (acoplamiento): moonshot de fondo.

**Honestidad:** R4-4 es donde de verdad puede crecer el resultado sin entrar en el moonshot de
batir B-Y. Si R4-4 cae, el paper pasa de "casos sharp + rigidez" a "una familia
positivo-dimensional de direcciones genéricas con Bang probado" — un salto cualitativo real.
