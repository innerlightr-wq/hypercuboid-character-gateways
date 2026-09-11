"""Round 13: compare S(p) against the LMFDB weight-3 CM newform 8.3.d.a
(level 8, nebentypus 8.d, CM by Q(sqrt(-2))).

Raw Hecke traces fetched via the LMFDB API (NOT via an AI-summarized
webfetch -- an earlier summarized fetch was found to contain silent
transcription errors for p=59,67,83,89,97; the raw API JSON is used here
and is the trustworthy source):

    curl -s "https://www.lmfdb.org/api/mf_newforms/?level=8&weight=3&_format=json&_fields=label,traces"

Main finding verified here: S(p) = chi(-1)*(a_p(f) + p) exactly, for
every prime tested, where a_p(f) is 8.3.d.a's Hecke eigenvalue.
"""
import json
import sys
from pathlib import Path

import sympy

sys.path.insert(0, str(Path(__file__).parent))
from core import ZeroSectorSystem, chi_columns, sigma_S  # noqa: E402


def chi(a, p):
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def a_p_E(p):
    """Trace of Frobenius for E: y^2=x^3+4x^2+2x (CM by Z[sqrt(-2)])."""
    s = sum(chi((x**3 + 4 * x**2 + 2 * x) % p, p) for x in range(p))
    return -s


def g(t, p):
    return sum(chi(x * (x + 1) * (x + t) % p, p) for x in range(p))


def S_of(p):
    return sum(chi(t * (t + 1) % p, p) * g(t, p) for t in range(p))


def a_p_f_derived(p):
    """From the Sym^2 decomposition: a_p(f) = a_p(E)^2 - p(1+chi(-2))."""
    return a_p_E(p)**2 - p * (1 + chi(-2, p))


if __name__ == "__main__":
    traces_path = Path("/tmp/newform_8_3_d_a.json")
    if not traces_path.exists():
        raise SystemExit(
            "Run: curl -s 'https://www.lmfdb.org/api/mf_newforms/"
            "?level=8&weight=3&_format=json&_fields=label,traces' "
            "-o /tmp/newform_8_3_d_a.json"
        )
    data = json.load(open(traces_path))
    traces = data["data"][0]["traces"]

    sys4 = ZeroSectorSystem.build(4)
    S_I = (0, 1, 2, 3, 4, 5)

    print(f"{'p':>4}{'p%8':>4}{'a_p(f) LMFDB':>13}{'a_p(f) derived':>15}"
          f"{'match1':>7}{'S(p)':>7}{'chi(-1)(af+p)':>14}{'match2':>7}")
    all_ok = True
    for p in sympy.primerange(3, 150):
        if p > len(traces):
            continue
        af_lmfdb = traces[p - 1]
        af_derived = a_p_f_derived(p)
        Sp = S_of(p)
        cm1 = chi(-1, p)
        pred = cm1 * (af_lmfdb + p)
        m1 = af_lmfdb == af_derived
        m2 = pred == Sp
        all_ok &= m1 and m2
        print(f"{p:>4}{p%8:>4}{af_lmfdb:>13}{af_derived:>15}{str(m1):>7}"
              f"{Sp:>7}{pred:>14}{str(m2):>7}")
    print("\nALL MATCH (independent LMFDB data):", all_ok)
