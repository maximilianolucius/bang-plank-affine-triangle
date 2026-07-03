# R12 — Paquete de entrega: sexta pasada de doña Rosa

> Date: 2026-07-03. Status: **[LISTO — entrega el jefe]**. Versión congelada:
> `drafts/entregas/affine-plank-triangle-2026-07-03-pasada6.{pdf,tex}`
> (**31 pp**; 0 errores / 0 undefined / 0 overfull). Integra: todos sus puntos
> aceptados de la pasada 5, el paquete R10 (descongelado) y los resultados
> nuevos de la Ronda 12 (cobertura canónica, programa C(u)).

## Mensaje sugerido para doña Rosa

Doña Rosa: esta revisión ejecuta todos los puntos de su quinta lectura —
incluida su mejora de la constante, que adoptamos tal cual (29/31) — e
integra el material que teníamos retenido para no mover su numeración
mientras leía. Dos precisiones: (i) en el Pocket Lemma su objeción parte de
una lectura sin la clausura: el enunciado ya decía `P̄∩∂Δ` finito; añadimos
la palabra "closure" en prosa para blindarlo, sin cambio matemático.
(ii) Su conjetura sobre el covering constant es ahora el programa explícito
del §10, con la tabla de gaps que usted sugirió; su "inverse stability" está
en Prop 7.16 (es un corolario de una línea de nuestra cota de momentos, como
sospechábamos). Le pedimos foco en: §7 (dualidad renombrada y ampliada:
δ=δ_c es ahora Teorema 7.11, y la cota de momentos quedó refutada como
identidad general — Rem 7.20), el Teorema 6.13 (cobertura canónica con
exceso exacto), y el §10 reescrito.

## Mapa punto (pasada 5) → resolución (pasada 6)

| # | Su punto | Resolución |
|---|---|---|
| Pocket Lemma "P∩∂Δ finito no tiene sentido" | **Sin error en el texto** (la clausura ya estaba: `P̄∩∂Δ`); añadida la palabra "closure" en prosa como blindaje. Cortésmente: era mislectura. |
| `27/29 → 29/31` | **Adoptada tal cual.** Thm 7.15 enuncia el recíproco exacto `Σrw ≥ m(m−ε)/(m(m−ε)+ε)`; Cor 7.17 da `29/31 > 4√3−6` con certificado `46225 > 46128`; intro actualizada. El tubo (Cor 7.18) ya usaba el recíproco. |
| Abstract cargado; B-Y fuera | Abstract a **3 mensajes** (defecto+dualidad minimax / caracterización D=1 / familia cíclica tight+rígida, con las calibraciones al final); la comparación B-Y es ahora un párrafo sobrio al FINAL de la intro, con su caveat. |
| "best constant is certified" | Su frase, adoptada: "we determine exactly when **the transport method certifies the sharp constant 1**". |
| Dualidad: precisión + nombre | Renombrada **"minimax duality"** (Thm 7.7); el enunciado dice explícitamente que NO se afirma el alcance del supremo (y que sí se alcanza en todos los ejemplos exactos del paper). |
| Mini-tabla de patrones | Añadida junto al Thm de caracterización (patrón / concurrencia / soporte / mecanismo). |
| Tabla de 7 casos del Apéndice A | Añadida (tipo / órbita / resultado / mecanismo etiquetado: traza de línea llena ⟹ interior vacío, endpoint `h₁=1` vs tipo L, solape de interiores). |
| C(u) y el gap (su idea) | **Def 2.3 + Rem 2.4** (`1/D ≤ C ≤ 1`; Bang ⟺ `C=1`; gap `G = C − 1/D`); tabla de gaps en §10 (facetas: 1/3; concurrentes: 0; sandwich y clase-b con brackets). Es el **programa del §10** (Prob 10.1) con el lema de reducción a aristas (Lem 10.2) y el estado honesto del certificado híbrido. |
| Inverse stability (su idea) | **Prop 7.16**: `D ≤ 1+η ⟹ δ ≤ η/(2(1+η))` — corolario de una línea de nuestra Prop 7.2; con Thm 7.15, `D−1` es métrica bilateral de no-concurrencia. |
| Figura del certificado dual (su idea) | **Fig. 4**: la cuña `(1−3t/2)₊` + el hexágono de contacto con el lazo inscrito. |
| Phase diagram (su idea) | **Fig. 5** [Evidence, not proof]: mapa certificado de la cota inferior en la rebanada `τ₃=½`; anti-diagonal `Π=Q` = lugar concurrente; gaps UB/LB documentados con números verificados (0.06 en la franja, 0.59 en la esquina). |

## Qué es NUEVO desde su pasada 5 (pedirle foco)

1. **Thm 7.11 (the two defects coincide):** `δ = δ_c` SIEMPRE — las cuñas de
   un nudo alcanzan siempre la cota de momentos; `δ` tiene forma cerrada.
   Prueba vía el lema de conteo generalizado (Lem 7.10, a nivel `a` general).
2. **Rem 7.20:** la cota de momentos NO es exacta en general — tres
   certificados duales archivados (18/13 > 15/11; 32/29 > 153/142; sandwich
   estrictamente > 225/224), verificador autocontenido en ancillary.
3. **Thm 6.13 (canonical covering):** TODA terna cíclica porta una cobertura
   canónica explícita con `Σrw = 1 + (Π−Q)²/((1+Π)(1+Q))`; `Π=Q ⟺`
   concurrencia. Tres identidades polinomiales + la maquinaria de cobertura
   existente.
4. **Prop 7.4:** `δ = 1/6` solo en las facetas (mód flips) — unicidad del
   extremo, vía la alternativa de Gordan.
5. **Prop 7.16, Prop 7.21, Rem 7.22:** estabilidad inversa; semicontinuidad
   inferior de `D`; el camino de degeneración paralela con cotas bilaterales
   exactas (`D → 1` linealmente, sin salto).
6. §10 reescrito como el programa del covering constant (SU conjetura,
   formalizada), incl. experimentos exactos que no produjeron ninguna
   cobertura con `Σr < 1`.

## Mapa de numeración (pasada 5 → pasada 6)

Sin cambios: §1–§6 hasta 6.12 (en particular 6.3, 6.4, **6.6–6.9**, 6.11,
6.12), 7.1–7.3, 8.1, 8.2, 8.4, 9.1, 9.2, A.1, App B.

| Pasada 5 | Pasada 6 | Objeto |
|---|---|---|
| Thm 2.3 / Rem 2.4 | **Thm 2.5 / Rem 2.6** | uniforme `D≤d` / una-vs-todas (corridas por Def 2.3 + Rem 2.4 nuevas, covering constant) |
| — | **Thm 6.13 / Rem 6.14** | cobertura canónica (nuevo) |
| — | **Prop 7.4** | unicidad del maximizador de δ (nuevo) |
| Thm 7.4 / Rem 7.5 | **Thm 7.5 / Rem 7.6** | facetas 3/2 / complementariedad |
| Thm 7.6 / Cor 7.7 / Prop 7.8 | **Thm 7.7 / Cor 7.8 / Prop 7.9** | dualidad (ahora "minimax") / certificados / cuñas |
| Lem 7.9 | **Lem 7.10** | lema de conteo (generalizado a nivel `a`) |
| — | **Thm 7.11** | δ = δ_c (nuevo) |
| Rem 7.10 | **Rem 7.12** | jerarquía (reescrita: colapsa) |
| Prop 7.11 / Rem 7.12 | **Prop 7.13 / Rem 7.14** | equality pattern / esqueleto |
| Thm 7.13 | **Thm 7.15** | estabilidad (recíproco exacto) |
| — | **Prop 7.16** | estabilidad inversa (nuevo) |
| Cor 7.14 / Cor 7.15 | **Cor 7.17 / Cor 7.18** | 29/31 / tubo |
| Rem 7.16 / Rem 7.17 | **Rem 7.19 / Rem 7.20** | caveat B-Y / certificados-gap (reescrita) |
| — | **Prop 7.21 / Rem 7.22** | lsc / camino paralelo (nuevos) |
| Prob 10.1 (3-planks) | **Prob 10.1 + Lem 10.2** | programa covering constant |
| Prob 10.2 / 10.3 | **Prob 10.3 / 10.4** | suficiencia d≥3 / sup D = 3/2 (reescrito) |
| Fig. 4 (tiling) | **Fig. 6** | (Figs. 4, 5 nuevas: certificado dual; phase diagram) |
