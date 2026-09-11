import sympy as sp

S, Xt, Yt, x1, y1, x2, y2, x3, y3 = sp.symbols('S Xt Yt x1 y1 x2 y2 x3 y3')

a2t = S*(S+1)*(2*S+1)
a4t = S**3*(S+1)**3

F = Yt**2 - Xt*(Xt+a2t)*(Xt) - a2t*0  # placeholder, build properly below
F = Yt**2 - (Xt**3 + a2t*Xt**2 + a4t*Xt)
F = sp.expand(F)

print("F(Xt,Yt,S) near S=0:", F)
print("singular at (0,0,0)?", [sp.diff(F,v).subs({Xt:0,Yt:0,S:0}) for v in (Xt,Yt,S)])

# multiplicity: check leading terms
print("F at S=0:", F.subs(S,0))

# blow up: Xt = S*x1, Yt = S*y1
F1t = F.subs({Xt:S*x1, Yt:S*y1})
F1t = sp.expand(F1t)
poly = sp.Poly(F1t, S)
print("\nterms by degree in S:", poly.all_terms())
