"""Round 25: explicit ORDINARY (non-weighted) blow-up sequence resolving
part of the I_2^* singularity at t=0.

Found this round (all verified by exact Jacobian/Hessian computation):

  Blow-up 1 (X=t*x1, Y=t*y1): exceptional component
      C1 = {t=0, y1=0},  smooth for x1 not in {0,-1},
           smooth through x1=infinity too (second chart checked).
  Blow-up 2a (at x1=-1): nondegenerate ternary quadric -> smooth conic
      M_a (matches N / T2's component from Round 18).
  Blow-up 2b (X1=t*A part, i.e. x1=t*A, y1=t*B): exceptional component
      C2 = {t=0, B=0}, smooth for A not in {0,-1}.
  Blow-ups 3a, 3b (at A=-1 and A=0 of C2): both nondegenerate ternary
      quadrics -> smooth conics M_b, M_c (match F1, F2).

Every M_* is unconditionally F_p-rational for every odd p (nondegenerate
ternary quadratic forms over finite fields are always isotropic).

NOT resolved this round: assembling {O,N}-C1-C2-{F1,F2} gives only 6
components / 5 edges, failing the Euler-number check (needs 7/6 to match
e(I_2^*)=8). A third interior node (or hidden structure at C1's meeting
with the identity component) remains to be found -- see
notes/round25_report.md.
"""
import sympy

t, X, Y, x1, y1, t2, y2, A, B = sympy.symbols("t X Y x1 y1 t2 y2 A B")
a2 = t * (t + 1) ** 2
a4 = t ** 3 * (t + 1) ** 2
F = sympy.expand(Y ** 2 - (X ** 3 + a2 * X ** 2 + a4 * X))


def leading_quadratic_form(expr, vars_):
    poly = sympy.Poly(expr, *vars_)
    return sum(c * sympy.prod(v ** e for v, e in zip(vars_, m))
               for m, c in poly.terms() if sum(m) == 2)


if __name__ == "__main__":
    print("=== Blow-up 1: X=t*x1, Y=t*y1 ===")
    Fsub = sympy.expand(F.subs({X: t * x1, Y: t * y1}))
    F1 = sympy.simplify(Fsub / t ** 2)
    print("F1 =", sympy.expand(F1))
    print("F1(0,x1,y1) =", F1.subs(t, 0))
    for x1v in [0, -1]:
        pt = {t: 0, x1: x1v, y1: 0}
        print(f"  at x1={x1v}: dF1/dt={sympy.diff(F1,t).subs(pt)}, "
              f"dF1/dx1={sympy.diff(F1,x1).subs(pt)}, dF1/dy1={sympy.diff(F1,y1).subs(pt)}")

    print("\n=== second chart of blow-up 1: t=X*t2, Y=X*y2 (checks x1=infinity) ===")
    Gsub = sympy.expand(F.subs({t: X * t2, Y: X * y2}))
    G2 = sympy.simplify(Gsub / X ** 2)
    pt0 = {X: 0, t2: 0, y2: 0}
    print(f"  at t2=0: dG2/dX={sympy.diff(G2,X).subs(pt0)} (nonzero => smooth, C1 extends through x1=inf)")

    print("\n=== Blow-up 2a: near x1=-1, w2=x1+1 ===")
    w2 = sympy.Symbol("w2")
    F1w = sympy.expand(F1.subs(x1, -1 + w2))
    quad = leading_quadratic_form(F1w, (t, w2, y1))
    print("  leading quadratic form:", quad, " Hessian det:", sympy.hessian(quad, (t, w2, y1)).det())

    print("\n=== Blow-up 2b: x1=t*A, y1=t*B ===")
    Gsub2 = sympy.expand(F1.subs({x1: t * A, y1: t * B}))
    G = sympy.simplify(Gsub2 / t ** 2)
    print("  G =", sympy.expand(G))
    for Av in [0, -1]:
        pt = {t: 0, A: Av, B: 0}
        print(f"  at A={Av}: dG/dt={sympy.diff(G,t).subs(pt)}")

    print("\n=== Blow-ups 3a/3b: near A=-1 and A=0 ===")
    w3 = sympy.Symbol("w3")
    Gw = sympy.expand(G.subs(A, -1 + w3))
    quad2 = leading_quadratic_form(Gw, (t, w3, B))
    print("  at A=-1, leading form:", quad2, " det:", sympy.hessian(quad2, (t, w3, B)).det())
    quad3 = leading_quadratic_form(G, (t, A, B))
    print("  at A=0,  leading form:", quad3, " det:", sympy.hessian(quad3, (t, A, B)).det())
