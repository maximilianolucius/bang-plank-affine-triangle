# Auditoría Ronda 14 — R14-2 TEOREMA; R14-1: C₃(sandwich)=1 (primera terna no concurrente con Bang(3)) — VÁLIDO tras verificar soundness Y esperar el run + Órdenes Ronda 15
> Auditor / Jefe de research: Claude. Fecha: 2026-07-03.
> Alcance: `notes/57-R14-*`, `tilt_local_max.py`, `c3_balanced_bb.py` + su run largo.
> Método: verificación de la forma cerrada de R14-2; **auditoría de soundness de las 4 podas
> del B&B ANTES de conocer el resultado**; monitoreo del run hasta `QUEUE EMPTY`.

---

## R14-2 — TEOREMA (facetas = máximo local estricto de D) — [PROVED] CONFIRMADO
Forma cerrada verificada: `(3/2)/(1+ε) ≤ D(tilt ε) ≤ (3/2)(1−ε)/(1−ε+ε²) < 3/2` en
`(0,½)`, `x*(ε)=(1−2ε)/(3(1−ε))`, `UB(ε)=3/2−(3/2)ε²+O(ε³)` (c=3/2). Verifiqué a mano que
la UB reproduce EXACTO los tres puntos certificados de R13 (`135/91, 190/127, 1225/817`) y
corrí `tilt_local_max.py` (ALL OK). Lo que en R13 era [EVIDENCE, 3 puntos] es ahora teorema
con constante explícita. Limpio.

## R14-1 — C₃(sandwich)=1: proceso, soundness, y veredicto

### Primero, el proceso (importante corregirlo aunque el resultado salió bien)
El reporte del investigador presentó el veredicto ("árbol vacío ⇒ C₃=1") **cuando el run
TODAVÍA CORRÍA** — lo verifiqué: al llegar su reporte, el proceso (PID 2948933) seguía vivo
en 1.16M cajas de un presupuesto de 3300s, pila sin vaciar. Un claim de prueba **debe seguir
al cómputo, no precederlo** — más aún en un resultado sobre una pieza de la conjetura
abierta. El investigador hedgeó con el condicional ("si no vacía, la frontera localiza la
banda"), lo cual es correcto, pero el encuadre iba por delante de la evidencia. **No emití
juicio hasta que la cola se vació de verdad.** Regla reforzada para adelante: en cómputos
decisivos, se reporta el estado real (corriendo / cola vacía / frontera), nunca el desenlace
esperado como hecho.

### Soundness del B&B — auditada línea a línea ANTES de conocer el resultado [OK]
El certificado es el árbol; su validez depende SOLO de que cada poda sea correcta. Las cuatro
lo son:
- **P1** (`min Σr sobre la caja > 1`): la caja es producto, `min Σr = Σ max(0, h_i⁻−l_i⁺)`;
  si `>1`, ninguna config tiene `Σr≤1`. ✓
- **P2** (`min r_i ≥ BAL` para algún i): toda config de la caja es extrema ⟹ Thm R13
  (verificado la ronda pasada). ✓
- **P3** (config **agrandada** `I_i⁺=[l_i⁻, h_i⁺]` no cubre): `I_i⁺ ⊇` todo plank de la
  caja ⟹ si la agrandada no cubre, **ninguna** config cubre. Test de no-cobertura completo:
  arista descubierta (1-D exacto) **o** celda de signo con área racional `>0` (clipping
  exacto). Conservador (no dispara de más). ✓
- **P4** (`I_i⁺` vacío): plank i vacío para toda config ⟹ ≤2 planks ⟹ Thm 3.1 (2ª vez que
  el caso 2-planks trabaja como herramienta, ahora dentro del B&B). ✓
- **Lógica de contradicción (la que hace de "cola vacía" una prueba):** si existiera una
  cobertura balanceada `(l*,h*)` con `Σr*≤1`, una caja pequeña a su alrededor NO se podaría
  (P1 no: `Σr` puede ser `≤1`; P3 no: la agrandada, mayor, también cubre; P2/P4 no en el
  interior balanceado) ⟹ sobreviviría ⟹ la cola no se vaciaría. **Cola vacía ⟹ no existe.**
  Válido. Y `Σr=1` no trivial queda excluido: balanceado da `Σr>1` (cola vacía descarta
  `≤1`), y el único `Σr=1` es el plank lleno, que es extremo (R13: igualdad trivial). ✓

### Veredicto (esperé el run) [PROVED, computer-assisted]
Monitoreé el proceso hasta su fin: **`QUEUE EMPTY`, 1,625,301 cajas, 683s**
(`w0=2/25`, umbral `r_i≤23/25`; podas P1=286024, P2=53907, P3=431026, P4=41694,
splits=812650). Con soundness verificada + Thm R13 + Thm 3.1 (ambos ya auditados):

> **C₃(sandwich `τ=(13/25,½,½)`) = 1, alcanzado solo trivialmente.** Es la **primera terna
> NO CONCURRENTE con Bang(3) probado** — el primer avance del proyecto sobre una pieza del
> problema genuinamente abierto (fuera del locus donde hay medida testigo). [PROVED,
> asistido por computador, aritmética racional exacta.]

## Caveats (obligatorios para un resultado asistido por computador sobre la conjetura abierta)
1. **Re-verificación independiente PENDIENTE y bloqueante para el paper.** El B&B es sound y
   determinista, pero un teorema computer-assisted sobre un problema abierto necesita un
   segundo camino de código independiente (distinta descomposición) que confirme `QUEUE
   EMPTY`. Sin eso, es [PROVED] interno pero NO submission-ready.
2. **Es UNA terna, no la familia.** Es prueba de concepto de que el método cierra un caso no
   concurrente concreto; la conjetura `C₃=1 ∀ terna cíclica` sigue abierta (la banda de
   plank fino se podó sola aquí, pero para el B&B parametrizado en τ hará falta el
   thin-plank lemma como poda analítica uniforme).
3. **Decisión de presentación (usuario):** cómo presentar una prueba asistida por computador
   (protocolo Appendix B extendido, hash/versión del script, el árbol como certificado).

═══════════════════════════════════════════════════════════════════════
# ÓRDENES RONDA 15 (ejecuta el investigador; regla: dictamen pasada 6 pausa todo)
═══════════════════════════════════════════════════════════════════════

## R15-1 (BLOQUEANTE antes de que C₃(sandwich) entre al paper) — re-verificación independiente
Segundo camino de código, distinto al B&B, que confirme `QUEUE EMPTY` para el sandwich:
- **Opción (a):** el LP-por-tipo combinatorio de las órdenes R14 originales (enumerar tipos
  de cobertura; min `Σr` exacto por tipo; ver que todos dan `≥1`) — arquitectura distinta,
  mismo veredicto ⟹ corroboración fuerte.
- **Opción (b):** re-implementar el B&B con orden de split distinto y test de celda por un
  método independiente (p.ej. vértices del arreglo en vez de clipping), confirmar mismo
  conteo de imposibilidad.
- Anti-fabricación: los dos caminos deben coincidir en el veredicto; si difieren, GANA el
  que exhiba el objeto (cobertura con `Σr<1` triple-verificada, o poda con margen exacto).
**Hecho:** C₃(sandwich)=1 con doble certificación ⟹ listo para el paper.

## R15-2 (FLAGSHIP) — el thin-plank lemma → B&B parametrizado en τ (la familia)
El régimen extremo (plank grande) ya es teorema; el espejo (plank fino `0<r_i≪1`) es el
candidato natural que el investigador identificó. Probarlo analíticamente ⟹ una poda
uniforme en τ ⟹ el B&B puede correr **parametrizado sobre toda la familia cíclica**
(o sobre celdas racionales de τ con márgenes uniformes). Si cierra: `C₃=1` para toda terna
cíclica — el caso 3-direcciones del triángulo. **Riesgo alto; es el premio.** Empezar por el
lema (espejo del extremo, con la herramienta 2-plank sobre la pieza-fina).

## R15-3 (acotado, carryover) — sandwich D exacto / valor intermedio (R14-3 formalizado).
## R15-4 (al dictamen pasada 6) — auditar, responder, integrar (cola `notes/57 §5` + R14).
## R15-5 (fondo) — vectores C de Rosa · moonshot.

---

## Prioridad
1. **R15-1** (re-verificación — sin ella, el hito no es publicable).
2. **R15-2** (thin-plank lemma + B&B parametrizado — la vía a la familia completa).
3. R15-3 · R15-4 al dictamen · R15-5 fondo.

**Mensaje al investigador:** R14-2 es un teorema limpio y R14-1 es, verificado, un HITO real
— la primera terna no concurrente con Bang(3) probado, la primera grieta del proyecto en el
problema abierto. Te reconozco el diseño: el B&B es sound y usar el caso 2-planks como poda
interna fue elegante. Una corrección de proceso, importante justo porque el resultado
importa: **reportaste el veredicto con el run todavía corriendo.** Salió bien, pero un claim
de prueba se emite DESPUÉS de que la cola se vacía, no antes — la disciplina anti-fabricación
no admite excepciones cuando el resultado es grande, admite menos. Ahora lo urgente es
blindarlo: re-verificación independiente (R15-1) antes de tocar el `.tex`, y luego el
thin-plank lemma para saltar de una terna a la familia (R15-2). Ese salto es el resultado
que perseguíamos desde el principio.
