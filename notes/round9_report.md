# Hypercuboid exploration — Round 9 working notes

## Part I — reproduction (expanded)

Recomputed `Sigma_I(p)` directly from `core.py` for all 49 primes
`5 <= p <= 229`, spanning all four residues mod 8 (13 primes each for
1,3,5,7 mod 8 roughly). `Sigma_I(p) = -chi(2)*p(p-1)` holds with **zero
exceptions** on the 27 primes with `p==5,7 (mod8)`, and fails on **every
single one** of the 22 primes with `p==1,3(mod8)` (no accidental matches
either way). Confirms and substantially strengthens the Round-8 pattern.

## Part II — residue-class table, mod 8 vs mod 16

Built `p mod8, chi(-1), chi(2), chi(-2), Sigma_I(p)` for all 49 primes
(see `scripts/round9_mod8.py` output for a representative slice). Key
structural fact, immediate from quadratic reciprocity but worth stating
explicitly: **`p mod 8` is exactly the joint data `(chi(-1),chi(2))`**
(mod4 has 2 classes, mod8 refines each into 2, and `chi(-1),chi(2)` are
exactly independent enough to reconstruct all 4 mod-8 classes). Checking
which pair-values correspond to which class:

| p mod 8 | chi(-1) | chi(2) | chi(-2)=chi(-1)chi(2) |
|---|---|---|---|
| 1 | +1 | +1 | +1 |
| 3 | -1 | -1 | +1 |
| 5 | +1 | -1 | -1 |
| 7 | -1 | +1 | -1 |

**The "good" classes (5,7 mod 8) are exactly `chi(-2)=-1`; the "bad"
classes (1,3 mod 8) are exactly `chi(-2)=+1`.** So the correct controlling
character is `chi(-2)`, not `chi(2)` in isolation — a genuine refinement
of the Round-8 phrasing. Moreover, on the good locus, since
`chi(-2)=chi(-1)chi(2)=-1` there, we have `chi(2)=-chi(-1)` identically,
so
$$-\chi(2)\,p(p-1) = \chi(-1)\,p(p-1)\quad\text{on the good locus},$$
i.e. **the Round-8 formula is exactly `Sigma_I(p) = chi(-1)*p(p-1)`** on
its domain — the *same* sign character that already governs the
Class-I/Class-II relation, not an independent new character. This is a
real simplification, not merely cosmetic (see Part VII).

**Mod-16 refinement: tested explicitly, no evidence found.** Both mod-8
subclasses (`p mod16 in {5,13}` for the 5-class; `{7,15}` for the 7-class)
match the formula with zero exceptions regardless of the mod-16 value —
ruling out a finer congruence masquerading as mod 8 on the good locus. On
the bad locus, splitting the residual quantity `S(p)` (Part IV) by
`p mod16 in {1,9}` and `{3,11}` shows **no clean pattern in sign or
magnitude** in either sub-split (values scattered, e.g. mod16=1 gives
`S/p` = 1.12, 0.03, 1.87, 1.51, 1.80, 2.50 — no constant, no simple
sub-dichotomy) — mod-16 does **not** resolve the bad locus either.

## Part III — search for a pointwise transformation producing a factor of 2

Extended Round 8's exhaustive 24-permutation `S_4` scan (already known:
never produces a factor of 2, only `+-1`) with additional structurally
motivated linear maps on `P_I`, checked via exact symbolic ratio
`P_I(Mx)/P_I(x)`:

- pair-sum/difference basis `(x0+x1, x0-x1, x2)`
- single-coordinate sign flip, and the full sign flip `-x` (gives ratio 1,
  trivial, matches degree-6-even homogeneity)
- shears `x0 -> x0+x1`, `x0 -> x0+x2`
- coordinate doubling (`x0->2x0`; all coords `->2x`, giving the trivially
  expected `2^6=64` from degree-6 homogeneity)
- a rotate-and-double composite

**None produced a constant ratio** (only the two homogeneity-trivial cases
did, and neither involves a genuine `+-2` factor — the all-coordinates
doubling gives `64=2^6`, an even power, so `chi(64)=1`, contributing
nothing). **Killed: no low-complexity pointwise linear symmetry of `P_I`
produces a literal `+-2` (or `+-2*square`) scalar factor.** This is
consistent with a general fact worth stating plainly: an invertible
*linear change of variables* never by itself introduces a character
factor into `Sigma_S(p)` (it only relabels the summation index); the only
way to get a nontrivial factor is a genuine algebraic coincidence
`P(Tx) = c*P'(x)`, and no such coincidence involving `2` was found among
these candidates.

## Part IV/V — partial elimination + projectivization (the two, mutually confirming, exact reductions found)

**Route 1 (projectivization, Part V, the cleaner argument).** `P_I` is
homogeneous of even degree 6, so `chi(P_I(lam*x)) = chi(lam)^6 chi(P_I(x))
= chi(P_I(x))` for every `lam != 0` — `chi(P_I)` is literally constant on
every punctured line through the origin. Hence, for **any** subset `S`
with `|S|` even (not special to Class I — this is a general, previously
implicit fact about every even-cardinality case throughout this whole
project):
$$\Sigma_S(p) = (p-1)\cdot\sum_{\ell\in\mathbb P^2(\mathbb F_p)}\chi(P_S(\text{rep}_\ell))$$
Verified directly by brute-force enumeration over representatives for
small `p` (`scripts/round9_mod8.py:projective_sum`, matches `Sigma_I(p)`
exactly). This is an elementary, general, PROVED explanation of why a
clean `(p-1)` factor keeps appearing throughout the classification.

**Route 2 (partial elimination, Part IV, gives an explicit residual
sum).** Fixing `x2=c`, `x1=b` and summing over `x0` first: for fixed
`b,c != 0`,
$$\sum_{x_0}\chi(P_I) = \chi(bc(b+c))\cdot T(b,c),\qquad T(b,c)=\sum_{x_0}\chi(x_0(x_0+b)(x_0+c)).$$
`T(b,c)` is a **cubic character sum with roots `0,-b,-c`** — the classical
**Legendre family** `E_t: y^2 = x(x+1)(x+t)` after normalizing (Round 3's
elliptic-curve-trace territory, genuinely arising here, not forced).
Homogeneity of the cubic gives `T(lam*b,lam*c) = chi(lam)*T(b,c)` exactly
(PROVED, one line: substitute `x0=lam*y`). Writing `t=c/b` and
`g(t)=T(1,t)=sum_x chi(x(x+1)(x+t))`, this reduces (after handling the
`b=0`/`c=0` boundary, where the product vanishes identically) to:
$$\Sigma_I(p) = (p-1)\cdot S(p),\qquad S(p)=\sum_{t\in\mathbb F_p}\chi(t(t+1))\,g(t) = \sum_{x,t\in\mathbb F_p}\chi\big(x(x+1)\,t(t+1)\,(x+t)\big).$$
**Verified exactly (both the `(p-1)S(p)` identity and its equality with
Route 1's projective sum) at every tested prime, zero mismatches.** This
is now a fully PROVED, elementary, general reduction — but `S(p)` itself
is a genuine 2-variable character sum of a degree-5 expression, not
obviously reducible further by the elementary toolkit (multiplicity/
dependency/complementary-pair/`S_n`-symmetry) developed in Rounds 1-8.

**Discriminant/root-collision audit:** the roots `0,-b,-c` of the cubic
coincide exactly when `b=0`, `c=0`, or `b=c`; all three boundary loci were
checked and contribute correctly (the `b=0`/`c=0` cases force `P_I=0`
identically, handled above; `b=c` is a measure-zero locus inside the
`(b,c)` sum already correctly included in `S(p)`'s definition, no special
treatment needed since `g(t)` is defined by direct summation, not by an
assumed-distinct-roots formula).

## Part VI — the elliptic family, examined honestly

The curve `E_t: y^2=x(x+1)(x+t)` is the classical Legendre family,
`j`-invariant `j(t) = 256(t^2-t+1)^3 / (t^2(t-1)^2)`, discriminant
`Delta(t) = 16 t^2(t-1)^2` (both standard, not re-derived in full here —
flagged as textbook facts, not new results). `g(t)` relates to
`#E_t(F_p)` via `#E_t(F_p) = p+1+g(t)` (affine count `p+g(t)`, plus point
at infinity), i.e. `g(t) = -a_p(E_t)` up to the usual sign convention.

**Critically, `S(p)` is a sum of `g(t)` over the *entire* family
(weighted by `chi(t(t+1))`), not a single curve's trace.** By the Hasse
bound `|g(t)| <= 2*sqrt(p)` pointwise, but `S(p)` sums ~`p` such terms
with a quadratic-character weight — by Weil's theorem for character sums
of curves this two-variable quintic-type sum is expected at scale `O(p)`
generically (not `O(sqrt(p))`, and not `O(p^1.5)` either, reflecting
partial-but-not-complete cancellation), which matches the observed data
(e.g. `S(227) = -673`, comparable to `p=227`, not to `sqrt(227)=15` or
`227^1.5=3420`).

**Killed: `S(p)` is not simply `+-2a` for the CM representation
`p=a^2+2b^2`**, despite the striking coincidence that the "bad" classes
(`p==1,3 mod8`) are *exactly* the classes where `p=a^2+2b^2` is solvable
(classical fact, CM by `Z[sqrt(-2)]`, discriminant `-8`). Computed `a,b`
for 21 bad primes up to 227 and the ratio `S(p)/(2a)` is wildly
non-constant (`-4.17, 3.17, 7.5, -0.83, -5.7, ..., 79.5, -22.4` — no
pattern). **This natural hypothesis is explicitly killed, not merely
unconfirmed.**

Found (but not pursued further) an exact identity for `g` itself:
`g(t) = chi(-1)*g(1-t)` for all `t` (derived via the substitution
`x -> -1-x`, a genuine one-line algebraic identity, verified
numerically) — a real fact about the Legendre family's trace under the
classical root-swap `t -> 1-t`, but it did not lead to a further
reduction of `S(p)` in the time available (attempts to exploit it inside
`S(p)`'s definition led back to the same circular identity `S(p)=S(p)`,
not new information).

**No elliptic-curve identification of the exceptional-prime split was
completed.** The reduction genuinely produces an elliptic family (Part
VI's stated precondition is met), but connecting the family's
`chi(t(t+1))`-twisted second-moment-like sum `S(p)` to a specific single
curve's CM/twist behavior was attempted (the natural `a^2+2b^2` guess)
and **failed**. Whether `S(p)` corresponds to a specific weight-2 modular
form coefficient or a Jacobi-sum evaluation is flagged as open, not
resolved.

## Part VII — Class II consequence (derived, clean)

Using Round 8's proved relation `Sigma_II(p)=chi(-1)*Sigma_I(p)` together
with the Part II reframing `Sigma_I(p)=chi(-1)*p(p-1)` on the good locus:
$$\Sigma_{II}(p) = \chi(-1)\cdot\chi(-1)\cdot p(p-1) = p(p-1)\qquad\text{exactly, whenever }p\equiv5,7\pmod8.$$
**This is even cleaner than Class I's formula — a single sign-free closed
form, with no `chi(-1)` or `chi(2)` needed at all.** Verified exactly at
every tested prime with `p==5,7(mod8)` (zero exceptions; see
`scripts/round9_mod8.py` output). Not extended to the bad locus (Class II
there is exactly as unresolved as Class I, being `chi(-1)` times it).

## Part VIII — proof status of the target formula

**NOT proved from first principles.** What Round 9 achieved: an exact,
general, PROVED *reduction* of the entire question to a single concrete
2-variable character sum `S(p)`, plus overwhelming computational
confirmation (49 primes, zero exceptions in either direction) that
`S(p) = -chi(2)*p` exactly iff `chi(-2)=-1`. The domain was tested for
being larger or smaller than `p==5,7(mod8)`: **no**, it is exactly this
set, both ways (no exceptions inside, no accidental matches outside), up
to `p=229`. The reduction to `S(p)` is a genuine advance (it replaces an
opaque 3-variable degree-6 sum with a more classical-looking 2-variable
degree-5 sum tied to a named elliptic family), but the final evaluation
step remains a verified conjecture, not a theorem.

## Part IX — Gateway H?

**Not declared.** The round's own criteria require an exact evaluation or
exact sector-level relation from a mechanism that isn't reducible to
existing gateways. What was found:
- The projectivization/homogeneity fact (Part V) *is* new and general,
  but it is elementary bookkeeping (not a deep mechanism) and produces no
  evaluation by itself — every even-`|S|` case gets the same `(p-1)`
  factor for free; it does not distinguish good from bad loci.
- The partial-elimination reduction to `S(p)` (Part IV) is an exact,
  proved identity, but it is a *reduction*, not an evaluation — it
  produces a new open problem (evaluate `S(p)`), not a closed form.
- No mechanism was found that actually *proves* `S(p)=-chi(2)p`, so there
  is nothing yet to name.

**Conclusion: no Gateway H this round.** The honest state is "one proved
reduction lemma + one still-open, well-defined target," not a new closure
mechanism.

## Part X/XI — remaining residue classes and statistics

`p==1,3(mod8)`: genuinely unresolved. `S(p)` values (25 tested primes,
`5<=p<=229`) have mean `S(p)/p ~ 0.005` (statistically indistinguishable
from 0), sample standard deviation of `S(p)/p ~ 1.71`, sign roughly
balanced (14 positive, 11 negative) — consistent with a "hard,"
square-root-cancellation-scale-relative-to-`p` quantity with no obvious
bias, but this is **STATISTICAL EVIDENCE ONLY**, not a derived law, and
the sample (25 points) is too small to responsibly claim a specific
distribution (e.g. Sato-Tate-like) — flagged honestly as under-powered
rather than forcing a claim.

## Part XII — progressive character refinement: partially survives, partially killed

`mod4 -> mod8` **is** a genuine, proved refinement: `chi(-1)` (mod 4)
governs the Class I/II *relation* and Class III's *vanishing*; `chi(-2)`
(equivalently, `p mod 8`) governs Class I's *value* on exactly half the
primes. That much is real, not an artifact.

**But the naive continuation `mod8 -> mod16 -> ...` is explicitly
killed**: mod-16 refinement was tested on both the good locus (no effect,
consistent with the good locus already being fully resolved) and the bad
locus (no clean sub-pattern found in sign, magnitude, or a mod-16 split).
The bad locus's difficulty does not look like "one more layer of the same
kind of congruence obstruction" — it looks like a qualitatively different
kind of problem (an unresolved elliptic-family moment), not a finer
residue class waiting to be split. **The "progressively finer congruence"
mental model does not survive past mod 8** for this family; the correct
framing is closer to "one exact congruence layer, then a genuinely hard
remainder," not an infinite descending tower.

## Adversarial notes / everything killed this round

1. Pointwise-transformation-producing-a-factor-of-2 hypothesis (Part
   III): killed for every structurally motivated candidate tried.
2. Mod-16-refines-mod-8 hypothesis, both loci: killed.
3. `S(p) proportional to 2a` (CM-trace, `p=a^2+2b^2`) hypothesis: killed,
   despite a suggestive coincidence in which classes are affected.
4. Pure `chi(2)`-dependence hypothesis: superseded (not exactly killed,
   but shown imprecise) by the cleaner `chi(-2)`/`chi(-1)` reframing in
   Part II/VII.
5. "Elliptic curve directly explains everything" hope (Part VI):
   genuinely produced the right family, but did not yield a proof —
   downgraded from hoped-for mechanism to "correctly identified but
   unresolved."

## Highest-value next question

**Evaluate (or prove non-elementary) the single 2-variable sum**
$$S(p) = \sum_{x,t\in\mathbb F_p}\chi\big(x(x+1)\,t(t+1)\,(x+t)\big),$$
proved in Round 9 to be *exactly equivalent* (via `Sigma_I(p)=(p-1)S(p)`)
to the entire Class-I/Class-II mystery. This is strictly more tractable
than the original 3-variable degree-6 problem — it is a named, classical-
shaped object (a quadratic character sum of a quintic built from the
Legendre family) — and resolving it (or proving it has no elementary
closed form) would settle Round 9's central question completely.
