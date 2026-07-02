# Attackable gaps & refined milestones (post deep-research)

Derived from `01-deep-research-state-of-the-art.md` + `method-abstraction.md`. Every gap below is something a new paper could plausibly own.

## A. The concrete gaps (ranked by attractiveness = impact × feasibility × fit)

| # | Gap | Why open / who's near | Our angle | Risk | Payoff |
|---|---|---|---|---|---|
| G1 | **No variational/Euler–Jacobi proof of Ball's symmetric theorem** | Everyone proves it via Bang's Lemma (quadratic on `{±1}ⁿ`) | Reconstruct via the M–OM critical system; symmetric ⟹ clean Bézout `2ⁿ` count | **Low** | Proof-of-concept; standalone note; unlocks G2–G4 |
| G2 | **Sharp bound 1 unknown for non-symmetric structured bodies (simplex!)** | Ambrus reportedly *reduced the whole conjecture to simplices* (unconfirmed lead) | Simplex = explicit support function ⟹ explicit critical system + BKK; attack `Σ rel-width ≥ 1` directly | **Med** | *First* sharp non-symmetric case → disruptive |
| G3 | **General bound stuck at `2/(1+√d)` (BY26, Feb 2026)** | Classical width/John-position methods | Different machinery (critical points + toric residue) might squeeze past | **Med-High** | Beats live SOTA → headline |
| G4 | **3 planks in the plane still open** | No one has closed even `n=3`, `d=2` | Finite, low-dim: critical system is tiny; possibly brute-but-rigorous variational/case analysis | **Med** | Small, quotable, famous-adjacent |
| G5 | **Chambers–Mouille "convex-remainder" condition (Thm 1) un-removed** | Their sharp bound needs each remainder convex | Recast their condition as a non-degeneracy/reality hypothesis on the critical system; try to weaken it | **Med-High** | Removes a hypothesis from a known theorem |
| G6 | **No equality/rigidity theory for the affine bound** | Focus has been on the inequality | Once an existence/critical-point proof exists, characterize equality (à la Pinasco's orthonormal rigidity) | Low (conditional on G1–G3) | Natural companion result |

**Primary line:** G1 → G2 (with G4 as a parallel cheap probe; G3 as the stretch headline).

## B. The three crux questions that decide everything (resolve EARLY)

1. **Reality (CRUX 1).** Does the M–OM imaginary-part argument (`s‖b‖² = −Σ … ≤ 0 ⟹ b=0`) survive when `A=G⁻¹` is replaced by the support-function Hessian of a *non-symmetric* body? → smooth strictly-convex: likely yes; polytopes/simplex: needs limiting argument. **Test on the simplex first.**
2. **The count (CRUX 2).** For a non-round constraint, is the critical system a 0-dim complete intersection, and is its **BKK mixed-volume** count attained by **simple real** roots in bijection with the body's combinatorial cells? **Compute the simplex Newton polytopes by hand.**
3. **The vanishing identity (CRUX 3).** Pin down the **toric/BKK Euler–Jacobi** statement (global/toric residue vanishing; Khovanskii) and its exact degree condition replacing `deg g ≤ n−1`. **Library question, resolve from references before building.**

> Falsifier discipline: if CRUX 1 or 2 fails *already on the simplex* (the friendliest non-symmetric body), the BKK route is probably wrong — stop and pivot to G1-only (a "new proof of Ball" note) or to a non-algebraic variational attack.

## C. Refined milestone ladder

- **M0 — De-risk (1–2 weeks).**
  - Negative literature check on method novelty (§7 of report): Scholar cite-trees of M–OM, BY26, CM16; search "plank"+"Euler–Jacobi"/"BKK"/"Bernstein theorem"/"toric residue".
  - Read Ball91, CM16, BY26, Verreault survey in full. **Confirm or kill the Ambrus→simplex reduction.**
  - Resolve CRUX 3 (toric Euler–Jacobi statement) from the algebraic-geometry literature.
  - **Gate G0:** niche still empty? Ambrus reduction real? toric vanishing usable? → if any "no", re-scope.

- **M1 — Recover Ball symmetric via Euler–Jacobi (2–4 weeks).** Reconstruct Ball's `Σ ≥ 1` (symmetric) with the critical-point + Euler–Jacobi engine. **Gate G1:** engine reproduces a *known* theorem ⟹ machine works. If it can't even do the symmetric case, the approach is dead.

- **M2 — Simplex / first non-symmetric class (4–8 weeks).** Using M1 + Ambrus reduction (if real): attack the **sharp bound 1 for the simplex**. Resolve CRUX 1 & 2 concretely here. **Gate G2:** a sharp non-symmetric case in hand ⟹ paper exists regardless of M3.

- **M3 — Stretch (open-ended).** Either (a) beat `2/(1+√d)` for general bodies, or (b) close `d=2, n=3`, or (c) weaken Chambers–Mouille's convexity hypothesis (G5). Upside, not promised.

- **M4 — Rigidity + write-up (G6).** Equality characterization; assemble paper.

## D. What NOT to do (lessons from the report)
- Don't claim the planar case or `n=3` is "easy/known" — it is **open** (the Bang-1953 misreading trap).
- Don't cite arXiv:2203.11260 as a proof — **withdrawn** (error in Lemma 2).
- Don't announce a "new general bound" without **beating `2/(1+√d)`** — anything weaker is already superseded.
- Don't over-rely on Bezdek slides / single-source claims for load-bearing history — corroborate.
