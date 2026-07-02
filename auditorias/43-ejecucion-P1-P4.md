# Auditoría de la ejecución P1–P4 (notas `43-*`, `42`) + Órdenes Ronda 2
> Auditor / Jefe de research: Claude. Fecha: 2026-06-30.
> Notas auditadas: `43-P1-batir-BY`, `43-P2-ambrus-dimension`, `43-P3-gardner-suficiencia`,
> `43-P4-rigidez-medianas`, `42-refs-papers-resumen`.
> Método: revisión de referee + verificación a mano del álgebra nueva.

---

## Veredicto global de la ronda

**Ejecución excelente y honesta.** El investigador (a) probó matemática nueva correcta
(P4 régimen genérico), (b) **resolvió mi objeción de P2** (disolvió el WLOG ortogonal, algo
que yo había dejado como duda dura), (c) no fabricó ningún teorema en P1 y delimitó el
requisito exacto, (d) refutó mi propia hipótesis en P3 leyendo la fuente. Dos defectos
concretos: **el parche a `notes/40` quedó a medias (auto-contradicción)** y P4 no cierra el
régimen no-genérico. Detalle abajo.

---

## P4 — Rigidez de medianas: **VERIFICADO (régimen genérico)** ✓

Reproduje el álgebra a mano. En el régimen genérico (los 3 `I_i` cruzan `½`), el orden de
las trazas está forzado por anclaje a vértices (verifiqué: traza de `P_i` es preimagen de un
intervalo bajo un mapa afín monótono, anclada donde `m_i=½∈I_i`), y las ecuaciones de
abutting dan el sistema lineal:
- `l`: `l1=1−2l3, l3=1−2l2, l2=1−2l1` ⟹ `9l1=3` ⟹ **`l_i=1/3`**.
- `h`: `h1=2−2h2, h2=2−2h3, h3=2−2h1` ⟹ `9h1=6` ⟹ **`h_i=2/3`**.
- Lema de concurrencia: `m(centroide)=(½,½,½)` ⟹ algún `I_i∋½`. ✓ (verificado).

**`I_i=[1/3,2/3]` único en el régimen genérico: correcto.** ✓ Es el **primer caso tight
NO-faceta de Bang(3) con rigidez** (parcial) — resultado genuino y citable.

**Pendiente real (no cerrado):** el **régimen no-genérico** (algún `I_i` no cruza `½`) está
solo *grid-exacto* (D=6,9,12) + "reducido a finitos sistemas lineales". El propio autor lo
etiqueta bien: el grid da cota superior y solo cubre endpoints racionales acotados ⟹ **NO es
prueba del continuo ahí**. La rigidez **completa** aún no está `[PROVED]`; el titular honesto
es "rigidez probada en el régimen genérico". Corrección menor aplicada bien: el espacio de
longitudes es **3-dim** (no 2-dim).

## P2 — Dimensión y WLOG de Ambrus: **ACEPTADO, resuelve mi objeción** ✓

Verifiqué la lógica central: la construcción de Ambrus (combinación convexa `x=Σc_j x_j`,
condición de escape, mapa al símplex estándar `T` en el espacio de coeficientes `c`) **preserva
el ancho relativo sin usar ortogonalidad**. Comprobé que `w_T(ũ_k)=1` (los `x_j∈K`, `w_K(u_k)=1`,
y los puntos de ancho realizan el spread), luego `rw_T(L̃_k)=rw_K(L_k)`. La normalización a
ancho unidad por dirección se logra **reescalando cada funcional `u_i↦u_i/w_K(u_i)`
independientemente** (rw invariante de escala) — **sin mapa afín global, sin ortogonalidad,
para cualquier `N`**. **Conclusión correcta:**
- Dimensión del símplex-objetivo = **`2N−1`, `N`=nº de planks** (impar, crece con `N`). El
  `2d−1` era un artefacto de que Ambrus reusa la letra `d` para el conteo. ✓
- El WLOG ortogonal es **cosmético** (artefacto de su normalización por mapa afín); la
  reducción vale para direcciones arbitrarias. ✓
- **Triángulo (2-símplex, dim par) nunca es target** (targets de dim impar). Robusto. ✓

Trabajo de primera; disolvió una objeción que yo di como "dura".

### ⚠ DEFECTO — el parche a `notes/40` quedó INCOMPLETO (auto-contradicción)
`43-P2` afirma "Corregido también en `notes/40`", pero `notes/40` **solo recibió una
inserción parcial**: hay una nota nueva (líneas ~79–86) que dice `2N−1`, **pero el cuerpo §3
(línea 73) sigue diciendo** "símplex `T` de dimensión **`2d−1`** embebido en `R^{2d}`" **y el
veredicto §5 (líneas 132–136) sigue diciendo** "objetivo = símplices de dim **`2d−1`** …
tetraedro en `R⁴`, no el triángulo". **`notes/40` ahora se contradice a sí misma.** Repetimos
el patrón que venimos corrigiendo. **Acción obligatoria:** reemplazar TODO `2d−1`→`2N−1` en el
cuerpo §3 y §5 de `notes/40` (no solo insertar una nota).

## P1 — Batir B-Y: **honesto, sin teorema, requisito bien aislado** ✓ (con una aclaración)

Verifiqué la expansión de primer orden: `S_c−1 ≈ δ+(1−c)Σrw_iε_i` (correcto), el requisito
`Σrw_iε_i ≥ |δ|/(1−c)`, y la Prop. §3 ("`S_0=1` + no-balanceado ⟹ `Σrw<1`", correcta). No
fabricó teorema; redujo P1 a: **"Lema 5 con holgura relativa uniforme `γ>0`"**. Bien.

**Aclaración que debo hacer (corrige un matiz de la nota):** el investigador leyó "Ruta A"
como "rehacer el SOS del **Lema 7**" y la declaró muerta — correcto que el Lema 7 no ayuda.
**Pero mi "Ruta A" era rehacer el Lema 5 con `N_c`**, y eso **es exactamente lo mismo que
probar `S_c≥1`**: en efecto `S_c = Σ width_i/N_c(u_i)` (pues `N_c=w·q_c`), o sea la meta ES
"**Bang-fuerte normalizado por `N_c`**", el Lema 5 con la cuerda `ℓ` reemplazada por
`N_c=(1−c)ℓ+c·w ≥ ℓ`. Ruta A y Ruta B **convergen**: la tarea es re-correr el argumento de
signos de Bang (Lema 5) con el normalizador `N_c`. Esto **afina** (no contradice) su §5.

**No hay atajo numérico** (confirmado por el autor §6): los tests solo tocan `δ≥0` donde
`S_c≥1` es trivial por el sandwich; el régimen decisivo `δ<0` no tiene configs testeables. P1
es **puramente analítico**.

## P3 — Gardner: **ACEPTADO; mi hipótesis refutada correctamente** ✓

El investigador leyó Gardner y **refutó mi hipótesis** ("`cond=2` = criterio de Gardner"):
Gardner Thm 1 es positivo **solo `≤2` direcciones**; el caso finito `≥3` es **su pregunta
explícitamente abierta**, justo donde vive `cond=2`. Verdicto correcto: **Gardner NO cierra
la suficiencia**; sigue `[OPEN]`, ahora identificada como caso de la pregunta abierta de
Gardner (lo cual **eleva** su valor si se prueba). Cita de `notes/12` arreglada (positivo→
Gardner Thm 1; negativo→Example 1). Consistencia `cond=3` facetas (Gardner Example 1) ✓.

## `42` — Digest de refs: **sólido**; buen catch de errata

Buen resumen de fuente primaria. **Catch correcto:** la errata del preprint B-Y
(`2/√(d+1)=1.155>1` imposible como cota inferior; la correcta es `2/(1+√d)=0.828`) — verifiqué
la aritmética. La lección de rigor de Pinasco (decimales no certificados, Prop 2.8; falla en
`n=15,16`) bien registrada — aplicarla a toda verificación futura.

---

## Estado de las 4 órdenes

| Orden | Estado | Nota |
|---|---|---|
| P1 batir B-Y | **ABIERTO, bien reducido** | = "Bang-fuerte con `N_c`" para `c>0`; requisito `γ>0` en Lema 5 |
| P2 Ambrus dim/WLOG | **RESUELTO** ✓ | dim `2N−1`; WLOG cosmético; **falta terminar el parche a `notes/40`** |
| P3 Gardner | **RESUELTO** ✓ | no cierra suficiencia; cita `notes/12` arreglada |
| P4 rigidez medianas | **PARCIAL** | genérico PROVED ✓; no-genérico pendiente (mecánico) |

═══════════════════════════════════════════════════════════════════════
# ÓRDENES DE TRABAJO — RONDA 2
═══════════════════════════════════════════════════════════════════════

Reglas de siempre: aritmética exacta / continuo (nunca grilla como prueba); etiquetas
estrictas; sin lenguaje grandilocuente; fuente primaria → PDF en `refs/`.

## R2-1 (FLAGSHIP, alto riesgo/alto valor) — Bang-fuerte con `N_c` (= batir B-Y)
**El objetivo primario se reduce a UN lema limpio:**
> **Probar `Σ_i width_i / N_c(u_i) ≥ 1` para algún `c>0` fijo**, con `N_c=(1−c)ℓ_K+c·w_K`.
> Da `Σrw ≥ c+(1−c)·min(ℓ/w) > 0.928` (triángulo) / `> 2/(1+√d)` (general). **Mejora SOTA.**

`N_c` interpola cuerda `ℓ` (c=0, = Lema 5 de B-Y, PROBADO) y ancho `w` (c=1, = la conjetura).
`c` mide "cuánto hacia el ancho llega el argumento de signos de Bang".

**Pasos:**
1. **Extraer la prueba del Lema 5 de B-Y** (sigue Bang / **Verreault Lema 2.3**). Identificar
   EXACTAMENTE dónde se usa que el normalizador es la **cuerda más larga `ℓ`** (vs el ancho `w`).
2. Re-correr ese argumento con `ℓ → N_c`. La cuerda entra porque Bang selecciona signos **a lo
   largo de la cuerda más larga**; el gap `ℓ` vs `w` es el "chord vs width" del Lema 7.
   Pregunta: ¿el argumento de signos tolera un normalizador entre cuerda y ancho, y hasta qué `c`?
3. Objetivo: `c>0` explícito, o una obstrucción demostrada de por qué `c*=0`.
**Bloqueador:** falta **Verreault survey (arXiv:2203.05540)** en `refs/` — tiene la prueba del
Lema 2.3 y el catálogo de métodos. **Descargarlo primero.**
**Riesgo:** alto (es la frontera 2026). **Criterio de parada:** si tras estudiar la prueba de
Bang no aparece holgura para `N_c`, documentar la obstrucción y **congelar P1**; el valor pasa a R2-4.

## R2-2 (cierre limpio, bajo riesgo) — completar la rigidez de medianas
Cerrar el **régimen no-genérico** de P4 (algún `I_i` no cruza `½`) a mano, por el mismo método
de anclaje de §2 (finitos sub-casos: uno o dos `I_i` sin `½`). Cierra el teorema de medianas
**completo** (cota + rigidez), citable como caso tight no-faceta con unicidad.
**Criterio hecho:** rigidez `[PROVED]` sin apoyarse en grid.

## R2-3 (higiene obligatoria, trivial) — terminar el parche de `notes/40`
Reemplazar **todo** `2d−1`/`tetraedro en R⁴` por `2N−1` (`N`=#planks) en el cuerpo §3 (línea
~73) y el veredicto §5 (~132–136) de `notes/40`. Hoy la nota se auto-contradice. También en
`notes/42 §4` ("dim `2d−1`") y `notes/04` (tabla G0) si arrastran el `2d−1`.

## R2-4 (deliverable seguro, en paralelo) — paper "casos + método", alcance honesto
Ensamblar el núcleo probado con **alcance explícito**: *"nuevos casos tight y un método de
transporte/celdas para el triángulo (un cuerpo concreto); NO la conjetura vía Ambrus (el
triángulo no es target de la reducción, `43-P2`)."* Contenido firme: `1/d` (`08`), 2-direcciones
(`12`, cita Gardner Thm 1), faceta-paralelo, `3 facetas+1` (`30 §1`), **medianas cota+rigidez**
(`36`+R2-2), **caracterización necesaria** de concurrencia (`37`, `1ᵀV⁻¹1=2`). Este es el
resultado que existe pase lo que pase con P1.

## R2-5 (opcional, medio riesgo) — transporte en símplices de dim impar
Solo si R2-1 se congela. La caracterización `1ᵀV⁻¹1=2` y la medida del perímetro
(`36/37`) son dimension-agnósticas. El mínimo target real de Ambrus es el **3-símplex**
(pero `N=2` planks = 2 direcciones = ya resuelto por Gardner Thm 1 / AKP). El primer caso
nuevo sería `N=3` planks → 5-símplex, o el símplex regular en dim `d` con sus cevianas
concurrentes ("medianas" del d-símplex). Exploratorio: ¿generaliza el teorema de medianas al
símplex regular en toda dimensión? Sería una familia nueva en todas las dimensiones (aunque
codim-restringida, no cierra la conjetura).

---

## Prioridad
1. **R2-1** (flagship; empezar por descargar Verreault y estudiar el Lema 5).
2. **R2-3** (trivial, ya) + **R2-2** (barato) + **R2-4** (continuo).
3. **R2-5** solo si R2-1 se atasca.

**Recordatorio estratégico honesto:** batir B-Y (R2-1) es territorio de expertos 2026, alto
riesgo. El **deliverable garantizado es R2-4** (casos + método, alcance honesto). Mantener
ambas vías; no vender el triángulo como ataque a la conjetura.
