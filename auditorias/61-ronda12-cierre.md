# Auditoría Ronda 12 — Thm 6.13 (cobertura canónica) CONFIRMADO; pasada 6 lista + Órdenes Ronda 13
> Auditor / Jefe de research: Claude. Fecha: 2026-07-03.
> Alcance: `notes/55-R12-*`, el `.tex` (31 pp), `covering_constant.py`, copia pasada 6.
> Método: verificación a mano del Thm 6.13 (dependencia, márgenes, exceso, δ_c cerrada,
> criterio Π=Q); ejecución de scripts; diff de la copia congelada.

---

## Veredicto: ronda completa y limpia. El flagship dejó un teorema verificado y honesto.

### 1. Thm 6.13 (cobertura canónica de toda terna cíclica) — [PROVED] CONFIRMADO

Verificaciones mías, independientes:
- **Dependencia `Σcᵢuᵢ≡1`, `cᵢ=gᵢ/(1+Π)`:** evaluada A MANO en los tres vértices — las tres
  dan `1+Π` exacto (`τ₁g₁+g₃`, `g₂+τ₃g₃`, `g₁+τ₂g₂`). ✓
- **Identidades de margen:** verificadas numéricamente en medianas
  (`(1+Π)²−Στg² = 27/64 = g₁g₂g₃` y `Σgg_{+1}−(1+Π)(1+Q) = 27/64` ✓) + simbólico del
  script. Márgenes estrictos porque `gᵢ∈(0,1)` siempre ✓.
- **Fórmula del exceso:** la rederivé simbólicamente ANTES de leer el `.tex`:
  `Σρ−Σλ = (2+Q+Π)/(1+Q) − (1−Q+2Π)/(1+Π)` tiene numerador `1+Π+Q+Π²+Q²−ΠQ` — idéntico al
  de `1+(Π−Q)²/((1+Π)(1+Q))` ✓✓.
- **`Π=Q ⟺ concurrencia`:** rederivado — la condición vieja `Σp*=1` equivale a
  `e₁−e₂+2e₃=1` y `Π−Q = e₁−e₂+2e₃−1` ✓; chequeado además en la terna concurrente conocida
  `τ=(5/9,4/5,1/6)`: `Π=Q=2/27` ✓✓. Criterio nuevo, limpio y correcto.
- **`δ_c = |Π−Q|/(2(2+Π+Q))`:** rederivada desde `Σg=2+Π+Q` (que verifiqué:
  `3−(e₁−e₂) = 2+Π+Q`) ✓; sandwich `δ=1/450` ✓; penalización sandwich
  `1/12656 = (1/100)²/((113/100)(112/100))` ✓.
- **Cobertura:** el mecanismo es el correcto y está bien distinguido — mixtos excluidos por
  ACOTACIÓN (Pocket Lemma; las rectas de nivel concurrentes dan cono no acotado), no por
  no-concurrencia de mid-lines; puros chocan con los márgenes; Lem de cobertura corre con
  `(cᵢ,1)` en lugar de `(aᵢ,S)` ✓.
- **Honestidad ejemplar del Remark:** "certifies only `C≤1` (which is trivial); its value
  is structural". Exactamente el tono que Rosa nos exigió — sin sobreventa.

**Lectura estructural:** la mitad sharp del teorema de rigidez ahora se extiende
cuantitativamente FUERA del locus concurrente: toda terna cíclica lleva una cobertura
canónica no degenerada con exceso = **penalización de concurrencia** exacta. Junto con
`δ_c` cerrada y el criterio `Π=Q`, la familia cíclica queda completamente entendida del
lado de coberturas explícitas.

### 2. Parte A — verificada
Pasada 6 congelada = vivo (diff 0); 31 pp, compila limpio. `29/31` adoptada (recíproco
exacto en el Thm de estabilidad; certificado `46225>46128` en el Cor; intro y tubo
consistentes — verificado por grep). Pocket Lemma blindado sin ceder. Abstract a 3 mensajes
con la frase exacta de Rosa; "minimax duality" con no-alcance del supremo explícito;
mini-tabla de la tricotomía; tabla de 7 casos etiquetados en el Apéndice A; R10 íntegro
(Lem 7.10 + Thm 7.11 δ=δ_c en el texto, certificados-gap, unicidad, lsc + camino). UNA
tabla de numeración, claves estables.

### 3. Parte B — verificada, con un punto de higiene digno de mención
`C_K(u)` (Def 2.3) + `1/D ≤ C ≤ 1` + tabla de gaps; Prop 7.16 (estabilidad inversa, el
corolario de una línea); Figs 4–5. **Lo mejor de la ronda en disciplina:** el investigador
iba a escribir en la caption del phase diagram "gap ≈0.02 cerca de la anti-diagonal", lo
recomputó, era FALSO, y la caption lleva el máximo exacto verificado
(`1432/23961 ≈ 0.06`). Eso es exactamente la cultura anti-fabricación que este proyecto
necesita — un dato de figura también es un claim.

### 4. Parte C1 — el programa C(u) arrancó bien y sin fantasías
- Oráculo exacto de cobertura (8 celdas de signo + LP Chebyshev en fracciones + chequeo
  independiente de aristas) ✓ corrido: **ninguna cobertura certificada con `Σr<1`** en las
  3 ternas no concurrentes (las de `Σr=1` son las triviales degeneradas — plank lleno).
  El protocolo anti-sensación quedó instalado y no se disparó ✓.
- `C₃(sandwich) ∈ [111/112, 1]` vía transporte — el gap ya es minúsculo.
- Lem 10.2 (edge reduction) con su límite honesto declarado (3/5 en medianas): el híbrido
  queda como PROGRAMA en §10, no como resultado ✓ — como se ordenó.

═══════════════════════════════════════════════════════════════════════
# ÓRDENES RONDA 13 (ejecuta el investigador)
═══════════════════════════════════════════════════════════════════════

## R13-0 (usuario) — entregar la pasada 6 a doña Rosa
Paquete listo (`entregas/...pasada6.{pdf,tex}` + hand-off `notes/55-R12-entrega...`).
Regla vigente: su dictamen pausa todo. Bloque de autor: sigue pendiente del usuario.

## R13-1 (RESEARCH FLAGSHIP) — `C₃` para ternas cíclicas: el caso 3-planks con estrategia
de dos regímenes
La ronda dejó la foto clara: `C₃(u)=1` se alcanza solo trivialmente (plank lleno); la
conjetura de trabajo es **"Σr ≥ 1 para toda cobertura por 3 planks (uno por dirección) de
cualquier terna cíclica"** con caracterización de igualdad (= solo triviales cuando no hay
concurrencia; = canónica/tight cuando la hay). Estrategia de dos regímenes:
1. **Régimen extremo (algún width grande):** si `r₁ ≥ 1−w₀`, el resto no cubierto
   `{u₁∉I₁}` son 1–2 regiones convexas pequeñas (esquinas/trapecio) que deben cubrir los
   otros 2 planks — **reducir al caso de 2 planks, que está RESUELTO en el plano** (la
   única pieza cerrada de la conjetura; citarla con precisión — es la primera vez que la
   usamos como herramienta). Cuidado real: los 2 planks deben cubrir AMBAS componentes a la
   vez — formular la reducción con eso en mente (por componente + argumento de suma).
2. **Régimen balanceado (todos los widths < w₀):** maquinaria de la ronda — dependencia
   explícita positiva `Σcᵢuᵢ≡1`, celdas de signo, Pocket Lemma, y las cotas de borde
   (trazas deben cubrir cada arista ⟹ LP de aristas con los pesos congelados de Thm 7.15:
   `C₃ ≥ 1/D_edge`). El hueco a cerrar: pasar de `1−ε` a `1` exacto en este régimen —
   aquí puede entrar el certificado híbrido (medida + obstrucción de sumset en las
   esquinas). Si el empalme de los dos regímenes cierra: **teorema `C₃=1` para toda la
   familia cíclica** — el caso 3-planks/3-direcciones cíclicas del triángulo, un avance
   genuino sobre el problema abierto.
3. Bounded fallback si no cierra: el sandwich decidido (`C₃(sandwich)=1` exacto vía el
   empalme en UNA terna concreta) — ya sería publicable como primera terna no concurrente
   con Bang probado.

## R13-2 (research, acotado — carryover C2) — alimenta directamente a R13-1
(a) UB fino cerca de facetas (¿máximo local de D en 3/2?); (b) sandwich `D` exacto
(matched pair o prueba de óptimo no-esquelético). Cada mejora de `D` fuera del locus
sube la cota `C₃ ≥ 1/D` del régimen balanceado.

## R13-3 (al llegar el dictamen de la pasada 6) — auditar y responder; integrar lo que pida.
## R13-4 (fondo) — C3 de Rosa (fórmula cerrada `D(τ)` por regiones; `D_∂=D`) · moonshot.

---

## Prioridad
1. **R13-0** (entrega — usuario).
2. **R13-1** (flagship: el empalme de dos regímenes; empezar por formalizar la reducción a
   2 planks del régimen extremo, que es la pieza nueva con herramienta ya resuelta).
3. **R13-2** en paralelo (acotado).
4. R13-3 al llegar; R13-4 fondo.

**Mensaje al investigador:** el Thm 6.13 es exactamente lo que el programa necesitaba —
la cobertura canónica convierte "no-concurrencia" en un número (la penalización) y te
verifiqué todo hasta la última identidad. Mención especial a la caption del phase diagram:
recomputar un dato antes de publicarlo y descubrir que era falso es el estándar; que nunca
se pierda. La R13 tiene la primera estrategia de prueba completa para `C₃` cíclico: dos
regímenes, y el extremo usa por primera vez el caso de 2 planks resuelto como herramienta.
Si solo cierra en el sandwich, ya es la primera terna no concurrente con Bang probado —
eso también es un teorema.
