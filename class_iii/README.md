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

## Revision status

The manuscript in this directory is a **corrected author revision**, dated
**21 September 2026**, of *Class III Hypercuboid Character Sums and a
Discriminant-4 Singular K3 Surface*. It is not a published version.

What changed relative to the originally submitted and deposited manuscript:

- **Provenance.** The Class III surface is now explicitly identified with the
  exceptional $\lambda=-1$ ($t=-1$) member of the Ahlgren–Ono–Penniston /
  van Geemen–Top family, via an exact $\mathbb Q$-rational coordinate change
  ($T\mapsto -T-1$, giving literal equality of defining equations). See
  `## Main result` below and the manuscript's §9.1.
- **Known prior art, credited.** The discriminant-4 singular-K3 geometry —
  $T(X)\cong\operatorname{diag}(2,2)$ and complex multiplication by
  $\mathbb Q(i)$ — is consequently presented as known prior art (Persson;
  van Geemen–Top; Shioda–Inose), independently re-derived here from the
  hypercuboid construction rather than claimed as new.
- **Surviving principal result.** The exact Class III character-sum
  evaluation remains the principal project-specific contribution: the generic
  Ahlgren–Ono–Penniston zeta-function theorem is stated for
  $\lambda\neq0,-1$ and does not cover this exceptional parameter.
- **$I_n^*$ rigidity positioning.** The four-fixed-legs component argument is
  retained as a self-contained technical step but is now positioned as a
  standard corollary of published split/non-split $I_n^*$ component theory
  (Wazir; Ulmer), not as a new general theorem.
- **Néron–Severi / trivial-lattice correction.** The integral relation is
  corrected from the false $\operatorname{NS}=\operatorname{Triv}$ to
  $\operatorname{NS}/\operatorname{Triv}\cong\mathrm{MW}\cong(\mathbb Z/2)^2$
  with $[\operatorname{NS}:\operatorname{Triv}]=4$. The 20 standard classes
  form a $\mathbb Z$-basis of $\operatorname{Triv}$; two rational $2$-torsion
  section classes complete the integral lattice.
- **K3-status proof repair.** A circular argument at the fiber over infinity
  is removed: the transformed discriminant is now computed directly from the
  rescaled coefficients, and K3 status is concluded from the resulting fiber
  types rather than assumed in obtaining them.
- **Odd-prime reduction repair.** The good-reduction argument is strengthened
  so that residue characteristic 3 is handled explicitly, rather than being
  covered by a fiber-classification criterion valid only in residue
  characteristic $\geq5$.
- **Main result unchanged.** The principal Class III character-sum theorem,
  its closed formula, and the reported numerical evaluations are **unchanged**
  by these corrections. What changed are intermediate proof statements and
  proof logic, together with the prior-art positioning.
- **Validation.** The revised manuscript rebuilds cleanly (0 errors, 0
  undefined references or citations), and the final cross-consistency checks
  produced **zero mismatches** across all odd primes $\leq61$ tested,
  including $p=3$.

The corrected manuscript revision was established at commit `6779b6f`.

### Current archival version

The corrected September 21, 2026 author revision is archived on Zenodo:

> Elias De Jesús (2026), *Class III Hypercuboid Character Sums and a
> Discriminant-4 Singular K3 Surface*. Zenodo.
> <https://doi.org/10.5281/zenodo.22883331>

This version incorporates the provenance and proof-architecture corrections
described above. The principal Class III character-sum theorem and numerical
evaluations are unchanged.

It was deposited as a **new version of the existing record**, not as a separate
upload: Zenodo registers it as a version of the concept DOI
[`10.5281/zenodo.22713446`](https://doi.org/10.5281/zenodo.22713446), which
always resolves to the most recent version. Cite the concept DOI wherever a
stable pointer is wanted, and a version DOI when a specific text is meant.

### Earlier deposited versions

Earlier Zenodo versions and the SSRN posting are **historical versions** and
remain as deposited. Nothing has been erased or rewritten. Readers comparing
against them should note that they predate the corrections listed above — in
particular, they identify the surface differently and contain the superseded
`NS = Triv` statement.

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
Ahlgren, Ono, and Penniston's own form, governing their K3 surface at
their parameter $\lambda=8$ ("Zeta functions of an infinite family of K3
surfaces," *Amer. J. Math.* **124** (2002), no. 2, 353–368).

**Neither is the surface (corrected September 2026).** A prior-art audit
established that $X_{\rm III}$ is the $\lambda=-1$ member of that same
family. Two independent checks, both in
[`scripts/class3_aop_identification.py`](scripts/class3_aop_identification.py):
$T(p)=A(-1,p)$ at every odd prime tested, and the $\mathbb Q$-linear
substitution $(x,t,w)\mapsto(x,\,t-x,\,-t-w)$ carries the Class III branch
sextic *exactly* onto the $\lambda=-1$ branch sextic, with no residual
scalar — so the two surfaces are isomorphic **over $\mathbb Q$**.

Consequently $T(X)\cong\operatorname{diag}(2,2)$, $\operatorname{disc}=4$
and CM by $\mathbb Q(i)$ are **known prior art**: van Geemen–Top, *An
isogeny of K3 surfaces*, Bull. LMS **38** (2006), 209–223, record the
lattice and discriminant, citing Persson, LNM **1124** (1985), p. 298, and
note Shioda–Inose's identification of the surface as the desingularised
quotient of $E_i\times E_i$, $E_i=\mathbb C/\mathbb Z[i]$.

This paper is therefore an **independent derivation and hypercuboid
realization of a known singular-K3 arithmetic sector**, not the discovery
of a new one. Earlier versions of this README and of the manuscript said
the surface was different from Ahlgren–Ono–Penniston's; that comparison
had been made against $\lambda=8$ only and did not extend over the family.

One point runs the other way: $\lambda=-1$ is precisely where
Ahlgren–Ono–Penniston's closed-form evaluation degenerates (it carries a
factor $\chi(\lambda+1)$ and an inverse of $\lambda+1$), and van
Geemen–Top exclude $t=-1$ from their isogeny theorem. The exact evaluation
of $\Sigma_{\rm III}(p)$ obtained here is therefore not a specialization
of theirs.

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
unconditionally. This is a different route from both
Ahlgren–Ono–Penniston's and the companion paper's methods for
establishing the analogous fact about their respective surfaces.

The graph-rigidity step itself is a **standard corollary**, not a new
result. Wazir, *Arithmetic on elliptic threefolds*, Compositio Math.
**140** (2004), 567–580, records that an $I_n^*$ fiber has either $n+5$ or
$n+3$ rational components, determined by the splitting of a quadratic;
Ulmer, PCMI **18** (2011), Lecture 3 §6, gives the same dichotomy in
split/non-split form. At most one conjugate pair of multiplicity-one
components is ever exchanged, which is exactly the lemma's conclusion.
Two caveats travel with it: $I_0^*$ needs separate treatment (its dual
graph is $\widetilde D_4$, with automorphism group $S_4$), and the
statement presumes a perfect residue field. What is claimed here is the
assembly — deducing $\operatorname{NS}$-rationality from rational
$2$-torsion alone, with no fiber resolved.

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
