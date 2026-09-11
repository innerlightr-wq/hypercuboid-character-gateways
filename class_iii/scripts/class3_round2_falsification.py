"""
Round 2, Part XI: falsification battery for T(p) = a_p(16.3.c.a) (untwisted).

Five independent falsification directions, at least one via an independent
code path (direction 3 recomputes T(p) via the raw 3-variable Sigma_III sum
divided by (p-1), NOT via the 2-variable reduction used elsewhere).

1. Wrong newform in the same level/weight orbit: 16.3.f.a (the OTHER newform
   found at level 16, weight 3 in Round 1's search) must NOT match.
2. Wrong AOP surface: A(8,p) and A(1/8,p) (Round-1-killed hypotheses) must
   NOT match T(p) -- re-confirmed here as a regression check.
3. Independent code path: T(p) recomputed as Sigma_III(p)/(p-1) via the raw
   3-variable six-factor sum, cross-checked against the 2-variable T(p).
4. Wrong twist (chi(-1)-twist): F_{-1}(p) = chi(-1)(p) * a_p(f16) must equal
   F_0(p) = a_p(f16) at every p = 1 mod 4 tested (degeneracy, not a real
   distinct hypothesis at these primes) -- included to confirm the collapse
   claim itself is not silently hiding a live alternative.
5. Vanishing sanity check: T(p) = 0 at every tested p = 3 mod 4 (Round 1's
   elementary involution argument), independently reconfirmed here as a
   boundary/regression check on the same code used for the p = 1 mod 4 claims.
"""
import json


def chi(a, p):
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def T_of(p):
    total = 0
    for x in range(p):
        for t in range(p):
            val = (x * t * (t + 1) * (x + t) * (x + t + 1)) % p
            total += chi(val, p)
    return total


def Sigma_III_raw(p):
    total = 0
    for x0 in range(p):
        for x1 in range(p):
            for x2 in range(p):
                val = (x0 * x1 * x2 * (x0 + x2) * (x1 + x2) * (x0 + x1 + x2)) % p
                total += chi(val, p)
    return total


def A_of(lam, p):
    """AOP's A(lambda,p) = chi(lambda+1) * (a(lambda,p)^2 - p), reduced form
    reused from Round 1's class3_aop_compare.py logic (recomputed here for
    an independent regression check, not imported)."""
    lam = lam % p
    total = 0
    for x in range(p):
        for y in range(p):
            val = (x * y * (x + 1) * (y + 1) * (x + lam * y)) % p
            total += chi(val, p)
    return total


data = json.load(open("/tmp/level16_weight3.json"))
traces_c = next(r["traces"] for r in data["data"] if r["label"] == "16.3.c.a")
traces_f = next(r["traces"] for r in data["data"] if r["label"] == "16.3.f.a")

primes_1mod4 = [5, 13, 17, 29, 37, 41]
primes_3mod4 = [3, 7, 11, 19, 23, 31]

print("=== Direction 1: wrong newform 16.3.f.a must NOT match ===")
d1_pass = True
for p in primes_1mod4:
    Tp = T_of(p)
    af = traces_f[p - 1]
    mismatch = (Tp != af)
    d1_pass = d1_pass and mismatch
    print(f"  p={p:3d}  T(p)={Tp:5d}  a_p(16.3.f.a)={af:5d}  correctly mismatched={mismatch}")
print(f"Direction 1 result: 16.3.f.a correctly REFUTED at all tested p: {d1_pass}")
print()

print("=== Direction 2: AOP's own killed hypotheses A(8,p), A(1/8,p) re-confirmed dead ===")
d2_pass = True
for p in primes_1mod4:
    Tp = T_of(p)
    a8 = A_of(8, p)
    inv8 = pow(8, -1, p)
    a18 = A_of(inv8, p)
    mismatch8 = (Tp != a8)
    mismatch18 = (Tp != a18)
    d2_pass = d2_pass and mismatch8 and mismatch18
    print(f"  p={p:3d}  T(p)={Tp:5d}  A(8,p)={a8:5d}  A(1/8,p)={a18:5d}  both correctly mismatched={mismatch8 and mismatch18}")
print(f"Direction 2 result: AOP lambda=8, lambda=1/8 surfaces correctly stay REFUTED: {d2_pass}")
print()

print("=== Direction 3: independent code path, Sigma_III(p)/(p-1) vs T(p) ===")
d3_pass = True
for p in primes_1mod4:
    Tp = T_of(p)
    Sig = Sigma_III_raw(p)
    Sig_over = Sig // (p - 1)
    consistent = (Sig % (p - 1) == 0) and (Sig_over == Tp)
    d3_pass = d3_pass and consistent
    print(f"  p={p:3d}  T(p)={Tp:5d}  Sigma_III(p)={Sig:6d}  Sigma_III/(p-1)={Sig_over:5d}  consistent={consistent}")
print(f"Direction 3 result: independent 3-variable code path agrees with T(p) at all tested p: {d3_pass}")
print()

print("=== Direction 4: chi(-1)-twist degeneracy collapse confirmed (not a live alternative) ===")
d4_pass = True
for p in primes_1mod4:
    a = traces_c[p - 1]
    Fm1 = chi(-1, p) * a
    F0 = a
    collapsed = (Fm1 == F0)
    d4_pass = d4_pass and collapsed
    print(f"  p={p:3d}  chi(-1)(p)={chi(-1,p):2d}  F0={F0:5d}  F_{{-1}}={Fm1:5d}  collapsed={collapsed}")
print(f"Direction 4 result: chi(-1)-twist collapses to F0 at all tested p=1 mod 4 (as expected): {d4_pass}")
print()

print("=== Direction 5: p=3 mod 4 vanishing sanity re-check (Round 1 result, regression test) ===")
d5_pass = True
for p in primes_3mod4:
    Tp = T_of(p)
    vanishes = (Tp == 0)
    d5_pass = d5_pass and vanishes
    print(f"  p={p:3d}  T(p)={Tp:5d}  vanishes={vanishes}")
print(f"Direction 5 result: T(p)=0 at all tested p=3 mod 4: {d5_pass}")
print()

overall = d1_pass and d2_pass and d3_pass and d4_pass and d5_pass
print(f"ALL FIVE FALSIFICATION DIRECTIONS PASS (i.e. nothing refuted the T(p)=a_p(16.3.c.a) claim,")
print(f"and all intended-to-fail alternatives correctly failed): {overall}")
