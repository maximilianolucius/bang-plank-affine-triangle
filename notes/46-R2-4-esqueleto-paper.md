# R2-4 — Esqueleto del paper del núcleo probado (deliverable garantizado)

> Date: 2026-07-01. Status: **[ESQUELETO / SCOPE]**. Ensambla lo firme con alcance honesto.
> NO reclama la conjetura ni la vía Ambrus. Todas las piezas están probadas y verificadas.

---

## 0. Título y marco (honesto)

**Título de trabajo:** *"Transport and tiling bounds for the affine plank problem on the
triangle: new sharp cases and a normalizer obstruction."*

**Marco (alcance explícito, para el referee):** este es un estudio del **triángulo como cuerpo
concreto** + desarrollo de método (transporte por medida testigo, teselación por celdas).
**NO** es un ataque a la conjetura general vía Ambrus: la reducción de Ambrus produce símplices
de dimensión `2N−1` (`N`=nº de planks), y **el triángulo (2-símplex) nunca es un target**
(`notes/40/43-P2`). Los resultados son nuevos casos sharp y un mapa de obstrucciones, no la
conjetura.

**Posicionamiento:** primer uso del **método de transporte por medida de marginal uniforme**
para casos NO-faceta del plank afín, con el **primer caso tight no-faceta con rigidez**
(medianas). Complementa Bakaev–Yehudayoff 2026 (cota general `2/(1+√d)`) y Gardner 1988
(no-existencia de medida para direcciones densas).

---

## 1. Estructura y contenido (qué sección usa qué nota)

### §1 Introducción
- Conjetura afín de Bang (`Σrw≥1`), historia, estado abierto (incl. **abierto en el plano /
  ≥3 planks**, verbatim B-Y `refs/2602.20290`; Hunter solo hizo 2 planks + igualdad).
- Modelo del triángulo = 2-símplex; planks = franjas `{f_i∈I_i}`, `f_i:Δ→[0,1]` afín normalizada.
- Contribuciones (lista de teoremas §2–§5) + alcance honesto (§0).

### §2 Cotas por medida única (baseline)
- **Teorema `1/d`** (`notes/08`): `Σrw≥1/d` por medida uniforme + Brunn–Minkowski; sharp en el
  símplex. Elegante, self-contained. [PROVED]
- **Techo de la medida única** (`notes/08` + Gardner `refs/gardner1988`): una sola medida no
  pasa de `1/d` para `≥3` direcciones genéricas; cita a **Gardner Thm 4** (no-existencia para
  `Θ` denso) y **Example 1** (triángulo, facetas). [cita fuente primaria]

### §3 Casos sharp por acoplamiento/transporte
- **2 direcciones → `Σrw≥1`, sharp** (`notes/10-12`): acoplamiento de marginales uniformes;
  existencia por **Gardner Thm 1** (`≤2` direcciones, `notes/43-P3`). [PROVED, cita Gardner]
- **Faceta-paralelo, toda dimensión → `Σrw≥1`, sharp** (`notes/23-A2`): sumset 1-D. [PROVED]
- **3 facetas + 1 plank arbitrario → `Σrw≥1`** (`notes/30 §1`, argumento de fibras, sin Hunter).
  [PROVED, auditado línea a línea]

### §4 El resultado central: medianas (primer tight no-faceta con rigidez)
- **Teorema (medianas):** 3 planks medianos que cubren `Δ` ⟹ `Σr≥1`, **igualdad sii
  `I_i=[1/3,2/3]`**. [PROVED completo]
  - Cota: transporte con **medida del perímetro** (marginal uniforme en las 3 medianas,
    `notes/36`).
  - Rigidez: partición del perímetro + enumeración exacta (3 teselaciones candidatas) +
    **centroide como testigo interior** que elimina las 2 falsas (`notes/45`, R2-2).
- **Caracterización necesaria** (`notes/37`): una terna admite medida de marginal uniforme sii
  las 3 líneas `{u_i=½}` concurren en `Δ` (`1ᵀV⁻¹1=2`). Familia codim-1; incluye genéricas;
  excluye facetas. [necesidad PROVED; suficiencia OPEN — es la pregunta finita abierta de
  Gardner, `notes/43-P3`].

### §5 Obstrucciones (mapa de por qué es difícil)
- **Obstrucción del normalizador `N_c`** (`notes/44`, R2-1): el argumento de signos de Bang
  (vía cuerda, Lema 2.3 de Verreault) topa exactamente en la cuerda `ℓ`; `N_c>ℓ` es
  inalcanzable por ese método (`c*=0` para Bang). Batir `2/(1+√d)` requiere un testigo de
  acoplamiento, no el sistema de Bang. [PROVED como no-go de método]
- **Medida única capada** (Gardner + `notes/08`); **posición-dependencia** (`notes/23 D12`);
  **quantifier-swap** (`notes/23 D11`). El certificado ganador debe ser
  entero/posición-dependiente/de-borde/escape-de-TODAS (`notes/23 E`).

### §6 Conclusión y problemas abiertos
- Bang(3) general (abierto); suficiencia de concurrencia (pregunta finita de Gardner);
  `S_c≥1` para `c>0` (requiere acoplamiento, `notes/43-P1`+`44`).

---

## 2. Tabla de teoremas (estado, para el abstract)

| # | Resultado | Estado | Fuente propia |
|---|---|---|---|
| A | `Σrw≥1/d`, sharp símplex | PROVED | `08` |
| B | 2 direcciones `Σrw≥1`, sharp | PROVED (cita Gardner Thm1) | `10-12` |
| C | faceta-paralelo, toda dim, sharp | PROVED | `23` |
| D | 3 facetas + 1 arbitrario | PROVED | `30 §1` |
| **E** | **medianas: `Σrw≥1`, igualdad sii `[1/3,2/3]`** | **PROVED (cota+rigidez)** | `36`,`45` |
| F | caracterización `1ᵀV⁻¹1=2` (necesaria) | PROVED (nec.) | `37` |
| G | no-go del normalizador `N_c` (método Bang) | PROVED | `44` |

**Cabecera honesta del abstract:** "Probamos nuevos casos sharp del plank afín para el
triángulo —incluyendo el **primer caso tight no-faceta con rigidez** (las medianas)— por un
método de transporte, y establecemos una obstrucción precisa (el normalizador entre cuerda y
ancho no es alcanzable por el argumento de Bang). No resolvemos la conjetura."

---

## 3. Qué NO incluir (higiene de alcance)
- NO presentar el triángulo como reducción de la conjetura (Ambrus da símplices dim `2N−1`).
- NO citar `S_c≥1` (`c>0`) como probable/probado (es OPEN; el método de Bang no lo da, `44`).
- NO usar afirmaciones de grilla como prueba (todo lo `[PROVED]` es exacto).
- NO la vía Euler-Jacobi/tórica (muerta, `notes/15/23`); a lo sumo mención en "métodos
  intentados".

## 4. Venue y siguientes pasos
- Venue plausible: *Mathematika* / *Discrete Comput. Geom.* / *Amer. Math. Monthly* (según
  extensión) — "nuevos casos sharp + rigidez + obstrucción" es sólido mid-tier.
- Redacción: ensamblar §2–§5 desde las notas citadas; añadir figuras (medianas tercio-central,
  la teselación del perímetro). Numérica certificada (`fractions`/`sympy`) ya disponible.
