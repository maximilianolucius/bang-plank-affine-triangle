# bang-plank — Affine plank problem on the triangle

Investigación sobre la **conjetura afín de planks de Bang** (1951): si un cuerpo convexo
`K` está cubierto por planks, `Σ rw_K(P_i) ≥ 1`. Abierta en general; abierta ya para 3
planks en el plano (Bakaev–Yehudayoff 2026).

## Manuscrito vigente

**`drafts/affine-plank-triangle.tex`** — *Transport and tiling bounds for the affine plank
problem on the triangle* (único manuscrito vivo; ver `drafts/BUILD.md`). Resultados
principales: teorema de medianas con rigidez completa, teorema del perímetro ponderado
(familia cíclica 2-paramétrica de ternas concurrentes), caracterización de concurrencia,
obstrucción del normalizador.

## Estructura

| Directorio | Contenido |
|---|---|
| `drafts/` | Manuscrito vigente + `ancillary/` (scripts para arXiv) + `obsolete/` (era tórica, refutada — no citar) |
| `notes/` | Notas de investigación numeradas (el registro primario del trabajo) |
| `auditorias/` | Dictámenes del jefe de research + órdenes de trabajo por ronda (`00-ordenes-de-trabajo.md` es el documento vivo) |
| `experiments/` | Scripts load-bearing (verificaciones exactas con `sympy`/`fractions`; ver notas que los citan) |
| `paper-ready/` | Material de rondas tempranas (two-walls, M4) |
| `kimi/` | Infraestructura del orquestador investigador/jefe |

`refs/` (PDFs de terceros: Bakaev–Yehudayoff, Ball, Ambrus, Gardner, Verreault) está
**excluida del repo** por copyright; las citas exactas están en la bibliografía del `.tex`
y en `notes/42`.

## Reglas de rigor del proyecto

- Aritmética exacta (`fractions`/`sympy`); una grilla nunca es prueba.
- Etiquetas estrictas `[PROVED] / [EVIDENCE] / [OPEN]` en cada afirmación.
- Todo enunciado del manuscrito está probado en el texto o citado con atribución.

## Compilar el paper

```bash
cd drafts/
pdflatex -interaction=nonstopmode affine-plank-triangle.tex
pdflatex -interaction=nonstopmode affine-plank-triangle.tex
```
