# Novelty and provenance audit

**Date:** 2026-09-18 · **State audited:** `b94beb5` (= `origin/main`), no tags in the repository
· **Bibliography added:** [`references.bib`](../references.bib), 20 entries

A finite-field, character-sum and theorem-ancestry audit. It does not touch the manuscripts, the
scripts, or any computed value.

## 0. First, a correction to the audit brief itself

The brief asked about a result stated as

> `N_0^clean(p,5) = 2^(-15) p^4 + O(p^(7/2))`

**No such statement exists in this repository.** The strings `2^{-15}`, `32768` and `p^{7/2}` appear
nowhere in any file. What exists is:

* `scripts/core.py` — a general-`n` implementation whose docstring names the quantity
  `N_0^clean(p,n)` and defines it exactly (see §2);
* `scripts/baseline_verification.py` — which reproduces, and attributes to a paper, a
  **"Theorem 6.1: `N_0^clean(p,5) = 0` for `p ≡ 3 (mod 4)`; nonzero (eventually) for `p ≡ 1 (mod 4)`"**
  and a "Proposition 6.2 / Appendix C.5" on odd-cardinality vanishing;
* the two manuscripts actually present, which are about **`n = 4`** and evaluate three character sums
  `Σ_I, Σ_II, Σ_III` via singular K3 surfaces.

So the brief's numbers are structurally right but attached to a document that is not here. **The
paper containing "Theorem 6.1", "Proposition 6.2", "Appendix C.5" and "Section 9" is not in this
repository**, and `scripts/baseline_verification.py` cites it as "the paper's own theorem-level
results". That is a genuine provenance gap and it is the one documentation defect this audit found
(§9).

This audit therefore does two things: it answers the brief's five questions about the construction as
implemented (which *is* here, in full generality), and it audits the claims the repository actually
makes.

## 1. Claim inventory

| # | Claim | Where | Class |
|---|---|---|---|
| C1 | Zero sector: `A_n = −(A_1+…+A_{n−1})` eliminates the `D_full = 0` constraint | `core.py`; manuscript §2 | definition |
| C2 | The representative forms are `L_J(x) = Σ_{j∈J} x_j`, nonempty `J ⊆ [n−1]`: `2^(n−1) − 1` of them | `core.py`; manuscript §2 | symmetry reduction |
| C3 | `Σ_S(p) = 0` for every odd-cardinality `S` | Prop 6.2 (absent paper); reproduced in `baseline_verification.py` | quadratic-character identity |
| C4 | `Σ_I(p) = (p−1) S(p)` | manuscript Lemma 3.1 | elementary finite-field fact |
| C5 | `#V(F_p) = p² + S(p)` | manuscript Lemma 3.2 | elementary finite-field fact |
| C6 | `X` is a K3 with `ρ = 20`, `disc NS = 8`, `T(X) ≅ diag(2,4)` | manuscript Prop 6.x | computational + geometric result |
| C7 | `Tr(F_p | NS(X)) = (19 + χ(−1))p` | manuscript Prop 7.1 | geometric result |
| C8 | `Tr_T(p) = χ(−1) a_p(f)`, `f = 8.3.d.a` | manuscript Prop 7.2 | asymptotic/modularity theorem (cited: Livné) |
| C9 | The character-sum identity for `S(p)` | manuscript Thm 8.1 | **explicitly attributed to `AOP2002`** |
| C10 | **Gateway relation** `Σ_II(p) = χ(−1) Σ_I(p)` | manuscript Prop 9.2 | claimed novelty |
| C11 | `Σ_III(p) = 0` for `p ≡ 3 mod 4` | manuscript Prop 10.1 | symmetry reduction |
| C12 | Class III for `p ≡ 1 mod 4` resolved by a second K3 (disc 4, CM by `Q(i)`) | `class_iii/` | geometric result |
| C13 | The independent K3-geometric derivation of C9 | manuscript §8–9 | new derivation of known ingredients |
| C14 | `N_0^clean(p,5) = 0` for `p ≡ 3 mod 4`, eventually nonzero for `p ≡ 1 mod 4` | absent paper's Thm 6.1 | counting/existence claim |

The repository makes **no** claim of the form "`2^-15 p^4 + O(p^{7/2})`", and makes **no** novelty
claim for C9 — which it credits to Ahlgren–Ono–Penniston prominently, in the README and in the
manuscript's own section heading.

## 2. The construction in standard language

From `scripts/core.py`, exactly:

* field `F_p`, `p` odd — **`p = 2` is excluded from the outset**, and correctly so: the whole
  construction is built on the quadratic character, which is trivial in characteristic 2 (every
  element is a square). `notes/NOTATION.md` states this globally. The condition `p ≡ 1 mod 4` never
  silently covers `p = 2`.
* ambient `F_p^d` with `d = n − 1`, coordinates `x = (x_1,…,x_{n−1})`;
* `A_i = x_i` for `i < n` and `A_n = −(x_1+…+x_{n−1})`, so `Σ_i A_i = 0` — the "zero sector";
* for `S ⊆ [n]` nonempty proper, the diagonal sum `D_S = Σ_{i∈S} A_i`;
* `χ = ` the Legendre symbol, with the convention `χ(0) = 0` (`legendre_table` sets `table[0] = 0`);
* the `2^(n−1) − 1` representative forms `L_J(x) = Σ_{j∈J} x_j`, nonempty `J ⊆ [n−1]`;
* `N_0^clean(p,n) = #{ x ∈ F_p^{n−1} : χ(L_J(x)) = +1 for every nonempty J ⊆ [n−1], and A_1,…,A_n
  pairwise distinct }`;
* `Σ_S(p) = Σ_{x ∈ F_p^d} χ( Π_{J∈S} L_J(x) )` for a set `S` of forms.

"Gateway" is this project's word for a point of the clean set — a simultaneous prescription of
quadratic characters. "Clean" means: no form vanishes (all characters are `+1`, hence nonzero) **and**
the `n` coordinates are pairwise distinct. In standard language the clean set is the set of
`F_p`-points of the complement of an explicit hyperplane arrangement on which fifteen prescribed
quadratic characters all take the value `+1`.

## 3. `p ≡ 1 mod 4` is exactly `χ(−1) = 1` — classical

In the zero sector `Σ_i A_i = 0`, so for every `S`

```
D_{S^c} = −D_S     hence     χ(D_{S^c}) = χ(−1) · χ(D_S).
```

A condition family closed under complement can therefore demand one common sign for all of its
members **iff `χ(−1) = +1`**, i.e. iff `p ≡ 1 mod 4`, by Euler's criterion
`χ(−1) = (−1)^((p−1)/2)`.

That is the entire content of the mod-4 obstruction. **Classification: `CLASSICAL` /
`ELEMENTARY SYMMETRY CONSEQUENCE`.** The same obstruction, from the same `χ(−1)` computation, is what
forces `p ≡ 1 mod 4` for Paley *graphs* to be undirected (`Paley1933`) and governs the
conference-matrix and quadratic-residue-difference-set constructions. It is not specific to this
project and should not be presented as a project-specific discovery. To the repository's credit, it
is not: the manuscript derives everything through `χ(−1)` explicitly and never calls the mod-4
dichotomy new.

## 4. Where `2^n − 2` comes from, and the collapse to `2^(n−1) − 1`

**`2^n − 2` = the number of nonempty proper subsets `S ⊊ [n]`**, i.e. the nontrivial diagonal sums
`D_S`. (Equivalently: nonconstant `{0,1}`-vectors of length `n`; equivalently the nonzero, non-all-ones
elements of `F_2^n`.) Verified for `n = 2,…,6`.

**The collapse is exactly the quotient by `S ↔ S^c`.** The involution is fixed-point-free: `S = S^c`
would force `S = S ∩ S^c = ∅`, which is excluded. Hence the orbits all have size 2 and

```
(2^n − 2)/2 = 2^(n−1) − 1 .
```

Verified: `n=4` gives `14 → 7`, `n=5` gives `30 → 15`, `n=6` gives `62 → 31`.

**And the quotient is a standard object.** The conditions are indexed by `F_2^n` minus `{0, 1}`,
modulo the all-ones vector, i.e. by the nonzero elements of

```
F_2^n / ⟨(1,1,…,1)⟩ ,     of dimension n − 1 ,
```

which has `2^(n−1) − 1` nonzero elements. Over `F_2` the only nonzero scalar is `1`, so nonzero
vectors and projective points coincide and there is **no further quotient**: the index set is the
point set of `PG(n−2,2)`.

* `n = 5`: `15` classes = the **15 points of `PG(3,2)`**.
* `n = 4`: `7` classes = the **7 points of `PG(2,2)`, the Fano plane**.

Verified computationally, including that the repository's own representative set — `L_J` for nonempty
`J ⊆ [n−1]` — is exactly the set of coset representatives whose `n`-th coordinate is `0`, and that
`J ↦ {J, [n]\J}` is a **bijection** onto the complement-pairs.

**Answer to the brief's question 3 and 4: yes, the collapse is nothing more than identifying each
sign pattern with its complement, and the resulting 15-element index set is a classical finite
geometry.** Classification: `ELEMENTARY SYMMETRY CONSEQUENCE`, with the standard formulation being
`F_2^n/⟨1⟩` and `PG(n−2,2)` (`Hirschfeld1998`). The coding-theoretic reading is the same object: the
`2^(n−1) − 1` nonzero classes are the coordinates of the binary simplex code of length `2^(n−1) − 1`
(`MacWilliamsSloane1977`) — for `n = 5`, length 15, the `[15,4]` simplex code, dual to the `[15,11,3]`
Hamming code. That is an exact identification of the index set, **not** a claim that the repository's
character conditions form a code; the coding language adds vocabulary, not content, and should be
cited only as such. Likewise the oriented-matroid reading (`BjornerEtAl1999`): complement-pairing of
sign vectors is standard projectivisation, and nothing in the construction needs matroid machinery.

## 5. The square-class rank is exactly 15 — so `2^-15` is correct

This was the audit's highest-priority check (the brief's steps 30, 31, 48, 49). **The rank is 15 and
the coefficient `2^-15` is right.** No mathematical correction is needed.

*Proof.* The 15 forms `L_J` are degree-1 polynomials in `F_p[x_1,…,x_4]`, hence irreducible, and
pairwise non-proportional (verified symbolically: 0 proportional pairs among all 105 pairs). A
product over any nonempty subset of them is therefore a **squarefree** non-constant polynomial, so it
is never a constant times a square in `F_p(x_1,…,x_4)^×`. Hence there is no nontrivial multiplicative
relation modulo squares, the exponent matrix over `F_2` is the `15 × 15` identity, and the 15
characters `χ(L_J(x))` are independent. The square-class rank is `15`; the same argument gives `7`
for `n = 4` and `2^(n−1) − 1` in general. ∎

**Conceptual ancestry (the brief's steps 33, 34).** Prescribing the 15 signs is prescribing the
Frobenius sign vector in the multiquadratic extension `F_p(x)(√L_J : J)`. Independence modulo squares
makes the Galois group `(Z/2)^15`, of order `2^15`, and each sign vector is one coset — so the density
`2^-15` is a subgroup index, and the square-root error is the usual Chebotarev error in that setting
(`Rosen2002`). **This is the cleanest ancestry for the main term, and it is entirely standard.**

The one-dimensional prototype is classical and predates the sheaf language: counting `x` with a
prescribed pattern of `k` Legendre symbols gives `p/2^k` plus a square-root error
(`Peralta1992`; `DavenportErdos1952` for the underlying equidistribution; `Burgess1957` for the
character-sum input).

**Caveat the main term does not see.** The all-`+1` set is invariant under scaling by nonzero squares
(`χ(z²L) = χ(L)`), so its cardinality is always a multiple of `(p−1)/2`. Measured for `n = 5`:
`p = 23 → 11 = 1 × 11`, `p = 47 → 115 = 5 × 23`, `p = 73 → 540 = 15 × 36`, and `0` for every other
prime tested up to 73. The count is thus quantised into square-class orbits, which the smooth main
term cannot reflect at small `p`.

## 6. The error term `O(p^{7/2})`: elementary Weil, and not optimal

The exponent is exactly `d − 1/2` with `d = 4`. Its source is the **one-variable** Weil bound
(`Weil1949`): fix three of the four variables, and the inner sum is `Σ_{x_1} χ(f(x_1))` with `f` a
product of distinct linear forms; Weil gives `O(√p)`, and summing trivially over the `p^3` choices of
the other three variables gives `p^3 · O(√p) = O(p^{7/2})`.

So: **no multivariate theorem is needed for `O(p^{7/2})`, and citing "the Weil bound" for it is
legitimate** — provided the citation is to the one-variable bound used one slice at a time, which is
what the exponent reflects. Two consequences the repository (or the absent paper) should state:

* `O(p^{7/2})` is **coarse**. For a nondegenerate `d`-dimensional multiplicative character sum,
  Deligne's theory gives `O(p^{d/2}) = O(p^2)` (`Deligne1980`), a saving of `p^{3/2}`. A sharper
  statement is available and would need the nondegeneracy hypotheses checked on the strata where
  forms become proportional.
* The zero locus and the pairwise-distinctness conditions are **not** an `O()` hand-wave: the clean
  locus is the complement of an explicit hyperplane arrangement, whose point count is a polynomial in
  `p` (`Athanasiadis1996`, `OrlikTerao1992`), and the excluded part is `O(p^3)` — too small to disturb
  a `p^4` main term. This is worth stating exactly rather than absorbing.

**Effective threshold (the brief's step 36).** `2^-15 p^4` exceeds `C p^{7/2}` only when
`√p > C · 2^15`, i.e. `p > C² · 2^30 ≈ 1.07 × 10^9 · C²`. With any realistic constant the threshold
is well beyond `10^9`. **So the asymptotic gives existence only for astronomically large `p`, and no
computation can confirm it.** The measured clean counts are `0` for every prime up to 73 — for both
residue classes mod 4 — which is entirely consistent, and exactly what the absent paper's "Section 9
caution" apparently says. An existence claim derived from this asymptotic is honest only if the
threshold is stated.

**Why the small-`p` counts vanish, concretely.** Every all-`+1` point found at `p ≤ 73` is maximally
degenerate: the coincidence patterns of `(A_1,…,A_5)` are `(4,1)` at `p=23`, `(4,1)` and `(3,1,1)` at
`p=47`, `(4,1)` and `(3,2)` at `p=73` — i.e. always with four or three coordinates equal. On such a
diagonal the 15 conditions collapse to 2 or 3 distinct ones, so the degenerate strata have far higher
density than the generic locus and dominate at small `p`. The pairwise-distinctness requirement then
removes all of them, giving `N_0^clean = 0`. This is a sharper explanation than "small `p` is noisy",
and it also shows the implied constant in the error term is genuinely large.

## 7. The Gateway relation is an elementary symmetry consequence

The README presents `Σ_II(p) = χ(−1) Σ_I(p)` as the repository's own contribution, one that "appears
to be new and is specific to the hypercuboid construction". The relation is correct — reproduced
independently here for 14 primes — but it is **two substitutions deep**, and the audit classifies it
as `ELEMENTARY SYMMETRY CONSEQUENCE` rather than a theorem.

*Derivation* (verified symbolically; the ratio below is exactly `−1`).
`Σ_I` omits the form of the complement-pair `{1,2,3}|{4}`; `Σ_II` omits `{3}|{1,2,4}`. Both omitted
pairs have shape `(1,3)`, so they lie in the **same** `S_4`-orbit — yet the two sums differ. The
reason is the representative convention: `Σ_II`'s product contains the form
`L_{\{1,2,3\}} = A_1+A_2+A_3 = −A_4`, and rewriting it as `A_4` costs one factor `χ(−1)`. Applying the
transposition `A_3 ↔ A_4` — a measure-preserving bijection of the zero sector — then carries the
remaining product exactly onto `Σ_I`'s integrand, because `A_1+A_4 = −(A_2+A_3)` and
`A_2+A_4 = −(A_1+A_3)` contribute two sign flips that cancel. Hence

```
Σ_II(p) = χ(−1) · Σ_I(p)          for every odd p.
```

The same bookkeeping explains the whole classification. Computing all **seven** "omit one form" sums
directly gives exactly **three** distinct values, split `3 + 1 + 3`:

| Omitted complement-pair | shape | count | value |
|---|---|---|---|
| `{1}\|{2,3,4}`, `{2}\|{1,3,4}`, `{3}\|{1,2,4}` | (1,3) | 3 | `Σ_II` |
| `{1,2,3}\|{4}` | (1,3) | 1 | `Σ_I = χ(−1) Σ_II` |
| `{1,2}\|{3,4}`, `{1,3}\|{2,4}`, `{2,3}\|{1,4}` | (2,2) | 3 | `Σ_III` |

`S_4` has only **two** orbits on the 7 points of the Fano plane (sizes 4 and 3, by pair shape). The
"three classes" arise because the size-4 orbit splits `3 + 1` according to whether the omitted
representative involves the eliminated coordinate `A_4` — and crossing that split costs exactly one
`χ(−1)`. So the three-class structure and the Gateway relation are **one** phenomenon: the
complement relation `D_{S^c} = −D_S` of §3, applied to the choice of representative.

`Σ_III`'s vanishing is the same mechanism in its self-paired form: under the double transposition
`(1 3)(2 4)` the `Σ_III` integrand maps to exactly `−1` times itself (verified symbolically), so
`Σ_III = χ(−1) Σ_III`, forcing `Σ_III = 0` when `p ≡ 3 mod 4`. A sign-reversing involution argument;
`ELEMENTARY SYMMETRY CONSEQUENCE`. The repository already describes this one accurately as "an
independent, self-contained symmetry argument".

Also elementary, and worth recording as such: **`Σ_S(p) = 0` for every odd `|S|`** (C3). The product
of `|S|` linear forms is homogeneous of odd degree, so `χ(P(zv)) = χ(z)χ(P(v))`, and summing over the
punctured line gives `Σ_{z≠0} χ(z) = 0`. One line, and the same homogeneity device the manuscript
already uses for `Σ_I = (p−1)S(p)` with even degree 6.

## 8. Computational reproduction

Independent re-implementation (`pow(a,(p−1)/2,p)` only, no repository imports, exact integers
throughout — no floating point anywhere):

| Claim | Primes checked | Result |
|---|---|---|
| `Σ_I(p) = (p−1) S(p)` | 14 primes, 5–53 | exact match, every prime |
| **`Σ_II(p) = χ(−1) Σ_I(p)`** | 14 primes, 5–53 | exact match, every prime |
| `Σ_III(p) = 0` for `p ≡ 3 mod 4` | 7 primes | exact, and nonzero for every `p ≡ 1 mod 4` |
| `Σ_S(p) = 0` for all odd `|S|`, `n = 4` | all 64 odd subsets × 14 primes | no violation |
| `N_0^clean(p,5)` | 17 primes, 3–73 | `0` throughout — matches the repository's own run exactly |
| all-`+1` count (no distinctness), `n = 5` | 17 primes | `0` except `p = 23, 47, 73` → `11, 115, 540` |

The repository's own `scripts/baseline_verification.py` was run as shipped: odd-cardinality vanishing
holds in **131,072** checked `(S,p)` pairs for `n = 5` (plus 512 for `n = 4`, 32 for `n = 3`), and its
clean counts agree with the independent implementation. Environment: Python 3.14.7, numpy 2.5.3,
sympy 1.14. No random seeds are used anywhere — every computation is deterministic and exact.

**Software-path audit (step 55):** clean. `baseline_verification.py` imports from `core` via an
explicit `sys.path.insert` of its own directory — a deliberate, visible path setup, not a hack; there
is no `conftest.py`; there is no second implementation of `legendre_table`, `chi_columns` or
`sigma_S`; `results/*.json` are outputs, never inputs to a computation. There is, however, **no test
suite** — `scripts/verify_engine.py` and the round scripts are verification programs, not tests, and
nothing pins the reproduced values.

## 9. The one documentation defect

`scripts/baseline_verification.py` reproduces and cites, as "the paper's own theorem-level results":

* "Theorem 6.1" (`N_0^clean(p,5)` vanishing / eventual nonvanishing),
* "Proposition 6.2 / Appendix C.5" (odd-cardinality vanishing),
* "Section 9" (a caution about small-`p` clean counts and a "main term").

**None of these exists in either manuscript in this repository.** Both manuscripts are the K3 papers;
neither has a Theorem 6.1 of that content, and neither states a main term for `N_0^clean`. A reader
cannot check the script against its stated source. Either the referenced paper should be added, or
the script's docstring should name the external document and its DOI. This is recorded, not fixed:
fixing it needs the author to say which document is meant.

## 10. Novelty verdict, claim by claim

| Claim | Verdict |
|---|---|
| C1, C2 zero sector and representative forms | `ELEMENTARY SYMMETRY CONSEQUENCE` — the `F_2^n/⟨1⟩` quotient, `PG(n−2,2)` |
| C3 odd-cardinality vanishing | `CLASSICAL` — odd-degree homogeneity, one line |
| C4, C5 projective reduction and point count | `FINITE-FIELD STANDARD` — even-degree homogeneity; `1 + χ(c)` |
| C6, C7 Picard rank, lattices, algebraic trace | `NEW DERIVATION OF KNOWN INGREDIENTS` — Shioda–Tate plus explicit computation, carefully done |
| C8 modular trace | `SPECIALIZATION` of Livné's modularity theorem, correctly cited |
| C9 the character-sum identity | `KNOWN` — `AOP2002`, and the repository says so |
| **C10 Gateway relation** | **`ELEMENTARY SYMMETRY CONSEQUENCE`** — downgraded from the README's "appears to be new"; see §7 |
| C11 Class III vanishing | `ELEMENTARY SYMMETRY CONSEQUENCE` — sign-reversing involution |
| C12 Class III via a second K3 | `NEW DERIVATION OF KNOWN INGREDIENTS` |
| C13 independent K3-geometric derivation of C9 | **`APPARENTLY DISTINCT STRUCTURAL RESULT`** — the strongest surviving contribution |
| C14 clean-count vanishing / eventual existence | `SPECIALIZATION OF CHARACTER-SUM THEORY`, with an unstated and astronomical effective threshold |
| the `2^-15` coefficient | **correct**; square-class rank verified to be exactly 15 |
| the `O(p^{7/2})` error | correct but **coarse**; `O(p^2)` is available from `Deligne1980` under nondegeneracy |

## 11. Manuscript revision classification: **B, with one C element**

`B — citation/provenance only` for the mathematics: nothing is wrong. Every claim checked reproduces
exactly, the `2^-15` coefficient matches the true rank, the error exponent is sound, and the
manuscripts already attribute the central evaluation to `AOP2002` prominently and correctly.

The `C` element is confined to two wordings:

1. the README's description of the Gateway relation as a contribution that "appears to be new"
   should be softened to what §7 establishes — an elementary consequence of `D_{S^c} = −D_S` and one
   transposition, which is worth stating but is not a theorem;
2. the finite-field ancestry (§3–§5) should be cited. The manuscript's bibliography has ten entries,
   all K3/modularity; it contains nothing on quadratic-character sums, prescribed Legendre-symbol
   patterns, `PG(n−2,2)`, or Kummer/Chebotarev, so a reader cannot see how standard the combinatorial
   layer is. `references.bib` now supplies that.

Not D: the strongest prior art (`AOP2002`) implies the *evaluation*, which was never claimed, and no
located theorem implies C13's independent geometric derivation. Not E: no mathematical correction is
required. **No Zenodo record was updated and no manuscript was modified.**

---

## WHAT IS CLASSICAL

Euler's criterion and `χ(−1) = (−1)^((p−1)/2)`, hence the entire `p ≡ 1 mod 4` obstruction. The
vanishing of odd-degree homogeneous character sums. The `1 + χ(c)` point-count identity. The
one-variable Weil bound and the square-root error it produces. The density `2^-m` for `m`
multiplicatively independent quadratic conditions, whether read through Kummer theory and
function-field Chebotarev or through the classical prescribed-Legendre-pattern literature. The point
counts of `PG(n−2,2)`. The evaluation of `S(p)` itself (`AOP2002`).

## WHAT IS JUST A REPARAMETERIZATION OR SYMMETRY QUOTIENT

The `2^n − 2 → 2^(n−1) − 1` collapse: the fixed-point-free involution `S ↔ S^c`, i.e. the quotient
`F_2^n/⟨(1,…,1)⟩`, whose nonzero classes are the points of `PG(n−2,2)` — 15 for `n = 5`, the Fano
plane for `n = 4`. The repository's representative forms `L_J`, `J ⊆ [n−1]`, are exactly the coset
representatives with last coordinate zero. The three-class structure for `n = 4` and the Gateway
relation `Σ_II = χ(−1) Σ_I` are a single consequence of that same quotient together with one
transposition. "Gateway" and "hypercuboid" are this project's names for a simultaneous prescription
of quadratic characters on the complement of a hyperplane arrangement.

## WHAT APPEARS DISTINCT

The independent K3-geometric derivation of the `AOP2002` character-sum identity — a Picard-lattice,
Mordell–Weil and modularity route to an identity that was originally proved by direct Jacobi-sum
computation. No located source derives it this way. The identification of the specific surface
(`disc NS = 8`, `T(X) ≅ diag(2,4)`, CM by `Q(√−2)`, newform `8.3.d.a`) arising from this particular
reduction, and the companion Class III surface (`disc 4`, CM by `Q(i)`), are concrete and appear
unstated elsewhere. That the two resolved classes land in two different arithmetic-geometric sectors
is an observation the repository already scopes correctly as an observation, not a theorem.

## WHAT THIS REPOSITORY ACTUALLY ADDS

A specific, fully worked reduction from a combinatorial residue condition to a named singular K3
surface and a named weight-3 CM newform, together with a second, geometric proof of an identity that
previously had only an analytic one — and an unusually disciplined audit trail: a theorem ledger, a
reference audit that flags which citations were read directly and which were not, and a round-by-round
research log that records its own corrected errors. The combinatorial layer is classical, the
character-sum layer is classical, and the repository does not claim otherwise for the evaluation. What
is genuinely its own is the bridge and the second derivation. The Gateway relation should be presented
as a convenient bookkeeping identity, not as a discovery.

---

## TABLE 1 — Novelty and provenance after Zotero review

| Result / claim | Closest literature | Standard formulation | Repository contribution | Classification | Confidence | Recommended wording |
|---|---|---|---|---|---|---|
| `p ≡ 1 mod 4` obstruction | `Paley1933`, `IrelandRosen1990` | `χ(−1) = (−1)^((p−1)/2)` | applies it | `CLASSICAL` | high | "as for Paley-type constructions, the condition is exactly `χ(−1) = 1`" |
| `2^n − 2` raw conditions | — | nonempty proper subsets of `[n]` | indexing | `CLASSICAL` | high | "indexed by nonempty proper subsets" |
| collapse to `2^(n−1) − 1` | `Hirschfeld1998`, `MacWilliamsSloane1977` | `F_2^n/⟨1⟩`; points of `PG(n−2,2)` | applies it | `ELEMENTARY SYMMETRY CONSEQUENCE` | high | "the quotient by the all-ones vector; `PG(3,2)` for `n = 5`" |
| 15 independent conditions | `Rosen2002`, `Peralta1992` | independence mod squares; `(Z/2)^15` Kummer group | verified rank | `CLASSICAL` | high | "independent modulo squares since the forms are distinct and linear" |
| main term `2^-15 p^4` | `Peralta1992`, `DavenportErdos1952` | `2^-m q^d` for `m` independent conditions | specialization | `SPECIALIZATION OF KUMMER/CHEBOTAREV` | high | "the expected density for 15 independent quadratic conditions" |
| error `O(p^{7/2})` | `Weil1949`; sharper `Deligne1980` | `p^{d−1/2}` from one-variable Weil | specialization | `SPECIALIZATION OF CHARACTER-SUM THEORY` | high | "one Weil saving in one variable; not optimal" |
| clean/zero-locus correction | `Athanasiadis1996`, `OrlikTerao1992` | arrangement-complement point count | applies it | `FINITE-FIELD STANDARD` | med-high | "the excluded locus is `O(p^3)`, by an exact arrangement count" |
| `Σ_S = 0`, odd `\|S\|` | `LidlNiederreiter1997` | odd-degree homogeneity | one-line proof | `CLASSICAL` | high | "immediate from homogeneity of odd degree" |
| `Σ_I = (p−1)S(p)` | `LidlNiederreiter1997` | even-degree homogeneity | explicit reduction | `FINITE-FIELD STANDARD` | high | keep as is |
| **Gateway `Σ_II = χ(−1)Σ_I`** | none located | complement relation + one transposition | the observation | `ELEMENTARY SYMMETRY CONSEQUENCE` | high | "an elementary bookkeeping identity" — **not** "appears to be new" |
| `Σ_III = 0`, `p ≡ 3 mod 4` | none located | sign-reversing involution | the observation | `ELEMENTARY SYMMETRY CONSEQUENCE` | high | keep — already described as elementary |
| `S(p)` evaluation | `AOP2002` | Jacobi sums | none claimed | `KNOWN` | high | keep — already credited |
| independent K3 derivation | `Shioda1972`, `Livne1995` | Shioda–Tate + modularity | **the contribution** | `APPARENTLY DISTINCT STRUCTURAL RESULT` | med-high | keep |

## TABLE 2 — Ancestry of the `n = 5` count

| Step | Mathematical fact | Known previously? | Source | Repo-specific? | Proof / computation status |
|---|---|---|---|---|---|
| 1 | zero sector `Σ A_i = 0`, ambient `F_p^4` | yes | elementary | no | definition |
| 2 | conditions indexed by nonempty proper `S ⊊ [5]`: 30 | yes | elementary | no | verified |
| 3 | `D_{S^c} = −D_S` | yes | elementary | no | symbolic, exact |
| 4 | `χ(−1) = 1` ⟺ `p ≡ 1 mod 4` | yes | `IrelandRosen1990` | no | Euler's criterion |
| 5 | complement quotient: `30 → 15` | yes | `Hirschfeld1998` | no | verified, fixed-point-free |
| 6 | 15 classes = nonzero `F_2^5/⟨1⟩` = `PG(3,2)` | yes | `Hirschfeld1998` | no | verified |
| 7 | the 15 forms independent mod squares | yes | `Rosen2002` | no | **certificate below**; rank = 15 |
| 8 | indicator `1_{χ(f)=ε} = (1+εχ(f))/2` off the zeros | yes | `LidlNiederreiter1997` | no | elementary |
| 9 | main term `2^-15 p^4` | yes | `Peralta1992` | no | standard |
| 10 | nontrivial sums bounded by `√p` per variable | yes | `Weil1949` | no | standard |
| 11 | error `O(p^{7/2})` | yes | `Weil1949` | no | standard; coarse |
| 12 | clean-locus correction `O(p^3)` | yes | `Athanasiadis1996` | no | exact arrangement count |
| 13 | effective threshold `p ≳ 10^9` | — | — | **yes (unstated)** | computed here |
| 14 | `N_0^clean = 0` for all `p ≤ 73` | — | — | yes | computed, both residue classes |
| 15 | small-`p` solutions confined to deep diagonals | — | — | **yes (new here)** | computed |

### Independence certificate (step 48)

The 15 forms `L_J(x) = Σ_{j∈J}x_j`, `∅ ≠ J ⊆ {1,2,3,4}`, are degree-1, hence irreducible, and
pairwise non-proportional (checked: 0 proportional pairs out of 105). Any nonempty subproduct is
therefore squarefree of positive degree, so it is not a constant times a square in
`F_p(x_1,…,x_4)^×`. The exponent matrix over `F_2` is the `15 × 15` identity; its rank is 15.
Equivalently `[F_p(x)(√L_J : J) : F_p(x)] = 2^15`, so the Kummer group is `(Z/2)^15` and the density
of any prescribed sign vector is `2^-15`. **The coefficient `2^-15` matches the true rank.**

## TABLE 3 — The `30 → 15` collapse

| Raw object | Equivalence relation | Reduced object | Standard mathematical interpretation | Known? | Repo contribution |
|---|---|---|---|---|---|
| 30 nonempty proper subsets `S ⊊ [5]` | `S ↔ S^c` | 15 complement-pairs | orbits of a fixed-point-free involution | yes | applies it |
| 30 diagonal sums `D_S` | `D_S ↔ −D_S` | 15 sums up to sign | `χ(D_{S^c}) = χ(−1)χ(D_S)` | yes | applies it |
| 30 nonconstant vectors of `F_2^5` | add `(1,1,1,1,1)` | 15 nonzero classes | `F_2^5/⟨1⟩`, dimension 4 | yes | applies it |
| 15 classes | — | 15 points | `PG(3,2)` (`n = 4`: Fano plane) | yes | identification made here |
| 15 classes | — | 15 coordinates | `[15,4]` binary simplex code; dual `[15,11,3]` Hamming | yes | analogy only — vocabulary, not content |
| 15 forms `L_J`, `J ⊆ [4]` | — | coset reps with `x_5`-coefficient 0 | canonical representatives of `F_2^5/⟨1⟩` | yes | verified bijection |

---

# THREE-PAPER RECONCILIATION

Added 2026-09-18, after examining three PDFs supplied in `~/Downloads`. **This section corrects §0 and
§9 above.** Full detail in [`PAPER_CROSSWALK.md`](PAPER_CROSSWALK.md) and
[`ASYMPTOTIC_AUDIT.md`](ASYMPTOTIC_AUDIT.md).

## 33. The missing paper exists, and the repository's references are correct

§0 above reported that no document in the repository contained
`N_0^clean(p,5) = 2^{-15}p^4 + O(p^{7/2})`, and §9 recorded the scripts' references to
"Theorem 6.1", "Proposition 6.2 / Appendix C.5" and "Section 9" as a documentation defect.

**Verdict A — the exact theorem has been found**, in a third paper that is not committed here:

> **"Zero-Diagonal Complement Collapse and Character-Sum Asymptotics in Clean Finite-Field Hypercuboid
> Residue Systems"**, Elias De Jesús, 15 pp, created 2026-08-31.
> DOI [`10.5281/zenodo.22216640`](https://doi.org/10.5281/zenodo.22216640) (`DeJesus2026collapse`;
> concept DOI `10.5281/zenodo.20533894`; the deposit title omits "and Character-Sum Asymptotics").
> SHA-256 `7994b538772237663aec70940278467a60c2512f65c894f006b80df5f4b03bbb`.

It contains Theorem 6.1 (the exact asymptotic, §6), Proposition 6.2 (odd-`|S|` exact vanishing, §6),
Appendix C.5 (additional symmetry of the zero sector) and Section 9 (computational diagnostics,
including the small-`p` caution). **All four repository references are correct and correctly
numbered.** §9's "documentation defect" is withdrawn: nothing was stale. What remains is narrower and
now editorial only: the paper is deposited and citable (DOI above) but is not committed here, and the
citing script does not name it. Adding `DeJesus2026collapse` to that docstring closes the loop.

## 34. The prior audit's reconstructions were right, and the paper is more careful than assumed

The audit above reconstructed the mathematics without access to this paper. The comparison is close:

| Audit's finding (§3–§5 above) | Paper 1's own statement |
|---|---|
| `p ≡ 1 mod 4` is exactly `χ(−1) = 1` via `D_{S^c} = −D_S` | Theorem 3.1, same derivation |
| the collapse is the fixed-point-free involution `I ↔ I^c`, `(2^n−2)/2` | Theorem 3.1, verbatim |
| main term `2^{-15}` needs the forms independent modulo squares | Prop 7.1 + **Remark 7.4**, which deliberately avoids the word "independent" in favour of "pairwise non-associate, no nonempty product is a square" |
| error `7/2 = 4 − 1/2` from one-variable Weil summed over `p^3` | Theorem 5.1, exactly this, with explicit constants |
| the clean locus is a hyperplane-arrangement complement | handled as an `O(p^{d−1})` correction, folded into the constant |

Remark 7.4 is a sharper formulation than the audit's own wording. The paper also states its
non-claims explicitly (§10: no consequence for the integer perfect cuboid is claimed, and Theorem 7.2
"points the other way").

What the paper does **not** do is place any of this in the literature: its bibliography has four
entries, and it names neither `PG(3,2)`, nor the resonance arrangement, nor prescribed-Legendre-pattern
counts, nor Kummer/Chebotarev. That gap is what `references.bib` now fills.

## 35. The error term: the suggested improvement is withdrawn

The audit above closed by suggesting Deligne might sharpen `O(p^{7/2})` to about `O(p^2)`.
**That suggestion is wrong and is withdrawn.** Checked, not assumed:

* **The domain is a cone**, and for even `|S|` the integrand is scaling-invariant, so `(p−1)` divides
  every term exactly — verified at ten primes. One full factor of `p` can never oscillate, so
  `O(p^{5/2})` is the floor and `O(p^2)` is impossible.
* **Nonresonance fails** for the small subsets: the worst `|S| = 2` term is `S = {x_1, x_2+x_3}`, whose
  product does not involve `x_4` at all, so that direction admits no cancellation. The hypotheses of a
  `O(p^{d/2})` theorem are violated, not merely unchecked (`STV1995` is the framework that makes this
  precise).
* **Empirically** `max_S|T_S| ~ p^{3.4}`–`p^{3.9}` over `p = 23…43` — consistent with `7/2`, and
  inconsistent with `2` or `5/2`.

The paper itself is careful here: Remark 6.3 says the odd-vanishing does not improve the exponent, and
**Open Problem 11.1 asks exactly whether `O(p^{7/2})` can be improved to `O(p^3)`.** It never invokes
Deligne.

## 36. What *is* available: an exact main term

The 15 forms are all nonzero `0/1` forms in four variables — the **resonance arrangement `R_4`**
(`Kuhne2023`), which none of the three papers names. Computed and verified at eleven primes:

```
χ_{R_4}(p)   = p^4 − 15p^3 + 80p^2 − 170p + 104 = (p−4)(p−1)(p^2−10p+26)
|clean domain| = p^4 − 25p^3 + 215p^2 − 695p + 504 = (p−1)(p−7)(p−8)(p−9)
```

and, since the domain is a cone, Proposition 6.2 extends to it verbatim (odd-`|S|` terms vanish
exactly over the restricted domain — verified). Hence the exact identity

```
N_0^clean(p,5) = 2^{-15}(p−1)(p−7)(p−8)(p−9) + 2^{-15} Σ_{|S| even ≠ ∅} T_S .
```

This is a genuine structural sharpening — the `p^3`, `p^2`, `p^1` terms become exact and the number of
terms needing an estimate halves — and it needs no new analysis. It does not change the error
exponent. Classification: `ELEMENTARY CONSEQUENCE`, worth a remark, not a theorem.

## 37. Effective threshold, rigorously

From Paper 1's own explicit constants (`m = 15`, `d = 4`, plus 10 distinctness hyperplanes), the error
is at most `14p^{7/2} + 130p^3`, so a nonzero count requires `p^4/32768 > 14p^{7/2} + 130p^3`, i.e.

```
p > 2.10 × 10^11      (full inequality: p ≳ 2.14 × 10^11).
```

The audit above said "≈`10^9`" using an implied constant of 1; **that was two orders too optimistic**
and is corrected here. The `p^3` term alone would need only `p > 4.3 × 10^6` — which is why an
exponent improvement to 3 would matter, and why §35 saying it is unavailable is the operative finding.

## 38. K3 and AOP status across the three papers

Both K3 papers are scrupulous. Paper 2: `disc NS = 8`, `T(X) ≅ diag(2,4)`, CM by `Q(√−2)`, newform
`8.3.d.a`, and it states that its identity "recovers `AOP2002` Theorem 2.1 at `λ = 1`" and is "not
claimed as new", while its proof method is "a different proof method from Ahlgren–Ono–Penniston's
direct Jacobi-sum computation". Paper 3: `disc NS = 4`, `T ≅ diag(2,2)`, CM by `Q(i)`, newform
`16.3.c.a = η^6(4z)`, explicitly "Ahlgren–Ono–Penniston's own modular form, not claimed as new", with
its surface **provably non-isomorphic** to AOP's `λ = 8` surface. The repository's README matches both.

So the "independent derivation" claim is justified in the precise sense the papers state it: the
*identity* is AOP's, the *route* (Picard lattice → Mordell–Weil → Livné modularity) is not, and the
papers say so themselves rather than leaving it to a reader. For the analytic side of the comparison —
AOP's own method — the standard reference for the Jacobi-sum machinery is
`BerndtEvansWilliams1998`; the two proof architectures share only the statement, since the geometric
route never forms a Jacobi sum and the analytic route never mentions a lattice. The novelty resides in the bridge and in
the identification of the specific surfaces — which is what §"WHAT THIS REPOSITORY ACTUALLY ADDS"
above already concluded, and this reconciliation does not change it.

## 39. Publication assessment, per paper

* **Paper 1** — `B`: a publishable focused contribution built from classical machinery. Its
  theorems are specializations of one-variable Weil plus exact bookkeeping, but they are correct,
  explicitly constanted, honestly scoped, and not in the literature in this form. Needs the citation
  layer of `references.bib` and should state its threshold.
* **Paper 2** — `B/C`: the strongest single item is the independent geometric derivation; the
  evaluation is `AOP2002`'s and is credited. The Gateway relation should be demoted to a remark.
* **Paper 3** — `B`: the most technical of the three, and the only one resolving a case AOP does not
  cover, with a provably distinct surface.

Nothing requires a mathematical correction (`E`), and nothing is a wholesale novelty collapse (`D`).
**No Zenodo record was updated and no PDF was modified.**
