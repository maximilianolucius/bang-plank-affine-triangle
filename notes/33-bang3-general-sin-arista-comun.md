# Bang(3) general (sin arista comun) -- ¿se generaliza la dicotomia del locus?

> **[MATIZ 2026-06-30, de notas 37/38]** La conclusion §4/§5 "NO hay holgura generica /
> Bang es tight en esencialmente todas las direcciones" usaba `min Sum r` de
> grilla/optimizador continuo, que son **cotas SUPERIORES** del min. Por tanto:
> - "on-surface" (concurrencia, `cond=1^TV^-1 1=2`, p.ej. la simetrica/medianas): tight
>   **exacto** (`Sum r=1` con teselacion exhibida). FIRME.
> - "off-surface" (`cond != 2`, p.ej. triple C `2.022`): `min Sum r ~ 1.0005` es cota
>   superior -> **AMBIGUO** (tight o holgura pequena, no decidido). La afirmacion "todas
>   tight" es por tanto **evidencia, no establecida** para off-surface.
> El resultado firme se reduce a: sin contraejemplo (`Sum r<1`) exacto en 9891 configs; y
> tight exacto en la superficie de concurrencia.
>
> Date: 2026-06-30. Status: LIVE / EVIDENCE (no prueba).
> Modelo P3 del jefe de research: TRES planks con direcciones ARBITRARIAS sobre el
> triangulo `Delta` (no necesariamente con arista activa comun). Este es el escenario de
> Bang(3) **de verdad**; `notes/32` (W_2 borde comun) es un subcaso estricto.
>
> Motor: `experiments/exp_w2_delta.span_free` (recorte de poligonos, validado; el bug de
> frontera ya esta corregido). Las busquedas amplias son float (por velocidad), pero los
> resultados clave estan **verificados EXACTO** (`fractions`): no-contraejemplo (9891
> configs generales), la teselacion simetrica `Sum r=1`, y el argumento 1-D §4.5. Toda
> afirmacion es **evidencia numerica / observacion estructural, no prueba** de Bang(3).

---

## 1. Modelo y reduccion

Direcciones `u_i` = formas afines normalizadas por valores en vertices `(vA,vB,vC)`,
`min=0, max=1`. Arista activa de `u` = arista entre `argmin` y `argmax`. FACET <=> dos
valores de vertice iguales (`tau in {0,1}`). Generica (no-faceta) <=> tres valores
distintos (arista activa unica y bien definida).

**Reduccion (usa el motor de span):** para direcciones fijas,
`min Sum r sobre coberturas = min_{l1,r1,l2,r2} [ r1 + r2 + span_{u3}(Delta\(P1 U P2)) ]`,
porque el ancho minimo `r3` que cubre el libre residual es exactamente su `u3`-span.
`min Sum r` es simetrico, asi que fijar `u3` como "target" es WLOG.

---

## 2. CAVEAT de degeneracion (decisivo)

La cobertura **degenerada** por un solo plank de ancho 1 (`P3={u3 in [0,1]}=Delta`,
`r1=r2=0`) da `Sum r = 1` para CUALQUIER direccion. Por tanto `inf Sum r = 1`
trivialmente para toda terna, y "min Sum r = 1" sin restriccion **no dice nada** sobre
extremalidad. La pregunta con contenido es por coberturas **no degeneradas** (todos los
planks esenciales): se impone `r_i in [eps, 1-eps]`.

(Este caveat invalida una primera medicion que daba "100% tight" — era el artefacto del
plank unico. Registrado para honestidad.)

---

## 3. Sin contraejemplo

En todas las corridas, **0 eventos de `Sum r < 1`**. Verificacion **EXACTA** (`fractions`)
para 3 direcciones ARBITRARIAS: 9891 configuraciones, `min Sum r = 1`, ninguna `<1`.
(Complementa las 115k exactas de borde comun en `notes/32`.) Evidencia exacta consistente
con Bang(3); no es prueba.

---

## 4. ¿Hay holgura generica? NO -- autocorreccion (artefacto de grilla)

### 4.1 Lo que parecia (grilla gruesa) -- DESCARTADO

Una primera medicion por grilla (`exp_bang3_edges.py`, `N=20-24`, `eps=0.12`) sugeria que
las teselaciones esenciales ajustadas vivian solo en `#aristas=1`, con holgura en
`#aristas=2,3`:

```
#aristas | min(grilla N=24) | mediana | ajustadas(<1.01)
   1     | 1.000            | 1.000   | 100%
   2     | 1.012            | 1.055   | 0%
   3     | 1.020            | 1.067   | 0%
```

**Esto era un ARTEFACTO de grilla.** El `min` por grilla es **cota superior** del `min`
verdadero; al refinar, baja. Para la terna "C" `(0.45,0,1),(0,1,0.45),(1,0.55,0)`:
`min Sum r` = `1.0417 (N=24) -> 1.017 (N=32) -> 1.025 (N=40)` y, con optimizador continuo
(Nelder-Mead, esencialidad dura): **`1.0005`**. La "holgura `~4%`" se evapora.

### 4.2 Lo correcto (continuo + EXACTO): no hay holgura generica

- **Config simetrica de 3 aristas distintas** `u1=(1/2,0,1), u2=(0,1,1/2), u3=(1,1/2,0)`
  **TESELA EXACTO** con `I_i=[1/3,2/3]` (`r_i=1/3`), `Sum r = 1` exacto (`gap=0`,
  verificado con `fractions`), todos los planks esenciales y NO degenerados. Es la
  teselacion "tercio central" simetrica.
  > **[MATIZ 2026-06-30 — auditoria #4]** Este **unico ejemplo exacto** son **precisamente las
  > 3 medianas** (`tau=1/2`, balanceadas `rho=1`, `cond=1^TV^-1 1=2`, ON-surface): es el caso
  > probado en `notes/36`, **NO** una direccion generica. Por tanto **NO** sostiene por si solo
  > "tight en esencialmente TODAS las direcciones": lo firme es tight-exacto ON-surface
  > (medianas) + sin contraejemplo; el resto (generico OFF-surface, p.ej. triple C) es cota
  > superior AMBIGUA, no tight establecido. Ver `notes/37 §2`, `notes/38 §1`.
- Terna C: `min Sum r esencial ~ 1.0005` (continuo) -> ajustada dentro de tolerancia.

**Conclusion corregida:** las direcciones GENERICAS de 3 aristas distintas **tambien
admiten teselaciones ajustadas no degeneradas** (`Sum r = 1`). **No existe holgura
generica explotable.** Bang(3) es **ajustado (tight) en esencialmente todas las
direcciones** (facetas, borde comun, Y genericas como la simetrica). El conjunto de
igualdad es rico (consistente con la caracterizacion amplia `T=1` de Hunter).

> Leccion de proceso: nunca concluir "holgura" de un `min` por grilla (es cota superior).
> Verificar con optimizador continuo + exacto. La holgura reportada en una version previa
> de esta nota era falsa; corregida aqui.

### 4.5 Por que `#aristas=1` es ajustado: argumento 1-D [PROVED]

Si las tres direcciones comparten la **misma arista activa** `E` (cada `g_i` recorre
`[0,1]` sobre `E`), entonces la traza de `P_i` sobre `E` es un intervalo de longitud
`<= r_i` (porque `g_i|_E` es una biyeccion afin `E -> [0,1]`). Cubrir `Delta` exige
cubrir `E`, y cubrir `E` por intervalos de longitud total `<= Sum r_i` exige

`Sum r_i >= 1`.

Luego `#aristas=1` => `Sum r >= 1` **trivialmente** (argumento 1-D sobre la arista comun),
y es ajustado teselando `E`. **No es un caso profundo.** (Generaliza el argumento de borde
ya usado en `notes/30`/`notes/26`.) Conclusion: la tightness de `#aristas=1` es trivial;
el caso tight NO trivial es el de **facetas** (Hunter, ya probado por faceta-paralelo /
baricentrico de `notes/32` EXP-C), donde la cobertura la fuerza `Sum x_i=1` (2-D), no una
arista.

---

## 5. Veredicto de scoping (responde la pregunta del jefe de research)

1. **La dicotomia "extremal => >=1 faceta" NO se generaliza.** En el modelo general,
   direcciones genericas (3 aristas activas distintas, sin faceta) **tambien admiten
   teselaciones ajustadas** `Sum r = 1` (p.ej. la simetrica tercio-central, §4.2, exacta).
2. **Tampoco hay holgura generica explotable** (la sospecha de §4.1 era artefacto de
   grilla, §4.2). Bang(3) es **ajustado en esencialmente todas las direcciones**.
3. **Mapa de los casos tight de Bang(3)** (corregido):
   - `#aristas=1` (arista comun): tight pero **trivial** (1-D, §4.5) [PROVED].
   - **facetas / Hunter**: tight, **ya probado** (faceta-paralelo / baricentrico).
   - **generico (incl. simetrica tercio-central)**: tight, y **NO probado** — es parte del
     mismo problema duro. No hay region "facil".
4. **Sigue en pie la reserva #1, reforzada:** cerrar `W_2` borde-comun NO cierra Bang(3),
   y ademas **no da ninguna ventaja** (el caso generico es igual de ajustado; no hay
   holgura que herede). `W_2` borde-comun (`#aristas=2`) no es extremal ni un peldano con
   holgura. La igualdad de Bang(3) es un conjunto rico (Hunter `T=1`), no concentrado en
   facetas.

---

## 6. Implicacion estrategica (honesta)

- **La via "holgura/dicotomia" esta muerta** como atajo a Bang(3): no hay region generica
  con margen. Bang(3) es tight en todo el espacio de direcciones.
- Particion vigente de Bang(3):
  - **degenerado** (un plank ~cubre): reduce a W_1/W_2.
  - **`#aristas=1`**: trivial (1-D, §4.5) [PROVED].
  - **facetas**: probado (baricentrico).
  - **resto (generico, incl. simetrico)**: **abierto y duro**, sin holgura.
- Nuevas familias tight concretas para estudiar el certificado de igualdad:
  **tercio-central simetrica** `I_i=[1/3,2/3]` con `u` simetricas — teselacion exacta no
  faceta. Certificado de escape-cells verificado (`exp_w2_C.py` extendido): a diferencia
  del caso faceta (celda `+++`, baricentrico `(1,1,1)`), aqui **NO** binden `+++`/`---`;
  binden las **6 celdas mixtas**, cada una con **1 arista de `Delta` + 2 caras de plank**,
  pesos `{1/2, 2/3, 1/3}`. Es un certificado **mas rico** (arista+caras), no baricentrico
  puro. Entender este patron de 6 celdas mixtas es el camino hacia el certificado general
  de igualdad de Hunter `T=1`.
- **Reevaluacion de prioridades:** dado que no hay atajo por holgura, la jugada de payoff
  seguro **P4 (N_c, batir B-Y)** sube de prioridad relativa frente a perseguir el subcaso
  borde-comun. Bang(3) pleno requiere el certificado de igualdad general (Hunter `T=1`),
  que es el muro conocido.

---

## 7. Proximos pasos

1. **Generalizar el certificado de 6 celdas mixtas** (ya obtenido para la simetrica, §6):
   entender por que binden las 6 celdas con pesos `{1/2,2/3,1/3}` y si el patron
   "arista + 2 caras" se extiende a la familia tight no-faceta general (camino a Hunter `T=1`).
   Es el primer certificado tight NO trivial y NO faceta.
2. **Re-verificacion exacta** (P5): hecho parcialmente (9891 configs generales exactas,
   `min Sum r=1`, sin contraejemplo). Ampliar malla antes de citar en escrito.
3. **P5 (contaminacion):** re-correr las afirmaciones "sin contraejemplo" por grilla de
   `notes/28,30,31` con el motor de clipping/optimizador continuo; retirar las basadas en
   grilla gruesa (esta nota muestra por que: la grilla miente sobre `min`).
4. **P4 (N_c, remoto):** fijar `ell(u)` de B-Y, verificar formula `ell/w`, buscar mayor
   `c>0`. Sube de prioridad: es el camino citable que no depende de romper Hunter `T=1`.

Archivos: `experiments/exp_bang3_general.py` (artefacto degenerado, conservado como
leccion), `exp_bang3_essential.py` (esencialidad por #facetas), `exp_bang3_edges.py`
(eje correcto: #aristas activas), `exp_bang3_epssweep.py` (barrido eps).
