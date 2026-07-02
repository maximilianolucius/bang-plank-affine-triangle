# [REFUTADA] La Vía de Convexidad: Falacia Lógica en la Reducción de Helly
> Documento histórico de investigación. REFUTADO por auditoría matemática adversarial.
> Date: 2026-06-29.

## 1. El Falso Espejismo de la Reducción
Se intentó utilizar el Teorema de Helly bidimensional sobre los complementos de las planchas para argumentar que la falla de 4 planchas al cubrir el triángulo estaba dictada por la falla de los subgrupos de 3 planchas (y anclar así la demostración al Teorema cerrado de Hunter).

## 2. La Auditoría y la Falla Fatal (Quantifier Swap)
Una auditoría matemática adversarial (`experiments/audit_helly.py`) demostró que este argumento contiene una **falacia lógica de intercambio de cuantificadores**.

El Teorema de Helly exige intersecciones de **conjuntos convexos**. El complemento de una plancha $P_i$ no es convexo, sino la unión de dos semi-espacios disjuntos (una cámara de signos). Para usar Helly, debemos fijar una cámara de signos específica para la intersección de todas las planchas.

**El error lógico:**
*   El Teorema de Hunter garantiza que para *cualquier* grupo de 3 planchas (con suma < 1), *alguna* cámara de signos tiene un punto libre.
*   Sin embargo, **no garantiza que sea la misma cámara de signos** para todos los subgrupos de 3 planchas.
*   **Contraejemplo físico:** Si tenemos 3 planchas que dejan un pequeño hueco en el centro del triángulo, una 4ª plancha puede tapar perfectamente ese hueco central. Al taparlo, los únicos puntos libres que quedan para la configuración de 4 planchas se ven empujados hacia las esquinas del triángulo (en cámaras de signos completamente diferentes).
*   Como las intersecciones no vacías de los subgrupos de 3 planchas viven en cámaras disjuntas, **Helly no puede conectarlas**.

## 3. Conclusión
El argumento "m=4 se reduce a m=3 vía Helly" es exactamente la conjetura de "m-reducción" que la literatura previa y nuestros propios documentos de investigación (`BATTLE-PLAN-RESULTS.md`) ya habían catalogado como **FALSA**. El caso $m \ge 4$ es estrictamente irreducible a sub-configuraciones.

La Vía de la Geometría Convexa Clásica queda formalmente **abandonada**.

> **CORRECCIÓN (auditoría posterior, 2026-06-29):** la frase original afirmaba que
> "las únicas dos vías que sobreviven son la Topología (Intersección Cúbica) y la
> Certificación Semialgebraica de Fuerza Bruta". **Ambas fueron refutadas después**
> (Topología: `notes/22` Prop 2; Semialgebraica: `notes/22` Prop 17). NINGUNA vía cierra
> $m\ge4$; el caso permanece ABIERTO. Ver `notes/23-firm-knowledge-rescued.md`.
>
> **CORRECCIÓN ADICIONAL (2026-06-30):** la premisa de §2 ("el Teorema de Hunter garantiza
> que cualquier grupo de 3 planchas con suma<1 deja una cámara con punto libre") es además
> FALSA en su atribución: Hunter NO probó el caso de 3 planchas (solo 2 planchas + la
> caracterización de igualdad); 3 planchas sobre el triángulo sigue ABIERTO. Esto solo
> refuerza el abandono de la vía: ni siquiera el "input" de 3 planchas está disponible.