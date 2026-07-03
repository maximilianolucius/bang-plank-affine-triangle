# R10-2 — TEOREMA: δ = δ_c para toda terna no-paralela dos a dos (las cuñas de un nudo siempre alcanzan la cota de momentos)

> Date: 2026-07-03. Ejecuta `auditorias/58` R10-2. Status: **[PROVED]** —
> prueba humana completa abajo + verificación exacta a máquina
> (`experiments/delta_eq_deltac.py`: lema de conteo en 2928 pares externos
> `(q,a)` exactos; barrido de **507 ternas** sobre las tres clases de patrón,
> incluida la clase (b) nunca muestreada, con `δ == δ_c` y `p* ∈ T_u` en el
> 100%). **Sin cambios en el `.tex`** (congelación de numeración).

## Enunciado

**Teorema.** Para toda terna `u = (u₁,u₂,u₃)` de direcciones no-paralelas dos
a dos en el triángulo,
```
δ(u) = δ_c(u) = |c₀ − ½Σᵢcᵢ| / Σᵢ|cᵢ|,
```
donde `Σcᵢuᵢ ≡ c₀` es la dependencia afín. Equivalentemente: la proyección
`ℓ∞` del centro `(½,½,½)` sobre el plano imagen `Π` cae SIEMPRE en el
triángulo imagen `T_u`; las cuñas de un nudo de Prop 7.8 alcanzan SIEMPRE la
cota de momentos, y `δ` tiene forma cerrada racional.

(Tu pista era exacta: es el mismo conteo de signos con `Σq = 1` del lema de
no-concurrencia exterior, corrido a nivel general `a` en vez de `½`.)

## Prueba

**Paso 0 (reducción).** Por Prop 7.8(ii), `δ ≥ δ_c`, con igualdad ⟺
`p* ∈ T_u` (Prop 7.8(iii); `p*` = punto de `Π` ℓ∞-más-cercano al centro,
único si `δ_c > 0`). Si `δ_c = 0`, la igualdad es el Lema 7.9 (no-concurrencia
exterior): `δ_c = 0 ⟺ δ = 0`. Asumimos `δ_c > 0` y, por contradicción,
`p* ∉ T_u`.

**Paso 1 (normalización por flips).** El flip `uᵢ ↦ 1−uᵢ` transforma
`cᵢ ↦ −cᵢ, c₀ ↦ c₀−cᵢ`; deja invariantes `δ, δ_c` (cálculo directo:
`c₀−½Σc` y `Σ|c|` no cambian) y conjuga coherentemente `T_u` y `p*`
(reflexión `tᵢ ↦ 1−tᵢ` de la coordenada i). Flipeando cada `i` con `cᵢ < 0`:
**WLOG todos los `cᵢ > 0`**. Entonces `sign(cᵢ) = +1` para todo i y
`p* = (a,a,a)` con `a = ½ + ε·δ_c ∈ (0,1)` (`δ_c < ½`), `ε = sign(c₀−½Σc)`.

**Paso 2 (bajada al plano de Δ).** La evaluación `E(x) = (u₁(x),u₂(x),u₃(x))`
es una biyección afín del plano de Δ sobre `Π`: inyectiva porque `u₁,u₂`
no-paralelas son coordenadas afines del plano; la imagen es un 2-plano
contenido en `Π` (por la dependencia) y de su misma dimensión, luego igual.
Sea `q = E⁻¹(p*)`: un punto del plano con `uᵢ(q) = a` para `i = 1,2,3`, y
`p* ∉ T_u = E(Δ) ⟺ q ∉ Δ`.

**Paso 3 (lema de conteo a nivel general).**

> **Lema.** Sean `q` un punto del plano (`Σqⱼ = 1`) con `q ∉ Δ` (alguna
> coordenada baricéntrica negativa) y `a ∈ (0,1)`. Entonces a lo sumo DOS
> direcciones no-paralelas dos a dos toman el valor `a` en `q`.

Con el lema: `u₁,u₂,u₃` son tres direcciones no-paralelas con valor `a` en
`q`, luego `q ∈ Δ`: contradicción. Por tanto `p* ∈ T_u` y `δ = δ_c`. ∎

## Prueba del lema de conteo

Los flips biyectan {direcciones con valor `a` en `q`} con {valor `1−a` en
`q`} preservando paralelismo: WLOG `a ≤ ½`. El caso `a = ½` es el conteo del
Lema 7.9. Sea `a < ½`; escribimos `rⱼ = qⱼ − a`, `r'ⱼ = qⱼ − (1−a)`, de modo
que `rⱼ − r'ⱼ = 1−2a > 0`.

Una dirección de patrón `(j₀ ↦ 0, j₁ ↦ 1, j_s ↦ s)` toma en `q` el valor
`q_{j₁} + s·q_{j_s}`.

**(i) Caso `q_{j_s} = 0`:** valor `a` exige `q_{j₁} = a`, y entonces
`q_{j₀} = 1−a`, con lo que las tres coordenadas son ≥ 0: `q ∈ Δ`, excluido.
Luego todo patrón solvable tiene `q_{j_s} ≠ 0` y `s = (a−q_{j₁})/q_{j_s}`
único; `s ∈ [0,1] ⟺ a` está débilmente entre `q_{j₁}` y `1−q_{j₀}` ⟺
`r_{j₁}·r'_{j₀} ≥ 0`.

**(ii) Paralelismo y colisiones:** paralelo ⟺ flip o igual. El flip de una
solución toma valor `1−a ≠ a` (aquí `a < ½`): dos soluciones distintas nunca
son paralelas. Con `s ∈ (0,1)` (signos estrictos) el patrón está determinado
por la dirección: patrones estrictos distintos ⟹ direcciones distintas. Los
casos frontera son tipo-faceta y COLISIONAN: `s = 0` (⟺ `r_{j₁} = 0`) da la
dirección `x_{j₁}` desde AMBOS patrones `(j₀,j₁)` y `(j_s,j₁)`; `s = 1`
(⟺ `r'_{j₀} = 0`) da `1−x_{j₀}` desde ambos `(j₀,·)`. Así:
```
N = #{patrones con signos estrictos} + #{j : rⱼ = 0} + #{j : r'ⱼ = 0},
```
con cada índice-cero aportando UNA dirección (`x_j`, resp. `1−x_j`; nunca
paralelas entre sí para índices distintos, y `rⱼ = r'ⱼ = 0` es imposible).

**(iii) Conteo bajo externalidad.** Sea `q_m < 0` (existe): `r_m, r'_m < 0`
estrictos. Sean `{j,k}` las otras dos coordenadas: `qⱼ + q_k = 1 − q_m > 1`.

*Caso (3): `rⱼ, r_k ≤ 0`* (ambas `≤ a`): `qⱼ + q_k ≤ 2a < 1` — imposible.

*Caso (2): exactamente una positiva*, digamos `rⱼ > 0 ≥ r_k`. Entonces
`qⱼ = 1 − q_m − q_k > 1 − 0 − a = 1−a`, luego `r'ⱼ > 0` estricto. Patrones
estrictos: lado positivo (`r'_{j₀} > 0 ∧ r_{j₁} > 0`): `j₀ = j` pero no hay
`j₁ ≠ j` con `r > 0`: cero. Lado negativo (`r'_{j₀} < 0 ∧ r_{j₁} < 0`):
`j₀, j₁ ∈ {k, m}` (nota `r'_k = r_k − (1−2a) < 0` estricto): si `r_k < 0`:
dos patrones `(k,m), (m,k)`, ceros 0 ⟹ `N = 2`; si `r_k = 0`: un patrón
`(k,m)` más el cero `x_k` ⟹ `N = 2`.

*Caso (1): ambas positivas* (`rⱼ, r_k > 0`). Subcasos por los signos de
`(r'ⱼ, r'_k)`:
- ambos `> 0`: estrictos = `(j,k), (k,j)` (el lado negativo exigiría
  `j₀ = m = j₁`): `N = 2`.
- `r'ⱼ > 0 > r'_k`: estrictos = `(j,k)` y `(k,m)`: `N = 2`.
- `r'ⱼ > 0 = r'_k`: estricto `(j,k)`; cero `1−x_k`: `N = 2`.
- ambos `< 0`: estrictos = `(j,m), (k,m)`: `N = 2`.
- `r'ⱼ = 0 > r'_k`: estricto `(k,m)`; cero `1−x_j`: `N = 2`.
- `r'ⱼ = r'_k = 0`: sin estrictos; ceros `1−x_j, 1−x_k`: `N = 2`.

En todos los casos `N ≤ 2`. ∎

## Verificación a máquina (exacta, `delta_eq_deltac.py`)

- **A (lema):** 2928 pares externos `(q,a)` racionales aleatorios:
  enumeración de los 6 patrones, agrupación por clases de paralelismo
  `{v, 1−v}`: `N ≤ 2` en el 100% (assert).
- **B (teorema):** 507 ternas exactas — 222 cíclicas (incl. sandwich y
  medianas), 220 de clase (b) (nunca muestreada antes), 60 all-shared
  (dependencia homogénea `c₀ = 0`, manejada vía kernel — bug de la
  normalización `c₀ = 1` encontrado y corregido en el barrido), facetas y 4
  inclinadas. En el 100%: `δ` (LP exacto) `= δ_c` (fórmula) y el test
  punto-en-triángulo `p* ∈ T_u` (resolviendo `q` exacto y chequeando
  `q ≥ 0`, con la consistencia `u₃(q) = p*₃` asertada).
- **C:** ninguna terna no-faceta del barrido alcanza `δ = 1/6` (soporte al
  lema de unicidad de `notes/54-R10-1 §5`).

## Consecuencias (para integrar tras el dictamen de Rosa — .tex congelado)

1. `δ(u)` tiene **forma cerrada racional** — el LP de `δ` sobra como
   definición operativa; la grilla de δ-landscape queda obsoleta.
2. **Las cuñas de un nudo siempre alcanzan la cota de momentos**: la
   jerarquía de Rem 7.10 colapsa por la izquierda (`1/(1−2δ_c) = 1/(1−2δ)`
   siempre); junto con los certificados de R10-1, la foto completa es
   `momentos = cuñas-1-nudo < D` estrictamente en ternas explícitas.
3. Prop 7.8(iii) se convierte en teorema incondicional; Rem 7.10 y la frase
   "we do not claim equality in general" se reescriben; Problem 10.3 pierde
   su primera mitad (respondida: NO exacta en general) y queda enfocado en
   `sup D = 3/2?`.
4. La dependencia con `c₀ = 0` (clase all-shared) es un caso degenerado real
   que la redacción de Prop 7.8 debe acomodar al integrarse (hoy la prueba
   asume implícitamente la normalización `c₀` arbitraria — la fórmula de
   `δ_c` ya es homogénea y correcta; solo hay que decirlo).
