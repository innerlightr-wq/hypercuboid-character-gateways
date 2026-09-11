# Hypercuboid exploration — Round 10 working notes

## Part I — reproduction (frozen baseline)

Independently re-derived and re-verified `Sigma_I(p) = (p-1)*S(p)`,
`S(p) = sum_{x,t} chi(x(x+1)t(t+1)(x+t))`, at 12 primes covering all four
mod-8 classes — exact match, zero exceptions (`scripts/round9_mod8.py`
baseline unchanged, re-run in this round as the frozen starting point).

## Part II — trace interpretation and singular fibers (corrected/sharpened)

Let `g(t) = sum_x chi(x(x+1)(x+t))`. The cubic `x(x+1)(x+t)` has roots
`0,-1,-t`; these collide exactly at **`t=0`** (root `-t` meets `0`) and
**`t=1`** (root `-t` meets `-1`) — **not at `t=-1`** (roots `0,-1,1` are
pairwise distinct for every odd `p`; `t=-1` is a perfectly smooth fiber).
This is a small but real sharpening of the Round-9 picture: the sum's
weight `chi(t(t+1))` happens to vanish at `t=0,-1`, which is a *different*
pair of points than the curve's actual singular fibers `t=0,1` — only
`t=0` is common to both. Concretely (both PROVED, closed form, not
estimated):
$$g(0) = -1 \quad\text{(exactly, every odd }p\text{)},\qquad g(1) = -\chi(-1)\quad\text{(exactly, every odd }p\text{)}.$$
Both verified symbolically and numerically (zero exceptions).

For generic `t` (`t \ne 0,1`), `E_t: y^2=x(x+1)(x+t)` is a smooth
elliptic curve with `#E_t(F_p) = p+1+g(t) = p+1-a_t(p)`, i.e.
`a_t(p) = -g(t)`.

Splitting `S(p) = sum_t chi(t(t+1)) g(t)` by fiber type:
- `t=0`: weight `chi(0)=0`, contributes nothing.
- `t=-1`: weight `chi((-1)(0))=chi(0)=0`, contributes nothing (even
  though the fiber itself is smooth and arithmetically interesting — see
  below).
- `t=1`: weight `chi(2)`, fiber singular, contributes `chi(2)*(-chi(-1)) = -chi(-2)` exactly.
- All other `t`: smooth fiber, contributes `chi(t(t+1))*(-a_t(p))`.

**Exact moment formula (PROVED):**
$$\boxed{S(p) = -\chi(-2) \;-\!\!\sum_{t\ne0,\pm1}\chi(t(t+1))\,a_t(p)}$$
This is a genuine **`chi(t(t+1))`-twisted first moment of the Legendre
family's Frobenius trace**, over the smooth locus, plus one elementary
correction term from the single singular-but-weight-nonzero fiber `t=1`.
(Note in passing: `g(-1)` — the trace of the CM curve `y^2=x^3-x`,
`j=1728`, CM by `Z[i]` — was checked and matches the classical fact
`a_p=0` for `p\equiv3(4)`, nonzero tied to `p=a^2+b^2` for `p\equiv1(4)`;
this fiber is arithmetically rich but numerically irrelevant to `S(p)`
since its weight is exactly zero.)

## Part III — which moment, precisely

Confirmed: this is a **twisted first moment**, `sum_t chi(f(t)) a_t(p)`
with `f(t)=t(t+1)`, not a second moment or unweighted moment. No
rewriting attempted turned it into a pure `sum_t a_t(p)` or
`sum_t a_t(p)^2` — the weight `chi(t(t+1))` is load-bearing and does not
cancel.

## Part IV — literature search (WebSearch used; results assessed honestly)

Searched for: Jacobsthal sums of cubic character sums, moments of
Legendre-family traces, finite-field hypergeometric evaluations.

**FOUND IN LITERATURE (genuinely relevant, standard theory — not
claimed as new here):**
- Ronald Evans and collaborators' classical work on **Jacobsthal sums**
  (`sum chi(f(x))` for cubic/quartic `f`) evaluated via Jacobi sums and
  binary-quadratic-form parameters — the correct general toolkit for
  single-variable sums like `g(t)`, confirming `g(0),g(1)` above are of
  the expected classical shape (Evans, *Sums of Gauss, Jacobi, and
  Jacobsthal*, J. Number Theory 1979).
- The Legendre family's trace is classically `a_p(E_\lambda) =
  -p\,\chi(-1)\,{}_2F_1(\chi,\chi;\varepsilon;\lambda)_p` in Greene's
  finite-field hypergeometric normalization (Ono and others) — confirms
  `g(t)` (equivalently `a_t(p)`) is exactly a normalized finite-field
  `_2F_1` value, standard and expected, not news.
- A paper titled *"2,3,5,Legendre: trace ratios in families of elliptic
  curves"* (Experimental Mathematics) studies exactly **ratios/relations
  between Legendre-family traces and traces of fixed small curves** —
  **SIMILAR IN SPIRIT** to what a resolution of `S(p)` would need
  (comparing our family to a reference object), but the search snippet
  gives no formula matching `S(p)`'s specific `chi(t(t+1))`-twisted
  double-sum shape.
- A Jacobsthal-type identity specifically **"for `Q(sqrt(-2))`"** turned
  up (arXiv:1110.5815) — **structurally suggestive** given `chi(-2)`
  is exactly our controlling character, but not read in enough depth
  this round to confirm or rule out an exact match; flagged as the
  single most promising lead for a follow-up round, not claimed as a
  match.

**NOT FOUND:** no source located that states or evaluates the exact
double sum `S(p) = sum_{x,t} chi(x(x+1)t(t+1)(x+t))`, or the specific
self-twisted family `t(t+1)y^2=x(x+1)(x+t)`, in closed form. **No claim
of prior-work equivalence is made** — the literature confirms the
*toolkit* (Jacobi sums, finite-field hypergeometric) is the right one,
not that the *answer* is already written down somewhere found this round.

## Part V — Jacobi-sum / substitution route

Tried `x = t\cdot u` (t != 0): reduces cleanly to
`S(p) = \sum_{t\ne0}\chi(t)\chi(t+1)\sum_u \chi(u(u+1)(tu+1))`, and
further algebra (`u(u+1)(tu+1) = t\cdot u(u+1)(u+1/t)`) brings this back
to `S(p) = \sum_{s\ne0}\chi(s(s+1))g(s) = S(p)` — an honest **circular
identity**, not a new reduction (the substitution is a genuine symmetry
of the sum, verified algebraically, but adds no new information).

No factorization into a product or convolution of two independent
single-variable character sums (which would signal a true Jacobi-sum
`J(\chi,\chi)`-type closed form) was found. **Not proved to be
impossible** — only that the substitutions tried (multiplicative
rescaling by `t`, by `t+1`, projective normalization of `(x,t)`) did not
produce one in the time available.

## Part VI — finite-field hypergeometric framing

`a_t(p) = -\chi(-1)\,p\cdot {}_2F_1(\chi,\chi;\varepsilon;t)_p$
(Greene/Ono normalization) turns `S(p)` into a genuine
**`chi(t(t+1))`-twisted moment of a finite-field `_2F_1`, taken over the
whole base field `t\in F_p`** — a recognized object type in the
literature on finite-field hypergeometric functions (twisted moments of
${}_2F_1$/${}_3F_2$ values are an active research area). This framing is
used here only as **language that correctly classifies the problem**,
not as a shortcut to a value — no specific published twisted-moment
formula matching this exact twist (`t(t+1)`, i.e. weight `\chi` of the
base parameter times its own unit shift) was located.

## Part VII — geometric point-count interpretation (the main new finding this round)

`S(p) = \#V(F_p) - p^2` where `V: Y^2 = F(X,T)`,
`F(X,T)=X(X+1)T(T+1)(X+T)` (verified via the standard `1+\chi(f)` point
counting trick, exact, no approximation). Since `F` is symmetric in
`X,T` (`F(X,T)=F(T,X)`, checked directly), fibering over `T=t` gives, for
each `t`, the curve `Y^2 = t(t+1)\cdot X(X+1)(X+t)` — **the QUADRATIC
TWIST of `E_t` by the constant `t(t+1)` (a function of the base
parameter itself)**. So **`V` is the "self-twisted Legendre elliptic
surface"**: take the classical Legendre family and twist each fiber by a
specific function of its own modulus.

**Discriminant-degree check (rough classification signal, not a full
resolution).** The cubic `t(t+1)\cdot X(X+1)(X+t)` has discriminant
`[t(t+1)]^4\cdot t^2(t-1)^2 = t^6(t+1)^4(t-1)^2`, total degree **12** in
`t`. For a relatively minimal elliptic surface over `P^1` with section in
Weierstrass form, discriminant degree 12 is exactly the classical
signature of a **RATIONAL elliptic surface** (vs. 24 for K3). **This is a
plausible, motivated classification, not a completed one** — proper
minimalization (clearing the common `t(t+1)` scaling via a coordinate
twist, resolving the fiber at `t=\infty`, checking no further common
factor reduces the effective degree) was not carried out symbolically
this round. Reported as: **COMPUTATIONALLY/STRUCTURALLY SUGGESTIVE that
`V` is (birational to) a rational elliptic surface, not verified.**

**Why this classification would matter, if confirmed.** A genuinely
rational elliptic surface has `h^{2,0}=0` — no transcendental cohomology
— so by the (unconditional, for rational surfaces) Tate conjecture its
entire point-count deviation from `p^2` is `p` times the trace of
Frobenius acting on a *bounded*, finite-rank (rank <= 10 for extremal
rational elliptic surfaces) Néron–Severi lattice, an integer combination
of roots of unity, **not** a genuine unbounded-relative-to-`p` or
elliptic-modular-scale quantity. This would predict exactly the kind of
behavior observed: **`S(p)/p` bounded and non-decaying as `p` grows**
(confirmed in Part IX/X below), rather than either (a) growing without
bound or (b) decaying like `O(1/\sqrt p)` as it would for a hard,
genuinely transcendental (K3-type) contribution.

## Part VIII — attempt to prove the good-locus formula

**Not proved.** The rational-surface picture (Part VII) gives a
*plausible mechanism*: `S(p)/p = \text{Tr}(\text{Frob}_p\mid NS\otimes\mathbb Q)`
for a bounded lattice action, and the observed exact value `-\chi(2)`
(equivalently `\chi(-1)`, Round 9 Part II) on the good locus would then
correspond to Frobenius acting on (a piece of) that lattice by exactly
`+-1` times a sign character — consistent with, e.g., a **rank-1
eigenspace controlled by whether `-2` is a square mod `p`** (a "vanishing
eigenspace" story, per the round's own candidate list) — but no explicit
Néron–Severi basis, monodromy computation, or eigenspace derivation was
carried out. **This is a CONJECTURAL MECHANISM consistent with all data,
not a proof.** The domain being exactly `chi(-2)=-1` is *observed* to
coincide with "one eigenvalue" vs "more than one contributing eigenvalue"
in this picture, but that correspondence itself is not derived from
first principles this round.

## Part IX — bad locus, searched further

Round 9's `S(p) \propto 2a` (`p=a^2+2b^2`) hypothesis stays killed.
This round additionally tested, against 27 bad-locus primes up to 283:
`p mod 3`, `p mod 24`, `chi(3)`, `chi(-3)`, `chi(6)`, `chi(-6)` — **none
produce a clean sub-split** (e.g. all 8 primes with `p\equiv11\pmod{24}`
give `S(p)/p \in \{-2.27,0.39,-2.90,0.66,-1.47,-0.81,-2.97,0.86\}`, no
shared value, no visible finer dichotomy). **Killed: no simple small-
discriminant character or mod-24 refinement controls the bad locus.**

## Part X — statistical evidence (bad locus only, correctly normalized)

Normalizing by `p` (the scale implied by the Part VII rational-surface
hypothesis — a bounded Néron–Severi trace — **not** the elliptic-curve
`\sqrt p` Hasse scale, since `S(p)` is a moment/point-count-deviation
object, not a single curve's trace): across 27 primes, `5<=p<=283`,
`p\equiv1,3\pmod8`:
- mean `S(p)/p \approx -0.016` (statistically indistinguishable from 0),
- sample stdev `\approx 1.65`,
- range `[-2.96, 2.86]`,
- **no visible decay in magnitude as `p` grows** (large primes like
  233, 257, 283 give `|S/p|` comparable to small primes like 11, 17) —
  this specifically supports the "bounded, non-decaying" signature
  expected from Part VII's rational-surface picture, and argues
  *against* a decaying `O(1/\sqrt p)` transcendental-noise
  interpretation.

**Labeled STATISTICAL EVIDENCE only** — 27 points is not enough to claim
a specific limiting distribution, and no exact formula was recovered.

## Part XI — does the hierarchy become arithmetic?

**Partially supported.** Round 10 did not need to invoke a hard,
non-elementary (K3/modular-form-scale) arithmetic object to explain the
*shape* of the remaining difficulty — the working hypothesis is that the
unresolved core is governed by a **bounded, algebraic (Néron–Severi-
level) invariant of a specific rational elliptic surface**, which is
"arithmetic" in the sense of depending on how Frobenius acts on a finite
lattice, but is a considerably *tamer* kind of arithmetic than a generic
elliptic-curve trace or modular form coefficient would be. The
hierarchy is better stated as:
`local exact -> structural exact -> global symmetry -> bounded lattice arithmetic`,
with the important caveat that **the last step is a plausible hypothesis
from a discriminant-degree count, not a confirmed classification.**

## Everything killed this round

1. `S(p) \propto 2a` for `p=a^2+2b^2` — re-confirmed killed (Round 9),
   not resurrected.
2. `p mod 3`, `p mod 24`, `chi(3),chi(-3),chi(6),chi(-6)` as controlling
   characters for the bad locus — killed, no clean split found.
3. The idea that `t=-1` is a singular fiber of the curve (an easy-to-make
   error given it's weight-zero in `S(p)`) — explicitly checked and
   corrected: it is a *smooth*, arithmetically rich (CM, `j=1728`) fiber
   that simply never contributes to `S(p)` because its weight vanishes;
   the actual singular fibers are `t=0,1`.
4. Any claim that this round's literature search found the exact answer
   — explicitly not claimed; the search found the right toolkit and one
   promising but unconfirmed lead (`Q(sqrt(-2))` Jacobsthal identity),
   nothing more.

## Highest-value next question

**Determine whether `V: Y^2=X(X+1)T(T+1)(X+T)` (or its minimal resolved
model) is genuinely a rational elliptic surface**, by either (a) writing
an explicit minimal Weierstrass model over `F_p(T)` and computing its
Kodaira fiber types and Euler number directly, or (b) reading the
`Q(\sqrt{-2})` Jacobsthal-identity paper (arXiv:1110.5815) in full to
check whether it already evaluates exactly this twisted family. Either
would convert this round's plausible mechanism into an actual proof of
the good-locus formula and very likely reveal the bad locus's true
controlling invariant at the same time.
