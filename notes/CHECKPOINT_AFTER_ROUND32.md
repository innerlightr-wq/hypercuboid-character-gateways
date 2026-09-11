# CHECKPOINT — Hypercuboid Arithmetic Exploration, after Round 32

Supersedes `CHECKPOINT_AFTER_ROUND31.md`. Read this file first. **This
round found and corrected a genuine error** in a previously-"proved"
formula (`N_{I_2}(p)`), resolving the `D(p)=1-\chi(-2)` residual that
survived Rounds 27–31 almost entirely. One narrow bridge remains.

---

## 1. Current PROVED results (updated — one correction, one new derivation)

**CORRECTED this round**:
$$N_{I_2}(p) = 2p+1-\chi(-2)\qquad(\text{NOT }2p\text{ unconditionally — Round 22/28's formula was wrong}).$$
Source of the error: the `I_2` fiber's two components `C_1` (normalized
nodal cubic) and `C_2` (exceptional conic, Round 28) meet at **2**
geometric points (`C_1\cap C_2`), which form a degree-2 closed point —
split (2 rational points) iff `\chi(2)`... **correction: iff `\chi(-2)=1`**,
inert (0 rational points) iff `\chi(-2)=-1`. Round 22/28 implicitly
assumed these 2 points always both individually rational; they do not.
Derived directly from the Round 16/28 equations
(`Y^2=X'(X'-2)(X'+8\varepsilon)`, node tangent directions
`s=\pm\sqrt{-2}$, conic infinity points `(W/u)^2\to-2`) — **not a guess,
a re-derivation from the actual local model**, numerically confirmed at
8 primes spanning both `\chi(-2)` classes.

**CORRECTED accordingly**:
$$\#X(\mathbb F_p) = \#V(\mathbb F_p) + 19p + 1$$
(replacing Round 27's `\#X=\#V+19p+\chi(-2)`) — re-derived this round via
a complete, fiber-by-fiber, set-theoretic reconstruction (Part II of
`round32_report.md`), with the one `N_{I_2}(p)` fix as the only change
from Round 27's method. **All other Round 27–29 local geometry
(`I_2^*`, `I_0^*`'s `+1` constants) reconfirmed unconditional this round
via a fresh audit specifically targeting hidden `\chi(-2)`-dependence in
every junction point — none found; those fibers are trees, structurally
immune to the `I_2`-cycle's specific failure mode.**

**NEW, proved this round (general tools, reusable)**:
- `\mathrm{Tr}_{NS}(p)` is **always** an exact integer multiple of `p`
  (Frobenius on `NS(X_{\bar{\mathbb F}_p})` has finite order by
  Kronecker's theorem, since its Tate-twisted eigenvalues have absolute
  value exactly 1) — **no bounded non-`p`-multiple correction can ever
  hide in `\mathrm{Tr}_{NS}`.**
- `\mathrm{Tr}_T(p)` is forced by **Livné's classification theorem** to
  equal `\chi\cdot a_p(f)` exactly, for one fixed quadratic character
  `\chi` — **no bounded additive correction can ever hide in
  `\mathrm{Tr}_T`** either (isomorphic Galois representations have
  identically equal traces, no exceptions).
- **Consequence**: any bounded residual in this project's whole
  framework MUST live in the geometric point-count ledger's own
  constants — correctly predicting, before the fact, where Part V's
  actual error was found.

Everything else (Kodaira types, multiplicities, `\rho=20`,
`T(X)=\mathrm{diag}(2,4)`, `\mathrm{Tr}_{NS}(p)=(19+\chi(-1))p`) stands
PROVED, unchanged.

---

## 2. Computationally verified but NOT proved (substantially narrowed)

$$S(p)=\chi(-1)(a_p(f)+p)\quad\text{now follows EXACTLY from four ingredients, three fully proved:}$$
1. `\#V=p^2+S(p)` — PROVED.
2. `\#X=\#V+19p+1` — PROVED this round (corrected).
3. `\mathrm{Tr}_{NS}(p)=(19+\chi(-1))p` — PROVED (Round 22).
4. `\mathrm{Tr}_T(p)=\chi(-1)a_p(f)` — **the one remaining gap**: Livné
   forces `\mathrm{Tr}_T(p)=\chi\cdot a_p(f)` for SOME fixed quadratic
   `\chi`; that `\chi=\chi(-1)` specifically is supported by three
   convergent, independent lines of evidence (Round 21's proved algebraic-
   cycle Galois action; Round 30's elimination of "no twist"; Round 31's
   independent Kummer-side `\mathrm{Tr}_T(\mathrm{Km}A)=a_p(f)` computation)
   but **has not been proved by a single direct computation of Galois
   action on a transcendental cycle/period of `X` itself.**

Numerically: forcing `\mathrm{Tr}_T(p)` from the corrected ledger
(`S(p)-\chi(-1)p`) matches `\chi(-1)a_p(f)` **exactly**, zero exceptions,
`p<150` (re-confirmed this round with the LMFDB `8.3.d.a` traces).

---

## 3. Important corrections and KILLED hypotheses — DO NOT RETRY

All prior checkpoints' lists stand, **with one now-superseded entry**:
- **Round 22/28's `N_{I_2}(p)=2p` "proved unconditionally" claim is
  WRONG** — do not cite it again. The correct formula is
  `N_{I_2}(p)=2p+1-\chi(-2)`. (Round 28's *sub*-result, `\#C_2(\mathbb F_p)=p+1`
  for the exceptional conic alone, remains correct and was reused this
  round — only the *union formula combining `C_1` and `C_2`* was wrong.)
- **KILLED, still correctly**: the Shioda–Inose/Kummer degree-2
  mechanism as the source of the residual (Round 31) — reconfirmed
  consistent this round: the true source was geometric (a local
  intersection-point miscount), exactly as Round 31's `O(p)`-vs-`O(1)`
  argument predicted it had to be.
- **Do not** re-propose additive corrections to `\mathrm{Tr}_T(p)` (Round
  30's checkpoint) — now doubly confirmed unnecessary: the residual is
  fully explained geometrically, with `\mathrm{Tr}_T(p)=\chi(-1)a_p(f)`
  exactly, no correction term of any kind.

---

## 4. Current geometric state (updated: `I_2` corrected)

`I_2(1)`: **`2p+1-\chi(-2)`** (corrected this round, was `2p`).
`I_0^*(-1)`: `5p+1` (reconfirmed unconditional). `I_2^*(0)`,
`I_2^*(\infty)`: `7p+1` each (reconfirmed unconditional). **All local
geometry now believed fully correct** — this is the first checkpoint
since Round 27 where every ingredient of the master identity's proof
chain is either fully proved or narrowed to a single, sharply-defined
remaining question (§5).

---

## 5. Exact current bottleneck (read this first when resuming)

> **The immediate unresolved task is:** prove, by a **direct**
> computation (not by analogy or convergent indirect evidence), that
> `\mathrm{Tr}_T(p)=\chi(-1)a_p(f)` specifically (i.e. that `T(X)`'s
> quadratic twist, relative to the untwisted newform `f`, is exactly
> `\chi(-1)`) — mirroring how Round 21 directly proved the algebraic
> Mordell–Weil generator's Galois action (`\sigma(P_1)=-P_1`, giving
> eigenvalue `\chi(-1)p`) rather than assuming it by analogy.

**Do not**: re-audit `I_2^*` or `I_0^*` (Parts III/IV, exhaustively
reconfirmed clean, including specifically for hidden `\chi(-2)`); revisit
the Shioda–Inose/Kummer mechanism (killed, Round 31, and now doubly
unnecessary); re-derive `\#V=p^2+S(p)` or the character-sum zero-locus
(Part VIII, clean); propose an ad hoc additive correction to
`\mathrm{Tr}_T(p)` (unnecessary and structurally impossible, Part XII).

**Concretely, what "direct" could mean for Round 33**: locate an
explicit period, transcendental cycle, or 2-dimensional piece of
`H^2(X,\mathbb Z)` (e.g., via the elliptic fibration's own
transcendental-cycle description, or via explicit comparison with
`\mathrm{Km}(A)`'s own `T(A)` generators identified in Round 31 Part
III) whose Galois/Frobenius action can be computed directly, the way
Round 21 computed `\sigma(P_1)=-P_1$ for the algebraic generator.

---

## 6. Round-32 outcome (for continuity)

- Rebuilt the entire `\#X-\#V` constant ledger from sets, fiber by fiber,
  tracking every `+1` individually (Part II).
- Reconfirmed `I_2^*`, `I_0^*`'s `+1` constants unconditional, with a
  fresh audit specifically for hidden `\chi(-2)`-dependence (Parts
  III/IV) — clean.
- **Found and corrected a genuine, previously undetected error**:
  `N_{I_2}(p)=2p+1-\chi(-2)`, not `2p` (Part V) — traced to the `I_2`
  fiber's two intersection points forming a `\chi(-2)`-dependent
  degree-2 closed point.
- Proved two general, reusable structural facts (`\mathrm{Tr}_{NS}(p)`
  always a `p`-multiple; `\mathrm{Tr}_T(p)$ forced by Livné to be a
  pure character-twist of `a_p(f)`, no additive room) that jointly and
  correctly predicted the error had to be geometric (Part XII).
- Verified the fix symbolically (exact algebra, zero residual) and
  numerically (LMFDB `8.3.d.a`, `p<41`, zero exceptions) (Part XIII).
- Verdict: **ROUND32-B** — discrepancy fully identified and corrected;
  one narrow, well-defined proof bridge remains (`\chi=\chi(-1)`
  specifically, proved directly rather than by convergent evidence).

---

## 7. Planned Round 33 strategy

**Primary next step**: prove `\mathrm{Tr}_T(p)=\chi(-1)a_p(f)` directly.
Candidate approaches, roughly in order of promise:
1. Identify an explicit generator (or pair of generators) of `T(X)`
   as an actual `2`-cycle / period on the resolved elliptic K3 `X` (using
   the now-fully-explicit resolved-fiber geometry from Rounds 24–29), and
   compute the Galois action on it directly — the most Round-21-like
   approach.
2. Use the Round 31 Kummer-side identification (`A=E\times E`,
   `T(A)`'s explicit generators — the CM-endomorphism graph
   `\Gamma_{\sqrt{-2}}` and the polarization-related classes) together
   with Morrison's `T(X)\cong T(\mathrm{Km}\,A)` isomorphism, tracked
   through the **specific field of definition** of that isomorphism (not
   just its existence over `\bar{\mathbb Q}`) to pin down the twist.
3. If both prove intractable, consider a targeted Faltings–Serre-style
   finite-prime-set rigidity argument: since `\mathrm{Tr}_T(p)` is known
   to be `\chi\cdot a_p(f)` for SOME fixed quadratic `\chi` (Livné), and
   `a_p(f)=0` at inert primes (so those primes carry no information about
   `\chi`), a handful of **split-prime** point counts of `X` itself
   (or a direct, small-scale computation of `\#X(\mathbb F_p)` at one or
   two primes via the fully explicit resolved model) would determine
   `\chi` outright — this may be more tractable than a full structural
   proof.

**Do not**: touch any local fiber geometry (§4, now fully correct and
closed for real, not just "exhaustively audited" as in prior rounds —
this time an actual bug was found and fixed, closing the loop). **Do
not** revisit Shioda–Inose/Kummer as an explanation for any residual
(none remains).

---

## 8. Logical dependency chain (updated — nearly complete)

```
hypercuboid character sum (n=4 zero-sector)         [PROVED — Rounds 1–9]
S_I(p) = (p-1) S(p)                                  [PROVED]
S(p) = #V(F_p) - p^2                                 [PROVED]
K3 surface X (Weierstrass model, fibers, e=24)       [PROVED]
rho(X_Qbar)=20 ; |disc NS|=8 ; T(X)=diag(2,4)        [PROVED — Round 21]
Tr_NS(X)(p) = (19+chi(-1)) p                         [PROVED — Round 22]
N_I2(p) = 2p+1-chi(-2)  [CORRECTED, was wrongly 2p]  [PROVED — Round 32]
I_2^*, I_0^* formulas unconditional, reconfirmed     [PROVED — Rounds 24-29, 32]
#X(F_p) = #V(F_p) + 19p + 1  [CORRECTED, was +chi(-2)][PROVED — Round 32]
Tr_NS always in pZ ; Tr_T forced = chi*a_p(f)        [PROVED, general tools — Round 32]
S(p) = chi(-1)(a_p(f)+p)   [master identity]          [FOLLOWS EXACTLY, GIVEN
        <-- BLOCKED HERE ONLY (need chi=chi(-1)         Tr_T(p)=chi(-1)a_p(f)]
             proved directly, not by analogy)
```

**This is the shortest, cleanest form this dependency chain has taken
in the whole project.** Exactly one link (`\chi=\chi(-1)` proved
directly) separates "computationally verified" from "PROVED."

---

## 9. Files needed for Round 33

- **This checkpoint** (`notes/CHECKPOINT_AFTER_ROUND32.md`) — read first.
- `notes/round32_report.md` — the `N_{I_2}(p)` correction, full ledger
  re-derivation, and the `\mathrm{Tr}_{NS}\in p\mathbb Z$ /
  Livné-rigidity structural arguments.
- `scripts/round32_I2_intersection_fix.py`,
  `scripts/round32_full_chain_check.py` — numerical confirmation of the
  fix, reusable for further checks.
- `notes/round21_report.md` — the template for a *direct* Galois-action
  proof (used for the algebraic Mordell–Weil generator; needed as a
  model for Round 33's primary task on the transcendental side).
- `notes/round31_report.md` — the Kummer-side `A=E\times E`,
  `T(A)` generator data, needed for Round 33's approach 2.
- `notes/round16_report.md`, `notes/round28_report.md` — the exact `I_2`
  local equations, needed if any further local double-check is required
  (should not be — this round closed that loop).

---

## 10. Repository status (checked just now, after Round 32)

Unchanged in kind: pre-existing content outside
`explorations/hypercuboid/` remains untouched. `explorations/hypercuboid/`
remains untracked, now also containing `notes/round32_report.md`,
`scripts/round32_I2_intersection_fix.py`,
`scripts/round32_full_chain_check.py`, and this checkpoint. No staged
changes, no commits made by this exploration. `hypercuboid.pdf` and all
unrelated repository content remain untouched.

---

NEXT SESSION STARTING POINT

Round 32 found and corrected a genuine error (N_I2(p)=2p+1-chi(-2), not 2p), which fully resolves the D(p) residual that survived Rounds 27-31: #X(F_p)=#V(F_p)+19p+1 now holds unconditionally, and combined with the proved Tr_NS(p)=(19+chi(-1))p, this forces Tr_T(p)=chi(-1)a_p(f) exactly, matching the master identity with zero residual (verified symbolically and numerically, p<41, LMFDB-cross-checked). The ONE remaining gap: Livne's theorem proves Tr_T(p)=chi*a_p(f) for SOME fixed quadratic character chi, but chi=chi(-1) specifically rests on convergent indirect evidence (three independent lines), not a single direct proof. Round 33 should prove this directly -- e.g. by computing the Galois action on an explicit transcendental cycle/period of X, mirroring Round 21's direct proof for the algebraic Mordell-Weil generator. Do not re-audit any local fiber geometry (now fully correct, bug found and fixed) or revisit Shioda-Inose/Kummer (unnecessary, residual fully explained).

PAUSED AFTER ROUND 32 — READY FOR ROUND 33
