# R2-2 — Rigidez de las medianas: PRUEBA COMPLETA (cierra el régimen no-genérico)

> Date: 2026-07-01. Status: **[PROVED — completo, sin grid]**. Cierra la Prioridad R2-2.
> Reemplaza el "generic PROVED + resto grid-exacto" de `notes/43-P4` por una prueba completa.
> Verificación exacta: `sympy` (enumeración) + `fractions` (centroide), `scratchpad/r2_2.py`,
> `r2_2b.py`.

---

## Teorema (medianas, cota + rigidez — COMPLETO)

Sean `P_i={m_i∈I_i}` los 3 planks medianos del triángulo con `r_i=|I_i|>0`. Si cubren `Δ`,
entonces `Σr_i≥1`, con **igualdad sii `I_i=[1/3,2/3]` para todo `i`** (tercio-central).

- **Cota:** `notes/36` (transporte, medida del perímetro). [PROVED]
- **Rigidez:** esta nota, en 3 pasos, **sin argumentos de grilla**. [PROVED]

---

## Prueba de la rigidez

### Paso 1 — Igualdad ⟹ partición del perímetro [PROVED]
`Σr=1` fuerza igualdad en `1=μ(Δ)≤Σμ(P_i)≤Σr_i` (`μ`=medida del perímetro, marginal uniforme
en cada mediana, `notes/36`). Luego (i) `I_i⊂[0,1]` y (ii) los `P_i` particionan `μ` a.e., i.e.
**en cada arista las 3 trazas teselan `[0,1]`** (partición exacta). (Detalle: `notes/43-P4 §1`;
las ecuaciones de longitud dan un espacio 3-dim, insuficiente sin el abutting.)

### Paso 2 — El edge-tiling tiene EXACTAMENTE 3 soluciones [PROVED, enumeración exacta]
Enumeración simbólica exhaustiva (`sympy`, `scratchpad/r2_2.py`): para cada uno de los
**27 patrones de cruce** `(c_1,c_2,c_3)∈{L,M,R}³` (`L`: `I_i⊂[0,½]`; `M`: cruza `½`; `R`:
`I_i⊂[½,1]`) y **todos los órdenes** de las trazas por arista, se imponen las ecuaciones de
abutting (las 3 trazas parten `[0,1]`) y se resuelve el sistema lineal exacto con las
restricciones `0≤l_i<h_i≤1` y consistencia de cruce. **Resultado: exactamente 3 soluciones**
```
MMM:  I_i = [1/3, 2/3]   (todas cruzan 1/2)
LLL:  I_i = [0,   1/3]   (todas ⊂ [0,1/2])
RRR:  I_i = [2/3, 1]     (todas ⊂ [1/2,1])
```
(Los patrones mixtos y todos los demás órdenes son **infeasibles**.) Esto **cierra el régimen
no-genérico**: no hay que apelar a grilla — la enumeración es completa y exacta.

### Paso 3 — Sólo MMM cubre el interior; LLL y RRR fallan en el CENTROIDE [PROVED]
El edge-tiling es **necesario** pero no suficiente (garantiza cubrir la frontera, no el
interior). El **centroide** `G=(1/3,1/3)` tiene `m(G)=(½,½,½)` (verificado, `fractions`). Y:
```
½ ∈ [1/3,2/3]  (MMM: G cubierto ✓)      MMM cubre Δ ✓
½ ∉ [0,1/3]    (LLL: G NO cubierto ✗)   LLL NO cubre Δ
½ ∉ [2/3,1]    (RRR: G NO cubierto ✗)   RRR NO cubre Δ
```
LLL y RRR teselan el **perímetro** pero **dejan el centroide sin cubrir** — no son coberturas
de `Δ`. **Único cover con `Σr=1`: MMM = `[1/3,2/3]`.** ∎

> El centroide es el **testigo interior exacto** que separa la tercio-central de los dos
> falsos positivos del perímetro. Limpio y citable.

---

## Consecuencias y correcciones

- **`notes/43-P4`:** la rigidez pasa de "genérico PROVED + resto grid" a **PROVED completo**.
  El caso genérico (sistema lineal `9l=3,9h=6`, `notes/43-P4 §2`) es el patrón MMM; los
  patrones L/R (no-genéricos) están ahora **eliminados exactamente** (Paso 2 + Paso 3), no por
  grilla. Actualizado.
- **`notes/36 §2`:** rigidez `[EVIDENCE/OPEN]` → **[PROVED]**.
- **Degeneración:** el cover de un solo plank `I_1=[0,1]` (`r_2=r_3=0`) queda excluido por la
  hipótesis `r_i>0`; con `r_i>0` la rigidez es la de arriba.

## Enunciado citable (deliverable, para R2-4)
> **Teorema (Bang tight en las 3 medianas del triángulo).** Tres planks paralelos a las
> medianas que cubren el triángulo satisfacen `Σ rw_i ≥ 1`, con igualdad **si y sólo si** cada
> uno es el tercio central de su mediana (`I_i=[1/3,2/3]`). Es el **primer caso tight
> NO-faceta de Bang(3) con rigidez completa**.

Prueba: cota por transporte (medida del perímetro, `notes/36`); rigidez por partición del
perímetro + enumeración exacta de teselaciones de aristas (3 candidatas) + el centroide como
testigo interior (`notes/45`).

---

## Verificación (doble método, scripts ARCHIVADOS en `experiments/`)

El "exactamente 3 edge-tilings" se confirma por **dos métodos independientes**:
1. **`experiments/median_rigidity_enumeration.py`** (`sympy`): enumeración simbólica exhaustiva
   de los 27 patrones de cruce × todos los órdenes; resuelve el sistema lineal exacto por caso.
   Da las 3 soluciones **en el continuo** (prueba completa).
2. **`experiments/median_edgetilings_independent.py`** (`fractions`, método distinto): brute
   sobre endpoints racionales con chequeo **directo** de partición de aristas (sin órdenes ni
   sympy). Da las **mismas 3** en `D=6,12,18`. Corroboración independiente.
- **`experiments/median_rigidity_centroid.py`**: verifica `m(G)=(½,½,½)` y que LLL/RRR no
  cubren `G` ni `Δ`; MMM sí.
- Soporte P4: `experiments/median_generic_linsolve.py` (sistema genérico `9l=3,9h=6`),
  `median_tiling_gridsearch.py` (grid con interior). `bang_Nc_nogo_chord.py` (R2-1: `ℓ≤w`,
  tightness del segmento).

(Higiene: scripts movidos de `scratchpad` (efímero) a `experiments/` — cierra la reincidencia
señalada por `auditorias/44-46`.)
