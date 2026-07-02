# Conocimiento FIRME rescatado de toda la investigación
> Lo que sobrevive a la auditoría adversarial — proven, o establecido con certeza.
> Date: 2026-06-29.
>
> **[CORRECCION CRITICA 2026-06-30 — auditoria]** El item **A.4** abajo ("Hunter 1993:
> 3 planchas sobre el triángulo ⟹ Σrw≥1") es **INCORRECTO** como teorema probado.
> Hunter (Proc. AMS 117, 1993) probó (i) el caso de DOS planks en el plano y (ii) la
> CARACTERIZACION DE IGUALDAD `Σrw=1 ⟺ t1+t2+t3=1`. El caso de TRES planks arbitrarios
> sobre el triángulo sigue ABIERTO (Verreault survey §2.2.3; Bakaev-Yehudayoff 2026).
> Reclasificar A.4: la parte de **igualdad/config extremal** es firme; la **desigualdad
> general de 3 planks NO** lo es. Lo único probado sin Hunter en esa direccion es
> "3 facetas + 1 arbitrario ⟹ Σrw≥1" (`notes/30` §1, prueba por fibras).

## A. Teoremas PROBADOS (rigurosos, nuestros salvo donde se cita)
1. **Teorema de 2 direcciones** (sharp): cualquier nº de planchas en 2 direcciones
   sobre el triángulo ⟹ Σrw≥1. Prueba: acoplamiento con marginales uniformes (c=1)
   vía Strassen. (= AKP 2019.)
2. **Teorema faceta-paralelo** (sharp, TODA dimensión): planchas paralelas a las
   caras del símplex, cualquier nº ⟹ Σrw≥1. Prueba: Brunn–Minkowski 1-D / sumset
   `1∈ΣFᵢ`. Genuino y corto.
3. **Teorema 1/d + cota refinada** en el plano: `1 ≤ 2S − Σrw²`. (= Chambers–Mouillé.)
4. **Hunter (1993) [CORREGIDO]:** probó el caso de DOS planks (plano) y la
   CARACTERIZACION DE IGUALDAD `Σrw=1 ⟺ t1+t2+t3=1` (config extremal `R−1=(1−T)²/(2−T)`
   es la frontera de igualdad). La **desigualdad general para 3 planks queda ABIERTA**
   (ver banner). NO contar A.4 como prueba de Bang(3).

## B. Reformulaciones LIMPIAS (firmes, reutilizables)
5. **Modelo vectorial/cúbico:** triángulo ≡ 2-símplex; planchas ≡ franjas
   coordinadas `yⱼ∈Iⱼ` en `[0,1]^m`. Elimina toda la geometría de complementos.
6. **El problema como SET-COVER entero:** Σrw≥1 ⟺ el mínimo entero de un set-cover
   geométrico es ≥1. Da acceso a ILP exacto y a la teoría de brechas de integralidad.

## C. Hallazgos ESTRUCTURALES (firmes, establecidos numéricamente exacto)
7. **La brecha de integralidad es REAL.** Al refinar la malla, el LP/medida se
   estabiliza en ~0.70 (<1) mientras el entero queda en 1.0000. ⟹ el caso m≥4 está
   **genuinamente más allá de cualquier medida testigo única** — es combinatorio,
   no fraccionario. (Consistente con la imposibilidad de Gardner.)
8. **El certificado vive en el BORDE.** El testigo fraccionario óptimo concentra
   54% de su masa en las aristas, 0% en los vértices, las direcciones igualmente
   binding. Conecta con la prueba de borde de Hunter.
9. **m≥4 es IRREDUCIBLE — confirmado por 4 ángulos independientes:**
   (a) 95% de coberturas m=4 tienen las 4 planchas esenciales;
   (b) no hay reducción a facetas (la dirección inclinada es no-reducible pero neutra);
   (c) el residuo tras bandas de faceta es un triángulo auto-similar, pero quitar una
       plancha inclinada deja un cuadrilátero (peeling se rompe);
   (d) el sumset de la dirección inclinada escapa de Δ.
10. **Confirmación ILP exacta:** mínimo entero Σrw = 1.0000 en TODA configuración
    testeada (3–6 direcciones). La evidencia numérica más fuerte (no es prueba).

## D. Conocimiento NEGATIVO firme (saber qué NO funciona, y por qué)
11. **Principio del "quantifier swap"** (de tus refutaciones de Helly y entropía):
    cualquier potencial/medida que haga a un punto "escapar de ALGUNA plancha" falla,
    porque una falla de cobertura exige escapar de TODAS a la vez. Mata de un golpe a
    toda una clase (potenciales de entropía, Helly por celda de signos, suma-log).
    **Reutilizable y valioso.**
12. **Barrera de posición-independencia:** ningún certificado construido solo con
    normales+anchos (zonotopo, Farkas 0-1) puede servir — cubrir depende de la
    posición. (Verificado: coberturas válidas violan la dominancia del zonotopo.)
13. **La vía algebraica/tórica está muerta:** denominadores no-Laurent; al limpiarlos,
    la resultante densa es idénticamente nula (raíces en el infinito). Sin blow-ups, no.
14. **Medida única topada en c*≈1.60** (⟹ ≥0.624) para direcciones **faceta/genéricas**.
    La ruta de medida es de fondo <1 **ahí**. **MATIZ 2026-06-30 (notas 36/37):** una medida
    única SÍ alcanza `c=1` (marginal uniforme en las 3 direcciones) para las **ternas de
    concurrencia** — aquéllas cuyas 3 líneas `{u_i=1/2}` concurren en Δ, i.e. `1ᵀV⁻¹1=2`
    (equiv. `Σa_i=2κ` para la relación `Σa_i u_i=κ`). Ejemplo: **medianas** (`Σm=3/2`,
    concurren en el centroide) ⟹ Bang probado por transporte (nota 36). Evade Gardner
    justo donde las facetas (`Σx=1≠3/2`) no pueden. Es una **familia 2-dim** (codim 1),
    incl. genéricas; suficiencia [evidencia fuerte]. NO contradice lo anterior: "single-
    measure muerto" valía para faceta/genérico-fuera-de-superficie, no para la superficie
    de concurrencia.
15. **~19 rutas refutadas con certeza** (el mapa de obstrucción completo).

## E. LA SÍNTESIS — qué debe ser un certificado ganador (lo más valioso)
Combinando C7, C8, D11, D12, un certificado que cierre m≥4 debe ser SIMULTÁNEAMENTE:
- **entero/combinatorio** (no una medida fraccionaria) — por la brecha real (C7);
- **dependiente de la posición** (no solo normales+anchos) — por D12;
- **basado en el borde** (aristas, no interior ni vértices) — por C8;
- **tipo "escapar de TODAS"** (sup, no suma/promedio) — por D11.
Ningún método actual (medida, cuerda/B-Y, polarización, simpléctico, Carathéodory
colorido, zonotopo, entropía, topología del nervio) cumple las cuatro a la vez.
**Esta caracterización de 4 propiedades es el producto firme más útil de todo el
trabajo:** dice qué apuntar y descarta clases enteras de un plumazo.
