# Hypercuboid exploration — Round 5 working notes

## Gateway F — omit-one-coordinate closure (the main Round-5 finding)

**Object.** n=5 (d=4), S = {Q-x_0, Q-x_1, Q-x_2, Q-x_3}, Q=x_0+x_1+x_2+x_3
("all four triples"). Independently reconfirmed (Part I): rank 4 (full
rank, corank 0), every coordinate has multiplicity 3, no linear
dependency exists, no Gateway-E complementary pairing exists within S
(complements of the triples are singletons, absent from S), and the
configuration is invariant under all 24 permutations of the 4 coordinates
(the symmetric group acts transitively on the 4 forms).

**Derivation (fix Q, then TWO nested multiplicity-2 eliminations in the
fiber).** Change variables to (Q, x_1, x_2, x_3) [x_0 = Q-x_1-x_2-x_3].
Then the four factors become $(x_1+x_2+x_3)$, $(Q-x_1)$, $(Q-x_2)$,
$(Q-x_3)$ — for FIXED Q this is a 4-form system in 3 variables where each
of $x_1,x_2,x_3$ has multiplicity exactly 2 (once in the "coupling" factor
$x_1+x_2+x_3$, once in its own $(Q-x_i)$ factor).

Eliminating $x_1$ (multiplicity-2 identity, Round 2 Part III) between
$(x_1+x_2+x_3)$ and $(Q-x_1)=-(x_1-Q)$: roots $r_1=-(x_2+x_3)$, $r_2=Q$,
leading coefficients $a=1,b=-1$ ($\chi(ab)=\chi(-1)$). Coincidence
$r_1=r_2 \iff x_2+x_3=-Q$.
$$\sum_{x_1}\chi(\cdot) = \chi(-1)\big[-1 \text{ if } x_2+x_3\neq-Q,\ (p-1)\text{ if }x_2+x_3=-Q\big].$$
The "no-coincide" branch, summed against the remaining factors
$(Q-x_2)(Q-x_3)$ over ALL $(x_2,x_3)$, is $-\chi(-1)\cdot
[\sum_{x_2}\chi(Q-x_2)][\sum_{x_3}\chi(Q-x_3)] = -\chi(-1)\cdot0\cdot0=0$
exactly (each bracket is a full-field character sum, $=0$).

The "coincide" branch restricts to the line $x_3=-Q-x_2$; substituting,
$(Q-x_2)(Q-x_3)\big|_{\text{line}} = (Q-x_2)(2Q+x_2)$, which factors as
$-(x_2-Q)(x_2-(-2Q))$ — a SECOND multiplicity-2 elimination (now in
$x_2$), with coincidence condition $Q=-2Q \iff 3Q=0$.
$$\sum_{x_2}\chi(\cdot)\big|_{\text{line}} = \chi(-1)\big[-1\text{ if }3Q\neq0,\ (p-1)\text{ if }3Q=0\big].$$

Multiplying the $p$ (from the coincidence branch's weight) and the two
$\chi(-1)$ factors ($\chi(-1)^2=1$), the FIBER sum is, for $p\neq3$
(so $3Q=0\iff Q=0$):
$$\sum_{x_1,x_2,x_3}\chi(\cdot)\Big|_Q = \begin{cases}p(p-1) & Q=0\\ -p & Q\neq0\end{cases}$$
**Verified exactly, fiber by fiber, at $p=5,7,11,13$ — not just after
summing over $Q$** (every single nonzero $Q$ gives exactly $-p$, matching
the derivation's claim that the fiber sum does not depend on WHICH nonzero
$Q$, only on whether $Q=0$).

**Summing over all $Q\in\mathbb F_p$:**
$$\Sigma_S(p) = 1\cdot p(p-1) + (p-1)\cdot(-p) = p(p-1) - p(p-1) = 0.$$

**Verified by full direct 4-variable enumeration at $p=5,7,11,13,17$: exactly
0 at every prime.** $p=3$ is a genuine, correctly-predicted exception
(3Q=0 for every Q when p=3, breaking the Q=0/Q≠0 dichotomy the derivation
relies on) — directly checked: $\Sigma_S(3)=18\neq0$, exactly as the
derivation's own stated scope predicts.

**Implemented as a general structural detector** (`try_gateway_f_full_rank_omit_one`
in `elimination_engine.py`, scoped honestly to $d=4$ only, since that is
what was actually derived — not extrapolated to other $d$ without
re-deriving the nested-elimination arithmetic, which would differ). Full
regression suite (n=4 classification, adversarial n=5 battery, all
Round 1-4 sanity examples) re-run: zero regressions, the only "failure" is
the correctly-flagged, documented $p=3$ exception.

## Part III (dual/complement with singletons) — superseded, not pursued

The complementary singleton family $\{L_0,L_1,L_2,L_3\}$ is itself a
trivial Gateway-A (private-coordinate) case, $\Sigma=0$. A "duality"
relation between two objects that are both already independently resolved
adds nothing beyond what Gateway F already fully settles; not pursued
further once the direct fix-$Q$ derivation succeeded.

## Part IV (symmetric-polynomial rewriting) — symmetry without separability

$\prod_i(Q-x_i) = e_2 Q^2 - e_3 Q + e_4$ (evaluating the monic quartic with
roots $x_i$ at $t=Q=e_1$; the $e_1^4$ terms cancel identically). This is a
clean, fully symmetric rewriting — but $e_2,e_3,e_4$ still depend jointly
on all four original variables, so this rewriting **by itself changes
nothing about the character sum's difficulty** (explicitly a negative
result, per the round's own required distinction between symmetry and
separability). The actual gateway (above) came from working directly with
the raw coordinates after fixing $Q$, not from this symmetric form.

## Part VI (adversarial separability search) — summary

Considered: Hadamard-type sum/difference coordinates, pair-sum/pair-difference
bases, coordinate-complement transformations. The fix-$Q$-plus-three-free-
coordinates basis (used above) was the one that worked; it is exactly the
"$Q$ plus coordinate differences"-flavored transformation the round
suggested trying, and it succeeded completely — so no further adversarial
search was needed once the correct basis was found and driven to a
complete derivation.

## Part VII — Gateway E, d>k+1 control experiment

**Proved (well, derived and verified — the derivation is essentially
immediate)**: an untouched/free coordinate contributes an independent
factor of $p$ to the whole sum (same mechanism as Round 1's original free-
coordinate observations), so Gateway E generalizes to $d=k+1+r$ (r free
coordinates) as $\Sigma_S(p) = p^r\cdot\big[\chi(-1)^k(p-1)((-1)^k+(p-1)^{k-1})\big]$.
Verified directly: $k=2$, one extra free coordinate ($d=4$), predicted
$p^2(p-1)$ — matched exactly at $p=5,7,11,13,17$.
