import sympy as sp

X, Y, T, s, x1, y1, x2, y2, x3, y3 = sp.symbols('X Y T s x1 y1 x2 y2 x3 y3')

u = T+1
F = Y**2 - X*(X+T*u)*(X+T*u**2)
F = sp.expand(F)

# Substitute T = -1+s (local param at T=-1)
Fs = F.subs(T, -1+s)
Fs = sp.expand(Fs)
print("F at T=-1+s:", Fs)
print("F at s=0:", Fs.subs(s,0))

# First blow up: X = s*x1, Y=s*y1
F1t = Fs.subs({X:s*x1, Y:s*y1})
F1t = sp.expand(F1t)
poly = sp.Poly(F1t, s)
print("\nterms by degree in s:", poly.all_terms())
F1 = sp.expand(F1t/s**2)
print("\nF1 (proper transform):", F1)
print("F1 at s=0:", sp.expand(F1.subs(s,0)))

dF1_ds = sp.diff(F1,s)
sols = sp.solve(sp.Eq(dF1_ds.subs({s:0,y1:0}),0), x1)
print("\nsingular x1 at s=0,y1=0:", sols)
