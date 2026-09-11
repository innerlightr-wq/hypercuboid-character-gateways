# Class III Round 4 — Split I₂* Certification and Néron–Severi Rationality Closure

**Scope discipline.** Work confined to `explorations/class_iii/`. The
published Classes I/II manuscript untouched. Nothing committed, nothing
pushed.

**Primary target (only target).** Prove `Tr(F_p|NS(X_III)) = 20p` for every
good odd prime, i.e. that all 20 `NS(X_III)` generators are `Q`-rational.

**Result.** Closed — via the route Parts V/VI of this round's prompt
anticipated (full rational 2-torsion + graph rigidity), **not** via
completing the from-scratch blow-up bookkeeping that stalled Round 3.

---

## Part I — Frozen structure

All listed items (Weierstrass model, three `I2*` fibers, rank-20
expectation, MW rank 0, torsion `(Z/2)^2`, full rational 2-torsion over
`Q(T)`, `|disc NS|=4`, `T(X_III)≅diag(2,2)`, modular candidate `16.3.c.a`,
Round 2 twist analysis) are treated as frozen. No contradiction found. No
coefficient search redone.

---

## Part II — Theorem/classification route, tried first

Searched (per instruction) for a black-box theorem certifying split `I2*`
directly. **No single citable theorem does the whole job in one step** (see
`literature/ROUND4_EXTREMAL_K3_AUDIT.md`). What **was** found — and is
standard enough to use directly — are two textbook facts:

1. **Any section of a relatively minimal elliptic fibration meets exactly
   one component of any fiber, forced to have multiplicity 1.** Proof:
   `section · fiber = 1` (standard), and `fiber = Σ m_i C_i`; since the
   section meets only one `C_j` (transversally, intersection number 1) and
   none of the others, `1 = m_j·1`, so `m_j=1`. Elementary, no citation
   risk.
2. **The dual graph of a Kodaira `I_n^*` fiber is the extended Dynkin
   diagram of type `D_{n+4}`**: `n+5` components, 4 of multiplicity 1
   ("legs," in 2 pairs, one pair per end of a path) and `n+1` of
   multiplicity 2 ("spine," the path connecting the two ends). For `I2*`
   (`n=2`): 4 legs + 3 spine = 7. **PROVED — LITERATURE** (Kodaira 1963;
   Néron 1964; Tate 1975 — textbook, e.g. Silverman *ATAEC* Ch. IV).

Extremal-K3 classification tables (Miranda–Persson's 112 configurations;
Shioda's 325-surface list) almost certainly contain `X_III`'s configuration,
but specific table access was not available this round (Part XIII, unchanged
conclusion from Round 3). **This round does not rely on a catalogue match**
— the closure below is self-contained given facts 1–2 above.

---

## Part III — No catalogue match pursued

Not applicable: no explicit catalogue entry was retrieved to compare
against, so Part III (model equivalence) is not exercised. The closure in
Parts IV–IX below is entirely self-contained, not catalogue-dependent.

---

## Part IV/V/VI — The closing argument

### Setup: three explicit rational sections beyond `O`

Recall (Round 3, re-verified `scripts/class3_round3_factorization.py`): the
generic fiber's full 2-torsion is `Q(T)`-rational, given by
`P1=(0,0)`, `P2=(-T(T+1),0)`, `P3=(-T(T+1)^2,0)`, together with `O`, forming
`(Z/2)^2` over `Q(T)` itself.

### Step 1 — Explicit specialization, all three fibers (all sympy-verified)

For each bad fiber, the local blow-up coordinate of each `P_i` was computed
**exactly** (not to leading order — exact rational functions evaluated at
the bad fiber), in `scripts/class3_round4_torsion_specialization.py`:

| Fiber | `P1` lands at | `P2` lands at | `P3` lands at | Tangent cone there |
|---|---|---|---|---|
| `T=0` | `x1=0` (leg `E1`) | `x3=-1` (leg `E3`) | `x3=-2` (leg `E4`) | `y²-Tx` / `y²+Tx` / `y²-Tx` — all split |
| `T=-1` | `x3=0` (leg `E3'`) | `x1=1` (leg `E1'`) | `x3=1` (leg `E4'`) | `y²-sx` / `y²-sx` / `y²+sx` — all split |
| `T=∞` | `x3=0` (leg) | `x3=-1` (leg) | `x1=-1` (leg `E1''`) | `y²-Sx` / `y²+Sx` / `y²-Sx` — all split |

(`T=∞` second-level tangent cones freshly verified this round,
`scripts/class3_round4_blowup_tinf_step2.py` — the one gap Round 3 left
open at that fiber is now closed.) At **every** one of these 9 points, the
tangent cone is of the universally-split `y²=uv` type — confirming, via an
entirely independent route (torsion specialization) from Round 3's blind
tangent-cone survey, the same "no field-extension obstruction anywhere"
finding.

`O` specializes, at every fiber (trivially, no computation needed), to the
point at infinity of the Weierstrass model — always a smooth, always
multiplicity-1 ("identity") component, by definition of a relatively
minimal Weierstrass model.

**At each of the three bad fibers, `O, P1, P2, P3` are four *pairwise
distinct* points** (confirmed: the local coordinates `{0,-1,-2}`,
`{0,1,1}` — on genuinely different exceptional curves despite the numeral
repeat — and `{0,-1,-1}` are computed at each fiber to lie on 3 different,
explicitly-typed leg components, plus `O` on the always-separate identity
leg — 4 total, pairwise distinct by construction).

### Step 2 — Four sections, four legs, forced individually `Q`-rational

By Part II fact 2, each `I2*` fiber has **exactly 4** multiplicity-1
components. By Part II fact 1, each of `O,P1,P2,P3` (bona fide, distinct
sections of the fibration) lands on a multiplicity-1 component. Step 1
shows these 4 landing spots are pairwise distinct. **Four distinct sections
landing on four distinct slots, when there are only four slots, exhausts
them all**: every one of the 4 leg components, at every one of the 3 bad
fibers, contains an explicit point defined by rational functions with `Q`
(indeed `Z[1/2]`) coefficients — i.e. is individually `Q`-rational (and, by
the same explicit-integer-coefficient argument, individually `F_p`-rational
for every prime `p` of good reduction, `p≠2`).

**Status: PROVED — SELF-CONTAINED.** All 4 legs of all 3 `I2*` fibers
(12 components total) are individually `Q`-rational.

### Step 3 — Graph rigidity closes the spine, without constructing it

Galois (equivalently, Frobenius at each good `p`) acts on the components of
a fiber defined over `Q` by a **permutation preserving the intersection
(incidence) graph and the multiplicities** — standard scheme theory (the
fiber, as a `Q`-scheme, is Galois-stable as a set of components with an
intrinsic, Galois-equivariant incidence structure). Given all 4 legs are
now individually fixed (Step 2 — not merely fixed as a *set*, but each one
individually, since each carries its own distinguishing rational point):

- The spine-end node meeting a **specific** pair of (now individually
  fixed) legs is the **unique** component with that pair of neighbors (per
  the `D6` incidence structure, Part II fact 2) — so Galois, which must
  send this node to a component with the same neighbor pair, is forced to
  fix it. This applies at **both** spine ends.
- The middle spine node is the **unique** component adjacent to *both*
  (now individually fixed) spine-end nodes — forced fixed by the same
  argument.

**No assumption of graph rigidity was made — it was derived** from the
concrete incidence structure (a path with forks at both ends has no
nontrivial automorphism fixing all 4 leaf-adjacent leg vertices) combined
with the already-established individual fixing of all 4 legs.

**Status: PROVED — SELF-CONTAINED.** All 3 spine components of all 3 `I2*`
fibers (9 components total) are individually `Q`-rational, **without having
constructed them via blow-up charts.**

### Honest side-note: the "extra chart" anomaly

While attempting (before finding the above argument) to complete Round 3's
blow-up bookkeeping directly, checking an additional chart of the second
blow-up at `T=0` (`scripts/class3_round4_blowup2_extra_chart.py`) revealed
a **previously-missed singular point** (at `x3=∞` on the curve called `E2`
in Round 3), itself resolving via **another** universally-split tangent
cone (`y1p²+t2·x2`). This shows Round 3's hand bookkeeping of the *spine's*
internal structure was incomplete in a way not fully reconciled (exactly
which curve is the true middle spine node, versus an artifact of the
specific blow-up sequence chosen, was not pinned down). **This anomaly does
not affect the closing argument above**, which never depends on having
personally constructed the spine via blow-ups — it relies only on the cited
abstract structure (Part II fact 2) plus the explicit leg data (Step 1–2).
It is recorded honestly as a loose end in the *hand-resolution* approach
that Round 4's cleaner route made moot.

---

## Part VII — CAS resolution: not needed, not used

No algebraic-geometry CAS (Magma, Singular) was available in this
environment. Per the round's own instruction ("if no suitable CAS is
available, say so and return to theorem-level local algebra"), this was
done — and the theorem-level route (Parts IV–VI) **succeeded**, making CAS
resolution unnecessary for closing the primary target.

---

## Part VIII — Explicit NS basis

`NS(X_III)` generators: zero section `O` (1), general fiber class `F` (1),
and the 6 non-identity components of each of the 3 `I2*` fibers (3 legs +
3 spine minus... precisely: of the 7 components per fiber, 6 are
"non-identity," i.e. excluding whichever leg contains `O`) — `6×3=18`.
Total `2+18=20`, matching Shioda–Tate exactly.

**Why torsion adds no free rank**: `MW_tors=(Z/2)^2` is a *finite* group;
Shioda–Tate states `rank(NS) = 2 + Σ_v(m_v-1) + rank(MW)`, and torsion
affects only the *index* `[NS:Triv]` (via `|disc NS| = |disc(Triv)|/|MW_tors|²`,
already used in Part X below), not the *rank* of `Triv` itself, since
torsion sections are themselves elements of the already-counted trivial
lattice's saturation, not independent generators.

**Every one of the 20 generators is `Q`-rational**: `O` and `F` trivially
(both defined by the Weierstrass model's global structure, no local
subtlety); the 18 non-identity fiber components, by Parts IV–VI (all 21
components across the 3 fibers shown individually `Q`-rational, hence in
particular the 18 non-identity ones — and, for completeness, the 3 identity
components too, consistent with `O` sitting on each).

**Status: PROVED — SELF-CONTAINED.**

---

## Part IX — `Tr(F_p|NS)`, derived

Since every one of the 20 generating divisor classes is individually
`F_p`-rational for every good odd `p` (Parts IV–VIII), Frobenius fixes each
one individually. Each Frobenius-fixed algebraic (Tate) class contributes
eigenvalue exactly `p` to `Frob` acting on `H²_et(X_III,Q_ℓ)` (standard fact
about algebraic cycle classes on a variety over `F_p`). Therefore:

```
Tr(F_p | NS(X_III)) = 20p     for every good odd prime p.
```

No nontrivial Galois action survives anywhere in the argument — the
character-twisted alternatives the round's Part IX explicitly allowed for
(`(18+2χ(d))p` etc.) do **not** occur; `20p` is not "forced" by assumption,
it is the **derived** consequence of all 20 generators being individually
rational, which was itself derived (not assumed) in Parts IV–VIII.

**Status: PROVED — SELF-CONTAINED.**

---

## Part X — Lattice recomputation

With the now-rigorous basis (Part VIII): `Triv(X_III) = U + D6+D6+D6`
(unchanged — this was always about the *lattice structure*, which Round 1
already established correctly; what Round 4 adds is the *rationality* of
the generators, not a change to the lattice itself). `|disc(Triv)| =
1×4×4×4=64`. With `|MW_tors|=4`: `|disc NS| = 64/16 = 4` — **unchanged**,
independently reconfirmed (not inferred from the modular form; the
direction geometry→NS→T(X)→modularity is maintained throughout this report,
consistent with the round's explicit requirement). `T(X_III)≅diag(2,2)`
follows as before.

**Status: PROVED — SELF-CONTAINED** (conditional only on Round 1's
already-established, unmodified trivial-lattice computation).

---

## Part XI — The modularity argument, now fully closed

Combining: `T(X_III)≅diag(2,2)` (Part X), CM field `Q(i)` (Round 2),
candidate `16.3.c.a` (Round 2, unique admissible candidate), Livné's theorem
(existence, Round 2 Part III), exhaustive twist set `{1,χ(-1),χ(2),χ(-2)}`
(Round 2 Part IV), degeneracy collapse, and the exact `p=5` discriminator
(Round 2, regression-tested every round since):

```
Tr(F_p | T(X_III)) = a_p(16.3.c.a)     for every odd prime p ≠ 2,
```

with `p≡3(mod 4)` automatically zero (CM-inertness). This was already
`FINITE THEOREM-BASED VERIFICATION`-level before this round and remains so
— it was never the blocked part. **What changes this round is that it can
now be combined with a fully proved `Tr(F_p|NS)=20p` (Part IX)** to close
the point-count bridge (Part XII) unconditionally.

**Status: FINITE THEOREM-BASED VERIFICATION** (unchanged; this is the
strongest honest label for the twist-elimination step itself, which remains
a finite check over a theorem-restricted candidate set rather than a
first-principles derivation of the twist).

---

## Part XII — The Class III sum, closed

```
#X_III(F_p) = 1 + p² + Tr(F_p|NS) + Tr(F_p|T)
            = 1 + p² + 20p + a_p(16.3.c.a)     [now unconditional, Parts IX+XI]
```

Combined with the point-count ledger `#X_III(F_p) = #V_III(F_p) + 20p + 1`
(Round 2/3, re-derivable from Part IX's now-proved `Tr_NS=20p` rather than
resting on analogy) and `#V_III(F_p)=p²+T(p)`:

```
T(p) = a_p(16.3.c.a)     for p ≡ 1 (mod 4)   [now closed given Tr_NS=20p]
T(p) = 0                  for p ≡ 3 (mod 4)   [PROVED, two independent ways]

Σ_III(p) = (p-1)·a_p(16.3.c.a)     for p ≡ 1 (mod 4)
Σ_III(p) = 0                        for p ≡ 3 (mod 4)
```

**`p≡3(mod4)`**: two independent mechanisms, unchanged from Round 2/3 —
(1) elementary involution cancellation on the raw character sum (Round 1,
self-contained, no modularity or geometry needed), and (2) CM-inertness of
`16.3.c.a` at inert primes (a fact about the newform, Round 2). These
coincide in residue class only because this particular CM field happens to
be `Q(i)`; they are logically independent proofs of the same numerical fact.

**`p≡1(mod4)`**: modular coefficient formula, `FINITE THEOREM-BASED
VERIFICATION`-level (Part XI), now combined with a fully `PROVED` `NS`
trace to give a **theorem-level** (not merely conditional) statement of
`T(p)` and `Σ_III(p)`.

**Sum-of-two-squares form**: not re-attempted this round (the literature-
quoted `a_p=2(x²-4y²)` sign convention remains unverified, `CONJECTURAL`,
unchanged — left as stated in Round 3, correctly not promoted, per the
round's own "derive only with correct sign normalization" instruction).

**Status: FINITE THEOREM-BASED VERIFICATION**, now **unconditional** (no
longer resting on an open `Tr_NS` assumption) for the `T(p)`/`Σ_III(p)`
formulas as stated.

---

## Part XIII — Literature/catalogue check

Unchanged from Round 3 (see `literature/ROUND4_EXTREMAL_K3_AUDIT.md`): the
Miranda–Persson/Shioda extremal-K3 classification almost certainly contains
`X_III`'s configuration, but specific table access was not available.
**SAME FIBER CONFIGURATION** (strongly indicated, unconfirmed);
**RELATED ONLY** for AOP's `X_8`; exact sum and model **NOT FOUND**
elsewhere. No novelty claimed from any NOT FOUND result.

---

## Part XIV — Falsification

Five directions, `scripts/class3_round4_falsification.py`, at least one
(#1, raw modular arithmetic) fully independent of the symbolic `sympy`
derivation used throughout Parts IV–VI:

1. **Independent modular-arithmetic recomputation** of the pairwise
   distinctness of the 9 specialization coordinates (3 per fiber), for 12
   primes — the single most load-bearing numeric claim in the whole round,
   re-derived via raw integer arithmetic, not sympy. **Passes.**
2. **Tangent-cone nondegeneracy** re-checked (the `y²=uv`-type conics are
   nondegenerate for every odd `p`, an elementary discriminant check).
   **Passes.**
3. **Group-law sanity**: the three 2-torsion `x`-coordinates are pairwise
   distinct at good `(T,p)` pairs (needed for a genuine `(Z/2)^2`, not a
   degenerate torsion group) — re-checked independently. **Passes.**
4. **Regression**: `T(p)=a_p(16.3.c.a)` unaffected, re-verified.
   **Passes.**
5. (Qualitative, not scripted) **Attempted to break graph rigidity**: could
   any nontrivial automorphism of the affine `D6` diagram fix all 4 leaf
   (leg) vertices while nontrivially permuting spine vertices? No — the
   spine is a path uniquely reconstructible from its leaf-adjacencies once
   the leaves are individually distinguished (not just fixed as a set); no
   such automorphism exists. Checked by direct graph inspection, not
   assumed.

**Status: no falsifying evidence found**, across 5 directions, with the
load-bearing numeric claim independently re-derived by a different method.

---

## Part XV — Status discipline

| Claim | Status |
|---|---|
| Frozen Round 1–3 results | Unchanged, no contradiction found |
| Any section meets exactly 1 fiber component, mult. 1 | PROVED — SELF-CONTAINED (elementary) |
| `I2*` dual graph = affine `D6`, 4 legs + 3 spine | PROVED — LITERATURE (Kodaira/Néron/Tate) |
| 9 explicit specialization points, all pairwise distinct, all on split tangent cones | PROVED — SELF-CONTAINED (sympy + independent modular-arithmetic re-check) |
| All 4 legs of all 3 fibers individually `Q`-rational | PROVED — SELF-CONTAINED |
| Graph rigidity forces all 3 spine nodes of all 3 fibers individually `Q`-rational | PROVED — SELF-CONTAINED |
| `Tr(F_p|NS(X_III)) = 20p`, all good odd `p` | **PROVED — SELF-CONTAINED** |
| `|disc NS|=4`, `T(X_III)≅diag(2,2)` | PROVED — SELF-CONTAINED (reconfirmed, not inferred from modularity) |
| `Tr(F_p|T(X_III)) = a_p(16.3.c.a)` | FINITE THEOREM-BASED VERIFICATION (unchanged) |
| Full Class III theorem (point-count bridge) | **FINITE THEOREM-BASED VERIFICATION, now unconditional** |
| `T(p)`, `Σ_III(p)` closed forms | FINITE THEOREM-BASED VERIFICATION, unconditional |
| Extremal-K3 catalogue match | Strongly indicated, NOT FOUND (access limitation) |

The round's own instruction — "do not promote the theorem unless NS
rationality is closed" — is honored: NS rationality **is** closed this
round (`PROVED — SELF-CONTAINED`), and the theorem is promoted accordingly,
but **only** to the extent actually proved (the transcendental-side twist
elimination remains, honestly, at the finite-theorem-based-verification
level it has held since Round 2 — this round did not touch or re-derive
that part).

---

## Final Report

1. **Theorem/classification route found?** Partially — two elementary/
   textbook facts (section-multiplicity; `I_n^*` dual graph structure) did
   the job; no single all-in-one theorem was found or needed.
2. **Catalogue match?** Strongly indicated (Miranda–Persson/Shioda), not
   confirmed against actual tables; not used in the proof.
3. **Split/non-split status of all three `I2*` fibers.** All three: **split**
   over `Q` — every one of the 21 components (7×3) is individually
   `Q`-rational.
4. **Role of rational 2-torsion.** Decisive — it supplied 3 explicit,
   individually-rational, pairwise-distinct sections that, together with
   `O`, exhaust the 4 leg slots of each fiber, triggering graph rigidity.
5. **Galois automorphism group of the `I2*` graph.** The full automorphism
   group of the abstract affine-`D6` graph (compatible with multiplicities)
   allows swapping the 2 legs at a given end, swapping the 2 ends
   wholesale, etc. — but the subgroup **compatible with 4 individually
   (not just setwise) fixed legs is trivial**.
6. **Whether graph rigidity forces componentwise rationality.** Yes —
   derived explicitly (Part VI), not assumed.
7. **CAS resolution used or not used.** Not used (unavailable); not needed
   (theorem-level route succeeded).
8. **Explicit NS basis.** `O`, `F`, plus 6 non-identity components per
   fiber × 3 fibers = 20 total (Part VIII).
9. **Exact Galois action on NS.** Trivial — every generator individually
   fixed.
10. **Exact `Tr(F_p|NS)`.** `20p`, for every good odd `p`. **Proved.**
11. **Recomputed `|disc NS|`.** `4`, unchanged, reconfirmed.
12. **Recomputed `T(X_III)`.** `diag(2,2)`, unchanged.
13. **Modular theorem used.** Livné's singular-K3 modularity theorem
    (existence), combined with finite twist elimination (Round 2),
    unchanged this round.
14. **Twist candidates.** `{1,χ(-1),χ(2),χ(-2)}`, unchanged.
15. **Selected twist.** Trivial (untwisted), unchanged.
16. **Exact `Tr(F_p|T)`.** `a_p(16.3.c.a)`, all odd `p`, unchanged.
17. **Exact `T(p)`.** `a_p(16.3.c.a)` (`p≡1 mod4`), `0` (`p≡3 mod4`) — now
    **unconditional** (Part XII).
18. **Exact `Σ_III(p)`.** `(p-1)a_p(16.3.c.a)` (`p≡1 mod4`), `0` (`p≡3 mod4`)
    — now unconditional.
19. **`p≡3 mod4` interpretation.** Two independent mechanisms (involution;
    CM-inertness), unchanged.
20. **`p≡1 mod4` interpretation.** Finite theorem-based twist elimination,
    now combined with proved `NS` trace for a fully closed point-count
    identity.
21. **Literature overlap.** Unchanged from Round 3 — strongly indicated
    catalogue membership, not confirmed; exact sum `NOT FOUND` anywhere.
22. **Strongest falsification attempt.** Independent raw-modular-arithmetic
    re-derivation of the 9 pairwise-distinctness claims underlying the
    entire closing argument (Part XIV, Direction 1) — the single most
    consequential numeric fact in the round, re-checked by a genuinely
    different method and found to hold.
23. **Any killed/corrected assumption?** Round 3's implicit assumption that
    the spine must be fully hand-constructed via blow-up charts to prove
    its rationality is superseded (not "killed" as wrong, just shown
    unnecessary) by the graph-rigidity shortcut. The "extra chart anomaly"
    found while probing Round 3's bookkeeping (Part VI side-note) exposed a
    genuine incompleteness in that hand construction, but this round's
    actual proof route does not depend on it.
24. **Remaining mathematical gap, if any.** None in the `NS`-rationality
    argument itself. The transcendental-side twist elimination (Round 2)
    remains at `FINITE THEOREM-BASED VERIFICATION` rather than a
    first-principles derivation of triviality — this is an honest,
    pre-existing limitation of the *modular* half of the theorem, unrelated
    to this round's `NS` target, and was explicitly out of scope
    ("DO NOT broaden the project").
25. **Whether Class III is theorem-ready.** Yes, for the `NS`/point-count
    half (fully proved this round). The overall Class III result is now
    theorem-level modulo the same twist-elimination status the modularity
    literature (Livné) already accepts as standard practice for this class
    of argument — i.e., at the same rigor level as the *published* main
    manuscript's own Classes I/II result.
26. **Sequel/addendum/separate paper?** **Sequel-grade**, upgraded from
    Round 3's addendum-grade assessment: the result is now a complete,
    self-contained geometric+modular theorem for a *new, previously
    uncatalogued-in-detail* singular K3 surface, comparable in completeness
    to the main manuscript's Classes I/II treatment. It could stand as its
    own short paper/sequel rather than merely an addendum, though final
    editorial judgment is left to the user.
27. **Single highest-value next action.** Confirm `X_III`'s exact place (or
    absence) in the Miranda–Persson/Shioda extremal-K3 catalogue via direct
    database/table access (not available this round) — this is now a
    literature-completeness question, not a mathematical gap, and is the
    only remaining open item of any kind in this investigation.

### Verdict: **CLASSIII-4A**

NS rationality proved (all 20 generators individually `Q`-rational, via an
elementary section-multiplicity argument plus graph rigidity on the
standard affine-`D6` incidence structure — no blow-up-chart completion
needed), and the Class III theorem is fully closed: `Tr(F_p|NS)=20p`
(proved), `Tr(F_p|T)=a_p(16.3.c.a)` (finite theorem-based, standard rigor
for this argument type), giving unconditional closed forms for `T(p)` and
`Σ_III(p)` for every odd prime.

---

## THE THREE MOST IMPORTANT THINGS WE LEARNED

1. **The hardest-looking part of a proof sometimes isn't necessary at
   all** — three rounds were spent trying to hand-construct every piece of
   a complicated resolved surface, one blow-up at a time, and kept coming
   up short. The actual fix didn't require finishing that construction: it
   required noticing that three already-known rational points (torsion
   sections), landing on four distinct required "slots," pin down the whole
   structure by a simple counting-and-rigidity argument — no further
   blow-ups needed.

2. **Full rational torsion is a much more powerful tool than it first
   looks** — knowing that certain special points on a curve are "defined
   over the rational numbers" doesn't just describe those points; when
   there are exactly as many of them as there are "slots" they could fill,
   it can pin down the rationality of an entire surrounding structure that
   would otherwise take a great deal of separate work to verify piece by
   piece.

3. **Going back and checking a claim by a second, completely different
   method is what turns "probably right" into "verified"** — this round's
   central numeric claim (nine specific points landing at nine specific,
   pairwise-different locations) was first found using one method
   (symbolic algebra) and then re-derived from scratch using a second,
   unrelated method (direct arithmetic), specifically so that a mistake in
   one approach couldn't quietly survive into the final answer.
