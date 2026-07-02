# R3-2 — ¿Se extiende el teorema de medianas al símplex regular? Honesto: parcial

> Date: 2026-07-01. Status: **necesidad [PROVED, dim-agnóstica]; construcción 2D-específica
> [negativo verificado]; suficiencia d≥3 [OPEN, LP no concluyente]**.
> Veredicto: la parte **caracterización** generaliza; el **teorema con medida explícita +
> rigidez NO** se extiende mecánicamente. Downgrade honesto de la expectativa "fortalece mucho".
> Scripts: `experiments/simplex_medians_explore.py`, `simplex_medians_LP.py`.

---

## 1. Caracterización NECESARIA — dimension-agnóstica [PROVED]

Sea `Δ^d` el símplex estándar (`d+1` vértices), `u_1,…,u_{d+1}` direcciones (formas afines
normalizadas a `[0,1]`), `V=(V_{ij})` la matriz de valores de vértice (`u_i=Σ_j V_{ij}x_j`),
`V` invertible.

**Proposición.** Si existe una probabilidad `μ` en `Δ^d` con `u_{i#}μ=Leb[0,1]` para todo `i`,
entonces el baricentro `p=E_μ[x]∈Δ^d` cumple

`V p = (1/2)·1`  ⟺  las `d+1` hiperplanos de nivel medio `{u_i=1/2}` **concurren** en `p∈Δ^d`,

lo que exige `1ᵀV⁻¹1 = 2` y `V⁻¹1 ≥ 0`.

*Prueba.* `E_μ[u_i]=1/2` (marginal uniforme) `= Σ_j V_{ij}E_μ[x_j]=(Vp)_i`. Y `p∈Δ^d` ⟹
`1ᵀp=1`, `p≥0`. De `Vp=(1/2)1`: `p=(1/2)V⁻¹1`, luego `1ᵀp=(1/2)1ᵀV⁻¹1=1 ⟹ 1ᵀV⁻¹1=2`, y
`p≥0 ⟹ V⁻¹1≥0`. ∎

Es **exactamente** la condición de `notes/37 §2` (`1ᵀV⁻¹1=2`, concurrencia), ahora para
`Δ^d` con `V` de tamaño `(d+1)×(d+1)`. **Generaliza verbatim; nada es 2-dimensional aquí.**

---

## 2. Las "medianas cíclicas" satisfacen la necesidad en TODA dim [PROVED]

Generalización cíclica de las medianas del triángulo (`m_i(e_i)=1/2, m_i(e_{i+1})=0,
m_i(e_{i-1})=1, m_i(e_j)=1/2` resto). Entonces las **filas de `V` suman `(d+1)/2`**
(`V·1=(d+1)/2·1`), luego

`V·(centroide) = V·(1/(d+1))1 = (1/(d+1))·(d+1)/2·1 = (1/2)1`,

i.e. **los `{m_i=1/2}` concurren en el centroide** en toda dimensión, y `V⁻¹1=2/(d+1)·1>0`,
`1ᵀV⁻¹1=2`. (Verificado exacto d=2,3,4,5, `r32chk`.) **Cumplen la condición necesaria ∀d.**

**Consecuencia condicional:** IF existe una medida de marginal uniforme para las medianas
cíclicas de `Δ^d`, THEN `Σrw≥1` (Bang) vale para ellas (transporte, `notes/36 §1`).

---

## 3. La CONSTRUCCIÓN (medida del perímetro) es 2D-específica [NEGATIVO verificado]

La medida testigo del triángulo (uniforme en el 1-esqueleto = aristas) **NO** da marginales
uniformes para `d≥3`: `max|marginal−1|` = `0.025` (`d=2`, uniforme ✓) → **`3.16`** (`d=3`) →
`5.71` (`d=4`) (`simplex_medians_explore.py`). Tampoco la uniforme en facetas
(`(d−1)`-caras). **El "median as parallel-to-cevian + perímetro" es un accidente 2D**: en
`d≥3` una ceviana es una recta y "slabs paralelos a ella" no definen una única dirección; y la
medida del perímetro pierde la uniformidad.

---

## 4. Suficiencia para d≥3: OPEN, LP no concluyente

LP de factibilidad (¿existe *alguna* medida con marginales uniformes para las medianas
cíclicas?, como `notes/37`): resultados **grid-inestables** — `d=2, K=10 bins` da **falso
negativo** (sabemos que el perímetro funciona), luego la discretización a esa resolución es
**inadecuada** y no permite concluir para `d≥3`. (`simplex_medians_LP.py`; consistente con
`notes/38 §2.2`: el LP es evidencia, no prueba, y aquí ni siquiera evidencia limpia.)

La existencia de la medida para `d≥3` es la **misma pregunta abierta de suficiencia** de
`notes/38`, ahora en dimensión superior (y en el hueco finito abierto de Gardner, `notes/43-P3`).

---

## 5. Veredicto honesto (para el paper, R3-1)

- **SÍ va al paper (dim-agnóstico, PROVED):** la **caracterización necesaria** (concurrencia
  `1ᵀV⁻¹1=2`) vale en todo `Δ^d`; y las medianas cíclicas la cumplen ∀d (concurren en el
  centroide). Es un resultado estructural general, no 2D.
- **NO va como teorema (no probado):** "Bang tight para las medianas del símplex regular en
  toda dim" — la medida explícita **no** se extiende (perímetro 2D-específico), y la
  suficiencia `d≥3` está abierta. **R3-2 NO fortalece el paper "mucho"**; el teorema de
  medianas **con medida + rigidez** sigue siendo el **caso `d=2` (triángulo)**, que es el
  resultado sharp firme.
- Encuadre correcto en el paper: teorema de medianas = `d=2` (completo, `notes/36/45`);
  caracterización de concurrencia = general `Δ^d` (necesidad); suficiencia general = conjetura
  bien fundada (open, reduce a Gardner-finito en dim `d`).

**Recomendación:** no invertir más en R3-2 como extensión-teorema (reduce a un abierto duro).
Usar la caracterización general como sección estructural del paper; el corazón sharp es el
triángulo. Prioridad real: **R3-1 (escribir el paper)**.
