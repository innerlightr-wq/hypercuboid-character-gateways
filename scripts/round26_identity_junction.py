"""Round 26: explicit construction of the identity component near O, and
its junction with C1 (Round 25).

Confirms:
  - identity = the standard (u,v) chart u=X/Y, v=1/Y (Z=1 implicit),
    equation H(t,u,v)=v-u^3-a2(t)u^2 v-a4(t)u v^2=0, SMOOTH for every
    finite (t,u,v) near (0,0,0) since dH/dv=1 identically at t=0 -- no
    blow-up needed on the identity side itself.
  - identity meets C1 at u=infinity (equivalently x1=infinity in C1's
    own chart, Round 25's second-chart check, dG2/dX=-1 there): CLEAN,
    already verified smooth in both directions.

New finding this round (NOT fully resolved): C2 (Round 25's second
interior node, from blowing up C1 at x1=0) has a THIRD marked point,
A=infinity (equivalently t3=0 in the x1=t3*x1, y1=t3*y3-style second
chart of that same blow-up), which was never checked in Round 25 --
and it IS singular, smooth only away from t3 in {0,-1}. Since t3=-1
already matches the known A=-1 node, the genuinely new content is at
t3=0 (A=infinity) -- the most likely location of the still-missing
third I_2^* interior component. Not fully disentangled from C2 itself
this round -- flagged for Round 27.
"""
import sympy

t, X, Y, u, v = sympy.symbols("t X Y u v")
a2 = t * (t + 1) ** 2
a4 = t ** 3 * (t + 1) ** 2


def check_identity_chart():
    H = sympy.expand(v - X ** 0 * 0)  # placeholder, real eq below
    H = v - u ** 3 - a2 * u ** 2 * v - a4 * u * v ** 2
    H = sympy.expand(H)
    print("H(t,u,v) =", H)
    print("H(0,u,v) =", H.subs(t, 0), " (v=u^3, a smooth graph)")
    pt = {t: 0, u: 0, v: 0}
    print("dH/dv at (0,0,0) =", sympy.diff(H, v).subs(pt), " (nonzero => smooth everywhere finite)")
    # check dH/dv nonzero for ARBITRARY finite u at t=0 (not just u=0)
    dHdv_at_t0 = sympy.diff(H, v).subs(t, 0)
    print("dH/dv at t=0 (any u,v) =", dHdv_at_t0, " -- identically 1, so smooth for ALL finite u")


def check_C2_third_point():
    x1, y1, A, B, t3, y3 = sympy.symbols("x1 y1 A B t3 y3")
    F1 = -t ** 4 * x1 - t ** 3 * x1 ** 2 - 2 * t ** 3 * x1 - 2 * t ** 2 * x1 ** 2 - t ** 2 * x1 - t * x1 ** 3 - t * x1 ** 2 + y1 ** 2
    print("\n=== C2's A=infinity point (second chart of blow-up 2) ===")
    Fsub3 = sympy.expand(F1.subs({t: x1 * t3, y1: x1 * y3}))
    G3 = sympy.simplify(Fsub3 / x1 ** 2)
    print("G3(x1,t3,y3) =", sympy.expand(G3))
    pt = {x1: 0, t3: 0, y3: 0}
    print("dG3/dx1 at (x1,t3,y3)=(0,0,0):", sympy.diff(G3, x1).subs(pt), " (t3(t3+1), vanishes at t3=0,-1)")
    print("  => singular at t3=0 (A=infinity, NEW, unexamined in Round 25) and t3=-1 (A=-1, already known)")


if __name__ == "__main__":
    check_identity_chart()
    check_C2_third_point()
