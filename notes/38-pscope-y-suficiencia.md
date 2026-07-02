# P-SCOPE (alcance del transporte) y ataque a la suficiencia (P-A1´-suf)

> Date: 2026-06-30. Status: P-SCOPE **[DECIDIDO]**; suficiencia **[OPEN, evidencia fuerte]**.
> Continuacion de `notes/37`. Responde a la auditoria: delimita el metodo de transporte y
> ataca la suficiencia (el crux para un teorema de familia).

---

## 1. P-SCOPE: la superficie de concurrencia es una rebanada estricta [DECIDIDO]

Pregunta: ¿la superficie `cond=2` (concurrencia) = el locus tight completo, o estrictamente
menor? Calculo de `cond = 1^T V^{-1} 1` y `min Sum r` (continuo) para ternas tight de
`notes/33`:

```
terna                         cond     ¿on surface?   min essential Sum r
triple C (33)                 2.0223   OFF            ~1.0005   (casi tight)
symmetric / medianas          2.0000   ON             ~1.0000   (tight exacto)
generic 3-edge a              2.0000   ON             ~1.0003
generic 3-edge b              1.9677   OFF            ~1.0277   (holgura ~0.028)
random gen                    2.0000   ON             ~1.0615
```

**Conclusiones:**
- **Existen ternas OFF-surface** (`cond != 2`): triple C (`2.022`), generic-b (`1.968`).
  La superficie `cond=2` es **codimension 1** (1 ecuacion) -> **medida cero** en el espacio
  3-dim de ternas. El transporte (una sola medida) alcanza **solo esta rebanada**.
- **¿La superficie es el locus tight completo? [OPEN]** triple C esta OFF-surface con
  `min Sum r ~ 1.0005` (**cota SUPERIOR** > 1) -- compatible con holgura genuina O con
  tight. **NO se demuestra que triple C sea tight.** (Correccion de auditoria: la version
  previa decia "surface=tight REFUTADA"; es un **overstatement** -- queda **ABIERTO** si el
  locus tight contiene estrictamente la superficie; haria falta una terna off-surface
  *genuinamente* tight, o probar off-surface `<=>` holgura.)
- **Lo que SI es riguroso:** off-surface EXISTE (`cond != 2`), y off-surface `=>` **no hay
  medida uniforme** (nota 37 §2, necesidad PROBADA). Esto basta para la conclusion de scope,
  independiente de la tightness.

**Respuesta al auditor:** la familia de concurrencia es una **rebanada codim-1**, NO casi
todo el locus tight. **Bang(3) general necesita estrictamente mas que una sola medida**
(las ternas off-surface, incl. casi-tight como triple C, no las alcanza el transporte).

---

## 2. P-A1´-suf: ataque a la suficiencia [OPEN, evidencia fuerte]

Objetivo: probar que `cond=2` + `p` interior `=>` existe medida con marginal uniforme en
las 3 direcciones (lo que convierte "Bang para la familia de concurrencia" en teorema).

### 2.1 Reduccion tipo Strassen + restriccion lineal

De la relacion `sum a_i u_i = 1` (normalizada; `a = (V^T)^{-1} 1`), `u_3` es funcion afin
de `(u_1,u_2)`. Pedir las 3 uniformes equivale a:

> acoplar `u_1, u_2` (marginales uniformes) tal que `S := a_1 u_1 + a_2 u_2` sea uniforme
> en `[1-a_3, 1]` (longitud `a_3`).

- **Media:** `E[Sum a_i u_i]=kappa` (constante). Uniforme => `sum a_i * (1/2) = kappa` =>
  `sum a_i = 2 kappa` (SUMA CON SIGNO; con `kappa=1`, `sum a_i = 2`). Es exactamente `cond`.
  (Correccion: NO es `sum|a_i|`; para signo mixto difieren, ver abajo.)
- **Varianza (regimen `a_i>0`):** `Var(S)=a_3^2/12` requiere
  `Cov(u_1,u_2)=(a_3^2-a_1^2-a_2^2)/(24 a_1 a_2)`, realizable (`Cov in [-1/12,1/12]`) **sii
  `|a_i|` cumplen la desigualdad triangular**. **Hallazgo (verificado):** para `cond=2` con
  `p` interior, la desigualdad triangular es **automatica** (373/0 violaciones) -- NO es una
  obstruccion extra.
- **Signo mixto [caveat de auditoria]:** hay pasadoras con `a` de signo mixto (p.ej.
  `a=(2,-2,2)`, `sum a=2`, `sum|a|=6`), donde el argumento "intervalo de longitud `a_3`" no
  aplica directo -- y sin embargo la medida existe (LP). Asi §2.1 es analisis parcial
  (regimen `a>0`); el general (signo mixto) requiere otra forma.
- **Distribucion completa:** falta que `S` sea uniforme (no solo media+varianza). Es un
  problema de 3-marginales sobre el cuadrado `(u_1,u_2)` -- mismo tipo, no resuelto. Es el
  UNICO hueco real (momentos superiores).

### 2.2 Kellerer = el LP de factibilidad

Existencia de la medida `<=>` condicion de Kellerer: para toda `(phi_1,phi_2,phi_3)`,
`sum phi_i(u_i(x)) >= 0` en `Delta` `=>` `sum integral phi_i >= 0`. El **dual del LP de
factibilidad** de `notes/37` ES esta condicion discretizada. La factibilidad
**453/453** (robusta a `K=10..25`) es evidencia fuerte de que Kellerer se cumple en toda
la superficie interior. Pero es discretizada -> **no es prueba**.

### 2.3 Obstaculo a la construccion explicita

La medida testigo del LP para una pasadora **generica** es **singular y complicada**: ~34
puntos de soporte, **24 interior + 10 borde**, en ~20 direcciones distintas desde `p`. **No**
es el perimetro (que sirve solo para medianas) ni una curva simple reconocible. Asi que:
- **medianas:** construccion explicita limpia (perimetro, `notes/36`). ✓
- **pasadoras genericas:** sin construccion explicita; el soporte LP es un vertice disperso,
  podria existir una medida AC mas suave, pero no se exhibio.

### 2.4 Estado

Suficiencia **fuertemente soportada** (LP/Kellerer 453/453 robusto; medias+varianza OK con
desigualdad triangular) pero **NO probada**. El crux es la existencia analitica del
3-marginal (uniforme) sobre `Phi(Delta)` fuera del caso simetrico. Opciones:
1. Teorema de Kellerer/Strassen analitico para 3 marginales uniformes con relacion afin
   `Sum a_i u_i = 1`, `Sum a_i = 2` (la condicion). Probar que media+(triangular) basta.
2. Construccion por "barrido" (familia de segmentos) que uniformice las 3 direcciones.

---

> **[ACTUALIZADO 2026-06-30 — `notes/43-P3`, fuente primaria Gardner 1988.]** Se testeó la
> hipótesis del jefe de research "`1ᵀV⁻¹1=2` = criterio de Gardner para 3 direcciones":
> **NO**. El resultado **positivo** de Gardner (Thm 1) está capado a **≤2 direcciones**; el caso
> de finitas **≥3** direcciones es su pregunta **explícitamente abierta**. La suficiencia de
> `cond=2` (medianas/concurrencia) vive en ese hueco abierto — probarla sería un criterio
> positivo **nuevo** para 3 direcciones, no un corolario de Gardner. Sigue `[OPEN]`.

## 3. Sintesis y recomendacion honesta

- **P-SCOPE decidido:** transporte = rebanada codim-1; Bang(3) general necesita mas. Esto
  **acota el metodo**: util para una familia (publicable si se prueba §2), no para todo Bang(3).
- **Suficiencia:** evidencia fuerte, prueba abierta. Es un problema de existencia de
  3-marginales (Kellerer) -- puede ser genuinamente dificil fuera de medianas.
- **Valor seguro ya en mano:** (i) Bang para medianas PROBADO (nota 36, con medida
  explicita); (ii) la **caracterizacion** `cond=2`/concurrencia [necesaria PROBADA]; (iii)
  el mapa de alcance (codim-1).
- **Reevaluacion:** si la suficiencia general resulta dura, el resultado citable solido es
  **nota 36 (medianas) + la caracterizacion necesaria (nota 37)**; la "familia entera"
  queda como conjetura bien fundada. La via competitiva **P-B (B-Y, batir 0.928)** sigue
  independiente y no depende de esto.

---

## 4. Proximos pasos

1. **Suficiencia (§2):** intentar el teorema de Kellerer para el caso afin
   (`Sum a_i u_i=1`, `Sum a_i=2`, triangular); o una construccion por barrido. Alto riesgo.
2. **Rigidez mediana** (P-A1´´): cierra el teorema completo de medianas (cota+igualdad) --
   bajo riesgo, citable.
3. **P-B** (independiente): `S_0-1 >= L_c` via Lema 5 de B-Y -- la via que realmente bate B-Y.
4. **Revisar `notes/33`:** matizar "no hay holgura generica" -- las cotas eran superiores;
   on-surface es tight exacto, off-surface es ambiguo (triple C casi-tight, generic-b ~0.028).

Scripts inline (cond, relacion `a_i`, soporte LP); motor `exp_w2_delta.py`.
