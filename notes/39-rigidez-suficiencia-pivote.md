# P-A1″ (rigidez mediana), P-SUF (suficiencia), higiene y pivote

> Date: 2026-06-30. Status: rigidez [REDUCED/EVIDENCE]; suficiencia [OPEN, evidencia
> fuerte]; higiene [DONE]. Cierra la fase de transporte; marca el pivote a P-B / certificado.

---

## 0. Higiene aplicada (correcciones de auditoria)

- `notes/38` §1: "surface=tight REFUTADA" -> **OPEN** (triple C `min Sum r ~1.0005` es cota
  superior >1; no se demuestra tight). Lo firme: off-surface EXISTE => transporte insuficiente.
- `notes/33` (banner): "no hay holgura generica" usaba cotas superiores; **on-surface tight
  exacto, off-surface AMBIGUO**. Firme = sin contraejemplo (9891) + tight en la superficie.
- `notes/38` §2.1: la condicion de media es `sum a_i = 2 kappa` (**suma CON SIGNO**), no
  `sum|a_i|` (difieren en signo mixto).

---

## 1. P-A1″: rigidez de la teselacion mediana [REDUCED + EVIDENCE fuerte]

**Meta:** probar que una cobertura mediana con `Sum r=1` fuerza `I_i=[1/3,2/3]`.

### 1.1 Evidencia exacta
Busqueda EXACTA de teselaciones medianas (`Sum r=1`) en grilla `/24` (con bordes):
**exactamente UNA** -- la tercio-central `I_i=[1/3,2/3]`. (Grilla incluye `1/3,2/3`.)
Fuerte evidencia de unicidad; falta cerrar el continuo.

### 1.2 Reduccion rigurosa a particion del perimetro
Por la prueba de transporte (`notes/36`), igualdad `Sum r=1` <=> los 3 planks
**particionan el perimetro** `mu`-c.t.p. (cada punto de `partial Delta` en exactamente un
plank) Y cubren `Delta`. En cada arista, las 3 trazas tilean `[0,1]` (el parametro).

Rangos de los `m_i` por arista (verificado):
- `AB`: `m2` recorre `[0,1]` (pleno), `m1` `[0,1/2]`, `m3` `[1/2,1]`.
- `BC`: `m1` pleno, `m2` `[1/2,1]`, `m3` `[0,1/2]`.
- `CA`: `m3` pleno, `m1` `[1/2,1]`, `m2` `[0,1/2]`.

Con `a_i=|I_i cap [0,1/2]|`, `b_i=|I_i cap [1/2,1]|` (`r_i=a_i+b_i`), las **ecuaciones de
longitud de la particion** (cada arista suma 1):

`(AB): r2 + 2 a_1 + 2 b_3 = 1`
`(BC): r1 + 2 b_2 + 2 a_3 = 1`
`(CA): r3 + 2 b_1 + 2 a_2 = 1`

(Su suma da `Sum r + 2 Sum(a_i+b_i) = 3`, i.e. `1+2=3`, automatica.) La tercio-central
(`a_i=b_i=1/6`) las cumple. Son **necesarias** pero **no suficientes**.

> **[CORRECCION 2026-06-30 — auditoria.]** Dos precisiones:
> - **Dimension:** son **3 ecuaciones** independientes en **6 variables** (`a_i,b_i`); el
>   espacio de soluciones de longitud es **3-dimensional**, no 2-dim (la cuarta relacion
>   `Sum r=1` es automatica, no independiente). La version previa decia "2-dim".
> - **Cobertura interior:** las ecuaciones de longitud + el **cierre posicional** (las 3
>   trazas deben ABUTAR en cada arista, no solo sumar bien) controlan **solo el perimetro**;
>   falta ademas exigir la **cobertura del interior** de `Delta`, que es una condicion
>   separada NO capturada por las ecuaciones de arista. La rigidez completa es: (longitud) +
>   (cierre posicional en las 3 aristas) + (cobertura interior). Es un **CSP finito** sobre
>   6 parametros, atacable exacto, pero mas grande que "1-D sobre las 3 aristas".

### 1.3 Estado
Rigidez **reducida** a un CSP finito posicional + evidencia exacta de unicidad. **No
cerrada** rigurosamente aqui. El **teorema de medianas** queda:
- **COTA `Sum r>=1`: PROBADA** (`notes/36`, medida del perimetro). [firme, citable]
- **Igualdad (rigidez): evidencia fuerte + reducida** al CSP de particion; pendiente cerrar.

---

## 2. P-SUF: suficiencia de `cond=2` [OPEN, evidencia fuerte] -- time-boxed

**Meta:** `cond=2` + `p` interior `=>` existe medida de marginal uniforme (=> teorema de
familia).

### 2.1 Reduccion y lo que esta garantizado
Relacion `sum a_i u_i = 1` (`a=(V^T)^{-1}1`). Pedir 3 uniformes <=> acoplar `u_1,u_2`
uniformes con `S=a_1u_1+a_2u_2` uniforme.
- **Media:** `sum a_i = 2` = `cond`. [necesario, PROBADO]
- **Varianza (a>0):** realizable sii `|a_i|` triangular; **AUTOMATICO** para `cond=2`
  interior (**373/0** violaciones -- confirma auditoria). NO es obstruccion extra.
- **Hueco REAL:** que `S` sea **plenamente uniforme** (momentos >=3), no solo media+var.

### 2.2 Obstaculos
- **Signo mixto:** hay pasadoras con `a=(2,-2,2)` (`sum a=2`, `sum|a|=6`); el argumento de
  varianza (regimen `a>0`) no aplica directo, pero la medida existe (LP). Falta forma general.
- **Sin construccion limpia:** el **perimetro de peso constante FALLA** para pasadoras
  genericas (funciona SOLO para medianas, verificado); la medida generica es singular
  interior+borde, sin forma cerrada. Kellerer = el LP (evidencia 453/453, no prueba).

### 2.3 Veredicto time-box
Suficiencia **fuertemente soportada** (media+var garantizadas; LP/Kellerer robusto) pero
**abierta** -- reducida a la uniformidad plena de `S` (existencia analitica de 3-marginales
fuera de medianas). Es un **moonshot** (Kellerer analitico con relacion afin). **Se banca
como conjetura bien fundada**; no bloquea.

---

## 3. Pivote estrategico (rol de jefe de research, reconocido)

El **transporte esta minado a su limite**. Contribucion real y firme:
- **PROBADO:** Bang para medianas (medida explicita), y la **caracterizacion necesaria**
  `cond=2`/concurrencia de `{u_i=1/2}` (nota 37).
- **Conjetural (evidencia fuerte):** Bang en toda la superficie de concurrencia (codim-1).
- **Fuera del alcance del transporte (PROBADO):** las ternas off-surface (medida positiva,
  el grueso de Bang(3)) -- ahi single-measure esta MUERTO (nota 37 §2 necesidad).

Frontera de mayor valor ahora (NO capada por el limite del transporte):
1. **P-B (batir B-Y, 0.928):** la pieza cuantitativa `S_0 - 1 >= L_c` del **Lema 5 de
   B-Y** (`notes/35` §3.2). Independiente, competitiva, citable aunque Bang(3) no caiga.
2. **Certificado combinatorio / integralidad** (notas 23 E, 30 §5/§8.5; celdas de escape /
   Farkas): la unica via candidata para el grueso **off-surface**.

---

## 4. Proximos pasos

1. **P-B (prioridad competitiva):** obtener/reconstruir la prueba del **Lema 5 de B-Y** y
   extraer su holgura `S_0-1` como funcion de la no-balanza `(1-rho_i)`; testear
   `S_0-1 >= L_c`. Si cierra, `Sum rw >= c+(1-c)0.928` (bate B-Y). Requiere el paper B-Y.
2. **Certificado off-surface:** retomar celdas de escape/Farkas (notas 30/33 §6) como la
   herramienta para el grueso; el patron de 6 celdas mixtas es el lead estructural.
3. **P-A1″ cierre (opcional, bajo riesgo):** resolver el CSP posicional 1-D de §1.2 para
   completar la rigidez mediana (teorema completo cota+igualdad).
4. **P-SUF (moonshot):** Kellerer analitico; no bloqueante.

Scripts inline (busqueda exacta de teselaciones, triangular, signo mixto, perimetro);
motor `exp_w2_delta.py`.
