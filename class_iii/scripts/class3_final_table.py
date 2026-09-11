"""Final consolidated computational table for the Round-1 Class III report."""
import json

def chi(a, p):
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1

def Sigma_III_raw(p):
    total = 0
    for x0 in range(p):
        for x1 in range(p):
            for x2 in range(p):
                val = (x0*x1*x2*(x0+x2)*(x1+x2)*(x0+x1+x2)) % p
                total += chi(val, p)
    return total

def T_of(p):
    total = 0
    for x in range(p):
        for t in range(p):
            val = (x*t*(t+1)*(x+t)*(x+t+1)) % p
            total += chi(val, p)
    return total

data = json.load(open("/tmp/level16_weight3.json"))
traces_c = next(r["traces"] for r in data["data"] if r["label"] == "16.3.c.a")

primes = [3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139]
print(f"{'p':>4}{'p%4':>5}{'chi2':>5}{'chim2':>6}{'Sigma_III(p)':>13}{'(p-1)T(p) match':>17}{'T(p)':>7}{'a_16.3.c.a(p)':>14}{'match':>7}")
for p in primes:
    SIII = Sigma_III_raw(p)
    Tp = T_of(p)
    ok_reduction = (SIII == (p-1)*Tp)
    a = traces_c[p-1]
    ok_aop = (Tp == a)
    c2, cm2 = chi(2,p), chi(-2,p)
    print(f"{p:>4}{p%4:>5}{c2:>5}{cm2:>6}{SIII:>13}{str(ok_reduction):>17}{Tp:>7}{a:>14}{str(ok_aop):>7}")
