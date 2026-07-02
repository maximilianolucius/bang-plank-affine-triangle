# Ataque paralelo a `W_3` — sintesis auditada
> Date: 2026-06-29. Status: PARTIAL / OPEN.
> Se ejecutaron cinco rutas en paralelo. No se obtuvo prueba completa de `W_3` ni
> contraejemplo. Esta nota separa resultados probados, reducciones exactas, numerica
> no-probatoria y obstrucciones.
>
> **[CORRECCION CRITICA 2026-06-30 — auditoria]** Varios subcasos pelan a un subtriangulo
> cubierto por 3 planks y aplican "Hunter". Pero Hunter NO probo el caso de 3 planks en
> el triangulo (solo 2 planks + caracterizacion de igualdad; 3 planks sigue ABIERTO —
> Verreault, B-Y 2026). Estado por seccion:
> - **§2.1, §2.2 (rama "se usa 2.1")**: **INVALIDOS** (Hunter sobre "1-2 facetas + tilted"
>   en un subtriangulo = 3 planks abierto).
> - **VALIDOS (no usan Hunter)**: §1.1, §1.3, §3.1 (=dos-direcciones, AKP), §3.2, §3.3
>   (argumentos de borde/fibra 1-D), §4.2 (homotecia facetaria directa).
> - **§2.2 rama E12** (trazas 1-D sobre el borde comun): VALIDA.

---

## 0. Recordatorio: `W_3`

En `Delta`, para tres planks normalizados

`P_i={x in Delta : f_i(x) in I_i}`, `r_i=|I_i|`, `R=r_1+r_2+r_3<1`,

la propiedad `W_3` afirma que para toda forma afin normalizada `f:Delta->[0,1]`,
si

`F = Delta \ (P_1 union P_2 union P_3)`,

entonces

`span_f(F) >= 1-R`.

Por `notes/27-hunter-triples-span-reduction.md`, `W_3` es equivalente al caso de
cuatro planks del triangulo. Por tanto, probar `W_3` cerraria `m=4`; fallarlo daria
un contraejemplo a `m=4`.

---

## 1. Opcion 1 — fibras de una cuarta coordenada

### 1.1 Correccion conceptual [PROVED]

Fijada una forma afin normalizada `f`, sea

`Delta_t = {x in Delta : f(x)=t}`

y

`C = {t in [0,1] : Delta_t subset P_1 union P_2 union P_3}`.

Entonces

`f(F) = [0,1] \ C`.

Por tanto `W_3` equivale a

`diam([0,1] \ C) >= 1-R`.

La desigualdad mas fuerte

`Leb(C) <= R`

es suficiente para `W_3`, pero **no es equivalente**: los intervalos interiores de
`C` no reducen necesariamente el span de `[0,1]\C`.

Equivalentemente, definiendo `m = inf([0,1]\C)` y `M = sup([0,1]\C)` (de modo que
`[0,m) subset C` y `(M,1] subset C`), `W_3` falla si y solo si los casquetes extremos
maximales `[0,m] union [M,1] subset C` satisfacen

`m + (1-M) > R`.

### 1.2 Geometria de una fibra [PROVED]

En cada tramo donde las fibras `Delta_t` varian linealmente, la interseccion de un
plank `P_i` con `Delta_t` es un intervalo de un segmento, con extremos afines en `t`
antes del clipping. Asi, que una fibra este cubierta por los tres planks equivale,
en cada celda combinatoria, a una cadena finita de solapamientos de intervalos 1D.

Esto da una formulacion exacta por cadenas, pero no todavia una cota global.

### 1.3 Subcaso facetario de fibras [PROVED]

Si `P_i={lambda_i in I_i}` son los tres planks de faceta y `f=lambda_3`, entonces

`Leb(C) <= r_1+r_2+r_3`.

Prueba: para `t=lambda_3`, la fibra es el segmento `lambda_1=x`,
`lambda_2=1-t-x`. Si `t notin I_3` y la fibra esta cubierta por los planks
`lambda_1,lambda_2`, su longitud `1-t` no puede exceder `r_1+r_2`; luego
`t>=1-r_1-r_2`. Asi

`C subset I_3 union [1-r_1-r_2,1]`,

y la medida queda acotada por `r_1+r_2+r_3`.

### 1.4 Obstruccion

Una descarga por una medida fija en las fibras vuelve a chocar con Gardner: pedir
marginales uniformes simultaneas en tres coordenadas facetarias fuerza
`E lambda_1=E lambda_2=E lambda_3=1/2`, incompatible con
`lambda_1+lambda_2+lambda_3=1`.

La descarga, si existe, debe depender de la posicion de los intervalos y de la cadena
combinatoria de cobertura de cada fibra.

---

## 2. Opcion 2 — dos facetas + dos planks arbitrarios

> **Nota de encuadre.** Por la equivalencia `W_3 <=> Bang(4)` (nota 27 §0/§3), aqui se
> prueban subcasos de **Bang(4)** (4 planks: 2 facetas + 2 tilted), no instancias directas
> de `W_3` (3 planks). Es legitimo por la equivalencia. **Pero §2.1/§2.2 usan Hunter sobre
> un subtriangulo de 3 planks (abierto): ver la correccion critica del encabezado.**

El caso completo queda abierto, pero hay subcasos probados.

### 2.1 Un plank de faceta toca un extremo [PROVED]

Supongamos que `P_i={lambda_i in I_i}` es uno de los dos planks facetarios y que
`I_i` toca `0` o `1`.

Si `I_i=[0,a_i]`, el subtriangulo

`{lambda_i >= a_i+epsilon}`

es homotetico a `Delta` con factor `h=1-a_i-epsilon` y evita `P_i`. Los otros tres
planks lo cubren, luego Hunter da

`sum_{j!=i} r_j >= h`.

Haciendo `epsilon->0`, se obtiene `sum_j r_j >= 1`.

Si `I_i=[1-a_i,1]`, se toma una copia homotetica de escala `h=1-a_i-epsilon`
contenida en `{lambda_i <= 1-a_i-epsilon}`; evita `P_i`. El mismo argumento con
Hunter da la conclusion.

### 2.2 Los dos planks tilted comparten borde activo [PROVED]

Si los dos planks arbitrarios tienen el mismo borde activo, la desigualdad se prueba
por restriccion al borde comun o por el caso anterior.

Ejemplo: si el borde comun es `E_12`, entonces sobre `E_12` las trazas de los dos
planks tilted tienen longitudes afines exactamente `r_3,r_4`, y las trazas de
`lambda_1,lambda_2` tienen longitudes `a_1,a_2`. Como `E_12` esta cubierto,

`a_1+a_2+r_3+r_4 >= 1`.

Si el borde comun es `E_23`, entonces si `0 in I_1` se usa 2.1; si no, `P_1` no
interseca `E_23`, y el borde queda cubierto por `P_2,P_3,P_4`, dando
`a_2+r_3+r_4>=1`. El caso `E_13` es simetrico.

### 2.3 Residual exacto [OPEN]

Queda el caso en que los dos intervalos facetarios son interiores y los dos planks
tilted tienen bordes activos distintos. Una formulacion equivalente del obstaculo es:

Sea

`C = {x in Delta : lambda_1(x) notin I_1, lambda_2(x) notin I_2}`.

Si `C` esta cubierto por dos planks arbitrarios `P_3,P_4`, probar

`r_3+r_4 >= 1-a_1-a_2`.

Esto cerraria la subfamilia `2 facetas + 2 tilted`.

---

## 3. Opcion 3 — clasificacion por bordes activos

### 3.1 Todos los planks paralelos [PROVED]

Si los tres planks dependen de la misma coordenada afin `h`, entonces `W_3` se reduce
al teorema de dos direcciones: una falla de `W_3` permitiria agregar un plank en la
direccion `f` y obtener una cobertura por solo dos direcciones, de suma `<1`.

### 3.2 Borde activo comun, target con el mismo borde activo [PROVED]

Si los tres planks comparten un borde activo `AB` y el target `f` tambien tiene
`AB` como borde activo, entonces en `AB` todos se restringen a la misma coordenada
`t in [0,1]`. El complemento de tres intervalos de longitud total `R` en `[0,1]`
tiene diametro al menos `1-R`, de donde `span_f(F)>=1-R`.

### 3.3 Borde activo comun, target la coordenada de la faceta opuesta [PROVED]

En coordenadas donde el borde comun es `AB`, escribimos los planks como

`f_i = y+s_i z`, `0<=s_i<=1`, y el target opuesto como `z=lambda_C`.

En la fibra `z=z_0`, el segmento tiene longitud `1-z_0` y cada plank elimina un
intervalo en `y` de longitud a lo sumo `r_i`. Si `z_0<1-R`, la fibra no puede estar
completamente cubierta. Por tanto el conjunto libre alcanza valores de `z` con sup
al menos `1-R`, y tambien intersecta `z=0`; luego `span_z(F)>=1-R`.

### 3.4 Obstruccion [OPEN]

El caso de borde activo comun pero target genericamente tilted sigue abierto. Las
restricciones a bordes pierden factores de pendiente: el plank agregado puede tener
traza de longitud `|J|/s` sobre el borde, no `|J|`. Esta inflacion impide cerrar con
un argumento 1D simple.

Los patrones “dos bordes iguales, uno distinto” y “tres bordes distintos” tambien
siguen abiertos fuera de los subcasos facetarios.

---

## 4. Opcion 4 — enumeracion simbolica de camaras

### 4.1 Reduccion finita exacta [PROVED]

Para tres planks hay `2^3=8` camaras convexas. Cada vertice de una camara es de uno
de estos tipos:

- un vertice de `Delta`;
- interseccion de un lado de `Delta` con una frontera de plank;
- interseccion de dos fronteras de planks.

Hay finitamente muchos slots. Los conteos `3 + 18 + 12 = 33` vertices candidatos (o
`8*binom(6,2)=120` slots etiquetados por camara) son **cotas ilustrativas, no exactas**
(no toda recta-frontera de plank corta las tres aristas dentro del triangulo; las camaras
no son hexagonos genericos). Lo que carga el peso —y es correcto— es que hay FINITOS tipos
combinatorios; los enteros concretos no deben citarse como exactos.

En una carta de normales `u=(0,theta,1)` permutada por vertices, los valores del
target `f` en esos slots son racionales en los parametros direccionales y lineales en
los extremos `a_i,b_i` una vez fijadas las direcciones.

Fijando los signos de factibilidad de cada slot y el orden global de los valores de
`f`, el par que realiza `max f` y `min f` queda determinado. En tal celda,
`W_3` se reduce a una desigualdad racional concreta:

`f(M)-f(m)+(r_1+r_2+r_3)-1 >= 0`.

Por tanto `W_3` equivale a la infeasibilidad de finitos sistemas semialgebraicos:
condiciones de celda mas la desigualdad estricta inversa.

### 4.2 Familias cerradas [PROVED]

- Facetas ancladas `P_i={lambda_i in [0,r_i]}`: la camara
  `lambda_i>=r_i` contiene el triangulo homotetico
  `(r_1,r_2,r_3)+(1-R)Delta`, cuyo `f`-span es `1-R`.
- Si los tres planks y el target se restringen a la misma coordenada sobre algun
  borde, el argumento de intervalos sobre ese borde da `W_3`.

### 4.3 Nucleo duro [OPEN]

La dificultad no es enumerar vertices sino probar las desigualdades en las celdas
genericas donde el maximo y el minimo son intersecciones no triviales de fronteras de
planks. La factibilidad del par max/min no basta; hay que imponer que todos los demas
vertices factibles queden ordenados por debajo/encima. Esto introduce cientos de
comparaciones por carta.

La via promete una prueba finita con certificados de Farkas/Positivstellensatz por
template, pero todavia no produce una demostracion manual.

---

## 5. Opcion 5 — busqueda adversarial de contraejemplo

### Estado [NUMERICAL ONLY — NOT PROOF]

No se encontro contraejemplo a `W_3`.

Los mejores deficits observados

`span_f(F)+R-1`

permanecieron no negativos. Las casi igualdades aparecen cerca de mecanismos ya
entendidos: configuraciones facetarias, colapso a una direccion efectiva, o planks
con borde activo comun y target casi facetario.

Lejos de esos bordes degenerados, la busqueda observo margenes positivos mas grandes.
Esto solo orienta la prueba; no se invoca como demostracion.

---

## 6. Conclusion auditada

- [OPEN] `W_3` completo, por tanto `m=4` general, no fue probado ni refutado.
- [PROVED] La formulacion por fibras correcta es `diam([0,1]\C)>=1-R`; `Leb(C)<=R`
  es solo una condicion suficiente mas fuerte.
- [INVALIDO] El subcaso "un facet plank tocando extremo en 2 facetas+2 tilted" (§2.1)
  usaba Hunter sobre un subtriangulo de 3 planks (abierto): NO esta probado.
- [PROVED] Subcasos que SI sobreviven (no usan Hunter): tilted con borde activo comun
  via trazas 1-D (§2.2 rama E12); borde activo comun con target del mismo borde (§3.2) o
  target de la faceta opuesta (§3.3); todos paralelos = dos-direcciones (§3.1).
- [PROVED] Hay una reduccion finita exacta por camaras y vertices de arreglo (los conteos
  numericos de §4.1 son ilustrativos, no exactos).
- [NUMERICAL ONLY] No aparecio contraejemplo; las casi igualdades se concentran en
  fronteras ya explicadas.

La ruta mas prometedora ahora es combinar la reduccion simbolica de camaras con la
clasificacion por bordes activos: primero cerrar rigurosamente las celdas genericas
que no degeneran a los casos de igualdad conocidos, y luego tratar los limites por
continuidad.
