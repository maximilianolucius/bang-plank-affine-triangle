# Nucleo convergente: Bang en direcciones BALANCEADAS (facetas + medianas)

> Date: 2026-06-30. Status: LIVE / INCREMENTAL.
> Las notas 32-33-34 convergen a un unico objetivo duro y bien definido. Esta nota lo
> aisla y lo ataca. Etiquetas `[PROVED]`/`[OPEN]`/`[EVIDENCE]`.

---

## 0. Convergencia (de donde venimos) y baseline resuelto

- **No hay holgura generica** (nota 33): direcciones genericas de 3 aristas distintas
  tambien teselan ajustado (`Sum rw=1`); no hay region facil. Verificado exacto, sin
  contraejemplo.
- **`N_c(c>0)` se cierra <=> Bang en teselaciones BALANCEADAS no-faceta** (nota 34): el
  caso binding de `S_c>=1` son las direcciones con `rho=1`, i.e. `tau in {0,1/2,1}`;
  facetas (`tau in {0,1}`) ya probadas, **medianas (`tau=1/2`) no**. Ejemplo canonico: la
  teselacion **tercio-central simetrica** (`I_i=[1/3,2/3]`, 3 medianas).
- **Herramienta candidata**: el certificado de **6 celdas de escape mixtas**
  (nota 33 §6), ya verificado para ese ejemplo (cada celda: 1 arista de `Delta` + 2 caras
  de plank, pesos `{1/2,2/3,1/3}`).

**Baseline RESUELTO (B-Y 2026).** `S_0 = sum width_i/ell_i >= 1` es el **Lema 5** de
Bakaev-Yehudayoff (`sum opt(P_i)/ell_K(u_i) >= 1`). Luego `c=0` esta **probado** y da
`Sum rw >= min rho = 4 sqrt3 - 6 ~ 0.928` (**NO** es el Teorema 8 de B-Y, que es el general
`2/(1+sqrt(d))=0.828`; el `0.928` es **consecuencia del Lema 5 de B-Y** `sum width/ell >= 1`
aplicado al `min ell/w` del triangulo equilatero — lo derivan ellos, no es un teorema con nombre).
Cualquier `c>0` probado lo bate estrictamente.

---

## 1. La reduccion EXACTA (que hay que probar para `c>0`)

Sea `rho_i = ell_i/w_i` (formula verificada nota 34 §1), `q_c(tau)=c+(1-c)rho`,
`S_c = sum rw_i/q_c(tau_i)`. Define la **perdida-c**:

`L_c := S_0 - S_c = sum_i rw_i (1/rho_i - 1/q_c(tau_i)) = sum_i rw_i * c(1-rho_i)/(rho_i q_c(tau_i)) >= 0`

(verificado con `sympy`). Como B-Y da `S_0 >= 1`,

`S_c >= 1  <=>  (S_0 - 1) >= L_c`,

es decir: **la holgura de B-Y (`S_0-1`) debe dominar la perdida-c (`L_c`)**.

**Clave:** ambos lados se anulan exactamente cuando todas las direcciones activas son
balanceadas (`rho_i=1`): ahi `L_c=0` (sin perdida) y `S_0-1 = Sum rw - 1 = 0` en una
teselacion. Por tanto la desigualdad `S_c>=1` es **tight precisamente en el conjunto de
igualdad de B-Y = teselaciones balanceadas**. Probar `N_c(c>0)` es probar que la holgura
de B-Y domina la perdida-c **cerca de las teselaciones balanceadas** (condicion
transversal/local en el conjunto de igualdad de B-Y).

Esto unifica las tres notas: el objeto a entender es **B-Y en su conjunto de igualdad =
direcciones balanceadas (facetas + medianas)**.

---

## 2. P-A´: el conjunto de igualdad balanceado [EVIDENCE exacta]

Direcciones **balanceadas** (`rho=1`, `tau in {0,1/2,1}`) = **6 lineas**: 3 paralelas a
aristas (facetas, `tau in {0,1}`) + 3 paralelas a **medianas** (`tau=1/2`):
`mA=(1/2,0,1)`, `mC=(0,1,1/2)`, `mB=(1,1/2,0)`.

`min Sum r` EXACTO (grid con bordes `l=0`) por terna de direcciones balanceadas:
- **3 facetas** `xA,xB,xC`: `=1` (Hunter; familia 2-parametros `t1+t2+t3=1`). [PROVED]
- **3 medianas** `mA,mC,mB`: `=1` (la **tercio-central** `I_i=[1/3,2/3]`, `r_i=1/3`).
  **EVIDENCIA de rigidez** (parece la unica teselacion mediana, a diferencia de la familia
  2-param de Hunter): fijando `r1=3/10`, grid exacto `N=60` y NelderMead continuo dan
  `min Sum r ~ 1.05` y NO encuentran teselacion; barrido de `r1` da `~1.05` salvo en
  `r1=1/3` (`~1.0`).
  **CAVEAT (leccion nota 33):** grid/NM dan **cota SUPERIOR** del min; "no tesela en
  `r1!=1/3`" necesita una cota INFERIOR (argumento exacto), aun **pendiente**. Por ahora es
  evidencia fuerte de rigidez, no prueba.
- **`2F+1M`**: `=1` -- **tesela genuinamente** (familia rica; auditoria: 10 r-triples
  no-degenerados, `r_i>=1/6`). Exacto.
- **`1F+2M`**: ~~`=1`~~ **CORRECCION 2026-06-30 (auditoria):** es **FALSO/overclaim**.
  La esencial (`r_i>=1/6`) da `min Sum r = 13/12 > 1`; el `=1` previo era el **artefacto
  del plank unico** (un plank de ancho 1 cubre `Delta`) -- exactamente la trampa de
  degeneracion que `notes/33` §2 documento y en la que esta nota recayo. **NO hay
  teselacion 1F+2M no-degenerada;** se descarta como caso de igualdad.

Conclusion P-A´ (corregida): el conjunto de igualdad de `S_c` (= de B-Y) son las
**teselaciones en las 6 direcciones balanceadas**, problema de Bang de **direcciones
FINITAS**. Casos tight genuinos no-faceta: **solo 3-medianas (rigida) y 2F+1M (familia)**;
`1F+2M` NO. `inf S_c = 1` se alcanza solo ahi (consistente con nota 34).

---

## 3. P-A: Bang en las 6 direcciones balanceadas, y que falta para `N_c`

### 3.1 El blanco contenido [OPEN, atacable]

**Bang para coberturas en las 6 direcciones balanceadas** (3 aristas + 3 medianas). Es
finito -> set-cover exacto por celdas de escape + Farkas. Estado:
- facetas-solo: **probado** (faceta-paralelo, certificado baricentrico `+++`, nota 32).
- mediana (tercio-central): certificado de **6 celdas mixtas** (nota 33 §6) ya verificado
  para el. SI es rigida (evidencia §2), bastaria UN certificado (no familia); confirmar
  rigidez (cota inferior) es parte del trabajo. **Atacado en `notes/36` (via transporte).**
- `2F+1M` (familia): nuevo; baricentrico para 2 facetas + celdas mixtas para la mediana.
  (`1F+2M` NO aplica: no tesela, §2.)

Cerrarlo daria el **primer caso tight no-faceta de Bang(3)** (las teselaciones mediana/
mixtas), citable por si mismo.

### 3.2 Honestidad: balanceado NO basta para cerrar `N_c` [MATIZ]

Probar "Bang en balanceadas" (3.1) es **necesario pero NO suficiente** para `N_c(c>0)`.
Por §1, `S_c>=1 <=> S_0-1 >= L_c` para TODA cobertura. En las balanceadas ambos lados son
0 (tight). Para coberturas NO balanceadas hace falta la **condicion cuantitativa**
`S_0 - 1 >= L_c` (la holgura de B-Y domina la perdida-c). B-Y solo da `S_0-1 >= 0`, no la
cota cuantitativa. Numericamente `S_c>=1` se cumple en todas partes (min `S_c=1` solo en
balanceadas, nota 34), asi que la condicion **es cierta**; **probarla** requiere la
estructura de la holgura de B-Y cerca de su conjunto de igualdad (internos del **Lema 5**
de B-Y). Esa es la pieza analitica real, no solo "Bang en balanceadas".

### 3.3 Plan

1. **Generalizar el certificado de 6 celdas** de la tercio-central a la familia mediana/
   mixta -> probaria Bang en las 6 direcciones balanceadas (3.1). Set finito -> factible.
2. **Leer B-Y Lema 5** y extraer la holgura `S_0-1` como funcion de la "no-balanceza"
   (`1-rho_i`) cerca del conjunto de igualdad; verificar la condicion transversal
   `S_0-1 >= L_c` (3.2). Esto es lo que cierra `N_c(c>0)` y bate 0.928.
3. **P-C en paralelo** (higiene): re-verificar grilla de notas 28/30/31 con motor exacto.

> Sub-resultados limpios de esta nota: (i) la reduccion EXACTA `S_c>=1 <=> S_0-1>=L_c`
> (verificada con `sympy`); (ii) el conjunto de igualdad balanceado = teselaciones en 6
> direcciones finitas (facetas 2-param + mediana + mixtas, todas con `Sum r=1` exacto);
> (iii) EVIDENCIA (no prueba) de que la teselacion mediana es rigida/aislada. Scripts
> inline + `exp_w2_delta.py`, `exp_w2_C.py`.
