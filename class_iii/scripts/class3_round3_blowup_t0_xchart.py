import sympy as sp

X, Y, T, t1, y1p, x1p, tp = sp.symbols('X Y T t1 y1p x1p tp')

u = T+1
F = Y**2 - X*(X+T*u)*(X+T*u**2)
F = sp.expand(F)

# X-dominant chart: T = X*t1, Y = X*y1p
FX_total = F.subs({T: X*t1, Y: X*y1p})
FX_total = sp.expand(FX_total)
print("X-chart total transform:", FX_total)
polyX = sp.Poly(FX_total, X)
print("terms by degree in X:", polyX.all_terms())
