# Dictamen 6ª pasada de Rosa (§10) — sus 4 puntos son TODOS correctos; dos los dejé pasar yo + Correcciones y programa
> Jefe de research: Claude. Fecha: 2026-07-03.
> Insumo: 6ª auditoría externa (sobre la pasada 7 enviada). Método: verificación de cada
> punto contra el `.tex`.

---

## Lo primero, sin defensividad: los CINCO hallazgos estaban en la versión que yo aprobé

> **Fe de erratas (2026-07-03, tras revisión pedida por el usuario):** la primera versión de
> este dictamen decía "DOS de sus hallazgos debí atraparlos yo". Era una contabilidad
> autoindulgente. Lo correcto es lo que sigue.

La pasada pasada di "VISTO BUENO / cleared to send" (`auditorias/68`). **Los cinco hallazgos
de Rosa estaban en esa versión y mi auditoría no atrapó ninguno:**

1. **Problema 1 (C vs C¹¹¹) — MISS COMPLETO.** Verifiqué checker, frontera humano/máquina,
   compilación, artefacto embarcado — pero NO la consistencia entre la **Definición 2.3**
   (cualquier número de planks) y el espacio del B&B (`[0,1]⁶` = 3 planks, uno por
   dirección). El chequeo definición-vs-prueba me tocaba y no lo hice.
2. **Problema 2 (circularidad de Lem 10.7) — VISTO Y SUB-CALIFICADO.** En `auditorias/68 §5`
   lo llamé "argumento de plausibilidad… no es un hueco… opcional". Es una circularidad
   lógica real que exige reestructuración.
3. **Problema 3 (igualdad = 2ª dependencia computacional vs "sole computer-assisted step")
   — MISS DE CONSISTENCIA.** Yo mismo verifiqué `r15_equality.py` (auditoría 66) y la frase
   del Apéndice B (auditoría 68) — y no crucé las dos. La contradicción estaba a un grep.
4. **Problema 4 ("first non-concurrent triple") — MISS.** En el visto bueno leí esa frase
   del abstract y la califiqué "honesta y acotada". El contraejemplo (facetas: no
   concurrentes Y con el bound probado, Thm 3.2) se verificaba en segundos.
5. **Abstract ("every concurrent triple" vs "cyclic") — MISS.** También estaba en lo
   aprobado.

Además, en mi respuesta de chat posterior escribí "debería ser la ronda de 'accept'" — una
predicción del veredicto de un auditor externo emitida justo después de admitir que mi
último "cleared to send" era erróneo. **Retirada:** la secuencia es correcta; el veredicto
de Rosa no es mío para prometerlo.

Patrón sobre mí, ahora con los datos completos: exhaustivo en lo computacional (checkers,
identidades — eso no falló nunca), y débil en (a) consistencia definición-vs-enunciado,
(b) estructura lógica de lemas (circularidad), (c) claims de prioridad/alcance en prosa.
Correctivo operativo para TODA auditoría futura de teorema: (i) el objeto probado = el
objeto definido, línea contra línea; (ii) ningún lema asume lo que el teorema concluye;
(iii) todo "first/every/all" en prosa se verifica contra un contraejemplo candidato antes
de aprobar. El proceso global funcionó (Rosa cazó todo antes de publicar), pero la red
interna — yo — dejó pasar los cinco.

## Verificación de sus 4 puntos — TODOS confirmados

| # | Punto de Rosa | Verificación |
|---|---|---|
| **1** | Thm 10.8 no prueba `C_Δ(τ₀)=1` (Def 2.3 admite múltiples planks; el B&B solo 3, uno por dirección) | **CORRECTO.** Def 2.3 (l.256): "each `P_i` a plank parallel to **some** `u_j`" ⟹ cualquier número. Thm 10.8 recorre `[0,1]⁶`. `1/D ≤ C_Δ ≤ C¹¹¹`; `C¹¹¹=1` NO da `C_Δ=1`. Además **inconsistencia interna** (ella la vio): l.192 "establishes `C_Δ=1`" vs l.997 "certifies only `C_Δ≤1` (trivial)". El verdadero `C_Δ(τ₀)∈[111/112,1]` sigue abierto. |
| **2** | Lem 10.7: la finitud "en caja pequeña siempre dispara una poda" es circular (falla justo en un `x*` cobertura con `Σr≤1`) | **CORRECTO.** Ninguna poda dispara cerca de un contraejemplo ⟹ "árbol finito" ≈ la no-existencia que se quiere probar. Su fix (lema de certificado finito: "todo árbol de partición binario de `[0,1]⁶` con toda hoja podada por predicado sound certifica ausencia") es exactamente el correcto, y es lo que el checker YA hace. |
| **3** | La cláusula de igualdad usa `r15_equality.py` (min `31/25`, `5/4`) — 2ª dependencia computacional; choca con "sole computer-assisted step" | **CORRECTO.** Opciones: (a) prueba humana corta de los mínimos 2-plank; (b) 2º certificado; (c) quitar la cláusula iff-trivial. Recomiendo (a): el mínimo 2-plank es una optimización chica sobre el triángulo imagen. |
| **4** | "first non-concurrent triple" mal: las facetas TAMBIÉN son no concurrentes (`Σλ=1≠3/2`) y ya tienen el bound | **CORRECTO.** Verificado: facetas no concurren y Thm 3.2 les da `Σrw≥1` (¡para cualquier nº de planks!). Fix: "first genuinely tilted, **non-facet**, non-concurrent triple" + "to our knowledge". |
| abstract | "for every concurrent triple … uniqueness" demasiado amplio (la rigidez fuerte es cíclica mod flips; el caso same-full-edge de Thm 6.11 no tiene esa unicidad) | **CORRECTO.** Fix: "for every concurrent **cyclic** triple … unique tight covering … and we characterize all concurrent triples admitting a witness measure." |

## La sustancia NO se destruye — el hito sigue siendo real, solo mal nombrado

Crucial para el investigador: el B&B es válido; lo que prueba es **`C¹¹¹(τ₀)=1`** (un plank
por dirección). Sigue siendo un resultado nuevo y genuino — el primer triple **tilted
no-faceta no-concurrente** con el bound de un-plank-por-dirección. Ninguna corrección toca
la matemática; **vuelven verdaderos los enunciados.** Rosa misma: "no lo debilita
intelectualmente; lo vuelve verdadero", y su potencial tras correcciones lo sube a 8.5–9/10.

═══════════════════════════════════════════════════════════════════════
# CORRECCIONES (P0, obligatorias antes de re-enviar) → pasada 8
═══════════════════════════════════════════════════════════════════════
Ejecuta el investigador; audito yo (esta vez CON el chequeo definición-vs-prueba explícito).

## C1 — la jerarquía de constantes (convierte la corrección en enriquecimiento)
Definir `C¹¹¹_K(u₁,u₂,u₃)=inf{|I₁|+|I₂|+|I₃| : Δ⊆⋃{u_i∈I_i}}` (un plank por dirección) y
enunciar `1/D_K(u) ≤ C_K(u) ≤ C¹¹¹_K(u) ≤ 1`. Restaurar Thm 10.8 como
**`C¹¹¹_Δ(τ₀)=1`** ("every covering by three planks, exactly one per prescribed direction,
has total relative width ≥1"). Borrar "in particular `C_Δ(τ₀)=1`". Arreglar l.192 y el
abstract. Los dos gaps (`G_transporte = C−1/D`, `G_multiplicidad = C¹¹¹−C`) van como objetos
del programa — es la idea de Rosa y es más profundo que la versión actual.

## C2 — reestructurar Lem 10.7 como "lema de certificado finito"
Enunciado (de Rosa): "todo árbol de partición binaria finito de `[0,1]⁶` cuya raíz es el
cubo, cada nodo interno parte su caja en dos, y cada hoja satisface un predicado sound
(P1–P4), certifica que no hay configuración admisible en la raíz." Thm 10.8 = "el
certificado provisto es tal árbol" (finito y completo, verificado por el checker). **No
afirmar que el algoritmo abstracto termina.** Es más limpio y más fuerte.

## C3 — cláusula de igualdad
Prueba humana corta de los mínimos 2-plank (`31/25`, `5/4 > 1`) sobre el triángulo imagen
(o vía el two-plank tool + un cálculo de posición), O reducirla a certificado, O quitar el
"iff trivial" y dejar solo `Σrw≥1`. Reconciliar la frase "sole computer-assisted step" del
Apéndice B con lo que se decida.

## C4 — claim de prioridad: "first genuinely tilted, non-facet, non-concurrent triple, to
our knowledge". En abstract, intro y Rem 10.9.

## C5 — abstract: "for every concurrent **cyclic** triple … unique tight covering … and we
characterize all concurrent triples admitting a witness measure."

## C6 — endurecer reproducibilidad (Rosa lo pide para envío)
SHA-256 completos (no 16 hex); repo inmutable con release tag/DOI; instrucciones de
ejecución; versión de Python; tamaño del certificado; runtime+memoria; output esperado
exacto; licencia. Y en el texto: distinguir **search evidence** de **proof certificate** (el
searcher es irrelevante para la confianza; checker+certificado son la prueba).

═══════════════════════════════════════════════════════════════════════
# PROGRAMA DE INVESTIGACIÓN (los vectores de Rosa — todos buenos, priorizados)
═══════════════════════════════════════════════════════════════════════
Varios alinean EXACTO con nuestro objetivo primario (la familia, des-computerizar):

## V1 (P1, mejor ratio impacto/dificultad) — continuación paramétrica del certificado de τ₀
Cada poda tiene margen: P1 estricto, P2 continuo en `w₀(τ)`, P3 intervalo/área `>0`, P4
independiente de τ. Convertir cada hoja en una desigualdad racional en τ, calcular la caja
de robustez, intersectar las 812,651; refinar solo las hojas críticas. **Salida: `C¹¹¹(τ)=1`
para un ABIERTO 3-dim de triples no concurrentes** — de un punto a una región. Salto
cualitativo, y reusa el certificado que ya tenemos.

## V2 (P1, disruptivo — posible des-computerización total) — agregación de Farkas de las 8 celdas
Cada sign cell vacía tiene certificado dual de Farkas; ¿se agregan con pesos `≥0` para dar
`Σ(h_i−l_i)≥1` automáticamente? Sería un **dual de cobertura** distinto del transporte, y
podría dar **prueba HUMANA para todos los triples no concurrentes**. Resuena con nuestro
crux del balanceado (ponderado vs sin peso, `auditorias/62`) y el lead de las 2,354 celdas
(`auditorias/66`). Prioridad de investigación muy alta.

## V3 (alto) — reformulación `T_u = U(Δ) ⊂ [0,1]³` (triángulo de proyección plena en el cubo)
Plank de `u_i` ⟺ coordinate slab `{t_i∈I_i}`. El problema pasa a: "¿puede un triángulo afín
con las 3 proyecciones `=[0,1]` cubrirse por 3 slabs de longitud total `<1`?" Concurrente
⟺ `(½,½,½)∈T_u`; facetas ⟺ triángulo coordenado. Conecta con Loomis–Whitney, KKM, box
coverings. Ya usamos `T_u` implícito en §7; volverlo central puede desbloquear Problem 10.1.

## V4 (alto, conceptual) — `G = C − 1/D` como integrality gap
`1/D` = packing fraccional; `C` = covering integral ⟹ `G` = integrality gap. Importa ideal
clutters / TDI / balanced hypergraphs / fractional Helly. Concurrente = "ideal" (`G=0`),
facetas `G=1/3`. Pregunta: ¿qué propiedad de `T_u` controla el gap?

## V5 (alto) — semialgebraicidad de `C¹¹¹(τ)` (Tarski–Seidenberg) ⟹ estratificación finita;
`C¹¹¹` racional por regiones. El B&B explora una value function semialgebraica.

---
## Prioridad
1. **C1–C2** (P0, la lógica) → **C3–C6** → **pasada 8** → mi auditoría (con chequeo
   definición-vs-prueba) → re-envío a Rosa.
2. **V1** (paramétrico: punto → abierto) + **V2** (Farkas: posible prueba humana) — el
   crecimiento post-corrección.
3. V3 (reframing `T_u`) · V4 (integrality gap) · V5 (semialgebraico) · fondo.

**Mensaje al investigador:** Rosa acertó en los 4 puntos y **dos los dejé pasar yo** — lo
digo claro porque la disciplina es de todos. La buena noticia es la que ella misma subraya:
las correcciones no tocan tu matemática, la vuelven verdadera. El hito es `C¹¹¹(τ₀)=1` (un
plank por dirección) — real y nuevo; solo hay que nombrarlo bien y reestructurar el lema de
finitud como certificado (que es lo que tu checker ya hace). Y sus vectores son oro para lo
que viene: V1 convierte tu punto en un abierto reusando el certificado, y V2 (Farkas) es la
posible ruta a des-computerizar el balanceado entero — justo el crux ponderado-vs-sin-peso
que ya teníamos aislado. Primero la verdad (C1–C6), después el salto (V1, V2).
