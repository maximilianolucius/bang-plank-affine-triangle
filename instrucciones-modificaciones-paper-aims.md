# Instrucciones de modificación del paper "Bang / affine plank triangle" — para sesión ejecutora

> Fecha: 2026-07-05. Autor de estas instrucciones: sesión "bang" (Claude).
> **Estas instrucciones NO fueron ejecutadas.** La sesión que las ejecute debe seguirlas
> en orden, verificando cada paso. Idioma del paper: inglés (no cambiar).

## 0. Contexto y preliminares

- **Máquina:** 172.16.0.144 (user `maxim`). Repo: `/home/maxim/PycharmProjects/bang-plank-euler-jacobi/`.
- **Versión de partida (canónica):** `drafts/entregas/affine-plank-triangle-2026-07-03-pasada8.tex`
  (≡ "pasada 8", 35 pp., compila limpio con `pdflatex`, clase `amsart`).
  El working draft `drafts/affine-plank-triangle.tex` debería ser idéntico; verificar con `diff` antes de elegir base.
- **Ancillary:** `drafts/ancillary/` (23 scripts + `c3_sandwich_certificate.txt`, ~12 MB). Forma parte del entregable de submission (ver §5.D).
- **Regla de trabajo:** crear una rama de trabajo nueva, p. ej. `drafts/entregas/affine-plank-triangle-aims-v1.tex` + copia del directorio. NUNCA editar la pasada 8 in place. Compilar tras cada bloque de cambios (`pdflatex` ×2, exigir 0 errores y revisar warnings de refs).
- **R11 (.144) no debe usarse para trabajo pesado** — compilar LaTeX está bien; no lanzar búsquedas B&B ni recomputar certificados ahí sin pedido explícito.
- Ya existe una implementación de referencia del cambio de autoría (formato `amsart`) en el zip `~/Downloads/bang-plank-affine-triangle-entregable-2026-07-04.zip` (y quizá `/tmp/bang-entregable/` si no fue purgado).

---

## 1. Autoría (CUATRO autores — actualizado 2026-07-06)

> **Cambio 2026-07-06:** el paper pasó de 2 a **4 autores**. La versión canónica que ya
> compila con esta lista está en `drafts/affine-plank-triangle.tex` del repo (commit
> `3d2aac2`, "Update author list to four authors") y en el entregable
> `~/Downloads/bang-plank-affine-triangle-entregable-2026-07-06.zip`. Partir de ahí; los
> datos de abajo son la fuente de verdad para el bloque AIMS.

Orden y datos exactos (los cuatro, en este orden):

1. **Ibrahim Alraddadi** (primer autor)
   - Affiliation: Department of Mathematics, Faculty of Science, Islamic University of Madinah, Madinah, Saudi Arabia
   - Email: `ialraddadi@iu.edu.sa`
2. **Maximiliano Lucius** (segundo autor; **autor corresponsal** salvo indicación en contra del usuario)
   - Affiliation: **Independent Researcher, CABA, Argentina** (decisión confirmada por el
     usuario 2026-07-06; descartada la variante "Aureus Technology LLC" que se había
     considerado antes — usar CABA/Argentina en todas las apariciones).
   - Email: `maximiliano.lucius@gmail.com`
3. **Hijaz Ahmad** (tercer autor) — afiliación múltiple:
   - (a) Department of Mathematics, Faculty of Science, Islamic University of Madinah, Madinah, Saudi Arabia
   - (b) Operational Research Center in Healthcare, Near East University, Near East Boulevard, PC: 99138 Nicosia/Mersin 10, Turkey
   - (c) Department of Mathematics, College of Science, Korea University, 145 Anam-ro, Seongbuk-gu, Seoul 02841, South Korea
   - Email: `hijazahmad@korea.ac.kr`
4. **Waleed Mohammed Abdelfattah** (cuarto autor) — afiliación múltiple:
   - (a) College of Engineering, University of Business and Technology, Jeddah 23435, Saudi Arabia
   - (b) Department of Engineering Mathematics and Physics, Faculty of Engineering, Zagazig University, P.O. 44519, Egypt
   - Email: `w.abdelfattah@ubt.edu.sa`

El markup concreto depende del template AIMS (§2). En el template de AIMS Mathematics los autores van en un solo bloque `\author[...]{...}` numerado con superíndices por afiliación y `*` para el corresponsal; con afiliaciones múltiples (Ahmad, Abdelfattah) un autor lleva varios superíndices (`\affil{3,4,5}`). Seguir EXACTAMENTE el ejemplo del template descargado, no el de esta nota; enumerar todas las afiliaciones distintas una sola vez en el bloque `\address`.

**Nota de integridad (dejar constancia, decisión del usuario ya tomada):** el orden y la lista de autores fueron decididos por el usuario; no revertir ni cuestionar en la ejecución.

---

## 2. Conversión al template de AIMS Mathematics

Datos verificados el 2026-07-05 contra aimspress.com (Instructions for Authors + template zip real, versión 2025-03-17).

### 2.1 Obtener el template

- Zip oficial: `https://www.aimspress.com/aimspress-upload/news/math/202531774922592.zip`
  ("Tex Template" en Instructions for Authors: `https://www.aimspress.com/math/news/solo-detail/instructionsforauthors`).
- **Copia local ya descargada:** `aims-math-latex-template.zip` junto a este archivo en el repo (mismo contenido; usarla si el link cambia).
- Contenido relevante: `Template-AIMS Mathematics.tex` (ejemplo), `Template-AIMS Mathematics.pdf`, `aims.cls`, `AIMS_unsrt.bst`, y `figure.pdf`, `logo.pdf`, `logobottom.pdf` (los logos son requeridos por la clase para header/footer — deben quedar junto al .tex; obliga a compilar con **pdflatex**).

### 2.2 Conversión desde `amsart`

1. `\documentclass{aims}` (la clase es un wrapper de `article`; carga graphicx, xcolor, amsfonts/amssymb/amsmath/**amsthm**, hyperref, geometry, float, caption).
2. **La clase NO define entornos de teorema** — portar TODOS los `\newtheorem` de la pasada 8 (theorem, lemma, proposition, corollary, remark, problem, conjecture, definition...) al preámbulo, con la misma numeración interna (el paper usa referencias cruzadas densas; tras compilar, verificar que `thm:char`, `thm:sandwichbang`, etc. resuelvan igual).
3. Copiar del template los macros de metadata que la clase espera, con placeholders:
   `\typeofarticle{Research article}`, `\currentvolume`, `\currentissue`, `\currentyear`, `\ppages`, `\DOI`, `\Received`, `\Revised`, `\Accepted`, `\Published` (producción los completa).
4. El template usa `\usepackage{txfonts}` (Times) y `\numberwithin{equation}{section}` — adoptarlos, PERO: la pasada 8 tiene macros propios y posiblemente símbolos especiales; compilar inmediatamente tras el cambio de fuente y revisar que ningún símbolo se rompa. Si `txfonts` choca con algún paquete del paper, resolver caso a caso (txfonts es viejo; un fallback aceptado es `newtxtext,newtxmath`, pero primero intentar lo que trae el template).
5. Añadir `\usepackage{lineno}` + `\linenumbers` para la versión de submission (cortesía a referees, pedido explícito de AIMS).
6. Migrar los macros propios del paper (`\rw`, `\wid`, `\Leb`, etc.) tal cual.
7. Headings en *sentence case* (solo la primera palabra con mayúscula) — revisar títulos de secciones; máx. 4 niveles.
8. **Apéndices:** el paper tiene 2 (`app:tilings`, `app:ancillary`). El template no trae ejemplo de apéndice; mantener `\appendix` + `\section` y verificar la numeración compilando; si queda fea, renombrar como secciones finales numeradas. Los apéndices van ANTES del end matter de §2.4.

### 2.3 Front matter (aquí se implementa la autoría de §1)

Orden en esta clase: `\title`, `\author`, `\address`/`\corraddr`, luego `\begin{abstract}...\end{abstract}`, `\keywords{...}`, y **recién después `\maketitle`** (la clase captura abstract y keywords en cajas que `\maketitle` tipografía).

```latex
\author{Ibrahim Alraddadi\affil{1}
Maximiliano Lucius\affil{2,}\corrauth
Hijaz Ahmad\affil{1,3,4}
and
Waleed Mohammed Abdelfattah\affil{5,6}}
\shortauthors{I. Alraddadi et al.}
\address{%
\addr{\affilnum{1}}{Department of Mathematics, Faculty of Science,
Islamic University of Madinah, Madinah, Saudi Arabia}
\addr{\affilnum{2}}{Independent Researcher, CABA, Argentina}
\addr{\affilnum{3}}{Operational Research Center in Healthcare, Near East
University, Near East Boulevard, PC: 99138 Nicosia/Mersin 10, Turkey}
\addr{\affilnum{4}}{Department of Mathematics, College of Science, Korea
University, 145 Anam-ro, Seongbuk-gu, Seoul 02841, South Korea}
\addr{\affilnum{5}}{College of Engineering, University of Business and
Technology, Jeddah 23435, Saudi Arabia}
\addr{\affilnum{6}}{Department of Engineering Mathematics and Physics,
Faculty of Engineering, Zagazig University, P.O. 44519, Egypt}}
\corraddr{maximiliano.lucius@gmail.com}
```

- Nota: afiliación 1 es compartida (Alraddadi y Ahmad) — se enumera una sola vez; Ahmad lleva `\affil{1,3,4}` y Abdelfattah `\affil{5,6}`. Verificar contra el ejemplo real del template `aims.cls` cómo se listan múltiples afiliaciones por autor y ajustar.
- `\corrauth` marca al corresponsal con `*`; `\corraddr` genera el párrafo "\* Correspondence: ...". AIMS pide para el corresponsal dirección de contacto exacta; email es lo mínimo — si piden teléfono en JAMS, lo completa el usuario.
- Afiliación 2 de Maximiliano: **Independent Researcher, CABA, Argentina** (confirmado, ver §1).
- Abstract: **máximo 300 palabras**, sin referencias. Contar las palabras del abstract de la pasada 8; si excede, recortar (proponer el recorte al usuario, no mutilar en silencio).
- Keywords + MSC (la clase no tiene macro de MSC; va dentro de `\keywords` como en el template):

```latex
\keywords{
{plank problem, affine plank conjecture, relative width, witness measure,
optimal transport, computer-assisted proof, convex geometry}
\newline
\textbf{Mathematics Subject Classification:} 52A40, 52A38, 52C15}
```

  (5–10 keywords; si la pasada 8 trae `\subjclass`, partir de esos códigos y verificar contra MSC 2020.)

### 2.4 End matter obligatorio (en este orden, todas `\section*`)

1. **`Author contributions`** — OBLIGATORIA en papers multi-autor; roles CRediT (https://credit.niso.org/). **Redacción sensible: la decide el usuario** — dejar un placeholder `[PENDIENTE: wording del usuario]` y avisarle; no inventar contribuciones.
2. **`Use of Generative-AI tools declaration`** — en este paper es **OBLIGATORIA y no negociable**: el manuscrito se produjo con asistencia sustancial de IA (plataforma de agentes; búsqueda B&B guiada; redacción asistida). AIMS trata el uso no declarado como violación de estándares de publicación (retractable). Redactar con honestidad: qué herramientas, para qué (búsqueda de la prueba, redacción, verificación auxiliar) y qué validaron los humanos + el checker independiente. Borrador de partida (ajustar con el usuario):
   > *The authors declare they have used Artificial Intelligence (AI) tools (large-language-model agents) in the creation of this article: in the exploration and drafting of proofs, in the design of the branch-and-bound search, and in the preparation of the manuscript text. All mathematical statements were verified by the authors; the computer-assisted certificate of Theorem [sandwichbang] is validated by an independent checker in exact rational arithmetic, as described in Appendix [ancillary].*
3. **`Acknowledgments`** — aquí va TODO el funding con número de grant (AIMS no usa sección Funding separada). Si no hay funding, puede omitirse o declararse sin financiamiento — confirmar con el usuario.
4. **`Conflict of interest`** — OBLIGATORIA. Si aplica: `All authors declare no conflicts of interest in this paper.`
5. Referencias (§4).
6. **`Supplementary`** — después de la bibliografía; aquí se referencia el paquete ancillary (§5.D). AIMS acepta supplementary hasta ~100 MB (el nuestro ~13 MB zip: OK); código/certificado como supplementary files o depósito externo (Zenodo) citado.

### 2.5 Referencias en formato AIMS

- Numeradas, corchetes, **estrictamente por orden de primera citación** (comportamiento `unsrt`). Formato de la casa para artículo:
  `Y. Benoist, P. Foulon, F. Labourie, Flots d'Anosov..., J. Amer. Math. Soc., 5 (1992), 33–74. https://doi.org/10.1090/...`
  — iniciales + apellido, título en redonda, revista abreviada (ISO 4) en itálica, **volumen en negrita** (año), páginas, y el DOI como URL al final. Primeros 6 autores, luego *et al.*
- Dos vías (elegir una y ser consistente):
  a. Mantener `thebibliography` manual reformateando cada entrada a mano al estilo de arriba. La clase extiende `\bibitem` con `\bibitem{key}[10.xxxx/doi]` (linkea el título) y macros `\doilink{...}`, `\arXiv{...}` — usarlas.
  b. Migrar a BibTeX con `AIMS_unsrt.bst`. OJO: ese .bst ignora el campo `doi` — poner el DOI en el campo `url` como `https://doi.org/...`.
  Con ~24 referencias, la vía (a) con `\doilink`/`\arXiv` es la de menor riesgo.
- Preprints: citar como `arXiv:XXXX.XXXXX` con `\arXiv{}` (BY26, MOM26, Verreault).
- Recordar reordenar: `unsrt` = orden de aparición, el `thebibliography` actual está alfabético.

### 2.6 Mecánica de submission (informativo, para la nota al usuario)

- Se somete el **PDF compilado** vía JAMS: `https://aimspress.jams.pub/` (el fuente se pide en producción).
- Figuras: EPS/PNG/PDF/JPEG, ≥300 dpi, además como archivos separados; captions abajo (figuras) / arriba (tablas).
- Sin límite de extensión (35 pp. OK). APC: **2000 USD** por paper aceptado (tarifa oficial 2026; +80 USD si AIMS formatea). Mencionarlo al usuario en el reporte final.

---

## 3. Afiliación de Maximiliano Lucius

**Independent Researcher, CABA, Argentina** — decisión final del usuario (2026-07-06), ya en el `.tex`/PDF canónico. La variante "Aureus Technology LLC" quedó descartada. `grep -i "aureus" *.tex` debe dar 0 resultados.

---

## 4. Expansión de referencias (7 → ≥24)

### 4.0 Estado actual y reglas

La pasada 8 tiene **7 referencias** (`Ambrus, Ball91, Bang51, BY26, Gardner88, Sion58, Verreault`) y 21 sitios de citación, todos en `thebibliography` manual al final del .tex.

**Reglas duras para la sesión ejecutora:**
1. **Verificar cada dato bibliográfico contra fuente primaria** (arXiv / zbMATH / MathSciNet / página del journal) ANTES de incluirlo. Los datos de abajo provienen de un deep research de 2026-07-04 pero volumen/páginas marcados `[VERIFICAR]` no fueron confirmados contra la fuente — no copiarlos a ciegas.
2. **No citar por citar:** cada referencia nueva entra con una frase de anclaje que la haga genuinamente pertinente (se da el anclaje sugerido en cada caso). Si al leer el abstract la referencia no calza, descartarla y anotarlo.
3. Convertir TODO al formato de referencias de AIMS (§2): numeradas por orden de aparición, estilo de la casa. Las claves (`\cite{...}`) pueden conservarse.
4. Completar la entrada `Ambrus` existente: hoy dice "manuscript, 2010" con URL de renyi.hu — verificar que la URL siga viva y si el manuscrito fue publicado formalmente; si no, mantener como manuscript con fecha de acceso.

### 4.1 Bloque histórico / literatura plank (anclar en la Introducción)

Anclaje: la Intro abre con "affine plank conjecture~\cite{Bang51,Ambrus}" (~l. 78) y cita a Ball91 y BY26. Insertar 1–2 frases de historia: el problema de planks se origina en Tarski (1932, resuelto por Bang 1951), y la comunidad lo ha revisitado en surveys.

| # | Clave | Entrada (verificar datos) | Anclaje |
|---|-------|---------------------------|---------|
| 1 | `Tarski32` | A. Tarski, *Uwagi o stopniu równoważności wielokątów*, Parametr **2** (1932), 310–314. | Frase histórica en Intro: el problema original de Tarski que Bang resolvió. |
| 2 | `Moese32` | H. Moese, *Przyczynek do problemu A. Tarskiego "O stopniu równoważności wielokątów"*, Parametr **2** (1932), 305–309. [VERIFICAR páginas] | Junto a Tarski32 (caso especial temprano). |
| 3 | `Alexander68` | R. Alexander, *A problem about lines and ovals*, Amer. Math. Monthly **75** (1968), 482–487. | Intro, al enunciar la conjetura afín. **VERIFICAR la atribución** (la forma afín se atribuye según la fuente a Bang o a Alexander; Verreault y BY26 dan la genealogía — seguir la de ellos). |
| 4 | `Ball01` | K. Ball, *The complex plank problem*, Bull. London Math. Soc. **33** (2001), 433–442. | Intro, tras la mención de Ball91: "and its complex analogue \cite{Ball01}". |
| 5 | `OM21` | O. Ortega-Moreno, *An optimal plank theorem*, Proc. Amer. Math. Soc. **149** (2021), 1225–1237. [VERIFICAR vol/pp] | Intro o §Open problems: técnica moderna de planks vía polinomios/análisis. |
| 6 | `Bezdek13` | K. Bezdek, *Tarski's plank problem revisited*, en *Geometry — Intuitive, Discrete, and Convex*, Bolyai Soc. Math. Stud. **24**, Springer, 2013. [VERIFICAR pp] | Junto a `Verreault` (l. 462): "surveys \cite{Verreault,Bezdek13}". |
| 7 | `BezdekBezdek95` | A. Bezdek, K. Bezdek, *A solution of Conway's fried potato problem*, Bull. London Math. Soc. **27** (1995), 492–496. | Intro o sección de aplicaciones: ancho relativo sucesivo (pariente directo del ancho relativo). |

### 4.2 Bloque programa de cubrimiento / direcciones modernas (anclar en §"Open problems and the covering-constant program")

Esa sección ya discute las constantes C, C^111 y el estado del arte vía BY26; agregar un párrafo corto "other modern routes" citando:

| # | Clave | Entrada (verificar datos) | Anclaje |
|---|-------|---------------------------|---------|
| 8 | `AKP19` | A. Akopyan, R. Karasev, F. Petrov, *Bang's problem and symplectic invariants*, J. Symplectic Geom. **17** (2019). [VERIFICAR número/pp] | Ruta simpléctica al problema de Bang. |
| 9 | `GKP22` | A. Glazyrin, R. Karasev, A. Polyanskii — paper del método polinomial para planks. **[VERIFICAR título y venue exactos — el research lo identifica como el "GKP polynomial method", posiblemente IMRN ~2022; buscar en arXiv por autores]** | Ruta polinomial. |
| 10 | `MOM26` | Martínez, O. Ortega-Moreno (VERIFICAR lista de autores y título en arXiv:2605.28744, mayo 2026), solución de la polarización fuerte vía identidad Euler–Jacobi. Citar como **preprint**. | §Open problems: la dirección "Euler–Jacobi para anchos relativos" (es una de las direcciones declaradas del programa). |
| 11 | `Pinasco23` | D. Pinasco, *On the n-th linear polarization constant of* $\mathbb R^n$, Math. Nachr. **296** (2023), no. 8, 3593–3605, DOI 10.1002/mana.202200026. | Junto a Ball01/MOM26: puente planks↔polarización. (Opcional pero recomendado: es literatura de polarización directamente citada por la línea M–OM.) |

### 4.3 Bloque transporte / marginales (anclar en §2 "The transport defect" y §7 "Duality")

El defecto de transporte D_K(u) es un problema de medidas con marginales prescritas; hoy el paper no cita NADA de esa literatura — es la laguna bibliográfica más señalable por un referee.

| # | Clave | Entrada | Anclaje |
|---|-------|---------|---------|
| 12 | `Strassen65` | V. Strassen, *The existence of probability measures with given marginals*, Ann. Math. Statist. **36** (1965), 423–439. | §sec:measure, al definir la medida testigo: "existence of measures with prescribed marginals is classical \cite{Strassen65,Kellerer84}". |
| 13 | `Kellerer84` | H. G. Kellerer, *Duality theorems for marginal problems*, Z. Wahrsch. Verw. Gebiete **67** (1984), 399–432. | §sec:defect, junto a Sion58: la dualidad del defecto es de la familia de dualidades de problemas marginales. |
| 14 | `Villani09` | C. Villani, *Optimal Transport: Old and New*, Grundlehren **338**, Springer, 2009. | §sec:measure, primera aparición de "transport": referencia general. |
| 15 | `Schneider14` | R. Schneider, *Convex Bodies: The Brunn–Minkowski Theory*, 2nd ed., Encyclopedia Math. Appl. **151**, Cambridge Univ. Press, 2014. | Subsección de terminología (ancho, función soporte). |

### 4.4 Bloque computer-assisted / verificación (anclar en `rem:boundary` y Appendix `app:ancillary`)

El paper defiende el estándar "certificado + checker independiente" sin citar el linaje. Anclar en la Remark "the human/machine boundary" (~l. 2722) y/o al inicio del apéndice de ancillary:

| # | Clave | Entrada | Anclaje |
|---|-------|---------|---------|
| 16 | `AppelHaken77` | K. Appel, W. Haken, *Every planar map is four colorable. Part I: Discharging*, Illinois J. Math. **21** (1977), 429–490. | Precedente clásico de prueba computer-assisted. |
| 17 | `Hales17` | T. Hales et al., *A formal proof of the Kepler conjecture*, Forum Math. Pi **5** (2017), e2. | Estándar Flyspeck de verificación formal. |
| 18 | `HKM16` | M. J. H. Heule, O. Kullmann, V. W. Marek, *Solving and verifying the Boolean Pythagorean triples problem via cube-and-conquer*, en SAT 2016, LNCS **9710**, Springer, 228–245. | Estándar certificado-verificable a gran escala (análogo directo del árbol de 812.651 hojas). |
| 19 | `mathlib20` | The mathlib Community, *The Lean mathematical library*, en CPP 2020, ACM, 367–381. | Mención de formalización como asíntota (frase tipo "a Lean formalization of the checker is a natural next step"). |

### 4.5 Conteo y verificación final

7 existentes + 12 obligatorias (4.1–4.4 sin las opcionales) + opcionales ⇒ **24–26 referencias**. Tras insertar:
- `grep -c bibitem` (o contar el .bbl) ≥ 22;
- toda `\cite` resuelve (0 warnings "Citation undefined");
- ninguna referencia queda sin citar en el texto (AIMS lo objeta);
- releer cada frase de anclaje: debe leerse natural, no "reference stuffing". Ante la duda, menos es más: preferible 22 referencias bien ancladas que 26 forzadas.

---

## 5. Correcciones imprescindibles al contenido (hallazgos del panel de referato, 2026-07-04)

Estas cuatro son las que considero **absolutamente imprescindibles** antes de someter. Provienen de una evaluación con 3 agentes referee adversariales + lectura propia sobre la pasada 8; el veredicto global fue "aceptación condicionada a revisión menor" con estos ítems como condiciones.

### (A) Errata load-bearing en `lem:noncover` — superíndice equivocado

- **Dónde:** Lemma "complete non-covering test" (`\label{lem:noncover}`, ~l. 2660–2665 de pasada 8), cláusula (b): dice `some sign cell $\{u_i<l_i^+\text{ or }u_i>h_i^+\}$`.
- **Problema:** la configuración agrandada se define en (P3) como $I_i^+=[l_i^-,h_i^+]$ (l. 2640). El complemento de $\{u_i\in I_i^+\}$ es $\{u_i<l_i^-\ \text{o}\ u_i>h_i^+\}$. El $l_i^+$ del lema debe ser $l_i^-$. Con $l_i^+$ el test declararía "no cubierto" en puntos que sí están cubiertos por la configuración agrandada — **unsound** para el prune (P3).
- **Acción:** (i) corregir el superíndice en el .tex; (ii) **auditar el checker** (`drafts/ancillary/`, checker independiente de `thm:sandwichbang`; y el searcher `c3_balanced_bb.py`) y confirmar que el código implementa $l_i^-$ (lo esperable: la errata sería solo tipográfica en el paper y el certificado sigue válido). Documentar el resultado de la auditoría en el commit message / nota. Si el código implementara $l_i^+$, **PARAR y escalar al usuario**: el certificado entero estaría comprometido.

### (B) Caso degenerado en la tricotomía de `thm:char` (direcciones facet-parallel / full edge no único)

- **Dónde:** Theorem "three-direction characterization" (`\label{thm:char}`, ~l. 867) y su prueba (casos (1)/(2)/(3) por full edges compartidos).
- **Problema:** la clasificación por "full edge" asume tácitamente que cada dirección normalizada tiene UN único full edge, i.e. $\tau_i\in(0,1)$. Una dirección con valores de vértice $(0,1,1)$ o $(0,0,1)$ (facet-parallel, $\tau_i\in\{0,1\}$) tiene **dos** full edges y los casos (1)–(3) no la clasifican sin ambigüedad. Contraejemplo de trabajo del panel: $u_1=(0,1,1)$, $u_2=(0,0,1)$, $u_3=(1,\tau_3,0)$.
- **Acción (elegir una, documentar cuál):**
  1. **Restricción explícita + remisión:** añadir a las hipótesis de `thm:char` que ningún $u_i$ es facet-parallel ($\tau_i\in(0,1)$ tras normalizar), y una Remark que remita los triples con direcciones facet-parallel a la sección de familias facet-parallel (§sec:sharp) donde ya están resueltas — verificando que efectivamente TODOS los casos mixtos (1 o 2 direcciones facet-parallel) quedan cubiertos por resultados existentes; si alguno no, tratarlo.
  2. **Extender la prueba:** rehacer la clasificación con una convención de full edge para $\tau_i\in\{0,1\}$ y chequear caso por caso que el enunciado (concurrencia ⟺ testigo) sobrevive.
  - La opción 1 es más barata y honesta; la 2 solo si los casos mixtos no están ya cubiertos.
- **Ojo:** el enunciado dice "pairwise non-parallel" — eso NO excluye facet-parallel (excluye $u_i\parallel u_j$ entre sí, no paralelismo a una faceta).

### (C) Hueco en la partición de la prueba de `thm:sandwichbang` — planks de ancho cero no vacíos

- **Dónde:** prueba de `thm:sandwichbang` (~l. 2705): "Partition three-plank coverings into (i) extreme, (ii) some plank empty, (iii) proper balanced."
- **Problema:** "proper" está definido como $r_i>0$ para todo $i$ (l. 2632); "empty" significa $I_i=\varnothing$. Un covering con algún $r_i=0$ pero $I_i=\{c\}$ (plank degenerado = una recta, NO vacío) no es proper ni tiene plank empty ⇒ **cae fuera de la partición** si además es balanced.
- **Fix sugerido (una frase):** en el caso (ii) reemplazar "some plank empty" por "some plank empty or of zero width", y justificar: si $r_i=0$, el plank $P_i$ es una recta; $\Delta\setminus P_i$ es denso en $\Delta$ y los otros dos planks son cerrados, de modo que cubren $\overline{\Delta\setminus P_i}=\Delta$; entonces `thm:twodir` aplica a esos dos planks y da $\sum r\ge1$. Verificar que el enunciado de `thm:twodir` realmente soporta esta invocación (cubrimiento por dos planks de a lo sumo dos direcciones no paralelas).
- Chequear también que (P4) ($l_i^->h_i^+$, "plank empty") y el checker no dependen de la distinción empty vs ancho-cero (el certificado vive en el régimen proper balanced, así que debería ser inmune; confirmar).

### (D) Reproducibilidad / entregable de submission

1. El **paquete ancillary debe acompañar la submission** (supplementary material o repositorio citado con hash): el paper apela al checker y al certificado; un referee debe poder correrlos. Preparar un zip de `drafts/ancillary/` con README de una página (cómo correr el checker, tiempo esperado, qué imprime en éxito/fallo).
2. Añadir al Appendix `app:ancillary` un **manifiesto SHA-256** de certificado y checker (el hash del certificado de 12 MB fija el objeto verificado; hoy el apéndice describe el protocolo pero verificar que los hashes estén impresos en el paper — si ya están, confirmar que coinciden con los archivos actuales).
3. Documentar en el apéndice los **controles negativos** (mutation tests: certificado corrompido ⇒ checker rechaza) si no están ya; una frase con el conteo de mutaciones probadas basta.
4. Completar la cita `Ambrus` (§4.0.4).

**Además — no imprescindible pero fuertemente recomendado:** re-correr el checker completo una vez sobre el paquete final (en una máquina que NO sea R11 salvo permiso; R14/R15 = 172.16.0.14/.15 suelen estar libres) y registrar fecha/duración/hash en la nota de submission.

---

## 6. Checklist final antes de dar por terminado

- [ ] Compila con el template AIMS: 0 errores; revisar overfull boxes > 10pt.
- [ ] 0 warnings de referencias/citas indefinidas.
- [ ] Los **4** autores/afiliaciones/emails EXACTOS como en §1 (Alraddadi, Lucius, Ahmad, Abdelfattah), afiliaciones múltiples de Ahmad y Abdelfattah bien mapeadas; corresponsal (Lucius) marcado.
- [ ] ≥22 referencias, todas citadas, todas verificadas contra fuente primaria.
- [ ] (A)–(D) de §5 aplicadas; auditoría del checker de (A) documentada.
- [ ] End matter completo: `Author contributions` (wording del usuario), `Use of Generative-AI tools declaration` redactada y **honesta**, `Acknowledgments` (funding confirmado con el usuario), `Conflict of interest`, `Supplementary`.
- [ ] Datos/decisiones pendientes con el usuario: wording CRediT (ahora 4 autores); funding sí/no; conflicts of interest de los 4. (Afiliación de Lucius ya cerrada: Independent Researcher, CABA, Argentina.)
- [ ] `\linenumbers` activo en el PDF de submission.
- [ ] PDF final releído: título, running heads, abstract, keywords, MSC 2020 (sugeridos: 52A38, 52A40, 52C15; verificar contra el alcance real), numeración de secciones estilo AIMS.
- [ ] Zip de submission: .tex + figuras + .bbl/.bst según pida AIMS + ancillary + cover letter (si el usuario la pide).
- [ ] Dejar en el repo una nota `notes/` con el diff resumido de lo hecho y cualquier desvío de estas instrucciones.

**Si algo de §5 no se puede verificar o el fix rompe otra cosa: PARAR y consultar al usuario. No someter un paper con un hueco conocido.**
