"""TRACK B: prime-power lifting, direct exhaustive verification.

Hand derivation (to be checked, not assumed):
  Using the exact-elimination parametrization (A_n := -(A_1+...+A_{n-1})),
  D_full = 0 holds identically at every prime-power level for ANY lift of
  (A_1,...,A_{n-1}). Every representative form L_J is then a UNIT mod p
  (nonzero, since it's a QR), and by elementary group theory the kernel of
  reduction (Z/p^{k+1})^x -> (Z/p^k)^x has ODD order p, hence lies inside
  the index-2 subgroup of squares -- so QR-status of a unit mod p^k depends
  ONLY on its reduction mod p (this is exactly Prop A.3, "shallow lifting").
  Distinctness mod p is preserved under any refinement to mod p^k trivially.

  CONSEQUENCE (to be checked): every clean-mod-p zero-sector tuple should
  have ALL p^{(n-1)(k-1)} naive digit-lifts to mod p^k be clean mod p^k,
  with NO obstruction beyond ordinary shallow/unit-square lifting.

This script checks that claim by DIRECT EXHAUSTIVE ENUMERATION (not by
trusting the derivation), for n=3 and n=4, p -> p^2 and (for n=3) p^2 -> p^3.
"""

import itertools
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from core import ZeroSectorSystem  # noqa: E402


def is_prime(m: int) -> bool:
    if m < 2:
        return False
    return all(m % d for d in range(2, int(m ** 0.5) + 1))


def _base_prime(modulus: int) -> tuple[int, int]:
    """Return (p, k) with modulus == p**k, by trial division. Only ever
    called with modulus = p or p**2 or p**3 in this script's usage."""
    for p in range(2, modulus + 1):
        if modulus % p == 0 and is_prime(p):
            k = 0
            m = modulus
            while m % p == 0:
                m //= p
                k += 1
            assert m == 1, "modulus must be a prime power for this script"
            return p, k
    raise ValueError(modulus)


def legendre(a: int, modulus: int) -> int:
    """Exact quadratic-residue indicator for a UNIT a modulo a prime power
    p**k. Uses the correct Euler-criterion exponent phi(p**k)/2 =
    p**(k-1)*(p-1)/2 -- NOT (modulus-1)/2, which is only valid when
    modulus itself is prime (k=1). Using the wrong exponent for k>=2 was
    caught and fixed in this round (see notes/track_b_bugfix.md)."""
    a %= modulus
    p, k = _base_prime(modulus)
    if a % p == 0:
        return 0
    phi = p ** (k - 1) * (p - 1)
    r = pow(a, phi // 2, modulus)
    return 1 if r == 1 else -1


def clean_mod(sys_: ZeroSectorSystem, A_free: tuple[int, ...], modulus: int) -> bool:
    """A_free = (A_1,...,A_{n-1}) mod `modulus`. Check clean mod `modulus`:
    every representative form is a nonzero QR mod `modulus`, and all n
    coordinates (including the eliminated A_n) are pairwise distinct."""
    d = sys_.d
    n = sys_.n
    for J in sys_.subsets:
        val = sum(A_free[i] for i in J) % modulus
        if legendre(val, modulus) != 1:
            return False
    An = (-sum(A_free)) % modulus
    full = list(A_free) + [An]
    return len(set(full)) == n


def find_clean_mod_p(sys_: ZeroSectorSystem, p: int) -> list[tuple[int, ...]]:
    d = sys_.d
    out = []
    for A in itertools.product(range(p), repeat=d):
        if clean_mod(sys_, A, p):
            out.append(A)
    return out


def lift_test(sys_: ZeroSectorSystem, p: int, k_from: int, k_to: int,
               base_moduli_examples: int = 5) -> dict:
    """base is mod p^k_from clean tuples; lift to mod p^k_to and count how
    many of the p^{d*(k_to-k_from)} digit-lifts remain clean mod p^k_to."""
    d = sys_.d
    mod_from = p ** k_from
    mod_to = p ** k_to
    step = p ** (k_to - k_from)  # number of digit choices per coordinate

    clean_base = find_clean_mod_p(sys_, p) if k_from == 1 else None
    if k_from != 1:
        raise NotImplementedError
    print(f"  p={p}: {len(clean_base)} clean tuples mod p^{k_from} "
          f"(out of {p**d} total)")

    results = []
    tested = 0
    for A0 in clean_base[:base_moduli_examples]:
        total_lifts = step ** d
        clean_lifts = 0
        for extra_digits in itertools.product(range(step), repeat=d):
            A_lift = tuple(a0 + digit * mod_from for a0, digit in zip(A0, extra_digits))
            if clean_mod(sys_, A_lift, mod_to):
                clean_lifts += 1
        results.append((A0, clean_lifts, total_lifts))
        tested += 1
    return {"p": p, "clean_base_count": len(clean_base), "lift_results": results}


def main():
    print("=== n=3 (d=2), p -> p^2 lifting, exhaustive over ALL lifts ===")
    sys3 = ZeroSectorSystem.build(3)
    for p in [5, 13, 17]:
        r = lift_test(sys3, p, 1, 2, base_moduli_examples=10**9)
        for A0, clean_lifts, total_lifts in r["lift_results"]:
            status = "ALL CLEAN" if clean_lifts == total_lifts else "OBSTRUCTION FOUND"
            print(f"    base A={A0}: {clean_lifts}/{total_lifts} lifts clean mod p^2  [{status}]")

    print("\n=== n=3 (d=2), p -> p^3 lifting (direct, small p only) ===")
    for p in [5]:
        r = lift_test(sys3, p, 1, 3, base_moduli_examples=10**9)
        for A0, clean_lifts, total_lifts in r["lift_results"]:
            status = "ALL CLEAN" if clean_lifts == total_lifts else "OBSTRUCTION FOUND"
            print(f"    base A={A0}: {clean_lifts}/{total_lifts} lifts clean mod p^3  [{status}]")

    print("\n=== n=4 (d=3), p -> p^2 lifting (small p, sample of bases) ===")
    sys4 = ZeroSectorSystem.build(4)
    for p in [5, 13]:
        r = lift_test(sys4, p, 1, 2, base_moduli_examples=10**9)
        n_ok = sum(1 for _, c, t in r["lift_results"] if c == t)
        n_total = len(r["lift_results"])
        print(f"    p={p}: {n_ok}/{n_total} clean-mod-p bases have ALL lifts clean mod p^2")
        for A0, clean_lifts, total_lifts in r["lift_results"]:
            if clean_lifts != total_lifts:
                print(f"      OBSTRUCTION at base {A0}: {clean_lifts}/{total_lifts}")


if __name__ == "__main__":
    main()
