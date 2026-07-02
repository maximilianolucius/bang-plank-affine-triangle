# Auditoría de la Ronda 2 (notas `44`, `45`, `46`) + Órdenes Ronda 3
> Auditor / Jefe de research: Claude. Fecha: 2026-07-01.
> Notas: `44-R2-1-bang-Nc-nogo`, `45-R2-2-rigidez-medianas-COMPLETA`, `46-R2-4-esqueleto-paper`.
> Método: referee + verificación numérica del núcleo del no-go.

---

## Veredicto global

Ronda muy fuerte. El resultado central —el **no-go de R2-1**— es **correcto y lo verifiqué**;
es un hallazgo estructural genuino (no un fracaso). La rigidez de medianas quedó **completa
y limpia**. El esqueleto del paper es honesto. **Consecuencia estratégica dura: la única vía
incremental para batir B-Y (el `N_c`) está muerta; el objetivo primario "batir B-Y" ya no
tiene ruta tratable conocida.** Reoriento el trabajo hacia el deliverable. Dos defectos de
higiene reinciden (scripts efímeros, parche parcial en `notes/36`).

---

## `notes/44` — NO-GO de R2-1: **ACEPTADO y VERIFICADO** ✓✓

**Claim:** rehacer el argumento de signos de Bang (Lema 2.3–2.5 de Verreault) con `N_c` en vez
de la cuerda `ℓ` no puede dar `c>0`; el presupuesto de movimiento del testigo `x_ε=x_0+Σε_j u_j`
es exactamente la **semi-cuerda más larga** `ℓ(u)/2`, y `N_c≥ℓ` pide superarla.

**Verificación (mía, numérica).** Para el triángulo equilátero, en varias direcciones,
computé el mayor `|u|` tal que `x_0±u∈C` para algún `x_0` (el presupuesto del testigo) y la
cuerda más larga:
```
dir       longest_chord   2·max|u|_feasible
(1,0)        1.00            0.98
(0,1)        0.87            0.85
(1,1)        0.90            0.88
(0.3,0.9)    0.91            0.89
```
`2·max|u| ≈ cuerda más larga` en todas (discrepancia ≤0.03 = ruido del paso de marcha 0.002).
**Confirmado: el presupuesto del testigo de Bang = la cuerda más larga.** El argumento
`(C−u)∩(C+u)≠∅ ⟺ C contiene un segmento de longitud `2|u|` paralelo a `u` ⟺ `2|u|≤ℓ(u)` es
correcto. Y `ℓ≤w` siempre (`ρ=ℓ/w≤1`). **`c*=0` para el método de Bang: PROBADO.**

**Calidad del razonamiento:** correcto que es un **no-go de método, no de la afirmación**
(`S_c≥1` para `c>0` sigue `[OPEN]`, indemostrable por Bang pero no refutado). Coincide con el
techo de B-Y (sharp en el cubo vía `ℓ/w`). **Conclusión estratégica correcta y firme:** batir
B-Y exige un testigo de **acoplamiento** (no el punto del sistema de Bang, confinado a
cuerdas) — exactamente el certificado "escape-de-TODAS + posición-dependiente" de `notes/23 E`.

Este no-go es un resultado publicable por sí mismo (Teorema G del paper) y **ahorra esfuerzo
futuro**: cierra la ruta natural. Excelente trabajo.

## `notes/45` — Rigidez de medianas COMPLETA: **ACEPTADO** (con higiene) ✓

**Lógica (correcta):** igualdad `Σr=1` ⟹ partición del perímetro ⟹ (enumeración exacta) el
edge-tiling tiene exactamente 3 soluciones `{MMM=[⅓,⅔], LLL=[0,⅓], RRR=[⅔,1]}` ⟹ solo MMM
cubre el interior (centroide `m(G)=(½,½,½)`; `½∉[0,⅓]` y `½∉[⅔,1]` matan LLL/RRR). ⟹ MMM único.

Verifiqué a mano que **LLL es un edge-tiling genuino** (en AB: `P2=[0,⅓]`, `P1=[⅓,1]`, `P3=∅`;
tesela) y que el **centroide lo mata** (`½∉[0,⅓]`). El "centroide como testigo interior" es
limpio y citable. La reducción de `auditorias/39 §A.1` (faltaba el interior) queda **cerrada**:
el interior entra vía el centroide. **Rigidez [PROVED] completa: aceptada.**

**⚠ Higiene (bloqueante para el paper):** el paso clave "exactamente 3 edge-tilings" descansa
en una **enumeración `sympy` en `scratchpad/r2_2.py` — EFÍMERO**. Un `[PROVED]` asistido por
computador **debe** tener el script archivado en `experiments/` y, dado que es load-bearing,
conviene una **segunda enumeración independiente** antes de escribirlo en el paper. (No dudo
del resultado —verifiqué MMM/LLL/RRR y que los mixtos como LMR no teselan— pero un [PROVED]
computacional no puede colgar de scratchpad.)

## `notes/46` — Esqueleto del paper: **ACEPTADO** (alcance honesto) ✓

Estructura sólida, alcance honesto (triángulo ≠ conjetura vía Ambrus; dim target `2N−1`).
Teoremas A–G bien clasificados. Cabecera de abstract honesta ("no resolvemos la conjetura").
**Menor:** el Teorema A (`1/d`) es un **nuevo *proof* elegante de una cota clásica** (John+Bang
ya daban `1/d`), no una cota nueva — enunciarlo así para el referee. Venue (Mathematika/DCG/
Monthly) razonable.

## Estado de los parches (R2-3 y updates)

- **`notes/40` (R2-3):** el `2d−1` bare de §3/§5 **ya está corregido**; las menciones
  restantes son la nota-explicación del error y el caso correcto `N=2→`tetraedro. **OK.**
- **`notes/36 §2`:** ⚠ **parche parcial otra vez.** El banner nuevo (líneas 78–86) dice
  "rigidez [PROVED completo]", pero **el encabezado Status (línea 3) sigue diciendo "rigidez
  [OPEN/EVID]"** y **las líneas 92–99 conservan el texto viejo** ("apoya rigidez… falta la cota
  inferior exacta") que **contradice** el [PROVED]. Limpiar (ver R3-3).

---

## Reevaluación estratégica (importante, honesta)

Con el **no-go de `notes/44`** (verificado), el balance del objetivo primario cambia:

- **Batir B-Y por `N_c` / modificar Bang: MUERTO** (probado, no solo "difícil").
- **La única ruta viva a batir B-Y** es un **certificado de acoplamiento** (escape-cells /
  Farkas, `notes/23 E`, `notes/30 §8.5`, `notes/33 §6`) — **moonshot, territorio experto, sin
  ruta conocida**. No hay atajo incremental.
- **Por tanto el objetivo primario realista pasa a ser: consolidar y publicar el deliverable
  (R2-4), maximizándolo**, y mantener el acoplamiento como apuesta de fondo de alto riesgo.

Esto no es rendición: el proyecto tiene un paper honesto y sólido (5 casos sharp + rigidez +
un no-go estructural). Es el resultado que existe con certeza. Beat-B-Y era, y sigue siendo,
la frontera 2026 de expertos.

═══════════════════════════════════════════════════════════════════════
# ÓRDENES DE TRABAJO — RONDA 3
═══════════════════════════════════════════════════════════════════════

## R3-1 (PRIORIDAD #1 ahora) — Escribir el paper R2-4 (deliverable)
Redactar el manuscrito completo desde el esqueleto `notes/46`, con **pruebas completas** de los
Teoremas A–G, en `drafts/`. Es el objetivo primario realista.
- Cada `[PROVED]` con su prueba autocontenida; citas de fuente primaria a los PDF de `refs/`.
- Alcance honesto en intro y abstract (triángulo = cuerpo concreto; no la conjetura).
- Figuras: tercio-central de medianas, teselación del perímetro, el `N_c`/cuerda-vs-ancho.
- **Precondición:** R3-3 (archivar scripts) hecho, para que A/E/G sean reproducibles.
**Entregable:** `drafts/paper-triangulo.tex` compilable. **Riesgo:** bajo (todo probado).

## R3-2 (value-add, medio) — Extender medianas al `d`-símplex regular (todas las dimensiones)
El teorema de medianas usa transporte por una medida de marginal uniforme; la caracterización
`1ᵀV⁻¹1=2` (concurrencia) es **dimension-agnóstica**. Probar el análogo para las **cevianas
medianas del símplex regular en `Rᵈ`** (concurrentes en el centroide) elevaría el Teorema E de
"triángulo" a "toda dimensión" — **fortalece mucho el paper** sin depender de batir B-Y.
- Construir la medida testigo (¿la del `(d−1)`-esqueleto/facetas, análoga al perímetro?).
- Verificar marginal uniforme en las `d+1` medianas; cota `Σrw≥1`; intentar rigidez.
**Entregable:** Teorema E generalizado (cota; rigidez si sale). **Riesgo:** medio (la medida
puede no ser tan limpia como el perímetro en `d=2`). Alta relación valor/esfuerzo para el paper.

## R3-3 (higiene OBLIGATORIA) — archivar scripts + cerrar parche `notes/36`
1. **Mover a `experiments/`** todos los scripts load-bearing de scratchpad: `r2_1.py`
   (no-go/cuerda), `r2_2.py`+`r2_2b.py` (enumeración de rigidez), `p4_*.py`. Un `[PROVED]`
   computacional NO puede colgar de scratchpad (3ª reincidencia: ya pasó con `ball_fitz.txt`,
   `ambrus.txt`).
2. **Segunda enumeración independiente** del "exactamente 3 edge-tilings" (`notes/45 §2`),
   idealmente por otra vía, para blindar el `[PROVED]` de rigidez antes del paper.
3. **`notes/36`:** actualizar el encabezado Status (línea 3) a "rigidez [PROVED]" y **borrar**
   el texto viejo contradictorio (líneas ~92–99).

## R3-4 (moonshot, fondo) — Certificado de acoplamiento (única vía viva a batir B-Y)
Tras el no-go de `44`, es la ÚNICA ruta al objetivo primario. Concreto:
- Formalizar el certificado de **celdas de escape + Farkas** para `m=3` (`notes/30 §8.5`),
  con el patrón de **6 celdas mixtas** de `notes/33 §6` como semilla.
- Nugget analítico: **estabilidad transversal en el collar `R=1`** (`notes/30 §8.4`).
- Anti-fabricación: solo cuenta una identidad SOS/Farkas exacta o intervalos certificados en
  TODO el collar; grilla ≠ prueba.
**Riesgo:** muy alto, sin ruta conocida. Solo con capacidad sobrante y tras R3-1.

## R3-5 (opcional) — Suficiencia de concurrencia (`1ᵀV⁻¹1=2`) → caracterización iff
Es la pregunta finita abierta de Gardner (`notes/43-P3`). Probarla (aunque sea para `d=2`)
convertiría el Teorema F de "necesaria" a "iff" — refuerza el paper. Lead: extender la
construcción por segmentos de Gardner (Thm 1, 2 direcciones) a 3 concurrentes. **Riesgo:** alto
(Kellerer). Baja prioridad.

---

## Prioridad
1. **R3-3** (higiene, primero — desbloquea la reproducibilidad del paper).
2. **R3-1** (escribir el paper) — objetivo primario realista.
3. **R3-2** (extender a `d`-símplex) — fortalece el paper, en paralelo.
4. **R3-4 / R3-5** — moonshots de fondo.

**Statement honesto para el jefe (yo) y el usuario:** el no-go de `44` cierra el último vector
incremental para batir B-Y. El objetivo "mejorar la SOTA" queda **sin ruta tratable conocida**
(solo el acoplamiento moonshot). Recomiendo **consolidar el paper** como entrega y tratar el
acoplamiento como investigación de alto riesgo separada.
