# Hypercuboid exploration — Round 24 working notes

## Part I — frozen local model (PROVED, reconfirmed)

`a_2=t(t+1)^2,a_4=t^3(t+1)^2`, `(v(c_4),v(c_6),v(\Delta))=(2,3,8)` at
`t=0`, Kodaira type `I_2^*`, Tate cubic `P(T)=T^2(T+1)` (double root `0`,
simple root `-1`) — all reconfirmed exactly, matching Rounds 11–18.

## Part III (addressed first) — resolving Round 23's "asymmetry" concern: KILLED, a real clarification

Round 23 worried that Rounds 17–19's 4 multiplicity-1 components
(identity, `N`, `F_1`, `F_2`) looked structurally asymmetric compared
to the expected affine-`D_6` diagram's two separate 2-node forks.
**This concern is resolved, not confirmed**: affine `D_6` has exactly
**4 outer (multiplicity-1) nodes total**, arranged as **two forks of 2
nodes each** — and the component group `(\mathbb Z/2)^2` (order 4) already
forces there to be *exactly* 4 such nodes (one per group element), not
5. **The correct pairing is: `\{$identity`, N\}` form one fork (both
attach to the same first interior chain node), and `\{F_1,F_2\}` form
the other fork** (both attach to the last interior chain node). This
is fully consistent with everything built in Rounds 17–19 — **no
component is missing from the multiplicity-1 layer.** What genuinely
remains missing is only the **3 interior multiplicity-2 chain nodes**
connecting the two forks — exactly as Round 23 also (correctly)
flagged, but now with the "asymmetry" false alarm cleared.

## Part II — attempting to construct the interior chain: a genuine, verified negative result

**Attempted the natural intermediate step**: before jumping to the
final smooth chart `X=t^2X_1,Y=t^3Y_1` (Round 17), tried the
*shallower* substitution `X=tX'` alone (leaving `Y` unscaled), hoping
to expose an intermediate exceptional component at this halfway stage.
**Verified by exact symbolic computation** (`H(t,X',Y)=Y^2-(X^3+a_2X^2+a_4X)`
with `X=tX'`): `H(0,0,0)=0` and **all three partial derivatives vanish
identically at the origin** (`\partial H/\partial Y=\partial H/\partial X'=\partial H/\partial t=0`).
**This chart is still singular** — it does *not* reveal an intermediate
chain component as a separate smooth affine piece. The resolution from
the naive singular model to the final smooth `(X_1,Y_1)` chart does not
factor through this simple one-parameter intermediate scaling in an
exposed way.

**Interpretation, stated honestly.** The weighted substitution
`X=t^2X_1,Y=t^3Y_1$ has weights `(2,3)` with `\gcd(2,3)=1` — a
coprime-weight blow-up of this kind can genuinely resolve a
singularity in "one step" without an intermediate exceptional divisor
appearing as a *separate, simply-parametrized* affine chart of the kind
used successfully for the multiplicity-1 components. **The 3 interior
chain components almost certainly exist geometrically** (forced by the
Euler-number/component-group consistency already checked in Round 23),
**but constructing them explicitly requires a genuine toric or
iterated-blow-up treatment** (tracking the exceptional locus of the
weighted blow-up itself, or a correctly-sequenced chain of *several*
ordinary blow-ups with carefully chosen shifts at each step) —
**materially more involved than the direct "guess a rescaling, check
the Jacobian" method that worked for the multiplicity-1 layer, and this
was not achieved this round.**

## Part IV/V — fields of definition, Frobenius action: NOT obtained (blocked on Part II)

Since the interior components were not constructed, their fields of
definition and the Frobenius action on them **cannot yet be
determined**. This remains open exactly where Round 23 left it, with
the added clarity that a natural first attempt at building them (Part
II above) has been tried and shown not to work in the simple way that
succeeded for the outer components — a genuine narrowing of *how* the
remaining construction must proceed, even though it does not supply
the construction itself.

## Part VI — exact resolved-fiber point count: NOT obtained

Blocked on Parts II/IV — without the interior chain's point counts and
intersection structure, `\#I_2^*(\mathbb F_p)` cannot be derived from first
principles this round. The Euler-characteristic-consistent *candidate*
formula `7p+1$ (Round 22/23, assuming all 7 components rational, tree
graph) stands as an unverified but not-yet-falsified candidate.

## Part VII — independent `t=\infty` calculation

Not attempted independently this round, since the prerequisite (`t=0`'s
interior chain) is itself unresolved — repeating an incomplete
construction at a second point would not add information. The proved
`t=0\leftrightarrow\infty` local isomorphism (Round 17/18) continues to
guarantee that whatever is eventually found at `t=0` transfers
verbatim to `t=\infty`.

## Part VIII — finite-field checks

Not performed as a numerology exercise this round, consistent with the
project's standing discipline (do not fit or verify a formula that has
not yet been derived) and the round's own explicit instruction not to
let direct enumeration substitute for derivation.

## Part IX — the global discrepancy

Unchanged from Round 23: `C_A(p)` and `C_B(p)` were not brought to
agreement, because Route B's prerequisite (the complete `I_2^*`
resolution) remains unbuilt. No numeric correction is proposed.

## Parts X/XI — deferred, per the round's own instruction ("only if the bookkeeping now closes exactly")

Not attempted. `\mathrm{Tr}_T(p)`, the modular twist, and the master
identity remain exactly as open as at the end of Round 23.

## Falsification requirement — applied where there was something to test

- The claimed fork-pairing (`\{$identity,N\}`, `\{F_1,F_2\}`) was
  checked against the **hard constraint** that the component group has
  order exactly 4 (`(\mathbb Z/2)^2`) — a real, non-negotiable check, not a
  guess — and passed as the *only* consistent pairing.
- The intermediate-chart hypothesis (Part II) was tested directly by
  computing an explicit Jacobian, not assumed to work or fail.
- No claim about the interior chain's rationality is made in either
  direction — nothing was "verified" that wasn't actually checked.

## Everything killed or corrected this round

1. **KILLED (a concern, not a prior claim)**: Round 23's worry that the
   `I_2^*` construction was missing an entire second near-identity
   fork. **Clarified**: identity and `N` themselves constitute that
   fork together; nothing is missing at the multiplicity-1 level.
2. **NEW NEGATIVE RESULT, verified**: the natural shallow intermediate
   chart (`X=tX'`, `Y` unscaled) is singular at the relevant point —
   ruled out as a route to the interior chain components.
3. **NOT resolved**: the interior chain's explicit construction, field
   of definition, `C(p)`, `\mathrm{Tr}_T(p)`, the modular twist, and the
   master identity — all remain open, exactly where Round 23 left them.

## Highest-value next question

Construct the `I_2^*` interior chain via a genuinely different method
than scalar rescaling — e.g., an explicit sequence of **ordinary**
(non-weighted) blow-ups of the surface singularity at the origin,
tracking each exceptional `\mathbb P^1` one at a time (rather than jumping
directly via the coprime-weighted `(2,3)` substitution that resolves
everything "in one step" but hides the intermediate stages), or a
direct toric description of the `A_1`-type (or worse) surface
singularity being resolved. This is now a well-defined, narrowly-scoped
technical task, not an open-ended search.

## Required-report items

1. `t=0` local model: unchanged, Part I.
2. Blow-up sequence: **incomplete** — the multiplicity-1 layer
   (identity, `N`, `F_1`, `F_2`) is fully built (Rounds 17–19); the
   interior chain is not.
3–4. Components/multiplicities: 4 multiplicity-1 (built, verified
   smooth) + 3 multiplicity-2 (not built) = 7 total, matching the
   Euler-consistent count.
5. Intersection graph: **abstract structure clarified** this round
   (two 2-node forks joined by the 3-node chain, `\{O,N\}` and
   `\{F_1,F_2\}`), but not independently verified component-by-component
   (no explicit intersection points computed for any edge).
6. Equations for the 3 missing interior components: **not obtained**;
   one natural candidate approach tried and shown not to work (Part II).
7–9. Fields of definition, Frobenius action, intersection-point
   rationality: **not obtained**, blocked on item 6.
10. `\#I_2^*(\mathbb F_p)`: **not derived**; `7p+1` remains an unverified
   candidate.
11. `t=\infty`: not independently attempted (would repeat the same gap).
12. Finite-field table: not produced (nothing derived yet to check).
13–15. Correction to Round 22/23, `C_A=C_B`, residual discrepancy: **no
   change** — still open, exactly as Round 23 left it.
16. NS trace: reconfirmed unchanged, `(19+\chi(-1))p`.
17–19. Transcendental trace, modular twist, master identity: **not
   derived**, per the round's own instruction not to proceed without a
   closed bookkeeping.
20. Highest-value next question: as stated above.

**Verdict: ROUND24-D** — the `I_2^*` resolution itself remains
incomplete. This round cleared up a real point of confusion (the fork
structure is not asymmetric; nothing is missing at the multiplicity-1
level) and ruled out one natural, concrete approach to building the
interior chain (verified singular, not just assumed), but did not
construct the three interior components, and therefore none of the
downstream bookkeeping, twist, or master-identity questions were
reached.

**THE THREE MOST IMPORTANT THINGS WE LEARNED**
- A worry from last round turned out to be based on a slightly wrong
  mental picture of how the pieces fit together — once we checked the
  hard constraint (exactly four pieces, no more, no less), the picture
  we already had turned out to be complete after all at that level.
- We tried the most natural "next thing to try" for building the
  missing middle pieces, and it genuinely didn't work — a real,
  checked dead end, not a guess we're leaving untested.
- This confirms that the last missing piece of a very long chain of
  reasoning needs a properly different technique (not just "try a
  slightly different number"), and now we know that specifically
  rather than vaguely — which is exactly the kind of narrowing that
  makes the next attempt more likely to succeed.

Stopping here per the round's instructions — no further action taken.
