import sympy as sp

x2, y1, T, x3, y3, t2, x2p, y1p = sp.symbols('x2 y1 T x3 y3 t2 x2p y1p')

F1_shift = -T**4*x2 + T**4 - T**3*x2**2 - T**3*x2 + 2*T**3 - 3*T**2*x2**2 + 3*T**2*x2 - T*x2**3 + T*x2**2 + y1**2
F1_shift = sp.expand(F1_shift)

# x2-dominant chart: T = x2 * t2, y1 = x2 * y1p
Fx2_total = F1_shift.subs({T: x2*t2, y1: x2*y1p})
Fx2_total = sp.expand(Fx2_total)
poly = sp.Poly(Fx2_total, x2)
print("x2-dominant chart, terms by degree in x2:", poly.all_terms())

# check at t2=0 (this would be the strict transform of {T=0} in this chart)
Fx2 = sp.expand(Fx2_total / x2**2)
print("\nProper transform Fx2:", Fx2)
print("Fx2 at t2=0:", sp.expand(Fx2.subs(t2,0)))
print("Fx2 at x2=0:", sp.expand(Fx2.subs(x2,0)))

# check smoothness at (x2,t2,y1p)=(0,0,0)
for v in (x2,t2,y1p):
    print("dFx2/d%s at origin:"%v, sp.diff(Fx2,v).subs({x2:0,t2:0,y1p:0}))
