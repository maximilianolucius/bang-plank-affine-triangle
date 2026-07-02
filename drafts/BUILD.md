# Build & status — UN SOLO MANUSCRITO VIVO

## Manuscrito vigente: `affine-plank-triangle.tex`

- **Título:** *Transport and tiling bounds for the affine plank problem on the triangle*.
- **Estado (2026-07-02):** compila limpio con `pdflatex` local (2 pasadas): **0 errores,
  0 referencias sin resolver, 5 páginas** → `affine-plank-triangle.pdf`.
- **Contenido probado (todo verificado, ver `notes/46` y auditorías `43/44-46/47/48`):**
  Thm `1/d` (Brunn–Minkowski); 2 direcciones (cita Gardner Thm 1); faceta-paralelo
  (Minkowski-sum/BM-1D, prueba corregida en R4-1); 3 facetas + 1 arbitrario (fibras);
  **medianas: `Σrw≥1` + rigidez completa** (centerpiece; lema computer-assisted con scripts
  archivados); caracterización de concurrencia (dim-agnóstica) + `perímetro ⟺ τ=½`;
  no-go del normalizador `N_c` (obstrucción al argumento de Bang).
- **Alcance honesto:** el triángulo como cuerpo concreto; NO la conjetura vía Ambrus
  (Remark 1.3: la reducción produce símplices de dim `2N−1`, nunca el triángulo).

## Cómo compilar
```bash
cd drafts/
pdflatex -interaction=nonstopmode affine-plank-triangle.tex
pdflatex -interaction=nonstopmode affine-plank-triangle.tex   # 2ª pasada (refs)
```

## Ancillary files (para arXiv, ver `auditorias/49 §R5-1`)
El Lema computer-assisted (rigidez de medianas) cita scripts **archivados** en
`experiments/`; al someter, incluir como ancillary:
`median_rigidity_enumeration.py`, `median_edgetilings_independent.py`,
`median_rigidity_centroid.py`, `bang_Nc_nogo_chord.py`. Copias en `drafts/ancillary/`.

## Pendiente antes de someter
- Bloque autor/afiliación/email (decisión del investigador; placeholder marcado en el .tex).

## Obsoletos
`drafts/obsolete/` contiene los manuscritos de la **era tórica** (`paper.tex`, `paper.pdf`,
`bang-plank-paper.tex`), refutada y abandonada (`notes/15/22/23`; auditoría externa
coincidente: `auditorias/49`). **No auditar ni citar** — ver `obsolete/README-OBSOLETE.md`.

(Nota: los ficheros `hamilton-jacobi-*` en `drafts/` son de OTRO trabajo, no de este proyecto
de planks; no forman parte de este manuscrito.)
