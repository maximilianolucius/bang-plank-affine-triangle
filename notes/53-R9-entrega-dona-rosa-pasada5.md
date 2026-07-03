# R9-entrega — Paquete: quinta pasada de doña Rosa

> Date: 2026-07-03. Status: **[LISTO — decide el jefe]**. Versión congelada:
> `drafts/entregas/affine-plank-triangle-2026-07-03-pasada5.pdf` (**24 pp**;
> 0 errores / 0 undefined / 0 overfull).
> Nota del investigador al jefe: A1–A6, B1, B2 y B4 están completas; de B3, la
> sub-pregunta (a) quedó PROBADA (`δ ≤ 1/6`, centroide) y además cayó
> `D_d(facetas) = (d+1)/2` en toda dimensión; la sub-pregunta (b) (¿`D ≤ 3/2`
> universal?) sigue ABIERTA y así está declarada en el Problem 10.3. Si
> prefieres agotar B3(b) antes de la 5ª pasada, el paquete espera.

## Mensaje sugerido para doña Rosa

Doña Rosa: decidimos NO partir el manuscrito, y en su lugar atacar la raíz de
su objeción estructural: el defecto de transporte `D(u)` es ahora la columna
vertebral del paper desde la introducción — medianas, ternas cíclicas,
facetas y la caracterización son casos especiales de un solo objeto (`D = 1`
en concurrencia, `3/2` en facetas, `≤ d` siempre), y §7 tiene ahora la teoría
que usted echó en falta: dualidad fuerte con certificados explícitos en ambos
lados. Todos sus puntos aceptados de la 4ª pasada están ejecutados (mapa
abajo). Le pedimos foco en: (i) la dualidad (Thm 7.6) y sus certificados
(Cor 7.7, Prop 7.8, Prop 7.11); (ii) el teorema del centroide (Thm 7.3) y el
defecto facetario en toda dimensión (Thm 8.2), que son nuevos; (iii) si la
reestructura responde su lectura de "tres papers".

## Mapa objeción (pasada 4) → resolución (pasada 5)

| # | Su objeción | Resolución |
|---|---|---|
| 1 | Tres papers en un PDF; partir | **No se partió (decisión del autor), se unificó**: `D_K(u)` definido en §2 como marco general; §1 con subsección "The transport defect as organizing frame"; cada bloque del paper es un caso/valor del mismo objeto. La expansión de §7 (dualidad) hace que §7–§8 sean la segunda columna, no un agregado. |
| 2 | Abstract inaceptable; una sola tesis | Reescrito (~200 palabras): una tesis (caracterización `D=1 ⟺` concurrencia + familias sharp rígidas, organizadas por el defecto y su dualidad); sin lista de resultados secundarios; sin la comparación B-Y como logro central; cierre de alcance intacto. |
| 3 | "Settling Gardner" demasiado amplio | Quirúrgico en intro y Rem 6.12: "settles the existence question of Gardner **only** for three directions on the triangle" / "completely — but only — for". |
| 4 | Thm 6.6 Step 2 no está a nivel | Partido en **Lemma 6.7 (margin identity)**, **Lemma 6.8 (coverage)** (con el Pocket Lemma topológico, casos de vértice/coincidencia explícitos), **Lemma 6.9 (interior witnesses)** (positividad de x*,y* en el texto); prueba del teorema = ensamblaje de tres lemas. |
| 5 | Apéndice A: degenerados y tilings cerrados | (O2) reescrito airtight con las dos cláusulas separadas: una traza degenerada *ni cubre* (a lo sumo un punto, y los no-degenerados son cerrados) *ni estorba* (interior vacío ⟹ disjunción de interiores vacua) ⟹ **ninguna solución cerrada se pierde**. Grupo `G≅S₃` explícito ya desde la pasada 4. |
| 6 | §7 inmadura; falta dualidad; "computable by LP" falso | **Thm 7.6 (strong duality)** con prueba completa (Sion + dos lemas de identificación); Cor 7.7 (certificados); Prop 7.8 (cuñas explícitas = forma dual de la cota de momentos, con criterio exacto de igualdad); Prop 7.11 (holgura complementaria); Rem 7.12 (cuándo el óptimo vive en el esqueleto: `D_∂ = 1` en concurrencia, `D_∂ = ∞` en facetas). El overclaim del LP **eliminado**: Rem 7.17 dice explícitamente que el LP esquelético da solo cota superior, y el sandwich `225/224 ≤ D ≤ 112/111` lleva ahora certificado dual explícito del lado inferior. |
| 7 | Comparación con `4√3−6` demasiado intensa | Fuera del abstract; en la intro una sola mención con el caveat en la misma frase; Rem 7.16 intacta; el nuevo Cor 7.15 (región) declara él mismo que es "la región que certifica nuestra cota, no el sublevel set completo". |
| 8 | §8 prematura; sacar | Se queda (decisión del autor) pero re-motivada: título nuevo, introducción propia colgada del marco, y un teorema nuevo de peso: **`D_{Δ^d}(facetas) = (d+1)/2` exacto en toda dimensión (Thm 8.2)**, con par primal–dual explícito (ciclo inscrito + `ψ = (1−(d+1)t/2)_+`). |
| 9 | Normalizer = observación | Ya partido (Prop 9.1 + Rem 9.2) desde la pasada 4; sin cambios. |
| 10 | Thm 3.2 artesanal; aislar sumsets | **Lemma 3.2 (sumset lemma)** aislado y probado una vez (compactos, `Σ|C_k| > d ⟹ 1 ∈ ΣC_k`); la prueba del teorema queda en: agrupar, recortar con `η`, invocar el lema. |
| 11 | Jerarquía difusa (Thm 4.1 al nivel de 6.6) | Subsección "Results and their hierarchy": main / framework / **illustrative** (Thm 4.1 nombrado ahí explícitamente: "not at the level of the main results") / extensions. §4 abre diciéndolo también. |
| 12 | Terminología; masas α/β/γ ambiguas | "Direction" (coordenada afín normalizada, no normal euclídea), "witness measure" y "cyclic triple" definidos formalmente en §1. **Convención de masas fijada una vez en Thm 6.3**: `α=w_BC, β=w_CA, γ=w_AB` (letra griega = arista opuesta al vértice homónimo), referenciada en Thm 6.6 y §7. |
| 13 | Señales de borrador | **Appendix B**: protocolo de verificación (paper NO computer-assisted; scripts = verificación secundaria exacta; tabla script→enunciado). Bloque de autor: pendiente (identidad real, decisión humana). |

## Mapa de numeración (pasada 4 → pasada 5) — para sus referencias

| Pasada 4 | Pasada 5 | Objeto |
|---|---|---|
| Def 7.1 | **Def 2.1** | D_K(u) (ahora general) |
| Prop 7.2 | **Prop 2.2** | propiedades básicas (general) |
| Thm 2.1 | **Thm 2.3** | 1/d = uniforme certifica D≤d |
| Rem 2.2 | **Rem 2.4** | una-medida-vs-todas [½,⅔] |
| — | **Lem 3.2** | sumset lemma (nuevo) |
| Thm 3.2 | **Thm 3.3** | facet-parallel |
| Thm 5.1, Lem 5.2, Thm 6.3, Cor 6.4, **Thm 6.6**, Prop A.1 | **sin cambio** | |
| — | **Lem 6.7 / 6.8 / 6.9** | split de la prueba de 6.6 (nuevos) |
| Thm 6.8 | **Thm 6.11** | caracterización 3 direcciones |
| Rem 6.9 | **Rem 6.12** | alcance de la caracterización |
| Prop 7.3 | **Prop 7.2** | cota de momentos (ahora general) |
| — | **Thm 7.3** | centroide δ≤1/6 (nuevo) |
| Thm 7.4 | **Thm 7.4** | D(facetas)=3/2 (conserva número) |
| Rem 7.5 | **Rem 7.5** | complementariedad |
| — | **Thm 7.6 / Cor 7.7 / Prop 7.8 / Lem 7.9 / Rem 7.10 / Prop 7.11 / Rem 7.12** | dualidad (todo nuevo) — ¡ojo: "Cor 7.7" ahora es certificados, no 27/29! |
| Thm 7.6 | **Thm 7.13** | estabilidad lineal |
| Cor 7.7 | **Cor 7.14** | 27/29 > 4√3−6 |
| — | **Cor 7.15** | región certificada (nuevo) |
| Rem 7.8 | **Rem 7.16** | caveat B-Y |
| Rem 7.9 | **Rem 7.17** | sandwich (reescrita) |
| Thm 8.1 | **Thm 8.1** | σ-familia (conserva) |
| — | **Thm 8.2** | D_d(facetas)=(d+1)/2 (nuevo) |
| Prop 8.2 | **Prop 8.4** | obstrucción d≥4 |
| Prob 10.3 | **Prob 10.3** | reescrito con el estado nuevo |
| — | **App B** | protocolo ancillary (nuevo) |

## Qué es NUEVO desde su pasada 4 (pedirle foco)

1. **Thm 7.6 (strong duality)** — el dual que usted pidió, con prueba completa.
2. **Thm 7.3 (centroid bound)**: `δ(u) ≤ 1/6` para toda familia, de cualquier
   tamaño; la cota de momentos nunca certifica `D > 3/2`.
3. **Thm 8.2**: `D_{Δ^d}(facetas) = (d+1)/2` exacto, todas las dimensiones.
4. **Prop 7.8 + Lem 7.9**: la cota de momentos como certificado dual explícito
   (cuñas), con su criterio geométrico exacto de igualdad.
5. **Cor 7.15**: tubo certificado alrededor de todo el lugar concurrente.
6. La reestructura completa (D_K en §2; jerarquía; abstract).
