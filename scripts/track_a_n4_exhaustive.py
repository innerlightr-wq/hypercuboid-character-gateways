"""TRACK A, n=4: exhaustive even-cardinality character-moment search.

n=4 -> d=3 variables, m=7 representative forms L_J (J nonempty subset of
{0,1,2}). There are 2^7-1=127 nonempty subsets S of the forms; 63 of them
have even |S|. Fully tractable to test ALL 63 at many primes -- no
symmetry reduction needed for correctness (we still record the invariant
classification for interpretability).

Exact arithmetic throughout (int64 modular sums via numpy, no floats
except the final diagnostic growth-rate estimate, which is clearly
labeled as a diagnostic).
"""

import itertools
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from core import (  # noqa: E402
    PRIMES_1MOD4,
    PRIMES_3MOD4,
    ZeroSectorSystem,
    chi_columns,
    coeff_matrix,
    matrix_rank_mod,
    sigma_S,
)

N = 4
PRIMES = sorted(PRIMES_1MOD4[:8] + PRIMES_3MOD4[:8])  # mix of both classes


def even_subsets(m: int):
    out = []
    for k in range(2, m + 1, 2):
        out.extend(itertools.combinations(range(m), k))
    return out


def main():
    sys_ = ZeroSectorSystem.build(N)
    m = sys_.m
    d = sys_.d
    S_list = even_subsets(m)
    print(f"n={N}, d={d}, m={m} forms, {len(S_list)} nonempty even-|S| subsets, "
          f"{len(PRIMES)} primes: {PRIMES}")

    # Precompute chi columns per prime once.
    cols_by_p = {}
    t0 = time.time()
    for p in PRIMES:
        cols, _ = chi_columns(sys_, p)
        cols_by_p[p] = cols
    print(f"chi columns precomputed in {time.time()-t0:.2f}s")

    records = []
    t0 = time.time()
    for S in S_list:
        rankQ = matrix_rank_mod(coeff_matrix(sys_, S), modulus=None)
        rank2 = matrix_rank_mod(coeff_matrix(sys_, S), modulus=2)
        vals = {}
        for p in PRIMES:
            vals[p] = sigma_S(cols_by_p[p], S)
        records.append({
            "S": S, "size": len(S), "rankQ": rankQ, "rank2": rank2,
            "sigma": vals,
        })
    print(f"all Sigma_S computed in {time.time()-t0:.2f}s")

    out_path = Path(__file__).parent.parent / "results" / "track_a_n4_full.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump({"n": N, "d": d, "m": m, "primes": PRIMES, "records": records}, f)
    print("wrote", out_path)

    # Quick scan: any S with Sigma_S == 0 at EVERY tested prime?
    always_zero = [r for r in records if all(v == 0 for v in r["sigma"].values())]
    print(f"\nSubsets with Sigma_S(p)=0 at ALL {len(PRIMES)} tested primes: "
          f"{len(always_zero)}")
    for r in always_zero:
        print(" ", r["S"], "size=", r["size"], "rankQ=", r["rankQ"],
              "rank2=", r["rank2"])

    # Growth-rate diagnostic (float ratio, clearly diagnostic only):
    # generic scale is p^{d-1/2}=p^{2.5}; "anomalous" would be p^{d-1}=p^2
    # or smaller. Compare |Sigma_S| at the two largest tested primes.
    p_hi2 = sorted(PRIMES)[-2:]
    print(f"\nDiagnostic growth check using primes {p_hi2} "
          f"(generic exponent 2.5, anomalous <= 2.0):")
    import math

    anomalous = []
    for r in records:
        v1, v2 = r["sigma"][p_hi2[0]], r["sigma"][p_hi2[1]]
        if v1 == 0 and v2 == 0:
            continue
        if v1 == 0 or v2 == 0:
            continue
        slope = math.log(abs(v2) / abs(v1)) / math.log(p_hi2[1] / p_hi2[0])
        if slope < 2.1:
            anomalous.append((r["S"], r["size"], r["rankQ"], r["rank2"], round(slope, 3)))
    print(f"subsets with estimated growth slope < 2.1: {len(anomalous)}")
    for a in anomalous[:20]:
        print(" ", a)


if __name__ == "__main__":
    main()
