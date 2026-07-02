# R5-4 — Constancia del material M1 rescatable (línea Euler–Jacobi, archivada)

> Date: 2026-07-02. Status: **[REGISTRO — no urgente, línea archivada]**. Cumple R5-4
> (`auditorias/49`): el viejo draft muere (`drafts/obsolete/`), pero el contenido genuino de
> `drafts/M1-working-notes.md` queda inventariado aquí con el **test polynomial escrito
> correctamente** (el punto 1 de doña Rosa). Si algún día se publica como nota separada,
> partir de aquí.

---

## 1. Los resultados genuinos de M1 (probados módulo GOP, validados numéricamente)

1. **Identidad shifted Euler–Jacobi `(⋆⋆)`** (draft M1 §10.1): para formas afines
   `L_j(x)=⟨v_j,x⟩−m_j` (`v_j` unitarios, pesos `1/n`), los críticos de
   `Ψ_m=½‖x‖²−(1/n)Σlog|L_j|` satisfacen
   `Σ_crit μ(x)·(n²−Σ_j 1/L_j(x)²) = 0` con peso `μ>0`
   ⟹ existe crítico con `|L_j(x)|≥1/n` ∀j — **margen sharp `1/n` con shifts**.
   Validada a `~1e-15` (`experiments/m1_check.py`).
2. **Prop. M1.2:** ∃`x` con `‖x‖≤√(1+‖m‖)` y `|⟨v_j,x⟩−m_j|≥1/n` — plank afín con cota de
   norma explícita dependiente del shift.
3. **Props M1.1 / §9.1 (homogenización `(n+1)`):** teorema de plank shifted en la bola
   unidad con constante `(√2−1)/n` (no sharp; el cap `(√2−1)` es estructural, §9.2).
4. **El impasse honesto** (§10.3): el motor continuo NO coloca el testigo sharp en la bola
   unidad; eso lo hace el lema discreto de Bang. La "reproducción de Ball" quedó como
   margen (sí) + pertenencia (no).

## 2. El test polynomial, escrito CORRECTAMENTE (punto 1 de doña Rosa)

El viejo draft transcribía el test como `g = Q(y)·(s²−Σk_j²/y_j²)` con `Q=∏y_j` — **eso no
es un polinomio** tal como está escrito (`Q/y_j²` tiene denominador); la igualdad solo vale
**sobre el locus crítico**. La forma correcta (que SÍ es polinomio, grado `≤n−1`):

- **Caso centrado (GOP):** `g = 2·Σ_{i<j} k_i k_j ⟨v_i,v_j⟩ ∏_{ℓ≠i,j} y_ℓ` (grado `n−2`);
  coincide con `ΔP` en el caso no ponderado. Sobre las soluciones,
  `g(y) = (∏y_j)·(s²−Σk_j²/y_j²)`, que es la forma útil pero NO la definición.
- **Caso shifted (M1 §10.1):** `g = ΔP_m − n·g₂`, con `P_m=∏_j L_j` y
  `g₂ = Σ_j m_j ∏_{ℓ≠j} L_ℓ`. Ambos sumandos son polinomios (grados `n−2` y `n−1`); la
  corrección `−n·g₂` **cancela el término de shift**, y sobre los críticos
  `g/det J_h = μ·(n²−Σ1/L_j²)`. Este es el enunciado que debe aparecer en cualquier
  escritura futura.

## 3. Disposición

- Los `.tex` de la era tórica: `drafts/obsolete/` (no citar).
- `drafts/M1-working-notes.md` se CONSERVA en `drafts/` (material fuente de esta línea).
- Scripts: `experiments/m1_check.py`, `m1_homog.py` (existen, verificados en auditoría §1).
- **Si se retoma:** publicable como nota corta "A shifted Euler–Jacobi identity with sharp
  margin" (resultados 1–3), con el test polynomial de §2 y el impasse de §1.4 declarado.
  Prioridad: baja (línea deprioritizada; el deliverable vivo es el paper de transporte).
