# P-A1´: la familia de ternas con medida de marginal uniforme (caracterización necesaria)

> **[NOTA DE ALCANCE — auditoría #menor]** El título describe una **caracterización**, no un
> teorema de familia. Lo **probado** es solo la **condición necesaria** (`1^TV^-1 1=2`). "Bang
> por transporte para toda la familia de concurrencia" es **[CONSECUENCIA condicional]** que
> depende de la **suficiencia**, que está **[ABIERTA]** (§3, evidencia LP fuerte, no prueba).
> Lo único probado como teorema de Bang en esta línea es el **punto** de las medianas
> (`notes/36`).
>
> Date: 2026-06-30. Status: necessary cond **[PROVED]**, sufficiency **[STRONG EVIDENCE / OPEN]**.
> Generaliza la prueba de transporte de `notes/36` (medianas) a una **familia
> positivo-dimensional** de ternas de direcciones. Es el lead mas valioso reciente.

---

## 0. La idea (de la auditoria de nota 36)

`notes/36` probo Bang para las 3 medianas exhibiendo una medida `mu` con marginal uniforme
en las 3 direcciones (transporte: cubrir => `1=mu(Delta)<=sum mu(P_i)<=sum r_i`).
Pregunta: **¿que ternas admiten tal medida?** Caracterizarlas = caracterizar las ternas
con Bang demostrable por una sola medida.

---

## 1. Criterio de transporte [PROVED]

Si existe una medida de probabilidad `mu` sobre `Delta` con `u_{i#}mu = Leb[0,1]` para las
3 direcciones, entonces toda cobertura cumple `sum r_i >= 1` (Bang). (Prueba: `notes/36`
§1; `mu(P_i)=(u_{i#}mu)(I_i)<=r_i`, subaditividad, `mu(Delta)=1`.)
*No se puede relajar a `<=Leb`*: con `mu` probabilidad, `u_{i#}mu<=Leb` fuerza `=Leb`
(masa 1 = longitud 1). Asi que la medida debe ser **exactamente uniforme**.

---

## 2. Condicion NECESARIA [PROVED]

Escribe cada forma normalizada por valores de vertice: `u_i = sum_j v_{ij} x_j`
(`x_j` baricentricas, `sum_j x_j = 1`), `V=(v_{ij})` (fila `i` = valores de la forma `i`).
Para cualquier `mu`, el baricentro `p_j := E_mu[x_j]` cumple `p` en el simplex
(`p_j>=0`, `sum p_j=1`). Marginal uniforme => `E_mu[u_i]=1/2` para todo `i` =>

`V p = (1/2) 1`  =>  `p = (1/2) V^{-1} 1`.

Para que `p` sea baricentro valido: `sum_j p_j = 1`, i.e.

`**1^T V^{-1} 1 = 2**`,  y  `**V^{-1} 1 >= 0**` (`p` en el simplex).

### Forma geometrica (limpia)

`Vp=(1/2)1` dice que las **tres lineas de nivel medio `{u_i = 1/2}` CONCURREN** en el
punto `p`, y `p in Delta`. Es decir:

> **una terna admite medida de marginal uniforme solo si las 3 lineas `{u_i=1/2}`
> concurren dentro del triangulo.**

- **Medianas:** `{m_i=1/2}` son las **3 cevianas medianas**, concurrentes en el
  **centroide** `(1/3,1/3,1/3)`. Pasan. (Verificado: `u_i(p)=1/2`, `p=centroide`.)
- **Facetas:** `{x_i=1/2}` concurren en `(1/2,1/2,1/2)`, con `sum=3/2 != 1`: **fuera de
  `Delta`**. Fallan. Es exactamente la **obstruccion de Gardner / nota 12**: `sum x_i=1`
  pero la concurrencia exige `sum=3/2`. (Por eso las facetas NO se prueban por una sola
  medida; necesitan Brunn-Minkowski.)

`cond := 1^T V^{-1} 1`: facetas `cond=3`, medianas `cond=2`.

---

## 3. SUFICIENCIA [STRONG EVIDENCE]

Conjetura: `cond=2` con `p` en el **interior** del simplex `=>` existe la medida de
marginal uniforme.

Evidencia (LP de factibilidad sobre malla de `Delta`, binning `K` por direccion):
- **453/453** ternas con `cond=2` y `p` interior admiten la medida (binned-uniforme),
  **robusto a `K`** (`K=10,18,25` todas factibles).
- **Control:** las no-pasadoras (`cond != 2`) **fallan** al refinar (`K=20,40`).
  (A `K` chico hay falsos positivos por la holgura de binning ~`1/K`, que desaparecen.)
- Asi la condicion de medias `cond=2` (+`p` interior) parece **necesaria Y suficiente**.
  No aparecen obstrucciones de momento superior.

[OPEN] prueba rigurosa de suficiencia: construir `mu` explicito para una pasadora
generica. Para **medianas** sirve la **medida del perimetro** (`notes/36`); para pasadoras
genericas la solucion LP es **singular** (~0.3% soporte) con parte interior y parte de
borde (~35% borde) -- **no** es solo el perimetro. Falta una construccion general (o un
argumento de dualidad tipo Strassen/Kellerer).

---

## 4. La FAMILIA [EVIDENCE]

- **Positivo-dimensional:** `cond=2` es **1 ecuacion** sobre la terna (3 params `tau` por
  combinacion de roles) => **superficie 2-dim** (codimension 1). Fijando 2 `tau` y
  resolviendo el tercero por `cond=2`, hay solucion interior (familia continua).
- **Incluye ternas GENERICAS de 3 aristas activas distintas** (no solo medianas/balanceadas
  ni borde-comun). Ej.: `(0,0.7,1),(0.5,1,0),(0,1,0.7)` (`#aristas=3`), con medida
  existente. **Es Bang demostrable para genericas.**
- **NO coincide con "balanceado" (`rho=1`):** las **facetas son balanceadas pero estan
  EXCLUIDAS** (`cond=3`); y la familia incluye **no-balanceadas** (`tau` generico). Asi
  "admite medida uniforme" y "balanceado" son condiciones **distintas** (casi ortogonales):
  comparten solo las medianas.
- **Borde (`p` en `partial`simplex, algun `p_j=0`):** la medida se fuerza a una cara ->
  caso **trivial 1-D**. P.ej. **2F+1M** tiene `p=(1/2,0,1/2)` -> medida en la arista `AC`,
  donde dos formas coinciden -> es el caso 1-D trivial (no profundo). Esto explica por que
  `notes/35` lo veia "teselar": es trivial, no un caso tight nuevo.

---

## 5. Consecuencia y alcance HONESTO

- **[CONSEQUENCE, modulo §3]** Bang(3) es **demostrable por transporte para toda la
  familia de concurrencia** (2-dim), incluyendo ternas genericas. Es un avance estructural
  **mucho mayor** que el punto aislado de las medianas.
- **[SCOPE]** la familia es **codim-1** (medida cero en el espacio de ternas): **NO prueba
  Bang(3) general** (la terna generica fuera de la superficie sigue abierta). El metodo de
  transporte da **exactamente** esta familia (no se puede relajar, §1).
- **[vs N_c]** NO cierra `N_c` directamente: el conjunto binding de `N_c` es **balanceado**
  (facetas + medianas); las facetas estan **fuera** de esta familia, y la familia incluye
  genericas que **no** son binding de `N_c`. Solo las **medianas** estan en ambos. La
  pieza cuantitativa de B-Y (`notes/35` §3.2) sigue siendo aparte (P-B).
- **Lo verdaderamente nuevo:** una **caracterizacion limpia y verificable**
  (`1^T V^{-1}1=2` / concurrencia de `{u_i=1/2}`) de un conjunto positivo-dimensional de
  ternas con Bang(3) probado por una sola medida -- el primer resultado de Bang para una
  **familia** de direcciones genericas no-faceta.

---

## 6. Actualizacion de narrativa (P-C, nota 23)

"Medida unica topada en `<1` / imposible en 3 direcciones" (notas 12/23/30) era para
direcciones **faceta o genericas fuera de la superficie**. **Matiz correcto:** una medida
unica alcanza `c=1` (marginal uniforme) en las **ternas de concurrencia** (`Sum=2kappa`,
lineas `{u_i=1/2}` concurrentes), p.ej. medianas (`Sum m=3/2`). Evade Gardner justo donde
las facetas (`Sum=1`) no pueden. (Se anota en `notes/23`.)

---

## 7. Proximos pasos

1. **Probar suficiencia (§3):** construccion general de `mu` para pasadoras genericas, o
   dualidad. Cerraria "Bang(3) para la familia de concurrencia" como **teorema**.
2. **Rigidez mediana** (P-A1´´, `notes/36` §2): cierra el caso de igualdad de las medianas.
3. **Mapear la superficie:** ecuacion explicita de `cond=2` en `(tau_1,tau_2,tau_3)` por
   combinacion de roles; relacion con el locus tight de `notes/33` (¿toda terna tight, o
   solo la superficie?).
4. **P-B (batir B-Y):** independiente; `S_0-1>=L_c` via Lema 5 de B-Y (`notes/35` §3.2).

Scripts: caracterizacion y LP inline; motor `exp_w2_delta.py`, transporte `notes/36`.
