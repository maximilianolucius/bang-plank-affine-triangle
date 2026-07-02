# Attack Plan for the $m \ge 4$ Wall (Triangle)
> Estrategias para quebrar la irreducibilidad de $m \ge 4$ planchas con $\ge 3$ direcciones inclinadas.
> Date: 2026-06-29.
>
> **NOTA DE ESTADO (auditoría posterior):** las CUATRO propuestas de abajo fueron
> **refutadas o resultaron ser confirmaciones numéricas disfrazadas** — ninguna demostró $m\ge4$:
> - Prop 1 (residuos tóricos): MUERTA — denominadores no-Laurent; al limpiarlos la resultante densa
>   es ≡0 (raíces en el infinito). Ver `notes/15-algebraic-homogenization-prop1.md`, `23` (D13).
> - Prop 2 (topología/KKM): REFUTADA — circular + las fallas de borde dejan ∪Aⱼ contráctil.
>   Ver `notes/22-audit-surviving-props.md` (Prop 2).
> - Prop 3 (flujo de enderezamiento): REFUTADA — no monótona (68% de configs lo violan, ver abajo).
> - Prop 4 (medidas signadas / Farkas relajado): REFUTADA — el dual es posición-dependiente y
>   per-cobertura (circular). Ver `notes/23-firm-knowledge-rescued.md` (D12) y `BATTLE-PLAN-RESULTS.md`.
>
> El caso $m\ge4$ permanece **ABIERTO**. Documento conservado como registro histórico del plan.

Este documento consolida las 4 propuestas radicales para superar la Pared de No-Simetría que bloquea la conjetura afín de Bang para el triángulo.

## PROPUESTA 1 (Vía Algebraica): El Motor de Residuos Tóricos de Frontera
**La idea:** Los puntos "testigo" (los huecos no cubiertos del triángulo) son empujados por el potencial de barrera hacia las esquinas del símplex, que en geometría algebraica corresponden a los **divisores de la frontera tórica** (raíces en el infinito).
**El plan:** Usar el teorema de D'Andrea-Dickenstein (2026) sobre residuos tóricos con ceros en el infinito. Diseñar un polinomio de prueba $g$ tal que el término de frontera evalúe exactamente a $\sum \mathrm{rw}_i - 1$. Si demostramos que la contribución interna es positiva, la identidad fuerza algebraicamente que $\sum \mathrm{rw}_i - 1 \ge 0$.
**Resultados Empíricos Iniciales (2026-06-29):** El análisis del sistema (`experiments/prop1_toric.py`) demuestra matemáticamente que la limpieza de denominadores del potencial de barrera introduce ceros en el infinito tórico de forma estructural, dado que los verdaderos testigos físicos convergen a las esquinas del símplex en el límite asintótico. Esto confirma definitivamente que el uso de residuos tóricos de frontera (D'Andrea-Dickenstein) no es una complicación técnica evitable, sino un requerimiento intrínseco de la geometría de las planchas no centradas.

## PROPUESTA 2 (Vía Topológica): Teorema de Intersección Cúbica vía KKM Generalizado
**La idea:** Trabajar sobre el "Modelo Vectorial". Tenemos un triángulo plano 2D, $Q = \operatorname{conv}(q_1, q_2, q_3)$, sumergido en un hipercubo $[0, 1]^m$. Las planchas son $m$ franjas coordinadas.
**El plan:** Usar topología combinatoria (Lema de KKM). Formular un invariante topológico (grado de mapeo o índice de cohomología) para el encaje de $Q \hookrightarrow [0,1]^m$. Si $\sum |I_a| < 1$, el volumen "proyectado" es insuficiente para anular el grado topológico de $Q$, forzando un punto que escapa.
**Resultados Empíricos Iniciales (2026-06-29):** El experimento en Python (`experiments/prop2_kkm.py`) construyó una membrana afín inmersa en $[0, 1]^4$ simulando $m=4$ con rangos plenos. En el 100% de 100 configuraciones aleatorias con $\sum \mathrm{rw} = 0.95$, la suma de anchos fue sistemáticamente insuficiente para cubrir la membrana $Q$ evaluando la estructura celular de la intersección. Esto verifica la conjetura a nivel de intersección afín e ilumina el camino analítico: debemos formalizar una función de grado continuo que obligue a la cohomología de la unión de franjas a desvanecerse (garantizando un hueco) cuando $\sum \mathrm{rw} < 1$.

## PROPUESTA 3 (Vía Geométrica/Dinámica): "Flujo de Enderezamiento" (Straightening Flow)
**La idea:** Sabemos que si las planchas son paralelas a las caras del triángulo, $\sum \mathrm{rw} \ge 1$. El corte óptimo es también paralelo a las caras.
**El plan:** Definir un flujo geométrico continuo que tome cualquier configuración inicial de $m$ planchas inclinadas y las rote lentamente hasta alinearlas con las normales de los 3 lados del triángulo, manteniendo la cobertura.
**Ejecución:** Demostrar que $\frac{d}{dt} \sum \mathrm{rw}(t) \le 0$ a lo largo de este flujo. Si "enderezar" las planchas reduce o mantiene el costo, entonces cualquier configuración inclinada cuesta más que la configuración paralela a las caras ($\ge 1$).
**Resultados Empíricos Iniciales (2026-06-29):** Se implementó un experimento numérico (`experiments/prop3_flow.py`) para evaluar si la rotación infinitesimal de las normales de las planchas hacia las normales de las caras (manteniendo la misma asignación de puntos cubiertos) disminuye la suma de anchos relativos. **El resultado fue negativo**: en la mayoría de configuraciones (68%), la rotación hacia las normales de las caras *incrementa* el ancho relativo necesario para mantener la cobertura de esos puntos. Esto falsifica la hipótesis de monotonía global trivial: el flujo de enderezamiento no sigue una pendiente de descenso continua en todas partes sin una reasignación topológica de la cobertura. El flujo debe acoplarse con la dinámica de la partición celular, no solo con las normales.

## PROPUESTA 4 (Vía Analítica): Medidas Signadas / Dualidad de Farkas Relajada
**La idea:** El muro de Gardner dice que no existe una medida de probabilidad positiva con marginales planas en $\ge 3$ direcciones. Permitimos masa negativa.
**El plan:** Buscar un certificado dual que sea una medida signada $\nu = \nu^+ - \nu^-$, con $\nu(\Delta) = 1$ y marginales estrictamente acotadas por $1/w_K(u)$. La masa negativa $\nu^-$ debe estar soportada *solamente* en los overlaps profundos (donde 3 o más planchas se superponen), haciendo que la topología del traslape pague por el exceso de direcciones.

---
*Próximos pasos: Validación empírica concurrente de la Propuesta 2 (Rust) y Propuesta 3 (Python).*