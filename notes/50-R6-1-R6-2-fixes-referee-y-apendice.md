# R6-1 / R6-2 — Fixes de referee ejecutados + Lemma 5.2 con prueba humana (Apéndice A)

> Date: 2026-07-02. Status: **[HECHO — compila 0 errores, 0 undefined, 0 overfull]**.
> Ejecuta `auditorias/50 §R6-1` (los 6 fixes) y `§R6-2` **opción (a)** (prueba a mano,
> la preferida — no hizo falta el fallback de certificación).
> El paper pasó de 6 pp a **11 pp** (los fixes + apéndice + los dos teoremas nuevos de
> R6-4/R6-5, ver notas 50-R6-4 y 50-R6-5).

## 1. R6-1 — mapa objeción → resolución (para R6-3 / doña Rosa)

| # | Objeción de doña Rosa | Dónde se resolvió |
|---|---|---|
| 1 | "sharp for the simplex" (Thm 2.1) falso leído como cobertura | Thm 2.1 reescrito: `d≥2` explícito (`d=1` trivial anotado); sharpness ahora **del per-plank estimate** `μ(P)≤d·rw(P)`; el final de la prueba añade la frase explícita "this does NOT assert any covering with Σrw near 1/d" + referencia a Thm 3.2. Abstract corregido igual. |
| 2 | Lemma 5.2 caja negra computacional | **Prueba humana completa en Apéndice A** (Prop. A.1, más general: clasificación para ternas cíclicas arbitrarias; Lemma 5.2 = caso `τ=½`). Los 3 scripts quedan como verificación independiente ancillary, ya no como sustento. |
| 3 | "first tight non-facet case" sin soporte | "To our knowledge" en abstract y §5 + frase de soporte citando [Verreault], [Gardner88], [BY26]. |
| 4 | Thm 7.1 no es teorema formal | Reclasificado **Proposición 7.1** con enunciado matemático preciso (el paso del chord-lemma es sharp; el ratio se alcanza en el segmento); la lectura metodológica quedó en el Remark. Referencias cruzadas (abstract, intro) actualizadas. |
| 5 | Thm 3.1 sin no-degeneración + cita Gardner imprecisa | Hipótesis "non-parallel" añadida + caso paralelo despachado en una línea dentro del enunciado + cita "[Gardner88, Theorem 1]" con su alcance ("any two directions on any planar convex body"). |
| 6 | `d=1`; truncamiento `I⊄[0,1]`; estilo | `d≥2` en Thm 2.1; WLOG `I⊂[0,1]` justificado en el modelo (§1: truncar preserva cobertura y no aumenta `rw`); paréntesis contradictorio de la prueba de medianas borrado. |

Extra R6-1f (orden del jefe): **Corolario 6.4 (iff cíclico)** añadido — con un hallazgo
mejor que lo pedido: la interioridad del punto de concurrencia es **automática**
(`det V = −(1+τ₁τ₂τ₃) ≠ 0` siempre; la solución de `Vp=½·1` cumple `p_j>0` y `p_j<½`
para todo `τ∈(0,1)³` vía `2(1+τ₁τ₂τ₃)p_A = 1−τ₃(1−τ₂) > 0` y `½−p_C = τ₁p_A > 0`,
cíclicamente). El corolario no necesita hipótesis de interioridad. Verificado simbólico.

## 2. R6-2(a) — la prueba humana del Apéndice A

Estructura (ahora para **ternas cíclicas arbitrarias** `τ∈(0,1)³`, sin concurrencia —
generalización necesaria para el teorema de R6-4):

1. **Tabla de trazas**: cada arista ve (low, full, high) = `(1,2,3)/(3,1,2)/(2,3,1)`;
   trazas `T_c=[max(0,1−h/τ),1−l/τ]`, `T_f=I_f`, `T_g=[(1−h)/(1−τ), min(1,(1−l)/(1−τ))]`.
2. **Tipos L/M/R** de cada `I_i` respecto de `τ_i`; observaciones (O1) (traza-M ancla en
   el extremo; traza L/R del lado equivocado degenera) y (O2) (las degeneradas no
   cuentan: cerradura).
3. **Simetrías**: rotación (τ y planks se desplazan cíclicamente) + reflexión∘flip
   (`τ↦1−τ` con `L↔R`) ⟹ los 27 patrones caen en **7 órbitas**.
4. **Casos**: MMM y LLL(~RRR) → sistemas cíclicos de mapas afines decrecientes
   (pendiente compuesta ≠ 1 ⟹ solución única); MML, LLM, LLR, LMR, LRM → imposibles
   en 2-4 líneas cada uno.

**Prop. A.1**: para todo `τ∈(0,1)³` hay **exactamente tres** soluciones de edge-tiling:
`([λ_i,ρ_i])`, `([0,λ_i])`, `([ρ_i,1])` con
`λ_i = τ_i(1−τ_{i+1}(1−τ_{i+2}))/(1+τ₁τ₂τ₃)`,
`ρ_i = (1−τ_{i+2}(1−τ_i))/(1+(1−τ₁)(1−τ₂)(1−τ₃))`, y siempre `0<λ_i<τ_i<ρ_i<1`.
Caso `τ=½`: `[⅓,⅔]³, [0,⅓]³, [⅔,1]³` = Lemma 5.2. ∎

**Verificación**: búsquedas racionales exactas en grilla conteniendo los endpoints:
`τ=(½,½,½)` (3 soluciones ✓) y `τ=(½,⅔,⅓)` (3 soluciones = las fórmulas ✓);
script nuevo `experiments/median_edgetiling_types_crosscheck.py` (+ los 2 previos).

## 3. Estado del build

11 pp, `pdflatex` 2 pasadas: 0 errores, 0 referencias sin resolver, 0 overfull.
`drafts/ancillary/`: 7 ficheros (6 scripts + README actualizado).
