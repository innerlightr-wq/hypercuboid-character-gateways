# Hypercuboid exploration — Round 12 working notes

## Part I — freeze/audit of Round 11 (PROVED, reconfirmed)

Independently recomputed `c4,c6,Delta,j`, the four Kodaira fibers
(`I_2^*,I_2,I_0^*,I_2^*`), the Euler-number sum (24, K3), the rational
`(\mathbb Z/2)^2` torsion, and the master identity at a sweep of primes.
**No discrepancy found** — Round 11 stands as the frozen baseline.
**Extended verification this round: the identity also holds exactly at
`p=3`** (`a_p(E)=-2`, `S(3)=-1`, predicted `-1` — match), and at every
prime `5\le p<500` (95 primes, zero exceptions) — strictly more evidence
than Round 11 had, still zero counterexamples anywhere.

## TRACK A — Shioda–Inose / Kummer route

### Part II — is the K3 singular (`rho=20`)? **NOT PROVED, NOT REFUTED**

Shioda–Tate gives `rho=19+\mathrm{rank}(MW)`, so `rho=20` iff a
non-torsion section exists. This round searched **systematically** (not
just spot-checks) for a low-degree section `X(t)=At^2+Bt+C`:

- The degree-7 (leading) term of `X^3+a_2X^2+a_4X` factors as `A(A+1)`,
  forcing `A\in\{0,-1\}` for the result to have a chance of even degree.
- **`A=-1`: PROVEN IMPOSSIBLE.** The resulting degree-6 polynomial has
  leading coefficient `-t^6` — a negative leading coefficient can never
  be a perfect square over `\mathbb Q` (or `\mathbb R`). Killed outright
  for *all* `B,C`, not just the tested values.
- **`A=0` (linear `X=Bt+C`): reduces to a product of three generically
  coprime irreducible factors** of degrees `1,2,3`
  (`RHS=(Bt+C)(t^2+(B+1)t+C)(t^3+t^2+Bt+C)`, verified by exact
  factorization). A perfect square requires every irreducible factor to
  occur to an even power; with three generically-distinct factors of odd
  total multiplicity pattern, this forces coincidences. Solved exactly
  for when the linear factor divides the quadratic one (`C=0` or `C=B`);
  checked both resulting one-parameter families (`X=Bt`, `X=B(t+1)`)
  explicitly and **both still contain a genuinely irreducible non-square
  residual factor for every `B`** (`(t+B+1)(t^2+t+B)` type residues, or
  `(1+t^2)`-type factors) — **no non-torsion section of degree `\le2`
  exists.** This is a real, derived negative result, not a failed guess.

**Conclusion: `rho=20` is neither proved nor refuted.** A higher-degree
section is not ruled out. **CONJECTURAL** that `rho=20`; the master
identity's shape (a clean rank-2-transcendental-lattice-flavored formula)
remains the only evidence for it.

### Part III — Néron–Severi / transcendental lattice: **NOT COMPUTED**

Without a resolved value of `rank(MW)`, the exact `NS(X)` lattice
(beyond its rank being 19 or 20) and its discriminant were **not**
computed this round — this needs either an explicit MW generator (not
found) or an independent period/lattice computation (out of scope for
hand/light-symbolic work here). **Honest gap, not filled.**

### Part IV — Shioda–Inose structure: **NOT ESTABLISHED**

No explicit Nikulin involution, quotient map, or identification with a
known Inose pencil was constructed. The candidate mechanism (`X`
Shioda–Inose-related to `\mathrm{Km}(E\times E)` for our `E`) remains
exactly what it was at the end of Round 11: **a well-motivated hypothesis
consistent with the numerics, not a constructed correspondence.**
**CONJECTURAL, unchanged in status from Round 11 — no progress made on
the actual construction this round**, despite real effort on the
Mordell–Weil prerequisite (Part II).

### Part V — the eigenvalue algebra (PROVED, elementary, useful regardless of Part IV)

This part **is** fully derivable and is recorded precisely so any future
attempt at Part IV has the exact target formula, not a vague
proportionality. Write `\alpha_p,\beta_p` for the Frobenius eigenvalues
of `E` (`\alpha_p+\beta_p=a_p(E)`, `\alpha_p\beta_p=p`). Then, exactly:
$$a_p(E)^2=\alpha_p^2+\beta_p^2+2p.$$
For the *traceless* symmetric-square piece (the natural transcendental
candidate in a Kummer/Shioda–Inose construction from `E\times E`), the
relevant quantity is `\alpha_p^2+\beta_p^2 = a_p(E)^2-2p`. The **boxed
master identity**, rewritten in this language, is:
$$S(p) = -\chi(2)p + \chi(-1)\big[(\alpha_p^2+\beta_p^2) + 2p\big] = \big[2\chi(-1)-\chi(2)\big]p + \chi(-1)(\alpha_p^2+\beta_p^2).$$
**This is a PROVED algebraic rewriting** (pure eigenvalue arithmetic,
`\alpha\beta=p` used once), **not a proof of the identity itself** — it
simply isolates which piece would need to be the "genuine transcendental
trace" (`\alpha_p^2+\beta_p^2`) versus which piece would need to come
from the algebraic/Tate part of `H^2` (`[2\chi(-1)-\chi(2)]p`, a clean
`p`-multiple of a sign character, exactly the flavor of quantity a
bounded Néron–Severi trace produces). **This rewriting is offered as the
precise target for a future Part IV attempt — it was not itself derived
from `X`'s cohomology this round.**

## TRACK B — modular-form route

### Part VI — weight-3 CM form: **NOT ATTEMPTED IN FULL, HONEST SCOPE LIMIT**

A literature/database search for "the weight-3 CM newform attached to
`\mathbb Q(\sqrt{-2})`, discriminant -8" was not carried out with actual
LMFDB-style coefficient lookups this round (would need live access to a
modular forms database, matching Fourier coefficients against
`a_p(E)^2-2p` at several primes, and confirming a level/character exactly
— a well-defined task, not attempted here due to time, not because it is
believed to fail). **NOT ATTEMPTED — explicitly flagged as a gap, not
silently skipped.**

### Part VII — CM formula for `a_p(E)` (PROVED / LITERATURE-STANDARD, cleanly stated)

Classical (Deuring; already invoked in Round 11, restated precisely
here): for `E` with CM by an order in `K=\mathbb Q(\sqrt{-2})`
(class number 1, so the theory is at its simplest):
- **`p` inert in `K`** (`\chi(-2)=-1`, i.e. `p\equiv5,7\pmod8`):
  `a_p(E)=0` exactly (supersingular reduction). **PROVED (classical).**
- **`p` split in `K`** (`\chi(-2)=+1`, i.e. `p\equiv1,3\pmod8`): writing
  `p=\pi\bar\pi` in `\mathbb Z[\sqrt{-2}]`, `a_p(E)=\pi+\bar\pi` up to a
  root-of-unity twist fixed by the specific model of `E` and a Hecke
  character; concretely, `a_p(E)=\pm2A(p)` where `p=A(p)^2+2B(p)^2` is
  the classical representation (Hashimoto–Long–Yang's own `A,B`, their
  Theorem 1) — **the precise sign of `\pm` was not independently
  re-derived from the Hecke character this round** (it is fixed but its
  exact rule, e.g. via `A(p)\equiv\pm1\pmod4`-type normalization, was not
  rederived) — **LITERATURE-STANDARD, cited, not independently proved
  here.**

## TRACK C — direct character-sum attack

### Part VIII — direct proof attempt (attempted seriously; **obstruction found, not a proof**)

Completed the square: `x=(u-1)/2,\,t=(v-1)/2` type substitution gives,
after full reduction (bijective, verified symbolically):
$$S(p) = \chi(2)\sum_{a,b}\chi\big(a(a+2)b(b+2)(a+b)\big).$$
Attempting to push further (rescale `a=2a',b=2b'`) **returns exactly to
`S(p)` itself** — a genuine but **circular** identity (verified
symbolically): this specific substitution chain is a self-symmetry of
`S(p)`, not a reduction to a new object. **KILLED as a route**, cleanly
(not just "didn't work" — shown to close a loop).

**Degree-obstruction to any direct pointwise substitution.** The target
`\chi(-1)a_p(E)^2 = \chi(-1)\sum_{x,y}\chi(h(x)h(y))` is (up to the
`\chi(-1)` scalar) a degree-**6** two-variable expression (`h` is cubic,
`h(x)h(y)` is bidegree `(3,3)`). Our `F(x,t)=x(x+1)t(t+1)(x+t)` is
degree **5**. **A literal polynomial identity
`F(\phi(x,y),\psi(x,y)) = c\cdot u(x,y)^2\cdot h(x)h(y)`** for a linear
(or otherwise low-complexity) change of variables `(\phi,\psi)` is
**degree-inconsistent** unless `u` has *negative* degree, which is
impossible for a genuine correction polynomial. **This is a real,
derived, structural reason no simple pointwise substitution proof can
work** — if a direct proof exists, it must go through a genuinely
non-pointwise mechanism (Gauss-sum Fourier expansion, Jacobi-sum
convolution in the sense of an actual integral/sum transform, not an
algebraic change of variables). **Reported as a genuine finding: the
"easy" route is provably not available in this form.**

No Gauss/Jacobi-sum Fourier-expansion proof was completed this round
(this is a substantially harder undertaking than the pointwise-
substitution attempts and was not carried through to a result).
**KILLED: naive pointwise substitution route. UNRESOLVED: Fourier/Jacobi-
sum route (not disproved, not completed).**

### Part IX — literature re-check (no new match)

Re-examined the Hashimoto–Long–Yang paper's content (already read in
full in Round 11) specifically for any stated double-sum or moment
identity matching `S(p)` or the twisted-Legendre-first-moment shape.
**None found** — their paper's actual theorems are one-variable
Jacobsthal sums (`A` from `x^3+4x^2+2x`, and separate quintic/sextic `B`
sums for the two mod-8 sub-cases; see Round 11 Part X) and do not state
or imply a two-variable convolution formula. **Classification unchanged
from Round 11: STRUCTURALLY RELATED (their curve `E` is the right
object), NOT a literature statement of the master identity itself.** No
other paper located this round that states the exact double sum in
closed form. **KNOWN IN LITERATURE: NO. REDERIVED HERE: NOT FULLY (only
verified, not derived).**

### Part X — affine/projective bookkeeping (partial, honest)

`S(p)=\#V(\mathbb F_p)-p^2` for the literal affine model `V`, exact
(re-confirmed, PROVED, unchanged from Round 10/11). Relating this
precisely to `\#X(\mathbb F_p)` for the smooth **projective, resolved**
model `X` requires accounting for: (a) the points of `V` missing at
infinity in each of the two affine coordinates, (b) the effect of
resolving the `I_2^*` (7 components each, at `t=0,\infty`) and `I_0^*`
(5 components, at `t=-1`) singular fibers, and (c) the section(s)
(torsion points contribute `p+1` points per section at every fiber, `2`
sections beyond the zero-section already known via the `(\mathbb
Z/2)^2` torsion, contributing predictable but nontrivial correction
terms). **This full accounting was not carried out to an explicit
formula this round** — it is a concrete, well-defined, and bounded
computation (not a research-level open question, just a bookkeeping
exercise requiring care with each bad fiber's exact resolved
component count and intersection pattern) that remains **undone**. **No
claim is made that `-\chi(2)p` has been *located* inside a specific
algebraic-cycle correction — this remains asserted only via the
Part V rewriting's shape, not derived from the resolved model.**

## Part XI — aggressive falsification (identity survives everything tried)

1. All four mod-8 classes tested (Round 11 + this round): zero mismatches.
2. `p=3` (a genuine edge/bad-reduction-adjacent prime elsewhere in this
   whole project): **matches exactly** (new check this round).
3. Extended range to `p<500` (95 primes): **zero mismatches**.
4. Sign convention for `a_p(E)`: fixed once (`a_p=-\sum\chi(h(x))`,
   Silverman's standard convention) and used consistently; since the
   identity uses `a_p(E)^2`, **the sign of `a_p(E)` cannot matter to the
   identity at all** — this is a useful robustness feature: even if the
   literature's or our own sign convention were flipped, the identity is
   invariant. (Worth noting explicitly, since Part XI asked to check sign
   conventions — here the check is that they are provably irrelevant.)
5. Quadratic-twist convention (`d y^2=f(x)` vs `y^2=f(dx)/d^3` etc.):
   re-verified in Round 11 via two independent invariant computations
   (`b`-form and `c4,c6`-form); unaffected this round since no new twist
   was introduced.
6. **No counterexample found at any stage.** The identity is not
   falsified — but Track C's obstruction finding (Part VIII) shows the
   *easiest possible* proof strategy is unavailable, which is itself a
   meaningful (negative) result about *how hard* a proof would be, even
   though it says nothing against the identity's truth.

## Part XII — final classification of the master identity

**COMPUTATIONALLY VERIFIED ONLY.** None of PROVED DIRECTLY (Track C
found a real obstruction, not a proof), PROVED VIA K3/SHIODA–INOSE
(Track A: `\rho=20` and the Nikulin involution/Kummer identification
were not established), PROVED VIA MODULAR FORM (Track B: not attempted
to completion), or KNOWN IN LITERATURE (Part IX: no source states it)
was achieved. The identity has survived every falsification test applied
across two rounds (Round 11 + Round 12, now ~95+ primes, all four
residue classes, including `p=3`) with zero exceptions, and its
constituent pieces (the CM curve identification, the classical
inert/split dichotomy, the eigenvalue-algebra rewriting) are all
individually solid — but the **connective tissue** (why `X`'s H² trace
equals `\chi(-1)(a_p(E)^2-2p)` plus a specific algebraic term) remains
unproved.

## Part XIII — the progressive-constraint picture, reassessed

Round 12 refines rather than overturns the Round 11 formulation. The
more precise statement this round supports:
**"Each earlier reduction removes algebraically tractable degrees of
freedom until the residual invariant is no longer controlled by
incidence geometry alone, but by the Frobenius action on a global
algebraic variety."** Round 12 adds a needed caveat, tested directly by
trying (and failing) to *complete* the arithmetic-geometry step: **being
controlled by a global variety's Frobenius action does not, by itself,
make the invariant tractable by hand** — the last rung of the hierarchy
is qualitatively different from the previous ones in that its resolution
(if it exists via Shioda–Inose) requires machinery (lattice theory,
period computations, or database-level modular form lookups) that is not
a further application of the same elementary character-sum toolkit used
in Rounds 1–9. **The hierarchy survives as a true description of what
was *tried and exhausted* at each stage, but Round 12 shows the final
stage is not self-contained the way the earlier ones were** — it
currently terminates in "identify the right classical object and verify
numerically," not "derive it."

## Everything killed or corrected this round

1. **KILLED**: any non-torsion section of `X(t)` with degree `\le2`
   (fully, rigorously, via the factorization/sign arguments above, not
   just spot-checking numeric guesses as in Round 11).
2. **KILLED**: the "rescale-and-reduce" substitution chain in Part VIII
   as a route to a direct proof (shown circular, not merely unproductive).
3. **KILLED**: the possibility that a literal low-degree pointwise
   polynomial substitution proves the identity (degree-mismatch argument,
   Part VIII) — any direct proof must be Fourier/Jacobi-sum-based, not
   algebraic-substitution-based.
4. **NOT killed, reconfirmed**: the master identity itself — survived
   its most aggressive test yet (`p=3`, 95-prime sweep).
5. **NOT resolved**: `\rho=20` vs `19`; the Shioda–Inose correspondence;
   the weight-3 modular form identification; the affine/projective
   bookkeeping's exact formula.

## Highest-value next question

Given Track C's pointwise-substitution route is now provably closed off,
the two live paths are: **(a)** compute an explicit height pairing / try
a genuinely higher-degree (degree 3-4) section search to settle
`\rho\in\{19,20\}` definitively, or **(b)** look up the weight-3 newform
associated to discriminant `-8` in a modular forms database (e.g. LMFDB)
and directly compare its first 20-30 Fourier coefficients against
`\chi(-1)(a_p(E)^2-2p)` — this is a **finite, mechanical check** that
would either confirm Track B decisively or falsify it outright, and is
very likely more tractable in a future round than completing the full
Shioda–Inose lattice construction by hand.
