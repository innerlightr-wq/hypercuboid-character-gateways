# Paper crosswalk

Three papers were examined (placed in `~/Downloads`, 2026-09-18). Only two of them are committed to
this repository. Hashes are of the files as examined; no PDF was edited.

## Paper 1 — the asymptotics paper (**not in this repository**)

**"Zero-Diagonal Complement Collapse and Character-Sum Asymptotics in Clean Finite-Field Hypercuboid
Residue Systems"** · Elias De Jesús · 15 pp · pdfTeX · created 2026-08-31
· **DOI [`10.5281/zenodo.22216640`](https://doi.org/10.5281/zenodo.22216640)** (`DeJesus2026collapse`;
concept DOI `10.5281/zenodo.20533894`)
· SHA-256 `7994b538772237663aec70940278467a60c2512f65c894f006b80df5f4b03bbb`

*Metadata note:* the Zenodo deposit is titled "Zero-Diagonal Complement Collapse in Clean
Finite-Field Hypercuboid Residue Systems" — it drops "and Character-Sum Asymptotics", which the PDF's
own title page carries. Same document (deposit date matches the PDF exactly); worth aligning if the
record is ever updated.

* **Central claim.** `N_0^clean(p,5) = 0` for `p ≡ 3 (mod 4)`, and `= 2^{-15}p^4 + O(p^{7/2})` along
  `p ≡ 1 (mod 4)`.
* **Theorem numbers.** Def 2.1 (clean tuple), Def 2.2 (response channels), **Thm 3.1** (zero-diagonal
  complement collapse, `2^n − 2 → 2^{n−1} − 1`), Cor 3.2 (`n = 5`: 30 → 15; `n = 4`: 14 → 7),
  Prop 4.1–4.3 (symmetry, orbits, cyclic pentagon), **Thm 5.1** (general character-count asymptotic,
  explicit constants), **Thm 6.1**, **Prop 6.2** (odd-`|S|` exact vanishing), Prop 7.1 (pairwise
  non-associateness), **Thm 7.2** (`2^{-30}p^4 + O(p^{7/2})`, nonzero-diagonal sector), Cor 7.3,
  Thm 8.1 (exact scaling correspondence), §9 (computational diagnostics), §10 (non-claims re the
  integer perfect cuboid), §11 (eight open problems), App A (composite moduli), App B (discussion),
  **App C.5** (additional symmetry of the zero sector).
* **Repository scripts depending on it.** `scripts/baseline_verification.py` cites Thm 6.1,
  Prop 6.2 / App C.5 and §9 — **all correct**. `scripts/core.py` implements Def 2.1 and the
  `2^{n−1} − 1` representative forms of Thm 3.1. `scripts/adversarial_n5.py`,
  `classify_n4.py`, `track_a_*` operate on the same objects.
* **Closest prior art.** `Peralta1992` and `DavenportErdos1952` (prescribed Legendre patterns);
  `Weil1949` (the error term); `Rosen2002` (Kummer/Chebotarev reading of `2^{-m}`);
  `Hirschfeld1998` (the `30 → 15` index set as `PG(3,2)`); **`Kuhne2023`** (the 15 forms are the
  resonance arrangement `R_4`); `STV1995` (what a sharper error term would require).
* **Novelty classification.** `SPECIALIZATION OF CHARACTER-SUM THEORY` for Thm 5.1/6.1/7.2 —
  correct, cleanly proved, with explicit constants, but the machinery is one-variable Weil plus exact
  bookkeeping. `ELEMENTARY SYMMETRY CONSEQUENCE` for Thm 3.1. `CLASSICAL` for Prop 6.2. The
  **assembly** — this specific system, worked through with explicit constants and honest
  non-claims — is where its value lies. See `ASYMPTOTIC_AUDIT.md`.

## Paper 2 — Classes I/II and the discriminant-8 K3 (**committed**)

**"Finite-Field Hypercuboid Character Sums and a Discriminant-8 Singular K3 Surface"** · 15 pp ·
Zenodo `10.5281/zenodo.22711323` · SHA-256
`fe4dcb227b20129977f7ec15ffba1e4f8f7c83849724f13b55ab0746bbef20f8`
(the committed `manuscript/hypercuboid_character_sums.pdf`)

* **Central claim.** `Σ_I(p) = (p−1)S(p)` with
  `S(p) = χ(−1)a_p(f) + p = −χ(2)p + χ(−1)a_p(E)^2`, `E : y^2 = x^3+4x^2+2x`, `f = 8.3.d.a`;
  plus the **Gateway relation** `Σ_II(p) = χ(−1)Σ_I(p)`.
* **K3 data.** `V : Y^2 = X(X+1)T(T+1)(X+T)`; `X` its smooth model, geometric Picard number 20,
  `disc NS(X) = 8`, `T(X) ≅ diag(2,4)`, CM by `Q(√−2)`, newform `8.3.d.a` (weight 3, level 8).
* **Theorem numbers.** Lem 3.1 (projective reduction), Lem 3.2 (affine point count), Prop 4.x
  (elliptic K3 model), Prop 5.x (bad-fibre and global point-count correction), Lem/Prop 6.x
  (Mordell–Weil torsion; Picard rank and lattices), Prop 7.1–7.2 (algebraic and transcendental
  Frobenius traces), Thm (Livné), **Thm 8.1** (character-sum identity, "cf. `AOP2002` Thm 2.1"),
  Cor 9.1/Prop 9.2/Cor 9.3 (Class I closed form, Gateway relation, Class II), Prop 10.1 (Class III
  vanishing for `p ≡ 3 mod 4`), §§12–13 discussion and limitations.
* **Repository scripts depending on it.** `round11`–`round34`, `verify_engine.py`,
  `track_b_lifting.py`, `circuit_analysis.py`, `gateway_g_symmetry.py`.
* **Closest prior art.** `AOP2002` (the evaluation itself — credited, not claimed); `Shioda1972`,
  `Livne1995`.
* **Novelty classification.** `APPARENTLY DISTINCT STRUCTURAL RESULT` for the independent
  K3-geometric derivation; `KNOWN` for the evaluation; **`ELEMENTARY SYMMETRY CONSEQUENCE`** for the
  Gateway relation (downgraded in the previous audit — it is `D_{S^c} = −D_S` plus one transposition).

## Paper 3 — Class III and the discriminant-4 K3 (**committed**)

**"Class III Hypercuboid Character Sums and a Discriminant-4 Singular K3 Surface"** · 23 pp ·
Zenodo `10.5281/zenodo.22713447` · SHA-256
`ba37532b68873b903fe692ff745cd06131395ad61103a27cd2aa9aca2f9d9eb7`

*(These are the originally deposited first version: 23 pp. The current text is
the corrected revision of 21 September 2026, `10.5281/zenodo.22883331`, 27 pp,
SHA-256 `42dbaccc77aaa4f582da1c6a2b6283d81d10fe0f96325089635cd5e7cc6273e8`.
Concept DOI for all versions: `10.5281/zenodo.22713446`.)*

* **Central claim.** Evaluates `Σ_III(p)` for `p ≡ 1 (mod 4)` — the case Paper 2 left open — via a
  *different* singular K3 surface.
* **K3 data.** `disc NS(X_III) = 4`, `T(X_III) ≅ diag(2,2)`, CM field `Q(i)`,
  `Tr(F_p | NS(X_III)) = 20p` unconditionally, Mordell–Weil rank 0 (Picard number 20 from the trivial
  lattice alone), governing newform **`16.3.c.a` = `η^6(4z)`, untwisted**.
* **Theorem numbers.** Thm 6.1 is a *different* Theorem 6.1 from Paper 1's — here it is part of the
  CM-field/modularity chain, not a counting statement. Also a graph-rigidity argument for the Picard
  lattice, and a point-count ledger in §8.
* **Repository scripts depending on it.** everything under `class_iii/scripts/`.
* **Closest prior art.** `AOP2002` — and the paper is explicit that `16.3.c.a` "is exactly Ahlgren,
  Ono and Penniston's own modular form, not claimed as new"; it also states that its surface is
  **provably non-isomorphic** to AOP's `λ = 8` surface.
* **Novelty classification.** `NEW DERIVATION OF KNOWN INGREDIENTS`, with the identification of the
  specific non-isomorphic surface as the distinct part.

## Shared mathematics

The zero-diagonal complement collapse (`D_{S^c} = −D_S`, `2^n − 2 → 2^{n−1} − 1`, `χ(−1) = 1` forcing
`p ≡ 1 mod 4`) underlies all three. Paper 1 proves it as Theorem 3.1; Papers 2 and 3 use it as setup.
All three take `χ(0) = 0`, exclude `p = 2` globally, and use the same `L_J` representative convention.
`AOP2002` is the common analytic anchor for Papers 2 and 3.

## Distinct mathematics

* Paper 1: the counting theorems and their explicit constants. **No K3 content at all** — the strings
  `K3`, `Deligne`, `Kummer`, `Chebotarev` and `gateway` do not appear in it.
* Paper 2: the discriminant-8 surface, `T(X) ≅ diag(2,4)`, `8.3.d.a`, the Gateway relation, and the
  independent geometric route to the AOP identity.
* Paper 3: the discriminant-4 surface, `T ≅ diag(2,2)`, `Q(i)`, `16.3.c.a`, Mordell–Weil rank 0, and
  the non-isomorphism with AOP's `λ = 8` surface.

Duplication is modest and mostly the shared setup. The three are not salami slices of one result: the
counting theorems and the two surfaces are genuinely different mathematics, and the two surfaces are
provably distinct. Paper 3 is the longest and most technical.

## Dependency map

```
Paper 1  (asymptotics, 2026-08-31)      — cites none of the family
   │  provides Thm 3.1 (the collapse) and Def 2.1 (clean), used as setup by:
   ├─ Paper 2  (disc-8 K3, 2026-09-11)  — does NOT cite Paper 1
   └─ Paper 3  (disc-4 K3, 2026-09-11)  — cites Paper 2 as [1]; does NOT cite Paper 1
```

**Two citation gaps follow, and both are real:**

1. **Papers 2 and 3 both use Paper 1's collapse theorem without citing it.** Paper 2's §2 asserts the
   `n = 4` setup and the 7 representative forms directly; that content is Paper 1's Theorem 3.1 and
   Corollary 3.2. Paper 3 cites Paper 2 but not Paper 1.
2. **Paper 1 is not committed here**, so the repository's scripts cite a document that is not in the
   tree. It is, however, deposited and citable —
   [`10.5281/zenodo.22216640`](https://doi.org/10.5281/zenodo.22216640) — so the fix is small: name
   `DeJesus2026collapse` and its DOI in `scripts/baseline_verification.py`'s docstring, and cite it
   from Papers 2 and 3.

## Claims appearing in code but not in any paper

* The **deep-diagonal structure** of the small-`p` all-QR solutions (coincidence patterns `(4,1)`,
  `(3,2)`, `(3,1,1)`) appears in no paper. New computational observation; not theorem-level.
* The **exact clean-domain cardinality** `(p−1)(p−7)(p−8)(p−9)` and the resonance-arrangement
  identification appear in no paper. Established in this audit; see `ASYMPTOTIC_AUDIT.md` §5.
* `results/classify_n4.json` and `results/track_a_n4_full.json` are exploratory outputs with no
  corresponding paper claim — correctly, since the repository describes `scripts/` as verification
  only.

## Missing citations, by paper

**Paper 1** has four references in total (Weil 1948; Sárközy 2012; Guy; Rathbun). Missing, and all
directly load-bearing: prescribed-Legendre-pattern counts (`Peralta1992`, `DavenportErdos1952`); the
Kummer/Chebotarev reading of the `2^{-m}` density (`Rosen2002`); the finite geometry of the collapse
(`Hirschfeld1998` — `PG(3,2)`); the arrangement it works over (`Kuhne2023` — the resonance
arrangement); standard finite-field texts (`LidlNiederreiter1997`, `IrelandRosen1990`); and
`Deligne1980`/`STV1995` if the error term is ever discussed as improvable — which §11.1 does discuss.

**Papers 2 and 3** cite the K3/modularity literature carefully and completely (Paper 2's own
`REFERENCE_AUDIT.md` even records which citations were read directly). Both are missing Paper 1, and
neither cites the finite-field layer for the combinatorial setup they inherit.

## Terminology

`clean`, `zero sector`, `response channel` and `hypercuboid` are defined in **Paper 1** (Defs 2.1,
2.2). `Gateway` is **Paper 2's** term and appears nowhere in Paper 1. `collapse` is Paper 1's
(Theorem 3.1). None of these is standard terminology outside these papers, and repository
documentation should not imply otherwise.
