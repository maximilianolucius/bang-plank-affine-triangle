# Órdenes de trabajo — Jefe de research
> Fecha: 2026-06-30. Objetivo primario: **avanzar la conjetura afín de Bang** —
> concretamente **mejorar la mejor cota conocida** (B-Y `2/(1+√d)`; triángulo `4√3−6≈0.928`)
> y/o resolver casos limpios. Estado de fuentes: **desbloqueado** — `refs/` ya tiene
> B-Y 2026, Ball 1991, Ambrus (apéndice), Gardner 1988.
>
> Reglas para todos los trabajos:
> - **Aritmética exacta** (`fractions`) o **optimizador continuo**; NUNCA concluir de grilla
>   gruesa (la grilla miente sobre `min` y sobre "no hay otras" — lección `notes/33`).
> - **Separar `[PROVED]/[EVIDENCE]/[OPEN]`** en cada párrafo. Confirmar ≠ demostrar.
> - Sin lenguaje grandilocuente. Escribir como referee que rechaza al primer hueco.
> - Cada afirmación de fuente primaria debe apuntar al PDF en `refs/`, no a scratchpad.

---

## P1 (FLAGSHIP) — Batir Bakaev–Yehudayoff: `Σrw ≥ c+(1−c)·0.928` para algún `c>0`
**Por qué:** única vía **incremental, publicable e independiente de Ambrus** que toca el
objetivo primario. Mejora estricta del SOTA (`0.928` triángulo / `0.828` general).

**Fundamento ya firme (`notes/31/34/35`):** `S_1≤S_c≤S_0`; `S_0=Σ width_i/ℓ_i ≥1` es el
**Lema 5 de B-Y** (ahora en `refs/2602.20290`); reducción exacta
`S_c≥1 ⟺ S_0−1 ≥ L_c`, con `L_c=Σ rw_i·c(1−ρ_i)/(ρ_i q_c)`, `ρ_i=ℓ_i/w_i`,
`q_c=c+(1−c)ρ`. Probar `S_c≥1` para un `c>0` fijo da `Σrw ≥ c+(1−c)·min ρ > 0.928`.

**Guía de dirección (de-risking, ya verificado por mí):** para coberturas reales
`S_0 ≥ Σrw ≥ 1`, y `S_0=1 ⟺ balanceado (ρ_i=1) Y Σrw=1`. Es decir, **el caso peligroso
(B-Y-tight con dirección no-balanceada) sería casi-contraejemplo de Bang y no ocurre.** Así
que la viabilidad de P1 se reduce a **cuantificar la holgura `S_0−1`** cerca del conjunto de
igualdad balanceado. No es circular.

**Pasos concretos:**
1. Leer B-Y (`refs/2602.20290`): **Lema 5** (strong/chord Bang) y **Lema 7 / Teorema 8**
   (el paso perfect-square/SOS `ℓ/w ≥ 2/(1+√d)`). Transcribir el **conjunto de igualdad** de
   cada uno.
2. **Ruta A (preferida):** rehacer la prueba de B-Y con el normalizador `N_c=(1−c)ℓ+c·w` en
   lugar de `ℓ`. ¿Tolera el paso SOS/perfect-square un `c>0`? Si sí, sale `S_c≥1` directo.
3. **Ruta B:** extraer de la prueba de B-Y una **cota inferior cuantitativa** de `S_0−1` en
   términos de la no-balanza `(1−ρ_i)`; verificar `S_0−1 ≥ L_c` para el mayor `c`.
4. Localizar `c*` numéricamente (exacto/continuo) antes de probar; luego demostrar.

**Entregable:** un teorema `Σrw ≥ c+(1−c)·0.928` con `c>0` explícito (triángulo), y/o el
análogo general con `2/(1+√d)`. O una **obstrucción rigurosa** de por qué `c*=0`.
**Riesgo:** medio. **Hecho:** teorema con `c>0`, o obstrucción demostrada.

---

## P2 — Re-auditar la reducción de Ambrus (arreglar la inconsistencia de dimensión)
**Por qué:** `notes/40` se contradice (dim `2d−1` fija vs "todos los símplices, toda
dimensión") y el WLOG pairwise-ortogonal es **incompatible con `>d` direcciones** (ver
`auditorias/40 §3`). Necesario para la honestidad de alcance del paper.

**Pasos:**
1. Con `refs/ambrus_appendix.pdf` (ya archivado), re-leer §3 verbatim.
2. Fijar la **dimensión correcta** del símplex-objetivo (mi conjetura: `≈2k−1`, `k`=nº de
   direcciones ⇒ símplices de dimensión impar que crecen con la cobertura; "tetraedro en R⁴"
   es probablemente artefacto del caso `k=2`).
3. Auditar el paso "simple approximation technique" (WLOG normales ortogonales): ¿reduce de
   verdad, o solo aplica a `≤d` direcciones? Documentar el alcance real.
**Entregable:** `notes/40 §3` corregido + una línea firme del enunciado exacto de la reducción.
**Riesgo:** bajo. **Hecho:** dimensión y WLOG resueltos contra fuente.

---

## P3 — Gardner: cerrar la suficiencia de `cond=2` y arreglar la cita de `notes/12`
**Por qué:** (a) `notes/12` cita "existencia del acoplamiento a Gardner" pero apunta al
resultado **negativo** (`notes/40 §4`); falta el **positivo** (2 direcciones). (b) La
suficiencia de `cond=2` (`notes/37/38`, `[OPEN]`) podría cerrarse con la teoría de Gardner.

**Pasos (con `refs/gardner1988_relative-width-plank.pdf`):**
1. Localizar el **teorema positivo** de existencia de medida de ancho relativo para `≤2`
   direcciones y citarlo correctamente en `notes/12`.
2. Localizar el criterio general de existencia para **finitas direcciones**. **Hipótesis a
   testear:** la condición de concurrencia `1ᵀV⁻¹1=2` (`notes/37`) = criterio de Gardner
   para 3 direcciones. Si Gardner lo contiene ⇒ **cierra la suficiencia** ⇒ "Bang(3) para la
   familia de concurrencia" pasa de `[OPEN]` a teorema.
**Entregable:** cita corregida en `notes/12`; veredicto (Gardner cierra suficiencia / es
nuevo) en `notes/38`. **Riesgo:** medio. **Hecho:** suficiencia decidida o reducida a un
lema nombrado de Gardner.

---

## P4 — Cerrar la rigidez de las medianas (teorema completo, cota+igualdad)
**Por qué:** bajo riesgo, citable; da el "primer caso tight no-faceta de Bang(3) con
rigidez". La cota ya está PROBADA (`notes/36`).

**Pasos (arreglando el defecto de `auditorias/39 §A.1`):**
1. **Completar la reducción:** el CSP de `notes/39 §1.2` omite la **cobertura del interior**
   (condición 2-D) — añadirla. Corregir el conteo (el espacio de longitudes es **3-dim**, no
   2-dim).
2. Resolver el CSP finito (partición de frontera + abutting + interior) por **análisis de
   casos exacto** (racional); probar `Σr=1 ⟹ I_i=[⅓,⅔]` único.
**Entregable:** teorema de medianas completo en `notes/36`. **Riesgo:** bajo. **Hecho:**
unicidad de la teselación tercio-central demostrada (no por grilla).

---

## P5 (cheap, cierre) — Ball 1991: cerrar el `[PENDIENTE]` de `notes/41`
Con `refs/math9201218_ball_plank-symmetric.pdf`: re-leer el **Lemma 4** (simetrización por
norma nuclear + rotación ortogonal) y verificar el resumen de `notes/41 §2.2`/`04 §T0.2`
contra el original (venían del perdido `ball_fitz.txt`). **Entregable:** `[PENDIENTE]`→
`[FIRME]` o corrección. **Riesgo:** bajo. Prioridad baja (la línea Euler-Jacobi está
deprioritizada), pero es barato y elimina la última dependencia de fuente perdida.

---

## P6 (continuo) — Esqueleto del paper del núcleo probado
Ensamblar lo firme, con **alcance honesto**: "primer ataque por transporte/medida al plank
afín; nuevos casos tight para el triángulo (un cuerpo concreto) — **no** la conjetura vía
Ambrus". Contenido: `1/d` (`08`), 2-direcciones (`12`, cita Gardner), faceta-paralelo,
`3 facetas+1` (`30 §1`), **medianas** (`36`+rigidez de P4), **caracterización necesaria** de
concurrencia (`37`). Citas de fuente primaria ya disponibles (B-Y, Ball, Ambrus, Gardner).

---

## P7 (moonshot, background) — Certificado off-surface (la conjetura Bang(3))
Solo si hay capacidad sobrante. Nugget concreto: **estabilidad transversal en el collar
`R=1`** (`notes/30 §8.4`); lead: el certificado de **6 celdas mixtas** (`notes/33 §6`) hacia
el locus de igualdad de Hunter `T=1`. Recordatorio anti-fabricación: solo cuenta una
identidad SOS/Farkas exacta o intervalos con `Lipschitz·celda < margen` en TODO el collar.

---

## Prioridad y secuencia
- **Foco #1: P1** (batir B-Y). Es la apuesta de mayor valor y ya está desbloqueada.
- **En paralelo, baratos y de honestidad:** P2 (Ambrus), P3 (Gardner + cita), P4 (rigidez).
- **Cierre:** P5, P6. **Fondo:** P7.
- No perseguir más el transporte fuera de P3/P4 (está capado a codim-1, `auditorias/39/40`).

Reportar cada avance con etiquetas estrictas y, cuando corresponda, la auditoría en
`auditorias/<id-de-la-nota>.md`.

---

## Estado (2026-07-01) — Ronda 1 ejecutada, ver auditoría
- **P1** batir B-Y: ABIERTO, bien reducido a "Bang-fuerte con `N_c`" (`notes/43-P1`).
- **P2** Ambrus: RESUELTO (dim `2N−1`; WLOG cosmético) — falta terminar el parche a `notes/40`.
- **P3** Gardner: RESUELTO (no cierra suficiencia; cita `notes/12` arreglada).
- **P4** rigidez medianas: PARCIAL (genérico PROVED; no-genérico pendiente, mecánico).

**Auditoría de la ronda + ÓRDENES RONDA 2 (R2-1..R2-5): `auditorias/43-ejecucion-P1-P4.md`.**
Prioridad: R2-1 (flagship, descargar Verreault primero) · R2-3 (higiene ya) · R2-2/R2-4.

## Estado (2026-07-01, tarde) — Ronda 2 cerrada
- **R2-1** batir B-Y vía `N_c`: **NO-GO PROBADO** (`notes/44`, verificado) — el método de Bang
  topa en la cuerda `ℓ`; batir B-Y requiere un certificado de acoplamiento (moonshot).
- **R2-2** rigidez medianas: **PROVED completo** (`notes/45`; centroide como testigo interior).
- **R2-4** esqueleto paper: hecho (`notes/46`).
- **Estratégico:** el vector incremental para batir B-Y está muerto → objetivo primario realista
  = **publicar el paper** (R3-1) + extender a `d`-símplex (R3-2).

**Auditoría + ÓRDENES RONDA 3 (R3-1..R3-5): `auditorias/44-46-ronda2-cierre.md`.**
Prioridad: R3-3 (higiene: archivar scripts, cerrar parche `36`) · R3-1 (escribir paper) · R3-2.

## Estado (2026-07-01, noche) — Ronda 3 cerrada
- **R3-3** higiene: HECHO (scripts archivados; enumeración simbólica exhaustiva corrida → 3
  edge-tilings; verificación independiente; `notes/36` cerrada).
- **R3-1** paper: `drafts/affine-plank-triangle.tex` (compila). **1 error de prueba**
  (faceta-paralelo) + polish de biblio → ver auditoría.
- **R3-2** (`notes/47`): downgrade honesto — solo la caracterización de concurrencia generaliza
  (dim-agnóstica, PROVED); el teorema con medida+rigidez sigue siendo d=2.

**Auditoría + ÓRDENES RONDA 4 (R4-1..R4-5): `auditorias/47-ronda3-paper.md`.**
Prioridad: R4-1/2/3 (cerrar el paper) · **R4-4 (suficiencia de concurrencia, mejor apuesta de
investigación)** · R4-5 (acoplamiento, moonshot).

## Estado (2026-07-01, cierre Ronda 4) — PAPER REFEREE-CLEAN
- **R4-1** fix faceta-paralelo: CORRECTO (verificado paso a paso). Error bloqueante eliminado.
- **R4-2/3** hardening + biblio + referee pass: HECHO (compila 5pp; rigidez = lema
  computer-assisted, enumeración corrida = 3 tilings; biblio corregida).
- **R4-4** (`notes/48`): teorema nuevo "perímetro ⟺ τ=½" [PROVED, verificado]; suficiencia
  general sigue OPEN (3-marginal de Kellerer, sin ruta).
- **DELIVERABLE ENTREGADO:** `drafts/affine-plank-triangle.tex`, honesto, todo probado.

**Auditoría + ÓRDENES RONDA 5: `auditorias/48-ronda4.md`.**
- R5-1 finalizar paper (cierre) · R5-2 un triple concurrente no-mediana (construir o refutar —
  informativo en ambos casos, mejor apuesta) · R5-3 acoplamiento (moonshot).
- **Mensaje honesto:** objetivo "resultado sólido y honesto" CUMPLIDO; batir B-Y / probar la
  conjetura = frontera 2026 sin ruta conocida (investigación de alto riesgo, no ejecución).

## Estado (2026-07-01) — Auditoría externa (doña Rosa): dictamen
- **Hallazgo central (verificado contra disco):** doña Rosa auditó `drafts/paper.pdf` — el
  manuscrito VIEJO de la era tórica (27-jun), ya refutado y superseded. Sus citas (Thm 2.3
  Euler–Jacobi, Prop 3.3, Conj 4.2/4.3, "Status of results", "companion notes") existen SOLO
  en el viejo; el vigente (`affine-plank-triangle.pdf`) tiene 0 ocurrencias de todo eso.
- Su crítica es CORRECTA sobre el documento que leyó — coincide punto por punto con nuestras
  refutaciones internas (`notes/15/22/23`) y su recomendación ("caso trabajado") es lo que ya
  hicimos (medianas + rigidez). Al paper vigente solo aplica: bloque de autor + ancillary files.
- **Fallo de proceso nuestro:** drafts obsoletos sin archivar ⟹ auditor externo leyó el
  artefacto muerto.

**Dictamen + ÓRDENES RONDA 5 revisada: `auditorias/49-dictamen-dona-rosa-paper.md`.**
Prioridad: **R5-0 archivar obsoletos (YA)** · R5-1 carryovers · R5-2 re-auditoría del PDF
correcto · R5-3 triple no-mediana · R5-4/5 fondo.

## Estado (2026-07-02) — Ronda 5 cerrada: TEOREMA NUEVO + re-auditoría externa
- **R5-3 (`notes/49-R5-3`): TEOREMA DEL PERÍMETRO PONDERADO — [PROVED], verificado** (a mano
  las 6 identidades + simbólico + MC + terna exacta `τ=(5/9,4/5,1/6)`). Bang `Σrw≥1` para
  **toda la familia cíclica 2-paramétrica** de ternas concurrentes (medianas = caso
  `p=centroide`). Ya incorporado al paper (Thm 6.3, ahora 6 pp). El mejor resultado desde las
  medianas; da caracterización **iff** para el patrón cíclico (corolario a añadir, R6-1f).
- **R5-0/1/4:** ejecutados y verificados (obsolete/ + BUILD.md; ancillary/; rescate M1 con el
  test polynomial correcto). Pendiente solo el bloque de autor.
- **R5-2 (doña Rosa, 2ª pasada):** esta vez auditó el paper CORRECTO, pero la versión 5 pp del
  1-jul — **no vio el Thm 6.3**. Veredicto "major revision"; sus 6 objeciones son VÁLIDAS
  (cotejadas contra el `.tex`): sharpness de Thm 2.1 mal formulada (obligatoria), Lemma 5.2
  necesita apéndice o certificación formal, claim de prioridad sin soporte, Thm 7.1 →
  Proposición, Thm 3.1 sin hipótesis de no-paralelismo, menores (`d≥2`, WLOG `I⊂[0,1]`).
  Ninguna toca la validez de un resultado; todas salvo Lemma 5.2 son redacción (~1 día).

**Auditoría + ÓRDENES RONDA 6: `auditorias/50-ronda5-cierre.md`.**
Prioridad: R6-1 fixes de referee + R6-2 Lemma 5.2 (apéndice a mano o certificación) ·
R6-3 tercera pasada de doña Rosa (6 pp, foco Thm 6.3) · R6-4 tightness `p≠centroide`
(¿igualdad solo en medianas? rigidez de familia) · R6-5 patrones mixtos · R6-6 moonshot.

## Ronda 7 pre-asignada (2026-07-02) — valor añadido al paper
**Órdenes: `auditorias/51-ordenes-ronda7.md`.** R7-1 esqueleto ponderado en `d≥3`
(**empezar YA**, independiente de R6; binario) · R7-2 defecto de transporte `D(u)`
(definición + `Σrw≥1/D` + cota cuantitativa de primeros momentos, `D(facetas)≥3/2`) ·
R7-3 titular "Gardner 3 direcciones en el triángulo" (condicional a R6-5) · R7-4
estabilidad cuantitativa de la rigidez · R7-5 figuras TikZ + mapa de estatus.
Advertencia vigente: R7-2 se presenta como caracterización del método, NO como mejora de
cota (cerca de facetas `D≈3/2 ⟹ 1/D≈2/3 < 0.928`).

## Estado (2026-07-02, noche) — RONDA 6 CERRADA: dos teoremas nuevos, todo confirmado
- **R6-4 → Thm 6.6 [PROVED, verificado]:** la igualdad `Σr=1` SÍ se alcanza en TODA la
  familia cíclica — cobertura tight explícita (`I` con endpoints `αγ/S` etc., margen
  exacto `αβγ`) y **única**. Desenlace contrario a mi apuesta: la grilla de `notes/38`
  mintió otra vez (endpoints `k/29` fuera de grilla). Lección endurecida: la grilla no
  orienta; lo exacto decide.
- **R6-5 → Thm 6.8 [PROVED, verificado]:** caracterización completa para 3 direcciones no
  paralelas dos a dos: medida testigo ⟺ mid-lines concurren (tricotomía por arista llena
  módulo flips; 216/216 exacto). Cierra Gardner N=3 en el triángulo; Bang-triángulo
  reducido EXACTAMENTE a ternas no concurrentes.
- **R6-1/R6-2:** los 6 fixes de doña Rosa aplicados y verificados; Lemma 5.2 ahora es el
  caso `τ=½` de la **Prop. A.1 probada a mano** (Apéndice A, revisado línea a línea:
  7 órbitas, todo correcto). 11 pp, compila limpio. Cor 6.4: interioridad automática.
- **Pendiente:** R6-3 (doña Rosa) NO ejecutada aún — ahora hay 4 piezas sin auditoría
  externa (Thm 6.3/6.6/6.8, Apéndice A). Pasa a R7-0.

**Auditoría + ÓRDENES RONDA 7 REVISADAS: `auditorias/52-ronda6-cierre.md`.**
Prioridad: **R7-0** re-entrega a doña Rosa (con mapa objeción→resolución) · **R7-1**
esqueleto `d≥3` (ya) · **R7-2 reenfocado**: defecto de transporte `D(u)` con foco en el
módulo de continuidad cerca de la superficie de concurrencia (primeras cotas `>0.928` en
territorio no concurrente = el objetivo real) · R7-4 estabilidad de TODA la familia ·
R7-5 figuras · R7-3 decisión editorial de título.

## Estado (2026-07-02, noche) — RONDA 7 CERRADA: primera cota en territorio abierto + 3ª pasada de Rosa
- **R7-2 → §7 defecto de transporte [PROVED, verificado]:** `D(u)` bien definido;
  `D(facetas)=3/2` exacto (testigo = triángulo inscrito `(0,⅓,⅔)…`, verificado a mano);
  estabilidad lineal cerca de concurrencia; **Cor 7.7: `Σrw≥27/29>4√3−6` para ternas
  cíclicas con `max|τ_i−½|≤1/60`** — PRIMERA cota que bate B-Y dentro de territorio no
  concurrente (entorno full-dim; caveat honesto en Rem 7.8: uniforme-vs-local, coberturas
  ⊥ a las 3 direcciones). `40401>40368` ✓.
- **R7-1 → §8 familia testigo en Δ³ [PROVED, verificado]:** Thm 8.1 (familia σ, pesos
  cerrados `a(σ),b(σ)` rederivados a mano) — primer transporte fuera del plano;
  Prop 8.2 (`d≥4` sin testigo en 1-esqueleto, verificado d=4..7). Fracaso `D=1/(1−2δ)`
  general reportado como Problem 10.3 (honesto).
- **Discrepancia chat/paper:** el chat citó el testigo de facetas con vértices del triángulo
  medial (dan átomo, inválido); el paper usa el inscrito (correcto). Sin acción en `.tex`.
- **R7-0:** copia congelada 11 pp entregada a Rosa; **R7-3:** título se mantiene.
- **3ª pasada de doña Rosa (sobre 11 pp, SIN §7–§8):** "major revision bordering on reject".
  Su tesis de fondo es CORRECTA y ya la dijo 3 veces: **los claims exceden lo probado.**
  Dos overclaims vivos y bloqueantes: (1) "no single-measure argument can improve 1/d"
  (l.48/153 — contradicho por §6–§7); (2) "(equivalently Conjecture 1.1 for the triangle)"
  (l.929 — falsa equivalencia 3-planks ⟺ conjetura). Resto válido, mayormente precisión y
  presentación (no toca validez de resultados).

**Auditoría + ÓRDENES RONDA 8: `auditorias/53-ronda7-y-dona-rosa-pasada3.md`.**
Ronda 8 = **pasada de precisión** (sin matemática nueva obligatoria): R8-1 corregir los 2
overclaims (bloqueante) · R8-2 acotar alcance de caracterizaciones + blindar §7 antes de que
Rosa lo vea · R8-3 rigor (Thm 6.6 Step 2, Prop 7.1 split, Gardner exacto, Apéndice A) ·
R8-4 editorial · R8-5 figuras (ahora prioritario) · R8-7 4ª pasada de Rosa DESPUÉS · R8-6/8
fondo.

## Estado (2026-07-02, cierre Ronda 8) — PASADA DE PRECISIÓN CUMPLIDA (17 pp)
- **R8-1 overclaims eliminados y verificados:** "single-measure" → sharpness de la uniforme
  + Rem 2.2 con contenido real (mejor constante por 1 medida ∈ `[½,⅔]`); "equivalently
  Conjecture" borrado (Problem 1: 3-planks es sub-problema).
- **HALLAZGO R8-3:** la queja #7 de Rosa destapó un **hueco de prueba real** en Thm 3.2
  (los `C_k` son abiertos, no compactos); RESUELTO con recorte a compactos, holgura
  `(d+3−R)/(d+2)>1` verificada. (Fallo mío de auditoría en R3: lo di por correcto.)
- **Numeración preservada** (`.aux`: 6.6/6.8 intactos vía Pocket Lemma sin numerar); 4
  figuras TikZ (Fig. 3 verificada, vértices correctos `(0,⅓,⅔)…`); compila 17 pp limpio.
- **Nota permanente:** el investigador volvió a escribir MAL en el chat el testigo de
  facetas (triángulo medial `(0,½,½)…`, da átomo); el paper siempre tuvo el inscrito
  correcto. Vigilar que no "corrija" la figura hacia el error.
- **Pendiente único:** bloque de autor (identidad real). **R8-7 (entrega a Rosa pasada 4):
  me toca.**

**Auditoría Ronda 8: `auditorias/54-ronda8-cierre.md`.** Sin órdenes de investigación nuevas:
la siguiente ronda depende del dictamen de Rosa (pasada 4). No agregar teoremas hasta que la
auditoría externa valide §7–§8.

## Estado (2026-07-03) — 4ª pasada de Rosa: "Reject, resubmit after restructuring"
- Crítica de FONDO (correcta): el paper está sobredimensionado — "tres papers en un PDF".
  Insiste por 3ª pasada en "promete más de lo que prueba". Ya no son frases: es arquitectura.
- **Calibración:** ningún resultado refutado; toda la matemática verificada (rondas 5–8). Las
  pruebas de 6.6/App A que llama "frágiles" son CORRECTAS (auditadas línea a línea); su
  objeción es de exposición. "Reject" traducido = reestructurar, no re-derivar.
- **Dos puntos técnicos verificados:** (a) overclaim real en §7 l.916 ("D(u) computable by LP
  over skeleton" — el LP da solo cota superior; corregir a sandwich); (b) footgun de notación
  α/β/γ como "edge masses" sin fijar α↦BC/β↦CA/γ↦AB.
- **DECISIÓN ESTRATÉGICA RECOMENDADA: partir en Paper 1 (triángulo, publicable ya) + Paper 2
  (defecto de transporte, con dualidad).** Es un cambio de alcance → pendiente OK del usuario.

**Dictamen sobre la pasada 4 de Rosa: `auditorias/55-dona-rosa-pasada4-y-decision-split.md`.**

## Estado (2026-07-03) — DECISIÓN: un solo paper + expansión del defecto de transporte
- **El usuario decidió NO partir el paper.** En su lugar: aplicar TODOS los puntos aceptados de
  Rosa (salvo el split) + EXPANDIR la dirección `D(u)` con las tareas #1 (dualidad), #3
  (cuerpos generales), #2 (`sup D=3/2`).
- **Encuadre obligatorio:** `D(u)` pasa de sección tardía a **columna vertebral** del paper
  (medianas/cíclicos/facetas/caracterización = casos especiales de `D`). Así se responde la
  crítica de "tres papers en un PDF" **por coherencia, sin partir**. La secuencia importa:
  primero el marco (dualidad + cuerpos generales), luego los resultados nuevos.

**ÓRDENES RONDA 9: `auditorias/56-ordenes-ronda9.md`.**

## Estado (2026-07-03) — RONDA 9 CERRADA: la dualidad existe y está probada (24 pp)
- **B1 [PROVED, verificado línea a línea]:** dualidad fuerte `D_K(u)=sup_ψ min_x Σψᵢ(uᵢ(x))`
  (K, n arbitrarios; Sion + Urysohn); certificado dual de facetas en 3 líneas
  (`ψ=(1−3t/2)₊`); cuñas `D≥1/(1−2δ_c)` con criterio exacto `δ_c=δ ⟺ p*∈T_u`;
  **lema de no-concurrencia exterior** (mid-lines no concurren fuera de Δ̄ — conteo por
  pares con `Σq=1`, la joya de la ronda); holgura complementaria ⟹ overclaim A1a liquidado
  por teorema.
- **B3(a) [PROVED]:** `δ(u)≤1/6` para TODA familia finita (centroide testigo universal, 1
  línea) ⟹ momentos capados en 3/2. **Y el conjetural probado:** `D_{Δ^d}(facetas)=(d+1)/2`
  ∀d≥2 (matched pair: dual + ciclo `P_k=s^k(0,…,d)/m`; verificado a mano d=3, script d=2..7).
- **B3(b) [OPEN]:** `sup D∈[3/2,2]` — consolidado como Problem; pasa a R10-1.
- **B2 + B4 + Parte A completas y verificadas:** `D_K` marco general desde §2; tubo
  certificado alrededor de TODO el locus concurrente (`km²/(1+km)`, aritmética verificada:
  `10092>9801`); abstract a UNA tesis (Cor 27/29 fuera; frase final de alcance); convención
  de masas fijada; sumset lemma aislado; Appendix B protocolo. 24 pp limpio; pasada5
  congelada = vivo (diff 0); 3 scripts ALL OK.
- **DECISIÓN DEL JEFE: entregar pasada 5 YA** (no esperar B3(b) — el lazo externo es el más
  lento; B3(b) es aditivo, no estructural). Bloque de autor sigue pendiente (usuario).

**Auditoría + ÓRDENES RONDA 10: `auditorias/57-ronda9-cierre.md`.**
R10-1 `sup D`: cacería exacta de `D>3/2` (LP dual multi-nudo) + intento de `D≤3/2` universal
(lazo generalizado) — cualquiera de los dos desenlaces es teorema · R10-2 ¿`δ_c=δ` siempre?
(criterio `p*∈T_u`) · R10-3 abstract ≤200 palabras · R10-4 estabilidad (fondo) · R10-5
moonshot.

## Ronda 10 — PAQUETE EJECUTABLE PREPARADO (2026-07-03)
**Órdenes detalladas: `auditorias/58-ordenes-ronda10.md`.** Corre EN PARALELO a la lectura de
Rosa (pasada 5). Novedades del paquete respecto del resumen:
- **Regla de proceso bloqueante: congelación de numeración** del `.tex` mientras Rosa lee —
  material nuevo solo en `notes/54-*` o en números nuevos al final.
- **R10-1 Ruta B (nueva, hacer PRIMERO):** mezcla de testigos de Gardner por pares —
  `μ=⅓(ν₁₂+ν₁₃+ν₂₃)` da `dens_i ≤ ⅔+M_i/3`; si toda tercera-marginal admite `M≤5/2` ⟹
  **`D≤3/2` universal**. Test crítico y barato: `M*(facetas)` exacto (allí `D=3/2` fuerza
  `M≥5/2` — la ruta vive sii se alcanza). Calibración perfecta.
- **R10-1 Ruta A:** LP dual multi-nudo (cotas inferiores CERTIFICADAS — el lado dual no
  tiene "grilla que miente"); terrenos: (i) clase (b) dos-aristas-compartidas (nunca
  concurren, nunca cazada), (ii) cerrar el sandwich `τ=(13/25,½,½)`, (iii) facetas
  inclinadas, (iv) límite casi-paralelo (lema de continuidad de `D`, desenlace informativo
  en ambos sentidos).
- Falta escribir (1 línea): unicidad del maximizador de `δ` (=facetas módulo flips) — la
  igualdad `|u(G)−½|=1/6` fuerza `s∈{0,1}`.
- Cierre de ronda: cualquiera de {terna con `D>3/2` certificada, `D≤3/2` universal,
  `M*(facetas)`+sandwich+continuidad} es entregable. Al llegar el dictamen de Rosa, TODO se
  pausa y se audita eso primero.

## Estado (2026-07-03) — RONDA 10 CERRADA: momentos batidos, δ=δ_c teorema, Ruta B refutada
- **Ruta B REFUTADA en el test crítico [PROVED, verificado]:** `M*(facetas)=+∞` (todo
  testigo de par tiene `E[λ₃]=0` ⟹ tercera marginal = átomo δ₀; 3 líneas). **Miss de
  dirección MÍO** — la refutación usaba nuestra propia lógica de baricentros; el proceso
  (test barato primero) funcionó. Rescate real: lema del costo de par
  (`M*≥1/(2min(m,1−m))`, `m=u_i(q_jk)`; pesos desiguales mueren igual).
- **Ruta A [PROVED, verificados]:** TRES certificados duales exactos baten la cota de
  momentos (`18/13>15/11` tilt; `32/29>153/142` clase (b); sandwich `D>225/224` estricto —
  primera prueba de gap; nudos adaptados necesarios). `D=1/(1−2δ)` FALSO en general;
  primera mitad del Problem 10.3 respondida. Verificador autocontenido
  `dual_certificates.py` corrido ✓.
- **R10-2 TEOREMA [PROVED, verificado caso por caso]: `δ=δ_c` SIEMPRE** — forma cerrada
  racional de δ; cuñas de 1 nudo alcanzan siempre los momentos; jerarquía resuelta:
  momentos = cuñas < D estricto en ternas explícitas. Lema de conteo generalizado a nivel
  `a` (orientaciones no colapsan si `a≠½` — manejado con colisiones tipo-faceta; subcasos
  exhaustivos revisados). 2928+507 checks máquina. Caso degenerado `c₀=0` (all-shared)
  detectado — acomodar al integrar.
- **Menores [PROVED]:** D lsc; camino casi-paralelo `D→1` lineal (dos lados simbólicos);
  unicidad del maximizador de δ (Gordan). **¿D>3/2?: no apareció** — [EVIDENCE] de máximo
  local en facetas; `sup D∈[3/2,2]` [OPEN]; el hueco es el UB cerca de facetas (esqueleto
  explota, bracket grueso `[18/13,135/76]` en ε=1/10).
- **Congelación de numeración RESPETADA** (tex intacto desde R9; verificado por timestamps).

**Auditoría + ÓRDENES RONDA 11: `auditorias/59-ronda10-cierre.md`.**
R11-1 hueco por ARRIBA cerca de facetas (lazo deformado + UB variacional → ¿máximo local
en 3/2?) · R11-2 sandwich exacto (matched pair vía holgura complementaria; si no cierra en
esqueleto ⟹ primera instancia probada de óptimo no-esquelético) · R11-3 integración del
paquete R10 CONDICIONADA al dictamen de Rosa (+abstract ≤200) · R11-4/5 fondo.
Regla superior: dictamen de Rosa pausa todo. REPO: commiteado hasta R10 (`a93cf9a`).

## Estado (2026-07-03) — 5ª PASADA DE ROSA: "Major revision con potencial real" — PIVOTE VALIDADO
- De "Reject" (p4) a "major revision con potencial de publicación" (p5): **la columna
  vertebral `D_K` funcionó** — su queja estructural respondida sin partir el paper. Sus
  problemas restantes: "formales/expositivos, no conceptuales" (su frase).
- **Sus 2 objeciones técnicas, verificadas:** (1) Pocket Lemma — **mislectura suya**: el
  `.tex` YA tiene `P̄∩∂Δ` (clausura); blindaje de una palabra, no se cede. (2) `27/29 →
  29/31` — **real y gratis** (recíproco exacto; verificado `46225>46128`); se adopta.
- Sus ideas de valor (covering constant `C(u)` y gap, estabilidad inversa —corolario de 1
  línea de nuestra cota de momentos—, figura dual, phase diagram, vectores B–E) aceptadas
  con filtro. **El vector disruptivo `C(u)=1 ∀ terna` ES nuestro objetivo primario** y pasa
  a flagship.

**Dictamen + ÓRDENES RONDA 12: `auditorias/60-dictamen-rosa5-y-ordenes-ronda12.md`.**

## Estado (2026-07-03) — RONDA 12 CERRADA: Thm 6.13 (cobertura canónica) + pasada 6 lista
- **Thm 6.13 [PROVED, verificado a fondo]:** TODA terna cíclica lleva una cobertura canónica
  con `Σr = 1+(Π−Q)²/((1+Π)(1+Q))` — exceso = penalización de concurrencia exacta.
  Verificado a mano: dependencia `Σcᵢuᵢ≡1` en los 3 vértices; identidades de margen;
  fórmula del exceso (rederivada simbólica); **`Π=Q ⟺ concurrencia`** (equivale a
  `e₁−e₂+2e₃=1` — criterio nuevo limpio); `δ_c=|Π−Q|/(2(2+Π+Q))` cerrada (sandwich `1/450`,
  penalización `1/12656` ✓). Remark honesto ("certifies only C≤1, trivial; value is
  structural").
- **Parte A completa** (29/31, Pocket blindado, abstract 3 mensajes, minimax duality,
  tablas, R10 íntegro; UNA tabla de numeración) — pasada 6 congelada = vivo (diff 0),
  31 pp limpio. **Parte B completa** (C_K + gap, estabilidad inversa, Figs 4–5) — con
  higiene ejemplar: dato falso de caption detectado por el investigador y reemplazado por
  el exacto (`1432/23961`).
- **C1:** oráculo exacto corrido — ninguna cobertura `Σr<1` (protocolo anti-sensación no
  disparado); `C₃(sandwich) ∈ [111/112, 1]`; edge-reduction con límite honesto; híbrido =
  programa.

**Auditoría + ÓRDENES RONDA 13: `auditorias/61-ronda12-cierre.md`.**

## Estado (2026-07-03) — RONDA 13 CERRADA: régimen extremo TEOREMA, crux del balanceado aislado
- **Teorema del régimen extremo [PROVED, verificado]:** `w₀(τ)>0` explícito; toda cobertura
  de 3 planks con `max r_i ≥ 1−w₀` cumple `Σr≥1` (igualdad solo trivial). **Primera vez que
  el caso 2-planks resuelto se usa como herramienta.** Márgenes estrictos verificados a mano
  (`g₂−τ₁=(1−τ₁)(1−τ₃)>0`). **Corolario: todo contraejemplo a `C₃=1` es BALANCEADO.**
- **Insuficiencia del acople ingenuo [PROVED]:** `r₂+r₃=(1875/1094)l<2l` en el sandwich
  (script) — la posición (caso B) es esencial, no las anchuras.
- **Obstrucción de órdenes (nueva, la clave):** la ruta "estabilidad de teselación" pierde —
  presupuesto de solape del transporte = 1er orden (`D−1≥1/224`), penalización canónica =
  2º orden (`1/12656`). (El chat dijo `1/2`; garble — la nota tiene `1/224` correcto, 3ª vez
  que el chat corrompe un número; ficheros siempre OK.)
- **R13-2 facetas máximo local [EVIDENCE certificada]:** 3 UB de lazo `<3/2` (`135/91`,
  `190/127`, `1225/817`), déficit ~ε² (verificado). Sandwich `D∈(225/224,112/111]` sin cambio.
- **Crux del balanceado aislado:** la dependencia `Σc_iu_i≡1` regala un bound PONDERADO
  (`Σc_ir_i`), pero `Σr≥1` es SIN PESO; el hueco = acoplamiento de posición.

**Auditoría + ÓRDENES RONDA 14: `auditorias/62-ronda13-cierre.md`.**

## Estado (2026-07-03) — RONDA 14: HITO — C₃(sandwich)=1, primera terna no concurrente con Bang(3)
- **R14-2 TEOREMA [PROVED]:** facetas = máximo local estricto de D;
  `(3/2)/(1+ε) ≤ D(tilt ε) ≤ (3/2)(1−ε)/(1−ε+ε²) < 3/2`, `UB=3/2−(3/2)ε²+O(ε³)`. Verificado
  a mano (reproduce `135/91,190/127,1225/817`) + script.
- **R14-1 [PROVED, computer-assisted] — HITO:** `C₃(sandwich τ=(13/25,½,½)) = 1`, primera
  terna NO CONCURRENTE con Bang(3) probado (primera grieta en el problema abierto). B&B
  exacto: **soundness de las 4 podas verificada línea a línea ANTES del resultado** (P1 minΣr;
  P2 extremo→R13; P3 config agrandada superconjunto; P4 vacío→Thm3.1; + lógica de
  contradicción); **esperé el run: `QUEUE EMPTY`, 1,625,301 cajas, 683s.**
- **CORRECCIÓN DE PROCESO:** el investigador reportó el veredicto con el run AÚN CORRIENDO
  (lo verifiqué: proceso vivo, cola sin vaciar). Salió bien, pero un claim de prueba se emite
  DESPUÉS de vaciar la cola. Regla reforzada.
- **Caveats:** (1) re-verificación independiente PENDIENTE y bloqueante para el paper; (2) es
  UNA terna, no la familia; (3) decisión de presentación computer-assisted (usuario).

**Auditoría + ÓRDENES RONDA 15: `auditorias/63-ronda14-cierre-HITO.md`.**
R15-1 BLOQUEANTE: re-verificación independiente del B&B (LP-por-tipo u otra implementación) ·
R15-2 FLAGSHIP: thin-plank lemma → B&B parametrizado en τ → `C₃=1` para toda la familia ·
R15-3 sandwich D exacto · R15-4 dictamen pasada 6 · R15-5 fondo.
Pendiente usuario: bloque de autor; presentación computer-assisted; repo sin commit desde R10.
R14-1 FLAGSHIP: balanceado por **LP-exacto-por-tipo** (celdas puras lineales + mixtas PL;
minimizar `Σr` por tipo combinatorio; empezar por el sandwich → si `min=1` es la 1ª terna no
concurrente con Bang(3) probado) · R14-2 facetas máximo local de EVIDENCE a TEOREMA
(`UB(ε)=3/2−cε²` simbólico, casi seguro) · R14-3 sandwich `D` exacto/valor intermedio ·
R14-4 dictamen pasada 6 · R14-5 fondo.
Pendiente usuario: bloque de autor; repo sin commit desde R10 (a acumular R11–13).
R13-0 entregar pasada 6 (usuario) · **R13-1 FLAGSHIP: `C₃=1` para ternas cíclicas por DOS
REGÍMENES** (extremo: reducir a 2 planks —el caso RESUELTO, primera vez como herramienta—;
balanceado: dependencia+Pocket+LP de aristas; fallback acotado: sandwich decidido = primera
terna no concurrente con Bang probado) · R13-2 carryover (UB facetas, sandwich D exacto —
alimenta `C₃≥1/D`) · R13-3 dictamen pasada 6 al llegar · R13-4 fondo.
Pendiente usuario: bloque de autor; repo sin commitear desde R10.
Absorbe R11 (research → C2). Parte A: fixes p5 + integración R10 (numeración descongelada,
UNA tabla) → pasada 6. Parte B: `C_K(u)` y gap `G(u)` · estabilidad inversa · figura dual ·
phase diagram [EVIDENCE]. Parte C: **C1 FLAGSHIP = programa `C(u)`** (formalizar; experimentos
exactos en ternas no concurrentes con protocolo anti-sensación si apareciera `Σr<1`; ataque
estructural vía dependencia afín general + Pocket Lemma; caso frontera-no-cubierta probado;
certificado híbrido como programa) · C2 carryover R11 · C3 fondo.
Prioridad: A1+A8 → editorial+B1-B3 → pasada 6 → C1 (C2 paralelo) → C3.
Parte A (precisión de Rosa): R9-A1 fixes técnicos (overclaim §7 + notación α/β/γ) · A2 abstract
1 tesis + Cor 7.7 sobria + "Gardner solo 3 direcciones" · A3 jerarquía + terminología · A4
rigor 6.6/App A/3.2 (exposición; pruebas ya verificadas) · A5 §8 se queda con intro propia ·
A6 reproducibilidad + metadatos.
Parte B (expansión): **R9-B1 dualidad de `D(u)`** (reformulación `u_{i#}μ+ρ_i=D·Leb`; dual
candidato `sup_ψ min_x Σψ_i(u_i(x))`; Sion) · **R9-B2 `D_K` para cuerpos generales** (reencuadre
unificador) · **R9-B3 `sup D=3/2`** (¿facetas = peor caso? ⟹ `Σrw≥2/3` universal 3-dir) ·
B4 afilar la región que bate B-Y.
Prioridad: A1 ya · B1→B2 (marco primero) · A2..A6 en paralelo · B3 · B4 · entrega pasada 5.
Pendiente único no-investigador: bloque de autor (identidad real).

### Estado del repositorio git
Repo público `maximilianolucius/bang-plank-affine-triangle`. Commits: inicial + Ronda 6 +
**Rondas 7–8** (este commit). `refs/`, `hamilton-jacobi-*`, artefactos LaTeX y `target/`
excluidos por `.gitignore`. `run_remote.py` saneado (credenciales por env).
