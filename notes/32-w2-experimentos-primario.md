# Experimentos hacia un SUBCASO de Bang(3): W_2 de borde activo comun

> **[SCOPING — CRITICO]** `W_2` de **borde activo comun** es un **SUBCASO ESTRICTO** de
> Bang(3), NO Bang(3). Tres planks arbitrarios pueden tener sus tres aristas activas
> distintas; ahi ningun par comparte borde activo y este modelo no aplica. Cerrar
> `W_2`-borde-comun **NO cierra Bang(3)**. (Es exactamente el salto que causo el incidente
> Hunter; se mantiene la distincion explicita.) Bang(3) general se ataca en `notes/33`
> (modelo sin arista comun).
>
> Date: 2026-06-30. Status: LIVE / INCREMENTAL.
> Programa EXP-A..E (objetivo: probar `W_2` de borde activo comun = subcaso real de
> Bang(3)). Aritmetica exacta (`fractions`) donde corre localmente; backend numerico
> (`numpy/scipy`) en venv `.venv` para EXP-C/D. Toda evidencia numerica se marca como
> evidencia, nunca como prueba.
>
> Modelo (de `notes/31` §2): `Delta=(y,z)` vertices `A=(0,0),B=(1,0),C=(0,1)`. Borde
> activo comun `z=0` (arista `AB`). Formas por valores en vertices `(vA,vB,vC)`,
> normalizadas (min 0, max 1). `g1=(0,1,a1)`. DOS orientaciones del borde comun:
> - **SAME**: `g2=(0,1,a2)` (= la del shear `g_i=y+a_i z` de nota 31 §2.4);
> - **OPP**: `g2=(1,0,a2)` (orientacion opuesta; contiene la config de Hunter).
> `a_i in {0,1}` <=> `g_i` de faceta. Target `f=(0,s,1)` (`s in {0,1}` <=> faceta).
> Objetivo exacto: `span_f(Delta \ (P1 U P2)) >= 1 - r1 - r2`.
>
> **HALLAZGO transversal:** el shear de nota 31 §2.4 solo captura SAME (ambos `g`
> crecientes en el borde); el caso ajustado/duro vive tambien en OPP. El motor general
> sobre `Delta` (no el shear) cubre ambos.

---

## EXP-A. Estructura extremal exacta de `W_2` (racional) [HECHO]

### Motor exacto (validado)

`experiments/exp_w2_delta.py`: motor de span sobre `Delta=(y,z)` con formas afines dadas
por valores en vertices `(vA,vB,vC)`, planks `P_i={g_i in [l_i,h_i]}`, y
`span_f(Free)` por **recorte de poligonos** (Sutherland-Hodgman exacto, `fractions`):
el libre es la union de <=4 celdas convexas (complemento de cada tira ∩ `Delta`);
las celdas degeneradas (area 0) se descartan. Exacto y robusto.

> **Bug corregido (importante):** una version previa contaba vertices de plank-frontera
> (p.ej. `C=(0,1)` con `l1=0`) como libres, inflando el span a 1 y ocultando los casos
> ajustados. El metodo de recorte lo corrige. Validacion: sin planks `span=1`; config
> de Hunter (`g1=x_B`, `g2=x_A`, `f=x_C`, `I_i=[0,t_i]`) da `span=1-R` con `gap=0` exacto.

Dos sub-modelos de borde activo comun `z=0` (ambos necesarios; antes solo se modelaba el
primero, que es el "facil"):
- **SAME** (misma orientacion en el borde): `g1=(0,1,a1)`, `g2=(0,1,a2)`.
- **OPP** (orientacion opuesta): `g1=(0,1,a1)`, `g2=(1,0,a2)`. Contiene la config de
  Hunter (`a1=a2=0`, target `f=x_C`).
`a_i in {0,1}` <=> `g_i` paralelo a faceta. Target `f=(0,s,1)`; `s in {0,1}` <=> `f`
paralelo a faceta.

### Resultado 1 -- sin contraejemplo, envolvente ajustada `1-R` [EVIDENCE exacta]

Busqueda EXACTA (`fractions`) sobre **115.337** configuraciones (ambas orientaciones,
`(a1,a2,s)` y placements racionales): **0 gaps negativos, 0 FREE_EMPTY**, `min gap = 0`
(alcanzado). Es decir, en el modelo de borde comun `span_f(F) >= 1-R` se cumple sin
contraejemplo y `1-R` es la **envolvente ajustada exacta** (no mejorable). Evidencia
exacta fuerte, no prueba.

### Resultado 2 -- LOCUS extremal = "al menos una direccion de faceta" [EVIDENCE]

`experiments/exp_w2_locus.py` (min gap por direccion). Para **target generico**
`s in (0,1)`: una direccion `(a1,a2,s)` admite config ajustada (`gap=0`) **si y solo si
al menos una de `g1,g2` es paralela a faceta** (`a1 in {0,1}` o `a2 in {0,1}`). Si
`a1,a2 in (0,1)` (ambos planks NO-faceta) hay **holgura estricta** `gap>0` en todo
placement. Para **target de faceta** `s in {0,1}` el locus ajustado es mayor.

Interpretacion (clave para la prueba): los casos **extremales** de `W_2` borde comun
siempre involucran un elemento paralelo a faceta entre `{g1,g2,f}`. El caso totalmente
generico (los tres no-faceta) tiene holgura -> es el "facil". Esto conecta el caso duro
con la maquinaria de facetas ya probada (`notes/30` §1, fibras).

### Resultado 3 -- patrones de vertices testigo (plantilla) [EVIDENCE]

`experiments/exp_w2_search.py`. En el caso faceta-ajustado (`a1=a2=0`, `s=0`, Hunter),
los testigos `(argmin | argmax)` caen en tres estratos:
- `min @ A=(0,0)`  |  `max @ arista y=0` (la arista activa del target);
- `min @ arista z=0` (arista comun)  |  `max @ arista y+z=1`;
- `min @ arista z=0`  |  `max @ interior` (cruce de fronteras de plank).
En todos, `inf_F f = 0` (el target alcanza su minimo en un punto libre).

---

## EXP-B. Cota acoplada sup-inf y regimen `inf>0` [HECHO parcial]

- **Envolvente verdadera:** `span_min(a1,a2,s) = 1-R` exacto (Resultado 1). No hay cota
  intermedia mejor que `1-R` de forma uniforme; la holgura es estrictamente positiva
  salvo en el locus de faceta.
- **Regimen `inf_F f > 0`:** ~9% de las configuraciones muestreadas (origen `A` y arista
  comun cubiertos). Es el subcaso "esquina" de `notes/31` §2.3. En el muestreo, estas
  NO son las mas ajustadas: cuando `inf_F f>0`, el `sup` sube por el mecanismo de vaciado
  de fibras altas (nota 31 §2.3) y el gap se mantiene `>0`. Las configuraciones ajustadas
  (`gap=0`) tienen `inf_F f=0`.
- **Consecuencia para cerrar `W_2` borde comun:** basta tratar el locus extremal
  (≥1 direccion de faceta). Sub-rutas:
  - `f` de faceta (`s in {0,1}`): target es coordenada de faceta -> argumento de fibras
    tipo `notes/30` §1 con el target como facet-plank.
  - `g_i` de faceta (`a_i in {0,1}`): "1 facet plank + 1 plank general + target";
    es un caso de "facetas + general" atacable por fibras.
  - ambos `g` no-faceta: holgura estricta -> no extremal (queda por cuantificar la
    holgura como margen positivo).

Archivos: `experiments/exp_w2_delta.py` (motor), `exp_w2_search.py` (mapa tight/inf),
`exp_w2_locus.py` (locus). Evidencia exacta donde se indica; el resto, evidencia float.

---

## EXP-C. Certificador de celdas de escape + Farkas (`m=3` borde comun) [HECHO]

`experiments/exp_w2_C.py` (scipy HiGHS para el LP de margen + duales; certificados clave
verificados EXACTO con `fractions`).

### Construccion

3 planks `i`: forma `g_i` y `[l_i,h_i]`. Un punto NO cubierto cae en alguna celda de
escape `R_sigma`, `sigma in {-,+}^3` (`g_i<=l_i` si `-`, `g_i>=h_i` si `+`). Cobertura
<=> las 8 celdas vacias. LP de margen por celda: `max t` con `x in Delta` y los escapes
con holgura `t`; `t*<0` => celda vacia (cubierta con margen), `t*=0` => binding.

### Resultado 1 -- la celda gobernante es `+++`, certificado baricentrico [PROVED-template]

Para los planks de faceta `P1={x_B in[0,t1]}`, `P2={x_A in[0,t2]}`, `Q={x_C in[0,t3]}`,
la celda `+++` `={x_B>=t1, x_A>=t2, x_C>=t3}`. Como `x_A+x_B+x_C=1` (identidad
baricentrica), el certificado de Farkas con multiplicadores `(1,1,1)` da

`(x_A-t2)+(x_B-t1)+(x_C-t3) = 1-(t1+t2+t3)`,

luego `R_{+++}` es vacia `<=>` `t1+t2+t3 >= 1`. Verificado EXACTO: en `sum=1` el valor
del certificado `1-sum=0` (la celda degenera al **punto de teselado de Hunter**, margen
`t*=0`); `sum>1 =>` vacia; `sum<1 =>` no vacia (no cubre). Las demas celdas, con planks
anclados en `0`, son vacias por las aristas de `Delta`. Conclusion: para la familia de
faceta, **cobertura `<=> R >= 1`**, y el unico certificado necesario es la identidad
baricentrica sobre la celda `+++`. Este es precisamente el certificado "entero /
de-borde / escape-de-todas" que el dossier (`notes/23` E) buscaba, realizado en el locus
extremal.

### Resultado 2 -- `min Sum r = 1` exacto sobre el locus extremal [EVIDENCE exacta]

`min` de `Sum r` sobre coberturas (motor exacto), target `f=x_C` (`s=0`):
- `(a1,a2)=(0,1/3)`, `(1/3,0)`, `(1/2,1/4)` [ambos `g` NO-faceta], `(0,0)`: **todos dan
  `min Sum r = 1`** exacto. Es decir, Bang(3) es ajustado (`=1`) en el locus extremal,
  tambien cuando los planks de borde comun no son de faceta pero el target si.

### Resultado 3 -- collar `R=1` y estabilidad transversal [EVIDENCE]

En el caso de faceta, el valor del certificado de la celda `+++` es `1-R`, que cruza `0`
**linealmente** en `R=1` (margen `t*` proporcional a `1-R`). No hay tangencia: el estrato
de igualdad se atraviesa transversalmente, justamente la condicion que pedia
`notes/30` §8.4 para el collar `R=1` en esta familia.

### Lo que queda [OPEN]

Para `g1,g2` NO-faceta y target generico (`s in (0,1)`): EXP-A mostro holgura estricta;
las celdas binding ya no son `+++` sino combinaciones con aristas (`-+-`, `-++`, ...). El
certificado global que combine las 8 celdas para forzar `Sum r >= 1` en ese regimen con
holgura sigue pendiente (pero por EXP-A ese regimen NO es extremal).

---

## EXP-D. Peor cover para `N_c` (competitivo) [BLOQUEADO: falta definir `ell(u)`]

EXP-D requiere la funcion normalizadora `ell(u)` del triangulo. **Auditoria:** en el
repo NO existe una definicion precisa de `ell(u)`; solo la "formula de trabajo" de
`notes/30` §8.2 (`ell/w = 2(tau^2-tau+1)/(2-tau)`, etc.), marcada como *a verificar*.
He verificado su **minimo** (`4 sqrt(3)-6` en `tau=2-sqrt(3)`) pero NO la formula en si,
porque no hay definicion de `ell`. Para no fabricar, EXP-D queda **bloqueado** hasta:
1. fijar la definicion de `ell(u)` (probablemente de Bakaev-Yehudayoff 2026: longitud de
   cuerda / normalizador que da `2/(1+sqrt d)`), y
2. verificar simbolicamente la formula `ell/w` para el triangulo equilatero.

Nota: los resultados de `notes/31` §1 (sandwich `S_1<=S_c<=S_0`, rigidez de igualdad,
buffer de primer orden) usan SOLO `ell<=w` y siguen validos sin la formula. Lo que el
`ell` explicito habilita es el test cuantitativo del mayor `c>0` admisible.

---

## EXP-E. Circuitos de Farkas (`m=3`) [PARCIAL via EXP-C]

EXP-C ya realiza el programa de circuitos: cada celda de escape vacia tiene un
certificado de Farkas con `<=3` restricciones activas (aristas de `Delta` + caras de
plank). En el locus extremal, la incompatibilidad global cuando `R<1` es simplemente que
la celda `+++` se vuelve no vacia (certificado baricentrico). El etiquetado coherente
global de las 8 celdas que fuerce `Sum r>=1` en el regimen NO-faceta (con holgura) queda
`[OPEN]`, consistente con que ese regimen no es extremal.

---

## Sintesis del programa EXP (hacia probar `W_2` = Bang(3) borde comun)

- Motor exacto validado (`exp_w2_delta.py`); **sin contraejemplo** en 115k configs
  exactas; envolvente ajustada `1-R`.
- **Locus extremal = al menos una direccion de faceta** entre `g1,g2,f` (EXP-A). El caso
  totalmente generico tiene holgura estricta.
- En el locus extremal, certificado de Farkas **baricentrico** sobre la celda `+++`
  (EXP-C), con `min Sum r = 1` exacto y collar `R=1` transversal.
- Plan de prueba: (i) cerrar el locus de faceta por fibras/baricentrico (caso duro pero
  estructurado); (ii) acotar la holgura estricta del caso generico como margen positivo.
- EXP-D (N_c competitivo) bloqueado por falta de `ell(u)` verificado; no se fabrica.

Archivos canonicos: `exp_w2_delta.py` (motor por recorte), `exp_w2_search.py`,
`exp_w2_locus.py`, `exp_w2_C.py`. (Los `exp_w2_shear/_A/_A2/_fast` quedaron obsoletos por
el bug de frontera; eliminados.)
