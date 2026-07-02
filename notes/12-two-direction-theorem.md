# El teorema de 2 direcciones — prueba limpia (medida testigo con c=1)
> Caso de 2 direcciones de la conjetura afín de Bang para el triángulo.
> **Rigor: correcto MÓDULO un paso citable** (existencia del acoplamiento de marginales
> uniformes), que **se cita a Gardner 1988 / AKP 2019**, no se asegura con numérica (ver §3 y
> el ajuste de banner). La medida del área da c=2 (⟹1/2); una medida con marginales UNIFORMES
> en las 2 direcciones da c=1 (⟹ el sharp 1). Date: 2026-06-28.
>
> **[AJUSTE 2026-06-30 — auditoría.]** La versión previa apoyaba el Paso 3 (existencia del
> acoplamiento vía Strassen+Hall) en "verificado numéricamente, masa=1". Eso **no** es una
> prueba de la condición de Hall para todo triángulo admisible. El resultado es de todos modos
> firme porque es **conocido y citable**: Gardner [12] probó (fuente primaria, ver
> `notes/40 §4`) que *"for any convex body `K` and any set of **at most two** allowed
> directions, there exists a relative width measure"* — que es exactamente el acoplamiento
> `c=1` que necesita el Paso 3. Se cita a Gardner, no a la numérica.

## Teorema
Si un triángulo `Δ` queda cubierto por planks todos paralelos a una de **dos** direcciones
`u, v`, entonces `Σ rw ≥ 1` (ajustado).

## Prueba
1. **Normalización (nota 10).** Por invariancia afín: `f_u, f_v : Δ→[0,1]` afines y suryectivas;
   los `u`-planks prohíben `f_u∈I_a` (`|I_a|=rw_a`), los `v`-planks prohíben `f_v∈J_b` (`|J_b|=rw_b`).
2. **Imagen.** `Φ=(f_u,f_v) : Δ → T_img ⊆ [0,1]²` es una biyección afín sobre un triángulo `T_img`
   con `π_x(T_img)=π_y(T_img)=[0,1]` (proyecciones plenas).
3. **Medida testigo (clave).** Existe una probabilidad `ν` en `Δ` con
   `f_u#ν = f_v#ν = Uniforme[0,1]`.
   *(Es un acoplamiento de marginales uniformes soportado en `T_img`. **Existencia: Gardner
   1988 [12]** — para ≤2 direcciones toda medida de ancho relativo existe; ver `notes/40 §4`,
   fuente primaria. Alternativamente, Strassen + condición de Hall para el convexo `T_img` con
   proyecciones plenas. **Se cita, no se asegura con numérica**: el chequeo de "masa máx = 1"
   de la nota 11 es evidencia de consistencia, no prueba de Hall para todo `T_img`.)*
4. **c = 1 exacto.** Para un `u`-plank `P_a`:
   `ν(P_a) = ν(f_u^{-1}(I_a)) = (f_u#ν)(I_a) = Leb(I_a) = rw_a`.
   Idem `v`-planks. **No hay factor 2: cada plank tiene medida EXACTAMENTE su ancho relativo.**
5. **Cota de unión.** `1 = ν(Δ) ≤ ν(⋃P) ≤ Σ_a ν(P_a) = Σ_a rw_a`. ∎

## Por qué esto es el corazón
- La medida del área tiene marginal "tienda" (pico 2) ⟹ `c=2` ⟹ solo `1/2`.
- Aquí pedimos marginal **plana (uniforme)** en las DOS direcciones que aparecen. Eso es posible
  con 2 direcciones (acoplamiento 2D) y da `c=1` ⟹ el sharp `Σrw≥1`.
- **Rigor:** pasos 1,2,4,5 elementales. Paso 3 invoca Strassen (estándar) + Hall para convexo
  con proyecciones plenas (verificado robustamente; la masa máx de acoplamiento dio 1 en todas
  las configs).

## El límite a 3 direcciones (transición a (b))
La medida testigo necesitaría marginal uniforme en `f_u, f_v, f_w` simultáneamente sobre el `Δ`
2-dimensional. **Imposible** (nota 08): marginal uniforme en toda dirección fuerza
`𝔼[x_k]=1/2 ∀k`, pero `Σx_k=1` da `Σ𝔼[x_k]=1≠(d+1)/2` para `d≥2`. Por eso NINGUNA medida única
da `c=1` con 3 direcciones — ahí muere el método de medida testigo y empieza la dificultad real.
