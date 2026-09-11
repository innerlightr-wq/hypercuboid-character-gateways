"""Round 22: attempted (INCOMPLETE, see notes/round22_report.md Part
VII/VIII) exact affine/projective point-count bookkeeping.

Confirms, exactly:
  - naive Weierstrass fibers at t=0 and t=-1 (and at infinity, u=0) are
    all Y^2=X^3 (cuspidal), each with naive affine point count p.
  - the naive fiber at t=1 is Y^2=X'^2(X'-2) (nodal, X=X'-2), with
    naive affine point count p-chi(-2).

Also documents the CAUGHT ERROR: the I_2 fiber's component graph is a
2-cycle (2 edges between its 2 components), not a tree (1 edge) --
this changes its resolved point count from an initially-assumed
2p+1 to the corrected 2p.

The overall target identity
    affine(infinity) + sum_T (resolved(T) - naive_total(T)) == 18*p
needed for S(p)=chi(-1)(a_p(f)+p) to follow from the Lefschetz
formula does NOT close exactly with the counts derived here -- a
residual constant-order discrepancy remains, reported honestly as
unresolved rather than forced.
"""
import sympy

t, x, X = sympy.symbols("t x X")
p = sympy.Symbol("p")  # symbolic prime, chi(-2) tracked as a symbol


def chi(a, modp):
    a %= modp
    if a == 0:
        return 0
    return 1 if pow(a, (modp - 1) // 2, modp) == 1 else -1


def naive_affine_count(f_expr, xv, modp):
    """Count (x,y) in F_p^2 with y^2 = f_expr(x), via the 1+chi trick."""
    total = 0
    for xv0 in range(modp):
        val = int(f_expr.subs(xv, xv0)) % modp
        total += 1 + chi(val, modp)
    return total


if __name__ == "__main__":
    for modp in [5, 7, 11, 13]:
        # t=0, t=-1, infinity: Y^2 = X^3
        n_cusp = naive_affine_count(X**3, X, modp)
        # t=1: Y^2 = X'^2(X'-2)
        n_node = naive_affine_count(X**2 * (X - 2), X, modp)
        c2 = chi(-2, modp)
        print(f"p={modp}: naive(cusp)={n_cusp} (predict p={modp}), "
              f"naive(node)={n_node} (predict p-chi(-2)={modp - c2})")
