import sympy as sp
T, x1, y1, x4, y4 = sp.symbols('T x1 y1 x4 y4')

# F1 from Round 3 (proper transform after first blow-up at T=0 fiber)
F1 = y1**2 - (T*x1*(1+x1)**2 + 3*T**2*x1*(1+x1) + T**3*x1*(3+x1) + T**4*x1)
F1 = sp.expand(F1)

# resolve the ordinary node at (x1,T,y1)=(0,0,0): blow up x1=T*x4, y1=T*y4
F_blown = F1.subs({x1: T*x4, y1: T*y4})
F_blown = sp.expand(F_blown)
poly = sp.Poly(F_blown, T)
print("total transform terms by degree in T:", poly.all_terms())

# multiplicity of the point was 2 (tangent cone rank-3 nondegenerate), divide by T^2
F_E1 = sp.expand(F_blown / T**2)
print("\nproper transform E1 (leg) equation:", F_E1)
print("E1 restricted to T=0 (the fiber divisor's local equation transverse to E1):")
at_T0 = sp.expand(F_E1.subs(T,0))
print(" ", at_T0)
print("\nIs this REDUCED (multiplicity 1, i.e. NOT of the form (poly)^2)?")
# check: does at_T0 factor as a perfect square?
factored = sp.factor(at_T0)
print("factored form:", factored)
print("--> a linear relation y4^2=x4 (or similar), degree 1 in each variable separately,")
print("    is NOT a perfect square -- confirms T vanishes to order exactly 1 transverse")
print("    to E1, i.e. E1 has fiber-multiplicity 1 (a genuine LEG, not a spine node).")
