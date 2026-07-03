# R8 — Pasada de precisión ejecutada (R8-1..R8-5, R8-7 preparada)

> Date: 2026-07-02. Status: **[HECHO — compila 17 pp, 0 errores / 0 undefined /
> 0 overfull]**. Ejecuta `auditorias/53` órdenes R8-1 a R8-5 y deja R8-7 lista para
> el jefe. R8-6 (estabilidad) y R8-8 (moonshot) NO empezadas (cola, por orden).
> Mapa detallado objeción→resolución para la entrega: `notes/52-R8-7-entrega-dona-rosa-pasada4.md`.

## R8-1 (bloqueantes) — los dos overclaims ELIMINADOS

1. **"no single-measure argument can improve 1/d"**: reescrito en abstract + Thm 2.1 +
   final de su prueba. Lo que ahora se afirma (y es verdadero): la sharpness per-plank
   es de la **medida uniforme**. La nueva **Rem 2.2** hace la separación completa y
   añade un enunciado con contenido: la mejor constante certificable por UNA medida
   contra TODAS las direcciones del triángulo está en **`[½, ⅔]`** (uniforme da ½ por
   Prop 7.2(iv); facetas fuerzan ≤ 1/D(facetas) = ⅔ por Thm 7.4). Sección 2 renombrada
   "The uniform-measure bound". Verificado: no contradice §6–§7.
2. **"(equivalently Conjecture 1.1 for the triangle)"**: borrado; Problem 1 ahora dice
   explícitamente que 3-planks es sub-problema no equivalente.

## R8-2 (alcance) — el texto ya no puede leerse de más

- Rem 6.9: "within the uniform-marginal witness-measure approach … a statement about
  the reach of the method, not a reduction of Conjecture 1.1".
- Intro/Scope: párrafo nuevo con los **cinco niveles (a)–(e)** (familia fija de
  direcciones / medidas testigo / todas las coberturas / conjetura-triángulo /
  conjetura-plano) y la frase "every theorem lives at level (a) or (b)".
- **Blindaje §7 (anticipado a Rosa):** abstract e intro presentan Cor 7.7 SIEMPRE con
  el caveat (restricción a las familias de direcciones; B-Y uniforme vs nuestro local);
  el preámbulo de §7 remite a Rem 7.8 y ya no dice "first bounds".

## R8-3 (rigor) — los cinco puntos de prueba

- **Thm 6.6 Step 2**: hecho topológico aislado como **Pocket Lemma** con prueba
  completa. SIN NUMERAR adrede (`\newtheorem*`): así Thm 6.6/6.8/Rem 6.9 conservan los
  números que Rosa citó en su pasada 3 (verificado contra `.aux`). Positividad de
  `x*`, `y*` escrita en el texto (desigualdades elementales).
- **Prop 9.1 split**: Proposición = solo el ratio `(ℓ−a)/ℓ` sharp (prueba del
  segmento); la lectura metodológica ("esta vía no alcanza ningún `N>ℓ`") vive en
  **Remark 9.2** rotulado "methodological obstruction".
- **Thm 3.1**: [Gardner88, Thm 1] enunciado verbatim con hipótesis exactas (ℝⁿ, dos
  direcciones, medida posiblemente singular, marginales uniformes normalizadas).
- **Thm 3.2**: corregido un defecto real que la queja de Rosa destapó — los `C_k` son
  abiertos relativos, NO compactos como decía el texto. Arreglo: compactos `C_k'⊆C_k`
  con pérdida `η=(1−R)/(d+2)` y holgura final `2−R−(d+1)η>1`; BM-1D probado en una
  línea. **[Este era un hueco de prueba genuino, no redacción.]**
- **Apéndice A**: grupo `G=⟨ϱ,ς⟩ ≅ S₃` explícito (`ς²=id`, `ςϱς=ϱ⁻¹`, acción sobre
  tipos `(X₁,X₂,X₃)↦(X̄₁,X̄₃,X̄₂)`); frase global de no-genericidad tras (O2); LMR
  aireado con subcasos truncado/no-truncado separados.

## R8-4 (editorial)

- Abstract reescrito completo: más corto, resultados numerados (1)–(5), caveat de B-Y
  integrado, frase final de alcance, cero palabras-venta y cero claims de prioridad.
- "centerpieces" → "main results"; "generic" eliminado en todos los usos venta;
  claim de prioridad §5 → "We are not aware of a previous…".
- MSC 2020 `52C17 (52A40, 52A10)` + keywords añadidos.
- Ref Ambrus con URL verificable (`https://users.renyi.hu/~ambrus/appendix.pdf`,
  de `notes/40`).
- **Bloque de autor: SIGUE PENDIENTE** — es identidad real de los humanos del
  proyecto; no la invento. Única decisión que no puedo tomar yo.

## R8-5 (figuras) — 4 figuras TikZ, render verificado visualmente

1. **Fig 1 (§5)**: cobertura tight de medianas `[⅓,⅔]³` (tres bandas de colores).
2. **Fig 2 (§6)**: testigo ponderado en `p=(9/20,3/10,1/4)`: mid-lines concurrentes,
   medial punteado, masas `γ=½, α=1/10, β=2/5`, leyenda lateral (colisiones de
   etiquetas corregidas tras inspección del PNG).
3. **Fig 3 (§7)**: lazo inscrito de Thm 7.4 con flechas + hexágono `{λᵢ≤⅔}` punteado.
4. **Fig 4 (Ap. A)**: teselación MMM de la arista `AB` en el ejemplo corrido
   `τ=(5/9,4/5,1/6)`: trazas abutan en `20/29` y `24/29`.

## Estado y qué falta

- **17 pp**, 0/0/0. Copia congelada pasada 4:
  `drafts/entregas/affine-plank-triangle-2026-07-02-pasada4.{pdf,tex}`.
- **R8-7**: paquete listo (`notes/52-R8-7`) — la entrega física la hace el jefe.
- **R8-6** (estabilidad cuantitativa de la familia) y **R8-8** (moonshot): no
  empezadas, siguientes en cola.
- Sin matemática nueva salvo: Rem 2.2 (`[½,⅔]`, consecuencia directa de §7) y el
  arreglo real de compacidad en Thm 3.2. Todos los scripts previos siguen válidos
  (ninguno afectado por esta ronda).
