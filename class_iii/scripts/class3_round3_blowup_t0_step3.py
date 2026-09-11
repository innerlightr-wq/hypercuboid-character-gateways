import sympy as sp

x2, y1, T, x3, y3, x4, y4 = sp.symbols('x2 y1 T x3 y3 x4 y4')

F1_shift = -T**4*x2 + T**4 - T**3*x2**2 - T**3*x2 + 2*T**3 - 3*T**2*x2**2 + 3*T**2*x2 - T*x2**3 + T*x2**2 + y1**2
F1_shift = sp.expand(F1_shift)

# second blow up: x2 = T*x3, y1 = T*y3
F2_total = F1_shift.subs({x2:T*x3, y1:T*y3})
F2_total = sp.expand(F2_total)
print("Total transform:", F2_total)

# find the common power of T to divide by
poly = sp.Poly(F2_total, T)
print("terms by degree in T:", poly.all_terms())
F2 = sp.simplify(F2_total / T**2)
F2 = sp.expand(F2)
print("\nProper transform F2 (divided by T^2):", F2)
print("\nF2 at T=0:", sp.expand(F2.subs(T,0)))
