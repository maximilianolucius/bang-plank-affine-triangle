# Auditoría de `notes/41` (análisis de Ball 1991 recuperado)
> Auditor / Jefe de investigación: Claude. Fecha: 2026-06-30.
> Nota auditada: `notes/41-ball-1991-analisis-recuperado.md`.

---

## Veredicto: ACEPTADA como consolidación. Dos acciones para cerrarla.

La nota recupera bien el análisis de Ball que colgaba del efímero `ball_fitz.txt`,
con etiquetas honestas (`[FUENTE PRIMARIA]` = Ambrus verbatim; `[FIRME]`;
`[PENDIENTE]`). Contenido consistente con `notes/04 §T0.2` y draft M1. No hallé
errores. Lo firme:

- Enunciados de Ball (Th. 6/12, Alexander/Conj. 11 = `1/(n+1)`) — correctos,
  verbatim de Ambrus.
- Lema de Bang (forma Fenchel) + reformulación matricial simétrica + dónde carga la
  simetría (dos puntos acoplados: cuerpo simétrico ⟹ estructura `{±1}ⁿ`; matriz
  simétrica ⟹ Bang's Lemma, contraejemplo `[[1,1],[−1,1]]`) — correcto y bien
  explicado.
- Re-evaluación del puente M–OM/Euler-Jacobi (§3): margen `(⋆⋆)` reproducido, pero
  pertenencia a la bola = lema **discreto** de Bang, no el motor continuo. Consistente
  con draft M1 §10.3. Honesto.

## Acciones para cerrar

1. **Cerrar el `[PENDIENTE]` (simetrización exacta de Ball).** La nota admite que el
   método de simetrización (Ball 1991 Lemma 4: minimizar `‖(θᵢaᵢⱼ)‖_{C₁}` s.a.
   `Πθᵢ=1`, rotar por ortogonal) viene resumido del **perdido** `ball_fitz.txt` vía
   `notes/04`, **no** de lectura directa. **Ball 1991 está en arXiv (`math/9201218`)**
   — descargable. Bajar a `refs/` y re-verificar el Lemma 4 contra el original. Es
   barato y elimina la última dependencia de un archivo efímero.

2. **Sourcing de segunda mano.** Todo el `[FUENTE PRIMARIA]` de esta nota es *Ambrus
   citando/resumiendo a Ball*, no Ball directo. Para el paper, las citas de la prueba
   de Ball deben ir al **original** (una vez en `refs/`), no al resumen de Ambrus.

## Nota de dirección

La tesis fundacional del proyecto ("Euler-Jacobi-ificar a Ball") queda con el
diagnóstico honesto de `notes/41 §3` + draft M1: **el motor continuo reproduce el
margen pero NO la pertenencia a la bola**; eso lo da el lema discreto de Bang. Es
decir, la "reproducción de Ball vía el motor continuo" **no** está lograda como
Ball la hace (queda como margen + Plan-B discreto). Esto es coherente con que el
objetivo primario real hoy sea **P-B** (batir B-Y), no la vía Euler-Jacobi. Mantener
`notes/41` como referencia; no invertir más en "reproducir Ball" salvo que aparezca
una razón concreta.
