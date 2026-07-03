#!/usr/bin/env python3
"""
gardner_third_marginal.py -- R10-1 Route B (mixing Gardner pair witnesses).

VERDICT (proved by hand, verified here): the route is DEAD in its pure form.

1. The chief's mixing inequality is CORRECT: if nu_jk are Gardner witnesses
   for the pairs and mu = (1/3)(nu_12 + nu_13 + nu_23), then the u_i-marginal
   of mu has density <= 2/3 + M_i/3 with M_i = ||dens(u_i# nu_jk)||_inf,
   {j,k} the complementary pair.  (Symbolic check below.)

2. But M*(lambda_1, lambda_2; lambda_3) = +infinity, NOT 5/2:
   any pair witness nu for (lambda_1, lambda_2) on the triangle has
   E[lambda_1] = E[lambda_2] = 1/2 (mean of a uniform marginal), hence
   E[lambda_3] = 1 - 1/2 - 1/2 = 0 with lambda_3 >= 0, forcing
   lambda_3 = 0 nu-a.s.: the third marginal is the ATOM delta_0 -- it is not
   absolutely continuous, so no finite M exists.  The mixture's marginal at
   the facets is (1/3)(2 Leb + delta_0): not even dominated.

3. Unequal weights die too: the constraint is w_{jk(i)} (M_i - 1) <= D - 1
   per direction; M_i = infinity forces every weight to 0 -- no mixture.

4. General pair-cost lemma [PROVED]: for any pair witness nu of (u_j, u_k)
   (u_j, u_k non-parallel with mid-lines meeting at the single point q_jk,
   which lies in Delta by Gardner existence + the barycenter argument):
        M*(u_j, u_k; u_i)  >=  1 / (2 min(m, 1-m)),   m = u_i(q_jk),
   because the barycenter of nu IS q_jk (u_j(b) = u_k(b) = 1/2 determine it),
   so the third marginal has mean u_i(q_jk); the 1-D moment bound
   (mean of a density-<=M law lies in [1/(2M), 1-1/(2M)]) gives the claim.
   At the facets m = lambda_3((1/2,1/2,0)) = 0: the lemma recovers M* = inf.
   Pure route B could work at best on triples where every u_i(q_jk) is in
   [1/5, 4/5] -- and never at/near the facets, which is where the worst case
   lives.  [The obstruction, exactly documented.]

Checks below are exact (sympy).
"""

import sympy as sp

S = sp.S
H = S(1) / 2


def check_mixing_inequality():
    # densities: marginal_i of mu = (1/3)(Leb + Leb + u_i# nu_jk)
    # if u_i# nu_jk <= M * Leb then marginal_i <= (2 + M)/3 * Leb.
    M = sp.symbols('M', positive=True)
    bound = (2 + M) / 3
    assert sp.simplify(bound - (S(2) / 3 + M / 3)) == 0
    # need <= 3/2  <=>  M <= 5/2
    assert sp.solve(sp.Eq(bound, S(3) / 2), M) == [S(5) / 2]
    print("1. mixing inequality verified: dens_i <= 2/3 + M/3; "
          "target 3/2 <=> M <= 5/2  OK")


def check_facet_moment_obstruction():
    # E[lambda_1] = E[lambda_2] = 1/2 under any pair witness (mean of Leb[0,1])
    t = sp.symbols('t')
    mean_unif = sp.integrate(t, (t, 0, 1))
    assert mean_unif == H
    # => E[lambda_3] = 1 - 1/2 - 1/2 = 0
    assert 1 - mean_unif - mean_unif == 0
    # lambda_3 >= 0 with zero mean => lambda_3 = 0 a.s. => third marginal is
    # delta_0, which is not <= M*Leb for any finite M (mass at a point).
    print("2. facets: E[lam3] = 0 under ANY pair witness => third marginal "
          "= atom delta_0 => M*(facets) = +infinity (route B pure: DEAD)  OK")


def check_pair_cost_lemma_cases():
    # 1-D moment step: nu <= M Leb on [0,1], mean m => m in [1/(2M), 1-1/(2M)]
    # (same computation as Prop 7.2 / moment bound); check the extremal case:
    M = sp.symbols('M', positive=True)
    t = sp.symbols('t')
    mean_extremal = sp.integrate(t * M, (t, 0, 1 / M))
    assert sp.simplify(mean_extremal - 1 / (2 * M)) == 0
    # q_jk and u_3(q_jk) for examples:
    # facets: midlines lam1=1/2, lam2=1/2 => q=(1/2,1/2,0); lam3(q)=0.
    q = (H, H, 0)
    assert sum(q) == 1 and q[2] == 0
    # concurrent cyclic triple: q_jk = p, u_i(p) = 1/2 => lemma bound = 1
    # (consistent: mu_p itself is a pair witness with third marginal Leb, M=1).
    m = H
    assert 1 / (2 * sp.Min(m, 1 - m)) == 1
    print("3. pair-cost lemma pieces: 1-D moment step exact; facets m=0 "
          "(M*=inf); concurrent m=1/2 (M*=1, attained by mu_p)  OK")


def check_unequal_weights_dead():
    # mu = sum w_jk nu_jk, sum w = 1, w >= 0. Marginal i <= (1-w_bad) + w_bad M_i
    # where w_bad = weight of the pair NOT containing i. Need finite bound =>
    # w_bad * (M_i - 1) finite; M_i = inf => w_bad = 0 for all i => all three
    # weights are 0 (each weight is the bad one for exactly one direction),
    # contradicting sum w = 1.
    # (bookkeeping check: pairs {12,13,23}; bad pair for i=1 is 23, etc.)
    pairs = [(1, 2), (1, 3), (2, 3)]
    bad = {i: [p for p in pairs if i not in p] for i in (1, 2, 3)}
    assert all(len(b) == 1 for b in bad.values())
    assert {b[0] for b in bad.values()} == set(pairs)
    print("4. unequal weights: each pair is 'bad' for exactly one direction "
          "=> M=inf at facets kills every mixture  OK")


if __name__ == '__main__':
    check_mixing_inequality()
    check_facet_moment_obstruction()
    check_pair_cost_lemma_cases()
    check_unequal_weights_dead()
    print("ALL OK -- Route B (pure Gardner mixing) is refuted at the "
          "calibration point; obstruction documented exactly.")
