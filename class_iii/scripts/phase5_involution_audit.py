import sympy as sp
x0,x1,x2 = sp.symbols('x0 x1 x2')

def T(v):
    a,b,c = v
    return (c, -(a+b+c), a)

v = (x0,x1,x2)
Tv = T(v)
TTv = T(Tv)
TTv = tuple(sp.expand(e) for e in TTv)
print("T(x) =", Tv)
print("T(T(x)) =", TTv, " -- should equal (x0,x1,x2)")
print("Matches identity:", TTv == (x0,x1,x2))
