# Class III Hypercuboid Character Sums and a Discriminant-4 Singular K3 Surface

## Paper

[`manuscript/class3_hypercuboid_k3.pdf`](manuscript/class3_hypercuboid_k3.pdf)
(LaTeX source: [`manuscript/class3_hypercuboid_k3.tex`](manuscript/class3_hypercuboid_k3.tex))

## Citation

> De Jesús, Elias. (2026). *Class III Hypercuboid Character Sums and a
> Discriminant-4 Singular K3 Surface*. Zenodo.
> https://doi.org/10.5281/zenodo.22713447

This paper is the sequel to the repository's Classes I/II paper (see the
top-level [`README.md`](../README.md) for that paper's citation and the
`## Companion Papers` section comparing the two).

**Revision note (September 2026)**: four new remarks were added — an
explicit coordinate bridge connecting the projective-reduction lemma to
the stated affine model (Remark 4.1); a discriminant-factorization
identity shared with the companion paper, explaining this paper's three
*uniform* bad fibers directly (Remark 4.2); a characteristic clarification
confirming the Kodaira classification at every odd prime (Remark 4.4,
simpler here than in the companion paper since none of this paper's
fibers land on the $j=0,1728$ extra-automorphism locus); and a note that
the rank-$0$ conclusion needs no base-field subtlety, unlike the companion
paper's own rank-$1$ surface (Remark 4.6). See the top-level README's own
revision note and
`explorations/sector_signature_proof_closure_2026-09-14/PROOF_CLOSURE.md`
for the full derivations. No claim in this paper was changed — all four
are explanatory additions or omitted-justification repairs.

## Main result

This paper evaluates the third residual character-sum class,
$\Sigma_{\rm III}(p)$, of the same finite-field hypercuboid classification
studied by the companion Classes I/II paper — the sector that paper left
open. The sum is realized through an associated **discriminant-4 singular
K3 surface** $X_{\rm III}$, with:

- three fibers of Kodaira type $I_2^*$;
- full rational $2$-torsion, $(\mathbb Z/2)^2$, over the fibration's base
  field $\mathbb Q(T)$;
- geometric Picard rank $\rho=20$;
- $|\operatorname{disc}\operatorname{NS}(X_{\rm III})|=4$;
- transcendental lattice $T(X_{\rm III})\cong\operatorname{diag}(2,2)$;
- complex multiplication by $\mathbb Q(i)$;
- governed, via Livné's modularity theorem and a finite quadratic-twist
  elimination argument, by the weight-3, level-16 newform
  $\eta^6(4z)=$ LMFDB `16.3.c.a`.

**The modular form itself is not new.** `16.3.c.a` $=\eta^6(4z)$ is
Ahlgren, Ono, and Penniston's own form, governing their own (different)
K3 surface at their parameter $\lambda=8$ ("Zeta functions of an infinite
family of K3 surfaces," *Amer. J. Math.* **124** (2002), no. 2, 353–368).
**The K3 surface $X_{\rm III}$ is also not claimed as new beyond what a
literature search could confirm**: the exact surface, the exact character
sum, and the graph-rigidity technique used to establish
$\operatorname{NS}$-rationality were not located in the literature
searched (see the paper's own §9.1 and the `verification/` directory for
the full search discipline) — this is reported as a search-scope
limitation, not a stronger claim of originality.

## Methodological contribution

The paper's central technical step is a proof that every irreducible
component of every reducible fiber of $X_{\rm III}$ is defined over
$\mathbb Q$, without resolving any fiber explicitly. The argument: the
zero section and the three nonzero rational $2$-torsion sections mark
four pairwise-distinct multiplicity-one components ("legs") of each
$I_2^*$ fiber's affine-$D_6$ dual graph; since these four marked points
are individually $\mathbb Q$-rational, the only graph automorphism of the
fiber compatible with fixing all four legs is the identity, forcing the
remaining ("spine") components to be Galois-fixed as well. This yields
$\operatorname{Tr}(F_p\mid\operatorname{NS}(X_{\rm III}))=20p$
unconditionally. As far as this project's own literature search
determined, this is a different route from both Ahlgren–Ono–Penniston's
and the companion paper's own methods for establishing the analogous
fact about their respective surfaces.

## Relation to Classes I/II

| | Classes I/II | Class III |
|---|---|---|
| $\operatorname{disc}T(X)$ | $8$ | $4$ |
| CM field | $\mathbb Q(\sqrt{-2})$ | $\mathbb Q(i)$ |
| Modular form level | $8$ | $16$ |
| Mordell–Weil rank | $1$ (over a quadratic extension) | $0$ |

This is presented, in the paper itself and here, strictly as a structural
comparison between the two proved examples in this project — **not** as a
general theorem that the hypercuboid classification's constraint classes
always select distinct arithmetic-geometric sectors. Only two branches
have been resolved; two data points do not establish a general law.

## Prior literature

The governing modular form `16.3.c.a` $=\eta^6(4z)$ was already known
before this project, as **Ahlgren–Ono–Penniston**'s own object (attached
to their own $\lambda=8$ K3 surface), and is independently documented
elsewhere (Huber–Liu–McLaughlin–Ye–Yuan–Zhang, "On the vanishing of the
coefficients of CM eta quotients") as the trace form of a third,
different K3 surface (the quartic Fermat K3 surface). This paper does not
claim the modular form was newly discovered here — see the paper's §6.3
Remark and §9.1 for the full, precise comparison against the prior
literature.

## Reproducibility

- **`scripts/`** — Python/`sympy` scripts independently verifying the
  manuscript's symbolic identities (the projective reduction, the
  mod-4 involution, the torsion factorization, the graph-automorphism
  enumeration, the fiber-multiplicity tangent-cone computations, the
  twist-elimination discriminator at $p=5$, and the point-count ledger).
  As the manuscript itself states throughout: no script output is a
  logically necessary step in any proof — every load-bearing claim rests
  on an exact symbolic identity, a cited theorem, or a finite deductive
  elimination over an already-proved-exhaustive candidate set. Scripts
  are included for independent numerical cross-checking only.
- **`verification/`** — the external referee audit
  (`EXTERNAL_REFEREE_REPORT.md`), the repair carried out in response to
  it (`REFEREE_REPAIR_REPORT.md`), the phase-by-phase adversarial
  self-reviews performed during drafting (`PHASE2A_DRAFT_AUDIT.md`,
  `PHASE2B_DRAFT_AUDIT.md`, `PHASE3_APPENDIX_AUDIT.md`), the complete
  proof-dependency ledger (`CLASSIII_COMPLETE_PROOF_LEDGER.md`), and the
  manuscript planning documents (notation, literature positioning,
  architecture blueprint, and an earlier theorem ledger drafted before
  the appendices were written).
- **`notes/`** — the full round-by-round research log (four numbered
  research rounds plus a fifth independent audit round) documenting how
  the results were derived, audited, corrected, and eventually assembled
  into the manuscript, including a `literature/` subdirectory with the
  literature-search logs for each round.

## License

This directory follows the same split-license policy as the rest of the
repository: code (`scripts/`) under the MIT License (see the top-level
[`LICENSE-MIT`](../LICENSE-MIT)); the manuscript and supporting scholarly
material under the license specified by this paper's own Zenodo record.

That record's license was verified directly against the Zenodo API
(`https://zenodo.org/api/records/22713447`) rather than assumed, and is:

**Creative Commons Attribution 4.0 International (CC BY 4.0)** — the same
license type as the companion Classes I/II paper's own Zenodo record. See
[`LICENSE-PAPER`](LICENSE-PAPER) for the full terms, and the top-level
[`README.md`](../README.md#license) for the repository-wide split-license
explanation. **The MIT License does not apply to this paper merely
because it is stored in this repository.**
