# CHECKPOINT — Hypercuboid Arithmetic Exploration, after Round 28

Supersedes `CHECKPOINT_AFTER_ROUND27.md`. Read this file first.
Sections 1–4 carry forward unchanged (all local geometry remains
PROVED and complete); §§5–7 updated with Round 28's negative-but-useful
findings.

---

## 1. Current PROVED results (unchanged from Round 27's checkpoint)

Everything through the complete `I_2^*`/`I_0^*`/`I_2` resolutions and
`N_{I_2^*}(p)=7p+1$, `N_{I_0^*}(p)=5p+1`, `N_{I_2}(p)=2p` stands PROVED
(see `CHECKPOINT_AFTER_ROUND27.md` §1 for the full list). The global
ledger identity
$$\#X(\mathbb F_p) = \#V(\mathbb F_p) + 19p + \chi(-2)$$
combined with `\mathrm{Tr}_{NS}(p)=(19+\chi(-1))p` gives
$$\boxed{D(p) = S(p)-\chi(-1)p-\mathrm{Tr}_T(p) = 1-\chi(-2)}$$
— still PROVED as the exact symbolic residual, still not identically
zero.

**NEW this round — two candidate sources of `D(p)` ruled out by exact
proof:**
- **PROVED**: the `t=1` (`I_2`) fiber's local resolution is **not** the
  source. Its tangent cone (`Y^2+2X'^2+16\varepsilon X'` in
  `(X',\varepsilon,Y)`) has Hessian determinant `-2^9`
  (`\chi(\det)=\chi(-2)`) — genuinely nondegenerate, hence
  unconditionally isotropic (Chevalley–Warning), so the exceptional
  conic is `\mathbf P^1` over every odd `\mathbb F_p`. The finer
  affine/infinity split of this conic **does** depend on `\chi(-2)`
  (`p-\chi(-2)` affine points, `1+\chi(-2)` points at infinity) but
  these **exactly cancel** to give the unconditional total `p+1`,
  confirmed exactly by the classical identity
  `\sum_u\chi(u(u+8))=-1` and numerically re-verified at 10 primes.
  `N_{I_2}(p)=2p$ is untouched by any `\chi(-2)`-dependence.
- **RULED OUT**: the `H^0`/`H^4` Lefschetz normalization
  (`\#X=1+p^2+\mathrm{Tr}(H^2)`) — both the `1` and `p^2` terms are
  unconditional, standard facts for any smooth projective surface, and
  were re-verified to be applied identically and correctly.

---

## 2. Computationally verified but NOT proved (unchanged)

Master identity `S(p)=\chi(-1)(a_p(f)+p)`, equivalently
`S(p)=-\chi(2)p+\chi(-1)a_p(E)^2`. **Status: NOT proved.** The gap
remains `D(p)=1-\chi(-2)`, now with two major candidate explanations
eliminated but the true source still unfound.

---

## 3. Important corrections and KILLED hypotheses — DO NOT RETRY

All prior checkpoints' lists stand. **NEW this round:**
- **KILLED (with full exact proof)**: the `t=1` node's split/non-split
  behavior as the source of `D(p)`. Do not re-examine `t=1`'s local
  resolution again without a genuinely new reason — it is fully,
  unconditionally understood and does not carry `\chi(-2)`-dependence
  into the final `N_{I_2}(p)=2p`.
- **RULED OUT**: `H^0`/`H^4` normalization as the source. Do not
  re-audit this without new information.

---

## 4. Current geometric state (unchanged — all four bad fibers complete)

`I_2(1)`: `2p`. `I_0^*(-1)`: `5p+1`. `I_2^*(0)`, `I_2^*(\infty)`:
`7p+1` each. **No local geometry remains unresolved anywhere in this
project.**

---

## 5. Exact current bottleneck (read this first when resuming)

> **The immediate unresolved task is:** locate the exact source of
> `D(p)=1-\chi(-2)$ in the global affine/projective point-count ledger.
> Two major candidates (`t=1`'s node geometry; `H^0/H^4` normalization)
> have now been **ruled out by exact proof**, not merely by suspicion.

**Most promising remaining candidates, per Round 28's own diagnosis**:
(a) the `t=0`/`t=\infty` `I_2^*` fibers' own boundary bookkeeping —
specifically, whether the "`+1` per good `T`" convention used for
*generic* fibers correctly matches how the point `O` (on the identity
component, constructed via a genuinely different chart — Round 26's
`u,v` chart — than the rest of `I_2^*`) is counted there; (b) the
`I_0^*$ fiber at `t=-1`, not yet individually re-audited with the
`t=1`-style exact tangent-cone/infinity-count method used successfully
this round.

**Do not** re-examine `t=1`'s local geometry (closed, §3) or the
`H^0/H^4$ normalization (ruled out, §1) without new information.

Nothing else is currently blocking — every piece of local geometry and
`\mathrm{Tr}_{NS}(p)` remain PROVED.

---

## 6. Round-28 outcome (for continuity)

- Conducted a full, exact audit of the round's own top-priority
  hypothesis (`t=1`'s split/non-split node) and **definitively killed
  it** via direct computation (tangent cone, Hessian, exact
  affine/infinity point counts, classical character-sum identity,
  numeric cross-check at 10 primes).
- Audited the `H^0/H^4` Lefschetz normalization and found no error.
- **Did not locate the actual source of `D(p)=1-\chi(-2)`** — the
  search space is now smaller (two major candidates eliminated) but the
  residual remains unexplained.
- Therefore Round 28 ended with verdict **ROUND28-D** (residual remains
  unexplained), with real, useful negative progress and a sharpened
  next-step focus (the `t=0/\infty` boundary/identity-counting
  convention, or a fresh `t=-1` audit).

---

## 7. Planned Round 29 strategy

**Primary next step**: repeat Round 28's exact method (tangent cone at
the singular point, Hessian determinant, explicit affine + points-at-
infinity count, cross-checked numerically) — but applied to **`t=-1`
(`I_0^*`)** first (simpler than `I_2^*`, a good next test of the
method), and then, if still unresolved, to the **specific junction
between the identity component (Round 26's `u,v` chart) and the rest of
`I_2^*` at `t=0`**, checking very carefully whether the "`+1` per
`T`"-style bookkeeping convention used in the Round 27 global ledger
derivation is actually counting `O`'s own contribution at `t=0,1,-1,\infty`
consistently with how it's counted at good fibers (this is a
bookkeeping-convention check, not a new local-geometry construction —
all local geometry is already proved, §4).

**Do not** re-derive `t=1`'s geometry again (§3). **Do not** guess at a
correction term and check numerically — the round's own discipline
(carried through successfully in Round 28) is to locate the source via
exact computation before declaring anything.

Once `D(p)` is fully explained (whether it resolves to `0` after finding
a missing term, or is proved to be a genuine `1-\chi(-2)` correction
reflecting that the two sides count different things), proceed exactly
as previously planned: solve for `\mathrm{Tr}_T(p)`, compare against
`8.3.d.a` without curve-fitting, and determine the master identity's
final status.

---

## 8. Logical dependency chain (unchanged from Round 27's checkpoint)

```
hypercuboid character sum (n=4 zero-sector)         [PROVED — Rounds 1–9]
S_I(p) = (p-1) S(p)                                  [PROVED — Round 9/10]
S(p) = #V(F_p) - p^2                                 [PROVED — Round 10]
K3 surface X (Weierstrass model, fibers, e=24)       [PROVED — Round 11]
rho(X_Qbar)=20 ; |disc NS|=8 ; T(X)=diag(2,4)        [PROVED — Round 21]
Tr_NS(p) = (19+chi(-1)) p                            [PROVED — Round 22]
Complete I_2^*/I_0^*/I_2 resolutions, N(p) formulas  [PROVED — Round 27]
#X(F_p) = #V(F_p) + 19p + chi(-2)                    [PROVED — Round 27]
D(p) = 1-chi(-2)  (t=1 and H^0/H^4 RULED OUT          [OPEN — Rounds 27-28,
        as sources; true source still unlocated)       narrowed Round 28]
        <-- BLOCKED HERE
modular twist vs. newform 8.3.d.a                    [OPEN, not curve-fit]
S(p) = chi(-1)(a_p(f)+p)   [master identity]          [COMPUTATIONALLY VERIFIED ONLY]
```

---

## 9. Files needed for Round 29

- **This checkpoint** (`notes/CHECKPOINT_AFTER_ROUND28.md`) — read first.
- `notes/round28_report.md` — the full `t=1` tangent-cone/isotropy audit
  and `H^0/H^4` check (method template to reuse for `t=-1` next).
- `notes/round27_report.md`, `scripts/round27_C3_and_ledger.py` — the
  complete `I_2^*` resolution and the global ledger derivation being
  audited.
- `notes/round19_report.md` — the `I_0^*` resolution, needed for the
  planned next audit there.
- `notes/round26_report.md`, `scripts/round26_identity_junction.py` —
  the identity component's own chart, relevant to the "how is `O`
  counted at bad fibers" candidate lead.

---

## 10. Repository status (checked just now, after Round 28)

Unchanged in kind: pre-existing Phase-1 files outside
`explorations/hypercuboid/` remain untouched. `explorations/hypercuboid/`
remains untracked, now also containing `notes/round28_report.md` and
this checkpoint (no new script file was needed this round beyond inline
verification). No staged changes, no commits made by this exploration.
`hypercuboid.pdf` and all unrelated repository content remain untouched.

---

NEXT SESSION STARTING POINT

Repeat Round 28's exact tangent-cone/Hessian/affine-plus-infinity-count method, applied first to the t=-1 (I_0^*) fiber, and if still unresolved, to the specific bookkeeping convention for how the zero section O is counted at each bad fiber (t=0,1,-1,infinity) versus at good fibers in the Round 27 global ledger derivation. Do not re-examine t=1's local geometry (fully ruled out) or the H^0/H^4 normalization (ruled out). Once D(p)=1-chi(-2) is fully explained, solve for Tr_T(p), compare against newform 8.3.d.a without curve-fitting, and determine the master identity's final status.

PAUSED AFTER ROUND 28 — READY FOR ROUND 29
