# Reference Audit — `hypercuboid_character_sums.tex`

Every citation in the bibliography, verified.

| # | Citation | Verified how | Used for | Primary or secondary source? |
|---|---|---|---|---|
| [1] | Shioda, "On elliptic modular surfaces," J. Math. Soc. Japan 24 (1972), 20–59 | Bibliographic citation confirmed by web search (title, journal, volume, pages, year all cross-checked) | Shioda–Tate rank formula | Primary |
| [2] | Shioda, "On the Mordell–Weil lattices," Comment. Math. Univ. St. Paul. 39 (1990), no.2, 211–240 | Bibliographic citation confirmed by web search | Height pairing, local-contribution table, discriminant formula | Primary |
| [3] | Pjateckiĭ-Šapiro, Šafarevič, "A Torelli theorem for algebraic surfaces of type K3," Izv. Akad. Nauk SSSR Ser. Mat. 35 (1971), 530–572 | Citation confirmed via its appearance (as reference "[16]") in the fetched Schütt paper (arXiv:0804.1558), cross-checked against general knowledge of the K3 Torelli theorem literature | Torelli theorem input to the singular-K3 classification | Primary (cited secondhand via Schütt; **not independently fetched and read this phase** — flagged below) |
| [4] | Shioda, Inose, "On singular K3 surfaces," in Complex Analysis and Algebraic Geometry, Iwanami Shoten (1977), 119–136 | Bibliographic citation confirmed by web search; its content (the Shioda–Inose diagram, both maps degree 2) independently confirmed by directly fetching and reading Schütt's arXiv:0804.1558, which reproduces the diagram explicitly | Singular K3 `\leftrightarrow` rank-2 lattice bijection; degree-2 correspondence (background only) | Cited via Schütt; diagram content independently confirmed against a source that itself reproduces it faithfully |
| [5] | Livné, "Motivic orthogonal two-dimensional representations of Gal(Q̄/Q)," Israel J. Math. 92 (1995), 149–156 | Bibliographic citation confirmed by web search; **its precise statement (Theorem 4) was fetched and read directly from Schütt's arXiv:0804.1558**, which states and attributes it explicitly — not relied on from memory or an AI paraphrase | Modularity of `T(X)` up to twist — the single most load-bearing citation in the paper | Cited secondhand (Schütt's restatement), but that restatement was itself fetched and read directly, satisfying the "not an AI summary" discipline for the *statement actually used* |
| [6] | Schütt, "K3 surfaces with Picard rank 20," arXiv:0804.1558; and "CM newforms with rational coefficients," Ramanujan J. (2008/09), arXiv:math/0511228 | **Fetched and read directly** (first six pages, including Theorems 1–6, the Shioda–Inose diagram, and Example 5's Hecke-character construction) | Twist-classification theorem, source of the verified Livné statement | Primary — directly fetched, not summarized secondhand |
| [7] | Ribet, "Galois representations attached to eigenforms with nebentypus," Lecture Notes in Math. 601, Springer (1977), 17–52 | Bibliographic citation confirmed by web search | CM symmetric-square decomposition shape | Primary (cited, not independently fetched and read this phase — flagged below) |
| [8] | LMFDB, `8.3.d.a` | Retrieved via the raw API endpoint (`mf_newforms`, `traces` field), not an AI-summarized web fetch, per the discipline established in the underlying project's Round 13 | Identification/tabulation only — explicitly labeled in the bibliography entry as not the source of any theorem | Primary data source, correctly scoped |

## Honest gaps in this audit

- **[3] and [7] were not independently fetched and read this phase** — their citations are bibliographically verified (correct title/journal/year via search), and [3]'s content was cross-confirmed indirectly (via its role in Schütt's paper, which was directly read), but neither paper's own text was fetched and read the way [5]/[6] were. This is a lower-risk gap than it would be for [5] (Livné's theorem is the crux of the twist argument, and *that* citation's content was verified directly); [3]'s and [7]'s roles are more standard/textbook-level classical facts (the K3 Torelli theorem; the general shape of CM-newform Galois representations) less likely to contain a surprising hypothesis mismatch, but a human co-author should still verify both directly before submission, particularly [7] since it is the source of the paper's `\mathrm{Sym}^2` splitting claim.
- **No claim in the paper depends on any citation being wrong in a way that would go undetected**: the numerical/algebraic content combining these citations (the Main Theorem's derivation) was independently verified end-to-end (symbolically and against LMFDB data) in prior rounds of this project and re-checked during this manuscript phase, so an error confined to [3] or [7]'s exact wording (as opposed to their well-established mathematical content) would be caught by the numerical cross-check, not silently propagate.

## Citation-use audit (per Part XII's instruction: LMFDB cited only as catalogue, not as proof)

Confirmed: LMFDB is used, throughout the manuscript, only to retrieve/identify the specific Hecke eigenvalues of `8.3.d.a` (e.g. `a_3(f)=-2` in the proof of Proposition 7.2/Appendix D). No theorem in the manuscript cites LMFDB as its source.

---

## Manuscript Phase 4 update

The bibliography was revised. Current numbering (10 entries):

1. **Ahlgren, Ono, Penniston (2002)** — **new, the central prior
   reference.** Directly fetched and read in full (author's own posted
   PDF). Its Theorem 2.1, specialized at `\lambda=1`, and Theorem 1.2
   together establish the manuscript's central character-sum identity
   and the singularity/CM-field of the same K3 surface, independently
   and 24 years prior. Now cited prominently in the abstract,
   introduction, Theorem `thm:main`'s statement, a dedicated comparison
   section (`sec:methods`), and the Limitations section.
2. Shioda 1972 — unchanged.
3. Shioda 1990 — unchanged, now also cited for the torsion-embedding
   fact underlying the new Lemma `lem:torsion`.
4. **Miranda–Persson 1989 — new.** *"Torsion groups of elliptic
   surfaces,"* Compositio Math. 72 (1989), 249–267 — bibliographically
   confirmed (title, authors, journal, volume, pages verified directly
   against the journal's own numdam.org copy, first page read). Cited
   for the general theory of torsion groups of elliptic surfaces,
   supporting Lemma `lem:torsion`.
5. Pjateckiĭ-Šapiro–Šafarevič 1971 — **citation text repaired**: now
   explicitly states, within the bibliography entry itself, that the
   1971 original was not directly read, names the secondary sources
   used (Huybrechts' *Lectures on K3 Surfaces*, Schütt), and recommends
   a direct primary-source check before submission. This is a more
   honest and more useful bibliography entry than Phase 2/3's version,
   which left this caveat only in supporting documents rather than the
   manuscript itself.
6. Shioda–Inose 1977 — unchanged.
7. Livné 1995 — unchanged; still the most rigorously verified citation
   in the paper (directly fetched and read, Round 34 and reconfirmed
   Phase 3).
8. Schütt 2008/2010 — unchanged.
9. **CM/Hecke-character theory (Shimura + Ribet) — repaired.** Previously
   attributed the Sym² symmetric-square splitting to "Ribet's classical
   result" alone; now cites Shimura's *Introduction to the Arithmetic
   Theory of Automorphic Functions* alongside Ribet 1977, and explicitly
   notes that Ribet's paper is more precisely the source for the
   *converse* fact (rational-coefficient weight-3 newforms have CM),
   not necessarily the sole source for the forward Sym² splitting
   itself. Both hardcoded `[7]`-style in-text citations to "Ribet's CM
   symmetric-square decomposition" were replaced with `\cite{CMtheory}`
   pointing to this corrected, dual-attributed entry.
10. LMFDB — unchanged, still explicitly scoped as identification-only.

**All ten entries now compile correctly** (no undefined `\cite` keys,
verified by a clean `pdflatex` run, zero citation warnings in the final
pass).

