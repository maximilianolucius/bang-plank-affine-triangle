# Auditoría Ronda 9 — dualidad probada, D(u) columna vertebral. DECISIÓN: entregar pasada 5 YA. + Órdenes Ronda 10
> Auditor / Jefe de research: Claude. Fecha: 2026-07-03.
> Alcance: `notes/53-R9-*`, el `.tex` completo (24 pp), `defect_duality.py`.
> Método: verificación a mano de la dualidad fuerte, las cuñas, el lema de no-concurrencia
> exterior, el teorema del centroide, el tubo B4 y `Δ^d`; ejecución de los 3 scripts; cotejo
> de la Parte A contra el texto; diff de la copia congelada.

---

## Veredicto: la ronda pedida, entregada entera. TODO [PROVED] CONFIRMADO.

### 1. B1 — Dualidad fuerte (Thm 7.6-nuevo `thm:duality`) — verificada línea a línea
- **Dualidad débil bilateral** ✓ (la cadena `min ≤ ∫Σψ dμ = Σ∫ψ dν_i ≤ D` es correcta).
- **Claim 1** (`sup_ψ Φ = D_min(μ)`): la construcción regularidad-interior/exterior + Urysohn
  es correcta y cuidadosa (el `F≠∅` fuerza `∫g>0`; el tuple un-solo-ψ es admisible). ✓
- **Claim 2** trivial ✓. **Sion:** hipótesis verificadas (P(K) débil-* compacto convexo, Φ
  bilineal, continua en cada variable). ✓ El enunciado para `K` y `n` arbitrarios — mejor de
  lo pedido (ya en forma B2).
- **Certificado dual de facetas:** `ψ_i=(1−3t/2)₊` — verifiqué masa (3·⅓=1), valor
  (`Σψ(λᵢ)≥3−(3/2)Σλᵢ=3/2`) y el patrón de igualdad (contacto = hexágono; `ψ` se anula donde
  vive la holgura `ρ_i=(3/2)1_{[⅔,1]}`). Tres líneas, matched pair con el lazo primal. ✓
- **Cuñas (Prop `prop:wedge`):** rehíce (i) completo — `κ₁=Σ_{c>0}cᵢuᵢ+Σ_{c<0}|cᵢ|(1−uᵢ)`
  constante ≥0, no nula por ontoness; admisibilidad (`Σ∫ψ=1` vía `∫(θ−φ)₊=θ²/2`); el valor
  `A/(2κ)=1/(1−2δ_c)` con `|c₀−½Σc|=A/2−κ` ✓. (ii) distancia `ℓ∞`/dual `ℓ¹` ✓.
  (iii) unicidad de `p*` y el criterio `δ_c=δ ⟺ p*∈T_u` ✓. El matiz honesto (igualdad en los
  12 muestreados = [EVIDENCE], sin claim general) está bien etiquetado en Rem `rem:wedgemoment`.
- **Lema de no-concurrencia exterior (`lem:external`) — la joya escondida de la ronda.** Lo
  rederivé independientemente: por par no-ordenado `{j₀,j₁}` el `s` queda determinado por `q`,
  y las dos orientaciones dan `s'=1−s` (flip) **precisamente porque `Σq=1`** — así el conteo
  "≤ nº de pares con `(q_j−½)(q_k−½)≥0`" es exacto; fuera de `Δ̄` a lo sumo 2 pares califican.
  Consecuencia `δ_c=0⟺δ=0⟺D=1` ✓ (cierra el caso degenerado de las cuñas). Correcto.
- **Holgura complementaria (`prop:slack`)** + criterio de optimalidad esquelética: liquida el
  overclaim R9-A1a **por teorema**, como se ordenó. El sandwich de Rem 7.9-viejo lleva ahora
  certificado dual exacto (`c=(75,76,74|113)`, script check 4 ✓).

### 2. B3(a) + el "conjetural" probado
- **Thm `thm:centroid` (`δ(u)≤1/6` para TODA familia finita):** verificado — una línea,
  `u(G)=(1+s)/3∈[⅓,⅔]`; el centroide es testigo universal; igualdad ⟺ valores de vértice
  repetidos (tipo faceta). Consecuencia: **la cota de momentos nunca certifica `D>3/2` en el
  triángulo**. Sub-pregunta (a) de B3: SÍ, cerrada.
- **Thm `thm:facetd` (`D_{Δ^d}(facetas)=(d+1)/2`, todo `d≥2`):** lo que en mis órdenes era
  conjetural, PROBADO con matched pair: dual `ψ_i=(1−(d+1)t/2)₊` (∫=1/(d+1), suma ≥(d+1)/2 ✓
  verificado) + ciclo primal `P_k=s^k(0,1,…,d)/m`. **Verifiqué el ciclo a mano en `d=3`**
  (marginal `2·1_{[0,½]}` exacta: lado largo densidad ½ + tres cortos densidad 3/2) y por
  script `d=2..7` ✓. Honestidad escrita (no mejora el covering de facetas; es el alcance
  exacto del transporte). Además la cota de momentos es exacta en facetas en toda dimensión.
- **B3(b) (`D≤3/2` universal) queda [OPEN]** con estado consolidado `sup D∈[3/2,2]` —
  correcto no forzarlo esta ronda.

### 3. B2, B4, Parte A — verificadas
- **B2:** `D_K` definido para `K` general desde §2; el `1/d` re-encuadrado como "la uniforme
  certifica `D_K≤d`"; dualidad enunciada general. El reencuadre unificador está hecho.
- **B4-lite (`cor:region`):** verifiqué la aritmética completa — `1+k=1/(4√3−6)` exacto con
  `k=(2√3−3)/6`; `ε(1+km)<km² ⟺ ε/(m(m−ε))<k`; radio en medianas `k/(4+2k)>1/60 ⟺ 58√3>99
  ⟺ 10092>9801` ✓ (la caja vieja queda estrictamente dentro). Y el enunciado es honesto:
  "the region certified by the upper bound…, not the full sublevel set". ✓
- **Parte A:** convención de masas fijada (`α:=w_BC, β:=w_CA, γ:=w_AB`, l.507-510, y en la
  figura) ✓; sumset Lemma 3.2 aislado ✓; abstract reescrito — **una sola tesis (`D_K` como
  marco), Cor 27/29 FUERA del abstract, frase final de alcance impecable** ("none resolves
  the conjecture for the triangle, let alone the plane") ✓; §8 con intro propia; Appendix B
  protocolo (paper NOT computer-assisted) ✓. Copia congelada pasada5 = vivo (diff 0) ✓.
  Compila 24 pp limpio ✓. Scripts: `defect_duality.py` 8 bloques ALL OK (corrido) ✓.
- **Menor (no bloqueante):** abstract ≈ 230 palabras vs. las 150–200 que pidió Rosa. Está
  denso pero es UNA tesis; recorte fino opcional en la próxima pasada editorial.
- Decisión del investigador de NO figura para LMR (caso imposible): razonable, documentada.

---

## DECISIÓN (me la delegó el investigador): ENTREGAR LA PASADA 5 YA — no esperar B3(b)

Razones:
1. **El lazo externo es el más lento y el único no controlado.** Rosa debe evaluar la
   reestructuración (su objeción central) — eso no depende de B3(b).
2. **B3(b) es un problema abierto genuino** (`sup D∈[3/2,2]`): puede caer en una ronda o no
   caer en cinco. No se bloquea una auditoría estructural con una apuesta de investigación.
3. **B3(b) es aditivo, no estructural:** si cae después, entra como un teorema más colgado
   del marco ya validado; no cambia la arquitectura que Rosa debe juzgar.
4. El paquete está listo (`notes/53-R9-entrega-dona-rosa-pasada5.md`, con el mapa de las 13
   objeciones y la tabla de numeración vieja↔nueva — necesaria e inevitable: los lemas que
   ELLA pidió desplazan números).

**Al usuario:** entregar `drafts/entregas/affine-plank-triangle-2026-07-03-pasada5.pdf` con
el hand-off de `notes/53-R9-entrega...`. Pedir foco en: (i) la dualidad (Thm 7.6/su prueba),
(ii) el reencuadre `D_K` como respuesta a su crítica estructural SIN partir, (iii) las cuñas
y el lema de no-concurrencia exterior (nuevos), (iv) `Δ^d` (Thm 8.2). Recordar la tabla de
numeración. **Bloque de autor sigue placeholder (decisión del usuario).**

═══════════════════════════════════════════════════════════════════════
# ÓRDENES RONDA 10 (ejecuta el investigador; arrancan en paralelo a la pasada 5)
═══════════════════════════════════════════════════════════════════════

## R10-1 (research #1, la pregunta que quedó viva) — `sup_u D(u)`: ¿es 3/2?
Estado: `sup∈[3/2,2]`; momentos capados en 3/2 (Thm centroide) ⟹ cualquier terna con `D>3/2`
solo puede certificarse con `ψ` multi-nudo. Dos frentes simultáneos:
1. **Cacería exacta de `D>3/2`:** LP dual exacto con `ψ` lineales a trozos (nudos racionales,
   la ruta que dejaste en BUILD) sobre candidatos extremos: ternas casi-degeneradas (dos
   direcciones casi paralelas — ¡cuidado: el enunciado exige no-paralelas, mirar el límite!),
   ternas "faceta+2 lejanas", esquinas del espacio de patrones. Si aparece `D>3/2` con
   certificado dual exacto: teorema "las facetas NO son el peor caso" + localización.
2. **Intento de `D≤3/2` universal:** construcción primal — ¿existe un "lazo inscrito"
   generalizado (ciclo/esqueleto con masas) que dé marginales `≤(3/2)Leb` para TODA terna?
   Pista estructural: en facetas el óptimo es el ciclo por los vértices alternos del hexágono
   de contacto; buscar el análogo con el contact set del dual óptimo (prop:slack).
**Cualquiera de los dos desenlaces es un teorema.** Exacto/racional; la grilla no decide.

## R10-2 (research #2, acotado) — ¿`δ_c=δ` siempre? (el criterio `p*∈T_u`)
En los 12 ejemplos exactos hay igualdad [EVIDENCE]. Probar `p*∈T_u` para toda terna
no-paralela (⟹ las cuñas SIEMPRE igualan la cota de momentos — bonito y redondea §7) o
exhibir contraejemplo exacto (⟹ delimita las cuñas; también publicable). Nota: `T_u` es el
triángulo imagen — la pregunta es si el punto `ℓ∞`-más-próximo del plano `Π` cae siempre en
él. Conexión con `lem:external` (que ya cierra el caso `δ_c=0`).

## R10-3 (editorial menor) — recorte fino del abstract a ≤200 palabras
Sin tocar la tesis única; es poda de palabras, no de contenido.

## R10-4 (carryover, fondo) — estabilidad cuantitativa `ε` de la familia cíclica (ex R8-6).
## R10-5 (moonshot, fondo) — acoplamiento (batir B-Y global). Sin cambios.

---

## Prioridad
1. **Entrega pasada 5 (usuario, ya)** — R10-1/R10-2 arrancan en paralelo.
2. **R10-1** (sup D — la pregunta abierta con más gancho del nuevo marco).
3. **R10-2** (acotada, redondea la teoría de cuñas).
4. R10-3 · R10-4 · R10-5 fondo.

**Mensaje al investigador:** la dualidad quedó exactamente como debía — con certificados en
ambos lados y el overclaim convertido en teorema. El lema de no-concurrencia exterior es la
joya silenciosa de la ronda. La decisión de entrega está tomada: pasada 5 sale ya; tú sigue
con `sup D` — es la pregunta que el propio marco dejó madura, y con el LP dual multi-nudo
tienes la herramienta exacta para decidirla.
