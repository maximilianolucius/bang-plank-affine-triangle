# Órdenes de trabajo — RONDA 9 (un solo paper: pasada de precisión de Rosa + expansión del defecto de transporte)
> Jefe de research: Claude. Fecha: 2026-07-03. Ejecuta el investigador.
> **Decisión del usuario (2026-07-03):** NO partir el paper. Se mantiene un manuscrito único,
> se aplican TODOS los puntos aceptados de la 4ª pasada de doña Rosa (`auditorias/55`) salvo el
> split, y se EXPANDE la dirección del defecto de transporte con las tareas #1, #3, #2 de
> `auditorias/55 §expansión`.
>
> **Encuadre estructural (obligatorio, es la respuesta a Rosa sin partir):** promover `D(u)`
> de sección tardía a **columna vertebral** del paper. Medianas, triples cíclicos, facetas y la
> caracterización son *casos/valores especiales de `D(u)`* (`D=1` en concurrencia, `D=3/2` en
> facetas, `D≤2` siempre, `≤d` en `Δ^d`). Con `D(u)` como marco desde la introducción, el paper
> es UNA teoría con casos sharp, no "tres papers pegados". La expansión (Parte B) debe colgar
> de ese marco; expandir §8 SIN el marco de dualidad empeora la crítica de sobredimensión — la
> secuencia importa.
>
> Reglas vigentes: aritmética exacta (nunca grilla como prueba); `[PROVED]/[EVIDENCE]/[OPEN]`
> por afirmación; todo enunciado del `.tex` probado o citado; scripts load-bearing a
> `experiments/` con protocolo de reproducibilidad.

═══════════════════════════════════════════════════════════════════════
# PARTE A — Los puntos aceptados de doña Rosa (pasada de precisión, un solo paper)
═══════════════════════════════════════════════════════════════════════

## R9-A1 (bloqueante ya) — dos fixes técnicos concretos
a. **Overclaim de §7 (l.916):** "D(u) is computable to certified precision by exact LP over
   skeleton measures" es FALSO — el LP esquelético da solo **cota superior**; `D(u)` es un
   ínfimo sobre TODAS las medidas de `P(Δ)`. Reformular a: cotas superiores LP-computables +
   cota inferior de momentos (Prop 7.3) ⟹ **sandwich** de `D(u)`. (Queda subsumido/mejorado
   por R9-B1: la dualidad da la cota inferior certificada real.)
b. **Notación de masas (footgun):** fijar UNA vez la convención `α↦BC, β↦CA, γ↦AB`
   (`α=1−2p_A=w_BC`, etc.) y usarla en Thm 6.3/6.6 y §7. Hoy l.510 llama a `α,β,γ`
   "edge masses" sin decir de qué arista es cada una.

## R9-A2 — abstract y control de claims
- Abstract a **una sola tesis** (150–200 palabras): "para tres direcciones en el triángulo,
  caracterizamos cuándo existe medida testigo de marginal uniforme, y de ahí probamos familias
  sharp de coberturas; el marco es el defecto de transporte `D(u)`." Todo lo demás → resultados
  secundarios en el cuerpo, NO en la lista del abstract.
- **Cor 7.7 fuera del abstract como "resultado principal":** presentarla sobria — "en este
  entorno restringido de ternas, la cota de transporte supera el valor numérico de la constante
  general de B-Y", explicitando que B-Y es uniforme y esto es local. Es consecuencia local de
  método, no mejora del SOTA global.
- **"Settle Gardner" quirúrgico:** "we settle Gardner's finite-direction relative-width-measure
  question **only for three directions on a triangle**".
- Claims de prioridad: "we are not aware of a previous…" (ya en §5; barrer el resto).

## R9-A3 — jerarquía y terminología
- **Jerarquía explícita** de resultados: principal (caracterización + familias sharp) /
  herramientas (transporte, Apéndice A) / ilustrativos (Thm 4.1 "3 facetas+1") / extensiones
  (§8). Thm 4.1 NO al mismo nivel que 6.6/6.8.
- **Definir formalmente al inicio** "witness measure" (medida de probabilidad con
  `u_{i#}μ=Leb[0,1]`) y "direction" (forma afín normalizada `u:K→[0,1]` onto; fijar que NO es
  la normal euclídea). "Cyclic triple" con definición exacta + remitir a la figura.

## R9-A4 — rigor de las pruebas centrales (exposición; las pruebas ya están verificadas)
- **Thm 6.6:** partir en lemas nombrados — (i) cobertura (el Step 2 como lema topológico, con
  los casos de vértice/multiconstraint explícitos), (ii) unicidad, (iii) testigos `x*,y*` con
  las **desigualdades de positividad escritas EN EL TEXTO** (son productos de factores
  elementales positivos: `α,β,γ>0`, `1−α=β+γ>0`, `2−2α−β=β+2γ>0`, etc.), no en script.
- **Apéndice A:** (i) grupo de simetría explícito (orden 6: rotación `⟨Q⟩₃` × reflexión∘flip
  `⟨S⟩₂`, acción sobre pares (problema `τ`, solución) y por qué preserva el enunciado ∀`τ`);
  (ii) **O2 airtight para tilings CERRADOS** — escribir por qué una traza degenerada (interior
  vacío) ni cubre ni estorba ⟹ no se pierde ninguna solución cerrada (la preocupación de Rosa
  sobre endpoints); (iii) LMR expandido con subcasos truncado/no-truncado y **figura** (ya hay
  Fig. de tiling; añadir la de LMR si ayuda).
- **Thm 3.2:** aislar el lema de sumsets como enunciado separado ("si `C_1,…,C_{d+1}⊂[0,1]`
  tienen medida suficiente entonces `1∈ΣC_k`"), probarlo una vez, aplicarlo. El arreglo
  abierto/compacto (recorte con `η=(1−R)/(d+2)`) ya es correcto; solo extraer el lema.

## R9-A5 — §8 se QUEDA pero con introducción propia
Rosa pidió sacar §8; el usuario decidió mantenerlo y expandirlo (Parte B). Condición: §8 con
**motivación e introducción propias** (no aparece en el abstract como resultado principal), y
colgando del marco `D_d(u)` (R9-B2). El `d≥4` (¿revive con valores interiores distintos, o la
masa sube a 2-caras?) como problema abierto de esa sección.

## R9-A6 — reproducibilidad y metadatos
- **Protocolo de scripts ancillary:** por cada script — nombre, versión/hash, inputs/outputs,
  qué verifica, **qué parte de qué prueba depende de él**, y por qué no hay pérdida de casos.
  Dejar claro que el paper NO es computer-assisted: los scripts son verificación secundaria
  (las pruebas están en el texto/Apéndice A).
- MSC 2020 + keywords; Ambrus con URL Rényi verificable (está en `notes/40`).
- Bloque de autor: **pendiente — decisión del usuario (identidad real); no lo cierra el
  investigador.** Dejar el placeholder marcado.

═══════════════════════════════════════════════════════════════════════
# PARTE B — Expansión del defecto de transporte (tareas #1, #3, #2; en ese orden)
═══════════════════════════════════════════════════════════════════════
Objetivo: que §7–§8 dejen de ser "agregado" y se vuelvan la segunda columna coherente del
paper. **La secuencia es obligatoria: primero el marco (B1, B2), luego el resultado nuevo (B3).**

## R9-B1 (#1, PRIORIDAD) — dualidad de `D(u)`
Convertir §7 en teoría con backbone dual. Deliverable: teorema de dualidad fuerte + optimizador.

- **Reformulación de arranque (probar equivalencia):**
  `D(u)=inf\{D:\ ∃μ∈P(Δ),\ ∃ρ_i≥0\text{ en }[0,1]\text{ con } u_{i#}μ+ρ_i=D·\mathrm{Leb}\}`
  (masa: `1+|ρ_i|=D` ⟹ `|ρ_i|=D−1`). Es una feasibility de transporte: "rellenar" cada
  marginal hasta `D·Leb` con holgura `ρ_i`.
- **Candidato de dual (probar dualidad fuerte, es el núcleo de la tarea):**
  `D(u)=\sup\{\ \min_{x∈Δ}\sum_i ψ_i(u_i(x))\ :\ ψ_i≥0\text{ en }[0,1],\ \sum_i∫_0^1ψ_i=1\ \}`.
  Ruta: minimax de Sion (el conjunto de `μ` es convexo y débil-* compacto; el objetivo es
  convexo lsc). **Verificaciones de sanidad obligatorias:** (a) `ψ_1≡1`, resto `0` ⟹ da `D≥1`;
  (b) recuperar la cota de momentos de Prop 7.3 con una elección explícita de `ψ_i`;
  (c) exhibir el `ψ_i` dual que certifica `D(facetas)=3/2` (matchear la construcción primal del
  triángulo inscrito de Thm 7.4).
- **Optimizador:** por holgura complementaria, decir dónde se concentra el `μ` óptimo y dónde
  el dual `ψ_i` "cobra"; en particular, **cuándo el óptimo vive en el esqueleto y cuándo NO**
  (esto es lo que convierte el "sandwich" de Rem 7.9 en afirmación con contenido, y liquida el
  overclaim de R9-A1a: el LP esquelético es exacto ⟺ el optimizador es esquelético).
- **Entregable:** Teorema de dualidad de `D(u)` + corolario "cotas inf certificadas por el
  dual". **Riesgo:** medio. **Valor:** alto — es lo que Rosa pidió y lo que hace madura a §7.

## R9-B2 (#3) — `D(u)` para cuerpos convexos generales (el reencuadre unificador)
- Definir `D_K(u_1,…,u_n)` para `K` convexo arbitrario (mismo ínfimo). Probar el bound general
  `Σrw ≥ 1/D_K(u)` para toda cobertura por planks en esas direcciones (la Prop 7.2(ii) ya es
  esto; enunciarla para `K` general).
- Observar que el Thm 2.1 es exactamente `D_K(u)≤d` para toda dirección en cualquier `K` (pico
  de la marginal por BM). Así el `1/d` y el transporte son **el mismo objeto**.
- **Reencuadre del paper:** presentar `D_K` como el **motor general** en §1–§2, y los
  resultados del triángulo como sus **especializaciones sharp**. Esto es lo que hace que el
  paper se lea como una teoría, no como triángulo + agregados. **Riesgo:** bajo (es
  reencuadre + un par de enunciados generales). **Valor:** alto en coherencia — responde
  directamente la queja estructural de Rosa sin partir.

## R9-B3 (#2) — `sup_u D(u)=3/2`: ¿son las facetas el peor caso?
- **Pregunta exacta:** ¿es `3/2` el máximo de `D(u)` sobre TODAS las ternas no paralelas dos a
  dos en el triángulo? Sub-preguntas: (a) ¿`δ(u)≤1/6` siempre? (lado momentos); (b) ¿`D(u)≤3/2`
  siempre? (necesita construir, para una terna arbitraria, una medida con las 3 marginales
  `≤(3/2)Leb`).
- **Si SÍ:** teorema **`Σrw≥2/3` para tres direcciones cualesquiera en el triángulo** —
  primer bound de transporte universal para 3 direcciones. Honestidad obligatoria en el texto:
  `2/3<4√3−6≈0.928`, así que NO bate B-Y globalmente; el valor es **estructural** (las facetas
  son el peor caso del transporte) y generalizable en dimensión (`D_d(facetas)=(d+1)/2`
  conjetural, R9-A5/B2). Con B-1 el dual debería dar la cota inferior; la superior es la
  construcción.
- **Si NO** (existe terna con `D>3/2`): también publicable — "hay ternas peores que las facetas
  para el transporte", y localiza dónde. Exhibir la terna exacta.
- **Regla:** exacto/racional; la grilla no decide (lección `notes/33`). **Riesgo:** medio-alto
  (la cota superior universal es lo difícil). **Valor:** alto — cierra la estructura global de
  `D` y da el bound universal.

## R9-B4 (afilado, opcional tras B1) — la región completa que bate B-Y
Con el optimizador de B1, caracterizar el conjunto abierto `{u : D(u)<1/(4√3−6)≈1.0776}` —
mucho mayor que la caja `1/60` de la Cor 7.7 actual. Convierte "un ejemplo" en "un abierto
explícito donde superamos el valor de B-Y". Baja dificultad una vez hecho B1.

═══════════════════════════════════════════════════════════════════════
# Secuencia y prioridad
═══════════════════════════════════════════════════════════════════════
1. **R9-A1** (los 2 fixes técnicos — ya, son literalmente falso/ambiguo).
2. **R9-B1 → R9-B2** (marco: dualidad + cuerpos generales — PRIMERO el marco, es lo que
   cohere el paper y lo que evita que la expansión empeore la sobredimensión).
3. **R9-A2..A6** (pasada de precisión de Rosa — abstract, jerarquía, terminología, rigor de
   6.6/App A, metadatos) — en paralelo con B, pueden ir intercaladas.
4. **R9-B3** (sup D=3/2, el resultado nuevo con gancho) tras el marco.
5. **R9-B4** afilado; luego **R9-A-entrega**.

## R9-entrega — 5ª pasada de doña Rosa
Cuando A + B1/B2/B3 estén hechas: entregar el manuscrito único reestructurado con el mapa
objeción→resolución de la pasada 4, señalando (i) que NO se partió pero (ii) `D(u)` es ahora
el marco unificador (su queja de "tres papers" respondida por coherencia), y (iii) §7 tiene
dualidad (su queja de inmadurez respondida). Pedir foco en la dualidad y en `sup D=3/2`.

**Mensaje al investigador:** el usuario decidió no partir el paper y en cambio **profundizar**
el defecto de transporte. Eso solo funciona si `D(u)` se vuelve la columna vertebral: haz
primero el marco (dualidad B1 + cuerpos generales B2), y recién entonces cuelga los resultados
nuevos (sup D=3/2 B3, región B4). Si expandes §8/§7 sin el marco, le das la razón a Rosa sobre
la sobredimensión. Todas las correcciones de la Parte A son de exposición/precisión sobre
matemática ya verificada — ninguna prueba está rota; se trata de escribirlas al estándar de su
ambición. Corrige R9-A1 sin discutir (son un overclaim y una ambigüedad reales).
