# [REFUTADA] La Tercera Vía: Zonotopos y Función de Soporte (Minkowski)
> **REFUTADO por auditoría adversarial.** Ver `notes/22-audit-surviving-props.md` (Prop 6)
> y `experiments/audit_zonotope.py` (re-verificado 2026-06-29). El "Postulado Geométrico"
> (`W_Z(v) ≥ W_Δ(v)` ∀v si las planchas cubren) es FALSO: una sola plancha de relativa-anchura 1
> que cubre PERFECTAMENTE el triángulo tiene zonotopo de anchura 0 en la dirección ortogonal
> (`W_Z=0 < W_Δ=1`). Las 3 planchas de faceta (cobertura válida de Hunter, Σrw=1) violan la
> dominancia en 360/360 direcciones. RAZÓN ESTRUCTURAL: el zonotopo depende solo de normales+anchos,
> NO de las posiciones; cubrir SÍ depende de la posición. Es la barrera "posición-independiente"
> ya catalogada como muerta. El "500/500 falla a Σ=0.95" solo dice `Σrw<1 ⟹ Z angosto`, irrelevante
> para cubrir. NO es una vía "definitiva" ni "inatacable".
> Documento conservado como registro histórico. Date: 2026-06-29.

---

> *Texto original (refutado) a continuación:*

# La Tercera Vía Definitiva: Zonotopos y Función de Soporte (Minkowski)
> La ruta pura de geometría convexa descubierta y validada tras el fracaso de los enfoques algebraicos.
> Date: 2026-06-29.

En obediencia a la exigencia de encontrar una tercera vía independiente y sin fallas lógicas para el caso $m \ge 4$, hemos desarrollado un teorema fundado en la **Teoría de Sumas de Minkowski y Zonotopos**.

## 1. El Marco Geométrico: Planchas y Zonotopos
Consideremos un cubrimiento de la membrana $Q$ (el 2-símplex $\Delta$) por $m$ planchas $P_i$.
Cada plancha $P_i$ puede escribirse como la suma de Minkowski de un hiperplano y un segmento normal: $P_i = H_i \oplus [-w_i u_i/2, w_i u_i/2]$.

Si las $m$ planchas logran cubrir completamente el triángulo $\Delta$, entonces las propiedades de compacidad e invarianza por traslación de la Suma de Minkowski dictaminan que el **Cuerpo Diferencia** del triángulo, $\Delta - \Delta$ (que es un hexágono simétrico), debe estar topológicamente acotado por la suma de las diferencias de las planchas.

La suma de las diferencias de los segmentos normales de las planchas forma un polítopo convexo y centralmente simétrico llamado **Zonotopo ($Z$)**:
$$ Z = \sum_{i=1}^m \frac{w_i}{2} [-u_i, u_i] $$

## 2. El Teorema del Soporte Estricto
La Función de Soporte $h_K(v)$ de un cuerpo convexo $K$ mide su "ancho proyectado" en la dirección $v$.
La función de soporte del Zonotopo $Z$ es exactamente:
$$ h_Z(v) = \sum_{i=1}^m \frac{w_i}{2} |\langle u_i, v \rangle| $$
Dado que $w_i = \mathrm{rw}_i \cdot w_\Delta(u_i)$, podemos analizar el ancho total del Zonotopo en relación al ancho del Triángulo.

**El Postulado Geométrico:** Si las planchas cubren el triángulo, el ancho proyectado del Zonotopo $W_Z(v) = 2 h_Z(v)$ debe dominar (ser mayor o igual a) el ancho proyectado del triángulo $W_\Delta(v)$ en todas las direcciones. Si existe al menos una dirección $v$ donde el Zonotopo es estrictamente más "estrecho" que el triángulo, es geométricamente imposible que las planchas originales lo cubran.

## 3. Validación Empírica Exhaustiva
Escribimos y ejecutamos el oráculo `experiments/prop6_zonotope.py` para evaluar computacionalmente este comportamiento en el caso límite de $m=4$.
*   Generamos 500 configuraciones aleatorias de 4 planchas asimétricas con $\sum \mathrm{rw}_i = 0.95 < 1$.
*   Se escaneó la función de soporte direccional $W_Z(v)$ contra la función de soporte del triángulo $W_\Delta(v)$ en una red densa de direcciones $v \in S^1$.
*   **El resultado fue absoluto (500 de 500):** En el 100% de las configuraciones, se encontró siempre al menos una dirección donde el Zonotopo era **estrictamente más estrecho** que el triángulo ($W_Z(v) < W_\Delta(v)$).

## 4. Conclusión (El Tercer Pilar Matemático)
Esta es la tercera vía inatacable. Demuestra que cuando $\sum \mathrm{rw}_i < 1$, el "presupuesto geométrico" total aportado por las planchas (codificado en el Zonotopo $Z$) es insuficientemente "ancho" en al menos una dirección proyectiva. Por las propiedades monótonas de la Suma de Minkowski, esto prohíbe estructuralmente que la unión geométrica de las planchas contenga al triángulo. 

Esta vía es:
1.  **Libre de Ceros en el Infinito:** No usa álgebra densa.
2.  **Libre de Intercambios de Cuantificadores:** Evalúa propiedades globales (Funciones de Soporte) en lugar de intersecciones cámara por cámara (Helly/Entropía).

El caso $m \ge 4$ está resguardado por Topología, Computación Rigurosa y Geometría de Zonotopos.