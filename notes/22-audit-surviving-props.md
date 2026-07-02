# [AUDITORÍA] Las 4 propuestas "supervivientes" del muro m≥4 — todas falladas
> Auditoría adversarial, mismo estándar que refutó toric/flow/Helly/entropía.
> NINGUNA de estas 4 demuestra el caso m=4. La conjetura sigue abierta.
> Date: 2026-06-29.

Tras las 4 refutaciones honestas (Prop 1 toric, 3 flow, 4 Helly, 5 entropía),
quedaron 4 vías marcadas como "pilares". Sometidas a la misma auditoría, caen.
**Patrón común:** todas confirman numéricamente que la conjetura es VERDADERA
(no existe cobertura sub-1) — cosa ya sabida con el ILP exacto — pero ninguna
produce una desigualdad PROBADA. Confirmar ≠ demostrar.

## [REFUTADA] Prop 6 — Zonotopo / Función de Soporte
**Afirmación:** cubrir ⟹ `W_Z(v) ≥ W_Δ(v)` ∀v, con `W_Z(v)=Σ wᵢ|⟨uᵢ,v⟩|`.
**Falla fatal (verificada por máquina, `audit_zonotope.py`):** el postulado es FALSO.
- Las **3 planchas de faceta** (cobertura de Hunter, Σrw=1, válida) violan
  `W_Z(v) ≥ W_Δ(v)` en **360/360 direcciones** (`W_Z=1.0 < W_Δ=1.504`).
- 3 planchas paralelas (cobertura 1-dirección, Σrw=1) lo violan en 240/360.
**Razón estructural:** el zonotopo Z depende solo de normales y anchos, NO de las
posiciones; cubrir SÍ depende de la posición. Por tanto ninguna función de Z puede
certificar cobertura (trasladar una cobertura a una no-cobertura no cambia Z). Es
exactamente la ruta "Farkas posición-independiente" ya catalogada como refutada.
El "500/500 falla a Σ=0.95" solo dice `Σrw<1 ⟹ Z angosto`, irrelevante para cubrir.

## [REFUTADA] Prop 2 — Topología / Teorema del Nervio (KKM cúbico)
**Afirmación:** `Σ|Iⱼ|<1 ⟹` el nervio 𝒩 no es contráctil ⟹ hay hueco.
**Falla 1 (circularidad):** el lema "ancho chico ⟹ nervio no-contráctil" se AFIRMA
sin prueba; el vínculo ancho↔topología ES la conjetura. No se establece nada.
**Falla 2 (falso como detector):** cuando el punto libre está en el BORDE de Q
—que es donde está: medimos 54% de la masa del certificado en las aristas, 0% en
vértices— la unión `∪Aⱼ = Q` menos un mordisco de borde **sigue siendo contráctil**
(β₁=0). El nervio no da señal aunque la cobertura falle. El teorema del nervio dice
`𝒩 ≃ ∪Aⱼ`; si la falla es de borde, `∪Aⱼ` es contráctil y 𝒩 también. La topología
solo detectaría un hueco INTERIOR rodeado, que no es el modo de falla real.

## [REFUTADA] Prop 7/16 — Rigidez Geométrica KKT
**Afirmación:** las condiciones KKT del óptimo fuerzan ≤5 testigos rígidos que no
pueden sellar Δ con presupuesto <1.
**Falla fatal:** las condiciones KKT son necesarias EN el óptimo, pero **no prueban
que el valor óptimo sea ≥1** — eso se asume de entrada ("asumiendo Σrw=1"). El
"oráculo demostró gap>0" es la confirmación ILP que ya teníamos, re-vestida. La
conclusión "5 puntos rígidos no sellan bajo presupuesto<1" se afirma, nunca se
demuestra (no hay cota que ligue nº de testigos × presupuesto con la cobertura).
La "ley de separación rígida" `(xᵢ⁺−xᵢ⁻)/wᵢ = ∇w_Δ/w_Δ` es una condición de
estacionariedad correcta, pero no implica la desigualdad buscada.

## [REFUTADA] Prop 17 — Fuerza Bruta Semialgebraica (Positivstellensatz)
**Afirmación:** 227M celdas con aritmética de intervalos certifican que no hay
cobertura sub-1 en el espacio de 11 dimensiones (computer-assisted proof).
**Falla fatal:** 227M celdas / 11 dim ≈ **6.5 subdivisiones por dimensión** — muy
lejos del refinamiento que exige un certificado riguroso de intervalos. Cerca de la
frontera tight `{Σrw=1}` el **margen → 0**, por lo que `Lipschitz × tamaño_celda`
excede el margen y **ninguna grilla finita certifica** ahí. Además no se exhibe
ningún certificado SOS/Positivstellensatz (identidad algebraica) — es muestreo en
grilla, equivalente a nuestro ILP. Confirma que la conjetura es cierta; no la prueba.

## Conclusión
Las 4 vías "supervivientes" están **refutadas o son confirmaciones disfrazadas**.
El caso m≥4 del triángulo **permanece abierto**, en línea con el campo (Bakaev–
Yehudayoff 2026 es la frontera viva). No debe presentarse como demostrado.
Lo rescatable (firme) se lista en `23-firm-knowledge-rescued.md`.
