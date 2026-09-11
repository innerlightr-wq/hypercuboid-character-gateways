# Hypercuboid exploration — Round 4 working notes

## Gateway E — complementary-pair factorization (the main Round-4 finding)

**Setup.** S consists of k complementary pairs of representative forms
with respect to the FULL current coordinate set $\{0,\dots,d-1\}$: for
each pair, $J \sqcup J^c = \{0,\dots,d-1\}$, both forms present in $S$.
Precondition (derived and checked, not assumed): $d = k+1$ exactly (one
extra independent dimension beyond the $k$ pair-representative
coordinates), and the $k$ representative coefficient vectors together
with the all-ones vector $Q=(1,\dots,1)$ have rank $k+1$ (checked via
exact rank, every time — not assumed from the complementary structure
alone).

**Derivation.** Change of variables $u_i = $ (one representative of pair
$i$), $Q = x_0+\cdots+x_{d-1}$ (invertible exactly when the rank
condition above holds — checked, e.g. via $p$ odd making $1/2$ available
where needed). Each complementary pair's product becomes
$L_{A_i}\cdot L_{A_i^c} = u_i\cdot(Q-u_i)$, a function of $u_i$ and $Q$
ONLY. The full product factors as $\prod_i u_i(Q-u_i)$, and — crucially —
once $Q$ is fixed, the $k$ factors are **completely independent** (each
depends on a different free variable $u_i$), so
$$\Sigma_S(p) = \sum_Q \prod_{i=1}^k \Big(\sum_{u_i}\chi(u_i(Q-u_i))\Big).$$
Using the classical fact (re-derived, Round 2 Part III):
$\sum_u \chi(u(Q-u)) = -\chi(-1)$ if $Q\neq0$, $\chi(-1)(p-1)$ if $Q=0$
(this is literally the multiplicity-2 identity applied to the pair
$\{u, -(u-Q)\}$), summing over $Q$ gives, EXACTLY:
$$\Sigma_S(p) = \chi(-1)^k\,(p-1)\Big[(-1)^k + (p-1)^{k-1}\Big].$$

**Verification and unification (not assumed, checked at every step):**
- $k=1$: formula gives exactly $0$ — correctly reduces to the already-known
  Level-0 (private-coordinate) case, since one complementary pair covering
  every coordinate exactly once IS a private-coordinate configuration for
  every coordinate simultaneously. Sanity check, not a new claim.
- $k=2$: formula gives $p(p-1)$ — matches Round 1's $(0,1,4,5)$ example
  (previously reached only via the pairwise Level-1 recursion) exactly,
  an independent cross-check from a completely different derivation route.
- $k=3$: formula gives $\chi(-1)\,p(p-1)(p-2)$ — **new this round**,
  resolves the n=5 "all 6 pairs" corank-2 core that was unresolved through
  Round 3. Verified against direct enumeration at 12 primes (both $p\bmod4$
  classes), zero mismatches. Implemented as a genuine structural detector
  in the engine (`try_gateway_e_complementary_pairs` in
  `elimination_engine.py`) — re-verified through the engine itself (not
  just a standalone hand check), 14/14 primes via `adversarial_n5.py`.

**Scope, precisely as verified (not extrapolated):** requires $m=2k$
forms, $d=k+1$ exactly. NOT tested/claimed for $d>k+1$ (extra untouched
free coordinates would presumably contribute a bare factor of $p$ each, by
analogy with Round 1's free-coordinate pattern, but this was not checked
this round). Does not apply to n=4's seven corank-3 $|S|=6$ cases (wrong
size: those need $m=6$, $d=3\Rightarrow k=2$ would need $m=4$, mismatch)
or to the "all 4 triples" corank-0 case (no complementary pairing exists
at all within that specific 4-form set, since the complements of the four
triples are singletons that aren't part of $S$).

## Full-rank core ("all 4 triples", n=5)

Zero circuits (confirmed, `circuit_analysis.py`): the four triple-forms
are linearly INDEPENDENT (rank 4, $|S|=4=d$). No Gateway-E structure
(complements of these triples are singletons, absent from $S$). Considered
or the substitution $Q-x_i$ = the triple missing coordinate $i$: product
$=\prod_i(Q-x_i)$, a genuine quartic that does not separate into
independent single-variable factors the way the pairs case did (each
factor still depends on 3 of the 4 original variables even after fixing
$Q$). No further gateway found this round — reported as a genuine boundary
result per the round's own instruction not to brute-force it.

## Circuit inventory, n=4 corank-3 cases (Part IV/V)

All seven unresolved $|S|=6$ n=4 cores were fully decomposed into matroid
circuits (`circuit_analysis.py`, brute-force minimal-dependent-subset
search — exact, exhaustive at this size). Every one contains **multiple
overlapping size-3 and size-4 circuits**, including the "trivial" additive
circuit type ($L_i+L_j=L_{ij}$, coefficient product $+1$, present whenever
two singletons and their union-pair co-occur) and the Round-3 Level-2 type
(coefficient products $\pm1,\pm2$, matching $(3,4,5,6)$'s $\chi(-2)$
family exactly where that specific 4-subset appears as a circuit inside a
larger unresolved set). No combination rule that predicts the FULL
6-element sum from its circuits' individual formulas was found this round
(character sums for overlapping products do not combine by simple
multiplication of the circuits' individual values) — reported as tried,
not resolved.
