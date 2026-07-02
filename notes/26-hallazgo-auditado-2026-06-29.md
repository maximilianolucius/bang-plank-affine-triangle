# Hallazgo auditado (2026-06-29)
> Status global: PARTIAL. No resuelve el residual completo m>=4 con >=4 direcciones tilted efectivas.
> Todo lo que sigue esta etiquetado como [PROVED] u [OPEN].
>
> **[CORRECCION CRITICA 2026-06-30 — auditoria]** El Teorema B usa "Hunter (3 planks en
> triangulo => Sigma rw >= 1)", pero Hunter NO probo eso (solo 2 planks + la
> caracterizacion de igualdad; el caso de 3 planks esta ABIERTO — Verreault, B-Y 2026).
> Por tanto:
> - **Teorema A [PROVED]**: sigue VALIDO (argumento 1-D sobre el borde comun; no usa Hunter).
> - **Teorema B, Caso 1 (`0 notin I1,I2,I3`) [PROVED]**: VALIDO (argumento de borde E12).
> - **Teorema B, Caso 2 (`0 in I_i`)**: la prueba ORIGINAL (via Hunter) era INVALIDA.
>   **REPARADO 2026-06-30**: `notes/30` §1 da una prueba COMPLETA y sin Hunter (argumento
>   de fibras `F_s={lambda_i=s}`) que cubre AMBOS casos de una sola vez. Por tanto el
>   ENUNCIADO del Teorema B es CORRECTO y queda **[PROVED] via notes/30 §1**.

---

## Setup comun [PROVED]

Trabajamos en
`Delta = {x in R^3 : x_i >= 0, x_1+x_2+x_3=1}`.

Cada plank se escribe como
`P_j = {x in Delta : f_j(x) in I_j}`,
donde `f_j: Delta -> [0,1]` es afin con rango total `[0,1]`,
`I_j` es un intervalo, y `r_j := |I_j| = rw_Delta(P_j)`.

Para planks de faceta,
`P_i = {lambda_i in I_i}`, `a_i := |I_i|`.

---

## Teorema A (subfamilia con borde activo comun) [PROVED]

### Enunciado

Supongamos que existe un borde `E=[v_a,v_b]` tal que para todo `j`:
`f_j(v_a)=0` y `f_j(v_b)=1`.

Si `Delta subset union_j P_j`, entonces
`sum_j r_j >= 1`.

### Prueba

Parametrizamos `E` por `x(t)=(1-t)v_a+t v_b`, `t in [0,1]`.
Como `f_j` es afin y toma valores `0,1` en los extremos de `E`,
`f_j(x(t))=t`.

Luego
`P_j cap E = {x(t): t in I_j}`.
En la coordenada afin `t`, su longitud es `|I_j|=r_j`.

Del cubrimiento `E subset union_j (P_j cap E)` se obtiene un cubrimiento de
`[0,1]` por los intervalos `I_j`; por tanto
`1 <= sum_j |I_j| = sum_j r_j`.
QED.

### Nota metrica [PROVED]

La igualdad anterior usa longitud en la coordenada `t` del borde.
En longitud euclidea sobre `E`, cada traza mide `|E|*r_j`; la desigualdad es
la misma tras dividir por `|E|`.

---

## Teorema B (m=4, tres facetas + un plank arbitrario) [PROVED]

### Enunciado

Sean
`P1={lambda1 in I1}`, `P2={lambda2 in I2}`, `P3={lambda3 in I3}`,
`a_i:=|I_i|`;
y un cuarto plank arbitrario
`P4={f in J}`, `t:=|J|=rw_Delta(P4)`.

Si
`Delta subset P1 union P2 union P3 union P4`,
entonces
`a1+a2+a3+t >= 1`.

### Prueba

#### Caso 1: `0 notin I1, I2, I3` [PROVED]

Relabelamos vertices (y por simetria indices de faceta) para tener
`f(v1)=0`, `f(v2)=1`.
Sobre `E12=[v1,v2]`, `f|_{E12}` es biyectiva afina sobre `[0,1]`, asi que
`|P4 cap E12|_aff = t`.

Como `lambda3=0` en `E12` y `0 notin I3`, se tiene `P3 cap E12 = empty`.
Las otras trazas tienen longitudes afines
`|P1 cap E12|_aff = a1`, `|P2 cap E12|_aff = a2`.

Del cubrimiento de `E12`:
`a1+a2+t >= 1`.
Luego, sumando `a3>=0`,
`a1+a2+a3+t >= 1`.

#### Caso 2: `0 in I_i` para algun `i` [PROVED]

La prueba original por homotecia + Hunter era invalida, porque invocaba el caso de
3 planks del triangulo. El caso queda ahora demostrado por el argumento de fibras de
`notes/30-tier1-reenfoque-hallazgos.md`, que en realidad cubre los dos casos de una
sola vez. Lo registramos aqui en la forma especializada.

Sin perdida de generalidad, elegimos un borde activo de `f` y lo orientamos como

`f(v_j)=0`, `f(v_k)=1`,

siendo `v_i` el vertice opuesto. Escribimos `theta=f(v_i)`.

Para `s in [0,1]`, consideramos la fibra

`F_s={lambda_i=s}`

y la parametrizamos por `u=lambda_k in [0,1-s]`; entonces

`lambda_j=1-s-u`,

`f|_{F_s}(u)=theta s+u`.

En esa fibra:

- `P_i cap F_s=F_s` si `s in I_i`, y es vacio si `s notin I_i`.
- `P_j cap F_s` tiene longitud a lo sumo `a_j`.
- `P_k cap F_s` tiene longitud a lo sumo `a_k`.
- `P4 cap F_s` tiene longitud a lo sumo `t`.

Sea `B=a_j+a_k+t`. Si `s notin I_i` y la fibra esta cubierta, la longitud total
`1-s` de `F_s` no puede exceder `B`, o sea

`1-s <= B`.

Si `B>=1`, ya tenemos `a_i+B>=1`. Si `B<1`, la desigualdad anterior implica que todo
`s<1-B` debe pertenecer a `I_i`, pues de otro modo la fibra `F_s` quedaria sin cubrir.
Luego `[0,1-B) subset I_i`, y por tanto

`a_i >= 1-B`.

En ambos casos,

`a1+a2+a3+t = a_i+B >= 1`.

QED.

---

## Alcance exacto

- [PROVED] Teorema A: cualquier numero de planks, siempre que compartan el mismo
  borde activo (`0->1`) en sus formas normalizadas.
- [PROVED] Teorema B: `m=4` con tres planks paralelos a facetas y un cuarto
  plank arbitrario.
- [OPEN] El residual completo: `m>=4` con `>=4` direcciones tilted efectivas,
  sin hipotesis extra de borde comun ni estructura 3+1.

---

## Relacion con notas previas

Esto extiende el caso simetrico de
`notes/25-theorem-3plus1-symmetric.md`.
No contradice el estado OPEN documentado en
`notes/24-m4-research-deliverable.md`.
