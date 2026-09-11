# Hypercuboid exploration — Round 3 working notes

## The Level-2 (minimal corank-1 dependency) rule

For a set S of d+1 representative forms in F_p^d with rank(S) = d exactly
(corank 1), let c_1,...,c_{d+1} be the primitive integer coefficients of
the (unique up to scalar) linear dependency sum_i c_i L_i = 0 (computed via
exact nullspace + denominator-clearing + gcd reduction, never guessed).
**Verified** (not assumed): for d ODD,
    Sigma_S(p) = chi(prod_i c_i)^{(d-1)/2} * p^{(d-1)/2} * (p-1)
exactly.

Verification: ALL 35 rank-3 (corank-1), |S|=4 subsets of the n=4 (d=3)
system match this formula exactly across all 16 tested primes, zero
mismatches (`results/classify_n4.json`, re-run after adding the rule).
Separately confirmed at d=5 (n=6, one hand-built example: 5 singleton
forms + the full-sum form, dependency (1,1,1,1,1,-1)): matches p^2(p-1)
exactly at p=5,7,11,13, with the character factor correctly trivializing
(exponent (d-1)/2=2 is even, so chi(-1)^2=1, matching the observed
sign-independent p^2(p-1) with no chi(-1) dependence at any tested prime,
including p=7,11 where chi(-1)=-1).

**Explains the Round-2 chi(-2) mystery exactly**: (3,4,5,6) at n=4 has
dependency L3+L4+L5-2*L6=0, i.e. c=(1,1,1,-2), product=-2, giving
chi(-2)*p^1*(p-1) — matching Round 2's pattern-matched-but-undevired
formula precisely, now with a full derivation and general rule instead of
a single fitted example.

**Parity/scope boundary (found, not assumed):** the rule requires d ODD
(so (d-1)/2 is an integer exponent) AND corank exactly 1 (|S|=d+1). At
n=5 (d=4, even), corank-1 sets have odd size d+1=5, hence are already
covered (trivially zero) by the paper's own odd-cardinality vanishing —
so the Level-2 rule contributes **nothing new at n=5**. This was checked,
not assumed: n=5's two genuine dense unresolved cores were inspected and
found to be corank 2 ("all 6 pairs", rank 4, corank 2) and corank 0 ("all
4 triples", rank 4, |S|=4=d exactly, no dependency at all — a distinct
structural situation, not covered by any rule derived this round).

## New n=4 classification (post Level-2)

56/63 (88.9%) resolved, up from 55/63. Zero direct-enumeration
mismatches, zero confluence failures (re-run, unchanged from Round 2's
22 tested multi-order cases). The 7 remaining unresolved subsets are
EXACTLY the seven |S|=6 subsets (all corank 3 in d=3 space) — Level 2
does not touch |S|=6 (only |S|=d+1=4 qualifies).

## Confluence

**Semantic confluence: provable, and essentially immediate** given that
every individual rule (mult-1 vanishing, mult-2 identity, Level-2
dependency formula) was independently derived as an EXACT algebraic
identity (not a heuristic) — since Sigma_S(p) is a single fixed number for
each (S,p), any two fully-correct derivations of it must agree, simply
because both equal the same number. This is not a deep separate theorem;
it follows from the soundness of each individual rule.

**Syntactic confluence (local confluence of the rewrite system itself,
independent of the semantic target): NOT proven this round.** Only
checked computationally (22/22 n=4 cases with multiple valid first moves,
0 disagreements in the final symbolic expression). A genuine proof would
need a local-confluence (diamond property) argument for the case where two
different multiplicity-2 coordinates are both eligible at once, combined
with the obvious termination (dimension strictly decreases each step) via
Newman's lemma. Flagged as a natural, well-scoped Round-4 target — not
claimed as proven.

## Finer invariant beyond multiplicity vectors (Part VIII)

The multiplicity vector alone is insufficient (Round 2 finding, reconfirmed).
The invariant that DOES cleanly organize the classification, as far as
this round's evidence goes: **the corank of the incidence matrix (and,
when corank=1, the primitive dependency coefficients themselves)**. This
is well-defined, exactly computable (sympy nullspace + gcd reduction), and
directly explains every case tested: mult-1 existence is itself a
(trivial) rank/dependency fact; the mult-2 recursion's D-hyperplane
structure is a corank argument one level down; and Level 2 is corank-1 at
the top level. Cycle structure / 2-core graph language was considered but
not needed — the pure linear-algebra invariant (corank + dependency
coefficients) already explains everything found.

## Level hierarchy assessment (Part X)

LEVEL 0 (mult-1) and LEVEL 2 (corank-1, d odd) are each a single, clean
algebraic condition. LEVEL 1 (pairwise peelable) is really "LEVEL 0 or
LEVEL 2 reachable via a sequence of mult-2 reductions" — mechanistically
distinct from Level 2 (recursive vs. one-shot) but not a separate
algebraic PHENOMENON. LEVEL 3 ("unresolved") is **not yet a single clean
class** — this round found it splits into at least two structurally
different sub-cases (corank-2 dense cores like "all 6 pairs" at n=5; and
full-rank, no-dependency-at-all cores like "all 4 triples" at n=5, or the
seven corank-3 |S|=6 cases at n=4). The hierarchy is mathematically
meaningful through Level 2; Level 3 remains a procedural catch-all, not
(yet) a mathematical category.
