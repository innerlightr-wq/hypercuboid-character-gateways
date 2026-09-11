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
machinery. Its value for $p\equiv1\pmod4$ — not addressed by
Ahlgren–Ono–Penniston either — remains **open**, and is the genuine
research frontier this project leaves behind.

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

No license has been specified for this repository.
