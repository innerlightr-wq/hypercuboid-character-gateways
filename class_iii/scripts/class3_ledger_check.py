"""
Round 2, Part VII: independent verification of the corrected point-count ledger.

V_III : Y^2 = X(X+1) T(T+1) (X+T+1)      (affine Weierstrass model over the t-line)
X_III : minimal desingularization, elliptic surface over P^1_t with fiber
        E_t : y^2 = x(x+1) t(t+1) (x+t+1)   (t fixed)

Bad fibers of X_III: I2* at t=0, I2* at t=-1, I2* at t=infinity (3 total, only
2 finite). This differs from the main manuscript's 4-bad-fiber Classes I/II
surface, and is the source of the Round-2 self-correction: the number of
GOOD FINITE fibers is p-2 (not p-3).

Ledger claim (derived from scratch this round):
    #X_III(F_p) = #V_III(F_p) + 20p + 1

Derivation sketch being checked:
  - At each of the (p-2) good finite fibers t, the smooth affine curve
    y^2 = x(x+1)t(t+1)(x+t+1) has (p - a_t) points in the x-line's affine
    part in the sense of the standard elliptic-curve point count, but the
    bookkeeping constant that makes #X_III(F_p) = #V_III(F_p) + (correction)
    an IDENTITY (not an approximation) comes from comparing the surface's
    total point count (via desingularization: each I2* fiber contributes a
    fixed number of F_p points from its exceptional configuration) against
    the raw affine sum V_III(F_p) = sum_t #{(x,y): y^2 = RHS}.
  - This script does NOT re-derive the local blow-up charts (that remains an
    explicitly flagged gap, structural analogy to the main manuscript's
    proved I2* resolution). It DOES independently, numerically confirm that
    the claimed closed-form correction (20p+1) makes the identity
    #X_III(F_p) = #V_III(F_p) + 20p + 1 numerically consistent with the
    independently-established fact T(p) = a_p(16.3.c.a), via the Lefschetz
    bridge:
        #X_III(F_p) = 1 + p^2 + Tr(Frob | NS) + Tr(Frob | T)
                     = 1 + p^2 + 20p + a_p(f16)          [assuming Tr_NS=20p]
    and
        #V_III(F_p) = p^2 + T(p)      [see class3_reduction.py, Round 1]
    so the ledger identity holds iff T(p) = a_p(f16), which is exactly the
    Round-2 central claim, cross-checked independently here via raw brute
    force point counts on V_III (NOT via the T(p) 2-variable reduction, to
    keep this an independent code path).
"""
import json


def chi(a, p):
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def count_V_III_points(p):
    """Brute-force count of affine points on V_III: Y^2 = X(X+1)T(T+1)(X+T+1),
    via direct enumeration over (X,T) and counting Y-solutions -- an
    INDEPENDENT code path from the T(p) character-sum reduction used
    elsewhere (no chi() shortcut on the full RHS; count Y directly)."""
    squares = {}
    for y in range(p):
        squares.setdefault((y * y) % p, []).append(y)
    total = 0
    for X in range(p):
        for T in range(p):
            rhs = (X * (X + 1) * T * (T + 1) * (X + T + 1)) % p
            total += len(squares.get(rhs, []))
    return total


def V_III_via_T(p):
    """#V_III(F_p) = p^2 + T(p), the formula from Round 1's reduction."""
    total = 0
    for x in range(p):
        for t in range(p):
            val = (x * t * (t + 1) * (x + t) * (x + t + 1)) % p
            total += chi(val, p)
    return p * p + total


data = json.load(open("/tmp/level16_weight3.json"))
traces_c = next(r["traces"] for r in data["data"] if r["label"] == "16.3.c.a")

primes = [5, 13, 17, 29, 37, 41, 53, 61]

print(f"{'p':>4}{'#V_III(brute)':>15}{'#V_III(p^2+T)':>15}{'agree':>7}{'a_p(f16)':>10}{'#X_III(pred)':>13}{'ledger':>18}")
for p in primes:
    v_brute = count_V_III_points(p)
    v_formula = V_III_via_T(p)
    agree = (v_brute == v_formula)
    a = traces_c[p - 1]
    X_pred_lefschetz = 1 + p * p + 20 * p + a
    X_pred_ledger = v_brute + 20 * p + 1
    ledger_ok = (X_pred_ledger == X_pred_lefschetz)
    print(f"{p:>4}{v_brute:>15}{v_formula:>15}{str(agree):>7}{a:>10}{X_pred_lefschetz:>13}{str(ledger_ok):>18}")

print()
print("All 'agree' True  => independent brute-force V_III count matches the")
print("  Round-1 character-sum reduction #V_III(F_p) = p^2 + T(p).")
print("All 'ledger' True => the corrected ledger #X_III(F_p) = #V_III(F_p) + 20p + 1")
print("  is numerically consistent, at every tested prime, with the Lefschetz")
print("  prediction #X_III(F_p) = 1 + p^2 + 20p + a_p(f16) assuming Tr_NS = 20p.")
print("  This is a CONSISTENCY check, not an independent proof of Tr_NS = 20p")
print("  (that assumption is flagged as an open structural-analogy gap in the report).")
