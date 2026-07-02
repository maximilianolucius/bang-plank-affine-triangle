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
