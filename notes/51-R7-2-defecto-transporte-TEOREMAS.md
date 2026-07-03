# R7-2 — El defecto de transporte `D(u)`: sección §7 del paper, con la primera cota dentro del territorio no concurrente

> Date: 2026-07-02. Status: **[PROVED las 4 piezas centrales; EVIDENCE el paisaje;
> OPEN la exactitud de la cota de momentos]**. Ejecuta `auditorias/52 §R7-2`
> (sub-tareas 1, 2, 3-nuevo y 3-viejo completas; 4 parcial como remark + problema).
> Script: `experiments/transport_defect.py` (todo exacto; copiado a ancillary).
> En el paper: §7 (`sec:defect`), Def 7.1, Prop 7.2, Prop 7.3, Thm 7.4, Thm 7.6,
> Cor 7.7, Rem 7.8–7.9, Problem 10.3.

## 1. Definición y propiedades básicas [PROVED — Prop 7.2]

`D(u) = inf {D≥1 : ∃μ∈P(Δ), u_{i#}μ ≤ D·Leb, i=1,2,3}`.

- Ínfimo **alcanzado**: compacidad débil-* + portmanteau sobre `u_i^{-1}(J)` con `J`
  ABIERTO (la dirección correcta de la desigualdad; los cerrados no sirven).
- **`Σrw ≥ 1/D(u)`** para toda cobertura por planks paralelos a las 3 direcciones.
- `D=1 ⟺ concurrencia` (vía Thm 6.8 + el ínfimo alcanzado): `D` es la
  **cuantificación exacta** de la caracterización de R6-5.
- `D ≤ 2` (medida uniforme, estimación per-plank de Thm 2.1).

## 2. Cota de momentos [PROVED — Prop 7.3]

Defecto de concurrencia `δ(u) = min_{p∈Δ} max_i |u_i(p)−½|` (alcanzado; `=0 ⟺`
concurrencia; `<½` siempre). Densidad `≤D` con masa 1 ⟹ media `∈[1/(2D), 1−1/(2D)]`
(vía `∫(1−F)` con `F ≤ min(1,Dt)` — constantes verificadas con cuidado, como pidió la
orden). Media de `u_{i#}μ` = `u_i(baricentro)` ⟹ **`D(u) ≥ 1/(1−2δ(u))`**.
Facetas: `Σλ_i=1 ⟹ δ=1/6 ⟹ D≥3/2` (dos líneas, como anticipó la orden).

## 3. `D(facetas) = 3/2` EXACTO [PROVED — Thm 7.4] — y sin LP

La orden preveía ansatz S₃ o LP; salió mejor: **construcción explícita a mano**.
La medida uniforme sobre el perímetro del triángulo inscrito
`P₀=(0,⅓,⅔), P₁=(⅔,0,⅓), P₂=(⅓,⅔,0)` (vértices alternos del hexágono `{λ_i≤⅔}`,
masa ⅓ por lado) tiene las TRES marginales `= (3/2)·1_{[0,2/3]}`: cada `λ_i` recorre
`0→⅔` en un lado (densidad ½) y baja por las dos mitades en los otros (densidad 1).
La cota inferior de momentos es tight en facetas. Cierra la pareja metodológica:
teselación certifica 1 (Thm 3.2), transporte certifica exactamente `1/D = 2/3`
(Rem 7.5). [Equivale a la 3-mezclabilidad completa de la uniforme; nuestra prueba es
autocontenida y elemental.]

## 4. El foco nuevo: módulo lineal cerca de la superficie [PROVED — Thm 7.6, Cor 7.7]

**Thm 7.6.** `τ*` cíclico concurrente con masas `(α,β,γ)`, `m = min_i min(τ_i*,1−τ_i*)`;
`τ` cíclico con `ε = max|τ_i−τ_i*| < m`. La medida de esqueleto con **pesos congelados**
`(γ,α,β)` empujada por las direcciones perturbadas tiene las 6 densidades en
`1 ± ε·w*/(τ τ*)`, luego

```
D(u_τ) ≤ 1 + ε/(m(m−ε))      y      Σrw ≥ 1 − ε/(m(m−ε)).
```

**Cor 7.7 (la primera cota en territorio abierto real).** Con `τ*=medianas` (`m=½`),
`ε=1/60`: pérdida `= 2/29`, y

```
Σrw ≥ 27/29 ≈ 0.93103  >  4√3−6 ≈ 0.92820      (40401 > 40368, exacto)
```

para TODA `τ` cíclica con `max|τ_i−½| ≤ 1/60` — un entorno 3-dimensional lleno cuyo
locus concurrente es codim-1: **casi todas esas ternas son genuinamente no
concurrentes, no existe medida testigo (Thm 6.8), y aun así batimos la constante
general de B-Y**. Exactamente lo que pedía R7-2.3.
Con la cota inferior de §2 (`D ≥ 1/(1−2δ) > 1` fuera de la superficie), el módulo de
`D` en la superficie es **lineal por ambos lados**.

**Advertencia vigente (Rem 7.8, en el paper):** B-Y es uniforme sobre TODAS las
ternas; nuestra mejora es local. Lejos de la superficie el método degrada sin remedio
(facetas: 2/3). Sin overclaim.

## 5. Paisaje y lo que queda [EVIDENCE / OPEN]

- **Sandwich exacto** en muestras no concurrentes (Rem 7.9):
  `τ=(13/25,½,½)`: `225/224 ≤ D ≤ 112/111` (LP de esqueleto exacto, pesos óptimos
  `(38/111, 1/3, 12/37)`); `τ=(7/10,2/5,½)`: `223/218 ≤ D ≤ 109/104`. [PROVED cada
  cota; el valor exacto de `D` en medio queda abierto.]
- **Barrido `δ`** (9 ternas exactas variadas): máximo `δ = 1/6` en facetas; los `δ=0`
  del barrido son exactamente ternas concurrentes (sanity ✓). [EVIDENCE]
- **Problema 10.3 (nuevo en el paper):** ¿`D(u) = 1/(1−2δ(u))` siempre? ¿`sup D = 3/2`
  en facetas? Mi conjetura inicial de que el lazo inscrito lo da en general **fracasó**
  y es instructivo: el sistema del lazo (9 ecs) es estructuralmente singular — la
  dependencia afín `Σν_iu_i ≡ const` fuerza `Σν_iκ_i = 0` sobre offsets ENTEROS
  `κ_i∈{±1,±2}`, y eso solo pasa donde `ν` admite relación entera (medianas y facetas:
  `ν∝(1,1,1)`, `κ=(2,−1,−1)`). Los lazos de 3 segmentos con masas iguales NO existen
  genéricamente; la clase siguiente (masas desiguales, cobertura doble por tramos =
  6 ecuaciones en 8 incógnitas) es la maquinaria natural para atacar 10.3. [OPEN]

## 6. R7-3 (decisión editorial, delegada): título — SE MANTIENE

Decisión: conservar *"Transport and tiling bounds for the affine plank problem on the
triangle"*. Razones: (a) con §8 el paper ya no es solo "on the triangle" en sentido
estricto, pero el grueso sí — y el título propuesto ("…sharp families, a
three-direction characterization, and obstructions") es una lista larga sin nombrar
los métodos; (b) doña Rosa audita la pasada 3 contra el título congelado — cambiarlo
entre pasadas confunde; (c) el cierre de Gardner-N=3 ya está en abstract, intro y
Rem tras Thm 6.8. Revisitar tras su dictamen si el jefe discrepa.
