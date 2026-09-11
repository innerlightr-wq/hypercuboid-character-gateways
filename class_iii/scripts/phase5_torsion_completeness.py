import sympy as sp
T = sp.symbols('T')

# cubic X^3+a2 X^2+a4 X, a2=T(T+1)(T+2), a4=T^2(T+1)^3
a2 = T*(T+1)*(T+2)
a4 = T**2*(T+1)**3
X = sp.symbols('X')
cubic = X**3 + a2*X**2 + a4*X
factored = X*(X+T*(T+1))*(X+T*(T+1)**2)
print("cubic - factored =", sp.expand(cubic-factored), "(should be 0)")

# roots
r0, r1, r2 = sp.Integer(0), -T*(T+1), -T*(T+1)**2
# pairwise differences, as polynomials in T -- must be NONZERO polynomials
# (i.e. roots coincide only at finitely many T, not identically)
d01 = sp.factor(r0-r1)
d02 = sp.factor(r0-r2)
d12 = sp.factor(r1-r2)
print("r0-r1 =", d01)
print("r0-r2 =", d02)
print("r1-r2 =", d12)
print("All three nonzero as polynomials in T (i.e. roots generically distinct):",
      d01 != 0 and d02 != 0 and d12 != 0)

# where do roots collide? (bad fibers)
print("r0-r1=0 at T=", sp.solve(d01, T))
print("r0-r2=0 at T=", sp.solve(d02, T))
print("r1-r2=0 at T=", sp.solve(d12, T))
