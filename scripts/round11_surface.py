"""Round 11: minimal Weierstrass model / Kodaira fibers for the elliptic
surface underlying S(p), and the resulting closed-form identity found this
round:

    S(p) = -chi(2)*p + chi(-1)*a_p(E)^2       (COMPUTATIONALLY VERIFIED,
                                                see round11_report.md)

where E: y^2 = x^3+4x^2+2x is the CM-by-Z[sqrt(-2)] curve identified in
Hashimoto-Long-Yang, "Jacobsthal identity for Q(sqrt(-2))" (arXiv:1110.5815).
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


def a_p_E(p):
    """Trace of Frobenius for E: y^2=x^3+4x^2+2x (CM by Z[sqrt(-2)])."""
    s = sum(chi((x**3 + 4 * x**2 + 2 * x) % p, p) for x in range(p))
    return -s


def g(t, p):
    return sum(chi(x * (x + 1) * (x + t) % p, p) for x in range(p))


def S_of(p):
    return sum(chi(t * (t + 1) % p, p) * g(t, p) for t in range(p))


def invariants(a2, a4, a6):
    b2, b4, b6 = 4 * a2, 2 * a4, 4 * a6
    b8 = sympy.expand(4 * a2 * a6 - a4**2)
    c4 = sympy.expand(b2**2 - 24 * b4)
    c6 = sympy.expand(-b2**3 + 36 * b2 * b4 - 216 * b6)
    Delta = sympy.expand((c4**3 - c6**2) / 1728)
    return c4, c6, Delta


if __name__ == "__main__":
    t = sympy.symbols("t")
    a2, a4, a6 = t * (t + 1)**2, t**3 * (t + 1)**2, 0
    c4, c6, Delta = invariants(a2, a4, a6)
    j = sympy.factor(c4**3 / Delta)
    print("c4 =", sympy.factor(c4))
    print("c6 =", sympy.factor(c6))
    print("Delta =", sympy.factor(Delta))
    print("j =", j)

    print("\n=== master identity verification ===")
    sys4 = ZeroSectorSystem.build(4)
    S_I = (0, 1, 2, 3, 4, 5)
    ok_all = True
    for p in sympy.primerange(5, 200):
        ap = a_p_E(p)
        pred = -chi(2, p) * p + chi(-1, p) * ap * ap
        Sp = S_of(p)
        cols, _ = chi_columns(sys4, p)
        sI_direct = sigma_S(cols, S_I)
        sI_pred = (p - 1) * pred
        ok = (pred == Sp) and (sI_direct == sI_pred)
        ok_all &= ok
        if not ok:
            print(f"MISMATCH at p={p}: pred={pred}, S(p)={Sp}")
    print("all primes 5..200 match:", ok_all)
