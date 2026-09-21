"""Verify that X_III is the lambda = -1 member of the Ahlgren-Ono-Penniston family.

Three independent checks, all exact (integer arithmetic only, no floating point):

  1.  CHARACTER SUM.  T(p) = A(-1, p) for every odd prime tested, where
          T(p)        = sum_{x,t} chi( x t (t+1)(x+t)(x+t+1) )          [this paper]
          A(lambda,p) = sum_{x,y} chi( x y (x+1)(y+1)(x + lambda y) )   [AOP]

  2.  BRANCH SEXTIC.  The Q-linear substitution (x,t,w) -> (x, t-x, -t-w) carries
      the branch sextic of X_III onto the branch sextic of the lambda = -1 member
      EXACTLY -- with no residual scalar -- so the two double covers, and hence
      their minimal resolutions, are isomorphic over Q.  Verified by expanding
      both degree-6 forms as integer polynomials and comparing coefficients.

  3.  AOP'S OWN EVALUATION DEGENERATES AT lambda = -1.  AOP evaluate A(lambda,q)
      in closed form via chi(lambda+1) * (a(lambda,q)^2 - q), which requires
      lambda + 1 invertible.  The check confirms the closed form reproduces the
      direct sum at lambda = 8 and lambda = 2, and is undefined at lambda = -1.
      So X_III sits at precisely the parameter AOP's evaluation cannot reach.

Run:  python3 class_iii/scripts/class3_aop_identification.py
Exit code 0 on success.
"""

import itertools
import sys
from collections import defaultdict

PRIMES = [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]


def chi(a, p):
    """Quadratic character mod p."""
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def T_sum(p):
    """This paper's two-variable sum T(p)."""
    return sum(chi(x * t * (t + 1) * (x + t) * (x + t + 1), p)
               for x in range(p) for t in range(p))


def A_direct(lam, p):
    """AOP's two-variable sum A(lambda, p), as a direct sum."""
    return sum(chi(x * y * (x + 1) * (y + 1) * (x + lam * y), p)
               for x in range(p) for y in range(p))


def A_closed(lam, p):
    """AOP's closed-form evaluation; None where it degenerates."""
    lp1 = (lam + 1) % p
    if lp1 == 0:
        return None
    inv = pow(lp1, p - 2, p)
    a = -sum(chi((x - 1) * (x * x - inv), p) for x in range(p))
    return chi(lp1, p) * (a * a - p)


# ---------------------------------------------------------------- polynomials
# Sparse integer polynomials in (x, t, w) as {(i,j,k): coeff}.

def pmul(f, g):
    out = defaultdict(int)
    for m1, c1 in f.items():
        for m2, c2 in g.items():
            out[tuple(a + b for a, b in zip(m1, m2))] += c1 * c2
    return {m: c for m, c in out.items() if c}


def lin(cx, ct, cw):
    """The linear form cx*x + ct*t + cw*w."""
    f = {}
    for mono, c in (((1, 0, 0), cx), ((0, 1, 0), ct), ((0, 0, 1), cw)):
        if c:
            f[mono] = c
    return f


def product(forms):
    out = {(0, 0, 0): 1}
    for f in forms:
        out = pmul(out, f)
    return out


def substitute(f, M):
    """Substitute (x,t,w) -> M applied to (x,t,w); M is a 3x3 integer matrix."""
    images = [lin(*row) for row in M]
    out = defaultdict(int)
    for (i, j, k), c in f.items():
        term = pmul(pmul(product([images[0]] * i), product([images[1]] * j)),
                    product([images[2]] * k))
        for m, c2 in term.items():
            out[m] += c * c2
    return {m: c for m, c in out.items() if c}


def main():
    failures = []

    # ---- check 1: the character-sum identity -----------------------------
    print("1. character-sum identity  T(p) = A(-1, p)")
    for p in PRIMES:
        t, a = T_sum(p), A_direct(-1, p)
        flag = "ok" if t == a else "MISMATCH"
        if t != a:
            failures.append(f"T({p})={t} != A(-1,{p})={a}")
        print(f"     p = {p:3d}   T(p) = {t:7d}   A(-1,p) = {a:7d}   {flag}")

    # ---- check 2: the branch sextics agree after a Q-linear substitution --
    print("\n2. branch sextics, under (x,t,w) -> (x, t-x, -t-w)")
    # X_III : x t (t+w)(x+t)(x+t+w) w
    P_III = product([lin(1, 0, 0), lin(0, 1, 0), lin(0, 1, 1),
                     lin(1, 1, 0), lin(1, 1, 1), lin(0, 0, 1)])
    # AOP at lambda = -1 : x z (x+w)(z+w)(x - z) w
    P_AOP = product([lin(1, 0, 0), lin(0, 1, 0), lin(1, 0, 1),
                     lin(0, 1, 1), lin(1, -1, 0), lin(0, 0, 1)])
    M = [[1, 0, 0], [-1, 1, 0], [0, -1, -1]]
    got = substitute(P_III, M)
    same = got == P_AOP
    if not same:
        failures.append("branch sextics differ after substitution")
    print(f"     monomials in P_III(Mv) : {len(got)}")
    print(f"     monomials in P_AOP     : {len(P_AOP)}")
    print(f"     identical as integer polynomials (scalar exactly +1): {same}")

    # ---- check 3: AOP's closed form degenerates at lambda = -1 -----------
    print("\n3. AOP's closed-form evaluation")
    for lam in (8, 2):
        agree = all(A_direct(lam, p) == A_closed(lam, p) for p in PRIMES)
        if not agree:
            failures.append(f"closed form disagrees with direct sum at lambda={lam}")
        print(f"     lambda = {lam:2d}:  closed form reproduces the direct sum: {agree}")
    undef = all(A_closed(-1, p) is None for p in PRIMES)
    if not undef:
        failures.append("closed form unexpectedly defined at lambda = -1")
    print(f"     lambda = -1:  closed form UNDEFINED (lambda + 1 = 0): {undef}")
    print("     -> X_III sits at the one parameter AOP's evaluation cannot reach.")

    print()
    if failures:
        print("FAILURES:")
        for f in failures:
            print("   ", f)
        return 1
    print("all checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
