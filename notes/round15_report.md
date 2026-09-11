# Hypercuboid exploration — Round 15 working notes

## Part I — freeze (PROVED, reconfirmed)

Re-verified the Weierstrass model, minimality, Kodaira fibers
(`I_2^*,I_2,I_0^*,I_2^*`), `(\mathbb Z/2)^2` torsion,
`\mathrm{rank}(\mathrm{Triv})=19`, `|\mathrm{disc}(\mathrm{Triv})|=128`,
and the `(\rho,\mathrm{rank\,MW})\in\{(19,0),(20,1)\}` alternative — all
unchanged from Round 14, no discrepancy.

## Part II — admissible height-1 fiber-component patterns (PROVED, complete enumeration)

Using the standard local-contribution values (derived from the
multiplicity-1-only rule: a section can only meet a fiber component of
multiplicity 1, since `P\cdot F=1=\sum m_i(P\cdot\Theta_i)` forces the met
component to have `m_i=1`):
- `I_2^*` (D6, 4 mult-1 components): `\{0\text{(O)}, 1\text{(N)}, 1.5\text{(F1)}, 1.5\text{(F2)}\}`
- `I_2` (A1, 2 components): `\{0\text{(O)}, 0.5\text{(N)}\}`
- `I_0^*` (D4, 4 mult-1 components): `\{0\text{(O)}, 1\text{(N1)}, 1\text{(N2)}, 1\text{(N3)}\}`
- `I_2^*` (second copy, at `t=\infty`): same as the first.

Assuming `P\cdot O=0` (generic, not the zero section), `\hat h(P)=1`
requires `\sum\mathrm{contr}_v(P)=3` exactly (from `\hat h=4-\sum`).
**Exhaustive enumeration (`scripts` inline, all `4\times2\times4\times4=128`
tuples checked): exactly 23 admissible component patterns achieve
`\sum=3`** (full list recorded in the session; representative examples:
`(O,N,N_i,F_j)`, `(N,O,N_i,N)`, `(N,N,O,F_j)`, `(F_i,O,O,F_j)`,
`(F_i,N,O,N)`, `(F_i,N,N_j,O)`, for `i,j\in\{1,2\}` and the three `N_i`
at `I_0^*`). **PROVED complete for this enumeration** (a pure
combinatorial fact given the stated per-fiber value sets).

## Part III — component constraints → valuation constraints: **NOT COMPLETED RIGOROUSLY (honest gap)**

Translating each of the 23 abstract patterns into precise local
pole/zero-order and congruence conditions on `x(t),y(t)` requires a full
Tate's-algorithm blow-up tracking at each of the four bad fibers (which
specific sequence of blow-ups produces which named component, and what
that means for the valuation of `x-x_0` or `x` itself in the original
non-resolved model). **This was not carried out with full rigor this
round** — attempting it from memory risks silently encoding an error
into the search ansatz, which would be worse than an honest gap. Instead
(Part V), a **direct computational search** was run without first fixing
which of the 23 patterns to target, checking candidates for the perfect-
square condition directly and (had one been found) determining its
actual component pattern *afterward* by inspecting valuations of the
found `x(t)` at `t=0,1,-1,\infty` — a valid, rigorous, but less
targeted approach than the round's suggested order. **Explicitly
flagged: Parts III/IV's intended derivation is incomplete; Part V below
substitutes a broader direct search instead.**

## Part IV — minimal degree: not derived from first principles, addressed empirically instead

Because Part III was not completed, the minimal degree forced by the
height-1 constraints was **not derived**. Instead, Part V searched
degrees 3 and 4 directly (the natural next steps after Round 12's
degree-`\le2` exclusion), plus two natural low-complexity
rational-function ansätze with poles at the bad fibers.

## Part V — structured search results (all NEGATIVE, reported precisely, `scripts/round15_section_search.py`)

1. **Degree-3 polynomial `X(t)=At^3+Bt^2+Ct+E`.** Leading (degree-9)
   coefficient of the RHS is `A^2(A+1)`, forcing `A\in\{0,-1\}`.
   `A=0` reduces to Round 12's already-excluded linear case.
   `A=-1`: RHS factors exactly as
   `(t^3-Bt^2-Ct-E)(({B+1})t^2+Ct+E)(t^3-(1+B)t^2-(1+C)t-E)`
   (degrees 3,2,3). **Proved algebraically that the two cubic factors
   can never coincide** (`-B=-(1+B)` is impossible), removing the
   simplest route to a perfect square. **Exhaustive check over integer
   `B,C,E\in[-6,6]^3` (2197 combinations): zero real (`\mathbb Q`-rational)
   solutions.** One spurious hit at `(B,C,E)=(-2,-1,0)`
   (`X=-t(t+1)^2`) gives `RHS=-t^4(t+1)^4` — a **negative** perfect
   square, i.e. `Y=i\,t^2(t+1)^2`, a point defined over `\mathbb Q(i)(t)`,
   **not** a `\mathbb Q(t)`-rational section — correctly identified and
   excluded (a genuine near-miss, caught by requiring the leading
   numeric content of the factorization to itself be a positive perfect
   square, a check that was *not* present in a first draft of the
   search code and was added after this exact false positive appeared).
2. **Degree-4 polynomial, leading coefficient `\pm1`, other coefficients
   in `[-3,3]^4`** (4802 combinations): zero perfect squares found.
3. **`X(t)=(At^2+Bt+C)/t^2`** (pole of order 2 at `t=0`, motivated by
   several of Part II's 23 patterns requiring a non-identity component
   at that fiber), `A,B,C\in[-4,4]`, `A\ne0` (648 combinations): zero
   perfect squares found.
4. **`X(t)=(At^2+Bt+C)/(t+1)^2`** (pole at `t=-1`), same range (648
   combinations): zero perfect squares found.

**Total: 4 distinct, well-motivated search classes, ~8300 combinations,
zero non-torsion sections found.** This is a substantial negative
result but is **explicitly not exhaustive**: rational (non-integer)
coefficients, larger integer ranges, denominators of the form `t(t+1)`
or degree 3, and degree-5+ ansätze were **not** tried.

## Part VI — 2-torsion translation cross-check

Not exercised this round since no candidate section was found to
translate. (Method remains available for a future round once/if a
candidate appears.)

## Part VII — N/A

No candidate section was found; none of the 8-step verification
protocol applies.

## Part VIII/IX — N/A (conditional on Part VII)

Not reached.

## Part X — per the round's own instruction: **do not conclude `\rho=19`**

The search was **not exhaustive** (Part V), so, exactly as instructed,
**no conclusion that `\mathrm{rank\,MW}=0}` or `\rho=19` is drawn**. The
search classes exhausted were: polynomial degree `\le4` (with the
degree-3/4 leading-coefficient constraints derived, not guessed) and two
natural low-order pole ansätze. **Not exhausted**: any rational function
with a degree-`\ge2` denominator polynomial other than `t^2` or `(t+1)^2`
(e.g. `(t(t+1))^2` or `(t-1)^2`-type poles at other points), coefficients
outside `[-6,6]`/`[-4,4]`, and degree `\ge5` numerators.

## Part XI — reduction-based cross-check: **not attempted**

As in Round 14, a rigorous van Luijk-style Picard-rank bound needs the
affine/projective bookkeeping (still incomplete since Round 12) to even
state `\#X(\mathbb F_p)` correctly for the smooth projective model, so
this was not attempted this round (consistent with the round's own
instruction to keep this secondary, and with there being no completed
prerequisite for it).

## Part XII — master-identity status: unchanged

`S(p)=\chi(-1)(a_p(f)+p)` remains **COMPUTATIONALLY VERIFIED ONLY**
(Round 13 status). Since no geometric progress on `\rho` was achieved
this round (only a substantiated negative search), there is nothing new
to update here, and — per the round's explicit instruction — the modular
trace question and the affine/projective bookkeeping question are kept
**distinct**, neither collapsed into the other.

## Part XIII — falsification checks performed

- Every "hit" from the perfect-square search was checked for **sign of
  the leading numeric content** (catching the `Y=i\,t^2(t+1)^2` false
  positive) — this is itself a real falsification catch, not a
  hypothetical one.
- All degree-3/4 candidates were required to satisfy the Weierstrass
  equation exactly via `sympy.expand`, not floating-point root-finding.
- No candidate survived to the point of needing torsion-orbit,
  height, or reduction checks (none were found).

## Everything killed or corrected this round

1. **Killed (extended)**: non-torsion sections with `x(t)` a polynomial
   of degree `\le4$ (leading coefficient `\pm1$ for degree 4) with
   integer coefficients in the tested ranges, and with `x(t)` a simple
   rational function with a double pole at `t=0` or `t=-1$ in the
   tested integer range.
2. **Caught and corrected (methodological)**: an initial version of the
   perfect-square search accepted `-1\times(\text{perfect square})` as
   a hit (missing the leading-sign/content check) — found by manual
   verification of the one hit it produced (`X=-t(t+1)^2`, RHS
   `=-t^4(t+1)^4$, a point over `\mathbb Q(i)(t)`, not `\mathbb Q(t)`) and
   fixed before further searches were run. **Consistent with the
   project's standing discipline of not trusting a computational hit
   without direct symbolic verification.**
3. **Not killed**: `\rho=19` — still fully open, explicitly not
   concluded despite the negative search, per the round's own
   instruction.
4. **Not killed**: `\rho=20` / `\hat h(P)=1` — still fully open; the
   negative search narrows *where* a low-complexity section could live,
   without excluding higher-complexity ones.

## Highest-value next question

Complete Part III properly: carry out (or find in a reference) the
actual Tate's-algorithm component identification at `t=0,1,-1,\infty`
for this specific Weierstrass model, so that a *targeted* valuation
ansatz (rather than an untargeted polynomial/rational-function sweep)
can be constructed for one of the 23 admissible height-1 patterns from
Part II — this is likely to be far more efficient than further blind
degree/coefficient-range expansion of the search performed this round.

## Required-report items

1. **Admissible height-1 patterns**: 23, enumerated in Part II.
2. **Degree/pole constraints derived**: only the elementary leading-
   coefficient conditions (`A\in\{0,-1\}` at degree 3; automatic even
   degree at degree 4) — the finer Tate's-algorithm-based constraints
   were not derived (Part III gap).
3. **Search space examined**: degree-3 polynomial (`A=-1$, `B,C,E\in[-6,6]`),
   degree-4 polynomial (leading `\pm1`, others in `[-3,3]`), and two
   double-pole rational-function ansätze (`A,B,C\in[-4,4]`) — roughly
   8300 combinations total, all via exact symbolic (not floating-point)
   perfect-square checks.
4. **Non-torsion section found?** **No.**
5. **Exact coordinates**: N/A.
6–10. N/A (no section; MW rank, `\rho`, `NS`, `T(X)` all remain exactly
   as constrained in Round 14: `\rho\in\{19,20\}`, conditional
   `|\mathrm{disc}(NS)|\in\{8,\,8\hat h(P)\}`).
11. **Discriminant-8 uniqueness theorem**: still only conditionally
    applicable (requires `\rho=20`, not established).
12. **Is `8.3.d.a` rigorously attached?** No — unchanged, conditional.
13. **Master identity status**: unchanged, COMPUTATIONALLY VERIFIED ONLY.
14. **Reduction-based check**: not attempted (Part XI).
15. **Killed/corrected**: see above (methodological catch on the sign
    check; extended-but-still-partial negative section search).
16. **Highest-value next question**: as stated above.

**Verdict: ROUND15-C** — the structured search substantially narrows
the possibilities (23 admissible abstract patterns identified; roughly
8300 low-complexity candidate sections exhaustively ruled out across
four natural ansatz classes, with one methodological error caught and
fixed along the way) — but no non-torsion section is proved to exist or
not exist, and per the round's own instruction, `\rho=19` is **not**
concluded from the negative search.

**THE THREE MOST IMPORTANT THINGS WE LEARNED**
- We now know exactly *which* 23 specific "landing patterns" a
  height-1 generator point would need to have, turning a vague
  geometric question into a concrete, finite checklist — even though we
  haven't yet found which (if any) of the 23 is realized.
- We searched a substantial, honestly-bounded set of natural candidate
  points (roughly 8000+) and found none that work, which is useful
  negative information, but we're explicit that this is not the same as
  proving no such point exists — the search wasn't exhaustive, and we
  are not claiming more than we found.
- We caught our own tool making a subtle mistake (accepting a "negative
  perfect square," which secretly meant an imaginary-number solution,
  as if it were a real one) before it could contaminate the result —
  another example of the checking discipline this whole project has
  leaned on paying off.

Stopping here per the round's instructions — no further action taken.
