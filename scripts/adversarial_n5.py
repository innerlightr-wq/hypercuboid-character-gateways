"""Part XI: n=5 adversarial test of the elimination engine.

Not exhaustive (2^14-1 nonempty even subsets is too many); instead
targeted cases chosen to challenge the mechanism found at n=4.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from core import ZeroSectorSystem  # noqa: E402
from elimination_engine import eliminate, multiplicities  # noqa: E402
from verify_engine import direct_sigma  # noqa: E402

PRIMES = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]


def to_forms(sys_, S_idx):
    d = sys_.d
    out = []
    for j in S_idx:
        v = [0] * d
        for i in sys_.subsets[j]:
            v[i] = 1
        out.append(tuple(v))
    return tuple(out)


def run(label, sys_, S_idx, primes=PRIMES):
    forms = to_forms(sys_, S_idx)
    mult = multiplicities(forms, sys_.d)
    res = eliminate(forms, sys_.d)
    print(f"\n[{label}] S={S_idx} mult={mult}")
    if res.value is None:
        print("  UNRESOLVED")
        return
    print(f"  predicted: {res.value.pretty()}")
    all_ok = True
    for p in primes:
        pred = res.value.evaluate(p)
        act = direct_sigma(forms, sys_.d, p)
        ok = pred == act
        all_ok &= ok
        if not ok:
            print(f"    MISMATCH at p={p}: predicted={pred} actual={act}")
    print(f"  {'ALL MATCH' if all_ok else 'HAS MISMATCH'} across {len(primes)} primes")


def main():
    sys_ = ZeroSectorSystem.build(5)
    print("index map:", {i: sorted(s) for i, s in enumerate(sys_.subsets)})

    # 1. trivial private-coordinate case
    run("private (trivial)", sys_, (0, 1))

    # 2. fully-peelable mult-2 "star+full" (analogue of n=4's (0,1,2,6))
    run("star+free-coord (chi(-1) expected)", sys_, (0, 1, 2, 10))

    # 3. simple 4-cycle (already validated in Round 1, re-confirm here)
    run("4-cycle (p^2(p-1) expected)", sys_, (4, 5, 8, 9))

    # 4. a DIFFERENT 4-cycle labeling (isomorphic graph, tests permutation invariance)
    run("4-cycle, different labeling", sys_, (4, 9, 6, 7))

    # 5. overlapping cycles: ALL 6 pairs at once (dense 3-core, adversarial)
    run("all 6 pairs (dense 3-core, adversarial)", sys_, (4, 5, 6, 7, 8, 9))

    # 6. same mult vector [2,2,2,2], different incidence geometry (mixed
    #    single/pair/triple forms instead of a pure 4-cycle of pairs)
    run("mult=[2,2,2,2] but mixed-type incidence", sys_, (7, 11, 5, 3))

    # 7. a genuine private-coordinate n=5 case with |S| larger (even)
    run("private coordinate, |S|=4", sys_, (0, 4, 5, 6))  # coord0 mult? check below

    # 8. all 4 triples (mult should be 3 each -- adversarial core)
    run("all 4 triples (3-core)", sys_, (10, 11, 12, 13))

    # 9. mixed: 2 triples + 2 pairs, designed to test partial peeling
    run("2 triples + 2 pairs", sys_, (10, 13, 4, 9))

    # 10. |S|=2 pair sharing NO coordinate structure oddities: two triples
    run("two triples (mult check)", sys_, (10, 11))


if __name__ == "__main__":
    main()
