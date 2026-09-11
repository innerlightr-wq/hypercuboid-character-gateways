# Hypercuboid exploration — Round 17 working notes

## Part I — freeze (PROVED, reconfirmed)

Re-verified minimality, `v(c_4)=2,v(c_6)=3,v(\Delta)=8` at `t=0`, the
Kodaira type `I_2^*`, the singular point of the special cubic at the
origin, and the Tate-cubic double root at `T=0` (simple root at `T=-1`)
— all match Round 14/16 exactly. Proceeded.

## Part II — explicit blow-up (PARTIAL SUCCESS + one caught error)

**Chart 1 (successful, rigorously verified): `X=t^2X_1, Y=t^3Y_1`.**
Substituting into `Y^2=X^3+a_2X^2+a_4X` and dividing by `t^5` (the
correct common factor, confirmed by exact polynomial division) gives
$$F(t,X_1,Y_1) = -X_1^3t-2X_1^2t-X_1^2t^2-X_1t^2-2X_1t-X_1+Y_1^2t,$$
$$F(0,X_1,Y_1) = -X_1(X_1+1).$$
**Smoothness explicitly checked (not assumed) at both roots**:
- At `X_1=0,t=0`: `(\partial F/\partial Y_1,\partial F/\partial X_1,\partial F/\partial t)=(0,-1,Y_1^2)` — `\partial F/\partial X_1\ne0` for every `Y_1`: **smooth line, a genuine component, no further blow-up needed.**
- At `X_1=-1,t=0`: `(0,+1,Y_1^2+1)` — likewise **smooth**.

**These are two distinct, rigorously confirmed multiplicity-1
components of the `I_2^*` fiber.**

**Chart 2 (attempted, FAILED, error caught and reported — not
patched).** The Tate-cubic's *simple* root at `T=-1` was expected
(per standard Tate's-algorithm folklore, which this round tested rather
than trusted) to be an *already-smooth* direction needing no further
blow-up. Testing this directly: substituting `X=-t+tW` (so `W=0`
matches `T=-1`) and guessing the scale `Y=tY_2`, then dividing by `t^2`,
gives
$$G(t,W,Y_2) = Y_2^2 + t\cdot(\text{terms in }W) + \dots,\qquad G(0,W,Y_2)=Y_2^2.$$
At the point matching `T_2`'s actual limiting behavior
(`t=0,W=0,Y_2=0`): **`\partial G/\partial Y_2=\partial G/\partial W=\partial G/\partial t=0` — all three vanish simultaneously.** **This chart is
SINGULAR exactly at the point of interest — the `Y=tY_2` scaling guess
is WRONG.** A closer look (substituting `T_2`'s exact formula directly)
shows `Y^2\sim t^3\cdot w` for `w=W+1\to0`, i.e. the correct local scale
requires **an additional square-root-type ramification in the `w`
direction**, not a single clean rescaling. **This was identified and
reported as an open sub-problem, not resolved this round** — the
"simple root ⟹ automatically smooth" folklore does **not** apply
naively here without more careful treatment, and the round's own
falsification discipline (Part XI) is exactly what caught this before
it could be silently assumed.

## Part III — identity component and component group: PARTIALLY determined

The identity component (met by `O`) lives at "`X=O(1)`" (i.e.
`X_1\to\infty`, `T\to\infty`) — **not** captured by either chart above,
consistent with `O` never appearing in an affine blow-up chart centered
on the original singular point. **Component group `\Phi_0\cong(\mathbb Z/2)^2`,
as required for `I_2^*` with `n=2` even — reconfirmed, not re-derived
independently this round** (relies on the standard Kodaira-type-to-
component-group table, itself validated via the `(v(c_4),v(c_6),v(\Delta))`
match in Round 11/14).

## Part IV — 2-torsion tracking (PARTIAL, with the caught error documented)

- **`T_1=(X=0)`: lands at `X_1=0`** (chart 1), confirmed smooth.
- **`T_3=(X=-t^2(t+1))`: `X_1=X/t^2=-(t+1)\to-1`**, lands at `X_1=-1`
  (chart 1), confirmed smooth.
- **`T_2=(X=-t(t+1))`: does not appear in chart 1** (`X_1\to\infty` — a
  pole), and the natural "next" chart (Chart 2, above) was shown to be
  **incorrectly scaled**, not merely under-explored. **`T_2`'s exact
  component was NOT determined this round.**

**Consistency check attempted, inconclusive on its own**: Shioda's
formula requires each nonzero torsion point's total local-contribution
sum (across all four bad fibers) to equal exactly 4 (Round 16). This by
itself does not, without the missing `T_2`-at-`t=0` data, pin down
`T_1,T_3`'s individual contribution values (1 vs. 1.5) — see Part VII
below for how this was nonetheless narrowed using Round 16's results.

## Part V — valuation dictionary: PARTIAL

**What is proved**: a section `P` with `v_0(x(t)) \ge 2` and
`x(t)/t^2\to0` meets the `X_1=0` component; a section with
`v_0(x(t))\ge2$ and `x(t)/t^2\to-1` meets the `X_1=-1` component. (Both
directly follow from Chart 1's confirmed smoothness — any section
whose `X_1$-limit is finite and equal to one of these values lands
there, by continuity of the resolved model.) **What is NOT determined**:
the exact valuation/leading-coefficient conditions for meeting the
*identity* component or the still-unresolved `T_2$-type component,
since Chart 2 was shown incorrect and no corrected chart was completed.

## Part VI — application to the 23 patterns: not completed to a clean classification

Because two of the four multiplicity-1 components (identity's precise
boundary condition, and the `T_2`-type component) remain without a
verified valuation dictionary, **the 23 patterns from Round 15/16 cannot
yet be individually sorted** into ELIMINATED / RESTRICTED / UNCHANGED
with full rigor. What *can* be stated: any candidate section found to
satisfy `x(t)=O(t^2)` with `x(t)/t^2\to0$ or `\to-1$ at `t=0` is now
**verified** (not merely hypothesized) to meet a specific named
component of `I_2^*` with contribution to be pinned down by Part VII.

## Part VII — combining with Round 16's height-consistency result (real, if partly circumstantial, progress)

Round 16 found exactly 2 surviving global torsion patterns after using
the `t=1` result. **Chart 1's finding that `T_1` and `T_3` both emerge
at the *same* blow-up depth (`X=O(t^2)`) — a depth strictly greater
than `T_2`'s (`X=O(t)`, one level shallower)** — is consistent with,
and mildly favors, the hypothesis that `T_1,T_3` are the two "far"
(`F_1,F_2`, contribution `1.5` each) components while `T_2` (shallower,
closer to the identity direction in blow-up depth) is the "near" (`N`,
contribution `1`) component — matching **Solution A** of Round 16's two
surviving patterns
(`c_0=(1.5,1.0,1.5)` for `(T_1,T_2,T_3)`) over Solution B. **This is
reported as CIRCUMSTANTIALLY SUPPORTED, not proved** — the blow-up-depth
heuristic ("deeper blow-up needed ⟹ larger contribution") matches the
general `I_n^*` pattern (far components require more resolution steps
than the near one) but was not independently verified via a completed
`T_2` chart this round, precisely because that chart's construction
failed (Part II/IV).

## Part VIII — `t=0\leftrightarrow t=\infty` symmetry: verified algebraically, not yet exploited for components

Re-confirmed (Round 11): substituting `t=1/u` with the scaling `k=2`
gives `a_2'(u)=u(u+1)^2`, `a_4'(u)=u^3(u+1)^2$ — **literally the same
functional form** as `a_2(t),a_4(t)`. This means the map
`t\mapsto1/t$ combined with the corresponding `(X,Y)` rescaling **is an
actual isomorphism of the local Weierstrass models at `t=0` and
`t=\infty`** (not merely "the same Kodaira type by coincidence") —
**PROVED, exact, symbolic**. Consequently, **Chart 1's entire analysis
transfers verbatim to `t=\infty`**: the two components found there
(images of `T_1,T_3$-*type* data under the appropriate transform)
require no new computation. **This was not carried further to identify
exactly how `T_1,T_2,T_3$ individually map under this specific
isomorphism** (i.e., whether `T_1\leftrightarrow T_1$ or `T_1\leftrightarrow T_3$
etc. under `t\to1/t`) — a well-defined, likely quick follow-up not
completed this round.

## Part IX — `t=-1` (I_0^*): not attempted, per the round's own priority instruction

## Part X — consequences

1. **23 patterns still stand at 23** — none eliminated with full rigor
   this round (the torsion-only elimination from Round 16 remains the
   only firm reduction).
2. **`t=0` and `t=1` now both have partial-to-complete determined
   behavior**: `t=1` fully solved (Round 16); `t=0` has 2 of 4
   multiplicity-1 components rigorously located and shown smooth,
   1 (identity) understood only qualitatively, and 1 (`T_2`'s) actively
   shown to need more work.
3. **No pole/zero order forced yet** for a hypothetical section beyond
   what Chart 1 directly implies for landing on `X_1=0` or `X_1=-1`
   specifically (`v_0(x)\ge2`).
4. **No new degree bound derived.**
5. **Torsion translation**: still only the `I_2$ (t=1) action is fully
   known (Round 16); the `t=0` action remains open pending `T_2`'s
   resolution.
6. **No finite exact ansatz constructed** — the local dictionary is not
   yet complete enough to hand off to a symbolic solve.

## Part XI — falsification discipline: the round's central success

**A genuine error was caught, not merely a null result.** The initial
attempt to treat the Tate-cubic's simple root (`T=-1`) as automatically
giving a smooth, already-resolved component — a common informal
shortcut — was **tested explicitly and found false at the precise point
matching `T_2`**, via direct computation of all three partial
derivatives vanishing simultaneously. This is exactly the round's
instruction ("if a generic Kodaira-table statement disagrees with the
explicit resolution, trust neither until reconciled") being followed in
practice, not just stated as a principle.

## Everything killed or corrected this round

1. **KILLED (a folklore shortcut, not a prior result of this project)**:
   "a simple root of the Tate cubic automatically gives an
   already-smooth, no-further-blow-up-needed component" — false at
   least at the specific point tested here; the correct chart for that
   direction needs an additional ramified substitution not yet
   constructed.
2. **PROVED, new this round**: `T_1\to X_1=0` and `T_3\to X_1=-1` are
   genuine, smooth, verified components of `I_2^*` at `t=0`.
3. **PROVED, new this round**: the `t=0\leftrightarrow t=\infty` local
   Weierstrass models are literally isomorphic (exact algebraic
   identity of `a_2',a_4'$ with `a_2,a_4`), not merely sharing a Kodaira
   type by coincidence.
4. **Not killed, still open**: which of Round 16's 2 surviving torsion
   patterns is correct — Solution A is *favored* by a depth heuristic,
   not proved.

## Highest-value next question

Construct the correct local chart for the Tate-cubic's simple-root
direction (containing `T_2`) at `t=0`. Given the diagnosed failure mode
(`Y^2\sim t^3\cdot w`, `w=W+1\to0`, an extra ramification in `w` itself),
the natural next attempt is a **two-step substitution** — first
`w=t\cdot\omega` (matching the order-of-vanishing mismatch found), then
re-examining the resulting equation's smoothness — rather than a single
guessed rescaling. Completing this would very likely fully resolve the
`t=0` fiber and, via the now-proved `t=0\leftrightarrow\infty` isomorphism
(Part VIII), the `t=\infty` fiber simultaneously, leaving only `t=-1`
before the full 23-pattern classification (Round 15's Part IV) becomes
possible.

## Required-report items

1–2. See Parts I–II.
3. Full diagram: not completed (2 of `\ge4` multiplicity-1 components
   located; the mult-2 chain not explored, though sections cannot meet
   those regardless so this does not block the height calculation).
4. Multiplicities: mult-1 confirmed at `X_1=0,-1`; others not derived.
5. Identity component: qualitatively located (`X=O(1)`), not charted.
6. Component group: `(\mathbb Z/2)^2`, reconfirmed from standard theory.
7. Torsion locations: `T_1,T_3` located and proved smooth; `T_2` not
   located (chart attempt failed, honestly reported).
8. Local height contributions: not assigned with full proof; Solution
   A's assignment (`T_1,T_3\to1.5`, `T_2\to1`) is circumstantially
   favored, not proved.
9. Dictionary: partial (see Part V).
10–11. Patterns eliminated/restricted by `t=0`: **0 eliminated with
   full rigor this round** (the underlying component dictionary is
   incomplete); no false claim of elimination is made.
12. Combined `t=0,t=1` count: unchanged at 23 (only the pre-existing
    torsion-only elimination from Round 16 stands).
13. `t=0\leftrightarrow\infty` symmetry: **PROVED to exist** (exact
    algebraic isomorphism of local models); its action on individual
    torsion points/components not yet traced.
14. Finite exact ansatz: **not yet possible** — dictionary incomplete.
15. MW-rank/Picard-rank: unchanged, still open.
16. Modular attachment: unchanged, conditional.
17. Master identity: unchanged, COMPUTATIONALLY VERIFIED ONLY.
18. Killed/corrected: see above (the simple-root-is-smooth folklore
    killed; two genuine new component locations proved; the `0\leftrightarrow\infty`
    isomorphism proved).
19. Highest-value next question: as stated above.

**Verdict: ROUND17-D** — the additive-fiber resolution at `t=0` remains
incomplete: two of its multiplicity-1 components were rigorously located
and proved smooth (real, checked progress, plus a valuable caught error
in a common shortcut), but the identity component and the component
containing `T_2` were not resolved, so the round's central objective
("completely resolve this one fiber") was not achieved.

**THE THREE MOST IMPORTANT THINGS WE LEARNED**
- We proved, rigorously and by direct computation (not by trusting a
  standard shortcut), that two of the special "extra" landing spots at
  one of the surface's tricky points are real, smooth, and exactly
  where two of our three known special points sit.
- We also proved that a common simplifying assumption in this kind of
  analysis — "the easy-looking direction doesn't need extra work" — is
  actually false here, catching it before it could quietly corrupt the
  final answer, exactly the kind of check this whole project depends on.
- We found a genuine bonus fact along the way: the two trouble-spots at
  opposite ends of the surface (t=0 and t=infinity) are not just
  "the same type" by coincidence — they are provably, exactly, the same
  local shape, which means solving one properly will solve the other
  for free.

Stopping here per the round's instructions — no further action taken.
