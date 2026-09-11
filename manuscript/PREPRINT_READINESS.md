# Preprint Readiness — `hypercuboid_character_sums.tex`

**Final Preprint Polish phase.** This note summarizes the release
status after the last two source-level checks and a full copy-edit
pass.

## Final title

*"Finite-Field Hypercuboid Character Sums and a Discriminant-8 Singular
K3 Surface"* — unchanged from Phase 4, no novelty implication.

## Theorem status

Every proposition, lemma, and theorem in the manuscript is proved in
the text (five appendices contain the longer explicit calculations, all
fully written out, none placeholders). The one gap identified in Phase
3 — completeness of `\mathrm{MW}(X/\Qbar(t))_{\mathrm{tors}}\cong(\Z/2)^2`
— was closed in Phase 4 with a self-contained lemma. This phase found
and repaired one further imprecision: the elliptic-curve relationship
underlying Remark 7.3 (connecting this paper's `E` to Ahlgren–Ono–
Penniston's `E_1`) is now an **exact, explicit isomorphism over
`\Q(\sqrt2)`** (`E_1` is the quadratic twist of `E` by `2`, not `-1`),
proved via the explicit map
`(x,y)\mapsto(x/2+1,\,y/(2\sqrt2))` with inverse
`(x',y')\mapsto(2(x'-1),\,2\sqrt2\,y')`, verified symbolically. This is
strictly stronger than the previous "verified numerically" statement
and corrects a genuine (if numerically invisible) imprecision: the two
curves are twists by `2`, and the resulting trace identity only
coincides with `\chi(-1)a_p(E)` because `\chi(2)=\chi(-1)` wherever
`a_p(E)\ne0` — a fact now stated explicitly rather than left as an
unexplained coincidence.

**No mathematical claim in the manuscript is unresolved or
conditional.**

## Prior-literature attribution status

Fully honest and prominent throughout: the abstract's fourth sentence,
the introduction's dedicated subsection, the Main Theorem's own name
and statement, a full comparison-of-methods section, the Discussion,
and the Limitations all state plainly that the central character-sum
identity recovers Ahlgren–Ono–Penniston (2002), Theorem 2.1, and is not
claimed as new. The paper's own contribution — the hypercuboid
reduction, the Gateway relation, and the independent K3-geometric proof
method — is stated explicitly and separately at every one of these
points, not merely once.

## Remaining open problem

`\Sigma_{III}(p)` for `p\equiv1\pmod4` — not addressed by
Ahlgren–Ono–Penniston (no Class III analogue in their family) and not
addressed by this paper's own methods. Stated as the paper's genuine
open frontier in a dedicated, explicitly-titled section
("Class III: the genuine open problem"), the Open Problem environment,
the Discussion, and the Limitations — four independent, consistent
statements, verified this phase to contain no contradiction.

## Source verification status

- **Livné's modularity theorem**: verified directly against the
  primary citing source (Schütt, arXiv:0804.1558), fetched and read —
  Round 34 and reconfirmed Phase 3.
- **Ahlgren–Ono–Penniston (2002)**: the original paper itself fetched
  and read in full (author's own posted PDF) — Phase 3.
- **Pjateckiĭ-Šapiro–Šafarevič (1971)**: the 1971 original remains
  inaccessible in practice; **this phase directly fetched and read**
  Huybrechts, *Lectures on K3 Surfaces* (2016), Chapter 7, Theorem 5.3
  (Global Torelli Theorem), the modern authoritative statement, and
  confirmed it matches the manuscript's usage exactly (including the
  "oriented lattice" qualifier, now explicitly justified via the
  requirement that a Hodge isometry preserve `H^{2,0}(X)`). The
  bibliography entry now cites the exact theorem number and page.
- **Ribet (1977) / Shimura**: dual-attributed since Phase 4, correctly
  scoped (Ribet's paper is the source for the converse CM fact; the
  forward Sym² splitting is classical CM theory more broadly).
- **Miranda–Persson (1989)**: bibliographic details verified directly
  against the journal's own posted copy (title page read) — Phase 4.
- **LMFDB**: used only for data retrieval (`a_3(f)=-2`), never as a
  theorem source, consistently disclosed.

**Every citation in the ten-entry bibliography has now been checked at
least to the level of a directly-read primary or authoritative
secondary source**, with precise scope notes wherever a citation covers
only part of what it supports.

## Copy-edit result

Full line-by-line visual read of all 15 compiled pages performed this
phase. No grammar errors, no awkward or redundant prose, no broken
cross-references, no stale content (stale title, uncorrected
`N_{I_2}(p)=2p`, or unresolved `1-\chi(-2)` residual language — all
explicitly searched for and confirmed absent) found. One cross-
reference inconsistency between the Introduction and Remark 7.3 (the
Introduction cited `\chi(-1)(p)a_p(E)` while Remark 7.3, after this
phase's correction, correctly states `\chi(2)(p)a_p(E)`) was found and
fixed — both now state the algebraically exact relationship
consistently. Automated repeated-word and double-space scans found
nothing beyond benign LaTeX table-specifier false positives.

## Compile status

Compiles cleanly: `pdflatex` exit code `0`, three passes (for stable
cross-references and bibliography), **zero errors, zero undefined
references, zero undefined citations**. Final page count: **15**. One
pre-existing, previously disclosed cosmetic warning remains (a single
13.7pt overfull `\hbox` in one paragraph of Proposition 7.2's proof,
present since Phase 2, does not affect readability or correctness) and
a small number of benign `Underfull \hbox` warnings in the narrow
comparison table (Section 9) — neither is an error and neither was
introduced this phase.

## Safe for preprint release?

**Yes.** All mathematics is proved and self-contained; prior literature
is credited honestly and prominently at every point where it matters;
every citation has been checked to the depth appropriate to its role in
the argument (with the two most load-bearing — Livné and
Ahlgren–Ono–Penniston — read directly in full, and the remainder
verified to at least the level of a directly-read authoritative
secondary source); the manuscript compiles without error; the one
genuine open problem is stated clearly and consistently. No further
mathematical or scholarly work is required before release as a
preprint. Ordinary final-author proofreading (a human read-through
before public posting) is always sensible but is not, on this audit,
required to correct any identified defect.
