"""Round 17: explicit blow-up analysis of the I_2^* fiber at t=0.

Model: y^2 = x^3 + t(t+1)^2 x^2 + t^3(t+1)^2 x  (a6=0).

Confirmed this round (verified smoothness via partial derivatives,
not merely asserted):

  Substitution X = t^2*X1, Y = t^3*Y1, then dividing the transformed
  equation by t^5, gives a surface F(t,X1,Y1)=0 with
      F(0,X1,Y1) = -X1(X1+1)
  and F=0 is SMOOTH along the entire lines {X1=0} and {X1=-1} at t=0
  (dF/dX1 = -1 and +1 respectively, nonzero for every Y1). These are
  two of the I_2^* fiber's multiplicity-1 components.

  The known 2-torsion sections land as:
    T1 = (X=0)          -> X1 = X/t^2 = 0            (this chart)
    T3 = (X=-t^2(t+1))  -> X1 = -(t+1) -> -1 at t=0   (this chart)
    T2 = (X=-t(t+1))    -> X1 = -(t+1)/t -> pole (NOT in this chart)

  Attempting a naive chart for T2's direction (X=tW, Y=t^{3/2}... or
  Y=t*Y2) was tried and found to be SINGULAR / wrongly scaled at the
  point matching T2 -- an error caught and reported rather than
  silently patched (see round17_report.md, Part II/IV).
"""
import sympy

t, X1, Y1, W, Y2, w = sympy.symbols("t X1 Y1 W Y2 w")
a2 = t * (t + 1) ** 2
a4 = t ** 3 * (t + 1) ** 2


def chart_t2X1():
    X = t ** 2 * X1
    Y = t ** 3 * Y1
    eqn = sympy.expand(Y ** 2 - (X ** 3 + a2 * X ** 2 + a4 * X))
    F = sympy.simplify(eqn / t ** 5)
    return F


def check_smoothness(F, point):
    dY1 = sympy.diff(F, Y1).subs(point)
    dX1 = sympy.diff(F, X1).subs(point)
    dt = sympy.expand(sympy.diff(F, t).subs(point))
    return dY1, dX1, dt


if __name__ == "__main__":
    F = chart_t2X1()
    print("F(t,X1,Y1) =", sympy.expand(F))
    print("F(0,X1,Y1) =", sympy.factor(F.subs(t, 0)))
    for x1v in [0, -1]:
        d = check_smoothness(F, {t: 0, X1: x1v})
        print(f"at X1={x1v}, t=0: (dF/dY1, dF/dX1, dF/dt) = {d}")

    print()
    print("=== attempted naive chart for the T2 (simple-root) direction ===")
    X = -t + t * W
    G_try1 = sympy.expand((t * Y2) ** 2 - (X ** 3 + a2 * X ** 2 + a4 * X))
    G = sympy.simplify(G_try1 / t ** 2)
    print("G(t,W,Y2) =", sympy.expand(G))
    print("G(0,W,Y2) =", sympy.factor(G.subs(t, 0)))
    pt = {t: 0, W: 0, Y2: 0}
    print("at (t,W,Y2)=(0,0,0) [T2's naive image]:",
          "dG/dY2=", sympy.diff(G, Y2).subs(pt),
          " dG/dW=", sympy.diff(G, W).subs(pt),
          " dG/dt=", sympy.expand(sympy.diff(G, t).subs(pt)))
    print(">>> ALL THREE VANISH: this naive chart is SINGULAR at T2's",
          "image -- the Y=t*Y2 scaling guess was WRONG. Flagged, not fixed,",
          "this round.")
