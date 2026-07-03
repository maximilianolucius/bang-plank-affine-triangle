# Auditoría Ronda 7 (§7 defecto de transporte, §8 símplex-3) + dictamen 3ª pasada de doña Rosa + Órdenes Ronda 8
> Auditor / Jefe de research: Claude. Fecha: 2026-07-02.
> Alcance: `notes/51-R7-0/1/2`, §7–§8 del `.tex` (14 pp), y la 3ª auditoría externa de doña
> Rosa (sobre la copia congelada de 11 pp, SIN §7–§8).
> Método: verificación a mano de las identidades de §7–§8 + ejecución de los 2 scripts nuevos
> + cotejo de cada punto de doña Rosa contra el texto vivo.

---

## PARTE A — Ronda 7: §7 y §8 CONFIRMADOS [PROVED]. Y por primera vez, una cota en el territorio abierto.

### A.1 §7 (defecto de transporte) — verificado

- **Prop 7.2 (`D` bien definido):** (i) inf alcanzado por compacidad débil-* ✓; (ii)
  `Σrw≥1/D` ✓; (iii) `D=1⟺`concurrencia (vía Thm 6.8) ✓; (iv) `D≤2` (medida uniforme,
  estimación per-plank de Thm 2.1) ✓. Correcta.
- **Prop 7.3 (cota de momentos `D≥1/(1−2δ)`):** rederivada — media de `ν≤D·Leb` está en
  `[1/(2D),1−1/(2D)]`; el baricentro `p` da `media(u_{i#}μ)=u_i(p)`; luego
  `δ(u)≤½−1/(2D)` ⟹ la cota. Facetas: `Σλ_i(p)=1` fuerza algún `λ_i(p)≤⅓` ⟹ `δ≥1/6` ⟹
  `D≥3/2`. ✓
- **Thm 7.4 (`D(facetas)=3/2` exacto):** **verifiqué el testigo exactamente** (Fraction).
  El triángulo inscrito del PAPER `P₀=(0,⅓,⅔), P₁=(⅔,0,⅓), P₂=(⅓,⅔,0)` da, para `λ₁`:
  densidad `½` en `[0,⅔]` (arista `P₀P₁`) + `1` en `[⅓,⅔]` + `1` en `[0,⅓]` = **`3/2` en
  `[0,⅔]`** exacto ✓. Cota inferior (momentos) = cota superior ⟹ `D=3/2`. Elegante y
  correcto; sin LP, a mano.
  - **⚠ Discrepancia chat vs paper (a favor del paper):** el reporte del investigador en el
    chat citó los vértices `(0,½,½),(½,0,½),(½,½,0)` (triángulo **medial**). Los verifiqué:
    dan un **átomo en ½** (arista donde `λ₁` es constante) ⟹ NO uniformes ⟹ testigo
    inválido. **El paper NO usa esos** — usa el inscrito `(0,⅓,⅔)…`, que es correcto. Es
    un lapsus del mensaje, no del manuscrito. Sin acción sobre el `.tex`; anotado para que
    el investigador no propague el testigo equivocado.
- **Thm 7.6 (estabilidad lineal):** pesos congelados `(γ,α,β)=(⅓,⅓,⅓)` empujados por
  direcciones perturbadas; desviación `(α+γ/τ₁)−1=γ(τ₁*−τ₁)/(τ₁τ₁*)`, acotada por
  `ε/(m(m−ε))` (γ≤1, τ*≥m, τ≥m−ε). ✓ `D≤1+ε/(m(m−ε))`, `Σrw≥1−ε/(m(m−ε))`.
- **Cor 7.7 (LA cota nueva):** `τ*=medianas, m=½, ε=1/60` ⟹ pérdida
  `(1/60)/((½)(½−1/60))=2/29` ⟹ **`Σrw≥27/29≈0.93103`**. Comparación exacta con
  `4√3−6≈0.92820`: `(201/29)²=40401/841>48 ⟺ 40401>40368` ✓. **Correcto.**

  **Esto es el primer resultado del proyecto DENTRO del territorio abierto.** Un entorno
  full-dimensional (3-paramétrico) de ternas cíclicas donde el locus concurrente es
  codim-1: casi todas NO tienen medida testigo (Thm 6.8) y aun así se bate B-Y. Real.

  **Caveat de honestidad (crítico, y el investigador LO PUSO — Rem 7.8):** `4√3−6` de B-Y
  es **uniforme sobre TODAS las ternas**; esto mejora **solo en ese entorno y solo para
  coberturas por planks en esas 3 direcciones cíclicas**. La cota `Σrw≥1/D` sí vale para
  cualquier NÚMERO de planks (mientras sean ⊥ a las 3 direcciones), así que la comparación
  es legítima en esa clase restringida de coberturas. La Rem 7.8 lo dice bien. **Vigilar
  que abstract e intro NO lo simplifiquen a "beats B-Y" sin el caveat** (ver Parte C).
- **Rem 7.9 (sandwich `225/224≤D≤112/111` para `τ=(13/25,½,½)`):** cota de momentos NO
  exacta fuera de los casos simétricos — reportado como `[OPEN]` (Problem 10.3). Honesto.

### A.2 §8 (familia testigo en Δ³) — verificado

- **Thm 8.1 (familia σ):** **rederivé `a(σ),b(σ)` a mano.** Pieza media `[σ,1−σ]`:
  `a[1+2/(1−σ)+1/(1−2σ)]=1`, numerador común `=2(σ²−4σ+2)` ⟹
  `a=(1−σ)(1−2σ)/(2(σ²−4σ+2))` ✓. Pieza externa ⟹
  `b=σ(2−3σ)/(2(σ²−4σ+2))` ✓. Positividad en `(0,½]` (denom>0 pues raíces `2±√2`;
  numeradores≥0) ✓. Marginal uniforme en las 4 direcciones ⟹ `Σrw≥1` en Δ³. **Primera
  instancia del método de transporte fuera del plano.** Medianas: `a=0,b=½`.
- **Prop 8.2 (obstrucción `d≥4`):** removiendo 2 vértices del ciclo de `d+1≥5` quedan ≥3 en
  ≤2 arcos ⟹ un arco con 2 consecutivos ⟹ `u_m≡½` en esa arista ⟹ átomo ⟹ sin testigo en
  1-esqueleto. Script confirma `d=4,5,6,7` (todas las aristas constantes). ✓

### A.3 Fracaso reportado sin enterrar — bien hecho

El investigador conjeturó `D(u)=1/(1−2δ(u))` en general, **falla** (sistema del lazo
singular; la relación afín `Σv_i u_i=const` exige una relación entera en `V` que solo se
da en medianas/facetas). Lo dejó como Problem 10.3 con sandwich exacto de muestra. Exacto
lo que pido: el fracaso se reporta como resultado, no se esconde. La regla "lo exacto
decide, ni grilla ni jefe" está internalizada.

**Veredicto Parte A:** §7–§8 son [PROVED] con verificación exacta independiente. La Cor 7.7
es un salto cualitativo — el proyecto por primera vez dice algo NUEVO sobre coberturas que
no admiten el método (aunque en una clase restringida y con caveat honesto).

---

## PARTE B — 3ª pasada de doña Rosa: alta calidad, y su tesis central es CORRECTA

Leyó la copia congelada de 11 pp (SIN §7–§8). Su recomendación ("major revision bordering
on reject") es dura pero su **diagnóstico de fondo es acertado y es el más importante que
hemos recibido**: *los claims globales van más rápido que las pruebas; se difuminan las
fronteras entre (a) resolver una familia de direcciones, (b) caracterizar medidas testigo,
(c) acotar para un nº fijo de planks, (d) resolver el triángulo, (e) resolver el plano.*
Esta es exactamente la enfermedad recurrente del paper, y ahora **también amenaza a §7**
(Cor 7.7 "beyond B-Y", que ella no vio). Cotejo punto por punto:

| # | Punto de doña Rosa | Dictamen | Evidencia |
|---|---|---|---|
| 1 | "no single-measure argument can improve 1/d" es overclaim | **VÁLIDO — MUST FIX, y AHORA más claro** | Vivo en l.48 (abstract) y l.153. La frase es **contradicha por el propio paper**: la medida de transporte `μ_p` (§6) y `D(u)` (§7) SON medidas únicas adaptadas a una terna y dan constante `1≫1/2=1/d`. Lo verdadero: *la medida uniforme de volumen* (o cualquier medida acotada-uniforme en TODAS las direcciones a la vez) no puede batir `1/d`. Reformular a eso. |
| 2 | "(equivalently Conjecture 1.1 for the triangle)" es overclaim grave | **VÁLIDO — MUST FIX** | l.929. Falso: la conjetura para el triángulo admite CUALQUIER nº de planks; 3 planks es subfamilia; no hay reducción probada de coberturas arbitrarias a 3 planks. Borrar el paréntesis; dejar "the remaining three-plank case is non-concurrent triples". |
| 3 | Thm 6.8 "complete characterization" — acotar alcance | **VÁLIDO** | Rem 6.9 debe decir "reduced **within the witness-measure approach**, not as a theorem of the conjecture". Es la misma enfermedad que #2. |
| 4 | Thm 6.6 Step 2 muy comprimido; positividad de `x*,y*` en el texto, no en script | **VÁLIDO (rigor)** | Las coordenadas cerradas SÍ están en el texto (l.498–508), pero la positividad se delega al script. Aislar Step 2 como lema topológico + escribir las desigualdades elementales (son elementales). |
| 5 | Apéndice A: acción de grupo precisa; casos frontera L/M/R; LMR condensado; scripts secundarios | **VÁLIDO (presentación)** | Definir el grupo (rotación⟨3⟩ × reflexión∘flip⟨2⟩ = orden 6) y por qué `τ↦(1−τ₁,1−τ₃,1−τ₂)` preserva el enunciado ∀τ; en cada caso imposible, una frase de que los endpoints degenerados no añaden solución; LMR con más aire (separar subcaso truncado). |
| 6 | Thm 3.1 cita a Gardner como caja negra | **VÁLIDO** | Enunciar `[Gardner88, Thm 1]` con hipótesis exactas (par de direcciones no paralelas / cuerpo convexo planar / medida de probabilidad / marginales = Leb tras normalizar / posible soporte singular). |
| 7 | Thm 3.2 medibilidad/compacidad de `U_k`, cita de BM-1D | **VÁLIDO (menor)** | Una línea: intervalos cerrados ⟹ `U_k` compacto; `|A+B|≥|A|+|B|` para compactos citado/probado en una línea. |
| 8 | Prop 7.1 (no-go) sigue con "no argument can" informal | **PARCIAL** | Split: la **Proposición** enuncia SOLO el ratio sharp `(ℓ−a)/ℓ` (matemática); la lectura "ningún normalizador `>ℓ` por esta vía" va a un Remark rotulado como obstrucción metodológica. Ya está medio hecho; completar el corte. |
| 9 | Claim de prioridad aún débil | **VÁLIDO** | "We are not aware of a previous tight non-facet three-direction rigidity result for the triangle" — menos fuerte, defendible. |
| 10 | Editorial: `[AUTHOR NAMES]`, abstract largo/cargado, exceso de palabras-venta, `[1]` manuscript 2010, pocas refs, faltan figuras | **VÁLIDO** | Author block pendiente (decisión del investigador); figuras = R7-5 (no empezada); podar el abstract y las palabras-venta ("centerpieces", "generic", "full rigidity" acumuladas). |

**Lo que ella reconoce sólido** (1/d bien encaminado, Thm 3.2 elegante, Thm 4.1 correcto,
Thm 6.3 contribución real, Cor 6.4/Thm 6.8 con potencial, Apéndice A en la dirección
correcta) coincide con mis verificaciones. Convergencia otra vez.

**Puntos donde su crítica es más débil (defenderemos, no cederemos):**
- Su #1 y #3 se resuelven con **precisión de redacción**, no recortando resultados: los
  teoremas son correctos; el problema es cómo se enuncian. No hay que degradar Thm 6.8.
- El "computer-assisted" del Apéndice A ya es prueba humana; su queja #5 es de presentación,
  no de validez (yo revisé el apéndice línea a línea en `auditorias/52` — es correcto).

---

## PARTE C — La enfermedad recurrente, y por qué la Ronda 8 es la decisiva

Doña Rosa ha señalado **tres veces** (pasadas 2 y 3) variantes del mismo problema: claims
que exceden lo probado. No es azar; es el patrón de fallo característico de este paper. Y
§7 acaba de crear el ejemplo más peligroso hasta ahora — Cor 7.7 "beyond B-Y" — que si se
enuncia sin el caveat de Rem 7.8 en el abstract/intro será **exactamente** el tipo de
overclaim que hace que un referee rechace. El investigador puso el caveat donde el teorema
vive; falta blindar el resto del texto.

**La Ronda 8 es una "pasada de precisión": cada afirmación acotada a su alcance exacto.**
No hay matemática nueva obligatoria; hay que hacer que el texto diga exactamente lo que las
pruebas soportan, ni más. Es lo que separa este paper de ser publicable.

═══════════════════════════════════════════════════════════════════════
# ÓRDENES DE TRABAJO — RONDA 8 (pasada de precisión + cierre editorial)
═══════════════════════════════════════════════════════════════════════

## R8-1 (MUST FIX, bloqueante) — los dos overclaims vivos
a. **`single-measure` (l.48, l.153, y donde aparezca):** reformular a "the uniform
   (volume) measure cannot improve `1/d`; more generally no measure that is
   uniform-bounded in all directions simultaneously can" — y verificar que NO contradice
   §6–§7 (donde medidas adaptadas SÍ superan `1/d`). Ajustar Rem 2.2 acorde.
b. **"(equivalently Conjecture 1.1 for the triangle)" (l.929):** BORRAR el paréntesis.
   Dejar: "The three-plank case for non-concurrent tilted triples on the triangle
   (Theorem 6.8 settles the concurrent case)."
**Hecho:** ningún enunciado afirma más de lo probado.

## R8-2 (precisión de alcance) — acotar las caracterizaciones
- **Rem 6.9:** "reduced **within the uniform-marginal witness-measure approach**" (no como
  teorema de la conjetura). Misma cirugía en el abstract si insinúa reducción estructural.
- **Abstract e intro:** una frase explícita separando (a)–(e) de la Parte C. Que el lector
  no pueda confundir "caracterizamos medidas testigo" con "resolvemos el triángulo".
- **§7 (blindaje anticipado, antes de que Rosa lo vea):** verificar que abstract/intro
  presenten Cor 7.7 CON el caveat de Rem 7.8 (uniforme-vs-local; clase de coberturas
  restringida a las 3 direcciones). Es el próximo overclaim si se descuida.

## R8-3 (rigor) — los puntos de prueba de Rosa
- Thm 6.6 Step 2 → lema topológico aislado + positividad de `x*,y*` escrita en el texto.
- Prop 7.1 → split (Proposición = ratio sharp; obstrucción metodológica = Remark).
- Thm 3.1 → enunciado exacto de `[Gardner88, Thm 1]`.
- Thm 3.2 → una línea de medibilidad/compacidad + cita BM-1D.
- Apéndice A → grupo explícito + frases de casos frontera + LMR con aire.

## R8-4 (editorial) — presentabilidad
- Podar abstract y palabras-venta (auditar "centerpiece/generic/full rigidity/first"
  acumulados; dejar solo los justificados con "to our knowledge").
- Claim de prioridad → "we are not aware of…".
- Author/affiliation/email/MSC/keywords (decisión del investigador).
- Ref `[1]` Ambrus: forma verificable (URL Rényi ya la teníamos en `notes/40`).

## R8-5 (R7-5, ahora prioritario) — figuras
Las figuras dejaron de ser cosmética: Rosa las pide y son la mejor defensa contra las dudas
de rigor de §6/Apéndice A. Mínimo: (1) tercios centrales / familia cíclica con `p` y masas
`1−2p_j`; (2) edge-tilings del Apéndice A (una arista con las 3 trazas); (3) opcional: el
lazo inscrito de Thm 7.4 y/o el mapa de estatus del espacio de ternas. TikZ.

## R8-6 (R7-4, research acotado) — estabilidad cuantitativa de la familia
Sin cambios respecto a `auditorias/52 §R7-4`: versión `ε` de la rigidez para toda la
familia cíclica (con A.1 general-τ). Después de R8-1..R8-5.

## R8-7 (entrega) — 4ª pasada de Rosa DESPUÉS de R8-1..R8-4
NO entregar antes: la copia debe tener los overclaims corregidos Y §7–§8 (que ella aún no
vio). Entregar el manuscrito vivo completo (14 pp) con el mapa objeción→resolución de la
pasada 3. Es la primera vez que verá §7–§8 y la caracterización sin overclaims.

## R8-8 (moonshot, fondo) — acoplamiento. Sin cambios.

---

## Prioridad
1. **R8-1** (los dos overclaims — bloqueantes, son lo que la hace "bordering on reject").
2. **R8-2 + R8-3** (precisión de alcance + rigor de pruebas).
3. **R8-4 + R8-5** (editorial + figuras).
4. **R8-7** (recién entonces, Rosa pasada 4).
5. R8-6, R8-8 fondo.

**Mensaje al investigador:** §7–§8 son sobresalientes — la Cor 7.7 es lo más cerca que ha
estado el proyecto de decir algo nuevo sobre el problema abierto, y el fracaso del lazo
general lo reportaste como corresponde. Pero doña Rosa tiene razón en lo de fondo, y lo ha
dicho tres veces: **el texto promete más de lo que prueba.** La Ronda 8 no agrega teoremas;
hace que cada frase diga su alcance exacto. Ese es el trabajo que convierte "bordering on
reject" en "accept with minor revisions". Corrige R8-1 sin discutir: son dos frases
literalmente falsas leídas al pie. Corregí el testigo del chat en tu cabeza (el paper está
bien; tu mensaje citó el triángulo medial, que da un átomo).
