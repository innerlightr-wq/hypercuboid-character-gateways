# Class III Sequel — Phase 3 Appendix Audit

Six appendices (A–F) were drafted, expanding every compressed
computation in the main text (Sections 1–10) into a line-by-line,
independently checkable derivation. This document records the
cross-appendix consistency audit, the literature re-verification, and
the adversarial final check required by this phase.

## Appendix status

- **Appendix A** (character-sum reduction): complete. Rebuilds the
  projective reduction with every substitution shown, explicitly flags
  and resolves the exact point where Phase 2A's variable-swap bug
  occurred, and ends with the symbolic identity
  `P_III(1,x,t) - xt(t+1)(x+t)(x+t+1) = 0` stated as the closing check.
- **Appendix B** (Weierstrass model and singular fibers): complete. All
  of `a_2, a_4, c_4, c_6, Δ, j` derived from the affine surface; `I2*`
  classification independently justified at each of `T=0,-1,∞` via
  explicit valuations (not a bare Kodaira-table citation); minimality,
  component pattern, and the `3×8=24` Euler-number check all included.
- **Appendix C** (rational 2-torsion and specialization): complete. The
  factorization re-verified via Vieta; torsion completeness given in
  full (both the ≤3-roots elementary step and the Shioda-injectivity
  exponent-2 step); a consolidated specialization table across all three
  fibers; the multiplicity-one independent-chart cross-check included.
- **Appendix D** (graph rigidity and NS lattice): complete. The
  five-step rigidity proof restated with each step labeled; the 20-generator
  basis and rank count; the `Tr(F_p|NS)=20p` derivation; and — per this
  round's explicit demand — the discriminant computed strictly
  line-by-line (`det(D6 Cartan matrix)=4` shown, not quoted; `disc(Triv)=-64`;
  `|disc NS|=64/16=4`), each factor separately justified.
- **Appendix E** (transcendental lattice, CM, modularity): complete.
  Derives `T(X_III)=diag(2,2)` from `ρ=20,|disc NS|=4` alone; explicitly
  distinguishes the lattice from its associated quadratic form
  `(a,b,c)=(1,0,1)` (the corrected convention, with the erroneous
  `(2,0,2)` reading named and flagged as a historical note, not
  reintroduced); verifies `b²-4ac=-4`; cross-checks the convention
  against Classes I/II's own `diag(2,4)→disc -8` result; reconstructs
  the full twist-elimination chain with an explicit "why one prime
  suffices" closing paragraph.
- **Appendix F** (point-count ledger and reproducibility): complete.
  Derives `#X_III(F_p)=1+p²+20p+a_p(f)` via the full `H⁰`–`H⁴` Lefschetz
  decomposition (each cohomological degree's contribution stated
  separately, as required), then independently re-derives the same
  quantity via the affine/projective fiber-by-fiber route, and shows the
  two agree. Includes a small reproducibility table explicitly labeled
  illustrative, not evidentiary, plus a script pointer list.

## Cross-appendix consistency audit

Searched the complete `.tex` source for:

- **Phase-2A swapped-variable remnant** (`x_1=t,x_2=x`): **not found**
  anywhere in the current source — the corrected renaming (`x_1=x,x_2=t`)
  is used consistently in both the main text and Appendix A.
- **Phase-2B erroneous `(2,0,2)` form**: found in exactly two places, both
  in Appendix E, both **intentionally** naming it as the historical error
  being corrected (never used as a live claim).
- **"Matches at p=5"-type language implying a numerical pattern proves
  modularity**: found in exactly one place, which is the sentence
  explicitly *denying* this framing ("This is not a claim that `F_0`
  'matches at p=5.'"). No instance asserts the forbidden framing.
- **Claims that the modular form or K3 surface itself is new**: none
  found anywhere in the source.
- **`|disc NS|`, `|disc T|` numeric consistency**: every occurrence
  across the main text, comparison table, and both relevant appendices
  states `4` (Class III) and `8` (Classes I/II, cited) with no stray
  inconsistent value.
- **"Standard computation" as an unexplained placeholder**: the only
  occurrence of this phrase is the sentence stating that *no* step is
  left as such — i.e., it appears only to disclaim itself.

**No stale or inconsistent convention was found.**

## Literature re-verification

A fresh search this round independently confirmed the Shioda–Inose
(1977) convention used throughout Section 6 and Appendix E: singular K3
surfaces correspond, via their transcendental lattice, to matrices of
the form $\begin{pmatrix}2a&b\\b&2c\end{pmatrix}$ (i.e. the *halved*
diagonal convention), under $\mathrm{SL}_2(\Z)$-equivalence — matching
exactly the corrected dictionary used here, independently confirming the
Phase 2B fix was not just internally consistent but matches the
literature's own stated convention. Kodaira/Néron/Tate, Shioda's
Mordell–Weil-lattice paper, Miranda–Persson, Livné, and AOP citations
were re-checked against their already-established bibliographic data
(carried over from Phases 2A/2B, themselves independently sourced); no
discrepancy found. Novelty language was not strengthened anywhere.

## Adversarial final check (13 targets)

All thirteen targets listed in this round's prompt were attacked
directly, each via the corresponding appendix's from-scratch derivation
(not by re-reading the main text for plausibility):

1. `Σ_III=(p-1)T(p)` — Appendix A, symbolic identity to literal zero. **Survives.**
2. Three `I2*` classifications — Appendix B, explicit valuations at all
   three points, not a table lookup. **Survives.**
3. Rational 2-torsion completeness — Appendix C, both steps shown in full. **Survives.**
4. Multiplicity-one specialization — Appendix C, cross-checked via a
   second, independent blow-up chart. **Survives.**
5. Graph rigidity — Appendix D, five explicitly labeled steps, tree
   structure only. **Survives.**
6. `ρ=20` — re-derived from `Triv` rank matching the Hodge bound with
   equality. **Survives.**
7. `|disc NS|=4` — Appendix D, `det(D6 Cartan)=4` shown explicitly, not
   quoted. **Survives.**
8. `T(X)=diag(2,2)` — Appendix E, derived from `ρ,|disc NS|` alone. **Survives.**
9. CM by `Q(i)` — Appendix E, via the corrected `(1,0,1)` form,
   `h(-4)=1` uniqueness, cross-checked against Classes I/II. **Survives.**
10. Twist exhaustiveness — Appendix E, ramification argument shown
    before any numerical step. **Survives.**
11. The `p=5` discriminator — recomputed independently (25-term sum,
    LMFDB lookup, elementary `χ(2)(5)` check). **Survives.**
12. Every constant in the point-count formula — Appendix F, derived two
    independent ways (cohomological and combinatorial), agreeing. **Survives.**
13. The final Class III theorem — follows deductively from items 1–12,
    all of which survived. **Survives.**

No contradiction between any appendix and the main text was found. No
correction was required this round beyond what Phases 2A and 2B had
already made (both of which are referenced, not silently absorbed,
throughout the appendices).

## Compile status

15 → 21 pages after adding Appendices A–F. Clean compile: no errors, no
undefined references, no undefined citations, across three full
`pdflatex` passes.
