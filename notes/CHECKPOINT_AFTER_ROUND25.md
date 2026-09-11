# CHECKPOINT — Hypercuboid Arithmetic Exploration, after Round 25

This supersedes `CHECKPOINT_AFTER_ROUND24.md` for resuming work. Read
this file first; consult individual `round<N>_report.md` files only for
derivation detail on a specific point. Sections 1–4, 8–10 below carry
forward Round 24's checkpoint essentially unchanged (all still PROVED/
unchanged); §§5–7 are updated with Round 25's findings.

---

## 1. Current PROVED results (unchanged from Round 24's checkpoint)

**Elementary/structural layer (Rounds 1–9):** Gateways A, B, C, E, F, G,
each with a proved scope; n=4 classification reduced to Class I via
Gateway G. **Class-I reduction (Rounds 9–11):** `Σ_I(p)=(p-1)S(p)`;
`S(p)=#V(F_p)-p^2` for `V:Y^2=X(X+1)T(T+1)(X+T)`; minimal Weierstrass
model, Kodaira fibers, `e=24` (K3, not rational); full `(\mathbb Z/2)^2`
torsion. **Geometric/arithmetic layer (Rounds 14–22):** trivial lattice
rank 19, `|\mathrm{disc}|=128`; `t=1` and `t=-1` fully resolved; `t=0/\infty`
multiplicity-1 layer (identity,`N`,`F_1`,`F_2`) fully resolved and
torsion-assigned; `P\cdot O=0` forced for height 1; all 23 `\mathbb Q(t)`
height-1 patterns exhaustively eliminated; the 4 distinct `-q(t)^2`
polynomials are genuine `\mathbb Q(i)(t)` sections forming one torsion
orbit of a height-1 non-torsion generator; `\rho(X_{\overline{\mathbb Q}})=20`;
`|\mathrm{disc}(NS)|=8`; `T(X)\cong\mathrm{diag}(2,4)`; `\sigma(P_1)=-P_1`;
$$\boxed{\mathrm{Tr}_{NS}(p) = (19+\chi(-1))\,p \quad\text{EXACTLY, PROVED.}}$$
(Full derivations: see `CHECKPOINT_AFTER_ROUND24.md` §1, unchanged.)

**NEW this round (Round 25) — partial, general arithmetic result:**
- **PROVED**: every exceptional conic obtained by blowing up an
  ordinary node of this surface (specifically: the three found so far,
  matching `N,F_1,F_2`'s neighboring singularities) is **unconditionally
  `\mathbb F_p`-rational for every odd prime `p`**, via the classical fact
  that a nondegenerate ternary quadratic form over any finite field is
  isotropic. Verified via explicit Hessian-determinant computation
  (`=-2\ne0` in every case checked) at each of the 3 nodes resolved this
  round.
- **PROVED**: two new interior (multiplicity-2) components of `I_2^*`,
  `C_1` and `C_2`, explicitly constructed via genuine ordinary
  (non-weighted) blow-ups and verified smooth by exact Jacobian
  computation (away from their own marked singular points, which were
  then further resolved). `C_1` connects identity, `N`, and `C_2`
  (valence 3); `C_2` connects `C_1`, `F_1`(`=M_b`), `F_2`(`=M_c`)
  (valence 3).
- **NOT proved / incomplete**: assembling `\{O,N\}\!-\!C_1\!-\!C_2\!-\!\{F_1,F_2\}`
  gives only **6 components, 5 edges** — this **fails** the Euler-number
  cross-check (`2\cdot6-5=7\ne8=e(I_2^*)`). A **third interior node is
  still missing** (or hidden structure remains at `C_1`'s meeting point
  with the never-separately-constructed "identity" chart). See §5.

---

## 2. Computationally verified but NOT proved (unchanged)

**Master identity**: `S(p)=\chi(-1)(a_p(f)+p)`, equivalently
`S(p)=-\chi(2)p+\chi(-1)a_p(E)^2` for `E:y^2=x^3+4x^2+2x` and `f=`LMFDB
**8.3.d.a**. Verified exactly at every prime `3\le p<500`, cross-checked
against raw LMFDB API data, zero exceptions, all four mod-8 classes
including `p=3`. **Status: NOT proved** — the gap is geometric (§5), not
numerical. Also unproved: the Sym²-decomposition relation
`a_p(f)=a_p(E)^2-p(1+\chi(-2))` (standard mechanism, checked against
real data, not independently re-derived from a cited theorem here).

---

## 3. Important corrections and KILLED hypotheses — DO NOT RETRY

All of Round 24's checkpoint list stands unchanged (rational-surface
hypothesis; `t=-1` singular-fiber misconception; pointwise-substitution
proof attempts; height-1 `\mathbb Q(t)`-section; Round-20 "6 candidates"
miscount — corrected to 4; "simple-root automatically smooth" folklore;
"`I_2` is a tree" — it's a 2-cycle; "missing second fork near identity"
— false alarm, resolved Round 24; `I_0^*` "hidden elliptic curve" —
false alarm, resolved Round 23).

**NEW this round:**
- **KILLED**: the shallow substitution `X=tX'` with `Y` *unscaled* was
  already known singular (Round 24). This round used the **correctly
  scaled** ordinary blow-up (`X=t\,x_1,\ Y=t\,y_1`, i.e. scaling **both**
  `X` and `Y` by `t` together) and it worked — do not confuse these two;
  the fix was scaling `Y` too, not merely retrying `X` alone.
- **DISFAVORED (not fully killed, but strongly undermined)**: Round 23's
  leading hypothesis that a **quadratic-extension interior component**
  is the source of the Round-22/23 point-count discrepancy. Every
  interior/exceptional component actually constructed this round
  (`C_1,C_2,M_a,M_b,M_c`) is unconditionally rational — if the still-
  missing third node is also rational (likely, by the same mechanism),
  the discrepancy's true source lies elsewhere (see §5's "most likely
  next step").

---

## 4. Current geometric state

**Weierstrass model** (unchanged since Round 11):
$$y^2 = x^3 + t(t+1)^2\,x^2 + t^3(t+1)^2\,x$$
Bad fibers: `I_2^*(0), I_2(1), I_0^*(-1), I_2^*(\infty)`.

- **`t=1` (`I_2`)**: COMPLETE (unchanged).
- **`t=-1` (`I_0^*`)**: COMPLETE (unchanged).
- **`t=0`/`t=\infty` (`I_2^*` each)**: multiplicity-1 layer COMPLETE
  (unchanged: identity, `N`, `F_1`, `F_2`). **Interior chain: 2 of 3
  components now explicitly built** (`C_1,C_2`, new this round, both
  rational, both verified smooth away from their own marked points) —
  **one interior component (or one hidden sub-structure) still missing.**

---

## 5. Exact current bottleneck (read this first when resuming)

> **The immediate unresolved task is:** find the **third** interior
> multiplicity-2 component of the `I_2^*` resolution at `t=0` (the
> assembled graph `\{O,N\}\!-\!C_1\!-\!C_2\!-\!\{F_1,F_2\}` has only
> 6 components/5 edges and **fails** the Euler-number check,
> `2\cdot6-5=7\ne8`).

**Most promising concrete lead (identified this round, not yet
pursued)**: `C_1` was verified smooth at its meeting point with
"identity" (`x_1=\infty`, checked via `C_1`'s own second chart,
`\partial G_2/\partial X\ne0$ at `t_2=0`) — but **"identity" itself (the
strict transform of the naive curve, e.g. via `s=Y/X` normalization) was
never independently constructed or checked for smoothness at *its own*
end of that same meeting point.** A hidden node could live exactly
there, not yet ruled out.

This gap continues to block closing the Round-22/23 affine-to-projective
bookkeeping and, downstream, `\mathrm{Tr}_T(p)`, the modular twist, and
the master identity. **Nothing else is currently blocking** — everything
in §1 above `\mathrm{Tr}_{NS}(p)` is already PROVED.

**Positive update from this round**: the likely *nature* of the missing
piece is now much better constrained — it is very likely a further
**unconditionally-rational** ordinary-node-type component (matching the
pattern of everything found so far), **not** a quadratic-extension
phenomenon as Round 23 suspected. If so, once found, the "7p+1"-style
tree formula is likely to be confirmed correct, and Round 22/23's
residual discrepancy will need to be traced to the naive-count/
bookkeeping arithmetic itself, not to fiber-component rationality.

---

## 6. Round-25 outcome (for continuity)

- Successfully performed genuine **ordinary** (non-weighted) blow-ups
  for the first time (per the round's explicit instruction), correcting
  Round 24's failed attempt by scaling **both** `X` and `Y` by `t`
  together (not `X` alone).
- Found and verified smooth **two new interior components** `C_1,C_2`,
  each of valence 3, via exact Jacobian checks.
- Found and verified **three exceptional conics** (`M_a{=}N`,
  `M_b{=}F_1`, `M_c{=}F_2`) all arise from **nondegenerate ternary
  quadratic form** singularities, hence are **unconditionally
  `\mathbb F_p`-rational** (Hessian determinant `=-2` in every case) — a
  clean, general, valuable new fact.
- **Assembled graph fails the Euler-number check by exactly one
  component/edge** — caught by the round's own required adversarial
  check, correctly preventing a premature "resolution complete" claim.
- Therefore Round 25 ended with verdict **ROUND25-D** (`I_2^*` arithmetic
  itself remains unresolved), with substantially more built than at the
  start and a sharply narrowed, concrete next lead.

---

## 7. Planned Round 26 strategy

**Primary next step**: explicitly construct "identity" (the strict
transform of the naive singular curve `Y^2=X^3` at `t=0`, e.g. via
`s=Y/X`, `X=s^2\cdot(\text{unit})`-type normalization adapted to the
full surface, not just the curve) as its **own** chart, and check its
Jacobian/smoothness **at the specific point where it should meet `C_1`**
(`x_1=\infty` in `C_1`'s parametrization). If a further singularity is
found there, resolve it via the same ordinary-blow-up-plus-Hessian-check
method that worked cleanly three times this round.

**If that specific point turns out smooth too** (no hidden node),
reconsider whether the abstract "3 interior nodes" expectation itself
needs re-examination for this specific surface (e.g., whether the
`\{O,N\}` fork's shared attachment might not require its own separate
first-chain-node the way generic affine-`D_6` diagrams assume — though
note this would be surprising given the Euler-number arithmetic is a
hard, unconditional constraint that must be satisfied somehow).

**Do not** re-attempt the already-killed `Y`-unscaled `X=tX'` substitution
(Round 24) — the working method this round scaled `Y=t\,y_1` alongside
`X=t\,x_1` from the start.

**Escape hatch** (unused so far, still available): cite rigorous
minimal-regular-model/Tate's-algorithm theory for the missing piece if
explicit construction stalls again, clearly labeling theorem-derived
vs. explicitly-constructed facts.

Once the full 7-component structure is confirmed (Euler number 8,
component group `(\mathbb Z/2)^2` correctly reproduced), proceed exactly as
previously planned: derive `N_0(p)`, cross-check at `t=\infty`, close the
Round-22/23 `C_A(p)=C_B(p)` bookkeeping, then and only then solve for
`\mathrm{Tr}_T(p)` and compare against `8.3.d.a` without curve-fitting.

---

## 8. Logical dependency chain (unchanged from Round 24's checkpoint)

```
hypercuboid character sum (n=4 zero-sector)         [PROVED — Rounds 1–9]
        |  Gateways A,B,C,E,F,G
        v
S_I(p) = (p-1) S(p)                                  [PROVED — Round 9/10]
        |
        v
S(p) = #V(F_p) - p^2  (elliptic-family moment)       [PROVED — Round 10]
        |
        v
K3 surface X (Weierstrass model, fibers, e=24)       [PROVED — Round 11]
        |
        v
rho(X_Qbar)=20 ; |disc NS|=8 ; T(X)=diag(2,4)        [PROVED — Round 21]
        |
        v
Tr_NS(p) = (19+chi(-1)) p                            [PROVED — Round 22]
        |
        v
Tr_T(p) = ?  <-- BLOCKED HERE (I_2^* interior chain,  [OPEN — Rounds 22-25,
                 2 of 3 interior components now built] narrowed Round 25]
        |
        v
modular twist vs. newform 8.3.d.a                    [OPEN, not curve-fit]
        |
        v
S(p) = chi(-1)(a_p(f)+p)   [master identity]          [COMPUTATIONALLY VERIFIED ONLY]
```

---

## 9. Files needed for Round 26

- **This checkpoint** (`notes/CHECKPOINT_AFTER_ROUND25.md`) — read first.
- `notes/round25_report.md`, `scripts/round25_ordinary_blowups.py` —
  the full ordinary-blow-up derivation and code from this round (`C_1`,
  `C_2`, and the three Hessian-verified nondegenerate nodes); reuse the
  pattern directly for constructing "identity"'s own chart.
- `notes/round17_report.md`, `round18_report.md` — the original
  multiplicity-1 `I_2^*` constructions (`F_1,F_2` via `X=t^2X_1,Y=t^3Y_1`;
  `N` via `Y=t^2\tau`) — useful for cross-checking `M_a,M_b,M_c` against
  these prior labels.
- `notes/round19_report.md` — completed `I_0^*` resolution (template).
- `notes/round22_report.md`, `round23_report.md`, `round24_report.md` —
  full history of the point-count bookkeeping attempts and killed leads.
- `scripts/core.py` — foundational machinery, unrelated to the current
  bottleneck but available for any direct finite-field cross-check.

---

## 10. Repository status (checked just now, after Round 25)

- Unchanged in kind from Round 24's checkpoint: pre-existing Phase-1
  (KV-cache) modifications/untracked files outside
  `explorations/hypercuboid/` remain exactly as they were, **not touched
  by this exploration**.
- `explorations/hypercuboid/` remains untracked (as every round),
  containing the full `notes/`, `scripts/`, `results/` history plus this
  new checkpoint and Round 25's new files
  (`notes/round25_report.md`, `scripts/round25_ordinary_blowups.py`).
- **Staged changes**: none.
- **Commits made by this exploration**: none.
- **Confirmed**: `hypercuboid.pdf` and all unrelated repository content
  remain untouched.

---

NEXT SESSION STARTING POINT

Construct the strict-transform "identity" chart explicitly (e.g. via s=Y/X normalization) and check its Jacobian at the point where it meets C_1 (x_1=infinity), to determine whether the still-missing third I_2^* interior component hides exactly there. Resolve it with the same ordinary-blow-up-plus-Hessian-determinant method that worked three times in Round 25, then reassemble the seven-component fiber, verify the Euler number (8) and component group ((Z/2)^2), derive N_0(p), and only then return to closing the Round-22/23 affine/projective bookkeeping toward the master identity.

PAUSED AFTER ROUND 25 — READY FOR ROUND 26
