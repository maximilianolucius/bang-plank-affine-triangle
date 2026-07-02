# Vector 4 · Hito 1 — La reducción a vectores (montada y verificada)
> Reformulación afín-invariante del problema del triángulo como un problema de
> distribuciones/medias sobre el símplex estándar. Base para atacar el lema tipo-Bang (Vector 1).
> Date: 2026-06-28.  Status: reducción RIGUROSA + verificada numéricamente.

## La reducción
Por invariancia afín, todo triángulo ≡ el 2-símplex estándar
`Δ = {x∈ℝ³ : x_i≥0, Σx_i=1}`.

Cada plank `P_a` se normaliza (shift por constante, lícito pues `Σx_i=1`; luego escala) a:
- un covector `ũ_a ∈ [0,1]³` con **`min_i ũ_{a,i}=0`, `max_i ũ_{a,i}=1`**,
- un intervalo `I_a ⊆ [0,1]` con **`|I_a| = rw_a`**,
- el plank cubre `{x∈Δ : ⟨ũ_a,x⟩ ∈ I_a}`.

**Problema (forma vectorial):** dados `{(ũ_a, I_a)}`, "cubren `Δ`" ⟺ `∀x∈Δ ∃a: ⟨ũ_a,x⟩∈I_a`.
**Conjetura:** cubren ⟹ `Σ|I_a| ≥ 1`.

## Interpretación probabilística (puente a Bang)
`x∈Δ` es una **distribución** sobre `{1,2,3}`, y `f_a(x) := ⟨ũ_a,x⟩ = 𝔼_x[ũ_a]`.
- Cada `f_a : Δ → [0,1]` es **afín**, con `f_a(e_{min})=0`, `f_a(e_{max})=1`.
- El plank `a` cubre la franja `f_a(x)∈I_a`.

**LEMA TIPO-BANG (núcleo abierto):** si `Σ|I_a| < 1`, existe una distribución `x` con
`𝔼_x[ũ_a] ∉ I_a` para todo `a` (punto que esquiva todos los planks).
- Región no-cubierta = intersección de pares de semiespacios (`f_a<inf I_a` ó `f_a>sup I_a`).
- Es **lineal en `x`** ⟹ máquina de álgebra lineal / puntos extremos (vértices/aristas).
- Conecta con el argumento de signos de Bang (Vector 1, Hito 2): buscar el punto extremo que
  realiza la evasión.

## Verificación numérica (2026-06-28)
- **Correctitud de la reducción:** 62 coberturas genuinas (forma vectorial), **mín Σ|I_a| = 1.151 ≥ 1**.
- **Bound del área recuperado:** `max[μ(P) − rw(2−rw)] = +0.003` (ruido de grilla) ⟹ `Σrw ≥ 1/2`
  en la forma vectorial (la marginal de la uniforme bajo `f_a` es la "tienda" de pico ≤2).

## Qué da y qué NO da
- **DA:** un marco lineal limpio, afín-invariante, sin geometría de complementos (evita el hueco
  del "triángulo semejante" que mató los intentos de peeling). Toda la dificultad queda
  concentrada en UN lema combinatorio-lineal.
- **NO da (todavía):** el salto de `1/2` a `1`. El bound del área es ciego a la combinatoria del
  cubrimiento (ver nota 08: cap de medida única en `1/c∈[1/2,1)`). El lema tipo-Bang ES esa
  combinatoria.

## Próximo paso (Vector 1 sobre este marco)
Probar el lema tipo-Bang afín: versión NO simétrica del lema de Bang para la matriz
`U = (ũ_{a,i})` (filas = planks, columnas = vértices), que produzca la distribución evasora
cuando `Σ|I_a|<1`. El caso de **2 direcciones** (recientemente resuelto en la literatura) es el
sub-hito para calibrar la técnica antes de 3 direcciones (triángulo genérico).
