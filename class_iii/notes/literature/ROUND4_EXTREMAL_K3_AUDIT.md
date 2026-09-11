# Class III Round 4 — Extremal K3 Classification / Component-Rationality Literature Audit

Searched (web search only, no institutional database access) for a
theorem-level route to split-`I2*` certification, per Round 4 Part II.

## Search 1: split I2*/component-group-via-torsion theory

No single citable theorem was found stating exactly "full rational
2-torsion forces all fiber components of a reducible additive fiber to be
individually rational." What **was** found, and is standard/foundational
enough to use directly without further citation-hunting, are the two
elementary facts this round's closing argument is built from:

- **Any section of a relatively minimal elliptic fibration meets exactly one
  irreducible component of any fiber, and that component necessarily has
  multiplicity 1** — this is a direct consequence of the intersection number
  `section · fiber = 1` combined with `fiber = sum m_i C_i`, and is standard
  (e.g. implicit throughout Miranda's "Basic Theory of Elliptic Surfaces,"
  and used without further citation in the main manuscript already).
- **The dual graph of a Kodaira `I_n^*` fiber is the extended (affine)
  Dynkin diagram of type `D_{n+4}`**, with `n+5` total components: 4 of
  multiplicity 1 ("legs," two pairs, one pair per end) and `n+1` of
  multiplicity 2 ("spine," a path); for `n=2` (`I2*`): 4 legs + 3 spine = 7
  (Kodaira 1963; Néron 1964; Tate 1975 — textbook, e.g. Silverman's
  *Advanced Topics in the Arithmetic of Elliptic Curves*, Ch. IV).

**Classification: no single named theorem found that directly does the
"torsion ⟹ split" step in one citation** — but the two facts above, combined
with elementary graph rigidity (this round's own short argument, Part VI),
suffice to reconstruct the needed result from first principles without
requiring a black-box theorem.

## Search 2: extremal elliptic K3 classification tables (`3×I2*`, torsion `(Z/2)^2`)

As in Round 3: Miranda–Persson's complete determination of the 112 possible
extremal fiber configurations, and Shioda's complete list of all 325
extremal elliptic K3 surfaces (with transcendental lattice, fiber type, and
Mordell–Weil data per surface), almost certainly contain `X_III`'s
configuration. This round's web search again could not access the specific
table entries. **NOT FOUND** (specific confirmation), **SAME FIBER
CONFIGURATION** (strongly indicated, not confirmed).

## Search 3: AOP `λ=8` model fiber structure

AOP's own `X_8` (governed by the same untwisted `16.3.c.a` newform, Round 2
Part X) has a *different* Weierstrass model and fiber arrangement from
`X_III` (Round 1 killed `T(p)=A(8,p)` directly). No claim of birational
equivalence is made; this is a **RELATED ONLY** classification, unchanged
from Rounds 2–3.

**No novelty claim is made from any NOT FOUND result above.**
