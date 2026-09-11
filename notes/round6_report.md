# Hypercuboid exploration — Round 6 working notes

## Part I — Gateway F baseline reproduced

Independently re-derived (not copied) the d=4 result via the fix-Q,
nested-multiplicity-2 argument; re-verified fiber values at p=5,7,11,13
and Sigma_S(3)=18. Matches Round 5 exactly. Not altered.

## Part IV — General S_d = {Q-x_1,...,Q-x_d}

**Odd d: trivial.** |S_d|=d odd => Sigma_d(p)=0 for EVERY prime, via the
paper's own Prop 6.2 (odd-cardinality homogeneous vanishing) -- not a
Gateway-F phenomenon at all. Checked d=3,5 computationally as a sanity
confirmation only.

**Even d: computationally verified pattern.**

| d | d-1 | exceptional prime(s) found | value at exceptional prime |
|---|---|---|---|
| 2 | 1 | none (trivial mult-1 case) | -- |
| 4 | 3 | p=3 | 18 |
| 6 | 5 | p=5 | 500 |
| 8 | 7 | none found among {3,5} tested (7^8 too large to brute-force this round) | -- |
| 10 | 9=3^2 | p=3 | -486 |

Tested primes with NO exception, for each d: d=4 (5,7,11,13,17), d=6
(3,7,11,13,17), d=8 (3,5), d=10 (5; p=7 attempted, too slow to complete).

**Conjectural pattern (COMPUTATIONALLY VERIFIED for the cases above, NOT
proved for general d):** for even d, Sigma_d(p)=0 for every prime p that
does not divide (d-1), and Sigma_d(p) != 0 at (at least some) primes
dividing (d-1). The d=10 case (d-1=9=3^2, composite) is the most
informative data point: it shows the exceptional-prime set is governed by
**prime factors of (d-1)**, not simply "p=d-1" (which would be meaningless
once d-1 is composite) -- p=3 (a proper factor of 9) is exceptional, while
p=5 (not a factor of 9) is not.

**Mechanistic root (PROVED for d=4, CONJECTURAL for general even d):** in
the d=4 derivation, eliminating the fiber's coupling variable twice
(nested multiplicity-2 elimination) produces a coincidence condition that
reduces to exactly "(d-1)*Q=0" (concretely "3Q=0" at d=4). This is
p-divides-(d-1), matching the data exactly at d=4,6,10. The general-d
nested recursion was NOT fully carried out symbolically this round (it
would need tracking a growing chain of substitutions); the pattern is
reported as a strongly-supported conjecture with a verified mechanism at
one specific depth (d=4), not a general proof.

## Part V — Gateway F outside the omitted-coordinate family (key positive result)

Constructed S = {L_{01}, L_{023}, L_{123}, L_{0123}} at n=5 (d=4) -- a
pair + two triples + the full-sum form, mult=[3,3,3,3], full rank, no
Gateway A/B/C/E applicability in the original coordinates (verified via
the engine: UNRESOLVED before this round's work).

Fixing Q and changing to coordinates (Q,x_0,x_1,x_3) [x_2 eliminated]:
$L_{0123}=Q$ becomes a bare constant (**killing the ENTIRE Q=0 fiber via
chi(0)=0**, a private-coordinate-style effect on the CONDITIONING variable
itself, not on the fiber); $L_{023}=Q-x_1$, $L_{123}=Q-x_0$; $L_{01}=x_0+x_1$
depends on neither $Q$ nor $x_3$ (**$x_3$ becomes a completely free fiber
coordinate**, contributing a bare factor of $p$). The genuine remaining
work is a 2-variable, ordinary multiplicity-2 problem in $(x_0,x_1)$.
Full derivation (elementary, single mult-2 step, no nesting needed):
$$\Sigma_S(p) = \chi(-2)\,p^2(p-1)\qquad\text{for every odd }p.$$
**Verified by direct enumeration at 7 primes (5,7,11,13,17,19,23), zero
mismatches, no exceptional prime found** (in contrast to the omit-one
family) -- consistent with the mechanistic finding that exceptional primes
arise specifically from NESTED elimination depth, and this example only
needed one (unnested) elimination step.

**This is the requested positive result**: not-A/B/C/E originally to
A/B/C-on-fibers, on a structurally different family from Round 5's.
Confirms Gateway F is not a narrow accident of the omitted-coordinate
symmetry.

## Part VII — evaluation vs. representation gateway

A/B/C/E are **evaluation gateways**: given the right structural condition,
they directly output a value. F is best classified as a **representation
gateway** (a meta-gateway): conditioning on Q never evaluates anything by
itself; in every example found, the actual value came from re-applying A
(private coordinate, both in the omit-one recursion's inner steps and in
the new example's Q=0-kills-everything step), B (multiplicity-2, in both
examples), or a bare free-coordinate factor of p (also both examples) --
all AFTER the representation change. No example this round required E or
C on a fiber, but nothing rules that out either. This distinction held up
under the two concrete tests run and is reported as **COMPUTATIONALLY
SUPPORTED / mechanistically clear for the cases checked**, not as a proved
general theorem about all possible Q-conditionings.

## Part VIII — complexity measure

Minimum coordinate multiplicity is NOT monotonically decreasing under
Q-conditioning as a standalone invariant (the omit-one family's fiber
still has min-multiplicity 2 everywhere, same as post-Level-1 recursion
states -- conditioning didn't lower it below what a good multiplicity-2
elimination sequence would eventually reach on its own; what changed was
the *availability* of a private coordinate/free coordinate that was not
visible in the original basis). The general lexicographic tuple candidate
(corank first, min-multiplicity second) was not falsified but also not
confirmed to strictly decrease across ALL rules uniformly -- Gateway F's
value is in REVEALING a private coordinate or a mult-2 pair that was
"hidden" by a change of basis, which the original coefficient matrix's own
invariants (in the ORIGINAL basis) do not obviously detect. Reported as a
genuine open question, not resolved this round.

## Part IX — reduction graph (partial)

Not built as a full formal data structure given time constraints; the two
concrete Gateway-F derivations in this round each constitute one worked
edge-path (S -> fiber decomposition -> [A or free-p] + [B] -> terminal
value), independently verified against direct enumeration. Multiple paths
to the same terminal value were not tested this round (would need e.g.
trying a different conditioning functional Q' on the same S and checking
agreement) -- flagged as a natural, well-scoped next check, not attempted
here to keep the round bounded.
