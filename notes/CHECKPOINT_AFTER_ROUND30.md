# CHECKPOINT — Hypercuboid Arithmetic Exploration, after Round 30

Supersedes `CHECKPOINT_AFTER_ROUND29.md`. Read this file first. §§1–4
carry forward (geometric side still exhaustively closed); §§5–7 updated
with Round 30's independent-derivation findings and course-correction.

---

## 1. Current PROVED results (unchanged)

Everything through the complete `I_2^*`/`I_0^*`/`I_2` resolutions,
`\mathrm{Tr}_{NS}(p)=(19+\chi(-1))p`, and
`\#X(\mathbb F_p)=\#V(\mathbb F_p)+19p+\chi(-2)` stands PROVED (Round 27,
exhaustively re-audited Rounds 28–29). **No local geometry was touched
this round** (per the round's own instruction).

**NEW this round — modular side, re-derived from first principles
(PROVED, elementary representation theory, not cited)**:
- `H^1(E)\otimes H^1(E)` trace `=a_p(E)^2` exactly; `\Lambda^2$ trace
  `=p` (always algebraic); `\mathrm{Sym}^2` trace `=a_p(E)^2-p`.
- `\mathrm{Sym}^2H^1(E)\cong\rho_f\oplus(\chi(-2)\cdot\mathrm{cyc})`, giving
  `a_p(f)=a_p(E)^2-p(1+\chi(-2))` — Round 13's relation, now derived,
  not cited.
- The singular K3's classification (`T(X)`, `\mathrm{disc}=8`) forces
  the newform `8.3.d.a` **by theory** (`h(-8)=1` uniqueness), not by
  numerical matching.

---

## 2. Computationally verified but NOT proved

Master identity `S(p)=\chi(-1)(a_p(f)+p)`. **Status: still NOT proved.**
`D(p)=1-\chi(-2)` still open.

**NEW this round — the twist question is narrowed, but the residual is
NOT resolved:**
- **KILLED, independently**: `\mathrm{Tr}_T(p)=a_p(f)` (no twist) —
  refuted by direct comparison against the proved geometric ledger
  (produces a term proportional to `a_p(f)(1-\chi(-1))`, not a bounded
  correction — genuinely inconsistent, not just unmatched).
- **Best-motivated remaining hypothesis**: `\mathrm{Tr}_T(p)=\chi(-1)a_p(f)`
  (single global twist, by analogy with the proved `\mathbb Q(i)`-descent
  of the algebraic cycle, Round 21) — reproduces the master identity's
  *original, zero-residual* algebraic form when combined with the
  ledger... **but only by re-deriving the exact same `D(p)=1-\chi(-2)`
  residual on this independent route too.**
- **COURSE-CORRECTION (important)**: Round 29's leading hypothesis,
  `\mathrm{Tr}_T(p)=\chi(-1)a_p(f)+\chi(-2)-1`, is **NOT supported** by
  this round's independent H¹⊗H¹ derivation — there is no natural place
  for that extra additive term in the representation theory as derived.
  **Do not pursue that specific correction further.**
- **NEW leading hypothesis for `D(p)`'s true source**: the Shioda–Inose
  correspondence between `X` and `\mathrm{Km}(E\times E)` is generically
  a **degree-2** rational map (Nikulin-involution quotient), not an
  isomorphism — this was never accounted for in either the geometric
  ledger (Rounds 27–29) or this round's Künneth-algebra derivation, both
  of which implicitly treated `T(X)` and `\rho_f` as directly identified.
  A genuine Riemann–Hurwitz/degree-2 correction is the most likely
  missing piece. **Not yet derived or tested.**
- **Secondary candidate, also new, also untested**: whether all 16
  order-2 points of `E\times E` are individually `\mathbb F_p`-rational in
  the Kummer construction's node resolution — plausibly `\chi(2)`- or
  `\chi(-2)`-dependent, since `2` is ramified in `\mathbb Q(\sqrt{-2})`.

---

## 3. Important corrections and KILLED hypotheses — DO NOT RETRY

All prior checkpoints' lists stand. **NEW this round:**
- **KILLED**: `\mathrm{Tr}_T(p)=a_p(f)$ (no twist at all).
- **KILLED / do not retry**: Round 29's `\mathrm{Tr}_T(p)=\chi(-1)a_p(f)+\chi(-2)-1`
  hypothesis — an independent, more careful derivation gives no natural
  room for this term. Do not re-propose an ad hoc additive correction to
  `\mathrm{Tr}_T(p)` again without a specific geometric mechanism behind
  it (e.g. the degree-2 correspondence below).

---

## 4. Current geometric state (unchanged, exhaustively closed)

`I_2(1)`: `2p`. `I_0^*(-1)`: `5p+1`. `I_2^*(0)`, `I_2^*(\infty)`: `7p+1`
each. No local geometry remains unaudited. **This round correctly did
not re-touch it.**

---

## 5. Exact current bottleneck (read this first when resuming)

> **The immediate unresolved task is:** determine whether the
> Shioda–Inose map `X\dashrightarrow\mathrm{Km}(E\times E)` is degree 1
> or degree 2 for this specific surface, and — if degree 2 — derive the
> exact point-count/trace correction it contributes. This is now a
> precisely-scoped question, not a vague "find the twist."

**Do not**: re-audit local fiber geometry (§4, closed); re-propose a
bare additive correction to `\mathrm{Tr}_T(p)` without deriving it from
an explicit geometric mechanism (§3); re-litigate the `\chi(-1)` vs.
"no twist" question (§2, `\chi(-1)$ is now independently well-motivated,
even though it alone doesn't close the gap).

**Two independent derivations (geometric ledger; modular Künneth
decomposition) now agree exactly on both the identity's algebraic form
AND the exact size/shape of the residual `D(p)=1-\chi(-2)`** — this
convergence is itself informative: it makes a bookkeeping slip in
either route much less likely, and points toward a **single shared
structural cause** likely sitting in the Shioda–Inose/Kummer
correspondence itself (used implicitly by both routes, examined
explicitly by neither).

---

## 6. Round-30 outcome (for continuity)

- Independently re-derived (not cited) the `H^1(E)\otimes H^1(E)`
  decomposition and the classical `a_p(f)=a_p(E)^2-p(1+\chi(-2))`
  relation from first-principles Frobenius-eigenvalue algebra.
- Independently re-derived the theory-forced (not numerically matched)
  identification of newform `8.3.d.a`, given `h(-8)=1`.
- Killed the "no twist" hypothesis for `\mathrm{Tr}_T(p)` by genuine
  independent contradiction (not just non-match).
- **Course-corrected against** Round 29's leading conditional hypothesis
  — a real, useful negative result, not a repeat.
- Located a new, sharply-scoped, well-motivated leading candidate for
  `D(p)`'s source (Shioda–Inose correspondence degree), not yet tested.
- Verdict: **ROUND30-C** (transcendental representation substantially
  narrowed; master identity not proved; residual persists identically
  across two independent derivation routes).

---

## 7. Planned Round 31 strategy

**Primary next step**: determine explicitly, for this specific `T(X)`
(discriminant 8, `h(-8)=1`), whether the classical Shioda–Inose
construction gives `X\cong\mathrm{Km}(E\times E)$ (degree 1) or a genuine
degree-2 correspondence via a Nikulin involution (the general
Shioda–Inose theorem's usual statement). If degree 2: derive the exact
trace/point-count correction such a correspondence contributes (a
Riemann–Hurwitz-flavored computation on the level of `\#X(\mathbb F_p)`
vs. `\#\mathrm{Km}(E\times E)(\mathbb F_p)`), and check whether it
produces exactly `1-\chi(-2)`.

**Secondary/fallback**: examine the 16-node Kummer resolution's
`\mathbb F_p`-rationality directly — count how many of `E[2]\times E[2]`'s
16 points are individually rational as a function of `\chi(2)`,
`\chi(-2)`, `\chi(-1)`, and whether an odd number of non-rational nodes
(forcing a Galois-orbit pairing in the resolution) could plausibly
contribute a small, bounded, `\chi(-2)`-shaped correction of exactly the
right size.

**Escape hatch (unchanged from Round 29's checkpoint, still available
and untried)**: direct brute-force `\#X(\mathbb F_p)` computation via the
now-fully-explicit resolved fiber structures, to obtain `\mathrm{Tr}_T(p)`
numerically at a handful of primes, independent of both derivation
routes, as a non-circular tie-breaker.

---

## 8. Logical dependency chain (updated)

```
hypercuboid character sum (n=4 zero-sector)         [PROVED — Rounds 1–9]
S_I(p) = (p-1) S(p)                                  [PROVED]
S(p) = #V(F_p) - p^2                                 [PROVED, re-audited Round 29]
K3 surface X (Weierstrass model, fibers, e=24)       [PROVED]
rho(X_Qbar)=20 ; |disc NS|=8 ; T(X)=diag(2,4)        [PROVED — Round 21]
Tr_NS(p) = (19+chi(-1)) p                            [PROVED — Round 22]
Complete I_2^*/I_0^*/I_2 resolutions, N(p) formulas  [PROVED — Round 27, re-audited 28-29]
#X(F_p) = #V(F_p) + 19p + chi(-2)                    [PROVED — Round 27, RECONFIRMED, likely FINAL]
H^1(E)xH^1(E) decomposition, a_p(f) relation         [PROVED, elementary — Round 30, new]
newform 8.3.d.a forced by disc(T(X))=8, h(-8)=1      [PROVED-by-theory — Round 30, new]
Tr_T(p) = chi(-1)*a_p(f)                              [BEST-MOTIVATED, still leaves
        <-- BLOCKED HERE (residual D(p)=1-chi(-2)      D(p)=1-chi(-2) unresolved]
             reappears via this independent route)
Shioda-Inose correspondence degree (1 vs 2)?          [OPEN, NEW — Round 30's leading
                                                        hypothesis for D(p)'s source]
S(p) = chi(-1)(a_p(f)+p)   [master identity]          [COMPUTATIONALLY VERIFIED ONLY]
```

---

## 9. Files needed for Round 31

- **This checkpoint** (`notes/CHECKPOINT_AFTER_ROUND30.md`) — read first.
- `notes/round30_report.md` — full H¹⊗H¹ derivation, twist analysis,
  course-correction against Round 29, and the new Shioda–Inose-degree
  hypothesis.
- `notes/round21_report.md`, `round22_report.md` — the proved `\mathbb Q(i)`
  algebraic-cycle Galois action (template/analogy source for the
  `\chi(-1)` twist hypothesis).
- `notes/round13_report.md` — original Track A framework.
- Any standard reference on the Shioda–Inose construction's degree (not
  in this repo — general literature fact to be applied carefully, as
  was done for Livné's theorem in Round 22).

---

## 10. Repository status (checked just now, after Round 30)

Unchanged in kind: pre-existing content outside
`explorations/hypercuboid/` remains untouched. `explorations/hypercuboid/`
remains untracked, now also containing `notes/round30_report.md` and
this checkpoint. No staged changes, no commits made by this exploration.
`hypercuboid.pdf` and all unrelated repository content remain untouched.

---

NEXT SESSION STARTING POINT

Determine whether the Shioda-Inose correspondence X -> Km(ExE) is degree 1 or degree 2 for this specific discriminant-8 K3, and if degree 2, derive its exact point-count/trace correction and test it against D(p)=1-chi(-2). Fallback: audit F_p-rationality of the 16 Kummer nodes as a function of chi(2)/chi(-2)/chi(-1). Do not re-propose bare additive corrections to Tr_T(p) without a derived geometric mechanism (Round 29's guess was tested and does not hold up). Do not re-audit local fiber geometry, which remains exhaustively closed.

PAUSED AFTER ROUND 30 — READY FOR ROUND 31
