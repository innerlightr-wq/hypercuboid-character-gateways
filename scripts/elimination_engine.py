r"""Symbolic recursive elimination engine for Sigma_S(p).

Object being studied (Part I), in the paper's own notation:
    Sigma_S(p) = sum_{x in F_p^d} chi( prod_{J in S} L_J(x) )
where each L_J is a HOMOGENEOUS linear form (zero-sector representative
form: L_J(x) = sum_{j in J} x_j). More generally the engine works for any
finite list of homogeneous linear forms with INTEGER coefficients (no
constant term), which is the class the multiplicity-1/2 reductions stay
inside of after successive coordinate eliminations (Part III).

Symbolic value representation
------------------------------
A "SymValue" is an exact element of Z[p, e]/(e^2-1), represented as a dict
mapping (e_power_mod2, p_power, pminus1_power) -> integer coefficient. This
exactly captures every term the elimination rules can produce:
    +- e^{0,1} * p^a * (p-1)^b
summed over finitely many such terms (sums arise from the multiplicity-2
hyperplane-coincidence correction, Part III).

An "UNRESOLVED" leaf is returned (instead of a SymValue) when, at some
point in the recursion, every remaining active coordinate has multiplicity
>= 3 in the remaining form list -- Part IV requires NOT inventing a
reduction there; the caller must fall back to direct enumeration for that
residual instance.

Elimination rules implemented (derived and checked by hand in Part II/III
before being coded here; see notes/round2_report.md for the derivations):

  Multiplicity 1 (private coordinate): Sigma_S(p) = 0 exactly. (Lemma,
  Part II -- elementary: fix the other variables, the sum over the private
  coordinate is a sum of chi over a full affine shift of F_p, exactly 0,
  for EVERY fixing of the other variables, hence for the total sum too.)

  Multiplicity 2: coordinate x_k occurs (with nonzero integer coefficients
  a, b) in exactly two forms L_a = a*x_k + A(y), L_b = b*x_k + B(y) (A, B
  homogeneous linear in the other coordinates y). Then, EXACTLY:
      sum_{x_k} chi(L_a L_b) = chi(a*b) * [ -1 + p * 1{A(y) = B(y)} ]
  (classical fact: sum_x chi((x-r1)(x-r2)) = -1 if r1 != r2, else p-1;
  here r1 = -A(y)/a, r2 = -B(y)/b, and A(y)=B(y) <=> b*A(y) = a*B(y) after
  clearing denominators, matching r1=r2 up to the nonzero scalars a,b not
  affecting the comparison -- checked explicitly in the code, not assumed).
  Writing D(y) = b*A(y) - a*B(y) (homogeneous linear in y, since A,B are):
    - If D is NOT identically zero, its zero locus H = {D(y)=0} is a
      genuine linear hyperplane in y-space (a nonzero homogeneous linear
      form always has a full-codimension-1 zero set -- never empty, never
      everything). Then
        Sigma_S(p) = -chi(ab) * Sigma_{S'}(p)
                     + p * chi(ab) * Sigma_{S'}(p) restricted to H,
      where S' = S \ {L_a, L_b} in the (d-1)-dim y-space, and the
      H-restricted term is computed by solving D(y)=0 for one variable
      (coefficient +-1, since D's coefficients are differences of the
      original 0/1-type coefficients -- see notes) and substituting,
      landing in a (d-2)-dim space with a new list of homogeneous linear
      forms (still integer-coefficient, so the SAME engine applies
      recursively).
    - If D IS identically zero (only possible if L_a, L_b were literally
      proportional on the y-part -- checked explicitly; for the zero
      sector's pairwise-non-associate forms this does not occur, but the
      code does not assume it and handles it if it ever does):
        Sigma_S(p) = chi(ab) * (p-1) * Sigma_{S'}(p)
      (single term, no hyperplane split, since r1=r2 for every y).

  Multiplicity >= 3 for every remaining coordinate: UNRESOLVED, returned
  as-is (list of forms + dimension) for direct numeric evaluation.
"""

from __future__ import annotations

import itertools
from collections import defaultdict
from dataclasses import dataclass, field
from fractions import Fraction
from typing import Union

import numpy as np


# ---------------------------------------------------------------------
# Symbolic values in Z[p,e]/(e^2-1)
# ---------------------------------------------------------------------

def char_arg_of(x) -> int:
    """Canonical integer character-argument for an int or Fraction x.
    chi(num/den) = chi(num)*chi(den) = chi(num*den) mod p (den invertible
    mod p generically), so a Fraction's numerator*denominator is exactly
    the right integer to feed chi at evaluation time."""
    if isinstance(x, Fraction):
        return x.numerator * x.denominator
    return int(x)


def _squarefree_part(n: int) -> int:
    """Reduce an integer character-argument to its squarefree part (times
    sign), since chi(c) = chi(squarefree part of c) for c coprime to p:
    chi(k^2 * r) = chi(k)^2 chi(r) = chi(r) whenever chi(k)!=0. This keeps
    the symbolic character argument canonical and small."""
    if n == 0:
        return 0
    sign = -1 if n < 0 else 1
    n = abs(n)
    d = 2
    while d * d <= n:
        while n % (d * d) == 0:
            n //= d * d
        d += 1
    return sign * n


class SymValue:
    """dict: (chi_arg, p_power, pm1_power) -> integer coefficient.

    chi_arg is an integer (canonicalized to its signed squarefree part);
    the term represents  coeff * chi(chi_arg) * p^p_power * (p-1)^pm1_power,
    where chi(1)=1 (chi_arg=1 means "no character factor"). chi is the
    Legendre symbol mod the evaluation prime p; multiplicativity of chi
    means ANY product of chi(a)*chi(b)*... collapses to chi(a*b*...), so a
    single integer chi_arg per term suffices -- no need for a separate
    symbol per small constant (this generalizes the Round-2-Part-III
    special case chi(-1) found in Round 1, to chi(c) for whatever integer
    c actually arises from non-unit coefficients).
    """

    __slots__ = ("terms",)

    def __init__(self, terms: dict | None = None):
        self.terms = defaultdict(int)
        if terms:
            for k, v in terms.items():
                self.terms[k] += v
        self._clean()

    def _clean(self):
        self.terms = defaultdict(int, {k: v for k, v in self.terms.items() if v != 0})

    @staticmethod
    def zero() -> "SymValue":
        return SymValue()

    @staticmethod
    def term(sign: int, chi_arg: int, p_power: int, pm1_power: int) -> "SymValue":
        return SymValue({(_squarefree_part(chi_arg), p_power, pm1_power): sign})

    def __add__(self, other: "SymValue") -> "SymValue":
        out = SymValue(dict(self.terms))
        for k, v in other.terms.items():
            out.terms[k] += v
        out._clean()
        return out

    def scale(self, sign: int, chi_arg_mult: int, p_power_shift: int = 0,
              pm1_power_shift: int = 0) -> "SymValue":
        out = {}
        for (ca, p_, m), c in self.terms.items():
            new_ca = _squarefree_part(ca * chi_arg_mult) if chi_arg_mult != 1 else ca
            key = (new_ca, p_ + p_power_shift, m + pm1_power_shift)
            out[key] = out.get(key, 0) + sign * c
        return SymValue(out)

    def evaluate(self, p: int) -> int:
        def chi(c, p):
            c %= p
            if c == 0:
                return 0
            return 1 if pow(c, (p - 1) // 2, p) == 1 else -1

        total = 0
        for (ca, p_pow, m_pow), c in self.terms.items():
            chi_val = chi(ca, p) if ca != 1 else 1
            total += c * chi_val * (p ** p_pow) * ((p - 1) ** m_pow)
        return total

    def pretty(self) -> str:
        if not self.terms:
            return "0"
        parts = []
        for (ca, p_pow, m_pow), c in sorted(self.terms.items(), key=lambda kv: (abs(kv[0][0]), kv[0])):
            s = ""
            if c != 1 or (ca == 1 and p_pow == 0 and m_pow == 0):
                s += f"{c}"
            elif c == -1:
                s += "-"
            if ca != 1:
                s += f"*chi({ca})"
            if p_pow:
                s += f"*p^{p_pow}" if p_pow != 1 else "*p"
            if m_pow:
                s += f"*(p-1)^{m_pow}" if m_pow != 1 else "*(p-1)"
            parts.append(s.lstrip("*"))
        return " + ".join(parts).replace("+ -", "- ")


ONE = SymValue.term(1, 1, 0, 0)


# ---------------------------------------------------------------------
# Forms: list of integer coefficient vectors (homogeneous linear forms)
# ---------------------------------------------------------------------

Forms = tuple[tuple[int, ...], ...]


def multiplicities(forms: Forms, d: int) -> list[int]:
    m = [0] * d
    for f in forms:
        for k in range(d):
            if f[k] != 0:
                m[k] += 1
    return m


def drop_coord(forms: Forms, k: int) -> Forms:
    return tuple(tuple(c for i, c in enumerate(f) if i != k) for f in forms)


def try_level2_dependency(forms: Forms, d: int) -> Union["SymValue", None]:
    """Round-3 Level-2 rule: |forms| == d+1, rank(forms) == d (corank
    exactly 1), d odd. Computes the PRIMITIVE integer dependency relation
    sum_i c_i * forms[i] = 0 via sympy's exact nullspace + denominator
    clearing + gcd reduction (never hard-coded), and returns
        chi(prod_i c_i)^{(d-1)/2} * p^{(d-1)/2} * (p-1).
    Returns None if the preconditions don't hold (falls back to UNRESOLVED
    upstream, or -- in principle -- a future rule)."""
    if len(forms) != d + 1 or d % 2 == 0:
        return None
    import sympy

    M = sympy.Matrix([list(f) for f in forms])
    if M.rank() != d:
        return None  # not corank-1 (or forms not even rank d -- shouldn't happen)
    ns = M.T.nullspace()
    if len(ns) != 1:
        return None
    v = ns[0]
    L = 1
    for x in v:
        L = sympy.ilcm(L, sympy.Rational(x).q)
    v_int = [int(x * L) for x in v]
    g = 0
    for x in v_int:
        g = sympy.igcd(g, x)
    if g != 0:
        v_int = [x // g for x in v_int]
    prod_c = 1
    for c in v_int:
        prod_c *= c
    exponent = (d - 1) // 2
    chi_arg = prod_c if exponent % 2 == 1 else 1
    return SymValue.term(1, chi_arg, exponent, 1)


def try_gateway_e_complementary_pairs(forms: Forms, d: int) -> Union["SymValue", None]:
    """Round-4 Gateway E: forms partition perfectly into k complementary
    pairs w.r.t. the FULL current coordinate set {0,...,d-1} (each form is
    a 0/1 vector; its partner is the bitwise complement, i.e. Q - form
    where Q is the all-ones vector), AND d == k+1 exactly (one extra
    independent "Q" dimension beyond the k pair-representative
    coordinates -- this is the precise condition actually derived and
    verified this round; NOT extrapolated to d>k+1).

    Derivation (notes/round4_report.md): substituting u_i = one
    representative of pair i and Q = sum of all coordinates (an invertible
    change of variables when the k representatives + Q are linearly
    independent, checked explicitly) turns the product of all 2k forms
    into prod_i [u_i * (Q-u_i)], which separates completely once Q is
    fixed. Using the classical fact sum_u chi(u*(Q-u)) = -chi(-1) if Q!=0,
    chi(-1)*(p-1) if Q=0 (itself a restatement of the multiplicity-2
    identity, Part III of Round 2), summing over Q gives EXACTLY:
        Sigma_S(p) = chi(-1)^k * (p-1) * [ (-1)^k + (p-1)^{k-1} ]
    Sanity checks built into the derivation: k=1 gives exactly 0 (a
    complementary PAIR covering all coordinates once each is exactly a
    private-coordinate/Level-0 situation -- the general formula correctly
    reduces to the already-known case); k=2 gives plain p*(p-1) (matching
    Round 1's (0,1,4,5)-type example, previously reached only via the
    pairwise Level-1 recursion -- an independent cross-check, not assumed).
    """
    m = len(forms)
    if m % 2 != 0:
        return None
    k = m // 2
    if d != k + 1:
        return None
    Q = tuple(1 for _ in range(d))
    remaining = list(forms)
    reps = []
    used = [False] * m
    forms_list = list(forms)
    for i in range(m):
        if used[i]:
            continue
        fi = forms_list[i]
        complement = tuple(Q[t] - fi[t] for t in range(d))
        found = None
        for j in range(i + 1, m):
            if not used[j] and forms_list[j] == complement:
                found = j
                break
        if found is None:
            return None  # not a perfect complementary-pair partition
        used[i] = True
        used[found] = True
        reps.append(fi)
    if len(reps) != k:
        return None
    # verify reps + Q independent (rank k+1), using exact rational rank
    import sympy

    M = sympy.Matrix(reps + [list(Q)])
    if M.rank() != k + 1:
        return None
    chi_pow_arg = -1 if k % 2 == 1 else 1
    term1 = SymValue.term((-1) ** k, chi_pow_arg, 0, 1)
    term2 = SymValue.term(1, chi_pow_arg, 0, k)
    return term1 + term2


def try_gateway_f_full_rank_omit_one(forms: Forms, d: int) -> Union["SymValue", None]:
    """Round-5 Gateway F: S = { Q - x_i : i = 0,...,d-1 } exactly (every
    coordinate omitted by exactly one form, all d forms present), for
    d == 4 SPECIFICALLY (the only case actually derived this round -- see
    notes/round5_report.md for the full fix-Q, nested-multiplicity-2
    derivation). Verified: Sigma_S(p) = 0 EXACTLY for every prime p != 3
    (p=3 is a genuine, separately-computed exception -- NOT represented by
    the SymValue this function returns, so callers evaluating at p=3 will
    get the wrong number; this is documented, not silently wrong within
    the derived scope).

    Structural detection (not hard-coded to specific coordinate labels):
    checks that |forms| == d, that each form equals (all-ones vector) -
    (standard basis vector e_i) for some permutation of i's covering every
    coordinate exactly once, i.e. forms == {Q - x_i} as a SET regardless of
    order.
    """
    if d != 4 or len(forms) != d:
        return None
    Q = tuple(1 for _ in range(d))
    expected = set()
    for i in range(d):
        e_i = tuple(1 if t == i else 0 for t in range(d))
        expected.add(tuple(Q[t] - e_i[t] for t in range(d)))
    if set(forms) != expected:
        return None
    return SymValue.zero()


@dataclass
class EliminationResult:
    value: SymValue | None  # None if unresolved
    unresolved: list[tuple[Forms, int]] = field(default_factory=list)
    trace: list[str] = field(default_factory=list)


def eliminate(forms: Forms, d: int, order_hint: list[int] | None = None,
              depth: int = 0, max_depth: int = 30) -> EliminationResult:
    """Recursively eliminate multiplicity-1 and multiplicity-2 coordinates.

    order_hint: optional explicit priority list of coordinate indices to
    prefer when multiple multiplicity-2 choices exist (used for the
    confluence test, Part VII). If None, picks the first (lowest index)
    available multiplicity-2 coordinate.
    """
    if depth > max_depth:
        return EliminationResult(value=None, unresolved=[(forms, d)],
                                  trace=["max depth exceeded"])
    if len(forms) == 0:
        # empty product, sum over F_p^d of chi(1) = p^d
        return EliminationResult(value=SymValue.term(1, 1, d, 0), trace=["empty S -> p^d"])
    if d == 0:
        # no variables left but forms nonempty: forms must be the zero form
        # (all coefficients gone) -- chi(prod of nonzero constants) is a
        # fixed +-1, times the (single, x-less) point. Constants here are
        # always taken to be 0 in our homogeneous reduction (a form with no
        # coordinates left has coefficient vector of length 0, i.e. the
        # ZERO form) so chi(0)=0 -> the whole sum is 0. Flag as such.
        return EliminationResult(value=SymValue.zero(), trace=["d=0, degenerate zero form -> 0"])

    mult = multiplicities(forms, d)
    trace = [f"depth={depth} d={d} |S|={len(forms)} mult={mult}"]

    # Multiplicity-1 check (any coordinate with mult==1) -> exact 0.
    for k in range(d):
        if mult[k] == 1:
            trace.append(f"coord {k} has multiplicity 1 -> Sigma_S=0 exactly")
            return EliminationResult(value=SymValue.zero(), trace=trace)

    # Multiplicity-2 candidates.
    candidates = [k for k in range(d) if mult[k] == 2]
    if not candidates:
        # Level-2 rule (Round 3, Part IV/VI): minimal (corank-1) linear
        # dependency, |forms| == d+1 with rank(forms) == d exactly. Derived
        # and verified this round (see notes/round3_report.md): for a
        # primitive integer dependency sum_i c_i*L_i = 0,
        #   Sigma_S(p) = chi(prod_i c_i)^{(d-1)/2} * p^{(d-1)/2} * (p-1)
        # This is STRUCTURAL (computed from the actual coefficient vectors
        # every time, never hard-coded to a specific example) but is only
        # applied when d is ODD (so (d-1)/2 is an integer) and the corank is
        # EXACTLY 1 -- broader coranks (e.g. |S|=d+2 with a 2-dim dependency
        # space) are NOT covered and are left UNRESOLVED, matching what was
        # actually derived and verified, not extrapolated further.
        level2 = try_level2_dependency(forms, d)
        if level2 is not None:
            trace.append(f"Level-2 minimal-dependency rule applied: {level2.pretty()}")
            return EliminationResult(value=level2, trace=trace)
        gate_e = try_gateway_e_complementary_pairs(forms, d)
        if gate_e is not None:
            trace.append(f"Gateway-E complementary-pairs rule applied: {gate_e.pretty()}")
            return EliminationResult(value=gate_e, trace=trace)
        gate_f = try_gateway_f_full_rank_omit_one(forms, d)
        if gate_f is not None:
            trace.append(f"Gateway-F omit-one-coordinate rule applied: {gate_f.pretty()} "
                         "(derived/verified for d=4 only; p=3 is a known exception, NOT "
                         "covered by this symbolic value -- see notes/round5_report.md)")
            return EliminationResult(value=gate_f, trace=trace)
        trace.append("no multiplicity<=2 coordinate and no Level-2/Gateway-E/F rule applies -> UNRESOLVED")
        return EliminationResult(value=None, unresolved=[(forms, d)], trace=trace)

    if order_hint:
        pick_list = [k for k in order_hint if k in candidates] + [
            k for k in candidates if k not in order_hint
        ]
        k = pick_list[0]
    else:
        k = candidates[0]

    idx_ab = [i for i, f in enumerate(forms) if f[k] != 0]
    assert len(idx_ab) == 2
    ia, ib = idx_ab
    fa, fb = forms[ia], forms[ib]
    a, b = fa[k], fb[k]
    A = tuple(c for i, c in enumerate(fa) if i != k)
    B = tuple(c for i, c in enumerate(fb) if i != k)
    rest_forms = tuple(f for i, f in enumerate(forms) if i not in (ia, ib))
    rest_reduced = drop_coord(rest_forms, k)
    d2 = d - 1

    # D(y) = b*A(y) - a*B(y)
    D = tuple(b * A[i] - a * B[i] for i in range(d2))
    # chi(ab) is tracked EXACTLY as a symbolic character argument (the
    # integer a*b itself, canonicalized to its squarefree part at
    # evaluation time) -- this is fully general, no restriction to a,b in
    # {+-1} is needed: chi is multiplicative and well-defined for any
    # nonzero integer argument, evaluated mod the prime at the end.
    chi_ab_arg = a * b

    trace.append(f"eliminating coord {k}: forms idx {ia},{ib} a={a} b={b} "
                 f"A={A} B={B} D=b*A-a*B={D}")

    if all(c == 0 for c in D):
        trace.append("D identically 0 -> coincide-always branch: "
                     "Sigma_S = chi(ab)*(p-1)*Sigma_S'")
        sub = eliminate(rest_reduced, d2, order_hint, depth + 1, max_depth)
        if sub.value is None:
            return EliminationResult(value=None, unresolved=sub.unresolved,
                                      trace=trace + sub.trace)
        val = sub.value.scale(1, char_arg_of(chi_ab_arg), 0, 1)  # * chi(ab) * (p-1)^1
        return EliminationResult(value=val, trace=trace + sub.trace)

    # D nonzero: genuine hyperplane. Solve for one coordinate exactly using
    # Fraction arithmetic (works for ANY nonzero D[piv], not just +-1 --
    # this generalizes beyond the Round-2 first draft, which only handled
    # unit pivots; a non-unit pivot was found to occur in practice, see
    # notes/round2_report.md).
    piv = next(i for i in range(d2) if D[i] != 0)
    inv_piv = Fraction(1) / D[piv]
    # y_piv = -(1/D[piv]) * sum_{i!=piv} D[i]*y_i

    # Term 1: -chi(ab) * Sigma_{S'}(p)  [S' = rest_reduced, dim d2]
    sub1 = eliminate(rest_reduced, d2, order_hint, depth + 1, max_depth)

    # Term 2: p*chi(ab) * Sigma_{S' restricted to H}(p), dim d2-1
    # Substitute y_piv = -inv_piv*sum_{i!=piv} D[i]*y_i into every form in
    # rest_reduced (exact Fraction arithmetic), then drop coordinate piv.
    def substitute(f) -> tuple:
        coeff_piv = f[piv]
        new = list(f)
        if coeff_piv != 0:
            for i in range(d2):
                if i == piv:
                    continue
                new[i] = new[i] + coeff_piv * (-inv_piv * D[i])
            new[piv] = 0
        return tuple(new)

    restricted = tuple(substitute(f) for f in rest_reduced)
    restricted_dropped = drop_coord(restricted, piv)
    d3 = d2 - 1

    sub2 = eliminate(restricted_dropped, d3, order_hint, depth + 1, max_depth)

    if sub1.value is None or sub2.value is None:
        unresolved = (sub1.unresolved if sub1.value is None else []) + (
            sub2.unresolved if sub2.value is None else []
        )
        return EliminationResult(value=None, unresolved=unresolved,
                                  trace=trace + sub1.trace + sub2.trace)

    ca = char_arg_of(chi_ab_arg)
    term1 = sub1.value.scale(-1, ca, 0, 0)
    term2 = sub2.value.scale(1, ca, 1, 0)  # * p * chi(ab)
    total = term1 + term2
    return EliminationResult(value=total,
                              trace=trace + ["-- term1 (no-coincide) --"] + sub1.trace +
                              ["-- term2 (coincide, *p) --"] + sub2.trace)
