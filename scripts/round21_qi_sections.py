"""Round 21: the four (not six -- see notes/round21_report.md Part I
correction) Round-20 candidate polynomials define genuine sections over
Q(i)(t), forming a single torsion orbit of a single non-torsion,
height-1 generator.

Correction to Round 20's report: only 4 DISTINCT polynomials appear
among the 10 raw pattern-instances that reached the square-condition
check (multiplicities 3,3,3,1 across the (O,N,N_i,F1), (N,O,N_i,N),
(F1,N,N_i,O), and (F2,O,O,F2) pattern families respectively) -- Round
20's report said "6", which was an arithmetic slip in that summary
paragraph (the underlying case-by-case table and code output were
themselves correct). This is fixed here per Round 21 Part I's own
instruction to reconcile before proceeding.
"""
import sympy

t = sympy.symbols("t")
I = sympy.I
a2 = t * (t + 1) ** 2
a4 = t ** 3 * (t + 1) ** 2


def rhs(X):
    return sympy.expand(X ** 3 + a2 * X ** 2 + a4 * X)


X1, q1 = -(t + 1), (t - 1) * (t + 1) ** 2
X2, q2 = -t * (t + 1) ** 2, t ** 2 * (t + 1) ** 2
X3, q3 = -t ** 2, t ** 3
X4, q4 = -t ** 3 * (t + 1), t ** 3 * (t - 1) * (t + 1) ** 2

POINTS = {
    "P1": (X1, I * q1),
    "P2": (X2, I * q2),
    "P3": (X3, I * q3),
    "P4": (X4, I * q4),
}

T = {"O": sympy.Integer(0), "T2": -t * (t + 1), "T3": -t ** 2 * (t + 1)}


def add(P1, P2):
    x1, y1 = P1
    x2, y2 = P2
    if sympy.simplify(x1 - x2) == 0:
        return None
    lam = sympy.simplify((y2 - y1) / (x2 - x1))
    x3 = sympy.simplify(lam ** 2 - a2 - x1 - x2)
    y3 = sympy.simplify(lam * (x1 - x3) - y1)
    return (x3, y3)


if __name__ == "__main__":
    print("=== verify all four are genuine points (RHS = (i*q)^2 exactly) ===")
    for name, (X, Y) in POINTS.items():
        ok = sympy.simplify(rhs(X) - Y ** 2) == 0
        print(f"{name}: X={X}  RHS-(iq)^2==0: {ok}")

    print("\n=== torsion-orbit structure (P1 as base point) ===")
    for tname, tx in [("T2", T["T2"]), ("T3", T["T3"])]:
        res = add(POINTS["P1"], (tx, sympy.Integer(0)))
        for qn, Q in POINTS.items():
            if sympy.simplify(res[0] - Q[0]) == 0:
                sign = "+" if sympy.simplify(res[1] - Q[1]) == 0 else "-"
                print(f"P1 + {tname} = {sign}{qn}")

    print("\n=== height-1 dictionary check for P1 ===")
    print("x1(0) =", X1.subs(t, 0), " (!=0 => identity @ t=0)")
    print("x1(1) =", X1.subs(t, 1), " (== -2 => nontrivial @ t=1)")
    print("x1(-1) =", X1.subs(t, -1), " (== 0 => named @ t=-1)")
    print("deg(x1) =", sympy.Poly(X1, t).degree(), " (<=2 => F @ infinity)")

    print("\n=== complex conjugation (i -> -i, t fixed) ===")
    Y1 = POINTS["P1"][1]
    print("sigma(Y1) =", Y1.subs(I, -I), " == -Y1:", sympy.simplify(Y1.subs(I, -I) + Y1) == 0)

    print("\n=== numeric specialization check, t=2 ===")
    x0 = X1.subs(t, 2)
    y0 = Y1.subs(t, 2)
    print(f"x(2)={x0}, y(2)={y0}, y^2={sympy.expand(y0**2)}, "
          f"RHS(2)={rhs(X1).subs(t,2)}, match: {sympy.simplify(y0**2-rhs(X1).subs(t,2))==0}")
