"""Part IV/V: dependency-lattice and matroid-circuit analysis of the
corank>=2 unresolved n=4 cores (and the n=5 corank-2/corank-0 examples)."""

import itertools
import sys
from pathlib import Path

import sympy

sys.path.insert(0, str(Path(__file__).parent))
from core import ZeroSectorSystem  # noqa: E402


def to_forms(sys_, S):
    d = sys_.d
    out = []
    for j in S:
        v = [0] * d
        for i in sys_.subsets[j]:
            v[i] = 1
        out.append(v)
    return out


def primitive(v):
    L = 1
    for x in v:
        L = sympy.ilcm(L, sympy.Rational(x).q)
    v2 = [int(x * L) for x in v]
    g = 0
    for x in v2:
        g = sympy.igcd(g, x)
    if g != 0:
        v2 = [x // g for x in v2]
    return tuple(v2)


def find_circuits(forms, labels):
    """All minimal dependent subsets (matroid circuits), by brute force
    over subset size (fine at these small sizes: <=7 forms)."""
    m = len(forms)
    circuits = []
    for size in range(2, m + 1):
        for combo in itertools.combinations(range(m), size):
            sub = [forms[i] for i in combo]
            rank = sympy.Matrix(sub).rank()
            if rank < size:  # dependent
                # minimal? every proper subset must be independent
                minimal = True
                for j in combo:
                    rest = [forms[i] for i in combo if i != j]
                    if sympy.Matrix(rest).rank() < len(rest):
                        minimal = False
                        break
                if minimal:
                    # get the primitive dependency coefficients for this circuit
                    M = sympy.Matrix(sub)
                    ns = M.T.nullspace()
                    coeffs = primitive(list(ns[0])) if len(ns) == 1 else None
                    circuits.append({
                        "labels": tuple(labels[i] for i in combo),
                        "size": size,
                        "coeffs": coeffs,
                    })
    return circuits


def analyze(sys_, S, name):
    forms = to_forms(sys_, S)
    circuits = find_circuits(forms, S)
    print(f"\n=== {name}: S={S} ===")
    print(f"  {len(circuits)} circuits found:")
    for c in circuits:
        prod = None
        if c["coeffs"]:
            prod = 1
            for x in c["coeffs"]:
                prod *= x
        print(f"   size={c['size']} labels={c['labels']} coeffs={c['coeffs']} "
              f"product={prod}")
    return circuits


if __name__ == "__main__":
    sys4 = ZeroSectorSystem.build(4)
    unresolved4 = [(0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 6), (0, 1, 2, 3, 5, 6),
                   (0, 1, 2, 4, 5, 6), (0, 1, 3, 4, 5, 6), (0, 2, 3, 4, 5, 6),
                   (1, 2, 3, 4, 5, 6)]
    all_circuits = {}
    for S in unresolved4:
        all_circuits[S] = analyze(sys4, S, "n=4 unresolved")

    sys5 = ZeroSectorSystem.build(5)
    analyze(sys5, (4, 5, 6, 7, 8, 9), "n=5 all-6-pairs (corank 2)")
    analyze(sys5, (10, 11, 12, 13), "n=5 all-4-triples (corank 0)")
