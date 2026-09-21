"""Verification for notes/INCIDENCE_STRUCTURE_LEMMA.md.

All arithmetic is exact integer/modular arithmetic; no floating point enters any
reported number. Reproduces, in order:

  1. the Incidence Structure Lemma   m_q(x) = 2^z * s - 1   by exhaustive
     brute force over every nonzero x in F_q^d;
  2. the tables T_k(q) of achievable |S'| for k nonzero values;
  3. the realizable spectra S_d(q) derived from the corollary, cross-checked
     against direct enumeration of m_q;
  4. the stabilization caveat (T_6(7) differs from T_6(11) = T_6(13) = T_6(17));
  5. Remark 2.1: the factorization needs neither primality, nor odd
     characteristic, nor x != 0 -- checked over Z/n for composite and even n,
     over non-cyclic abelian groups, and at x = 0.

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


def lemma_holds_over_group(elements, add, zero, d: int) -> bool:
    """The factorization, checked over an arbitrary finite abelian group.

    `elements` lists the group, `add` is the operation, `zero` the identity.
    Every x in elements^d is tested, INCLUDING x = 0.
    """
    for x in itertools.product(elements, repeat=d):
        m = 0
        for mask in range(1, 1 << d):
            t = zero
            for i in range(d):
                if mask >> i & 1:
                    t = add(t, x[i])
            if t == zero:
                m += 1
        z = sum(1 for v in x if v == zero)
        nz = [v for v in x if v != zero]
        k = len(nz)
        s = 0
        for mask in range(1 << k):
            t = zero
            for i in range(k):
                if mask >> i & 1:
                    t = add(t, nz[i])
            if t == zero:
                s += 1
        if m != 2**z * s - 1:
            return False
    return True


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

    # --- 5. Remark 2.1: no primality, no odd characteristic, no x != 0 ---
    print("5. Remark 2.1 (hypotheses are not load-bearing):")

    # x = 0 is the boundary case: z = d, s = 1, so the formula must return 2^d - 1.
    zero_ok = all(2**d * 1 - 1 == 2**d - 1 for d in range(1, 7))
    for d in (1, 3, 6):
        x = (0,) * d
        assert m_q(x, 5) == 2**d - 1, "every form vanishes at x = 0"
        z, s = z_and_s(x, 5)
        zero_ok &= (z, s) == (d, 1) and m_q(x, 5) == 2**z * s - 1
    ok &= zero_ok
    print(f"     x = 0 (z = d, s = 1 -> 2^d - 1, all forms vanish): {zero_ok}")

    groups = [
        ("Z/2  (characteristic 2)", list(range(2)), lambda a, b: (a + b) % 2, 0, 4),
        ("Z/4  (not a field)", list(range(4)), lambda a, b: (a + b) % 4, 0, 4),
        ("Z/6  (composite, even)", list(range(6)), lambda a, b: (a + b) % 6, 0, 4),
        ("Z/9  (prime power)", list(range(9)), lambda a, b: (a + b) % 9, 0, 3),
        ("(Z/2)^2  (non-cyclic)",
         [(a, b) for a in range(2) for b in range(2)],
         lambda a, b: ((a[0] + b[0]) % 2, (a[1] + b[1]) % 2), (0, 0), 5),
        ("Z/2 x Z/4  (non-cyclic)",
         [(a, b) for a in range(2) for b in range(4)],
         lambda a, b: ((a[0] + b[0]) % 2, (a[1] + b[1]) % 4), (0, 0), 3),
    ]
    for label, els, add, zero, dmax in groups:
        good = all(lemma_holds_over_group(els, add, zero, d)
                   for d in range(1, dmax + 1))
        ok &= good
        print(f"     {label:<26} d = 1..{dmax}, all x incl. 0: {good}")

    print("\nALL CHECKS PASS" if ok else "\nCHECKS FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
