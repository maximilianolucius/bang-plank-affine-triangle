# Auditoría — ejecución D1/D2 (Discussion + Conclusions) de la directiva 70
> Jefe de research: Claude. Fecha: 2026-07-07.
> Método: lectura de las dos secciones en disco línea a línea; recompilación desde cero
> (borré `.aux/.out`, `pdflatex` ×2); verificación de las 26 `\bibitem` citadas; los 3
> chequeos obligatorios contra el cuerpo. NO comité (hay 2 correcciones pendientes).

## Verificación mecánica (independiente, la corrí yo)
- **Ubicación/numeración:** §11 Discussion (`sec:discussion`, l. 2886), §12 Conclusions
  (`sec:conclusions`, l. 2957), ambas entre §10 (`sec:problems`) y `\appendix`; apéndices
  siguen A/B. ✓ exactamente como pedía la directiva.
- **Compilación desde cero:** exit 0, **42 pp**, **0 undefined (refs+citations)**,
  **0 overfull hbox > 10pt**. Confirma el reporte del investigador.
- **Citas:** las 13 claves usadas en las dos secciones nuevas
  (`Strassen65, Kellerer84, Villani09, mathlib20, AppelHaken77, Hales17, HKM16, BY26, OM21,
  GKP22, AKP19, Pinasco23, MOM26`) tienen `\bibitem`. **No hubo que quitar ninguna** — la
  expansión de refs de §4 ya tenía las de transporte. 26 `\bibitem` totales (≥22 ✓).
- **`drafts_uso_ai.zip`:** snapshot de `drafts/` (7.4 MB, notas+logs+ancillary), sin trackear,
  no lo creó el investigador. **No es parte del paper — excluir del commit.** Bien dejado intacto.

## Chequeo (i) objeto afirmado = objeto probado — 3 imprecisiones, TODAS mías (directiva 70)
El investigador pegó mis borradores verbatim; los tres defectos están en el texto que yo
redacté, no en su ejecución.

### Corrección A [aplicar] — overclaim de `G_tr>0` fuera del locus (Discussion, l. 2914–2917)
El cuerpo (l. 367–374) solo prueba `G_tr=1/3` en la terna facet; en el sandwich `C_Δ(τ₀)`
está abierto, así que `G_tr>0` no está establecido en general. Mi frase lo afirma para toda
la región no concurrente. Reemplazo honesto (usa `D>1` estricto fuera del locus, que sí está
probado por `thm:char`):

REEMPLAZAR:
```latex
(Corollaries~\ref{cor:beyond},~\ref{cor:region}). Off the concurrent locus the
transport bound $1/D_\Delta$ is \emph{strictly} below the covering truth: the
gap $G_{\mathrm{tr}}=C_\Delta-1/D_\Delta$ is positive there, as the facet
triple already shows ($1/D=\tfrac23$ while $C_\Delta=1$; Theorem~\ref{thm:facet}).
```
POR:
```latex
(Corollaries~\ref{cor:beyond},~\ref{cor:region}). Off the concurrent locus
$D_\Delta(u)>1$ strictly (Theorem~\ref{thm:char}), so the transport bound
$1/D_\Delta<1$ and transport alone can no longer reach the covering value~$1$.
How large the resulting gap $G_{\mathrm{tr}}=C_\Delta-1/D_\Delta$ is remains
open in general; at the facet triple it is $\tfrac13$ ($1/D=\tfrac23$,
$C_\Delta=1$; Theorem~\ref{thm:facet}).
```
La frase siguiente ("This is a limitation of the object…") sigue coherente.

> **Re-auditoría (2026-07-07, tras aplicar A/B/C).** Verificado en disco:
> A — frase vieja ausente, nueva en l. 2917 (usa `D_\Delta(u)>1` estricto vía `thm:char`,
> gap "open in general", facet=`1/3`); enlaza coherente con "This is a limitation of the
> object…". B — `\sup_K D_K` ausente, `\sup_u D_\Delta(u)` en l. 2979 + cita a `prob:defect`
> (l. 2981), coincide con el enunciado del cuerpo. C — "known to us" en l. 2969. Recompilé
> desde cero: 42 pp, 0 undefined, 0 overfull >10pt. El `.tex` dentro de
> `submission-source-aims-v1.zip` es **idéntico** al de trabajo (investigador regeneró el zip).
> **Cerrado: apto para commit.**

### Corrección B [aplicar] — objeto equivocado `\sup_K D_K` (Conclusions, l. 2976–2980)
El open problem real (`prob:defect`, l. 2865–2867) es `\sup_u D(u)` sobre ternas no paralelas
del triángulo, no `\sup_K D_K` (sup sobre cuerpos). Corregir el objeto y citar `prob:defect`.

REEMPLAZAR:
```latex
remain beyond it: the exact value of $\sup_K D_K\in[\tfrac32,2]$, whose
resolution would give the universal bound $\sum\rw\ge\tfrac23$ for arbitrary
triples on the triangle, and the affine plank conjecture itself, where the best
known general constant remains $2/(1+\sqrt d)$~\cite{BY26}.
```
POR:
```latex
remain beyond it: the exact value of $\sup_u D_\Delta(u)\in[\tfrac32,2]$, the
supremum of the transport defect over pairwise non-parallel triples on the
triangle (Problem~\ref{prob:defect}), a positive answer to which would give the
universal bound $\sum\rw\ge\tfrac23$ for coverings by planks parallel to any
three directions, and the affine plank conjecture itself, where the best known
general constant remains $2/(1+\sqrt d)$~\cite{BY26}.
```

### Corrección C [opcional] — hedge de consistencia (Conclusions, l. 2966–2968)
La intro (l. 279) y §10 (l. 2644) dicen "to our knowledge"; Conclusions lo afirma sin hedge.
Opcional: en "the first genuinely tilted non-concurrent triple for which the
one-plank-per-direction bound is established" insertar "known to us" tras "triple"
("…non-concurrent triple known to us for which…"). No bloqueante.

## Chequeo (ii) ninguna prueba asume su conclusión
N/A estructural (secciones de síntesis, no prueban nada). Sí verifiqué que no haya
**overclaim de "probado" sobre lo conjetural**: todo lo abierto está marcado como abierto
(`open`, `Conjecture`, `seem within reach`, `local consequence, not an improvement`). El único
resbalón era el A (afirmar `G_tr>0` general como hecho) — cubierto arriba.

## Chequeo (iii) "first/every/all" contra contraejemplo
- "first genuinely tilted non-concurrent triple" — protegido por "non-facet, non-concurrent";
  las facetas (también no concurrentes) quedan excluidas. ✓ (falta solo el hedge, corr. C).
- "universal bound `δ(u)≤1/6`" — "every family", coincide con `thm:centroid`. ✓
- "in every dimension" (facet defect) — coincide con `thm:facetd`. ✓
- "G_tr is positive there [off the locus]" — FALLA el chequeo (contraejemplo: el sandwich,
  donde no está probado). Corrección A.

## Veredicto
**Aprobado con las correcciones A y B (aplicar) + C (opcional) antes del commit.** La
matemática es fiel al cuerpo salvo esos dos overclaims de alcance/notación, ambos redactados
por mí. Compila 42 pp limpio, citas resueltas, ubicación correcta. Tras aplicar A/B (y C si se
quiere), recompilar (exigir 0 undefined / 0 overfull >10pt), regenerar PDF + zip, y **entonces**
comitear (excluyendo `drafts_uso_ai.zip`). Secuencia: investigador aplica A/B/C → re-auditoría
corta mía → commit.
