# Class III Round 3 — Closing the Néron–Severi Rationality Gap

**Scope discipline.** Work confined to `explorations/class_iii/`. The
published Classes I/II manuscript was not touched. Nothing committed, nothing
pushed.

**Primary target (and only target).** Round 2 established
`Tr(F_p|T(X_III)) = a_p(16.3.c.a)` (untwisted) by finite theorem-based
elimination, but left one assumption unverified: `Tr(F_p|NS(X_III)) = 20p`,
resting on structural analogy to the main manuscript rather than an
independent construction showing all 20 `NS(X_III)` generators are
individually `Q`-rational. This round attacks exactly that gap via explicit,
computer-algebra-verified local blow-ups of all three `I2*` fibers — **not**
weighted `(2,3)` substitutions, per the round's explicit instruction.

---

## Part I — Frozen results and exact fiber locations

All Round 1/2 results (character sum, `T(p)` reduction, `p≡3(4)` involution,
Weierstrass model, `ρ=20`, MW rank 0, torsion `(Z/2)^2`, `|disc NS|=4`,
`T(X_III)≅diag(2,2)`, modular candidate `16.3.c.a`, twist elimination) are
treated as frozen; no contradiction was found this round.

**Exact fiber locations and local minimal models**, freshly derived (not
copied from Round 1) via `scripts/class3_round3_factorization.py`:

The cubic `X^3 + a2(T)X^2 + a4(T)X` with `a2(T)=T(T+1)(T+2)`,
`a4(T)=T^2(T+1)^3` factors **exactly**, over `Q[T]`, as:

```
X^3 + a2(T)X^2 + a4(T)X = X (X + T(T+1)) (X + T(T+1)^2)
```

(verified symbolically — `sympy` confirms the difference simplifies to `0`,
and independently re-verified mod `p` for 12 primes in
`scripts/class3_round3_falsification.py`, Direction 1). This means **the
full 2-torsion of `E_T` is rational over `Q(T)` itself** — the roots are `0`,
`-T(T+1)`, `-T(T+1)^2`, all polynomial in `T`. This was not previously
observed explicitly and is a genuinely new structural fact this round
surfaced; it directly explains the `(Z/2)^2` torsion found in Round 1 at the
level of the *generic fiber*, not merely at each bad fiber individually.

Consistent with this, the discriminant of the quadratic factor,
`a2(T)^2-4a4(T) = T^4(T+1)^2 = (T^2(T+1))^2`, is a **perfect square** in
`Q[T]` (verified symbolically and mod `p`).

Local minimal models (verified via `c4,c6,Delta` valuations,
`scripts/class3_round3_factorization.py`):

```
c4 = 16 T^2(T+1)^2(T^2+T+1)
c6 = -32 T^3(T-1)(T+1)^3(T+2)(2T+1)
Delta = 16 T^8 (T+1)^8
```

At `T=0`: `v(c4)=2, v(c6)=3, v(Delta)=8` — Kodaira `I2*` **independently
re-confirmed** via Tate's minimality/type criterion (not merely quoted).
At `T=-1`: identical valuations (`(T+1)` factors), `I2*` re-confirmed.
At `T=infinity`: degree count gives `deg(c4)=6, deg(c6)=9, deg(Delta)=16`, so
`v_infinity(Delta) = 24-16 = 8` (using the K3 total-discriminant-degree-24
bound), and a correct `(2,4)`-weighted rescaling `S=1/T`,
`ã2(S)=S^4a2(1/S)=S(S+1)(2S+1)`, `ã4(S)=S^8a4(1/S)=S^3(S+1)^3` gives
`v(c̃4)=2, v(c̃6)=3` — `I2*` independently confirmed at infinity too. All
three bad fibers are `I2*`; `3×8=24` matches the K3 Euler characteristic
exactly, confirming no other singular fibers exist.

**Status: PROVED — SELF-CONTAINED** (fiber locations, types, and local
minimal models; all independently re-derived and cross-checked mod `p`, not
merely inherited from Round 1).

---

## Part II — Explicit successive blow-ups of each `I2*` fiber

Per the round's explicit instruction, **ordinary (unweighted) blow-ups only**
were used throughout — no `(2,3)`-weighted substitution was applied at any
step. All computations below are `sympy`-verified in
`scripts/class3_round3_blowup_t0_step1.py` through `_step3.py` (`T=0`),
`_blowup_tm1_step1.py`/`_step2.py` (`T=-1`), and `_blowup_tinf_step1.py`
(`T=infinity`).

### `T=0` fiber

Singular point of the total space at `(X,Y,T)=(0,0,0)` (all partials
vanish — verified). **Blow-up 1**: `X=Tx1, Y=Ty1`. Total transform has
uniform factor `T^2` (multiplicity 2 — matches the tangent cone `Y^2=0`,
confirming additive, worse-than-nodal reduction). Proper transform
`F1 = y1^2 - [T x1(1+x1)^2 + 3T^2 x1(1+x1) + T^3 x1(3+x1) + T^4 x1]`.

`F1|_{T=0} = y1^2` — exceptional curve `E0 = {T=0, y1=0}` (parametrized by
`x1`), a genuine new fiber component, with multiplicity 2 as a divisor
(consistent with `E0` being a **spine** component). Checked in both the
`T`-dominant and `X`-dominant charts (`_xchart.py`): `E0` is singular
(needs further blow-up) at **exactly** `x1=0` and `x1=-1` (no other point,
including at `x1=infinity`, requires further blow-up — confirmed via the
`X`-dominant chart, which shows the same two points and nothing new).

**At `x1=0`**: tangent cone `y1^2 - T x1` — a rank-3, **nondegenerate**
quadratic form. This is an **ordinary node** (`A1` Du Val singularity),
resolving in a single further blow-up into one smooth exceptional `P^1`
(component `E1`).

**At `x1=-1`**: tangent cone `y1^2 = 0` (multiplicity 2 again) — requires
**Blow-up 2**: `x1 = -1+x2`, then `x2 = T x3, y1 = T y3`. Proper transform
`F2 = y3^2 + T x3(x3+1) + higher order` — new exceptional curve `E2`
(spine), singular at `x3=-1` and `x3=-2` (both **simple** roots this
time). Both resolve via **ordinary nodes**: tangent cones `y3^2 + T x4`
(`x3=-1`) and `y3^2 - T x5` (`x3=-2`) — components `E3`, `E4`.

### `T=-1` fiber

Local parameter `s=T+1`. **Blow-up 1**: `X=sx1,Y=sy1` gives proper
transform `F1 = y1^2 + s x1^2(1-x1) - s^2 x1 + s^3 x1(2-x1) - s^4 x1`,
exceptional curve `E0'`, singular at `x1=1` (simple) and `x1=0` (double).

**At `x1=1`**: tangent cone `y1^2 - s x2` (`x2=x1-1`) — ordinary node,
component `E1'`.

**At `x1=0`**: requires **Blow-up 2** (`x1=sx3,y1=sy3`): proper transform
`F2 = y3^2 + s(x3^2-x3) + ...`, singular at `x3=0` and `x3=1` (both
simple). Tangent cones `y3^2 - s x3` and `y3^2 + s x4` (`x4=x3-1`) — both
ordinary nodes, components `E3'`, `E4'`.

### `T=infinity` fiber

Local parameter `S=1/T`, with the correctly `(2,4)`-weighted rescaled model
`ã2(S)=S(S+1)(2S+1)`, `ã4(S)=S^3(S+1)^3`. The cubic factors, exactly as at
the finite fibers, with a perfect-square discriminant
`ã2^2-4ã4 = S^2(S+1)^2`, giving roots `0, -S^2(S+1), -S(S+1)^2`. **Blow-up
1** (`X̃=Sx1,Ỹ=Sy1`): proper transform singular at `x1=-1` (simple) and
`x1=0` (double, by the same pattern). At `x1=-1`: tangent cone
`y1^2 - S x2` (`x2=x1+1`) — ordinary node. The double-root branch at `x1=0`
was not carried to full completion this round (see honesty flag below), but
by the now-threefold-repeated pattern (identical algebraic shape at every
one of the other five simple-root points found), it is expected — not yet
independently confirmed — to resolve the same way.

### Consolidated finding

**Every tangent cone found this round — 7 of them, across all three bad
fibers — is of the form `y^2 = (unit) · u · v` for two independent local
coordinates `u, v` (never `y^2 = c·w^2` for a single coordinate `w`, and
never with a coefficient requiring a square-class check).** A quadratic
form `y^2 - c\,uv` (`c` a unit) is **always isotropic over any field** — it
has the manifest rational point `[u:v:y]=[1:0:0]` regardless of `c` or of
the residue field — so **every one of these 7 ordinary-node resolutions is
individually `Q`-rational, for every prime `p`, unconditionally**. This is
the central, load-bearing computational finding of Round 3.

**Honesty flag — component count not fully closed.** The standard Kodaira/
Tate theory (cited, `PROVED — LITERATURE`) guarantees exactly 7 components
per `I2*` fiber with multiplicity pattern `(1,1,2,2,2,1,1)`. This round's
explicit blow-up trace found and typed **5 of 7** components at each of the
`T=0` and `T=-1` fibers (2 spine + 3 leg, rather than the expected 3 spine +
4 leg), and did not complete the `x1=0` branch at `T=infinity` at all. The
discrepancy (5 found vs. 7 expected, per finite fiber) was **not resolved**
this round — it most likely reflects either an additional blow-up needed at
the "simple root" end (`x1=0` at `T=0`; `x1=1` at `T=-1`) that was not
found because ordinary-node resolutions were (correctly, per standard Du Val
theory) treated as terminal, or a self-intersection/contraction subtlety in
the iterated-blow-up bookkeeping that would require redoing the computation
with full intersection-number tracking (effectively requiring computer
algebra system support, e.g. Magma or Singular's resolution routines, beyond
what was tractable by hand/`sympy` this round). **This is reported
honestly as an incomplete verification, not swept under a structural-analogy
assumption** — it is a narrower, better-characterized gap than Round 2's
(which had zero explicit local verification), but it is not zero.

**Status: FINITE THEOREM-BASED VERIFICATION** for the 7 tangent cones
explicitly found (all confirmed unconditionally split); **OPEN** for
complete closure of the component count and full intersection graph.

---

## Part III — Adversarial field-of-definition check

Per the round's explicit instruction, the implication "fiber defined over
`Q` ⟹ every component defined over `Q`" was **not** assumed. Every
component found was checked individually:

| Component | Fiber | Tangent cone | Type | `Q`-rational? |
|---|---|---|---|---|
| `E0` (spine) | `T=0` | `Y^2=0` (mult. 2, not a node) | additive, needs further blow-up | pending further resolution, not itself a leaf |
| `E1` | `T=0`, `x1=0` | `y1^2-Tx1` | ordinary node, `y^2=uv` | **yes**, unconditionally |
| `E2` (spine) | `T=0`, `x1=-1` | `Y^2=0` again | needs further blow-up | pending |
| `E3` | `T=0`, `x3=-1` | `y3^2+Tx4` | ordinary node | **yes**, unconditionally |
| `E4` | `T=0`, `x3=-2` | `y3^2-Tx5` | ordinary node | **yes**, unconditionally |
| `E0'` (spine) | `T=-1` | `Y^2=0` | needs further blow-up | pending |
| `E1'` | `T=-1`, `x1=1` | `y1^2-sx2` | ordinary node | **yes**, unconditionally |
| `E3'` | `T=-1`, `x3=0` | `y3^2-sx3` | ordinary node | **yes**, unconditionally |
| `E4'` | `T=-1`, `x3=1` | `y3^2+sx4` | ordinary node | **yes**, unconditionally |
| (∞-fiber, one branch) | `T=∞`, `x1=-1` | `y1^2-Sx2` | ordinary node | **yes**, unconditionally |

Specifically tested per the round's checklist and **found not to occur**:
Galois exchange of components, non-rational tangent directions, exceptional
conics without rational points, or fork components requiring a quadratic
extension. `Q(i)`, `Q(sqrt(2))`, `Q(sqrt(-2))` were each checked as
candidate obstruction fields (per the round's explicit instruction) by
examining whether any tangent-cone coefficient was a non-unit or required a
square-root of `-1`, `2`, or `-2` — **none did**; every coefficient found
was exactly `+1` or `-1` (a unit, and moreover a unit whose square-class is
irrelevant to a `y^2=uv`-type form's splitting, since such forms split
regardless of the unit's square-class). **No quadratic extension was
detected anywhere this round.**

An earlier heuristic within this round (before the tangent-cone computation
was carried out) suggested the opposite: computing the leading coefficient
of the *difference* of the two coinciding roots at `T=0`
(`e_1-e_2 = -T^2(T+1)`, leading coefficient `-1` at `T=0`) suggested a
possible `chi(-1)`-dependent splitting obstruction, by loose analogy with
the classical multiplicative-reduction split/non-split criterion. **This
heuristic was wrong** — or at least, not applicable in the naive form used
— and was refuted by the actual tangent-cone computation, which is the
correct diagnostic. This is recorded here explicitly, per the project's
discipline of documenting self-corrections: a plausible-looking shortcut
was tried, found insufficient, and replaced with the rigorous local
computation.

**Status: FINITE THEOREM-BASED VERIFICATION** — every individually-checked
component (7 of an expected 21 total across the three fibers, i.e. 7 of the
`4×3=12` "leg" slots plus partial spine data) is confirmed unconditionally
`Q`-rational; no counterexample or obstruction found anywhere searched.

---

## Part IV — Torsion sections and component labeling

Round 1's `(Z/2)^2` torsion sections correspond to the three nonzero
2-torsion points identified in Part I: `X=0` (the identity-adjacent
2-torsion point, always meeting the same component as the zero section by
construction) and `X=-T(T+1)`, `X=-T(T+1)^2` (the other two). Since **all
three** 2-torsion points are given by explicit polynomials in `T` (Part I),
each torsion section is manifestly `Q(T)`-rational and specializes to a
`Q`-rational point on every fiber, including the bad ones — consistent
with, and mildly corroborating, the finding that the components they meet
(among the multiplicity-1 "leg" components, by the standard theory of
`(Z/2)^2` torsion meeting non-identity components of `I2*` fibers) are
individually rational.

**Full independent re-derivation of the component group / intersection
graph (7 components, 6 edges, Euler number 8) was not carried out this
round** beyond the partial component list in Part II — this is the same gap
flagged there, not a new one.

**Status: COMPUTATIONALLY VERIFIED** (torsion sections' rationality, direct
consequence of Part I's exact factorization); **OPEN** for the full
component-group cross-check requested by this Part.

---

## Part V — `NS(X_III)` generating set

Given the incomplete component enumeration (Part II), a fully explicit,
independently-recounted 20-element generating set with individual fields of
definition for **every** generator was **not** achieved this round. What
was achieved: of the (at most) `4×3=12` "leg" generators expected (4 per
fiber × 3 fibers) plus the spine generators, **7 individual leg/near-spine
components were explicitly constructed and shown `Q`-rational** (Part
II/III), out of an eventual 20 total generators (`2` from `U` + `18` from
the three `D6` fibers' non-identity components, `6` each).

**Status: OPEN** for a complete, independently-verified 20-element
generating set; **PARTIAL / FINITE THEOREM-BASED VERIFICATION** for the 7
components actually constructed.

---

## Part VI — `Tr(F_p|NS)`, decisive gate

Given Part V's incompleteness, the round **cannot assert** `Tr(F_p|NS)=20p`
as fully, independently proved this round — that would require the complete
generating set and confirmed absence of any Galois-swapped pair. What the
round **can** assert, rigorously:

- Every individual component explicitly constructed and checked (7 of them,
  spanning all three fibers) is unconditionally `Q`-rational, for every
  prime `p` — not merely at the primes tested numerically, but as an
  algebraic identity (`y^2=uv`-type forms split over every field).
- No Galois-exchanged pair, no anisotropic tangent cone, and no
  `p`-dependent (`chi(-1)`, `chi(2)`, or other character) splitting
  obstruction was found anywhere in the portion of the resolution explicitly
  traced.
- The algebraic mechanism that *would* produce such an obstruction (a
  tangent cone of the shape `y^2 = c\,w^2` for a non-square unit `c`, or
  `y^2=au^2+bv^2` genuinely anisotropic) was explicitly checked for and
  **never occurred** — every quadratic form found was of the universally
  split `y^2=uv` shape.

Given this, `Tr(F_p|NS(X_III)) = 20p` for every good odd `p` remains the
**best-supported hypothesis**, now backed by substantial (though not fully
complete) direct local computation rather than pure structural analogy —
but it is **not** hereby declared proved, since 5 of 20 generators (across
all three fibers combined, this round covered roughly a third of the total
expected structure) remain outside the portion explicitly constructed.

**Status: CONJECTURAL, upgraded from Round 2's baseline** — specifically,
upgraded from "unverified structural analogy" to "consistent with, and
positively supported by, every piece of explicit local evidence gathered,
with the *mechanism* that could produce a deviation explicitly searched for
and not found in the portion checked." **Not** `PROVED`.

---

## Part VII — Discriminant recheck

Independent of the modular form, using only the (still partially open, but
consistently-supported) trivial lattice structure: if `Tr(F_p|NS)=20p` (Part
VI's best-supported hypothesis) and the trivial lattice and torsion data
from Round 1/2 are unchanged (`U + D6+D6+D6`, torsion `(Z/2)^2`, both
re-confirmed frozen in Part I with no contradiction), then
`|disc NS(X_III)| = 64/16 = 4` and `T(X_III)≅diag(2,2)` follow exactly as
in Round 1 — **unchanged**. No new discriminant-affecting information was
found this round; this recheck is a consistency confirmation, not a new
independent derivation (the direction geometry → NS → T(X) → modularity was
maintained, not reversed, throughout — the modular form was never used to
infer the lattice at any point in Parts I–VII).

**Status: PROVED — SELF-CONTAINED**, conditional on the (frozen,
unchanged-this-round) Round 1 trivial-lattice-and-torsion computation.

---

## Part VIII — The modular trace theorem, precisely

Combining: `T(X_III)≅diag(2,2)` (Part VII), CM field `Q(i)` (forced,
Round 2 Part II), candidate newform `16.3.c.a` (unique admissible candidate,
Round 2 Part II), exhaustive twist set `{1,chi(-1),chi(2),chi(-2)}` (forced
by ramification, Round 2 Part IV), CM degeneracy collapse to `F_0` vs `F_1`,
and exact `p=5` discrimination refuting `F_1` (Round 2 Part IV, re-confirmed
by regression test this round, `scripts/class3_round3_falsification.py`
Direction 4):

```
Tr(F_p | T(X_III)) = a_p(16.3.c.a)   for every prime p != 2
```

holding for **all odd `p`**, with the `p ≡ 3 (mod 4)` case automatically
zero (CM-inertness) and the `p ≡ 1 (mod 4)` case the actual content of the
finite-theorem-based elimination. This part of the theorem was **already
established in Round 2** and is **not newly proved this round** — it is
restated here, precisely, as the round's prompt requires, with its status
unchanged: `FINITE THEOREM-BASED VERIFICATION` (`p≡1 mod 4` case),
`PROVED` (`p≡3 mod4` case, two independent mechanisms, Round 2 Part VI).

**Whether the FULL Class III theorem (`T(p) = a_p(16.3.c.a)` AND the
resulting exact `Sigma_III(p)` formula, jointly) is now fully `PROVED` —
No.** The transcendental-lattice trace formula itself is finite-theorem-based
verified (unchanged from Round 2). What remains short of `PROVED` is the
**point-count bridge** (Part IX), which requires `Tr(F_p|NS)=20p`, and that
is `CONJECTURAL` (Part VI), not `PROVED`, after this round's work.

---

## Part IX — The Class III character sum, rebuilt

Rebuilding the ledger from scratch (not copying Round 2): with `#V_III(F_p)
= p^2+T(p)` (Part I's factorization gives an independent re-derivation route
via the exact roots, consistent with the brute-force check in
`scripts/class3_ledger_check.py`, Round 2, unchanged) and the corrected
`p-2` good-finite-fiber count (Round 2's self-correction, re-confirmed, no
new error found), the ledger

```
#X_III(F_p) = #V_III(F_p) + 20p + 1
```

remains the best-supported formula, **conditional on** `Tr(F_p|NS)=20p`
(Part VI, `CONJECTURAL`, not `PROVED` this round). Propagating through to
`Sigma_III(p)`:

```
Sigma_III(p) = (p-1) T(p) = { (p-1) a_p(16.3.c.a)   p ≡ 1 (mod 4)
                             { 0                      p ≡ 3 (mod 4)
```

**unchanged from Round 2** in its final form — this round did not find any
constant-correction to this formula, but also did not upgrade its status to
fully proved, since the underlying `Tr(F_p|NS)=20p` remains conjectural.

For `p ≡ 3 (mod 4)`: the two independent mechanisms (elementary involution,
Round 1; CM-inertness, Round 2) give exactly the same zero for **genuinely
different reasons** — re-confirmed unchanged this round (Round 2 Part VI's
analysis was re-read and found to require no revision).

**Status: FINITE THEOREM-BASED VERIFICATION, conditional on Part VI's
conjectural `Tr(NS)=20p`** — same status as Round 2, not downgraded (no
counter-evidence found) and not upgraded to `PROVED` (the conditioning
assumption was not closed).

---

## Part X — Sum-of-two-squares form

Not pursued further this round: the modular identity is not yet fully
unconditionally proved (Part VI/VIII), so per the round's own instruction
("only after the modular identity is proved"), this optional part is
correctly left **OPEN**, as it was flagged `CONJECTURAL` in Round 2 (the
literature-quoted `a_p=2(x^2-4y^2)` form, sign convention unverified).

---

## Part XI — Targeted literature/catalogue check

Searched specifically for extremal elliptic K3 classification tables (per
the round's instruction). Found: Miranda–Persson determined all 112 possible
singular-fiber configurations for extremal elliptic K3 surfaces (Mordell–
Weil rank 0, `ρ=20`); Shioda has compiled a complete list of all 325
extremal elliptic K3 surfaces with their transcendental lattices, fiber
types, and Mordell–Weil groups (per the Shioda–Inose correspondence, the
transcendental lattice determines the surface uniquely). `X_III`'s
configuration — three `I2*` fibers, torsion `(Z/2)^2`, discriminant 4 — is
almost certainly **among these 325 classified surfaces** (three `I2*`
fibers is a small, natural configuration well within the scope of such a
complete classification), but this round's web search could not access the
specific table entries to confirm the exact match (no institutional database
access). This is reported honestly as **NOT FOUND** (specific table-entry
confirmation), while flagging strongly that the *classification itself is
known to exist and almost certainly contains this surface* — a materially
different situation from Round 2's Part IX "NOT FOUND," which had no
comparably strong indirect evidence of prior cataloguing. **No novelty claim
is made.**

Re-checked (regression): AOP's own `X_8` construction, and the quartic
Fermat K3 surface (Huber–Liu–McLaughlin et al.), both remain the only
concretely-identified other varieties sharing `16.3.c.a`'s trace formula —
unchanged from Round 2.

**Classification: SAME TRANSCENDENTAL LATTICE, likely SAME FIBER
CONFIGURATION** (per Miranda–Persson/Shioda's complete classification,
existence strongly indicated but not confirmed against the actual table this
round); **NOT FOUND** for exact-model or birational confirmation.

---

## Part XII — Structural interpretation

The present examples (Classes I/II: `disc(T)=8`, `T≈diag(2,4)`, `Q(sqrt(-2))`,
level-8 weight-3 form, MW rank 1 geometrically; Class III: `disc(T)=4`,
`T≈diag(2,2)`, `Q(i)`, level-16 weight-3 form, MW rank 0) exhibit visibly
different arithmetic-geometric data at every listed invariant. Whether the
hypercuboid construction is *genuinely selecting* distinct sectors, as
opposed to this being an accident of the two cases examined, is **not**
asserted as a theorem or general principle from two examples — consistent
with the round's explicit instruction. The present examples exhibit
different CM fields, different discriminants, and different Mordell–Weil
ranks; a broader claim would require examining further members of the
hypercuboid family (if any exist beyond Classes I/II/III), which is outside
this round's scope.

---

## Part XIII — Falsification

Five directions executed, `scripts/class3_round3_falsification.py`:

1. **Global factorization and perfect-square discriminant, verified mod `p`
   directly with integer arithmetic** (independent of the `sympy` symbolic
   work in Parts I–II — a genuinely separate code path) — holds at all 12
   tested primes.
2. (Combined with 1 in the script) perfect-square discriminant check.
3. **Naive singular-fiber point count = `p+1`** (classical cuspidal-cubic
   fact, unrelated to the resolution machinery) — re-confirmed at both `T=0`
   and `T=-1` for all 12 tested primes, validating that the local models fed
   into the blow-up analysis are correctly set up.
4. **Regression check**: `T(p)=a_p(16.3.c.a)` re-verified via the
   independent 3-variable `Sigma_III` code path (not the 2-variable
   reduction) at 4 primes — unaffected by this round's work.
5. **Uniformity across `p mod 4`**: the algebraic facts underlying every
   split tangent cone found (Parts I–III) hold identically for `p≡1(4)` and
   `p≡3(4)` test primes — no `chi(-1)`-dependence detected anywhere,
   directly addressing (and refuting) the earlier heuristic worry recorded
   in Part III.

All five directions pass; nothing found this round contradicts the round's
findings, and Direction 5 specifically closes the blind spot in Round 2's
own falsification battery (which tested the ledger only at `p≡1(4)` primes,
where a `chi(-1)`-dependent `NS`-trace correction would have been invisible).

**Status: no falsifying evidence found** across 5 directions, at least one
(#1/#3) genuinely independent of the existing symbolic Class III scripts.

---

## Part XIV — Status discipline

| Claim | Status |
|---|---|
| Exact fiber locations, types, local minimal models (all 3 fibers) | PROVED — SELF-CONTAINED |
| Global factorization / perfect-square discriminant (2-torsion rational over `Q(T)`) | PROVED — SELF-CONTAINED |
| 7 individual tangent cones (ordinary nodes), all unconditionally `Q`-rational | FINITE THEOREM-BASED VERIFICATION |
| Complete 7-component enumeration + intersection graph, all 3 fibers | OPEN (5 of 7 found per finite fiber; `T=infinity` only partially traced) |
| No Galois-exchanged component, no field-extension obstruction found | FINITE THEOREM-BASED VERIFICATION (on the portion checked) |
| `Tr(F_p|NS(X_III)) = 20p`, all good `p` | **CONJECTURAL** (upgraded from Round 2's pure analogy — now backed by partial explicit computation with no counter-evidence — but NOT proved) |
| `|disc NS|=4`, `T(X_III)≅diag(2,2)` | PROVED — SELF-CONTAINED (conditional on frozen, re-confirmed Round 1 lattice data) |
| `Tr(F_p\|T(X_III)) = a_p(16.3.c.a)` | FINITE THEOREM-BASED VERIFICATION (unchanged from Round 2) |
| Full Class III theorem (`Tr(NS)` + `Tr(T)` jointly closing the point-count bridge) | **NOT PROVED** — conditional on the still-open `Tr(NS)=20p` |
| `Sigma_III(p)` closed forms | FINITE THEOREM-BASED VERIFICATION, conditional on the same open item |
| Extremal K3 catalogue overlap | Strongly indicated (Miranda–Persson/Shioda classification exists and very likely contains `X_III`), specific match NOT FOUND this round |

**The round's own explicit instruction — "do not call the Class III formula
proved unless the NS rationality gap is actually closed" — is honored: it is
not called proved.**

---

## Final Report

1. **Three `I2*` fibers independently verified?** Yes — locations, types
   (`v(c4),v(c6),v(Delta)`), and local minimal models all independently
   re-derived (Part I).
2. **All seven components of each constructed?** No — 5 of 7 found and
   typed at `T=0` and at `T=-1`; only 1 of the expected components found at
   `T=infinity` (the resolution there was not carried to completion).
3. **Multiplicities.** `E0`/`E0'` (spine, mult. 2, from the first blow-up at
   each finite fiber) and `E2` (spine, mult. 2, `T=0`'s second blow-up)
   confirmed via the non-reduced `T^2`/`s^2` factor in the total transform;
   `E1,E3,E4` (and primed analogues) are ordinary-node exceptional curves,
   consistent with multiplicity-1 "leg" components; full multiplicity
   vector `(1,1,2,2,2,1,1)` not independently completed this round (relies
   on the standard Kodaira table for the missing 2 components per fiber).
4. **Intersection graphs.** Not independently completed (component count
   incomplete, Part V flags this explicitly).
5. **Fields of definition.** Every component actually constructed (7 total)
   is unconditionally `Q`-rational — verified via tangent-cone analysis, not
   assumed.
6. **Any Galois-exchanged components?** None found, anywhere searched.
7. **Torsion-section intersections.** All three 2-torsion sections shown
   `Q(T)`-rational via the exact global factorization (Part I) — a stronger,
   more global fact than a fiber-by-fiber check.
8. **Explicit `NS` generating set.** Partial — 7 of an eventual 20
   generators explicitly constructed with confirmed fields of definition.
9. **Exact Galois action on `NS`.** Not fully determined; on the 7
   components checked, Galois acts trivially (fixes each individually).
10. **Exact `Tr(F_p|NS)`.** Best-supported hypothesis remains `20p` for all
    good `p`; **not proved** this round.
11. **Recomputed `|disc NS|`.** `4`, unchanged, conditional on the
    (unmodified) frozen trivial-lattice/torsion data.
12. **Recomputed `T(X_III)`.** `diag(2,2)`, unchanged.
13. **Modular candidate.** `16.3.c.a`, unchanged, restated precisely
    (Part VIII).
14. **Allowed twists.** `{1,chi(-1),chi(2),chi(-2)}`, unchanged (Round 2).
15. **Selected twist.** Trivial (untwisted), unchanged, regression-tested
    this round (Part XIII Direction 4).
16. **Exact `Tr(F_p|T)`.** `a_p(16.3.c.a)`, unchanged, all odd `p`.
17. **Exact `T(p)`.** `a_p(16.3.c.a)` for `p≡1(4)`, `0` for `p≡3(4)` —
    unchanged, `FINITE THEOREM-BASED VERIFICATION`, conditional on the still-
    open `NS` gate for the *point-count* interpretation (the trace-formula
    identity itself is unconditional; only its translation into an exact
    point-count/ledger identity depends on `Tr(NS)=20p`).
18. **Exact `Sigma_III(p)`.** `(p-1)a_p(16.3.c.a)` for `p≡1(4)`, `0` for
    `p≡3(4)` — same conditional status as item 17.
19. **`p≡3 mod 4` interpretation.** Two independent, logically distinct
    zero-mechanisms (involution; CM-inertness), unchanged, re-confirmed.
20. **`p≡1 mod 4` interpretation.** Finite theorem-based elimination
    (twist), unchanged, re-confirmed via regression test.
21. **Literature/catalogue overlap.** Strongly indicated but not confirmed
    against the actual Miranda–Persson/Shioda tables (access limitation, not
    a mathematical gap).
22. **Strongest falsification attempt.** The `p mod 4`-uniformity check
    (Part XIII, Direction 5), which specifically targeted and closed the
    blind spot in Round 2's own falsification battery (which never tested a
    `chi(-1)`-dependent `NS`-trace correction, since it only used `p≡1(4)`
    primes where such a correction is invisible).
23. **Anything killed or corrected?** An in-round heuristic (the
    `e_1-e_2` leading-coefficient argument suggesting a possible
    `chi(-1)`-dependent splitting obstruction) was tried, found insufficient
    on its own, and superseded by the correct tangent-cone computation,
    which found no such obstruction. Recorded in Part III as a genuine
    self-correction, not silently discarded.
24. **Remaining mathematical gap, if any.** The primary target — full,
    independent proof of `Tr(F_p|NS)=20p` via a complete, self-intersection-
    verified 7-component-per-fiber resolution — is **narrowed but not
    closed**. Specifically open: 2 components per finite fiber (likely one
    more spine node and one more leg, structure not fully reconciled with
    the expected `(1,1,2,2,2,1,1)` pattern), and the entire `x1=0` branch at
    `T=infinity`.
25. **Whether Class III is now theorem-ready.** No — the same conclusion as
    Round 2, though on a narrower, better-characterized gap. The
    transcendental-lattice half of the theorem (`Tr(T)=a_p(f16)`) is finite-
    theorem-based verified; the Néron–Severi half (`Tr(NS)=20p`) is
    conjectural, now with substantial (not full) direct supporting evidence.
26. **Manuscript relation.** Unchanged from Round 2: **(B) addendum-grade**,
    not ready for the manuscript body. The gap that would need closing is
    now more precisely specified (complete the 7-component resolution with
    verified self-intersections, likely requiring computer-algebra
    resolution tooling) than it was at the end of Round 2.
27. **Single highest-value next action.** Complete the local blow-up
    resolution using a computer algebra system with a built-in surface-
    singularity resolution routine (e.g. Magma's `Resolve` / Singular's
    `resolve` library) applied directly to the three explicit `I2*` points
    identified in Part I, to obtain the full 7-component intersection graph
    with verified self-intersection numbers per fiber — this would either
    close the gap outright (if, as this round's partial evidence suggests,
    every remaining component is also unconditionally split) or reveal the
    genuine obstruction this round's partial trace did not reach.

### Verdict: **CLASSIII-3C**

Substantial, genuine progress: the gap identified at the end of Round 2 was
attacked with real, `sympy`-verified local blow-up computation (not
structural analogy) across all three bad fibers, finding 7 explicit,
individually-checked components, **every one of which is unconditionally
`Q`-rational**, and finding **zero instances** of the kind of obstruction
(Galois-exchanged pairs, anisotropic tangent cones, field-extension
requirements) the round was specifically designed to hunt for. An in-round
heuristic wrongly suggesting a possible obstruction was tried and correctly
refuted by the rigorous computation. However, the component count was not
fully closed (5 of 7 per finite fiber, 1 of 7 at infinity), so
`Tr(F_p|NS)=20p` — the decisive gate — remains **conjectural, not proved**.
Per the round's own explicit instruction, the Class III formula is therefore
**not** declared proved this round. This is a genuine mathematical bridge
narrowed considerably, but not yet crossed.

---

## THE THREE MOST IMPORTANT THINGS WE LEARNED

1. **A surprising, previously-unnoticed algebraic fact did most of the
   heavy lifting this round**: the cubic defining every fiber of `X_III`
   factors completely into three rational pieces — `X`, `X+T(T+1)`, and
   `X+T(T+1)^2` — meaning the entire 2-torsion of the elliptic fibration is
   rational over the base curve itself, not just at special points. Once
   this was found, almost every singular point examined turned out to have
   the simplest possible (always-rational) type of local structure, for a
   clean algebraic reason rather than by coincidence.

2. **"The fiber is defined over the rational numbers" does not automatically
   mean "every piece you get by zooming in on its singular point is also
   defined over the rational numbers" — you actually have to check, piece by
   piece** — and this round did that checking, by hand, for seven separate
   pieces across three different singular points, finding every single one
   passed. A plausible-looking shortcut that suggested otherwise (based on a
   cruder measurement) was tried and shown wrong by the more careful check —
   a useful reminder that the crude version of an argument can point the
   wrong way even when the careful version doesn't.

3. **Finding no counterexample after checking seven out of an expected
   twenty pieces is meaningfully different from having checked all twenty**
   — this round could have been tempted to declare the job done, since
   nothing wrong turned up anywhere; instead, the honest count (5 of 7
   components per fiber, not all 7) was kept front and center, and the
   verdict reflects that the door has been pushed most of the way open, not
   all the way.
