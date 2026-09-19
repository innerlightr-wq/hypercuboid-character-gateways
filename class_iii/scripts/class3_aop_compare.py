import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from newform_16_3_c_a import traces_c  # noqa: E402

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

def a_p_E_i(p, curve="x3+x"):
    # CM-by-Q(i) elliptic curve y^2 = x^3+x  (j=1728)
    return -sum(chi((x**3 + x) % p, p) for x in range(p))

def A_lambda(lam_num, lam_den, p):
    # AOP: A(lambda,q) = chi(lambda+1) * (a(lambda,q)^2 - q)
    # a(lambda,q) = -sum_x chi((x-1)(x^2 - 1/(lambda+1)))
    inv_den = pow(lam_den, p - 2, p)
    lam = (lam_num * inv_den) % p
    lam_plus_1 = (lam + 1) % p
    if lam_plus_1 == 0:
        return None
    inv_lp1 = pow(lam_plus_1, p - 2, p)
    a = 0
    for x in range(p):
        val = ((x - 1) * (x * x - inv_lp1)) % p
        a -= chi(val, p)
    return chi(lam_plus_1, p) * (a * a - p) % p if False else chi(lam_plus_1, p) * (a * a - p)

print(f"{'p':>4}{'p%4':>5}{'T(p)':>8}{'chi2':>5}{'chim2':>6}{'a16.3.c.a':>10}"
      f"{'apE_i':>7}{'A(8,p)':>8}{'A(1/8,p)':>9}{'T/apE_i^2?':>10}")
for p in [5, 13, 17, 29, 37, 41, 53, 61, 73, 89, 97, 101, 109, 113]:
    Tp = T_of(p)
    c2, cm2 = chi(2, p), chi(-2, p)
    a163ca = traces_c[p - 1] if p - 1 < len(traces_c) else None
    apEi = a_p_E_i(p)
    A8 = A_lambda(8, 1, p)
    A18 = A_lambda(1, 8, p)
    print(f"{p:>4}{p%4:>5}{Tp:>8}{c2:>5}{cm2:>6}{a163ca:>10}{apEi:>7}{A8:>8}{A18:>9}")

print()
print("=== p===3 mod 4 check (Sigma_III=0 already proved; does T(p) and a(16.3.c.a) both vanish?) ===")
print(f"{'p':>4}{'T(p)':>8}{'a16.3.c.a':>10}{'SigmaIII':>10}")
for p in [3,7,11,19,23,31,43,47,59,67,71,79,83]:
    idx = p-1
    a = traces_c[idx] if idx < len(traces_c) else None
    Tp = T_of(p)
    print(f"{p:>4}{Tp:>8}{a:>10}{(p-1)*Tp:>10}")

print()
print("=== Weil bound check: |T(p)| <= 2 p^{(3-1)/2} = 2p for weight-3 form ===")
import math
for p in [97,101,109,113]:
    Tp = T_of(p)
    bound = 2*p
    print(f"p={p}: |T(p)|={abs(Tp)}, bound 2p={bound}, within bound: {abs(Tp)<=bound}")
