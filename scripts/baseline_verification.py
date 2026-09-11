"""Baseline reproduction of the paper's own theorem-level results.

Reproduces (does NOT claim as new):
  - Proposition 6.2 / Appendix C.5: exact vanishing of Sigma_S(p) for every
    nonempty ODD-cardinality S, for n=4 and n=5, across many primes
    (both p = 1 and 3 mod 4, since the odd-vanishing proof does not use
    p mod 4 at all).
  - Theorem 6.1: N_0^clean(p,5) = 0 for p = 3 (mod 4); nonzero (eventually)
    for p = 1 (mod 4), consistent with the paper's own Section 9 caution
    that small-p clean counts are frequently 0 even where the main term is
    nonzero.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from core import (  # noqa: E402
    PRIMES_1MOD4,
    PRIMES_3MOD4,
    ZeroSectorSystem,
    chi_columns,
    clean_count_zero_sector,
    sigma_S,
)


def verify_odd_vanishing(n: int, primes: list[int]) -> dict:
    sys_ = ZeroSectorSystem.build(n)
    m = sys_.m
    results = {"n": n, "m": m, "checked": 0, "violations": []}
    odd_subsets = []
    for k in range(1, m + 1, 2):
        import itertools

        odd_subsets.extend(itertools.combinations(range(m), k))
    for p in primes:
        cols, _ = chi_columns(sys_, p)
        for S in odd_subsets:
            val = sigma_S(cols, S)
            results["checked"] += 1
            if val != 0:
                results["violations"].append((p, S, val))
    return results


def verify_clean_counts(primes_1mod4: list[int], primes_3mod4: list[int]) -> dict:
    sys5 = ZeroSectorSystem.build(5)
    out = {"n": 5, "p_1mod4": {}, "p_3mod4": {}}
    for p in primes_3mod4:
        out["p_3mod4"][p] = clean_count_zero_sector(sys5, p)
    for p in primes_1mod4:
        out["p_1mod4"][p] = clean_count_zero_sector(sys5, p)
    return out


if __name__ == "__main__":
    print("=== Baseline: odd-cardinality exact vanishing (Prop 6.2 / App C.5) ===")
    for n in (3, 4, 5):
        primes = [p for p in (PRIMES_1MOD4[:4] + PRIMES_3MOD4[:4])]
        res = verify_odd_vanishing(n, sorted(primes))
        print(f"n={n}: m={res['m']} forms, checked {res['checked']} (S,p) pairs, "
              f"violations={len(res['violations'])}")
        if res["violations"]:
            print("  FIRST VIOLATION:", res["violations"][0])

    print()
    print("=== Baseline: Theorem 6.1 zero-diagonal clean counts, n=5 ===")
    cc = verify_clean_counts(primes_1mod4=[5, 13, 17, 29, 37, 41],
                              primes_3mod4=[3, 7, 11, 19, 23, 31])
    print("p = 3 (mod 4) -> N_0^clean(p,5):", cc["p_3mod4"])
    print("p = 1 (mod 4) -> N_0^clean(p,5):", cc["p_1mod4"])
