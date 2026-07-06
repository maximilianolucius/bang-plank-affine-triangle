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
