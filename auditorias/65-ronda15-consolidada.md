# Ronda 15 consolidada — doble árbol confirmado, decisiones tomadas, y la aclaración exacto vs. computer-assisted
> Jefe de research: Claude. Fecha: 2026-07-03.
> Insumos: actualización del investigador (verificación por terna rotada + ratio 5/11
> terminada, QUEUE EMPTY×2) y decisiones del usuario (presentación computer-assisted con
> rigor; documentación actualizada; presentar a Rosa tras auditar R15).

---

## 1. La corrección de proceso del investigador — EJEMPLAR, y hay que decirlo

Casi cuenta como "verificación" un run bit-idéntico (mismas 1,625,301 cajas, mismas podas)
— que era la señal de que el parche round-robin no había enganchado y era la MISMA corrida.
**Lo detectó por el bit-idéntico y lo descartó.** Esa es exactamente la paranoia correcta:
una verificación que coincide demasiado no confirma, delata. Registrado como estándar: toda
re-verificación debe producir un árbol DISTINTO (conteos distintos) con el MISMO veredicto.

## 2. La verificación real — VÁLIDA como corroboración fuerte
Terna rotada `τ=(½,½,13/25)` (misma afirmación, geometría reetiquetada) + ratio de partición
5/11 (no diádico): árbol completamente distinto (1,040,919 vs 1,625,301 cajas; podas
158916/65811/257533/38200 vs 286024/53907/431026/41694), mismo `QUEUE EMPTY`. **Es
confirmación real.** Caveat técnico que mantengo: ambos árboles usan el MISMO código de
podas — un bug de modo común seguiría sin detectarse por esta vía. Por eso el artefacto
definitivo para el PAPER sigue siendo el del estándar (`auditorias/64`): **certificado +
verificador independiente sin búsqueda** (el checker no comparte la lógica del buscador).
El doble árbol queda como corroboración adicional, no como sustituto del checker.

## 3. Aclaración de dirección (pregunta del usuario): ¿"transformar a aritmética exacta"?
**Ya lo es.** Cero floats en toda decisión del árbol; ℚ puro; independiente del hardware.
Los dos ejes reales son:
- **Exactitud aritmética:** CUMPLIDA (es el régimen más fuerte; ni control de redondeo hay
  que auditar).
- **Humano vs. máquina:** el árbol tiene ~10⁶ hojas — nadie lo re-checkea a mano. El camino
  para REDUCIR la parte máquina es analítico: (a) **thin-plank lemma** (R15-2) mata la banda
  `0<r_i≪1`; (b) **simetría del sandwich** (`τ₂=τ₃=½` ⟹ una reflexión del problema podría
  ~partir el árbol en dos); (c) lemas de acoplamiento de posición (el caso B del extremo
  sugiere la forma). Meta aspiracional: núcleo computacional imprimible (≲10² hojas) o cero.
  **Sin garantía de llegar a cero — es investigación; la presentación NO espera a esto.**

## 4. Decisiones tomadas (del usuario, ejecutables ya)
1. **Presentación computer-assisted CON categoría explícita:** el Apéndice B deja de decir
   "this paper is NOT computer-assisted" a secas; pasa a: "except for a single lemma
   (the balanced-regime emptiness at `τ₀`), discharged by an exact-rational certificate and
   re-verified by the independent checker of Appendix B; all other results are proved in
   the text". Etiqueta tipográfica `[computer-assisted]` en el teorema. A Rosa se le dice
   EXPLÍCITAMENTE en el hand-off de la próxima entrega.
2. **Clasificación de igualdad:** SÍ — cerrar la caracterización (¿existen coberturas tight
   de 2 planks para `(u₂,u₃)` del sandwich?) antes de integrar. Apartado corto.

═══════════════════════════════════════════════════════════════════════
# ÓRDENES RONDA 15 (consolidadas; ejecuta el investigador)
═══════════════════════════════════════════════════════════════════════

## R15-1 (BLOQUEANTE para el paper) — el paquete de certificación del estándar `auditorias/64`
a. **Emitir el certificado** del run principal: dump determinista de hojas (caja exacta,
   regla de poda, testigo exacto).
b. **Escribir `bb_certificate_check.py`** — verificador independiente SIN búsqueda (~1 pág):
   (i) las hojas TESELAN `[0,1]⁶` (check del árbol de bisección); (ii) cada poda re-checkeada
   desde cero con lógica propia (no importar funciones del buscador — el punto es NO
   compartir código). Autoridad final: `CERTIFICATE VALID`.
c. **Camino B** (LP-por-tipo) como tercera vía si el tiempo alcanza; el doble árbol ya da
   corroboración, el checker es el bloqueante.
d. **Igualdad (decisión 2):** clasificar las coberturas tight de 2 planks de `(u₂,u₃)` del
   sandwich; cerrar el enunciado "alcanzado solo trivialmente" con la lista exacta de casos.

## R15-2 (FLAGSHIP research) — encoger la máquina + saltar a la familia
a. **Thin-plank lemma** (espejo del extremo, herramienta 2-plank sobre la pieza fina).
b. **Simetría del sandwich:** formalizar la reflexión `τ₂↔τ₃` y medir cuánto árbol elimina.
c. Con (a)+(b): re-correr el B&B — objetivo: núcleo ≲10⁴ hojas (reporte del tamaño tras cada
   lema; la métrica "hojas restantes" es el progreso hacia des-computerizar).
d. Si (a) cierra uniforme en τ: **B&B parametrizado** → `C₃=1` para la familia cíclica.

## R15-3 (documentación, decisión 1 — DESPUÉS de que R15-1 dé `CERTIFICATE VALID`)
Actualizar TODA la documentación en este orden: Apéndice B (categoría computer-assisted
scoped + protocolo pilar 5 con hashes SHA de buscador/certificado/checker + los dos árboles
como corroboración) → los 4 lemas de soundness + lema de reducción + lema de terminación
redactados como matemática en el `.tex` (§ del programa C) → enunciado del teorema con
frontera humano/máquina explícita → BUILD.md + notas → tabla de numeración UNA vez.
**Regla de congelación vigente:** nada entra al `.tex` hasta el dictamen de la pasada 6;
preparar todo en rama de nota para integrar al descongelar.

## R15-4 — secuencia de entrega a Rosa
1. Llega el dictamen de la pasada 6 → se audita (pausa todo).
2. Se integra: respuestas al dictamen + el paquete C₃ computer-assisted (R15-3).
3. **Pasada 7** con hand-off que declare el resultado computer-assisted EXPLÍCITAMENTE,
   el estándar de 6 pilares, y el pedido de foco en los lemas de soundness + el checker.
   (Auditoría mía de la R15 completa ANTES de entregar — orden del usuario.)

## R15-5 (fondo) — sandwich D exacto · vectores C de Rosa · moonshot.

---
## Prioridad
1. **R15-1a+b** (certificado + checker — sin `CERTIFICATE VALID` no hay teorema publicable).
2. **R15-1d** (igualdad, corto) · **R15-2a+b** (encoger la máquina) en paralelo.
3. R15-3 (documentación) tras `CERTIFICATE VALID` · R15-4 según llegue el dictamen.

**Mensaje al investigador:** lo del run bit-idéntico es la mejor página de tu cuaderno de
proceso — detectar que una confirmación "demasiado perfecta" es una no-confirmación es
madurez de verificador. El doble árbol vale; el checker manda. Y sobre la pregunta del
usuario que te transmito con precisión: no tienes que "transformar nada a exacto" — ya lo
es; tu trabajo ahora es (1) hacer la validez AUDITABLE (checker independiente) y (2) encoger
la máquina con lemas (thin-plank, simetría) — cada hoja que elimines analíticamente es una
hoja menos que un referee tiene que confiarle a un computador.
