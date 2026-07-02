# P1 (FLAGSHIP) — Batir Bakaev–Yehudayoff vía `N_c`: análisis riguroso y el requisito exacto

> Date: 2026-06-30. Status: **NO cerrado**. Se establece rigurosamente (i) la reducción
> exacta, (ii) que "el caso peligroso = casi-contraejemplo de Bang", (iii) el análisis local
> de primer orden, (iv) que la **Ruta A del jefe de research es un callejón sin salida** y solo
> la **Ruta B** (Lema 5 cuantitativo) puede funcionar, con el requisito preciso. No se fabrica
> un teorema. Fuentes: `refs/2602.20290` (B-Y), `notes/31/34/35`.

---

## 0. Objetivo y estado

Meta: `S_c := Σ width_i/N_c(u_i) ≥ 1` para un `c>0` fijo, con `N_c=(1−c)ℓ+c·w`. Esto da
`Σrw ≥ c+(1−c)·min ρ`, batiendo `0.928` (triángulo) / `2/(1+√d)` (general) para todo `c>0`.
**No se logra un `c>0` probado ni una obstrucción `c*=0`.** Sí se determina exactamente qué
falta y se descarta una de las dos rutas propuestas.

Notación: `ρ_i=ℓ_i/w_i∈(0,1]`, `ε_i=1−ρ_i≥0`, `q_c(ρ)=c+(1−c)ρ=1−(1−c)ε`,
`rw_i=width_i/w_i`, `A_i=width_i/ℓ_i=rw_i/ρ_i`. `S_0=ΣA_i` (cuerda), `S_1=Σrw_i` (Bang).
`δ := S_1−1 = Σrw_i−1` (**déficit/holgura de Bang** de la cobertura; `δ≥0 ⟺ Bang vale ahí`).

---

## 1. Lo firme de B-Y (fuente primaria, `refs/2602.20290`)

- **Lema 5 [VERBATIM]:** `Σ width_i/ℓ_K(u_i) ≥ 1`, i.e. **`S_0 ≥ 1`** para toda cobertura.
  Es el baseline `c=0`, **PROBADO** (sigue la prueba de Bang / Verreault Lema 2.3).
- **Lema 7 [VERBATIM]:** `ℓ_K(u)/w_K(u) ≥ 2/(1+√d)`, vía `L=½(K−K)`, John, y un
  **cuadrado perfecto** `(√(r+1)t−√(r−1))²≥0`. **Sharp para el CUBO.**
- Teorema 8 = `Lema 7 × Lema 5`: `Σrw ≥ (min ℓ/w)·S_0 ≥ 2/(1+√d)`.

---

## 2. La reducción exacta y la cota cruda [PROVED]

De `notes/35 §1` (verificado con `fractions`), para toda cobertura:
```
S_c ≥ 1   ⟺   S_0 − 1 ≥ L_c ,     L_c = Σ rw_i · c(1−ρ_i)/(ρ_i q_c(ρ_i)) ≥ 0.
```
Y el **sandwich** (`notes/31`): como `q_c(ρ_i)≤1`, cada `rw_i/q_c ≥ rw_i`, luego
```
S_c = Σ rw_i/q_c(ρ_i) ≥ Σ rw_i = S_1 = 1+δ.        (★)
```
**Consecuencia inmediata [PROVED]:** en toda cobertura donde Bang ya vale (`δ≥0` — facetas,
medianas, ≤2 direcciones, o cualquier tiling con `Σrw≥1`), `S_c ≥ 1` **gratis** para todo `c`.
El trabajo real está **solo** en coberturas con `δ<0` (hipotéticos contraejemplos de Bang).

La **cota cruda** (pull-out del mínimo) da solo `S_c ≥ q_c(ρ_min)·S_0/... ` insuficiente:
concretamente `Σrw ≥ q_c(ρ_min)=c+(1−c)·0.928`, que es `>0.928` **si se prueba `S_c≥1`**, pero
la cota cruda por sí sola NO prueba `S_c≥1` (da `<1` para `c>0`). Hace falta la estructura.

---

## 3. El "caso peligroso" es un casi-contraejemplo de Bang [PROVED]

**Proposición.** Si `S_0=1` (cuerda-Bang ajustado) y **alguna dirección activa es no-balanceada**
(`ρ_i<1`, `rw_i>0`), entonces `Σrw < 1` (contraejemplo de Bang).

*Prueba.* `S_0=Σrw_i/ρ_i ≥ Σrw_i` con desigualdad **estricta** si algún `rw_i>0` tiene `ρ_i<1`.
Luego `1=S_0>Σrw_i=S_1`. ∎

Interpretación: el conjunto de igualdad del Lema 5 (`S_0=1`), **si contiene alguna
configuración no-balanceada, produce un contraejemplo de Bang**. Como Bang(3) se cree cierto
(sin contraejemplo, evidencia fuerte), `S_0=1` debería forzar todo balanceado — pero probar
eso **incondicionalmente** = probar no-contraejemplo en ese régimen = tan difícil como Bang
ahí. Esto confirma el de-risking del jefe de research y explica por qué P1 no es trivial.

---

## 4. Análisis local en el conjunto de igualdad balanceado [PROVED, primer orden]

Cerca de una cobertura **balanceada-tight** (`ε_i→0`, punto donde ambos lados de la reducción
se anulan), expandiendo `1/q_c=1/(1−(1−c)ε_i)≈1+(1−c)ε_i`:
```
S_c − 1 = Σ rw_i/q_c(ρ_i) − 1 ≈ δ + (1−c) Σ rw_i ε_i .      (†)
```
Por tanto, a primer orden, **`S_c ≥ 1 ⟺ (1−c) Σ rw_i ε_i ≥ −δ`**:
- Si `δ≥0` (Bang vale): trivial.
- Si `δ<0` (sub-Bang): se necesita **`Σ rw_i ε_i ≥ |δ|/(1−c)`**.

El Lema 5 (`S_0≥1`) da, a primer orden, exactamente el caso `c=0`:
`S_0−1 ≈ δ + Σ rw_i ε_i ≥ 0 ⟺ Σ rw_i ε_i ≥ |δ|`. Es decir, **la no-balanza siempre domina
el déficit de Bang, pero solo por el factor `1`** (`c=0`).

> **Requisito EXACTO para `c* ≥ c` (Ruta B):** una **versión cuantitativa del Lema 5** con
> holgura relativa uniforme: `Σ rw_i (1−ρ_i) ≥ (1+γ) |δ|` con `γ>0` uniforme sobre coberturas.
> Entonces `c* ≥ γ/(1+γ) > 0` y se bate B-Y. El Lema 5 estándar da `γ=0` (holgura ≥ déficit,
> sin margen). **Extraer un `γ>0` de la prueba de signos de Bang (Lema 5) es la tarea abierta.**

---

## 5. Ruta A y Ruta B CONVERGEN (corrección de interpretación) [ARGUIDO]

> **[CORRECCIÓN 2026-07-01 — auditoría `auditorias/43`.]** Malinterpreté la "Ruta A" del jefe
> de research. Su **Ruta A** era **rehacer el argumento de signos del Lema 5 con `N_c` en lugar
> de `ℓ`** — lo cual **es literalmente probar `S_c = Σ width/N_c ≥ 1`**, i.e. coincide con la
> **Ruta B**. No son dos rutas: **convergen** en el mismo objetivo (R2-1). Lo de abajo (que el
> SOS del **Lema 7** no sirve) es cierto pero es un punto DISTINTO, no "Ruta A".

**Aclaración firme (lo que sí es un callejón):** el **Lema 7** (`ℓ/w ≥ 2/(1+√d)`, con su paso
SOS/perfect-square) es **per-direction** y **no** es el lugar a modificar. Sustituir `ℓ→N_c`
en el Lema 7 da `N_c/w = q_c = c+(1−c)ρ ≥ ρ` trivialmente; el `2/(1+√d)` sale de
`(min ℓ/w)·S_0`, y el factor que satura es el **acoplamiento del Lema 5**. Por tanto la
modificación relevante es la del **Lema 5** (el acoplamiento / argumento de signos de Bang),
NO la del Lema 7.

**Conclusión unificada:** batir B-Y por esta vía = **rehacer el Lema 5 de B-Y con `N_c`**
(= probar `S_c≥1`, R2-1). El requisito cuantitativo exacto está en §4 (holgura relativa
uniforme `γ>0` en el Lema 5). Esto es lo que se ataca con el Verreault survey (`refs/`, tiene
la prueba del Lema 2.3 = argumento de signos de Bang).

---

## 6. ¿Hay obstrucción `c*=0`? [no hallada, no descartada]

- **No hay obstrucción numérica barata:** una violación `S_c<1` requiere `δ<0` (un
  contraejemplo de Bang) con no-balanza insuficiente; como no se conoce contraejemplo de Bang,
  no hay config testeable que viole. Los tests de `notes/34` ("min `S_c`=1 sobre tilings") son
  **triviales** por (★) (en tilings `δ=0`), NO evidencia de `c*>0` en el régimen `δ<0`.
- **No hay prueba de `c*>0`:** por §3–§4, `c*>0` ⟺ Lema 5 con holgura relativa uniforme `γ>0`,
  no establecido.
- Estado honesto: `c* ∈ (0,1]` con `c=0` probado (Lema 5) y `c=1` = Bang(3) (abierto). El
  valor `c*` **no está determinado**; batir B-Y por esta vía **queda abierto**, reducido a la
  Ruta B con el requisito preciso de §4.

---

## 7. Próximo paso concreto (si se retoma P1)

Leer la prueba del **Lema 5 de B-Y** (sigue Bang/Verreault Lema 2.3, en `refs/2602.20290`) y su
argumento de signos, y buscar si produce **holgura estricta** `Σ rw_i(1−ρ_i) ≥ (1+γ)|δ|`
cuando hay direcciones no-balanceadas. Ese `γ>0` es el único ladrillo que falta; todo lo demás
(§2–§4) ya está montado. Riesgo: alto (es esencialmente pedirle a Bang una cota cuantitativa
en su conjunto de igualdad). Valor: batir el SOTA 2026.

## 8. Resumen de contribución de esta nota
- **[PROVED]** reducción exacta + sandwich (★); "caso peligroso = casi-contraejemplo" (§3);
  análisis de primer orden (†) con el requisito `Σrw_iε_i ≥ |δ|/(1−c)`.
- **[ARGUIDO]** Ruta A muerta; solo Ruta B (Lema 5 cuantitativo) es viable.
- **[OPEN]** `c*>0`. Reducido a: **Lema 5 con holgura relativa uniforme `γ>0`**.
