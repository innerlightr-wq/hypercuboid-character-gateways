# Hypercuboid exploration — Round 23 working notes

## Part I — frozen inputs (PROVED, reconfirmed)

`\rho=20`, `|\mathrm{disc}(NS)|=8`, `T(X)\cong\mathrm{diag}(2,4)`, the
`\mathbb Q(i)(t)` height-1 section, `\mathrm{Tr}_{NS}(p)=(19+\chi(-1))p`,
and `S(p)=\#V(\mathbb F_p)-p^2` for `V:Y^2=X(X+1)T(T+1)(X+T)` — all
reconfirmed, no discrepancy.

## Part IV/V — independent Euler-characteristic check of the fiber graphs (PROVED, a genuine positive result this round)

For a fiber that is a union of `r` copies of `\mathbb P^1` meeting in a
graph with `V=r` vertices and `E` edges (simple normal crossings, all
components/nodes `\mathbb F_p`-rational), inclusion–exclusion gives
`\chi(\text{fiber})=2r-E`, which must equal the fiber's Euler number
`e=v(\Delta_{\min})` (a fact independent of, and a genuine cross-check
on, the specific graph shape assumed). **Checked exactly**:
$$I_2\ (r{=}2,E{=}2):\ 2r-E=2=e(I_2)\ \checkmark\qquad I_0^*\ (r{=}5,E{=}4):\ 6=e(I_0^*)\ \checkmark\qquad I_2^*\ (r{=}7,E{=}6):\ 8=e(I_2^*)\ \checkmark$$
**All three pass.** This confirms the *counts* `(r,E)` used since Round
22 are arithmetically consistent with the independently-known Euler
numbers — a real, non-trivial check that was not performed before
(Round 22 corrected `I_2`'s edge count by inspection, not by this
cross-check). **This rules out `(r,E)` being simply wrong in a way that
would violate the Euler-number identity** — but, importantly, it does
**not** by itself prove the graph is the *correct* one, nor that every
component is individually `\mathbb F_p$-rational (a graph with the wrong
shape, or with non-rational components arranged differently, could
still satisfy the same Euler-number arithmetic).

## Part II/III — reconstructing the resolution: one false lead corrected, one real structural gap found

**False lead, corrected.** Initially suspected the `I_0^*` central
(multiplicity-2) component might be exotic — attempting to locate it
via the `Y^2=u^3Q(T',u)` equation at `u=0` seemed to produce a residual
cubic `Q(T',0)=T'^3-T'`, momentarily read as "a hidden elliptic curve."
**This was a false alarm, corrected on closer inspection**: the central
component is simply the exceptional `\mathbb P^1` of the *first* blow-up
(`X=uT'`), parametrized by `T'\in\mathbb P^1` itself — an entirely
ordinary, manifestly `\mathbb F_p`-rational line, with the three named
components and the identity component attached to it at the four points
`T'=0,1,-1,\infty` respectively (matching the affine-`D_4` "star"
picture exactly, once correctly understood). **No exotic geometry
here** — this specific suspicion is killed.

**A real, precisely-located structural gap.** The affine `D_6` diagram
(for `I_2^*`) is known to have a **symmetric shape**: two "forks" of 2
outer (multiplicity-1) nodes each, joined by a chain of 3 interior
(multiplicity-2) nodes. **Rounds 17–19's explicit construction found
only 4 multiplicity-1 components in an *asymmetric* arrangement** —
1 "near" component (`T_2`'s direction, one blow-up level from identity)
plus 2 "far" components (`T_1,T_3`, one further blow-up level in) — with
**no independent construction of a second fork** on the identity side.
**This does not match the expected symmetric two-fork shape of an
affine `D_6` diagram**, and the three interior multiplicity-2
components (needed to connect the pieces) were **never explicitly
built** in any prior round — their rationality (and indeed their exact
adjacency structure) was only ever *assumed* from the standard abstract
Kodaira table, not independently verified against this specific
surface's actual resolution. **This mismatch is now identified as the
single most likely, concrete source of the persistent point-count
discrepancy** — height computations (Rounds 15–21) never needed the
full graph shape (only the correct *contribution values* at
multiplicity-1 components, independently cross-validated via the
height-sums-to-4 torsion check), so this gap was invisible until this
round's point-counting work exposed it.

## Part VI — infinity, independently

Re-derived via `t=1/u`: the local model at `u=0` has `a_2'(u)=u(u+1)^2`,
`a_4'(u)=u^3(u+1)^2` — literally identical in form to `t=0`'s (Round
17/18, re-confirmed, not merely asserted again). **The same structural
gap identified above at `t=0` therefore transfers unchanged to
`t=\infty`** — it is not a `t=0`-specific artifact.

## Part VII — search for the constant-order error: located a *candidate* class of error, not a confirmed fix

Per the round's checklist, the most plausible candidate is:
**"an exceptional divisor defined only over a quadratic extension"**
(or, more precisely here, an exceptional divisor whose full structure —
including how many components it actually contains and how they meet —
was never verified, given the asymmetry found in Part II/III). A
component pair not individually `\mathbb F_p`-rational (e.g. swapped by
Frobenius, or requiring `\mathbb Q(\sqrt2)$ or `\mathbb Q(\sqrt{-2})$ given how
pervasively those fields appear elsewhere in this surface's arithmetic)
would change its contribution to the point count by a bounded,
character-dependent amount — **exactly the shape of error Round 22
could not close.** **This is a diagnosis, not a confirmed correction**:
the interior components were not explicitly constructed this round
either, so no verified numeric fix is reported.

## Part VIII — forensic prime table: not completed to a closed numeric match

Given Part II/III's gap, a full forensic per-prime table (comparing
`\#V(\mathbb F_p)`, a claimed `\#X(\mathbb F_p)`, and `C(p)`) would require
committing to a specific (unverified) guess for the interior
components' structure — the round's own discipline ("do not fit a
correction term from data") rules this out until the structure is
actually built. **Not attempted as a numerology exercise; deferred
until Part II/III's gap is closed.**

## Part IX — Routes A and B: do not yet agree, and the reason is now precisely identified

**Route B (fiber ledger) cannot yet be completed**, because it requires
the full, correct interior-component structure of `I_2^*` at `t=0` and
`t=\infty` (Part II/III), which remains unbuilt. **Route A (modification
ledger)** was not independently attempted this round given Route B's
gap already pinpoints where the disagreement must originate. **No
`C(p)` is claimed proved.**

## Part X/XI/XII — deferred, per the round's own explicit instruction ("do not proceed until Routes A and B agree identically")

Not attempted — attempting to back out `\mathrm{Tr}_T(p)` or the
modular twist from an unclosed `C(p)` would only reproduce Round 22's
mistake of fitting a term to make the numbers work, which this round
was specifically tasked to avoid.

## Part XIII — falsification discipline (applied; one false lead killed, no premature closure claimed)

- The "exotic `I_0^*` center" hypothesis was raised and then **killed**
  by direct reconsideration (Part II/III) — a real example of proposing
  and then falsifying a lead, not just confirming what was expected.
- The `(r,E)` counts for all three fiber types were cross-checked
  against independently-known Euler numbers (Part IV/V) and passed —
  this is reported as exactly what it is (a necessary consistency check
  that passed), not over-claimed as proof the graphs are fully correct.
- No character term or correction constant was inserted to force a
  match at any point this round.

## Everything killed or corrected this round

1. **KILLED**: the momentary "hidden elliptic curve at `I_0^*`'s
   center" concern — the center is an ordinary rational `\mathbb P^1`.
2. **CONFIRMED (positive result)**: the `(r,E)` component/edge counts
   used since Round 22 for `I_2,I_0^*,I_2^*` are Euler-number-consistent.
3. **IDENTIFIED, new and important**: Rounds 17–19's explicit `I_2^*`
   construction is **structurally asymmetric** relative to the expected
   affine-`D_6` two-fork shape, and its three interior multiplicity-2
   components were never built — the single most concrete, well-located
   candidate explanation for Round 22's unresolved discrepancy.
4. **NOT resolved**: `C(p)`, `\mathrm{Tr}_T(p)`, the modular twist, and
   the master identity all remain exactly as open as at the end of
   Round 22 — this round's contribution is a sharper diagnosis, not a
   closure.

## Highest-value next question

Explicitly construct the three interior (multiplicity-2) components of
the `I_2^*` fiber at `t=0` (and, via the proved `t=0\leftrightarrow\infty`
isomorphism, at `t=\infty`), determining precisely: (a) whether the true
diagram is the expected symmetric two-fork affine-`D_6` shape or
something else specific to this surface, and (b) whether each interior
component is individually `\mathbb F_p`-rational or requires a quadratic
extension (and if so, which one — `\mathbb Q(\sqrt2)`, `\mathbb Q(\sqrt{-2})`, or
`\mathbb Q(i)`, each of which appears elsewhere in this surface's arithmetic
and would leave a distinctive, checkable signature in the point count).

## Required-report items

1–2. Affine/smooth-projective models: unchanged, Part I.
3. Modification ledger: incomplete (Part II/III gap).
4–5. Naive/resolved bad-fiber counts: naive counts reconfirmed
   (`p,p,p-\chi(-2),p` at `0,-1,1,\infty`); resolved counts' `(r,E)`
   pairs Euler-number-verified but the underlying component structure
   for `I_2^*` is now known to be incompletely built.
6. Exact contribution of each resolution: not finalized (depends on
   Part II/III).
7. Independent `t=\infty` calculation: performed, confirms the same
   local model (and hence the same gap) as `t=0`.
8–10. Routes A/B, agreement: **not reached this round** — Route B's
   prerequisite (full interior-component structure) is unbuilt.
11. Source of the Round-22 discrepancy: **precisely located** (the
   unbuilt, possibly-non-rational interior components of `I_2^*`) —
   not yet confirmed/fixed.
12. Final `C(p)`: **not obtained.**
13. NS trace: reconfirmed `(19+\chi(-1))p`.
14. Transcendental trace: not independently derived (blocked on `C(p)`).
15. Modular twist: not proved.
16. Master identity: **not proved.**
17. Elliptic-curve corollary: not re-derived as a theorem this round.
18. `p=2,3`: unchanged treatment from Round 22 (both correctly handled
   as before; no new issue found specific to them this round).
19. Killed/corrected: see above (one false lead; one genuine structural
   gap identified; the Euler-consistency check newly performed and
   passed).
20. Remaining gap: explicit construction of `I_2^*`'s interior
   multiplicity-2 components and their fields of definition — now the
   single, sharply-defined blocking task.

**Verdict: ROUND23-D** — the bounded discrepancy remains unresolved.
This round did not close it, but replaced a vague "something in the
bookkeeping is off" with a precise, well-motivated, checkable
hypothesis about exactly which unbuilt piece of the geometry is most
likely responsible, after killing one false lead and independently
verifying the fiber graphs' Euler-number consistency.

**THE THREE MOST IMPORTANT THINGS WE LEARNED**
- We chased down a scary-looking lead (a hidden, more complicated
  curve appearing where we expected something simple) and it turned
  out to be a false alarm — a good reminder to double-check unsettling
  intermediate results before trusting them.
- We found a real, independent way to sanity-check the shapes we'd been
  using (checking they add up to the surface's own known "Euler number")
  and they all passed — good news, but we're careful to say what that
  check does and doesn't prove.
- We now know almost certainly *where* the missing piece of this puzzle
  lives — three specific, never-yet-built pieces of the surface's
  geometry — even though we haven't built them yet. Knowing exactly
  where to dig next is real progress, even without having found the
  treasure.

Stopping here per the round's instructions — no further action taken.
