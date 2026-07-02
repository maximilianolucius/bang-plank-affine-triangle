# P-A1: Bang para las 3 direcciones MEDIANAS -- PROBADO (primer tight no-faceta)

> Date: 2026-06-30 (rigidez cerrada 2026-07-01). Status: **THEOREM [PROVED]** — cota
> `Sum r >= 1` (transporte) **+ rigidez COMPLETA** (igualdad sii `I_i=[1/3,2/3]`, ver
> `notes/45`). Es el **primer caso tight NO-faceta de Bang(3) con rigidez**, citable por si
> solo. Prueba por transporte con una medida EXPLICITA.

---

## 0. Setup y estructura

Las 3 direcciones **medianas** (`tau=1/2`, balanceadas `rho=1`), como formas afines sobre
`Delta = {(y,z): y,z>=0, y+z<=1}` (vertices `A=(0,0),B=(1,0),C=(0,1)`):

`m1 = 1/2 - y/2 + z/2`   (valores en `A,B,C`: `1/2, 0, 1`),
`m2 = y + z/2`           (`0, 1, 1/2`),
`m3 = 1 - y/2 - z`       (`1, 1/2, 0`).

Cada `m_i: Delta -> [0,1]` (normalizada). Plank `P_i = {m_i in I_i}`, `I_i=[l_i,h_i]`,
`r_i=|I_i|` (= ancho relativo, `w=1`).

**Identidad estructural [PROVED]:** `m1 + m2 + m3 = 3/2` sobre todo `Delta` (verificado
`sympy`). Es el analogo baricentrico de `Sum x_i = 1` de las facetas (alli la suma es 1).

**Auto-similaridad [PROVED]:** la imagen `T = Phi(Delta)`, `Phi=(m1,m2,m3)`, es un
triangulo en el plano `Sum m = 3/2` con vertices los 3 vectores mediana
`(1/2,0,1),(0,1,1/2),(1,1/2,0)`; y las formas `m_i` restringidas a `T` son **de nuevo las
medianas de `T`** (valores de vertice = perm de `{0,1/2,1}`). El problema "cubrir por
medianas" es auto-similar.

---

## 1. TEOREMA (Bang en medianas) [PROVED]

**Teorema.** Si los 3 planks medianos `P_i = {m_i in I_i}` cubren `Delta`, entonces
`r_1 + r_2 + r_3 >= 1`.

### Prueba (transporte con medida explicita del perimetro)

Sea `mu` la medida de probabilidad sobre `Delta` dada por **uniforme-en-parametro sobre
las 3 aristas, peso `1/3` cada una**:

- arista `AB`: puntos `(t,0)`, `t~U[0,1]`, masa `1/3`;
- arista `CA`: puntos `(0,t)`, `t~U[0,1]`, masa `1/3`;
- arista `BC`: puntos `(t,1-t)`, `t~U[0,1]`, masa `1/3`.

**Afirmacion:** la marginal de `mu` por cada mediana es Lebesgue uniforme en `[0,1]`:
`(m_{i#} mu) = dt`.

*Prueba de la afirmacion* (exacta, para `m1`; las otras igual):
- `AB`: `m1 = 1/2 - t/2 in [0,1/2]`, `|dt/dm1|=2` -> densidad `(1/3)*2 = 2/3` en `[0,1/2]`.
- `CA`: `m1 = 1/2 + t/2 in [1/2,1]`, densidad `2/3` en `[1/2,1]`.
- `BC`: `m1 = 1 - t in [0,1]`, `|dt/dm1|=1` -> densidad `1/3` en `[0,1]`.
- Total: en `[0,1/2]`: `2/3 + 1/3 = 1`; en `[1/2,1]`: `2/3 + 1/3 = 1`. Densidad `= 1`
  uniforme, masa total `1`. QED afirmacion.
(Verificado numericamente: marginales planas, max desv `8e-4` con `6e5` muestras; y exacto
por las densidades arriba para `m1`,`m2`,`m3`.)

**Conclusion.** Para `I_i subset [0,1]`, `mu(P_i) = (m_{i#}mu)(I_i) = Leb(I_i) = r_i`
(y `<= r_i` si `I_i` se sale de `[0,1]`). Si los planks cubren `Delta`:

`1 = mu(Delta) = mu(union P_i) <= sum_i mu(P_i) <= sum_i r_i`.

Luego `sum r_i >= 1`. **QED.**

### Comentarios

- Es la primera prueba de Bang para un triple de direcciones **no-faceta** sobre el
  triangulo (las medianas, `tau=1/2`). El metodo es transporte/acoplamiento (estilo
  teorema de 2-direcciones AKP/Strassen) pero con una **medida testigo explicita**.
- La medida del perimetro es **singular** (vive en `dim 1`); por eso da la **cota**
  `Sum r>=1` pero NO directamente la rigidez (que necesita el caso de igualdad).
- Conexion con la cota de transporte de `notes/30` §5: alli el cap multimarginal de
  facetas era `2/3`; aqui la medida del perimetro logra marginal uniforme **plena**
  (masa 1) en las 3 medianas, dando la cota `1` (ajustada).

---

## 2. Rigidez (caso de igualdad) [PROVED — completo; ver notes/45 (R2-2)]

> **[ACTUALIZADO 2026-07-01 — `notes/45` (R2-2).]** Rigidez **PROBADA completa** (ya no
> `[OPEN]`): (1) igualdad ⟹ partición del perímetro (edge-tiling); (2) enumeración simbólica
> exacta (`sympy`) de los 27 patrones de cruce × órdenes ⟹ el edge-tiling tiene **exactamente 3**
> soluciones `[1/3,2/3]³, [0,1/3]³, [2/3,1]³`; (3) las dos últimas **no cubren el centroide**
> `G` (`m(G)=(½,½,½)`, `½∉[0,⅓]∪[⅔,1]`), luego la única cobertura con `Σr=1` es la
> tercio-central. Sin grid. (Corrección: espacio de longitudes 3-dim; se excluye el cover
> degenerado `r_i=0`.) Detalle: `notes/43-P4` + `notes/45`.

`Sum r = 1` requiere igualdad en `1 <= sum mu(P_i)`: (i) `I_i subset [0,1]` (sin
desperdicio) y (ii) los `P_i` **particionan el perimetro** `mu`-c.t.p. (disjuntos en
`mu`). La teselacion **tercio-central** `I_i=[1/3,2/3]` lo cumple (`Sum r=1`).

Hecho concreto (apoya rigidez): en la tercio-central, **cada arista se parte en tercios
exactos** por los 3 planks. P.ej. en `AB` (`(t,0)`, `t in [0,1]`): `P1={m1 in[1/3,2/3]}`
cubre `t in [0,1/3]`, `P2` cubre `[1/3,2/3]`, `P3` cubre `[2/3,1]` -- particion perfecta
(`Sum=1` en cada arista). Por simetria igual en `BC`, `CA`.

**Rigidez [PROVED — `notes/45`, R2-2].** "Particion del perimetro (3 trazas medianas tilean
`[0,1]` en cada arista) + cobertura del interior fuerza `I_i=[1/3,2/3]`" quedo **probado**
(no por grilla): la enumeracion simbolica exacta (`sympy`) de los 27 patrones de cruce x todos
los ordenes da **exactamente 3** edge-tilings — `[1/3,2/3]³, [0,1/3]³, [2/3,1]³` — y solo la
tercio-central cubre el **centroide** (`m(G)=(1/2,1/2,1/2)`); las otras dos teselan el borde
pero dejan `G` sin cubrir. Unico cover con `Sum r=1` = tercio-central. Ver `notes/45` +
`notes/43-P4`. (La evidencia de grilla de `nota 35 §2` queda como confirmacion redundante.)

---

## 3. Implicaciones

- **P-A1 cota: HECHA** (`Sum r>=1` en medianas, probado). Junto con facetas (probado), son
  2 de los 3 tipos de direcciones balanceadas; falta **2F+1M** (P-A2).
- **Primer tight no-faceta de Bang(3): logrado** como cota; rigidez pendiente.
- **Para `N_c` (batir B-Y):** sigue faltando la pieza cuantitativa `S_0-1 >= L_c` de
  coberturas NO balanceadas (nota 35 §3.2). Probar Bang en balanceadas (incl. esto) es
  necesario pero no suficiente; el transporte aqui NO la da (es la cota `=1`, no la
  cuantificacion de la holgura de B-Y).
- **Posible generalizacion:** el transporte prueba Bang para CUALQUIER triple de
  direcciones que admita una medida con marginales uniformes simultaneas. Las medianas y
  los `<=2` casos lo admiten; mapear "que triples lo admiten" es una linea nueva (¿coincide
  con el locus tight de nota 33?).

---

## 4. Proximos pasos

1. **Rigidez mediana** (cota inferior): analisis 1-D de la particion del perimetro por las
   3 trazas medianas. Cierra P-A1 completo (cota + rigidez).
2. **P-A2 (2F+1M):** baricentrico (2 facetas) + transporte/celdas (1 mediana). ¿Hay medida
   testigo para 2F+1M? (probablemente, mezcla perimetro + baricentrico).
3. **P-B (la pieza que bate B-Y):** cuantificar holgura del Lema 5 de B-Y vs `L_c`
   (nota 35 §3.2). Independiente del transporte.
4. **P-C** higiene en paralelo.

Scripts: `exp_w2_delta.py`, verificacion de `mu` inline (medida del perimetro).
Identidad `Sum m=3/2`, auto-similaridad y marginales: `sympy`/`numpy` exacto.
