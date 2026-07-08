# AIMS Mathematics conversion — `affine-plank-triangle-aims-v1` (from pasada 8)

> Date: 2026-07-05. Executes `instrucciones-modificaciones-paper-aims.md` (repo root).
> Base: `drafts/entregas/affine-plank-triangle-2026-07-03-pasada8.tex` (verified
> byte-identical to the working draft before starting). Working dir (never edits
> pasada 8): `drafts/aims-v1/` — contains the converted `.tex`, `aims.cls`,
> `AIMS_unsrt.bst`, logos, `figure.pdf`, the compiled PDF, and
> `supplementary-ancillary.zip`.
> **Compiles: 40 pp, 0 errors, 0 undefined refs/cites, 0 overfull hbox >10pt.**

## UPDATE 2026-07-05 (later) — third author + funding

Per user request, added a **third author in second position**; final order is
**Ibrahim Alraddadi (1) — Thoraya N. Alharthi (2) — Maximiliano Lucius (3,
corresponding)**.
- New affiliation 2: Department of Mathematics, College of Science, University of
  Bisha, P.O. Box 551, Bisha 61922, Saudi Arabia; email `talhrthe@ub.edu.sa`.
  Aureus (Lucius) shifts to affiliation 3. `\shortauthors` = "I. Alraddadi,
  T. N. Alharthi, M. Lucius" (propagates to the copyright footer).
- **Funding changed:** the earlier "no external funding" is **superseded**. New
  Acknowledgments (verbatim from the user): "The authors are thankful to the
  Deanship of Graduate Studies and Scientific Research at University of Bisha for
  supporting this work through the Fast-Track Research Support Program."
- Author contributions reworded "Both authors" → "All authors" (still equal, all
  CRediT roles). GenAI declaration and Conflict of interest already plural — no
  change. All three emails shown in the affiliation block (verified p.1).
- Recompiled clean (40 pp, 0/0/0). Both zips rebuilt: `submission-source-aims-v1.zip`
  (source; changed) and `supplementary-ancillary.zip` (unchanged — scripts only).
- Later same day: **author 3 changed** (per user, two successive edits):
  first affiliation "Aureus Technology LLC" → "Research Fellow, Buenos Aires
  Institute of Technology"; then the whole author 3 was **replaced** by
  **Victoria Lucius**, Universidad Torcuato Di Tella, CABA, Argentina, email
  `vlucius@mail.utdt.edu` (also the corresponding author). Maximiliano Lucius no
  longer appears; no stray old strings in the .tex (grep-verified). Recompiled
  clean (40 pp, 0/0/0); source bundle rebuilt.
- **FINAL (2026-07-06) — four authors** (per user; supersedes all above):
  (1) Ibrahim Alraddadi (Islamic Univ. of Madinah, `ialraddadi@iu.edu.sa`);
  (2) Maximiliano Lucius (**Independent Researcher, CABA, Argentina**,
  `maximiliano.lucius@gmail.com`, **corresponding**); (3) Hijaz Ahmad (Islamic
  Univ. of Madinah [affil 1, shared w/ Alraddadi] + Near East University, Turkey
  + Korea University, `hijazahmad@korea.ac.kr`); (4) Waleed Mohammed Abdelfattah
  (Univ. of Business and Technology, Jeddah, `w.abdelfattah@ubt.edu.sa` + Zagazig
  University, Egypt). Six numbered affiliations; Alharthi/Victoria removed.
  **Funding reverted** to "no external funding": the University of Bisha
  acknowledgment no longer applies (no Bisha-affiliated author remains).
  Recompiled clean (40 pp, 0/0/0); both zips rebuilt. **Pushed to GitHub**
  (`origin/main`, commit after `3d2aac2`).
- **Layout fix (2026-07-06, later)**: with 4 authors / 6 affiliations the class's
  one-page title layout overflowed (~90pt), so page 1 was emitted *before*
  `\maketitle`'s `\thispagestyle{title}` — the AIMS logo header landed on page 2,
  overprinting the MSC line and "1. Introduction". Fix: local `\@maketitle`
  redefinition in the preamble (aims.cls untouched) — `\small` affiliation and
  correspondence blocks (as in published AIMS papers), inter-block skips
  12pt→6pt, `\titlesep` left at the class default 70pt (58pt and below collide
  with the fixed header rule — tested). Verified: p.1 = logo header + full
  4-author front matter + abstract + keywords + MSC, no overlap; p.2 clean.
  The 89.85pt overfull vbox in the log is PRE-EXISTING (present since the very
  first single-author AIMS compile; a figure page), unrelated to this fix.
  Bundle rebuilt; pushed.

## Correctness gate — §5(A) audit of the checker code [PASSED]

Rosa/panel flagged `lem:noncover`(b) writing `l_i^+` where the complement of the
enlarged config `I_i^+=[l_i^-,h_i^+]` requires `l_i^-`. Order was: fix the .tex
AND audit the code; **stop and escalate if the code implemented the wrong sign.**

- Searcher `c3_balanced_bb.py:113–116` (`cell_positive_area`): `lo=lh_plus[i][0]
  =box[2i][0]=l_i^-`, `hi=box[2i+1][1]=h_i^+`; σ_i=0 clips `u_i<lo`, σ_i=1 clips
  `u_i>hi`. Correct complement.
- Independent checker `bb_certificate_check.py:120–127,166–169` (`enlarged`,
  `check_P3_cell`): identical `l_i^-`/`h_i^+`. Correct.

**Conclusion (evidenced):** the code uses `l_i^-`. The paper's `l_i^+` was a pure
typo; the certificate is NOT compromised. No escalation. Fixed the .tex
(+ the same slip at the `lem:noncover` proof line, "rational in τ,l⁻,h⁺").

## §5 content corrections (all applied, confirmed in the compiled PDF)

- **(A)** `lem:noncover`(b): `l_i^+`→`l_i^-` (and proof line). One-char; gated above.
- **(B)** `thm:char`: added hypothesis "none parallel to a facet (τ_i∈(0,1), unique
  full edge)"; new `rem:facetparallel` — necessity preserved generally via
  `prop:concur`; all-facet case → `thm:facet` (Σrw≥1, no witness); **mixed
  facet/tilted triples honestly declared out of scope** (NOT a false
  cross-reference — the paper has no result covering them). Abstract qualified
  "none parallel to a facet". Chose directive option 1 (restrict + remit).
- **(C)** `thm:sandwichbang` proof partition case (ii): "some plank empty" →
  "empty **or of zero width**"; justified: r_i=0 ⇒ P_i a line ⇒ the two closed
  planks cover cl(Δ∖P_i)=Δ ⇒ `thm:twodir`. Certificate lives only in case (iii)
  proper-balanced, so it is untouched (confirmed: `lem:prunes`/`lem:reduction`
  are stated for *proper* coverings).
- **(D)** reproducibility:
  - SHA-256 manifest in App. B **verified byte-for-byte** against the current
    files: searcher `b2468aa9…`, certificate `ead66ff2…`, checker `90a25ce8…`
    (all match). No drift.
  - Negative controls already documented (4 mutation tests: tampered header,
    non-interior split, false leaf, truncated tree).
  - `supplementary-ancillary.zip` (24 files, 12 MB uncompressed, 0.75 MB zipped)
    built from `drafts/ancillary/`. README opening de-staled (removed the false
    "the paper is NOT computer-assisted"; added a checker QUICK START: command,
    Python-3-stdlib-only, ~minutes, expected `CERTIFICATE VALID`, failure mode).
  - Ambrus entry completed (manuscript + live URL + access date).

## Template / front matter / end matter

- `\documentclass{aims}`; ported all 8 theorem environments (class defines none);
  added `txfonts`, `mathtools`, `tikz`, `lineno`+`\linenumbers`, AIMS metadata
  placeholders, `\numberwithin{equation}{section}`. Dropped the amsart `geometry`
  and `hyperref` (class supplies both). **Added `\usepackage[T1]{fontenc}`**
  (deviation — not in template) because the Polish titles use `\k` (ogonek),
  unavailable in OT1; T1 renders ą correctly (verified).
- Front matter (AIMS macros, after `\begin{document}`): Alraddadi¹ /
  Lucius²,\* order; `\shortauthors`; `\address` with both affiliations
  (Madinah; **Aureus Technology LLC, Buenos Aires, Argentina** — per user);
  `\corraddr{maximiliano.lucius@gmail.com}`. Abstract unchanged (~205 words,
  under AIMS 300). Keywords (7) + MSC 52C17, 52A40, 52A10, 52C15. All rendered
  and visually verified on p.1.
- End matter (AIMS-mandatory): Author contributions (**equal, all CRediT roles**
  — user choice), Use of Generative-AI tools declaration (honest; names the
  agent assistance and the independent checker), Acknowledgments (**no external
  funding** — user), Conflict of interest, Supplementary (points to the zip +
  SHA manifest). All verified on pp. 38, 40.

## References: 7 → 26 (directive asked ≥24), all verified, all cited

Verified against primary sources (DOI resolution / arXiv abstracts), formatted
AIMS house style, ordered strictly by first citation (`unsrt`) via a splice
script (`scratchpad/order_bib.py`): **0 cited-but-missing, 0 uncited-but-present.**
Corrections found during verification: Bezdek13 pp. 45–64; AKP19 pp. 1579–1611
no. 6; GKP22 = "Covering by planks and avoiding zeros of polynomials," IMRN 2023,
DOI `10.1093/imrn/rnac259` (a fabricated DOI from web search was caught and
rejected); MOM26 = "Polarization problems and Coxeter systems," Martínez–
Ortega-Moreno, arXiv:2605.28744.

### Deviations / judgment calls (flagged)
- **`\doilink{bareDOI}`, not `[DOI]` optional + full URL.** `aims.cls`'s
  `\doilink#1` expands to `\href{https://dx.doi.org/#1}{#1}`, i.e. it *prepends*
  the resolver — the deep-research entries passed a full `https://doi.org/…` URL,
  which would have doubled the prefix. Fixed to bare DOI; the two underscored
  DOIs escaped `\_` (render correctly).
- **MOM26 anchored WITHOUT the "Euler–Jacobi identity" mechanism.** The agent
  could not confirm that mechanism from the abstract (only the bibliographic
  fields). Anchored it neutrally as recent polarization progress, not as the
  directive's suggested "Euler–Jacobi para anchos relativos".
- **Alexander68** cited as an *equivalent reformulation*, not the origin: both
  Verreault and Bakaev–Yehudayoff attribute the affine conjecture to **Bang
  (1951)**, with Alexander only noting an equivalence.
- **Verreault** kept as the arXiv form: the journal version (BLMS,
  `10.1112/blms.70230`) has an ambiguous volume/year (58/2026 vs 2025 online).
- Corresponding author = **Lucius** (directive default; not overridden).

## Open items for the user (not blockers to the draft)
- **APC**: AIMS charges **USD 2000** per accepted paper (2026 rate; +80 if AIMS
  formats). Purely informational.
- Both author emails are now shown in the affiliation block (`ialraddadi@iu.edu.sa`
  under affil 1, `maximiliano.lucius@gmail.com` under affil 2), plus the
  `* Correspondence` line for Lucius — per explicit user request (2026-07-05).
  The class has no `\email` macro, so emails were appended to the `\addr` entries.
- Metadata (`\currentvolume`, `\DOI`, dates) are placeholders; production fills them.
- Submission via JAMS (`https://aimspress.jams.pub/`): submit the compiled PDF;
  source requested at production; ancillary zip as supplementary.
- **Source bundle built** (2026-07-05, user request): `submission-source-aims-v1.zip`
  = `.tex` + compiled PDF + `aims.cls` + `AIMS_unsrt.bst` + `logo.pdf` +
  `logobottom.pdf` + `figure.pdf` (no build artifacts). The supplementary
  material is the separate `supplementary-ancillary.zip`.

## Not done (deliberately)
- No git commit (not requested).
- Did not re-run the full checker on this machine (directive: not on R11 for
  heavy work; the certificate + SHAs are unchanged from pasada 8, where
  `CERTIFICATE VALID` was established).

## UPDATE 2026-07-07 — Maximiliano Lucius removed from the author list

Per user. Three authors remain: (1) Ibrahim Alraddadi (Madinah,
`ialraddadi@iu.edu.sa`) — **now corresponding** (user-confirmed); (2) Hijaz
Ahmad (Madinah + Near East Univ. + Korea Univ.); (3) Waleed Mohammed
Abdelfattah (UBT Jeddah + Zagazig). Affiliations renumbered 1–5 ("Independent
Researcher, CABA" dropped). No stray Lucius strings (grep-verified). Recompiled
clean (40 pp, 0/0/0); title page verified (logo header, no overlap). Source
bundle rebuilt; pushed to origin/main.

## UPDATE 2026-07-07 — directiva 70 (Discussion + Conclusions) + AI declaration corrected

Two things this pass (executed, NOT committed — sequence is investigador → jefe
audita 3 chequeos → commit):

1. **AI-tools declaration corrected to the truth.** The version committed by the
   user in `a574e73` named the tool "Alibaba Cloud service, Qwen 3.6 Plus" and
   scoped it to "language editing, clarity, grammar, structure" — both false:
   the tool was **Claude (Anthropic)** and it did the proofs, the B&B algorithm
   (Thm sandwichbang), the certificate-generating code, and the manuscript text.
   Rewrote the declaration (same AIMS four-part Q&A format) with the real tool
   and real scope; kept "authors verified all statements" and the independent
   checker (App. B). Qwen/Alibaba absent from the compiled PDF (grep-verified);
   "Claude (Anthropic)" present. This is a research-integrity requirement (COPE/
   AIMS: false AI disclosure is retractable), not a stylistic choice.

2. **Directiva 70 executed.** Inserted `\section{Discussion}` (§11,
   `sec:discussion`) and `\section{Conclusions}` (§12, `sec:conclusions`)
   between the end of §10 (`sec:problems`) and `\appendix`, verbatim from the
   directive's blocks. Pre-insert I verified every `\ref`/`\cite` against disk:
   19 labels + 13 keys all resolve — **no citation removed or added**
   (Strassen65/Kellerer84/Villani09/mathlib20 all present in the bibliography).
   Appendices remain **A/B** (not renumbered).

Verification: `pdflatex` ×2 → **42 pp** (was 40), 0 errors, 0 undefined
refs/cites, 0 overfull hbox >10pt. `.aux` confirms Discussion=§11, Conclusions=
§12, App=A/B. Read both sections in the PDF (pp. 32–33): interpretive, no
verbatim repetition of the Intro or §10.

§5 criterion point (non-blocking): left §10's title "Open problems…" as is
(renaming = scope creep, per recommendation). The BY26 comparison now appears in
the Intro (factual: 4√3−6) and in Discussion (interpretive: local 29/31 vs
global, "not an improvement") — differentiated, not redundant; flagged for the
audit, no move made.

Source bundle rebuilt. Not committed.

## UPDATE 2026-07-07 (later) — audit 71 corrections A/B/C applied

Applied the three corrections from `auditorias/71` (all in directive-70 text the
chief authored; pasted verbatim, so his to fix):
- **A** (Discussion, "where it stops"): dropped the overclaim that $G_{tr}>0$
  on the whole non-concurrent region (only proven at the facet triple; $C_\Delta$
  open at the sandwich). Now states $D_\Delta(u)>1$ strictly off the locus
  (Thm~thm:char), so $1/D_\Delta<1$; gap size "remains open in general"; facet
  value $\tfrac13$.
- **B** (Conclusions): wrong object $\sup_K D_K$ (sup over bodies) → correct
  $\sup_u D_\Delta(u)$ (sup over non-parallel triples on the triangle), citing
  Problem~prob:defect (renders "Problem 10.12").
- **C** (Conclusions, optional, applied): added hedge "known to us" to the
  first-tilted-triple claim, matching the intro and §10.

Verified: `prob:defect` resolves; no stray `\sup_K D_K` or old $G_{tr}$ phrasing.
Recompiled from clean aux: **42 pp, 0 errors, 0 undefined, 0 overfull hbox
>10pt**. Both corrections confirmed in the rendered PDF (pp. 32–33). Source
bundle rebuilt. **Not committed** — awaiting the chief's short re-audit; commit
must exclude `drafts_uso_ai.zip`.
