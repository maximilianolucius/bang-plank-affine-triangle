# Ball 1991 (caso simétrico) — análisis recuperado y consolidado

> Date: 2026-06-30. Status: **[CONSOLIDACIÓN PERSISTENTE]**.
> Resuelve la recomendación #5 de `AUDITORIA_CLAUDE_30Jn.md`: el análisis de la prueba de
> Ball colgaba de `scratchpad/ball_fitz.txt`, archivo **efímero y ya perdido**. Aquí se
> consolida en nota persistente lo que sobrevive, cruzado con **fuente primaria**
> (Ambrus, *Appendix: Plank problems*, §"Ball", leída verbatim 2026-06-30) y con
> `notes/04 §T0.2`, draft `M1-working-notes §9`.
> Etiquetas: **[FUENTE PRIMARIA]** = verbatim de Ambrus; **[FIRME]** = derivado/estándar;
> **[PENDIENTE]** = requiere re-lectura del original Ball 1991 (Invent. Math. 104).

---

## 0. Por qué importa (la tesis del proyecto colgaba de esto)

La tesis original (dossier §2) era "Euler-Jacobi-ificar la prueba de Ball". Esa lectura
vivía en `scratchpad/ball_fitz.txt`, que ya no existe (scratchpad es efímero). Sin la
fuente, la tesis quedaba sin respaldo. Esta nota recupera el contenido desde fuentes
persistentes y de fuente primaria, y **separa lo firme de lo pendiente**.

---

## 1. Lo que prueba Ball (enunciados) [FUENTE PRIMARIA]

Ball 1991 prueba la Conjetura 10 (afín) para `K` **simétrico**, vía espacios de Banach
(`K` = bola unidad de la norma que genera). Verbatim de Ambrus:

> **Theorem 12 (Ball).** If the unit ball of a real Banach space is covered by a
> (countable) collection of planks, then the sum of the **half-widths** of these is at
> least 1.

donde un plank es `{x ∈ X : |φ(x) − m| ≤ w}`, `φ` funcional unitario, `w` = **semi-ancho**.
(Normalización: coincide con `Σ rw ≥ 1` completo; ver `notes/40 §2`.)

Predecesores en la misma línea (verbatim):
- **Theorem 6:** lo mismo sobre la bola de un **Hilbert** (real o complejo).
- **Corollary / Alexander (Conj. 11):** forma dual — existe un trasladado de `1/(n+1) K`
  dentro de `K` evitando `n` hiperplanos (el `1/(n+1)` del draft M1).

---

## 2. La maquinaria: Lema de Bang + simetrización [FUENTE PRIMARIA + FIRME]

### 2.1 Lema de Bang (Lemma 5, forma de Fenchel) [FUENTE PRIMARIA]
> Sean `(uᵢ)₁ⁿ` unitarios en `Rᵈ`, `(wᵢ)` positivos. Para toda sucesión de reales `(mᵢ)`,
> existe un punto del **sistema de Bang** `B = {Σ εᵢ uᵢ wᵢ : εᵢ = ±1}` que **no** está
> cubierto por los planks abiertos `Lᵢ = {|⟨x,uᵢ⟩ − mᵢ| < wᵢ}`.

`B` es una imagen afín del cubo discreto `{−1,1}ⁿ`. **Este es el objeto discreto clave:**
Ball reduce cubrir a un enunciado sobre el cubo de signos `{±1}ⁿ`.

### 2.2 Reformulación matricial (el corazón, y donde entra la simetría) [FUENTE PRIMARIA]
Con `xᵢ ∈ B_X`, `φᵢ(xᵢ)=1`, la matriz `A=(aᵢⱼ)=(φᵢ(xⱼ))` tiene `aᵢᵢ=1`. El candidato
`x = Σ cᵢ xᵢ` da `φₖ(x) = (Ac)ₖ`. Bang's Lemma se reformula (verbatim):

> Si `A=(aᵢⱼ)` es una matriz real **simétrica** con 1's en la diagonal, `(mᵢ)` reales y
> `(wᵢ)` positivos, entonces existe una elección de signos `ε=(εᵢ)` tal que
> `|Σᵢ aₖᵢ εᵢ wᵢ − mₖ| ≥ wₖ` para todo `k`.

- En **Hilbert real** con `φᵢ=⟨uᵢ,·⟩`: `xᵢ=uᵢ`, `aᵢⱼ=⟨uᵢ,uⱼ⟩` (Gram) ⟹ `A` **simétrica**
  automáticamente. Aquí el lema aplica directo.
- En **Banach general** `A` **no** es simétrica; Ball usa (verbatim) "an ingenious method
  to modify and **symmetrize** the matrix `A`" para trasladar al setting simétrico donde
  Bang's Lemma aplica.

### 2.2bis Detalle desde el PDF de Ball (`refs/math9201218`, leído directo 2026-06-30)
Actualiza el **[PENDIENTE]** de §4: ahora respaldado por el original, no solo por Ambrus.
- **Lemma 3 (Bang) [VERBATIM Ball]:** "Let `H=(hᵢⱼ)` be a real, symmetric `n×n` matrix with
  1's on the diagonal, `(µᵢ)` reals and `(θᵢ)` non-negative. Then there is a sequence of signs
  `(εⱼ)` so that for each `i`, `|Σⱼ hᵢⱼ εⱼ θⱼ − µᵢ| ≥ θᵢ`." Prueba: **elegir signos que
  maximicen** `Σ hᵢⱼ εᵢ εⱼ θᵢ θⱼ − 2 Σ εᵢ θᵢ µᵢ`; un flip `εₖ→−εₖ` no puede aumentarlo, y la
  simetría colapsa la diferencia a `4 εₖ θₖ(Σⱼ hₖⱼ εⱼ θⱼ − µₖ) − 4θₖ² ≥ 0`.
- **La simetría de `H` es indispensable [VERBATIM]:** contraejemplo `[[1,1],[−1,1]]`
  (`θ=1`, `µ=0`) — ningún signo hace ambas filas `≥1`.
- **`A` de Banach no se rota a simétrica directo [VERBATIM]:** "it is not the case that for
  every matrix `A` with 1's on the diagonal there is an orthogonal `U` with `AU` both symmetric
  and having large diagonal" (contraejemplo `[[1,1],[½,1]]`). Por eso Ball **modifica** `A`.
- **Lemma 4 (el simetrizador) [VERBATIM]:** "there is a sequence `(θᵢ)` of positive numbers
  and an orthogonal `U` so that `hᵢⱼ = θᵢ(AU)ᵢⱼ` is positive [PSD simétrica] and has 1's on the
  diagonal." Dos pruebas: una de punto fijo/topológica, y una **variacional elemental** que
  **minimiza la norma nuclear** `‖(θᵢaᵢⱼ)‖_{C₁}` s.a. `Πθᵢ=1` (usa `‖B‖_{C₁}=max_U tr(BU)` y
  Cauchy–Schwarz de operadores `‖BC‖_{C₁} ≤ (tr BB*)^½(tr CC*)^½`).
- **Cierre [VERBATIM/inferido]:** aplicar Bang a `H`, back-substituir `λₖ=(1/n)Σⱼ uₖⱼ εⱼ θⱼ`,
  y usar ortogonalidad de `U` + Lemma 5 (`Σ(HU)²ᵢᵢ/hᵢᵢ ≤ Σhᵢᵢ`) para obtener **`Σλ²ₖ ≤ 1/n`**
  (⟹ `Σ|λⱼ|≤1` por Cauchy–Schwarz). El infinito-dim (Thm 7,8) por compacidad weak* + límite ℓ₁.

### 2.3 Dónde carga la simetría (dos puntos acoplados) [FIRME, de notes/04 §T0.2]
1. **Simetría del cuerpo:** `K` simétrico ⟹ `C` es bola de norma, `±xⱼ ∈ C` y
   `‖Σ λⱼ xⱼ‖ ≤ Σ|λⱼ|` — la estructura de signos `{±1}ⁿ` solo tiene sentido si `C` es
   simétrico.
2. **Simetría de la matriz:** esencial para Bang's Lemma (contraejemplo de Ball
   `[[1,1],[−1,1]]` para el caso no-simétrico). Como `A` no es simétrica en Banach, la
   simetrización (norma nuclear / rotación ortogonal) es obligatoria.

**Carácter de la prueba [FIRME]:** NO es geometría algebraica, NO hay sistema polinómico
ni puntos críticos/Lagrange. Es híbrida: **discreto-variacional** (Bang, argmax sobre
`{±1}ⁿ` de una forma cuadrática con perturbación de un signo) + **optimización continua**
(simetrización por norma nuclear) + Cauchy–Schwarz de operadores.

---

## 3. Conexión con el motor M–OM / Euler-Jacobi (la tesis, re-evaluada) [FIRME]

- **El puente que motivó el proyecto:** el argmax de Bang sobre `{±1}ⁿ` de una forma
  cuadrática simétrica es *la sombra discreta* de las `2ⁿ` cámaras de signo del sistema
  crítico continuo M–OM (`notes/04 §T0.2 P2`; draft M1 §9.3). Ese paralelismo es real y es
  lo que hace natural el intento M1.
- **Resultado de M1 (firme, ver draft M1 §10.1):** el motor continuo SÍ reproduce una
  identidad de Euler-Jacobi *shifted* `(⋆⋆)` con margen sharp `1/n` — reproduce el
  **margen** de Bang. Lo que el motor continuo NO da gratis es la **pertenencia a la bola
  unidad** (draft M1 §10.3): eso es precisamente lo que el lema **discreto** de Bang
  resuelve (vía `Σ λⱼ² ≤ 1/n` con `λⱼ` pequeños), y el motor continuo tiene `λⱼ` grandes
  cerca de las paredes. Por eso la "reproducción de Ball vía Euler-Jacobi" queda como:
  **margen sharp reproducido; pertenencia a la bola = lema discreto de Bang (Plan B) o
  toric-EJ (M2).**
- **Implicación para los shifts (CRUX 0):** los shifts `mᵢ` viven **dentro** del lema de
  Bang (los `mₖ` en 2.2); por eso el teorema simétrico afín "ya lleva los shifts" — buena
  señal, confirmada en M1 (§2 del draft: reality sobrevive al shift; §10.1: el shift se
  cancela con el polinomio de test `g = ΔP_m − n·g₂`).

---

## 4. Estado honesto y pendientes

- **[RECUPERADO]** El análisis de Ball ya no cuelga de un archivo efímero: los enunciados
  (Th. 6/12, Conj. 11), la maquinaria (Lema de Bang forma Fenchel, reformulación matricial
  simétrica, simetrización) y los dos puntos donde carga la simetría están aquí,
  respaldados por fuente primaria (Ambrus) y por `notes/04`/draft M1.
- **[RESUELTO 2026-06-30]** El **método exacto de simetrización** (Lemma 4, norma nuclear) ya
  está **verificado contra el original**: el PDF de Ball 1991 está en `refs/math9201218` y se
  leyó directo (ver §2.2bis, con Lemma 3/4/5 verbatim y `Σλ²≤1/n`). Ya no cuelga del perdido
  `ball_fitz.txt`. Único matiz remanente: la numeración de página exacta (Invent. Math. 104,
  535–543) no se cotejó contra el reprint arXiv, irrelevante para el contenido.
- La demostración del **propio Lema de Bang** (Lemma 5) está en Ambrus §2 con
  formulaciones alternativas; disponible si se necesita.

**Acción de higiene asociada:** `notes/04 §T0.2` cambió la referencia muerta
`scratchpad/ball_fitz.txt` por un puntero a esta nota.
