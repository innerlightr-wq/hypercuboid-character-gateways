import sympy as sp

X, Y, T, x1, y1, x2, y2, x3, y3 = sp.symbols('X Y T x1 y1 x2 y2 x3 y3')

# F = Y^2 - X(X+Tu)(X+Tu^2), u = T+1
u = T+1
F = Y**2 - X*(X+T*u)*(X+T*u**2)
F = sp.expand(F)
print("F =", F)

# Check singular point at (0,0,0)
print("F at origin:", F.subs({X:0,Y:0,T:0}))
for v in (X,Y,T):
    print("dF/d%s at origin ="%v, sp.diff(F,v).subs({X:0,Y:0,T:0}))

# Blow up: X = T*x1, Y = T*y1 (chart where T is "small parameter")
F1_total = F.subs({X:T*x1, Y:T*y1})
F1_total = sp.expand(F1_total)
print("\nTotal transform (chart X=T x1, Y=T y1):")
print(F1_total)
# factor out T^2
F1 = sp.simplify(F1_total / T**2)
F1 = sp.expand(F1)
print("\nProper transform F1 = total/T^2:")
print(F1)

print("\nF1 at T=0:", sp.expand(F1.subs(T,0)))
