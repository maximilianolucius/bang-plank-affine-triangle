# Auditoría Ronda 15 — CERTIFICATE VALID reproducido por el auditor; el hito queda submission-ready (pendiente solo del dictamen p6)
> Auditor / Jefe de research: Claude. Fecha: 2026-07-03.
> Método: **ejecuté el checker yo mismo**; corrí MIS PROPIOS controles negativos (no los del
> investigador); verifiqué SHAs, consistencias de árbol y la clasificación de igualdad; revisé
> la estructura de los lemas redactados.

---

## Veredicto: R15-1 CERRADO con autoridad independiente. `C₃(sandwich)=1` está blindado.

### 1. El checker — ejecutado por MÍ: `CERTIFICATE VALID` ✓
- Corrida propia: **22 s**; `w0=2/25` recomputado por el checker; **812,650 internos +
  812,651 hojas** (identidad de árbol binario ✓ — y cuadra con `splits=812650` y
  `1,625,301` cajas del run de R14, consistencia que verifiqué antes de correr nada);
  teselación de `[0,1]⁶` confirmada (splits estrictamente interiores, stream consumido,
  pila vacía); cada hoja re-validada con geometría propia; desglose
  `P1=286024, P2=53907, P3edge=428672, P3cell=2354, P4=41694` — y
  `428672+2354=431026` = el `P3` del run principal ✓.
- **SHAs verificados por mí:** `b2468aa9` (buscador), `ead66ff2` (certificado),
  `90a25ce8` (checker) — coinciden con los del Apéndice B propuesto ✓.
- Diseño del certificado correcto y astuto: almacena SOLO la forma del árbol
  (splits + regla/testigo), **forzando al checker a reconstruir la aritmética de cajas por
  su cuenta** — máxima independencia.

### 2. Controles negativos — LOS MÍOS, no los reportados ✓
Mutación de regla de hoja (`L1→L4`): **rechazada** (fallo de validación); árbol truncado
(−100 líneas): **rechazada** ("tree incomplete: 9 unexpanded boxes remain"); header `W0`
alterado: **rechazada** ("w0 mismatch: checker 2/25 vs header 1/5"). El checker tiene
dientes ante tampering que el investigador no eligió. *Menor no bloqueante:* la mutación de
regla muere por excepción (IndexError) en vez de assertion limpia — cosmético (cualquier
no-validación es rechazo; el único peligro sería un tamper que PASE, y no lo hay), pero
endurecer el parser a assertions con mensaje es pulido barato.

### 3. Igualdad — [PROVED] verificada
Corrí `r15_equality.py`: mínimos sobre coberturas PROPIAS de 2 planks = `31/25, 31/25, 5/4`
(> 1, exactos) ⟹ no hay coberturas tight propias de 2 planks; con la estrictitud del
balanceado (B&B) y el R13: **`C₃(sandwich)=1` alcanzado SOLO por las coberturas triviales.**
La caracterización de igualdad queda completa.

### 4. R15-2 — dos hallazgos honestos
- **La simetría del sandwich NO existe** (τ₁=13/25 la rompe) — negativo verificado y
  reportado sin maquillaje; la 3-fold vive en la familia tilt. Correcto.
- **Baseline de des-computerización — el dato estructural de la ronda:** núcleo
  genuinamente-máquina = P1+P3 = 717,050 hojas; de las P3, **solo 2,354 necesitan el test
  2-D de celda; 428,672 cierran por arista descubierta (1-D)**. La frontera hace casi todo
  el trabajo ⟹ el thin-plank/boundary lemma correcto podría comerse >99% del núcleo.
  Lead de investigación de primera.

### 5. R15-3 — documentación lista y bien estructurada
`notes/58-R15-lemas-soundness.tex`: los 5 lemas (extremo, soundness P1–P4, test de
no-cobertura completo, reducción-a-árbol, terminación) + teorema principal etiquetado
"partially computer-assisted" con frontera humano/máquina explícita + igualdad — todo como
matemática redactada, etiquetas placeholder para reconciliar al integrar ✓.
`notes/58-R15-appendixB-pilar5.tex`: Apéndice B re-scoped con la frase exacta acordada +
protocolo con SHAs + doble árbol como corroboración (no sustituto) ✓. `.tex` vivo intacto
(congelación) ✓.

## Estado del hito
**`C₃(sandwich τ=(13/25,½,½)) = 1, alcanzado solo trivialmente** — primera terna no
concurrente del triángulo con Bang(3) probado — [PROVED, partially computer-assisted],
con: 5 lemas humanos, certificado exacto en ℚ, checker independiente ejecutado por el
auditor, controles negativos propios del auditor, doble árbol corroborante, igualdad
clasificada, y protocolo de reproducibilidad con hashes. **A prueba del estándar de la
6ª pasada.** Bloqueado SOLO por la congelación (dictamen de la pasada 6 pendiente).

## Cola (sin órdenes nuevas de investigación — la secuencia R15-4 está vigente)
1. **Esperar el dictamen de la pasada 6** → auditarlo (pausa todo).
2. Integrar: respuestas + paquete C₃ (notes/58-*) con UNA tabla de numeración.
3. **Mi auditoría de la integración** → **pasada 7** con hand-off que declara el resultado
   computer-assisted abiertamente (pedido de foco: lemas de soundness + checker).
4. Fondo: thin-plank/boundary lemma (con el lead de las 2,354 celdas), sandwich `D` exacto,
   vectores C, moonshot. Menor: assertions limpias en el parser del checker.
5. Usuario: bloque de autor (ÚLTIMO pendiente no técnico); commit/push del paquete R15
   cuando lo pida.

**Mensaje al investigador:** ronda impecable. El certificado que fuerza al checker a
reconstruir las cajas es diseño de verificación de primera; los mínimos `31/25` cierran la
igualdad con elegancia; y los dos negativos (simetría inexistente, baseline honesto) valen
tanto como los positivos. Corrí el checker y mis propios tampers: todo aguanta. El hito está
blindado — ahora es cuestión de secuencia, no de matemática. Cuando Rosa devuelva la pasada
6, integramos y le presentamos el primer resultado del proyecto dentro del territorio
abierto, con un estándar de verificación que no va a poder objetar.
