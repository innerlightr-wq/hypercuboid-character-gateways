"""Verify the symbolic elimination engine against direct finite-field
enumeration, for arbitrary integer-coefficient homogeneous linear forms
(not just the standard 0/1 subset-sum family, since substitution can
introduce -1 coefficients)."""

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))
from elimination_engine import Forms, eliminate  # noqa: E402


def legendre_table(p: int) -> np.ndarray:
    table = np.empty(p, dtype=np.int64)
    table[0] = 0
    e = (p - 1) // 2
    for a in range(1, p):
        table[a] = 1 if pow(a, e, p) == 1 else -1
    return table


def direct_sigma(forms: Forms, d: int, p: int) -> int:
    if d == 0:
        return 0 if forms else 1
    leg = legendre_table(p)
    axes = [np.arange(p, dtype=np.int64) for _ in range(d)]
    grids = np.meshgrid(*axes, indexing="ij")
    coords = np.stack([g.reshape(-1) for g in grids], axis=1)
    prod = np.ones(p**d, dtype=np.int64)
    for f in forms:
        val = (coords * np.array(f)).sum(axis=1) % p
        prod = prod * leg[val]
    return int(prod.sum())


def check(forms: Forms, d: int, primes: list[int], label: str):
    res = eliminate(forms, d)
    if res.value is None:
        print(f"{label}: UNRESOLVED (residual branches: {len(res.unresolved)})")
        for f, dd in res.unresolved:
            print("   residual:", f, "dim", dd)
        return False
    print(f"{label}: predicted = {res.value.pretty()}")
    all_ok = True
    for p in primes:
        pred = res.value.evaluate(p)
        act = direct_sigma(forms, d, p)
        ok = pred == act
        all_ok &= ok
        print(f"   p={p:4d} predicted={pred:8d} actual={act:8d} {'OK' if ok else 'MISMATCH'}")
    return all_ok


if __name__ == "__main__":
    primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 61]

    print("=== Round-1 example A: n=4, S={L0,L1,L2,L012} -> claimed chi(-1)p(p-1) ===")
    # coordinates 0,1,2 (d=3); L0=(1,0,0) L1=(0,1,0) L2=(0,0,1) L012=(1,1,1)
    formsA: Forms = ((1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 1))
    check(formsA, 3, primes, "A")

    print("\n=== Round-1 example B: n=4, S={L0,L1,L4,L5} i.e. (0,1,4,5) -> claimed p(p-1) ===")
    # need to reconstruct which forms these are: from core.py enumeration
    # for n=4 (d=3): idx0={0},1={1},2={2},3={0,1},4={0,2},5={1,2},6={0,1,2}
    formsB: Forms = ((1, 0, 0), (0, 1, 0), (1, 0, 1), (0, 1, 1))  # L0,L1,L02,L12
    check(formsB, 3, primes, "B")

    print("\n=== Round-1 example C: n=5, S=(4,5,8,9) 4-cycle -> claimed p^2(p-1) ===")
    # n=5 (d=4): idx4={0,1},5={0,2},8={1,3},9={2,3}
    formsC: Forms = ((1, 1, 0, 0), (1, 0, 1, 0), (0, 1, 0, 1), (0, 0, 1, 1))
    check(formsC, 4, primes, "C")

    print("\n=== Sanity: private coordinate, should give exact 0 ===")
    formsD: Forms = ((1, 0, 0), (0, 1, 0))  # L0, L1: coordinate 2 has mult 0 (fine, unused), no issue
    check(formsD, 3, primes, "D (pair, mult profile [1,1,0])")

    print("\n=== Odd cardinality sanity (already proved elsewhere): single form ===")
    formsE: Forms = ((1, 1, 1),)
    check(formsE, 3, primes[:6], "E (|S|=1)")
