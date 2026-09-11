# Appendix Plan — Manuscript Phase 1

Minimal appendix structure for a skeptical reader to verify the
argument without the main text becoming a computation log.

## Appendix A — Weierstrass model and Kodaira classification

`a_2(t),a_4(t),a_6=0`; the computation of `c_4,c_6,\Delta,j` (exact
polynomials); the `(\mathrm{ord}\,c_4,\mathrm{ord}\,c_6,\mathrm{ord}\,\Delta)`
table at `t=0,1,-1,\infty`, classified against Tate's algorithm's
valuation criteria; the Euler-number cross-check (`8+2+6+8=24`).
**Source**: Round 34 Part IV (freshly reconstructed), Round 11
(original construction). **Why an appendix, not main text**: the
polynomial algebra is mechanical and lengthy; the main text should
state the four Kodaira types and cite this appendix for the
verification.

## Appendix B — Local fiber-component and point-count calculations

The full explicit resolution of `I_2^*` (7 components, Round 27's
table with equations and fields of definition), `I_0^*` (5 components,
Round 19/29), and `I_2` (2 components, the corrected intersection-point
analysis, Round 32/34) — including the `N_{I_2}(p)=2p+1-\chi(-2)` proof
in full (the node/conic tangent-direction identification). **Source**:
Rounds 16, 19, 24–29, 32, 34 Part V. **Why an appendix**: this is the
single longest and most technical piece of the whole proof; the main
text (Proposition 4) should state the four `N_\bullet(p)` formulas and
the resulting `\#X=\#V+19p+1` identity, with full derivations here.

## Appendix C — Height computation and the Mordell–Weil section

`P_1$'s explicit coordinates over `\mathbb Q(i)(t)`; the curve-membership
and Galois-action verifications by direct substitution; the four-fiber
local-contribution table and Shioda height formula computation giving
`\hat h(P_1)=1`; the torsion-orbit argument (Round 21) showing this is
the unique relevant generator up to sign/torsion translation. **Source**:
Round 20–21, Manuscript Phase 1 Part II.A. **Why an appendix**: the
substitution algebra and the four-fiber lookup are exactly the kind of
"a skeptical reader should be able to check this line by line" material
that belongs out of the main narrative flow.

## Appendix D — Modularity, twist determination, and the CM identity

The full statement of Livné's theorem as verified against the primary
source; the ramification argument restricting the twist to a 4-element
set; the degeneracy argument collapsing this to 2; the `p=3` elimination
computation; the Sym² decomposition algebra deriving
`a_p(f)=a_p(E)^2-p(1+\chi(-2))`. **Source**: Round 30, 33, 34 Parts
VIII–XII. **Why an appendix**: this is the highest-scrutiny part of the
proof (per the manuscript's own audit history) and deserves to be laid
out in complete, unhurried, line-by-line detail for referee
verification, separate from the main text's compressed statement
(Proposition 7).

## Appendix E — Computational verification scripts and reproducibility

Pointers to the `scripts/` directory: which script verifies which
formula, how to regenerate the LMFDB `8.3.d.a` trace data (raw API
call, documented to avoid AI-summarized-fetch transcription errors, per
Round 13's discipline), and an explicit statement that **every script
here is verification only** — none supplies a step the proof logically
requires (cross-referencing the Theorem Ledger's "COMPUTATIONAL CHECK
ONLY" column, which is empty for anything load-bearing). **Source**: all
rounds' `scripts/*.py`. **Why an appendix**: standard reproducibility
practice; keeps "trust me, I ran the numbers" material clearly
separated from the deductive argument.

## Recommendation

**Five appendices (A–E) is the right minimal count.** Do not split
further (e.g. separate appendices per Kodaira fiber) — Appendix B can
internally subdivide by fiber type with subsection headers without
needing separate appendix letters. Do not merge C and D — the height
computation (C, purely `\mathbb Q(i)(t)`-algebra) and the modularity/twist
argument (D, representation theory + one external citation-based
computation) are logically and stylistically distinct enough to deserve
separate appendices, and a referee auditing D (the highest-risk part)
should not have to wade through C's unrelated algebra first.
