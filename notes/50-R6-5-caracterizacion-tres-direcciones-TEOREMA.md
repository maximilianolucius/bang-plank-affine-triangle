# R6-5 — TEOREMA: los patrones mixtos se disuelven; caracterización completa para 3 direcciones (Thm 6.8)

> Date: 2026-07-02. Status: **[PROVED — prueba humana en el paper + barrido exhaustivo
> exacto de los 216 patrones]**. Resuelve R6-5 entero y con un desenlace más fuerte que
> el pedido ("clasificar y decidir"): no hay que decidir nada patrón por patrón — la
> pregunta de suficiencia queda **cerrada para TODA terna** de direcciones no paralelas
> dos a dos en el triángulo.
> Script: `experiments/role_patterns_classification.py` (216/216 patrones, exacto).

## 1. La observación que colapsa todo: invariancia por flip

El problema de planks es invariante bajo `u ↦ 1−u, I ↦ 1−I` **por dirección**: mismo
plank, mismo ancho, marginal uniforme ⟺ uniforme, y la recta `{u=½}` queda fija.
Módulo flips, lo único que importa de la asignación de roles de una dirección es su
**arista llena** (la que une su vértice-0 con su vértice-1). Tres clases:

1. **Aristas llenas distintas** (48/216 patrones): los flips orientan el ciclo ⟹
   **toda** esta clase es la familia cíclica (el anti-cíclico incluido: flip de las 3).
   Los "mixtos con mismo vértice-0" de `notes/49-R5-3 §3` estaban aquí — eran cíclicos
   disfrazados.
2. **Exactamente dos comparten arista llena** (144/216): **nunca concurren**. Prueba:
   tras un flip `uᵢ−uⱼ = (τᵢ−τⱼ)x_v` (v = vértice opuesto a la arista compartida `e`);
   sus mid-lines se cortan solo en el punto medio de `e`; la tercera dirección no es
   llena en `e` y en ese punto vale `τ_k/2` o `(1+τ_k)/2 ≠ ½`. Consistentemente,
   tampoco hay medida: `E[uᵢ]=E[uⱼ]=½ ⟹ E[x_v]=0 ⟹ supp μ ⊂ e`, donde `u_k` no es
   sobreyectiva a `[0,1]`. **Clase vacía para ambos lados del iff.**
3. **Las tres comparten arista llena** (24/216): concurren **siempre** (en el punto
   medio de la arista, borde); la medida uniforme **sobre la arista** es testigo
   trivial, y `Σrw≥1` sale de cubrir la arista sola (caso 1-D).

## 2. Teorema (Thm 6.8 del paper)

**Para `u₁,u₂,u₃` normalizadas, no paralelas dos a dos: existe `μ` con
`u_{i#}μ = Leb[0,1]` ∀i ⟺ las tres rectas `{uᵢ=½}` tienen un punto común.**
Y en ese caso `Σrw ≥ 1` para toda cobertura, con dicotomía: (a) punto interior ⟹
cíclica módulo flips ⟹ Thm 6.3 (medida `μ_p`) + Thm 6.6 (tight única);
(b) punto = medio de arista ⟹ las tres llenas en esa arista, medida = uniforme en la
arista, cota trivial.

- La necesidad no usa invertibilidad de `V` (solo baricentro).
- Responde **completamente** la pregunta de existencia de Gardner para N=3 en el
  triángulo. El caso abierto de Bang en el triángulo queda reducido EXACTAMENTE a las
  ternas **no concurrentes** (donde ninguna medida única puede funcionar — ahí el
  método de transporte simple muere y se necesita acoplamiento/otra idea).

## 3. Verificación exhaustiva

Barrido sympy de los 6³=216 patrones ordenados `(v₀,v₁)³`: para cada uno, condición
exacta de concurrencia (`Σp=1` con `Vp=½·1`):
- 48 con aristas distintas: superficie 2-paramétrica (la relación cíclica y sus
  transformadas por flip). ✓
- 144 con dos compartidas: `R(τ)=0` sin raíces en `(0,1)³` (formas `−t/2`, `(1−t)/2t`,
  `−½`, o `det V=0` inconsistente), **o** raíces solo en `τⱼ+τ_k=1` ⟹ tras flip las
  dos direcciones coinciden (degenerado, no es terna). ✓
- 24 con una sola: siempre resoluble, `p = punto medio` del lado. ✓

## 4. Nota sobre la evidencia LP previa (punto 3 de la orden R6-5)

La pregunta "¿las 453 ternas del LP de `notes/37` incluían mixtos?" queda **moot**:
todo triple concurrente es cíclico-módulo-flips o del caso trivial de arista; no
existen "mixtos concurrentes" que testear. La evidencia LP 453/453 estaba
necesariamente dentro de la clase hoy probada.
