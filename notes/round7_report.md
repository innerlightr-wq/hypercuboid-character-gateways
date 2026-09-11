# Hypercuboid exploration — Round 7 working notes

## Part II — isomorphism classes among the 7 residual cores (verified)

All 7 cases are exactly "all 7 forms minus one excluded form" (verified
directly: (0,1,2,3,4,5) excludes idx6; (0,1,2,3,4,6) excludes idx5;
(0,1,2,3,5,6) excludes idx4; (0,1,2,4,5,6) excludes idx3;
(0,1,3,4,5,6) excludes idx2; (0,2,3,4,5,6) excludes idx1;
(1,2,3,4,5,6) excludes idx0). The coordinate-permutation group S_3 acts on
the 7 forms with three orbits: {idx6} (the full triple, fixed), {idx0,1,2}
(singletons), {idx3,4,5} (pairs). This gives exactly **THREE isomorphism
classes**, not seven independent cases:

- **Class I** (1 case): exclude the full triple — S=(0,1,2,3,4,5).
- **Class II** (3 cases, one orbit): exclude a singleton — e.g. (1,2,3,4,5,6).
- **Class III** (3 cases, one orbit): exclude a pair — e.g. (0,1,2,4,5,6).

Resolving one representative per class resolves the whole orbit by the
proved coordinate-permutation invariance (Round 6, Part I).

## Part IV/V — candidate-Q screening (symbolic, `aggregate_screen.py`)

Screened structurally-motivated $\lambda$ (coordinate sum, all six
pairwise differences and their negatives, one non-primitive control) on
all three classes. Key findings:

- **Class I**: no candidate produces a private coordinate, a mult-2
  coordinate, or a pure-$q$ form. Best case (coordinate sum) still leaves
  fiber multiplicities $[4,4]$ on only 2 fiber variables — 6 forms
  distributed over 2 variables cannot avoid heavy overlap. **No promising
  Q found.**
- **Class II**: $Q=x_0+x_1+x_2$ makes the full-triple form collapse to
  **exactly $q$** (pure function of $Q$, killing the $Q=0$ fiber via
  $\chi(0)=0$, same mechanism as Round 6's successful n=5 example) — a
  genuine, real reduction. BUT the remaining 5-form fiber still has
  multiplicity $[3,3]$ (no coordinate becomes free or mult-2); one
  coordinate is shared by 3 forms whose roots are generically distinct
  (a genuine cubic/elliptic-type sub-problem), so full closure was **not**
  reached this round.
- **Class III**: same $Q=$ coordinate-sum choice again collapses the
  full-triple form to pure-$q$; residual fiber multiplicity $[4,3]$ —
  similarly not fully peelable.

**No candidate transformation fully exposes A/B/C/E for any of the three
classes.** This is a genuine, actively-searched negative result for the
specific linear-$Q$ mechanism as currently understood, not an
under-explored gap.

## New structural facts found (COMPUTATIONALLY VERIFIED, mechanism not derived)

1. **Class III vanishes exactly at every tested $p\equiv3\pmod4$** (8/8:
   $p=3,7,11,19,23,31,43,47$ all give exactly 0) **and is nonzero at every
   tested $p\equiv1\pmod4$** (8/8: $p=5,13,17,29,37,41,53,61$, none
   proportional to $p(p-1)$ by a simple constant). A clean, exact,
   verified dichotomy — but not a closed-form evaluation.
2. **Class II $=\chi(-1)\times$ Class I, exactly, at all 16 tested
   primes** (sign or exact equality tracks $p\bmod4$ perfectly: equal at
   every $p\equiv1\pmod4$, negated at every $p\equiv3\pmod4$, including the
   non-obvious equal-and-negative case at $p=41$). A genuine cross-class
   exact relation, found by direct data comparison — the algebraic reason
   (some natural sign-flip or complementation map between "exclude the
   full form" and "exclude a singleton") was not derived this round.

Both facts are reported as exact, verified, and mathematically real — but
as *relations among the unknowns*, not evaluations of them. They do not
by themselves constitute Gateway-F closures.

## Part VI — per-class status

- **Class I: F-FAILED.** No natural aggregate exposes A/B/C/E on the fiber.
- **Class II: F-REDUCED.** $Q$-conditioning genuinely simplifies the
  problem (removes one form entirely via the pure-$q$/private-$Q$ effect,
  reducing to a 5-form, 2-variable residual) but the residual is not yet
  in a solved class — it is a smaller, but still not fully elementary,
  object (a shared-coordinate triple with generically distinct roots).
- **Class III: F-REDUCED**, same mechanism as Class II, plus the
  additional exact (but unexplained) $p\bmod4$ vanishing dichotomy.

**None reached F-RESOLVED this round.**

## Part VII — criterion for a promising Q (partial, not general)

The one clear, reproducible signal found: **$Q$ collapses a form to a pure
function of $Q$ exactly when that form's coefficient vector equals the
all-ones vector** (i.e. the full-triple form, whose coefficients are
literally $(1,1,1)=\lambda$ for $\lambda=(1,1,1)$) — an entirely
elementary fact (a form equals $Q$ exactly iff its coefficient vector *is*
$\lambda$), not a deep criterion. Beyond this single elementary
observation, **no criterion tested predicted which further coordinate
would become free or mult-2** — every attempted $\lambda$ left the
residual fiber at multiplicity 3 for Classes II/III. This is reported
honestly as **a narrow, elementary sufficient condition for one specific
form-collapse effect, not a general predictive criterion for Gateway-F
success.**

## Part VIII — contraction language

Considered; not adopted beyond Round 6's assessment. The one new fact
(coefficient-vector-equals-$\lambda$ collapse) is exactly elementary
linear algebra (evaluating one linear form at the chosen functional) and
gains nothing from matroid/contraction phrasing.

## Part IX — exceptional primes

Not reached — no candidate $Q$ produced a resolvable fiber for any of the
three classes, so there was no derived formula whose exceptional-prime set
could be predicted this round. The Class III $p\bmod4$ dichotomy is a
genuine "exceptional prime"-flavored fact but was found empirically, not
derived from a determinant/coefficient condition.

## Part X — negative-result statement

The three residual classes genuinely resist the linear-$Q$-conditioning
version of Gateway F as currently formulated: even the best-case
reductions (Classes II/III) bottom out in a coordinate shared by exactly
3 forms with generically-distinct roots on the fiber — structurally the
SAME kind of object Round 3 identified as genuinely elliptic-curve-typed
in general, not the special nested-coincidence structure that made
Round 5/6's successes work. The minimal shared "F-resistant" invariant
across all three: **after removing the one collapsible full-triple form
(where present), every remaining coordinate is still shared by exactly 3
forms, and no natural linear recombination lowers this** (verified by
explicit search over the motivated candidate list, not merely assumed).
