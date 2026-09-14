"""
Regression check for the manuscript remarks added in the September 2026
integration round: the Class III coordinate bridge (Remark rem:bridge,
class3_hypercuboid_k3.tex), the discriminant-factorization identity
(Remark rem:disc-factorization, both papers), the characteristic-3/every-
odd-prime fiber classification (Remark rem:char-p, both papers), and the
Class II quadratic-twist / field-specific Mordell-Weil rank results
(Remark rem:class2-twist and Appendix "Class II's own Weierstrass model",
hypercuboid_character_sums.tex).

This script is verification only -- no output here is a logically
necessary step in any proof in either manuscript; every claim it checks
is proved in the manuscript text (or its appendices) by an exact symbolic
or algebraic argument. Reproduces, in one place, the identities derived
across explorations/sector_signature_*_2026-09-14/.

Run: python3 scripts/verify_char3_fiber_and_rank.py
"""
import sympy as sp

T, X, Y, S, x, t, u, v = sp.symbols("T X Y S x t u v")


def a2a4(b):
    return sp.expand(T * (T + 1) * (T + b + 1)), sp.expand(T ** 2 * (T + 1) ** 2 * (T + b))


def invariants(a2, a4, a6=0):
    b2, b4, b6, b8 = 4 * a2, 2 * a4, 4 * a6, 4 * a2 * a6 - a4 ** 2
    c4 = sp.expand(b2 ** 2 - 24 * b4)
    c6 = sp.expand(-b2 ** 3 + 36 * b2 * b4 - 216 * b6)
    Delta = sp.expand(-b2 ** 2 * b8 - 8 * b4 ** 3 - 27 * b6 ** 2 + 9 * b2 * b4 * b6)
    return c4, c6, Delta


ok = True


def check(label, cond):
    global ok
    print(f"  [{'OK' if cond else 'FAIL'}] {label}")
    ok = ok and cond


print("=" * 70)
print("1. Class III coordinate bridge (Remark rem:bridge)")
print("=" * 70)
lemma_summand = x * t * (t + 1) * (x + t) * (x + t + 1)
affine_model = X * (X + 1) * T * (T + 1) * (X + T + 1)
Xsub, Tsub = -(t + 1), x + t
check("X(X+1)T(T+1)(X+T+1) with X=-(t+1),T=x+t equals x t(t+1)(x+t)(x+t+1)",
      sp.expand(affine_model.subs({X: Xsub, T: Tsub}) - lemma_summand) == 0)

print()
print("=" * 70)
print("2. Discriminant factorization identity (Remark rem:disc-factorization),")
print("   both b=0 (Classes I/II) and b=1 (Class III)")
print("=" * 70)
for b in (0, 1):
    a2, a4 = a2a4(b)
    c4, c6, Delta = invariants(a2, a4)
    disc_naive = sp.expand(((0 - (-1)) * (0 - (-(T + b))) * (-1 - (-(T + b)))) ** 2)
    predicted = sp.expand(16 * (T * (T + 1)) ** 6 * disc_naive)
    check(f"b={b}: Delta == 16*[T(T+1)]^6*disc_X{{0,-1,-(T+b)}}",
          sp.expand(Delta - predicted) == 0)

print()
print("=" * 70)
print("3. Characteristic-3 Step-6 check at the one potentially-good fiber")
print("   (Classes I/II, T=-1): P(Y)=Y^3-Y, disc=4, nonzero at every odd p")
print("=" * 70)
a2_0, a4_0 = a2a4(0)
# direct local computation as in the manuscript remark:
shifted_a2 = sp.expand(a2_0.subs(T, T - 1))
shifted_a4 = sp.expand(a4_0.subs(T, T - 1))
a2_prime = sp.Poly(shifted_a2, T).nth(1)   # coefficient of T^1 = a2/pi at pi=T
a4_prime = sp.Poly(shifted_a4, T).nth(2)   # coefficient of T^2 = a4/pi^2
P = sp.expand(Y ** 3 + a2_prime * Y ** 2 + a4_prime * Y)
check("P(Y) == Y^3 - Y", sp.expand(P - (Y ** 3 - Y)) == 0)
disc_P = sp.Poly(P, Y).discriminant()
check("disc(P) == 4", disc_P == 4)
check("4 nonzero mod 3 (and every odd prime)", 4 % 3 != 0)

print()
print("=" * 70)
print("4. Class II's own model: the exact -1-twist law (Remark rem:class2-twist,")
print("   Appendix app:class2)")
print("=" * 70)
a2_II = sp.expand(2 * v * (v + 1) ** 2)
a4_II = sp.expand(v ** 2 * (v + 1) ** 2 * (v ** 2 + 3 * v + 1))
a6_II = sp.expand(v ** 4 * (v + 1) ** 4)
c4_II, c6_II, D_II = invariants(a2_II, a4_II, a6_II)
a2_I = sp.expand(v * (v + 1) ** 2)
a4_I = sp.expand(v ** 3 * (v + 1) ** 2)
c4_I, c6_I, D_I = invariants(a2_I, a4_I, 0)
check("c4_II == c4_I", sp.simplify(c4_II - c4_I) == 0)
check("c6_II == -c6_I", sp.simplify(c6_II + c6_I) == 0)
check("Delta_II == Delta_I", sp.simplify(D_II - D_I) == 0)

print()
print("=" * 70)
print("5. The explicit translation, and the transported point")
print("=" * 70)
Xnew = sp.Symbol("Xnew")
cubic_II = X ** 3 + a2_II * X ** 2 + a4_II * X + a6_II
translated = sp.expand(cubic_II.subs(X, Xnew - v * (v + 1) ** 2))
poly_t = sp.Poly(translated, Xnew)
check("translation by -v(v+1)^2 gives (a2,a4,a6)=(-a2_I,a4_I,0)",
      poly_t.coeff_monomial(Xnew ** 2) == -a2_I and
      poly_t.coeff_monomial(Xnew) == a4_I and
      poly_t.coeff_monomial(sp.Integer(1)) == 0)

Q_II = v * (u + 1) * (u + v) * (v + 1) * (u + v + 1)
u_native = sp.together(-(T ** 2 + T - 1) / T).subs(v, T)
Y_native = sp.together(-(T - 1) * (T + 1) / T)
lhs = sp.expand(Y_native ** 2)
rhs = sp.expand(Q_II.subs({u: u_native, v: T}))
check("transported point lies on Class II's own original quintic",
      sp.simplify(lhs - rhs) == 0)
check("transported point coordinates involve no I (genuinely Q(t)-rational)",
      not u_native.has(sp.I) and not Y_native.has(sp.I))

print()
print("=" * 70)
print("6. sigma(P_1) = -P_1 (group-law statement, Appendix app:height)")
print("=" * 70)
X1 = -(t + 1)
Y1 = sp.I * (t - 1) * (t + 1) ** 2
sigma_Y1 = Y1.subs(sp.I, -sp.I)
check("sigma(Y(P1)) == -Y(P1)", sp.expand(sigma_Y1 - (-Y1)) == 0)
check("sigma(X(P1)) == X(P1)", sp.expand(X1.subs(sp.I, -sp.I) - X1) == 0)

print()
print("=" * 70)
print(f"ALL CHECKS PASSED: {ok}")
print("=" * 70)
if not ok:
    raise SystemExit(1)
