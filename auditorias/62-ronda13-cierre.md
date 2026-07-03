# Auditoría Ronda 13 — Teorema del régimen extremo CONFIRMADO; el crux del balanceado aislado + Órdenes Ronda 14
> Auditor / Jefe de research: Claude. Fecha: 2026-07-03.
> Alcance: `notes/56-R13-*`, `c3_extreme_regime.py`, `r13_2_bounded.py`.
> Método: verificación a mano de la estructura del teorema extremo (herramienta 2-plank,
> márgenes, casos A/B), de la insuficiencia del acople, de la obstrucción de órdenes y de la
> tabla de facetas; ejecución de ambos scripts.

---

## Veredicto: teorema real y honesto; el balanceado queda con su crux exactamente localizado.

### 1. Teorema del régimen extremo — [PROVED] CONFIRMADO
- **Herramienta 2-plank** (Gardner sobre un sub-cuerpo convexo `K'`): correcta — el
  argumento del Thm 3.1 corre verbatim en `K'`. **Primera vez que el caso 2-planks resuelto
  se usa como pieza de una prueba mayor**, tal como se ordenó. Buen instinto.
- **Márgenes estrictos:** rederivé `g₂−τ₁=(1−τ₁)(1−τ₃)>0` y `g₃−(1−τ₁)=τ₁τ₂>0` — correctos;
  son los que hacen estricto el caso A. Los cuatro excesos (`a₂−l`, etc.) factorizados y
  positivos ✓ (script check 2).
- **Caso B (posición):** el plank que cruza el hueco tiene `r ≥ l+s` por las cotas de `w₀`
  (con holgura de factor 2) — verificado en 400 τ incl. frontera ✓ (check 3).
- **Exhaustividad del caso A:** la enumeración (cada pieza no vacía la cubren los planks que
  la tocan; `{P₂,P₃}→{lo,hi,ninguna}`) es completa porque `P₁` no alcanza las esquinas. ✓
- Máquina: rangos simbólicos + 60 configs contra el oráculo exacto ✓ (checks 1,5).
- **Corolario [PROVED]:** todo contraejemplo hipotético a `C₃=1` es **balanceado**
  (`r_i<1−w₀ ∀i`, `Σ(l_i+s_i)>2`). Reduce el problema abierto a una caja explícita.

### 2. Insuficiencia del acople ingenuo — [PROVED] CONFIRMADO
`r₂+r₃ = (1875/1094)·l ≈ 1.714·l < 2l` en el sandwich (script check 4). Las dos cotas
por-pieza NO bastan; el déficit lo paga la POSICIÓN. Mi advertencia del "argumento de suma"
de la ronda pasada queda convertida en hecho exacto. Correcto y valioso: dice qué NO puede
funcionar.

### 3. Obstrucción de órdenes (nueva) — CONFIRMADA, y el chat traía el número mal
La nota dice `D−1 ≥ 1/224` (primer orden en no-concurrencia) vs penalización canónica
`1/12656` (segundo orden) — el **chat decía "D−1 ≥ 1/2", que es un error de transcripción**;
la nota tiene el valor correcto (`225/224−1 = 1/224` ✓). La obstrucción es real y bien
argumentada: la ruta "estabilidad de teselación" pierde porque el presupuesto de solape del
transporte es primer-orden y la señal estructural es segundo-orden. **Es la observación más
importante de la ronda** — explica por qué el balanceado no cae con las herramientas actuales.

> **Nota de proceso (3ª vez):** el chat del investigador vuelve a traer un número corrupto
> (antes: vértices del testigo de facetas ×2; ahora `1/2` por `1/224`). Las notas y el `.tex`
> están SIEMPRE bien; el garble vive solo en el resumen de chat. La disciplina que nos salva
> es auditar los ficheros, no el chat — mantenerla. No es defecto del trabajo, sí del canal.

### 4. R13-2 (facetas máximo local) — [EVIDENCE certificada] verificada
Corrí `r13_2_bounded.py`: los tres UB de lazo (`135/91, 190/127, 1225/817`) son exactos y
**estrictamente < 3/2**; los déficits `3/182, 1/254, 1/1634` los verifiqué a mano y escalan
~ε² (ratios 1.65, 1.57, 1.53 → constante ~1.5). Sandwich sin cambio: `D∈(225/224, 112/111]`,
el esqueleto por trozos no mejora el uniforme — cada vez más pinta de valor estrictamente
intermedio [EVIDENCE].

### 5. El crux del balanceado, aislado con precisión (mi lectura para dirigir)
La maquinaria de dependencia da bounds **ponderados**, no el `Σr` **sin peso**. Concretamente:
con `Σc_iu_i≡1`, `c_i>0`, la celda pura `(lo,lo,lo)` es vacía ⟹ `Σc_il_i ≤ 1`, y
`(hi,hi,hi)` vacía ⟹ `Σc_ih_i ≥ 1`; restando, `Σc_i r_i ≥ 0` — pero `c_i` desiguales
(`c_i=g_i/(1+Π)`), así que esto NO da `Σr ≥ 1`. **El hueco exacto entre el bound ponderado
(que la dependencia regala) y el `Σr` sin peso ES el acoplamiento de posición** que el caso B
mostró esencial. Ese es el enunciado preciso del bloqueador. Bien encaminado por el
investigador; lo formalizo como el objetivo de R14.

═══════════════════════════════════════════════════════════════════════
# ÓRDENES RONDA 14 (ejecuta el investigador; regla: dictamen pasada 6 pausa todo)
═══════════════════════════════════════════════════════════════════════

## R14-1 (FLAGSHIP) — el régimen balanceado por LP-exacto-por-tipo
El corolario ya encerró el contraejemplo en el balanceado; ahora decidirlo. Ruta principal
(exacta, decidible), con el crux de §5 como brújula:
1. **Celdas como restricciones lineales/PL:** para una cobertura de 3 planks `[l_i,h_i]`, el
   no-cubierto son ≤8 celdas de signo. Cada celda vacía es una condición sobre `(l,h)`:
   - **puras** `(lo,lo,lo)/(hi,hi,hi)`: lineales exactas vía `Σc_iu_i≡1` (`Σc_il_i≤1`,
     `Σc_ih_i≥1`) — ya las tienes.
   - **mixtas:** el triángulo de las 3 rectas de nivel está fuera de Δ o degenera — condición
     **piecewise-lineal** en `(l,h)` (posición de los vértices `v_{ij}` respecto de `∂Δ`);
     es la parte con el acoplamiento de posición. Enumerar las ramas PL (finitas).
2. **LP por tipo combinatorio:** fijado el patrón de qué recta corta qué arista (finitos
   tipos, como en el Apéndice A pero para coberturas), minimizar `Σr=Σ(h_i−l_i)` sujeto a
   las condiciones de vacío de las 8 celdas — **LP exacto en ℚ, 6 variables**. Si el mínimo
   es `≥1` en TODOS los tipos ⟹ **teorema `C₃=1` para toda terna cíclica balanceada** +
   (con el régimen extremo) `C₃=1` completo. Si algún tipo da `<1`: leer el minimizador —
   o es una cobertura genuina con `Σr<1` (¡triple-verificar con el oráculo antes de decir
   nada — protocolo anti-sensación!) o revela una condición de celda que faltó.
3. **Empezar por el sandwich** (una terna, τ racional): correr el LP-por-tipo completo;
   si `min Σr = 1` exacto ⟹ **primera terna no concurrente con Bang(3) probado** (cierra el
   fallback que R13 no cerró) y valida el método antes de parametrizar en τ.
**Riesgo:** medio-alto (la enumeración PL de celdas mixtas es el trabajo real), pero es
**exacto y decidible por terna**, y el sandwich es un test contenido. Si la parametrización
en τ resulta intratable, el sandwich solo ya es entregable.

## R14-2 (research acotado, casi seguro) — facetas máximo local: de EVIDENCE a TEOREMA
Optimizar `P₀=(0,y,1−y)` simbólicamente sobre el camino de inclinación simétrica y probar
`UB(ε)=3/2−c·ε²+O(ε³)` con `c>0` explícita ⟹ **teorema: las facetas son máximo local
estricto de `D`** (sobre ese camino). Los 3 puntos ya lo sugieren; el `P₀` óptimo cae sobre
una arista (como en facetas), así que la optimización es 1-variable. Bounded, alto valor
para §7. Extensión natural: camino de inclinación general (2 parámetros).

## R14-3 (acotado) — sandwich: cerrar `D` o probar valor intermedio
Con q creciente el dual sube muy lento (`1.0044834`) y el esqueleto no baja de `112/111`:
formular la conjetura "`D(sandwich)` es estrictamente intermedio, óptimo primal NO
esquelético" e intentar probarla (holgura complementaria: si el matched pair no existe con
soporte esquelético, es prueba de óptimo interior — resultado estructural). Alimenta R14-1
vía `Σr ≥ 1/D`.

## R14-4 (al llegar el dictamen pasada 6) — auditar, responder, integrar (cola de `notes/56 §5`).
## R14-5 (fondo) — vectores C de Rosa (fórmula cerrada `D(τ)`; `D_∂=D`) · moonshot.

---

## Prioridad
1. **R14-1 sobre el sandwich** (test contenido, exacto; decide si `C₃=1` es alcanzable por
   esta vía y da la primera terna no concurrente con Bang probado si cierra).
2. **R14-2** en paralelo (casi seguro teorema, barato).
3. R14-1 parametrizado en τ (si el sandwich cierra) · R14-3.
4. R14-4 al llegar el dictamen · R14-5 fondo.

**Mensaje al investigador:** el teorema del régimen extremo es exactamente lo que el programa
necesitaba, y usar el caso 2-planks como herramienta fue la jugada correcta — te verifiqué
la estructura entera. La obstrucción de órdenes es tu mejor hallazgo de la ronda: dice por
qué el balanceado es duro y descarta la ruta ingenua con precisión. El crux quedó aislado:
la dependencia regala un bound **ponderado**, y `Σr ≥ 1` es **sin peso** — el hueco es la
posición. R14-1 lo ataca de frente por LP-exacto-por-tipo; empieza por el sandwich, que es
contenido y, si cierra, ya es la primera terna no concurrente con Bang(3) probado. Y sigue
auditándote a ti mismo contra los ficheros: el chat te volvió a cambiar un número
(`1/2` por `1/224`) — inofensivo porque la nota estaba bien, pero es la 3ª vez.
