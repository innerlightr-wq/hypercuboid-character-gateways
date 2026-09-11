# Hypercuboid exploration — Round 25 working notes

## Part I — frozen-input ledger (from CHECKPOINT_AFTER_ROUND24.md, reconfirmed)

`y^2=x^3+t(t+1)^2x^2+t^3(t+1)^2x`; bad fibers `I_2^*(0),I_2(1),I_0^*(-1),I_2^*(\infty)`;
`t=1,t=-1` fully resolved; `t=0/\infty` multiplicity-1 layer (identity,
`N`,`F_1`,`F_2`) fully resolved and torsion-assigned; `\rho=20`,
`|\mathrm{disc}(NS)|=8`, `T(X)=\mathrm{diag}(2,4)`, `\mathrm{Tr}_{NS}(p)=(19+\chi(-1))p`
all PROVED; Round-22/23 affine/projective correction unresolved,
localized to the unbuilt `I_2^*` interior chain. No discrepancy on
re-read — proceeded directly to Track A.

## Track A — Part II/III: explicit ORDINARY blow-ups (substantial new progress, not fully complete)

Working from `F(t,X,Y)=Y^2-(X^3+a_2X^2+a_4X)=0` at the singular point
`(t,X,Y)=(0,0,0)`.

**Blow-up 1** (ordinary, ambient `\mathbb A^3`, center the origin).
Chart `X=t\,x_1,\ Y=t\,y_1`: total transform `=t^2\cdot F_1`, with
$$F_1(t,x_1,y_1) = y_1^2 - t\big[x_1^3+x_1^2\big] - t^2\big[2x_1^2+x_1\big] - t^3\big[x_1^2+2x_1\big] - t^4x_1.$$
`F_1(0,x_1,y_1)=y_1^2`: the exceptional locus in this chart is the line
`\{t=0,y_1=0\}`, i.e. a genuine new component `C_1`. **Jacobian check**
(exact, sympy): `\partial F_1/\partial t|_{t=0,y_1=0} = -x_1^2(x_1+1)`,
`\partial F_1/\partial x_1|_{t=0,y_1=0}=0`, `\partial F_1/\partial y_1|_{y_1=0}=0`.
**`C_1` is smooth for every `x_1\notin\{0,-1\}`**, singular exactly at
`x_1=0` and `x_1=-1`. The second chart of this same blow-up
(`t=X\,t_2,Y=X\,y_2`) independently confirms `C_1` extends smoothly
through `x_1=\infty` (`t_2=0`): `\partial G_2/\partial X|_{X=0,t_2=0}=-1\ne0`.
**`C_1` is a complete `\mathbb P^1`, smooth except at two marked points**
(`x_1=0`, `x_1=-1`), and meets the strict transform of the original
curve (**identity**) at the third marked point `x_1=\infty`. `C_1` is
therefore an interior node of **valence 3** — exactly the shape expected
for the chain node adjacent to the `\{$identity`,N\}` fork.

**Blow-up 2a** (at `x_1=-1`, `w_2=x_1+1`). Leading (degree-2) form of
`F_1` after shift: `-t^2-tw_2+y_1^2`. **Verified nondegenerate**
(Hessian determinant `=-2\ne0` for every odd `p`, exact sympy
computation) — an **ordinary node**. A single further ordinary blow-up
resolves it completely to a smooth conic `M_a` (no residual
singularity, since nondegenerate quadrics blow up cleanly in one step).
**By the classical fact that a nondegenerate ternary quadratic form
over any finite field is isotropic**, `M_a` has an `\mathbb F_p`-point for
every odd `p` and is therefore **`\mathbb P^1$ over `\mathbb F_p$, unconditionally,
for every prime — no character dependence.** `M_a` matches `N` (Round
18's `T_2$-component) in location and role.

**Blow-up 2b** (at `x_1=0`). `F_1`'s leading form here is `y_1^2` alone
(degree 2, but the next terms are degree 3 — a *more* degenerate point
than blow-up 2a's). A second **ordinary** blow-up, `x_1=t\,A,\ y_1=t\,B`,
gives (after dividing by `t^2`) a new component
$$C_2:\ \{t=0,B=0\},\qquad G(t,A,B)=B^2-t(A^2+A)-t^2(A^3+2A^2+2A)-t^3(A^2+A),$$
**verified smooth for `A\notin\{0,-1\}$** (`\partial G/\partial t|_{t=0,B=0}=-A(A+1)`,
exact), singular at `A=0` and `A=-1`. `C_2$ is a **second interior
node**.

**Blow-ups 3a, 3b** (at `A=-1` and `A=0` of `C_2`). Leading quadratic
forms: at `A=-1` (`w_3=A+1`): `t^2+tw_3+B^2` — **nondegenerate**
(same shape/determinant as blow-up 2a). At `A=0`: `B^2-tA` —
**verified nondegenerate** (Hessian determinant `\ne0`, exact). **Both
resolve in one further ordinary blow-up to smooth conics `M_b,M_c`,
each unconditionally `\mathbb F_p$-rational by the same isotropy argument.**
`M_b,M_c` match `F_1,F_2` (Round 17) in location.

## Part IV — reconstructing the fiber: PARTIAL, one component short

Assembled so far: **identity, `C_1` (interior), `M_a\;({=}N)`, `C_2`
(interior), `M_b\,({=}F_1)`, `M_c\,({=}F_2)`** — **6 components**, of
which `C_1,C_2` are the only interior (multiplicity-2) pieces found.
**The expected total is 7 (4 multiplicity-1 + 3 multiplicity-2,
matching `e(I_2^*)=8` and `n+5` for `n=2`).** `C_1` and `C_2` were each
independently confirmed to have exactly the right valence for an
"end-of-chain, adjacent-to-a-fork" node (valence 3: `C_1$ meets
identity, `N`, and `C_2`; `C_2$ meets `C_1`, `F_1`, `F_2`) — **this
graph shape (`\{O,N\}-C_1-C_2-\{F_1,F_2\}`, a chain of length 2, not
3) is internally consistent as far as it was checked, but gives only 6
components and 5 edges, not 7 and 6.** `2\times6-5=7\ne8=e(I_2^*)`
— **this construction as it stands does NOT pass the Euler-number
cross-check**, meaning **either a third interior node is genuinely
missing, or one of `C_1,C_2$'s marked points hides a further, unresolved
sub-structure not yet found.** **This is reported as an honest,
located discrepancy, not resolved this round** — the natural next
candidate is that `C_1`'s meeting with identity (`x_1=\infty`), verified
smooth *in this chart*, may still require a genuinely separate treatment
of identity's own chart (never independently constructed) to see if a
further node hides there.

## Part V — fields of definition and Frobenius: a clean, general, unconditional result (PROVED, for the pieces found)

**Every exceptional component found via resolving these specific
singularities (`M_a, M_b, M_c`) is `\mathbb F_p`-rational for every odd
prime `p`, unconditionally** — this follows from the classical fact
that a nondegenerate quadratic form in 3 variables over any finite
field represents zero nontrivially (finite fields have no anisotropic
ternary forms), so the blow-up of an ordinary node of a surface always
yields a **split** exceptional conic. **No `\chi(-1),\chi(2),\chi(-2)`
dependence enters from any of the singularities resolved this round.**
`C_1,C_2` (the interior nodes themselves, found directly as smooth
loci, not via a quadric blow-up) are likewise manifestly `\mathbb F_p`-
rational (parametrized directly by `x_1`, resp. `A`, both natural
`\mathbb F_p`-coordinates). **This is a genuine, valuable, general finding**
that directly **kills Round 23's leading hypothesis** (that a
quadratic-extension interior component was the source of the point-count
discrepancy) **for every component actually constructed this round.**

## Part VI — exact `I_2^*` point count: NOT obtained (blocked by Part IV's gap)

Since the full 7-component structure was not reconstructed, `N_0(p)`
cannot yet be derived from first principles. **What is now known**: *if*
the missing third interior node is also unconditionally `\mathbb F_p$-
rational (highly likely, given every other piece found this round is),
then the original "`7p+1`" tree-formula candidate (Round 22/23) is very
likely **arithmetically correct as a formula** — meaning **Round
23's specific diagnosis (non-rational interior components) is now
disfavored**, and the true source of the earlier residual discrepancy
more likely lies in the naive-count/bookkeeping arithmetic itself
(the `+1`s, the edge-count, or the Lefschetz-formula normalization),
**not in fiber-component arithmetic** — a real, useful narrowing.

## Part VII — infinity: not independently repeated

Given Part IV/VI's gap at `t=0`, repeating the same incomplete
construction at `t=\infty` would not add information; the proved
`t=0\leftrightarrow\infty` isomorphism (Round 17/18) guarantees whatever
is eventually found transfers unchanged.

## Escape hatch: not invoked

Genuine further explicit progress was still being made (Part II/III)
when time ran out, so the escape hatch (citing general Tate's-algorithm
theory in place of explicit construction) was not needed to make
progress this round — though it remains available for Round 26 if the
missing third node again proves resistant to direct construction.

## Track D — Part VIII: global ledger

`C_A(p), C_B(p), D(p)`: **not recomputed** — per the round's own
instruction ("Once the `I_2^*` arithmetic is rigorously settled..."),
this was correctly not attempted given Part IV/VI's gap.

## Tracks E — Parts IX–X: deferred

Not attempted, per the round's explicit conditional instructions.

## Part XI — adversarial checks actually performed

- Every blow-up chart's Jacobian was computed and checked exactly by
  sympy, not asserted.
- The two "ordinary node" claims (blow-ups 2a, 3a, 3b) were verified
  nondegenerate via an explicit Hessian-determinant computation
  (`=-2$, and `\ne0` in the `A=0` case), not merely assumed from the
  shape of the leading form.
- The `C_1$ component's extension through `x_1=\infty` was checked in
  an **independently constructed second chart** (`t=Xt_2,Y=Xy_2`), not
  inferred from the first chart alone.
- **The Euler-number cross-check was applied to the assembled
  construction and found NOT to pass** (`7\ne8` for the 6-component,
  5-edge graph found so far) — this is reported as a genuine failure of
  the adversarial check, not glossed over, and is exactly what
  correctly prevented declaring the resolution complete this round.

## Everything killed or corrected this round

1. **DISFAVORED (not fully killed, but strong new evidence against)**:
   Round 23's hypothesis that a quadratic-extension interior component
   is the source of the point-count discrepancy — every interior/
   exceptional component actually constructed this round is
   unconditionally `\mathbb F_p`-rational.
2. **NEW, genuine progress**: two interior (multiplicity-2) components
   `C_1,C_2` explicitly constructed and verified smooth; three
   exceptional conics `M_a,M_b,M_c` (matching `N,F_1,F_2`) shown to
   arise from nondegenerate-ternary-quadratic-form ordinary nodes,
   hence unconditionally rational by a clean classical fact.
3. **LOCATED, not resolved**: the assembled 6-component, 5-edge graph
   fails the Euler-number check by exactly 1 (missing component,
   missing edge) — a third interior node (or additional structure at
   `C_1`'s meeting with identity) remains to be found.
4. **NOT reached**: `N_0(p)`, `D(p)`, `\mathrm{Tr}_T(p)`, the modular
   twist, and the master identity — all exactly as open as at the end
   of Round 24, though the most likely path to closing them has shifted
   (away from component-rationality, toward finding the missing node
   or a bookkeeping-arithmetic fix).

## Highest-value next question

Find the missing third interior component. The most promising lead:
**explicitly construct "identity" itself** (the strict transform of the
naive curve, via `s=Y/X`-type normalization) and check whether IT is
smooth at its own meeting point with `C_1` (`x_1=\infty`) — Part II
only checked smoothness of `C_1` there, not of identity's own chart,
so a hidden node at that junction (rather than elsewhere) has not been
ruled out.

## Required-report items

1. Frozen starting state: §Part I above.
2. Ordinary blow-up sequence: Blow-ups 1, 2a, 2b, 3a, 3b — fully given
   with exact equations and Jacobians (Part II/III).
3. `M_1{=}M_a{=}N`, and the two from `C_2`: `M_b{=}F_1,\ M_c{=}F_2$ —
   equations given (leading quadratic forms); full post-blow-up conic
   equations not separately written out (their existence/smoothness/
   rationality was established via the isotropy argument rather than
   an explicit final equation).
4. Complete seven-component fiber: **NOT achieved** — 6 found.
5. Multiplicities: 4 components multiplicity 1 (identity,N,F1,F2, from
   prior rounds) + 2 multiplicity-2 (`C_1,C_2`, new this round).
6. Intersection graph: `\{O,N\}\!-\!C_1\!-\!C_2\!-\!\{F_1,F_2\}`
   (chain of length 2) — **fails the Euler-number check**, so not
   accepted as final.
7. Fields of definition: **all components found are `\mathbb F_p`-rational,
   unconditionally** (proved for `M_a,M_b,M_c` via ternary-quadratic
   isotropy; manifest for `C_1,C_2`).
8. Frobenius action: trivial (identity permutation) on every component
   found, for every odd prime.
9. Rationality of nodes: all marked/singular points resolved this round
   are `\mathbb F_p`-rational.
10–15. `N_0(p), N_\infty(p)`, finite-field table, `C_A,C_B,D(p)`: **not
    reached**, per the round's own conditional structure.
16. Global bookkeeping: **not proved.**
17–19. `\mathrm{Tr}_T(p)`, modular twist, master identity: **unchanged**
    — COMPUTATIONALLY VERIFIED ONLY, not proved.
20. Killed/corrected: see above.
21. Highest-value next question: as stated above.

**Verdict: ROUND25-D** — the `I_2^*` arithmetic itself remains
unresolved: substantial genuine progress was made (two interior nodes
explicitly built and verified, a clean unconditional-rationality result
established for every component constructed, and Round 23's leading
hypothesis correspondingly disfavored), but the full seven-component
structure was not completed (the Euler-number check caught this before
it could be wrongly accepted), so the downstream bookkeeping and master
identity remain exactly as open as before.

**THE THREE MOST IMPORTANT THINGS WE LEARNED**
- Doing the careful, slow, one-step-at-a-time version of the
  construction (instead of a shortcut) actually worked this time and
  produced two brand-new, fully verified pieces of the surface that no
  previous round had managed to build.
- Along the way we found a clean, general mathematical reason (not
  specific to this surface) why those new pieces — and the three we'd
  already found — are all "well-behaved" over every prime, with no
  hidden dependence on whether numbers are squares mod p. This makes
  last round's leading suspicion about the missing piece look unlikely.
- We built our own check into the process (do the pieces we found add
  up to the number we independently know they should?) and it correctly
  caught that we're still one piece short — which is exactly the kind
  of self-correction that keeps this project from declaring victory too
  early.

Stopping here per the round's instructions — no further action taken.
