"""Round 15: structured search for a canonical-height-1 non-torsion
section of the K3 elliptic surface Y^2=X^3+t(t+1)^2 X^2+t^3(t+1)^2 X.

Search classes tried (all NEGATIVE this round -- no section found):
  1. X(t) = A t^3+B t^2+C t+E, A in {0,-1} forced by the deg-9 leading
     coefficient A^2(A+1)=0; A=0 reduces to Round 12's linear case
     (already proved impossible); A=-1 checked exhaustively for
     integer B,C,E in [-6,6]^3 -- zero real (Q-rational) perfect
     squares (one spurious Q(i)-rational point at (B,C,E)=(-2,-1,0),
     X=-t(t+1)^2, correctly excluded: RHS=-t^4(t+1)^4 is a NEGATIVE
     perfect square, i.e. only a point over Q(i)(t)).
  2. X(t) = A t^4+B t^3+C t^2+D t+E, A in {1,-1}, B,C,D,E in [-3,3]^4:
     zero perfect squares found.
  3. X(t) = (A t^2+B t+C)/t^2 (pole of order 2 at t=0, the natural
     ansatz for meeting a non-identity component at the I_2^* fiber
     there), A,B,C in [-4,4], A!=0: zero perfect squares found.
  4. X(t) = (A t^2+B t+C)/(t+1)^2 (pole at t=-1, the I_0^* fiber),
     same range: zero perfect squares found.

None of these searches is exhaustive (rational, non-integer, or larger
coefficients, and other denominator shapes such as t(t+1) or degree-3
denominators, were not tried). Reported honestly as a substantial but
incomplete negative result -- see notes/round15_report.md.
"""
import sympy

t = sympy.symbols("t")
a2 = t * (t + 1) ** 2
a4 = t ** 3 * (t + 1) ** 2


def is_real_perfect_square(poly_expr):
    p = sympy.Poly(poly_expr, t)
    if p.is_zero:
        return False
    if p.degree() % 2 != 0:
        return False
    content, factors = sympy.factor_list(poly_expr)
    if content < 0:
        return False
    cr = sympy.Rational(content)
    num, den = cr.p, cr.q
    if sympy.sqrt(num) != int(sympy.sqrt(num)) or sympy.sqrt(den) != int(sympy.sqrt(den)):
        return False
    return all(mult % 2 == 0 for _, mult in factors)


def rhs_for(X):
    return sympy.expand(X ** 3 + a2 * X ** 2 + a4 * X)


if __name__ == "__main__":
    # degree-3 polynomial ansatz, A=-1 branch
    found = []
    for B in range(-6, 7):
        for C in range(-6, 7):
            for E in range(-6, 7):
                X = -t ** 3 + B * t ** 2 + C * t + E
                RHS = rhs_for(X)
                if RHS != 0 and is_real_perfect_square(RHS):
                    found.append((B, C, E))
    print("degree-3, A=-1, B,C,E in [-6,6]: found =", found)
