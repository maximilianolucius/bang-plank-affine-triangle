# Auditoría detallada de `notes/*.md`
> Auditor: Claude (Opus 4.8). Fecha: 2026-06-30.
> Alcance: las 31 notas de `./notes/`. Método: revisión matemática a mano +
> verificación computacional de los `[PROVED]` nuevos (Python, `fractions`/MC) +
> cruce contra el sistema de archivos (`experiments/`, `refs/`, `drafts/`).
> Convención: separo **evidenciado** (verificado aquí) de **inferido** de **citado**.

---

## 0. Veredicto global

La carpeta tiene **dos capas de calidad epistémica muy distinta**:

- **Notas 30–37 (2026-06-30):** cuidadosas, auto-correctivas, etiquetan
  `[PROVED]/[EVIDENCE]/[OPEN]`, atrapan sus propios artefactos de grilla. La
  matemática nueva marcada `[PROVED]` **es correcta** (verificada, ver §5).
- **Notas 05–21 (2026-06-27/29):** mezcla de trabajo serio con **notas en estilo
  "victoria" que el propio proyecto tuvo que demoler** (auditoría `notes/22`). Casi
  todas quedan con banner `[REFUTADA]` — **pero no todas** (ver Hallazgo #1).

La trayectoria del proyecto es buena (la higiene mejora con el tiempo), pero
quedan **errores concretos, inconsistencias entre notas y desorden de archivos**.
Ningún `[PROVED]` del bloque final resultó falso; los problemas son de
notas obsoletas sin banner, duplicados, nombres engañosos y un par de
sobre-afirmaciones de etiqueta.

---

## 1. Verificación de existencia de artefactos (sistema de archivos)

- `experiments/` **existe** con ~40 scripts. La mayoría de los scripts citados en
  las notas **existen** (`m1_check.py`, `m1_homog.py`, `m2_triangle.py`,
  `prop1_toric.py`, `prop2_kkm.py`, `prop3_flow.py`, `audit_helly.py`,
  `audit_entropy.py`, `audit_zonotope.py`, `audit_kkt_contact.py`,
  `audit_algebra_2.py`, `exp_w2_delta.py`, `exp_w2_locus.py`, `exp_w2_search.py`,
  `exp_w2_C.py`, `exp_bang3_*.py`, `exp_ell_verify.py`). **No hay fabricación
  masiva de scripts.**
- `experiments/prop2_rust/` **existe y está compilado** (binario en `target/release/`).
- `drafts/paper.tex`, `drafts/bang-plank-paper.tex` y `drafts/paper.pdf`
  **existen** (la afirmación de `drafts/BUILD.md` es correcta). Hay **dos** `.tex`
  (`paper.tex` 06-27 y `bang-plank-paper.tex` 06-28): posible duplicado a depurar.
- **NO existen:**
  - `scratchpad/ball_fitz.txt` (citado en `notes/04 §T0.2`) — referencia muerta.
  - Ningún artefacto del barrido semialgebraico de **227M celdas** de `notes/17`
    (el único Rust es `prop2_rust` = Betti/nervio, de la nota 14).
  - `audit_zono.py` (citado en `notes/22`); el real es `audit_zonotope.py`.

---

## 2. Hallazgos GRAVES

### #1 — `notes/09-fibonacci-bootstrap.md`: nota no-refutada y matemáticamente insostenible
Es la nota más peligrosa que sobrevive. Presenta un "proof skeleton" de
`Σrw ≥ 1` para el triángulo (¡la conjetura!) y **NO tiene banner de refutación**
(a diferencia de 13–21). Tres fallas, cualquiera fatal:

1. **Depende de "peeling"**, refutado explícitamente en `paper-ready/BATTLE-PLAN-RESULTS.md`,
   `notes/24` y `PROMPT-TWO-WALLS §3`: el corte de un plank inclinado no es
   paralelo a la arista, el complemento es un cuadrilátero, no un triángulo
   semejante. El paso central de 09 ("la subregión más allá del nivel `s` es
   `T'=sT` semejante") solo vale para planks paralelos a aristas.
2. **Conflación de inducciones:** la inducción es sobre niveles abstractos `k`
   (con `b_k = 1 − 1/F_k → 1`), pero una cobertura tiene un conjunto **finito y
   fijo** de planks. No hay mecanismo que garantice que cubrir `T'` reinvoque la
   hipótesis al nivel `k` con las mismas planchas ni con las escalas de Fibonacci.
3. **El límite es imposible:** `b_k → 1` exige infinitos pasos de peeling, pero
   "se suma el rw de la plancha pelada" en cada paso — con planks finitos no se
   puede pelar infinitamente. La recursión `1/ε_{k+1}=1/ε_k+1/ε_{k−1}` es un
   *ajuste a posteriori* a `1/F_k`, no una derivación geométrica.

**Acción:** banner `[REFUTADA — depende de peeling]` o mover a histórico.

### #2 — Inconsistencia toric-EJ: `notes/05` y `06` con conclusión optimista que 13/15 mataron
- `notes/06 §5b`: *"la clean vanishing está disponible después de todo…
  plausiblemente al alcance, no bloqueado"*; `notes/05 §5c`: *"el símplex requiere
  genuinamente la maquinaria toric Euler–Jacobi"*.
- `notes/15` (auditoría 2): la vía algebraica/tórica está **MUERTA** —
  denominadores no-Laurent; al limpiarlos la resultante densa es ≡0 (raíces en el
  infinito). Confirmado en `notes/23 D13` y `notes/24`.

Ni 05 ni 06 tienen banner apuntando a esa muerte. Peor: **contradicción interna
en 06** — §3 dice "ceros en el infinito genéricos", §5b dice "ALL en el toro,
ninguno en la frontera".
**Acción:** banner en 05 y 06 → ver 15/23.

### #3 — `notes/16` y `notes/21` son la MISMA nota (KKT) duplicada; el nombre de 16 miente
Verificado por header:
- `16-dual-victory-synthesis.md` → contenido **KKT** ("Rigidez Geométrica de
  Puntos de Contacto"). El nombre "dual-victory-synthesis" no tiene relación con
  el contenido.
- `21-kkt-geometric-rigidity-prop7.md` → contenido **KKT**, casi idéntico (misma
  ecuación `(x_i⁺−x_i⁻)/w_i = ∇w_Δ/w_Δ`, mismo "≤5 testigos").

Son near-duplicados (la auditoría 22 los llama "Prop 7/16", reconociendo el
doblete). Nota: `18-helly-convex-geometry-prop4.md` **sí** es Helly (ahí el nombre
coincide). El esquema `propN` de los nombres está descuadrado respecto a las
PROPUESTAS de `notes/13` (propuesta 4 = "medidas signadas/Farkas", no Helly ni KKT).
**Acción:** renombrar 16 o fusionar 16+21.

---

## 3. Hallazgos MEDIOS

### #4 — `notes/33 §4.2` confunde "mediana" (balanceada) con "genérica"
Concluye "no hay holgura genérica: direcciones genéricas también teselan ajustado",
y su **único ejemplo exacto** es `u1=(½,0,1), u2=(0,1,½), u3=(1,½,0)` con
`I_i=[⅓,⅔]` — que son **exactamente las medianas** (= `notes/36`): **balanceadas y
simétricas** (`τ=½`, `ρ=1`), NO genéricas. La propia `notes/34 §2.2` corrige esto
("el error es 'no-faceta ⇒ ρ<1': las medianas son no-faceta pero balanceadas"). El
otro soporte de 33 (terna "C", `min≈1.0005` por Nelder-Mead) es **cota superior**,
no exacta. La afirmación "tight en *esencialmente todas* las direcciones" está
sobre-respaldada; el único soporte exacto es un caso no-genérico.

> **[RESUELTO 2026-06-30 por notas 38/39]** El banner nuevo de `notes/33` y
> `notes/38 §1` corrigen esto: on-surface (`cond=2`) tight solo para los casos
> **exhibidos** (medianas); off-surface **AMBIGUO** (los `min Σr` eran cotas
> superiores). Queda imprecisión residual menor ('on-surface ⟹ tight' no es
> general) — ver Adenda §8 y `auditorias/39-rigidez-suficiencia-pivote.md`.

### #5 — `notes/04` Gate G0: "Ambrus reduction CONFIRMED" más fuerte que lo evidenciado
La tabla G0 marca la reducción de Ambrus (símplices ⇒ general) como **"YES —
confirmed from primary source"**. Pero el mismo §T0.3 admite: (a) es **inédito**
(manuscrito en la web de Rényi), (b) discrepancia de normalización **½ vs 1** sin
resolver, (c) `notes/05 §1` aún dice "**Action: read the appendix**". O sea:
confirmado que *existe* y que B-Y lo cita, no que *se verificó la prueba*. La
normalización ½/1 **nunca se resuelve** en ninguna nota posterior. Es un cimiento
de M2 marcado "confirmado" sin auditar.

### #6 — El "incidente Hunter" fue una regresión desde una postura inicialmente correcta
`notes/01` (06-27, deep-research adversarial) ya decía correctamente: *"open even
for three planks (Bang settled only the two-plank case)"* `[3-0]`. Las notas del
bloque m4 (24–28) y `BATTLE-PLAN` **retrocedieron** a "3 planks cerrado por
Hunter" y construyeron sobre eso, hasta la corrección masiva del 06-30. El dato
correcto estaba desde el día 1; el error se introdujo después y fue **auto-
infligido**. **Lo positivo:** la corrección 2026-06-30 se aplicó bien y de forma
consistente (banners en 24, 25, 26, 27, 28, 30, 33 + reparación real vía
`notes/30 §1`). Es el mejor manejo de error del proyecto.

### #7 — `notes/17` (227M celdas): resultado sin artefacto reproducible
Afirma un certificador Rust/Rayon de **227.255.000 celdas** en `172.16.0.35`. En
`experiments/` el único proyecto Rust es `prop2_rust` (= Betti/nervio, nota 14).
**No hay** script/binario del barrido semialgebraico m=4. Ya deprecado como prueba
por `notes/22` (grilla ~6.5 subdiv/dim, margen→0 en `R=1`); añado que **el
resultado no es reproducible desde el repo** y exhibe los *tells* de fabricación
que `PROMPT-M4-ATTACK` prohíbe ("Conclusión Analítica Irrefutable", "escudo
definitivo"). Mismo estilo en 13, 16, 20, 21 (lenguaje grandilocuente +
confirmaciones redondas), todos ya refutados por 22.

---

## 4. Hallazgos MENORES / higiene

- **Referencia muerta:** `notes/04 §T0.2` cita `scratchpad/ball_fitz.txt` para el
  análisis de la prueba de Ball — no existe (scratchpad es efímero). Toda la tesis
  "Euler-Jacobi-ificar a Ball" cuelga de esa lectura; perder el fuente es relevante.
- **Nombre de script equivocado:** `notes/22` cita `audit_zono.py`; el real es
  `audit_zonotope.py`.
- **Atribución floja:** `notes/34 §3` y `notes/35` llaman al `0.928` "**Teorema 8
  de B-Y para el triángulo**". El Teorema 8 de B-Y es el general `2/(1+√d)=0.828`;
  el `0.928` es *consecuencia* del Lema 5 de B-Y aplicado al `min ℓ/w` del
  equilátero (lo derivan ellos mismos). La matemática es correcta
  (`Σrw ≥ (min ρ)·S_0 ≥ 0.928`); solo la etiqueta sobra.
- **`notes/12` "RIGUROSO":** el teorema de 2 direcciones es cierto (Gardner 1988 /
  AKP 2019), pero la prueba autocontenida apoya el Paso 3 (acoplamiento de
  marginales uniformes vía Strassen+Hall) en "verificado numéricamente, masa=1",
  no en una prueba de la condición de Hall para todo triángulo admisible. Riguroso
  *módulo* un paso citable a Gardner; conviene citarlo, no asegurarlo con numérica.
- **`notes/37` título vs alcance:** "Bang por transporte para la familia de
  concurrencia" suena a teorema, pero la suficiencia es `[STRONG EVIDENCE]` (LP
  numérico 453/453), no probada. Lo único realmente probado de esa familia es el
  **punto** de las medianas (`notes/36`). El §5 SCOPE lo aclara, pero el encabezado
  sobre-vende.

---

## 5. El núcleo SÓLIDO (verificado, sin objeciones)

Verificación computacional ejecutada (Python, `fractions`/Monte Carlo):

| Resultado | Nota | Verificación |
|---|---|---|
| `Σrw ≥ 1/d` por medida única (lema de concavidad Brunn–Minkowski) | 08 | prueba correcta; pico marginal triángulo = **2.02 ≈ d** ✓ |
| 2 direcciones → `Σrw ≥ 1` | 10–12 | cierto (Gardner/AKP); prueba módulo Strassen |
| **3 facetas + 1 plank arbitrario** → `Σrw ≥ 1`, sin Hunter (fibras `F_s`) | 30 §1 | **revisada línea a línea: correcta** |
| Teorema A (borde activo común) y B (m=4, 3 facetas+1) | 26 | Caso 1 ok; Caso 2 reparado vía 30 §1 ✓ |
| `W_k ⟺ Bang(k+1)` (Prop 3.1, lógica pura) | 27 | lógica correcta en ambas direcciones ✓ |
| **3 medianas → `Σrw ≥ 1`** (transporte, medida del perímetro) | 36 | `Σm=3/2` exacto; marginales uniformes (MC 0.99–1.01) ✓ |
| Condición necesaria `1ᵀV⁻¹1=2` (concurrencia de `{u_i=½}`) | 37 | medianas cond=2 / p=centroide; facetas cond=3 / fuera de Δ ✓ |
| Sandwich `S_1≤S_c≤S_0` + identidad de rigidez (R) | 31 | identidad (R): **error 6.7e-16** sobre 1e5 casos ✓ |
| Fórmula `ℓ/w` equilátero, `min=4√3−6` en `τ=2−√3` | 34 | `lw(0)=lw(½)=lw(1)=1`; **min=0.928203** exacto ✓ |
| Identidad shifted Euler–Jacobi `(⋆⋆)`, margen `1/n` | 30 §6 | consistente con drafts/M1; testigo no forzado a Δ/bola (honesto) |

Las **refutaciones** de `notes/22` (zonotopo posición-independiente; nervio
circular + falla de borde; KKT asume óptimo=1; semialgebraica margen→0) son
**correctas y honestas**. El "mapa de obstrucción" de `notes/23` (4 propiedades de
un certificado ganador: entero/combinatorio, dependiente de posición, de borde,
escape-de-TODAS) es el producto más reutilizable del proyecto; no hallé fallo
—con el matiz de que `notes/23 D14` ya fue correctamente actualizado por 36/37
(una medida única SÍ alcanza `c=1` en la superficie de concurrencia).

---

## 6. Estado por nota (resumen)

| Nota | Tema | Estado de auditoría |
|---|---|---|
| 01 | deep-research SOTA | Sólida; correcta desde el inicio (3-plank abierto) |
| 02 | gaps & milestones | Planificación; OK |
| 04 | M0 / Gate G0 | OK salvo "Ambrus CONFIRMED" sobre-afirmado (#5); ref muerta (#4-menor) |
| 05 | M2 setup | Hallazgo real (esquinas) ✓; conclusión pro-toric obsoleta sin banner (#2) |
| 06 | toric-EJ findings | Contradicción interna + optimismo obsoleto sin banner (#2) |
| 07 | medida elegante | Correcta (c=2 → 1/2); honesta sobre el cap |
| 08 | teorema 1/d | **Correcta, verificada** |
| 09 | Fibonacci bootstrap | **INSOSTENIBLE, sin banner — GRAVE (#1)** |
| 10 | reducción vectorial | Correcta |
| 11 | lema afín de Bang | Correcta; 2-dir como sub-hito |
| 12 | teorema 2 direcciones | Correcta (módulo Strassen); "RIGUROSO" algo fuerte |
| 13 | plan ataque m≥4 | Refutada (banner ok); reportes empíricos dudosos |
| 14 | nervio/KKM | Refutada (banner ok); refutación correcta |
| 15 | vía algebraica muerta | Correcta y definitiva |
| 16 | (KKT) | **Duplicado de 21 + nombre engañoso — GRAVE (#3)** |
| 17 | semialgebraica 227M | Refutada; resultado no reproducible (#7) |
| 18 | Helly | Refutada (banner ok); nombre coincide |
| 19 | entropía | Refutada (banner ok); quantifier-swap correcto |
| 20 | zonotopo | Refutada (banner ok); refutación correcta |
| 21 | KKT | Refutada (banner ok); duplicado de 16 |
| 22 | auditoría 4 props | **Excelente; refutaciones correctas** |
| 23 | conocimiento firme | **Producto más valioso**; corregido por 36/37 |
| 24 | deliverable m≥4 | Honesta; banner Hunter ok |
| 25 | teorema 3+1 simétrico | Correcta |
| 26 | teoremas A/B | Correcta (Caso 2 vía 30 §1) |
| 27 | W_k ⟺ Bang(k+1) | **Correcta (lógica pura)** |
| 28 | ataque W_3 | Honesta; banners correctos |
| 30 | tier1 reenfoque | **§1 correcta y verificada**; resto honesto |
| 31 | sandwich N_c / rigidez | **Correcta, verificada** |
| 32 | W_2 borde común | Honesta; scoping correcto |
| 33 | Bang(3) general | Conflación mediana/genérica (#4); auto-corrige grilla |
| 34 | ℓ/w verificado | **Correcta, verificada**; atribución floja del 0.928 |
| 35 | núcleo balanceado | Honesta; corrige overclaim 1F+2M |
| 36 | Bang medianas | **PROBADO, verificado** |
| 37 | familia concurrencia | Necesidad probada ✓; suficiencia solo evidencia; título sobre-vende |
| 38 | P-SCOPE + suficiencia | **Corrige #4**; scope codim-1 correcto; reducción media+var correcta; suficiencia bien delimitada |
| 39 | rigidez + pivote | Honesta y sólida; reducción de rigidez **incompleta** (omite cobertura interior); "2-dim"→3-dim |

---

## 7. Recomendaciones concretas

1. **Banner/mover `notes/09`** (peeling refutado) — única bomba sin desactivar.
2. **Banner en `notes/05` y `06`** → vía toric muerta (15/23/24).
3. **Renombrar/fusionar `notes/16`** (es KKT, dup de 21; nombre engañoso).
4. **Resolver normalización ½ vs 1 de Ambrus** o degradar el "CONFIRMED" de `notes/04`.
5. **Recuperar/re-derivar** el análisis de Ball (`scratchpad/ball_fitz.txt` perdido).
6. Para paper: el **núcleo citable** es `notes/30 §1` + `notes/36` (+ la
   caracterización necesaria de `notes/37`). "Medianas = primer caso tight
   no-faceta de Bang(3)" es limpio. El resto de `notes/` es andamiaje o refutado.

---

## 8. Resolución (2026-06-30) — estado de cada recomendación

| # | Recomendación | Estado | Acción tomada |
|---|---|---|---|
| GRAVE #1 | Banner `notes/09` (peeling) | **HECHO** | Banner `[REFUTADA — depende de peeling]` con las 3 fallas; se preserva solo la base `b_1=1/2` (=`notes/08`). |
| GRAVE #2 | Banners `notes/05`, `06` (tórica muerta) | **HECHO** | Banner en ambas → `notes/15/23-D13/24` (resultante ≡0, no-Laurent). En `06` se marca además la **contradicción interna** §3 vs §5b. |
| GRAVE #3 | Renombrar/fusionar `notes/16` | **HECHO** | `notes/16` vaciado a stub que explica el nombre engañoso y apunta a `notes/21` (ubicación canónica KKT). `notes/21` marcada canónica. |
| MEDIO #4 | Conflación mediana/genérica `notes/33 §4.2` | **HECHO** | Matiz en §4.2: el único ejemplo exacto = las 3 medianas (ON-surface), no genérico. |
| MEDIO #5 | Ambrus ½ vs 1 / "CONFIRMED" `notes/04` | **RESUELTO (fuente primaria)** | Apéndice leído verbatim → **`notes/40`**: ½ = semi-ancho (idéntico a `≥1`); reducción **probada** módulo WLOG ortogonal; objetivo = símplices dim `2d−1` (NO el triángulo). Tabla G0 y §T0.3 de `04` corregidas. |
| MENOR | Ref muerta `ball_fitz.txt` / recuperar Ball (#5) | **HECHO** | Análisis de Ball consolidado en **`notes/41`** (con fuente primaria: Lema de Bang, Th.6/12, reformulación simétrica); ref muerta en `04 §T0.2` repuntada a `notes/41`. Simetrización exacta de Ball queda `[PENDIENTE]` de re-lectura del original. |
| MEDIO #7 | `notes/17` no reproducible (227M) | **HECHO** | Banner ampliado: no existe artefacto Rust del barrido `m=4`; cifra no reproducible ⇒ no cuenta como evidencia. |
| MENOR | Script `audit_zono.py` en `notes/22` | **HECHO** | Corregido a `audit_zonotope.py`. |
| MENOR | Atribución 0.928 (`notes/34/35`) | **HECHO** | Reetiquetado: consecuencia del **Lema 5** de B-Y (no "Teorema 8", que es 0.828). |
| MENOR | `notes/12` "RIGUROSO" | **HECHO** | Rigor acotado "módulo paso citable"; existencia del acoplamiento citada a **Gardner 1988** (fuente primaria `notes/40 §4`), no a numérica. |
| MENOR | Título `notes/37` sobre-vende | **HECHO** | Título → "caracterización necesaria"; suficiencia marcada `[OPEN]`. |

**Nuevas notas creadas:** `notes/40` (reducción de Ambrus, fuente primaria) y `notes/41`
(análisis de Ball recuperado). Ambas aportan citas de fuente primaria reutilizables para el
paper (Gardner [12] = obstrucción de medida única; Alexander/Conj.11 = `1/(n+1)`; Lema de Bang
forma Fenchel).

**Pendiente NO cerrado aquí** (queda como trabajo, no higiene): el matiz de auditoría sobre
`notes/39 §1` (la reducción de rigidez omite la cobertura interior y el "2-dim" debe ser 3-dim)
— es contenido matemático abierto, no una nota a desactivar.

---

## 8. Adenda 2026-06-30 (tarde) — notas 38 y 39

Verificado por cómputo: `cond(triple C)=2.02227` (nota 38 dice 2.0223 ✓);
"triangular automática para `cond≈2`, `a>0`" reproducido (517 testeadas, 0
violaciones; nota afirma 373/0). **Los números de 38/39 son confiables.**

- **`notes/38` y `notes/39` son de calidad alta e incorporan esta auditoría:**
  corrigen el Hallazgo #4 (banner en 33), el "surface=tight REFUTADA"→`OPEN`, y
  `Σa_i=2` como suma **con signo** (no `Σ|a_i|`). El scope "transporte = rebanada
  codim-1, insuficiente para Bang(3) general" es **correcto** (se apoya en la
  necesidad probada de `notes/37 §2`). El pivote a P-B / certificado combinatorio
  es estratégicamente sólido.
- **Objeciones nuevas (menores, no invalidan nada):**
  1. `notes/39 §1.2` — la reducción de rigidez a "un CSP finito 1-D sobre las 3
     aristas" **omite la cobertura del interior** (condición 2-D); las 3 ecuaciones
     de partición son *necesarias* pero el sistema reducido está incompleto.
  2. `notes/39 §1.2` — el espacio de soluciones de longitud es **3-dim** (6
     incógnitas − 3 ecuaciones de rango 3), no "2-dim".
  3. `notes/39 §1.1` — "exactamente UNA teselación" es un resultado de grilla `/24`
     ⇒ solo "exactamente una *grid-aligned*"; la unicidad continua sigue abierta.
  4. `notes/38/39 §2` — la suficiencia se reduce bien a media+varianza, pero el
     hueco real es doble: (a) uniformidad *plena* de `S` (momentos ≥3) **y** (b) el
     soporte sobre `Φ(Δ)` con signo mixto de `a`; la reducción media+var solo cubre
     el régimen `a>0`. Bien etiquetado como `[OPEN, moonshot]`.
- **Veredicto:** trabajo honesto y correcto; el aporte firme/citable no cambia
  (`notes/36` medianas + necesidad de `notes/37`). La dirección de trabajo y las
  tareas asignadas están en **`auditorias/39-rigidez-suficiencia-pivote.md`**.
