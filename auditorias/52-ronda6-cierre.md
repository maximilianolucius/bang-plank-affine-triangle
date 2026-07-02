# Auditoría Ronda 6 — Thm 6.6 (tightness+rigidez de familia), Thm 6.8 (caracterización 3 direcciones), Apéndice A, fixes de referee + Órdenes Ronda 7 revisadas
> Auditor / Jefe de research: Claude. Fecha: 2026-07-02.
> Alcance: `notes/50-R6-1-R6-2`, `notes/50-R6-4`, `notes/50-R6-5`; el `.tex` completo (11 pp).
> Método: verificación a mano de todas las identidades load-bearing; revisión línea a línea
> del Apéndice A y del Paso 2 de Thm 6.6; ejecución de los 3 scripts nuevos; cotejo de los
> 6 fixes contra el texto.

---

## Veredicto: la mejor ronda del proyecto. TODO CONFIRMADO.

Los dos teoremas nuevos convierten el paper en una historia **cerrada** para 3 direcciones
en el triángulo: caracterización iff (existencia de medida ⟺ concurrencia) + familia
2-paramétrica sharp con cobertura tight explícita y **única** + reducción exacta del caso
abierto de Bang a ternas no concurrentes. Ninguna objeción bloqueante.

## 1. Thm 6.6 (tightness y rigidez de la familia cíclica) — [PROVED] CONFIRMADO

Verificaciones mías, independientes de los scripts:

- **A mano:** `Λ(A)=αγ+β(α+γ)=S`, `Λ(B)`, `Λ(C)` ✓; `Σaᵢ=1−Σα²=2S` ✓;
  `Σaᵢlᵢ=(Σα²β²+αβγ)/S=S−αβγ/S` y `Σaᵢhᵢ=S+αβγ/S` (expansión completa, usando
  `S²=Σα²β²+2αβγ`) ✓; consistencia del testigo: `Σaᵢ(λᵢ+δ)=S−αβγ/S+2S·αβγ/(2S²)=S` ✓;
  en el ejemplo `p=(9/20,3/10,1/4)`: `λ₁=5/29`, `ρ₁=25/29` = las fórmulas cerradas de A.1
  Y los endpoints de `I₁` — la sustitución `(l,h)=(λ,ρ)` cuadra ✓.
- **Lógica del Paso 2 (cobertura), revisada paso a paso:** finitud de
  `closure(P_σ)∩∂Δ` (≤9 puntos: contacto ⟹ `u_j=c_j` exacto, `u_j` no constante en cada
  arista) ✓; `H_σ⊂Δ̄` por el argumento del disco (segmentos por `y` fijo con punto de cruce
  común ⟹ `z` colineales ⟹ un disco da infinitos cruces) ✓; no-paralelismo: verifiqué
  independientemente que `u_i∥u_j ⟺ τ_i(1−τ_j)=1`-tipo (mi derivación `τ₁=1+τ₁τ₂` es la
  misma ecuación reordenada), imposible en `(0,1)³` ✓; concurrente ⟹ cono abierto ⟹ vacío
  por acotación ✓; no concurrente ⟹ triángulo de vértices `v_ij`, patrones **mixtos**
  fuerzan `S=Σa_mc_m` ⟹ `u_k(v_ij)=c_k` ⟹ concurrencia excluida, patrones **puros**
  chocan con el margen `±αβγ/S` ✓. El mecanismo margen-exacto-`αβγ` es genuinamente
  elegante.
- **Paso 3 (unicidad):** partición μ_p-a.e. ⟹ tiling cerrado real (complemento abierto de
  medida 0 = vacío) ✓; A.1 da los 3 candidatos; testigos `x*`, `y*` con coordenadas
  positivas (simbólico del script + fórmulas mostradas) ✓; degeneración al centroide de
  `notes/45` en `α=β=γ=⅓` ✓ (consistencia perfecta).
- **Script (`cyclic_family_tight_rigidity.py`), corrido:** simbólico OK; clipping racional
  exacto en 5 puntos (incl. casi-degenerados): área no cubierta MMM = **0**, LLL/RRR
  `1/6, 100/841, 20/169, 4900/38809, 13600/720801` — positivas todas ✓.

**Corrección a mi propia dirección (obligado decirlo):** mi orden R6-4 decía "la evidencia
ya apunta a que NO se alcanza". Estaba **equivocado**, y el error fue mío por citar la
grilla de `notes/38` como evidencia direccional — la misma trampa de `notes/33` que yo
mismo convertí en regla. La grilla no contenía los endpoints `k/29`. El investigador hizo
exactamente lo correcto: dejó que lo exacto decidiera. Lección endurecida: la grilla no es
evidencia ni siquiera para ORIENTAR una apuesta; solo el cómputo exacto orienta.

## 2. Thm 6.8 (caracterización de 3 direcciones) — [PROVED] CONFIRMADO

- **Caso dos-compartidas:** lo rederivé independientemente antes de leer la prueba y
  obtuve lo mismo: tras flip `u_i−u_j=(τ_i−τ_j)x_v`, mid-lines se cortan solo en el punto
  medio de `e`, donde la tercera vale `τ_k/2` o `(1+τ_k)/2 ≠ ½` (τ_k∈(0,1)) ⟹ nunca
  concurren; y `E[u_i]=E[u_j]=½ ⟹ E[x_v]=0 ⟹ supp μ⊂e` donde `u_k` no es onto ⟹ tampoco
  medida. Clase vacía en ambos lados del iff ✓.
- **Caso tres-compartidas:** uniforme en la arista empuja a `Leb[0,1]` por las 3 ✓; cota por
  cubrir la arista sola (1-D) ✓; concurrencia en el punto medio ✓.
- **Caso aristas distintas = cíclico módulo flips:** el argumento de orientación es
  correcto (asignar por arista llena + flips) ✓; interioridad automática vía Cor 6.4.
- **Cor 6.4 (interioridad automática):** verificado A MANO: resolví `Vp=½1` y obtuve
  exactamente `2(1+τ₁τ₂τ₃)p_A=1−τ₃(1−τ₂)>0`, y `p_A<½ ⟺ τ₂(1−τ₁)<1` automático;
  `½−p_C=τ₁p_A>0` ✓. Ojo: `Σp*=1` NO es automático — la concurrencia real sigue siendo
  codim-1 en τ (lo comprobé numéricamente: τ=(0.3,0.7,0.4) da `Σp*≈1.019`) — el enunciado
  del corolario lo maneja bien (pide concurrencia en el plano de Δ). ✓
- **Script (216/216):** corrido. Las clases 2-compartidas solo tienen "raíces" en
  `τ_j+τ_k=1` = las dos direcciones son flip una de otra (paralelas) — excluidas por la
  hipótesis pairwise non-parallel, que está en el enunciado ✓. `det V=0` inconsistente en
  las 18 restantes ✓. Clase distinta-arista: condición de concurrencia = superficie
  2-paramétrica ✓.
- La hipótesis "pairwise non-parallel" es necesaria y está bien puesta. La nota sobre las
  453 ternas del LP (moot) es correcta.

## 3. Apéndice A / Prop A.1 — [PROVED] CONFIRMADO (revisión de referee completa)

- **Tabla de trazas** verificada contra los valores de vértice en las 3 aristas
  (roles `(c,f,g)=(1,2,3)/(3,1,2)/(2,3,1)` ✓); fórmulas de inversión y condiciones de
  no-degeneración ✓. (O1)/(O2) correctas (unión cerrada de medida llena = `[0,1]`) ✓.
- **Órbitas recontadas a mano:** acción de orden 6 (rotación + reflexión∘flip
  `(X₁,X₂,X₃)↦(X̄₁,X̄₃,X̄₂)` con `L↔R`); tamaños `1+2+6+6+6+3+3=27` ✓ — la reducción a 7
  representantes es exhaustiva.
- **MMM:** sistemas cíclicos desacoplados, pendiente compuesta `−1/(τ₁τ₂τ₃)≠1` ⟹ punto
  fijo único; verifiqué la sustitución `1−λ₁/τ₁=λ₂` a mano ✓; cadena
  `0<λᵢ<τᵢ<ρᵢ<1` automática ✓ (spot-checks numéricos en casos extremos).
- **LLL/RRR:** forzado `l≡0` + mismo sistema cíclico ⟹ `h=λ` ✓; RRR por la simetría ✓.
- **Los 5 casos imposibles:** revisados uno a uno; todos correctos. El único punto que
  requirió doble lectura es LMR ("of positive length, so `l₂>0`"): la justificación
  correcta —y la que el texto usa— es que `T₃` tiene longitud positiva porque `I₃` tiene
  ancho positivo y el mapa es no degenerado (`h₃=1, l₃<1 ⟺ l₂>0`); sólido.
- **Crosscheck script:** 3 soluciones exactas en `τ=(½,½,½)` ✓ (y `(½,⅔,⅓)` según nota).
- El Lemma 5.2 ahora es el caso `τ=½` de un resultado más general **probado a mano** —
  exactamente la opción (a) que pedía doña Rosa, y mejor de lo pedido.

## 4. R6-1 — los 6 fixes verificados contra el texto

Todos aplicados tal como se ordenaron: abstract + Thm 2.1 (sharpness per-plank, `d≥2`,
frase explícita "does NOT assert any covering…" + referencia a Thm 3.2); modelo con WLOG
`I⊂[0,1]`; Thm 3.1 con hipótesis non-parallel + caso paralelo despachado en el enunciado +
cita `[Gardner88, Theorem 1]` con alcance; "to our knowledge" + soporte
`[Verreault]/[Gardner88]/[BY26]` (l.245-247); no-go reclasificado **Proposición** con
enunciado preciso del paso sharp; paréntesis contradictorio eliminado. Compila: 11 pp,
0 errores/0 undefined/0 overfull (log verificado). `ancillary/` (7 ficheros) y `BUILD.md`
al día.

## 5. Menores (polish, no bloqueantes — van en la próxima pasada)

1. **Thm 6.6, enunciado:** "three planks of positive width in the directions
   `u₁,u₂,u₃`" — precisar "**one in each direction**" (la prueba de unicidad usa
   exactamente un intervalo por dirección vía A.1). Igual criterio que Thm 5.1.
2. **Thm 6.8 (b):** la cota 1-D "covering `e` alone" podría citar el caso `d=1` anotado en
   Thm 2.1 para cerrar el círculo. Cosmético.
3. El Remark tras Thm 6.8 ya enuncia el cierre de la pregunta de Gardner para N=3 — con
   esto, la orden R7-3 (titular) está **sustancialmente cumplida**; queda solo decidir si
   se refleja más fuerte en el título del paper.

═══════════════════════════════════════════════════════════════════════
# ÓRDENES DE TRABAJO — RONDA 7 (revisada tras el cierre de R6)
═══════════════════════════════════════════════════════════════════════
Sustituye la priorización de `auditorias/51` (las tareas sobreviven; cambia el orden y el
enfoque de R7-2/R7-3). Ejecuta el investigador.

## R7-0 (PRIMERO) — R6-3 pendiente: tercera pasada de doña Rosa
El PDF (11 pp) tiene ahora **cuatro piezas sin auditoría externa**: Thm 6.3, Thm 6.6,
Thm 6.8, Apéndice A. Entregar con: (i) el mapa objeción→resolución (`notes/50-R6-1 §1`),
(ii) nota de que el Lemma 5.2 ya tiene prueba humana (su objeción mayor), (iii) pedido de
foco en las 4 piezas nuevas. Incorporar los menores §5.1–5.2 de arriba antes de entregar.

## R7-1 (sin cambios, EMPEZAR YA) — esqueleto ponderado en `d≥3`
Como `auditorias/51 §R7-1`. Ahora con anclaje extra: es literalmente el Problem 2 del
paper (primer test: medianas cíclicas de `Δ³`, 6 pesos de arista, exacto).

## R7-2 (reenfocado) — defecto de transporte `D(u)`: cuantificar el LADO no concurrente
Thm 6.8 cierra el lado concurrente; el problema abierto vive EXACTAMENTE en las ternas no
concurrentes, donde ninguna medida única funciona. `D(u)=inf_μ max_i sup dens(u_{i#}μ)`
cuantifica cuánto falla:
1. Definición + `Σrw≥1/D(u)` + alcanzabilidad del inf (como `auditorias/51 §R7-2.1`).
2. Cota de primeros momentos vía defecto de concurrencia (`§R7-2.2`); `D(facetas)≥3/2`.
3. **Nuevo foco (lo más valioso):** comportamiento de `D` cerca de la superficie de
   concurrencia: ¿`D(u)→1` continuamente, con módulo explícito? Si sí, `Σrw≥1/D` da las
   PRIMERAS cotas `>0.928` para un **entorno abierto** de ternas genuinamente no
   concurrentes — el primer resultado del proyecto dentro del territorio abierto real.
   Empezar perturbando una terna cíclica concurrente: ¿la medida `μ_p` perturbada
   (masas/soporte) controla `D(u+ε)`?
4. `D(facetas)=3/2` exacto (construcción o LP) y paisaje numérico etiquetado [EVIDENCE].
**Advertencia vigente:** lejos de la superficie `D≈3/2 ⟹ 1/D≈2/3`; el valor global no
bate B-Y — se presenta como caracterización + cotas locales, sin overclaim.

## R7-3 (reducido a decisión editorial) — titular
El cierre de Gardner-N=3 ya está enunciado (Remark tras Thm 6.8) y en el abstract.
Decidir: ¿título nuevo que lo refleje? Propuesta a evaluar: "…on the triangle: sharp
families, a three-direction characterization, and obstructions". Nada de matemática.

## R7-4 (subido de valor) — estabilidad cuantitativa, ahora de TODA la familia
Con A.1 general-τ y Thm 6.6, la versión `ε` aplica a la familia entera: si `Σr=1+ε`
(direcciones cíclicas concurrentes fijas), ¿los `I_i` están a distancia `O(ε)` de la
cobertura tight única? La maquinaria es lineal por tramos; constante explícita en
términos de `(α,β,γ)` (esperable que degenere cuando `αβγ→0`, el borde del medial — eso
es contenido, no defecto). Contraejemplo también publicable.

## R7-5 (sin cambios) — figuras TikZ + mapa de estatus.

## R7-6 (fondo) — moonshot acoplamiento (`auditorias/48`).

---

## Prioridad
1. **R7-0** (auditoría externa del estado real — es lo único que no controlamos nosotros).
2. **R7-1** (binario, barato) en paralelo.
3. **R7-2** (con el foco nuevo en el módulo de continuidad cerca de la superficie).
4. **R7-4 → R7-5 → R7-3**.

**Mensaje al investigador:** ronda sobresaliente — las dos piezas que faltaban para que el
paper cuente una historia completa, y el Apéndice A es exactamente el estándar que pedía
la auditoría externa. La corrección de mi apuesta en R6-4 es tuya por mérito y mía por
lección: ni la grilla ni el jefe orientan; lo exacto decide. El siguiente movimiento con
valor real es R7-2.3: cruzar por primera vez al territorio no concurrente con una cota.
