# Claim Ledger — `hypercuboid_character_sums.tex`

**Updated Manuscript Phase 4, then the September 2026 sector-signature
integration round.** Every substantive claim, its status, and where it is
verified — now including the Ahlgren–Ono–Penniston (2002) attribution,
the completed Mordell–Weil torsion lemma, and five new remarks (the
discriminant-factorization identity, validity of the Kodaira
classification at every odd prime, the fiber-to-rank structural
explanation, and the Class II quadratic-twist / field-specific rank
results with their full derivation in new Appendix D). Source of truth
for the integration-round additions:
`explorations/sector_signature_proof_closure_2026-09-14/PROOF_CLOSURE.md`
and `INSERTIONS_FINAL.md`; verification is mathematical argument plus the
computational checks in `scripts/verify_char3_fiber_and_rank.py` — **not**
Lean kernel verification (none is used anywhere in this repository).

| Manuscript label | Claim | Status | Verified |
|---|---|---|---|
| Lemma `lem:sigmaI` | `\Sigma_I(p)=(p-1)S(p)` | PROVED — self-contained, hypercuboid-specific | In-text proof |
| Lemma `lem:V` | `\#V(\Fp)=p^2+S(p)` | PROVED — self-contained | In-text proof |
| Prop. `prop:X` | Kodaira types `I_2^*,I_2,I_0^*,I_2^*` | PROVED — self-contained | In-text proof + Appendix A |
| Prop. `prop:fibers` | `N_{I_2}(p)=2p+1-\chi(-2)` etc. | PROVED — self-contained | In-text proof |
| Prop. `prop:ledger` | `\#X(\Fp)=\#V(\Fp)+19p+1` | PROVED — self-contained | In-text proof |
| **Lemma `lem:torsion` (NEW, Phase 4)** | `\mathrm{MW}(X/\Qbar(t))_{\mathrm{tors}}\cong(\Z/2)^2` **exactly** | PROVED — self-contained + literature (Shioda 1990, Miranda–Persson 1989) | In-text proof; closes the Phase-3 gap |
| Prop. `prop:picard` | `\rho=20`, `T(X)=\mathrm{diag}(2,4)` | PROVED — self-contained + literature, **now fully justified via Lemma `lem:torsion`, not merely "the visible structure"** | In-text proof |
| Prop. `prop:trns` | `\Tr(F_p\mid NS)=(19+\chi(-1))p` | PROVED — self-contained | In-text proof |
| Prop. `prop:trt` | `\Tr(F_p\mid T)=\chi(-1)a_p(f)` | PROVED — self-contained + literature (Livné) | In-text proof |
| Remark `rem:aop` (NEW) | `a(1,p)=\chi(-1)(p)a_p(E)`, connecting to AOP's `E_1` | Numerically verified, stated as such (not claimed as an algebraic isomorphism proof) | Direct computation |
| Thm. `thm:main` | `S(p)=\chi(-1)(a_p(f)+p)=-\chi(2)p+\chi(-1)a_p(E)^2` | **PROVED here — but explicitly attributed**: recovers Ahlgren–Ono–Penniston 2002, Thm. 2.1 at `\lambda=1`. **Not claimed as a new evaluation.** | In-text proof; cross-checked against AOP numerically |
| Sec. `sec:methods` (NEW) | Comparison of the two proof methods | Honest, conservative assessment: "genuine geometric reinterpretation," not a repackaging, but also not a new evaluation | — |
| Cor. `cor:classI` | `\Sigma_I(p)` closed form | PROVED — **immediate corollary of Thm. `thm:main` + Lemma `lem:sigmaI`**, explicitly labeled as such | Immediate |
| Prop. `prop:gateway` | `\Sigma_{II}(p)=\chi(-1)\Sigma_I(p)` | PROVED — self-contained, **hypercuboid-specific, apparently new** (no AOP analogue, not found elsewhere) | In-text proof |
| Cor. `cor:classII` | `\Sigma_{II}(p)` closed form | PROVED — corollary | In-text proof |
| Table `tab:mod8` | mod-8 corollary table | Derived from the Main Theorem, regenerated directly | — |
| Prop. `prop:classIII` | `\Sigma_{III}(p)=0` at `p\equiv3\bmod4` | PROVED — self-contained, independent mechanism, **not addressed by AOP (no Class III analogue) — genuinely outside their scope** | In-text proof sketch |
| Open Problem | `\Sigma_{III}(p)` at `p\equiv1\bmod4` | **OPEN** — explicitly the paper's genuine remaining frontier, emphasized as such (Section 11 title: "Class III: the genuine open problem") | — |
| **Remark `rem:disc-factorization` (NEW, integration round)** | `\Delta(t)=16[t(t+1)]^6\cdot\operatorname{disc}_X\{0,-1,-t\}` | PROVED — elementary identity, self-contained; explanatory, does not replace the existing Kodaira classification | `scripts/verify_char3_fiber_and_rank.py` §2 |
| **Remark `rem:char-p` (NEW)** | The Kodaira classification of Appendix A is valid at every odd prime, not only characteristic 0 | PROVED — Tate's algorithm Step 2 (multiplicative point, unconditional); potentially-multiplicative-reduction theorem (tame iff `p≠2`); explicit Tate Step 6 at the one potentially-good (`j=1728`) point, reducing to the fixed integer `disc(Y^3-Y)=4` | `scripts/verify_char3_fiber_and_rank.py` §3 |
| **Remark `rem:fiber-to-rank` (NEW)** | Structural reason Class I/II's rank-1 claim needs an explicit generator while `\cite{ClassIII}`'s rank-0 claim does not | PROVED — direct consequence of `\rk\Triv=19` vs. `20` against the shared ceiling `\rho\le20` | In-text |
| **Remark `rem:class2-twist` (NEW)** | Class II's own model is the quadratic twist by `-1` of `X`; `\rk\mathrm{MW}(X/\Q(t))=0`; `\rk\mathrm{MW}(X_{II}/\Q(t))=1` | PROVED — Galois descent on `\mathrm{MW}\otimes\Q` (`\sigma(P_1)=-P_1`, already in Appendix C) for the rank-0 half; explicit `\Q(t)`-isomorphism and transported non-torsion point (Appendix D) for the rank-1 half | Appendix D; `scripts/verify_char3_fiber_and_rank.py` §§4–6 |
| **Appendix `app:class2` (NEW)** | Full coordinate chain: Class II's own quintic → completed model → invariant match with the `-1`-twist → explicit translation → transported section | PROVED — see `explorations/sector_signature_proof_closure_2026-09-14/PROOF_CLOSURE.md` §3 for the derivation this appendix condenses | `scripts/verify_char3_fiber_and_rank.py` §§4–5 |

## What changed this phase

1. **Added**: explicit, prominent citation and attribution to Ahlgren,
   Ono, Penniston, *"Zeta functions of an infinite family of K3
   surfaces,"* Amer. J. Math. 124 (2002) — the abstract, introduction,
   Theorem `thm:main`'s statement, Section `sec:methods`, and the
   Discussion/Limitations sections all now state plainly that the
   central character-sum identity recovers their Theorem 2.1 and is not
   claimed as new.
2. **Added**: Lemma `lem:torsion`, a complete, self-contained proof
   that `\mathrm{MW}(X/\Qbar(t))_{\mathrm{tors}}\cong(\Z/2)^2` exactly
   (not merely `\supseteq`), closing the one genuine mathematical gap
   Phase 3 identified. Cites Shioda 1990 and (new) Miranda–Persson 1989
   for the standard torsion-embeds-into-component-groups fact, then
   completes the argument for this specific surface using the perfect-
   square discriminant of the 2-torsion locus and the elementary fact
   that `E_t[2]` has order exactly 4.
3. **Repaired**: the Ribet citation is now split — Ribet's paper is
   cited (alongside Shimura) for the general CM/Hecke-character
   framework the Sym² splitting sits inside, no longer implied to be
   the sole or precise source of that specific decomposition.
4. **Repaired**: the Pjateckiĭ-Šapiro–Šafarevič citation now explicitly
   discloses that the 1971 original was not directly read this project,
   names the secondary sources used to corroborate it (Huybrechts,
   Schütt), and recommends a direct primary-source check before journal
   submission — stated in the bibliography itself, not hidden.
5. **Reframed**: Classes I and II are now explicitly presented as
   corollaries (of the AOP-recovering Main Theorem plus the hypercuboid
   reduction), not as the paper's primary novel contribution. The
   Gateway relation and the hypercuboid motivation itself are now
   identified, throughout the paper, as the most likely genuinely new
   content, alongside Class III's open status.

## Items still flagged for a human co-author before submission

1. Directly fetch and read the 1971 Pjateckiĭ-Šapiro–Šafarevič original
   (or the relevant chapter of Huybrechts' book) rather than relying on
   this audit's secondary-source corroboration.
2. Confirm, independently, that AOP's `E_1` and this paper's `E` really
   are the stated `\chi(-1)`-quadratic twists of one another via an
   explicit change-of-variables (this audit verified the relation
   numerically at every tested prime and via the resulting `\#X(\Fp)`
   formula match, which is very strong evidence, but did not exhibit
   the explicit isomorphism `E_1\leftrightarrow E`).
3. A domain expert should still independently confirm that no other,
   more directly overlapping paper exists beyond AOP 2002 — this audit's
   search was thorough but not exhaustive.
