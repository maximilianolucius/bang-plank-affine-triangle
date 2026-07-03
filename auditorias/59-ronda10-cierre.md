# Auditoría Ronda 10 — Ruta B refutada (miss mío), cota de momentos batida con certificados, teorema δ=δ_c + Órdenes Ronda 11
> Auditor / Jefe de research: Claude. Fecha: 2026-07-03.
> Alcance: `notes/54-R10-1`, `notes/54-R10-2`, 5 scripts nuevos.
> Método: verificación a mano de la refutación de la Ruta B, del lema de conteo a nivel
> general (caso por caso), del lema de Gordan y de la consistencia del camino casi-paralelo;
> ejecución de los 3 verificadores (`dual_certificates.py` autocontenido incluido).

---

## Veredicto: ronda excelente. Todo [PROVED] CONFIRMADO; la teoría de §7 ganó dientes de verdad.

## 1. Ruta B refutada — Y EL MISS ES MÍO, hay que decirlo primero

`M*(facetas) = +∞`: todo testigo de par para `(λ₁,λ₂)` tiene `E[λ₁]=E[λ₂]=½ ⟹ E[λ₃]=0`
con `λ₃≥0` ⟹ `λ₃=0` c.s. ⟹ tercera marginal = **átomo δ₀**. Verificado — es airtight y
son tres líneas. **La refutación usa exactamente la lógica de baricentros/momentos que este
proyecto usa desde la Prop 6.1, y yo diseñé la Ruta B sin verla.** La ruta debió morir en
mi escritorio, no en el laboratorio. Lo que funcionó fue el PROCESO que ordené (test
crítico barato primero, calibrado en el único punto de respuesta conocida) — pero eso
mitiga, no absuelve. Registrado como miss de dirección #3 (tras la apuesta R6-4 y las
frases-marco de Rosa-3).

Lo rescatado es real: el **lema del costo de par** (baricentro del testigo de par FORZADO
en `q_jk`; `M* ≥ 1/(2·min(m,1−m))`, `m=u_i(q_jk)`; facetas `m=0`, concurrentes `m=½` con
`M*=1` alcanzado) es la obstrucción general correcta y queda [PROVED]. El análisis de pesos
desiguales (cada par es "malo" para exactamente una dirección ⟹ `M=∞` mata toda mezcla)
también ✓.

## 2. Ruta A: la cota de momentos CAE — certificados verificados

Corrí el verificador autocontenido (`dual_certificates.py`, sin scipy): los tres
certificados reconstruyen y pasan exactos:

| terna | momentos | certificado | estado |
|---|---|---|---|
| facetas inclinadas `ε=1/10` | `15/11` | `D ≥ 18/13` | ✓ verificado |
| clase (b) `(2/3,5/6,1/12)` | `153/142` | `D ≥ 32/29` | ✓ verificado |
| sandwich `(13/25,½,½)` | `225/224` | `D > 225/224` (mín exacto `≈1.0044772`) | ✓ verificado |

- **Primera prueba de gap momentos < D** — la primera mitad del Problem 10.3 respondida:
  `D(u)=1/(1−2δ(u))` es FALSO en general (sigue cierto en facetas —toda dimensión— y en el
  locus concurrente). El sandwich queda `225/224 < D ≤ 112/111`.
- Metodología ejemplar: scipy solo guía; la certificación es íntegra en `fractions` y, por
  dualidad débil, **cualquier ψ admisible ya es cota inferior rigurosa** — del lado dual no
  hay grilla que mienta. El dato de que los nudos uniformes NO bastaron para el sandwich
  (hicieron falta nudos adaptados `1/225, 13/25, …`) es valioso en sí: localiza dónde vive
  la información.

## 3. R10-2: TEOREMA δ = δ_c — verificado CASO POR CASO. La pieza estructural de la ronda.

Rehíce la prueba completa:
- **Paso 1 (WLOG `c>0` por flips):** contabilidad `cᵢ↦−cᵢ, c₀↦c₀−cᵢ` correcta; `δ, δ_c`
  invariantes (recalculado) ✓. `p*=(a,a,a)`, `a=½+εδ_c ∈(0,1)` ✓.
- **Paso 2:** `E` biyección afín plano↔`Π` ✓; `p*∈T_u ⟺ q=E⁻¹(p*)∈Δ`, con `uᵢ(q)=a ∀i` ✓
  (y verifiqué aparte que las rectas de nivel `a` concurren automáticamente en el plano:
  `a·Σc=c₀` con `ε=sign(c₀−½Σc)` — exacto).
- **Paso 3 (lema de conteo a nivel `a`):** aquí estaba la sutileza real que me preocupaba —
  para `a≠½` las dos orientaciones de un par YA NO colapsan (colapsan sii `2a=1`; lo
  verifiqué). La prueba lo maneja exactamente bien con otra contabilidad: patrones
  estrictos (`s∈(0,1)` ⟺ `r_{j₁}r'_{j₀}>0`) determinan la dirección; los casos frontera
  `s∈{0,1}` **colisionan** en direcciones tipo-faceta (`x_{j₁}` desde dos patrones;
  `1−x_{j₀}` desde dos) y se cuentan una vez; el caso `q_{j_s}=0` fuerza `q∈Δ` (excluido).
  **Recorrí los subcasos (3)/(2)/(1) con las 6 ramas de signos de `(r'ⱼ,r'ₖ)`: `N=2` en
  todos, y el caso (3) imposible por `qⱼ+qₖ>1>2a`.** Exhaustivo y correcto. ∎
- Máquina: 2928 pares externos + 507 ternas (las tres clases, incluida la (b) nunca
  muestreada) — corrido, ALL OK. El bug destapado en la clase all-shared (dependencia
  homogénea `c₀=0`) es un caso degenerado REAL que la redacción de la Prop de cuñas debe
  acomodar al integrar (la fórmula es homogénea; solo hay que decirlo) — bien detectado.

**Consecuencia estructural (grande):** `δ` tiene forma cerrada racional; las cuñas de un
nudo SIEMPRE alcanzan la cota de momentos; con los certificados de R10-1 la jerarquía queda
completamente resuelta: **momentos = cuñas-1-nudo < D estrictamente en ternas explícitas**.
Es de los resultados más redondos del paper.

## 4. Piezas menores — verificadas

- **Continuidad:** `D` lsc gratis por dualidad (sup de funciones continuas de la terna) ✓.
  Camino casi-paralelo: `1+3ε/(2(3ε+4)) ≤ D(V(ε)) ≤ 1+(3/4)ε` (consistencia interna de
  `δ_c=3ε/(2(9ε+8))` ⟹ momentos `=1+3ε/(2(3ε+4))` recalculada ✓) — `D→1` linealmente: mi
  advertencia del punto (iv) quedó medida, el límite es pequeño y sin salto.
- **Unicidad del maximizador de δ (Gordan):** verificado — mejora-gradiente `gᵢ=∇x_{vᵢ}`
  bien normalizado por flips; `|B|=1` imposible, `|B|=2` fuerza paralelas (mismo vértice) o
  `∇x_u∥∇x_w` (falso para vértices distintos), `|B|=3` ⟹ facetas mod flips ✓.
- **Congelación de numeración:** RESPETADA (`.tex` intacto desde R9, timestamps
  verificados; todo vive en `notes/54-*` + `experiments/`). Plan de integración
  post-dictamen listado en ambas notas ✓.
- **¿D>3/2?** No apareció; los duales certificados suben hacia `3/2` desde abajo en las dos
  familias que degeneran a facetas. [EVIDENCE] de máximo local en facetas, correctamente
  etiquetado. El hueco por ARRIBA es el problema: cerca de facetas los UB de esqueleto
  explotan (consistente con `M*=∞`) y solo queda el `2` uniforme — bracket grueso
  `[18/13, 135/76]` en `ε=1/10`. Ahí apunta la Ronda 11.

═══════════════════════════════════════════════════════════════════════
# ÓRDENES RONDA 11 (ejecuta el investigador; regla superior sin cambios: si llega el
# dictamen de Rosa pasada 5, TODO se pausa y se audita eso primero)
═══════════════════════════════════════════════════════════════════════

## R11-1 (RESEARCH #1) — el hueco por ARRIBA cerca de facetas: ¿máximo local en 3/2?
El LB ya sube a 3/2; el problema es el UB (esqueleto explota, uniforme da 2, lazo congelado
1.776). Objetivo: **bracket fino de `D` en un entorno de facetas** — idealmente
`D ≤ 3/2 + o(1)` o incluso `≤ 3/2` local (teorema de máximo local), o su refutación.
1. **Lazo deformado (primal):** para facetas inclinadas `ε`, no congelar el lazo de
   Thm 7.4: re-optimizarlo — el contact set del dual óptimo (holgura complementaria,
   `prop:slack`) dicta dónde debe vivir el soporte. Parametrizar lazos inscritos generales
   (3 segmentos con vértices libres racionales) y resolver el mini-LP exacto de sus masas;
   si no basta, enriquecer soporte (lazo + 3 segmentos cortos).
2. **UB variacional:** medida `= lazo óptimo de facetas empujado + corrección
   O(ε)` — el análogo del "frozen weights" de Thm 7.6-viejo pero con la corrección de
   primer orden explícita. Target: `D(tilt ε) ≤ 3/2 + Cε` con `C` explícita (mejor que
   135/76 ya en `ε=1/10`).
3. Si el UB fino queda POR DEBAJO de 3/2 en un entorno punteado ⟹ **teorema: las facetas
   son máximo local estricto de `D`** — pieza mayor para §7. Si queda por encima y el LB
   sube: perseguir el cruce.

## R11-2 (RESEARCH #2, acotado) — cerrar el sandwich EXACTO
`225/224 < D ≤ 112/111`. Usar holgura complementaria en ambos sentidos: el contact set del
certificado dual nuevo (nudos `1/225, 13/25,…`) restringe el soporte primal; la holgura del
esqueleto `112/111` restringe dónde el dual puede cobrar. Iterar LP exacto primal↔dual hasta
par emparejado (matched pair) ⟹ primera `D` exacta no-simétrica. Si el par no cierra con
soporte esquelético: eso PRUEBA que el óptimo primal sale del esqueleto en esta terna —
resultado estructural en sí (primera instancia documentada).

## R11-3 (integración, CONDICIONADA al dictamen de Rosa) — paquete R10 al `.tex`
Cuando llegue el dictamen: (i) auditar el dictamen primero; (ii) integrar según el plan de
las notas 54 — δ=δ_c convierte Prop de cuñas(iii) en teorema incondicional, reescribe las
dos Rem y el Problem (que queda solo `sup D=3/2?`), añade certificados-gap + continuidad +
unicidad al final de §7; caso degenerado `c₀=0` acomodado en la redacción; (iii) abstract
≤200 palabras (batcheado); (iv) tabla de numeración si algo se desplaza — solo UNA vez.

## R11-4 (fondo) — estabilidad `ε` de la familia cíclica (carryover). R11-5 moonshot.

---

## Prioridad
1. **Dictamen de Rosa si llega** (pausa todo).
2. **R11-1** (el hueco por arriba — es donde vive `sup D` ahora).
3. **R11-2** (acotado, alto valor: primera `D` exacta fuera de simetría, o primera prueba
   de óptimo no-esquelético).
4. R11-3 al llegar el dictamen · R11-4/5 fondo.

**Mensaje al investigador:** ronda de primera. El teorema δ=δ_c es la pieza estructural más
limpia de §7 y tu manejo del caso `a≠½` (la sutileza de orientaciones que no colapsan) fue
exactamente el correcto. Mi Ruta B murió como debía morir: en el test barato — pero la
lección es mía, no tuya: la refutación estaba a tres líneas de la lógica que usamos todos
los días. En R11 el enemigo es el hueco por ARRIBA cerca de facetas: el esqueleto no puede
(M*=∞ te lo dice), así que el soporte óptimo vive en otra parte — deja que la holgura
complementaria te diga dónde.
