# R5-3 — TEOREMA del perímetro ponderado: Bang PROBADO para la familia cíclica de concurrencia

> Date: 2026-07-02. Status: **[PROVED — verificado simbólico + MC]**. Resuelve R5-3 por
> **construcción** (el desenlace bueno), y no solo para UNA terna no-mediana: para **toda la
> sub-familia cíclica** (2-paramétrica) de la superficie de concurrencia. Es el salto
> "medianas → familia genérica" que pedía `auditorias/49 §R5-3` / R4-4.
> Scripts: `experiments/concurrent_nonmedian_triple.py` (terna exacta),
> `concurrent_perimeter_densities.py` (descubrimiento), `weighted_perimeter_theorem.py`
> (verificación simbólica de las 6 identidades + MC en 3 ternas).

---

## 1. Enunciado

**Teorema (perímetro ponderado).** Sea `p=(p_A,p_B,p_C)` interior al triángulo con
`max_j p_j < 1/2` (interior del **triángulo medial**). Sean `u_1,u_2,u_3` las direcciones
normalizadas del **patrón cíclico** concurrentes en `p`:

```
u_1 = (τ_1, 0, 1),  u_2 = (0, 1, τ_2),  u_3 = (1, τ_3, 0)      (valores en A,B,C)
τ_1 = (1/2−p_C)/p_A,   τ_2 = (1/2−p_B)/p_C,   τ_3 = (1/2−p_A)/p_B .
```

Entonces la medida `μ_p` = **uniforme en cada arista con masas**

```
w_AB = 1−2p_C ,   w_BC = 1−2p_A ,   w_CA = 1−2p_B      (suma = 1)
```

tiene marginal **uniforme** `u_{i#}μ_p = Leb[0,1]` para las tres direcciones. En
consecuencia (criterio de transporte, `notes/36 §1`): **toda cobertura del triángulo por
planks en las direcciones `u_1,u_2,u_3` cumple `Σ rw ≥ 1`** (Bang, constante óptima).

**Casos particulares:** `p = centroide` ⟹ `τ_i=1/2`, masas `1/3` = el teorema de las
medianas (`notes/36`). `p≠centroide` ⟹ ternas **genéricas no-mediana** (e.g.
`p=(9/20,3/10,1/4)`: `τ=(5/9,4/5,1/6)`, masas `(1/2,1/10,2/5)`).

---

## 2. Prueba (6 identidades; el mecanismo es `(1−2x)/(1/2−x)=2`)

Trazas de `u_i` sobre las aristas (parametrizadas `t∈[0,1]`): cada `u_i` es **full-range**
en la arista que conecta su vértice-0 con su vértice-1 (`u_1` en BC, `u_2` en AB, `u_3` en
CA), y afín sobre `[0,τ_i]` / `[τ_i,1]` en las otras dos. El pushforward de "uniforme con
masa `w_e`" por un mapa afín de rango `[a,b]` es uniforme de densidad `w_e/|b−a|` en `[a,b]`.
La marginal de `u_1` tiene densidad:

- en `[0,τ_1]`: `w_BC + w_AB/τ_1` (BC full + AB comprimida);
- en `[τ_1,1]`: `w_BC + w_CA/(1−τ_1)`.

Uniformidad ⟺ ambas `=1`; análogamente para `u_2, u_3` — **6 ecuaciones**. Con las masas
del enunciado, cada término compuesto colapsa:

`w_AB/τ_1 = (1−2p_C)·p_A/(1/2−p_C) = 2p_A`, y `w_BC + 2p_A = (1−2p_A)+2p_A = 1`. ✓

Las 6 se verifican idénticamente igual (`1−τ_1=(1/2−p_B)/p_A`, etc., usando `Σp_j=1`).
**Verificación simbólica** (`sympy`): las 6 expresiones simplifican a `1` exacto.
**Verificación MC**: marginales planas (dev ≈ ruido 0.015) en 3 ternas, incl. la exacta
`τ=(5/9,4/5,1/6)`. ∎

**Dominio exacto:** `τ_i∈(0,1)` para las tres ⟺ `max_j p_j<1/2` ⟺ las tres masas `>0`.
Las dos condiciones **coinciden**: toda terna cíclica válida admite la medida. (En el borde
del medial, `p_j=1/2`, una masa se anula y una `τ_i∈{0,1}`: degenera a caso de 2 direcciones.)

---

## 3. Qué resuelve y qué queda abierto

- **[PROVED] Suficiencia COMPLETA para el patrón cíclico:** toda terna cíclica concurrente
  (familia **2-paramétrica**, `p` en el medial abierto) admite medida de marginal uniforme
  **explícita** ⟹ Bang probado para **una familia 2-dim de ternas genéricas no-faceta,
  no-mediana**. Antes solo estaba el punto de las medianas; la suficiencia general era
  `[OPEN]` con evidencia LP (453/453, `notes/37/38`). La evidencia LP queda **explicada**:
  las pasadoras testeadas de patrón cíclico tienen esta medida.
- **El patrón anti-cíclico** (roles `0↔1` intercambiados) se cubre por reflexión (simetría
  del triángulo). **[PROVED]**
- **[OPEN] Patrones mixtos:** ternas concurrentes donde las asignaciones de roles no forman
  ciclo (p.ej. dos direcciones con el mismo vértice-0). La construcción no aplica verbatim;
  la suficiencia general de `cond=2` (toda asignación) sigue abierta. También sigue abierto
  si estas ternas admiten **teselación** con `Σr=1` esencial (tightness tipo medianas;
  `notes/38 §1` daba `min≈1.0003` ambiguo para una genérica).
- **Relación con Gardner:** esto responde afirmativamente, para la sub-familia cíclica, la
  pregunta finita abierta de Gardner (`notes/43-P3`) en 3 direcciones — con una medida tan
  simple como la suya de 2 direcciones (Lebesgue sobre segmentos, aquí las aristas
  ponderadas).

---

## 4. Impacto en el paper (aplicado)

Nuevo teorema en la sección de concurrencia (`drafts/affine-plank-triangle.tex`):
"weighted-perimeter theorem" — sube el techo de "medianas" a **familia cíclica completa**.
La Prop `perímetro⟺τ=½` (`notes/48`) queda como el caso equiponderado (masas iguales ⟺
`p=centroide`): consistente, no contradicho (aquella era la medida del perímetro **uniforme
1/3**; ésta pondera por arista).

Rigidez de la familia (¿la igualdad `Σr=1` esencial fuerza teselación única?) — **[OPEN]**,
análogo natural de `notes/45` para `p≠centroide`; siguiente objetivo barato.
