# Auditoría Ronda 4 (paper corregido + `notes/48`) + Órdenes Ronda 5
> Auditor / Jefe de research: Claude. Fecha: 2026-07-01.
> Alcance: R4-1 (fix faceta), R4-2 (hardening+biblio), R4-3 (referee pass), R4-4 (`notes/48`).

---

## Veredicto: el paper quedó REFEREE-CLEAN. Ronda excelente.

Todo lo que marqué en la Ronda 3 está resuelto y **lo verifiqué**:

- **R4-1 — fix faceta-paralelo: CORRECTO (verificado paso a paso).** La nueva prueba
  (`1∈C_1+…+C_{d+1}` por Minkowski; BM-1D ⟹ `|D∩[0,1]|≥1−Σ_{k≤d}|U_k|`;
  `|(1−C_{d+1})∩[0,1]|=1−|U_{d+1}|`; suma `=2−R>1` ⟹ intersecan ⟹ `1∈ΣC_k`) es **sólida**.
  El Remark que explica por qué la arista NO sirve (y por qué ninguna medida testigo tampoco,
  por concurrencia) es acertado. **El error bloqueante está eliminado.** ✓✓
- **R4-2 — hardening + biblio:** rigidez enunciada como **lema asistido-por-computador**
  citando `experiments/median_rigidity_enumeration.py` (que **corrí**: 3 edge-tilings exactos)
  + verificación independiente; caso genérico self-contained. Biblio **corregida**: `Bang53`
  eliminada (y la frase del intro reformulada), `Verreault` → título/fecha correctos (v2, 2025),
  `Gardner` con no.2. ✓
- **R4-3 — referee pass:** el `.tex` compila limpio (5 pp). Revisé cada teorema; todos pasan
  (1/d, 2-dir, faceta [ya corregido], 3-facetas+1, medianas cota+rigidez, concurrencia, no-go).
- **R4-4 — `notes/48`: teorema nuevo CORRECTO + crux honesto.** Verifiqué la Proposición
  "perímetro ⟺ `τ=½`": densidad total `1/(3τ)+1/3` en `[0,τ]` y `1/(3(1−τ))+1/3` en `[τ,1]`,
  ambas `=1` ⟺ `τ=½`. **Correcta.** Explica rigurosamente por qué las medianas son el único
  caso tight con medida explícita en la familia de concurrencia; buen añadido al paper (modesto
  pero real: es sobre *esa* medida, no una caracterización de qué direcciones admiten *alguna*).
  El resto de `notes/48` (estructura 2-dim de la familia, reducción de Kellerer, autocrítica del
  test inválido `u_0` no-onto, crux honesto) es sólido y sin overclaim.

**Estado del deliverable: ENTREGADO.** Paper honesto, referee-clean, 5 pp, 7 resultados
probados (A–G), scripts reproducibles archivados, alcance explícito. Es el resultado seguro y
está en mano.

---

## Reevaluación estratégica (honesta, importante)

El proyecto llegó a un **punto de cierre natural**. Lo que queda para el objetivo primario
("avanzar la conjetura / batir SOTA") son **dos problemas abiertos genuinos, sin ruta tratable
conocida**:

1. **Suficiencia de concurrencia** — reducida (rigurosamente) a un **3-marginal de Kellerer**
   sobre un triángulo 2-dim, para `τ≠½`. Media y varianza automáticas; el hueco son los
   momentos `≥3`. El template de Gardner (segmentos, 2 direcciones) **no** cierra el caso
   3-marginal 2-dim. Es el hueco finito abierto de Gardner en la rebanada de concurrencia.
2. **Batir B-Y** — tras el no-go de `notes/44` (verificado), requiere un **certificado de
   acoplamiento** (testigo que no sea el punto del sistema de Bang). Moonshot, sin ruta conocida.

No hay atajo incremental para ninguno. Debo decirlo con claridad: **el crecimiento adicional
del resultado exige resolver matemática abierta dura, no ejecutar tareas.**

═══════════════════════════════════════════════════════════════════════
# ÓRDENES DE TRABAJO — RONDA 5
═══════════════════════════════════════════════════════════════════════

## R5-1 (cierre del deliverable) — finalizar el paper para submission
El paper está referee-clean; falta lo administrativo/editorial:
- Bloque de autor + agradecimientos; revisar `\today`; una pasada de estilo/notación.
- Opcional: 1–2 figuras (tercio-central de medianas; teselación del perímetro).
- Decidir venue (Mathematika / DCG / Monthly) y preparar versión arXiv.
**Entregable:** `.tex` submission-ready. **Riesgo:** nulo. Es el cierre.

## R5-2 (research #1, BOUNDED e informativo pase lo que pase) — un triple concurrente NO-mediana
En vez de atacar la suficiencia general (dura), resolver **un solo caso explícito** `τ≠½`:
- Elegir una terna concurrente concreta con `p` interior, `τ_i≠½` (usar la parametrización de
  `notes/48 §1`).
- **Intentar construir a mano** una medida con las 3 marginales uniformes (barrido 2-dim, no
  cevianas desde `p` —ya fallan—; probar familias de segmentos paralelos a cada arista de la
  imagen, o una densidad AC explícita).
- **O demostrar que NO existe** (Kellerer: exhibir `(φ_1,φ_2,φ_3)` con `Σφ_i(u_i)≥0` en `Δ`
  pero `Σ∫φ_i<0`). Usar **LP exacto/racional fino**, no grid grueso (el LP previo era
  grid-inestable, `notes/47/48`).
**Por qué:** ambos desenlaces son publicables. Si **existe** ⟹ hint fuerte de suficiencia (y un
segundo caso tight no-faceta más allá de medianas). Si **no existe** ⟹ **concurrencia es
necesaria pero NO suficiente** — resultado nuevo que *sharpea* la caracterización (y acota el
método de transporte por dentro). **Riesgo:** medio; **valor:** alto en cualquier caso.
**Es la mejor apuesta de crecimiento.**

## R5-3 (moonshot, fondo) — certificado de acoplamiento (batir B-Y)
Sin cambios: única vía a la SOTA tras el no-go. Celdas de escape + Farkas (`notes/30 §8.5`),
semilla 6 celdas mixtas (`notes/33 §6`), nugget = transversalidad en `R=1`. Muy alto riesgo,
sin ruta conocida. Solo con capacidad sobrante.

---

## Prioridad y mensaje honesto
1. **R5-1** — cerrar y (si el usuario quiere) publicar el paper. **El deliverable está listo.**
2. **R5-2** — el único experimento acotado que aún puede mover la aguja (construir o refutar un
   caso no-mediana). Informativo en ambos sentidos.
3. **R5-3** — moonshot.

**Recomendación de dirección:** considerar el objetivo de "resultado sólido y honesto"
**cumplido** (paper referee-clean con un caso tight no-faceta con rigidez + un no-go
estructural). Batir B-Y y probar la conjetura siguen siendo frontera de expertos 2026 sin ruta
conocida; perseguirlos es investigación de alto riesgo, no ejecución. R5-2 es el siguiente paso
con mejor relación valor/riesgo; el resto es finalización o moonshot.
