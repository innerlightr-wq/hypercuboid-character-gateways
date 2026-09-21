# Hypercuboid K3 Research Closure: What Is Forced, What Is Not, and Where the Program Stops

## 1. Scope of this closure

This note closes out four adversarial audits run against this repository in September 2026. It
records which mechanisms survived, which proposed implications were refuted, and which
directions are now closed. **It claims no new mathematics.** Every mechanism named below is
standard; the contribution here is accounting, localization, and the removal of two pieces of
loose framing that the audits showed to be unsupported.

Nothing in the manuscripts' theorem or proof content is affected. The audits confirmed the
repository's stated results and non-claims; the corrections below are to *explanatory framing*
generated during the audits themselves, not to the papers.

## 2. Exact results that survive

- The Gateway relation `Sigma_II(p) = chi(-1) Sigma_I(p)` and the Class III vanishing
  `Sigma_III(p) = 0` for `p = 3 mod 4`. **PROVED EXACTLY**, and independently reproduced.
- The n=4 signed transport structure is complete: two components, `{I, II}` joined by a
  `c = -1` edge, and `{III}` carrying a `c = -1` self-action. **PROVED EXACTLY.**
- `disc NS = 8` for Classes I/II and `disc NS = 4` for Class III, with `T(X) = diag(2,4)` and
  `diag(2,2)` respectively. **ESTABLISHED** in the manuscripts; the discriminant accounting was
  independently reproduced. **For Class III this is also PRIOR ART** — the surface is the
  `λ = -1` member of the AOP family and its lattice was already published; see §14.
- The `I_n^*` graph-rigidity proposition (§4 below). **PROVED EXACTLY** for all `n`.

## 3. Signed transport and cancellation

For a group action satisfying `P_i(gx) = c(g,i) P_{g.i}(x)`, the character sums transform by

    Sigma_i = chi(c(g,i)) Sigma_{g.i}.

The scalars satisfy a 1-cocycle law — verified exhaustively at n=4 in the convention
`c(g∘h, A) = c(h,A) c(g, h.A)` (4032 cases, 0 violations; the other three pairings each fail in
1536 cases) — and restricted to a stabilizer the map `g -> c(g,i)` is a genuine one-dimensional
character. If that character is nontrivial, `Sigma_i = 0`.

So: an **edge** between distinct classes is a transport relation; a **nontrivial signed
self-action** is an internal cancellation constraint. Class III's vanishing is the second kind;
the Gateway relation is the first.

**Status: ESTABLISHED THEORY, project-specific application.** The underlying statement is that
the vector of character sums is an invariant of a monomial representation, and invariants of a
monomial representation are supported on orbits with trivial stabilizer character. This is
textbook and **must not be presented as a new theorem**. Its value here is explanatory: it
replaces an ad hoc "sign-reversing involution" with the standard principle, and it explains why
the *same-looking* `chi(-1)` behaves differently in the two cases.

At **n=5**: 15 classes, two ordinary orbits, and **every class has trivial signed stabilizer**.
The mechanism therefore predicts no forced vanishing — and independent exact computation of all
15 sums over 13 good primes (5..47) found none. (p=3 is excluded for cause: mod 3 every nonzero
point lies on at least three of the 15 hyperplanes, so all 14-fold products vanish identically —
arrangement degeneration, not a character phenomenon.) **COMPUTATIONALLY VERIFIED.** The
prediction was confirmed, which is what a falsification test is for.

## 4. Graph-rigidity boundary

The correct proposition is:

> For a Kodaira fiber of type `I_n^*`, if all four multiplicity-one outer components are
> individually Galois-fixed, then every component is Galois-fixed.

*Proof:* each leg is a leaf with a unique neighbour, so fixing the legs fixes both spine ends;
the spine is a path, and an automorphism fixing both endpoints of a path fixes it pointwise (for
`I_0^*` the centre is the only remaining vertex). **PROVED EXACTLY**, verified for `n = 0..4`;
the manuscript's `I_2^*` case (|Aut| = 8, marked stabilizer trivial) is reproduced exactly.

**Do not replace this by "full rational 2-torsion rigidifies reducible fibers."** That is
**REFUTED**: sections mark only the image of the torsion in the component group `Phi`, and
`(Z/2)^2` cannot inject into a cyclic `Phi`. Controls: `I_4` (`Phi = Z/4`) and `I_6`
(`Phi = Z/6`) with only `Z/2` rational torsion retain a stabilizer of order 2 — the reflection
fixing the two marked components and swapping the rest.

The correct chain is: rational torsion -> images in component groups -> which outer components
are individually fixed -> graph rigidity. Treat the proposition as useful packaging of
standard-looking material; prior art was not checked (see §13).

## 5. Observable versus arithmetic-forcing divergence

These are different events and the audits separated them.

**First observable divergence:** the `S_4` orbit type (singleton-type versus 2+2-split type).
Purely combinatorial, visible immediately, and carrying **no proved implication** to the
downstream arithmetic.

**First arithmetic-forcing datum:** the reducible-fiber package of a chosen elliptic fibration —
roughly five layers later. Everything in between (incidence structure, arrangement polynomial,
projective class, singularity configuration) is observable but not proved-forcing.

The forcing layer is itself branch-dependent: Class III is extremal (MW rank 0), so its fiber
configuration alone gives `rho = 20` and `disc NS = 4`; Classes I/II have MW rank 1, so the
Shioda height computation `h(P_1) = 1` is logically required even though its value is 1.

## 6. Discriminant accounting and its fibration dependence

For a chosen fibration, `|disc NS| = |disc Triv| * det(MW) / |MW_tors|^2`:

| | Classes I/II | Class III |
|---|---|---|
| root lattice `R` | `D_6 + A_1 + D_4 + D_6` | `D_6 + D_6 + D_6` |
| `\|disc R\|` | `4*2*4*4 = 128` | `4*4*4 = 64` |
| `det(MW)` | 1 (rank 1, height 1) | 1 (rank 0) |
| `/ \|MW_tors\|^2` | 16 | 16 |
| `\|disc NS\|` | **8** | **4** |

**Correction, and it matters.** An earlier framing said the 8-versus-4 distinction "is" one
factor of 2 in `|disc R|`. That is **fibration-dependent bookkeeping, not an intrinsic
statement**. A singular K3 admits many elliptic fibrations; Shioda–Tate holds for each, so
different fibrations carry compensating `(R, MW)` data while `|disc NS|` stays fixed. The
intrinsic content is simply `|disc NS| = 8` versus `4`; the root/MW accounting is one certificate
for it, not its cause.

**Do not write "hypercuboid combinatorics causes a factor of 2."** That is unsupported.

## 7. Torsion: rigidity role versus non-discriminating role

Rational 2-torsion is essential to the component-marking / Galois-rigidity argument of §4. But
it **does not distinguish the two arithmetic sectors**: `|MW_tors|^2 = 16` in *both* branches,
and `det(MW) = 1` in both. The entire branch distinction sits in `|disc R|`.

> An object can be essential to one mechanism and irrelevant to another. Torsion is load-bearing
> for rigidity and inert for discrimination.

## 8. The decisive AOP lambda-family control

This repository identifies its Class I/II sum with Ahlgren–Ono–Penniston's `A(lambda, q)` **at
lambda = 1**, a member of a one-parameter family of K3 surfaces, and cites their Theorem 1.2 for
the singular/CM structure at that parameter.

The underlying arrangement `{x, y, x+1, y+1, x + lambda*y}` keeps the **same incidence
combinatorics, matroid and singularity pattern** for generic `lambda`. This is now proved rather
than asserted: an exact symbolic incidence audit gives **3 triple + 6 double points** for generic
`lambda` and identically for `lambda = 1, 2, 3, 5, 1/2, -2`, with **exactly three exceptional
values** — `lambda = 0` and `lambda = ∞` (two branch lines coincide) and `lambda = -1`
(**4 triple + 3 double**). Independently confirmed by van Geemen–Top, whose parameter
restriction is precisely `t ≠ 0, -1` and who write that "in the special case `t = -1` there are
3 double points and 4 triple points".

The arithmetic does not follow suit: at `lambda = 1` the sum satisfies `A(1,p) = -chi(2)p`
exactly at every prime inert in `Q(sqrt-2)` (checked at p = 13, 23, 29, 31, 37 — the CM
signature), while `lambda = 2, 3, 5` show no such pattern, and generic members are not singular
at all, hence carry no CM field.

Two refinements the audit added. First, the two repository branches are **not** in the same
incidence stratum as each other — Classes I/II sit at `lambda = 1` (3+6), Class III at
`lambda = -1` (4+3) — so the control has to come from the family, not from comparing the two
branches, which is what §8 already does. Second, the refutation is **stratum-dependent**: the
`3+6` stratum carries a modulus, which is what lets the arithmetic vary across it, whereas the
`4+3` stratum is the complete quadrilateral and is projectively rigid. The general statement is
therefore *incidence type alone is insufficient in general, because some strata carry moduli* —
not that it is never sufficient.

**Status: ESTABLISHED THEORY** (the family and its properties are AOP's, already cited here);
the numerical check is **COMPUTATIONALLY VERIFIED**.

Stated carefully: **bare combinatorial incidence data do not determine the arithmetic sector in
this family.** This is *not* the claim that no combinatorics-to-arithmetic relationship is
possible. An enriched upstream invariant — carrying realization/moduli parameters, cross-ratios,
field-of-definition data or other arithmetic decoration — could still carry arithmetic
information. That is a different question, and it is not pursued here.

## 9. Refuted implication chain

| hypothesis | status | reason |
|---|---|---|
| orbit type -> arithmetic sector | **REFUTED** as a bare forcing law | a fortiori from the next row |
| incidence combinatorics -> arithmetic sector | **REFUTED** | AOP family: fixed combinatorics, varying arithmetic |
| singularity combinatorics -> arithmetic sector | **REFUTED** as a sufficient forcing datum | singularities are also constant in `lambda` on the same open set |
| visible resolution lattice -> `disc NS` | **REFUTED** as a general forcing claim | same control |
| root lattice + MW torsion -> `disc NS` | **NOT GENERAL** | holds here only because `det(MW) = 1`; free MW heights can be required |
| chosen-fibration root + MW package -> `disc NS` | **ESTABLISHED THEORY** | Shioda–Tate, per chosen fibration |
| `rho = 20` + NS data -> `\|disc T\|` | **ESTABLISHED THEORY** | orthogonal complement in the unimodular K3 lattice |
| `disc T` -> full `T` | **SPECIAL TO THESE CASES** | `h(-4) = h(-8) = 1`; false in general |
| `T(X)` -> CM field/order | **ESTABLISHED THEORY** | singular-K3 theory, with the usual order/conductor qualifications |
| same modular form -> same surface | **FALSE** | both branches share modular forms with AOP's family |

The pipeline is intact downstream and broken upstream.

## 10. The n=4 K3 / n>=5 general-type boundary

Degree and canonical-class audit of the natural construction (product of all-but-one of the
`2^{n-1}-1` complement-class forms, as a double cover):

| n | forms in product | ambient | `2k` | `K = (k-(d+1))H` | type |
|---|---|---|---|---|---|
| 4 | 6 | `P^2` | `k=3` | **0** | **K3** |
| 5 | 14 | `P^3` | `k=7` | `3H` | general type |
| 6 | 30 | `P^4` | `k=15` | `10H` | general type |

**The n=4 K3 program does not mechanically continue to n >= 5.** Forcing a K3 out of the n=5
threefold by slicing would be a category error. This does **not** mean the broader hypercuboid
character-sum program is finished for all `n` — only that any `n >= 5` continuation belongs to a
different geometric category and should not be described as a continuation of the singular-K3
classification without new ideas.

## 11. Closed directions

| direction | reason |
|---|---|
| **A.** Universal orbit-type -> CM-field law | refuted as a bare-combinatorics forcing claim (§8) |
| **B.** Universal incidence-lattice -> arithmetic-sector law | same incidence data vary arithmetically in the family |
| **C.** Higher-`n` signed-self-loop search as a research program | mechanism is standard stabilizer-character cancellation; n=5 supplied the control and no new mechanism |
| **D.** Mechanical extension of the n=4 K3 construction to n=5 | dimension / canonical-class category changes (§10) |
| **E.** Treating rational 2-torsion as the arithmetic branch discriminator | torsion correction identical in both branches (§7) |
| **F.** Treating the factor-of-2 root discriminant difference as an intrinsic combinatorial cause | root lattice is fibration-dependent; the intrinsic distinction is `disc NS` (§6) |

## 12. Legitimate future directions

Listed as possibilities only. **No conjectures are offered.**

1. **Realization/moduli arithmetic.** Fixed combinatorial type plus a varying realization
   parameter yields varying arithmetic geometry. The AOP `lambda`-family shows this is real and
   is the natural setting for any enriched upstream invariant. **OPEN.**
2. **Higher-`n` character-sum varieties.** `n >= 5` produces higher-dimensional general-type
   objects. A different program, not an extension of the K3 classification. **OPEN.**
3. **Picard-rank jumps / CM specializations.** Which parameter values in such a family produce
   singular members is a question of independent standing. **OPEN.**
4. **Arithmetic variation within the AOP family or relatives.** **OPEN.**

## 13. Rules for future agents

- Distinguish **observable divergence**, **arithmetic forcing**, and **downstream information
  loss**. They occur at different layers and the audits separated them by several.
- A root lattice belongs to a **chosen fibration**; `disc NS` is the surface invariant. Do not
  attribute intrinsic content to fibration-dependent bookkeeping.
- `disc T` determines `T` here **only** by class number one at `-4` and `-8`. Do not generalize.
- Same modular form does not recover the surface; same transcendental representation does not
  recover `NS`, the fibration or the Mordell–Weil group.
- Two data points do not establish a law — and the manuscripts already say so, in
  §`sec:comparison` of the Class III paper and in the README. Those statements are correct and
  should not be weakened.
- **Prior art has now been checked for §3, §4 and §6** — see §14 below. All three resolve as
  established theory or standard corollary. Nothing in this note is new, and that is now a
  checked statement rather than an assumption.

## 14. Prior-art status — resolved

A dedicated prior-art audit (September 2026; Zotero collection *Hypercuboid K3 — Prior Art
Audit*, key `CZMKB6UW`, 31 items) closed the three questions §13 previously left open. **None of
the three is novel, and none was ever claimed to be.**

| | claim | status | sources |
|---|---|---|---|
| **P1** | stabilizer-character cancellation / monomial representation (§3) | **ESTABLISHED THEORY / PROJECT-SPECIFIC APPLICATION** | Frobenius reciprocity: `Hom_G(1, Ind_H^G psi) = Hom_H(1, psi)`, so a nontrivial stabilizer character admits no invariant vector. Serre, *Linear Representations of Finite Groups*, GTM 42, Ch. 7; Isaacs, *Character Theory of Finite Groups*, Ch. 5 |
| **P2** | `I_n^*` four-fixed-legs rigidity (§4) | **STANDARD COROLLARY** | Wazir, *Arithmetic on elliptic threefolds*, Compositio Math. **140** (2004), 567–580: an `I_n^*` fiber has `n+5` or `n+3` rational components, by the splitting of a quadratic. Ulmer, PCMI **18** (2011), Lecture 3 §6, same dichotomy in split/non-split form. Ingredients: Bosch–Liu, manuscripta math. **98** (1999), §1 p. 277; Fuchs–Schellekens–Schweigert, CMP **180** (1996), §2.5 |
| **P3** | `disc NS = disc Triv · det(MW) / \|MW_tors\|²` (§6) | **ESTABLISHED THEORY / PROJECT-SPECIFIC APPLICATION** | Shioda, Comment. Math. Univ. St. Pauli **39** (1990), 211–240; modern statement in Schütt–Shioda, *Elliptic surfaces*, §11, which carries an additional `(-1)^{rank E(K)}` the absolute-value form here suppresses |

Two caveats attach to P2 and must travel with it: `I_0^*` needs separate treatment, since its
dual graph is `D̃_4` with automorphism group `S_4` rather than the order-8 group, so the
split/non-split dichotomy does not exhaust its monodromy; and the statement presumes a **perfect
residue field**. Both hold throughout this project. The refuted broader claim — that full
rational 2-torsion rigidifies every reducible fiber — is not merely unsupported: Schütt–Shioda's
Cor. 7.5 (`E(K)_tors` injects into `∏_v Φ_v`) supplies the obstruction, since `(Z/2)²` cannot
embed in a cyclic `Φ`. The `I_4` and `I_6` controls of §4 are what that theorem predicts.

### The Class III surface is a known one

The audit's substantive finding was not on the P1–P3 list.

> **The Class III surface is the `λ = -1` member of the Ahlgren–Ono–Penniston family.**

Two independent verifications, both in `class_iii/scripts/class3_aop_identification.py`:
`T(p) = A(-1, p)` at every odd prime tested, for AOP's two-variable sum `A(λ,p)`; and the
`Q`-linear substitution `(x,t,w) -> (x, t-x, -t-w)` carries the Class III branch sextic *exactly*
onto the `λ = -1` branch sextic, with no residual scalar — so the surfaces are isomorphic
**over `Q`**, not merely up to twist.

Consequently the arithmetic package `T(X) = diag(2,2)`, `|disc NS| = 4`, CM by `Q(i)` is
**already in the literature**: van Geemen–Top, Bull. LMS **38** (2006), 209–223, record the
lattice and discriminant for that member, citing Persson, LNM **1124** (1985), p. 298, and note
that Shioda–Inose exhibit it as the desingularised quotient of `E_i × E_i`, `E_i = C/Z[i]`.
Vinberg, Math. Ann. **265** (1983), shows the K3 carrying that lattice is unique.

**Label: KNOWN PRIOR ART / INDEPENDENT HYPERCUBOID RE-DERIVATION.** The Class III manuscript has
been revised accordingly (abstract, `Relation to Ahlgren–Ono–Penniston`, `sec:AOP-precise`,
`rem:known-vs-proved`, Discussion). Its own results — the reduction to `T(p)`, the elementary
vanishing proof, the `NS`-rationality argument, the exact evaluation — are untouched.

One point runs the other way and is recorded for fairness: `λ = -1` is precisely where AOP's own
closed-form evaluation degenerates (it carries a factor `χ(λ+1)` and an inverse of `λ+1`), and
van Geemen–Top exclude `t = -1` from their isogeny theorem. So the *evaluation* obtained here is
not a specialization of AOP's. What is prior art is the surface and its lattice/CM data.

### Labels

| item | label |
|---|---|
| P1 stabilizer cancellation | ESTABLISHED THEORY / PROJECT-SPECIFIC APPLICATION |
| P2 `I_n^*` four-fixed-legs rigidity | STANDARD COROLLARY |
| P3 `NS` discriminant formula | ESTABLISHED THEORY / PROJECT-SPECIFIC APPLICATION |
| Class III disc-4 / `Q(i)` arithmetic | KNOWN PRIOR ART / INDEPENDENT HYPERCUBOID RE-DERIVATION |
| AOP incidence-family control | ESTABLISHED CONTROL / SUPPORTS NONCLAIM |
| orbit / incidence → CM forcing | REFUTED AS A BARE-COMBINATORICS LAW |
| higher-`n` K3 continuation | CLOSED FOR THE DIRECT CONSTRUCTION |
| realization / moduli arithmetic | OPEN AS A SEPARATE FUTURE PROGRAM |

## Closing statement

The n=4 hypercuboid K3 classification is internally coherent and its arithmetic mechanisms are
now well localized. Bare combinatorial orbit or incidence data do not determine the downstream
transcendental/CM sector; the arithmetic distinction is carried by geometric realization and
lattice data not encoded by incidence combinatorics alone. The natural n=5 construction leaves
the K3 category. Accordingly, the current combinatorics-to-CM and higher-`n` K3 directions are
closed. Any future work should begin as a new program centred either on arithmetic variation in
realization/moduli parameters or on the higher-dimensional varieties arising for `n >= 5`.
