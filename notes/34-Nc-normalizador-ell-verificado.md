# P-A: normalizador `N_c` -- `ell(u)` definido y formula VERIFICADA, y busca de `c>0`

> Date: 2026-06-30. Status: LIVE / INCREMENTAL.
> Objetivo (P-A del jefe de research): (1) definir `ell(u)` rigurosamente y verificar
> simbolicamente la formula `ell/w` del equilatero; (2) buscar el mayor `c>0` con
> `S_c = sum width_i/N_c(u_i) >= 1` (peor cover). Desbloquea la jugada competitiva
> (batir B-Y) independiente del muro de Hunter.
>
> Matices del jefe de research asumidos: §6 de `notes/33` es DESCRIPTIVO (lead, no prueba);
> W_2 borde-comun es callejon sin salida (no se invierte mas); N_c sigue abierto pero
> estaba BLOQUEADO por falta de `ell(u)`. Esta nota lo desbloquea.

---

## 1. `ell(u)` definido y formula `ell/w` VERIFICADA simbolicamente [PROVED]

**Definicion (B-Y 2026):** `ell(u)` = longitud de la **cuerda mas larga de `K` paralela a
`u`** (el segmento mas largo en direccion `u` contenido en `K`). `w(u)` = ancho (extension
de la proyeccion sobre `u`). Siempre `ell(u) <= w(u)`.

Parametrizando una direccion por los valores de vertice de la forma `(0, tau, 1)`
(`tau in [0,1]` el valor del vertice intermedio), para el triangulo equilatero:

`ell(u)/w(u) = 2(tau^2 - tau + 1)/(2 - tau)`   si `tau <= 1/2`,
`ell(u)/w(u) = 2(tau^2 - tau + 1)/(1 + tau)`   si `tau >= 1/2`.

**Verificacion (exacta):**
- Geometrico vs formula: `max |ell/w_geom - formula| = 4.4e-16` sobre 3600 direcciones
  (`numpy`, cuerda mas larga por vertice medio en proyeccion perpendicular).
- **Prueba SIMBOLICA** (`sympy`) en el sector `theta in (pi/3, pi/2)` (roles de vertice
  fijos): con `ell = (sqrt3/2)/sin(theta)` (cuerda por el vertice `C` hasta la base) y
  `w = (cos theta)/2 + (sqrt3/2) sin theta`, se obtiene
  `ell/w = 2 sqrt3 / (sqrt3 - 2 cos(2 theta + pi/6))`, y la `formula(tau)` con
  `tau = cos theta / w` da **identicamente lo mismo** (`ell/w - formula = 0` exacto, via
  producto-a-suma `2 sin theta sin(theta+pi/6) = sqrt3/2 - cos(2 theta+pi/6)`).
- Por la simetria diedral `D_3` del equilatero y la simetria `tau <-> 1-tau` de la formula
  (mismo numerador `tau^2-tau+1`, denominador `2-tau <-> 1+(1-tau)=2-tau`), el sector
  cubre todas las direcciones. **Formula verificada en todo `u`.**
- Minimo: `min ell/w = 4 sqrt3 - 6 ~ 0.928203` en `tau = 2 - sqrt3` (`theta = 5 pi/12`),
  exacto. `ell/w = 1` (balanceado) sii `tau in {0, 1/2, 1}`.

Antes solo el minimo `4 sqrt3-6` estaba verificado; **ahora la formula completa lo esta.**
`N_c` queda rigurosamente fundado: `N_c(u) = (1-c) ell(u) + c w(u)`,
`q_c(u) = N_c/w = c + (1-c) rho(u)`, `rho(u) = ell/w in [4 sqrt3-6, 1]`.

Script: `experiments/exp_ell_verify.py`.

---

## 2. Busqueda del mayor `c>0` (peor cover) -- resultado y CORRECCION

`S_c = sum_i rw_i / q_c(tau_i)`, `q_c(tau) = c + (1-c) rho(tau)`,
`rho(tau) = ell/w` (formula verificada §1). `tau_i` = valor de vertice intermedio de la
direccion `i`. Como `q_c <= 1`, `S_c >= sum rw_i = Sum rw`, con igualdad sii `q_c=1` en
todo plank activo, i.e. `rho_i=1`, i.e. `tau_i in {0, 1/2, 1}` (direccion **balanceada**).

### 2.1 El caso binding = teselaciones BALANCEADAS (`tau in {0,1/2,1}`) [EVIDENCE+exacto]

Para teselaciones (`Sum rw = 1`):
- **Hunter faceta** (`tau=0`, `rho=1`): `S_c = 1` para todo `c`. Tight.
- **Simetrica tercio-central** (`tau=1/2`): `rho(1/2) = 1` **exacto** (`formula(1/2)=1`),
  luego `S_c = 1` para todo `c`. **Tight, sin buffer.**
- **No balanceada** (`tau=(0.45,0.45,0.55)`, `rho ~ 0.971 < 1`): `S_c > 1`. Buffer
  **EXACTO** (de la identidad (R) de nota 31, verificado con `sympy`):

  `S_c - Sum rw = (1-c) * sum_i rw_i (1-rho_i)/q_c(tau_i)`,  `q_c = c+(1-c)rho_i`.

  (Para teselaciones `Sum rw=1`, esto es `S_c - 1`.) Numericamente para este ejemplo:
  `0.031 (c=0) -> 0.015 (c=.5) -> 0.0037 (c=.9)`. La version `(1-c) sum rw_i(1-rho_i)`
  (sin `/q_c`) es solo el primer orden en `c->1`; la exacta lleva el factor `/q_c`.

Busqueda de peor cover (3782 teselaciones esenciales, grid): `min S_c -> 1` para todo `c`
(`1.005 @c=0`, `1.003 @c=.5`, `1.0005 @c=.9`), alcanzado en configs casi balanceadas.
Combinado con los balanceados exactos: **`min S_c = 1` para todo `c in [0,1]`**, binding en
las teselaciones balanceadas.

### 2.2 CORRECCION al matiz #3 del jefe de research [IMPORTANTE]

El matiz #3 afirmaba: "la teselacion simetrica tiene direcciones no-faceta (`rho_i<1`),
luego tiene buffer (`N_c` se satisface con margen ahi)". **Es incorrecto.** Las
direcciones simetricas tienen `tau=1/2`, y `rho(1/2) = 1` (balanceadas), **no** `rho<1`.
Luego `N_c` es **AJUSTADO (tight) en la simetrica para todo `c`**, sin buffer. El error
es la implicacion "no-faceta => `rho<1`": las direcciones **mediana** (`tau=1/2`) son
no-faceta pero balanceadas (`rho=1`). Balanceado `<=> tau in {0,1/2,1}` = 6 facetas + 3
medianas, NO solo facetas.

### 2.3 Interpretacion honesta (N_c no es un win gratis)

- Numericamente `N_c` es admisible para todo `c in [0,1]` (ningun cover rompe `S_c<1`),
  pero eso es solo **consistencia con Bang**; NO da un `c<1` "probable" automatico.
- El payoff competitivo exige **PROBAR** `S_c >= 1` para un `c<1` fijo (da
  `Sum rw >= c + (1-c)(4 sqrt3 - 6)`, batiendo 0.928 para todo `c>0`).
- El conjunto de igualdad de `S_c >= 1` (donde es tight) = **teselaciones balanceadas**
  (`tau in {0,1/2,1}`). Para coberturas NO balanceadas, `S_c >= 1 <=> Sum rw >= q_c`, y
  `q_c = c+(1-c)rho >= c + (1-c)0.928 > 0.928` para `c>0`: **mas fuerte que B-Y** pero
  **mas debil que Bang** (`q_c<1`).
- **El "muro" de `N_c` para `c>0`** son las teselaciones balanceadas: las **facetas**
  (`tau in {0,1}`) ya estan probadas (faceta-paralelo), pero las **medianas** (`tau=1/2`,
  p.ej. la tercio-central simetrica) **NO**. `N_c(c>0)` no se cierra sin manejar esas
  teselaciones mediana/balanceadas no-faceta.

**Veredicto:** `N_c` queda **fundado y es un blanco legitimo** (la verificacion de `ell`
es progreso real, §1), pero el experimento muestra que **NO es el win citable facil**: su
caso binding incluye una teselacion no-faceta no probada (medianas `tau=1/2`). Es un muro
**mas chico y bien definido** que Bang(3), no su ausencia.

---

## 3. Proximos pasos

1. **[RESUELTO]** `S_0 = sum width/ell >= 1` **ES** la desigualdad de cuerda de B-Y
   (**Lema 5** de Bakaev-Yehudayoff 2026: `sum opt(P_i)/ell_K(u_i) >= 1`). Luego el
   baseline `c=0` esta **probado** y da `Sum rw >= min rho = 4 sqrt3 - 6 ~ 0.928`
   (consecuencia del **Lema 5** de B-Y aplicado al `min ell/w` del equilatero; **no** es el
   Teorema 8, que es el general `2/(1+sqrt d)=0.828`). Cualquier `c>0` probado lo bate
   estrictamente. Ya no es pendiente.
2. **Atacar el muro de `N_c`:** Bang para coberturas de **direcciones balanceadas**
   (6 facetas + 3 medianas, conjunto FINITO de direcciones). Facetas: probadas. Medianas
   (`tau=1/2`): nuevo. Si Bang-balanceado se prueba, mas el control del termino no
   balanceado (`Sum rw >= q_c`), se cierra `S_c>=1` para ese `c`.
3. **P-C (higiene, en paralelo):** re-verificar afirmaciones de grilla de notas 28/30/31
   con motor exacto/continuo (la nota 33 mostro que la grilla miente sobre `min`).

Scripts: `experiments/exp_ell_verify.py` (`ell` y formula), analisis `S_c` inline.

