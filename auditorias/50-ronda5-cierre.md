# Auditoría Ronda 5 — teorema del perímetro ponderado, ejecución R5-0/1/4, re-auditoría de doña Rosa + Órdenes Ronda 6
> Auditor / Jefe de research: Claude. Fecha: 2026-07-02.
> Alcance: `notes/49-R5-3` (teorema nuevo), `notes/49-R5-4` (rescate M1), ejecución R5-0/R5-1,
> y dictamen sobre la segunda auditoría de doña Rosa (esta vez del PDF correcto).
> Método: verificación a mano de las 6 identidades + ejecución de los 3 scripts + cotejo de
> cada objeción de doña Rosa contra el texto real del `.tex`.

---

## 1. `notes/49-R5-3` (perímetro ponderado) — **[PROVED] CONFIRMADO. Resultado excelente.**

El mejor resultado de investigación del proyecto desde las medianas. Lo verifiqué por tres
vías independientes:

1. **A mano, las 6 identidades.** Con `τ_1=(½−p_C)/p_A` etc. y masas `w_AB=1−2p_C`,
   `w_BC=1−2p_A`, `w_CA=1−2p_B` (suma `3−2Σp=1` ✓): para `u_1`, densidad en `[0,τ_1]` es
   `w_BC+w_AB/τ_1 = (1−2p_A)+2p_A = 1` (usando `(1−2p_C)/(½−p_C)=2`); en `[τ_1,1]`,
   `1−τ_1=(½−p_B)/p_A` da `w_CA/(1−τ_1)=2p_A` ⟹ densidad `1`. Las 4 restantes (u_2, u_3)
   colapsan idéntico. **Correctas las 6.**
2. **Simbólico:** corrí `experiments/weighted_perimeter_theorem.py` → las 6 expresiones
   simplifican a `1` exacto (sympy). MC: dev ≈ 0.015–0.016 = ruido en 3 ternas. ✓
3. **Terna ejemplo exacta:** corrí `concurrent_nonmedian_triple.py` →
   `p=(9/20,3/10,1/4)`: `τ=(5/9,4/5,1/6)`, todas en `(0,1)`, ninguna `=½`;
   `1ᵀV⁻¹1=2` exacto y `V⁻¹1≥0` (consistente con Prop. de concurrencia). ✓
   `concurrent_perimeter_densities.py`: residual `1.9e-14`, densidades no-negativas. ✓

**Dominio:** verifiqué la equivalencia `τ_i∈(0,1) ∀i ⟺ max_j p_j<½ ⟺ masas >0` — correcta,
y además **automática**: terna cíclica válida + concurrencia interior ⟹ `max p_j<½` sin
hipótesis extra. Anti-cíclico por reflexión: correcto (una transposición de vértices lleva el
patrón anti-cíclico al cíclico con `p` reflejado, y el medial es invariante).

**Alcance honesto de la nota:** impecable — patrones mixtos `[OPEN]`, tightness para
`p≠centroide` `[OPEN]`, la evidencia LP 453/453 queda explicada para el patrón cíclico. Sin
overclaim. La incorporación al paper (Thm 6.3 `thm:wper`) ya está hecha y la revisé línea a
línea: fiel a la nota, sin reclamar sharpness. El paper pasa de 5 a **6 páginas** y compila
limpio (log: 0 errores).

**Consecuencia estructural que el paper aún NO explota (ordenar en R6-1f):** combinando
Prop 6.1 (necesidad) + Thm 6.3 (suficiencia), para el patrón cíclico queda una
**caracterización completa**: *una terna cíclica admite medida de marginal uniforme ⟺ sus
líneas de medio nivel concurren en un punto interior*. Es un corolario gratis de una línea y
sube el valor del paper (primer "iff" del proyecto). Verifiqué que `V` es siempre invertible
en el patrón cíclico (`det = −τ_1τ_2τ_3−1 ≠ 0`), así que el corolario no necesita hipótesis
de invertibilidad.

## 2. Ejecución R5-0 / R5-1 / R5-4 — VERIFICADA ✓

- **R5-0:** `drafts/obsolete/` existe con los 3 artefactos tóricos + `README-OBSOLETE.md`
  correcto; `BUILD.md` reescrito ("UN SOLO MANUSCRITO VIVO"). Imposible repetir el incidente. ✓
- **R5-1:** `drafts/ancillary/` con los 4 scripts + README descriptivo. **Pendiente
  declarado:** bloque autor/afiliación (decisión del investigador, placeholder marcado). ✓
- **R5-4:** `notes/49-R5-4` registra el material M1 con el test polynomial escrito
  correctamente (`g=ΔP_m−n·g₂`, ambos sumandos polinomios) — exactamente el punto 1 de la
  primera auditoría de doña Rosa. Disposición razonable (M1-working-notes se conserva). ✓
- **Higiene menor:** los ficheros `hamilton-jacobi-*` en `drafts/` son de otro trabajo
  (BUILD.md ya lo declara). Recomendación: moverlos fuera de `drafts/` de este proyecto —
  la política es "un solo manuscrito vivo" y son el tipo de artefacto que confunde a un
  auditor externo. No es orden bloqueante.

## 3. Dictamen sobre la re-auditoría de doña Rosa (segunda ronda)

**Esta vez auditó el paper correcto** — su numeración (Thm 2.1/3.1/3.2/4.1/5.1, Lemma 5.2,
Prop 6.1/6.2, Thm 7.1) coincide con `affine-plank-triangle.tex`. **Pero leyó la versión del
1-jul (5 pp), previa al Thm 6.3:** no menciona el perímetro ponderado en ninguna parte, y lo
que llama "resultado principal" es solo medianas. ⟹ **el teorema nuevo NO tiene auditoría
externa todavía** (R6-3).

Su veredicto "major revision" es razonable como referee. Cotejé cada objeción contra el
`.tex` real; mi dictamen punto por punto:

| # | Objeción | Dictamen | Evidencia |
|---|---|---|---|
| 1 | "sharp for the simplex" (Thm 2.1) mal formulado | **VÁLIDA — corrección obligatoria** | El enunciado (l.119) y el abstract (l.46) dicen "sharp at/for the simplex" a secas. Leído como enunciado de cobertura es **falso** (contradiría la propia conjetura, y el propio Thm 3.2 del paper da `≥1` faceta-paralelo en el símplex). Lo que es verdad —y lo que la última línea de la prueba ya dice— es que la **desigualdad por-plank** `μ(P)≤d·rw(P)` es sharp en el símplex ⟹ el método de una-sola-medida no puede superar `1/d`. Su reescritura propuesta es exactamente la correcta. |
| 2 | Lemma 5.2 = caja negra computacional | **VÁLIDA a medias; el estándar que pide es el correcto** | El paper SÍ describe la enumeración (27 patrones × órdenes, exacto sobre ℚ) y cita scripts archivados + verificación independiente (yo corrí ambos: 3 soluciones exactas). Pero tiene razón en que "reproducible desde un script no incluido" no alcanza para el resultado central: hace falta **prueba a mano en apéndice** o **certificación formal** (qué enumera, por qué es exhaustiva, ancillary con outputs). Ver R6-2. |
| 3 | "first tight non-facet case" = claim de prioridad sin soporte | **VÁLIDA (moderada)** | Aparece en abstract y §5 sin justificación bibliográfica. Fix estándar: "to our knowledge" + una frase apoyada en el survey de Verreault (ninguna instancia comparable aparece allí). No exige eliminar el claim. |
| 4 | Thm 7.1 no es un teorema formal ("Bang's sign argument" indefinido) | **VÁLIDA** | El contenido matemáticamente probado es: (a) el ratio del chord lemma es tight (segmento), (b) el presupuesto de movimiento del testigo es exactamente `ℓ/2`. Eso es una **Proposición** sobre el paso del chord-lemma; la lectura metodológica ("ningún normalizador mayor es alcanzable por esa vía") pertenece al Remark — que ya existe (l.361-367). Su reescritura propuesta es la honesta. Reclasificar, no borrar: el contenido es correcto (lo verifiqué en `notes/44`). |
| 5 | Thm 3.1 sin hipótesis de no-degeneración + cita de Gardner imprecisa | **VÁLIDA** | Si las dos direcciones son paralelas (formas afínmente dependientes, `f_v∈{f_u,1−f_u}`), `Φ` no es biyección y la prueba tal como está escrita falla. El caso paralelo es trivial (una dirección: empujar a `[0,1]`, cubrir un intervalo con intervalos ⟹ `Σ|I_i|≥1`) — falta decirlo. Y "By Gardner" debe ser "by [Gardner88, Thm 1]" con sus hipótesis. Ambos fixes de una línea. |
| 6 | `d=1` en Thm 2.1; truncamiento de `I_i`; estilo | **VÁLIDAS (menores)** | La prueba usa `V^{1/(d−1)}` ⟹ enunciar `d≥2` (el caso `d=1` es trivial: `Σrw≥1`). El modelo (l.102) ya fija `I⊂[0,1]`, pero la prueba de medianas tiene el paréntesis "(or ≤ r_i if I_i⊄[0,1])" que lo contradice — resolver con un WLOG en el modelo (truncar a `I∩[0,1]` preserva cobertura y no aumenta `rw`) y borrar el paréntesis. |

**Lo que ella valida** (Thm 3.2, Thm 4.1, Prop 6.1, Prop 6.2, la cota de medianas) coincide
con mis verificaciones previas — convergencia independiente, buena señal.

**Calibración del "major revision":** correcto como etiqueta de referee, pero conviene
cuantificarlo: **todas** las correcciones salvo la del Lemma 5.2 son de redacción/
formalización (≈1 día de trabajo); ninguna toca la validez de un resultado. La única con
contenido real es la certificación/prueba del Lemma 5.2. Y su puntuación de rigor (5/10) está
tomada sin poder correr los scripts y **sin haber visto el Thm 6.3** — está desactualizada
por construcción.

═══════════════════════════════════════════════════════════════════════
# ÓRDENES DE TRABAJO — RONDA 6 (ejecuta el investigador)
═══════════════════════════════════════════════════════════════════════

## R6-1 (OBLIGATORIO, ~1 día) — correcciones de referee al `.tex`
a. **Thm 2.1:** reescribir la sharpness — enunciado: "`Σrw≥1/d` (`d≥2`; `d=1` trivial). The
   per-plank estimate `μ(P)≤d·rw(P)` is sharp at the simplex; hence no single-measure
   argument can improve `1/d`." Corregir el abstract en el mismo sentido ("sharp at the
   simplex" → sharpness del método).
b. **Thm 3.1:** hipótesis "two non-parallel directions" + una línea despachando el caso
   paralelo + cita precisa "[Gardner88, Theorem 1]" (con sus hipótesis).
c. **Prioridad:** "to our knowledge, the first tight non-facet case…" + frase de soporte
   citando el survey [Verreault] (abstract y §5).
d. **Thm 7.1 → Proposición** ("the chord-lemma step is sharp; hence no direction-normalizer
   `N>ℓ` is attainable by the iterated chord-lemma placement") + la lectura metodológica se
   queda en el Remark existente. Actualizar las referencias cruzadas (abstract, intro, §8).
e. **Modelo:** WLOG `I⊂[0,1]` con justificación de una línea; borrar el paréntesis de la
   prueba de medianas.
f. **Corolario nuevo (gratis):** "for cyclic triples, a uniform-marginal witness measure
   exists **iff** the mid-level lines concur at an interior point" (Prop 6.1 + Thm 6.3) +
   una frase: el patrón anti-cíclico se cubre por reflexión (hoy el `.tex` under-claima
   respecto a `notes/49-R5-3`).
**Hecho:** todas las objeciones válidas de doña Rosa cerradas en el `.tex`; compila.

## R6-2 (el único punto con contenido) — Lemma 5.2 a estándar de publicación
**Opción (a), preferida:** prueba humana completa en un apéndice. La enumeración es finita y
chica; explotar la simetría cíclica de la configuración de medianas para colapsar los 27
patrones a pocas clases (el caso genérico ya está a mano: `l_i=⅓`, `h_i=⅔`). Intentarlo en
serio (~1-2 días).
**Opción (b), fallback:** certificación formal en el paper: (i) enunciado preciso del
algoritmo (por qué patrón×orden ⟹ sistema lineal; por qué la lista es exhaustiva), (ii)
ancillary files con outputs exactos y hash/versión, (iii) la verificación independiente
citada como tal. Doña Rosa aceptó explícitamente esta vía.
**Hecho:** el resultado central deja de pedir confianza en caja negra.

## R6-3 — tercera pasada de doña Rosa, versión 6 pp
Re-entregarle el PDF recompilado tras R6-1/R6-2 señalando: (i) qué objeción suya se resolvió
dónde (mapa de 1 línea por punto), (ii) que el **Thm 6.3 (perímetro ponderado) es nuevo desde
su lectura y no tiene auditoría externa** — pedirle foco ahí y en el apéndice del Lemma 5.2.

## R6-4 (research, acotado) — tightness/rigidez para `p≠centroide` en la familia cíclica
Pregunta exacta: ¿se alcanza `Σr=1` para alguna terna cíclica con `p≠centroide`?
- Adaptar la maquinaria de enumeración de medianas (trazas por arista con breakpoints en
  `τ_i`, sistemas lineales exactos sobre ℚ) a la terna ejemplo `τ=(5/9,4/5,1/6)`.
- La evidencia previa (`notes/38 §1`, min≈1.0003 en grilla) sugiere que **NO** — si se
  confirma exacto, el resultado es: *dentro de la familia cíclica, la igualdad se alcanza
  solo en las medianas* — rigidez de familia que empareja perfecto con Prop 6.2 y sube otra
  vez el techo del paper. Si SÍ se alcanza: segundo caso tight, también publicable.
**Regla:** exacto/racional; la grilla no decide (lección `notes/33`).

## R6-5 (research, acotado) — patrones mixtos: clasificar y decidir
1. Clasificación finita: qué asignaciones de roles no-cíclicas admiten terna válida
   (`τ_i∈(0,1)`) concurrente en `p` interior — análisis exacto, son pocos casos módulo
   simetría.
2. Para cada patrón admisible: intentar el ansatz de perímetro ponderado con masas libres
   (3 incógnitas, 6 ecuaciones — en el cíclico colapsan; ver si en mixtos el sistema es
   incompatible), luego ansatz con átomos/masa interior, y si todo falla, refutación por
   Kellerer con LP exacto racional.
3. Reportar de paso: ¿las 453 ternas del LP de `notes/37` incluían patrones mixtos, o eran
   todas cíclicas? (Si eran cíclicas, la evidencia sobre mixtos es hoy CERO.)
**Hecho:** suficiencia de concurrencia en `d=2` decidida patrón por patrón, o reducida a los
casos mixtos con veredicto parcial.

## R6-6 (moonshot, fondo) — acoplamiento (batir B-Y)
Sin cambios (`auditorias/48`).

---

## Prioridad
1. **R6-1 + R6-2** — el paper es el deliverable y ahora es MEJOR que el que doña Rosa puntuó;
   cerrar sus objeciones lo deja submission-ready de verdad.
2. **R6-3** — auditoría externa del estado real (con Thm 6.3).
3. **R6-4** — la apuesta acotada más valiosa (rigidez de familia; la evidencia ya apunta a un
   teorema limpio).
4. **R6-5** — completa el cuadro de suficiencia en `d=2`.
5. R6-6 fondo.

**Mensaje al investigador:** el perímetro ponderado es exactamente el tipo de resultado que
este proyecto necesitaba — simple, verificable a mano, y convierte un punto (medianas) en una
familia 2-paramétrica con caracterización iff. La ronda de doña Rosa, esta vez sí sobre el
paper real, deja una lista corta y ejecutable; ninguna objeción toca la validez de un
resultado. Ejecutar R6-1/R6-2 sin regatear: su estándar es el de un referee real y es el que
queremos pasar.
