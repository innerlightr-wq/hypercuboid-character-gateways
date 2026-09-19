"""Hecke eigenvalues a_p of the weight-3 CM newform 16.3.c.a, computed
from scratch -- no external data, no network access, no cached files.

Provenance and background
--------------------------
The manuscript (class_iii/manuscript/class3_hypercuboid_k3.tex, Section
"Identifying the candidate newform", label sec:CM) identifies the
transcendental-trace-governing newform as

    f(z) = eta^6(4z) = q * prod_{n>=1} (1 - q^{4n})^6,  LMFDB label 16.3.c.a,

a classical identity: eta^6(4z) is the weight-3, level-16, CM-by-Q(i)
newform, and the eta-product presentation is Ahlgren-Ono-Penniston's own
(\\cite{AOP2002} in the manuscript's bibliography), not new to this
project. Because the coefficients a_n of f are exactly the coefficients
of this explicit power series -- a closed-form definition, not a lookup
-- they can be recomputed deterministically by anyone, from nothing but
this docstring's formula, with a computer algebra system or a dozen
lines of Python. That is what this module does.

Earlier research rounds in this project (see class_iii/notes/ and
explorations/) originally cross-checked these coefficients against the
LMFDB API record for 16.3.c.a
(https://www.lmfdb.org/ModularForm/GL2/Q/holomorphic/16/3/c/a/,
retrieved during the September 2026 research rounds) and cached that
API response locally as /tmp/level16_weight3.json for reuse across
several verification scripts. That cache was session-local scratch
data -- never part of this repository, never committed, and not
needed: the eta-product identity above already pins down every
coefficient exactly, so recomputing them here removes the external
dependency without weakening any check. Consumers of this module get
identical values to what the LMFDB record reports (this was verified
directly, coefficient by coefficient, against the LMFDB page cited
above, before this module replaced the /tmp-file lookups in the
scripts that use it).

Interface
---------
`traces_c` is a 1-indexed-via-`traces_c[p-1]` list of coefficients
a_1, a_2, a_3, ... up to `MAX_N`, matching the indexing convention
already used throughout this directory's scripts (`traces_c[p-1]`
gives a_p). `a_p(p)` is the same lookup as a function.
"""
from __future__ import annotations

from math import comb

MAX_N = 200


def _eta6_4z_coefficients(n_max: int) -> list[int]:
    """Coefficients a_1..a_{n_max} of eta(4z)^6 = q*prod_{n>=1}(1-q^{4n})^6,
    via exact integer polynomial arithmetic (no floating point, no
    external library)."""
    # Build prod_{n>=1} (1 - q^{4n})^6 truncated mod q^{n_max}, then
    # shift by one power of q (the leading q in eta(4z) = q^{1/24}*prod...
    # here eta(4z)^6 carries the overall factor q^{6*4/24}=q^1).
    N = n_max  # we need coefficients of the *product* up to degree n_max-1,
    # then the q-shift brings them to a_1..a_{n_max}.
    cur = [0] * (N + 1)
    cur[0] = 1
    n = 1
    while 4 * n <= N:
        factor = [0] * (N + 1)
        for k in range(7):
            e = 4 * n * k
            if e > N:
                break
            factor[e] += (-1) ** k * comb(6, k)
        nxt = [0] * (N + 1)
        for i, ai in enumerate(cur):
            if ai == 0 or i > N:
                continue
            for j, bj in enumerate(factor):
                if bj == 0 or i + j > N:
                    continue
                nxt[i + j] += ai * bj
        cur = nxt
        n += 1
    coeffs = [0] * (N + 2)
    for i, c in enumerate(cur):
        if i + 1 <= N + 1:
            coeffs[i + 1] = c
    return coeffs  # coeffs[k] = a_k, for k = 1..n_max


_coeffs = _eta6_4z_coefficients(MAX_N)

# traces_c[p-1] == a_p, matching every existing script's indexing.
traces_c: list[int] = _coeffs[1:]


def a_p(n: int) -> int:
    """The n-th Hecke eigenvalue / q-expansion coefficient a_n of
    f = eta^6(4z) = 16.3.c.a."""
    return _coeffs[n]


if __name__ == "__main__":
    # Self-check against the values quoted in the manuscript's Section
    # "Identifying the candidate newform":
    #   f = q - 6q^5 + 9q^9 + 10q^13 - 30q^17 + 11q^25 + ...
    expected = {1: 1, 5: -6, 9: 9, 13: 10, 17: -30, 25: 11}
    for n, val in expected.items():
        got = a_p(n)
        status = "OK" if got == val else "MISMATCH"
        print(f"a_{n} = {got} (expected {val}) [{status}]")
        assert got == val, f"a_{n}: got {got}, expected {val}"
    print(f"All {len(expected)} manuscript-quoted coefficients match.")
    print(f"traces_c holds a_1..a_{MAX_N} ({len(traces_c)} values).")
