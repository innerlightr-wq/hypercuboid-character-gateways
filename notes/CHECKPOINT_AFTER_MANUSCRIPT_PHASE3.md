# CHECKPOINT — Hypercuboid Project, after Manuscript Phase 3

Supersedes nothing — all prior checkpoints (`CHECKPOINT_AFTER_ROUND34.md`,
`CHECKPOINT_AFTER_MANUSCRIPT_PHASE1.md`,
`CHECKPOINT_AFTER_MANUSCRIPT_PHASE2.md`) are preserved permanently. This
file records Phase 3's outcome: **a genuine, major prior-literature
overlap was found. The manuscript's mathematics is correct, but it is
not currently safe to submit or widely circulate as-is.**

---

## 1. Headline finding

**The manuscript's Main Theorem is an immediate corollary of a
published 2002 paper**: S. Ahlgren, K. Ono, D. Penniston, *"Zeta
functions of an infinite family of K3 surfaces,"* Amer. J. Math. **124**
(2002), no. 2, 353–368. Their family `X_\lambda:s^2=xy(x+1)(y+1)(x+\lambda y)`
at `\lambda=1` is **literally the same affine surface** as this
project's `V`. Their **Theorem 2.1**, specialized at `\lambda=1`,
**reproduces the manuscript's `S(p)` formula exactly** (verified
numerically this phase, fresh, 10 primes, zero discrepancy, via a
direct curve-twist identification `a(1,p)=\chi(-1)(p)a_p(E)`). Their
**Theorem 1.2** already proves `\lambda=1` is singular (`\rho=20`) with
CM by `\Q(\sqrt{-2})`, and a citing paper (Amir–Hong, arXiv:2007.09803,
fetched and read directly) reports their associated newform at
`\lambda=1` is CM-by-`\Q(\sqrt{-2})` twisted by `\chi_{-4}=\chi(-1)` —
apparently the same twist this project derived independently via K3
lattice theory.

**This was found by actually fetching and reading the AOP 2002 paper**
(full PDF obtained from Ken Ono's own posted copy,
`https://uva.theopenscholar.com/files/ken-ono/files/065_8.pdf`), not
inferred from an abstract — the polynomial match, Theorem 2.1's formula
match, and the elliptic-curve twist identification were all directly
verified, not merely suspected.

**What this does NOT mean**: the manuscript's mathematics is not wrong.
Every step was independently re-derived and confirmed correct in this
audit (Parts II–VIII, XI–XIII of `manuscript/REFEREE_AUDIT.md`). The
K3-surface/Picard-lattice/Livné-theorem proof route is a genuinely
different METHOD from AOP's elementary Jacobi-sum manipulation, reaching
the same conclusion — this has real independent value as an alternative
derivation, but the manuscript as currently written does not
acknowledge AOP at all, which is a serious omission for publication.

**What appears to remain genuinely unduplicated** (searched, not found
anywhere in the literature this phase): the hypercuboid character-sum
motivation itself (`\Sigma_I,\Sigma_{II},\Sigma_{III}`, the `S_4`
zero-sector classification, the `\Sigma_I(p)=(p-1)S(p)` reduction, and
the Gateway relation `\Sigma_{II}=\chi(-1)\Sigma_I`). This is the part
of the paper most likely to constitute a genuine new contribution.

---

## 2. Files created this phase

- `manuscript/REFEREE_AUDIT.md` — the full referee report (Summary,
  Major/Minor issues, Reference issues, Novelty issues, Exposition,
  Reproducibility, Required revisions, Recommendation). This is now the
  authoritative pre-submission status document for the manuscript —
  **read this before doing anything else with the manuscript.**

## 3. Files modified this phase (safe corrections only)

- `manuscript/hypercuboid_character_sums.tex` — one wording fix (Class
  III's "omitting two forms" phrasing, corrected to "omitting the
  remaining form," in both occurrences) — a notation/clarity fix, **no
  mathematical content changed**. Recompiled cleanly (exit 0, 12 pages,
  same one pre-existing cosmetic overfull-hbox warning, left as
  disclosed rather than risk disturbing an already-re-verified
  paragraph).
- `manuscript/hypercuboid_character_sums.pdf` — recompiled.

**No substantive mathematical content was changed anywhere.** The
`\mathrm{MW}_{\mathrm{tors}}` gap, the reference-precision issues, and
the AOP finding were all deliberately left untouched in the manuscript
itself, per this phase's explicit instruction, for a separate repair
phase.

---

## 4. Full audit results (see `manuscript/REFEREE_AUDIT.md` for detail)

| Part | Result |
|---|---|
| Main theorem chain | Every step proved or literature-cited; no unsupported assertion |
| Character-sum reduction | Sound; found and fixed one phrasing ambiguity (Class III) |
| K3 model | Sound; classification justification slightly terse (not fixed) |
| Point-count ledger (`N_{I_2}`) | Sound, re-verified in full a third time |
| Height/Picard rank | Sound |
| NS discriminant/transcendental lattice | **One genuine gap found**: `\mathrm{MW}_{\mathrm{tors}}=(\Z/2)^2` asserted, not proved complete |
| NS Frobenius trace | Sound |
| Pjatecki\u{i}-\u{S}apiro–\u{S}afarevi\v{c} source | Corroborated via secondary sources only, not directly fetched |
| Ribet source | Found via a citing paper; minor attribution-precision issue |
| Livné/Schütt | Reconfirmed fresh; found a new supporting precedent (Schütt's own discriminant-3 worked example uses the identical few-prime elimination method) |
| Twist proof (`p=3`) | Sound, third independent confirmation (Rounds 33, 34, this phase) |
| `a_3(f)=-2` source | Reproducible, correctly disclosed as external |
| CM/Sym² identity | Sound |
| **Novelty** | **Major finding: immediate corollary of AOP 2002** |
| Claim strength | No sentence-level overclaiming; the issue is a document-level omission |
| Class III | Not overclaimed |
| Reproducibility | All scripts run and match; one minor script-robustness issue found, not fixed |

---

## 5. Verdict

**PHASE3-C** — substantive repair required before release. The
mathematics is sound; the paper is not yet safe for submission or wide
circulation because it omits a directly overlapping, 24-years-prior
published result.

---

## 6. What must happen before this manuscript is submission-ready

1. **(Required, major)**: cite Ahlgren–Ono–Penniston (2002) explicitly
   and honestly relate the manuscript's Main Theorem to their Theorem
   2.1/1.2. This likely requires rewriting the Introduction and
   Discussion, and possibly the Abstract, to reframe the contribution
   — most plausibly as (a) an independent K3-geometric proof of part of
   a known result, newly and originally motivated by/connected to the
   hypercuboid character-sum construction, plus (b) the new Gateway
   relation and Class-III boundary, which are not found in AOP or
   anywhere else searched.
2. **(Required, minor)**: add a proof or citation for
   `\mathrm{MW}_{\mathrm{tors}}(X)\cong(\Z/2)^2` exactly.
3. **(Recommended)**: directly verify the Pjatecki\u{i}-\u{S}apiro–\u{S}afarevi\v{c}
   citation against a primary source (Huybrechts' book is a good
   candidate, already partially fetched this phase but not fully
   extracted); refine the Ribet citation.
4. **(Recommended)**: one added sentence on `q(X)=0` in Prop. 4.1.
5. **(Housekeeping, not blocking)**: make `round32_full_chain_check.py`
   and `round33_twist_proof_check.py` fail gracefully (like
   `round13_modular.py` does) when the cached LMFDB JSON is absent.

**None of these require new mathematics.** Item 1 is a substantial
writing/reframing task; items 2–5 are each small, contained additions.

---

## 7. Repository status

`explorations/hypercuboid/` remains untracked; no commits or pushes
made this phase. `hypercuboid.pdf` and the unrelated root-level
`manuscript/` directory untouched. All three prior checkpoints preserved
unmodified (confirmed by checksum before writing this file).

---

NEXT SESSION STARTING POINT

Manuscript Phase 3 (referee audit) found the manuscript's mathematics sound but uncovered that its Main Theorem is an immediate corollary of Ahlgren-Ono-Penniston (2002), Theorem 2.1, uncited -- a major finding requiring the paper to be substantially reframed before any submission or circulation. Verdict PHASE3-C. Full detail in manuscript/REFEREE_AUDIT.md. A "Manuscript Phase 4 -- Repair" should: (1) add the AOP citation and reframe the paper's contribution honestly (most plausibly around the hypercuboid motivation and the K3-geometric proof method, both of which appear genuinely unduplicated in the literature searched); (2) add the missing MW_tors=(Z/2)^2 lemma/citation; (3) optionally address the two smaller reference-precision and exposition items. Only safe wording corrections (Class III phrasing) were made to the manuscript this phase -- no mathematical content was changed. Class III (Sigma_III(p) at p=1 mod 4) remains the sole open mathematical problem, unrelated to any of this.

READY FOR: Manuscript Phase 4 (repair/reframing), or a decision from the user on how to proceed given the AOP finding.
