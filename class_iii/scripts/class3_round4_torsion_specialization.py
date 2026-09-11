import sympy as sp

T, S = sp.symbols('T S')

# ---- T=0 fiber ----
# P1: X=0 always -> x1 = X/T = 0
# P2: X=-T(T+1) -> x1 = -(T+1)
# P3: X=-T(T+1)^2 -> x1 = -(T+1)^2
x1_P2 = -(T+1)
x1_P3 = -(T+1)**2
print("T=0 fiber:")
print("  x1(P1) = 0 identically")
print("  x1(P2) at T=0:", x1_P2.subs(T,0), "  (matches simple root branch? expect -1)")
print("  x1(P3) at T=0:", x1_P3.subs(T,0), "  (expect -1, same double branch as P2)")

# second blow-up: x2 = x1+1, x3 = x2/T
x2_P2 = sp.expand(x1_P2 + 1)
x2_P3 = sp.expand(x1_P3 + 1)
x3_P2 = sp.simplify(x2_P2 / T)
x3_P3 = sp.simplify(x2_P3 / T)
print("  x2(P2) =", x2_P2, " -> x3(P2) =", x3_P2)
print("  x2(P3) =", x2_P3, " -> x3(P3) =", x3_P3, " at T=0:", x3_P3.subs(T,0))
print()

# ---- T=-1 fiber, local param s=T+1 ----
s = sp.Symbol('s')
Tval = -1+s
X_P1 = 0
X_P2 = -Tval*(Tval+1)
X_P3 = -Tval*(Tval+1)**2
x1_P1s = sp.simplify(X_P1/s)
x1_P2s = sp.simplify(sp.expand(X_P2)/s)
x1_P3s = sp.simplify(sp.expand(X_P3)/s)
print("T=-1 fiber (s=T+1):")
print("  x1(P1) =", x1_P1s)
print("  x1(P2) =", x1_P2s, " at s=0:", sp.limit(x1_P2s, s, 0))
print("  x1(P3) =", sp.expand(X_P3)/s, " simplified:", x1_P3s, " at s=0:", sp.limit(x1_P3s,s,0))

x3_P1s = sp.limit(x1_P1s/s, s, 0) if x1_P1s !=0 else 0
x3_P3s_expr = sp.simplify(x1_P3s/s)
print("  x3(P1) [since x1(P1)=0 identically] = 0")
print("  x3(P3) = x1(P3)/s =", sp.simplify(x1_P3s/s), " at s=0:", sp.limit(sp.simplify(x1_P3s/s), s, 0))
print()

# ---- T=infinity, S=1/T, Xtilde = S^4 * X ----
X_P1inf = 0
X_P2inf = sp.simplify(S**4 * (-(1/S)*(1/S+1)))
X_P3inf = sp.simplify(S**4 * (-(1/S)*(1/S+1)**2))
print("T=infinity fiber (S=1/T, Xtilde=S^4 X):")
print("  Xtilde(P2) =", sp.simplify(X_P2inf))
print("  Xtilde(P3) =", sp.simplify(X_P3inf))
x1_P2inf = sp.simplify(X_P2inf / S)
x1_P3inf = sp.simplify(X_P3inf / S)
print("  x1(P2) = Xtilde(P2)/S =", x1_P2inf, " at S=0:", sp.limit(x1_P2inf, S, 0))
print("  x1(P3) = Xtilde(P3)/S =", x1_P3inf, " at S=0:", sp.limit(x1_P3inf, S, 0))
