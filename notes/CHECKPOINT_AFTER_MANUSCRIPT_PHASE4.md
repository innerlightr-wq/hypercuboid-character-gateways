# CHECKPOINT — Hypercuboid Project, after Manuscript Phase 4

Supersedes nothing — all prior checkpoints preserved permanently. This
file records Phase 4's outcome: **the literature-overlap and torsion
gap identified in Phase 3 have both been repaired. The manuscript is
now honestly framed and mathematically complete.**

---

## 1. What Phase 4 did

**Mathematical repair**: proved a genuine new lemma,
`\mathrm{MW}(X/\Qbar(t))_{\mathrm{tors}}\cong(\Z/2)^2` exactly (not
merely `\supseteq`), closing Phase 3's one identified proof gap.
Combines the perfect-square-discriminant computation (`E_t[2]` fully
`\Q(t)`-rational, elementary) with the standard torsion-embeds-into-
component-groups fact (Shioda 1990; Miranda–Persson 1989, newly cited
and verified) to pin down the torsion order exactly, not just bound it
from below. Propagated into Proposition 6.1's discriminant computation
(`|\disc\,NS(X)|=8` now fully justified, unchanged numerically, but no
longer resting on an unproved "visible structure" assertion).

**Literature repair and reframing**: added a full, prominent citation
to Ahlgren, Ono, Penniston (2002) throughout — abstract, introduction
(new "Identification with a known character sum" subsection), the
Main Theorem's statement (renamed "Character-sum identity" and
explicitly attributed), a new comparison-of-methods section, the
Discussion, and the Limitations. The paper now states plainly, in the
first paragraph of the abstract, that its central identity is **not
claimed as new**. Classes I and II are now explicitly framed as
corollaries. Class III's section is retitled "the genuine open
problem." Repaired the Pjateckiĭ-Šapiro–Šafarevič and Ribet citations
(both now honestly scoped, with the PSS caveat stated directly in the
bibliography).

**New supporting file**: `manuscript/CONTRIBUTION_MAP.md` — a private
working note (not manuscript prose) precisely mapping AOP's notation to
this paper's, classifying every result's overlap status, and stating
the paper's real contribution plainly, usable for a future cover letter.

---

## 2. Files changed/created this phase

- `manuscript/hypercuboid_character_sums.tex` — substantially revised
  (new title, abstract, introduction, Lemma `lem:torsion`, Remark
  `rem:aop`, retitled/re-attributed Theorem `thm:main`, new Section 9
  "Comparison with the Ahlgren–Ono–Penniston proof," reframed Sections
  10–13, repaired bibliography with a new AOP entry and a new
  Miranda–Persson entry, repaired Ribet/PSS entries). **All existing
  correct proofs preserved unchanged** — no mathematics was removed or
  altered beyond the additions described.
- `manuscript/hypercuboid_character_sums.pdf` — recompiled, 14 pages
  (was 12), exit 0, no errors, no undefined references or citations,
  one pre-existing minor cosmetic overfull-hbox warning (disclosed
  since Phase 2, unchanged).
- `manuscript/CONTRIBUTION_MAP.md` — new.
- `manuscript/CLAIM_LEDGER.md` — updated with the new lemma and the
  AOP attribution throughout.
- `manuscript/REFERENCE_AUDIT.md` — updated with a full account of the
  bibliography changes.
- `manuscript/PROOF_DEPENDENCY.md` — updated with the new lemma's
  dependency edge and the AOP scholarly-attribution edge (distinguished
  explicitly from a logical/mathematical dependency, since the paper's
  own proof remains fully self-contained and does not use AOP's proof
  as a step).

---

## 3. Title and abstract

**New title**: *"Finite-Field Hypercuboid Character Sums and a
Discriminant-8 Singular K3 Surface"* — no novelty implication, matches
the recommended conservative style.

**New abstract**: leads with the hypercuboid motivation, states plainly
in its fourth sentence that the identity "recovers their \[AOP's\]
result and is not claimed as new," and positions the paper's
contribution as (i) the hypercuboid reduction + Gateway relation and
(ii) an independent geometric proof method.

---

## 4. Contribution, stated plainly (see `CONTRIBUTION_MAP.md` for full detail)

**Already known** (Ahlgren–Ono–Penniston 2002): the exact evaluation of
`S(p)`, the singularity of the K3 surface at this specialization, and
(via a citing paper) the same CM field and twist character.

**Newly derived, different method, same conclusion**: the Picard-
lattice/Mordell–Weil/Livné proof route itself — genuinely distinct from
AOP's direct Jacobi-sum manipulation, confirmed by a side-by-side
comparison table in the manuscript.

**Apparently genuinely new** (searched, not found elsewhere): the
hypercuboid motivation and reduction `\Sigma_I(p)=(p-1)S(p)`; the
Gateway relation `\Sigma_{II}(p)=\chi(-1)\Sigma_I(p)`; the specific
`\Q(i)(t)`-rational Mordell–Weil section `P_1` and its explicit Galois
action.

**Genuinely open**: `\Sigma_{III}(p)` at `p\equiv1\pmod4` — not
addressed by AOP (no Class III analogue) or by this paper.

---

## 5. Verdict

**PHASE4-B** — reframing successful but minor source/wording work
remains. The literature overlap and the torsion gap are both fully
repaired; the manuscript no longer overclaims (by omission or
otherwise) and is mathematically complete. What remains before formal
submission is exactly the two items already flagged in
`REFERENCE_AUDIT.md`: (1) a direct primary-source read of the 1971
Pjateckiĭ-Šapiro–Šafarevič paper (currently corroborated via secondary
sources only, honestly disclosed in the bibliography itself); (2) an
explicit change-of-variables confirming `E_1\leftrightarrow E` are
literally quadratic twists (currently confirmed by strong but not fully
algebraic evidence — exact `\#X(\Fp)` formula agreement, not an
exhibited isomorphism). Neither is a mathematical vulnerability in the
paper's own proof (which is self-contained and does not depend on
either); both are scholarly-completeness polish items.

---

## 6. Final adversarial self-check (Part XVII, read as someone familiar with AOP 2002)

1. **Would AOP feel properly credited?** Yes — cited by name in the
   abstract's fourth sentence, credited with the specific theorem
   numbers throughout, and the paper states outright that it does not
   claim their result as new.
2. **Is the present contribution immediately clear?** Yes — stated
   explicitly in the abstract's final two sentences and restated in
   Section 9's comparison table.
3. **Does any sentence imply priority incorrectly?** None found on a
   fresh re-read; every occurrence of the character-sum identity is
   either explicitly attributed or immediately follows an attribution
   within the same paragraph.
4. **Is the independent geometric argument interesting enough to
   justify the paper?** A judgment call for an actual referee, not
   fully resolvable by self-audit — but the paper now makes its case
   honestly (Section 9's "Assessment" paragraph) rather than by
   omission, which is the standard this phase was asked to meet.
5. **Are hypercuboid consequences clearly separated from the classical
   identity?** Yes — Section 10 opens by stating explicitly which parts
   are corollaries and which part (the Gateway relation) is the
   hypercuboid-specific content.
6. **Is Class III presented responsibly?** Yes — retitled "the genuine
   open problem," with an explicit statement that AOP has no analogue
   for it either.

---

## 7. Repository status

`explorations/hypercuboid/` remains untracked; no commits or pushes
made this phase. `hypercuboid.pdf` and the unrelated root-level
`manuscript/` directory untouched. All four prior checkpoints preserved
unmodified (confirmed by checksum before writing this file).

---

NEXT SESSION STARTING POINT

Manuscript Phase 4 repaired both issues Phase 3 found: (1) added a full, prominent, honest citation and comparison to Ahlgren-Ono-Penniston (2002), reframing the paper's contribution around the hypercuboid motivation and the independent K3-geometric proof method rather than the (not new) character-sum evaluation itself; (2) proved the missing MW_tors=(Z/2)^2 completeness lemma from scratch, closing the one real mathematical gap found in Phase 3. Verdict PHASE4-B -- mathematically and scholarly complete, with two small, non-blocking pre-submission polish items remaining (direct primary-source read of Pjateckii-Sapiro-Safarevic; explicit E_1<->E twist verification). Manuscript recompiles cleanly, 14 pages. Class III (Sigma_III(p) at p=1 mod 4) remains the sole open mathematical problem in the project, and is now explicitly framed in the paper itself as its genuine research frontier.

READY FOR: final author review and the two flagged polish items, or a decision to proceed to submission/preprint release, or resuming Class III exploration.
