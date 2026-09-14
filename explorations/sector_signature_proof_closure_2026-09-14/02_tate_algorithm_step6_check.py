"""
Target 1, continued: the j=1728 concern at T=-1 (Classes I/II, the ONE
potentially-good additive point) genuinely needs Tate's algorithm's actual
Step 6 (not the j-invariant shortcut, which is normally stated only for
p>3) -- run it explicitly, over Q and mod 3, at every additive point, for
both sectors, including infinity.

Setup (a1=a3=a6=0 throughout this family): y^2=x^3+a2x^2+a4x. At every
additive point checked, a2 and a4 BOTH vanish there already (verified
below), so the origin is already the singular point -- no translation
needed (Tate Step 2 trivial). Since a6=0 identically:
  b8 = -a4^2  (so pi^3 | b8  <=>  2*v(a4) >= 3  <=>  v(a4) >= 2)
  b6 = 0      (so pi^3 | b6 always -- Step 5's "type IV" branch never fires)
Hence Steps 3-5 reduce, for this family, to checking v(a4)>=2 (else type
III at that point -- checked, never happens at our bad points) and then
proceeding to Step 6: form
    P(Y) = Y^3 + a2' Y^2 + a4' Y + a6',   a2'=a2/pi, a4'=a4/pi^2, a6'=a6/pi^3=0
(pi = the local uniformizer -- (T-t0) for a finite point t0, or S=1/T at
infinity) and test whether P(Y) has DISTINCT roots (over the ALGEBRAIC
CLOSURE of the residue field): distinct -> type I_0^*, STOP (no further
step needed); repeated root -> continue Tate's algorithm further (not
needed below, since every case tested terminates with distinct roots or is
already covered by the potentially-multiplicative argument of script 01).
"""
import sympy as sp

T, Y, S = sp.symbols("T Y S")


def a2a4(b):
    return sp.expand(T * (T + 1) * (T + b + 1)), sp.expand(T ** 2 * (T + 1) ** 2 * (T + b))


def local_series(poly, point, var, order=6):
    """Return the coefficients of poly, expanded in the local parameter
    (var-point), up to `order` -- as a plain list [c0,c1,c2,...]."""
    shifted = sp.expand(poly.subs(var, var + point))
    p = sp.Poly(shifted, var)
    return [p.nth(k) for k in range(order)]


def step6_test(a2, a4, point, var, p=None, label=""):
    a2c = local_series(a2, point, var)
    a4c = local_series(a4, point, var)
    v_a2 = next(i for i, c in enumerate(a2c) if (c % p if p else c) != 0)
    v_a4 = next(i for i, c in enumerate(a4c) if (c % p if p else c) != 0)
    print(f"  {label}: v(a2)={v_a2}, v(a4)={v_a4}  "
          f"(need v(a2)>=1 [additive, origin already singular: {v_a2 >= 1}], "
          f"v(a4)>=2 [else type III -- not our case: {v_a4 >= 2}])")
    if v_a2 < 1 or v_a4 < 2:
        print("    -> does not fit this family's Step-6 shortcut; skip (handled elsewhere)")
        return
    a2p = a2c[1] if v_a2 == 1 else 0  # a2' = a2/pi ; if v(a2)>1, a2'=0 mod pi
    a4p = a4c[2]                       # a4' = a4/pi^2
    if p is not None:
        a2p %= p
        a4p %= p
    Ppoly = sp.Poly(Y ** 3 + a2p * Y ** 2 + a4p * Y, Y,
                     domain=sp.GF(p) if p is not None else sp.QQ)
    disc = Ppoly.discriminant()
    print(f"    P(Y) = Y^3 + ({a2p})Y^2 + ({a4p})Y  (a6'=0)")
    print(f"    disc(P) = {disc}  -> {'DISTINCT roots: type I_0^*, Step 6 terminates' if disc != 0 else 'REPEATED root: needs further Tate steps (not this shortcut)'}")


print("=" * 78)
print("The potentially-GOOD point: T=-1, Classes I/II (b=0)")
print("=" * 78)
a2_0, a4_0 = a2a4(0)
for p, name in [(None, "Q"), (3, "mod 3")]:
    step6_test(a2_0, a4_0, -1, T, p, label=f"T=-1 over {name}")

print()
print("=" * 78)
print("Cross-check: the potentially-MULTIPLICATIVE points should give a")
print("REPEATED root at Step 6 (confirming they are NOT I_0^*, consistent")
print("with n>0 found via the j-invariant route in script 01)")
print("=" * 78)
for b, name, pts in [(0, "I/II", [0]), (1, "III", [0, -1])]:
    a2, a4 = a2a4(b)
    for pt in pts:
        for p, pname in [(None, "Q"), (3, "mod 3")]:
            step6_test(a2, a4, pt, T, p, label=f"{name} T={pt} over {pname}")

print()
print("=" * 78)
print("Infinity, both sectors (S=1/T chart, weight-matched a2,a4)")
print("=" * 78)
for b, name in [(0, "I/II"), (1, "III")]:
    a2, a4 = a2a4(b)
    a2_inf = sp.simplify(sp.expand(S ** 4 * a2.subs(T, 1 / S)))
    a4_inf = sp.simplify(sp.expand(S ** 8 * a4.subs(T, 1 / S)))
    for p, pname in [(None, "Q"), (3, "mod 3")]:
        step6_test(a2_inf, a4_inf, 0, S, p, label=f"{name} T=inf (S=0) over {pname}")
