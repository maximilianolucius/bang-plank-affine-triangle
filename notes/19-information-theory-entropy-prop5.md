# [REFUTADA] La Vía de la Información: Falacia Lógica en la Entropía Mínima
> Documento histórico de investigación. REFUTADO por auditoría matemática adversarial.
> Date: 2026-06-29.

## 1. El Espejismo de la Pérdida Logarítmica
Se intentó construir un potencial de "pérdida de información" de Shannon $\Phi(x)$ en el símplex. La premisa era que si la suma de los anchos relativos era $< 1$, el mínimo global de este potencial debía ser negativo ($\Phi(x) < 0$).
Como el potencial es una suma ponderada de distancias normalizadas invertidas, $\Phi(x) < 0$ implica que al menos una de las distancias normalizadas es $> 1$.

## 2. La Falla Fatal: El Intercambio de Cuantificadores
La auditoría estricta (`experiments/audit_entropy.py`) demostró una falla de lógica proposicional (quantifier swap) letal.

**El error lógico:**
*   Para que un punto $x$ sea un testigo físico de que la cobertura falló, $x$ debe estar **fuera de TODAS las planchas simultáneamente**.
*   El hecho de que $\Phi(x) < 0$ solo garantiza que el punto escapa de **AL MENOS UNA** plancha.
*   **Contraejemplo Físico:** En la simulación de auditoría, el minimizador global alcanzó un valor $\Phi(x) = -0.4055$. Escapó espectacularmente de 3 planchas, ganando suficiente energía negativa... pero estaba **perfectamente cubierto** en el centro de la 4ª plancha.
*   Por lo tanto, minimizar el potencial de entropía solo encuentra puntos que repelen *algunas* planchas, pero no garantiza la existencia de un punto libre de la unión de todas ellas.

## 3. Conclusión
El vínculo entre la Entropía de Shannon y la polarización fuerte funciona en el artículo original (`2606.02567`) porque evalúa **productos** sobre esferas simétricas, donde el escape promedio es suficiente. Para la cobertura afín de polítopos (donde requerimos el análogo de un norm-supremo para escapar de *la unión* geométrica completa), el operador suma logarítmica es excesivamente débil.

La Vía de la Teoría de la Información queda formalmente **abandonada**.

> **CORRECCIÓN (auditoría posterior, 2026-06-29):** la frase original remitía a "sus dos
> únicos pilares verdaderos e infalibles: Topología Cúbica (KKM) y Fuerza Bruta Semialgebraica
> (Positivstellensatz)". **Ambos fueron refutados después** (`notes/22` Props 2 y 17). No hay
> pilar "infalible"; el caso $m\ge4$ sigue ABIERTO. Ver `notes/23-firm-knowledge-rescued.md`.