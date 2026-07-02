# Auditoría de `notes/39` (rigidez, suficiencia, pivote) + dirección de investigación
> Auditor / Jefe de investigación: Claude. Fecha: 2026-06-30.
> Nota auditada: `notes/39-rigidez-suficiencia-pivote.md` (mismo id: 39).
> Objetivo primario: **conjetura afín de Bang** — avanzar el caso del triángulo
> (Bang(3)) y/o **mejorar la mejor cota conocida** (Bakaev–Yehudayoff `2/(1+√d)`;
> triángulo `4√3−6 ≈ 0.928`).
> Estándar: referee. `[PROVED]/[OPEN]/[EVIDENCE]` estrictos.

---

## A. Auditoría exigente de `notes/39`

Verificación previa (cómputo exacto, `fractions`): `cond(triple C)=2.02227`
(nota dice 2.0223 ✓); identidad de `Cov` y "triangular automática para `cond≈2`,
`a>0`" reproducidas (0 violaciones sobre 517 casos; la nota afirma 373/0). Los
cómputos son **confiables** y la nota es honesta. Aun así, como referee, exijo lo
siguiente antes de que nada de §1–§2 se cite:

### A.1 §1 (rigidez mediana) — la reducción está INCOMPLETA
**Defecto principal (bloqueante para el `[REDUCED]`):** §1.2 reduce la rigidez a
las tres ecuaciones de partición del perímetro
`(AB) r2+2a1+2b3=1`, `(BC) r1+2b2+2a3=1`, `(CA) r3+2b1+2a2=1`
(correctas — verificadas contra los rangos de `m_i` por arista). Pero son
condiciones de **frontera (1-D)**. Una cobertura válida con `Σr=1` debe además
**cubrir el interior (2-D)**, y la nota escribe "+ cobertura interior" en prosa
pero **no la incorpora al CSP**. El sistema reducido a "un CSP finito 1-D sobre las
3 aristas" es por tanto un conjunto de condiciones *necesarias*, no el problema de
rigidez completo: un config que particiona la frontera pero deja un hueco interior
no es contraejemplo (no es cobertura), luego el CSP admite **soluciones espurias**
que solo la condición interior descarta.

**Defectos menores:**
- §1.2 dice "2-dim de soluciones de longitud". Son **3-dim**: 6 incógnitas
  `(a_i,b_i)` menos 3 ecuaciones de rango 3 (su suma da `3Σr=3`, no una dependencia
  ⇒ rango pleno).
- §1.1 "exactamente UNA teselación" proviene de grilla `/24` ⇒ solo "exactamente
  una **grid-aligned**". La unicidad continua es lo que falta; el grid **omite**
  candidatos off-grid, así que no acota la unicidad (lección simétrica a `notes/33`:
  el grid miente sobre `min`; aquí miente sobre "no hay otras").

**Veredicto §1:** la **cota** `Σr≥1` está PROBADA (`notes/36`, verificada). La
**rigidez** NO está "reducida a un CSP finito"; está reducida a *condiciones
necesarias de frontera* + un problema interior no formalizado. Reclasificar a
`[EVIDENCE + reducción parcial]`.

### A.2 §2 (suficiencia de `cond=2`) — bien delimitada, pero subvende el hueco
La reducción a media+varianza es **correcta** (verifiqué la identidad
`Cov=(a3²−a1²−a2²)/(24a1a2)` y que la desigualdad triangular ⟺ `|Cov|≤1/12`,
automática para `cond=2` interior). Pero el hueco real es **doble**, y la nota
enfatiza solo la mitad:
1. Uniformidad **plena** de `S=a1u1+a2u2` (momentos ≥3) — mencionado.
2. El acoplamiento debe estar **soportado en `Φ(Δ)`** (no en todo el cuadrado) y ser
   compatible con el **signo mixto** de `a` (ej. `a=(2,−2,2)`), régimen donde el
   argumento de varianza (`a>0`) **no aplica**.

Es decir: media+varianza es contabilidad de condiciones necesarias en un régimen
parcial; está **lejos** de una construcción. Correcto etiquetarlo `[OPEN]`, pero
"solo falta momentos superiores" subvende la dificultad. **Kellerer/LP (453/453) es
evidencia, no prueba.**

### A.3 §3 (pivote) — correcto, lo respaldo
"Transporte = rebanada codim-1; el grueso off-surface está fuera del alcance de una
sola medida (`notes/37 §2` necesidad, PROBADA)" es **correcto**. Consecuencia
operativa (clave de la dirección): **dejar de minar transporte** salvo el cierre
barato de rigidez.

**Imprecisión residual a corregir en 33/38:** se repite "on-surface ⟹ tight". Falso
en general: on-surface ⟹ (módulo suficiencia, abierta) existe medida ⟹ `Σr≥1`
*demostrable*; **no** implica `min Σr=1`. La tabla de `notes/38 §1` tiene una terna
"random gen" con `cond=2` y `min~1.0615` (cota superior, ambiguo). Firme solo:
**medianas** (medida explícita + teselación exhibida). Fijar el lenguaje.

---

## B. Mapa honesto del objetivo primario (a hoy)

| Frente | Estado | ¿Avanza el objetivo primario? |
|---|---|---|
| `Σrw≥1` general (la conjetura) | ABIERTA (incl. Bang(3)) | — |
| Cota SOTA general | `2/(1+√d)` (B-Y 2026) | mejorarla = avance real |
| Cota triángulo | `4√3−6≈0.928` (B-Y aplicado) | mejorarla = avance real |
| Transporte / familia concurrencia | codim-1; **probado solo medianas** | NO (medida cero) |
| Certificado combinatorio off-surface | abierto (lead: celdas de escape) | SÍ, pero moonshot |

**Conclusión de dirección:** el transporte NO puede alcanzar el objetivo primario
(capado a codim-1, demostrado). Las dos vías que lo tocan son **(P-B) mejorar la
cota** y **(P-4) el certificado combinatorio**. El resto es consolidación.

---

## C. Tareas asignadas (prioridad, riesgo, entregable)

### PRIORIDAD 1 — **P-B: batir Bakaev–Yehudayoff** [riesgo medio, EV alto, incremental]
Única vía con mejora *garantizada-si-funciona* de la SOTA, independiente de Bang(3).
- **Fundamento firme (`notes/31/34`):** sandwich `S_1≤S_c≤S_0`; `S_0=Σwidth/ℓ≥1` es
  el **Lema 5 de B-Y**; `S_c≥1 ⟹ Σrw≥q_c≥c+(1−c)·0.928 > 0.928`.
- **Reducción exacta (`notes/35 §1`):** `S_c≥1 ⟺ S_0−1 ≥ L_c`, con
  `L_c=Σ rw_i·c(1−ρ_i)/(ρ_i q_c)`. En balanceadas ambos lados = 0.
- **Observación de dirección:** por el sandwich, donde Bang YA está probado
  (facetas, medianas, ≤2 direcciones) se tiene `S_c≥S_1≥1` **gratis**; el trabajo
  real es el régimen off-surface no-balanceado, donde solo hay `S_0≥1`.
- **Tarea:** obtener/reconstruir la **prueba del Lema 5 de B-Y** y extraer la
  **holgura `S_0−1` como función de la no-balanza `(1−ρ_i)`**; probar `S_0−1 ≥ L_c`
  para el mayor `c` posible. Hay `c*∈(0,1)` umbral (`c→0` B-Y trivial; `c→1` Bang
  duro). **Objetivo: `c*>0` explícito.**
- **Entregable:** `Σrw ≥ c+(1−c)·(4√3−6)` (triángulo) — mejora estricta de 0.928,
  publicable aunque Bang(3) no caiga. Análogo general con `2/(1+√d)`.
- **BLOQUEADOR:** B-Y arXiv:2602.20290 NO está en `refs/`. Ver §D.

### PRIORIDAD 2 — **Cerrar el teorema de medianas (rigidez)** [riesgo bajo, citable]
- **Tarea:** (i) **completar la reducción** añadiendo la cobertura interior omitida
  (A.1); (ii) resolver el CSP (partición de frontera + interior) por **análisis de
  casos exacto** (racional), probar `Σr=1 ⟹ I_i=[⅓,⅔]` único; corregir el conteo de
  dimensión (3-dim).
- **Entregable:** "Bang para las 3 medianas, sharp, locus de igualdad = {tercio
  central} único" — primer caso tight no-faceta *con rigidez*.

### PRIORIDAD 3 — **Suficiencia de `cond=2` vía Gardner 1988** [riesgo medio-alto, valor alto]
- **Dirección nueva (no explorada):** la existencia de medida con marginales
  prescritas en **finitas direcciones** es el objeto de **Gardner, Pacific J. Math.
  135 (1988) 299**. Gardner probó existencia para 2 direcciones (R²) y no-existencia
  para *todas*. **Hipótesis: `1ᵀV⁻¹1=2` es la condición de resolubilidad de Gardner
  para 3 direcciones fijas.** Verificar puede **cerrar la suficiencia de un golpe** o
  probar que es nueva.
- **Tarea:** leer Gardner 1988; mapear su criterio al caso de 3 direcciones;
  contrastar con `cond=2` + `p` interior.
- **BLOQUEADOR:** Gardner 1988 no está en `refs/`. Ver §D.
- Si Gardner no cierra: existencia del 3-marginal uniforme sobre `Φ(Δ)` por dualidad
  de Kellerer analítica (moonshot, `notes/38 §2.2`).

### PRIORIDAD 4 — **Certificado combinatorio off-surface (la conjetura)** [moonshot]
- **Objeto (síntesis `notes/23 E`):** certificado entero / dependiente de posición /
  de borde / "escape-de-TODAS". Candidato: **celdas de escape + Farkas**
  (`notes/30 §8.5`, `notes/33 §6`): `m=3`, 8 celdas `R_σ`, cada `R_σ=∅` con Farkas
  de ≤3 restricciones (Helly 2-D).
- **Nugget concreto:** probar la **estabilidad transversal en el collar `R=1`**
  (`notes/30 §8.4`): el cono tangente de las condiciones de cobertura a lo largo de
  `{Σr=1}` no contiene dirección `dR<0`; si `dR=0`, el primer término no nulo es ≥0.
- **Lead:** el patrón de **6 celdas mixtas** (arista + 2 caras, pesos `{½,⅔,⅓}`) que
  certifica la tercio-central; ver si se extiende al locus de igualdad de Hunter `T=1`.
- **Regla anti-fabricación (`paper-ready/PROMPT-M4-ATTACK`):** grilla que "confirma"
  NO es prueba; solo cuenta una identidad SOS/Farkas exacta o aritmética de
  intervalos con `Lipschitz·celda < margen` *en todo el collar* `R=1` (margen→0).

### CONSOLIDACIÓN (continua) — **Paper del núcleo probado**
`1/d` (`notes/08`), 2-direcciones, faceta-paralelo, **3 facetas+1** (`notes/30 §1`),
**medianas** (`notes/36`), **caracterización necesaria** de concurrencia
(`notes/37`). Marco: "primer ataque por transporte/medida al plank afín; primeros
casos tight no-faceta".

### HIGIENE (pendiente de la auditoría global `AUDITORIA_CLAUDE_30Jn.md`)
- `notes/09` (Fibonacci) sin banner y depende de peeling (refutado): banner o mover.
- Banners en `notes/05`, `06` → vía toric muerta (`notes/15/23`).
- Renombrar/fusionar `notes/16` (es KKT, dup de 21).
- Corregir "on-surface ⟹ tight" en 33/38 (A.3).

---

## D. Bloqueadores (acción inmediata)

Los **dos papers load-bearing de las vías que tocan el objetivo primario NO están en
`refs/`** (solo hay 2 PDFs de Pinasco):

1. **Bakaev–Yehudayoff, arXiv:2602.20290 (2026)** — necesario para P-B (interior del
   Lema 5). Sin él, P-B está bloqueado.
2. **Gardner, Pacific J. Math. 135 (1988) 299** — necesario para P-3.

Acción: descargar ambos a `refs/` antes de arrancar P-B/P-3.

---

## E. Resumen ejecutivo

- **El transporte terminó su ciclo útil.** Firme: medianas (`36`) + necesidad (`37`).
  No perseguir más la familia por transporte salvo P-3 (Gardner) y cierre de rigidez.
- **Apuesta por el objetivo primario: P-B** (batir 0.928), incremental y publicable;
  requiere el paper B-Y.
- **Bang(3) pleno = P-4**, moonshot con nugget concreto (transversalidad en `R=1`).
- **Desbloquear ya:** adquirir B-Y 2026 y Gardner 1988.
