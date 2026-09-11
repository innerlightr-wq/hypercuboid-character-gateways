# Class III Sequel — Manuscript Blueprint

**Scope discipline.** Work confined to `explorations/class_iii/`. The
existing Classes I/II manuscript was not modified. Nothing committed,
nothing pushed. This phase does not search for new mathematics — it
organizes the already-audited (`CLASSIII-P5A`) result into a publication
architecture.

---

## Part I — The final theorem, frozen (not strengthened)

**Definitions.**
```
P_III(x0,x1,x2) = x0 x1 x2 (x0+x2)(x1+x2)(x0+x1+x2)
Σ_III(p) = Σ_{x∈F_p^3} χ(P_III(x))
T(p)     = Σ_{x,t∈F_p} χ(x t(t+1)(x+t)(x+t+1))
f_16     = LMFDB newform 16.3.c.a = η^6(4z)
```

**Reduction.** `Σ_III(p) = (p-1) T(p)`, for every odd prime `p`.

**Exact prime domain.** All odd primes `p` (`p=2` is the only bad prime;
not addressed by the theorem, correctly).

**Theorem (Class III evaluation).**
```
T(p) = a_p(f_16)                if p ≡ 1 (mod 4)
T(p) = 0                         if p ≡ 3 (mod 4)

Σ_III(p) = (p-1)·a_p(f_16)       if p ≡ 1 (mod 4)
Σ_III(p) = 0                     if p ≡ 3 (mod 4)
```

This is exactly the statement audited and passed in Phase 5 (verdict
`CLASSIII-P5A`). **Nothing here is strengthened beyond that audit** — in
particular, the split-representation form `a_p=2(x²-4y²)` for `p=x²+4y²`
remains explicitly excluded (its sign convention was never independently
verified) and must **not** appear in the paper's main theorem statement;
if mentioned at all, it belongs in a clearly-flagged remark, not the
boxed result.

---

## Part II — Minimal proof chain

See `CLASSIII_THEOREM_LEDGER.md` (this directory) for the full 13-step
chain with per-step proof method and target section. Summary of the
architecture it implies: §1 (reduction) → §2 (mod-4 vanishing) → §3 (K3
model) → §4 (torsion + graph rigidity, the paper's technical core) → §5
(lattice) → §6 (modularity + twist) → §7 (final evaluation) → §8
(comparison) → §9 (discussion/literature).

---

## Part III — The sequel's real contribution, audited

**Known/classical machinery** (cite, do not present as original):
- Shioda–Tate formula; Kodaira's fiber classification; the `I_n^*` affine-
  `D6` dual graph structure; Livné's singular-K3 modularity theorem; the
  standard twist-elimination technique (already used, and correctly not
  claimed as novel, in the existing Classes I/II manuscript); the
  character-sum-to-curve-count dictionary; binary-quadratic-form reduction
  theory (`h(-4)=1`).

**New, hypercuboid-specific results** (candidates for the paper's
contribution statement, individually assessed):

| Candidate contribution | Assessment |
|---|---|
| Class III's reduction `Σ_III(p)=(p-1)T(p)` and the mod-4 involution | Genuinely specific to the hypercuboid construction (a different `S_4`-orbit member from Classes I/II) — real, but modest in weight; the *technique* (projectivization, involution) is the same one already used for Classes I/II. |
| The distinct K3 model `X_III` (Weierstrass equation, `3×I2*` fibers) | Real and specific — this exact surface was not located in the literature search (§9 caveat applies). Moderate-weight contribution: a new example, not a new phenomenon. |
| **Graph-rigidity proof of `NS`-rationality via full rational 2-torsion** | **The strongest candidate.** Proves a structural fact (all fiber components individually `Q`-rational) without explicit fiber resolution, by an argument (torsion sections exhaust the leg slots + graph rigidity) not used, as far as searched, in the AOP line of argument or in the existing Classes I/II manuscript's own (more computational) route. This should be presented as the paper's central methodological contribution. |
| The Class III modular evaluation itself (`T(p)=a_p(16.3.c.a)`) | Specific numerical/arithmetic content not located elsewhere — moderate weight, parallels Classes I/II's own relationship to AOP closely (same *kind* of contribution, at a different discriminant). |
| Comparison with Classes I/II | Genuine observation about this project's own two branches — real, but explicitly **not** a general theorem (see Part IX below); frame as an interpretive remark, not a result. |
| Dual CM-sector interpretation (`Q(√-2)` vs `Q(i)` from one construction) | Same caveat as above — an observation about two examples, stated as such. |

**Explicit non-claim, per instruction**: novelty is **not** claimed merely
because the exact sum was not found in searches. Every "NOT FOUND" result
from the literature audits is reported in `CLASSIII_LITERATURE_POSITIONING.md`
as a search-scope limitation, not as evidence of originality.

---

## Part IV — Literature positioning

See `CLASSIII_LITERATURE_POSITIONING.md` for the full treatment, including
the required governing sentence for the introduction and the precise
extremal-K3-catalogue phrasing (deliberately hedged: "very likely
catalogued, not confirmed against tables we had access to").

---

## Part V — Title options

Five candidates (conservative, matching the existing manuscript's
register — `Finite-Field Hypercuboid Character Sums and a Discriminant-8
Singular K3 Surface`):

1. **Class III Hypercuboid Character Sums and a Discriminant-4 Singular K3
   Surface**
2. A Gaussian-CM Branch of Finite-Field Hypercuboid Character Sums
3. Class III Hypercuboid Character Sums via a Discriminant-4 Singular K3
   Surface
4. Rational Torsion and Néron–Severi Rigidity for a Class III Hypercuboid
   K3 Surface
5. Finite-Field Hypercuboid Character Sums and a CM-by-`Q(i)` Singular K3
   Surface

**Selected: Option 1 — "Class III Hypercuboid Character Sums and a
Discriminant-4 Singular K3 Surface."**

Rationale: it mirrors the existing manuscript's exact title pattern
(`[Class] Hypercuboid Character Sums and a Discriminant-[D] Singular K3
Surface`) as closely as possible, signaling to any reader familiar with
the first paper that this is its direct companion, not an unrelated work
— while stating the discriminant (a verifiable, precise fact) rather than
the CM field (Option 5) or a more editorial framing (Option 2, 4). Option
3's "via" phrasing is acceptable but slightly weaker than "and," which
matches the original title's grammar exactly. Option 4 foregrounds the
paper's real technical contribution but is a less natural title for a
reader encountering the two papers as a pair.

**Confirmed avoided**: no "breakthrough," "first," "new modular form," or
"solution of perfect hypercuboid" language anywhere in the selected title
or any candidate.

---

## Part VI — Paper architecture

```
Title: Class III Hypercuboid Character Sums and a
       Discriminant-4 Singular K3 Surface

Abstract

Introduction
  - the parent hypercuboid construction (cited, not redeveloped)
  - Class III's place among the classification (contrasted with I/II)
  - governing literature-positioning sentence (§IV above)
  - statement of the main theorem
  - summary of the proof architecture and its central new technique

1. Class III and its reduction
   - P_III, Σ_III(p), projectivization to T(p)

2. Elementary mod-4 vanishing
   - the involution, Σ_III(p)=0 for p≡3(4)

3. Elliptic K3 model
   - V_III, Weierstrass model, c4/c6/Δ, three I2* fibers, ρ=20

4. Rational 2-torsion and Néron–Severi rationality
   [the paper's technical core -- see Part VII below]
   - full 2-torsion over Q(T)
   - torsion completeness ((Z/2)^2 exactly)
   - the graph-rigidity argument, presented in full, in the main text

5. Transcendental lattice and CM
   - |disc NS|=4, T(X_III)=diag(2,2), CM field Q(i)

6. Modularity and twist
   - Livne's theorem, candidate set, degeneracy collapse, p=5 elimination

7. Exact evaluation
   - the final theorem, both cases, derivation via Lefschetz + ledger

8. Comparison with Classes I/II
   - the compact table (Part IX below), framed as interpretation only

9. Discussion
   - literature positioning recap, open catalogue-matching question,
     scope of the search, one paragraph on why this stands as a
     sequel rather than a manuscript revision

Appendices
   A. Weierstrass invariants
   B. Kodaira fiber-type verification
   C. Torsion completeness (full elementary argument)
   D. Graph automorphism verification (mathematical + computational)
   E. Modular twist discrimination (full p=5 derivation)
   F. Reproducibility scripts (pointers)

Bibliography
```

This follows the user's suggested structure exactly, with §4 marked as
the technical core per the explicit instruction to make graph rigidity
central rather than buried.

---

## Part VII — Graph-rigidity argument, main-text presentation plan

To appear in §4 of the paper, in full, as the section's centerpiece (not
summarized-and-deferred to an appendix). Planned presentation order,
matching the logical order that survived adversarial audit
(`PHASE5_CLASSIII_AUDIT.md` Part VII):

1. State the affine-`D6` dual graph abstractly (4 legs, 3 spine, cited to
   Kodaira/Néron/Tate) — one short paragraph, one figure (a simple graph
   diagram: two forks connected by a 3-node path).
2. Prove, in one paragraph, that any section meets exactly one component
   at multiplicity 1 (elementary, `section·fiber=1` argument) — this is
   short enough to include in full rather than cite.
3. Exhibit the four sections `O,P1,P2,P3` and their exact specialization
   coordinates at one representative fiber (`T=0`), with the explicit
   rational-function computations shown (not just asserted) — this is
   where the paper should show its work, since it is the load-bearing
   numerical content.
4. State (and, briefly, justify) that each specialization lands at a
   point where the local fiber equation is *reduced* — i.e. the
   fiber-multiplicity-1 check that Phase 5's audit added. This is short
   (one lemma, one computation) but should be **included explicitly**,
   since its earlier omission was the one real gap an audit found — its
   presence is a mark of the paper's care, not filler.
5. State the four-distinct-legs conclusion, then the graph-rigidity
   lemma (unique-neighbor argument) in full, with the automorphism-group
   computation presented as a short, self-contained combinatorial fact
   (order-8 group, trivial stabilizer of the 4-leg marking) — include the
   explicit automorphism list as a small table or figure, since it is
   compact and makes the "exhaustive, not just asserted" nature of the
   claim visible to the reader without requiring them to run code.
6. State the conclusion (`Tr(F_p|NS)=20p`) and note explicitly, in one
   sentence, that this route required no fiber resolution beyond
   identifying the four leg-landing points — the sentence that makes the
   paper's methodological contribution legible to a reader skimming for
   "what's new here."
7. Repeat (briefly — a short remark, not a full repetition) that the
   identical argument applies at `T=-1` and `T=∞`, with a one-line pointer
   to Appendix D for the explicit coordinate data at those two fibers
   (keeping the main text focused on one fully-worked example).

---

## Part VIII — Status of the hand blow-up work

**Decision: nowhere in the paper.** See `CLASSIII_APPENDIX_PLAN.md` for
full reasoning. It remains, correctly, repository-only research history.

---

## Part IX — Comparison with Classes I/II

| Feature | Classes I/II | Class III |
|---|---|---|
| `disc T(X)` | 8 | 4 |
| CM field | `Q(√-2)` | `Q(i)` |
| Modular form | level 8, weight 3 | level 16, weight 3 |
| Bad fibers | 4 total | 3 total (`3×I2*`) |
| MW behavior | rank 1 over a quadratic extension | rank 0 |
| `NS`-rationality mechanism | explicit extra section / twist isomorphism computation | full rational 2-torsion + graph rigidity |
| Twist | `χ(2)`-twisted | untwisted |

**Use only as interpretation, per instruction.** The paper's §8 should
frame this table with language such as: *"the present two examples
exhibit two structurally distinct CM sectors arising from the same
underlying hypercuboid construction, obtained by two different
Néron–Severi-rationality mechanisms"* — and must **not** claim, imply, or
gesture toward a general theorem that the hypercuboid classes always
select distinct CM sectors, or that the mechanism-type (extra-section vs.
torsion-rigidity) correlates with anything beyond these two examples. This
mirrors Round 3/4's own explicit discipline on this exact point and should
be enforced identically in the paper's prose.

---

## Part X — Computation independence

The three indispensable, exactly-sourced computational facts (unchanged
from Phase 5 Part XX, restated here for the manuscript record):

1. `a_5(16.3.c.a) = -6` (LMFDB database lookup, publicly verifiable).
2. `T(5) = -6` (one finite sum over 25 pairs `(x,t)∈F_5²`, exact).
3. `χ(2)(5) = -1` (elementary: `5 ≢ 1 mod 8`).

**No theorem in the paper depends on a prime sweep or pattern-fit.** The
paper's §6 (twist elimination) should state this explicitly, exactly as
Phase 5 Part XX did: the candidate set is proved finite and exhaustive
*before* any numerical value is consulted, and a single differing
coefficient then suffices deductively. Any multi-prime tables appearing in
the paper (if included at all, e.g. in an appendix for reader
reassurance) must be labeled as *illustrative/regression*, never as part
of the proof.

---

## Part XI — Appendix plan

See `CLASSIII_APPENDIX_PLAN.md` (this directory) for the full plan
(Appendices A–F, plus the explicit decision to exclude the hand blow-up
work entirely).

---

## Final Report

1. **Exact theorem**: Part I above — frozen at exactly the Phase 5 audited
   result, not strengthened.
2. **Minimal proof chain**: 13 steps, `CLASSIII_THEOREM_LEDGER.md`
   (manuscript version, discovery history removed).
3. **Main new contribution**: the graph-rigidity proof of
   `NS`-rationality via full rational 2-torsion (Part III table) —
   identified as the strongest, most defensible novelty claim.
4. **Literature overlap**: same modular form as AOP's `λ=8` surface and
   the quartic Fermat K3 (different surfaces); exact sum/model not found
   elsewhere; extremal-K3 catalogue membership likely but unconfirmed
   (`CLASSIII_LITERATURE_POSITIONING.md`).
5. **Selected title**: "Class III Hypercuboid Character Sums and a
   Discriminant-4 Singular K3 Surface" (Part V).
6. **Paper architecture**: 9 sections + 6 appendices (Part VI).
7. **Graph-rigidity presentation**: main text, §4, in full, 7-step
   presentation order including the fiber-multiplicity check the audit
   added (Part VII).
8. **Classes I/II comparison**: compact 7-row table, framed strictly as
   interpretation of two examples, not a general theorem (Part IX).
9. **Computation independence**: 3 indispensable facts, stated explicitly
   in §6, no proof step depends on a numerical pattern (Part X).
10. **Appendix plan**: A (Weierstrass), B (Kodaira type), C (torsion
    completeness), D (graph automorphism), E (twist discrimination),
    F (reproducibility) — hand blow-up work excluded entirely
    (`CLASSIII_APPENDIX_PLAN.md`).
11. **Remaining novelty uncertainty**: whether the exact `X_III` model
    already appears, uncredited to this project, in Schütt's or Shioda's
    complete tables — genuinely unresolved (access limitation, not a
    mathematical question), and the paper's §9 must say so plainly.
12. **Whether full manuscript drafting is safe**: **Yes.** The theorem is
    audited and stable (`CLASSIII-P5A`); the architecture, title,
    notation, literature framing, and appendix disposition are all now
    fixed; nothing in this blueprint phase surfaced a reason to delay.
13. **Single highest-value next action**: begin LaTeX drafting of §§1–4
    (the reduction, involution, K3 model, and — as the section requiring
    the most care in exposition — the graph-rigidity argument), using
    this blueprint's section-by-section plan and the existing Classes
    I/II manuscript's LaTeX source as a formatting/style template.

### Verdict: **CLASSIII-MP1A**

Blueprint complete; safe to draft the sequel manuscript. The theorem
statement is frozen at exactly its audited strength, the proof chain is
minimized and discovery history removed, the paper's real contribution is
identified and honestly weighted (graph rigidity as the centerpiece, the
comparison table as interpretation only), literature positioning is
precise and conservative, a title is selected with stated rationale, and
the appendix plan explicitly and deliberately excludes the superseded
hand blow-up work. No blueprint decision requires revisiting the
mathematics itself.

---

## THE THREE MOST IMPORTANT THINGS WE LEARNED

1. **Turning a research log into a paper is its own kind of editing work,
   separate from doing the math** — deciding what to cut (round-by-round
   self-corrections, an abandoned computational approach, exploratory
   dead ends) matters as much as deciding what to keep, and doing this
   deliberately, with reasons written down, produces a cleaner paper than
   just trimming the research notes down.

2. **The most defensible claim of "this is new" is usually about *how*
   something was shown, not just *that* it was shown** — the paper's
   strongest contribution isn't "we found a new K3 surface" (a
   overstatable claim, hard to fully verify against literature) but "we
   proved a structural fact about it using a technique that doesn't
   appear to have been used this way before," which is both true and
   checkable.

3. **A result that survived an adversarial audit doesn't need to be
   re-argued from scratch when writing it up — it needs to be
   re-organized** — this phase deliberately did no new mathematics,
   because the previous phase's whole point was to settle whether the
   mathematics was solid; treating that as settled and moving to
   architecture is what makes a multi-phase project actually converge
   instead of re-litigating itself indefinitely.
