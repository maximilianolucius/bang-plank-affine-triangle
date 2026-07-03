# Dictamen sobre la 4ª pasada de doña Rosa ("Reject, resubmit after restructuring") + decisión estratégica: PARTIR EL PAPER
> Jefe de research: Claude. Fecha: 2026-07-03.
> Insumo: 4ª auditoría externa de doña Rosa, sobre la copia congelada `pasada4` (17 pp, con
> §7–§8 por primera vez).
> Método: cotejo de cada uno de sus 13 puntos contra el `.tex` vivo; verificación de los dos
> puntos técnicos concretos que plantea.

---

## Lectura de conjunto: su crítica de FONDO es correcta. Recomiendo aceptar el split.

Esta es la auditoría de más valor que hemos recibido, y cambia de naturaleza respecto de las
tres anteriores: ya no señala frases, señala la **arquitectura**. Su tesis —"hay tres papers
compitiendo dentro de un PDF"— es **acertada**, y es la conclusión natural de un manuscrito
que creció por acreción (R6 añadió familia cíclica + caracterización; R7 añadió §7 defecto de
transporte —un objeto variacional nuevo— y §8 Δ³). Cuando un referee externo de calidad
insiste **tres pasadas seguidas** en la misma enfermedad ("promete más de lo que prueba /
está sobredimensionado"), la respuesta correcta deja de ser parchear y pasa a ser
reestructurar. **Recomiendo partir el paper.**

## PERO: calibración honesta del "Reject" — ninguna matemática está mal

Debo ser preciso, porque "Reject" suena a que algo está roto y **no lo está**:

- **Ningún resultado ha sido refutado.** Cada identidad load-bearing está verificada por mí,
  de forma independiente, a lo largo de las rondas 5–8 (perímetro ponderado; Thm 6.6 cobertura
  + unicidad; Thm 6.8 tricotomía 216/216; Apéndice A las 7 órbitas; §7 `D(facetas)=3/2`,
  Cor 7.7 `40401>40368`; §8 `a(σ),b(σ)`). La matemática es sólida.
- Lo que Rosa llama "pruebas frágiles" en Thm 6.6 Step 2 y Apéndice A **las auditué línea a
  línea** (rondas 6 y 8) y son **correctas**. Su objeción es de **estándar de exposición**
  (cada paso debería ser un lema nombrado, sin álgebra escondida en scripts), no de validez.
  Es una distinción importante: no vamos a arreglar pruebas rotas, vamos a **escribir pruebas
  correctas de forma más limpia**.
- Por tanto el contenido accionable de su "Reject" es: **(a) partir el paper, (b) endurecer
  la exposición de 6.6/App A, (c) un overclaim real en §7, (d) podar abstract/claims.** Es
  una reestructuración, no una re-derivación. En la práctica es "major revision" con nombre
  severo — y el nombre severo está justificado por la escala del reordenamiento, no por
  errores matemáticos.

## Los dos puntos técnicos concretos — VERIFICADOS, ambos válidos

1. **Overclaim real en §7 (su punto 6):** l.916 dice *"D(u) is computable to certified
   precision by exact linear programming over skeleton measures."* **Es un overclaim.**
   `D(u)` es un ínfimo sobre TODAS las medidas de probabilidad en Δ; el LP sobre medidas
   esqueléticas da solo una **cota superior**. La "certified precision" viene del **sandwich**
   (cota inferior de momentos, Prop 7.3, + cota superior esquelética), no de que el LP calcule
   `D(u)`. **Debe reformularse:** "upper bounds on `D(u)` are LP-computable over skeleton
   measures; with the moment lower bound this sandwiches `D(u)`" — exactamente la forma en que
   se usó en Rem 7.9. Este es el tipo de frase que yo debí marcar en R7 y no lo hice.
2. **Footgun de notación (su punto 12):** l.510 llama a `α=1−2p_A, β=1−2p_B, γ=1−2p_C` "the
   edge masses of `μ_p`", pero `α` es la masa de la arista **BC** (`w_BC`), no de AB (l.731:
   "masses `(γ,α,β)` on `(AB,BC,CA)`"). La asignación está escrita en un sitio pero el rótulo
   "edge masses" en Thm 6.6 es ambiguo y es fuente de error. **Fijar la convención una vez**
   (α↦BC, β↦CA, γ↦AB) y usarla consistentemente. Real, aunque menor.

## Cotejo de sus 13 puntos

| # | Punto | Dictamen |
|---|---|---|
| 1 | Sobredimensionado; 3 papers en uno | **ACEPTO — es la decisión central (split).** |
| 2 | Abstract inaceptable, una sola tesis | **ACEPTO.** Reducir a 150–200 palabras, 1 tesis. |
| 3 | "Settling Gardner" demasiado amplio | **ACEPTO (quirúrgico):** "only for three directions on a triangle". |
| 4 | Thm 6.6 Step 2 no está a nivel de prueba central | **ACEPTO como exposición** (prueba correcta, verificada; partir en lemas: cobertura / unicidad / testigos; positividad al texto). |
| 5 | Apéndice A insuficiente; trazas degeneradas y tilings cerrados | **ACEPTO como exposición.** Su preocupación fina (endpoints en tilings cerrados) la revisé: O2 es correcto (traza degenerada = interior vacío ⟹ ni cubre ni estorba ⟹ no pierde solución cerrada), pero **debe escribirse airtight**, no dejar que el lector lo reconstruya. Grupo de simetría explícito. |
| 6 | §7 inmadura; falta dualidad; "computable by LP" | **ACEPTO.** El overclaim (arriba) se corrige ya. La dualidad de `D(u)` es trabajo real: si §7 se queda, necesita el LP dual y la caracterización del optimizador. **Argumento fuerte para mover §7 a su propio paper**, donde se hace bien. |
| 7 | Comparación con `4√3−6` demasiado intensa | **ACEPTO.** Bajarla de tono; fuera del abstract como "resultado principal"; es consecuencia local de método. |
| 8 | §8 (Δ³) prematura | **ACEPTO.** No sostiene los teoremas del triángulo; a "Further directions" o al 2º paper. |
| 9 | Normalizer obstruction = observación | **PARCIAL.** Ya está partida (Prop 9.1 hecho + Rem 9.2 interpretación); su objeción está casi satisfecha. Va con §7 al 2º paper. |
| 10 | Thm 3.2 "artesanal"; aislar lema de sumsets | **ACEPTO (menor).** El arreglo abierto/compacto es correcto (verificado R8); extraer el lema de Minkowski como enunciado separado. |
| 11 | Jerarquía de resultados difusa (Thm 4.1 al mismo nivel) | **ACEPTO.** El split + una intro con jerarquía clara lo resuelve. |
| 12 | Terminología ("witness measure", "direction") + masas α/β/γ | **ACEPTO.** Definir formalmente al inicio; fijar convención de masas (arriba). |
| 13 | Señales de borrador ([AUTHOR NAMES], protocolo de scripts) | **ACEPTO.** Autor = pendiente (identidad real); protocolo de reproducibilidad para ancillary. |

Lo que ella **rescata** (separación de niveles a–e; Thm 6.3 perímetro ponderado; Thm 6.8
caracterización; Thm 7.4 `D=3/2`) coincide con mi valoración. No hay divergencia de fondo.

═══════════════════════════════════════════════════════════════════════
# DECISIÓN ESTRATÉGICA (recomendada; requiere OK del usuario — es un cambio de alcance)
═══════════════════════════════════════════════════════════════════════

**Partir en dos manuscritos:**

- **Paper 1 — "Uniform-marginal witness measures and sharp cyclic triples for the affine
  plank problem on the triangle"** (el publicable ya). Núcleo:
  §1 modelo + niveles a–e; Thm 2.1 (1/d, uniforme); Thm 3.1 (2 direcciones); Thm 3.2
  (faceta-paralelo, con lema de sumsets aislado); Thm 4.1 (3 facetas+1, como caso
  ilustrativo); §5 medianas + rigidez; §6 perímetro ponderado (6.3) + rigidez de familia
  (6.6) + caracterización (6.8) + Cor iff; **Apéndice A reescrito como prueba autoportante**.
  Todo verificado; con el endurecimiento de 6.6/App A queda referee-clean y **enfocado**.
- **Paper 2 — "The transport defect for plank coverings"** (necesita más trabajo). Núcleo:
  §7 `D(u)` **con dualidad LP** (el dual, el optimizador, cuándo el esqueleto es exacto),
  `D(facetas)=3/2`, estabilidad + Cor 7.7 (cota local más allá de B-Y, con su caveat), §8 Δ³,
  y la normalizer obstruction. Es donde vive el resultado más novedoso (Cor 7.7); darle paper
  propio le da el espacio que Rosa —con razón— dice que necesita.

**Por qué es la decisión correcta y no una derrota:** el split **elimina de un golpe la
crítica estructural más fuerte**, convierte el Paper 1 en el deliverable enfocado que
buscábamos desde el principio (todos sus resultados ya verificados), y libera al defecto de
transporte para desarrollarse con dualidad en vez de quedar aplastado como "agregado". Es
consolidación, no pérdida: 0 resultados se tiran.

**Alternativa (si el usuario prefiere un solo paper):** mantener unificado pero degradar §7–§8
a una sección breve "Further directions" (sin la teoría de `D(u)`, solo enunciados + cita a
un futuro paper), podar el abstract a la tesis única, y endurecer 6.6/App A. Peor opción: deja
el resultado más interesante (Cor 7.7) como nota de pasada y no responde del todo la objeción
de sobredimensión.

═══════════════════════════════════════════════════════════════════════
# ÓRDENES RONDA 9 (recomendadas — condicionadas a confirmar el split)
═══════════════════════════════════════════════════════════════════════
Si se confirma el split:

## R9-1 (Paper 1, cierre) — extraer y enfocar el núcleo del triángulo
Sacar §7, §8 y la normalizer obstruction a un `paper2/` aparte. Paper 1 = los resultados del
triángulo. Abstract nuevo (1 tesis, 150–200 palabras). Jerarquía explícita (principal /
herramientas / ilustrativos).

## R9-2 (Paper 1, rigor) — endurecer 6.6 y Apéndice A a estándar de prueba central
- Thm 6.6: lemas separados (cobertura Step 2 como lema topológico con casos de vértice
  explícitos; unicidad; testigos `x*,y*` con las desigualdades de positividad EN EL TEXTO).
- Apéndice A: grupo de simetría explícito (orden 6, generadores, acción sobre pares
  (τ, solución)); O2 escrito airtight para tilings cerrados; LMR con subcasos y figura.
- Thm 3.2: lema de sumsets aislado y probado una vez.
- Definir "witness measure" y "direction" al inicio; fijar convención α↦BC/β↦CA/γ↦AB.
- Thm 6.8: "settle Gardner **only for three directions on the triangle**".

## R9-3 (Paper 2, research) — hacer el defecto de transporte un paper de verdad
- **Dualidad de `D(u)`:** enunciar el LP dual (problema de momentos / cobertura fraccional),
  probar dualidad fuerte, y decir cuándo el óptimo vive en el esqueleto (y cuándo NO).
  Corregir YA el overclaim "computable by LP" → sandwich (cota inf de momentos + sup
  esquelética).
- §8 Δ³ con introducción y motivación propias; d≥4 (¿revive con valores interiores
  distintos, o la masa sube a 2-caras?) como problema abierto de ese paper.
- Cor 7.7 con su caveat, pero ahora como resultado central del Paper 2, no nota de pasada.

## R9-4 (ambos) — reproducibilidad y metadatos
Protocolo de scripts ancillary (nombre/versión/inputs/outputs/qué prueba/qué parte depende);
MSC + keywords; Ambrus con URL; bloque de autor (decisión del usuario).

## R9-5 — 5ª pasada de Rosa sobre el PAPER 1 solo, cuando R9-1/R9-2 estén hechos.

---

## Prioridad
1. **Decisión del usuario: split (recomendado) o unificado-con-poda.**
2. Si split: **R9-1 + R9-2** (Paper 1 al frente, es el que se publica primero).
3. R9-3 (Paper 2) en paralelo o después.
4. R9-4, R9-5.

**Mensaje honesto al usuario:** Rosa tiene razón en lo estructural y su nivel es exactamente
el que queremos. "Reject" asusta pero traducido es "reestructurar", no "está mal": toda la
matemática está verificada. La jugada correcta es partir el paper — el Paper 1 (triángulo) es
publicable ya con endurecimiento de exposición, y el Paper 2 (defecto de transporte) es donde
vive lo más nuevo y merece desarrollarse con dualidad. Es una decisión de alcance; la pongo en
tus manos antes de que el investigador ejecute.
