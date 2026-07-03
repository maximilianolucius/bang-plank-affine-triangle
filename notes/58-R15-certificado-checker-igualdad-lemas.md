# R15 — Paquete de certificación (estándar 6 pilares): certificado + checker independiente; igualdad clasificada; lemas de soundness redactados; simetría del sandwich (negativa)

> Date: 2026-07-03. Ejecuta `auditorias/65` (consolidada). **Numeración
> congelada (Rosa lee la pasada 6): CERO cambios al `.tex`** — todo aquí, para
> integrar al descongelar. Regla de re-verificación nueva del jefe aplicada:
> toda re-verificación debe producir un ÁRBOL DISTINTO con el MISMO veredicto.
> Todos los números copiados de salidas de script.

## R15-1a/b (BLOQUEANTE) — certificado + verificador independiente

**Certificado** (`c3_sandwich_certificate.txt`, emitido por `emit_certificate`
en `c3_balanced_bb.py`): volcado preorden determinista del árbol COMPLETO del
run principal (`τ₀=(13/25,½,½)`, split 1/2). Diseño clave: **almacena solo la
forma del árbol** — por nodo interno `S k mid` (coordenada + punto de corte
exacto en ℚ), por hoja `L1 / L2 i / L4 i / L3E e / L3C σ` (regla + testigo
exacto) — y **NO las cajas**. El checker las reconstruye desde el cubo raíz,
forzando una re-derivación independiente de la aritmética de cajas.

**Checker** (`bb_certificate_check.py`, ~1 pág, criterio de de Bruijn):
NO importa NADA del buscador. Reimplementa desde cero geometría del triángulo,
`w₀(τ)`, clipping de polígonos exacto, y las cuatro reglas de poda. Verifica:
- **TESELACIÓN**: el stream es preorden de un árbol binario con raíz = cubo y
  cada split estrictamente interior (`lo < mid < hi`) en `[lo,mid]∪[mid,hi]`;
  al consumir todo el stream la pila queda vacía ⟹ las hojas parten `[0,1]⁶`
  (solape de medida cero). Identidad de árbol binario `hojas = internos + 1`.
- **PODAS**: cada hoja re-validada por su regla con su testigo, con lógica
  propia:
  - P1: `min_caja Σr > 1` (recomputado) ⟹ ningún config con `Σr≤1`.
  - P2: `min_caja r_i ≥ 1−w₀` (con `w₀` recomputado por el checker) ⟹ extremo
    (Teorema R13, analítico).
  - P4: caja fuerza plank `i` vacío ⟹ ≤2 planks (Thm 3.1, analítico).
  - P3: config agrandada `[l_i⁻,h_i⁺]` (superconjunto de todo plank de la
    caja) NO cubre, testificado por arista descubierta (1-D exacto) o celda de
    signo con **área racional > 0** (clipping exacto).
- **ALCANCE**: `τ` del header = `τ₀` reclamado; `w₀`/`BAL` del header = los que
  el checker recomputa (detecta manipulación).
- Emite SHA-256 del certificado y **`CERTIFICATE VALID`** como autoridad final.

**[CERTIFICATE VALID — verificado.]** El checker independiente
(`bb_certificate_check.py`) recomputó `w₀=2/25`, validó teselación
(812 650 internos + 812 651 hojas, identidad de árbol binario OK), re-validó
las 812 651 hojas con código propio y confirmó el SHA. Salida:
```
tree: 812650 internal splits, 812651 leaves
leaf rules: P1=286024 P2=53907 P3edge=428672 P3cell=2354 P4=41694
certificate SHA-256: ead66ff2cfd547f8...  CERTIFICATE VALID
```
Conteos idénticos al run principal (P3=428672+2354=431026 ✓). Hashes (16 hex):
buscador `b2468aa9acc91f4f`, certificado `ead66ff2cfd547f8` (12 062 803 B),
checker `90a25ce8ea059abe`.

**Baseline de des-computerización ("hojas restantes"):** P2 (53 907, extremo →
R13 analítico) y P4 (41 694, vacío → Thm 3.1 analítico) YA son analíticas. El
núcleo genuinamente-máquina son P1+P3 = **717 050 hojas**. Dato estructural:
de las P3, solo **2 354** necesitan el test 2-D de celda con área>0; las otras
428 672 se cierran con el test 1-D de arista descubierta (Lem 10.2, reducción
a aristas) — la frontera hace casi todo el trabajo, el mecanismo interior es
una corrección pequeña. Lead para el thin-plank/des-computerizar: la historia
de aristas es casi todo.

**Auto-auditoría del checker (no-vacuidad) — hecha:** cuatro controles
negativos, todos RECHAZADOS como se esperaba: (1) header `w₀` manipulado
(`3/25`) → "w0 mismatch"; (2) split no-interior (`mid=5`) → "non-interior
split"; (3) hoja con P1 falsa → "P1 invalid at ..."; (4) árbol truncado →
"tree incomplete: 10 unexpanded boxes remain". El checker tiene dientes: un
certificado corrupto no pasa. (Disciplina "¿mi verificador detectaría un
fallo?" aplicada al propio verificador.)

**Doble árbol como corroboración adicional** (no sustituto del checker, por el
caveat de modo común que el jefe mantiene): run principal (split ½,
1 625 301 cajas) y verificación genuina (terna rotada `(½,½,13/25)` + split
5/11, 1 040 919 cajas) — árboles distintos, ambos `QUEUE EMPTY`.

## R15-1d — clasificación de igualdad: `C₃(sandwich)=1` alcanzado SOLO trivialmente [PROVED]

Dos piezas:

1. **Estrictitud del balanceado [PROVED, del propio B&B]:** toda cobertura por
   3 planks propios balanceada vive en una hoja; no es P2 (no extrema) ni P4
   (propios) ni P3 (una cobertura no puede estar en hoja P3, cuya config
   agrandada no cubre y la contiene); luego P1, cuya caja CERRADA tiene
   `min Σr > 1` ⟹ el config tiene `Σr > 1`. Así **ninguna cobertura balanceada
   de 3 planks propios alcanza `Σr = 1`** (condición cerrada, sin problema de
   frontera). Igual, ninguna cobertura de 3 planks propios cubre con `Σr ≤ 1`.
2. **2-planks (`r_k=0`) — solo triviales [PROVED, exacto]** (`r15_equality.py`):
   para los tres pares, minimizando `|I_i|+|I_j|` sobre coberturas exactas
   (imagen-triángulo evita las 4 esquinas complementarias; clipping exacto;
   óptimos en breakpoints exactos):
   - `(u1,u2)`: min propio = **31/25 = 1.24** (> 1)
   - `(u1,u3)`: min propio = **31/25 = 1.24** (> 1)
   - `(u2,u3)`: min propio = **5/4 = 1.25** (> 1)
   El mínimo global 1 se alcanza solo en las triviales (un intervalo `=[0,1]`).
   Con Gardner (`Σr ≥ 1` para 2 direcciones) esto es completo: **no hay
   cobertura tight propia de 2 planks**.

**Conclusión (enunciado de igualdad, listo para el .tex):** `C₃(τ₀)=1`,
alcanzado si y solo si la cobertura es trivial (un plank pleno `[0,1]`, los
otros dos de ancho 0). Sin coberturas tight propias de 2 ni de 3 planks.

## R15-2b — simetría del sandwich: NO existe (hallazgo negativo) [PROVED]

La reflexión `σ` (swap B↔C) manda `u₂ ↦ 1−u₃`, `u₃ ↦ 1−u₂` (flip-simétricas),
pero `u₁ ↦ (13/25, 1, 0) = 1−(12/25,0,1) ≠` ningún `u_k` ni su flip
(necesitaría `τ₁ = 12/25`, no `13/25`). **El sandwich no tiene simetría de
reflexión exacta**, así que la idea aspiracional de "partir el árbol por
simetría" NO aplica a `τ₀`. La simetría 3-fold completa vive en la familia
tilt `τ=(t,t,t)` (R14-2) — candidato natural a reducción ~3× cuando se
parametrice, no aquí. Registrado para no perseguir una reducción inexistente.

## R15-2a — thin-plank lemma: análisis y estado

Espejo del régimen extremo: plank fino `r₁ ≤ w₀'` ⟹ `Δ∖P₁` son dos casquetes
GRANDES convexos `{u₁≤l₁}`, `{u₁≥h₁}` que `P₂∪P₃` deben cubrir a la vez.
Herramienta 2-plank por casquete (`r₂/w₂(cap)+r₃/w₃(cap) ≥ 1`) + acoplamiento
de posición (ambos casquetes, mismos intervalos), como el caso B de R13.
[EN CURSO — el análisis reproduce la estructura de R13; el valor es
des-computerizar, NO probar (el árbol ya cubre la banda fina vía P1/P3). Es
investigación no-bloqueante, por orden del jefe.] Métrica "hojas restantes":
el núcleo genuinamente-máquina son las hojas P1+P3 (P2 = R13 analítico,
P4 = Thm 3.1 analítico); baseline exacto tras el checker.

## Cola

- Correr el checker → `CERTIFICATE VALID` + SHA + conteos (este turno).
- R15-3 (documentación, tras `CERTIFICATE VALID`): los 6 pilares al Apéndice B
  + lemas de soundness/reducción/terminación como matemática (rama de nota,
  .tex congelado).
- Thin-plank lemma (des-computerizar) · B&B parametrizado en τ · sandwich D
  exacto: fondo.
