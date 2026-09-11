# Class III Sequel — Appendix Plan

## Disposition of the abandoned Round 3 hand blow-up sequence

**Decision: nowhere in the paper, not even as supporting verification.**

Reasoning: the Round 3 blow-up sequence was explicitly superseded — it
stalled with an unreconciled component count (5 of 7 components found per
fiber) and an unexplained "extra chart anomaly," and the graph-rigidity
argument (§4 of the planned manuscript) proves the same result
(`NS`-rationality) by a route that does not depend on it at all. Including
it, even in an appendix framed as "an earlier approach," would:
- invite a reader to wonder whether the paper's real proof secretly needs
  it (it does not);
- require explaining and then dismissing the unreconciled component-count
  discrepancy, which adds length and risk without adding rigor;
- dilute the paper's main methodological contribution (graph rigidity) by
  suggesting it was a fallback rather than the intended, cleaner route.

The Round 3 material remains exactly where it already is — in this
project's `explorations/class_iii/ROUND3_CLASS_III_REPORT.md` and its
scripts — as part of the honest research record, but is **not** manuscript
material. If a future referee specifically asks "did you try direct
resolution," the response can point to the repository's public research
log rather than to anything in the paper itself.

## Planned appendices

### Appendix A — Weierstrass invariants

Full derivation of `c4, c6, Δ` from `a2(T), a4(T)`; valuations at `T=0,
-1, ∞`; minimality check (Kraus's criterion, `v(c4)<4` at each bad fiber).
Source: Round 3 §I, Round 4 §II, Phase 5 audit Part V (all independently
cross-checked across three separate derivations — worth noting in the
appendix that this triple redundancy exists, as a reproducibility
strength).

### Appendix B — Kodaira fiber-type verification

`v(c4)=2, v(c6)=3, v(Δ)=8` at each of the three bad points, confirming
`I2*`; the degree-count argument at `T=∞` (including the correct `(2,4)`-
weighted rescaling `S=1/T`, `X̃=S^4X` — worth spelling out carefully here
since it is the one place in the whole derivation most likely to trip up
a careful reader re-deriving it themselves, per this project's own
Round 3/4 experience of needing several attempts to get the exponent
right). Euler-number cross-check `3×8=24`.

### Appendix C — Torsion completeness

The full elementary argument (Phase 5's cleaner two-step version): (1) a
cubic has at most 3 roots, so 2-torsion is exactly `(Z/2)²`, not larger,
via the exact global factorization `X(X+T(T+1))(X+T(T+1)²)`; (2) Shioda's
injectivity theorem plus the exponent-2 structure of `Φ(I2*)=(Z/2)²` at
each of the three bad fibers rules out torsion of order `>2`. Present
exactly as reconstructed in Phase 5 Part VI, since it is strictly cleaner
than the original Round 1/2 citation-heavy version.

### Appendix D — Graph automorphism verification

The exhaustive computation (all 7! permutations of the affine-`D6`
vertex set, filtered for multiplicity- and edge-preserving automorphisms,
then filtered again for those fixing all four marked legs). Present both
the mathematical argument (elementary: legs are pairwise attached to a
unique spine-end, spine-ends share a unique common neighbor) **and** the
computational confirmation, with the script itself
(`scripts/phase5_graph_rigidity_audit.py`) referenced or reproduced. This
appendix should also include the fiber-multiplicity verification (Phase 5
Part VII, Step 4 — confirming the exceptional curve at each "leg"
resolution point is genuinely reduced/multiplicity-1, not a mislabeled
spine node) since this was the one genuine gap the independent audit
found and closed, and a careful referee is the audience most likely to
ask exactly this question.

### Appendix E — Modular twist discrimination

Full derivation of the twist candidate set from the ramification-at-2
constraint; the CM-degeneracy collapse; the explicit `p=5` computation
(`T(5)=-6`, `a_5(16.3.c.a)=-6`, `χ(2)(5)=-1`) stated as an exact,
checkable arithmetic fact, not a numerical trend. This appendix should
explicitly flag (once, clearly) the one place the paper's confidence rests
on structural analogy rather than independent derivation: the exact level
(16, not 8 or 32) of the candidate newform, identified by analogy to
Ahlgren–Ono–Penniston's own level-16 surface rather than an independently
computed conductor.

### Appendix F — Reproducibility scripts

Pointer to the repository's `explorations/class_iii/scripts/` directory
(or a curated subset copied into the paper's own ancillary files, if the
target venue supports supplementary code): the elementary-identity checks
(`sympy`, verified to literal zero, not per-prime), the `p=5` twist
discriminator, the graph-automorphism enumeration, and the point-count
ledger cross-check. State plainly (matching Phase 5 Part XX) that the
*proof* depends on none of these as a pattern-match — they are included
for reproducibility and as sanity checks a reader can re-run, mirroring
the existing Classes I/II manuscript's own `PROOF_DEPENDENCY.md`
convention of separating "logically necessary" from "independently
verified."

## What stays out of the paper entirely (repository-only)

- Round-by-round narrative, self-corrections, and discovery history (all
  four `ROUND*_CLASS_III_REPORT.md` files, the `PHASE5_CLASSIII_AUDIT.md`
  audit trail, all `CHECKPOINT_*` files).
- The abandoned blow-up sequence (see decision above).
- Multi-prime falsification batteries beyond what's needed to state the
  single decisive `p=5` computation (Appendix E) — these remain valuable
  as regression tests in the repository but add nothing to the paper's
  logical content.
- The "extra chart anomaly" and other investigative dead ends.
