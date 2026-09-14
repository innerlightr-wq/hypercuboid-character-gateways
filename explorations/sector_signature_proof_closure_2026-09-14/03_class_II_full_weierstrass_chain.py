"""
Target 3: complete the coordinate chain from Class II's OWN reduced
quintic through to ITS OWN minimal Weierstrass model, and determine
exactly how (or whether) that model identifies with the abstract -1-twist
X^(-1) of Class I's own model -- not merely at the level of an affine
polynomial correspondence, but as an isomorphism of elliptic FIBRATIONS
(matching base parameter, matching which coordinate is "the" fiber
coordinate, tracking any constant/square/denominator).

Source: Class II's quintic (dehomogenizing P_II via x1=1, as in the prior
"validation" round's equivalence_and_falsification_check.py, reused here):
    Q_II(u,v) = v(u+1)(u+v)(v+1)(u+v+1)
already known (prior round) to satisfy, EXACTLY:
    Q_II(u,v) = -Q_I(x,T),   u = -(x+T+1), v = T
where Q_I(x,T) = x(x+1)T(T+1)(x+T) is Class I's own quintic.
"""
import sympy as sp

u, v, x, T, Xs, Y = sp.symbols("u v x T X Y")

Q_II = v * (u + 1) * (u + v) * (v + 1) * (u + v + 1)
Q_I = x * (x + 1) * T * (T + 1) * (x + T)

print("=" * 78)
print("1. Re-confirm the affine bridge (already established, reused not redone)")
print("=" * 78)
usub, vsub = -(x + T + 1), T
check = sp.expand(Q_II.subs({u: usub, v: vsub}) + Q_I)
print(f"  Q_II(u,v) with u=-(x+T+1),v=T, plus Q_I(x,T): {check}  (0 = confirmed)")

print()
print("=" * 78)
print("2. Class II's OWN prefactor/cubic decomposition (in its own u,v)")
print("=" * 78)
Q_II_fac = sp.factor(Q_II)
print(f"  Q_II(u,v) = {Q_II_fac}")
print("""  Grouping: {v,v+1} is the pure-v pair (prefactor v(v+1), SAME shape as
  every other sector); {u+1,u+v,u+v+1} is the u-cubic -- roots -1,-v,-(v+1)
  -- notably NOT {0,-1,-v} or {0,-1,-(v+1)} like Classes I/II/III's own
  cubics: there is no bare "u" factor. This is a genuinely different root
  PATTERN in Class II's own natural variable u.
""")

print("=" * 78)
print("3. Complete the cube in u (same procedure as both other sectors,")
print("   verified monic before extracting a2,a4 -- not assumed)")
print("=" * 78)
prefactor = v * (v + 1)
up, Yp = sp.symbols("up Yp")
rhs_frac = prefactor * ((u + 1) * (u + v) * (u + v + 1)).subs(u, up / prefactor)
lhs_frac = (Yp / prefactor) ** 2
rhs_cleared = sp.expand(sp.together(rhs_frac) * prefactor ** 2)
lhs_cleared = sp.expand(sp.together(lhs_frac) * prefactor ** 2)
poly = sp.Poly(rhs_cleared, up)
leading = poly.coeff_monomial(up ** 3)
print(f"  leading (up^3) coefficient: {leading}  (monic check: {leading == 1})")
a2_II = poly.coeff_monomial(up ** 2)
a4_II = poly.coeff_monomial(up)
a6_II = poly.coeff_monomial(sp.Integer(1))
print(f"  Class II's own minimal model:")
print(f"    a2_II(T) = {sp.factor(a2_II)}")
print(f"    a4_II(T) = {sp.factor(a4_II)}")
print(f"    a6_II(T) = {sp.factor(a6_II)}   (should be 0 for a genuine")
print(f"    a1=a3=a6=0 short Weierstrass form -- IS it? {a6_II == 0})")
