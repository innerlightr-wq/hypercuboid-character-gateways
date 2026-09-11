# CHECKPOINT — Hypercuboid Arithmetic Exploration, after Round 29

Supersedes `CHECKPOINT_AFTER_ROUND28.md`. Read this file first. Sections
1–4 carry forward with the geometric side now essentially exhausted;
§§5–7 updated with Round 29's diagnostic shift.

---

## 1. Current PROVED results (unchanged, plus exhaustive re-confirmation)

Everything through the complete `I_2^*`/`I_0^*`/`I_2` resolutions,
`N(p)` formulas, `\mathrm{Tr}_{NS}(p)=(19+\chi(-1))p`, and
`\#X(\mathbb F_p)=\#V(\mathbb F_p)+19p+\chi(-2)` stands PROVED (see Round 27's
checkpoint §1 for the full list).

**NEW this round — the geometric point-count side is now exhaustively
audited and clean:**
- **PROVED**: `\#V(\mathbb F_p)=p^2+S(p)` re-derived from scratch,
  elementary, no correction (`1+\chi(c)` trick, valid for `c=0` too).
- **PROVED**: the generic-fiber relation `\#X_t=\mathrm{affine}_t+1` and
  the full fiberwise re-summation over `\mathbf P^1(\mathbb F_p)` reproduce
  `\#X=\#V+19p+\chi(-2)` exactly, independently of the Round 27
  derivation route.
- **PROVED**: zero-section bookkeeping is clean — `O_t` is a single,
  ordinary, already-counted-once point of the identity component at
  every fiber; no double-counting mechanism found.
- **NEW, closes a genuine gap**: `I_0^*`'s three named components each
  have their own `\rho=\infty` point (never checked since Round 19,
  exactly analogous to the `C_2`/`A=\infty` gap Round 26 found and
  Round 27 resolved for `I_2^*`) — **checked this round and found
  smooth and unconditionally rational** (`\partial K_2/\partial U=1`
  identically, all three cases). `N_{I_0^*}(p)=5p+1` stands unshaken.
- **RECONFIRMED**: `I_0^*`'s smoothness mechanism is genuinely different
  from `I_2^*`/`I_2`'s (implicit-function-theorem via a nonzero integer
  partial derivative, not ternary-quadratic-form isotropy — Hessian
  determinant is `0` in all three `I_0^*` cases, since the `\rho^2u`
  term is cubic, not quadratic) — both mechanisms are unconditional,
  and this project has now verified **every** local singularity by
  whichever of the two mechanisms actually applies.

**Conclusion of the three-round audit (Rounds 27–29)**: `t=1`'s local
resolution, `H^0`/`H^4` normalization, and now `t=-1`'s local resolution
(including its own previously-unchecked infinity points) are all **ruled
out** as the source of `D(p)=1-\chi(-2)`. **The geometric point-count
side of the ledger is essentially exhausted.**

---

## 2. Computationally verified but NOT proved (unchanged, with a sharpened leading hypothesis)

Master identity `S(p)=\chi(-1)(a_p(f)+p)`, equivalently
`S(p)=-\chi(2)p+\chi(-1)a_p(E)^2`. **Status: NOT proved.**

**NEW this round — leading hypothesis for `D(p)` has shifted**: given
the geometric side is now exhaustively clean (§1), the best-supported
(but **not proved**) reading is that the point-count ledger
`\#X=\#V+19p+\chi(-2)` is **already exactly correct**, and the
transcendental trace itself is
$$\mathrm{Tr}_T(p) \overset{?}{=} \chi(-1)a_p(f) + \chi(-2) - 1$$
(a small additive correction beyond a bare `\chi(-1)a_p(f)`) — **this
is explicitly CONDITIONAL**: it was derived only by combining the
(proved) ledger with the (numerically verified, not proved) master
identity as a working constraint, **not independently derived** from
the transcendental lattice's own Frobenius/period structure. Round 30
should attempt exactly that independent derivation.

---

## 3. Important corrections and KILLED hypotheses — DO NOT RETRY

All prior checkpoints' lists stand. **NEW this round:**
- **KILLED (t=-1's remaining unchecked locus)**: `I_0^*`'s named
  components' `\rho=\infty` points as a hidden source of `D(p)` — ruled
  out by direct, exact computation (all three cases smooth,
  `\partial/\partial U=1`).
- **RECONFIRMED, not an error**: `\#V=p^2+S(p)`, the zero-section
  ledger, and the fiberwise `\#X-\#V` derivation — all re-derived from
  scratch this round and found to exactly match prior rounds.

---

## 4. Current geometric state (unchanged, now doubly-verified)

All four bad fibers complete and now audited by two independent passes
each (Rounds 16–19 originally; Rounds 27–29 with the sharper
tangent-cone/Hessian/infinity-point method): `I_2(1)`: `2p`.
`I_0^*(-1)`: `5p+1`. `I_2^*(0)`, `I_2^*(\infty)`: `7p+1` each. **No
local geometry remains unaudited anywhere in this project.**

---

## 5. Exact current bottleneck (read this first when resuming)

> **The immediate unresolved task is:** determine, **independently of
> the (numerically verified but unproved) master identity**, the exact
> transcendental Frobenius trace `\mathrm{Tr}_T(p)`, and check whether it
> genuinely equals `\chi(-1)a_p(f)+\chi(-2)-1` (Round 29's leading,
> conditional hypothesis) rather than a bare `\chi(-1)a_p(f)`.

**Do not** continue auditing local point-counts at `t=0,1,-1,\infty` —
this is now considered exhaustively closed (§1/§4) unless a genuinely
new, specific reason to doubt a particular piece arises. **Do not**
re-derive `\#V=p^2+S(p)`, the zero-section ledger, or the fiberwise
summation again — all reconfirmed clean twice now.

**The search should move to the cohomological/modular side**: attempt
to derive `\mathrm{Tr}_T(p)` from the Shioda–Inose/Kummer construction's
own structure (Round 13's Track A framework — `H^1(E)\otimes H^1(E)`,
`\mathrm{Sym}^2`, and how many of `T(X)`'s generating periods/cycles are
`\mathbb Q$-rational vs. require `\mathbb Q(\sqrt{-2})` — a genuinely different
kind of calculation than anything attempted in Rounds 27–29).

---

## 6. Round-29 outcome (for continuity)

- Closed a new, genuine gap at `I_0^*` (the `\rho=\infty` points of its
  three named components, never checked since Round 19) — found clean.
- Re-derived `\#V=p^2+S(p)`, the zero-section ledger, and the fiberwise
  `\#X-\#V` summation entirely from scratch — all confirmed to match
  Round 27 exactly, with no new correction found anywhere.
- **Seriously tested (Part IX) the possibility that the ledger is
  already correct** and the residual belongs on the modular side —
  found this to be the best-supported reading given the now-exhaustive
  geometric audit, but did not prove it (the conditional formula for
  `\mathrm{Tr}_T(p)` was derived only by using the master identity as an
  input, not independently).
- Therefore Round 29 ended with verdict **ROUND29-D** (residual remains
  unexplained by independent derivation), but with a genuine, useful
  sharpening: the search has shifted from "find a geometric miscount"
  toward "derive the transcendental trace independently and check for
  a small correction term."

---

## 7. Planned Round 30 strategy

**Primary next step**: attempt to derive `\mathrm{Tr}_T(p)` from first
principles via the Shioda–Inose/Kummer structure, **without** using the
master identity as an input at any stage. Specifically:
1. Determine explicitly whether `X` (or its Kummer/Shioda-Inose
   partner) really does decompose so that the transcendental part's
   Frobenius trace is built from `H^1(E)\otimes H^1(E)` (Round 13's
   Track A, never completed) — if so, derive the *exact* trace formula
   (not just "`\chi(-1)a_p(f)`" by analogy) from the actual
   Künneth/quotient construction, tracking every algebraic-vs-
   transcendental piece and every `\mathbb Q$ vs. `\mathbb Q(\sqrt{-2})`
   distinction explicitly.
2. Compare the resulting formula against Round 29's conditional
   `\chi(-1)a_p(f)+\chi(-2)-1` — if they match, this would **prove**
   both the corrected transcendental trace formula and (combined with
   the now-exhausted geometric ledger) close to a full proof of the
   master identity.

**Escape hatch**: if the Shioda–Inose construction proves too intricate
to complete explicitly, consider instead directly computing
`\mathrm{Tr}_T(p)$ for a handful of primes via `\#X(\mathbb F_p)` computed
by BRUTE-FORCE enumeration of the now-fully-explicit resolved model
(summing the now-known exact fiber structures at every `t`, including a
direct finite-field count at each of the ~`p+1` fibers) — this would
give `\mathrm{Tr}_T(p)$ numerically, independent of the master identity,
and could be compared against both candidate formulas
(`\chi(-1)a_p(f)` vs. `\chi(-1)a_p(f)+\chi(-2)-1`) as a genuine,
non-circular test.

---

## 8. Logical dependency chain (updated)

```
hypercuboid character sum (n=4 zero-sector)         [PROVED — Rounds 1–9]
S_I(p) = (p-1) S(p)                                  [PROVED — Round 9/10]
S(p) = #V(F_p) - p^2                                 [PROVED — Round 10, re-audited Round 29]
K3 surface X (Weierstrass model, fibers, e=24)       [PROVED — Round 11]
rho(X_Qbar)=20 ; |disc NS|=8 ; T(X)=diag(2,4)        [PROVED — Round 21]
Tr_NS(p) = (19+chi(-1)) p                            [PROVED — Round 22]
Complete I_2^*/I_0^*/I_2 resolutions, N(p) formulas  [PROVED — Round 27, re-audited Round 28-29]
#X(F_p) = #V(F_p) + 19p + chi(-2)                    [PROVED — Round 27, RECONFIRMED
                                                        exhaustively Round 29 -- likely FINAL]
Tr_T(p) = chi(-1)a_p(f) + chi(-2) - 1 ?               [CONDITIONAL — Round 29,
        <-- BLOCKED HERE (independent derivation        not independently derived]
             needed, not via master identity)
S(p) = chi(-1)(a_p(f)+p)   [master identity]          [COMPUTATIONALLY VERIFIED ONLY]
```

---

## 9. Files needed for Round 30

- **This checkpoint** (`notes/CHECKPOINT_AFTER_ROUND29.md`) — read first.
- `notes/round29_report.md` — the full `t=-1` re-audit, `\#V=p^2+S(p)`
  re-derivation, zero-section ledger, and Part IX's conditional
  `\mathrm{Tr}_T(p)` formula.
- `notes/round27_report.md`, `round28_report.md` — the complete `I_2^*`
  geometry and the `t=1`/`H^0\!,\!H^4` audits (all now closed, reference
  only).
- `notes/round13_report.md` — the original Shioda–Inose Track A
  framework (`H^1(E)\otimes H^1(E)$, never completed) — the starting
  point for Round 30's primary strategy.
- `notes/round21_report.md`, `round22_report.md` — the algebraic-cycle
  Galois action and `\mathrm{Tr}_{NS}(p)` derivation (template for how a
  rigorous, non-circular trace derivation should look).

---

## 10. Repository status (checked just now, after Round 29)

Unchanged in kind: pre-existing Phase-1 files outside
`explorations/hypercuboid/` remain untouched. `explorations/hypercuboid/`
remains untracked, now also containing `notes/round29_report.md` and
this checkpoint. No staged changes, no commits made by this exploration.
`hypercuboid.pdf` and all unrelated repository content remain untouched.

---

NEXT SESSION STARTING POINT

Attempt to derive Tr_T(p) independently of the master identity, via the Shioda-Inose/Kummer construction's own H^1(E) tensor H^1(E) structure (Round 13's Track A, never completed) -- do not re-audit any local point-count geometry, which is now exhaustively closed. Compare the independently-derived trace against Round 29's conditional hypothesis Tr_T(p) = chi(-1)*a_p(f) + chi(-2) - 1. If they match, this would close the remaining gap and settle the master identity's status; if not, report the genuine discrepancy precisely. If the Shioda-Inose derivation proves too difficult, fall back to direct brute-force computation of #X(F_p) via the now-fully-explicit resolved fiber structures, to obtain Tr_T(p) numerically and independently as a non-circular check.

PAUSED AFTER ROUND 29 — READY FOR ROUND 30
