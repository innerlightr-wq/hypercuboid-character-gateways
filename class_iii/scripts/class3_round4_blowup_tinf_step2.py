import sympy as sp

S, x1, y1, x3, y3 = sp.symbols('S x1 y1 x3 y3')

# from earlier: F1 (proper transform at T=infinity, after first blowup) at x1=0 branch
# F1 = -S^3 x1^2 - S^3 x1 - S^2 x1^3 -3S^2x1^2 -Sx1^2+S^2 -... let's recompute cleanly
Xt, Yt = sp.symbols('Xt Yt')
a2t = S*(S+1)*(2*S+1)
a4t = S**3*(S+1)**3
F = Yt**2 - (Xt**3 + a2t*Xt**2 + a4t*Xt)
F = sp.expand(F)
F1t = F.subs({Xt:S*x1, Yt:S*y1})
F1t = sp.expand(F1t)
F1 = sp.expand(F1t / S**2)
print("F1 =", F1)
print("F1 at S=0:", sp.expand(F1.subs(S,0)))

# second blow up at x1=0 branch: x1 = S*x3, y1=S*y3
F2t = F1.subs({x1: S*x3, y1: S*y3})
F2t = sp.expand(F2t)
poly = sp.Poly(F2t, S)
print("\nterms by degree in S (x1=0 branch):", poly.all_terms())
F2 = sp.expand(F2t / S**2)
print("F2 =", F2)
print("F2 at S=0:", sp.expand(F2.subs(S,0)))

# find tangent cones at x3=0 and x3=-1
for pt in [0, -1]:
    shifted = F2.subs(x3, pt + sp.Symbol('x4'))
    shifted = sp.expand(shifted)
    low = sp.series(shifted, sp.Symbol('x4'), 0, 2).removeO()
    low = sp.series(low, S, 0, 2).removeO()
    print(f"tangent cone near x3={pt}:", sp.expand(low))
