# Zotero organisation for this project

Companion to [`NOVELTY_AND_PROVENANCE.md`](NOVELTY_AND_PROVENANCE.md). The authoritative bibliography
is [`references.bib`](../references.bib) (20 entries); Zotero is a convenience layer and nothing in
the repository depends on it.

Applied 2026-09-18 via the Zotero local API.

| Item | State |
|---|---|
| Parent collection | **created** — `Hypercuboid Character Gateways`, with all 17 specified subcollections |
| Items | **20**, of which 19 newly imported and 1 (`IrelandRosen1990`) already in the library from another project, re-filed rather than duplicated |
| Filing | **35 memberships** across 20 distinct items |
| Tags | **11** controlled tags |
| Notes | **7** child notes in the seven-field format |

## Scope: what this bibliography is and is not

The manuscripts' own bibliography (10 entries, inside
`manuscript/hypercuboid_character_sums.tex`, audited in `manuscript/REFERENCE_AUDIT.md`) covers the
K3 and modularity side and is not duplicated here. Only three of its entries appear in this tree —
`AOP2002`, `Shioda1972`, `Livne1995` — because the ancestry argument names them.

What this tree adds is the **finite-field layer the manuscripts do not cite at all**: quadratic
character sums, prescribed Legendre-symbol patterns, the Weil and Deligne bounds,
hyperplane-arrangement point counts, finite projective geometry, coding and oriented-matroid
formulations, and function-field Kummer theory. That absence was the audit's main bibliographic
finding: a reader of the manuscript cannot currently see how standard the combinatorial layer is.

## Subcollection contents

| Subcollection | Items |
|---|---|
| `00 — Reviews & Orientation` | **0** |
| `01 — Finite Fields` | 3 |
| `02 — Quadratic Characters & Legendre Symbols` | 3 |
| `03 — Prescribed Character Patterns` | 3 |
| `04 — Weil / Deligne Character-Sum Bounds` | 4 |
| `05 — Function-Field Chebotarev & Kummer Theory` | 1 |
| `06 — Paley Graphs & Residue Structures` | 1 |
| `07 — Finite Geometry / PG Structures` | 1 |
| `08 — Coding Theory` | 1 |
| `09 — Matroids / Sign Systems` | 1 |
| `10 — Hyperplane Arrangements` | 2 |
| `11 — Pseudorandomness of Character Sequences` | 3 |
| `12 — Simultaneous Residue Conditions` | 3 |
| `13 — Computational Finite-Field Enumeration` | **0** |
| `14 — Exact n=5 / 15-Condition Search` | **0** |
| `15 — Directly Cited in Repository` | 3 |
| `16 — Closest Prior Art / Novelty Checks` | 6 |

**Three subcollections are deliberately empty, and each emptiness is a finding rather than an
omission:**

* `00 — Reviews & Orientation`: no survey was needed. Every question the audit had to answer is
  settled by a primary source or by direct computation, and adding a survey would have been padding.
* `13 — Computational Finite-Field Enumeration`: the repository's enumeration is elementary exact
  modular arithmetic (`pow(a,(p-1)/2,p)` and exhaustive loops). No external method is used or needed,
  so there is nothing to cite.
* `14 — Exact n=5 / 15-Condition Search`: **no prior art was located at this specificity.** Searches
  for the exact configuration — 15 simultaneous Legendre conditions, 30 reduced to 15, the constant
  `2^-15`, `p^4/32768` — return nothing. That is a real (if weak) novelty signal for the *assembly*,
  and it coexists with every individual ingredient being classical.

`15 — Directly Cited in Repository` holds exactly the three manuscript-cited works that this audit
also uses. It is deliberately not a mirror of `references.bib`: most entries here are ancestry the
manuscripts do **not** cite, which is the point.

`16 — Closest Prior Art / Novelty Checks` holds six: `Weil1949`, `Deligne1980`, `Peralta1992`,
`Athanasiadis1996`, `Hirschfeld1998`, `AOP2002` — one per novelty question actually at issue
(error exponent, sharper error, main-term density, clean-locus correction, the `30 → 15` geometry,
the central evaluation).

## Tags

`character-sum-standard` 5, `classical` 8, `closest-prior-art` 6, `quadratic-character` 5,
`finite-field-standard` 3, `directly-cited` 3, `known-reparameterized` 1, `elementary-symmetry` 1,
`kummer-chebotarev` 1, `projective-geometry` 1, `coding-theory-prior-art` 1.

Not created, because nothing earned them: `new-derivation-known-ingredients`,
`computational-confirmation`, `apparently-distinct`, `uncertain-more-search`. The first two describe
*repository claims* rather than sources, and the classifications live in the tables of
`NOVELTY_AND_PROVENANCE.md`; no source in this bibliography is itself apparently distinct from prior
art, and none is in an unresolved state.

One shared item (`IrelandRosen1990`) additionally carries the tag `elementary-consequence` from an
earlier audit of a different project in the same library. Tags on a shared item are shared; it was
left in place rather than stripped.

## Notes

Seven child notes, each with the fields `REPOSITORY CLAIM`, `SOURCE RESULT`, `NOTATION TRANSLATION`,
`STANDARD FORMULATION`, `DOES SOURCE IMPLY THE REPO CLAIM?`, `ASSUMPTIONS`, `RECOMMENDED WORDING`, on:
`Peralta1992` (main-term density), `Weil1949` (the `7/2` exponent), `Deligne1980` (the sharper bound
available), `Hirschfeld1998` (the `30 → 15` geometry), `AOP2002` (the central evaluation),
`Rosen2002` (Kummer/Chebotarev ancestry) and `Athanasiadis1996` (clean-locus correction).

In all seven, the answer to **DOES SOURCE IMPLY THE REPO CLAIM?** is yes for the ingredient and no
for the assembly — except `AOP2002`, which implies the evaluation outright and which the repository
already credits.
