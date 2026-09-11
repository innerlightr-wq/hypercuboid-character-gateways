"""Round 9: investigate the mod-8 pattern Sigma_I(p) = -chi(2) p(p-1) for
p == 5,7 (mod 8), found empirically in Round 8.

Key exact (unconditional, proved) findings implemented/checked here:

1. Projectivization: P_I is homogeneous of even degree 6, so chi(P_I(lam*x))
   = chi(lam)^6 * chi(P_I(x)) = chi(P_I(x)) for every lam != 0. Hence
   chi(P_I) is constant on every punctured line through the origin, giving
   Sigma_I(p) = (p-1) * sum_{lines in P^2(F_p)} chi(P_I(representative))
   for ANY even |S| (not special to Class I) -- an elementary, general fact.

2. Partial elimination (fix x2=c, x1=b, sum x0) gives an independent,
   concrete derivation of the same (p-1) factor:
      Sigma_I(p) = (p-1) * S(p),   S(p) = sum_{x,t in F_p} chi(x(x+1)t(t+1)(x+t))
   via the homogeneity of the cubic x(x+1)(x+t)-type sums appearing along
   the way (the classical Legendre family y^2 = x(x+1)(x+t)).
   Both routes verified to agree numerically.

3. S(p) = -chi(2)*p exactly iff p == 5,7 (mod 8) (equivalently chi(-2)=-1),
   with ZERO exceptions found up to p=229 -- but no first-principles proof
   of this specific evaluation was found this round (see round9_report.md).
"""

import sys
from pathlib import Path

import sympy

sys.path.insert(0, str(Path(__file__).parent))
from core import ZeroSectorSystem, chi_columns, sigma_S  # noqa: E402


def chi(a, p):
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def g(t, p):
    return sum(chi(x * (x + 1) * (x + t) % p, p) for x in range(p))


def S_of(p):
    return sum(chi(t * (t + 1) % p, p) * g(t, p) for t in range(p))


def projective_sum(P_I_expr, xs, p):
    """Directly verify Sigma_I(p) = (p-1) * sum over representatives of
    P^2(F_p) of chi(P_I(rep)), by brute enumeration of one representative
    per line (small p only -- this is a sanity check, not the main route)."""
    reps = []
    seen = set()
    for x0 in range(p):
        for x1 in range(p):
            for x2 in range(p):
                if (x0, x1, x2) == (0, 0, 0):
                    continue
                # normalize: first nonzero coordinate = 1
                v = (x0, x1, x2)
                if v in seen:
                    continue
                first_nz = next(c for c in v if c != 0)
                inv = pow(first_nz, p - 2, p)
                norm = tuple((c * inv) % p for c in v)
                for lam in range(1, p):
                    seen.add(tuple((c * lam) % p for c in norm))
                reps.append(norm)
    total = 0
    P_I_num = sympy.lambdify(xs, P_I_expr, 'math')
    for r in reps:
        val = int(P_I_num(*r)) % p
        total += chi(val, p)
    return total


if __name__ == "__main__":
    sys4 = ZeroSectorSystem.build(4)
    S_I = (0, 1, 2, 3, 4, 5)
    S_II = (1, 2, 3, 4, 5, 6)

    print(f"{'p':>4}{'p%8':>5}{'chi(-1)':>8}{'chi(2)':>7}{'chi(-2)':>8}"
          f"{'Sigma_I':>9}{'S(p)':>7}{'(p-1)S(p)':>11}{'match':>7}"
          f"{'Sigma_II':>9}{'p(p-1)pred':>11}{'IImatch':>8}")
    for p in [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]:
        cols, _ = chi_columns(sys4, p)
        sI = sigma_S(cols, S_I)
        sII = sigma_S(cols, S_II)
        Sp = S_of(p)
        pred = (p - 1) * Sp
        cm1, c2 = chi(-1, p), chi(2, p)
        cm2 = chi(-2, p)
        good = cm2 == -1
        iipred = p * (p - 1) if good else None
        print(f"{p:>4}{p%8:>5}{cm1:>8}{c2:>7}{cm2:>8}{sI:>9}{Sp:>7}{pred:>11}"
              f"{str(sI==pred):>7}{sII:>9}{str(iipred):>11}{str(iipred==sII if good else 'n/a'):>8}")
