# R14 — TEOREMA: facetas máximo local estricto (camino simétrico, cotas cerradas); B&B exacto del balanceado en el sandwich (arquitectura validada, run largo en curso)

> Date: 2026-07-03. Ejecuta `auditorias/62` (Ronda 14). **Numeración
> congelada (Rosa lee la pasada 6): CERO cambios al `.tex`.**
> Scripts: `tilt_local_max.py` (teorema, ALL OK) y `c3_balanced_bb.py`
> (B&B exacto; dos runs de 6 min documentados; run largo de 55 min lanzado
> con checkpoint `bb_frontier.txt`). Nota de proceso del jefe aplicada:
> **todos los números de esta nota están copiados de salidas de script, no
> de memoria.**

## R14-2 — TEOREMA (de EVIDENCE a probado, como ordenaste)

**Teorema (máximo local estricto en el camino de inclinación simétrica).**
Para `ε ∈ (0, ½)`, sea `u_tilt(ε)` la terna cíclico-simétrica con valores de
vértice `(1,ε,0), (0,1,ε), (ε,0,1)`. Entonces
```
(3/2)/(1+ε)  ≤  D(u_tilt(ε))  ≤  (3/2)·(1−ε)/(1−ε+ε²)  <  3/2 .
```
En particular las facetas (`ε=0`, `D=3/2`) son **máximo local estricto** de
`D` a lo largo del camino, con
`UB(ε) = 3/2 − (3/2)ε² + O(ε³)` — la constante `c = 3/2` explícita que
pediste.

*Prueba.* **Cota inferior:** la dependencia es `Σuᵢ ≡ 1+ε` (`c=(1,1,1)`,
verificado coordenada a coordenada), luego
`δ = δ_c = |1+ε−3/2|/3 = (½−ε)/3` (Thm 7.11) y la cota de momentos da
`(3/2)/(1+ε)`. **Cota superior:** el lazo inscrito simétrico por
`P₀ = (x*, 1−x*, 0)` en la arista AB y sus dos rotaciones cíclicas (masa 1/3
uniforme por lado), con la elección igualadora
```
x*(ε) = (1−2ε)/(3(1−ε)) .
```
Los valores de `u₁` en los vértices del lazo son
`v₁ = εx* < v₀ = x*+ε(1−x*) < v₂ = 1−x*` (positividad de las tres
longitudes verificada), la marginal tiene exactamente dos ramas de densidad
y AMBAS valen `(3/2)(1−ε)/(1−ε+ε²)` en `x*` (la igualación es precisamente
la ecuación que define `x*`); masa total 1; por la simetría cíclica las tres
marginales coinciden. Estrictamente `< 3/2` porque
`(1−ε)/(1−ε+ε²) < 1 ⟺ ε² > 0`. ∎

Chequeos (`tilt_local_max.py`, todo simbólico): ramas iguales, masa 1,
igualación ⟺ x*, expansión en ε², y los tres puntos certificados de R13
reproducidos EXACTAMENTE: `UB(1/10) = 135/91`, `UB(1/20) = 190/127`,
`UB(1/50) = 1225/817`. (La extensión al camino de inclinación general de 2
parámetros queda para otra ronda.)

## R14-1 — B&B exacto del balanceado (sandwich): arquitectura montada y validada; decisión en curso

**Reformulación implementada** (equivalente al LP-por-tipo, y más robusta de
implementar exactamente): la región de coberturas es cerrada y PL; decidimos
"`¬∃` cobertura balanceada con `Σr ≤ 1`" por branch-and-bound sobre cajas de
`[0,1]⁶` con TRES certificados exactos por caja (todo en `fractions`):
- **P1**: `min Σr` sobre la caja `> 1` ⟹ caja irrelevante.
- **P2**: algún `rᵢ ≥ 1−w₀` en toda la caja ⟹ régimen extremo (teorema R13).
  `w₀(sandwich) = 2/25` (mínimo sobre las 3 rotaciones, calculado en
  script; balanceado ⟺ `rᵢ ≤ 23/25`).
- **P4** (añadida tras el run 1): algún plank vacío en toda la caja
  (`min lᵢ > max hᵢ`) ⟹ cobertura por ≤2 planks en 2 direcciones ⟹
  **Thm 3.1 da `Σr ≥ 1` analíticamente** — segunda vez que el caso 2-planks
  trabaja como herramienta.
- **P3**: la configuración AGRANDADA `Iᵢ⁺ = [min lᵢ, max hᵢ]` (superconjunto
  de todo plank de la caja) NO cubre ⟹ toda la caja falla. Test de fallo
  **completo y exacto**: (a) arista no cubierta por las trazas agrandadas
  (1-D exacto) — atrapa los no-cubiertos de borde; (b) celda de signo con
  **área positiva** dentro de Δ (clipping de polígonos exacto + shoelace) —
  atrapa los interiores (un no-cubierto interior tiene disco en su celda
  estricta). [Completitud probada en el docstring; sin ε numéricos: área>0
  exacta basta.]
- Si nada aplica: partir la coordenada más ancha.

**Si el árbol se vacía:** toda cobertura del sandwich tiene `Σr ≥ 1`
(extremo por el teorema R13; planks vacíos por Thm 3.1; resto por el árbol)
⟹ **`C₃(sandwich) = 1`** — primera terna no concurrente con Bang(3) probado
— con igualdad solo en las triviales y, a lo sumo, en coberturas tight de 2
planks con el tercero vacío (la clasificación de igualdad 2-plank queda como
apartado propio). Naturaleza: **computer-assisted con aritmética racional
exacta** (certificado = el árbol; requerirá extender el protocolo del
Appendix B y avisar a Rosa — decisión de presentación para el jefe).

**Estado de los runs (números de las salidas):**
- Run 1 (sin P4, 360 s): 1 273 547 cajas, frontera 21 — se atascaba en cajas
  con plank 1 vacío (configuraciones 2-plank casi-tight que el B&B solo
  puede excluir geométricamente a escala fina). Diagnóstico ⟹ P4.
- Run 2 (con P4, 360 s): 857 117 cajas, podas P1=149 964, P2=28 155,
  P3=228 038, P4=22 390; frontera 23 (DFS). El zoom vivo está donde debía:
  cajas alrededor de la variedad casi-tight de MMM (la caja muestra
  `l≈(0.325, 0.35, 0.315)`, `h≈(0.68, 0.65, 0.67)`, comparar
  `λ = (39,38,37)/113 ≈ (0.345, 0.336, 0.327)`,
  `ρ = (19/28, 37/56, 75/112) ≈ (0.679, 0.661, 0.670)`) — consistente con
  que la exclusión ahí requiere escala `~1/12656` (el exceso canónico).
- **RUN LARGO COMPLETADO — ÁRBOL VACÍO** (números de la salida):
  `processed 1625301 boxes in 683s; prunes P1=286024 P2=53907 P3=431026
  P4=41694, splits=812650; QUEUE EMPTY`. Con el teorema del régimen extremo
  (R13) y el Thm 3.1 para los planks vacíos:

  > **TEOREMA (computer-assisted, aritmética racional exacta).**
  > `C₃(sandwich) = 1`: toda cobertura del triángulo por tres planks (uno
  > por dirección de la terna `τ=(13/25,½,½)`) cumple `Σr ≥ 1`, con igualdad
  > solo en las coberturas triviales (un plank lleno) y, a lo sumo, en
  > coberturas tight de 2 planks con el tercero vacío.
  > **Primera terna NO CONCURRENTE del triángulo con Bang(3) probado.**

  Descomposición de la prueba: (i) régimen extremo (`max rᵢ ≥ 23/25`):
  teorema R13, analítico; (ii) algún plank vacío: Thm 3.1 (2 direcciones),
  analítico; (iii) resto (balanceado, 3 planks no vacíos, `Σr ≤ 1`):
  vacío por el árbol B&B exacto — determinista y reproducible (el script es
  el certificado; DFS con particiones deterministas).
  **Verificación independiente — CONFIRMADA (con corrección de proceso).**
  El 1er intento (round-robin) salió bit-idéntico al run principal
  (1 625 301 cajas, mismas podas): el parche no enganchó ⟹ era la MISMA
  corrida, no una verificación. Detectado y descartado (no cuenta).
  2º intento, genuinamente independiente: terna ROTADA
  `τ=(½,½,13/25)` (misma afirmación, geometría reetiquetada) + ratio de
  partición NO diádico `5/11` ⟹ árbol completamente distinto. Salida:
  `processed 1040919 boxes in 400s; prunes P1=158916 P2=65811 P3=257533
  P4=38200; QUEUE EMPTY`. **Números distintos (1.04M vs 1.63M cajas, podas
  distintas), mismo veredicto** ⟹ confirmación real, no un re-run.
  Naturaleza computer-assisted: requiere decisión de presentación del jefe +
  extensión del protocolo del Appendix B antes de entrar al paper.

**Lección estructural de la ronda** (para R15 si el run no cierra): el B&B
converge rápido en el interior del balanceado; las DOS bandas que piden
lemas analíticos son los degenerados: (i) plank grande — YA teorema (R13);
(ii) **plank fino** (`rᵢ → 0`, configuraciones casi-2-plank) — P4 cubre el
caso exactamente vacío, pero la banda `0 < rᵢ ≪ 1` es el espejo del régimen
extremo y pide su propio "thin-plank lemma" (el candidato natural: piezas
`{u₁<l}`, `{u₁>h}` GRANDES, extensiones por-pieza cercanas a 1, y las
mismas dos desigualdades de Gardner por pieza que en el caso pequeño eran
insuficientes aquí aprietan). Es la próxima pieza del programa.

## R14-3 (acotado) — conjetura formalizada

**Conjetura (sandwich intermedio).** `D(sandwich) ∈ (225/224, 112/111)`
estricto, y ningún óptimo primal es esquelético. Soporte: el dual sube muy
lento con los nudos (`225/224 = 1.0044643 → 1.0044834` con q=75) y el
esqueleto por trozos no baja de `112/111` (q=60 = uniforme exacto). Ruta de
prueba estructural (holgura complementaria, Prop 7.13): si `D = 112/111`,
todo par óptimo obliga a `ψ` a anularse en las holguras del esqueleto y a
que el conjunto de contacto soporte la medida esquelética — condiciones
finitas comprobables sobre los breakpoints; si son incompatibles ⟹ óptimo
interior [resultado estructural]. No ejecutado esta ronda (presupuesto al
B&B); en cola.

## Cola / pendientes

- Run largo del B&B: reportar al completar (teorema o frontera+diagnóstico).
- R14-1 parametrizado en τ: solo si el sandwich cierra.
- Thin-plank lemma (banda `rᵢ` pequeño): candidato R15.
- R14-4: al llegar el dictamen de la pasada 6, TODO se pausa.
- Integración al paper (congelado): teorema tilt → §7 (junto a Thm 7.5);
  B&B → programa del §10 + protocolo Appendix B extendido si cierra.
