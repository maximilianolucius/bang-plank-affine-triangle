# [REFUTADA] El Lema Topológico de Intersección Cúbica (Modelo Vectorial)
> **REFUTADO por auditoría adversarial.** Ver `notes/22-audit-surviving-props.md` (Prop 2).
> El "lema" central ("Σ|Iⱼ|<1 ⟹ nervio no contráctil") (a) es circular —el vínculo
> ancho↔topología ES la conjetura, se afirma sin prueba— y (b) es falso como detector:
> las fallas de cobertura viven en el BORDE de Q, donde ∪Aⱼ sigue siendo contráctil (β₁=0),
> así que el nervio no da señal. El experimento `prop2_kkm.py` solo CONFIRMA numéricamente
> que la conjetura es cierta (ya sabido vía ILP exacto); confirmar ≠ demostrar.
> Documento conservado como registro histórico de investigación.
> Date: 2026-06-29.

## 1. El Modelo Vectorial (Contexto)
Por invariancia afín, cualquier triángulo cubierto por $m$ planchas puede representarse como el 2-símplex estándar $\Delta = \{x \in \mathbb{R}^3 : x_i \ge 0, \sum x_i = 1\}$ cubierto por $m$ franjas (planchas). 

Si evaluamos las $m$ formas lineales que definen las planchas, obtenemos un mapeo afín:
$$ \Phi : \Delta \hookrightarrow [0,1]^m $$
La imagen de $\Delta$ bajo $\Phi$ es una membrana triangular plana 2D, que llamaremos **$Q = \operatorname{conv}(q_1, q_2, q_3)$**, sumergida en el hipercubo unitario $m$-dimensional.
Cada plancha original se convierte en este modelo simplemente en una **restricción coordinada**: $y_j \in I_j$, donde $I_j \subseteq [0,1]$ es un intervalo de longitud $|I_j| = \mathrm{rw}_j$.

**La Conjetura en Modelo Cúbico:** 
Si la membrana $Q$ está completamente contenida en la unión de los "cilindros coordinados" $C_j = \{y \in [0,1]^m : y_j \in I_j\}$, entonces la suma de las longitudes de los intervalos $\sum_{j=1}^m |I_j| \ge 1$.

## 2. El Lema Topológico (El "Nerve" de la Cobertura)
La geometría lineal falla en dimensiones altas porque la membrana $Q$ (2D) pierde "volumen" al ser embebida en $4D, 5D$, etc. Sin embargo, la topología persiste.

Definamos los subconjuntos $A_j = Q \cap C_j$. Son conjuntos convexos cerrados.
Si las planchas cubren $Q$, entonces $\bigcup_{j=1}^m A_j = Q$.
Como $Q$ es un triángulo sólido, $Q$ es topológicamente **contráctil** (homotópicamente equivalente a un punto).

Por el **Teorema del Nervio (Nerve Theorem)** de Borsuk/Leray, dado que los $A_j$ son convexos, el complejo simplicial abstracto formado por sus intersecciones (el *Nerve* $\mathcal{N}$) es homotópicamente equivalente a su unión $\bigcup A_j$.

**El Lema:**
> Si $\sum_{j=1}^m |I_j| < 1$, entonces el complejo del nervio $\mathcal{N}$ **no es contráctil**. En particular, la unión de las planchas no puede ser contráctil y, por lo tanto, no puede ser igual a $Q$ (siempre queda un hueco).

Matemáticamente, si $\mathcal{N}$ tuviera la topología de un espacio con huecos (por ejemplo, el primer número de Betti $\beta_1 > 0$), sabemos categóricamente que existe un punto en $Q$ que no pertenece a ningún $A_j$. El testigo del hueco existe.

## 3. Implicación de este Lema
Este lema cambia las reglas del juego:
1. **Evade la Pared de Gardner (No-simetría):** No necesitamos una medida dual "mágica" con marginales planas perfectas (lo cual es imposible). 
2. **Transforma el problema:** En lugar de optimización fraccionaria (que nos arrastra al dual circular o topado en 0.828), tenemos que probar un teorema puramente de **intersección combinatoria (tipo KKM)** sobre el esqueleto simplicial de $m$ intervalos.

## 4. Reproducibilidad Computacional
Para observar empíricamente este colapso topológico, implementamos un oráculo en Rust (ver `experiments/prop2_rust/src/main.rs`).

**Procedimiento de simulación:**
1. Generar la membrana $Q$ en $\mathbb{R}^m$ asegurando que el rango de cada coordenada $j$ en los vértices $q_k$ sea exactamente $[0, 1]$.
2. Muestrear una cuadrícula densa sobre $Q$.
3. Generar $m$ intervalos aleatorios $I_j$ tales que $\sum |I_j| < 1$.
4. Construir explícitamente el complejo de intersección $\mathcal{N}$ verificando qué combinaciones de cilindros $C_j$ se superponen en al menos un punto muestreado de $Q$.
5. Calcular los números de Betti (homología sobre $GF(2)$) del complejo $\mathcal{N}$.

Si $\sum |I_j| < 1$, observaremos que $\beta_0 > 1$ (desconectado) o $\beta_1 > 0$ (tiene un hueco tipo anillo), lo cual delata *inmediatamente* que el cubrimiento ha fallado. No puede ser $\beta_0=1, \beta_1=0$.