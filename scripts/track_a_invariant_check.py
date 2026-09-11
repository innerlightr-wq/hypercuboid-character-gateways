"""Post-process Track A n=4 data: test the 'private coordinate' vanishing
criterion and the 'multiplicity-2' anomalous-scaling criterion.

Rediscovery-filter candidate mechanism (derived by hand, verified here):
  For S a set of representative forms L_J, let r_k(S) = number of J in S
  with k in J (k ranges over the d coordinates). CLAIM: if r_k(S) = 1 for
  some k, then Sigma_S(p) = 0 EXACTLY for every odd prime p, by an
  elementary telescoping argument (fix all other variables; the sum over
  the private coordinate x_k is a sum of chi over a full affine shift of
  F_p, which is exactly 0).

  This is a strict generalization, via a DIFFERENT elementary argument, of
  Prop 6.2's homogeneous-scaling vanishing (which only covers odd |S|) --
  this one applies to any |S|, odd or even, whenever a private coordinate
  exists.
"""

import itertools
import json
from pathlib import Path

import sys
sys.path.insert(0, str(Path(__file__).parent))
from core import ZeroSectorSystem  # noqa: E402


def coordinate_multiplicities(sys_: ZeroSectorSystem, S: tuple[int, ...]) -> list[int]:
    d = sys_.d
    r = [0] * d
    for j in S:
        for k in sys_.subsets[j]:
            r[k] += 1
    return r


def main():
    data = json.load(open(Path(__file__).parent.parent / "results" / "track_a_n4_full.json"))
    sys_ = ZeroSectorSystem.build(data["n"])
    primes = data["primes"]

    n_private_vanish_match = 0
    n_private_but_nonzero = []
    n_no_private_but_zero = []
    mult2_slopes = []

    for r in data["records"]:
        S = tuple(r["S"])
        mults = coordinate_multiplicities(sys_, S)
        has_private = any(m == 1 for m in mults)
        all_zero = all(v == 0 for v in r["sigma"].values())
        if has_private:
            if all_zero:
                n_private_vanish_match += 1
            else:
                n_private_but_nonzero.append((S, mults, r["sigma"]))
        else:
            if all_zero:
                n_no_private_but_zero.append((S, mults))

        if not has_private and min(mults) == 2 if mults else False:
            mult2_slopes.append((S, mults))

    print(f"Total records: {len(data['records'])}")
    print(f"Has a private coordinate (r_k=1 for some k): "
          f"{n_private_vanish_match + len(n_private_but_nonzero)}")
    print(f"  -> of those, Sigma_S=0 at ALL {len(primes)} primes: {n_private_vanish_match}")
    print(f"  -> of those, Sigma_S NONZERO at some prime (COUNTEREXAMPLES to the "
          f"private-coordinate claim): {len(n_private_but_nonzero)}")
    for c in n_private_but_nonzero[:10]:
        print("    COUNTEREXAMPLE:", c)

    print(f"\nNo private coordinate, but Sigma_S=0 at all tested primes anyway: "
          f"{len(n_no_private_but_zero)}")
    for c in n_no_private_but_zero[:10]:
        print("   ", c)

    print(f"\nNo private coordinate, min multiplicity exactly 2 "
          f"(candidate for the anomalous ~p^(d-1) scaling): {len(mult2_slopes)}")
    for S, mults in mult2_slopes:
        sigma = next(r["sigma"] for r in data["records"] if tuple(r["S"]) == S)
        print("   ", S, "mults=", mults, "sigma@53,61=", sigma["53"], sigma["61"])


if __name__ == "__main__":
    main()
