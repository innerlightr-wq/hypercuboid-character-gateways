# Hypercuboid exploration — Round 14 working notes

## Part I — freeze (PROVED, reconfirmed, no discrepancy)

Re-verified Round 11's Weierstrass model, `c4,c6,Delta,j`, minimality,
the four Kodaira fibers (`I_2^*,I_2,I_0^*,I_2^*`), Euler number 24 (K3),
the rational `(\mathbb Z/2)^2` torsion, and the Shioda–Tate bound
`\rho\in\{19,20\}`. No discrepancy — proceeded.

## Part II — trivial lattice (PROVED, exact)

Root-lattice contributions: `I_2^*\to D_6`, `I_2\to A_1`, `I_0^*\to D_4`,
`I_2^*\to D_6`. Trivial lattice:
$$\mathrm{Triv}(X) = U\oplus D_6\oplus A_1\oplus D_4\oplus D_6.$$
$$\mathrm{rank}=2+6+1+4+6=19\quad(\text{matches Shioda-Tate's }2+\textstyle\sum(m_v-1)=19\text{ exactly}).$$
Discriminants (`\mathrm{disc}(U)=-1`, `\mathrm{disc}(D_n)=4`,
`\mathrm{disc}(A_1)=2`): $$\mathrm{disc}(\mathrm{Triv})=(-1)\cdot4\cdot2\cdot4\cdot4=-128,\qquad|\mathrm{disc}(\mathrm{Triv})|=128.$$
**PROVED, exact arithmetic, no approximation.**

## Part III — effect of `(\mathbb Z/2)^2` torsion (PROVED, standard formula applied)

Standard Shioda relation: `|\mathrm{disc}(NS)| = |\mathrm{disc}(\mathrm{Triv})|\cdot\det(\text{MW}_{\text{free height pairing}})/|\mathrm{MW}_{\text{tors}}|^2`,
with `|\mathrm{MW}_{\text{tors}}|^2=16`:

**Case A (`\mathrm{rank\,MW}=0`, `\rho=19`):**
$$|\mathrm{disc}(NS)| = 128/16 = 8.$$
`T(X)` would have **rank 3**, `|\mathrm{disc}(T(X))|=8`.

**Case B (`\mathrm{rank\,MW}=1`, `\rho=20`):**
$$|\mathrm{disc}(NS)| = 128\cdot h(P)/16 = 8\,h(P)$$
for the canonical height `h(P)` of a generator. `T(X)` would have
**rank 2** (signature `(2,0)`, positive definite — matches the general
theory for a singular K3 exactly).

## Part IV — candidate `T(X)` from the CM form, and a striking numerical coincidence

Classical fact (Shioda–Inose 1977; the correspondence between singular
K3 surfaces and `\mathrm{SL}_2(\mathbb Z)`-classes of positive-definite
even binary quadratic forms): the transcendental lattice for the
(unique, since `h(-8)=1`) singular K3 attached to CM discriminant `-8`
is the **principal form**, `T(X)=\begin{pmatrix}2&0\\0&4\end{pmatrix}`
(representing `2(x^2+2y^2)`), with
$$|\mathrm{disc}(T(X))| = 4\cdot2\cdot4-0^2\big/\text{(matches }4ac-b^2=8\text{ for }a=1,b=0,c=2)=8.$$

**This is exactly `8`, matching Case A's computed `|\mathrm{disc}(NS)|=8`
as a bare number** — but Case A has `\rho=19` (`T` rank 3), a *different*
lattice shape than the rank-2 principal form; the numerical coincidence
`8=8` there is **not** meaningful by itself (comparing a rank-3 and a
rank-2 discriminant as raw integers proves nothing group-theoretically).
**The meaningful consistency check is Case B**: if `\rho=20` and the
Mordell–Weil generator has canonical height **exactly `h(P)=1`**, then
`|\mathrm{disc}(NS)|=8\cdot1=8`, **matching the expected `|\mathrm{disc}(T(X))|=8`
exactly** (using `|\mathrm{disc}(NS)|=|\mathrm{disc}(T)|` for orthogonal
complements in the unimodular K3 lattice — PROVED, standard lattice
fact). **This is a real, derived consistency condition, not a guess: IF
`\rho=20`, the theory *requires* `h(P)=1` for our `X` to be the
discriminant-8 singular K3 (not merely `T(X)` having *some* even
positive-definite Gram matrix of *any* small discriminant).**

## Part V — Picard-rank bounds by reduction: NOT COMPLETED (honest gap)

A van Luijk-style argument needs, at two or more primes of good
reduction: (a) the *exact* point count `\#X(\mathbb F_p)` and
`\#X(\mathbb F_{p^2})` for the smooth *projective resolved* model (not
just `S(p)`, which is only related to it via the still-incomplete Part
X bookkeeping), and (b) an independent determination of the algebraic
(Picard) rank of the *reduced* surface over `\mathbb F_p` (via explicit
divisor classes visible in each reduction) so that discriminants of the
two reduced Picard lattices can be compared mod squares. **Neither (a)
nor (b) was computed this round** — this is a substantial additional
computation (requiring, at minimum, the affine/projective bookkeeping
from Part X to even state `\#X(\mathbb F_p)` correctly) that was not
completed. **NOT ATTEMPTED TO COMPLETION — explicitly flagged rather
than approximated.**

## Part VI — Mordell–Weil rank: still open, with one useful combinatorial check

**No non-torsion section found** (Round 12 already excluded degree
`\le2`; this round did not extend the polynomial-ansatz search, per the
instruction to prioritize the lattice argument over more brute force).
Instead, tested whether `h(P)=1` (the value Part IV shows is *required*
if `\rho=20` and `X` is the discriminant-8 surface) is even
**combinatorially reachable** under Shioda's height formula for a K3
(`\chi=2`): `h(P)=4+2(P\cdot O)-\sum_v\mathrm{contr}_v(P)`. Taking
`P\cdot O=0` (a section disjoint from the zero section, the generic
case) and enumerating the standard Tate/Shioda local-contribution values
at each fiber (`I_2^*`: `\{0,1,1.5\}`; `I_2`: `\{0,0.5\}`; `I_0^*`:
`\{0,1\}`; second `I_2^*`: `\{0,1,1.5\}`) gives 8 distinct achievable
positive heights: `\{0.5,1,1.5,2,2.5,3,3.5,4\}`. **`h(P)=1` is on this
list** (e.g. via corrections `1.5+0.5+1+0` or `1+0+1+1` or `1.5+0+0+1.5`
summing to the required total `3`) — **not excluded, but also not
uniquely forced**: it is one of 8 combinatorially valid values, so this
is **moderate, not strong, consistency evidence**, reported honestly at
that strength. **MW rank remains undetermined; no section exhibited.**

## Part VII — Shioda–Tate consistency triangle (two of three legs available, one entirely missing)

1. **Fiber lattice + torsion** (Parts II–III): gives `|\mathrm{disc}(NS)|=8`
   (rank 19) or `8h(P)` (rank 20) — **computed exactly**.
2. **`T(X)` from the CM form** (Part IV): predicts `|\mathrm{disc}(T)|=8`
   for the rank-2 case specifically — **derived from cited classical
   theory**, contingent on the (unproved) claim that our `X` is
   literally the discriminant-8 singular K3.
3. **Picard-rank information from reductions** (Part V): **entirely
   missing** — this leg was not computed.

**With only two of three legs available, this does *not* constitute a
proof of rank or discriminant** — it constitutes a **necessary
condition** (`h(P)=1` if `\rho=20`) that is consistent with, but does not
establish, the singular-K3 picture. **Conservative conclusion, exactly
as instructed: no triangle closure achieved.**

## Part VIII — Shioda–Inose/Kummer possibility (uniqueness argument found, construction not found)

**Key structural point, PROVED given the (still conditional) premises**:
the class number of discriminant `-8` is **`h(-8)=1`** (classical,
`\mathbb Z[\sqrt{-2}]` is a PID). By the Shioda–Inose bijection (Part
IV), **there is exactly one singular K3 surface (up to isomorphism)
with `|\mathrm{disc}(T)|=8`**, and by Shioda–Inose's structure theorem
every singular K3 is (birational to / admits a Shioda–Inose structure
with) `\mathrm{Km}(E_1\times E_2)` for CM curves `E_1,E_2` **isogenous**
to each other with the appropriate discriminant — for the *unique*
discriminant-8 surface, `E_1,E_2` are both curves with CM by
`\mathbb Z[\sqrt{-2}]$, i.e. (up to isogeny/twist) both our `E`. **So:
IF `X` has `\rho=20` and `|\mathrm{disc}(NS)|=8`, THEN, by uniqueness
alone (no explicit map needed), `X` is Shioda–Inose related to
`\mathrm{Km}(E\times E)`** — a genuine strengthening over Round 12/13's
"consistent hypothesis" language, because it replaces "we would need to
construct a map" with "uniqueness of the classification forces it,
once the two numerical facts (`\rho=20`, `\mathrm{disc}=8`) are known."
**No explicit Nikulin involution or degree-2 map was constructed** —
the argument is existence-by-uniqueness, not construction. **This is
still conditional on the unproved `\rho=20`.**

## Part IX — modular attachment (conditional chain, now fully spelled out)

Combining Parts IV, VIII and the cited Livné/Schütt theorem (Round 13
Part V): **IF `\rho(X)=20` and `|\mathrm{disc}(NS(X))|=8`, THEN by
uniqueness `X`'s transcendental Galois representation is rigorously
(by Livné's theorem, a proved general result — not fitted) the one
attached to the unique rational weight-3 CM newform for discriminant
`-8`, which is `8.3.d.a`.** No separate check of determinant/conductor/
nebentypus is needed beyond this uniqueness argument (there is only one
candidate newform, already confirmed in Round 13). **The entire
modular-attachment question has been reduced, rigorously, to the single
numerical fact `\rho=20` (with `\mathrm{disc}(NS)=8`, equivalently
`h(P)=1`) — this is a genuine tightening of the logical structure since
Round 13, even though the fact itself remains unproved.**

## Part X — affine/projective bookkeeping: deferred, per the round's own priority instruction

Not attempted this round, as instructed ("do not sacrifice the primary
Picard-rank/lattice objective"). Status unchanged from Round 12/13.

## Part XI — aggressive falsification: no contradiction found

- Trivial-lattice arithmetic double-checked (integer discriminants,
  correct rank, matches Shioda–Tate independently) — no error found.
- Case A's `|\mathrm{disc}|=8` and Case B's required `h(P)=1` were
  checked against the height-formula's combinatorial range — **`h(P)=1`
  is achievable, not excluded**. Had it been *excluded* (outside the
  achievable set `\{0.5,\dots,4\}`), that would have been a genuine,
  immediate contradiction of the `\rho=20`/discriminant-8 hypothesis —
  **this did not happen.**
- No reduction data was computed (Part V), so no reduction-based
  contradiction was possible to find *or* rule out this round.
- **No ad hoc twist was introduced anywhere to force agreement** — every
  number reported here follows from the stated lattice formulas without
  adjustment.

## Part XII — structural interpretation (tested against this round specifically)

Round 14 supports the offered interpretation **only partially, and the
distinction matters**: "progressively remove incidental degrees of
freedom until governed by a smaller, more globally rigid arithmetic
object" describes Rounds 1–13 well (elementary rules removed easy cases;
what remained needed a K3; what remained *of that* needed a modular
form). **But Round 14's own results show the final object is not
merely "smaller and more rigid" — it may be *unique in its isomorphism
class* (by class-number-one uniqueness, Part VIII), which is a
qualitatively stronger kind of rigidity than "governed by a global
arithmetic law" alone would suggest.** Where the interpretation is
**not** supported by this round: rigidity of the *target* object (the
singular K3, if it is one) does not imply rigidity of *access* to it —
Round 14's central finding is that even a maximally rigid, unique,
class-number-one target can remain computationally out of reach (no
section found, no reduction computed) without more machinery. **The
interpretation survives as a description of the mathematical objects
involved; it does not predict or explain why the last step remains hard
to verify by hand.**

## Everything killed or corrected this round

1. **Clarified, not killed**: the apparent "coincidence" that Case A's
   `|\mathrm{disc}(NS)|=8` matches the candidate `T(X)` discriminant
   is a **false pattern** — Case A is rank 19 (`T` rank 3), a different
   lattice shape; the matching integer means nothing on its own.
   Corrected to focus on Case B's genuine, rank-consistent condition
   (`h(P)=1`).
2. **Not killed**: `\rho=19` — still fully consistent with everything
   computed this round; not excluded by any lattice or combinatorial
   argument found.
3. **Not killed**: `h(P)=1` — shown achievable, not proved to occur.
4. **New, rigorous (conditional) result**: the uniqueness argument (Part
   VIII) — this specific logical strengthening (class-number-one forces
   identification without needing an explicit map) was not present in
   Rounds 11–13 and is a genuine addition this round.

## Highest-value next question

Exactly as in Round 13, but now sharpened to a single numeric target:
**does a Mordell–Weil generator of canonical height exactly `1` exist?**
Given Part VI's combinatorial analysis, a productive next step is to
enumerate which of the 8 achievable local-contribution combinations
summing to `h=1` corresponds to a section meeting *specific* fiber
components, then search for a low-height section constrained to meet
*exactly those* components (a much more targeted search than an
undirected polynomial ansatz) — or, in parallel, attempt the van Luijk
reduction argument (Part V) now that the affine/projective bookkeeping
(Part X) is the only remaining prerequisite for computing an honest
`\#X(\mathbb F_p)`.

## Required-report items not otherwise covered above

- **Exact `NS(X)`**: not determined (rank and generators both open).
- **Exact `T(X)`**: not determined for `X` itself; the *candidate*
  (`\mathrm{disc}=8`, principal form) is derived from classical theory
  contingent on `\rho=20`.
- **Updated status of `S(p)=\chi(-1)(a_p(f)+p)`**: unchanged from Round
  13 — COMPUTATIONALLY VERIFIED ONLY; this round worked entirely on the
  geometric side and did not add new prime tests (per the round's own
  instruction not to accumulate more matches).
