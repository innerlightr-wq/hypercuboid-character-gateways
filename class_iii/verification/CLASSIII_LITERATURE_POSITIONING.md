# Class III Sequel — Literature Positioning

> ## ⚠ SUPERSEDED IN PART — 2026-09-21
>
> A prior-art audit established that **`X_III` is the `λ = -1` member of the
> Ahlgren–Ono–Penniston family**: `T(p) = A(-1,p)` at every odd prime tested, and the
> `Q`-linear substitution `(x,t,w) -> (x, t-x, -t-w)` carries the Class III branch sextic
> exactly onto the `λ = -1` branch sextic, so the surfaces are isomorphic over `Q`.
> Verified in `class_iii/scripts/class3_aop_identification.py`.
>
> Two statements below are therefore **withdrawn**:
>
> 1. that "the specific character sum `T(p)`/`Σ_III(p)`, and the specific Weierstrass model /
>    fiber-location data of `X_III`, were not found in the literature searched" — the sum is
>    AOP's own at `λ = -1`, and the surface's transcendental lattice `diag(2,2)`, discriminant
>    `4` and CM field `Q(i)` are recorded by van Geemen–Top, Bull. LMS **38** (2006), 209–223,
>    citing Persson, LNM **1124** (1985), p. 298, and Shioda–Inose (1977);
> 2. the framing of `X_III` as a surface distinct from AOP's. That comparison was made against
>    `λ = 8` only and did not extend over the family.
>
> Also revised: the graph-rigidity step is a **standard corollary**, not a novel technique —
> Wazir, Compositio Math. **140** (2004), 567–580, and Ulmer, PCMI **18** (2011), Lecture 3 §6,
> record that an `I_n^*` fiber has `n+5` or `n+3` rational components. The *assembly* remains
> the paper's contribution.
>
> One point runs the other way: `λ = -1` is exactly where AOP's closed-form evaluation
> degenerates, so the evaluation of the sum obtained here is not a specialization of theirs.
>
> The current positioning is in `notes/HYPERCUBOID_K3_RESEARCH_CLOSURE.md` §14 and in the
> revised manuscript. This file is retained as the historical record of the earlier search.

Distilled from `literature/ROUND2_LITERATURE_AUDIT.md`,
`literature/ROUND4_EXTREMAL_K3_AUDIT.md`, and
`literature/PHASE5_LITERATURE_AUDIT.md`. This file states, precisely and
conservatively, what the paper may and may not claim.

## The governing sentence (use verbatim or near-verbatim in the paper's
introduction and/or related-work section)

> **Class III shares the same modular form / transcendental representation
> with Ahlgren–Ono–Penniston's `λ=8` singular K3 surface and with the
> quartic Fermat K3 surface, but differs in its underlying K3 model,
> Weierstrass equation, fiber configuration, and defining character sum.**

This sentence must appear early — it is the single most important
literature-positioning statement in the paper, and stating it plainly
forecloses any reading of the result as claiming a new modular form.

## What is **not** claimed

- The modular form `16.3.c.a` / `η^6(4z)` is **not new** — it is
  Ahlgren–Ono–Penniston's own object (their equation (31), their Theorem
  1.2), independently also identified by Huber–Liu–McLaughlin–Ye–Yuan–Zhang
  with the quartic Fermat K3 surface. The paper must cite both.
- Livné's modularity theorem is **not new** — cited exactly as used in the
  existing Classes I/II manuscript, re-applied here at a different
  discriminant.
- The general machinery (Shioda–Tate, Kodaira's classification, the
  `I_n^*` dual graph structure) is **entirely standard** and must be cited
  to Kodaira (1963), Néron (1964), Tate (1975) / a standard textbook
  (Silverman, *Advanced Topics in the Arithmetic of Elliptic Curves*),
  not presented as original.
- **Absence of a located prior source for the exact sum `Σ_III(p)`/`T(p)`
  or the exact `X_III` model is not evidence of novelty** — it reflects
  the limits of a web-search-only literature review (no access to
  Schütt's complete discriminant tables, no access to the full
  Miranda–Persson 112-configuration table or Shioda's complete 325-surface
  extremal-K3 list). The paper's introduction should say this plainly:
  the exact sum and model were not located, but a definitive novelty claim
  would require database access this project did not have.

## What **can** be claimed, and how to phrase it

- **The specific character sum `T(p)`/`Σ_III(p)`, and the specific
  Weierstrass model / fiber-location data of `X_III`, were not found in
  the literature searched.** Phrase as: "We are not aware of a prior
  treatment of this exact sum or surface; see §9 for the scope of our
  literature search."
- **The proof technique in §4** (proving `NS`-rationality via full
  rational 2-torsion landing on all four multiplicity-1 legs of each bad
  fiber, combined with graph rigidity of the affine-`D6` dual graph, in
  place of an explicit fiber resolution) **is, as far as this project's
  searches determined, not the technique used in the Ahlgren–Ono–Penniston
  line of argument** (which does not need it, since their own surfaces'
  `NS` structure is established by different means in their paper) **nor
  in the existing Classes I/II manuscript** (which resolves its bad fibers
  by a different, more computational route). This is the paper's
  strongest, most defensible novelty claim, and should be stated as a
  **methodological** contribution, not a claim about the surface or
  modular form themselves.
- **The pairing of two CM branches (`Q(√-2)`, `Q(i)`) from one underlying
  finite-field hypercuboid construction** is, as far as searched, not
  previously observed — but state this as an *observation about this
  project's own construction*, not a claim about the broader literature
  (since the hypercuboid construction itself is this project's own prior
  work, not something an external search could confirm or deny novelty
  against).

## Extremal-K3 catalogue status (be precise, do not overstate)

Miranda–Persson (1989) determined all 112 possible singular-fiber
configurations for extremal elliptic K3 surfaces; Shioda has compiled a
complete list of all 325 such surfaces with transcendental lattice, fiber
type, and Mordell–Weil data. `X_III`'s configuration (three `I2*` fibers,
torsion `(Z/2)²`) is **very likely** among these 325 — this project's
web-search-only literature review could not access the specific table
entries to confirm or refute an exact match. **The paper should say
exactly this**, framed as an open item for a referee or reader with table
access to check, not as a claim either way. Suggested phrasing: "The fiber
configuration `3×I2*` with torsion `(Z/2)²` is a natural candidate for
inclusion in Miranda–Persson's classification of extremal elliptic K3
configurations [cite] and Shioda's complete catalogue [cite]; we have not
been able to confirm the exact correspondence against the published
tables."

## Required citations (minimum list for the paper's bibliography)

1. Ahlgren, Ono, Penniston, "Zeta functions of an infinite family of K3
   surfaces," *Amer. J. Math.* **124** (2002).
2. Livné, R. — singular K3 modularity (1995) [exact citation to be pulled
   from the existing Classes I/II manuscript's bibliography, where it is
   already correctly formatted].
3. Kodaira, K. — classification of elliptic fibers (1963).
4. Néron, A. — models (1964).
5. Tate, J. — algorithm (1975), or a standard textbook exposition
   (Silverman, *ATAEC*).
6. Shioda, T. — Mordell–Weil lattices / trivial lattice theory (1990) and
   the extremal-K3 catalogue.
7. Miranda, R.; Persson, U. — extremal elliptic K3 classification (1989).
8. Huber, T.; Liu, ...; et al. — "On the vanishing of the coefficients of
   CM eta quotients" [for the independent `η^6(4z)` / quartic-Fermat-K3
   confirmation].
9. (Optional, flagged for a reader with access) Schütt, M. — "Arithmetic
   of a Singular K3 Surface," *Michigan Math. J.* **56** (2008), and
   Takatsu, T. — discriminant-3/4/7 singular K3 surfaces (arXiv:1903.03054)
   — cite as background on discriminant-4 singular K3 surfaces generally,
   without claiming either treats `X_III` specifically.
