# R4-4 — Suficiencia de la familia de concurrencia: estructura, un teorema nuevo, y el crux

> Date: 2026-07-01. Status: **estructura [PROVED]; "perímetro ⟺ τ=½" [PROVED, nuevo];
> suficiencia general [OPEN]**. Avanza R4-4 sin resolverlo. Scripts:
> `experiments/concurrence_measure_hunt.py`.

Objetivo R4-4: probar que `cond=2` (`1ᵀV⁻¹1=2`) + `p` interior ⟹ existe medida con marginal
uniforme en las 3 direcciones ⟹ `Σrw≥1` para **toda** la familia de concurrencia (subiría el
techo del paper de "medianas" a "familia genérica"). No se logra; se aísla el crux y se prueba
por qué la construcción del perímetro es especial de las medianas.

---

## 1. Estructura de la familia (corrige un malentendido de exploración) [PROVED]

Una dirección **normalizada** `u:Δ→[0,1]` afín **sobre** `[0,1]` tiene valores de vértice
`{0, τ, 1}` (min 0, max 1, medio `τ∈[0,1]`). Escribiendo `u_i` con valores `{0,τ_i,1}`
asignados a vértices, la **concurrencia** `Vp=(1/2)1` en un punto interior `p∈Δ` da, por fila,
`τ_i·p_{b(i)} + p_{c(i)} = 1/2` (donde `b(i),c(i)` son los vértices con valor `τ_i` y `1`).

- **La familia es 2-dimensional**, parametrizada por el punto de concurrencia `p` (interior).
  Fijado `p`, cada `τ_i` queda determinado por la asignación. **Medianas** = el caso
  `p=centroide`, que fuerza `τ_i=1/2` (pues fila-suma `1+τ_i=3/2`).
- **Caveat de auditoría a mí mismo:** un primer test usó `u_0=(0.2,0.5,0.8)`, que **no es
  onto** `[0,1]` (rango `[0.2,0.8]`), luego no es dirección válida. Las direcciones válidas
  tienen valores `{0,τ,1}`. Corregido.

---

## 2. Teorema nuevo: la medida del perímetro sirve SÓLO para `τ=½` [PROVED]

**Proposición.** Sea `u` con valores de vértice `{0,τ,1}` (`τ∈(0,1)`). La medida del perímetro
`μ` (uniforme en las 3 aristas, peso `1/3`) cumple `u_{#}μ=Leb[0,1]` **si y sólo si `τ=1/2`**.

*Prueba.* En cada arista `u` es afín entre dos valores de vértice; el pushforward de
uniforme-en-arista es uniforme en ese sub-intervalo, con densidad `(1/3)/\text{(longitud)}`.
Las tres aristas conectan los pares `{0,τ}`, `{τ,1}`, `{0,1}`, dando cajas
`[0,τ]` (densidad `\tfrac{1}{3τ}`), `[τ,1]` (densidad `\tfrac{1}{3(1-τ)}`), `[0,1]`
(densidad `\tfrac13`). La densidad total es
`\tfrac{1}{3τ}+\tfrac13` en `[0,τ]` y `\tfrac{1}{3(1-τ)}+\tfrac13` en `[τ,1]`.
Uniforme `≡1` ⟺ `\tfrac{1}{3τ}=\tfrac23` y `\tfrac{1}{3(1-τ)}=\tfrac23` ⟺ `τ=1/2`. ∎

**Consecuencia:** la construcción de `notes/36` (perímetro) es **exactamente** el caso
`τ=1/2` = medianas (y las permutaciones de `{0,½,1}`, verificado: `(0,½,1)` también da
uniforme, dev `0.028≈` ruido). Para `p≠centroide` (`τ_i≠½`) el perímetro **falla**
(verificado: triple válido genérico da dev `>0.7`). Esto explica rigurosamente por qué las
medianas son especiales y por qué el teorema con medida explícita no se extendió (R3-2).

---

## 3. Reducción de la suficiencia (Kellerer) [PROVED como reducción]

Para una terna concurrente, existe `μ` con `u_{i#}μ=Leb` ⟺ (Kellerer/Strassen) para toda
`(φ_1,φ_2,φ_3)` continua: `Σ_i φ_i(u_i(x)) ≥ 0` en `Δ` ⟹ `Σ_i ∫_0^1 φ_i ≥ 0`. Es un problema
de **3 marginales** sobre la imagen `Φ(Δ)⊂[0,1]^3`, que es un **triángulo 2-dim** en el plano
`Σa_i u_i=κ` (relación afín, `Σa_i=2κ`). El dual del LP de `notes/37` es esta condición
discretizada; la factibilidad `453/453` (robusta) es **evidencia**, no prueba.

**Lo garantizado (media+varianza), recap de `notes/38` §2.1 [PROVED]:** para `cond=2` con `p`
interior, la media (`E[u_i]=1/2`) se satisface por concurrencia, y la varianza es realizable
(la desigualdad triangular en los `|a_i|` es **automática**). El hueco real es la
**uniformidad plena** (momentos `≥3`) del acoplamiento, más el régimen de signo mixto de `a`.

---

## 4. El crux y el template (honesto)

- **Crux abierto:** construir `μ` explícita para una terna concurrente con `τ_i≠½` (o probar
  la condición de Kellerer). La solución LP es singular, soporte interior+borde (`~34` puntos,
  `notes/38 §2.3`), **no** el perímetro ni una curva simple. Es el **hueco finito abierto de
  Gardner** (`notes/43-P3`) en la rebanada de concurrencia (codim-1).
- **Template (siguiente intento natural):** la construcción de Gardner (Thm 1, 2 direcciones)
  arma `μ` como Lebesgue sobre segmentos del cuadrilátero inscrito. Para 3 direcciones
  concurrentes, el análogo sería una familia de segmentos a través de `p` que uniformice las
  3 direcciones simultáneamente. El obstáculo: con 3 direcciones la imagen es un triángulo
  2-dim y el acoplamiento 3-marginal no se resuelve por segmentos de una sola familia (los
  cevianos desde `p` fallan, dev `>5`, verificado). Requiere una construcción de barrido 2-dim
  o la dualidad de Kellerer analítica.

---

## 5. Valor para el paper (R4-1/2/3) y veredicto

- **Va al paper como resultado nuevo:** la Proposición §2 (perímetro ⟺ `τ=½`) — explica
  limpiamente la unicidad de las medianas dentro de la familia de concurrencia. Fortalece la
  sección de la caracterización sin depender de la suficiencia.
- **NO va como teorema:** "Bang para toda la familia de concurrencia" — sigue `[OPEN]`,
  reducido al 3-marginal de Kellerer para `τ≠½`. Riesgo medio-alto, sin ruta conocida limpia.
- **Recomendación:** mantener el techo del paper en "medianas (tight + rigidez) + caracterización
  necesaria + perímetro⟺½"; seguir R4-4 como línea de investigación (Kellerer/barrido), pero
  el deliverable seguro no depende de ella.
