# State of the art — Bang's affine (relative-width) plank conjecture
### Deep-research report (verified). Run wk2z98wy5 · 104 agents · 21 sources fetched · 25 claims adversarially verified (24 confirmed, 1 killed). Date: 2026-06-27.

> Verification protocol: each load-bearing claim survived a 3-vote adversarial refutation pass (needs 2/3 to kill). Votes shown as `3-0`. One claim was **killed 0-3** (see §8).

---

## 0. Bottom line (for the impatient)

- **The general affine plank conjecture is OPEN as of February 2026** — open *even in the plane*, and **not even known for three planks** (Bang settled only the two-plank case). `[3-0]`
- The **only** decisive positive result is the **centrally symmetric** case: **Ball, Invent. Math. 104 (1991)**. `[3-0]`
- Best general lower bound for the total relative width has climbed: **1/d → 2/(1+d) → 2/(1+√d)**, the last being **Bakaev & Yehudayoff, arXiv:2602.20290 (Feb 2026)** — *live competition*. `[3-0]`
- **No verified evidence** that anyone has applied **Euler–Jacobi / BKK / Morse-type polynomial-solution-counting** (the Martínez–Ortega-Moreno engine) to the plank / relative-width problem. **This is the open methodological niche.** `[unverified — absence of evidence, see §7]`

---

## 1. Origin (Q1) `[3-0]`

- **Tarski (1932):** posed the *absolute-width* plank problem (a convex body covered by planks ⟹ Σ widths ≥ minimal width `w(C)`). Tarski proved only the **disk** case.
- **Bang (1950 Mat. Tidsskr. B; 1951 Proc. AMS 2, 990–993):** proved Tarski's conjecture in full — `Σ w(Pᵢ) ≥ w(C)` — "using quite different ideas" (the combinatorial/quadratic **Bang's Lemma**).
- **At the END of the 1951 Proc. AMS paper**, Bang posed the **stronger affine/relative-width version** and **coined the term "relative width"**: measure each plank's width *relative to the width of `C` in that plank's normal direction*. He could not settle it.
- Statement (the target): `C` covered by planks `P₁,…,Pₙ` in `Eᵈ` (`d≥2`) ⟹ `Σ w_C(Pᵢ) ≥ 1`, where `w_C(P) = w(P)/w(C; normal dir)`. `[3-0]`

Sources: Bezdek (Fields slides); Ball 1991 (arXiv math/9201218); Kupavskii–Pach (arXiv:1511.08111); Bakaev–Yehudayoff (arXiv:2602.20290); Verreault survey (Bull. LMS 2026, "Conjecture 2.6").

---

## 2. Open status in 2026 (Q2) — CONFIRMED OPEN `[3-0]`

Direct quotes from primary 2026 sources:
- **Bakaev–Yehudayoff (Feb 2026):** *"This conjecture remains open. In fact, it is open even in the plane (some sources incorrectly claim that the conjecture has been resolved in the plane, citing [Ban53]; however, that paper proves the conjecture only for the special case of two planks)."*
- **Verreault, "Plank theorems and their applications: A survey", Bull. London Math. Soc. (2026):** *"to this day it remains an important open problem in convex geometry"*; *"the case of a covering by three planks is still open, and it was only recently that Bang's Theorem 2.6 was proved for two directions of planks."*
- **Kupavskii–Pach (2016):** *"still open … not known to be true even for triples."*
- **Balitskiy (2020):** *"Bang's conjecture on relative widths is solved by K. Ball for the case when the unit ball is centrally symmetric"* (general case open).

> ⚠️ Common error in the literature: citing Bang's **1953** paper as resolving the planar case. It only does **two planks**. Do not repeat this.

---

## 3. The symmetric case — Ball 1991 (Q3) `[3-0]`

**K. Ball, "The plank problem for symmetric bodies", Invent. Math. 104 (1991) 535–543** (arXiv math/9201218).

- **Theorem 1 (functional-analytic form):** *"If the unit ball of a Banach space `X` is covered by a (countable) collection of planks in `X`, then the sum of the half-widths of these planks is at least 1."*
- **Equivalent dual / geometric form (Inventiones abstract):** *"Given a symmetric convex body `C` and `n` hyperplanes in Euclidean space, there is a translate of a multiple of `C`, at least `1/(n+1)` times as large, inside `C`, whose interior does not meet any of the hyperplanes."* (Sharp.)
- **Technique:** an **extension of Bang's Lemma** — **optimization of a well-chosen quadratic function over the sign vectors `{±1}ⁿ`** of a symmetric matrix encoding the plank-normal inner products. *(Central symmetry is used essentially; the corollary explicitly assumes `C` centered at origin.)*
- Applications: **Diophantine / simultaneous approximation** (Ball; Kupavskii–Pach, Amer. Math. Monthly 2017).

> 🔑 **Strategic note:** "optimize a quadratic over `{±1}ⁿ` of a symmetric (Gram-type) matrix" is *the same algebraic flavor* as (i) Pinasco's longest-sum/sign arguments and (ii) the Martínez–Ortega-Moreno critical-point system `yⱼ(Ay)ⱼ=αⱼ`. This is the concrete reason the variational engine is a priori relevant here.

---

## 4. Partial results, general (non-symmetric) case (Q4) `[3-0]`

Total-relative-width lower bounds, chronological/strength order:

| Bound | Authors / how | Reference |
|---|---|---|
| **1/d** | John's theorem (John position) + Bang's theorem | Chambers–Mouille [CM16]; Bezdek–Litvak [BL09], J. Geom. Anal. 19 (2009) 233–243 |
| **2/(1+d)** | Ball's symmetric solution + a Minkowski–Radon result | Chambers–Mouille [CM16], Thm 2 & Remark 5 (arXiv:1604.00456) |
| **2/(1+√d)** ← current best | new argument | **Bakaev & Yehudayoff, "A note on the affine plank conjecture", arXiv:2602.20290 (Feb 2026)** |

**Chambers & Mouille, "A note on the affine-invariant plank problem" (arXiv:1604.00456):** two further partial results (verbatim):
- **Theorem 2 (unconditional, weaker bound):** planks in directions spanning `V` covering `C` ⟹ `Σ wᵢ/w_{vᵢ}(C) ≥ 1/dim(π_V(C))`, where `π_V(C)` = projection of `C` onto `V`.
- **Theorem 1 (conditional, SHARP bound 1):** *if `C \ (∪ of first m planks)` stays convex for every `m`*, then Bang's conjecture (`Σ ≥ 1`) holds.

**Special cases / reductions surfaced but NOT independently verified (treat as leads, not facts):**
- **Ambrus reduced the conjecture to SIMPLICES** (mentioned in verifier commentary on the Verreault survey; not a standalone verified claim). → **High-value lead for milestone M2.** Must confirm by reading the survey.
- Bodies of revolution, polygons, low dimensions `n=2,3`: **not covered** by any verified claim (absence ≠ nonexistence).

---

## 5. Variants & related work (Q5) `[3-0 where cited]`

- **Complex plank — Ball, "The complex plank problem", Bull. LMS 33 (2001):** if `v₁,…,vₙ` unit in `ℂᵈ` and `tₖ≥0` with `Σtₖ²=1`, then `∃` unit `v` with `|⟨vₖ,v⟩| ≥ tₖ` for all `k`. (This is exactly the "strong polarization in ℂ" shape — same family as the 2026 weighted inequality with `pⱼ=tⱼ²`.)
- **Balitskiy, arXiv:2003.06707 (2020):** generalizes **Bang and Kadets** inequalities to multiple planks; §5 states the **normed/non-symmetric counterparts are "widely open"** — the symmetric one is Ball's.
- **Polarization ↔ plank bridge:** Ball's plank solution yields the real-Banach bound `‖f₁‖···‖fₙ‖ ≤ nⁿ ‖f₁···fₙ‖`, i.e. `cₙ(X) ≤ nⁿ` — the explicit link to **linear polarization constants** (Benítez–Sarantopoulos–Tonge; Révész–Sarantopoulos; Pinasco; Matolcsi–Muñoz). Pinasco–Carando–Rodríguez "Non-linear Plank Problems" (arXiv:1507.02316) already pushes product-of-polynomial bounds into plank statements.
- **Kupavskii–Pach, "From Tarski's plank problem to simultaneous approximation", Amer. Math. Monthly (2017):** frames the affine plank problem inside simultaneous Diophantine approximation.

---

## 6. The 2026 algebraic-variational engine (Q6 context)

- The angle "recent-algebraic-variational-methods" surfaced **arXiv:2605.28744** (likely the Martínez–Ortega-Moreno polarization solution or a close relative — *to be pulled and read*) and the already-in-hand Galicer–Ortega-Moreno–Pinasco 2606.02567.
- The engine = critical-point system `yⱼ(Ay)ⱼ=αⱼ` (degree-2, `A=G⁻¹`), all-real simple solutions (Bézout `2ⁿ`), one per sign-chamber, + **Euler–Jacobi vanishing** to force a good root. (Full re-derivation in `notes/method-abstraction.md`.)

---

## 7. Has the engine been applied to planks? (Q6/Q7) — APPARENTLY NOT `[absence of evidence]`

- **No verified claim** found that Euler–Jacobi / BKK (Bernstein 1975) / Morse-theoretic solution-counting has been applied to the affine plank or relative-width problem. The deep-research `openQuestions` flags this explicitly as unaddressed.
- **No 2023–2026 preprint** (beyond Bakaev–Yehudayoff and the Verreault survey) claims a full resolution or further substantial advance on the general affine conjecture.
- ⚠️ **Caveat (epistemic):** "no verified evidence" ≠ "proven nobody did it." Before staking the paper's novelty claim, run a **targeted negative search** (Google Scholar citations of M–OM 2605/2606; "plank" + "Euler–Jacobi"/"BKK"/"Bernstein theorem"; cite-trees of 1604.00456 and 2602.20290).

---

## 8. Killed / unreliable items (intellectual honesty)

- **KILLED `0-3`:** "Chambers & Mouille treat the general case / settle `n=2`." FALSE — their general-case contribution is exactly the two *partial* results in §4 (one conditional, one weaker bound). Do not overstate.
- **WITHDRAWN:** arXiv:2203.11260 "The symmetric plank problem, revisited" was withdrawn due to an **error in its Lemma 2**. Use only for historical/attribution context, **never as an independent proof**.
- Bang's two-plank verification is attributed by some to his **1953** paper rather than the 1951 Proc. AMS one — minor bibliographic ambiguity to resolve.
- Verreault "Conjecture 2.6" label taken from arXiv:2203.05540 (the BLMS PDF was paywalled, HTTP 402).

---

## 9. Key references (consolidated)

| Tag | Reference | Role |
|---|---|---|
| Tarski32 | A. Tarski, *Remarks on the degree of equivalence of polygons*, Parametr 2 (1932) | origin (absolute) |
| Bang51 | T. Bang, *A solution of the "plank problem"*, Proc. AMS 2 (1951) 990–993 | proves absolute; poses affine |
| Ball91 | K. Ball, *The plank problem for symmetric bodies*, Invent. Math. 104 (1991) 535–543 | **symmetric case solved** |
| Ball01 | K. Ball, *The complex plank problem*, Bull. LMS 33 (2001) 433–442 | complex variant |
| BL09 | Bezdek–Litvak, *Covering convex bodies by cylinders…*, J. Geom. Anal. 19 (2009) 233–243 | bound 1/d |
| CM16 | Chambers–Mouille, *A note on the affine-invariant plank problem*, arXiv:1604.00456 | 2/(1+d) + conditional + projection bound |
| Bal20 | A. Balitskiy, arXiv:2003.06707 (2020) | Bang/Kadets multi-plank; normed open |
| KP16/17 | Kupavskii–Pach, arXiv:1511.08111; Amer. Math. Monthly 2017 | survey + Diophantine link |
| Ver26 | W. Verreault, *Plank theorems and their applications: A survey*, Bull. LMS (2026); arXiv:2203.05540 | **most up-to-date survey** |
| BY26 | **Bakaev–Yehudayoff, *A note on the affine plank conjecture*, arXiv:2602.20290 (Feb 2026)** | **current best bound 2/(1+√d); LIVE COMPETITION** |
| MOM26 | Martínez–Ortega-Moreno, *A solution to the polarization problem* (2026); cf. arXiv:2605.28744 | the engine |
| GOP26 | Galicer–Ortega-Moreno–Pinasco, arXiv:2606.02567 | weighted engine + Hilbert plank |

**Must-read-next (in `refs/`):** Ball91 (the proof to "Euler–Jacobi-ify"), CM16 (the conditional-convexity theorem — strikingly close to a variational reformulation), BY26 (the number to beat + their method), Verreault survey (to confirm the Ambrus→simplex reduction).
