# Tier 1 reenfocado -- hallazgos del ataque paralelo
> Date: 2026-06-30. Status: PARTIAL / AUDITED NOTES.
> Esta nota registra los hallazgos posteriores a la correccion critica sobre Hunter:
> no se usa Hunter como prueba de Bang(3) para el triangulo. Todo resultado abajo queda
> etiquetado como `[PROVED]`, `[OPEN]` o `[CANDIDATE / NEEDS AUDIT]`.

---

## 0. Correccion de contexto

La correccion de `notes/26` y `notes/27` cambia el objetivo limpio:

- `W_2` es equivalente a `Bang(3)` para el triangulo y queda `[OPEN]`.
- `W_3` es equivalente a `Bang(4)` para el triangulo y queda `[OPEN]`.
- Cualquier argumento que pele a un subtriangulo cubierto por 3 planks y luego invoque
  "Hunter" no es valido, salvo que el subcaso de 3 planks usado ya haya sido probado por
  otro medio.

---

## 1. Tres facetas + un plank arbitrario [PROVED]

### Enunciado

Sea

`P_i={lambda_i in I_i}`, `a_i=|I_i|`, `i=1,2,3`,

y sea

`Q={f in J}`, `t=|J|`,

donde `f:Delta->[0,1]` es afin normalizada. Si

`Delta subset P_1 union P_2 union P_3 union Q`,

entonces

`a_1+a_2+a_3+t >= 1`.

### Prueba sin Hunter

Elige un borde activo de `f`. Reetiquetando vertices, supongamos

`f(v_j)=0`, `f(v_k)=1`,

y sea `v_i` el vertice opuesto. Escribe `theta=f(v_i)`.

Para `s in [0,1]`, considera la fibra

`F_s={lambda_i=s}`.

Parametrizala por `u=lambda_k in [0,1-s]`; entonces

`lambda_j=1-s-u`,

y

`f|_{F_s}(u)=theta s+u`.

En esa fibra:

- `P_i cap F_s=F_s` si `s in I_i`, y es vacio si `s notin I_i`.
- `P_j cap F_s={u: 1-s-u in I_j}`, de longitud a lo sumo `a_j`.
- `P_k cap F_s={u: u in I_k}`, de longitud a lo sumo `a_k`.
- `Q cap F_s={u: theta s+u in J}`, de longitud a lo sumo `t`.

Sea

`B=a_j+a_k+t`.

Si `s notin I_i` y la fibra esta cubierta, entonces el segmento completo de longitud
`1-s` esta cubierto por tres trazas de longitud total a lo sumo `B`; por tanto

`1-s <= B`.

Si `B>=1`, ya se obtiene `a_i+B>=1`. Si `B<1`, la desigualdad anterior implica que
todo `s<1-B` debe pertenecer a `I_i`; de lo contrario la fibra `F_s` no podria estar
cubierta. Luego `[0,1-B) subset I_i`, y por tanto

`a_i >= 1-B`.

En ambos casos,

`a_1+a_2+a_3+t = a_i+B >= 1`.

QED.

### Consecuencia [PROVED]

El caso `3 facetas + 1 arbitrario` de `Bang(4)` queda cerrado sin invocar Bang(3).
Por la equivalencia logica de `notes/27`, esto tambien prueba el lema residual
`W_3` para triples de facetas:

si `P_i={lambda_i in I_i}`, `R=a_1+a_2+a_3<1`, y `F=Delta\(P_1 union P_2 union P_3)`,
entonces para toda `f:Delta->[0,1]` afin normalizada,

`span_f(F) >= 1-R`.

La prueba es por contradiccion: si `span_f(F)=L<1-R`, un plank adicional `{f in J}`
de longitud `L+epsilon` cubre `F`, y los cuatro planks tendrian suma menor que 1 para
`epsilon` pequeno, contradiciendo el teorema anterior.

---

## 2. `W_2` / `Bang(3)` por fibras [OPEN]

### Lo que sobrevive [PROVED]

Para dos planks `P_1={g_1 in I_1}`, `P_2={g_2 in I_2}` con suma `R<1`, la formulacion
correcta es:

`W_2` afirma que para todo target afin normalizado `f`, el libre

`F=Delta\(P_1 union P_2)`

satisface

`span_f(F) >= 1-R`.

Por `notes/27`, esto es equivalente a `Bang(3)` para el triangulo.

Subcasos cerrados sin Hunter:

- Si entre `P_1,P_2` y el target `f` hay solo dos direcciones efectivas, se reduce al
  teorema de dos direcciones.
- Si `P_1,P_2` y `f` tienen un borde activo comun, el borde da el argumento 1-D:
  el complemento de dos intervalos de longitud total `R` en `[0,1]` tiene diametro al
  menos `1-R`.
- Si `P_1,P_2` comparten borde activo `AB` y `f` es la coordenada de la faceta opuesta,
  escribiendo `g_i=y+s_i z`, cada fibra `z=z_0` tiene longitud `1-z_0` y los dos planks
  quitan longitud total a lo sumo `R`; para todo `z_0<1-R` queda punto libre.

### Obstruccion de pendiente [OPEN]

Si se intenta cerrar el target generico solo por trazas de borde, aparece el factor de
pendiente. Para una arista `E=[U,V]`, define

`delta_E(g)=|g(V)-g(U)|`.

La traza de `{g in I}` sobre `E` tiene longitud afin

`tau_E(g,I)=|I cap g(E)|/delta_E(g)`

si `delta_E(g)>0`.

Si una falla de `W_2` se cubre agregando `Q={f in J}`, `|J|=L`, entonces sobre `E`
solo se obtiene

`L >= delta_E(f) * (1 - tau_E(g_1,I_1) - tau_E(g_2,I_2))_+`.

En el borde comun de `g_1,g_2`, si el target es generico `f=z+s y`, entonces
`delta_E(f)=s`, y el borde solo fuerza

`L >= s(1-R)`,

no `L>=1-R`. Este factor `s` es la obstruccion concreta de `notes/28` §3.4.

### Candidato no bancado [CANDIDATE / NEEDS AUDIT]

El ataque paralelo sugirio que `W_2` podria valer cuando `P_1,P_2` comparten borde
activo y `f` es arbitrario. La parte para target con el mismo borde activo y para target
opuesto esta probada arriba. La rama generica requiere una compensacion global del
factor `s`; no se banca aqui como teorema hasta aislar un argumento que no reintroduzca
peeling a 3 planks.

---

## 3. Normalizador admisible [OPEN]

Para

`N_c(u)=(1-c) ell_K(u)+c w_K(u)`, `0<=c<=1`,

si se prueba la desigualdad de Bang fuerte

`sum width_i/N_c(u_i) >= 1`,

entonces se obtiene inmediatamente

`sum rw_i >= c+(1-c)*2/(1+sqrt(d))`,

mejorando Bakaev-Yehudayoff para todo `c>0`.

No hay refutacion barata de `c>0`: como `N_c<=w`, una cobertura con
`sum width_i/N_c(u_i)<1` implicaria `sum width_i/w(u_i)<1`, es decir, un contraejemplo
a Bang relativo.

### Test exacto propuesto

En el triangulo, normaliza una direccion como valores de vertices `(0,tau,1)`. Para
el triangulo equilatero,

`ell/w = 2(tau^2-tau+1)/(2-tau)` si `tau<=1/2`,

y

`ell/w = 2(tau^2-tau+1)/(1+tau)` si `tau>=1/2`,

con minimo `4*sqrt(3)-6`.

Para direcciones y placements dados, minimizar exactamente

`C_c=sum p_a/(c+(1-c) ell(u_a)/w(u_a))`

sujeto a cobertura. La cobertura se decide por las `2^m` celdas de signo y LP/Farkas
exacto, no por grilla. Una violacion con `C_c<1` refutaria ese `c`; una certificacion
uniforme daria el teorema del normalizador para el triangulo.

---

## 4. Prueba asistida para `m=3` [PLAN CERTIFICABLE]

El caso `m=3` debe atacarse antes que `m=4`.

Algoritmo minimo:

1. Normalizar cada direccion por una carta `u(e_p)=0`, `u(e_q)=1`, `u(e_r)=tau`,
   `tau in [0,1]`.
2. Escribir intervalos `I_i=[a_i,b_i]` y `R=sum(b_i-a_i)`.
3. Para cada signo `sigma in {-,+}^3`, resolver el LP de escape:
   maximizar `epsilon` con `x in Delta` y, para cada `i`, `f_i(x)<=a_i-epsilon`
   o `f_i(x)>=b_i+epsilon` segun `sigma_i`.
4. Cobertura equivale a que los 8 optimos sean `<=0`.
5. Enumerar bases activas de esos LPs; cada hoja produce condiciones semialgebraicas
   racionales en direcciones y endpoints.
6. Certificar cada hoja con Farkas exacto, Bernstein/SOS o CAD de baja dimension.

Estratos a separar analiticamente:

- direcciones coincidentes o dos direcciones efectivas;
- direcciones con borde activo comun;
- endpoints `a_i=0`, `b_i=1`, `a_i=b_i`;
- determinantes cero: fronteras paralelas, coincidencias, vertices de camara sobre
  `partial Delta`;
- collar de igualdad `R=1`.

Laguna exacta: cerca de `R=1`, el margen de escape se anula. La prueba asistida necesita
una estabilidad transversal: el cono tangente de las condiciones de cobertura no debe
contener una direccion con `dR<0`; si `dR=0`, el primer termino no nulo debe ser no
negativo salvo tangencias de la igualdad conocida.

---

## 5. Brecha de integralidad y transporte multimarginal [PROVED / OPEN]

### Lema de transporte positivo [PROVED]

Sea `mu` una medida positiva sobre `Delta` con marginales `f_{a#} mu <= dt` y masa `M`.
Si existe una dependencia positiva

`sum_a lambda_a g_a == C`, `lambda_a>=0`, `g_a in {f_a,1-f_a}`,

con `Lambda=sum_a lambda_a`, entonces

`M <= 2*min(C,Lambda-C)/Lambda`.

Prueba: para cualquier marginal `alpha<=dt` de masa `M`, el principio bathtub da

`M^2/2 <= int t d alpha(t) <= M-M^2/2`.

Aplicando esto a la dependencia positiva se obtiene la cota.

Para las tres facetas `x_1+x_2+x_3=1`, resulta `M<=2/3`, y la cota es sharp. Por tanto
el acoplamiento multimarginal positivo no puede dar masa 1 en el simplex facetario.

### Formulacion prometedora [OPEN]

El siguiente objeto evita el cap fraccionario: usar certificados enteros por celdas de
escape. Para cada `sigma in {0,1}^m`, define

`R_sigma={x in Delta: f_a(x)<=l_a si sigma_a=0, f_a(x)>=u_a si sigma_a=1}`.

Cobertura equivale a `R_sigma=empty` para todo `sigma`. Por Helly/Farkas en dimension 2,
cada vacio tiene certificado por un circuito de a lo sumo 3 semiplanos. El objetivo es
probar que no existe un etiquetado coherente de todas las celdas por tales circuitos si
`sum(u_a-l_a)<1`.

Este certificado seria entero, dependiente de posicion, de borde, y de tipo
"escape de todos".

---

## 6. Euler-Jacobi shifted [METHOD RESULT]

Para formas lineales desplazadas

`L_j(x)=<v_j,x>-m_j`, pesos `p_j>0`, `sum p_j=1`,

los criticos de

`Psi=1/2 ||x||^2 - sum_j p_j log|L_j(x)|`

satisfacen la identidad

`sum_crit mu(x) * (1 - sum_j p_j^2/L_j(x)^2) = 0`, con `mu>0`.

Un test polynomial explicito es

`g=sum_{i!=j} p_i p_j <v_i,v_j> prod_{l!=i,j} L_l - sum_i p_i m_i prod_{l!=i} L_l`.

Consecuencia: existe un critico con `|L_j(x)|>=p_j` para todo `j`, pero el punto no queda
forzado a pertenecer al simplex ni a la bola unidad.

Por eso no cierra `W_2/Bang(3)`: al imponer las facetas del simplex aparecen divisores
no monomiales; limpiar denominadores devuelve sistemas densos con degeneraciones en el
infinito. La opcion futura correcta seria usar residuos de arreglos de hiperplanos o
blow-ups, no EJ torico crudo.

---

## 7. Proximas opciones de exploracion

1. Actualizar `notes/26` para reemplazar el Caso 2 invalido por la prueba de fibras de
   esta nota.
2. Actualizar `notes/27` para marcar `W_3` facetario como probado usando esta nota, no
   Hunter.
3. Atacar `W_2` en el caso de borde activo comun y target generico; el objetivo exacto
   es compensar el factor de pendiente `s` con informacion de fibras interiores.
4. Implementar el certificador exacto `m=3` por LP/Farkas y aislar el collar `R=1`.
5. Ejecutar el test exacto para `N_c` en el triangulo y buscar el primer `c>0` viable.
6. Formalizar el certificado entero por circuitos de Farkas de las celdas de escape.

---

## 8. Continuacion tras la evaluacion de opciones [DRAFT]

> Status: borrador de trabajo. No contiene prueba nueva de `W_2/Bang(3)` ni de la
> conjetura completa. Separa consolidacion, avances reales, y tareas exactificables.

### 8.1 Consolidacion `3 facetas + 1` [PROVED]

La pieza matematica firme de esta ronda es el teorema de §1:

`3 facet planks + 1 arbitrary plank => sum rw >= 1`.

La prueba correcta es la de fibras `F_s={lambda_i=s}` y no usa Hunter/Bang(3). Esta
prueba debe tratarse como el enunciado canonico para el paper. Las notas `26` y `27`
ya tienen banners que apuntan a esta reparacion; si se reescriben, conviene eliminar
del cuerpo de esas notas cualquier prueba vieja que invoque Hunter sobre 3 planks.

Consecuencia reutilizable:

- `W_3` facetario queda probado: si `P_i={lambda_i in I_i}`, `R=sum |I_i|<1`, entonces
  para toda forma afin normalizada `f`, el libre de las tres facetas tiene
  `span_f >= 1-R`.

### 8.2 Normalizador `N_c` [OPEN / EXACT TEST]

Sea

`N_c=(1-c) ell + c w`, `q_c(u)=N_c(u)/w(u)=c+(1-c) ell(u)/w(u)`.

Entonces `q_c<=1` y

`width/N_c = rw/q_c >= rw`.

Por tanto, una violacion `sum width_i/N_c(u_i)<1` implicaria tambien
`sum rw_i<1`. Asi, un contraejemplo a `N_c` seria una configuracion sub-Bang. Esto
explica por que los tests aleatorios que solo confirman Bang no discriminan bien `c`.

La forma correcta de probar `c>0` no es repetir BY, sino demostrar un defecto sobre
la desigualdad fuerte de cuerdas. Es suficiente probar una desigualdad del tipo

`sum A_i - 1 >= sum A_i * (c beta_i)/(1+c beta_i)`,

donde

`A_i=width_i/ell_i`, `beta_i=w_i/ell_i - 1`.

En efecto,

`width_i/N_c = A_i/(1+c beta_i)`.

Asi, el programa del normalizador se reduce a controlar el defecto de la desigualdad
fuerte de BY en terminos de las direcciones donde `ell<w`.

Para el triangulo equilatero y una direccion normalizada por valores de vertices
`(0,tau,1)`, usar la formula de trabajo

`ell/w = 2(tau^2-tau+1)/(2-tau)` si `tau<=1/2`,

`ell/w = 2(tau^2-tau+1)/(1+tau)` si `tau>=1/2`,

con minimo `4*sqrt(3)-6`. Esta formula debe verificarse simbolicamente antes de usarla
en un certificado.

Test exactificable recomendado:

1. Fijar `m` direcciones `u_a=(0,tau_a,1)` modulo permutaciones.
2. Para endpoints `I_a=[l_a,u_a]`, comprobar cobertura por las `2^m` celdas de escape
   mediante LP exacto/Farkas.
3. Minimizar
   `C_c=sum_a (u_a-l_a)/q_c(tau_a)`
   sujeto a cobertura.
4. Una hoja de certificado debe ser un certificado Farkas para cada celda de escape,
   mas una prueba semialgebraica de `C_c>=1` sobre la caja de direcciones/endpoints.

Estado: no hay `c>0` probado todavia. La ruta barata sigue siendo correr primero el
test en direcciones fijas y plantillas degeneradas; si no aparece violacion numerica,
buscar el defecto BY anterior en esas plantillas.

### 8.3 `W_2` con borde activo comun y target generico [OPEN]

Modelo de trabajo:

`Delta={(y,z): y>=0, z>=0, y+z<=1}`,

`P_i={g_i in I_i}`, `g_i=y+a_i z`, `0<=a_i<=1`, `R=r_1+r_2<1`,

target `f=z+s y`, `0<s<1`.

Los subcasos firmes son:

- target con el mismo borde activo: argumento 1-D sobre `z=0`.
- target opuesto `f=z`: argumento de fibras horizontales, porque cada fibra `z=z_0`
  tiene longitud `1-z_0` y los dos planks eliminan longitud total `<=R`.
- dos direcciones efectivas: teorema de dos direcciones.

Para target generico, la traza sobre el borde comun solo da

`L >= s(1-R)`

al agregar un tercer plank `{f in J}` de longitud `L`; falta recuperar el factor
`(1-s)(1-R)` desde informacion interior. No se obtuvo una compensacion valida sin
reintroducir una forma disfrazada de Bang(3).

Lema exacto a atacar:

`span_{z+s y}(Delta \ (P_1 union P_2)) >= 1-r_1-r_2`

para `g_i=y+a_i z`. Este es el nucleo analitico manual mas prometedor para Bang(3),
pero sigue `[OPEN]`.

### 8.4 Certificador exacto para `m=3` [PLAN CERTIFICABLE]

El certificado correcto debe trabajar con celdas de signo, no con grillas.

Datos:

- Direcciones en cartas `u_a=(0,t_a,1)` modulo permutacion de vertices.
- Intervalos `I_a=[l_a,h_a]`, `r_a=h_a-l_a`, `R=sum r_a`.
- Celdas de escape `sigma in {-,+}^3`:

  `f_a(x)<=l_a` si `sigma_a=-`, y `f_a(x)>=h_a` si `sigma_a=+`.

Para cada `sigma`, resolver el LP de margen

`eta_sigma = max eta`

sujeto a `x in Delta` y las tres desigualdades de escape con margen `eta`.

Cobertura equivale a `eta_sigma<=0` para los 8 signos. Un certificado de cobertura
es una lista de certificados Farkas para esas 8 afirmaciones.

Plantillas:

- vertices de `Delta`;
- interseccion de lado de `Delta` con frontera de plank;
- interseccion de dos fronteras de planks;
- degeneraciones: direcciones coincidentes, endpoints `0/1`, intervalos degenerados,
  fronteras paralelas o triples.

Cuello exacto:

El collar `R=1` tiene margen cero. El modulo analitico debe probar estabilidad
transversal: el cono tangente de las condiciones `eta_sigma<=0` a lo largo del estrato
de igualdad no contiene direccion con `dR<0`; si `dR=0`, el primer termino no nulo debe
ser no negativo o tangente al estrato de igualdad. Sin esto, el refinamiento por
intervalos nunca termina cerca de `R=1`.

Primer prototipo recomendado:

generar automaticamente todos los candidatos de vertices de celdas para tres direcciones
fijas, calcular `eta_sigma` por LP racional, y emitir la base activa/Farkas dual. Esto no
prueba el teorema, pero produce las plantillas que luego se certifican por Bernstein/CAD.

### 8.5 Circuitos de Farkas [STRUCTURAL / OPEN]

Para cada celda de escape

`R_sigma=Delta cap halfspaces(sigma)`

vacia, Farkas/Helly en dimension 2 da un certificado por un circuito de a lo sumo tres
semiplanos activos. La idea estructural es etiquetar las `2^m` celdas por tales circuitos
y probar que no existe un etiquetado coherente si `sum r_a<1`.

Este objeto cumple las cuatro propiedades buscadas:

- entero/combinatorio: elige circuitos por celda;
- dependiente de posicion: usa endpoints `l_a,h_a`;
- de borde: los circuitos pueden involucrar lados de `Delta`;
- escape-de-todas: trabaja con celdas de escape simultaneo.

Estado: no hay todavia una desigualdad global que combine los circuitos y fuerce
`sum r_a>=1`. El primer caso a cerrar es `m=3`, donde hay 8 celdas y circuitos de
maximo 3 semiplanos.

### 8.6 Secuencia actualizada

1. Correr el test `N_c` en plantillas fijas y registrar solo evidencia numerica como tal.
2. En paralelo, atacar el lema `W_2` de borde activo comun + target generico.
3. Implementar el generador de bases/Farkas para `m=3`.
4. Usar la salida del generador para buscar la estabilidad transversal en `R=1`.
5. Mantener circuitos de Farkas como linea estructural de fondo.
