# R7-1 — VEREDICTO: el mecanismo ponderado SÍ se extiende a `Δ³` (familia 1-paramétrica); en `d≥4` el 1-esqueleto muere

> Date: 2026-07-02. Status: **[PROVED — álgebra lineal exacta, sympy sobre ℚ y ℚ(σ)]**.
> Resuelve `auditorias/51 §R7-1` / `auditorias/52 §R7-1` con veredicto binario POSITIVO
> en `d=3` (más fuerte: familia con formas cerradas) y certificado NEGATIVO limpio para
> el 1-esqueleto en `d≥4`.
> Script: `experiments/simplex3_weighted_skeleton.py` (corre limpio, todo exacto).

## 0. Precisión previa obligada: la definición de notes/47 degenera en `Δ³`

La generalización literal de notes/47 (`m_i(e_{i+1})=0, m_i(e_{i-1})=1`, resto `½`)
es **degenerada** en `Δ³`: `m₃ = 1−m₁` y `m₄ = 1−m₂` (pares de flip) — solo 2
direcciones efectivas, fuera del marco pairwise-non-parallel. [PROVED, trivial]
(Su sistema de esqueleto igualmente resuelve: familia 1-paramétrica
`w₀₁=w₂₃=t, w₀₃=w₁₂=½−t`, `t∈[0,½]` — anecdótico.)

La generalización cíclica **no degenerada** es `u_i(e_i)=0, u_i(e_{i+1})=1`, resto `½`
(mod 4): 4 direcciones **pairwise non-parallel** (verificado a mano por rango afín,
todas las clases cíclicas de pares), mid-planos `{u_i=½}` concurrentes en el centroide.
Estas son las "medianas" correctas de `Δ³`: `{u_i=½}` es el plano por la arista
`e_{i+2}e_{i+3}` y el punto medio de la arista opuesta `e_ie_{i+1}`.

## 1. Teorema (medianas cíclicas de `Δ³`) [PROVED]

**La medida `μ = ½·Unif(e₁e₃) + ½·Unif(e₂e₄)`** (masas iguales en las dos diagonales
del 4-ciclo, uniformes en parámetro) **tiene marginal `Leb[0,1]` bajo las cuatro
direcciones** — y es la ÚNICA medida de esqueleto que lo logra (las 4 aristas del ciclo
son constantes para alguna dirección ⟹ átomo ⟹ masa 0; las diagonales quedan forzadas).

Consecuencia (mecanismo de transporte, como Prop 6.1): **toda cobertura de `Δ³` por
planks en esas 4 direcciones cumple `Σrw ≥ 1`** — primera instancia del programa en
`d=3`. Responde el primer test del Problem 2 del paper.

## 2. Teorema (familia `σ`) [PROVED] — el análogo del "peso desigual"

Familia cíclica `u_i = (0, 1, σ, 1−σ)` en `(e_i, e_{i+1}, e_{i+2}, e_{i+3})`,
`σ ∈ (0,1)` (σ=½ = medianas). Para `0<σ<½`, el sistema exacto de 12 condiciones de
densidad en 6 pesos tiene solución **única** con formas cerradas:

```
aristas del ciclo {i,i+1}:  a(σ) = (1−σ)(1−2σ) / (2(σ²−4σ+2))
diagonales {1,3},{2,4}:     b(σ) = σ(2−3σ)     / (2(σ²−4σ+2))
```

- `4a+2b = 1` idénticamente ✓; positividad en todo `(0,½)`: `σ²−4σ+2 > 0` porque sus
  raíces son `2±√2` y `(0,½)⊂(0,2−√2)` [PROVED]; `σ>½` por el flip `u↦1−u` + relabel.
- En `σ=½`: `a→0, b→½` — recupera el Teorema §1 con continuidad perfecta.
- **Necesidad:** para la familia cíclica general `(σ,ρ)`, `V` es circulante ⟹ la
  concurrencia de los 4 mid-planos en el hiperplano de `Δ³` **fuerza `ρ=1−σ` y
  `p = centroide`** (verificado exacto). Es decir: dentro de la familia cíclica de `Δ³`
  no existe el análogo de "mover `p`" — la familia sharp-candidata es 1-paramétrica y
  toda ella concurre en el centroide. El análogo real de `p≠centroide` requiere
  asignaciones NO cíclicas (el barrido tipo-216 de `Δ³` es el siguiente paso natural,
  no ordenado en esta ronda).

Consecuencia: `Σrw ≥ 1` para coberturas por planks en las direcciones de la familia
`σ`, para **todo** `σ∈(0,1)`. El paper salta de `d=2` a instancias genuinas en `d=3`.

## 3. Certificado negativo en `d≥4` [PROVED]

Para las medianas cíclicas de `Δ^d` (`0,1` en `e_i,e_{i+1}`, resto `½`), **toda** arista
`{j,k}` de `Δ^d` es constante para alguna dirección: en un ciclo de `n=d+1≥5` vértices,
quitados 2, el resto (≥3 en arcos) siempre contiene un par consecutivo `{m,m+1}`
disjunto de `{j,k}`, y `u_m` vale `½` en ambos extremos ⟹ átomo ⟹ `w_{jk}=0`.
Verificado combinatoriamente `d=4..7`; el argumento del arco es general [PROVED].
**Ningún witness soportado en el 1-esqueleto existe en `d≥4`** — la masa debe subir a
2-caras (densidades lineales a trozos, sigue siendo LP). [OPEN, es el paso 2 de la
orden R7-1 si se decide continuar.]

## 4. Qué entra al paper

Sección corta "Higher dimensions: a witness family on the 3-simplex":
teorema §1+§2 (familia `σ` con formas cerradas y unicidad de esqueleto), la
proposición negativa §3, y la observación de necesidad (`ρ=1−σ`, `p=centroide`).
Con etiqueta honesta: tightness en `Δ³` (¿existe cobertura con `Σrw=1` en esas
direcciones?) queda [OPEN] — la rigidez tipo-Thm 6.6 no se ha estudiado en `d=3`.
