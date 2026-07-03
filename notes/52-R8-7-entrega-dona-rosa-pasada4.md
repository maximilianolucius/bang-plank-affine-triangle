# R8-7 — Paquete de entrega: cuarta pasada de doña Rosa

> Date: 2026-07-02. Status: **[LISTO PARA ENTREGAR]** — lo entrega el jefe de research.
> Versión congelada: `drafts/entregas/affine-plank-triangle-2026-07-02-pasada4.pdf`
> (**17 pp**; 0 errores / 0 undefined / 0 overfull). Primera vez que verá §7–§8 y las
> 4 figuras. Numeración de §1–§6 y Apéndice A **estable** respecto de su pasada 3
> (Thm 6.3/6.6/6.8, Rem 6.9, Prop A.1 conservan sus números; el lema topológico nuevo
> es un "Pocket Lemma" sin numerar precisamente para no desplazarlos).

## Mensaje sugerido para doña Rosa

Doña Rosa: su diagnóstico de fondo ("los claims globales van más rápido que las
pruebas") era correcto y esta revisión lo ataca frontalmente, no solo punto a punto.
Los dos overclaims que usted marcó como bloqueantes están eliminados. Además el
manuscrito ahora incluye dos secciones que usted no ha visto (§7, §8) — le pedimos
lectura completa, con foco en §7 (donde está la comparación con Bakaev–Yehudayoff,
que hemos blindado con su alcance exacto en abstract, intro y Rem 7.8).

## Mapa objeción (pasada 3) → resolución (esta versión)

| # | Su objeción | Resolución |
|---|---|---|
| 1 | "no single-measure argument can improve 1/d" (falso: §6–§7 lo contradicen) | Reformulado en abstract, Thm 2.1 y su prueba: la sharpness es de la **medida uniforme**; la nueva Rem 2.2 separa "medidas adaptadas a una familia" (que sí certifican 1) de "una medida para todas las direcciones" (imposible certificar 1 — Gardner; la mejor constante está en `[½,⅔]`, Prop 7.2(iv) + Thm 7.4). Sección renombrada "The uniform-measure bound". |
| 2 | "(equivalently Conjecture 1.1 for the triangle)" (falsa equivalencia) | Borrado. Problem 1 dice ahora explícitamente que 3-planks es sub-problema y que la conjetura para el triángulo (nº arbitrario de planks) NO se reduce a él. |
| 3 | Thm 6.8 "complete characterization" sin acotar | Rem 6.9 reescrita: "within the uniform-marginal witness-measure approach... a statement about the reach of the method, not a reduction of Conjecture 1.1". El párrafo de Scope de la intro ahora separa los cinco niveles (a)–(e) y sitúa cada teorema en (a)/(b). |
| 4 | Thm 6.6 Step 2 comprimido; positividad en script | Paso topológico aislado como **Pocket Lemma** (sin numerar, antes de Thm 6.6) con prueba completa; las desigualdades de positividad de `x*`, `y*` escritas en el texto (elementales: `1+α−β>1−β`, `2−2α−β=β+2γ`, etc.). |
| 5 | Apéndice A: grupo, casos frontera, LMR | Subsección de simetrías reescrita: grupo `G=⟨ϱ,ς⟩≅S₃` explícito con `ς²=id`, `ςϱς=ϱ⁻¹` y acción sobre vectores de tipo; frase global de no-genericidad (los endpoints degenerados los descarta (O2)); caso LMR aireado en tres párrafos con los dos subcasos (truncado / no truncado) separados. |
| 6 | Thm 3.1 cita a Gardner como caja negra | La prueba enuncia [Gardner88, Thm 1] **verbatim** (cuerpo convexo en ℝⁿ, dos direcciones, medida posiblemente singular, marginales = Leb normalizado). |
| 7 | Thm 3.2: medibilidad/compacidad de `C_k`; BM-1D | Corregido de verdad (no solo redacción): los `C_k` son abiertos relativos, se pasa a compactos `C_k'` con pérdida `η=(1−R)/(d+2)` y holgura total `>1`; BM-1D probado en una línea (`A+B ⊇ (A+min B)∪(max A+B)`). |
| 8 | Prop 7.1 (ahora 9.1) mezcla matemática y lectura informal | **Split**: Prop 9.1 = solo el ratio sharp `(ℓ−a)/ℓ` con prueba del segmento; la obstrucción metodológica completa vive en Remark 9.2, rotulada como tal. |
| 9 | Claim de prioridad fuerte | "We are not aware of a previous tight non-facet three-direction rigidity result for the triangle" (§5). El abstract ya no contiene claims de prioridad. |
| 10 | Editorial: abstract largo, palabras-venta, figuras, refs, metadatos | Abstract reescrito y podado (sin "centerpieces/first/full rigidity"); "generic" eliminado como venta; **4 figuras TikZ** (tercios centrales; testigo ponderado con `p` y masas; lazo inscrito de §7; teselación MMM del Apéndice A); MSC 2020 + keywords añadidos; ref. Ambrus con URL verificable (`users.renyi.hu/~ambrus/appendix.pdf`). Bloque de autor: pendiente (decisión humana). |

## Qué es NUEVO desde su pasada 3 (pedirle foco)

- **§7 "The transport defect"**: D(u); `Σrw ≥ 1/D`; `D=3/2` exacto en facetas (lazo
  inscrito, Fig. 3); estabilidad lineal cerca de concurrencia; **Cor 7.7:
  `Σrw ≥ 27/29 > 4√3−6`** para coberturas en las direcciones de ternas cíclicas con
  `max|τᵢ−½| ≤ 1/60`. El alcance exacto (local, clase de coberturas restringida,
  vs. B-Y uniforme) está en Rem 7.8 y repetido en abstract e intro.
- **§8 "A witness family on the 3-simplex"**: Thm 8.1 (familia σ con pesos cerrados) y
  Prop 8.2 (obstrucción d≥4 en el 1-esqueleto).
- Pocket Lemma (sin numerar), Rem 2.2 nueva, figuras, Problem 10.3.
