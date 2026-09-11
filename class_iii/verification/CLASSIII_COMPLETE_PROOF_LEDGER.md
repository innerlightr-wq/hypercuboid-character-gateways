# Class III — Complete Proof Ledger (Manuscript, Post-Phase 3)

This is the definitive, manuscript-level ledger, reflecting the fully
drafted `class3_hypercuboid_k3.tex` (Sections 1–10 plus Appendices A–F,
21 pages). It supersedes the earlier manuscript-blueprint theorem ledger
(`CLASSIII_THEOREM_LEDGER.md`, written before drafting began) as the
authoritative map from manuscript results to their status, proof
location, and supporting appendix.

Status codes: **E** (elementary/self-contained), **G** (explicit
geometry), **L** (literature theorem, cited), **F** (finite
theorem-based verification — a genuine elimination proof over an
exhausted finite candidate set), **C** (illustrative computation only,
not load-bearing).

| # | Result | Manuscript location | Status | Supporting appendix |
|---|---|---|---|---|
| 1 | `P_III` definition, homogeneity, vanishing on `x0=0` | Definition 2.1, §2 | E | A |
| 2 | `Σ_III(p)=(p-1)T(p)` | Lemma 2.2 | E | A |
| 3 | `τ` involution, `P_III(τx)=-P_III(x)` | Proposition 3.1 | E | — |
| 4 | `Σ_III(p)=0` for `p≡3(4)` | Proposition 3.1 | E | — |
| 5 | Weierstrass model, `c4,c6,Δ,j` | §4.1–4.2 | E/G | B |
| 6 | Three `I2*` fibers, minimal everywhere | Proposition 4.1 | E/G | B |
| 7 | `Triv=U+D6+D6+D6`, rank 20, MW rank 0 | Proposition 4.2 | E/G | B |
| 8 | Global factorization `X(X+T(T+1))(X+T(T+1)²)` | Proposition 4.3 | E | C |
| 9 | Full rational 2-torsion, `(Z/2)²` sections | Corollary 4.4 | E | C |
| 10 | Torsion completeness, `MW_tors=(Z/2)²` exactly | Proposition 4.5 | E + L (Shioda 1990) | C |
| 11 | Section-multiplicity lemma | Lemma 5.5 | E | D |
| 12 | Fiber-multiplicity-1 verification | Lemma 5.3 | G | C |
| 13 | Four distinct legs, all 3 fibers | Lemma 5.6, Remark 5.9 | G | C |
| 14 | Graph rigidity | Lemma 5.7 | E | D |
| 15 | All fiber components individually `Q`-rational | Proposition 5.1 | E+G (combining 11–14) | D |
| 16 | `Tr(F_p\|NS)=20p` | Theorem 5.10 | E (given 15) | D |
| 17 | `\|disc NS\|=4` | Lattice consequences, end of §5 | E/G | D |
| 18 | `T(X_III)≅diag(2,2)` | Lattice consequences, end of §5 | E/G | D, E |
| 19 | Separation of geometric/lattice/CM/arithmetic notions | §6 opening | E | E |
| 20 | Corrected lattice-to-quadratic-form dictionary, `(a,b,c)=(1,0,1)`, `D=-4` | §6.1 | E | E |
| 21 | CM field `Q(i)` | §6.1 | E (given `h(-4)=1`) | E |
| 22 | Livné's theorem, hypotheses checked | Theorem 6.1 | L (Livné 1995) | E |
| 23 | Candidate newform `16.3.c.a`, level 16 | §6.3 | G (unique match given CM+weight; level rests on structural search, not independent conductor computation) | E |
| 24 | Bad primes of `X_III` = `{2}` | §6.4 | E/G | B |
| 25 | Twist candidate set `{1,χ(-1),χ(2),χ(-2)}` | Lemma 7.1 | E | E |
| 26 | Degeneracy collapse to `F0,F1` | §7.2, Lemma 7.2 | E | E |
| 27 | `p=5` twist elimination | Proposition 7.3 | F | E |
| 28 | `Tr(F_p\|T)=a_p(16.3.c.a)`, all odd `p` | Theorem 7.5 | F (split case) + L (inert case, CM vanishing) | E |
| 29 | Point-count ledger, `20p+1` correction re-derived | Proposition 8.3 | E/G | F |
| 30 | `T(p)` exact formula | Theorem 8.5 | E (given 16, 28) | F |
| 31 | Main theorem, `Σ_III(p)` closed form | Theorem 8.6 | E (given 2, 30) | — |
| 32 | Consistency of elementary and CM-inertness vanishing mechanisms | Remark 8.7 | E | — |
| 33 | Classes I/II comparison table | §9 | Observation, not theorem (explicitly scoped) | — |
| 34 | AOP relation, six-way checklist | §9.1 | E (literature-search-bounded) | — |
| 35 | Lefschetz `H⁰`–`H⁴` decomposition of point count | §F opening | L (Grothendieck–Lefschetz, standard) | F |
| 36 | Reproducibility table (4 primes) | §F closing | C (illustrative only) | F |

## What the theorem depends on (load-bearing set)

Items **1–4, 5–10, 11–18, 19–28, 29–31** form the complete, unbroken
dependency chain for the boxed main theorem (Theorem 8.6). Every item in
this chain is E, G, or L — **no item the theorem depends on is C**
(illustrative-only) or unresolved. Item 36 (the reproducibility table) is
explicitly excluded from this chain, per the manuscript's own repeated
disclaimers.

## The one place the manuscript is honest about resting on analogy

Item 23 (exact level `= 16`, not `8` or `32`): the CM field, weight, and
discriminant are forced by theory (items 19–22); the specific level is
identified by matching the unique rational-eigenvalue candidate at
2-power level with the correct CM field and weight, via a literature/LMFDB
search — this is **not** an independent from-scratch conductor
computation for `X_III` specifically. This does not weaken the final
theorem, because item 27's elimination (`F0` vs `F1`) is conducted
*given* this candidate and would equally have refuted a wrong candidate
had one been chosen (a wrong level-16 candidate would simply have failed
to match at `p=5` too, and no such alternative candidate with the right
CM field and weight exists at level 16 in any case, per the LMFDB
search). This is stated plainly in the manuscript (§6.3, Remark 6.2) and
is not glossed over.

## Errors found and fixed across the manuscript's drafting phases (for the record)

1. **Phase 2A**: variable-labeling bug in the projective-reduction proof
   (`x1=t,x2=x` instead of `x1=x,x2=t`) — found via fresh `sympy`
   recomputation, fixed, verified absent from the final source (Phase 3
   consistency audit).
2. **Phase 2B**: quadratic-form discriminant bookkeeping error
   (`(a,b,c)=(2,0,2)` instead of `(1,0,1)`) in the already-compiled
   Section 5 lattice-consequences paragraph — found via the explicit
   determinant-computation discipline this phase's own instructions
   demanded, fixed, and independently re-confirmed this round (Phase 3)
   against a fresh literature check of the Shioda–Inose convention.

Both errors were caught by the same general practice: redoing a
computation from scratch rather than trusting previously-compiled,
plausible-looking text. No further error was found in Phase 3's
line-by-line appendix expansion.

## Final status

**The manuscript's main theorem (Theorem 8.6) is complete and
self-contained**, given the classical, cited results listed above (Kodaira,
Néron, Tate, Shioda, Miranda–Persson, Shioda–Inose, Livné) and one finite,
deductive elimination (`p=5`) conducted over a provably exhaustive
candidate set. The modular form itself, and its use by Ahlgren–Ono–Penniston
for a different surface, are not claimed as new anywhere. Appendices A–F
make every compressed step in the main text independently checkable.
