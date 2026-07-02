# Hunter por triples: reduccion exacta a una desigualdad de span
> Date: 2026-06-29. Status: PARTIAL / REDUCTION.
> No prueba el caso residual completo. Si separa con precision que habria que probar.
>
> **[CORRECCION CRITICA 2026-06-30 — auditoria]** La referencia Hunter (Proc. AMS 117,
> 1993, 819-821) EXISTE pero NO demuestra el caso general de 3 planks en el triangulo.
> Verreault (survey, §2.2.3) y Bakaev-Yehudayoff (2026) confirman: el caso de 3 planks
> sigue ABIERTO. Hunter solo probo (i) el caso de DOS planks en el plano y (ii) la
> CARACTERIZACION DE IGUALDAD `Sigma rw = 1 <=> t1+t2+t3 = 1`. NO la desigualdad para
> 3 planks arbitrarios.
> Impacto en esta nota:
> - **§4 `W_2` [PROVED] es FALSO**: por la Prop 3.1, `W_2 <=> Bang(3)`, que esta ABIERTO.
>   Reetiquetar `W_2` como **[OPEN, equivalente a Bang(3)]**.
> - **§5 `W_3` facetario**: la via original (Teorema B Caso 2 de nota 26) usaba Hunter.
>   **REPARADO 2026-06-30**: `notes/30` §1 prueba "3 facetas + 1 arbitrario" sin Hunter,
>   de donde `W_3` facetario queda **[PROVED] via notes/30 §1**.
> - **La Prop 3.1 (`W_k <=> Bang(k+1)`) SIGUE SIENDO CORRECTA** (es pura logica) y es el
>   aporte real: dice que probar `W_2` = probar el caso de 3 planks (la verdadera frontera).

---

## 1. Setup

Trabajamos en
`Delta = {x in R^3 : x_i >= 0, x_1+x_2+x_3=1}`.

Cada plank normalizado es
`P_i = {x in Delta : f_i(x) in I_i}`,
donde `f_i: Delta -> [0,1]` es afin con rango completo `[0,1]`,
`I_i` es un intervalo, y `r_i=|I_i|=rw(P_i)`.

Para una familia `P_1,...,P_k`, definimos el conjunto libre

`F(P_1,...,P_k) = Delta \ (P_1 union ... union P_k)`.

Para una forma afin normalizada `f: Delta -> [0,1]`, definimos

`span_f(A) = sup_{x in A} f(x) - inf_{x in A} f(x)`.

Si `A` es vacio, no usamos `span_f(A)`.

---

## 2. La propiedad residual `W_k`

**Definicion.** `W_k` es la siguiente afirmacion:

> Para cualesquiera `k` planks `P_1,...,P_k` sobre `Delta`, de suma
> `R = r_1+...+r_k < 1`, y para toda forma afin normalizada
> `f: Delta -> [0,1]`, el conjunto libre `F(P_1,...,P_k)` es no vacio y se cumple
> `span_f(F(P_1,...,P_k)) >= 1-R`.

Esta propiedad dice que los `k` planks no solo dejan algun punto libre, sino que
dejan un conjunto libre con ancho residual al menos `1-R` en toda coordenada afin.

---

## 3. Equivalencia con el caso de `k+1` planks [PROVED]

### Proposicion 3.1

Para un `k` fijo, `W_k` es equivalente al enunciado de Bang para `k+1` planks
sobre el triangulo.

### Prueba

**`W_k => Bang(k+1)`.**
Supongamos que `P_1,...,P_{k+1}` cubren `Delta` y que
`S = r_1+...+r_{k+1} < 1`.
Sea
`F = F(P_1,...,P_k)`.
Como `r_1+...+r_k < 1`, por `W_k`, aplicado a `f=f_{k+1}`,

`span_{f_{k+1}}(F) >= 1-(r_1+...+r_k) > r_{k+1}`.

Pero la cobertura por `P_1,...,P_{k+1}` implica
`F subset P_{k+1}`, luego `f_{k+1}(F) subset I_{k+1}` y por tanto
`span_{f_{k+1}}(F) <= |I_{k+1}| = r_{k+1}`.
Contradiccion. Entonces `S>=1`.

**`Bang(k+1) => W_k`.**
Primero, `F(P_1,...,P_k)` no puede ser vacio. Si fuera vacio, los primeros
`k` planks cubririan `Delta`; agregando un plank adicional arbitrario de ancho
relativo `epsilon>0` con `R+epsilon<1`, obtendriamos una cobertura por `k+1`
planks de suma menor que `1`, contradiciendo `Bang(k+1)`.

Supongamos ahora que la cota de span falla. Entonces existen `P_1,...,P_k`,
de suma `R<1`, y una forma afin normalizada `f` tales que

`L := span_f(F(P_1,...,P_k)) < 1-R`.

Para cualquier `epsilon>0`, elegimos un intervalo `J_epsilon` de longitud
`L+epsilon` que contiene `f(F(P_1,...,P_k))`.
Entonces los `k+1` planks

`P_1,...,P_k, Q_epsilon={x in Delta : f(x) in J_epsilon}`

cubren `Delta`: fuera de `F` cubren los primeros `k`, y sobre `F` cubre
`Q_epsilon`.

Si `epsilon` es suficientemente pequeno, `R+L+epsilon<1`, contradiciendo
`Bang(k+1)`. Por tanto `W_k` debe ser cierta.

QED.

### Consecuencia

El criterio recomendado para atacar `m=4`,

`span_{f_j}(Delta \ union_{i!=j} P_i) > r_j` para algun `j` cuando `S<1`,

queda implicado por `W_3`: de hecho, si `W_3` vale y `S<1`, entonces para
todo `j`, aplicado al triple `i!=j`,

`span_{f_j}(Delta \ union_{i!=j} P_i) >= 1-(S-r_j) > r_j`.

Por la proposicion, probar `W_3` en general es equivalente a probar el teorema
completo de 4 planks. El criterio mas debil "existe `j`" es suficiente para
refutar una cobertura sub-1, pero no se demuestra aqui que sea equivalente a
Bang. La formulacion equivalente correcta es `W_3` completo.

No es una reduccion a Hunter; es una reformulacion fiel del muro `m=4`.

---

## 4. Caso `W_2` [OPEN — equivalente a Bang(3)]

> **[CORRECCION 2026-06-30]** La version previa de esta seccion afirmaba `W_2`
> [PROVED] "via Hunter". Es FALSO. La prueba erronea decia "por Hunter, Bang es
> verdadero para tres planks". Hunter (1993) NO probo el caso de 3 planks; probo
> (i) el caso de DOS planks en el plano y (ii) la caracterizacion de igualdad.
> Por la Prop 3.1, `W_2 <=> Bang(3)`, y `Bang(3)` sobre el triangulo esta ABIERTO
> (Verreault survey §2.2.3; Bakaev-Yehudayoff 2026). Luego `W_2` esta ABIERTO.

### Proposicion 4.1 [OPEN]

`W_2` es equivalente al caso de Bang para tres planks sobre el triangulo
(`Bang(3)`), por la Proposicion 3.1 con `k=2`. Como `Bang(3)` permanece abierto,
`W_2` permanece abierto.

### Que SI aporta Hunter (y por que no basta)

Hunter da dos cosas firmes:
- **(2 planks)** Para dos planks que cubren un cuerpo convexo en el plano,
  `r_1+r_2 >= 1`. Esto es `Bang(2)` afin, equivalente a `W_1` (no a `W_2`).
- **(igualdad)** La caracterizacion `Sigma rw = 1` para configuraciones extremales.

Ninguna de las dos da `W_2`: `W_2` requiere controlar el *span del conjunto libre*
de DOS planks, lo que por la equivalencia es exactamente el caso de TRES planks.
El salto `2 planks -> span residual de 2 planks` es precisamente `Bang(3)`, abierto.

### Interpretacion (condicional)

SI `W_2` fuera cierto, diria que dos planks de suma `R<1` dejan un conjunto libre
cuyo span en toda direccion afin normalizada es al menos `1-R`. Esta forma residual
fuerte es, de hecho, una reformulacion de `Bang(3)`, no una consecuencia de Hunter.

---

## 5. Caso `W_3` para triples de facetas [PROVED]

### Proposicion 5.1

Sea `P_i={lambda_i in I_i}`, `i=1,2,3`, una terna de planks paralelos a facetas.
Sea `R=r_1+r_2+r_3<1`. Entonces, para toda forma afin normalizada
`f: Delta -> [0,1]`,

`span_f(F(P_1,P_2,P_3)) >= 1-R`.

### Prueba

Esta es la implicacion `Bang(4) => W_3`, pero restringida a la subfamilia
`3 facet planks + 1 arbitrary plank`, que ya fue probada en
`notes/26-hallazgo-auditado-2026-06-29.md`.

En detalle, si la desigualdad fallara, con
`L=span_f(F(P_1,P_2,P_3))<1-R`, tomamos un intervalo `J_epsilon` de longitud
`L+epsilon` que contiene `f(F(P_1,P_2,P_3))`. Entonces los cuatro planks

`P_1, P_2, P_3, {f in J_epsilon}`

cubren `Delta` y tienen suma

`R+L+epsilon<1`

para `epsilon` pequeno. Esto contradice el Teorema B de la nota 26.
QED.

---

## 6. Estado del ataque recomendado

- [PROVED] La estrategia Hunter-por-triples es correcta si se reemplaza el punto
  libre de cada triple por el conjunto libre completo y su `span`.
- [OPEN] El lema de `span` para `k=2` (`W_2`) es equivalente a `Bang(3)` (Prop 3.1),
  que esta ABIERTO. NO se sigue de Hunter (Hunter solo da 2 planks = `W_1`, mas la
  caracterizacion de igualdad). Correccion 2026-06-30.
- [PROVED] El lema de `span` para `k=3` queda demostrado cuando los tres planks
  del triple son paralelos a facetas (`W_3` facetario, via notes/30 §1).
- [OPEN] El lema `W_3` para tres planks arbitrarios es exactamente equivalente al
  caso general de cuatro planks. Probarlo cerraria `m=4`; no se obtuvo esa prueba.

---

## 7. Auditoria

Esta nota no usa evidencia numerica como prueba. La busqueda numerica realizada durante
el ataque no encontro contraejemplos a `W_3`, pero eso no se invoca. El unico contenido
marcado como [PROVED] son equivalencias logicas (Prop 3.1, pura logica) o consecuencias
de teoremas ya probados (notes/30 §1 para el caso facetario `W_3`; notes/26 Teorema B).
Hunter ya NO se invoca como fuente de ningun [PROVED] en esta nota: su unico uso valido
(`W_1` = 2 planks, y la caracterizacion de igualdad) no produce `W_2`.

La conclusion honesta es que la recomendacion produce una formulacion mas precisa del
muro `m=4`: hay que probar la desigualdad residual `W_3`, una afirmacion de ancho del
conjunto libre de tres planks, no solo combinar puntos libres de triples.
