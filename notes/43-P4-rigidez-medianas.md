# P4 — Rigidez de la teselación mediana (cota + igualdad)

> Date: 2026-06-30. Status: **cota [PROVED] (notes/36); rigidez [PROVED en el régimen
> genérico] + [grid-exacta en el resto]**. Cierra (casi por completo) la Prioridad 2 de
> `auditorias/00-ordenes-de-trabajo.md`, arreglando el defecto de `auditorias/39 §A.1`.
> Verificación: `fractions` exacto (`scratchpad/p4_rigidez.py`, `p4_lin.py`).

---

## 0. Enunciado

**Teorema (medianas, cota + rigidez).** Sean `P_i={m_i∈I_i}` los 3 planks medianos del
triángulo (`m1,m2,m3` las medianas normalizadas, `notes/36`). Si `P_1∪P_2∪P_3 ⊇ Δ` con los
tres anchos `r_i=|I_i|>0`, entonces `Σr_i ≥ 1`, con **igualdad sii `I_i=[1/3,2/3]` para todo
`i`** (la teselación tercio-central).

(La **cota** `Σr≥1` ya estaba PROBADA en `notes/36` por transporte con la medida del
perímetro. Esta nota prueba la **rigidez/igualdad**, que estaba `[OPEN]`.)

Nota sobre degeneración: si se permite `r_i=0`, el cover degenerado `I_1=[0,1]` (`r_1=1`),
`P_2,P_3` triviales tiene `Σr=1` y no es la tercio-central. Por eso el enunciado exige
`r_i>0` (los tres planks esenciales). Es la misma exclusión de `notes/33 §2`.

---

## 1. Reducción a teselación de las 3 aristas [PROVED]

Por la prueba de transporte (`notes/36`), la medida del perímetro `μ` (uniforme en las 3
aristas, peso 1/3 c/u) tiene marginal uniforme en cada mediana, y da
`1=μ(Δ)≤Σμ(P_i)≤Σr_i`. La **igualdad** `Σr_i=1` fuerza las dos igualdades:

1. `μ(P_i)=r_i` para todo `i` ⟹ `I_i⊂[0,1]` (sin desperdicio de intervalo fuera de `[0,1]`).
2. `Σμ(P_i)=μ(∪P_i)=μ(Δ)=1` con cobertura ⟹ los `P_i` son **`μ`-disjuntos** (partición a.e.).

Como `μ` vive en las 3 aristas, (2) significa: **en cada arista, las 3 trazas
`P_i∩arista` particionan `[0,1]`** (parámetro de la arista) a.e. — disjuntas y de longitud
total 1. Esto es una condición **necesaria** de la igualdad. (Corrige `auditorias/39 §A.1`:
la cobertura del interior es hipótesis dada; lo que la igualdad AÑADE es la partición exacta
de la frontera.)

**Rangos por arista** (verificados, `notes/39`, con `m1=½−y/2+z/2, m2=y+z/2, m3=1−y/2−z`):
- **AB** (param `t=m2∈[0,1]`): `m2` full; `m1∈[0,½]`; `m3∈[½,1]`.
- **BC** (param `t=m1∈[0,1]`): `m1` full; `m2∈[½,1]`; `m3∈[0,½]`.
- **CA** (param `s∈[0,1]`): `m3` full; `m1∈[½,1]`; `m2∈[0,½]`.

Con `a_i=|I_i∩[0,½]|`, `b_i=|I_i∩[½,1]|` (`r_i=a_i+b_i`), las **ecuaciones de longitud**
(cada arista suma 1):
```
(AB)  r2 + 2a1 + 2b3 = 1
(BC)  r1 + 2b2 + 2a3 = 1
(CA)  r3 + 2b1 + 2a2 = 1
```
Su suma es `Σr + 2Σ(a_i+b_i) = 3Σr_i = 3 ⟺ Σr=1` (**automática dado `Σr=1`**; las 3
ecuaciones son de rango 3, espacio de soluciones **3-dimensional** — corrige el "2-dim" de
`notes/39`, defecto menor de `auditorias/39`). Las ecuaciones de longitud **solas** no fijan
`I_i`; hace falta el **abutting** (las trazas deben pegar, no solo tener la longitud correcta).

---

## 2. Régimen genérico (cada `I_i` cruza `½`): rigidez [PROVED]

**Lema (concurrencia).** El centroide `G=(1/3,1/3)` tiene `m(G)=(½,½,½)`. Como `G∈Δ` debe
estar cubierto, **algún `I_i` contiene `½`**. En el régimen genérico los tres lo contienen
(`l_i<½<h_i`), luego `a_i=½−l_i`, `b_i=h_i−½`.

**Orientación forzada de las trazas (genérico).** Cada traza "mitad" está anclada a un
vértice concreto, porque su mapa afín alcanza el extremo del intervalo cuando `I_i` cruza `½`:
- En AB: la traza de `P_1` (parte `m1∈[0,½]`) tiene extremo en `t=0` (vértice `A`) pues
  `h1>½`; la de `P_3` (parte `m3∈[½,1]`) tiene extremo en `t=1` (vértice `B`) pues `l3<½`.
  `P_2=[l2,h2]` queda en el medio. **El orden en AB es forzado:** `P_1 | P_2 | P_3`.
- Análogo (por la simetría `S_3` de la configuración) en BC: `P_3 | P_1 | P_2`; en CA:
  `P_1 | P_3 | P_2`.

**Ecuaciones de abutting (genérico, orden forzado).** Igualando extremos consecutivos:
```
AB:  1−2l1 = l2 ,   h2 = 2−2h3
BC:  1−2l3 = l1 ,   h1 = 2−2h2
CA:  2h1−1 = 1−h3 (⟹ h3=2−2h1) ,   1−l3 = 2l2 (⟹ l3=1−2l2)
```
Sistema lineal exacto (verificado `p4_lin.py`). Las tres ecuaciones de los `l`:
`l1=1−2l3, l3=1−2l2, l2=1−2l1` ⟹ `l1=1−2(1−2(1−2l1))=3−8l1 ⟹ 9l1=3 ⟹ l1=1/3`, y
`l2=l3=1/3`. Las de los `h`: `h1=2−2h2, h2=2−2h3, h3=2−2h1` ⟹ `9h1=6 ⟹ h1=2/3`,
`h2=h3=2/3`.

> **Conclusión [PROVED]:** en el régimen genérico (los tres `I_i` cruzan `½`), la única
> teselación mediana es `I_i=[1/3,2/3]`, `r_i=1/3`.

---

> **[ACTUALIZADO 2026-07-01 — `notes/45` (R2-2): el régimen no-genérico está ahora PROBADO
> exactamente, sin grid.** Enumeración simbólica (`sympy`) de los 27 patrones de cruce × todos
> los órdenes ⟹ el edge-tiling tiene **exactamente 3** soluciones (`[1/3,2/3]³`, `[0,1/3]³`,
> `[2/3,1]³`); las dos últimas **no cubren el centroide** `G` (`m(G)=(½,½,½)`), luego la única
> cobertura con `Σr=1` es la tercio-central. La rigidez es **PROVED completo**; lo de abajo
> (grid) queda como verificación redundante.]**

## 3. Régimen no-genérico y verificación global [grid-EXACTA, ahora redundante — ver notes/45]

Falta el caso en que algún `I_i` **no** cruza `½` (⟹ `a_i=0` o `b_i=0`; ese plank no aparece
en una de las 3 aristas). Por el Lema de concurrencia, a lo sumo dos `I_i` pueden no contener
`½`. Estos sub-casos se reducen a finitos sistemas lineales (un análisis por orden/anclaje,
como §2). **Verificación exacta (`fractions`, `p4_rigidez.py`):** búsqueda EXHAUSTIVA de
teselaciones (`Σr=1`, tres planks `r_i>0`, con chequeo de cobertura del **interior** en malla
`/(4D)`) sobre endpoints en malla `/D`:

```
D=6:  1 teselación   D=9:  1 teselación   D=12: 1 teselación
      todas = ((1/3,2/3),(1/3,2/3),(1/3,2/3))
```

En los tres refinamientos aparece **exactamente una**: la tercio-central. Esto cubre los
casos no-genéricos con endpoints racionales de denominador ≤12 (incluye `l=0, h=½, h=1`, etc.)
e **incluye la cobertura del interior** (no solo la frontera), cerrando el defecto de
`auditorias/39 §A.1`.

**Honestidad (lección `notes/33`):** el grid da **cota superior** del número de soluciones y
solo cubre endpoints en la malla; NO es prueba del continuo en el caso no-genérico. El caso
**genérico** (§2, el que contiene la tercio-central y su vecindad) está **probado en el
continuo**. El no-genérico está **fuertemente evidenciado** (3 mallas exactas) y **reducido**
a finitos sistemas lineales; completarlo a mano es mecánico (bajo riesgo).

---

## 4. Estado y clasificación honesta

| Pieza | Estado |
|---|---|
| Cota `Σr≥1` (medianas) | **[PROVED]** (`notes/36`, transporte) |
| Reducción igualdad ⟹ partición exacta de las 3 aristas + `I_i⊂[0,1]` | **[PROVED]** (§1) |
| Rigidez, régimen genérico (los 3 cruzan `½`) | **[PROVED]** (§2, sistema lineal, único `[1/3,2/3]`) |
| Rigidez, régimen no-genérico | **[PROVED — `notes/45`: 3 soluciones edge-tiling; centroide mata las 2 falsas]** |
| Conteo de dimensión (`notes/39`: "2-dim"→**3-dim**) | **corregido** |

**Entregable (Prioridad 2) — COMPLETO:** *"Bang para las 3 medianas es sharp, y el locus de
igualdad `{Σr=1}` (planks esenciales) es el único punto `I_i=[1/3,2/3]` — primer caso tight
NO-faceta de Bang(3) con rigidez COMPLETA."* Prueba cerrada en `notes/45` (R2-2); `notes/36 §2`
actualizado a `[PROVED]`.
