# R12 — Ejecución: pasada 6 (fixes Rosa-5 + integración R10) y el programa C(u)

> Date: 2026-07-03. Ejecuta `auditorias/60` (Ronda 12, absorbe R11).
> Status: **[HECHO Parte A completa, Parte B completa, C1 con teorema nuevo +
> experimentos; C2/C3 fondo sin empezar]** — compila **31 pp, 0/0/0**.
> Congelada: `entregas/affine-plank-triangle-2026-07-03-pasada6.{pdf,tex}`.
> Hand-off con mapa punto→resolución y tabla de numeración:
> `notes/55-R12-entrega-dona-rosa-pasada6.md`. Script nuevo:
> `experiments/covering_constant.py` (sync a ancillary), "todo OK/exacto".

## Parte A — fixes de la pasada 5 + integración R10 [HECHO]

- **A1**: `27/29 → 29/31` adoptada sin discutir. Thm 7.15 con el recíproco
  exacto `Σrw ≥ m(m−ε)/(m(m−ε)+ε)`; Cor 7.17: `29/31 > 4√3−6` certificado
  `215² = 46225 > 46128 = 48·31²`; intro actualizada; el tubo (7.18) ya era
  recíproco-exacto — consistente.
- **A2**: Pocket Lemma — "the closure P̄ of P" en prosa. Sin ceder: el
  enunciado ya era correcto (la nota de entrega lo dice con cortesía).
- **A3/A4**: abstract a 3 mensajes con la frase de Rosa ("the transport
  method certifies the sharp constant 1"); B-Y en párrafo propio al final de
  la intro, sobrio, con caveat y referencia al alcance exacto.
- **A5**: "minimax duality" (Thm 7.7) + no-alcance del supremo explícito.
- **A6/A7**: mini-tabla de la tricotomía junto a Thm 6.11; tabla de 7 casos
  con mecanismo etiquetado en el Apéndice A.
- **A8 (R10 integrado)**: Lem 7.10 = lema de conteo GENERALIZADO a nivel `a`
  (prueba completa en el texto, con el manejo de ceros/colisiones
  tipo-faceta); **Thm 7.11 δ=δ_c** (prueba: flips + pull-back + conteo);
  Prop 7.9(i) acomoda `c₀=0` (homogeneidad dicha); Rem 7.12 reescrita
  (jerarquía colapsa); **Rem 7.20** con los TRES certificados-gap y el
  sandwich estricto `225/224 < D ≤ 112/111`; Prop 7.21 (lsc) + Rem 7.22
  (camino paralelo, cotas bilaterales simbólicas); Prop 7.4 (unicidad del
  maximizador, Gordan); Prob 10.4 reducido a `sup D = 3/2?`.
- **A9**: numeración actualizada UNA vez (tabla completa en la entrega;
  claves estables: 6.6–6.9, 6.11, 7.1–7.3, 8.x, A.1).

## Parte B — valor añadido de Rosa [HECHO]

- **B1**: Def 2.3 `C_K(u)` + Rem 2.4 (`1/D ≤ C ≤ 1`; Bang restringido ⟺
  `C=1`; gap `G`); tabla de gaps en §10 (facetas 1/3; concurrentes 0;
  sandwich `C ∈ [111/112, 1]`; clase-b `(2/3,5/6,1/12)`: `C ∈ [60/71, 1]`).
- **B2**: Prop 7.16 (inverse stability, una línea desde Prop 7.2);
  `D−1` como métrica bilateral de no-concurrencia (párrafo).
- **B3**: Fig. 4 (cuña + hexágono de contacto), verificada visualmente.
- **B4**: Fig. 5 phase diagram [EVIDENCE] — rebanada `τ₃=½`, 361 celdas
  exactas de la cota inferior cerrada (`δ=δ_c` ⟹ es certificada);
  anti-diagonal `Π=Q` = concurrencia; **números de la caption verificados**:
  gap UB/LB ≤ 0.06 en la franja `|τ₁+τ₂−1| ≤ 1/5` (máx exacto 1432/23961),
  0.59 en la esquina (1/20,1/20). Etiquetada "Evidence, not proof".

## Parte C1 — el programa C(u): TEOREMA nuevo + experimentos [PARCIAL fuerte]

- **Formalización** [HECHO]: `C_K` (Def 2.3), programa en §10 (Prob 10.1);
  `C ≤ 1` trivial (un plank lleno) — la conjetura de Rosa = cota inferior.
- **[PROVED] Thm 6.13 (canonical covering)**: para TODA terna cíclica, la
  configuración `([λ_i, ρ_i])` de la Prop A.1 CUBRE Δ con
  **`Σrw = 1 + (Π−Q)²/((1+Π)(1+Q))`**, `Π = τ₁τ₂τ₃`, `Q = Π(1−τ)`. Piezas:
  - dependencia explícita positiva `c_i = g_i/(1+Π)`, `g_i = 1−τ_{i+1}(1−τ_{i+2})`,
    con `Σc_iu_i ≡ 1` (identidades de vértice verificadas simbólicamente);
  - tres identidades polinomiales (en el texto + `covering_constant.py`):
    `(1+Π)² − Στ_ig_i² = g₁g₂g₃`, `Σg_ig_{i+1} − (1+Π)(1+Q) = g₁g₂g₃`,
    `(1+Π)Σg_i − (1+Q)Στ_ig_i − (1+Π)(1+Q) = (Π−Q)²` ⟹ márgenes estrictos
    SIEMPRE y la fórmula del exceso;
  - cobertura: Lem 6.8 verbatim con `(a_i,S) → (c_i,1)`.
  - **Bonus estructurales**: `Π=Q ⟺ δ_c=0 ⟺ concurrencia` (criterio limpio
    nuevo) y `δ(u_τ) = |Π−Q|/(2(2+Π+Q))` cerrada para toda cíclica
    (sandwich: 1/450 ✓).
- **Experimentos exactos** [EVIDENCE]: oráculo de cobertura EXACTO (8 celdas
  de signo por LP Chebyshev de vértices + chequeo independiente de aristas);
  sandwich: MMM cubre con exceso `1/12656` exacto; caza float-guiada con
  certificación exacta sobre 3 ternas no concurrentes: **ninguna cobertura
  certificada con `Σr < 1`** (el mínimo certificado = 1, el plank pleno);
  protocolo anti-sensación en el script, nunca disparado.
- **Caso (a) [PROVED]**: Lem 10.2 (edge reduction) — toda cobertura cubre
  cada arista; las condiciones lineales necesarias dan un LP cuyo valor es
  `3/5` en medianas ⟹ **insuficiente solo**: honestidad escrita (el híbrido
  de (b) queda formulado como programa, no resultado).
- **Caso (b)** [OPEN]: certificado híbrido (medida + obstrucción
  sumset/teselación) — formalizado como objetivo del programa en §10.

## No hecho (cola honesta)

- **C2** (UB fino cerca de facetas — ¿máximo local 3/2?; sandwich exacto):
  sin empezar esta ronda; alimentaría Fig. 5 y Prob 10.4.
- **C3** (fórmula cerrada `D(τ)` por regiones; transición `D_∂ = D`): sin
  empezar (solo la mención en Prob 10.4 y la caption de Fig. 5).
- Bloque de autor: pendiente (decisión del usuario).

## Verificación

- Compilación 31 pp, 0 errores / 0 undefined / 0 overfull; Figs. 4, 5 y las
  tablas revisadas visualmente en PNG.
- Identidades del Thm 6.13 (las 3 + vértices + `Σg = 2+Π+Q`): sympy → 0.
- Caption de Fig. 5: gaps recomputados exactos antes de escribirlos.
- Los certificados de Rem 7.20 corren en `dual_certificates.py` (ALL OK,
  autocontenido).
