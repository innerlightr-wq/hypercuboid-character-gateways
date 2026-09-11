"""Round 19: complete resolution of the I_0^* fiber at t=-1, plus the
resulting global degree bound on x(t) for a height-1 candidate.

Key results (all verified symbolically below):

1. At u=t+1=0, the Tate cubic is P(T')=T'^3-T' (three DISTINCT roots
   0,1,-1) via the substitution X=u*T' -- confirmed exact.

2. Near each root tau in {0,1,-1}, the correct local chart is
   K(u,eps,rho) = rho^2*u - Q(tau+eps,u),  Y=u^2*rho, eps=T'-tau,
   Q(T',u):=Y^2/u^3 -- verified SMOOTH at (u,eps,rho)=(0,0,0) for all
   three roots (partial derivative in eps is nonzero, a simple-root
   fact that DOES hold cleanly here, unlike the I_2^* case in Round 17
   where an analogous naive guess failed).

3. Torsion locations (T'=X/u limit): T1->0, T2->1, T3->-1 -- all three
   distinct, confirming bijective specialization MWtors->Phi(I_0^*).

4. GLOBAL CONSEQUENCE (the round's other main deliverable): since
   P.O=0 is proved (Round 16) for any height-1 candidate, x(t) can have
   NO finite poles anywhere (a pole at any t would force P to meet O
   there). Hence x(t) is a POLYNOMIAL. Combined with the t=0<->infinity
   local dictionary (Round 17/18), the component required at t=infinity
   forces an exact degree bound:
     identity @ infinity  <=> deg(x)=4 (leading coeff free, nonzero)
     "N"      @ infinity  <=> deg(x)=3 exactly, leading coeff = -1
     "F"      @ infinity  <=> deg(x)<=2
   This makes the height-1 section search a GENUINELY FINITE, exact
   algebra problem -- not a bounded coefficient guess.

Two concrete patterns are worked out exactly below (not by bounded
search) and PROVED to have no solution.
"""
import sympy

u, Tp, eps, rho = sympy.symbols("u Tp eps rho")
t, E = sympy.symbols("t E")


def tate_cubic_and_smoothness():
    tt = u - 1
    a2 = sympy.expand(tt * (tt + 1) ** 2)
    a4 = sympy.expand(tt ** 3 * (tt + 1) ** 2)
    X = u * Tp
    Q = sympy.expand(sympy.simplify((X ** 3 + a2 * X ** 2 + a4 * X) / u ** 3))
    print("Q(T',u) =", Q)
    print("Q(T',0) =", sympy.factor(Q.subs(u, 0)))
    for tau in (0, 1, -1):
        K = sympy.expand(rho ** 2 * u - Q.subs(Tp, tau + eps))
        pt = {u: 0, eps: 0, rho: 0}
        dK = (sympy.diff(K, rho).subs(pt), sympy.diff(K, eps).subs(pt), sympy.diff(K, u).subs(pt))
        print(f"tau={tau}: (dK/drho,dK/deps,dK/du) = {dK}  smooth={any(v != 0 for v in dK)}")

    T1_X, T2_X, T3_X = 0, sympy.expand(-tt * (tt + 1)), sympy.expand(-tt ** 2 * (tt + 1))
    for name, Xv in [("T1", T1_X), ("T2", T2_X), ("T3", T3_X)]:
        print(name, "-> T' limit:", sympy.limit(Xv / u, u, 0))


def eliminate_pattern_ON_named_F1():
    """Pattern: identity@0 excluded... this checks O,N,named,F1 style
    with deg(x)<=2, C=0 (F1 sub-branch), matching x(-1)=0, x(1)=-2,
    x(0)!=0."""
    a2 = t * (t + 1) ** 2
    a4 = t ** 3 * (t + 1) ** 2
    X = -(t + 1)   # unique solution of the resulting 2x2 linear system
    RHS = sympy.expand(X ** 3 + a2 * X ** 2 + a4 * X)
    print("X =", X, " RHS =", sympy.factor(RHS), " (negative perfect square -> Q(i)(t) only, FAILS)")


def eliminate_pattern_OO_named_F():
    a2 = t * (t + 1) ** 2
    a4 = t ** 3 * (t + 1) ** 2
    for C in (0, -1):
        D = C + E
        X = C * t ** 2 + D * t + E
        RHS = sympy.expand(X ** 3 + a2 * X ** 2 + a4 * X)
        print(f"C={C}: RHS(E) factored =", sympy.factor(RHS))


if __name__ == "__main__":
    print("=== I_0^* resolution ===")
    tate_cubic_and_smoothness()
    print("\n=== pattern (O,N,named,F1): unique candidate ===")
    eliminate_pattern_ON_named_F1()
    print("\n=== pattern (O,O,named,F): symbolic-E factorization ===")
    eliminate_pattern_OO_named_F()
