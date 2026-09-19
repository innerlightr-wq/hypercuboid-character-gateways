"""Trace-form coefficients of the Galois orbit 16.3.f.a, used only as a
deliberate *wrong-newform* falsification check in class3_round2_falsification.py
(Direction 1: "the other newform found at level 16, weight 3 must NOT match
T(p)"). This is genuinely external data -- unlike 16.3.c.a = eta^6(4z)
(see newform_16_3_c_a.py), 16.3.f.a has no elementary closed-form
generating function available to this project: it is a dimension-6
Galois orbit (character orbit 16.f, order 4), and the values below are
the *trace form* a_n = Tr_{K/Q}(lambda(T_n)) over its degree-6 Hecke
field K, not the eigenvalues of a single rational newform.

Provenance
----------
Source: LMFDB, label 16.3.f.a.
    https://www.lmfdb.org/ModularForm/GL2/Q/holomorphic/16/3/f/a/
Retrieved via the public LMFDB API:
    https://www.lmfdb.org/api/mf_newforms/?level=16&weight=3&char_orbit_label=f&_format=json
Retrieval date: 2026-09-19.
Field: the API response's own `traces` array, entries 1..150 (a_1..a_150),
truncated here from LMFDB's full 1000-entry array to the minimum needed
by the consuming script (which only ever indexes primes up to 41), plus
headroom. No value below was computed, edited, or estimated by this
project; each is the API's own reported integer, copied verbatim.

If more coefficients are ever needed, re-query the URL above and extend
`traces_f` in the same way -- do not extrapolate or invent values.
"""

N = 150

traces_f: list[int] = [
    6, -2, -2, -8, -2, -8, -4, 4, 0, 36, -18, 52, -2, 12, 0, -40, -4, -74,
    30, -84, -20, -52, 60, 48, 0, 96, 64, 56, -18, 52, 0, 8, -4, -76, -100,
    -52, 46, 40, -196, 40, 0, -24, -114, 20, 66, 28, 0, -24, -46, 46, 156,
    100, 78, 32, 252, -168, 0, -176, 206, -160, 30, -144, 0, 64, 12, 196,
    -226, 112, -116, -16, -260, 52, 0, -92, -238, -188, -212, -84, 0, 232,
    86, 304, 318, 232, -212, 268, 444, -8, 0, -160, 188, -168, -32, 48, 0,
    -80, -4, 10, -226, 316, 142, -256, -388, -400, 0, -124, -338, -80,
    366, -308, 0, -320, 108, 84, 156, -204, 382, -84, 120, 264, 0, 160,
    224, 128, 96, 148, 0, 432, -36, -116, -226, -176, -244, 552, -320,
    248, 0, 104, -50, 264, -608, 604, 0, 0, -148, -552, 26, -228, -418,
    -428,
]

assert len(traces_f) == N, f"expected {N} entries, got {len(traces_f)}"
