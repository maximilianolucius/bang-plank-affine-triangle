# R7-0 — Paquete de entrega: tercera pasada de doña Rosa

> Date: 2026-07-02. Status: **[LISTO PARA ENTREGAR]** — lo entrega el jefe de research.
> Versión congelada: `drafts/entregas/affine-plank-triangle-2026-07-02-pasada3.pdf`
> (11 pp; compila 0 errores / 0 undefined / 0 overfull; idéntica al `.tex` vivo a fecha
> de hoy, INCLUYE los dos menores de `auditorias/52 §5.1–5.2`).
> El trabajo de R7-2 en adelante entrará en versiones POSTERIORES a esta entrega; esta
> copia no se toca.

## Mensaje sugerido para doña Rosa

Doña Rosa: gracias a su segunda pasada el paper cambió sustancialmente. Las seis
objeciones están resueltas (mapa abajo). Además hay **cuatro piezas nuevas que nunca
fueron auditadas externamente** y son ahora el corazón del paper; le pedimos foco ahí:

1. **Theorem 6.3** (weighted-perimeter: medida testigo para toda terna cíclica
   concurrente, `p` interior al medial) — §6.
2. **Theorem 6.6** (tightness y rigidez: cobertura tight explícita y única para CADA `p`;
   la familia sharp es 2-paramétrica) — §6. La identidad afín `Λ≡S` y el margen `αβγ`
   son los puntos load-bearing.
3. **Theorem 6.8** (caracterización de tres direcciones: medida ⟺ concurrencia de
   mid-lines, para ternas no paralelas dos a dos; cierra la pregunta de existencia de
   Gardner para N=3 en el triángulo) — §6.
4. **Appendix A / Proposition A.1** (clasificación de edge-tilings para τ arbitrario;
   el Lemma 5.2 es el caso τ=½).

## Su objeción mayor de la pasada 2, resuelta como usted pidió

El Lemma 5.2 ya **no** descansa en scripts: tiene **prueba humana completa** en el
Apéndice A (opción (a) que usted prefería), y más general de lo pedido — la clasificación
se hace para ternas cíclicas arbitrarias y el lemma es el caso `τ=½`. Los scripts quedan
como verificación independiente ancillary.

## Mapa objeción → resolución (pasada 2 → esta versión)

| # | Objeción (pasada 2) | Resolución en esta versión |
|---|---|---|
| 1 | "sharp for the simplex" leído como cobertura (falso) | Thm 2.1 reescrito: sharpness del per-plank estimate `μ(P)≤d·rw(P)`; frase explícita "does NOT assert any covering…"; abstract corregido; `d≥2` explícito. |
| 2 | Lemma 5.2 caja negra computacional | Prueba humana: Apéndice A, Prop. A.1 (general τ); Lemma 5.2 = caso τ=½. |
| 3 | "first tight non-facet case" sin soporte | "To our knowledge" + soporte citando [Verreault], [Gardner88], [BY26]. |
| 4 | Thm 7.1 no es teorema formal | Reclasificado Proposición 7.1 con enunciado preciso; lectura metodológica en Remark. |
| 5 | Thm 3.1 sin no-degeneración; cita Gardner imprecisa | Hipótesis non-parallel + caso paralelo en el enunciado; "[Gardner88, Theorem 1]" con alcance. |
| 6 | `d=1`; truncamiento `I⊄[0,1]`; paréntesis contradictorio | `d≥2` en Thm 2.1 (`d=1` trivial anotado); WLOG `I⊂[0,1]` justificado en el modelo; paréntesis eliminado. |

## Cambios menores de última hora (auditoría interna ronda 6, ya incorporados)

- Thm 6.6: unicidad enunciada "one in each of the directions" (un plank por dirección).
- Thm 6.8(b): la cota 1-D cita explícitamente el caso `d=1` de Thm 2.1.

## Qué NO auditar (sin cambios desde su pasada 2)

§2 (salvo el enunciado de Thm 2.1), §3 (salvo hipótesis non-parallel), §4, §5 (salvo la
frase de prioridad), Proposición 7.1 (solo reclasificación). El Apéndice A sustituye por
completo la antigua prueba computacional del Lemma 5.2.
