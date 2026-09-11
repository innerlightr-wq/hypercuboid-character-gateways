import sympy as sp

x1, y1, T, x2, y2 = sp.symbols('x1 y1 T x2 y2')

F1 = y1**2 - (T*x1*(1+x1)**2 + 3*T**2*x1*(1+x1) + T**3*x1*(3+x1) + T**4*x1)
F1 = sp.expand(F1)

# find singular points along T=0, y1=0
dF1_dx1 = sp.diff(F1, x1)
dF1_dT = sp.diff(F1, T)
dF1_dy1 = sp.diff(F1, y1)

sing_x1 = sp.solve(sp.Eq(dF1_dT.subs({T:0,y1:0}), 0), x1)
print("Singular x1 values on {T=0,y1=0} (where dF1/dT vanishes too):", sing_x1)
print("dF1/dx1 at T=0,y1=0:", dF1_dx1.subs({T:0,y1:0}))  # should be 0 automatically (factor T)

# tangent cone at (x1,T,y1)=(0,0,0)
print("\n--- Tangent cone at x1=0 ---")
taylor = sp.series(F1, x1, 0, 3).removeO()
taylor = sp.series(taylor, T, 0, 3).removeO()
print("F1 truncated near x1=0,T=0:", sp.expand(taylor))

print("\n--- Tangent cone at x1=-1 ---")
F1_shift = F1.subs(x1, -1+x2)
F1_shift = sp.expand(F1_shift)
print("F1 shifted (x1=-1+x2):", F1_shift)
taylor2 = sp.series(F1_shift, x2, 0, 4).removeO()
taylor2 = sp.expand(taylor2)
print("expanded in x2:", taylor2)
taylor2b = sp.series(taylor2, T, 0, 4).removeO()
print("further truncated in T:", sp.expand(taylor2b))
