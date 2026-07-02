# R2-1 (FLAGSHIP) — Rehacer el argumento de signos de Bang con `N_c`: NO-GO riguroso

> Date: 2026-07-01. Status: **[NO-GO PROBADO para el método]**. La vía R2-1 propuesta
> (rehacer el Lema 5 de B-Y / argumento de signos de Bang con el normalizador
> `N_c=(1−c)ℓ+c·w` en lugar de la cuerda `ℓ`) **no puede dar `c>0`**: el presupuesto de
> movimiento del testigo de Bang es exactamente la cuerda más larga `ℓ(u)`, y `N_c≥ℓ` pide
> superarla. Fuente primaria: `refs/2203.05540` (Verreault survey), Lemas 2.3–2.5.
> Esto NO prueba que `S_c≥1` sea falso; prueba que **este método** tope en `c=0`.

---

## 0. Qué se pedía y qué se encontró

**R2-1 (unificado, tras la corrección de `notes/43-P1 §5`):** probar
`S_c := Σ width_i/N_c(u_i) ≥ 1` para algún `c>0`, rehaciendo el argumento de signos de Bang
(Lema 5 de B-Y = Lema 2.5 de Verreault) con `N_c` en vez de `ℓ`. **Resultado:** el argumento
de Bang **produce exactamente `ℓ` como normalizador y no más**; `N_c>ℓ` es geométricamente
inalcanzable por esta vía. **`c*=0` para el método de Bang.**

---

## 1. El mecanismo de Bang, con su presupuesto exacto (fuente primaria)

El teorema de plank de Bang (Verreault, Thm 2.2/2.4) construye un **punto testigo tipo sistema
de Bang** `x_ε = x_0 + Σ_j ε_j u_j` (`u_j` = vector-anchura del plank `j`, `ε_j=±1`) y usa el
**Lema de Bang** (2.5, argumento de signos: maximizar `Σ h_ij ε_iε_j w_iw_j − 2Σε_iw_im_i`,
óptimo bajo flip único ⟹ `|⟨x_ε,u_k⟩−m_k| ≥ w_k`) para elegir signos que hacen a `x_ε`
**escapar de todos los planks**. Si `x_ε∈C` siempre, hay contradicción con la cobertura ⟹ la
desigualdad de plank.

**El paso que fija el normalizador es el Lema 2.3 (cuerda), no el Lema de signos.** Verbatim
(Verreault, Lema 2.3):

> Sea `u` de norma `a/2` (`a<w(C)`), `m` el punto medio de una **cuerda más larga** de `C`
> paralela a `u`, de longitud `ℓ`. Entonces `(C−u)∩(C+u)` contiene una **homotecia de `C`**
> centro `m` y **razón `(ℓ−a)/ℓ`**.

Iterando sobre las direcciones (Verreault, ec. 2.1), `⋂_ε (C − Σε_j u_j)` contiene una
homotecia de `C` de razón `1 − Σ_j w(P_j)/ℓ_j`. Luego:

> **Si `Σ_j w(P_j)/ℓ_j < 1`, la intersección es no vacía** ⟹ existe `x_0` con `x_ε∈C` ∀`ε`
> ⟹ (Lema de signos) hay un testigo que escapa ⟹ **no cubre**.

Contrapositivo = **Lema 5 de B-Y:** cubrir ⟹ `Σ width_i/ℓ_i ≥ 1` (`S_0≥1`). **El
denominador `ℓ_j` (cuerda más larga en dirección `u_j`) es forzado por la geometría del
Lema 2.3: la razón de homotecia es `(ℓ_j−a_j)/ℓ_j`, con `ℓ_j` = cuerda real.**

---

## 2. `N_c > ℓ` es inalcanzable — y `(ℓ−a)/ℓ` es TIGHT [PROVED]

Para normalizar por `N_c(u_j)=(1−c)ℓ_j + c·w_j` en vez de `ℓ_j`, el Lema 2.3 tendría que dar
una homotecia de razón `(N_c−a)/N_c > (ℓ−a)/ℓ` (mayor razón = menos contracción, pues
`N_c≥ℓ`). **Pero la razón `(ℓ−a)/ℓ` es exacta y óptima**, y `ℓ` es la cuerda **más larga**:

- **Tightness (prueba 1-D, rigurosa).** Tómese `C=[y,z]` un **segmento** de longitud `ℓ`
  (cuerpo convexo degenerado, o límite de cuerpos delgados). Con `u = a(z−y)/2ℓ`,
  `(C−u)∩(C+u)` es el segmento `[y+a/2·, z−a/2·]` de longitud **exactamente `ℓ−a`**, razón
  `(ℓ−a)/ℓ`. **No se puede mejorar.** (Verificado, `scratchpad/r2_1.py`: `a=0.2,0.5,0.8` →
  longitud `= ℓ−a` exacta.)
- **`ℓ` es un tope duro.** El presupuesto de desplazamiento del punto de Bang en dirección
  `u` (cuánto puede moverse `±` desde el centro y seguir en `C`) es la **semi-cuerda más
  larga** `ℓ(u)/2`. Pedir presupuesto `N_c(u)/2 ≥ ℓ(u)/2` = pedir un segmento en `C` paralelo
  a `u` **más largo que la cuerda más larga**. Absurdo.
- Y `N_c ≥ ℓ` siempre (`N_c=(1−c)ℓ+cw`, `w≥ℓ`; igualdad sii `c=0` o `ℓ=w`). Confirmado
  `ℓ≤w` numéricamente (equilátero: `min ρ=ℓ/w=0.9282=4√3−6`, `scratchpad/r2_1.py`).

**Conclusión [PROVED]:** el argumento de signos de Bang + Lema 2.3 **produce el normalizador
`ℓ` y ningún normalizador mayor.** Rehacerlo con `N_c` (`c>0`) es imposible: la razón de
homotecia está atada a la cuerda real. **`c*=0` para este método.**

---

## 3. Qué significa (y qué NO)

- **NO** prueba que `S_c≥1` sea falso para `c>0`. La desigualdad `S_c≥1` (`c>0`) sigue
  `[OPEN]`; podría ser cierta y demostrable por **otro** método.
- **SÍ** prueba que la ruta propuesta (R2-1: "rehacer Bang con `N_c`") **no puede funcionar**.
  Es un no-go de método, no de la afirmación.
- **Coincide con el techo estructural de B-Y** (`notes/42`): su cota `2/(1+√d)` es
  `min(ℓ/w)·[cuerda-Bang]`, sharp para el cubo; la pieza cuerda-Bang usa `ℓ`, y aquí se prueba
  que `ℓ` es **forzado** por el argumento de Bang. Ambos apuntan a lo mismo: **la vía de
  testigo-por-cuerda (Bang system point) topa en `ℓ`.**
- **Consecuencia estratégica (firme):** batir B-Y **requiere un testigo que NO sea el punto
  del sistema de Bang** `Σε_j u_j` (confinado a cuerdas), sino uno que explote la estructura
  **global/de acoplamiento** de la cobertura. Esto es exactamente la propiedad "escape-de-
  TODAS + dependiente de posición" del certificado buscado (`notes/23 E`). El normalizador
  `N_c` no se alcanza mejorando Bang; se alcanzaría (si acaso) con un método de acoplamiento.

---

## 4. Reconciliación con `notes/43-P1`

`notes/43-P1 §4` mostró que `S_c≥1` (`c>0`) equivale a una **holgura relativa uniforme
`γ>0`** en el Lema 5 (`Σ rw_i(1−ρ_i) ≥ (1+γ)|δ|`). Esta nota añade: **esa holgura NO puede
extraerse del argumento de Bang**, porque el argumento produce la igualdad `S_0≥1` con
normalizador `ℓ` exacto (tight en segmentos/tilings), sin margen para `N_c>ℓ`. El `γ>0`, si
existe, vive fuera del método de Bang.

**Estado R2-1: método CERRADO (no-go).** La afirmación `c*>0` queda como problema abierto que
requiere una técnica de acoplamiento nueva; **no** una modificación de Bang. Recomendación:
tratar R2-1 como **alto riesgo / territorio experto sin ruta conocida**, y priorizar el
deliverable seguro **R2-4** (paper "casos + método"), manteniendo el acoplamiento off-surface
(`notes/23 E`, `notes/30 §8.5`) como la única vía candidata viva hacia `c>0`.

Scripts: `scratchpad/r2_1.py` (`ℓ≤w`, min `ρ=4√3−6`; tightness del segmento).
Fuente: `refs/2203.05540` Lemas 2.3–2.5 (Bang vía cuerda).
