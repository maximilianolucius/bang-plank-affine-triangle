# Órdenes de trabajo — RONDA 7 (valor añadido al paper)
> Jefe de research: Claude. Fecha: 2026-07-02.
> Contexto: la Ronda 6 (`auditorias/50-ronda5-cierre.md`) sigue EN VUELO (fixes de referee,
> Lemma 5.2, re-auditoría de doña Rosa, rigidez `p≠centroide`, patrones mixtos). Esta ronda
> pre-asigna las adiciones de valor al paper decididas con dirección el 2026-07-02.
> **Secuencia:** R7-1 es independiente y puede empezar YA en paralelo a R6; R7-2 a R7-5 se
> ejecutan al cerrar R6. Ejecuta el investigador; audita el jefe de research.
>
> Reglas vigentes: aritmética exacta (nunca grilla como prueba); etiquetas
> `[PROVED]/[EVIDENCE]/[OPEN]` por párrafo; scripts load-bearing a `experiments/`;
> todo lo que entre al `.tex` cumple la política "probado o citado".

---

## R7-1 (EMPEZAR YA — barato, binario) — Esqueleto ponderado en `d≥3`
**Pregunta:** ¿el mecanismo de masas desiguales del Thm 6.3 (perímetro ponderado) se extiende
a `Δ^d`, `d≥3`? `notes/47` solo descartó el perímetro **uniforme** (dev 3.16); el caso
ponderado está sin testear.

**Tarea (álgebra lineal exacta, una tarde):**
1. Para las medianas cíclicas de `Δ³` (valores `{0,½,1}` y resto `½`, `notes/47`): plantear
   el sistema exacto en los 6 pesos de arista `w_e≥0` — el pushforward de "uniforme en arista
   `jk` con masa `w_e`" por `u_i` es uniforme en `[V_ij,V_ik]` con densidad `w_e/|V_ik−V_ij|`
   (o átomo si `V_ij=V_ik`: ¡vigilar las aristas donde `u_i` es constante — en `d≥3` las hay,
   y un átomo mata la uniformidad salvo masa 0!). Exigir densidad total `≡1` en `[0,1]` para
   las 4 direcciones. Resolver exacto (`fractions`/`sympy`), explotando la simetría cíclica.
2. Si es incompatible: documentar el certificado de incompatibilidad (combinación lineal) —
   se convierte en teorema negativo: "el esqueleto-1 no basta en `d≥3`" (hoy solo hay
   observación para el caso uniforme). Probar entonces con soporte ampliado: aristas +
   2-caras (densidades lineales a trozos — el sistema deja de ser trivial pero sigue LP).
3. Si es compatible: **teorema "familia en toda dimensión"** — redactar el análogo exacto del
   Thm 6.3 para `Δ^d` (empezar por el caso mediana-cíclica, luego `p≠centroide`).

**Entregable:** veredicto binario con certificado exacto en ambos casos. **Riesgo:** medio.
**Valor:** si sale positivo, es el mayor salto de alcance disponible (el paper pasa de
`d=2` a toda dimensión); si sale negativo, teorema negativo limpio que blinda el "special
to `d=2`".

## R7-2 (núcleo de la ronda) — El defecto de transporte `D(u)`
Nueva sección del paper que unifica el método y cuantifica la Prop 6.1. Cuatro sub-tareas:

1. **[definición + cota, ~probado]** Definir
   `D(u) = inf_μ max_i ess-sup dens(u_{i#}μ)` para una terna de direcciones normalizadas.
   Probar: (a) el ínfimo se alcanza (compacidad débil-*: `{μ : u_{i#}μ ≤ D·Leb}` es
   débil-* cerrado); (b) **`Σrw ≥ 1/D(u)`** para toda cobertura por planks en esas
   direcciones (`μ(P_i) ≤ D·r_i` + unión). Observar `D=1 ⟺` existe medida de marginal
   uniforme (enlaza con Prop 6.1/Thm 6.3) y `D ≤ 2` siempre (medida uniforme, Thm 2.1).
2. **[cota de primeros momentos — el teorema cuantitativo]** La media de `u_{i#}μ` es
   `u_i(p)`, `p` = baricentro de `μ` — un solo punto controla las TRES medias. Densidad
   `≤D` con masa 1 en `[0,1]` fuerza media `∈[1/(2D), 1−1/(2D)]` (extremal: bloque
   `D·1_{[0,1/D]}`). Luego:
   `D(u) ≥ 1/(2·min_{p∈Δ} max_i dist_{[0,1]}-holgura de u_i(p))` — formular limpio: el
   mínimo sobre `p∈Δ` de `max_i |u_i(p)−½|` mide el **defecto de concurrencia** `δ(u)`, y
   `D(u) ≥ 1/(1−2δ(u))` (verificar constantes con cuidado). Casos: `δ=0 ⟺` concurrencia
   `⟹` cota trivial `D≥1`; **facetas:** `Σλ_i≡1 ⟹` alguna media `≤1/3 ⟹ D≥3/2` (dos
   líneas, ya derivado en dirección). Esto convierte la condición necesaria (binaria) en
   desigualdad cuantitativa — es el resultado nuevo central de la sección.
3. **[caso facetas exacto]** ¿`D(facetas)=3/2`? La igualdad requiere `μ` con las tres
   marginales `= (3/2)·1_{[0,2/3]}` (medias `1/3`, suma 1 ✓), soportada en
   `{max_i λ_i ≤ 2/3}` (triángulo interior no vacío ✓). Construir explícita (ansatz:
   simetría S₃, esqueleto ponderado del triángulo interior) o LP exacto. Si se alcanza:
   "el defecto de transporte de las facetas es exactamente 3/2" — pareja elegante del
   Thm 3.2 (allí la teselación da 1, el transporte solo 2/3: los dos métodos son
   genuinamente complementarios, y eso el paper hoy solo lo insinúa en un Remark).
4. **[paisaje, EVIDENCE]** Mapa numérico de `D(u)` sobre el espacio de ternas (LP por
   terna, exacto en puntos seleccionados): ¿dónde está el `sup`? ¿`D` es continua y `=1`
   exactamente en la rebanada concurrente? **Advertencia de dirección (honesta):** cerca de
   facetas inclinadas se espera `D≈3/2` sin fallback de teselación ⟹ esta vía
   probablemente NO bate B-Y (`1/D ≈ 2/3 < 0.928`). Se presenta como caracterización del
   alcance del método, NO como mejora de cota. Prohibido venderla de otra forma.

**Entregable:** sección "The transport defect" con 1–2 proposiciones probadas + paisaje
etiquetado `[EVIDENCE]`. **Riesgo:** bajo en 1–2, medio en 3, nulo en 4.

## R7-3 (condicional a R6-5) — Titular "Gardner para 3 direcciones en el triángulo"
Si R6-5 decide los patrones mixtos, reenmarcar la suma Prop 6.1 + Thm 6.3 + corolario iff +
mixtos como: **"resolvemos la pregunta de existencia de Gardner (1988) para tres direcciones
en el triángulo"** (afirmativa exactamente en la rebanada concurrente admisible; negativa
fuera). Tocar abstract, intro y título de sección. Cero matemática nueva; alto valor de
citabilidad. **No ejecutar si R6-5 queda parcial** — un titular con hueco es un regalo para
el referee.

## R7-4 — Estabilidad cuantitativa de la rigidez de medianas
Versión `ε` del centerpiece: si una cobertura por medianas tiene `Σr = 1+ε`, entonces está a
distancia `O(ε)` (Hausdorff sobre los `I_i`) de `[⅓,⅔]³`. El sistema de edge-tilings es
poliedral/lineal ⟹ la cota debe salir de dualidad LP / análisis de vértices del poliedro de
casi-igualdad, con **constante explícita**. Ruta: perturbar la enumeración del Lemma 5.2
(las 3 soluciones son vértices aislados ⟹ hay margen lineal). **Entregable:** proposición de
estabilidad con constante, o contraejemplo (una familia casi-tight lejos de tercios — lo que
también sería publicable). **Riesgo:** medio. **Valor:** conecta con la literatura de
estabilidad y hace el teorema principal más citable.

## R7-5 (cola de cierre) — Figuras + mapa de estatus del espacio de direcciones
1. Figura 1: triángulo medial con `p`, las tres direcciones cíclicas y las masas `1−2p_j`.
2. Figura 2: la teselación de tercios centrales (igualdad de medianas).
3. Figura 3 (si R7-2.4 sale): mapa del espacio de ternas coloreado por estatus — probado
   por transporte (`D=1`) / probado por teselación (facetas) / cota `1/D` / abierto.
TikZ en el `.tex`, nada de bitmaps. **Riesgo:** nulo. **Valor:** legibilidad de referee.

---

## Prioridad
1. **R7-1** — ya (independiente de R6; binario y barato).
2. **R7-2** — al cerrar R6 (núcleo: 1–2 primero, que están casi probados; 3 después; 4 es
   exploración etiquetada).
3. **R7-3** — solo si R6-5 cierra completo.
4. **R7-4 → R7-5** — cola de la ronda.

**Qué NO hacer (vigente de `auditorias/50`):** nada especulativo; nada de la línea EJ
(`notes/49-R5-4` es su registro y ahí se queda); ningún enunciado en el `.tex` que no esté
probado o citado; ningún claim de "mejora de cota" salvo desigualdad demostrada.
