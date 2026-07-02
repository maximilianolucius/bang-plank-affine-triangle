# Auditoría de `notes/40` (reducción de Ambrus — verificada contra fuente primaria)
> Auditor / Jefe de investigación: Claude. Fecha: 2026-06-30.
> Nota auditada: `notes/40-ambrus-reduccion-verificada.md`.
> Estándar: referee. Veredicto abajo separa lo **aceptado** de lo que **exijo re-auditar**.

---

## Resumen del veredicto

Trabajo valioso: resuelve la discrepancia ½-vs-1 (correcto) y trae la corrección
estratégica más importante en semanas (el triángulo NO es el blanco de la reducción
de Ambrus). **Acepto la conclusión estratégica.** Pero la nota tiene **una
inconsistencia interna matemática** en la afirmación de dimensión y un **problema de
higiene reincidente** (fuente primaria otra vez efímera). Ambos deben cerrarse antes
de citar la nota en el paper.

---

## 1. ACEPTADO — la discrepancia ½ vs 1 [correcto]

El argumento es correcto y cierra el Hallazgo #5. Ambrus usa semi-ancho `w_i`
(ancho completo `2w_i`), con `w_K(u_i)=1`, meta `Σw_i ≥ 1/2`, y `rw_T(L̃_i)=2w_i`,
luego `Σ2w_i ≥ 1 ⟺ Σrw ≥ 1`. Coincide con la convención de Ball (half-widths sobre
la bola, `w_K=2`). **No hay discrepancia; es half-width vs full-width.** ✓

## 2. ACEPTADO (con sharpening) — la corrección de foco

**El triángulo NO es el blanco de la reducción de Ambrus para cuerpos planos.** Esto
es correcto e importante, y **robusto** independientemente de la cuestión de
dimensión de §3 abajo: la reducción produce **símplices**, y el triángulo es el
2-símplex, que no es el target. Consecuencia estratégica (la asumo como director):

> "Probar Bang para el triángulo ⟹ conjetura plana" es **FALSO**. El programa del
> triángulo (`notes/30,32,33,36,37`) es **estudio directo de un cuerpo concreto** +
> desarrollo de método, **no** un ataque a la conjetura vía Ambrus.

**Sharpening que agrego (y que la nota debería incorporar):** la construcción toma
**2 puntos por dirección**; con `k` direcciones el símplex tiene dimensión `≈ 2k−1`.
Es decir, los símplices-objetivo tienen dimensión **impar** (`1,3,5,…`) y crecen con
el nº de direcciones. **El 2-símplex (triángulo) nunca es un target** (dim par). Esto
refuerza la corrección: el triángulo está *fuera* del camino de Ambrus por completo.

## 3. EXIJO RE-AUDITAR — inconsistencia interna en la dimensión del símplex

La nota se **contradice a sí misma**:
- **Matiz 1 (§3):** "el símplex objetivo es de dimensión **`2d−1`**; para `d=2` un
  **tetraedro en `R⁴`**, no el triángulo." (dimensión *fija por `d`*).
- **Box de §3:** "Ambrus da: Bang para **todos los símplices (toda dimensión)** ⟹
  cuerpos generales." (dimensión *no fija*).

**Estas dos afirmaciones son incompatibles.** `2d−1` está fijado por la dimensión
ambiente `d`; "toda dimensión" no. No pueden ser ambas correctas.

**Diagnóstico (inferido, a confirmar contra la fuente):** el `2d−1` proviene del paso
"WLOG normales *pairwise-orthogonal* formando **base** de `Rⁿ`" (Matiz 2), que impone
**exactamente `d` direcciones**. Pero:

> **Objeción dura:** en `Rᵈ` hay a lo sumo `d` vectores no nulos pairwise-ortogonales.
> Una cobertura con `>d` direcciones (p.ej. **3 planks en el plano**, el caso central
> del proyecto) **no puede** tener normales pairwise-ortogonales. Luego el "WLOG
> pairwise-orthogonal = base" **no puede aplicarse** a las coberturas que el proyecto
> estudia, salvo que la "simple approximation technique" haga un trabajo mucho mayor
> que un tecnicismo (reducir cualquier cobertura a `≤d` direcciones ortogonales —
> lo cual colapsaría toda la dificultad y sería sospechoso).

Lectura más probable (a verificar): la dimensión correcta es **`2k−1`** con `k` = nº
de direcciones (crece con la cobertura), consistente con "todos los símplices, toda
dimensión". Entonces **"tetraedro en `R⁴`" es un artefacto** del caso `k=2` /
del WLOG mal-escopado, **no** el target general para `d=2`.

**Impacto:** la conclusión estratégica (§2) **no depende** de esto y se mantiene. Pero
la afirmación concreta "target = símplex dim `2d−1`, tetraedro en `R⁴`" está
**probablemente equivocada** y no debe citarse hasta re-auditar. El estatus honesto
de la reducción es **"probada módulo un paso WLOG que, como está transcrito, es
incompatible con coberturas de `>d` direcciones"** — es decir, el "módulo WLOG" NO es
un tecnicismo menor; es el punto que decide (a) la validez para el caso real y (b) la
dimensión del target.

## 4. HIGIENE REINCIDENTE — la fuente primaria volvió a ser efímera

La nota dice: *"Fuente extraída: `scratchpad`/tool-results `ambrus.txt` (pdftotext)."*
Acabamos de arreglar exactamente este error con `ball_fitz.txt` (perdido, efímero) →
`notes/41`. **Y lo re-creamos:** `ambrus.txt` está en scratchpad (efímero), así que
las citas *verbatim* de la nota 40 **ya no son reproducibles desde el repo**.

> **Directiva:** descargar el PDF del apéndice de Ambrus
> (`https://users.renyi.hu/~ambrus/appendix.pdf`) a **`refs/`**. Sin eso, las citas
> verbatim y la re-auditoría de §3 no son verificables.

## 5. Gardner citado de segunda mano (traceabilidad)

La cita de Gardner [12] en §4 viene **vía Ambrus**, y es la de **NO-existencia**
(sin medida de ancho relativo para las facetas del triángulo). Pero `notes/12` (que
según el log ahora "cita la existencia del acoplamiento a Gardner 1988 vía
`notes/40 §4`") necesita el resultado **POSITIVO** de Gardner (existencia para ≤2
direcciones), que **NO** está en §4 (§4 solo tiene el negativo). Traceabilidad rota:
- Para el negativo (obstrucción de medida única, `notes/23/37`): §4 sirve.
- Para el positivo (2-direcciones, `notes/12`): **falta**; requiere Gardner 1988
  directo. **Directiva:** conseguir Gardner 1988 (Pacific J. Math. 135, 1988, 299) a
  `refs/` y citar el resultado correcto por lado.

---

## 6. Implicaciones para la dirección (deltas sobre `auditorias/39`)

1. **P-B (batir B-Y) sube aún más como prioridad #1.** Es **independiente de Ambrus**
   (vale para cualquier cuerpo/dimensión) y es ahora la **única** vía limpia al
   objetivo primario, dado que el triángulo quedó fuera del camino de la reducción.
2. **Reframe del programa del triángulo:** en el paper, presentarlo como "nuevos
   casos + método de transporte/celdas para un cuerpo concreto (el triángulo)", **no**
   como ataque a la conjetura. Honestidad de alcance obligatoria.
3. **Única vía transport→conjetura (opcional, riesgo alto):** el verdadero target de
   Ambrus es un símplex de dim impar (mínimo el **3-símplex**, `k=2` direcciones).
   La caracterización de concurrencia (`1ᵀV⁻¹1=2`, `notes/37`) y el transporte
   (`notes/36`) **se formulan en cualquier símplex**. Extenderlos al 3-símplex sería
   el único puente método→conjetura-plana. Medio-alto esfuerzo; explorar solo si P-B
   se atasca.
4. **Bloqueadores de fuentes (ahora URGENTE):** a `refs/` faltan, y todos son
   descargables:
   - Ambrus, *Appendix: Plank problems* (renyi.hu) — para re-auditar §3.
   - Bakaev–Yehudayoff, arXiv:2602.20290 — para P-B (Lema 5).
   - Gardner, Pacific J. Math. 135 (1988) 299 — para P-3 y `notes/12`.
   - Ball 1991 = **arXiv math/9201218** (¡está en arXiv!) — para cerrar el
     `[PENDIENTE]` de simetrización de `notes/41`.

---

## 7. Estado final de la nota 40

| Ítem | Veredicto |
|---|---|
| ½ vs 1 = half-width | **ACEPTADO** ✓ |
| Foco: triángulo ≠ target de Ambrus | **ACEPTADO** ✓ (robusto; sharpen: dim impar, crece con `k`) |
| Dim `2d−1` / tetraedro en `R⁴` | **RE-AUDITAR** — contradice el box "toda dimensión"; probablemente `2k−1`; depende del WLOG mal-escopado |
| Reducción "probada módulo WLOG" | **PARCIAL** — el WLOG pairwise-ortogonal es incompatible con `>d` direcciones como está transcrito; no es tecnicismo |
| Fuente primaria | **HIGIENE PENDIENTE** — `ambrus.txt` efímero; archivar PDF en `refs/` |
| Gardner (positivo, `notes/12`) | **TRACEABILIDAD ROTA** — §4 solo tiene el negativo; conseguir Gardner 1988 |
