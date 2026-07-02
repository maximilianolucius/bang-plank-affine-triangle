# P3 — Gardner 1988: ¿cierra la suficiencia de `cond=2`? + cita de `notes/12`

> Date: 2026-06-30. Status: **[VERDICTO: Gardner NO cierra la suficiencia]**; cita de
> `notes/12` **[CORREGIDA]**. Cierra la Prioridad P3 de `auditorias/00`.
> Fuente: `refs/gardner1988_relative-width-plank.pdf` (R. J. Gardner, *Relative width measures
> and the plank problem*, Pacific J. Math. 135(2) (1988) 299–312; PDF escaneado, cuerpo por OCR).

---

## 0. Las dos preguntas de P3

1. **(cita)** `notes/12` citaba "existencia del acoplamiento a Gardner" pero apuntaba al
   resultado **negativo** (`notes/40 §4`); falta enlazar el **positivo** (2 direcciones).
2. **(suficiencia)** ¿La condición de concurrencia `1ᵀV⁻¹1=2` (`notes/37`, suficiencia
   `[OPEN]`) coincide con un criterio de Gardner para 3 direcciones, cerrándola?

---

## 1. Qué prueba Gardner (fuente primaria)

- **[VERBATIM, Thm 1]** *"Let `K` be a convex body in `Rⁿ` and `θ₁,θ₂` two directions. Then
  there is a relative width measure in `K` for `{θ₁,θ₂}`."* Corolario explícito: *"Bang's
  conjecture is true for two slabs."* **⟹ POSITIVO, pero SOLO para `≤2` direcciones.**
- **[VERBATIM, Thm 2/4]** para `Θ` **analíticamente denso** ("infinito": toda función
  analítica que se anula en las rectas paralelas a `Θ` es idénticamente 0), las **únicas**
  medidas de ancho relativo posibles son Lebesgue 1-D en un segmento o las canónicas de la
  elipse/elipsoide. Thm 3: la bola en `n≥4` no admite medida para *todas* las direcciones.
- **[VERBATIM, Example 1]** el **triángulo** `(0,0),(1,0),(0,1)` con `Θ`= normales a las 3
  aristas: **NO existe** medida de ancho relativo (de las direcciones coordenadas sale
  `c=(⅓,⅓)`, incompatible con la simetría requerida en la hipotenusa).
- **[VERBATIM]** *"This negative result still leaves open the possibility of constructing
  relative width measures for a **finite** set of directions"* — el caso de finitas `≥3`
  direcciones queda **explícitamente ABIERTO** por Gardner.

---

## 2. VERDICTO: Gardner NO cierra la suficiencia de `cond=2`

**El resultado positivo de Gardner (Thm 1) está capado a `≤2` direcciones.** El objeto del
proyecto —medida de marginal uniforme para **3** direcciones (medianas / familia de
concurrencia, `notes/36/37`)— cae en el régimen de **finitas `≥3` direcciones**, que Gardner
**deja explícitamente abierto**. Por tanto:

> **La suficiencia de `cond=2` (`notes/37/38`) NO se sigue de ningún teorema con nombre de
> Gardner.** Gardner (a) prueba el caso `≤2` (que el proyecto ya usa) y (b) prueba
> no-existencia para `Θ` denso; el caso finito `≥3` es su pregunta abierta, y es exactamente
> donde vive `cond=2`.

Esto **descarta** la hipótesis del jefe de research ("`1ᵀV⁻¹1=2` = criterio de Gardner para 3
direcciones"): Gardner no formula tal criterio; su marco positivo no llega a 3 direcciones.

**Consistencia (no contradicción):** el Example 1 de Gardner (no hay medida para las 3
**facetas** del triángulo) es un caso `cond=3` (facetas, `notes/37 §2`), coherente con
`cond≠2` ⟹ no hay medida uniforme. El caso positivo del proyecto (3 **medianas**) es `cond=2`.
Gardner no estudió `cond=2` con 3 direcciones — **es genuinamente terreno nuevo**, dentro de
su pregunta abierta.

**Consecuencia para el estatus:** `notes/37/38` — la suficiencia de `cond=2` sigue **`[OPEN]`**,
y ahora se sabe que es un caso de la **pregunta finita explícitamente abierta de Gardner**
(no un corolario suyo). Esto **eleva** el valor del resultado si se prueba: sería el primer
criterio positivo de resolubilidad para 3 direcciones, en el hueco que Gardner dejó.

---

## 3. Lead (no cierre): la técnica constructiva de Gardner para 2 direcciones

La prueba del Thm 1 de Gardner construye `μ` para 2 direcciones como **suma de múltiplos de
Lebesgue lineal sobre segmentos/diagonales del cuadrilátero inscrito**. La medida del
**perímetro** de `notes/36` (para las 3 medianas) es de la misma familia (singular, soportada
en segmentos del borde). **Lead:** ¿la construcción de Gardner por segmentos se extiende a 3
direcciones **concurrentes** (`cond=2`)? Es la vía constructiva más prometedora para la
suficiencia, pero **no la cierra aquí** (para pasadoras genéricas la solución LP es singular
interior+borde, `notes/38 §2.3`, no sólo segmentos de borde).

---

## 4. Cita de `notes/12` — CORREGIDA

`notes/12 §3` (teorema de 2 direcciones) ahora cita el resultado **POSITIVO** correcto:
**Gardner 1988, Theorem 1** (existencia de medida de ancho relativo para `≤2` direcciones,
cualquier cuerpo convexo) ⟹ "Bang true for two slabs". La traceabilidad rota que señalaba
`auditorias/40 §5` (se apuntaba al negativo de `notes/40 §4`) queda **arreglada**: el positivo
va a Gardner Thm 1 directo; el negativo (obstrucción de medida única para facetas) va al
Example 1 / Thm 4. Cada lado a su fuente correcta.

## 5. Acciones aplicadas
- `notes/38 §2`/`notes/37 §3`: anotar que la suficiencia de `cond=2` es un caso de la
  **pregunta finita abierta de Gardner** (no cerrable por Gardner); sigue `[OPEN]`.
- `notes/12`: cita positiva → Gardner 1988 Thm 1 (ya aplicada el turno previo; confirmada
  correcta contra fuente).
