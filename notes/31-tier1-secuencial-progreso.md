# Tier 1 secuencial -- progreso por opciones (1..4)

> Date: 2026-06-30. Status: PARTIAL / AUDITED.
> Continuacion directa de `notes/30`. Registra avances nuevos y reales tras la
> correccion sobre Hunter (no se usa Hunter como prueba de Bang(3) en el triangulo).
> Etiquetas: `[PROVED]`, `[OPEN]`, `[CANDIDATE]`. La evidencia numerica se marca como
> evidencia, nunca como prueba.
>
> Verificaciones aritmeticas de esta nota (exactas, `fractions`/scan, 2026-06-30):
> - `min ell/w = 4 sqrt(3) - 6 ~ 0.9282` en `tau = 2 - sqrt(3)`; `max = 1` en
>   `tau in {0,1/2,1}` (formula de trabajo de `notes/30` §8.2).
> - `c |-> S_c` no-creciente y convexa.
> - identidad de rigidez `S_c - S_1 = (1-c) sum A_i beta_i / ((1+c beta_i)(1+beta_i))`.

---

## 1. Opcion 3 -- Normalizador `N_c`: sandwich monotono y rigidez de igualdad [PROVED]

### 1.0 Objetos

Para una cobertura de `Delta` por planks `P_i` en direcciones `u_i`, sea
`w_i = w(u_i)` el ancho del cuerpo en `u_i`, `ell_i = ell(u_i)` el normalizador de
cuerda de `notes/30` §8.2, y `width_i` el ancho del plank `i`. La unica propiedad
estructural que se usa abajo es

`0 < ell_i <= w_i`.

Define
`rw_i = width_i / w_i` (ancho relativo de Bang),
`rho_i = ell_i / w_i in (0,1]`,
`beta_i = w_i/ell_i - 1 = 1/rho_i - 1 >= 0`,
`A_i = width_i / ell_i = rw_i (1 + beta_i)`.

Para `c in [0,1]`, el normalizador y su cociente son
`N_c(u) = (1-c) ell(u) + c w(u)`,
`q_c(u) = N_c(u)/w(u) = c + (1-c) rho(u) in [rho, 1]`.

La suma fuerte de Bang con normalizador `N_c` es

`S_c = sum_i width_i / N_c(u_i) = sum_i rw_i / q_c(u_i) = sum_i A_i / (1 + c beta_i)`.

Las identidades `N_c = ell(1 + c beta)` y `width/N_c = A/(1+c beta) = rw/q_c` son
algebra directa. Casos extremos:
`S_0 = sum width_i/ell_i = sum A_i` (cuerda fuerte BY),
`S_1 = sum width_i/w_i = sum rw_i` (Bang relativo, la conjetura).

### 1.1 Proposicion (sandwich monotono) [PROVED]

Para toda cobertura fija y todo `c in [0,1]`:

(i) `c |-> S_c` es no-creciente y convexa.
(ii) `S_1 <= S_c <= S_0`, es decir `sum rw_i <= S_c <= sum width_i/ell_i`.

**Prueba.** Cada termino es `t_i(c) = A_i/(1+c beta_i)` con `A_i>=0`, `beta_i>=0`.
`t_i'(c) = -A_i beta_i/(1+c beta_i)^2 <= 0` y
`t_i''(c) = 2 A_i beta_i^2/(1+c beta_i)^3 >= 0`. Sumando se obtiene (i). La monotonia
da `S_1 <= S_c <= S_0`, que es (ii). QED.

### 1.2 Corolario (admisibilidad gratis en subfamilias probadas) [PROVED]

Si Bang relativo vale para una cobertura (`S_1 = sum rw_i >= 1`), entonces
`S_c >= S_1 >= 1` para **todo** `c in [0,1]`. En particular, en toda subfamilia donde
Bang ya esta probado (p.ej. tres facetas, o "3 facetas + 1" de `notes/30` §1), la
desigualdad fuerte del normalizador `S_c >= 1` se cumple automaticamente para todo `c`,
sin trabajo adicional.

Consecuencia metodologica: el programa `N_c` **no aporta nada** dentro de las
subfamilias ya probadas; su unico valor potencial esta en las configuraciones donde
Bang aun no se conoce.

### 1.3 Corolario (peso logico y cota BY mejorada) [PROVED]

Sea `m_K = min_u rho(u) = min_u ell(u)/w(u)`. Entonces `q_c(u) >= c + (1-c) m_K`, luego

`S_c = sum rw_i/q_c(u_i) <= (sum rw_i)/(c + (1-c) m_K)`.

Por tanto, si se prueba `S_c >= 1` para **todas** las coberturas (para un `c` fijo),
se obtiene

`sum rw_i >= c + (1-c) m_K`,

que supera estrictamente `m_K` para todo `c>0`. Ademas, por el sandwich, "para toda
cobertura `S_c >= 1`" es una consecuencia logica de Bang relativo y es potencialmente
**estrictamente mas debil** (una cobertura con `S_1<1` puede aun tener `S_c>=1` si
algun `beta_i>0`). El parametro `c` interpola: `c=1` es Bang; `c<1` es mas debil pero
ya bate BY. Para el triangulo equilatero `m_K = 4 sqrt(3) - 6 ~ 0.9282` (verificado;
distinto del `2/(1+sqrt(d)) ~ 0.828` general de BY, que es otra cota mas debil).

### 1.4 Proposicion (rigidez de igualdad) [PROVED]

Vale la identidad exacta, para todo `c in [0,1]`:

`S_c - S_1 = (1-c) * sum_i A_i beta_i / ((1+c beta_i)(1+beta_i))`,   (R)

con cada sumando `>= 0`. En consecuencia, si una cobertura cumple la igualdad de Bang
`S_1 = sum rw_i = 1`, entonces para todo `c in [0,1)` son equivalentes:

  (a) `S_c = 1` (la desigualdad fuerte `N_c` tambien es ajustada en `c`);
  (b) `beta_i = 0` (equivalente a `ell_i = w_i`, direccion "balanceada") en todo plank
      activo (`rw_i > 0`).

Y si (b) se cumple, entonces `S_c = 1` para **todo** `c in [0,1]`.

**Prueba.** Para (R): `1/(1+c beta) - 1/(1+beta) = beta(1-c)/((1+c beta)(1+beta))`;
multiplicando por `A_i` y sumando da (R) (verificado exactamente con racionales).
Con `S_1=1`, `S_c=1` sii la suma en (R) es cero; como `1-c>0` y cada sumando es `>=0`,
esto equivale a `A_i beta_i = 0` para todo `i`. Como `A_i = rw_i(1+beta_i)` y
`1+beta_i = w_i/ell_i >= 1`, se tiene `A_i>0 <=> rw_i>0`; luego `A_i beta_i = 0` sii
`beta_i = 0` en cada plank activo. La afirmacion final: `beta_i=0` da `1+c beta_i=1`,
luego `S_c = sum A_i = sum rw_i = S_1 = 1`. QED.

### 1.5 Correccion de una afirmacion previa

En `notes/30` (y en el plan) se enuncio de forma laxa que "la igualdad de `N_c` fuerza
`beta_i=0` en los planks activos". La forma **correcta** es la Prop 1.4: el forzamiento
`beta_i=0` ocurre cuando se combina `S_c=1` **con la igualdad de Bang `S_1=1`**. NO es
la igualdad en la cota derivada `sum rw = c+(1-c) m_K`: la igualdad en esa cota requiere
lo contrario, que todo plank activo este en la peor direccion `rho_i = m_K`
(`beta_i = 1/m_K - 1`, constante y no nula).

### 1.6 Corolario (buffer de primer orden; donde puede morder `N_c`) [PROVED]

Derivando `S_c` en `c=1`:

`dS_c/dc |_{c=1} = - sum_i A_i beta_i/(1+beta_i)^2 = - sum_i rw_i (1 - rho_i)`,

asi que cerca de `c=1`

`S_c = S_1 + (1-c) * sum_i rw_i (1 - rho_i) + O((1-c)^2)`.

Luego `N_c` tolera un defecto de Bang de orden `(1-c) * sum_i rw_i (1-rho_i)`. El buffer
de primer orden es **cero exactamente** cuando `rho_i=1` (`beta_i=0`) en todo plank
activo, es decir, en las direcciones balanceadas; en el triangulo esas son las de tipo
faceta (`tau in {0,1/2,1}`), donde Bang ya esta probado. En cualquier otra parte (algun
plank activo en direccion no balanceada) el buffer `(1-c) sum rw_i(1-rho_i)` es
estrictamente positivo.

**Lectura honesta.** El metodo `N_c` es "ortogonal" a los casos ya probados: no ayuda
en las configuraciones balanceadas (faceta), y concentra todo su margen en las
direcciones genericas no balanceadas. Esto NO prueba Bang(3); cuantifica con precision
donde hay margen y donde no. El objetivo exacto de la Opcion 3 queda reformulado:
acotar inferiormente el defecto `S_0 - 1 = sum A_i - 1` por el termino de penalidad
`sum A_i (c beta_i)/(1+c beta_i)` para el mayor `c` posible (cf. `notes/30` §8.2).

---

## 2. Opcion 2 -- `W_2` con borde activo comun y target generico [PARTIAL]

### 2.0 Modelo (de `notes/30` §8.3)

`Delta = {(y,z): y>=0, z>=0, y+z<=1}`, vertices `O=(0,0)`, `(1,0)`, `(0,1)`.
Dos planks con borde activo comun en `z=0`:

`P_i = {g_i in I_i}`, `g_i = y + a_i z`, `0 <= a_i <= 1`, `r_i = |I_i|`, `R = r_1+r_2 < 1`.

(`g_i` vale `0,1,a_i` en `O,(1,0),(0,1)`; ambos coinciden con `g=y` en el borde `z=0`.)
Target generico normalizado `f = z + s y`, `0 < s < 1` (vale `0,s,1` en `O,(1,0),(0,1)`;
su borde activo es `y=0`). Objetivo: `W_2` en este modelo,

`span_f(F) >= 1 - R`,  `F = Delta \ (P_1 union P_2)`.

Herramienta: fibras de `z` constante. En `z=z_0`, `y in [0, 1-z_0]`; `P_i` quita un
intervalo de `y` de longitud `<= r_i`. Luego la medida libre por fibra cumple

`mu(z_0) >= (1 - z_0) - R`,   nonempty para `z_0 < 1 - R`.   (F1)

### 2.1 Cota cruda [PROVED]

Para toda configuracion del modelo: `span_f(F) >= 1 - (1+s) R`.

**Prueba.** *Punto alto.* Para `0 < eps < 1-R`, en la fibra `z_0 = 1-R-eps` se tiene
`mu(z_0) >= eps > 0` por (F1); existe punto libre con `f = z_0 + s y >= z_0 = 1-R-eps`.
Luego `sup_F f >= 1-R`. *Punto bajo.* En la fibra `z=0`, el `y` libre minimo es
`<= R` (lo removido mide `<= R`, no puede cubrir `[0,R+delta]`); ese punto libre tiene
`f = s y <= s R`, luego `inf_F f <= sR`. Por tanto
`span_f(F) >= (1-R) - sR = 1 - (1+s)R`. QED.

Esta cota es `< 1-R` por `sR`; es el "factor de pendiente" de `notes/28` §3.4 /
`notes/30` §8.3, ahora cuantificado de forma limpia y valida en todos los subcasos.

### 2.2 Subcaso `0 notin I_1 union I_2` [PROVED]

Si ningun plank cubre el valor `g=0` del origen comun, entonces `O = (0,0) in F`. Como
`f >= 0` en `Delta` y `f(O)=0`, se tiene `inf_F f = 0`. Con `sup_F f >= 1-R` (§2.1),

`span_f(F) >= (1-R) - 0 = 1 - R`.

Luego `W_2` vale en este subcaso. QED.

### 2.3 Mecanismo de "vaciado de fibras altas" por plank esquina [CANDIDATE]

Si `0 in I_1` (subcaso complementario al 2.2; simetrico si `0 in I_2`), entonces, como
`g_1 >= 0`, `I_1 cap [0,1] = [0,h_1]` con `h_1 <= r_1`, y

`P_1 = {y + a_1 z <= h_1}`,

una "esquina" pegada a `O`. En la fibra `z_0`, `P_1` quita `{y <= h_1 - a_1 z_0}`, de
longitud `(h_1 - a_1 z_0)_+`, **decreciente en `z_0`**, y **nula** para `z_0 >= h_1/a_1`
(si `a_1 > 0`). En esas fibras altas solo actua `P_2`, luego la medida libre cumple
`mu(z_0) >= (1-z_0) - r_2`, nonempty hasta `z_0 < 1 - r_2`. Por tanto

`sup_F f >= 1 - r_2`   (cuando `h_1/a_1 <= 1 - r_2`),

que **supera** `1-R = 1 - r_1 - r_2` por `r_1`. Es decir: una esquina inclinada libera
las fibras altas y permite que `sup_F f` crezca de `1-R` a `1-r_2`, recuperando, en el
lado superior, exactamente el margen perdido por la pendiente.

**Por que aun NO cierra (gap honesto).** Para concluir `span >= 1-R` falta controlar
`inf_F f` simultaneamente. La cota cruda da solo `inf_F f <= sR`, y
`(1-r_2) - sR >= 1-R` equivale a `r_1 >= sR`, que **no** es universal. El lado inferior
interactua con `P_2` cerca de `O` y no se controlo por debajo de `sR` en general. El
subcaso `a_1 = 0` (esquina plana, plank paralelo a faceta) tampoco lo recupera por este
mecanismo (no hay vaciado). Asi que 2.3 identifica el mecanismo correcto del lado
superior pero deja `[OPEN]` el acoplamiento con el lado inferior.

### 2.4 Reformulacion por shear (planks -> tiras axis-parallel) [PROVED, estructural]

> **[NOTA 2026-06-30, de `notes/32` EXP-A]** Este shear modela solo la orientacion
> **SAME** (ambos `g_i` crecientes en el borde comun `g_i=y` en `z=0`). Existe tambien la
> orientacion **OPP** (`g_2 = 1-y+(a_2-1)z`, opuesta), que **contiene la config de Hunter**
> y es donde vive parte del caso ajustado. El motor general sobre `Delta` (no el shear)
> cubre ambas. Conclusion de EXP-A: el locus extremal (`span=1-R`) es exactamente
> "al menos una de `g_1,g_2,f` es de faceta"; el caso totalmente generico tiene holgura.

Si `a_1 != a_2`, el shear lineal `(y,z) |-> (g_1,g_2) = (y+a_1 z, y+a_2 z)` es invertible
y mapea `Delta` al triangulo `Delta'` de vertices `(0,0), (1,1), (a_1,a_2)` (verificado).
Como `g_i` recorre `[0,1]` en `Delta`, en coordenadas `(g_1,g_2)`:

- `P_1 = {g_1 in I_1}` y `P_2 = {g_2 in I_2}` son **tiras paralelas a los ejes** de
  anchos `r_1, r_2` (normalizados al lado `[0,1]` del cuadrado unidad).
- `Delta' subset [0,1]^2` con dos vertices en la diagonal `g_1=g_2` (imagen del borde
  comun `z=0`) y el tercero en `(a_1,a_2)`.
- el target `f = z + s y` es una forma afin de `(g_1,g_2)` (via `z=(g_1-g_2)/(a_1-a_2)`,
  `y = g_1 - a_1 z`).

Asi, el caso `W_2` de borde activo comun **equivale** a: *para un triangulo inscrito en
el cuadrado con dos vertices en la diagonal, dos tiras axis-parallel de anchos `r_1,r_2`,
y un target afin `f`, el span de `f` sobre el libre es `>= 1 - r_1 - r_2`.* Es la version
"dos planks de faceta (en el cuadrado) + 1 target generico, restringida al triangulo
`Delta'`". El obstaculo es exactamente que `Delta'` es medio cuadrado: no estan
disponibles las cuatro esquinas-rectangulo del complemento de la cruz. (`a_1=a_2` es el
caso degenerado de dos direcciones efectivas, ya cerrado por el teorema de dos
direcciones.)

### 2.5 Estado

- [PROVED] `span_f(F) >= 1 - (1+s) R` (todos los casos del modelo).
- [PROVED] `W_2` si `0 notin I_1 union I_2`.
- [CANDIDATE] mecanismo de vaciado: con `0 in I_1`, `a_1>0`, `h_1/a_1 <= 1-r_2`,
  `sup_F f >= 1 - r_2`. Falta el control de `inf_F f` para cerrar.
- [OPEN] `W_2` generico, equivalente a `Bang(3)` para el triangulo (Prop 3.1 de
  `notes/27`).

El nucleo exacto pendiente sigue siendo
`span_{z+s y}(Delta \ (P_1 union P_2)) >= 1 - r_1 - r_2` para `g_i = y + a_i z`, en el
regimen "esquina poco inclinada / esquina plana".

---

## 3. Evidencia numerica de control [EVIDENCE, NOT PROOF]

Barrido aleatorio del modelo §2 (Python puro; `seed=12345`; 4000 configuraciones
`(a_1,a_2,s,r_1,r_2,I_1,I_2)`; `span_f(F)` por grilla del triangulo), 2026-06-30:

- `min (span - (1-R))`: `-0.0025` con grilla `60`, que sube a `+0.010` con grilla `120`.
  El valor negativo es discretizacion (se anula al refinar): **ningun contraejemplo** a
  `W_2` (`span >= 1-R`). Las peores configuraciones tienen `s` muy chico o `R` cerca de
  `1`, consistente con que `W_2` es **cierto y ajustado** (`span -> 1-R`), como debe ser
  por su equivalencia con `Bang(3)`.
- `min (span - (1-(1+s)R)) > 0` siempre (la cota cruda probada §2.1 se cumple con
  margen). Confirmacion de consistencia, no prueba.
- Subcaso `0 notin I_1 union I_2` (§2.2): margen `>= -0.0025` (grilla) -> `+0.015`
  (refinada); consistente con la prueba `span >= 1-R`.

Esto es evidencia de consistencia y de ausencia de contraejemplo, no una prueba.

---

## 4. Secuencia / proximos pasos

1. (Opcion 2) Cerrar el acoplamiento `inf_F f` del §2.3, o construir el contraejemplo
   que muestre que `1-(1+s)R` es lo mejor por fibras puras (forzando un argumento global).
2. (Opcion 3) Implementar el test exacto `S_c` (defecto fuerte) sobre plantillas de
   direcciones fijas; buscar el mayor `c` certificable. Usar Prop 1.4/1.6 para enfocar
   en configuraciones no balanceadas.
3. (Opcion 4) Certificador exacto `m=3` por LP/Farkas (`notes/30` §8.4), con el collar
   `R=1` por estabilidad transversal.
4. Mantener circuitos de Farkas (`notes/30` §8.5) como linea estructural.

> Nota de entorno: el Python local no tiene numpy/scipy; los chequeos de esta nota se
> hicieron en Python puro (`fractions`). Los tests LP de Opciones 3/4 requieren un
> backend exacto (fractions+simplex propio) o ejecucion remota.
