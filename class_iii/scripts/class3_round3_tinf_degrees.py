import sympy as sp

T, S, X, Y, x, y = sp.symbols('T S X Y x y')
a2 = T*(T+1)*(T+2)
a4 = T**2*(T+1)**3

# T = 1/S, X = x/S^2, Y = y/S^3  (standard weight (2,3) scaling to move infinity to S=0)
a2S = sp.expand(a2.subs(T, 1/S) * S**2)   # a2(1/S) has pole order 1 in S (deg3 num), scale
a4S = sp.expand(a4.subs(T,1/S) * S**4)
print("a2 in terms of S (should be poly, deg 3 leading at S=0):", sp.simplify(a2.subs(T,1/S)))
print("a2 * S^3 =", sp.simplify(sp.expand(a2.subs(T,1/S)*S**3)))
print("a4 * S^5 =", sp.simplify(sp.expand(a4.subs(T,1/S)*S**5)))

# c4,c6,Delta valuations at infinity via degree count
c4 = sp.factor(16*(a2**2-3*a4))
c6 = sp.factor(-64*a2**3+288*a2*a4)
Delta = sp.factor(16*T**8*(T+1)**8)
print("\ndeg c4 =", sp.degree(sp.expand(16*(a2**2-3*a4)), T))
print("deg c6 =", sp.degree(sp.expand(-64*a2**3+288*a2*a4), T))
print("deg Delta =", sp.degree(sp.expand(Delta), T))
