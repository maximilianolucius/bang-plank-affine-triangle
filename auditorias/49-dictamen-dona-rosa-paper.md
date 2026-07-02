# Dictamen sobre la auditoría de doña Rosa + Órdenes Ronda 5 (revisada)
> Jefe de research: Claude. Fecha: 2026-07-01.
> Insumo: auditoría externa ("doña Rosa") del "paper del proyecto".
> Método: verificación contra los PDFs en disco (`pdftotext` + grep de las citas textuales
> de la auditoría contra ambos manuscritos).

---

## HALLAZGO CENTRAL: doña Rosa auditó el PAPER EQUIVOCADO

**Evidenciado (verificado contra disco):** la auditoría cita "Theorem 2.3 (Euler–Jacobi)",
"Proposition 3.3", "sección 4 con `H_C` / Conjecturas 4.2–4.3", "§1.4 Status of results",
"verification log in companion notes", "Bernstein–Kushnirenko". Ninguno de esos objetos
existe en el paper vigente. Grep sobre ambos PDFs:

| Cita de doña Rosa | `paper.pdf` (VIEJO, 27-jun) | `affine-plank-triangle.pdf` (VIGENTE, 1-jul) |
|---|---|---|
| "Euler–Jacobi" | **9 ocurrencias** | **0** |
| "Theorem 2.3" / "Proposition 3.3" | **sí** (3 / 4) | no existen (numeración distinta) |
| Conjecture 4.2 / 4.3 | **sí** | no existen |
| "Status of results" (§1.4) | **sí** | 0 |
| "companion notes" | **sí** | 0 |
| "Bernstein–Kushnirenko" | **3** | 0 |
| "polarization" | (tema central) | **0** |

**Conclusión:** doña Rosa leyó **`drafts/paper.pdf`** — el manuscrito de la **era tórica
(2026-06-27)**, correspondiente a la línea Euler–Jacobi/BKK que el propio proyecto **refutó y
abandonó** (`notes/15`, `notes/22`, `notes/23-D13`) y que fue **superseded** el 2026-07-01 por
`drafts/affine-plank-triangle.pdf` (el deliverable real: transporte/teselación, medianas con
rigidez, no-go del normalizador).

## Valoración de la auditoría de doña Rosa EN SUS PROPIOS TÉRMINOS

Sobre el documento que leyó, su auditoría es **de alta calidad y esencialmente correcta**:

1. **`g=Q(y)(s²−Σk_j²/y_j²)` no es un polinomio tal como está escrito** — CORRECTO
   (`Q/y_j² = ∏_{ℓ≠j}y_ℓ / y_j` tiene denominador). El `g` correcto de GOP es el
   Laplaciano/suma-de-productos de grado `n−2`, que coincide con esa expresión **solo sobre el
   locus crítico**. El draft viejo lo transcribía mal. Crítica válida.
2. **Prop 3.3 "equivalently" (centered vs shifted planks)** — CORRECTO; es exactamente el
   **CRUX 0 (shift problem)** que el propio proyecto identificó en `notes/04` como la
   obstrucción central de esa línea.
3. **"Self-contained" impreciso; §4 aspiracional (Φ, `H_C` sin definir); offsets `a_i,b_i`
   omitidos; conjetura de reality demasiado fuerte; BKK/normal-fan vs smooth incompatibles;
   símplex no es smooth; symmetric ≠ Hilbertian** — TODOS CORRECTOS. Son, punto por punto,
   **las razones por las que esa línea se abandonó** (auditorías internas `notes/15/22/23`).
4. **Su recomendación** ("no presentarlo como paper; reescribir como research note o ampliar
   con un caso trabajado") — es **exactamente lo que el proyecto hizo**: el caso trabajado
   existe (medianas: tight + rigidez completa) y el paper vigente lo tiene como centerpiece.

En síntesis: doña Rosa llegó, de forma independiente, al **mismo veredicto que nuestras
auditorías internas de hace 3 días** sobre un documento ya descartado. Eso valida el pivote.

## Qué SÍ aplica de su auditoría al paper VIGENTE (carryover)

Revisado punto por punto contra `affine-plank-triangle.tex`:

| Punto de doña Rosa | ¿Aplica al vigente? |
|---|---|
| 1–8 (EJ, Prop 3.3, framework, offsets, reality, BKK, Hilbertian) | **NO** — nada de eso está en el vigente |
| Falta autor/afiliación/email | **SÍ** — placeholder pendiente (ya estaba en R5-1) |
| "Un resultado nuevo pequeño pero completo / toy model no simétrico trabajado" | **CUMPLIDO** — medianas con rigidez ES ese toy model |
| Actualizar referencias con arXiv number | vigente ya cita arXiv en B-Y/Verreault ✓ |
| No apoyarse en "companion notes" no incluidas | vigente cita scripts **archivados** en `experiments/` (lema computer-assisted) — estándar aceptable, pero al someter habrá que incluir el código como ancillary files de arXiv |

## FALLO DE PROCESO (nuestro, y hay que decirlo)

La auditoría global (`AUDITORIA_CLAUDE_30Jn.md §1`) ya había señalado los `.tex` duplicados
("posible duplicado a depurar") y **no ordené archivarlos**. Consecuencia directa: un auditor
externo leyó el artefacto muerto. `drafts/` hoy contiene DOS manuscritos compilados
(`paper.pdf` viejo y `affine-plank-triangle.pdf` vigente) sin ninguna marca de obsolescencia.
Es un fallo de gestión de artefactos, no de matemática — pero costó una ronda de auditoría
externa. Se corrige en R5-0 (obligatorio, ya).

═══════════════════════════════════════════════════════════════════════
# ÓRDENES DE TRABAJO — RONDA 5 (revisada tras el dictamen)
═══════════════════════════════════════════════════════════════════════

## R5-0 (URGENTE, trivial) — un solo manuscrito vivo
1. Crear `drafts/obsolete/` y mover allí `paper.tex`, `paper.pdf`, `bang-plank-paper.tex`
   (+ un `README-OBSOLETE.md` de una línea: "era tórica, superseded 2026-07-01 por
   `affine-plank-triangle`; refutada en `notes/15/22/23`; auditoría externa coincidente en
   `auditorias/49`").
2. Reescribir `drafts/BUILD.md`: el único manuscrito vivo es `affine-plank-triangle.tex`
   (hoy BUILD.md aún describe el paper viejo).
**Hecho:** imposible volver a auditar el artefacto equivocado.

## R5-1 — carryovers de doña Rosa al paper vigente
1. Bloque autor/afiliación/email (el único punto suyo que aplica directo).
2. Preparar los scripts citados por el lema computer-assisted como **ancillary files** para
   arXiv (lista exacta: `median_rigidity_enumeration.py`, `median_edgetilings_independent.py`,
   `median_rigidity_centroid.py`, `bang_Nc_nogo_chord.py`).
3. Pasada final de estilo (sin autodescripciones tipo "correct and complete" — verificar que
   el vigente no tiene ninguna).
**Hecho:** `.tex` submission-ready.

## R5-2 — re-auditoría externa del PDF CORRECTO
Entregar a doña Rosa `drafts/affine-plank-triangle.pdf` (5 pp) con una nota de contexto de una
línea: qué documento es, que el que leyó estaba descartado, y que su recomendación ("caso
trabajado") está implementada (medianas + rigidez). Su nivel de exigencia es exactamente el
que queremos: **usarla**.

## R5-3 (research, sin cambios) — un triple concurrente NO-mediana (`τ≠½`)
Construir la medida de marginal uniforme para UNA terna concurrente concreta con `τ_i≠½`, **o**
refutar su existencia vía Kellerer (LP exacto/racional, no grid). Informativo en ambos
desenlaces: existencia ⟹ hint de suficiencia + 2º caso tight; no-existencia ⟹ "concurrencia
necesaria pero NO suficiente" (resultado nuevo, sharpea la Prop. del paper). Mejor apuesta de
crecimiento acotada.

## R5-4 (opcional, baja prioridad) — decidir el destino del contenido rescatable del viejo
El viejo draft muere, pero `drafts/M1-working-notes` contiene resultados genuinos (`(⋆⋆)`
shifted con margen sharp `1/n`; Props M1.1/M1.2, probadas módulo GOP). Si algún día se
publica esa línea como nota separada, el test polynomial debe escribirse **correctamente**
(`g=ΔP_m−n·g₂`, que SÍ es polinomio) — exactamente el punto 1 de doña Rosa. No urgente; dejar
constancia y no perder el material al archivar.

## R5-5 (moonshot, fondo) — acoplamiento (batir B-Y)
Sin cambios (`auditorias/48`).

---

## Prioridad
1. **R5-0** (ya — evita repetir el incidente).
2. **R5-1 → R5-2** (cerrar y re-auditar el paper correcto).
3. **R5-3** (única apuesta de crecimiento acotada).
4. R5-4/R5-5 fondo.

**Mensaje al investigador:** la auditoría externa NO tocó el deliverable — validó (sin
saberlo) nuestro pivote, al demoler el mismo documento que nosotros demolimos hace 3 días. El
paper vigente sigue referee-clean. El fallo fue de higiene de artefactos: un solo manuscrito
vivo a partir de ahora.
