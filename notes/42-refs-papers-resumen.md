# Resumen de los papers en `./refs/` (fuente primaria)

> Date: 2026-06-30. Status: **[DIGEST de fuente primaria]**.
> Seis PDFs en `refs/`, leídos verbatim (`pdftotext`; Gardner requirió OCR con `tesseract`).
> Convención: **[VERBATIM]** = citado del PDF; **[inferido]** = deducción. Los detalles de
> Ambrus están en `notes/40`; los de Ball en `notes/41` (esta nota los resume y remite).

---

## 0. Mapa de relevancia (qué aporta cada uno al proyecto)

| Paper | Rol | Qué da / qué cierra |
|---|---|---|
| **Bang-Yehudayoff 2026** | competencia viva | el récord `2/(1+√d)`; hay que batirlo |
| **Gardner 1988** | obstrucción de medida única | por qué una sola medida NO prueba Bang(3) |
| **Ball 1991** | el caso simétrico (la barrera) | qué "Euler-Jacobi-ificar"; dónde carga la simetría |
| **Ambrus 2010** | reducción a símplices | símplices (dim `2d−1`) ⟹ general (ver `notes/40`) |
| **GOP 2026** | el MOTOR | los 3 pilares Euler-Jacobi (caso centrado) |
| **Pinasco 2023** | precedente de rigor | `c_n=n^{n/2}`, `n≤14`; el gap de decimales |

---

## 1. Bakaev–Yehudayoff 2026 — la competencia viva `2602.20290`

**Ref.** E. Bakaev, A. Yehudayoff, *A Note on the Affine Plank Conjecture*, arXiv:2602.20290v1
(23 Feb 2026).

- **Teorema 8 [VERBATIM]:** "If the planks `P₁,…,Pₘ ⊂ Rᵈ` cover a convex body `K` then
  `Σᵢ rw_K(Pᵢ) ≥ 2/(1+√d)`." (⚠️ **Errata del preprint:** el enunciado formal imprime
  `2/√(d+1)`, pero abstract y prueba usan `2/(1+√d)`; `2/√(d+1)` daría `1.155>1` en `d=2`,
  imposible como cota inferior de cobertura — la correcta es `2/(1+√d)≈0.828` en el plano.)
  Récord previo: `2/(1+d)` [CM16 Thm 2].
- **Lemma 5 (cuerda) [VERBATIM]:** "If the planks … cover the convex body `K`, then
  `Σᵢ width(Pᵢ)/ℓ_K(uᵢ) ≥ 1`", con `ℓ_K(u)` = longitud de la cuerda más larga en dirección
  `u`. Sigue la prueba de Bang (Lemma 2.3 de Verreault). **Este es el "S₀" del proyecto**
  (`notes/34/35`), y el baseline `c=0`.
- **Lemma 7 [VERBATIM]:** "For every `u∈Sᵈ⁻¹`, `ℓ_K(u)/w_K(u) = ℓ_L(u)/w_L(u) ≥ 2/(1+√d)`",
  vía `L=½(K−K)` en posición de John (`B⊆L⊆√d·B`) reducido a 2D por triángulos rectángulos
  semejantes → **cuadrado perfecto/SOS** `(√(r+1)t − √(r−1))² ≥ 0`. **Sharp para el CUBO**
  (`r=√d`) [VERBATIM Remark].
- **Techo estructural [inferido]:** `rw = (width/ℓ)·(ℓ/w) ≥ Lema5 · min(ℓ/w)`; como `ℓ/w`
  es sharp para el cubo, esta ruta desacoplada **no puede pasar de `2/(1+√d)`**. Batirla exige
  **acoplar** los planks. La holgura vive en el símplex, no en el cubo.
- **Abierto [VERBATIM]:** "This conjecture remains open. In fact, it is open **even in the
  plane** (some sources incorrectly claim … citing [Ban53]; however, that paper proves the
  conjecture only for the special case of **two planks**)." → **Confirma la corrección Hunter
  del proyecto (2026-06-30):** el caso de ≥3 planks está abierto en el plano.

**Uso para el proyecto:** define exactamente `ℓ_K`, `S₀=Σwidth/ℓ` (Lema 5) y la constante a
batir. El programa `N_c` (`notes/34/35`) se apoya en el Lema 5 como baseline probado.

---

## 2. Gardner 1988 — la obstrucción de "una sola medida"  `gardner1988`

**Ref.** R. J. Gardner, *Relative width measures and the plank problem*, Pacific J. Math.
135(2) (1988) 299–312. (PDF escaneado; recuperado por OCR.)

- **Def. relative width measure [VERBATIM]:** medida de probabilidad de Borel `μ` en `K` tal
  que `μ(S∩K) = w(S,θ)` (ancho relativo del slab) para todo slab `S` ortogonal a alguna
  `θ∈Θ`. Si existe, **`K⊂∪Sᵢ ⟹ 1=μ(K)≤Σμ(Sᵢ) = Σ w(Sᵢ) ⟹ Bang`** (union bound; ec. (2)).
- **Positivo [VERBATIM, Thm 1]:** para **≤2 direcciones** siempre existe la medida. Corolario:
  "Bang's conjecture is true for two slabs". **Esta es la cita para el teorema de 2
  direcciones** (`notes/12` corregida).
- **Negativo [VERBATIM, Thm 4]:** para `Θ` analíticamente denso, las únicas medidas posibles
  son Lebesgue 1-D en un segmento, o las canónicas de la elipse (`(1−|x|²)^{-1/2}/2π`) /
  elipsoide (área superficial de Arquímedes). Thm 3: para la bola en `n≥4` no hay medida para
  todas las direcciones.
- **Ejemplo del TRIÁNGULO [VERBATIM, Example 1]:** triángulo `(0,0),(0,1),(1,0)`, `Θ` =
  direcciones **ortogonales a las aristas** (= planks paralelos a los lados): NO existe
  relative width measure (de las direcciones coordenadas sale `c=(⅓,⅓)`, que contradice la
  simetría `t(θ)=t(−θ)` para la hipotenusa). Análogo para el tetraedro (Example 2).
- **Matiz clave [VERBATIM]:** aun sin la medida, "Bang's conjecture is true for 3 slabs
  covering these polyhedra" vía la forma fuerte de Bang. **La no-existencia de la medida NO
  refuta Bang; solo cierra esa vía de prueba.**

**Uso para el proyecto:** es la **fuente primaria** de la "medida única topada <1"
(`notes/08/12/23-D14/37`). Confirma exactamente lo que el proyecto redescubrió: las facetas
del triángulo NO admiten medida única. Coincide con `notes/37`: la familia de concurrencia
(medianas) SÍ admite medida uniforme; las facetas NO. **Citar a Gardner, no como hallazgo
propio.** Su reducción "basta las direcciones coordenadas" (atribuida a Ohmann) complementa
la de Ambrus.

---

## 3. Ball 1991 — el caso simétrico (la barrera a romper)  `math9201218`

**Ref.** K. Ball, *The plank problem for symmetric bodies*, Invent. Math. 104 (1991).
Detalle completo en **`notes/41`** (enriquecida con este read). Resumen:

- **Thm 1/2 [VERBATIM]:** cubrir la bola unidad ⟹ `Σ semi-anchos ≥ 1`; forma dual: funcionales
  unitarios `φᵢ`, reales `mᵢ`, `wᵢ>0`, `Σwᵢ=1` ⟹ ∃`x` en la bola con `|φᵢ(x)−mᵢ|≥wᵢ`.
- **Corolario `1/(n+1)` [VERBATIM]:** `C` simétrico, `n` hiperplanos ⟹ ∃ trasladado de
  `1/(n+1)·C` dentro de `C` que no toca ninguno. Sharp. (= Alexander/Conj. 11 de `notes/40`.)
- **Motor:** Bang's Lemma (Lemma 3, matriz **simétrica** con 1's en diagonal, argmax de una
  forma cuadrática sobre `{±1}ⁿ`, condición de flip único) + **simetrización** de la matriz
  no simétrica `A=(φᵢ(xⱼ))` vía **minimización de norma nuclear** (Lemma 4), dando `Σλ²≤1/n`.
- **Simetría load-bearing:** contraejemplos `[[1,1],[−1,1]]` (Lemma 3 falla sin simetría) y
  `[[1,1],[½,1]]` (no toda `A` se rota a simétrica con diagonal grande). Sin cuerpo simétrico
  no hay norma, ni bola/punto que la alcance, ni forma de forzar diagonal 1.
- **Carácter [inferido]:** híbrido discreto (argmax de signos) + continuo (norma nuclear) +
  Cauchy–Schwarz de operadores. **NO hay puntos críticos suaves / Lagrange / Euler-Jacobi.**
  Cualquier "Euler-Jacobi-ificación" tendría que imponerse sobre el paso combinatorio de
  Bang. → Coincide con el veredicto de M1 (`notes/41 §3`): el motor continuo reproduce el
  **margen** sharp pero no la **pertenencia a la bola** (eso es el lema discreto de Bang).

---

## 4. Ambrus 2010 — reducción a símplices  `ambrus_appendix`

Ver **`notes/40`** (resuelto verbatim). Resumen: Conjecture 10 = `Σ rw ≥ 1`; la reducción
está **probada** (módulo WLOG ortogonal), con objetivo **símplices de dim `2d−1`** (no el
`d`-símplex); el "½" es semi-ancho (idéntico a `≥1`). Bonus: Alexander/Conj. 11 (`1/(n+1)`) y
la cita a Gardner.

---

## 5. GOP 2026 — el MOTOR (Euler-Jacobi, caso centrado)  `2606.02567`

**Ref.** Galicer, Ortega-Moreno, Pinasco, *Strong Polarization and Entropy*, arXiv:2606.02567
(1 Jun 2026).

- **Thm 1 (strong polarization) [VERBATIM]:** `vⱼ` unitarios, `pⱼ>0`, `Σpⱼ=1` ⟹ ∃ unit `u`
  con `Σⱼ pⱼ²/⟨vⱼ,u⟩² ≤ 1`. Constante **1** óptima. `pⱼ=1/n` recupera Ball–Frenkel.
- **Sistema crítico [VERBATIM]:** `yⱼ=⟨vⱼ,x⟩`, `A=G⁻¹`, `z=Ay`; los extremos cumplen
  `yⱼ(Ay)ⱼ = αⱼ` (cuadrático), `hⱼ(y)=yⱼ(Ay)ⱼ−αⱼ`.
- **3 pilares [VERBATIM]:** (1) **realidad** (Lemma 3, `s‖b‖²=−ΣkⱼBⱼ²/(Aⱼ²+Bⱼ²)≤0 ⟹ b=0`);
  (2) **una raíz por cámara** (Lemma 4: `2ⁿ` soluciones, todas reales y simples, `A` PD; = las
  `2ⁿ` cámaras = Bézout `2ⁿ`); (3) **Euler-Jacobi** (deg `hⱼ=2`, `2ⁿ` simples ⟹ para `deg g ≤
  n−1`, `Σ_{h=0} g/det Jh = 0`); el test polynomial es `g = 2Σ_{i<j} kᵢkⱼ⟨vᵢ,vⱼ⟩∏_{ℓ≠i,j}yℓ`
  (grado `n−2`; = el Laplaciano de `P` en el caso no ponderado), que da `g=Q·(s²−Σkⱼ²/yⱼ²)`.
- **Entropía [VERBATIM]:** ∃`u` con `−Σpⱼ log|⟨vⱼ,u⟩|² ≤ H(p)` (entropía de Shannon).
- **Plank CENTRADO [VERBATIM, Cor 6]:** ∃`u∈S_H` con `|⟨vⱼ,u⟩|≥pⱼ` — los planks
  `{|⟨vⱼ,u⟩|<pⱼ}` (simétricos, **sin shift**) no cubren la esfera. **Confirmado: centrado.**

**Uso para el proyecto:** es exactamente el motor que M1 intenta portar al caso **shifted**
(`notes/41 §3`, draft M1 §10.1: identidad `(⋆⋆)` shifted, margen sharp `1/n`). GOP es la
prueba de concepto en el caso centrado/esfera.

---

## 6. Pinasco 2023 — precedente de rigor (y su gap)  `2208.05584`

**Ref.** D. Pinasco, *On the n-th linear polarization constant of Rⁿ*, Math. Nachr. 296
(2023); arXiv:2208.05584.

- **Resultado [VERBATIM]:** para **`n≤14`**, `sup_{‖x‖=1}|⟨x,v₁⟩···⟨x,vₙ⟩| ≥ n^{−n/2}`, i.e.
  `c_n(Rⁿ)=n^{n/2}=√(nⁿ)`, con igualdad sii `{vᵢ}` ortonormal. Extiende Pappas–Révész (`n≤5`).
- **Método [inferido]:** analítico (no búsqueda de contraejemplos). Minimiza `f(a)=a₁···aₙ`
  sobre un símplex `Σ_s`, construye `μ(s)=min f`, prueba `μ(s)≥n^{−n/2}` (Lagrange +
  perturbaciones + semicontinuidad + quasi-concavidad).
- **Conexión plank [VERBATIM]:** la cota de Ball da `c_n(E)≤nⁿ`; productos de funcionales ⟺
  cobertura por planks (Tarski/Bang/Ball).
- **GAP de rigor [VERBATIM confirmado]:** el paso clave Prop. 2.8 se cierra con **una tabla de
  valores aproximados a 3 decimales** (`≈5.065`, `≈12.211`, …), aritmética **no certificada**
  (sin cotas de error). El propio autor nota (Remark 2.9) que en `n=15,16` la desigualdad
  **falla** — margen estrecho justo en el borde. **Confirma la lección del plan de trabajo
  (`03-work-plan §3 V4`):** no cerrar pruebas con decimales aproximados; usar aritmética
  certificada (intervalos/Arb). Es el error de rigor a NO repetir.

---

## 7. Síntesis para el proyecto

1. **Batir B-Y** requiere acoplar planks (el `ℓ/w` desacoplado topa en el cubo). El programa
   `N_c` es el intento correcto; su baseline (Lema 5) está **probado por B-Y**.
2. **La vía de medida única está cerrada por Gardner** (fuente primaria) para facetas del
   triángulo — pero NO refuta Bang. El proyecto (`notes/36/37`) encontró la excepción exacta:
   la familia de concurrencia (medianas) sí admite medida uniforme.
3. **El motor GOP es centrado**; el salto a shifted (CRUX 0) es el aporte de M1, con margen
   sharp `1/n` logrado pero pertenencia a la bola pendiente.
4. **Ball es discreto+continuo, no Euler-Jacobi** — la "Euler-Jacobi-ificación" no es una
   traducción directa de la prueba de Ball, sino una ruta alternativa (el paralelismo es
   `{±1}ⁿ` de Bang ↔ `2ⁿ` cámaras de GOP).
5. **Rigor:** el gap de Pinasco (decimales no certificados) es el patrón a evitar en cualquier
   verificación numérica del proyecto.
