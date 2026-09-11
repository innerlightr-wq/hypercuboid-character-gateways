# Proof Dependency Graph — `hypercuboid_character_sums.tex`

```
Lemma 3.1 (Sigma_I = (p-1) S(p))              [self-contained, E]
Lemma 3.2 (#V = p^2 + S(p))                    [self-contained, E]
        |
Prop 4.1 (Weierstrass model, Kodaira types)    [self-contained, G; Appendix A]
        |
Prop 5.1 (N_I2*, N_I0*, N_I2 formulas)         [self-contained, G; Appendix B]
        |
Prop 5.2 (#X = #V + 19p + 1)                    [self-contained, derived from 5.1]
        |
Prop 6.1 (rho=20, |disc NS|=8, T(X)=diag(2,4)) [self-contained + L: Shioda-Tate,
        |                                        Shioda height pairing, class-no-1;
        |                                        Appendix C]
        +--- Prop 7.1 (Tr(F_p|NS)=(19+chi(-1))p)      [self-contained, from 6.1]
        |
        +--- Prop 7.2 (Tr(F_p|T)=chi(-1)a_p(f))        [self-contained + L: Thm 7.3
                    |                                    (Livné, verified vs. primary
                    |                                    source); Appendix D]
                    |
              Theorem 8.1 (Main Theorem: S(p) formula)  [combines 5.2 + 7.1 + 7.2 + L:
                    |                                     Ribet's Sym^2 fact]
                    |
        +-----------+-----------+
        |                       |
Corollary 9.1 (Sigma_I)   Prop 9.2 (Gateway)
        |                       |
        +-----------+-----------+
                    |
            Corollary 9.3 (Sigma_II)
                    |
              Table 1 (mod-8 corollary, derived, not independent)

Prop 10.1 (Sigma_III = 0 at p=3 mod 4)   [self-contained, INDEPENDENT of everything
                                           above -- uses no result from Sections 3-9]
Open Problem 10.2 (Sigma_III at p=1 mod 4) [OPEN, no dependency graph -- unaddressed]
```

## Legend
- **E** = elementary (hand-checkable algebra/combinatorics), no citation needed.
- **G** = explicit geometric calculation (algebraic geometry, checkable via the
  equations given, no citation needed for the *method*, though the classification
  scheme — Tate's algorithm's valuation table — is classical and standard).
- **L** = external literature theorem (see `REFERENCE_AUDIT.md`).

## Load-bearing citations (removing any one breaks the Main Theorem)

1. **Shioda–Tate** (ref. [1]) — without it, Proposition 6.1's rank formula
   `\rho=19+\mathrm{rank}\,MW` has no justification.
2. **Shioda's height pairing** (ref. [2]) — without it, `\hat h(P_1)=1` and the
   discriminant-8 conclusion have no justification.
3. **Singular K3 classification** (refs. [3],[4]) — without it, the step from
   "`T(X)` is a positive-definite even rank-2 discriminant-8 lattice" to
   "`T(X)\cong\mathrm{diag}(2,4)`" (uniqueness) has no justification, though the
   *lattice computation itself* (Proposition 6.1's arithmetic) is unaffected.
4. **Livné's theorem** (ref. [5], via [6]) — without it, Proposition 7.2 has no
   starting point at all: there is no a priori reason `T(X)` should correspond
   to *any* modular form, let alone one of a specific finite twist-family. This
   is the single most load-bearing external input in the paper.
5. **Ribet's CM symmetric-square fact** (ref. [7]) — without it, the *second*
   boxed form of the Main Theorem (`S(p)=-\chi(2)p+\chi(-1)a_p(E)^2`) cannot be
   derived from the first; the first boxed form (`S(p)=\chi(-1)(a_p(f)+p)`) is
   unaffected.

## Non-load-bearing background (removing does not affect the proof)

- The explicit Shioda–Inose diagram / degree-2 correspondence with `\mathrm{Km}(E\times E')`
  (mentioned in ref. [4]'s description and §1's narrative) — used only for
  motivation/context in the Introduction; Proposition 7.2's actual proof routes
  entirely through Livné's theorem and the elimination argument, never through
  an explicit Shioda–Inose map. Confirmed during the underlying project's own
  audit (the Shioda–Inose correspondence was tested as a *candidate explanation*
  for an earlier point-count discrepancy and found unnecessary once the actual
  source of that discrepancy — the `I_2` fiber's intersection points — was
  located; see `notes/round31_report.md`, `notes/round32_report.md` in the
  repository for that history, deliberately excluded from the manuscript itself
  per `MANUSCRIPT_BLUEPRINT.md` Part X).

## Appendix completion status

| Appendix | Status | Content |
|---|---|---|
| A (Weierstrass/Kodaira) | **Complete** | Full `c_4,c_6,\Delta` derivation from `a_2,a_4`; full Tate-valuation classification at all four bad fibers; Euler-number cross-check. |
| B (local fibers) | **Complete** | Full `I_2^*` component table (7 rows, equations, fields of definition); `I_0^*` structure and rationality mechanism; the naive-count character-sum evaluation at `t=1` in full. |
| C (height computation) | **Complete** | Full symbolic curve-membership verification (the exact polynomial identity `X_1^3+a_2X_1^2+a_4X_1=-(t-1)^2(t+1)^4`, freshly re-verified symbolically during this drafting pass — see `REFERENCE_AUDIT.md`); full Galois-action computation; full four-fiber local-contribution table and height sum. |
| D (modularity/twist) | **Complete** | Full ramification argument; full degeneracy argument; the complete `p=3` numeric elimination with every intermediate value shown; the full symmetric-square algebra. |
| E (scripts/reproducibility) | **Complete** (by design, short) | Pointer to `scripts/`, LMFDB-retrieval discipline stated. |

**No appendix is a placeholder.** Every appendix in the compiled PDF contains the actual derivation, not a bracketed description of what should go there — this was completed during the current drafting pass (the manuscript went through two revisions: an initial skeleton with placeholder appendices, then a full appendix write-out, both compiled and checked).

## Computation-only dependencies (per the Phase-1 "computation-free" question, restated for this manuscript)

**None of the manuscript's logically necessary steps depend on a computation that could not, in principle, be checked by hand.** The one genuinely external numerical input is `a_3(f)=-2` (Appendix D), a single cited Hecke eigenvalue used deductively in a two-candidate elimination — not an inductive pattern-match over many primes. Every other numerical claim in the manuscript (`S(3)=-1`, the polynomial identities in Appendices A and C, the discriminant computations) is exact symbolic algebra, independently hand-verifiable, and was cross-checked with computer algebra (sympy) purely as an error-catching aid, never as the source of the claim's truth.

---

## Manuscript Phase 4 update

**Dependency graph addition**: `\mathrm{Triv}(X)` rank 19 →
**Lemma `lem:torsion`** (`\mathrm{MW}_{\mathrm{tors}}=(\Z/2)^2` exactly;
depends on: the perfect-square discriminant computation, **E**; the
torsion-embeds-into-`\bigoplus\Phi_v` fact, **L** — Shioda 1990 +
Miranda–Persson 1989) → **Prop. `prop:picard`** (`|\disc\,NS|=8`, now
fully justified, no remaining gap).

**Attribution addition**: **Theorem `thm:main`** now carries an
explicit dependency edge to **Ahlgren–Ono–Penniston 2002** (external,
independent prior result) — not as a logical dependency of the *proof*
(the manuscript's own proof does not use or cite AOP's Theorem 2.1 as a
step; it is fully self-contained, reaching the same conclusion by a
disjoint argument) but as a **scholarly/priority dependency**: the
manuscript's own proof stands alone, but the *claim of correctness* is
now also cross-validated against, and explicitly subordinated in
priority to, this independent 2002 source. This is a new kind of edge
this document did not previously need to track (Phase 1–3 only tracked
logical/mathematical dependencies) — recorded here for completeness.

**Load-bearing citations, updated list** (removing any one still breaks
the theorem exactly as before, Phase 3's list unchanged in substance):
Shioda–Tate; Shioda's height pairing (now also Miranda–Persson, for the
completed torsion lemma); the singular K3 classification; Livné's
theorem; the CM/Hecke-character Sym² fact (now dual-attributed,
Shimura + Ribet, not Ribet alone). **Non-load-bearing**: AOP 2002 itself
is, in this precise logical-dependency sense, **not** load-bearing for
the manuscript's own proof (which is fully independent) — it is
load-bearing for the manuscript's *honesty and scholarly completeness*,
a different, non-mathematical but equally essential kind of dependency.

**No appendix status change**: all five appendices remain fully
written out (Phase 2), with Appendix C's central polynomial identity
re-verified symbolically once more during this phase's rewrite
(`X_1^3+a_2X_1^2+a_4X_1=-(t-1)^2(t+1)^4`, confirmed via fresh `sympy`
computation, matching the already-published value with no discrepancy).
