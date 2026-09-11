import sympy as sp

X, T, Y, t, x1, y1, x2, y2 = sp.symbols('X T Y t x1 y1 x2 y2')

a2 = T*(T+1)*(T+2)
a4 = T**2*(T+1)**3

cubic = X**3 + a2*X**2 + a4*X
factored = X*(X+T*(T+1))*(X+T*(T+1)**2)
print("Cubic - claimed factorization simplifies to 0:", sp.expand(cubic - factored) == 0)

# discriminant check D2 = a2^2-4a4
D2 = sp.expand(a2**2 - 4*a4)
print("D2 =", sp.factor(D2))

c4 = sp.expand(16*(a2**2-3*a4))
c6 = sp.expand(-64*a2**3+288*a2*a4)
Delta = sp.expand((c4**3-c6**2)/1728)
print("c4 =", sp.factor(c4))
print("c6 =", sp.factor(c6))
print("Delta =", sp.factor(Delta))

# valuations at T=0
for expr,name in [(c4,'c4'),(c6,'c6'),(Delta,'Delta')]:
    p = sp.Poly(expr, T)
    # lowest degree term
    terms = sp.expand(expr).as_ordered_terms()
    print(name, "series at T=0:", sp.series(expr, T, 0, 6))
