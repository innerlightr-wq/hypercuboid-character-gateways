"""Class III, Round 1: exact reduction verification.

Raw Class III polynomial (A-coordinates, n=4):
    P_III(x0,x1,x2) = x0 x1 x2 (x0+x2)(x1+x2)(x0+x1+x2)
Sigma_III(p) = sum_{x in F_p^3} chi(P_III(x)).

This script verifies, by EXACT finite-field brute force (not numerical
pattern-matching), the chain of reductions claimed in the Round-1 report:

  Sigma_III(p) = (p-1) * T(p),   T(p) := sum_{x,t} chi(x t(t+1)(x+t)(x+t+1))
  T(p) = sum_{x,t} chi(x(x+1) t(t+1) (x+t+1))          [form "S(p) shifted by 1"]
  T(p) = chi(-1) * sum_{x,t} chi(x(x+1) t(t+1) (x-t))   [reflection form]

and compares T(p) against S(p) = sum_{x,t} chi(x(x+1)t(t+1)(x+t)) (Class I/II's sum).
"""
import itertools

def chi(a, p):
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1

def Sigma_III_raw(p):
    total = 0
    for x0, x1, x2 in itertools.product(range(p), repeat=3):
        val = (x0 * x1 * x2 * (x0 + x2) * (x1 + x2) * (x0 + x1 + x2)) % p
        total += chi(val, p)
    return total

def T_of(p):
    # T(p) = sum_{x,t} chi(x * t(t+1) * (x+t)(x+t+1))
    total = 0
    for x in range(p):
        for t in range(p):
            val = (x * t * (t + 1) * (x + t) * (x + t + 1)) % p
            total += chi(val, p)
    return total

def T_shifted_S_form(p):
    # sum_{x,t} chi(x(x+1) t(t+1) (x+t+1))
    total = 0
    for x in range(p):
        for t in range(p):
            val = (x * (x + 1) * t * (t + 1) * (x + t + 1)) % p
            total += chi(val, p)
    return total

def T_reflection_form(p):
    # chi(-1) * sum_{x,t} chi(x(x+1) t(t+1) (x-t))
    total = 0
    for x in range(p):
        for t in range(p):
            val = (x * (x + 1) * t * (t + 1) * (x - t)) % p
            total += chi(val, p)
    return chi(-1, p) * total

def S_of(p):
    def g(t):
        return sum(chi(x * (x + 1) * (x + t) % p, p) for x in range(p))
    return sum(chi(t * (t + 1) % p, p) * g(t) for t in range(p))

if __name__ == "__main__":
    print(f"{'p':>4}{'p%4':>5}{'SigmaIII':>10}{'(p-1)*T':>10}{'T':>8}"
          f"{'T_shiftS':>10}{'T_refl':>8}{'S(p)':>8}{'match_all':>10}")
    for p in [5, 13, 17, 29, 37, 41, 53, 61, 73, 89, 97, 101, 109, 113]:
        SIII = Sigma_III_raw(p)
        T = T_of(p)
        Tss = T_shifted_S_form(p)
        Tref = T_reflection_form(p)
        Sp = S_of(p)
        pred = (p - 1) * T
        ok = (SIII == pred) and (T == Tss) and (T == Tref)
        print(f"{p:>4}{p%4:>5}{SIII:>10}{pred:>10}{T:>8}{Tss:>10}{Tref:>8}{Sp:>8}{str(ok):>10}")
