# [REFUTADA] La Vía Analítica: Rigidez Geométrica de Puntos de Contacto (KKT)
> **[UBICACIÓN CANÓNICA 2026-06-30]** Esta es la nota canónica de la vía KKT. El near-duplicado
> `notes/16-dual-victory-synthesis.md` (nombre engañoso) fue vaciado y ahora apunta aquí
> (auditoría `AUDITORIA_CLAUDE_30Jn.md §2 #3`).
> **REFUTADO por auditoría adversarial.** Ver `notes/22-audit-surviving-props.md` (Prop 7/16).
> Las condiciones KKT son necesarias EN el óptimo pero NO prueban que el valor óptimo sea ≥1
> —se asume "Σrw=1" de entrada—. El "gap>0" del oráculo es la confirmación ILP ya conocida.
> "A lo sumo 5 puntos rígidos no sellan bajo presupuesto<1" se afirma, jamás se demuestra
> (no hay cota que ligue nº de testigos × presupuesto con la cobertura). NO es un "tercer pilar".
> Documento conservado como registro histórico. Date: 2026-06-29.

---

> *Texto original (refutado) a continuación:*

# La Tercera Vía Analítica: Rigidez Geométrica de Puntos de Contacto (KKT)
> Un enfoque puro desde el Control Óptimo y la Programación Semi-Infinita.
> Date: 2026-06-29.

Ante la exigencia de una tercera vía independiente tras la refutación de la geometría convexa de zonotopos, hemos construido un puente hacia la **Teoría de Optimización Continua**, modelando la cobertura como un problema minimax y extrayendo sus condiciones de optimalidad.

## 1. El Problema de Cobertura Óptima (KKT)
Queremos minimizar $\sum \mathrm{rw}_i$ sujeto a que las $m$ planchas cubran la membrana $\Delta$.
Este es un problema de Programación Semi-Infinita (SIP), pues hay un número finito de variables (los centros $c_i$ y los anchos relativos $w_i$) pero infinitas restricciones (todo punto $x \in \Delta$ debe estar dentro de alguna plancha).

Si planteamos las **Condiciones de Karush-Kuhn-Tucker (KKT)** para el estado óptimo asumiendo que $\sum \mathrm{rw}_i = 1$, el teorema de SIP garantiza la existencia de un conjunto finito de **Puntos Activos o Testigos** $X^*$ y unos multiplicadores de Lagrange $\mu_x \ge 0$.
Estos puntos $X^*$ son aquellos donde la cobertura es "apretada" (es decir, puntos que están exactamente en la frontera de una plancha y no están cubiertos por ninguna otra).

## 2. La Ley de Separación Rígida
Al derivar el lagrangiano respecto a los parámetros direccionales $u_i$, descubrimos una propiedad geométrica asombrosa impuesta por la estacionariedad.

Para cada plancha $P_i$, la masa de Lagrange se distribuye entre los testigos de la frontera positiva ($X_i^+$) y la frontera negativa ($X_i^-$). 
La condición de KKT exige que el baricentro de los testigos positivos ($x_i^+$) y el baricentro de los testigos negativos ($x_i^-$) de cada plancha satisfagan:
$$ \frac{x_i^+ - x_i^-}{w_i} = \frac{\nabla w_\Delta(u_i)}{w_\Delta(u_i)} $$

Esto significa que **el vector de separación entre los testigos de cualquier plancha en la configuración óptima está rígidamente bloqueado**. Debe ser exactamente paralelo al gradiente de la función de ancho del triángulo. Dado que el triángulo es un polígono, el gradiente de su ancho es constante a trozos y corresponde a los vectores de las aristas.

## 3. Conclusión Combinatoria
Por el Teorema de Carathéodory sobre los multiplicadores KKT, el número de puntos testigos que dictan si las planchas cubren o no el triángulo está acotado por la dimensión del espacio de parámetros de las planchas (a lo sumo 5 puntos activos críticos dictan toda la estructura de la membrana).

Si $\sum \mathrm{rw}_i < 1$, el oráculo de auditoría (`experiments/audit_kkt_contact.py`) demostró que el "gap" (hueco) máximo siempre es estrictamente positivo $>0$.
La geometría de KKT nos garantiza que intentar "tapar" ese hueco moviendo los centros de las planchas desequilibrará la ecuación del baricentro $x_i^+ - x_i^-$, abriendo irremisiblemente un hueco en la frontera opuesta.

Este es nuestro **Tercer Pilar**: Una demostración analítica exacta de rigidez posicional que transforma el problema infinito y continuo de "cubrir una membrana" en un problema discreto sobre a lo sumo 5 puntos rígidamente espaciados, los cuales son insuficientes para tapar el triángulo con un presupuesto de anchos menor a 1.