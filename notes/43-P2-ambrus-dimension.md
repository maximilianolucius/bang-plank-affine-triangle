# P2 — Re-auditoría de la reducción de Ambrus (dimensión y WLOG ortogonal)

> Date: 2026-06-30. Status: **[RESUELTO contra fuente primaria]**.
> Cierra la Prioridad P2 de `auditorias/00` y el punto "RE-AUDITAR" de `auditorias/40 §3`.
> Fuente: `refs/ambrus_appendix.pdf` §3 (re-leída verbatim, `pdftotext`).

---

## 0. Los dos defectos a resolver (de `auditorias/40`)

1. **Inconsistencia interna:** `notes/40` decía "dim del símplex-objetivo = `2d−1`
   (tetraedro en `R⁴` para `d=2`)" Y "todos los símplices, toda dimensión" — incompatibles.
2. **WLOG pairwise-ortogonal:** "en `Rᵈ` hay ≤`d` vectores ortogonales; una cobertura con
   `>d` direcciones (p.ej. 3 planks en el plano) no puede tener normales ortogonales" ⟹ el
   paso WLOG parecía incompatible con el caso real del proyecto.

---

## 1. La dimensión correcta es `2N−1`, `N = número de planks` [RESUELTO]

Transcripción verbatim de la construcción (Ambrus §3): la cobertura es `(Lᵢ)`, y **"for each
`i`, let `x_{2i}` and `x_{2i+1}` be points of `K`"** con `⟨x_{2i}−x_{2i+1}, uᵢ⟩=1`; luego
`x=Σcᵢxᵢ`, `Σcᵢ=1`, `cᵢ≥0`, con **`c=(cᵢ)₁^{2d} ∈ R^{2d}`**, recorriendo un símplex `T`.

- **La construcción toma 2 puntos POR PLANK.** Con `N` planks ⟹ `2N` puntos ⟹ símplex `T` de
  dimensión **`2N−1`** embebido en `R^{2N}`. El parámetro real es `N` = **número de planks**,
  NO la dimensión ambiente `d`.
- La confusión de `notes/40` (`2d−1`, "tetraedro en `R⁴`") nace de que **Ambrus reusa la
  letra `d`** para el número de planks tras su paso WLOG (que identifica #planks = #direcciones
  = dim ambiente). Leído correctamente, `d` en `(Lᵢ)₁^d` es el **conteo de planks**.
- **Corrección concreta:** para `N=2` planks el target es el 3-símplex (tetraedro en `R⁴`);
  para `N=3` planks es el **5-símplex** en `R⁶`; en general `2N−1`, que **crece con `N`** y es
  siempre de **dimensión impar**. Consistente con "todos los símplices (de dim impar)". La
  contradicción interna desaparece: NO es fija por `d`; crece por `N`.

Coincide (afinando) con la conjetura del auditor `2k−1`: es `2N−1` con `N` = #planks
(cada plank aporta su par de puntos; `k`=#direcciones sólo coincide si hay 1 plank por dirección).

---

## 2. El WLOG ortogonal NO es esencial para la reducción [RESUELTO]

**Hallazgo clave:** la **construcción** (`x=Σcᵢxᵢ`, combinación convexa; condición
`|⟨x,uₖ⟩−mₖ|>wₖ`; mapa a `T`) **no usa en ningún punto la ortogonalidad de los `uᵢ`**. Es
válida para direcciones **arbitrarias**. Donde entra una normalización es en dos lugares,
ambos manejables sin ortogonalidad:

- `⟨x_{2i}−x_{2i+1},uᵢ⟩=1` y "`{⟨c,ũₖ⟩:c∈T}` tiene longitud 1" ⟹ requiere `w_K(uₖ)=1` en cada
  dirección. Ambrus lo logra vía **"width of `K` is 1 in directions belonging to `Θ`"** por un
  **mapa afín sobre `K`**, que sí sólo puede fijar el ancho a 1 en `≤d` direcciones
  **simultáneamente** (de ahí el "base ortogonal"). **PERO** lo mismo se logra reescalando cada
  **funcional** `uᵢ ↦ uᵢ/w_K(uᵢ)` de forma **independiente por dirección** (el ancho relativo
  `wᵢ/w_K(uᵢ)` es invariante de escala) — **sin ortogonalidad y para cualquier `N`**.

**Conclusión:** el paso "pairwise-orthogonal ⟹ base de `Rⁿ`" es un **artefacto de la
presentación** de Ambrus (su normalización por mapa afín, que arrastra del párrafo previo
sobre *medidas* de ancho relativo — donde reduce a direcciones coordenadas). **No es esencial
para la reducción**, que vale para coberturas de `N` planks en direcciones arbitrarias. La
objeción de `auditorias/40` ("incompatible con `>d` direcciones") **se disuelve**: la
incompatibilidad afecta sólo a la normalización-por-mapa-afín de Ambrus, no a la validez de la
reducción (que se recupera reescalando funcionales).

> **Estatus honesto de la reducción:** **probada** para cualquier cobertura finita por `N`
> planks (direcciones arbitrarias), produciendo un `(2N−1)`-símplex. El único "módulo" real
> es cosmético (Ambrus normaliza por mapa afín en `≤d` direcciones; el caso general usa
> reescalado por funcional, trivial). NO es un hueco matemático.

---

## 3. La conclusión estratégica se mantiene (y se refuerza) [ROBUSTO]

**El triángulo (2-símplex) NUNCA es un target de la reducción de Ambrus**, porque los targets
tienen dimensión **impar** (`2N−1 ∈ {1,3,5,…}`) y `2` es par. Robusto e independiente de los
detalles de §1–§2.

> "Probar Bang para el triángulo ⟹ conjetura plana" es **FALSO** como uso de Ambrus. El
> programa del triángulo (`notes/30,32,33,36,37,43-P4`) es **estudio directo de un cuerpo
> concreto + desarrollo de método**, no un ataque a la conjetura vía reducción.

**Puente método→conjetura (opcional, riesgo alto):** el mínimo target no-trivial es el
**3-símplex** (`N=2` planks). El transporte (`notes/36`) y la caracterización de concurrencia
(`notes/37`) se formulan en cualquier símplex; extenderlos a símplices de dim impar sería la
única vía transporte→conjetura. Explorar sólo si P1 se atasca.

---

## 4. Higiene: fuente primaria ahora persistente

`auditorias/40 §4` señaló que las citas colgaban de `scratchpad/ambrus.txt` (efímero). **El
PDF ya está en `refs/ambrus_appendix.pdf`**; todas las citas verbatim de `notes/40` y de esta
nota son ahora verificables desde el repo. Corregido también en `notes/40`.

## 5. Acciones aplicadas
- `notes/40 §3`: reemplazar "dim `2d−1`, tetraedro en `R⁴`" por "**dim `2N−1`, `N`=#planks**"
  y marcar el WLOG ortogonal como cosmético (no esencial). Ver parche en `notes/40`.
- Conclusión estratégica (triángulo ≠ target) intacta.
