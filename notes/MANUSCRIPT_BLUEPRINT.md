# Manuscript Blueprint — Hypercuboid Classes I/II

Planning document only. No LaTeX yet.

## Part VI — mathematical starting point (do not begin with K3 surfaces)

**§1 of the paper** should open with the original finite-field problem,
self-contained:

> Fix `n\ge2`. For `x=(x_1,\dots,x_{n-1})\in\mathbb F_p^{n-1}`, set
> `A_i=x_i` (`i<n`), `A_n=-\sum_{i<n}x_i`. For each nonempty
> `J\subseteq\{1,\dots,n-1\}`, let `L_J(x)=\sum_{j\in J}x_j`. For `n=4`
> there are `2^3-1=7` such forms. A choice of `6` of the `7` forms (a
> "class") defines a character sum `\Sigma(p)=\sum_x\chi\bigl(\prod_{J\in S}L_J(x)\bigr)`.
> Up to the natural `S_4`-symmetry permuting `A_1,\dots,A_4`, there are
> exactly three orbits of such 6-subsets — **Classes I, II, III**.

Then state the two proved reductions as the paper's opening lemmas
(Part VII below), and explain in one paragraph, non-technically, that
Class I's evaluation is what forces the appearance of the auxiliary
surface `V` and hence the K3 surface `X` — **the K3 surface is
motivated as the object one is naturally led to when attempting to
evaluate `S(p)`, not introduced as a starting assumption.** This
framing (finite combinatorial origin `\to` forced geometric object)
should be the paper's actual narrative arc; **do not** import the
34-round chronological discovery order, dead ends, or numbering into
the exposition.

## Part VII — minimal lemma/theorem architecture (final)

1. **Lemma 1 (Character-sum reduction).** `\Sigma_I(p)=(p-1)S(p)`.
   Proof: homogeneity/projectivization (Theorem Ledger, self-contained).
2. **Lemma 2 (Point-count realization).** `\#V(\mathbb F_p)=p^2+S(p)`.
   Proof: `1+\chi(0)=1` trick.
3. **Proposition 3 (Elliptic K3 model).** Construction of `X`,
   Weierstrass model, `c_4,c_6,\Delta$, Kodaira fibers `I_2^*,I_2,I_0^*,I_2^*`
   at `t=0,1,-1,\infty`; Euler number `24`. (Appendix A.)
4. **Proposition 4 (Geometric point-count correction).**
   `\#X(\mathbb F_p)=\#V(\mathbb F_p)+19p+1`, including the corrected
   `N_{I_2}(p)=2p+1-\chi(-2)` intersection-point calculation in full.
   (Appendix B.)
5. **Proposition 5 (Picard and transcendental lattices).**
   `\rho=20`, `|\mathrm{disc}\,NS|=8`, `T(X)\cong\mathrm{diag}(2,4)`.
   Height computation in Appendix C; lattice-theoretic argument in the
   main text (Theorem Ledger Part III).
6. **Proposition 6 (Algebraic Frobenius trace).**
   `\mathrm{Tr}(F_p\mid NS)=(19+\chi(-1))p`, with the `\mathbb Q(i)`/
   `\sigma(P_1)=-P_1` mechanism stated in full in the main text (it is
   short and conceptually central — **do not** relegate this one to an
   appendix).
7. **Proposition 7 (Transcendental modular trace).**
   `\mathrm{Tr}(F_p\mid T)=\chi(-1)a_p(f)`, citing Livné's theorem;
   full twist-determination argument in Appendix D, with the logical
   skeleton (existence from Livné `\to` finite candidate set `\to`
   degeneracy `\to` one-prime elimination) stated compactly in the main
   text.
8. **Main Theorem.** `S(p)=\chi(-1)(a_p(f)+p)=-\chi(2)p+\chi(-1)a_p(E)^2`.
9. **Corollary (Classes I and II).** `\Sigma_I(p)`, `\Sigma_{II}(p)`
   closed forms, Gateway-G relation `\Sigma_{II}=\chi(-1)\Sigma_I` proved
   inline (short, self-contained).
10. **Remark/Open Problem (Class III).** State the proved vanishing
    `\Sigma_{III}(p)=0` (`p\equiv3\bmod4`) with a one-paragraph proof
    sketch (the unrelated involution mechanism), and name
    `p\equiv1\bmod4` explicitly as open — do not attempt it, do not
    speculate on its value.

This matches the round's suggested architecture; **no restructuring was
needed** — the mathematics fits this skeleton cleanly, confirmed while
extracting the Theorem Ledger.

## Part VIII — mod-8 corollary table (a corollary, stated after the Main Theorem, not before)

| `p\bmod8` | `\chi(-1)` | `\chi(2)` | `\chi(-2)` | `S(p)` | `\Sigma_I(p)` | `\Sigma_{II}(p)` |
|---|---|---|---|---|---|---|
| `1` | `+1` | `+1` | `+1` | `a_p(E)^2-p` | `(p-1)(a_p(E)^2-p)` | `(p-1)(a_p(E)^2-p)` |
| `3` | `-1` | `-1` | `+1` | `p-a_p(E)^2` | `(p-1)(p-a_p(E)^2)` | `(p-1)(p-a_p(E)^2)`\* |
| `5` | `+1` | `-1` | `-1` | `p` | `p(p-1)` | `p(p-1)` |
| `7` | `-1` | `+1` | `-1` | `-p` | `-p(p-1)` | `p(p-1)` |

(\*at `p\equiv3\bmod8`: `\chi(-1)=\chi(2)=-1`, so
`\Sigma_I=(p-1)(p+(-1)a_p(E)^2)`... **the table must be generated
directly from the boxed formulas at manuscript-writing time, not
hand-copied from this planning note** — this row is included only to
illustrate the table's shape; Phase 2 should regenerate all four rows
by direct substitution into the Main Theorem and Corollary to avoid a
transcription error entering the manuscript from this planning
document.) **Inert rows (`5,7`)**: `a_p(E)=a_p(f)=0`, giving the clean,
transparent `\Sigma_{II}(p)=p(p-1)` in both — this is exactly the
`\chi(-2)=-1` mechanism, displayed, not asserted.

**This table is explicitly a corollary**, stated as such in the paper,
never presented as though it were the main theorem or derived
independently of it.

## Part IX — novelty map

**New results proved here** (candidates, to be stated plainly as the
paper's contribution): (a) the specific hypercuboid character-sum
reduction and its Class I/II/III symmetry classification (original to
this project, `n=4` zero-sector construction); (b) the exact K3
realization of `S(p)` via `V\to X`; (c) the corrected fiberwise
point-count bridge `\#X=\#V+19p+1` (in particular the corrected
`N_{I_2}(p)=2p+1-\chi(-2)` intersection-point mechanism, which is a
genuinely new local computation for this specific surface, not a
citation); (d) the exact closed-form evaluation of Classes I and II via
the CM modular form, including the explicit, proved determination of
the quadratic twist `\chi(-1)` (the representation-theoretic
argument — Livné's theorem existence + ramification + degeneracy +
one-prime elimination — appears to be a novel *application* of standard
techniques to this specific surface, not a new general theorem); (e)
the Gateway-G relation `\Sigma_{II}=\chi(-1)\Sigma_I`; (f) the Class III
symmetry vanishing.

**Classical machinery applied here** (not new): Shioda–Tate, Shioda's
height pairing, the Pjatecki\u{i}-\u{S}apiro–\u{S}afarevi\v{c}/Shioda–Inose
singular-K3 classification, Livné's modularity theorem, Schütt's
twist-classification, Ribet's CM symmetric-square fact.

**Literature check performed this phase**: searched directly for prior
evaluations of `\sum_{x,t}\chi(x(x+1)t(t+1)(x+t))` or equivalent
character sums tied to weight-3 CM forms — **no exact match located**.
**This is not a conclusive novelty clearance**: the search was a
targeted web search, not a systematic survey of the character-sum or
"singular K3 surfaces of small discriminant" literature (e.g. Schütt's
own tables of explicit models by discriminant, which a human
co-author/referee familiar with that catalogue should check directly
against `T(X)\cong\mathrm{diag}(2,4)`, discriminant 8, before any "new"
claim is finalized in print). **Recommendation**: state novelty claims
(especially for item (b), the specific K3 model) provisionally in the
Phase-2 draft, and have a domain expert cross-check against Schütt's
explicit tables of low-discriminant singular K3 models before
submission — do not claim novelty "merely because it was found
independently during exploration," per this phase's explicit
instruction.

## Part X — what NOT to put in the main paper

Omit entirely from the main text (repository-only / at most a one-line
acknowledgment in an appendix if genuinely useful for reproducibility):
failed Gateway-F searches; the killed "rational elliptic surface"
hypothesis (Round 10); the temporary residual `1-\chi(-2)` and its
multi-round hunt (Rounds 27–32) — the paper should present
`\#X=\#V+19p+1` directly, as proved, with the corrected `N_{I_2}(p)`
derivation, and need never mention that an earlier, incorrect version
existed; the 34-round chronological narrative in its entirety; bounded
brute-force pattern searches (Rounds 9, 16, 20's exhaustive
enumerations) — state only their *conclusions* (e.g. "no
`\mathbb Q(t)$-rational height-1 section exists," Round 20) as a fact
with a one-line proof sketch, not as a search log; killed CM-twist
guesses (Round 29's `\chi(-1)a_p(f)+\chi(-2)-1` hypothesis, Round 31's
Shioda–Inose-degree hypothesis); intermediate bookkeeping errors
(Round 22/28's earlier `N_{I_2}(p)=2p` claim) — the paper states the
**correct** formula with its **correct** proof and never mentions the
error existed. **Preserve** (in Appendix E / repository, not main text):
the verification scripts themselves, since they provide genuine,
citable reproducibility value.

## Part XII — see `NOTATION.md` (separate file, per instruction)

## Part XIII — claim-strength audit

Checked the blueprint's own language for `new`, `first`, `unique`,
`exact`, `for all primes`, `equivalent`, `follows immediately`,
`proved`:
- **"unique"**: used correctly only where class-number-one forces
  literal uniqueness (the discriminant-8 lattice; the CM newform up to
  twist) — never used loosely for "the only approach we tried."
- **"for all primes"**: **every instance in this blueprint and the
  Theorem Ledger is "for every odd prime"** — `p=2` is consistently
  excluded (verified explicitly in Theorem Ledger Part IV: `X`'s bad
  reduction is only at `p=2`). Phase 2 must carry this qualifier on
  **every** boxed formula, not just the first occurrence in a section.
- **"exact"**: used only for identities verified to hold with no error
  term (all boxed formulas) — never for the mod-8 table's illustrative
  row above, which is explicitly marked as needing regeneration.
- **"follows immediately"**: **not used anywhere in the Theorem Ledger**
  — every step has an explicit justification, even short ones (e.g. the
  Gateway-G relabeling); Phase 2 should maintain this discipline and
  avoid the phrase entirely, replacing it with the actual one-line
  reason.
- **"new"/"first"**: reserved for Part IX's candidate list, all
  explicitly flagged as provisional pending the recommended expert
  literature cross-check — **not** asserted as settled fact anywhere
  else in this blueprint.
- **"proved"**: reserved exclusively for items so marked in the Theorem
  Ledger's status column; the two Round-34 caveats are now also
  PROVED — SELF-CONTAINED (Manuscript Phase 1 Part II), so no
  remaining item needed for the main theorem carries a weaker label.
