# Dictamen 5ª pasada de doña Rosa ("Major revision con potencial real") + Órdenes RONDA 12
> Jefe de research: Claude. Fecha: 2026-07-03.
> Insumo: 5ª auditoría externa (sobre la pasada 5, 24 pp, con dualidad).
> Método: cotejo de cada punto contra el `.tex`; verificación exacta de sus dos objeciones
> técnicas (una es real y gratis; la otra es mislectura suya).

---

## Calibración del dictamen: el pivote de arquitectura FUNCIONÓ

De "Reject" (pasada 4) a "Major revision con potencial real de publicación" (pasada 5), con
la validación explícita de lo que decidimos: **`D_K` como columna vertebral organiza el
manuscrito** — su queja estructural ("tres papers en un PDF") quedó respondida por
coherencia, sin partir. Reconoce además: niveles de claims bien marcados, jerarquía clara,
rigidez cíclica bien estructurada, protocolo de scripts serio. Los problemas restantes que
señala son "formales/expositivos, no conceptuales" — su frase, y es correcta.

## Sus objeciones técnicas — verificadas contra el `.tex`

| # | Punto | Dictamen |
|---|---|---|
| Pocket Lemma "P∩∂Δ finito no tiene sentido" | **INVÁLIDA (mislectura suya).** El `.tex` dice exactamente lo que ella pide: `P̄∩∂Δ` finito (barra de clausura presente, l.~"pocketlemma"). La copia congelada es diff-0 con el vivo. **Sin error nuestro.** Fix defensivo barato: añadir la palabra "closure" en prosa para que ni un lector apurado lo malinterprete. |
| **`27/29 → 29/31`** | **VÁLIDA — mejora real y GRATIS.** El `.tex` (l.1326) usa la forma débil `Σrw ≥ 1−x` vía `1/(1+x)≥1−x`; el recíproco exacto da `D ≤ 31/29 ⟹ Σrw ≥ 29/31 ≈ 0.93548 > 27/29 ≈ 0.93103`. Verifiqué: `29/31 > 4√3−6 ⟺ 215² = 46225 > 46128 = 48·31²` ✓. Adoptar en Thm de estabilidad (enunciar `Σrw ≥ m(m−ε)/(m(m−ε)+ε)`) y el Cor, y actualizar la mención de la intro (l.178). |
| Abstract cargado; B-Y fuera del abstract | VÁLIDA — 3 mensajes (D_K+dualidad; caracterización D=1; familia cíclica tight+rígida); la comparación B-Y al final de la intro. |
| "best constant is certified" ambiguo | VÁLIDA — la frase correcta es la suya: "when the **transport method** certifies the sharp constant 1". El covering constant verdadero puede ser 1 con D>1 (facetas — el propio paper lo dice). |
| Precisión quirúrgica de la dualidad + renombrar | VÁLIDA-menor — el enunciado ya especifica (ψ continuas ≥0, `Σ∫ψ=1`, extensión Borel); falta decir explícitamente que el sup puede no alcanzarse (no lo afirmamos) y renombrar a "minimax / continuous LP duality". |
| Mini-tabla para el Thm de caracterización | VÁLIDA — barata, alta legibilidad. |
| Tabla de 7 casos + razón de imposibilidad en Apéndice A | VÁLIDA — barata, sube la confianza del lector. |

**Sus ideas de valor** (C(u) y el gap, estabilidad inversa, figura del certificado dual,
phase diagram, vectores B–E) son buenas y varias alinean EXACTAMENTE con nuestro objetivo
primario — se adoptan filtradas abajo. Nota de crédito: su "inverse stability" es un
corolario de una línea de nuestra propia cota de momentos (`D≤1+η ⟹ δ ≤ η/(2(1+η))`) —
gratis y elegante.

═══════════════════════════════════════════════════════════════════════
# ÓRDENES RONDA 12 (ejecuta el investigador)
═══════════════════════════════════════════════════════════════════════
Absorbe la R11: sus tareas de research siguen vivas como C2. Descongelada la numeración
(el dictamen llegó): UNA actualización de la tabla vieja↔nueva, todo junto.

## PARTE A — fixes de la pasada 5 + integración del paquete R10 (desbloqueada)
- **A1 (gratis, ya):** `27/29 → 29/31` — recíproco exacto en el Thm de estabilidad
  (`Σrw ≥ m(m−ε)/(m(m−ε)+ε)`) y el Cor (`29/31 > 4√3−6`, certificado `46225>46128`);
  actualizar TODAS las menciones (intro l.178 incluida). El tubo (`cor:region`) ya usa el
  recíproco — verificar que quede consistente.
- **A2:** Pocket Lemma — sin error; añadir "the closure of P" en prosa (blindaje contra
  mislectura).
- **A3:** abstract a 3 mensajes; comparación B-Y al final de la intro (sobria, con su
  caveat).
- **A4:** "best constant is certified" → "the transport method certifies the sharp
  constant 1" (abstract y donde aparezca).
- **A5:** dualidad: renombrar "minimax (continuous LP) duality"; añadir al enunciado que el
  supremo no se afirma alcanzado; checklist de precisión (clase de ψ, normalización, Borel).
- **A6:** mini-tabla de patrones de arista llena junto al Thm de caracterización
  (patrón / ¿concurrencia? / soporte del testigo / mecanismo de cota).
- **A7:** Apéndice A: tabla de 7 filas (tipo, representante, resultado, ecuaciones clave) +
  en cada caso imposible la RAZÓN etiquetada (solape de interiores / hueco / endpoint /
  degeneración `l<h` / `τ∉(0,1)`).
- **A8 (integración R10):** teorema `δ=δ_c` (la Prop de cuñas (iii) pasa a incondicional;
  caso degenerado `c₀=0` acomodado); certificados-gap (los tres, con el verificador como
  ancillary); lema de continuidad (lsc + camino casi-paralelo); unicidad del maximizador de
  δ; Problem reducido a `sup D = 3/2?`. Reescribir las dos Rem afectadas.
- **A9:** tabla de numeración actualizada UNA vez; compilación limpia; copia congelada
  pasada 6; hand-off con mapa punto→resolución (incluida la nota educada de que el Pocket
  Lemma ya tenía la clausura). **Bloque de autor: sigue siendo decisión del usuario.**

## PARTE B — valor añadido barato (de Rosa, aceptado con filtro)
- **B1 — el covering constant `C_K(u)` y el gap `G(u) = C(u) − 1/D(u)`:** definir
  formalmente `C(u) = inf{Σrw : cobertura por planks en esas direcciones}`; tabla
  (2 direcciones, medianas, cíclicas concurrentes, facetas, near-concurrent) con los gaps
  conocidos (facetas: `1 − 2/3 = 1/3`; concurrentes: 0). Hace la narrativa más honesta y
  prepara el flagship C1.
- **B2 — estabilidad inversa (una línea):** `D ≤ 1+η ⟹ δ(u) ≤ η/(2(1+η))` (de la cota de
  momentos); con el Thm de estabilidad directo, `D−1` queda como métrica bilateral de
  no-concurrencia. Proposición corta.
- **B3 — figura del certificado dual:** las cuñas de facetas `ψ=(1−3t/2)₊` + el hexágono de
  contacto (donde vive el lazo y donde cobra la holgura). TikZ.
- **B4 — phase diagram [EVIDENCE]:** mapa racional certificado de `D(τ)` sobre `(0,1)³`
  módulo simetría (LB duales certificados; UB esqueléticos donde finitos; regiones donde el
  momento parece exacto vs. el sandwich-tipo). Etiquetado como orientación, no prueba.

## PARTE C — research
- **C1 (FLAGSHIP — el vector disruptivo, y ES nuestro objetivo primario):
  el programa `C(u)`: ¿`C(u) = 1` para TODA terna no-paralela del triángulo?**
  Probado: concurrentes (`D=1`) y facetas (teselación). Lo abierto: no-concurrentes
  no-faceta — exactamente el Problem 1 del paper. Plan concreto de esta ronda:
  1. **Formalizar** `C(u)` y `C₃(u)` (un plank por dirección; empezar por `C₃`).
  2. **Experimentos exactos primero** (3–5 ternas no concurrentes: el sandwich, las dos
     certificadas de R10, una clase (b)): minimizar `Σr` sobre coberturas — 6 parámetros,
     cobertura ⟺ las 8 celdas de signo vacías (condiciones polinomiales; análisis exacto
     de celdas, no grilla). Salidas posibles: (a) `inf Σr = 1` con estructura casi-tight
     visible ⟹ guía de la prueba; (b) cobertura con `Σr < 1` ⟹ **REFUTA la conjetura de
     Bang afín** — triple-verificación exacta obligatoria antes de reportar (probabilidad
     bajísima, protocolo por si acaso).
  3. **El ataque estructural:** generalizar el Paso 2 de la rigidez cíclica a `(l_i,h_i)`
     arbitrarios con `Σr < 1`: el conjunto no cubierto se parte en ≤8 celdas; la
     **dependencia afín `Σc_iu_i ≡ c₀` existe SIEMPRE** (Prop de cuñas (i)) y es el análogo
     general de `Λ≡S`; Pocket Lemma se generaliza. Diferencia clave a resolver: con
     `Σr<1` la frontera NO está teselada — separar (a) las trazas no cubren alguna arista ⟹
     punto de arista no cubierto, listo; (b) cubren las 3 aristas ⟹ cota de transporte de
     borde (`D_∂`) + análisis interior. En (b) es donde Rosa tiene razón: hará falta el
     **certificado híbrido** (medida + obstrucción de sumset/teselación tipo Thm 3.2) —
     formalizarlo es parte del programa, no de esta ronda.
  4. Entregable de ronda: formalización + experimentos exactos + el caso (a) probado + el
     estado honesto de (b). Va al paper como "Research Direction A" con la precisión que
     pide Rosa. **Riesgo alto; es investigación de frontera — pero es la primera ruta
     concreta al caso 3-direcciones del triángulo que tenemos.**
- **C2 (carryover R11):** UB fino cerca de facetas (¿máximo local en 3/2?) y sandwich
  exacto (matched pair o primera prueba de óptimo no-esquelético). Alimentan B4 y C1.
- **C3 (fondo):** vectores B/C de Rosa — fórmula cerrada `D(τ)` por regiones (¿nudos
  óptimos en clase finita?); caracterizar `D_∂ = D` (transición de fase del soporte). Solo
  con capacidad sobrante.

---

## Prioridad
1. **A1** (constante gratis) + **A8** (integración R10) — el paper primero.
2. **A3–A7, A9** + **B1–B3** (van juntas en la misma pasada editorial) → **pasada 6**.
3. **C1** flagship (con C2 en paralelo); B4 junto a C2.
4. C3 fondo.

**Mensaje al investigador:** Rosa pasó de "reject" a "major revision con potencial" y
validó la arquitectura — el trabajo de las rondas 9–10 hizo exactamente lo que debía. Dos
cosas de su dictamen que debes saber: (1) su objeción al Pocket Lemma es mislectura — tu
formulación ya era correcta; se blinda con una palabra, no se cede; (2) su mejora
`29/31` es real y gratis — adóptala sin discutir. El flagship ahora es `C(u)`: es la
primera vez que el proyecto tiene una ruta concreta hacia el caso abierto real, y viene
avalada por la auditora externa. Experimentos exactos primero; si aparece `Σr<1`,
triple-verificación antes de decir una palabra.
