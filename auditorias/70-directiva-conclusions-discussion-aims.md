# Directiva — agregar §Discussion y §Conclusions al paper AIMS
> Jefe de research: Claude. Fecha: 2026-07-07. Ejecuta el investigador; audita el jefe.
> Archivo objetivo: `drafts/aims-v1/affine-plank-triangle-aims-v1.tex`.
> Motivo: el template oficial de AIMS Mathematics trae `\section{Discussion}` y
> `\section{Conclusions}` como últimas secciones numeradas del cuerpo; el paper no las
> tiene (se detectó al auditar la conversión). Las instrucciones de conversión
> (`instrucciones-modificaciones-paper-aims.md`, §2.4) omitieron ambas — hueco nuestro,
> no del investigador. Esta directiva lo cierra.

## 0. Diagnóstico (contexto)
- Estructura actual: §1 Intro … §10 "Open problems and the covering-constant program"
  → `\appendix` A (tilings) / B (ancillary) → end matter. **No hay Discussion ni Conclusions.**
- Template AIMS: `Discussion` (§) y `Conclusions` (§) van como **últimas secciones numeradas
  del cuerpo, antes del end matter**.
- **Riesgo a evitar (léelo antes de escribir):** el paper YA tiene tres cierres que solapan
  — la subsección "Results and their hierarchy" de la Intro (recap completo de resultados),
  el §10 con su lista de open problems (`prob:covconst` + dos `problem` más sobre
  `sup D∈[3/2,2]` y el coupling certificate), y la comparación con `\cite{BY26}`. Si
  Discussion/Conclusions repiten eso, un referee lo lee como relleno. Cada sección nueva
  tiene un trabajo DISTINTO (abajo). **Regla dura: Discussion no re-enuncia teoremas
  literalmente; Conclusions NO re-lista los open problems — apunta a `prob:covconst`.**

## 1. Ubicación
Insertar **después** del final de §10 (`sec:problems`, termina justo antes de `\appendix`,
hoy ~l. 2886) y **antes** de `\appendix`. Orden resultante:

  … §10 sec:problems → §11 Discussion → §12 Conclusions → \appendix A → B → end matter.

Esto respeta el template (Conclusions = última sección numerada del cuerpo) y deja los
apéndices como material de soporte al final. NO tocar el end matter ni los apéndices.

## 2. Tarea D1 — insertar la sección Discussion
Pegar tal cual (ajustar solo si algún `\ref` no resuelve; ver §4). Sentence case en el
título, como pide AIMS.

```latex
\section{Discussion}\label{sec:discussion}

\subsection*{The transport defect as the organizing object}
The results of this paper are held together by a single quantity, the
transport defect $D_K(u)$. From it follow the covering bound
$\sum\rw\ge 1/D_K(u)$ and its attainment (Proposition~\ref{prop:defect}),
the equivalence between $D_\Delta(u)=1$ and concurrence of the mid-level
lines (Theorem~\ref{thm:char}), the strong minimax duality with its explicit
wedge certificates (\S\ref{sec:defect}), and the exact facet value
$D_{\Delta^d}(\mathrm{facets})=\tfrac{d+1}{2}$ in every dimension
(Theorem~\ref{thm:facetd}). The defect recasts a covering question as a
question about probability measures with prescribed marginals, a classical
theme in the theory of marginal problems~\cite{Strassen65,Kellerer84} and
optimal transport~\cite{Villani09}; the duality of \S\ref{sec:defect} is the
form that theory takes for relative widths on a simplex. This is, in our view,
the main conceptual contribution: a single object that specializes to the
sharp constant on the concurrent locus and, off it, exposes precisely what a
covering proof must still supply.

\subsection*{Where the transport method is sharp, and where it stops}
On and near the concurrent locus the method certifies the truth exactly. For
every concurrent cyclic triple it produces an explicit witness measure and a
tight covering with $\sum\rw=1$, together with their rigidity
(Theorems~\ref{thm:wper},~\ref{thm:tight}, extending the median case
Theorem~\ref{thm:median}); on the whole triangle it gives the universal
bound $\delta(u)\le\tfrac16$ on the concurrence defect (Theorem~\ref{thm:centroid})
and a linear stability modulus yielding, e.g., $\sum\rw\ge\tfrac{29}{31}$ on an
explicit neighbourhood of the concurrent family
(Corollaries~\ref{cor:beyond},~\ref{cor:region}). Off the concurrent locus the
transport bound $1/D_\Delta$ is \emph{strictly} below the covering truth: the
gap $G_{\mathrm{tr}}=C_\Delta-1/D_\Delta$ is positive there, as the facet
triple already shows ($1/D=\tfrac23$ while $C_\Delta=1$; Theorem~\ref{thm:facet}).
This is a limitation of the object, not of our estimates of it, and it is the
reason the covering-constant program of \S\ref{sec:problems} and the
computer-assisted foothold below are needed exactly in the regime where
transport alone can no longer decide the constant.

\subsection*{The computer-assisted result in perspective}
Theorem~\ref{thm:sandwichbang} establishes $C^{111}_\Delta(\tau_0)=1$ at one
tilted, non-facet, non-concurrent triple, the sandwich
$\tau_0=(\tfrac{13}{25},\tfrac12,\tfrac12)$. Its scope should be stated as
plainly as its content: it is a \emph{single} triple, not the family; it
settles the one-plank-per-direction constant $C^{111}_\Delta$, leaving the
full covering constant $C_\Delta(\tau_0)$ open; and it bears neither on
Conjecture~\ref{conj:bang} nor on the general constant $4\sqrt3-6$
of~\cite{BY26}. The proof is by hand except for the emptiness of one explicit
finite bisection tree, discharged by an exact-rational computation and
re-verified by an independent certificate checker sharing no code with the
search (Appendix~\ref{app:ancillary}); the human/machine boundary is drawn in
Remark~\ref{rem:boundary}. In this we follow the standard of computer-assisted
proof from the four-colour theorem~\cite{AppelHaken77} through the formal proof
of the Kepler conjecture~\cite{Hales17} and large-scale certificate
verification~\cite{HKM16}: the authority rests on the independent checker and
the exact arithmetic, not on trusting the search that produced the certificate.

\subsection*{Relation to the general bound and to other routes}
Our local estimate $\sum\rw\ge\tfrac{29}{31}\approx0.935$ exceeds the uniform
triangle bound $4\sqrt3-6\approx0.928$ of~\cite{BY26}, but only for coverings
by planks parallel to restricted direction families near the medians
(Remark~\ref{rem:beyond}); it is a local consequence of the method, not an
improvement of the general constant. Other modern approaches to plank-type
inequalities proceed very differently --- the analytic optimal plank
theorem~\cite{OM21}, the polynomial method of
Glazyrin--Karasev--Polyanskii~\cite{GKP22}, symplectic invariants for Bang's
problem~\cite{AKP19}, and the closely related polarization
line~\cite{Pinasco23,MOM26} --- and none of them yields the affine
relative-width bound pursued here. Against that background the contribution of
this paper is a unifying frame (the defect), sharp and rigid on the concurrent
locus, together with a first certified foothold in the genuinely tilted regime,
rather than a new value for the global constant.
```

## 3. Tarea D2 — insertar la sección Conclusions
Va **inmediatamente después** de Discussion. Corta (3 párrafos). No re-lista open
problems; apunta a `prob:covconst`.

```latex
\section{Conclusions}\label{sec:conclusions}

We have introduced the transport defect $D_K(u)$ as an organizing invariant
for affine plank problems and used it to give: the covering bound
$\sum\rw\ge 1/D_K(u)$ with its duality (\S\ref{sec:measure},~\S\ref{sec:defect});
on the triangle, the characterization of witness measures by concurrence
(Theorem~\ref{thm:char}) together with explicit tight coverings and their
rigidity for the concurrent cyclic family (Theorems~\ref{thm:wper},~\ref{thm:tight});
the exact facet defect $D_{\Delta^d}(\mathrm{facets})=\tfrac{d+1}{2}$ in every
dimension (Theorem~\ref{thm:facetd}); and, beyond the reach of the transport
method, the first genuinely tilted non-concurrent triple for which the
one-plank-per-direction bound is established, $C^{111}_\Delta(\tau_0)=1$
(Theorem~\ref{thm:sandwichbang}), by an exact-rational computation verified by
an independent checker.

The sharpest frontier left open is the passage from this single triple to the
non-concurrent family: closing the covering constants $C_\Delta,C^{111}_\Delta$
in the tilted regime (Problem~\ref{prob:covconst}) requires coupling the forced
boundary constraints of Lemma~\ref{lem:edgered} with an interior mechanism, the
hybrid certificate described in \S\ref{sec:problems}. Two structural questions
remain beyond it: the exact value of $\sup_K D_K\in[\tfrac32,2]$, whose
resolution would give the universal bound $\sum\rw\ge\tfrac23$ for arbitrary
triples on the triangle, and the affine plank conjecture itself, where the best
known general constant remains $2/(1+\sqrt d)$~\cite{BY26}.

Two directions seem within reach. A machine-checked formalization of the
certificate checker of Appendix~\ref{app:ancillary} --- in the spirit
of~\cite{Hales17,mathlib20} --- would remove the last element of trust from
Theorem~\ref{thm:sandwichbang}. And the covering-constant program of
\S\ref{sec:problems}, which isolates exactly the obstruction that the transport
defect cannot see, is in our view the natural route from the concurrent locus
into the open territory of the conjecture.
```

## 4. Verificación exigida (no cerrar sin esto)
1. `pdflatex` ×2. **0 errores.** Revisar `.log`: 0 "Citation undefined", 0 "Reference …
   undefined", 0 overfull > 10pt nuevos.
2. Confirmar que TODAS las `\ref`/`\cite` de los dos bloques resuelven. En particular
   `cor:region`, `rem:beyond`, `rem:boundary`, `lem:edgered`, `mathlib20`,
   `Strassen65`, `Kellerer84`, `Villani09` — si alguna clave de referencia **no existe**
   en el `thebibliography` actual, hay dos salidas: (a) quitar esa cita del borrador
   (las de transporte `Strassen65/Kellerer84/Villani09` y `mathlib20` son "nice to have",
   no load-bearing — se pueden borrar sin dañar el argumento), o (b) agregar la entrada
   bibliográfica si el investigador ya la tenía prevista de §4 de las instrucciones.
   **No inventar entradas** ni dejar citas colgadas. Reportar cuáles se quitaron/agregaron.
3. Numeración: Discussion y Conclusions deben quedar como §11 y §12 (o el número que toque);
   los apéndices deben SEGUIR siendo A y B (verificar que no se corrieron a números).
4. Releer los dos textos en el PDF: que no repitan frase por frase la Intro ni el §10.

## 5. Punto de criterio (menor, NO bloqueante) — para que el investigador decida y reporte
El §10 se titula "Open problems and the covering-constant program" pero contiene un teorema
**probado** (`thm:sandwichbang`). Con una Conclusions que ya carga el "frontier" y una
Discussion que interpreta, el título de §10 sigue siendo correcto (tiene `prob:covconst` y
dos `problem` más). **Recomendación: dejar §10 como está** — renombrar sería scope creep y
la sección es genuinamente de open problems. Solo si al compilar el trío
§10/Discussion/Conclusions se lee redundante, considerar mover la comparación con `\cite{BY26}`
que hoy está duplicada (Intro + §10 + Discussion) a un solo lugar. Reportar impresión.

## 6. Al terminar
- Recompilar el PDF y regenerar `submission-source-aims-v1.zip` (el investigador ya tiene el
  flujo; los tres archivos de `drafts/aims-v1/` se versionan juntos).
- Dejar una nota en `notes/` con el diff resumido (qué citas se quitaron/agregaron, número
  de páginas final, resultado de compilación).
- NO comitear: la secuencia es investigador ejecuta → jefe audita (los 3 chequeos) → commit.

**Si alguna cita no resuelve y no está claro si quitarla o agregar la entrada: PARAR y
consultar. No dejar el paper con referencias colgadas.**
