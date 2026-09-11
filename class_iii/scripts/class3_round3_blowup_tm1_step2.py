import sympy as sp

s, x1, y1, x3, y3 = sp.symbols('s x1 y1 x3 y3')

F1 = y1**2 + s*x1**2*(1-x1) - s**2*x1 + s**3*x1*(2-x1) - s**4*x1
F1 = sp.expand(F1)

# tangent cone check at x1=1 already done by hand; verify with sympy
F1_shift = F1.subs(x1, 1+x3)
F1_shift = sp.expand(F1_shift)
low = sp.series(F1_shift, x3, 0, 2).removeO()
low = sp.series(low, s, 0, 2).removeO()
print("Tangent cone at x1=1 (s,x3,y1 small):", sp.expand(low))

# second blow up at x1=0: x1 = s*x3, y1 = s*y3
F2t = F1.subs({x1: s*x3, y1: s*y3})
F2t = sp.expand(F2t)
poly = sp.Poly(F2t, s)
print("\nterms in s (x1=0 branch, second blowup):", poly.all_terms())
F2 = sp.expand(F2t / s**2)
print("F2:", F2)
print("F2 at s=0:", sp.expand(F2.subs(s,0)))

dF2_ds = sp.diff(F2, s)
sols = sp.solve(sp.Eq(dF2_ds.subs({s:0,y3:0}),0), x3)
print("singular x3 at s=0,y3=0:", sols)
