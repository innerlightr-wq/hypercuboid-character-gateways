# CHECKPOINT — Hypercuboid Arithmetic Exploration, after Round 26

Supersedes `CHECKPOINT_AFTER_ROUND25.md`. Read this file first; consult
individual `round<N>_report.md` files only for derivation detail.
Sections 1–4, 8–10 carry forward essentially unchanged from Round 25's
checkpoint; §§5–7 are updated with Round 26's findings.

---

## 1. Current PROVED results (unchanged core, plus one new item)

All of Round 25's checkpoint §1 stands: Gateways A–G; `Σ_I(p)=(p-1)S(p)`;
`S(p)=#V(F_p)-p^2`; minimal Weierstrass model, K3 classification (`e=24`);
full `(\mathbb Z/2)^2` torsion; trivial lattice rank 19; `t=1`,`t=-1` fully
resolved; `t=0/\infty` multiplicity-1 layer (identity,`N`,`F_1`,`F_2`)
built and torsion-assigned; `P\cdot O=0` forced for height 1; all 23
`\mathbb Q(t)` height-1 patterns eliminated; the 4 `\mathbb Q(i)(t)` sections
= one torsion orbit of a height-1 non-torsion generator;
`\rho(X_{\overline{\mathbb Q}})=20`; `|\mathrm{disc}(NS)|=8`;
`T(X)\cong\mathrm{diag}(2,4)`; `\sigma(P_1)=-P_1`;
$$\boxed{\mathrm{Tr}_{NS}(p) = (19+\chi(-1))\,p \quad\text{EXACTLY, PROVED.}}$$
(Round 25 additions, unchanged: `C_1,C_2` interior components built;
`N,F_1,F_2` shown to arise from nondegenerate-ternary-quadratic-form
ordinary nodes, hence unconditionally `\mathbb F_p$-rational for every odd
`p`, Hessian determinant `=-2` in every case checked.)

**NEW this round (Round 26):**
- **PROVED**: the **identity component** is explicitly constructed
  (standard chart `u=X/Y,v=1/Y` near `O`, equation
  `H(t,u,v)=v-u^3-a_2u^2v-a_4uv^2=0`) and is **smooth at every finite
  point** at `t=0` (`\partial H/\partial v=1` identically — not merely at
  `u=0`). No blow-up is needed on the identity side.
- **PROVED**: the **identity–`C_1` junction is clean** (Case A: already
  smooth and transverse). Identity meets `C_1` exactly at `u=x_1=\infty`,
  and this point was independently verified smooth from *both* sides
  (identity's own chart, and `C_1`'s second chart from Round 25,
  `\partial G_2/\partial X=-1\ne0`). **This rules out the identity side as
  the location of the missing seventh component.**
- **NEW, LOCATED, NOT YET RESOLVED**: `C_2` (Round 25's second interior
  node) has a **third marked point, `A=\infty`** (equivalently `t_3=0`
  in the chart `t=x_1t_3,y_1=x_1y_3`), which was **never checked in
  Round 25** — and it **is singular**
  (`\partial G_3/\partial x_1|_{x_1=0,y_3=0}=-t_3(t_3+1)$, vanishing at
  `t_3=0` **and** `t_3=-1`, the latter matching the already-known
  `A=-1$ node). **This is now the leading, concrete, well-located
  candidate for where the missing seventh `I_2^*` component hides.**

---

## 2. Computationally verified but NOT proved (unchanged)

Master identity `S(p)=\chi(-1)(a_p(f)+p)`, equivalently
`S(p)=-\chi(2)p+\chi(-1)a_p(E)^2` for `E:y^2=x^3+4x^2+2x`, `f=`LMFDB
**8.3.d.a**. Verified exactly `3\le p<500`, cross-checked against raw
LMFDB data, zero exceptions. **Status: NOT proved** — gap is geometric
(§5), not numerical.

---

## 3. Important corrections and KILLED hypotheses — DO NOT RETRY

All of Round 25's checkpoint §3 stands unchanged (rational-surface
hypothesis; `t=-1` misconception; pointwise-substitution proof attempts;
height-1 `\mathbb Q(t)`-section; Round-20 "6 candidates" miscount; "simple
root automatically smooth" folklore; "`I_2` is a tree"; "missing second
fork near identity" — false alarm; `I_0^*` "hidden elliptic curve" —
false alarm; shallow `X=tX'` with `Y` unscaled).

**NEW this round:**
- **KILLED (a specific, concrete Round-25/26 hypothesis)**: "the missing
  seventh component hides at the identity–`C_1` junction." **Directly
  ruled out** — that junction is smooth and transverse, checked from
  both sides.

---

## 4. Current geometric state

**Weierstrass model** (unchanged since Round 11):
$$y^2 = t(t+1)^2\,x^2\ \text{term form: } y^2=x^3+t(t+1)^2x^2+t^3(t+1)^2x$$
Bad fibers: `I_2^*(0), I_2(1), I_0^*(-1), I_2^*(\infty)`.

- `t=1` (`I_2`): COMPLETE (unchanged).
- `t=-1` (`I_0^*`): COMPLETE (unchanged).
- `t=0`/`t=\infty` (`I_2^*` each): multiplicity-1 layer COMPLETE
  (identity, `N`, `F_1`, `F_2` — identity now independently constructed
  and verified this round). **Interior chain: `C_1` fully resolved
  (valence 3: identity, `N`, `C_2` — all three junctions now checked);
  `C_2` has a newly-found unresolved singular point at `A=\infty`; the
  third interior component (if distinct from `C_2` itself) has not yet
  been constructed.**

---

## 5. Exact current bottleneck (read this first when resuming)

> **The immediate unresolved task is:** resolve `C_2`'s singular point
> at `A=\infty` (equivalently `t_3=0` in the chart
> `t=x_1t_3,\ y_1=x_1y_3`, giving
> `G_3=y_3^2-x_1t_3(t_3+1)-x_1^2[\cdots]-x_1^3[\cdots]`, singular at
> `(x_1,t_3,y_3)=(0,0,0)`), via the same ordinary-blow-up-plus-Hessian
> method used successfully four times already (Rounds 25–26).

**Key open question to resolve alongside the blow-up itself**: is this
`A=\infty` singularity a **genuinely new, distinct** third interior
component (giving the expected chain `C_1{-}C_2{-}C_3{-}\{F_1,F_2\}`,
7 components total), or does it turn out to be **the same underlying
locus as the already-known `A=-1` node** seen from a different chart
(in which case the graph interpretation needs correcting rather than
extending)? **Do not assume either answer — determine it explicitly.**

The identity side is now **fully closed off** (§1/§3) — do not re-check
it without a specific new reason. Nothing else is currently blocking —
everything in §1 above `\mathrm{Tr}_{NS}(p)` is already PROVED.

---

## 6. Round-26 outcome (for continuity)

- Explicitly constructed the identity component (`u,v` chart) and
  proved it smooth everywhere at `t=0` — a genuine gap filled, not
  merely asserted as in all prior rounds.
- Proved the identity–`C_1` junction is clean (Case A) — the round's
  top-priority suspected location for the missing component, directly
  ruled out.
- Applying the same adversarial "check the other chart too" discipline
  to `C_2` (which had only ever been examined in its first chart, `A`
  finite) immediately surfaced a genuine, previously-missed singular
  point at `A=\infty`.
- This new singularity was **not** resolved this round (time did not
  permit the further blow-up and disentangling its relation to the
  known `A=-1` node).
- Therefore Round 26 ended with verdict **ROUND26-D** (`I_2^*` geometry
  itself remains unresolved), with the search space narrowed further
  and a single, concrete, well-located next target identified.

---

## 7. Planned Round 27 strategy

**Primary next step**: resolve `C_2`'s `A=\infty` (`t_3=0`) singular
point via an ordinary blow-up, exactly as done for the `A=0` and
`A=-1$ points in Round 25 (find the leading quadratic form in
`(x_1,t_3,y_3)`, check its Hessian determinant for nondegeneracy, blow
up if nondegenerate, and determine whether the resulting exceptional
locus is a genuinely new component or coincides with something already
found).

**Then**: reassemble the full component list, check it has exactly 7
members forming a tree with 6 edges, verify the Euler-number identity
`2\times7-6=8` directly from the explicit intersection graph (not
assumed), and recover the component group `(\mathbb Z/2)^2` from the
explicit structure.

**Do not** re-examine the identity–`C_1` junction (closed, §3) or
re-attempt the killed `Y`-unscaled `X=tX'` substitution.

**Escape hatch** (still available, unused): cite rigorous minimal-
regular-model/Tate's-algorithm theory if explicit construction stalls
again on this specific point, with an explicit correspondence to the
divisors already built.

Once the seven-component structure is confirmed, proceed exactly as
previously planned: derive `N_0(p)`, cross-check `t=\infty`, close the
`C_A(p)=C_B(p)` bookkeeping, then solve for `\mathrm{Tr}_T(p)` and
compare against `8.3.d.a` without curve-fitting.

---

## 8. Logical dependency chain (unchanged)

```
hypercuboid character sum (n=4 zero-sector)         [PROVED — Rounds 1–9]
S_I(p) = (p-1) S(p)                                  [PROVED — Round 9/10]
S(p) = #V(F_p) - p^2                                 [PROVED — Round 10]
K3 surface X (Weierstrass model, fibers, e=24)       [PROVED — Round 11]
rho(X_Qbar)=20 ; |disc NS|=8 ; T(X)=diag(2,4)        [PROVED — Round 21]
Tr_NS(p) = (19+chi(-1)) p                            [PROVED — Round 22]
Tr_T(p) = ?  <-- BLOCKED HERE (I_2^* interior chain:  [OPEN — Rounds 22-26,
                 identity side now CLOSED; C_2's       further narrowed
                 A=infinity point is the new target]   Round 26]
modular twist vs. newform 8.3.d.a                    [OPEN, not curve-fit]
S(p) = chi(-1)(a_p(f)+p)   [master identity]          [COMPUTATIONALLY VERIFIED ONLY]
```

---

## 9. Files needed for Round 27

- **This checkpoint** (`notes/CHECKPOINT_AFTER_ROUND26.md`) — read first.
- `notes/round26_report.md`, `scripts/round26_identity_junction.py` —
  identity construction, the clean junction proof, and the newly-found
  `C_2` `A=\infty` singularity (exact equation given, ready to blow up).
- `notes/round25_report.md`, `scripts/round25_ordinary_blowups.py` —
  `C_1,C_2` construction and the three successful Hessian-verified node
  resolutions (method template, apply directly to the new point).
- `notes/round17-19_report.md` — original multiplicity-1 constructions.
- `notes/round22-24_report.md` — point-count bookkeeping history.
- `scripts/core.py` — unrelated to the bottleneck, available if needed.

---

## 10. Repository status (checked just now, after Round 26)

Unchanged in kind from prior checkpoints: pre-existing Phase-1 (KV-cache)
files outside `explorations/hypercuboid/` remain untouched by this
exploration. `explorations/hypercuboid/` remains untracked, now also
containing `notes/round26_report.md`,
`scripts/round26_identity_junction.py`, and this checkpoint. No staged
changes, no commits made by this exploration. `hypercuboid.pdf` and all
unrelated repository content remain untouched.

---

NEXT SESSION STARTING POINT

Resolve C_2's newly-found singular point at A=infinity (t_3=0 in the chart t=x_1*t_3, y_1=x_1*y_3, equation G_3=y_3^2-x_1*t_3*(t_3+1)-... ) via an ordinary blow-up (compute the leading quadratic form, check its Hessian determinant, blow up if nondegenerate), determine whether it is a genuinely new third interior component or coincides with the already-known A=-1 node, then reassemble and verify the complete seven-component I_2^* fiber (Euler number 8, component group (Z/2)^2) before returning to the affine/projective bookkeeping and the master identity.

PAUSED AFTER ROUND 26 — READY FOR ROUND 27
