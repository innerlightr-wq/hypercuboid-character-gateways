"""Verification for notes/INCIDENCE_STRUCTURE_LEMMA.md.

All arithmetic is exact integer/modular arithmetic; no floating point enters any
reported number. Reproduces, in order:

  1. the Incidence Structure Lemma   m_q(x) = 2^z * s - 1   by exhaustive
     brute force over every nonzero x in F_q^d;
  2. the tables T_k(q) of achievable |S'| for k nonzero values;
  3. the realizable spectra S_d(q) derived from the corollary, cross-checked
     against direct enumeration of m_q;
  4. the stabilization caveat (T_6(7) differs from T_6(11) = T_6(13) = T_6(17)).

Setup matches scripts/core.py: d = n - 1, forms L_J(x) = sum_{j in J} x_j for
nonempty J subseteq [d], evaluated at x in F_q^d with x != 0.

Run:  python3 scripts/incidence_lemma_check.py
Exit: 0 if every check passes, 1 otherwise.
"""

from __future__ import annotations

import itertools
import sys


def m_q(x: tuple[int, ...], q: int) -> int:
    """#{ nonempty J subseteq [d] : sum_{j in J} x_j = 0 mod q }, by direct count."""
    d = len(x)
    return sum(
        1
        for mask in range(1, 1 << d)
        if sum(x[i] for i in range(d) if mask >> i & 1) % q == 0
    )


def z_and_s(x: tuple[int, ...], q: int) -> tuple[int, int]:
    """(z, s): z = #zero coordinates; s = |S'| over the nonzero coordinates."""
    nz = [v for v in x if v % q]
    z = len(x) - len(nz)
    k = len(nz)
    s = sum(
        1
        for mask in range(1 << k)
        if sum(nz[i] for i in range(k) if mask >> i & 1) % q == 0
    )
    return z, s


def T(k: int, q: int) -> set[int]:
    """Achievable s = |S'| for k nonzero values in F_q^*.

    Scaling-invariant, so the first value may be fixed to 1 without loss.
    """
    if k == 0:
        return {1}
    out: set[int] = set()
    for rest in itertools.product(range(1, q), repeat=k - 1):
        y = (1,) + rest
        out.add(
            sum(
                1
                for mask in range(1 << k)
                if sum(y[i] for i in range(k) if mask >> i & 1) % q == 0
            )
        )
    return out


def spectrum_from_corollary(d: int, q: int) -> set[int]:
    """S_d(q) = { 2^z * s - 1 : 0 <= z <= d-1, s in T_{d-z}(q) }."""
    return {2**z * s - 1 for z in range(d) for s in T(d - z, q)}


def spectrum_direct(d: int, q: int) -> set[int]:
    """S_d(q) by direct enumeration of m_q over every nonzero x in F_q^d."""
    return {
        m_q(x, q)
        for x in itertools.product(range(q), repeat=d)
        if any(v % q for v in x)
    }


def main() -> int:
    ok = True

    # --- 1. the lemma, exhaustively -------------------------------------
    checked = 0
    for q in (3, 5, 7, 11, 13):
        for d in (2, 3, 4, 5):
            if q**d > 400_000:
                continue
            for x in itertools.product(range(q), repeat=d):
                if not any(v % q for v in x):
                    continue
                z, s = z_and_s(x, q)
                checked += 1
                if m_q(x, q) != 2**z * s - 1:
                    print(f"  FAIL lemma at q={q} d={d} x={x}")
                    ok = False
    print(f"1. lemma m_q = 2^z*s - 1 : {checked} nonzero points checked, "
          f"{'all pass' if ok else 'FAILURES'}")

    # --- 2. T_k(q) tables -----------------------------------------------
    print("2. T_k(q):")
    for k in range(1, 7):
        row = "  ".join(f"q={q}:{sorted(T(k, q))}" for q in (3, 5, 7, 11, 13))
        print(f"     k={k}: {row}")

    # --- 3. spectra, corollary vs direct enumeration --------------------
    print("3. spectra (corollary vs direct enumeration):")
    for d, q_min in ((3, 5), (4, 5), (5, 7)):
        for q in (3, 5, 7, 11, 13):
            if q**d > 400_000:
                continue
            a = spectrum_from_corollary(d, q)
            b = spectrum_direct(d, q)
            agree = a == b
            ok &= agree
            flag = "" if q >= q_min else "   (below stabilization threshold)"
            print(f"     d={d} n={d+1} q={q:<3} {sorted(a)}"
                  f"   corollary==direct: {agree}{flag}")

    # --- 4. the stabilization caveat ------------------------------------
    t6 = {q: sorted(T(6, q)) for q in (7, 11, 13, 17)}
    caveat = t6[7] != t6[11] and t6[11] == t6[13] == t6[17]
    ok &= caveat
    print("4. stabilization is NOT at q > k:")
    for q, v in t6.items():
        print(f"     T_6({q:>2}) = {v}")
    print(f"     T_6(7) != T_6(11) == T_6(13) == T_6(17): {caveat}")

    print("\nALL CHECKS PASS" if ok else "\nCHECKS FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
