# Correcciones C1–C6 (dictamen Rosa 6 / auditorias/69) → pasada 8

> Date: 2026-07-03. Ejecuta `auditorias/69`. Los 5 puntos de Rosa eran
> correctos; el jefe registró que dos los dejó pasar en su "cleared to send".
> Corregidos todos. **Pasada 8 congelada**:
> `drafts/entregas/affine-plank-triangle-2026-07-03-pasada8.{pdf,tex}`
> (35 pp, 0 errores / 0 undefined / 0 overfull). **No commiteada**: la secuencia
> del jefe es "audito y commiteamos" — espera su auditoría con el chequeo
> definición-vs-prueba. Repo en 00bf059 (pasada 7).

## El fondo, sin adorno

El error central (Problema 1) era mío antes que de nadie: probé `C¹¹¹` (tres
planks, uno por dirección — el espacio `[0,1]⁶` del B&B) pero lo nombré `C_Δ`
(Def 2.3, que admite cualquier número de planks). Objeto probado ≠ objeto
definido. Rosa lo cazó; el jefe lo confirmó línea contra .tex; yo debí verlo.
Corregido, y con el correctivo operativo aplicado a mis propias correcciones
(abajo). La matemática no cambia: el B&B es válido, prueba `C¹¹¹(τ0)=1`, y
sigue siendo un resultado nuevo — el primer triple **tilted no-faceta
no-concurrente** con el bound de un-plank-por-dirección.

## C1 — jerarquía de constantes [HECHO]

Def 2.3 ahora define `C_K` (cualquier nº de planks) **y** `C¹¹¹_K` (exactamente
uno por dirección). Rem 2.4 enuncia `1/D_K ≤ C_K ≤ C¹¹¹_K ≤ 1` con prueba de
cada desigualdad, y los dos gaps del programa: `G_tr = C − 1/D` (transporte),
`G_mult = C¹¹¹ − C` (multiplicidad). La corrección se vuelve enriquecimiento,
como pidió el jefe. **Thm 10.8 reenunciado como `C¹¹¹_Δ(τ0)=1`**; borrado "in
particular C_Δ=1". Tabla de §10 con columna `C¹¹¹` (sandwich: 1, resto según).

## C2 — Lem 10.7 como "finite covering certificate" [HECHO]

Antes: "el árbol crece podando…; es finito porque en caja chica siempre
dispara una poda" — circular (la finitud ≡ la no-existencia buscada). Ahora es
**estático**: "todo árbol binario finito de `[0,1]⁶`, raíz = cubo, nodos
internos = bisección, toda hoja satisface (P1)–(P4) ⟹ no hay cobertura
balanceada propia con Σr≤1". Prueba por inducción (las hojas cubren el cubo) +
Lem 10.5. El teorema **provee** ese árbol como certificado, verificado por el
checker; NO se afirma que un algoritmo termine. Exactamente el fix de Rosa, y
es lo que el checker ya hacía.

## C3 — cláusula de igualdad [HECHO — opción (c)+ ]

Quitada del enunciado del teorema (evita la 2ª dependencia computacional que
chocaba con "sole computer-assisted step"). `C¹¹¹=1` se sostiene por: cota
inferior (Σr≥1) + ínfimo alcanzado por el plank pleno. La caracterización
"solo trivial" queda en **Rem 10.9bis (rem:sandwicheq)** rotulada
"auxiliary": optimización exacta secundaria (`r15_equality.py`, min 2-plank
propio 31/25, 31/25, 5/4 > 1), explícitamente NO parte del certificado. Elegí
(c) sobre la prueba humana (a) por disciplina: una prueba humana nueva de los
mínimos 2-plank es superficie de error nueva, y la caracterización no es
load-bearing para `C¹¹¹=1`.

## C4 — claim de prioridad [HECHO]

"first non-concurrent triple" era FALSO (las facetas también son no
concurrentes, `Σλ=1≠3/2`, y ya tienen el bound por Thm 3.2). Ahora, en
abstract, intro y Thm 10.8/Rem 10.9: **"first genuinely tilted --- non-facet,
non-concurrent --- triple … to our knowledge"**.

## C5 — abstract [HECHO]

"for every concurrent triple … uniqueness" era demasiado amplio (la rigidez
fuerte es cíclica mod flips; el caso same-full-edge de Thm 6.11 no la tiene).
Ahora: "for every concurrent **cyclic** triple … the unique tight covering …
and we classify all concurrent triples admitting a witness."

## C6 — reproducibilidad [HECHO]

Apéndice B: **SHA-256 completos** (64 hex, tabla), entorno (Python 3, solo
`fractions`+`hashlib`, sin terceros), comando de re-verificación, output
esperado exacto (`CERTIFICATE VALID` + conteos), tamaño del certificado,
runtime ("a few minutes, one core"), regeneración determinista, y release
tag/DOI (DOI on acceptance). **Distinción search-evidence vs proof-certificate
escrita**: solo certificado+checker son load-bearing; el buscador es
irrelevante para la corrección y se puede descartar. Añadida la no-vacuidad del
checker (rechaza 4 corrupciones).

## Correctivo operativo aplicado a MIS correcciones (los 3 chequeos del jefe)

- **(i) objeto probado = objeto definido:** Thm 10.8 prueba `C¹¹¹` = ínfimo
  sobre coberturas de 3 planks uno-por-dirección = exactamente el espacio
  `[0,1]⁶` del B&B = Def 2.3 de `C¹¹¹`. Verificado por grep: 0 ocurrencias de
  `C_Δ(τ0)=1` stale; 4 de `C¹¹¹_Δ(τ0)=1`.
- **(ii) ningún lema asume la conclusión:** Lem 10.7 es estático (árbol dado →
  ausencia); no hay argumento de terminación. Sin circularidad.
- **(iii) todo "first/every/all" vs contraejemplo:** "first" → "first
  genuinely tilted non-facet, to our knowledge" (contraejemplo facetas
  descartado por "non-facet"); "every concurrent" → "every concurrent cyclic"
  (contraejemplo same-full-edge descartado por "cyclic"). Los demás "for all i"
  del .tex son cuantificadores rutinarios, revisados.

Corregí además una imprecisión pre-existente que el chequeo (i) destapó
(Rem 6.14 / rem:canon, l.1019): decía que la cobertura canónica "certifies only
C_Δ≤1 (trivial)" — pero su ancho es 1+penalty>1, así que NO certifica ≤1;
reescrito a "no mejora la cota trivial C¹¹¹≤C_Δ≤1".

## Estado y pendiente

- Compila 35 pp, 0/0/0. `CERTIFICATE VALID` sigue válido (el certificado y el
  checker no cambiaron; solo el texto que los enmarca).
- **Pendiente: auditoría del jefe** (con los 3 chequeos), luego commit
  (`audito y commiteamos`), luego re-envío a Rosa. Sin predicción de veredicto.
- Programa post-corrección (órdenes vigentes): V1 (continuación paramétrica
  del certificado: punto → abierto 3-dim), V2 (agregación de Farkas de las 8
  celdas: posible prueba humana del balanceado — resuena con el crux
  ponderado-vs-sin-peso y el lead de las 2 354 celdas). No empezados.
