# Estándar de presentación de la prueba asistida por computador (C₃(sandwich)=1) — a prueba de Doña Rosa
> Jefe de research: Claude. Fecha: 2026-07-03.
> Objetivo: presentar `C₃(sandwich)=1` con el rigor con que la comunidad presenta pruebas
> computer-assisted (Hales/Kepler, cuatro colores, aritmética de intervalos), de modo que la
> auditoría externa no tenga de qué quejarse. Refina R15-1 en deliverables concretos.

## Principio rector: el computador NO prueba el teorema — descarga un cómputo FINITO cuyo enunciado y validez son teoremas HUMANOS

La quinta pasada de Rosa nos enseñó su estándar: nada de cajas negras, aritmética exacta,
"scripts como verificación secundaria, no muleta". Un teorema computer-assisted riguroso se
estructura para que **toda la matemática esté en el papel** y el computador solo verifique un
hecho finito, explícito y re-checkeable. Seis pilares:

---

## Pilar 1 — Reducción humana a un problema finito (teorema + lemas de soundness a mano)

El paper debe contener, ANTES de mencionar ningún script, la cadena humana completa:

1. **Teorema del régimen extremo (R13):** `max r_i ≥ 1−w₀(τ) ⟹ Σr≥1`, igualdad trivial.
   Prueba humana (ya la tenemos, auditada). Deja SOLO el régimen balanceado.
2. **Lema de reducción balanceada (nuevo, a escribir):** "existe una cobertura balanceada
   con `Σr≤1` ⟺ el árbol de B&B `T(τ)` [definido explícitamente] tiene una hoja no podada".
   Es un enunciado matemático, no algorítmico.
3. **Cuatro lemas de soundness de poda, cada uno con prueba de un párrafo** (los verifiqué en
   `auditorias/63`; hay que ESCRIBIRLOS como lemas numerados):
   - **P1:** caja producto ⟹ `min Σr = Σ max(0, h_i⁻−l_i⁺)`; `>1` ⟹ sin config `Σr≤1`.
   - **P2:** `min r_i ≥ BAL` en la caja ⟹ toda config es extrema ⟹ Teorema R13.
   - **P3:** `I_i⁺=[l_i⁻,h_i⁺]` es superconjunto de todo plank de la caja; si `⋃I_i⁺` no
     cubre `Δ`, ninguna config cubre. **Test de no-cobertura completo y exacto:** arista
     descubierta (1-D) **o** celda de signo con área racional `>0` — con la prueba de
     completitud (todo punto no cubierto está en una arista o en una celda de interior no
     vacío).
   - **P4:** `I_i⁺=∅` ⟹ ≤2 planks ⟹ Teorema 3.1 (Gardner 2 direcciones).
4. **Lema de terminación-como-prueba (contradicción):** si existiera cobertura balanceada
   `(l*,h*)` con `Σr*≤1`, ninguna poda dispararía en cajas pequeñas a su alrededor (lo
   argumenté en `auditorias/63`), luego el árbol no se vaciaría. **Árbol vacío ⟹ no existe.**

Con esto, el ENUNCIADO del teorema principal es honesto sobre la frontera humano/máquina:

> **Teorema (parcialmente asistido por computador).** `C₃(τ₀)=1` para `τ₀=(13/25,½,½)`,
> alcanzado solo trivialmente. *Prueba.* Por los Lemas [extremo], [reducción] y [P1–P4,
> terminación], la afirmación equivale a que el árbol `T(τ₀)` —finito, definido en §X— no
> tiene hojas no podadas. Esto último es una verificación finita en aritmética racional
> exacta, realizada y **re-verificada independientemente** (Apéndice B).

---

## Pilar 2 — Separar BÚSQUEDA de VERIFICACIÓN (el criterio de de Bruijn: el checker es más simple que el buscador)

Hoy el B&B busca y poda a la vez; la confianza recae en el código de búsqueda. El estándar
riguroso **desacopla**:

- **Buscador** (puede usar float como guía, heurísticas, el orden de split que sea): produce
  un **certificado** = la lista de hojas del árbol, cada una con (i) su caja exacta y (ii) la
  regla de poda que la mata + el testigo exacto de esa poda (el valor `min Σr`, la arista y
  el hueco, o la celda y su área `>0`, o el índice del plank vacío).
- **Verificador** (independiente, corto, auditable a mano, SIN búsqueda): re-checkea que
  (a) **las hojas cubren `[0,1]⁶`** — la garantía de que ninguna región se saltó (el análogo
  exacto de la preocupación de Rosa con el Apéndice A: "no se pierde ningún caso"); y
  (b) **cada hoja está válidamente podada** por su regla con su testigo.
- Como el árbol es de bisección, (a) se reduce a verificar que el árbol es un árbol binario
  válido cuya raíz es el cubo y cada nodo interno se parte exacto en sus dos hijos — un check
  de una página.

**Este es el punto que más blinda contra Rosa:** la validez ya no depende de confiar en el
B&B; depende de un verificador que cualquiera puede leer y correr, y que NO busca nada.

---

## Pilar 3 — Aritmética exacta ⟹ independiente del hardware (dígalo explícitamente)

Todo el camino de certificación es `fractions.Fraction` (ℚ): cero float, cero epsilons, cero
error de redondeo. Consecuencia que hay que ENUNCIAR: el resultado es **independiente de la
máquina, el compilador y el orden de operaciones** — a diferencia de una prueba en float con
intervalos, aquí no hay siquiera que auditar el control de redondeo. Es el régimen más fuerte
posible de reproducibilidad numérica. El float, si aparece, es SOLO en el buscador y jamás
toca el certificado.

---

## Pilar 4 — Re-verificación independiente (R15-1, BLOQUEANTE)

Dos caminos independientes que coincidan en el veredicto:
- **Camino A:** el verificador de certificados del Pilar 2 (re-checkea el árbol del B&B).
- **Camino B:** un método DISTINTO — el LP-por-tipo combinatorio (enumerar tipos de cobertura,
  minimizar `Σr` exacto por tipo, ver `≥1`) — que decide lo mismo sin árbol de bisección.
- Si A y B coinciden: corroboración fuerte. Si difieren: gana el que exhiba el objeto
  (cobertura `Σr<1` triple-verificada, o poda con margen exacto). (Veo `bb_verify*.log` en
  `experiments/` — si el investigador ya arrancó esto, encaminarlo a ESTE formato: certificado
  + verificador separado, no un segundo B&B monolítico.)

---

## Pilar 5 — Protocolo de reproducibilidad (extender el Apéndice B que Rosa ya aprobó)

Por cada script del camino de certificación: nombre, versión/**hash SHA**, entrada exacta
(`τ₀`, `w₀`), salida (`QUEUE EMPTY`, nº de hojas, conteo por regla), runtime, **y la frase
"qué parte de qué lema depende de él"**. Incluir: el certificado (o instrucciones para
regenerarlo determinísticamente) y el verificador como ancillary files de arXiv. Declarar:
"el paper NO es computer-assisted en su arquitectura; el cómputo discharge un único lema
finito (el vaciado del árbol), re-verificable por el checker del Apéndice B".

---

## Pilar 6 — Alcance honesto (la lección repetida de Rosa)

- Es **UNA terna**, no la familia. Enunciar exactamente eso: "the first non-concurrent triple
  for which Bang's three-plank inequality is established", y presentar el B&B parametrizado
  (thin-plank lemma, R15-2) como el programa hacia la familia, **no** como hecho.
- NO ponerlo en el abstract como si fuera la conjetura del triángulo. Va como: un caso
  concreto que abre el territorio no concurrente, con método en principio uniforme.
- Etiqueta `[PROVED, computer-assisted]` distinta de los `[PROVED]` a mano. Rosa premia esa
  honestidad tipográfica.

---

## Deliverables concretos (refina R15-1; ejecuta el investigador)
1. **Emitir certificado** desde `c3_balanced_bb.py`: dump de hojas con (caja exacta, regla,
   testigo). Determinista.
2. **Escribir el verificador** `bb_certificate_check.py` — independiente, sin búsqueda,
   ~1 página: (a) cover-check del árbol de bisección; (b) re-check exacto de cada poda.
   Debe imprimir `CERTIFICATE VALID: leaves tile [0,1]^6; all pruned soundly`.
3. **Camino B** (LP-por-tipo) confirmando `≥1` en todos los tipos.
4. **Redactar en el `.tex`** (tras el dictamen de Rosa / descongelación): los 4 lemas de
   soundness + el lema de terminación + el enunciado del teorema con la frontera
   humano/máquina; §/Apéndice del cómputo con el protocolo del Pilar 5.
5. **Hashes** de los tres artefactos (buscador, certificado, verificador) en el Apéndice B.

## Anti-fabricación (recordatorio, reforzado tras R14)
El claim del teorema se emite tras `CERTIFICATE VALID` del verificador independiente — no tras
el `QUEUE EMPTY` del buscador, y desde luego no mientras el run corre. El verificador es la
autoridad; el buscador solo propone.

**Veredicto de dirección:** con estos seis pilares, `C₃(sandwich)=1` se presenta al nivel de
un resultado computer-assisted publicable. Lo que lo hace a prueba de Rosa no es que el
cómputo sea correcto (lo es), sino que **la matemática está toda en el papel** y el cómputo
queda reducido a un lema finito verificado por un checker independiente y auditable — con la
matemática humana (reducción + soundness + terminación) probada a mano.
