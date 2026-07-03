# Hand-off — pasada 7 (= pasada 6 + hito C₃), para doña Rosa

> Date: 2026-07-03. Ejecuta `auditorias/67` (integración). Versión congelada:
> `drafts/entregas/affine-plank-triangle-2026-07-03-pasada7.{pdf,tex}`
> (**34 pp**, 0 errores / 0 undefined / 0 overfull). Autor: Maximiliano Lucius.
> **Se envía tras la auditoría del jefe** (que re-corre el checker) + su OK.

## Nota de contexto para doña Rosa (importante, decírselo)

Usted evaluó la **pasada 5**. La **pasada 6** (con todos sus arreglos
aceptados) **nunca se le envió** — se decidió fusionarla con el hito nuevo en
una sola versión coherente. Por eso esta pasada 7 trae, a la vez: (a) todos
los puntos aceptados de su 5ª lectura, y (b) un resultado nuevo. Es un delta
grande para una sola lectura; este hand-off le guía la atención.

## Declaración abierta: hay un resultado PARCIALMENTE ASISTIDO POR COMPUTADOR

Por primera vez el paper contiene un teorema cuya prueba tiene un paso
finito verificado por computador: **Teorema 10.8, `C_Δ(τ₀)=1`** para la terna
NO concurrente `τ₀=(13/25,½,½)` — el primer triple no concurrente del
triángulo con la cota de 3 planks establecida. Lo declaramos abiertamente y lo
etiquetamos tipográficamente `[partially computer-assisted]` (distinto de los
resultados a mano). El estándar que seguimos (6 pilares):

1. **Reducción humana a un problema finito** (§10): teorema del régimen
   extremo (Thm 10.4, a mano), lema de reducción-a-árbol (10.7), soundness de
   las 4 podas (10.5), test de no-cobertura completo (10.6), terminación-como-
   prueba. El paso máquina es UNA frase: "el árbol T(τ₀) no tiene hoja sin
   podar".
2. **Búsqueda ≠ verificación** (de Bruijn): el buscador emite un
   **certificado**; un **checker independiente que NO comparte código** lo
   re-verifica. La confianza recae en el checker (legible, sin búsqueda), no
   en el buscador.
3. **Aritmética exacta** (ℚ, cero floats) ⟹ independiente del hardware.
4. **Re-verificación independiente**: el checker reconstruye cada caja desde
   el cubo raíz (detecta bugs de aritmética del buscador), verifica que las
   812 651 hojas teselan `[0,1]⁶` y re-valida cada poda. Emite
   `CERTIFICATE VALID`. **Además** probamos que el checker NO es vacuo
   (rechaza certificados corruptos: header alterado, split no-interior, poda
   falsa, árbol truncado).
5. **Reproducibilidad** (Apéndice B): tres SHA (buscador `b2468aa9`,
   certificado `ead66ff2`, checker `90a25ce8`), conteos por regla, y un
   segundo árbol (terna reetiquetada + split 5/11) como corroboración — con
   el caveat honesto de que la autoridad es el checker (un bug de modo común
   sobreviviría al doble árbol pero no a la re-implementación del checker).
6. **Alcance honesto**: es UN triple, NO la familia; NO toca la Conjetura de
   Bang. Vive en §10, no en el headline; media frase en el abstract.

**Pedido de foco:** por favor concentre la lectura crítica en (i) los lemas de
soundness de §10 (¿son las 4 podas correctas? ¿el test de no-cobertura es
completo?) y (ii) el checker del Apéndice B (¿la teselación y la
re-validación son suficientes?). Ahí es donde vive la carga de la prueba.

## Mapa objeción (pasada 5) → resolución (dónde quedó)

| Su punto (pasada 5) | Resolución (pasada 7) |
|---|---|
| `27/29 → 29/31` (mejora gratis) | Adoptada: Thm 7.15 recíproco exacto, Cor 7.17 `29/31 > 4√3−6` (`46225>46128`), intro. |
| Pocket Lemma "P∩∂Δ" | Ya decía `P̄∩∂Δ` (clausura); añadido "the closure of P" en prosa. Era mislectura; blindado. |
| Abstract cargado; B-Y fuera | Abstract 3 mensajes, ≤200 palabras, B-Y al final de la intro. |
| "best constant certified" | "the transport method certifies the sharp constant 1". |
| Dualidad: nombre + precisión | "minimax duality" (Thm 7.7), no-alcance del sup dicho, clase de ψ/Borel. |
| Mini-tabla de caracterización | Añadida (tricotomía) junto a Thm 6.11. |
| Tabla de 7 casos Apéndice A | Añadida con mecanismo etiquetado por caso. |
| δ=δ_c, certificados-gap, continuidad, unicidad (R10) | Integrados: Thm 7.11 (δ=δ_c), Rem 7.20 (3 certificados-gap), Prop 7.21 + Rem 7.22 (lsc + camino), Prop 7.4 (unicidad δ). |
| C(u) y el gap (su idea) | Def 2.3 `C_K` + Rem 2.4 (gap `G`); tabla de gaps en §10; inverse stability Prop 7.16. |
| Figura del certificado dual, phase diagram | Fig. 4 (cuña+hexágono), Fig. 5 (phase diagram [Evidence]). |
| Bloque de autor (marcado 2×) | **Resuelto**: Maximiliano Lucius. |

## Qué es NUEVO desde su pasada 5 (además de lo de arriba)

- **§10 subsección "A partially computer-assisted case"**: Thm 10.4 (régimen
  extremo, a mano, usa el caso 2-planks como herramienta — Lem 10.3),
  Lemas 10.5–10.7, **Thm 10.8** (`C_Δ(τ₀)=1`, etiquetado), Rem 10.9 (frontera
  humano/máquina).
- **Thm 6.13 (cobertura canónica)**: toda terna cíclica porta una cobertura
  con exceso exacto `(Π−Q)²/((1+Π)(1+Q))` (ya venía de la pasada 6).
- **Apéndice B re-scoped** con el cómputo certificado y los SHA.

## Mapa de numeración (pasada 5 → pasada 7) — ÚLTIMO cambio de numeración

Sin más congelaciones tras esto (no habrá lecturas parciales sin cerrar).
Estable desde la pasada 6: §1–§9 y Apéndice A. Novedades §10:
Lem 10.2 (edge reduction), **Lem 10.3 (two-plank tool), Thm 10.4 (extreme
regime), Lem 10.5–10.7, Thm 10.8 (sandwich, computer-assisted), Rem 10.9**;
luego Prob 10.10, 10.11 (antes 10.3, 10.4). Apéndice B ahora abre con el
cómputo certificado. (Respecto de su pasada 5, la tabla completa vieja↔nueva
está en `notes/55-R12-entrega-dona-rosa-pasada6.md`; esta pasada solo agrega
los 10.3–10.9 al final de §10.)

## Estado de verificación (para la auditoría del jefe)

- Compila 34 pp, 0/0/0.
- `CERTIFICATE VALID` re-confirmado sobre el certificado que embarca en
  `ancillary/` (checker independiente; 812 650 internos + 812 651 hojas;
  P1=286024 P2=53907 P3edge=428672 P3cell=2354 P4=41694).
- Checker no-vacuo (4 controles negativos rechazados).
- Doble árbol (1.63M vs 1.04M nodos) coincide.
- Igualdad clasificada (min propio 2-plank 31/25, 31/25, 5/4 > 1).
