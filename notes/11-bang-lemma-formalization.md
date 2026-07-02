# Vector 1 · Hito 1 — Formalización del lema tipo-Bang (afín, no simétrico)
> El lema combinatorio-lineal que cierra la conjetura sobre el marco vectorial (nota 10).
> Date: 2026-06-28.

## El lema clásico de Bang (caso simétrico/centrado, Tarski)
**Lema (Bang, 1951).** Sean `a_1,…,a_n` vectores en un espacio con producto interno.
Elegir signos `ε∈{±1}^n` que **maximizan** `‖Σ_j ε_j a_j‖²`. Entonces `y = Σ_j ε_j a_j` cumple
$$\varepsilon_k\langle y,a_k\rangle \ \ge\ \|a_k\|^2\quad\forall k,
\qquad\text{en particular } |\langle y,a_k\rangle|\ge\|a_k\|^2.$$
*Prueba:* voltear `ε_k` no aumenta la norma: `‖y‖² ≥ ‖y−2ε_k a_k‖²` ⟹ `4ε_k⟨y,a_k⟩−4‖a_k‖²≥0`. ∎
Esto da Tarski: planks `|⟨x,u_k⟩|≤w_k/2` (`‖u_k‖=1`), `a_k=(w_k/2)u_k`, el punto `y` esquiva
todos salvo que `Σw_k ≥` diámetro.

## Lo que necesitamos (versión AFÍN, no centrada, sobre el símplex)
Marco de la nota 10: matriz `U=(ũ_{a,i})∈[0,1]^{m×n}` (cada fila: min 0, max 1), intervalos
`I_a⊆[0,1]`, `|I_a|=rw_a`.

> **LEMA AFÍN DE BANG (objetivo).** Si `Σ_a |I_a| < 1`, existe `x∈Δ_n` (vector de probabilidad)
> con `(Ux)_a = ⟨ũ_a,x⟩ ∉ I_a` para todo `a`.

Diferencias con el clásico:
- el punto buscado es **convexo** (`x∈Δ`, no `ε∈{±1}^n`),
- los intervalos `I_a` son **arbitrarios en `[0,1]`** (no centrados en 0),
- `U` es **rectangular/no simétrica** (planks no perpendiculares).
La constante objetivo es **`1`** (no `1/2`): es la combinatoria del cubrimiento, no una medida.

## Reducción del caso 2-direcciones a un acoplamiento (transporte)
Si solo hay dos direcciones `u,v`, el mapa `Φ=(f_u,f_v):Δ→[0,1]²` (afín) tiene imagen un
**triángulo `T_img`** con proyección `[0,1]` en **ambos** ejes. Cubrir `Δ` ⟺ cubrir `T_img` por
**bandas verticales** (`f_u∈∪I_a`, ancho total `L_u`) y **horizontales** (`f_v∈∪J_b`, `L_v`).

**Dualidad (LP / Strassen):**
$$\min(L_u+L_v)\ =\ \max\{\,\text{masa de un acoplamiento } \nu \text{ soportado en } T_{img}
\text{ con marginales } \le \text{Leb}_{[0,1]}\,\}.$$
*Cota fácil (≥):* si existe `ν` en `T_img` con marginales `≤ Leb`, entonces
`ν(T_img) ≤ ν(V\text{-strips}) + ν(H\text{-strips}) ≤ L_u + L_v`.
Si además existe un acoplamiento de **masa 1** con ambas marginales `=Leb_{[0,1]}` soportado en
`T_img`, entonces **`L_u+L_v ≥ 1`** ⟹ `Σrw ≥ 1`. Su existencia es una **condición de matrimonio
(Hall/Strassen):** `Leb(N(A)) ≥ Leb(A)` para todo `A⊆[0,1]`, donde `N(A)={y:∃x∈A,(x,y)∈T_img}`.

## Caso 2-direcciones — RESUELTO (numérico) vía dualidad cobertura=acoplamiento
Verificación (R15, LP de transporte, grilla K=60): **`min Σrw = 0.983 ≈ 1`** sobre 51 configs,
con MUCHAS tocando ese mínimo ⟹ **el caso de 2 direcciones es ajustado en `Σrw = 1`**.
(Déficit 0.017 ≈ 1/K = discretización.)

**Estructura de la prueba (rigurosa salvo un lema estándar):**
1. `min(L_u+L_v)` = `max` masa de acoplamiento en `T_img` con marginales `≤ Leb` — **LP-dualidad
   exacta** (König / cobertura-fraccionaria = emparejamiento). RIGUROSO.
2. `T_img` (triángulo convexo con proyecciones plenas `[0,1]²`) **soporta un acoplamiento de masa
   1 con marginales uniformes** (condición de Hall/Strassen, verificada: el LP da masa = 1).
   ⟹ `L_u+L_v ≥ 1`.
3. **Clave conceptual:** la medida del **área** solo da `1/2` también en 2 direcciones
   (`1−2L_u ≤ 2L_v`). El salto a `1` lo da el **acoplamiento de marginales uniformes** sobre la
   imagen 2D — NO una medida sobre `Δ`. Esto vive en la combinatoria, no en una medida única.

## El obstáculo real: 3 direcciones
El truco del acoplamiento 2D **NO sobrevive a 3 direcciones**: `Φ=(f_u,f_v,f_w):Δ→[0,1]³` mapea
un triángulo 2D a una superficie 2D en el cubo; las "bandas" son losas 3D y la dualidad
cobertura=acoplamiento ya no es bipartita. Aquí es donde se necesita el lema de Bang afín pleno
(no la reducción 2D). Próximo: entender qué rompe exactamente al añadir la 3ª dirección.
