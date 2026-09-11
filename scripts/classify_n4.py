"""Part V: exhaustive n=4 classification of all nonempty even-|S| subsets
of the 7 zero-sector forms, using the elimination engine, cross-checked
against direct enumeration. Also runs the Part VII confluence test
(multiple elimination orders) on every resolved case with >1
multiplicity-2 coordinate available at the first step.
"""

import itertools
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from core import ZeroSectorSystem, coeff_matrix, matrix_rank_mod  # noqa: E402
from elimination_engine import eliminate, multiplicities  # noqa: E402
from verify_engine import direct_sigma  # noqa: E402


def to_forms(sys_: ZeroSectorSystem, S_idx):
    d = sys_.d
    out = []
    for j in S_idx:
        v = [0] * d
        for i in sys_.subsets[j]:
            v[i] = 1
        out.append(tuple(v))
    return tuple(out)


def even_subsets(m: int):
    out = []
    for k in range(2, m + 1, 2):
        out.extend(itertools.combinations(range(m), k))
    return out


PRIMES = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 61]


def main():
    sys_ = ZeroSectorSystem.build(4)
    m = sys_.m
    d = sys_.d
    S_list = even_subsets(m)
    print(f"n=4, d={d}, m={m}, {len(S_list)} nonempty even subsets")

    records = []
    n_resolved = 0
    n_unresolved = 0
    n_private = 0
    confluence_checked = 0
    confluence_failures = []

    for S_idx in S_list:
        forms = to_forms(sys_, S_idx)
        mult0 = multiplicities(forms, d)
        has_private = any(mm == 1 for mm in mult0)
        n2 = [k for k, mm in enumerate(mult0) if mm == 2]

        res = eliminate(forms, d)
        resolved = res.value is not None
        if resolved:
            n_resolved += 1
        else:
            n_unresolved += 1
        if has_private:
            n_private += 1

        rec = {
            "S": S_idx,
            "size": len(S_idx),
            "mult": mult0,
            "has_private": has_private,
            "resolved": resolved,
            "formula": res.value.pretty() if resolved else None,
        }

        # verify against direct enumeration at a couple of primes
        if resolved:
            mism = []
            for p in (13, 29, 53):
                pred = res.value.evaluate(p)
                act = direct_sigma(forms, d, p)
                if pred != act:
                    mism.append((p, pred, act))
            rec["verify_mismatches"] = mism

        # confluence test: if >=2 multiplicity-2 coords available at the
        # very first step, try each as the FIRST elimination choice and
        # compare final symbolic results.
        if resolved and len(n2) >= 2:
            confluence_checked += 1
            results = []
            for k0 in n2:
                r = eliminate(forms, d, order_hint=[k0])
                results.append((k0, r.value.pretty() if r.value else "UNRESOLVED"))
            base = results[0][1]
            if any(r[1] != base for r in results[1:]):
                confluence_failures.append((S_idx, results))
            rec["confluence_orders_tested"] = results

        records.append(rec)

    out_path = Path(__file__).parent.parent / "results" / "classify_n4.json"
    with open(out_path, "w") as f:
        json.dump({"n": 4, "records": records}, f, indent=1)
    print("wrote", out_path)

    print(f"\nTotal even subsets: {len(S_list)}")
    print(f"Resolved by elimination: {n_resolved} ({100*n_resolved/len(S_list):.1f}%)")
    print(f"Unresolved: {n_unresolved}")
    print(f"Has private coordinate: {n_private}")
    print(f"Confluence-checked (>=2 mult-2 coords at step 1): {confluence_checked}")
    print(f"Confluence FAILURES: {len(confluence_failures)}")
    for s, r in confluence_failures[:10]:
        print("  ", s, r)

    verify_fail = [r for r in records if r.get("verify_mismatches")]
    print(f"\nDirect-enumeration verification failures: {len(verify_fail)}")
    for r in verify_fail[:10]:
        print("  ", r["S"], r["verify_mismatches"])

    print("\n--- Unresolved subsets (mult profile) ---")
    for r in records:
        if not r["resolved"]:
            print("  ", r["S"], "mult=", r["mult"])


if __name__ == "__main__":
    main()
