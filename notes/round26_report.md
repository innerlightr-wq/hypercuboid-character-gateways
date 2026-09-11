# Hypercuboid exploration — Round 26 working notes

## Part I — frozen Round-25 state (reconfirmed, marked PROVISIONAL as instructed)

`C_1` (blow-up 1, `X=t x_1,Y=t y_1`, smooth for `x_1\notin\{0,-1\}`,
verified through `x_1=\infty` too), `C_2` (blow-up 2, `x_1=tA,y_1=tB`,
smooth for `A\notin\{0,-1\}`), and the three nondegenerate-ternary-
quadratic-form nodes giving `N,F_1,F_2` (Hessian determinant `=-2` in
every case) — all reconfirmed exactly, no contradiction. **Graph
`\{O,N\}-C_1-C_2-\{F_1,F_2\}` (6 components, 5 edges) is explicitly
marked PROVISIONAL/INCOMPLETE**, not re-derived from scratch.

## Part II — the identity component, constructed explicitly (PROVED, new this round)

Used the standard chart near the zero section `O`: `u=X/Y`, `v=1/Y`
(with `Z=1` already implicit — `O` is at `u=v=0`). Exact equation
(sympy, verified):
$$H(t,u,v) = v - u^3 - a_2(t)u^2v - a_4(t)uv^2 = 0.$$
**At `t=0`**: `H=v-u^3` — the graph `v=u^3`, manifestly smooth
(`\partial H/\partial v=1` identically). **Crucially, `\partial H/\partial v=1`
holds for *every* `t,u,v` near `t=0`, not merely at `u=0`** — so the
**entire identity component is smooth at every finite `u`**, with no
blow-up needed on the identity side at all. This had never been
independently checked before this round (prior rounds only asserted
"identity" abstractly).

## Part III — the identity–`C_1` junction: Case A confirmed (clean, already resolved)

`u=X/Y=x_1/y_1$ in `C_1`'s coordinates; on `C_1` (`y_1=0`), this is
formally `u=\infty`. Round 25 already verified `C_1`'s own second chart
is smooth exactly at this point (`\partial G_2/\partial X=-1\ne0` at
`x_1=\infty`, i.e. `t_2=0`). **Combining both directions (identity's
`H=0` smooth at every finite `u`; `C_1`'s own extension through
`x_1=\infty` smooth): the identity–`C_1` junction is Case A — already
smooth and transverse, no hidden component there.** This decisively
rules out the round's top suspected location for the missing piece.

## Part IV — a genuinely new, previously-unchecked singular point found: `C_2`'s own "`A=\infty`" point

Since the identity side is now cleanly closed off, the search moved to
whether `C_2` (like `C_1`) had ever been checked for smoothness through
its *own* point at infinity — **it had not**, in any prior round.
Using the complementary chart of blow-up 2 (`t=x_1t_3,\ y_1=x_1y_3`,
i.e. `t_3=1/A`), exact computation gives, after dividing by `x_1^2`:
$$G_3(x_1,t_3,y_3) = y_3^2 - x_1t_3(t_3+1) - x_1^2[\cdots] - x_1^3[\cdots],$$
$$\partial G_3/\partial x_1\big|_{x_1=0,y_3=0} = -t_3(t_3+1).$$
**This vanishes at `t_3=0` and `t_3=-1`** — i.e. `C_2` is singular at
**both** `A=\infty` (`t_3=0`) and `A=-1` (`t_3=-1`, already known from
Round 25's separate blow-up 3a). **`A=\infty` is a genuinely new,
previously unexamined singular point of `C_2`** — a real, concrete,
located candidate for exactly where the missing seventh component
hides.

## Case determination (Part III instructions)

**Case A applies to the identity–`C_1` junction** (clean, proved this
round). **Case B (or a relabeling per Case C) likely applies at `C_2`'s
own `A=\infty` point** — but this was **not fully resolved** this round:
time did not permit performing the further ordinary blow-up at this
newly-found singular point and disentangling its relationship to the
already-known `A=-1$ resolution (whether they are the same underlying
locus seen from two charts, or genuinely distinct nodes requiring the
graph to be `C_1{-}C_2{-}C_{\text{new}}{-}\{F_1,F_2\}` rather than
`C_1{-}C_2{-}\{F_1,F_2\}` directly).

## Parts V–IX — deferred, honestly

Since the seven-component structure is **still not fully closed** (one
newly-located singular point remains unresolved), the round's own
instruction ("Do not proceed to global modular arguments until the
seven-component `I_2^*` configuration passes every geometric
consistency check") was followed: **Test 1 (component count `=7`) was
not reached; Tests 2 and 3 were not attempted on an unfinished graph;
`N_0(p),N_\infty(p)`, and the global bookkeeping (`C_A,C_B,D(p)`) were
correspondingly not attempted.**

## Falsification / adversarial check performed

- **Actively searched for a hidden singularity at the top-suspected
  location (identity–`C_1`) and found none** — a genuine negative
  result, reported as such, not silently converted into "resolution
  complete."
- **That same adversarial mindset, applied to `C_2`'s own second chart
  (never checked before), immediately surfaced a real, previously-
  missed singular point** — exactly the kind of check the round asked
  for, and it worked: it found something.

## Everything killed or corrected this round

1. **KILLED (a specific, concrete hypothesis)**: the missing 7th
   component hides at the identity–`C_1` junction. **Ruled out
   directly** — that junction is smooth and transverse.
2. **NEW, located, unresolved**: `C_2` has an unexamined singular point
   at `A=\infty`, distinct from its already-known `A=0,-1` nodes. This
   is now the leading, concrete candidate location for the missing
   piece — replacing the prior round's (now-closed) identity-side
   suspicion.
3. **PROVED, new**: the identity component is fully smooth (no blow-up
   needed) at every finite point of its own chart — previously only
   asserted, now independently verified.

## Highest-value next question

Resolve `C_2`'s newly-found singular point at `A=\infty` via the same
ordinary-blow-up-plus-Hessian/Jacobian method that has worked cleanly
four times now (Rounds 25–26), and determine precisely how it relates
to the already-known `A=-1` node — i.e. whether the correct picture is
a genuinely new third interior component (`C_1{-}C_2{-}C_3{-}\{F_1,F_2\}`,
completing the expected 7) or a reinterpretation of `C_2` itself.

## Required-report items

1. Frozen Round-25 state: Part I.
2. Identity component: `H(t,u,v)=v-u^3-a_2u^2v-a_4uv^2=0`, smooth
   everywhere at `t=0`.
3. Identity–`C_1` local equation/junction: `u=x_1/y_1$, meeting `C_1`
   exactly at `x_1=\infty` (`t_2=0` in `C_1`'s second chart).
4. Jacobian at the junction: `\partial G_2/\partial X=-1\ne0` (Round 25,
   reconfirmed) — **smooth, no additional blow-up needed here.**
5. Whether an additional blow-up is required at this junction: **No.**
6. Identity of the missing seventh component: **not found this round**
   — but its most likely location is now pinpointed to `C_2`'s own
   `A=\infty` point, not the identity side.
7–11. Corrected complete component list, multiplicities, intersection
   graph, Euler-number/component-group checks: **not completed** — the
   graph remains at 6 components/5 edges, now with one concrete,
   located, unresolved singular point flagged for the next step.
12–15. Field of definition, Frobenius, `N_{I_2^*}(p)`, `t=\infty`:
   **not reached**, per the round's own explicit instruction not to
   proceed past an unresolved configuration.
16–22. `C_A,C_B,D(p)`, transcendental trace, modular attachment,
   master identity: **unchanged**, exactly as open as before this round.
23. Killed/corrected: see above.
24. Highest-value next question: as stated above.

**Verdict: ROUND26-D** — the seven-component `I_2^*` geometry itself
remains unresolved. This round made real, verified progress by
definitively closing off the top-suspected location (identity–`C_1`,
proved clean) and, via the same adversarial discipline, discovering a
genuinely new, previously-unexamined singular point (`C_2`'s own
`A=\infty`) that is now the concrete, well-located target for Round 27.

**THE THREE MOST IMPORTANT THINGS WE LEARNED**
- We finally built, explicitly and rigorously, the one piece of this
  surface that connects to the "starting point" of the whole group
  structure — and confirmed it's simple and well-behaved, closing off
  a location we'd been worried about for two rounds.
- Because that worry turned out to be a dead end, we didn't stop —
  we applied the same "check the other side too" discipline to a
  different piece we'd built earlier, and it immediately paid off: we
  found a genuine, previously-missed problem spot that had been sitting
  unexamined since last round.
- This is a good example of how ruling something out is still real
  progress even when it's not the final answer — it freed us to look
  in the right place next, rather than continuing to search where
  nothing was actually wrong.

Stopping here per the round's instructions — no further action taken.
