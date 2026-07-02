# R6-4 — TEOREMA: tightness y rigidez de TODA la familia cíclica (Thm 6.6)

> Date: 2026-07-02. Status: **[PROVED — prueba humana completa en el paper, verificación
> simbólica + racional exacta]**. Resuelve R6-4 con el desenlace CONTRARIO al esperado
> por el jefe: la igualdad `Σr=1` **SÍ se alcanza** para todo `p≠centroide`, con
> cobertura tight explícita y **única**. La evidencia de grilla de `notes/38`
> (min≈1.0003) era ruido de grilla — la lección de `notes/33` otra vez: la grilla no
> contenía los endpoints exactos `k/29`.
> Scripts: `experiments/cyclic_family_tight_rigidity.py` (consolidado, corre limpio).

## 1. Enunciado (Theorem 6.6 del paper)

Sea `p` interior al triángulo medial, `α=1−2p_A, β=1−2p_B, γ=1−2p_C` (= las masas de
arista de `μ_p`; `α+β+γ=1`, positivas), `S=αβ+βγ+γα`. Los planks

```
I₁ = [αγ/S, 1−αβ/S],   I₂ = [βγ/S, 1−αγ/S],   I₃ = [αβ/S, 1−βγ/S]
```

en las direcciones cíclicas concurrentes en `p` **cubren** `Δ` con
`Σrw = (βγ+αβ+αγ)/S = 1`, y son la **única** cobertura con `Σrw=1` por tres planks de
ancho positivo en esas direcciones. En el centroide (`α=β=γ=⅓`): `[⅓,⅔]³` = el teorema
de medianas. Ejemplo `p=(9/20,3/10,1/4)`: `I=([5/29,25/29],[20/29,24/29],[4/29,9/29])`.

**Consecuencia:** el techo del paper sube de "un caso tight con rigidez" (medianas) a
**una familia 2-paramétrica de configuraciones sharp, cada una con unicidad**.

## 2. Los tres ingredientes de la prueba

1. **Identidad afín (el hallazgo estructural):** con `a₁=α(1−α), a₂=γ(1−γ), a₃=β(1−β)`:
   `Λ := a₁u₁+a₂u₂+a₃u₃ ≡ S` (basta verificar en los 3 vértices: `Λ(A)=αγ+β(α+γ)=S`,
   etc.). Además `Σaᵢ = 1−Σα² = 2S` y — el cómputo central —

   ```
   Σaᵢlᵢ = (S²−αβγ)/S = S − αβγ/S   y   Σaᵢhᵢ = S + αβγ/S
   ```

   (expandiendo, ambos numeradores = `Σα²β² + αβγ` y `S² = Σα²β² + 2αβγ`).
   **El margen de cobertura es exactamente `αβγ`** — positivo en todo el dominio,
   cero solo en el borde del medial.

2. **Cobertura:** el conjunto no cubierto `U` se descompone en ≤8 regiones convexas
   abiertas por patrón de signos. (a) `closure(región)∩∂Δ` es finito (las aristas están
   teseladas y en un punto de contacto algún `u_j` vale exactamente `l_j` o `h_j`);
   (b) eso fuerza `H_σ ⊂ Δ̄` (si saliera, un disco de segmentos produce infinitos puntos
   de contacto); (c) rectas dos a dos no paralelas (`τᵢ(1−τⱼ)=1` imposible); si las 3
   rectas concurren ⟹ cono abierto no acotado ⟹ vacío; (d) si no, la región es el
   triángulo de las 3 rectas con vértices en `Δ̄`, y `Λ≡S` da en cada vértice una
   desigualdad `S ≤ Σaᵢcᵢ` o `S ≥ Σaᵢcᵢ`: los **patrones mixtos** fuerzan igualdad ⟹
   concurrencia ⟹ vacío; los **puros** chocan con el margen `±αβγ/S`. `U=∅`. ∎
3. **Unicidad:** igualdad en el transporte (`μ_p`) ⟹ las trazas teselan las 3 aristas ⟹
   Prop. A.1 (apéndice, general-τ) ⟹ solo 3 candidatos: el MMM (= la cobertura tight),
   `([0,λᵢ])` y `([ρᵢ,1])`. Estos dos NO cubren: testigo explícito
   `x* = V⁻¹(λ+δ·1)`, `δ=αβγ/(2S²)`, con coordenadas baricéntricas
   `x* = (αβ(1−α)(1+α−β), βγ(1−β)(α+2β), αγ(α+β)(2−2α−β))/(2S²)` — todas positivas
   en todo el dominio (y `y*` simétrico para RRR). En el centroide `δ=1/6` y ambos
   testigos degeneran al **centroide** — recupera exactamente el testigo de `notes/45`. ∎

## 3. Verificación (exacta, sin grillas para concluir)

- Simbólica (sympy): `Σr−1≡0` en la familia; las 6 identidades de validez M con margen
  positivo factorizado; `Σaᵢlᵢ`, `Σaᵢhᵢ`, positividad de `x*`, `y*`. ✓
- Racional exacta (fractions, clipping de polígonos): área no cubierta del MMM = **0**
  (⟹ cobertura genuina: el conjunto no cubierto es abierto) y de LLL/RRR > 0, en 5
  puntos de la familia incluidos casi-degenerados (`α=β=0.45`, `α=0.48,β=0.01`). ✓
- Las soluciones generales-τ de Prop. A.1 verificadas por búsqueda exacta en grilla en
  `τ=(½,⅔,⅓)`. ✓

## 4. Qué queda abierto tras esto

- Ternas **no concurrentes** (única situación restante en el triángulo, ver 50-R6-5):
  sin medida testigo posible; el problema de 3 planks genuinamente abierto vive ahí.
- `d≥3`: medianas cíclicas de `Δ^d` concurren en el centroide; ¿medida testigo? [OPEN]
