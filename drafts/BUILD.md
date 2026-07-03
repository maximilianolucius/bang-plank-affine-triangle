# Build & status — ONE LIVE MANUSCRIPT

## Current manuscript: `affine-plank-triangle.tex`

- **Title:** *Transport and tiling bounds for the affine plank problem on the triangle*
  (R7-3 decision 2026-07-02: KEEP; unchanged in R9).
- **Status (2026-07-03, post-R12 = pass-6 revision):** compiles clean with local
  `pdflatex` (2 passes): **0 errors, 0 unresolved references, 0 overfull, 31 pages**
  → `affine-plank-triangle.pdf`.
- **R12 (auditorias/60; Rosa pass 5 = "major revision with real potential"):**
  ALL accepted pass-5 fixes (29/31 exact reciprocal in Thm 7.15/Cor 7.17 with
  46225>46128; abstract = 3 messages; B-Y sober at end of intro; "the transport
  method certifies the sharp constant 1"; "minimax duality" + explicit
  non-attainment; Pocket Lemma "closure" prose shield — her objection was a
  misreading, politely noted; trichotomy mini-table; Appendix A 7-case table);
  **R10 package integrated** (Lem 7.10 counting lemma at general level,
  **Thm 7.11 delta=delta_c**, Rem 7.20 three gap certificates + strict sandwich,
  Prop 7.4 delta-max uniqueness, Prop 7.21 lsc + Rem 7.22 parallel path,
  Prob 10.4 = sup D question); **Rosa's cheap value adopted** (Def 2.3
  covering constant C_K + gap table in §10; Prop 7.16 inverse stability;
  Fig 4 dual-certificate; Fig 5 phase diagram [EVIDENCE] with verified caption
  numbers); **NEW Thm 6.13 (canonical covering)**: every cyclic triple carries
  the explicit covering ([lam_i,rho_i]) with excess exactly
  (P-Q)^2/((1+P)(1+Q)); P=Q <=> concurrence; delta closed form
  |P-Q|/(2(2+P+Q)) for all cyclic triples. §10 rewritten as the
  covering-constant program (Prob 10.1, Lem 10.2 edge reduction, honest hybrid
  status; exact experiments found NO covering with Sigma r < 1).
  Frozen: `entregas/affine-plank-triangle-2026-07-03-pasada6.{pdf,tex}`;
  hand-off + full numbering map: `notes/55-R12-entrega-dona-rosa-pasada6.md`.
- **R9 (auditorias/56) executed — single paper, `D_K(u)` as backbone:**
  - **Structure:** Def/Prop of the defect moved to §2 and generalized to arbitrary
    convex bodies (Def 2.1, Prop 2.2); Thm 2.3 = the 1/d bound recast as "the uniform
    measure certifies `D_K ≤ d` for every family"; intro rewritten (formal
    terminology, "organizing frame" subsection, explicit hierarchy
    main/framework/illustrative/extensions); abstract = one thesis.
  - **B1 duality:** Thm 7.6 strong duality `D_K(u) = sup_psi min_x sum psi_i(u_i(x))`
    (Sion; full proof); Cor 7.7 certificates; facet dual certificate
    `(1-3t/2)_+`; Prop 7.8 wedge certificates = dual form of the moment bound,
    value `1/(1-2delta_c)`, `delta_c` = l-inf distance center→image plane, equality
    criterion via `p* ∈ T_u`; Lem 7.9 no-external-concurrence (sign counting);
    Prop 7.11 complementary slackness; Rem 7.12 skeleton (`D_∂=1` concurrent,
    `D_∂=∞` facets); Rem 7.17 sandwich rewritten (LP = upper bound ONLY — Rosa's
    overclaim fixed) with dual certificate 225/224.
  - **B2:** everything defect-theoretic stated/proved for general `K`, n directions.
  - **B3 (partial):** **Thm 7.3 centroid bound `delta(u) ≤ 1/6` for EVERY finite
    family (PROVED)** — moment bound never certifies D > 3/2; **Thm 8.2
    `D_{Delta^d}(facets) = (d+1)/2` for all d ≥ 2 (PROVED)**, explicit inscribed
    cycle + dual certificate, verified exactly for d=2..7. Upper half
    (`sup D = 3/2`?) remains OPEN → Problem 10.3 rewritten (`sup ∈ [3/2, 2]`).
  - **B4 (lite):** Cor 7.15 — certified tube around the WHOLE concurrent family
    where `Σrw > 4√3−6` (box radius `km²/(1+km)`, `k=(2√3−3)/6`); honest: region
    certified by our bound, not the full sublevel set.
  - **Rosa pass-4 items (all accepted ones, split refused by user):** A1a LP
    overclaim removed; A1b mass convention `α=w_BC, β=w_CA, γ=w_AB` fixed once in
    Thm 6.3; A2 abstract/claims; A3 hierarchy + formal definitions; A4 Thm 6.6 split
    into Lemmas 6.7/6.8/6.9 + sumset Lemma 3.2 extracted + Appendix A (O2)
    airtight ("neither covers nor obstructs"); A5 §8 own intro & motivation;
    A6 Appendix B verification protocol (paper NOT computer-assisted).
- **Frozen delivery copy for doña Rosa (pass 5, R9-entrega):**
  `drafts/entregas/affine-plank-triangle-2026-07-03-pasada5.{pdf,tex}` (24 pp).
  Hand-off + old→new numbering map: `notes/53-R9-entrega-dona-rosa-pasada5.md`.
  Chief decides whether to deliver now or after closing B3(b).
- **Earlier frozen copies:** pass 4 (17 pp, 2026-07-02), pass 3 (11 pp, 2026-07-02)
  in `drafts/entregas/`. Do not touch.
- **Proved content (audit records `43/44-46/47/48/50/52/53/54` + R9):**
  `1/d` via uniform (= `D_K ≤ d`); two directions; facet-parallel (sumset lemma);
  3 facets + 1; **medians `Σrw ≥ 1` + rigidity**; **Thm 6.3 weighted perimeter**;
  **Thm 6.6 tightness/rigidity of the cyclic family** (Lemmas 6.7–6.9);
  **Thm 6.11 three-direction characterization** (Gardner N=3 on the triangle,
  scope-fenced); **§7: strong duality, wedge certificates, `D(facets)=3/2` with
  matched primal–dual pair, centroid bound `δ≤1/6`, linear stability, 27/29 box +
  certified tube (Cor 7.15), sandwich 225/224–112/111 with dual lower**;
  **§8: σ-family on Δ³; `D_d(facets)=(d+1)/2` all d; d≥4 skeleton obstruction**;
  normalizer no-go (Prop 9.1). Appendix A classification (Prop A.1).
- **Key numbering (pass 5):** Thm 6.3/6.6, Prop A.1, Thm 7.4, Thm 8.1 unchanged;
  Thm 6.8→6.11, Rem 6.9→6.12, Prop 7.2→2.2, Prop 7.3→7.2, Thm 7.6→7.13,
  Cor 7.7→7.14 (NEW 7.7 = certificates!), Rem 7.8→7.16, Rem 7.9→7.17,
  Prop 8.2→8.4. Full map in `notes/53-R9-entrega-dona-rosa-pasada5.md`.

## How to build
```bash
cd drafts/
pdflatex -interaction=nonstopmode affine-plank-triangle.tex
pdflatex -interaction=nonstopmode affine-plank-triangle.tex   # 2nd pass (refs)
```

## Ancillary files (for arXiv)
`drafts/ancillary/` (copies from `experiments/`): **15 scripts** + README with the
verification-protocol table (script → verifies → accompanies; R10/R12 additions
cited by Appendix B since pass 6). New in R9:
`defect_duality.py` (8 exact check blocks, "ALL OK": facet dual certificate,
wedge algebra + sandwich dependency, no-external-concurrence counting, centroid
bound, `Δ^d` facet-cycle marginals d=2..7, B-Y region algebra). Documented
in-paper in Appendix B.

## Round 10 (2026-07-03, auditorias/58) — NUMBERING FREEZE: zero .tex changes
Rosa is reading pass 5; all round-10 material lives in `notes/54-*` +
`experiments/` (synced to `ancillary/` under a clearly marked R10 section):
- **R10-2 THEOREM [PROVED]: `δ = δ_c` for every pairwise non-parallel triple**
  (closed form `δ = |c₀−½Σc|/‖c‖₁`; single-knot wedges ALWAYS attain the
  moment bound). Proof = flip normalization + counting lemma at general level
  (the lem:external sign count run at level `a`); machine-verified
  (`delta_eq_deltac.py`: 2928 external (q,a) + 507-triple sweep, all classes).
- **R10-1 [PROVED]: the moment bound is NOT exact in general** — three exact
  archival dual certificates (`dual_certificates.py`, self-contained):
  tilt-1/10 `D ≥ 18/13 > 15/11`; class-b (2/3,5/6,1/12) `D ≥ 32/29 > 153/142`;
  **sandwich `D > 225/224`** (now strictly `225/224 < D ≤ 112/111`). First
  half of Problem 10.3 answered negatively.
- **Route B (Gardner pair-witness mixing) REFUTED at the calibration point**:
  `M*(facets) = +∞` (moment obstruction: pair witness forces `E[λ₃]=0` ⟹
  atom), unequal weights dead too; pair-cost lemma documented
  (`gardner_third_marginal.py`).
- Near-parallel continuity: `D` lsc in general (via duality); along
  class-b(1/3,1/3+ε,1/2): `1+3ε/(2(3ε+4)) ≤ D ≤ 1+(3/4)ε` (both symbolic) —
  `D → 1` linearly at the parallel degeneration.
- δ-maximizer uniqueness [PROVED, Gordan]: `δ = 1/6` ⟺ facets mod flips.
- `sup D ∈ [3/2, 2]` remains OPEN; hunts (class-b corner, tilted facets)
  approach 3/2 from below without crossing.
- Post-verdict .tex integration plan is listed at the end of both notes.

## Round 13 (2026-07-03, auditorias/61) — NUMBERING FREEZE again (Rosa reads pass 6): zero .tex changes
All in `notes/56-R13-*` + experiments (synced to ancillary, marked):
- **EXTREME-REGIME THEOREM [PROVED]** for C_3 on cyclic triples: explicit
  w0(tau) > 0 such that any 3-plank covering with max r_i >= 1 - w0 has
  Sigma r >= 1 (equality only trivial). First use of the closed 2-plank case
  (Gardner witness ON the corner piece) as a tool. Corollary: any hypothetical
  counterexample to C_3 = 1 is BALANCED (all r_i < 1 - w0).
- **Naive per-piece coupling refuted [PROVED]**: at the sandwich the two
  Gardner piece-bounds admit r2+r3 = (1875/1094) l < l+s — position coupling
  (Case B gaps) is essential.
- **Order-mismatch obstruction documented**: tiling-stability route can't
  close the balanced regime (overlap budget ~ D-1 first order vs canonical
  penalty (P-Q)^2 second order).
- **Facets local max [certified evidence]**: adapted symmetric loops give
  D(tilt eps) <= 135/91, 190/127, 1225/817 (< 3/2) for eps = 1/10, 1/20, 1/50;
  deficit ~ eps^2. Sandwich unchanged: D in (225/224, 112/111], LB nudged to
  1.0044834 (q=75 dual); pw-skeleton does not beat uniform.
- Balanced regime and sandwich fallback: OPEN (blockers documented).

## Round 14 (2026-07-03, auditorias/62) — NUMBERING FREEZE (Rosa reads pass 6): zero .tex changes
All in `notes/57-R14-*` + experiments (synced to ancillary, marked):
- **R14-2 THEOREM [PROVED, symbolic]**: facets are a STRICT LOCAL MAX of D on
  the symmetric tilt path: (3/2)/(1+eps) <= D(tilt eps) <=
  (3/2)(1-eps)/(1-eps+eps^2) < 3/2 for eps in (0,1/2); optimal loop
  x* = (1-2eps)/(3(1-eps)); UB = 3/2 - (3/2)eps^2 + O(eps^3); reproduces the
  three R13 certified points exactly (tilt_local_max.py, ALL OK).
- **R14-1 (flagship)**: exact B&B for the balanced regime at the sandwich
  implemented and validated (c3_balanced_bb.py): complete exact failure test
  (1-D edge + positive-area cell by exact clipping), prunes by Sigma r /
  extreme theorem (w0 = 2/25, computed in script) / empty plank (2-plank
  Thm 3.1 as a tool, 2nd use). Two 6-min runs documented (~1M boxes each);
  bottleneck identified and fixed (P4); LONG RUN (55 min) in progress with
  checkpoint — if the tree empties: C_3(sandwich) = 1 (computer-assisted,
  exact) = first non-concurrent triple with Bang(3) proved.
- **Thin-plank band identified** as the next analytic lemma (mirror of the
  extreme regime; P4 covers exactly-empty, the 0 < r_i << 1 band is R15).
- R14-3: 'sandwich strictly intermediate / non-skeletal optimum' conjecture
  formalized with a complementary-slackness proof route (queued).

## Pending before submission
- R13-0/R14: chief hands the frozen pass-6 package (31 pp) to dona Rosa.
- Author/affiliation/email block — REAL human identity, cannot be decided by the
  investigator; placeholder marked in the .tex.
- C1 case (b): the hybrid certificate (boundary measure + sumset/tiling
  obstruction) — the program of §10, open.
- C2 (carryover): fine UB near facets (local max 3/2?); exact sandwich.
- `sup D = 3/2?` (Prob 10.4) — OPEN. C3 (closed form D(tau) by regions;
  D_boundary = D transition): background. Coupling moonshot: untouched.

## Obsolete
`drafts/obsolete/` contains the manuscripts of the **toric era** (`paper.tex`,
`paper.pdf`, `bang-plank-paper.tex`), refuted and abandoned (`notes/15/22/23`; a
concurring external audit is recorded in `auditorias/49`). **Do not audit or cite** —
see `obsolete/README-OBSOLETE.md`.

(Note: the `hamilton-jacobi-*` files formerly kept in `drafts/` belong to a DIFFERENT
project, not to this plank project; they are not part of this manuscript and are
excluded from the repository.)
