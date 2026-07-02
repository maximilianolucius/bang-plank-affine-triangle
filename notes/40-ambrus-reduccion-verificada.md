# La reducción de Ambrus a símplices — VERIFICADA contra la fuente primaria

> Date: 2026-06-30. Status: **[RESUELTO contra fuente primaria]**.
> Resuelve la recomendación #4/#5 de `AUDITORIA_CLAUDE_30Jn.md`: la discrepancia
> "½ vs 1" y el estatus del "CONFIRMED" de `notes/04 §T0.3`.
> Fuente: G. Ambrus, *Appendix: Plank problems* (2010),
> `https://users.renyi.hu/~ambrus/appendix.pdf`, §3 (leída verbatim vía `pdftotext`,
> 2026-06-30). Todas las citas de abajo son **verbatim** del apéndice.

---

## 0. Qué resolvió el auditor que había que resolver

`notes/04` marcó la reducción de Ambrus (símplices ⇒ cuerpos generales) como
**"YES — confirmed from primary source"** en la tabla G0, pero el propio §T0.3
admitía: (a) inédito, (b) discrepancia de normalización **½ vs 1** sin resolver,
(c) `notes/05 §1` decía todavía "Action: read the appendix". El auditor lo llamó
"cimiento de M2 marcado confirmado sin auditar". Ahora **está auditado**.

---

## 1. La conjetura objetivo es `≥ 1` (verbatim) [RESUELTO]

> **Conjecture 10 (Affine plank problem, Bang, 1951).** If a convex body `K ⊂ Rⁿ` is
> covered by a finite number of planks, then the sum of their relative widths is not
> less than **1**.

donde (verbatim) "the relative width of `L` with respect to `K` is `w(L)/w_u(K)`".
Es exactamente `Σ rw ≥ 1` con **anchos completos**. No hay ambigüedad en el objetivo.

---

## 2. El "½" es la convención de SEMI-ancho — NO es un enunciado más débil [RESUELTO]

La discrepancia ½ vs 1 queda **completamente explicada** y **no es una discrepancia**:
es half-width vs full-width. Verbatim, en la reducción Ambrus escribe el plank como

> `Lᵢ = {x ∈ Rᵈ : |⟨x,uᵢ⟩ − mᵢ| ≤ wᵢ}`

es decir `wᵢ` es el **semi-ancho** (el plank tiene ancho completo `2wᵢ`; la propia nota
de Ambrus lo dice: *"the shifts of the planks of normal vector uᵢ and width `2wᵢ`"*).
Con la normalización "width of K in each direction uᵢ is 1", el objetivo escrito es

> *"The goal is to prove `Σ wᵢ ≥ 1/2`."*

y al final de la construcción:

> *"the relative width of `L̃ᵢ` with respect to `T` is `2wᵢ`; hence the original covering
> is equivalent to a covering of `T` with the collection `(L̃ᵢ)`."*

Por tanto:

`Σ (semi-anchos) = Σ wᵢ ≥ 1/2  ⟺  Σ (anchos relativos completos) = Σ 2wᵢ ≥ 1`.

**Conclusión:** el `1/2` de Ambrus y el `1` de la Conjetura 10 son **idénticos**; la
diferencia es solo semi-ancho (`wᵢ`) vs ancho completo (`2wᵢ`). Coincide con la
convención de Ball (`notes/41`): Theorem 6/12 se enuncian "sum of the **half-widths** is
at least 1" sobre la bola unidad (donde `w_K = 2`, y `Σ 2wᵢ/2 = Σ wᵢ ≥ 1`). Consistente.

---

## 3. La reducción está PROBADA en el apéndice, con dos matices [AUDITADO]

Ambrus **no** conjetura la reducción; la demuestra ("Next we show that it **suffices** to
prove Conjecture 10 for simplices"). La construcción verbatim:

- Cobertura `(Lᵢ)` de `K ⊂ Rᵈ`, ancho de `K` en cada `uᵢ` igual a 1.
- Para cada `i`, elegir `x_{2i}, x_{2i+1} ∈ K` con `⟨x_{2i} − x_{2i+1}, uᵢ⟩ = 1`
  (realizan el ancho unidad).
- Buscar `x = Σ cᵢ xᵢ`, `Σ cᵢ = 1`, `cᵢ ≥ 0` ⟹ `x ∈ K` por convexidad, con
  `|⟨x,uₖ⟩ − mₖ| > wₖ` para todo `k` (el punto **escapa de todos** los planks ⟹ no-cobertura).
- Con `c = (cᵢ)₁^{2N} ∈ R^{2N}` (`N`=nº de planks) y `ũₖ = (⟨xᵢ,uₖ⟩)ᵢ`, la condición es
  `|⟨c,ũₖ⟩ − mₖ| > wₖ`, con `c` recorriendo un **símplex `T` de dimensión `2N−1` en `R^{2N}`**.
  (Ambrus escribe `2d`, reusando `d` para el conteo de planks; el parámetro real es `N`=#planks.)
- Los planks trasladados `L̃ₖ = {|⟨·,ũₖ⟩ − mₖ| ≤ wₖ}` cubren `T` sii los `Lₖ` cubren `K`,
  y `rw_T(L̃ᵢ) = 2wᵢ` (§2). Por tanto **cubrir `K` ⟺ cubrir el símplex `T`**.

### Matiz 1 (dimensión) — CORREGIDO en `notes/43-P2`
> **[CORRECCIÓN 2026-06-30 — `notes/43-P2`, re-auditoría].** La versión previa decía
> "dim `2d−1`, tetraedro en `R⁴` para `d=2`". **Es incorrecto.** La construcción toma **2
> puntos por PLANK**; con `N` planks el símplex tiene dimensión **`2N−1`** (`N`=número de
> planks), NO `2d−1` (dim ambiente). Para `N=2` planks → 3-símplex; `N=3` → 5-símplex; crece
> con `N`, siempre **impar**. El `2d−1` venía de que Ambrus reusa `d` para el conteo de planks
> tras su WLOG. Además, el **WLOG ortogonal NO es esencial** (la construcción es
> orthogonality-free; ver `notes/43-P2 §2`). El texto de abajo queda como registro.

El símplex objetivo es de dimensión **`2N−1`** (`N`=nº de planks; ver `notes/43-P2`), **NO**
el `d`-símplex. Consecuencia honesta:

> **"Probar Bang para el triángulo ⟹ cuerpos planos generales" es FALSO como uso de la
> reducción de Ambrus.** Lo que Ambrus da es: "Bang para **todos** los símplices (toda
> dimensión) ⟹ cuerpos generales". El trabajo sobre el triángulo (`notes/30,32,33,36,37`)
> sigue siendo un caso duro y legítimo por sí mismo, pero **no** es el blanco de la
> reducción para `d=2`.

Esto ajusta la narrativa de M2 en `notes/05` (que hablaba del "simplex" a secas).

### Matiz 2 (WLOG ortogonal) — RESUELTO en `notes/43-P2`: no es esencial
> **[RESUELTO 2026-06-30 — `notes/43-P2 §2`].** Ambrus enuncia la reducción tras suponer las
> normales "pairwise orthogonal ⟹ base de `Rⁿ`". Pero la **construcción** (2 puntos por plank,
> combinación convexa, mapa a `T`) es **orthogonality-free**: la única normalización necesaria
> (`w_K(uᵢ)=1`) se logra reescalando cada **funcional** `uᵢ↦uᵢ/w_K(uᵢ)` por dirección, sin
> ortogonalidad y para cualquier `N`. La ortogonalidad es un artefacto de la presentación de
> Ambrus (su normalización por mapa afín, que sí solo fija ≤`d` anchos a la vez, y que arrastra
> del párrafo previo sobre *medidas* de ancho relativo). La objeción "incompatible con >`d`
> direcciones" se **disuelve**: no es un hueco matemático. Ver `notes/43-P2 §2`.

---

## 4. Bonus de fuente primaria (citas nuevas, útiles para el paper)

- **Alexander [1] / Conjecture 11 (verbatim):** la Conjetura 10 es **equivalente** a:
  "Given a convex body `K` and `n` hyperplanes, there exists a translate of `1/(n+1) K`
  inside `K`, whose interior does not meet any of the hyperplanes." Es el `1/(n+1)` de
  Ball (`notes/41`, corolario) y del draft M1. Cita directa para la forma dual.
- **Gardner [12] (verbatim, la obstrucción de medida única):** para el triángulo con
  vértices `(0,0),(1,0),(0,1)`, "there is **no relative width measure** on `K` for planks
  that are parallel to one of the sides of `K`. Nevertheless, the plank theorem in this
  setting is true, because a suitable translate of the Bang system `B` sits inside `K`."
  **Esta es la cita de fuente primaria del "muro de medida única <1"** que el proyecto
  redescubrió (`notes/08 §"why caps at 1/d"`, `notes/12 §límite`, `notes/23 D14`,
  `notes/37 §2`). El resultado de Gardner: con direcciones "infinitas" (analíticamente
  densas) las únicas medidas de ancho relativo son Lebesgue 1-D en un segmento o las
  canónicas de la elipse/elipsoide. Confirma que la medida única **no** resuelve el caso
  faceta del triángulo — exactamente lo que dice `notes/37` (facetas fuera de la familia
  de concurrencia). Debe citarse a Gardner [12], no presentarse como hallazgo propio.

---

## 5. Veredicto (reemplaza el "CONFIRMED" ciego de notes/04)

- **½ vs 1: RESUELTO** — es half-width vs full-width; enunciados idénticos.
- **La reducción está probada** en el apéndice (no conjeturada); el paso "WLOG ortogonal" **no
  es esencial** (la construcción es orthogonality-free, `notes/43-P2 §2`).
- **Corrección de foco:** el blanco es "**todos** los símplices, dim **`2N−1`** (`N`=nº de
  planks, impar, crece con `N`)", **no** el `d`-símplex. Para `N=2` planks → 3-símplex
  (tetraedro en `R⁴`); para `N=3` → 5-símplex en `R⁶`. El **triángulo (2-símplex, dim par)
  nunca es un target.**
- **Estatus honesto para la tabla G0:** "verificado contra fuente primaria (§verbatim);
  reducción probada (WLOG ortogonal inesencial); objetivo = símplices de dim `2N−1`". Ver
  `notes/04` y `notes/43-P2`.

Fuente: **`refs/ambrus_appendix.pdf`** (PDF archivado en el repo; citas verbatim verificables).
