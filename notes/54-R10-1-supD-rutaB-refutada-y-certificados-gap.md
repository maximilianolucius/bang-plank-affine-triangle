# R10-1 — sup D: Ruta B refutada en la calibración; certificados duales que baten la cota de momentos; sandwich con gap probado; sin D>3/2 a la vista

> Date: 2026-07-03. Ejecuta `auditorias/58` R10-1. **Regla de congelación respetada:
> CERO cambios en el `.tex`** — todo vive aquí y en `experiments/`.
> Scripts: `gardner_third_marginal.py` (Ruta B), `supD_dual_hunt.py` +
> `supD_hunt_phase2.py` (Ruta A), **`dual_certificates.py` (verificador
> autocontenido de los certificados insignia, sin scipy — el artefacto
> load-bearing)**. Todos "ALL OK"/certificados exactos.

## Veredicto de la ronda en una línea

`sup D` sigue **[OPEN]** en `[3/2, 2]`, pero la ronda produjo un teorema
negativo limpio (Ruta B muerta con la obstrucción exacta), y el resultado
positivo mayor: **la cota de momentos NO es exacta en general** — tres
certificados duales exactos la baten, incluido el sandwich original.
`D(u) = 1/(1−2δ(u))` es FALSO como identidad general: la primera mitad del
Problem 10.3 queda respondida (negativamente) con certificados archivados.

## 1. Ruta B (mezcla de testigos de Gardner): REFUTADA en el test crítico [PROVED]

Tu derivación de la mezcla es correcta y quedó verificada
(`gardner_third_marginal.py` check 1): con testigos de par `ν_jk` y
`μ = ⅓Σν_jk`, cada marginal tiene densidad `≤ ⅔ + M_i/3`; el objetivo 3/2
equivale a `M ≤ 5/2`. Pero el test crítico da **`M*(λ₁,λ₂;λ₃) = +∞`, no 5/2
— y no hizo falta LP**, el argumento de momentos decide:

> **[PROVED]** Todo testigo de par para `(λ₁,λ₂)` tiene `E[λ₁]=E[λ₂]=½`
> (media de marginal uniforme) ⟹ `E[λ₃] = 1−½−½ = 0` con `λ₃ ≥ 0` ⟹
> `λ₃ = 0` ν-c.s. ⟹ la tercera marginal es el **átomo δ₀**. Ni siquiera es
> absolutamente continua: ningún `M` finito existe.

- **Pesos desiguales también mueren** [PROVED]: la restricción por dirección
  es `w_{par-malo}·(M_i − 1) ≤ D − 1`; `M_i = ∞` fuerza los tres pesos a 0,
  contra `Σw = 1` (cada par es "malo" para exactamente una dirección).
- **Lema del costo de par** [PROVED, la obstrucción general]: si las
  mid-lines de `u_j,u_k` se cortan en el punto único `q_jk` (que está en Δ:
  Gardner da existencia y el baricentro del testigo ES `q_jk`), entonces
  `M*(u_j,u_k;u_i) ≥ 1/(2·min(m, 1−m))` con `m = u_i(q_jk)` — la media de la
  tercera marginal está FORZADA. En facetas `m = λ₃(½,½,0) = 0` (recupera
  `M* = ∞`); en concurrentes `m = ½` y `M* = 1` (alcanzado por `μ_p`). La
  ruta pura solo podría operar donde todo `u_i(q_jk) ∈ [1/5, 4/5]` — nunca
  en/cerca de facetas, que es donde vive el peor caso. **Documentado: esto es
  lo que mata la ruta, no la mezcla en sí.**
- Rescate honesto: mezclar medidas de par *relajadas* (marginales `≤ a·Leb`)
  da `D ≤ (2a+b)/3` y en facetas el lazo realiza `a=b=3/2` — pero eso ya no
  es un lunch gratis de Gardner: es volver a construir medidas por terna.
  [OPEN como técnica, sin ventaja identificada.]

## 2. Ruta A (cacería dual multi-nudo): la cota de momentos CAE [PROVED]

Herramienta implementada como ordenaste (`supD_dual_hunt.py`): ψ lineales a
trozos sobre nudos racionales; el mínimo de `Σψᵢ(uᵢ(x))` se alcanza en los
vértices del complejo de rectas de nivel (todos exactos en ℚ); scipy solo
**guía** — el bound reportado se re-deriva íntegro en `fractions`
(racionalizar ψ, renormalizar masa exacta, mínimo exacto sobre los vértices,
más un sanity check independiente con 400 puntos interiores exactos). Por
dualidad débil cualquier ψ admisible certifica: del lado dual no hay grilla
que mienta.

**Certificados insignia (archivados y auto-verificables en
`dual_certificates.py`):**

| terna | momentos `1/(1−2δ)` | certificado dual | holgura |
|---|---|---|---|
| facetas inclinadas `ε=1/10` (cíclica `(1,1/10,0)`-shift) | `15/11 ≈ 1.36364` | **`D ≥ 18/13 ≈ 1.38462`** | `3/143 ≈ 0.021` |
| clase (b) `(t₁,t₂,t₃)=(2/3,5/6,1/12)` | `153/142 ≈ 1.07746` | **`D ≥ 32/29 ≈ 1.10345`** | `≈ 0.026` |
| **sandwich `τ=(13/25,½,½)`** | `225/224 ≈ 1.0044643` | **`D > 225/224`** (mín exacto `≈ 1.0044772`) | `≈ 1.3·10⁻⁵` |

- El del sandwich es el pedido explícito de (ii): **primera prueba de gap
  momentos < D** en el ejemplo original; el sandwich queda
  `225/224 < D ≤ 112/111` (estrictamente abierto por abajo ahora).
  Con nudos uniformes NO salió (q=10..50 dieron ≤ 226/225 < 225/224); hicieron
  falta nudos adaptados (`1/225, 224/225, 13/25, …`, q=45).
- `18/13` y `32/29` son limpios y con ψ sparse (~10–20 nudos no nulos);
  el verificador los reconstruye desde cero sin scipy.
- Consecuencia estructural (con el teorema R10-2 `δ = δ_c`): la jerarquía
  queda **completamente resuelta**: cuñas de 1 nudo = cota de momentos
  SIEMPRE, y ψ multi-nudo la baten ESTRICTAMENTE en ternas explícitas.
  `D(u) = 1/(1−2δ(u))` es falso en general (sigue cierto en facetas —
  toda dimensión — y en el lugar concurrente).

## 3. ¿D > 3/2? No apareció [OPEN, con el mapa de lo barrido]

- **Clase (b)** (147 ternas por momentos + duales en extremos): el máximo de
  momentos en la clase se acerca a 3/2 solo en la esquina
  `(η, 1−η, η) → facetas mod flips` (la clase degenera a las facetas).
  Duales certificados allí: `η=1/12: 1.38698`, `η=1/24: 1.43945`,
  `η=1/48: 1.46924` — suben hacia 3/2 **desde abajo**, sin cruzarlo.
- **Facetas inclinadas**: `ε=1/10: 18/13 = 1.3846`, `ε=1/20: 10/7 = 1.4286`
  — misma foto: los duales exceden momentos pero se aproximan a 3/2 sin
  cruzarlo. (UB del lazo congelado en `ε=1/10`: empujar el lazo inscrito por
  las direcciones inclinadas da marginales `≤ 135/76 ≈ 1.776` — bracket
  `D(tilt 1/10) ∈ [18/13, 135/76]`.)
- Los UB de esqueleto explotan cerca de la esquina (13/3, 25/3, 49/3 —
  consistente con `D_∂(facetas) = ∞`), así que por arriba solo tenemos el 2
  uniforme lejos del esqueleto; el sublevel real queda sin bracket fino.
- Lectura honesta: **[EVIDENCE]** de que las facetas son máximo local (todo
  lo certificado cerca queda < 3/2), cero evidencia de terna > 3/2.
  `sup D ∈ [3/2, 2]` sigue [OPEN].

## 4. Casi-paralelo (iv): lema de continuidad [PROVED]

- **General**: `D` es **inferiormente semicontinua** en los valores de
  vértice: por dualidad, `D = sup_ψ min_x Σψᵢ(uᵢ(x))` es un sup de funciones
  continuas de la terna (mín sobre compacto de función conjunta continua).
  [PROVED, un párrafo — la dualidad lo da gratis.]
- **Camino explícito** `V(ε) = clase-b(1/3, 1/3+ε, 1/2)` (u₂ → u₁):
  - UB [PROVED simbólico]: pesos de esqueleto
    `(w_AB, w_BC, w_CA) = ((1+3ε)/4, (2−3ε)/4, 1/4)` dan todas las densidades
    `≤ 1 + (3/4)ε` en `ε ∈ (0, 2/3)` (dos activas — LP tight).
  - LB [PROVED simbólico]: dependencia `c = ((ε+4/3)/ε, −4/(3ε), 2)`,
    `δ_c = 3ε/(2(9ε+8))`, momentos `= 1 + 3ε/(2(3ε+4))`.
  - **`1 + 3ε/(2(3ε+4)) ≤ D(V(ε)) ≤ 1 + (3/4)ε`: `D → 1` linealmente** al
    degenerar al par (consistente con Gardner `D=1` para dos direcciones).
    La intuición traicionera quedó medida: el límite es PEQUEÑO, sin salto.

## 5. Unicidad del maximizador de δ [PROVED — el "tema de una línea"]

**Lema.** Una terna no-paralela dos a dos tiene `δ(u) = 1/6` ⟺ es la terna
de facetas módulo flips.

*Prueba.* (⇐) Prop 7.2. (⇒) `δ ≤ max_i|u_i(G)−½| ≤ 1/6` fuerza que G sea
minimizador con valor exacto 1/6. Sea `B = {i : |u_i(G)−½| = 1/6}` (≠ ∅);
para `i ∈ B` el valor interior es `s_i ∈ {0,1}`, i.e. `u_i ∈ {x_v, 1−x_v}`,
y el gradiente "de mejora" normalizado por flips es `g_i = ∇x_{v_i}`. Si
existiera dirección `d` con `⟨g_i, d⟩ > 0` para todo `i ∈ B`, los puntos
`G + td` (t pequeño) tendrían `max_i |u_i−½| < 1/6` (los no-vinculantes
siguen < 1/6 por continuidad): contradicción. Por el teorema de Gordan,
`0 ∈ conv{g_i : i ∈ B}`. `|B| = 1` es imposible (`g ≠ 0`); `|B| = 2` forzaría
`g_i ∥ g_j`, i.e. `u_i ∥ u_j` — excluido. Luego `|B| = 3`: las tres
direcciones son tipo-faceta, y no-paralelismo fuerza tres vértices distintos:
facetas módulo flips. ∎

(Soporte a máquina: en los barridos exactos de la ronda ninguna terna
no-faceta alcanza `δ = 1/6`.)

## 6. Cierre R10-1 (criterio 3 del jefe)

Ninguno de los dos desenlaces mayores cayó; entregamos el paquete del
desenlace 3, mejorado:
1. `M*(facetas)` exacto: **+∞** (no 5/2) — Ruta B refutada con obstrucción
   documentada [PROVED].
2. **Sandwich decidido por abajo**: `225/224 < D ≤ 112/111` — primera prueba
   de gap momentos < D [PROVED]; añadidos dos gaps limpios más
   (`18/13 > 15/11`, `32/29 > 153/142`) [PROVED].
3. Lema de continuidad del punto (iv): lsc general + camino con tasas
   lineales exactas de dos lados [PROVED].
4. Unicidad del maximizador de δ [PROVED].
5. `sup D ∈ [3/2, 2]` [OPEN]; mapa de caza documentado (esquina de clase (b)
   y facetas inclinadas suben hacia 3/2 desde abajo sin cruzarlo).

**Sin tocar el `.tex`** (congelación). Material listo para integrarse tras el
dictamen de Rosa: los tres certificados-gap + δ=δ_c (R10-2) reescriben
Rem 7.10/7.17 y el Problem 10.3; el lema de unicidad y el de continuidad son
enunciados nuevos al final de §7.
