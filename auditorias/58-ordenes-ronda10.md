# Órdenes de trabajo — RONDA 10 (paquete ejecutable)
> Jefe de research: Claude. Fecha: 2026-07-03. Ejecuta el investigador.
> Contexto: Ronda 9 cerrada y verificada (`auditorias/57`); pasada 5 entregada/en curso con
> doña Rosa. La Ronda 10 corre EN PARALELO a su lectura. Foco: la pregunta que el propio
> marco dejó madura — **`sup_u D(u)` sobre ternas del triángulo: ¿es `3/2`?** — más el
> redondeo de la teoría de cuñas.
>
> **REGLA DE PROCESO (bloqueante): congelación de numeración.** Mientras Rosa lee la pasada 5,
> NO renumerar ningún enunciado existente del `.tex`. Todo material nuevo de esta ronda va en
> notas (`notes/54-*`) y/o en secciones/números NUEVOS al final; se integra al cuerpo solo
> tras su dictamen. La tabla vieja↔nueva de la pasada 5 fue inevitable una vez; dos veces es
> un patrón que un auditor externo no perdona.
>
> Reglas vigentes: exacto/racional (la grilla no decide — lecciones `notes/33`, `notes/38`);
> etiquetas `[PROVED]/[EVIDENCE]/[OPEN]` por afirmación; scripts load-bearing a
> `experiments/` + sync a `ancillary/` con el protocolo del Appendix B.

═══════════════════════════════════════════════════════════════════════
## R10-1 (RESEARCH #1) — `sup_u D(u)`: decidir si las facetas son el peor caso
═══════════════════════════════════════════════════════════════════════
**Estado:** `sup ∈ [3/2, 2]`. La cota de momentos está capada en `3/2` (Thm centroide) con
igualdad `δ=1/6` **solo** en el triple de facetas (la igualdad `|u(G)−½|=1/6` fuerza
`s∈{0,1}`, i.e. direcciones tipo-faceta; tres de ellas no-paralelas dos a dos = LAS facetas
módulo flips — dejar esta unicidad ESCRITA, es un lema de una línea que falta). Por tanto:
cualquier terna con `D>3/2` exige certificado dual **multi-nudo** (Rem `rem:wedgemoment`), y
cualquier prueba de `D≤3/2` universal exige una construcción primal nueva.

**Reducción previa (hacer primero, barato):** `D` es invariante por flips (`u↦1−u`) y por la
acción de `S₃` sobre los vértices. Parametrizar el espacio de ternas módulo esa acción
(patrón de aristas llenas de `thm:char`: {tres distintas} ∪ {dos compartidas} ∪ {una}) y
registrar en qué clase vive cada candidato testeado.

### Ruta A — cacería exacta de `D > 3/2` (certificado dual multi-nudo)
Herramienta: **LP dual exacto** que da cotas INFERIORES certificadas de `D(u)`:
1. `ψ_i` lineal a trozos con nudos en `{0, 1/q, …, 1}` (q moderado, racional); variables =
   valores `ψ_i(k/q) ≥ 0`.
2. `Σψ_i(u_i(x))` es afín a trozos sobre el complejo que cortan las rectas `{u_i = k/q}` en
   `Δ` ⟹ su mínimo se alcanza en un **vértice del complejo** (intersecciones de esas rectas
   entre sí y con `∂Δ` — `O(q²)` puntos, exactos en ℚ). Constraints: valor en cada vértice
   `≥ B` (lineal en las variables vía interpolación); normalización `Σ∫ψ_i = 1` (trapecios,
   exacto). Maximizar `B`. Todo en `fractions`.
3. **Validez del certificado:** el `B` óptimo es cota inferior RIGUROSA de `D` por dualidad
   débil (Thm duality) — el LP no necesita ser el sup exacto; cualquier `ψ` factible ya
   certifica. (Ventaja clave del lado dual: no hay riesgo de "grilla que miente".)

**Terrenos de caza, en orden:**
- **(i) La clase "dos aristas llenas compartidas"** (clase (b) de `thm:char`): ternas que
  **nunca** concurren — la no-existencia de testigo es estructural, así que el gap
  `D − 1/(1−2δ)` puede ser grande ahí. Ejemplo semilla: `u₁,u₂` llenas en `AB` con
  `τ₁≠τ₂` en `C`, `u₃` llena en `BC`; barrer `(τ₁,τ₂,τ₃)` racionales extremos.
- **(ii) Cerrar el sandwich:** `τ=(13/25,½,½)` con `225/224 ≤ D ≤ 112/111`. Subir la cota
  inferior con multi-nudo: si supera `225/224` ⟹ **primera prueba de gap** momentos < D
  (resultado en sí); si alcanza `112/111` ⟹ primera `D` exacta no-simétrica.
- **(iii) Facetas inclinadas:** perturbaciones de la terna de facetas (δ cerca de 1/6);
  ¿el multi-nudo empuja `D` por encima de `1/(1−2δ)` local?
- **(iv) Límites casi-paralelos:** `u₂ → u₁` (dentro de no-paralelas). OJO con la intuición:
  para DOS direcciones Gardner da `D=1` siempre, así que el límite podría tener `D` PEQUEÑO,
  no grande — pero la convergencia de mapas no controla densidades; medir exactamente qué
  pasa con `D` a lo largo de un camino `τ₂→τ₁`. Sea cual sea el desenlace, es un lema de
  continuidad/discontinuidad de `D` que hoy no tenemos.

### Ruta B — intento de `D ≤ 3/2` universal (construcción primal por MEZCLA)
Derivación que dejo hecha (verificarla y explotarla):
- Para cada par `{j,k}` existe testigo de Gardner `ν_{jk}` (marginales de `u_j,u_k`
  uniformes; 2 direcciones siempre). Definir
  **`M_i(ν_{jk}) := ‖dens(u_{i#}ν_{jk})‖_∞`** (la tercera marginal, `i∉{j,k}`).
- Mezcla simétrica `μ = ⅓(ν₁₂+ν₁₃+ν₂₃)`: densidad de la marginal `i` ≤ `⅔ + M_i/3`.
  ⟹ **si todo par admite un testigo de Gardner con tercera-marginal ≤ 5/2, entonces
  `D ≤ ⅔ + (5/2)/3 = 3/2` UNIVERSAL.** (Pesos desiguales dan la variante optimizada
  `dens_i ≤ (1−w_{jk(i)}) + w_{jk(i)}M_i`.)
- **Consistencia en facetas (test crítico, hacer PRIMERO):** como `D(facetas)=3/2` exacto,
  la mezcla fuerza `M ≥ 5/2` allí — es decir, TODO testigo `ν₁₂` de `(λ₁,λ₂)` tiene
  `λ₃`-densidad `≥ 5/2` en algún punto, y la ruta es viable sii se ALCANZA `5/2`.
  **Tarea concreta:** `M*(λ₁,λ₂;λ₃) := min_{ν₁₂} ‖dens(λ₃#ν₁₂)‖_∞` — es un `D`-tipo LP
  (mismo esquema dual/primal, con dos marginales FIJAS uniformes). Calcularlo EXACTO.
  - Si `M*(facetas) = 5/2`: la ruta es plausiblemente tight — atacar el caso general
    (¿`M* ≤ 5/2` para todo par y toda tercera dirección? — probablemente por la misma
    dualidad, con certificados de cuña adaptados).
  - Si `M*(facetas) > 5/2`: la mezcla simétrica NO puede probar `3/2`; documentar la
    obstrucción exacta y pasar a pesos desiguales o descartar la ruta [PROVED-negativo
    también cuenta].
- Pista estructural adicional: en facetas el óptimo primal es el ciclo por los vértices
  alternos del hexágono de contacto; para terna general, buscar el análogo sobre el
  **contact set del dual óptimo** (`prop:slack`): soporte candidato = `{Σψ_i(u_i(x)) = D}`.

### Criterio de cierre R10-1 (cualquiera de estos es entregable):
1. Terna exacta con certificado dual `> 3/2` ⟹ teorema "las facetas no son el peor caso".
2. Prueba de `D ≤ 3/2` universal ⟹ teorema **`Σrw ≥ 2/3` para TRES direcciones cualesquiera
   en el triángulo** (con la honestidad de siempre: `2/3 < 4√3−6`; el valor es estructural).
3. Si ninguno cae: `M*(facetas)` exacto + el sandwich decidido + el lema de continuidad del
   punto (iv) — tres piezas publicables menores, y `sup D` queda [OPEN] con el estado
   consolidado y las obstrucciones DOCUMENTADAS (qué mató cada ruta).

═══════════════════════════════════════════════════════════════════════
## R10-2 (RESEARCH #2, acotado) — ¿`δ_c = δ` siempre? (el criterio `p* ∈ T_u`)
═══════════════════════════════════════════════════════════════════════
En los 12 ejemplos exactos hay igualdad [EVIDENCE]. Decidirlo:
1. **Formulación concreta:** `T_u = conv{(u₁(V),u₂(V),u₃(V)) : V∈{A,B,C}}` ⊂ `Π`;
   `p*_i = ½ + ε·δ_c·sign(c_i)`. La pregunta es un **test punto-en-triángulo 2-D dentro de
   `Π`**, exacto en ℚ por instancia.
2. **Barrido exacto primero** (500+ ternas racionales cubriendo las tres clases de patrón,
   incluida la clase (b) que NUNCA se ha muestreado para esto): si aparece contraejemplo,
   reportarlo con ambos defectos calculados — delimita las cuñas, publicable.
3. **Si el barrido no encuentra nada: intentar la prueba.** Pista: es el mismo género de
   argumento que `lem:external` (conteo de signos con `Σq=1`) — allí se probó el caso
   `δ_c=0`; la pregunta general es si la proyección `ℓ∞` del centro cae siempre en la imagen.
   Escribir `p*∈T_u` como tres desigualdades baricéntricas en `Π` y ver si los signos de
   `c_i` las fuerzan.
**Valor:** si es teorema ⟹ "las cuñas de un nudo SIEMPRE igualan la cota de momentos" —
redondea §7 y simplifica el paper (la jerarquía `δ_c ≤ δ` colapsa). Si es falso ⟹ delimita
exactamente dónde hacen falta ψ multi-nudo (alimenta R10-1 Ruta A).

═══════════════════════════════════════════════════════════════════════
## R10-3 (editorial, 30 min) — abstract a ≤200 palabras
Hoy ~230. Poda de palabras sin tocar la tesis única ni la frase final de alcance. NO tocar
numeración (regla de congelación). Puede esperar al dictamen de Rosa si prefieres batchear.

## R10-4 (fondo) — estabilidad cuantitativa `ε` de la familia cíclica (ex R8-6/R7-4)
Sin cambios: versión `ε` de la rigidez (A.1 general-τ es la maquinaria). Solo con capacidad
sobrante — R10-1/R10-2 tienen prioridad.

## R10-5 (moonshot, fondo) — acoplamiento / batir B-Y global. Sin cambios (`auditorias/48`).

═══════════════════════════════════════════════════════════════════════
## Prioridad y secuencia
1. **R10-1 Ruta B test crítico (`M*(facetas)`)** — es barato, decide la viabilidad de la
   ruta universal, y su LP es el mismo esquema que ya tienes en `defect_duality.py`.
2. **R10-1 Ruta A terrenos (i)+(ii)** — la clase (b) nunca cazada + cerrar el sandwich.
3. **R10-2 barrido exacto** (rápido) → prueba o contraejemplo.
4. R10-1 (iii)/(iv) · R10-3 · R10-4/5 fondo.
5. **Al llegar el dictamen de Rosa (pasada 5): TODO se pausa y se audita eso primero.**

**Entregables de la ronda:** `notes/54-R10-1-*.md`, `notes/54-R10-2-*.md` con etiquetas
estrictas; scripts `supD_dual_hunt.py`, `gardner_third_marginal.py` (o nombres análogos) en
`experiments/`; NINGÚN cambio de numeración en el `.tex` vivo.

**Mensaje al investigador:** la Ronda 9 dejó el marco; la 10 pregunta qué tan lejos llega.
El test de `M*(facetas)` es la jugada de mejor información/costo de toda la ronda: decide en
un LP si la ruta universal está viva, y las facetas son el único punto donde ya sabemos la
respuesta contra la que calibrar. En la Ruta A, el certificado dual es tu red de seguridad:
cualquier `ψ` factible es cota inferior rigurosa — no hay grilla que pueda mentirte del lado
dual. Y respeta la congelación de numeración: Rosa está leyendo.
