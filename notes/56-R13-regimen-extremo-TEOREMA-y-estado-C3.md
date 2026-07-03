# R13 — TEOREMA del régimen extremo para C₃ cíclico; insuficiencia del acople ingenuo; facetas como máximo local [certificado]; estado honesto del balanceado

> Date: 2026-07-03. Ejecuta `auditorias/61` órdenes R13. **Numeración
> congelada (Rosa lee la pasada 6): CERO cambios al `.tex`** — todo aquí y en
> `experiments/` (`c3_extreme_regime.py`, `r13_2_bounded.py`, ambos con
> verificación exacta, "ALL OK"). Integración al paper: tras el dictamen.

## Resumen en tres líneas

1. **[PROVED] Régimen extremo:** para toda terna cíclica hay un `w₀(τ) > 0`
   explícito tal que toda cobertura de 3 planks con `max r_i ≥ 1 − w₀` tiene
   `Σr ≥ 1`, con igualdad solo trivial. **Primera vez que el caso 2-planks
   cerrado se usa como herramienta**, como ordenaste.
2. **[PROVED] El acople ingenuo NO cierra el balanceado:** las dos cotas
   por-pieza de Gardner admiten `r₂+r₃ = (1875/1094)·l < l+s` en el sandwich
   (exacto) — el acoplamiento de POSICIÓN del caso B es esencial, no un lujo.
3. **[EVIDENCE certificada] Facetas = máximo local (camino simétrico):**
   lazos adaptados dan `D(tilt ε) < 3/2` CERTIFICADO en ε = 1/10, 1/20, 1/50,
   con déficit ~ε². El balanceado general queda [OPEN] con las obstrucciones
   documentadas (incluida una nueva: el desajuste de órdenes).

## 1. Teorema del régimen extremo [PROVED]

**Teorema.** Sea `τ ∈ (0,1)³` cíclica y
```
w₀⁽¹⁾(τ) = ½·min( τ₁, 1−τ₁, (1−τ₂)τ₁/(1+τ₁), τ₃(1−τ₁)/(2−τ₁) ),
w₀(τ)   = min de w₀⁽ⁱ⁾ sobre las tres rotaciones cíclicas ϱ.
```
Toda cobertura de Δ por tres planks `P_i = {u_i ∈ [l_i, h_i]}` (uno por
dirección) con `max_i r_i ≥ 1 − w₀(τ)` cumple `Σr ≥ 1`, con igualdad si y
solo si la cobertura es trivial (un plank lleno y dos de ancho 0).

**Herramienta (2-plank tool).** Si un cuerpo convexo `K' ⊆ Δ` de dimensión 2
está cubierto por `P₂ ∪ P₃` (planks en direcciones no paralelas), entonces
`r₂/w₂(K') + r₃/w₃(K') ≥ 1`, donde `w_j(K') = |u_j(K')|`. *Prueba:* la
medida de anchura relativa de Gardner para dos direcciones SOBRE `K'`
(el argumento del Thm 3.1 corre verbatim en `K'`); cada plank captura a lo
sumo `r_j/w_j(K')` de su masa. ∎ — la primera aplicación del caso 2-planks
resuelto como pieza de una prueba mayor.

**Prueba del teorema** (plank grande = P₁; los otros dos casos por ϱ).
Escribimos `l = l₁`, `s = 1−h₁` (`l+s ≤ w₀`). El resto no cubierto por P₁ es
`K_lo = {u₁ < l}` (esquina en B, vacía ⟺ l=0) y `K_hi = {u₁ > 1−s}`
(esquina en C, vacía ⟺ s=0); como `l,s < min(τ₁, 1−τ₁)`, ambas son
triángulos con vértices `{B, X_AB(l), X_BC(l)}` y `{C, X_CA(s), X_CB(s)}`.
Rangos exactos (u_j afín ⟹ rango = [min,max] sobre los 3 vértices;
verificado simbólicamente):
```
u₂(K_lo) = [1 − l/τ₁, 1]                       extensión a₂ = l/τ₁
u₃(K_lo) = [τ₃(1−l), τ₃ + (1−τ₃)l/τ₁]          extensión a₃ = l·g₂/τ₁
u₂(K_hi) = [τ₂(1−s/(1−τ₁)), τ₂+(1−τ₂)s]        extensión b₂ = s·g₃/(1−τ₁)
u₃(K_hi) = [0, s/(1−τ₁)]                       extensión b₃ = s/(1−τ₁)
```
con `g₂ = 1−τ₃(1−τ₁)`, `g₃ = 1−τ₁(1−τ₂)` (los factores de la dependencia del
Thm 6.13). Los cuatro excesos son estrictos:
`a₂−l = l(1−τ₁)/τ₁ > 0`, `a₃−l = l(1−τ₁)(1−τ₃)/τ₁ > 0`,
`b₂−s = s·τ₁τ₂/(1−τ₁) > 0`, `b₃−s = s·τ₁/(1−τ₁) > 0`.

*Caso A (ningún plank de {P₂,P₃} toca ambas piezas).* Cada pieza no vacía
está cubierta por los planks que la tocan:
- (P₂→lo, P₃→hi): `P₂ ⊇ K_lo ⟹ r₂ ≥ a₂ > l`; `P₃ ⊇ K_hi ⟹ r₃ ≥ b₃ > s`.
- (P₂→hi, P₃→lo): `r₂ ≥ b₂ > s`; `r₃ ≥ a₃ > l`.
- ambos→lo (⟹ s=0): herramienta 2-plank en `K_lo`:
  `r₂/a₂ + r₃/a₃ ≥ 1 ⟹ r₂+r₃ ≥ min(a₂,a₃) = l·g₂/τ₁ ≥ l`
  (estricto: `g₂ − τ₁ = (1−τ₁)(1−τ₃) > 0`).
- ambos→hi (⟹ l=0): `r₂+r₃ ≥ min(b₂,b₃) = s·g₃/(1−τ₁) ≥ s`
  (estricto: `g₃ − (1−τ₁) = τ₁τ₂ > 0`).
- un plank→una pieza, el otro→ninguna: la otra pieza debe ser vacía; caso
  contenido en los anteriores.
En todos: `Σr ≥ (1−l−s) + l + s = 1`, estricto si `l+s > 0`.

*Caso B (algún plank toca ambas piezas).* Sus dos rangos están separados
(por la elección de `w₀`), así que el intervalo debe CRUZAR el hueco:
- P₂ toca ambas: `r₂ ≥ (1 − l/τ₁) − (τ₂ + (1−τ₂)s) = (1−τ₂) − l/τ₁ −
  (1−τ₂)s ≥ l+s`, garantizado por `l,s ≤ w₀ ≤ (1−τ₂)τ₁/(2(1+τ₁))`.
- P₃ toca ambas: `r₃ ≥ τ₃(1−l) − s/(1−τ₁) ≥ l+s`, por
  `w₀ ≤ τ₃(1−τ₁)/(2(2−τ₁))`.
`Σr ≥ (1−l−s) + (l+s) = 1`, estricto si `l+s > 0` (las desigualdades de w₀
tienen holgura de factor 2). ∎

*Verificación a máquina* (`c3_extreme_regime.py`): rangos y extensiones
simbólicos; los cuatro excesos factorizados y positivos (200 muestras
exactas c/u); las implicaciones de caso B en 400 τ aleatorias incluida la
frontera `l=s=w₀`; y 60 configuraciones extremas construidas por la receta
del caso A verificadas contra el oráculo exacto de cobertura (cubren y
`Σr ≥ 1`).

**Corolario (fase del problema).** Cualquier contraejemplo hipotético a
`C₃(u_τ) = 1` vive en el **régimen balanceado**: `r_i < 1 − w₀(τ)` para todo
i — y además `Σ(l_i+s_i) > 2` (pues `Σr = 3 − Σ(l_i+s_i) < 1`).

## 2. Insuficiencia del acople ingenuo [PROVED — obstrucción documentada]

Las dos desigualdades por-pieza de la herramienta 2-plank NO bastan solas:
en el sandwich con `l = s`, el punto de cruce del LP
`{r₂/a₂+r₃/a₃ ≥ 1, r₂/b₂+r₃/b₃ ≥ 1}` da exactamente
```
min(r₂+r₃) = (1875/1094)·l ≈ 1.714·l  <  2l = l+s.
```
El déficit lo cubre en el caso B la **posición** (los rangos de las dos
piezas están lejos: cruzarlos cuesta ~(1−τ₂) o ~τ₃), no el ancho. Cualquier
prueba del balanceado tendrá que acoplar posiciones, no solo anchuras.

## 3. Balanceado: estado honesto y una obstrucción nueva

- Transporte da `Σr ≥ 1/D(u)` siempre (sandwich: ≥ 111/112 ≈ 0.9911); el
  hueco a 1 es el problema.
- **Obstrucción de órdenes (nueva, documentada):** la ruta
  "estabilidad de teselación" (cobertura con `Σr < 1` ⟹ solapes pequeños en
  la medida esquelética ⟹ (l,h) cerca de una de las 3 teselaciones de
  Prop A.1 ⟹ contradicción con MMM/los testigos interiores) NO cierra tal
  cual: el presupuesto de solape que da el transporte es de PRIMER orden en
  la no-concurrencia (`D−1 ≥ 1/224` en el sandwich), mientras la penalización
  canónica del Thm 6.13 es de SEGUNDO orden (`(Π−Q)²/… = 1/12656`). El
  argumento pierde por dos órdenes de magnitud justo donde más se necesita.
  Cerrar exige o mejorar `D` (R13-2b) o un certificado híbrido genuino.
- Fallback sandwich: NO cerrado esta ronda — el balanceado es el bloqueador
  también ahí. `C₃(sandwich) ∈ [111/112, 1]`, extremo cubierto por el
  teorema de arriba con `w₀(13/25,½,½) = min(...) > 0` explícito.

## 4. R13-2 (acotado): facetas como máximo local [certificado]; sandwich sin cambio

- **(a) Lazos adaptados** (`r13_2_bounded.py`): triángulos inscritos
  simétricos `P₀, ϱP₀, ϱ²P₀` con masa uniforme; densidad máxima exacta para
  `P₀` racional (búsqueda float, certificación exacta). Resultados
  CERTIFICADOS:

  | ε | D(tilt ε) ≥ (momentos) | **D(tilt ε) ≤ (lazo)** | déficit vs 3/2 |
  |---|---|---|---|
  | 1/10 | 15/11 ≈ 1.3636 | **135/91 ≈ 1.48352** | 3/182 |
  | 1/20 | 10/7 ≈ 1.42857 | **190/127 ≈ 1.49606** | 1/254 |
  | 1/50 | 25/17 ≈ 1.47059 | **1225/817 ≈ 1.49939** | 1/1634 |

  Los tres UB son **estrictamente < 3/2**: primera evidencia certificada de
  que las facetas son máximo local de `D` (a lo largo del camino simétrico).
  El déficit escala ~ε² [EVIDENCE, 3 puntos]; los `P₀` óptimos quedan sobre
  una arista (lazo inscrito, como en facetas). Familia simbólica
  `UB(ε) = 3/2 − c·ε² + O(ε³)`: candidato natural a teorema de próxima
  ronda (optimizar `P₀ = (0, y, 1−y)` simbólicamente).
- **(b) Sandwich:** dual q=75 adaptado sube la LB solo a `1.0044834`
  (desde 1.0044772); esqueleto por trozos (q=60) NO mejora el uniforme
  (112/111 exacto en ambos): la evidencia apunta a que el esqueleto uniforme
  es óptimo dentro de su clase y el valor verdadero está estrictamente entre
  las cotas. `D(sandwich) ∈ (225/224, 112/111]` sin cambio. [OPEN]

## 5. Qué entra al paper tras el dictamen (cola de integración)

1. Teorema del régimen extremo (§10 / nueva subsección del programa, con la
   herramienta 2-plank como lema); el corolario "todo contraejemplo es
   balanceado".
2. La insuficiencia 1875/1094 como remark del programa (por qué el híbrido).
3. Los tres UB de lazo adaptado < 3/2 (tabla) + su lectura para Prob 10.4.
4. `covering_constant.py` ya citado; añadir `c3_extreme_regime.py` y
   `r13_2_bounded.py` al Appendix B.
