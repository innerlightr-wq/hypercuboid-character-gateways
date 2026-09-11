"""Round 8: Gateway G -- global S_n coordinate symmetry (not just the S_{n-1}
subgroup fixing the algebraically-eliminated coordinate) as an exact source
of sign relations among Sigma_S(p) values.

Setup (n=4, d=3): A1=x0, A2=x1, A3=x2, A4=-(x0+x1+x2) (the eliminated
coordinate). The 7 representative forms L_J, J subseteq {1,2,3} nonempty,
correspond exactly to the 7 ways to bipartition {1,2,3,4} into two nonempty
parts (each bipartition {K,K^c} gives L = +-A_K since sum of all 4 is 0):
  - 4 "1-3" bipartitions <-> singletons L_1=A1,L_2=A2,L_3=A3 and L_123=-A4.
  - 3 "2-2" bipartitions <-> pairs L_12,L_13,L_23 (each = -(the other pair)).
S_4 acts on these bipartitions (hence on the 7 forms, up to sign) via its
natural action on {1,2,3,4}. This script builds that action explicitly,
verifies the two Round-7 empirical facts as EXACT polynomial identities
(hence true for every prime p, not just tested ones), and cross-checks by
direct brute-force enumeration.
"""

import itertools
import sys
from pathlib import Path

import sympy

sys.path.insert(0, str(Path(__file__).parent))
from core import ZeroSectorSystem, chi_columns, sigma_S  # noqa: E402

x0, x1, x2 = sympy.symbols("x0 x1 x2")
XVARS = (x0, x1, x2)


def A(i, xx):
    if i == 1:
        return xx[0]
    if i == 2:
        return xx[1]
    if i == 3:
        return xx[2]
    if i == 4:
        return -(xx[0] + xx[1] + xx[2])
    raise ValueError(i)


def P_of(S_labels, xx):
    """S_labels: list of frozensets J subseteq {1,2,3} (1-indexed) defining
    the product of forms L_J = sum_{j in J} A_j."""
    prod = 1
    for J in S_labels:
        prod *= sum(A(j, xx) for j in J)
    return prod


# The three residual n=4 classes from Round 7, in 1-indexed A-coordinate form.
CLASS_I = [frozenset({1}), frozenset({2}), frozenset({3}),
           frozenset({1, 2}), frozenset({1, 3}), frozenset({2, 3})]
CLASS_II = [frozenset({2}), frozenset({3}),
            frozenset({1, 2}), frozenset({1, 3}), frozenset({2, 3}),
            frozenset({1, 2, 3})]
CLASS_III = [frozenset({1}), frozenset({2}), frozenset({3}),
             frozenset({1, 3}), frozenset({2, 3}), frozenset({1, 2, 3})]

P_I = sympy.expand(P_of(CLASS_I, XVARS))
P_II = sympy.expand(P_of(CLASS_II, XVARS))
P_III = sympy.expand(P_of(CLASS_III, XVARS))


def apply_perm(expr, perm):
    """perm: tuple (sigma(1),sigma(2),sigma(3),sigma(4)), 1-indexed images.
    Substitutes new-A_i := old-A_{sigma(i)} for i=1,2,3 (A4 determined)."""
    newx = (A(perm[0], XVARS), A(perm[1], XVARS), A(perm[2], XVARS))
    return sympy.expand(expr.subs({x0: newx[0], x1: newx[1], x2: newx[2]},
                                   simultaneous=True))


def scan_all_relations():
    named = {"P_I": P_I, "P_II": P_II, "P_III": P_III}
    found = []
    for perm in itertools.permutations([1, 2, 3, 4]):
        for pname, P in named.items():
            Pt = apply_perm(P, perm)
            for qname, Q in named.items():
                if sympy.expand(Pt - Q) == 0 and not (pname == qname and perm == (1, 2, 3, 4)):
                    found.append((perm, pname, "+1", qname))
                if sympy.expand(Pt + Q) == 0:
                    found.append((perm, pname, "-1", qname))
    return found


def verify_class_I_II_relation():
    """perm = 4-cycle (2,3,4,1): T(A1,A2,A3)=(A2,A3,A4). Claim:
    P_I(T(x)) = -P_II(x) identically (polynomial identity over Z)."""
    perm = (2, 3, 4, 1)
    Pt = apply_perm(P_I, perm)
    identity_holds = sympy.expand(Pt + P_II) == 0
    # T is the linear map with matrix given by expressing (A2,A3,A4) in x:
    Tmat = sympy.Matrix([[0, 1, 0], [0, 0, 1], [-1, -1, -1]])
    det = Tmat.det()
    return identity_holds, det


def verify_class_III_involution():
    """perm = double transposition (1 3)(2 4): T(A1,A2,A3)=(A3,A4,A1).
    Claim: P_III(T(x)) = -P_III(x) identically."""
    perm = (3, 4, 1)  # A1->A3, A2->A4, A3->A1  (perm tuple gives images of 1,2,3)
    # apply_perm expects a 4-tuple (perm[0..2] used, perm[3] unused since A4 derived)
    perm4 = (3, 4, 1, 2)
    Pt = apply_perm(P_III, perm4)
    identity_holds = sympy.expand(Pt + P_III) == 0
    Tmat = sympy.Matrix([[0, 0, 1], [-1, -1, -1], [1, 0, 0]])
    det = Tmat.det()
    is_involution = Tmat * Tmat == sympy.eye(3)
    # fixed locus: solve Tmat*v = v
    t = sympy.Symbol("t")
    # from earlier hand solve: x2=x0, x1=-x0
    on_line = sympy.expand(P_III.subs({x0: t, x1: -t, x2: t}))
    return identity_holds, det, is_involution, on_line


def brute_force_check(primes):
    sys4 = ZeroSectorSystem.build(4)

    def idx_tuple(class_labels):
        # map 1-indexed A-subsets in {1,2,3} to 0-indexed core.py subset indices
        out = []
        for J in class_labels:
            J0 = frozenset(j - 1 for j in J)
            out.append(sys4.subsets.index(J0))
        return tuple(sorted(out))

    S_I = idx_tuple(CLASS_I)
    S_II = idx_tuple(CLASS_II)
    S_III = idx_tuple(CLASS_III)

    def chi(a, p):
        a %= p
        if a == 0:
            return 0
        return 1 if pow(a, (p - 1) // 2, p) == 1 else -1

    rows = []
    for p in primes:
        cols, _ = chi_columns(sys4, p)
        sI = sigma_S(cols, S_I)
        sII = sigma_S(cols, S_II)
        sIII = sigma_S(cols, S_III)
        chi_m1 = chi(-1, p)
        rows.append((p, p % 4, p % 8, sI, sII, sIII, chi_m1,
                     sI == chi_m1 * sII, (p % 4 == 3 and sIII == 0) or (p % 4 == 1)))
    return rows


if __name__ == "__main__":
    print("=== Exhaustive S_4-permutation scan of sign relations among P_I,P_II,P_III ===")
    for rel in scan_all_relations():
        print(" ", rel)

    print("\n=== Class I <-> Class II relation (proved) ===")
    ok, det = verify_class_I_II_relation()
    print(f"  P_I(T(x)) + P_II(x) == 0 identically: {ok}   (T = 4-cycle (1 2 3 4), det={det})")

    print("\n=== Class III self-relation / vanishing mechanism (proved) ===")
    ok2, det2, invol, on_line = verify_class_III_involution()
    print(f"  P_III(T(x)) + P_III(x) == 0 identically: {ok2}   (T = double-transp (13)(24), det={det2})")
    print(f"  T is an involution (T^2=I): {invol}")
    print(f"  P_III restricted to T's fixed line: {on_line}  (must be 0 for consistency)")

    print("\n=== Independent brute-force reproduction (core.py, direct enumeration) ===")
    primes = [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]
    rows = brute_force_check(primes)
    print(f"{'p':>4} {'p%4':>4} {'p%8':>4} {'Sigma_I':>10} {'Sigma_II':>10} {'Sigma_III':>10} {'chi(-1)':>8} {'I=chi(-1)*II':>13} {'III-dichotomy':>14}")
    all_ok_a = True
    all_ok_b = True
    for p, m4, m8, sI, sII, sIII, cm1, okA, okB in rows:
        print(f"{p:>4} {m4:>4} {m8:>4} {sI:>10} {sII:>10} {sIII:>10} {cm1:>8} {str(okA):>13} {str(okB):>14}")
        all_ok_a &= okA
        all_ok_b &= okB
    print(f"\nAll primes satisfy Sigma_I = chi(-1)*Sigma_II: {all_ok_a}")
    print(f"All primes satisfy the Class III p mod 4 dichotomy: {all_ok_b}")
