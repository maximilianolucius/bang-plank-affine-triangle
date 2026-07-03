# Auditoría Ronda 8 (pasada de precisión) — CERRADA. Todo verificado.
> Auditor / Jefe de research: Claude. Fecha: 2026-07-02.
> Alcance: R8-1..R8-5 sobre el `.tex` vivo (17 pp). Método: verificación directa de cada
> corrección contra el texto + recompilación desde cero + chequeo de numeración en el `.aux`.

---

## Veredicto: los dos overclaims eliminados correctamente; un hueco real de prueba destapado y bien resuelto. Lista para la 4ª pasada de Rosa.

### R8-1 — overclaims (bloqueantes) — RESUELTOS ✓
- **`single-measure` (l.153 + abstract):** la prueba de Thm 2.1 ahora dice "the **uniform**
  measure cannot certify a constant larger than `1/d`" — verdadero. La **Rem 2.2**
  (`rem:oneall`) convirtió el overclaim en **contenido real y correcto**: la mejor constante
  certificable por una sola medida contra TODAS las direcciones a la vez está en `[½,⅔]`
  — `½` por la uniforme (Prop 7.2(iv), `D≤2`), `⅔` porque la terna de facetas ya la fuerza
  (Thm 7.4, `D=3/2`). Verifiqué ambas cotas. Buen giro: el defecto se volvió resultado.
- **"(equivalently Conjecture 1.1 for the triangle)":** borrado; Problem 1 ahora dice que
  3-planks es sub-problema, no equivalente. ✓

### R8-3 — HALLAZGO: la queja #7 de Rosa (Thm 3.2) era un hueco de PRUEBA, no de redacción
El investigador descubrió, al atender lo que parecía un menor, que los `C_k=[0,1]\U_k` son
**abiertos relativos** (los planks son cerrados ⟹ `U_k` cerrado ⟹ `C_k` abierto), no
compactos como afirmaba el texto — y BM-1D se aplicaba a compactos. **Lo verifiqué:** el
arreglo (recortar a compactos `C_k'` con pérdida `η=(1−R)/(d+2)`) da holgura final
`2−R−(d+1)η = (d+3−R)/(d+2) > 1 ⟺ R<1` — **correcto** (lo recalculé). BM-1D probado en una
línea (`A+B ⊇ (A+min B)∪(max A+B)`, solapan en un punto). El resultado siempre fue cierto;
la justificación escrita estaba mal y ahora es rigurosa.
**Nota de honestidad sobre MÍ:** yo audité Thm 3.2 en la Ronda 3 (`auditorias/47`) y lo di
por correcto sin notar el defecto abierto/compacto. Es un fallo mío de auditoría que la
disciplina de Rosa + el investigador corrigieron. Registrado.

### R8-3 resto + R8-2 + R8-4 + R8-5 — verificados por muestreo
- **Numeración preservada** (crítico para que la copia de Rosa no se desalinee): `.aux`
  confirma `thm:tight`=**6.6**, `thm:char`=**6.8**; el Step 2 de Thm 6.6 se aisló como
  "Pocket Lemma" **sin numerar** a propósito. Cor 7.7=7.7, Thm 7.4, Rem 7.5 correctos. ✓
- **Alcance:** intro con niveles (a)–(e) + "every theorem lives at level (a) or (b)";
  Rem 6.9 "within the witness-measure approach"; Cor 7.7 con caveat en abstract e intro. ✓
- **Rigor:** Prop 9.1 partida (ratio sharp) + Rem 9.2 metodológico; Gardner Thm 1 verbatim;
  Apéndice A con grupo explícito. (Muestreo; no re-audité línea a línea — ya lo hice en R6.)
- **Figuras:** 4 TikZ. **Verifiqué la Fig. 3** (la del testigo de facetas, la de mayor
  riesgo): convertí baricéntrico→cartesiano y `P_0=(0,⅓,⅔)→(0.6667,0.5773)`, etc. —
  coincide exacto con el TikZ. **La figura usa los vértices CORRECTOS.**
- **Compila:** 17 pp, 0 errores / 0 undefined / 0 overfull (recompilé desde cero). ✓

## ⚠ Nota permanente: confusión reincidente chat vs paper (inofensiva, pero vigilar)
Por **segunda vez** el investigador escribió en el reporte los vértices del testigo de
facetas como `(0,½,½),(½,0,½),(½,½,0)` (triángulo **medial** → átomo en ½, testigo
INVÁLIDO). El paper y la Fig. 3 **siempre** tuvieron el inscrito `(0,⅓,⅔),(⅔,0,⅓),(⅓,⅔,0)`
(correcto, verificado). Es un lapsus verbal, no del manuscrito. **Riesgo:** si el
investigador algún día "corrige" la figura para que coincida con su chat, la rompe. Dejar
constancia: el testigo correcto es el **medial-dual / inscrito de vértices `k/3`**, NO el
medial de puntos medios.

---

## Estado del deliverable
17 pp, todo [PROVED] verificado o citado; los dos overclaims que motivaban el "bordering on
reject" de Rosa están eliminados; el único hueco de prueba real (Thm 3.2) resuelto. **Único
pendiente que el investigador no puede cerrar:** el bloque de autor (identidad real).

## Próximo paso
- **R8-7 (entrega, me toca):** copia congelada `drafts/entregas/...pasada4.{pdf,tex}` +
  hand-off `notes/52-R8-7`. Es la 1ª vez que Rosa verá §7–§8 y la caracterización sin
  overclaims. Entregar con el mapa de las 10 objeciones→resolución.
- **Cola:** R8-6 (estabilidad `ε` de la familia, con A.1 general-τ) · R8-8 (moonshot).
- **Sin órdenes nuevas de investigación esta ronda:** la Ronda 8 era de precisión y está
  cumplida. La siguiente ronda depende del dictamen de Rosa (pasada 4). Mantener el foco:
  no agregar teoremas hasta que la auditoría externa valide §7–§8.
