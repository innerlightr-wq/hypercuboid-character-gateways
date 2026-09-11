# CHECKPOINT — Hypercuboid Arithmetic Exploration, after Round 31

Supersedes `CHECKPOINT_AFTER_ROUND30.md`. Read this file first. §§1–4
carry forward (geometric side still exhaustively closed); §§5–7 updated
with Round 31's Shioda–Inose/Kummer analysis and its structural kill.

---

## 1. Current PROVED results (unchanged, plus one new derived fact)

Everything through the complete `I_2^*`/`I_0^*`/`I_2` resolutions,
`\mathrm{Tr}_{NS}(X)(p)=(19+\chi(-1))p`, and
`\#X(\mathbb F_p)=\#V(\mathbb F_p)+19p+\chi(-2)` stands PROVED (Round 27,
re-audited 28–29). **No local geometry was touched this round.**

**NEW this round — derived (not cited/assumed) from the Kummer-surface
side, PROVED**:
- `A=E\times E` (the CM abelian surface associated to `T(X)`'s
  discriminant 8), forced by `h(-8)=1` and the diagonal shape of
  `\mathrm{diag}(2,4)`.
- `n_2=\#A[2](\mathbb F_p)^{\mathrm{rat}}=10+6\chi(2)` (`4` or `16`
  depending on `\chi(2)`) — derived from `E`'s explicit 2-torsion
  splitting (`x^2+4x+2`, discriminant `8`), governed by `\chi(2)`, a
  character genuinely distinct from the CM field's own `\chi(-2)`.
- `\#\mathrm{Km}(A)(\mathbb F_p)=(p+1)^2+a_p(E)^2+n_2p` — derived from
  scratch via explicit orbit-counting on the `\pm1`-quotient plus
  standard `A_1`-node resolution.
- `\mathrm{Tr}_T(\mathrm{Km}\,A)(p)=a_p(f)` **exactly, no twist** —
  derived via an exact `13+6\chi(2)+\chi(-2)=20` rank decomposition of
  `NS(\mathrm{Km}\,A)` (16 exceptional-curve classes + 4 classes from
  `A` itself, all individually accounted for, nothing left over).
- **Structural fact (the round's main tool)**: every term the
  degree-2 Shioda–Inose/Kummer quotient-and-resolution mechanism can
  produce is proportional to `p` (`O(p)`) — **it cannot, by
  construction, generate a bounded `O(1)` constant term.**

---

## 2. Computationally verified but NOT proved (unchanged in substance)

Master identity `S(p)=\chi(-1)(a_p(f)+p)`. **Status: still NOT proved.**
`D(p)=1-\chi(-2)$ still open, reconfirmed by direct LMFDB cross-check
(zero exceptions, `p<150`).

**NEW this round**: `\mathrm{Tr}_T(X)(p)=\chi(-1)a_p(f)` is now supported
by **two independent arguments** (Round 21's `\mathbb Q(i)`-descent
analogy; Round 31's clean `\mathrm{Tr}_T(\mathrm{Km}\,A)=a_p(f)`
derivation combined with the expected quadratic-twist relationship
between `X`'s and `\mathrm{Km}(A)`'s arithmetic models) — still not a
full proof (the Galois-equivariance of Morrison's Hodge-theoretic
isomorphism, specifically with a `\chi(-1)` twist and no other, remains
an assumption, not a derivation), but meaningfully more solid than
before.

---

## 3. Important corrections and KILLED hypotheses — DO NOT RETRY

All prior checkpoints' lists stand. **NEW this round:**
- **KILLED, structurally**: the degree-2 Shioda–Inose/Kummer
  quotient/resolution mechanism as the source of `D(p)=1-\chi(-2)`.
  Do not retry any variant of "the twist/correction comes from the
  Kummer node combinatorics" — **any such mechanism is provably `O(p)`,
  and `D(p)` is provably `O(1)`; this is a structural mismatch, not a
  computational one, so no cleverer node-counting will fix it.**
- **Checked and found insufficient**: a naive single-class
  reclassification of one of `NS(X)`'s "19 rational" classes to
  `\chi(-2)`-twisted does **not**, by itself, algebraically reproduce
  `1-\chi(-2)` exactly (tested this round) — if `NS(X)` does hide such a
  class, the fix is not this simple; don't assume a one-line patch.

---

## 4. Current geometric state (unchanged, exhaustively closed)

`I_2(1)`: `2p`. `I_0^*(-1)`: `5p+1`. `I_2^*(0)`, `I_2^*(\infty)`: `7p+1`
each. No local geometry remains unaudited. **Not re-touched this
round.**

---

## 5. Exact current bottleneck (read this first when resuming)

> **The immediate unresolved task is:** `D(p)=1-\chi(-2)` is a bounded
> (`O(1)`) quantity. Round 31 proved that the entire `O(p)`-scale
> machinery of this project (`\mathrm{Tr}_{NS}`, `\mathrm{Tr}_T`, Kummer
> node combinatorics) is structurally incapable of producing it. **The
> search must therefore focus exclusively on the ledger's bounded
> constant terms**: the Lefschetz `+1` in `\#X=1+p^2+\mathrm{Tr}(H^2)`,
> and the `+1` constants in `N_{I_2^*}(p)=7p+1` and
> `N_{I_0^*}(p)=5p+1`. Check specifically whether any of these bare
> constants is secretly a character-valued expression that has simply
> equaled `1` at every prime tested so far by algebraic necessity or
> coincidence, rather than by being a genuine unconditional constant.

**Secondary, also newly motivated**: audit `NS(X)` (rank 20) for a
hidden `\chi(-2)`-twisted class (analogous to `\mathrm{Km}(A)`'s CM
graph class `\Gamma_{\sqrt{-2}}`) inside what Round 22 classified as the
"19 rational" classes — tested this round only at the level of "does a
naive single-class swap fix the residual" (no), not at the level of
"does `NS(X)` actually contain such a class" (unexamined).

**Do not**: re-audit local fiber point-count geometry (§4, closed);
pursue the Shioda–Inose/Kummer degree-2 mechanism further as an
explanation for `D(p)` (§3, structurally killed); propose a bare,
undeserved additive correction to `\mathrm{Tr}_T(p)` without a derived
mechanism (still applies from Round 30's checkpoint).

---

## 6. Round-31 outcome (for continuity)

- Fully derived (not cited) the Shioda–Inose/Kummer quotient arithmetic
  for `A=E\times E`: 2-torsion Frobenius orbits, node-resolution point
  count, and `\mathrm{Tr}_T(\mathrm{Km}\,A)(p)=a_p(f)` via an exact
  rank-20 decomposition — all numerically cross-checked at 5 primes
  spanning both `\chi(2)` classes.
- Found and applied a genuinely new, structural falsification argument
  (`O(p)` vs. `O(1)` size-order) that **definitively kills** the round's
  central hypothesis, rather than merely re-finding the same residual by
  brute recomputation.
- Strengthened (not proved) the `\chi(-1)`-twist hypothesis for
  `\mathrm{Tr}_T(X)(p)` via a second, independent line of reasoning.
- Sharpened the search dramatically: only bounded (`O(1)`) constants in
  the whole derivation remain eligible as `D(p)`'s source.
- Verdict: **ROUND31-C** (Shioda–Inose hypothesis killed; a specific,
  narrower bridge — the ledger's bounded constants — identified as the
  next target).

---

## 7. Planned Round 32 strategy

**Primary next step**: re-derive, from scratch and with maximal
suspicion, **every bounded constant term** in the proved chain:
1. The Lefschetz `1` in `\#X(\mathbb F_p)=1+p^2+\mathrm{Tr}(H^2)(p)` — is
   `H^0(X)`'s contribution *really* always exactly `1` with trivial
   Frobenius eigenvalue, with no subtlety at any bad-reduction locus?
2. The `+1` in `N_{I_2^*}(p)=7p+1` (Round 27) — re-examine the exact
   origin of this `+1` (which named component or point contributes it)
   and check whether it could be a `(1+\chi(-2))/1`-type expression that
   only numerically looks constant.
3. The `+1` in `N_{I_0^*}(p)=5p+1` (Round 19/29) — same check.
4. Cross-check: does swapping any ONE of these bare `1`s for a
   `\chi(-2)`-dependent expression (holding everything else fixed)
   reproduce `D(p)=0` identically? Solve for what expression would be
   needed, then check whether that expression is actually what the
   underlying geometry gives (do not just pick the expression that
   works — derive it independently first, exactly as this project's
   discipline has required throughout).

**Secondary**: examine whether `NS(X)$ contains a `\chi(-2)`-twisted
class hiding among the "19 rational" ones, informed by the `A`-side
`\Gamma_{\sqrt{-2}}` analogy (Part VII of Round 31) — this requires
identifying candidate classes in `X`'s explicit resolved-fiber geometry
(the 19-dimensional trivial lattice `U\oplus D_6\oplus A_1\oplus D_4\oplus D_6`)
and checking each summand's own arithmetic individually, rather than
just its rank.

**Do not** revisit the Shioda–Inose/Kummer degree-2 mechanism (§3,
killed). **Do not** re-audit local fiber geometry (§4, closed).

---

## 8. Logical dependency chain (updated)

```
hypercuboid character sum (n=4 zero-sector)         [PROVED — Rounds 1–9]
S_I(p) = (p-1) S(p)                                  [PROVED]
S(p) = #V(F_p) - p^2                                 [PROVED, re-audited Round 29]
K3 surface X (Weierstrass model, fibers, e=24)       [PROVED]
rho(X_Qbar)=20 ; |disc NS|=8 ; T(X)=diag(2,4)        [PROVED — Round 21]
Tr_NS(X)(p) = (19+chi(-1)) p                         [PROVED — Round 22, NOW THE
                                                       LEADING SUSPECT for D(p), Round 31]
Complete I_2^*/I_0^*/I_2 resolutions, N(p) formulas  [PROVED — Round 27, re-audited 28-29,
                                                       their "+1" CONSTANTS now suspect]
#X(F_p) = #V(F_p) + 19p + chi(-2)                    [PROVED — Round 27, RECONFIRMED]
A = ExE, Kummer quotient arithmetic, n_2=10+6chi(2)  [PROVED, NEW — Round 31]
Tr_T(Km A)(p) = a_p(f), no twist                     [PROVED, NEW — Round 31]
Shioda-Inose degree-2 mechanism as source of D(p)    [KILLED, structurally — Round 31]
Tr_T(X)(p) = chi(-1)*a_p(f)                          [BEST-MOTIVATED, two independent
        <-- BLOCKED HERE (D(p)=1-chi(-2) provably      lines of support now]
             O(1); must come from a bounded constant,
             not from any O(p) mechanism tried so far)
S(p) = chi(-1)(a_p(f)+p)   [master identity]          [COMPUTATIONALLY VERIFIED ONLY]
```

---

## 9. Files needed for Round 32

- **This checkpoint** (`notes/CHECKPOINT_AFTER_ROUND31.md`) — read first.
- `notes/round31_report.md` — full Shioda–Inose/Kummer derivation, the
  `O(p)`-vs-`O(1)` structural kill, and the bounded-constants lead.
- `scripts/round31_kummer_verify.py` — numerical verification of `N_E'`,
  `n_2`, and the `\mathbb F_{p^2}` construction (reusable for further
  Kummer-side checks if ever needed again, though that avenue is now
  closed for `D(p)` purposes).
- `notes/round27_report.md`, `scripts/round27_C3_and_ledger.py` — exact
  origin of the `N_{I_2^*}(p)=7p+1` and ledger derivation, needed to
  re-examine the `+1` constants per Round 32's planned strategy.
- `notes/round19_report.md` — origin of `N_{I_0^*}(p)=5p+1`'s `+1`.
- `notes/round22_report.md` — the 19-dimensional trivial-lattice
  construction, needed for the `NS(X)` hidden-class audit.

---

## 10. Repository status (checked just now, after Round 31)

Unchanged in kind: pre-existing content outside
`explorations/hypercuboid/` remains untouched. `explorations/hypercuboid/`
remains untracked, now also containing `notes/round31_report.md`,
`scripts/round31_kummer_verify.py`, and this checkpoint. No staged
changes, no commits made by this exploration. `hypercuboid.pdf` and all
unrelated repository content remain untouched.

---

NEXT SESSION STARTING POINT

D(p)=1-chi(-2) is now proved to be structurally O(1), and every O(p)-scale mechanism tried so far (Tr_NS, Tr_T, Shioda-Inose/Kummer quotient combinatorics) has been shown incapable of producing it. Round 32 should audit, one at a time and from first principles, every bounded constant in the proved chain: the Lefschetz "+1", and the "+1" constants in N_{I_2^*}(p)=7p+1 and N_{I_0^*}(p)=5p+1. Secondarily, check whether NS(X)'s 19-dimensional trivial lattice hides a chi(-2)-twisted summand, informed by the A-side Gamma_{sqrt(-2)} analogy from Round 31. Do not revisit the Shioda-Inose/Kummer degree-2 mechanism (killed) or re-audit local fiber point-count geometry (exhaustively closed).

PAUSED AFTER ROUND 31 — READY FOR ROUND 32
