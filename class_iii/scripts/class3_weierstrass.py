"""Class III surface V_III: Y^2 = X(X+1)T(T+1)(X+T+1).
Weierstrass model (fixing T=t, standard scaling X'=t(t+1)X, Y'=t(t+1)Y,
verified against the known original-surface transformation as a sanity
check in class3_surface3.py):

    a2(t) = t(t+1)(t+2),   a4(t) = t^2(t+1)^3,   a6 = 0.

This script computes c4,c6,Delta,j and classifies all bad fibers exactly
as in the main manuscript's Appendix A.
"""
import sympy as sp

t = sp.symbols('t')
a2 = t*(t+1)*(t+2)
a4 = t**2*(t+1)**3
a6 = 0

b2, b4, b6, b8 = 4*a2, 2*a4, 4*a6, 4*a2*a6 - a4**2
c4 = sp.expand(b2**2 - 24*b4)
c6 = sp.expand(-b2**3 + 36*b2*b4 - 216*b6)
Delta = sp.factor(sp.expand((c4**3 - c6**2) / 1728))
c4f = sp.factor(c4)
c6f = sp.factor(c6)
j = sp.simplify(c4**3 / Delta)

print("c4 =", c4f)
print("c6 =", c6f)
print("Delta =", Delta)
print("j =", sp.factor(j))

def ord_at(expr, t0):
    expr = sp.together(expr)
    ser = sp.series(expr, t, t0, 14).removeO()
    ser = sp.expand(ser)
    if ser == 0:
        return ">=14"
    h = sp.Symbol('h')
    terms = sp.Poly(sp.expand(ser.subs(t, h + t0)), h).terms()
    return min(term[0][0] for term in terms)

print()
print("=== bad fiber orders ===")
# find roots of Delta (finite t)
Delta_poly = sp.factor(Delta)
print("Delta factored:", Delta_poly)
roots = sp.roots(sp.Poly(sp.numer(sp.together(Delta)), t))
print("roots of Delta (finite t):", roots)

for t0 in [0, -1, -2]:
    print(f"t={t0}: ord(c4)={ord_at(c4,t0)}, ord(c6)={ord_at(c6,t0)}, ord(Delta)={ord_at(Delta,t0)}")

print()
print("deg c4 =", sp.degree(sp.Poly(c4,t)), " deg c6=", sp.degree(sp.Poly(c6,t)), " deg Delta=", sp.degree(sp.Poly(Delta,t)))
