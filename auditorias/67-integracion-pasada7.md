# Directiva de integración — CONGELACIÓN LEVANTADA; construir la pasada 7 (= pasada 6 + hito C₃)
> Jefe de research: Claude. Fecha: 2026-07-03. Ejecuta el investigador; audita el jefe.
> Decisión del usuario: la pasada 6 NUNCA se envió; iba a enviar directamente la 7. ⟹ **no
> hay lectura externa en curso, la congelación de numeración era autoimpuesta y SE LEVANTA.**
> No se envía la pasada 6 suelta: se integra todo y sale UNA pasada 7 comprensiva.

## Contexto y riesgo asumido (consciente)
La pasada 7 será la PRIMERA vez que Rosa vea a la vez: (a) todos los arreglos aceptados de su
5ª pasada (cobertura canónica, `C_K`, `29/31`, minimax duality, tablas, R10 integrado —
auditados por mí internamente en la Ronda 12, referee-clean por nuestro estándar) y (b) el
hito C₃ computer-assisted. Es un delta grande para una sola pasada; se compensa con un
hand-off que guíe su atención (mapa de arreglos + mapa del hito). Riesgo aceptable — evita
un round-trip y le da una versión coherente. **Sin dos documentos en vuelo: es lo que
protege contra el incidente del paper equivocado.**

═══════════════════════════════════════════════════════════════════════
# DELIVERABLES DE INTEGRACIÓN (investigador)
═══════════════════════════════════════════════════════════════════════

## I1 — integrar el paquete C₃ al `.tex` vivo (§10, el programa del covering-constant)
De `notes/58-R15-lemas-soundness.tex`, insertar como subsección "A partially
computer-assisted case of the program":
- Lema del régimen extremo (ya en el cuerpo como teorema R13 — enlazar, no duplicar).
- Lema de reducción-a-árbol; Lema de soundness P1–P4; Lema del test de no-cobertura completo;
  Lema de terminación-como-prueba.
- **Teorema principal del caso** con la frontera humano/máquina EXPLÍCITA y la etiqueta
  tipográfica `[partially computer-assisted]` distinta de los `[PROVED]` a mano.
- La clasificación de igualdad ("alcanzado solo trivialmente", con los mínimos `31/25, 5/4`).
- Reconciliar labels placeholder (`thm:extreme` etc.) con la numeración real.

## I2 — Apéndice B re-scoped
De `notes/58-R15-appendixB-pilar5.tex`: cambiar la frase "this paper is NOT computer-assisted"
por la versión scoped acordada ("except for a single lemma… discharged by an exact-rational
certificate re-verified by the independent checker of Appendix B; all other results are
proved in the text"); añadir el protocolo Pilar 5 con los tres SHA
(`b2468aa9`/`ead66ff2`/`90a25ce8`) y la corroboración del doble árbol (con su caveat de modo
común: la autoridad es el checker independiente).

## I3 — ancillary + protocolo
Añadir a `ancillary/`: `c3_sandwich_certificate.txt` (o instrucciones de regeneración
determinista si 12 MB es mucho para arXiv — decidir), `bb_certificate_check.py`,
`c3_balanced_bb.py`, `r15_equality.py`. README de ancillary con "qué lema depende de qué
script".

## I4 — abstract / intro: mención honesta del hito, SIN romper el límite
Una frase, scoped, en intro (y a lo sumo media en abstract): "we establish, in part by an
exact-rational computation, the first non-concurrent direction triple on the triangle for
which the three-plank bound holds" — **NO** extrapolar a la familia, **NO** al headline.
Mantener el abstract **≤200 palabras** (Rosa lo pidió; hoy ~230) ⟹ podar en otro lado al
añadir la frase. El hito vive en §10, no en el resumen.

## I5 — compilar limpio + tabla de numeración (la ÚLTIMA)
`pdflatex` 2 pasadas, 0 errores/undefined/overfull. Tabla vieja↔nueva UNA vez (es la última;
a partir de aquí no hay más congelaciones porque no habrá lecturas parciales sin cerrar).
Copia congelada `entregas/…-pasada7.{pdf,tex}`.

## I6 — hand-off de la pasada 7 (`notes/59-…`)
- Mapa objeción(pasada 5)→resolución (dónde quedó cada punto).
- **Declaración abierta del resultado computer-assisted** + el estándar de 6 pilares +
  pedido de foco: los lemas de soundness (§10) y el checker (Apéndice B).
- Nota de que las pasadas 6 y 7 se fusionaron (ella no vio la 6; esta las incluye).

## I7 — bloque de autor: DECISIÓN DEL USUARIO (pendiente real)
Es la pasada fuerte y Rosa marcó el placeholder dos veces. **Recomiendo llenarlo antes de
enviar** — es lo único que aún "huele a borrador". Requiere identidad real; no lo decido yo.

═══════════════════════════════════════════════════════════════════════
# DESPUÉS de la integración
═══════════════════════════════════════════════════════════════════════
1. **Auditoría mía de la pasada 7 integrada** (orden del usuario): compilación, ubicación y
   numeración de los lemas, frontera humano/máquina, Apéndice B, abstract ≤200, ancillary,
   hand-off. Re-correr el checker sobre la copia congelada por última vez.
2. Con mi OK + el bloque de autor resuelto → **el usuario envía la pasada 7 a Rosa.**
3. Fondo (no bloquea el envío): boundary/thin-plank lemma (lead: las 2,354 celdas 2-D),
   sandwich `D` exacto, vectores C, moonshot; menor: assertions limpias en el parser del
   checker.

## Prioridad
1. **I1–I3** (integración del hito — es el núcleo).
2. **I4–I6** (abstract, compilación, hand-off).
3. **I7** (autor — usuario) → mi auditoría → envío.

**Mensaje al investigador:** se levanta la congelación — la pasada 6 no salió, así que
fusionamos todo en la 7. Integra el paquete C₃ tal como quedó en `notes/58-*` (que ya
auditué), con el teorema etiquetado `[partially computer-assisted]` y su frontera
humano/máquina explícita, y el Apéndice B scoped con los SHA. El hito va en §10 y una frase
honesta en la intro — NADA de extrapolarlo a la familia en el abstract. Cuando compile
limpio y esté la copia congelada, la audito entera (incluido re-correr el checker) antes de
que el usuario la envíe. Esta es la versión que le presenta a Rosa el primer resultado del
proyecto dentro del territorio abierto.
