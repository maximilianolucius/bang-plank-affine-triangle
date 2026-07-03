# R9 — Ejecución: D(u) columna vertebral, dualidad (B1), cuerpos generales (B2), sup D (B3 parcial), precisión de Rosa (A)

> Date: 2026-07-03. Ejecuta `auditorias/56` (Ronda 9). Status global:
> **[HECHO A1–A6, B1, B2, B4; B3 PARCIAL]** — compila **24 pp, 0 errores /
> 0 undefined / 0 overfull**. Copia congelada:
> `drafts/entregas/affine-plank-triangle-2026-07-03-pasada5.{pdf,tex}`.
> Script nuevo: `experiments/defect_duality.py` (copiado a `drafts/ancillary/`),
> corre "ALL OK" — 8 bloques de verificación, todo exacto (sympy), cero floats.

## Encuadre estructural (orden del jefe): ejecutado

`D_K(u)` es ahora la columna vertebral. Definición general (cuerpo convexo `K`,
`n` direcciones) en **§2** (`def:defect` = Def 2.1), con la forma de "relleno"
(`u_{i#}μ + ρ_i = D·Leb`, `|ρ_i| = D−1`); Prop 2.2 (alcanzado; `Σrw ≥ 1/D_K`;
`D_K=1 ⟺` testigo; monotonía). **Thm 2.3** = el viejo 1/d reescrito como "la
medida uniforme es `d`-admisible para TODA familia" (B2: el 1/d y el transporte
son el mismo objeto). Intro nueva: terminología formal (direction = coordenada
afín normalizada, NO normal euclídea; witness measure; cyclic triple con
remisión a figura) + subsección "The transport defect as organizing frame" +
jerarquía explícita (principal / marco / ilustrativos / extensiones — Thm 4.1
degradado a ilustrativo explícitamente). Abstract reescrito a **una tesis**
(caracterización D=1 ⟺ concurrencia con familias sharp rígidas, organizado por
el defecto), sin Cor 27/29 como "main result", con la frase final de alcance.

## B1 — Dualidad de D(u): TEOREMA con prueba completa

- **[PROVED] Thm 7.6 (strong duality).** Para todo cuerpo convexo `K` y toda
  familia `u₁..u_n`:
  `D_K(u) = sup{ min_{x∈K} Σψ_i(u_i(x)) : ψ_i ∈ C([0,1]), ψ_i ≥ 0, Σ∫ψ_i = 1 }`.
  Prueba en el texto: dualidad débil (2 líneas, dos lados); Claim 1
  (`sup_ψ Φ(ψ,μ) = D_min(μ)`, vía regularidad interior/exterior + Urysohn);
  Claim 2 (`inf_μ Φ = min_x`, Diracs); minimax de **Sion** (P(K) débil-*
  compacto convexo; Φ bilineal continua). Bibitem Sion 1958 añadido. El sup no
  cambia sobre ψ Borel acotadas (weak duality las tapa).
- **[PROVED] Cor 7.7 (certificates):** cotas inferiores certificadas por ψ
  explícitas (verificación = solo la desigualdad puntual + normalización, sin
  optimización); cotas superiores por medidas. OJO dirección: ψ acota D por
  ABAJO (límites del método); μ acota D por ARRIBA (da cotas de covering).
- **[PROVED] Certificado dual de facetas:** `ψ_i(t) = (1 − 3t/2)_+`, masa 3·⅓=1,
  `Σψ_i(λ_i) ≥ 3 − (3/2)Σλ_i = 3/2` puntual ⟹ `D ≥ 3/2` en tres líneas.
  Conjunto de contacto = EXACTAMENTE el hexágono `{max λ_i ≤ 2/3}` (⊃ lazo
  inscrito); ψ se anula exactamente donde vive la holgura `(3/2)1_{[2/3,1]}`.
  Sanidad (c) del jefe: par primal–dual calzado.
- **[PROVED] Prop 7.8 (wedge certificates).** Dependencia afín `Σc_iu_i ≡ c₀`
  (existe, única salvo escala, todos los `c_i ≠ 0` para no-paralelos);
  `κ₁ = c₀ − Σ_{c<0}c_i > 0`, `κ₂ = Σ_{c>0}c_i − c₀ > 0`, `κ₁+κ₂ = A = Σ|c_i|`;
  cuñas de un nudo `ψ_i = (2|c_i|/(Aθ²))(θ − φ_i)_+`, `θ = 2min(κ)/A ≤ 1`
  (¡siempre factible!), valor **`A/(2κ) = 1/(1 − 2δ_c)`** con
  `δ_c = |c₀ − ½Σc_i|/A` = **distancia ℓ∞ del centro (½,½,½) al plano imagen**.
  Sanidad (a): ψ₁≡1 da D≥1 (está en la prueba de dualidad). Sanidad (b): la
  cota de momentos se recupera EXACTAMENTE cuando el punto ℓ∞-más-cercano `p*`
  cae en el triángulo imagen `T_u` (criterio [PROVED]); en general
  `1/(1−2δ_c) ≤ 1/(1−2δ) ≤ D` (jerarquía en Rem 7.10).
- **[PROVED] Lema 7.9 (no external concurrence)** — no estaba pedido y cierra
  el caso degenerado: las mid-lines de una terna no-paralela dos a dos NO pueden
  concurrir fuera de Δ (conteo de signos: el patrón (j₀,j₁) admite mid-line por
  q ⟺ `(q_{j₀}−½)(q_{j₁}−½) ≥ 0`; los pares ordenados invertidos son flips
  paralelos; 3 pares ⟺ todos los `q_j ≤ ½` ⟺ `q ∈ Δ`). Consecuencia:
  `δ_c = 0 ⟺ δ = 0 ⟺ D = 1` — las cuñas son no-triviales exactamente cuando la
  cota de momentos lo es.
- **[PROVED] Prop 7.11 (equality pattern / holgura complementaria):** par
  óptimo ⟹ supp μ ⊆ conjunto de contacto y `∫ψ_i dρ_i = 0`; y recíproca
  (criterio de optimalidad verificable). **Rem 7.12 (skeleton):** `D_∂` def.;
  `D_∂ = D = 1` en el lugar concurrente (μ_p es esquelética); **`D_∂ = +∞` en
  facetas** (toda medida en ∂Δ da átomo en 0 — el óptimo abandona el borde);
  finito en cíclicas; `D_∂ = D ⟺ ∃óptimo esquelético` (test dual vía contacto).
  Esto responde "cuándo el óptimo vive en el esqueleto y cuándo NO".
- **[A1a liquidado]** Rem 7.17 (sandwich) reescrita: el LP esquelético da SOLO
  cota superior; sandwich `225/224 ≤ D ≤ 112/111` con la cota inferior ahora
  como **certificado dual de cuña** (`c = (75,76,74)`, `c₀ = 113`,
  `δ_c = 1/450 = δ`); cerrar el gap requiere μ no-esquelética < 112/111 o ψ
  más rica que cuñas > 225/224. [OPEN]

## B2 — D_K para cuerpos generales: ejecutado (reencuadre + enunciados)

Def 2.1, Prop 2.2, Thm 2.3 y Thm 7.6 (dualidad) están enunciados y probados
para `K ⊂ ℝ^N` arbitrario y `n` direcciones. La cota de momentos (Prop 7.2) y
el defecto de concurrencia (eq:cdefect) también son generales (la prueba del
baricentro es libre de dimensión). §8 los usa en `Δ^d`.

## B3 — sup D = 3/2: MITAD RESUELTA + teorema bonus

- **[PROVED] Thm 7.3 (centroid bound): `δ(u) ≤ 1/6` para TODA familia finita
  de direcciones en el triángulo, de cualquier tamaño.** Prueba de una línea
  que nadie había mirado: toda dirección tiene valores de vértice {0,s,1} ⟹
  `u(G) = (1+s)/3 ∈ [⅓,⅔]`. El centroide es testigo universal. Igualdad exige
  `s ∈ {0,1}` (direcciones tipo faceta). ⟹ **la cota de momentos NUNCA
  certifica D > 3/2** (sub-pregunta (a) del jefe: SÍ, `δ ≤ 1/6` siempre).
- **[PROVED] Thm 8.2 (facet defect in all dimensions):
  `D_{Δ^d}(facetas) = (d+1)/2` para todo `d ≥ 2`** — la conjetura que el jefe
  marcó como "conjetural" en la orden queda probada:
  - cota inferior: certificado dual `ψ_i = (1 − (d+1)t/2)_+` (una línea:
    `Σψ_i ≥ (d+1) − (d+1)/2·Σλ_i = (d+1)/2`); equivalentemente momentos con
    `δ_d = (d−1)/(2(d+1))` — la cota de momentos es exacta en facetas en toda
    dimensión;
  - cota superior: **ciclo inscrito explícito** por los d+1 puntos
    `P_k = shift^k(0, 1/m, ..., d/m)`, `m = d(d+1)/2`, masa 1/(d+1) por
    segmento: cada coordenada hace 1 subida (densidad ½ en [0, 2/(d+1)]) y d
    bajadas de 1/m (densidad d/2 teselando [0, 2/(d+1)]) ⟹ marginal
    `((d+1)/2)·1_{[0,2/(d+1)]}` EXACTA. Para d=2 es el lazo de Thm 7.4.
  - Verificado exacto en `defect_duality.py` para d = 2..7.
  - Honestidad en el texto: NO mejora el covering bound de facetas (el tiling
    Thm 3.3 ya da Σrw ≥ 1); el valor es estructural (alcance exacto del
    transporte contra facetas; soporte óptimo = lazo 1-dimensional INTERIOR,
    consistente con la obstrucción de esqueleto).
- **[OPEN] sub-pregunta (b): ¿D(u) ≤ 3/2 para toda terna?** Estado consolidado
  en Problem 10.3 reescrito: `sup D ∈ [3/2, 2]`; una terna con D > 3/2
  necesitaría un ψ estrictamente más rico que cuñas de un nudo (por Thm 7.6 la
  dualidad es lo ÚNICO que puede exponerla). Si sup = 3/2: `Σrw ≥ 2/3`
  universal para 3 direcciones cualesquiera — con la nota honesta
  `2/3 < 4√3−6` (estructural, no cuantitativo). No intenté la cota superior
  universal esta ronda (es la parte dura; requiere construcción de medida para
  terna arbitraria).
- **[EVIDENCE] `δ = δ_c` en los 12 triples cíclicos muestreados** (batch exacto
  con LP de vértices) — en el paper solo como "en todos los ejemplos calculados
  coinciden; no afirmamos igualdad general" (Rem 7.10).

## B4 (afilado) — región certificada que supera el valor de B-Y

**[PROVED] Cor 7.15:** con `k = (2√3−3)/6` (`1+k = 1/(4√3−6)`), para todo τ*
concurrente con `m = min_i min(τ_i*, 1−τ_i*)`, la caja
`max|τ_i − τ_i*| < km²/(1+km)` da `D < 1/(4√3−6)` ⟹ `Σrw > 4√3−6`. Unión sobre
la familia concurrente 2-paramétrica = abierto explícito (tubo alrededor de
TODO el lugar concurrente, no solo medianas). Verificación exacta: la caja de
Cor 7.14 (1/60 en medianas) está estrictamente dentro (`58k > 4 ⟺
10092 > 9801`). Honestidad escrita: es la región QUE NUESTRA COTA certifica,
no el sublevel set completo `{D < 1.0776}` (ese sigue [OPEN] — el B4 completo
del jefe requeriría D exacto).

## Parte A — pasada de precisión de Rosa (todos los puntos, sin el split)

- **A1a (bloqueante):** overclaim "computable to certified precision by LP"
  ELIMINADO (grep limpio); ahora sandwich con lados certificados (arriba).
- **A1b:** convención de masas fijada UNA vez en Thm 6.3: `α = w_BC = 1−2p_A`,
  `β = w_CA`, `γ = w_AB` ("cada letra griega nombra la masa de la arista
  OPUESTA al vértice homónimo"); referenciada en Thm 6.6 y en la prueba de
  estabilidad (§7). Consistente con la Fig. 2 (que ya la usaba bien).
- **A2:** abstract a una tesis (~200 palabras + frase de alcance obligatoria de
  R8); Cor 27/29 fuera del abstract, sobrio en la intro con caveat;
  "settles Gardner **only** for three directions on the triangle" en intro y
  Rem 6.12 ("completely — but only — for");
  claims de prioridad: ninguno en abstract; §5 mantiene "we are not aware".
- **A3:** jerarquía explícita en la intro (cuatro niveles con Thm 4.1
  degradado); "direction", "witness measure", "cyclic triple" definidos
  formalmente al inicio con la aclaración anti-normal-euclídea.
- **A4:** Thm 6.6 partido en **Lemma 6.7 (margin identity) + Lemma 6.8
  (coverage) + Lemma 6.9 (interior witnesses)** con la prueba del teorema como
  ensamblaje; el conteo de 9 puntos frontera ahora menciona vértices y
  coincidencias explícitamente; Pocket Lemma sigue sin numerar. **Thm 3.2:**
  lema de sumsets extraído como **Lemma 3.2** (compactos, Σ|C_k| > d ⟹
  1 ∈ ΣC_k) probado una vez; la prueba del teorema solo recorta con η y lo
  invoca. **Apéndice A (O2):** reescrito airtight con las dos cláusulas
  separadas (una traza degenerada "ni cubre ni estorba": interior vacío ⟹ la
  condición de interiores disjuntos es vacua) ⟹ no se pierde ninguna solución
  cerrada. LMR ya tenía subcasos separados de R8; no añadí figura de LMR (es un
  caso imposible; la Fig. 4 del tiling MMM ya ilustra el mecanismo — decisión
  documentada aquí).
- **A5:** §8 retitulado "Higher-dimensional simplices: witness families and
  the facet defect", con introducción propia colgada del marco `D_K`; no
  aparece en el abstract como resultado principal (solo "the facet directions
  of the d-simplex have D=(d+1)/2 exactly" como calibración del método).
- **A6:** **Appendix B "Ancillary files and verification protocol"** nuevo:
  declaración explícita "NOT computer-assisted", protocolo (exacto, sin
  floats, enumeraciones exhaustivas sin pérdida de casos), lista script →
  qué verifica → qué enunciado acompaña. `drafts/ancillary/README.md`
  actualizado en espejo (con tabla). MSC/keywords/Ambrus-URL ya estaban de R8.
  **Bloque de autor: SIGUE PENDIENTE (decisión del usuario).**

## Numeración (para la entrega): cambios inevitables

El split de 6.6 en lemas numerados y la reestructura de §2/§7 desplazan
números; mapa completo viejo→nuevo en
`notes/53-R9-entrega-dona-rosa-pasada5.md`. Claves: Thm 6.3/6.6 y Prop A.1
conservan número; **Thm 6.8 (caracterización) → 6.11**; **Prop 7.2 (props
básicas) → Prop 2.2**; **Prop 7.3 (momentos) → 7.2**; **Thm 7.4 (facetas) →
7.4 (¡conserva!)**; Thm 7.6 (estabilidad) → 7.13; **Cor 7.7 (27/29) → 7.14**
(¡el nuevo 7.7 es otra cosa!); Rem 7.8 → 7.16; Rem 7.9 → 7.17; Prop 8.2 → 8.4.

## Qué NO se hizo (cola)

- **B3(b)** (cota superior universal `D ≤ 3/2`): [OPEN], la parte dura.
  Ruta sugerida si se ordena: LP dual exacto con ψ lineales a trozos sobre
  nudos racionales (cualquier punto factible = cota inferior certificada) para
  buscar ternas con D > 3/2; y/o construcción de lazo adaptado a terna
  arbitraria para la superior.
- **B4 completo** (caracterizar el sublevel set exacto): [OPEN], requiere D(u)
  exacto fuera del lugar concurrente.
- Bloque de autor (humano).
