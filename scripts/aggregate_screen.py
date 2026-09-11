"""Round 7: screen candidate aggregate Q's for a given form family by
performing the exact symbolic substitution and reporting the resulting
FIBER multiplicity profile (as a function of the symbolic fiber
coordinates, with q held as a free parameter) -- this is a promise
SCREEN, not a derivation. Promising candidates (private coord, mult-2,
or a form collapsing to a pure function of q) are flagged for hand
derivation.
"""

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


def screen(forms, d, lam, labels=None):
    """lam: primitive integer coefficient vector for Q = lam . x.
    Substitutes x_{piv} = (q - sum_{i!=piv} lam_i x_i) / lam_piv for the
    first nonzero-coefficient coordinate piv, giving each form as an
    affine-in-(fiber vars, q) expression. Reports, for each form, whether
    it is: 'pure-q' (no fiber variables at all), 'free of coord k' for
    some k, and the fiber multiplicity vector.
    """
    piv = next(i for i in range(d) if lam[i] != 0)
    q = sympy.Symbol("q")
    xs = sympy.symbols(f"x0:{d}")
    fiber_vars = [xs[i] for i in range(d) if i != piv]
    x_piv_expr = (q - sum(lam[i] * xs[i] for i in range(d) if i != piv)) / lam[piv]

    subs_map = {xs[piv]: x_piv_expr}
    new_forms = []
    for f in forms:
        expr = sum(f[i] * xs[i] for i in range(d))
        expr = sympy.expand(expr.subs(subs_map))
        new_forms.append(expr)

    print(f"  lambda={lam} (pivot coord {piv}):")
    mult = {v: 0 for v in fiber_vars}
    for idx, (f, expr) in enumerate(zip(forms, new_forms)):
        involved = [v for v in fiber_vars if expr.coeff(v) != 0]
        for v in involved:
            mult[v] += 1
        tag = ""
        if not involved:
            tag = "  <-- PURE FUNCTION OF q (private-Q-style)"
        lbl = labels[idx] if labels else idx
        print(f"    form[{lbl}] = {expr}   involves={[str(v) for v in involved]}{tag}")
    print(f"    fiber multiplicity profile: {{{', '.join(f'{v}:{c}' for v,c in mult.items())}}}")
    return mult, new_forms


if __name__ == "__main__":
    sys4 = ZeroSectorSystem.build(4)
    cases = {
        "ClassI_exclude_full (0,1,2,3,4,5)": (0, 1, 2, 3, 4, 5),
        "ClassII_exclude_singleton (1,2,3,4,5,6)": (1, 2, 3, 4, 5, 6),
        "ClassIII_exclude_pair (0,1,2,4,5,6)": (0, 1, 2, 4, 5, 6),
    }
    candidates = [
        [1, 1, 1],   # coordinate sum
        [1, -1, 0],  # difference
        [1, 0, -1],
        [0, 1, -1],
        [1, 1, -1],
        [1, -1, -1],
        [2, -1, -1],
    ]
    for name, S in cases.items():
        forms = to_forms(sys4, S)
        print(f"\n=== {name}  S={S} ===")
        print("forms (original):", forms)
        for lam in candidates:
            screen(forms, 3, lam, labels=S)
