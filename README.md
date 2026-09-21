# Finite-Field Hypercuboid Character Sums and a Discriminant-8 Singular K3 Surface

This repository contains the manuscript and supporting research
material for a study of finite-field character sums arising from a
zero-diagonal symmetry classification of a clean finite-field
hypercuboid residue system.

**Manuscript**: [`manuscript/hypercuboid_character_sums.pdf`](manuscript/hypercuboid_character_sums.pdf)

## Permanent archive

This manuscript is permanently archived on Zenodo:

**DOI**: [https://doi.org/10.5281/zenodo.22711323](https://doi.org/10.5281/zenodo.22711323)

> De Jesus, Elias. (2026). *Finite-Field Hypercuboid Character Sums and
> a Discriminant-8 Singular K3 Surface*. Zenodo.
> https://doi.org/10.5281/zenodo.22711323

See [How to Cite](#how-to-cite) below for the distinction between
citing the manuscript (Zenodo) and citing this code/reproducibility
repository (GitHub).

## Companion Papers

This repository now contains two companion papers, resolving between
them all three character-sum classes of the same finite-field
hypercuboid construction.

### Classes I/II

**Finite-Field Hypercuboid Character Sums and a Discriminant-8 Singular
K3 Surface**

DOI: [https://doi.org/10.5281/zenodo.22711323](https://doi.org/10.5281/zenodo.22711323)

Manuscript: [`manuscript/hypercuboid_character_sums.pdf`](manuscript/hypercuboid_character_sums.pdf)

Key arithmetic sector: $T(X)\cong\operatorname{diag}(2,4)$,
$\operatorname{disc}=8$, CM by $\mathbb Q(\sqrt{-2})$.

### Class III

**Class III Hypercuboid Character Sums and a Discriminant-4 Singular K3
Surface**

DOI: [https://doi.org/10.5281/zenodo.22713447](https://doi.org/10.5281/zenodo.22713447)

Manuscript: [`class_iii/manuscript/class3_hypercuboid_k3.pdf`](class_iii/manuscript/class3_hypercuboid_k3.pdf)

Key arithmetic sector: $T(X)\cong\operatorname{diag}(2,2)$,
$\operatorname{disc}=4$, CM by $\mathbb Q(i)$.

**Provenance (September 2026).** This surface is the $\lambda=-1$ member
of Ahlgren–Ono–Penniston's family: $T(p)=A(-1,p)$, and the branch sextics
agree after an explicit $\mathbb Q$-linear substitution, so the surfaces
are isomorphic over $\mathbb Q$ (verified in
[`class_iii/scripts/class3_aop_identification.py`](class_iii/scripts/class3_aop_identification.py)).
Its transcendental lattice, discriminant and CM field are consequently
**known prior art** — van Geemen–Top (2006), citing Persson (1985) and
Shioda–Inose (1977). The hypercuboid route is an **independent derivation
and realization** of that arithmetic sector, not the discovery of a new
one. Note that $\lambda=-1$ is exactly where Ahlgren–Ono–Penniston's own
closed-form evaluation degenerates, so the evaluation of the sum is not a
specialization of theirs.

See [`class_iii/README.md`](class_iii/README.md) for the full account of
this paper, including its literature positioning, its relation to
Ahlgren–Ono–Penniston, and its own reproducibility material.

---

Together, the two studies show that the three hypercuboid character-sum
classes considered in this project separate into two distinct
arithmetic-geometric sectors. This is stated here, as in both papers
themselves, only as an observation about these two resolved cases — not
as a general theorem about the hypercuboid construction or its constraint
classes.

## What this project studies

A clean finite-field hypercuboid residue system on four coordinates,
under its zero-diagonal complement collapse, produces three residual
character-sum symmetry classes, $\Sigma_I(p)$, $\Sigma_{II}(p)$,
$\Sigma_{III}(p)$. Two of these, Classes I and II, reduce — by an
elementary projective argument — to a classical two-variable character
sum associated with a discriminant-8 singular K3 surface and a weight-3
CM newform.

**The central character-sum evaluation was previously obtained by
Ahlgren, Ono, and Penniston** ("Zeta functions of an infinite family of
K3 surfaces," *Amer. J. Math.* **124** (2002), no. 2, 353–368) and **is
not claimed as new** here. This repository's contribution is:

- the hypercuboid reduction that produces this sum in the first place,
  and an exact **Gateway relation** connecting Classes I and II
  ($\Sigma_{II}(p)=\chi(-1)\Sigma_I(p)$), which appears to be new and is
  specific to the hypercuboid construction;
- an **independent, K3-geometric derivation** of the same character-sum
  identity, via the singular K3 surface that the hypercuboid reduction
  naturally produces — a Picard-lattice / Mordell–Weil / modularity
  argument, structurally different from Ahlgren–Ono–Penniston's direct
  Jacobi-sum computation.

**Class III** is proved to vanish for $p\equiv3\pmod4$ by an
independent, self-contained symmetry argument unrelated to the K3
machinery. Its value for $p\equiv1\pmod4$ is resolved in a companion
paper via a singular K3 surface of discriminant 4 with CM by $\mathbb
Q(i)$. That surface is *not* a new one: it is the $\lambda=-1$ member of
Ahlgren–Ono–Penniston's own family (see the Class III entry above), and
its lattice and CM data are prior art. What the companion paper supplies
is the hypercuboid route to it and the exact evaluation at a parameter
where Ahlgren–Ono–Penniston's closed form degenerates; see
[`class_iii/`](class_iii/) and the **Companion Papers** section below.

## Repository contents

```
manuscript/   the final manuscript (PDF + LaTeX source) and its
              supporting audit documentation (theorem/claim ledger,
              literature and reference audits, contribution map,
              proof-dependency graph, preprint-readiness summary)
scripts/      Python/sympy scripts used to independently verify every
              formula in the manuscript (verification only — no script
              output is a logically necessary step in any proof)
results/      raw computational outputs from the classification and
              search scripts
notes/        the full round-by-round research log documenting how the
              results were derived, audited, and corrected
```

## Reproducibility

Every non-elementary claim in the manuscript rests on either an
elementary, self-contained derivation, an explicit geometric
calculation, or a cited, verified literature theorem — never on a
computation alone. The scripts in `scripts/` independently check the
manuscript's formulas against brute-force finite-field enumeration and
against Hecke eigenvalue data for the newform `8.3.d.a` from the
[LMFDB](https://www.lmfdb.org). See `manuscript/PROOF_DEPENDENCY.md`
for the complete dependency graph and `manuscript/REFEREE_AUDIT.md` /
`manuscript/CONTRIBUTION_MAP.md` for a detailed account of what is
established here versus what is recovered from prior literature.

## How to Cite

There are two things one might cite here, and they are not the same:

**1. The manuscript / mathematical results.** If you are citing the
mathematical content — the theorems, proofs, or the character-sum
identity itself — please cite the permanent Zenodo archive. This is
the preferred citation for the manuscript and mathematical results:

> De Jesus, Elias. (2026). Finite-Field Hypercuboid Character Sums and
> a Discriminant-8 Singular K3 Surface. Zenodo.
> https://doi.org/10.5281/zenodo.22711323

**2. The code, reproducibility materials, or research audit trail.** If
you are referring specifically to the computational scripts, raw
results, or the full round-by-round research/audit log in this
repository, you may additionally reference:

> Elias De Jesus, Hypercuboid Character Gateways, GitHub repository:
> https://github.com/innerlightr-wq/hypercuboid-character-gateways

This GitHub repository is a code and reproducibility archive, not a
peer-reviewed publication; it should not be cited in place of the
Zenodo record for the mathematical results themselves.

### BibTeX

```bibtex
@misc{dejesus2026hypercuboid,
  author       = {De Jesus, Elias},
  title        = {Finite-Field Hypercuboid Character Sums and a Discriminant-8 Singular K3 Surface},
  year         = {2026},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.22711323},
  url          = {https://doi.org/10.5281/zenodo.22711323}
}
```

## License

This repository uses a **split license**: the code and the manuscript
are licensed separately.

- **Code** — the scripts in `scripts/` and other original software
  components of this repository are licensed under the **MIT License**.
  See [`LICENSE-MIT`](LICENSE-MIT).

- **Manuscript** (`manuscript/hypercuboid_character_sums.tex` and
  `manuscript/hypercuboid_character_sums.pdf`) — the paper is **not**
  MIT-licensed. It is distributed under the scholarly-content license
  specified by its authoritative Zenodo record
  ([DOI 10.5281/zenodo.22711323](https://doi.org/10.5281/zenodo.22711323)),
  verified directly against that record to be
  **Creative Commons Attribution 4.0 International (CC BY 4.0)**. See
  [`LICENSE-PAPER`](LICENSE-PAPER) for the full terms and the official
  license text.

- **Supporting scholarly materials** — unless otherwise indicated, the
  contents of `notes/`, `results/`, and the Markdown documentation files
  in `manuscript/` (the theorem/claim ledger, audits, contribution map,
  etc.) follow the paper's license (CC BY 4.0), as they document and
  support the manuscript rather than constituting independent software.

- **Third-party material** — quotations, citations, and referenced
  works (e.g. theorem statements attributed to other authors) remain
  subject to their own original rights and licenses and are not
  relicensed by anything in this repository.

**The MIT License does not apply to the manuscript merely because the
manuscript is stored in this repository.** If you are unsure which
license governs a particular file, the code/paper split above is
authoritative; MIT covers `scripts/` and comparable original software
only.

**Manuscript citation** (see also [How to Cite](#how-to-cite) above):

> De Jesus, Elias. (2026). Finite-Field Hypercuboid Character Sums and
> a Discriminant-8 Singular K3 Surface. Zenodo.
> https://doi.org/10.5281/zenodo.22711323
