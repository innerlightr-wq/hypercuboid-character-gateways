# Class III Round 2 — Literature Audit (Part IX)

Mandatory search log and classification. Searches were run via web search
(no institutional database access); results are necessarily incomplete, and
absence of a hit is reported as `NOT FOUND`, never as evidence of novelty.

## Search 1: the exact sum T(p)

Query: the two-variable sum `T(p) = sum_{x,t in F_p} chi(x t(t+1)(x+t)(x+t+1))`
and equivalent formulations.

No source located stating this exact two-variable sum. The closest structural
relatives are the Ahlgren–Ono–Penniston family sum
`A(lambda,p) = sum_{x,y} chi(xy(x+1)(y+1)(x+lambda y))` (a DIFFERENT five-factor
two-variable sum, already compared and killed in Round 1 for lambda = 8, 1/8)
and Jacobsthal-type sums over products of consecutive residues.

**Classification: NOT FOUND.**

## Search 2: equivalent two-variable character sums / Jacobsthal-type sums

Query: Jacobsthal sums, generalized Jacobsthal sums, and finite-field
hypergeometric-series equivalents of products of consecutive linear factors.

Found: [Generalizations of Jacobsthal sums and hypergeometric series over
finite fields](https://arxiv.org/abs/2102.07086), which expresses generalized
Jacobsthal-type sums (character sums over quadratics/cubics in a single
variable) via Greene's finite-field hypergeometric series. This is the same
general toolbox (character sums over consecutive-residue products) but treats
one-variable sums, not the two-variable `T(p)` here, and does not construct or
analyze a K3 surface.

**Classification: RELATED ONLY.**

## Search 3: the Class III six-factor hypercuboid sum itself

Query: the raw three-variable sum
`Sigma_III(p) = sum_{x0,x1,x2} chi(x0 x1 x2 (x0+x2)(x1+x2)(x0+x1+x2))`.

No source located. This sum, and the "hypercuboid gateway" construction that
produces it (zero-diagonal complement collapse on a 4-coordinate residue
system), appears specific to this project's own prior rounds (Classes I/II,
already published in the manuscript). No external prior use found.

**Classification: NOT FOUND.**

## Search 4: a K3 model with transcendental lattice diag(2,2) / discriminant 4

Query: singular K3 surfaces of discriminant 4, transcendental lattice
`T(X) = diag(2,2)`, CM by `Q(i)`.

Found several relevant structural references:
- [Takatsu, "On the geometry of singular K3 surfaces with discriminant 3, 4
  and 7"](https://arxiv.org/pdf/1903.03054) — constructs and studies singular
  K3 surfaces of discriminant exactly 4 (among others) as double covers of
  P^2, giving explicit geometric models.
- Schütt's general classification framework for singular K3 surfaces over
  number fields (fields of definition, modularity) is the standard reference
  for the discriminant-4 case but the search did not surface a specific
  passage identifying Takatsu's (or any other) discriminant-4 surface with
  `X_III` or with the specific elliptic fibration
  `y^2 = x(x+1)t(t+1)(x+t+1)` used here.

`X_III` here is a *different* geometric model (a rational elliptic-fibration
construction with three `I2*` fibers, arising from a hypercuboid character-sum
reduction) than Takatsu's double-plane model. Both would, if the discriminant-4
identification in this round is correct, share the *same* transcendental
lattice and hence the *same* Frobenius trace formula (both governed by the
unique discriminant-4 CM newform), but they are not shown here to be the same
surface, and no source was found asserting they are.

**Classification: RELATED ONLY** (same discriminant/CM class, not shown to be
the same surface, and no explicit identification found in the literature).

## Search 5: the weight-3 CM eta-quotient `eta^6(4z)` beyond AOP

Query: uses of `eta(4z)^6` (= LMFDB `16.3.c.a`) outside Ahlgren–Ono–Penniston.

Found: [Huber, Liu, McLaughlin, Ye, Yuan, Zhang, "On the vanishing of the
coefficients of CM eta quotients"](https://www.wcupa.edu/sciences-mathematics/mathematics/jMcLaughlin/documents/Huber_Liu_McLaughlin_Ye_Yuan_Zhang_CM_eta_quotients_r2.pdf),
which explicitly treats `eta(4z)^6 = q - 6q^5 + 9q^9 + 10q^{13} - 30q^{17} +
11q^{25} + ...` as a CM newform by `Q(i)` in `S_3(Gamma_0(16), chi_{-1})`, and
records that this form is "associated with the quartic Fermat K3 surface,"
with the coefficient formula `a_p = 2(x^2 - 4y^2)` for `p = x^2 + 4y^2` (p ≡ 1
mod 4). This independently confirms (from a source outside AOP and outside
LMFDB) the form's CM field (`Q(i)`), level (16), weight (3), and nebentypus
(`chi_{-1}`) — exactly matching this round's theoretical derivation in Part
II/III, and gives an **independent literature confirmation of the newform
identity itself**, though for a *different* underlying variety (the quartic
Fermat K3 surface, not `X_III`).

This is a genuinely useful find: it means `16.3.c.a` is already known in the
literature to be a K3-surface Frobenius-trace newform — just for a different
K3 surface than either AOP's `X_8` or this project's `X_III`. Three distinct
varieties (quartic Fermat K3, AOP's `X_8`, and `X_III`) would then all share
the identical Frobenius-trace formula `a_p(16.3.c.a)`, which is unsurprising —
singular K3 surfaces of the same discriminant, and hence the same
transcendental lattice up to isomorphism, are Fourier-coefficient-identical in
their trace formula by definition, however geometrically distinct they are.

**Classification: SAME MODULAR FORM, DIFFERENT SUM/VARIETY.**

## Search 6: Ahlgren–Ono–Penniston direct uses of `eta^6(4z)`

Already established in Round 1 (re-confirmed here): AOP's Theorem 1.2 and the
surrounding text identify their own newform `A(z) = eta^6(4z)` as the modular
form governing `X_8` (their `lambda = 8` singular K3 surface), i.e. AOP
themselves already interpret `A(z)`'s coefficients as a K3 Frobenius trace —
just for `X_8`, not `X_III`. See Part X below for the precise relation.

**Classification: EXACT PRIOR RESULT** (for AOP's own surface `X_8`; not for
`X_III`, which is a different, though closely related, surface — see Round 1's
Part VIII "killed" result that `T(p) != A(8,p)`).

## Search 7: Schütt low-discriminant singular K3 tables (discriminant 4 specifically)

Covered under Search 4; no explicit table entry located this round matching
`X_III`'s specific elliptic fibration equation. Schütt's standard tables are
known (from the main manuscript's own literature review) to include small
discriminants including 4, but a full read of Schütt's complete tables was not
performed this round (would require database/journal access beyond web
search).

**Classification: NOT FOUND** (specific identification of `X_III` in any
published table).

## Search 8: finite-field hypergeometric formulas equivalent to `T(p)`

Covered under Search 2. Greene's finite-field hypergeometric series framework
is the standard tool for this class of sum, but no source was found
expressing `T(p)` itself in that framework.

**Classification: RELATED ONLY.**

## Search 9: Jacobsthal sums with CM by `Q(i)`

Covered under Search 2 / 9. The classical Jacobsthal sum
`phi(a) = sum_x chi(x)chi(x^2+a)` is well known to relate to representations
`p = a^2+b^2` (i.e. CM by `Q(i)`) when `p ≡ 1 mod 4` — this is a one-variable
analogue of the same underlying CM-by-`Q(i)` phenomenon driving `T(p)`'s trace
formula here, but is not the same sum and does not involve a K3 surface.

**Classification: RELATED ONLY.**

---

## Summary table

| # | Search target | Classification |
|---|---|---|
| 1 | exact sum `T(p)` | NOT FOUND |
| 2 | equivalent 2-var character sums | RELATED ONLY |
| 3 | exact `Sigma_III` six-factor sum | NOT FOUND |
| 4 | K3 model with `T=diag(2,2)` | RELATED ONLY |
| 5 | `eta^6(4z)` beyond AOP | SAME MODULAR FORM, DIFFERENT SUM/VARIETY |
| 6 | AOP's own use of `eta^6(4z)` for `X_8` | EXACT PRIOR RESULT (for `X_8`, not `X_III`) |
| 7 | Schütt discriminant-4 tables | NOT FOUND (specific match) |
| 8 | finite-field hypergeometric equivalents | RELATED ONLY |
| 9 | Jacobsthal sums with CM by `Q(i)` | RELATED ONLY |

**Conclusion.** No source was found stating or proving `T(p) = a_p(16.3.c.a)`
for `X_III` specifically. The newform `16.3.c.a` itself is well documented in
the literature (AOP 2002; Huber–Liu–McLaughlin–Ye–Yuan–Zhang) as a K3-surface
CM trace form of discriminant 4, for *other* varieties. `X_III`'s identity as
a *third* discriminant-4 singular K3 surface sharing this same trace formula
is, as far as this search could determine, not previously published — but per
the project's own discipline, **this is reported as NOT FOUND, not claimed as
proven novel**; a full novelty claim would require exhaustive access to
Schütt's tables and related literature beyond what web search can confirm.
