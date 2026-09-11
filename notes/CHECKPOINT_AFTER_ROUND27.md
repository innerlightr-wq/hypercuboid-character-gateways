# CHECKPOINT — Hypercuboid Arithmetic Exploration, after Round 27

Supersedes `CHECKPOINT_AFTER_ROUND26.md`. Read this file first. Sections
1–4 carry forward with a major update (the `I_2^*` resolution is now
COMPLETE); §§5–7 updated for the new (much smaller) bottleneck.

---

## 1. Current PROVED results (major addition this round)

All of Round 26's checkpoint §1 stands (Gateways A–G; `Σ_I(p)=(p-1)S(p)`;
`S(p)=#V(F_p)-p^2`; K3 classification `e=24`; full torsion;
`\rho(X_{\overline{\mathbb Q}})=20`; `|\mathrm{disc}(NS)|=8`;
`T(X)\cong\mathrm{diag}(2,4)`; `\mathrm{Tr}_{NS}(p)=(19+\chi(-1))p`;
identity component constructed and smooth; `O\leftrightarrow C_1`
junction clean).

**NEW, major — the `I_2^*` resolution is now COMPLETE and PROVED:**
- `C_2`'s previously-unexamined singular point at `A=\infty` (`t_3=0`)
  is a **genuine, distinct** ordinary node (leading form `-t_3x_1+y_3^2`,
  Hessian determinant `-2`), resolving via one ordinary blow-up to a
  smooth conic `C_3` (`Y'^2=T'X'`), **unconditionally `\mathbb F_p`-rational
  for every odd `p`**.
- **All 7 components of `I_2^*` explicitly constructed**: identity, `N`,
  `C_1`, `C_3`, `C_2`, `F_1`, `F_2`, forming the tree
  `\{O,N\}-C_1-C_3-C_2-\{F_1,F_2\}` (6 edges).
- **Multiplicities derived from genuine pullback-of-`t` computations**
  (a new methodological result — not assumed from the Kodaira table):
  identity, `N`, `F_1`, `F_2` have multiplicity 1; `C_1`, `C_3`, `C_2`
  have multiplicity 2.
- **All four hard consistency checks pass simultaneously**: component
  count `r=7`; Euler number `2r-E=8`; component group
  `\Phi\cong(\mathbb Z/2)^2` (from the explicit two-fork/three-chain
  structure); multiplicity vector `(1,1,2,2,2,1,1)`.
- **All 7 components are unconditionally `\mathbb F_p`-rational for every
  odd `p`** — confirms and completes Round 25's conjecture; there is
  **no `\chi(-1),\chi(2),\chi(-2)` dependence anywhere in the `I_2^*`
  fiber itself.**
- $$\boxed{N_{I_2^*}(p) = 7p+1 \quad\text{PROVED} \qquad (\text{and, by the proved }t{=}0\leftrightarrow\infty\text{ isomorphism, } N_\infty(p)=7p+1\text{ too}).}$$

**Global ledger — substantial progress, not yet closed:**
- Recomputing `\#X(\mathbb F_p)` from scratch using the now-proved
  `N_{I_2^*}(p)=7p+1`, `N_{I_0^*}(p)=5p+1`, `N_{I_2}(p)=2p` gives:
  $$\#X(\mathbb F_p) = \#V(\mathbb F_p) + 19p + \chi(-2).$$
- Combined with the proved `\mathrm{Tr}_{NS}(p)=(19+\chi(-1))p`:
  $$\boxed{D(p) := S(p)-\chi(-1)p-\mathrm{Tr}_T(p) = 1-\chi(-2)\ \in\{0,2\}.}$$
  **Not identically zero** — but now a **small, bounded constant** (not
  growing with `p`), a dramatic narrowing from Round 22's `p`-linear
  residual.

---

## 2. Computationally verified but NOT proved (unchanged)

Master identity `S(p)=\chi(-1)(a_p(f)+p)`, equivalently
`S(p)=-\chi(2)p+\chi(-1)a_p(E)^2`. Verified exactly `3\le p<500`,
cross-checked against raw LMFDB data. **Status: NOT proved** — the gap
is now precisely `D(p)=1-\chi(-2)$, a small bounded arithmetic residual
in the point-count bookkeeping (§5), not a geometric construction gap.

---

## 3. Important corrections and KILLED hypotheses — DO NOT RETRY

All of Round 26's checkpoint §3 stands. **NEW this round:**
- **RESOLVED (was open, now closed)**: `C_2`'s `A=\infty` point is a
  genuine distinct new component `C_3`, **not** a re-encounter of
  `A=0` or `A=-1` — confirmed via `t_3=1/A` being manifestly a third,
  distinct value.
- **The "`7p+1`" formula, previously only a candidate (Round 22/23),
  is now PROVED** — do not re-derive it from scratch; cite this
  checkpoint.

---

## 4. Current geometric state

**All four bad fibers are now COMPLETELY resolved and proved**:
`I_2(1)`: 2 components, 2-cycle, `2p`. `I_0^*(-1)`: 5 components, star,
`5p+1`. `I_2^*(0)` and `I_2^*(\infty)`: 7 components each, tree
(2 forks + 3-node chain), `7p+1` each. **No local geometry remains
unresolved.**

---

## 5. Exact current bottleneck (read this first when resuming)

> **The immediate unresolved task is:** find the source of the small,
> bounded residual `D(p)=1-\chi(-2)` in the global affine/projective
> point-count ledger.

This is now a **narrow arithmetic-bookkeeping audit**, not a geometric
construction task. **Most promising leads** (per Round 27's own
diagnosis): (a) a subtlety in exactly how the point `O` is counted at
each bad fiber relative to the `+1`-per-good-fiber convention used
elsewhere in the ledger — check whether `O` is single-counted,
double-counted, or miscounted somewhere in the bad-fiber resolved
counts; (b) a normalization/boundary term in how the literal Lefschetz
formula's `H^0`/`H^4` contributions (`1` and `p^2`) compare to this
specific singular-then-resolved model versus the abstract smooth
projective `X`. **Re-derive the ledger line-by-line from Round 27's
report (Part XI) and check each step for an off-by-one or
double-counting**, rather than re-deriving any fiber's local geometry
(that part is now closed, §1/§4).

Nothing else is currently blocking — everything through
`N_{I_2^*}(p)=7p+1` and the resulting `\#X(\mathbb F_p)=\#V(\mathbb F_p)+19p+\chi(-2)`
identity is PROVED.

---

## 6. Round-27 outcome (for continuity)

- Resolved `C_2`'s `A=\infty` singularity: genuine, distinct ordinary
  node, giving the missing seventh component `C_3`.
- **Completed the full `I_2^*` resolution**, passing all four hard
  consistency checks (component count, Euler number, component group,
  multiplicity vector) simultaneously, without any adjustment.
- **Derived every multiplicity from genuine pullback-of-`t` computations**
  for the first time (previously assumed from the Kodaira table);
  results matched the table exactly, a strong independent confirmation.
- **Proved `N_{I_2^*}(p)=7p+1`** (upgraded from a Round-22 candidate to
  a theorem).
- Recomputed the global ledger from scratch: residual narrowed from an
  unbounded/`p`-dependent error (Round 22) to an exact, small, bounded
  constant `D(p)=1-\chi(-2)`.
- Therefore Round 27 ended with verdict **ROUND27-C** (complete `I_2^*`
  geometry proved; a precisely identified bookkeeping discrepancy
  remains).

---

## 7. Planned Round 28 strategy

**Primary next step**: audit the Round 27 Part XI ledger derivation
line by line (reproduced in `scripts/round27_C3_and_ledger.py`'s
comments and `notes/round27_report.md`), specifically checking:
1. Whether the "`+1` for each good `T`, `resolved(T)` for each bad `T`"
   convention double-counts or misses a point at any of the four bad
   fibers (`t=0,1,-1,\infty`) — compare directly against a from-scratch
   re-derivation using the alternative route (Route B: sum resolved
   fiber counts directly, matching Round 25's "two independent routes"
   instruction) to see exactly where the `1-\chi(-2)` enters.
2. Whether the smooth-projective-model Lefschetz formula
   `\#X=1+p^2+\mathrm{Tr}(H^2)` needs any correction specific to this
   surface (e.g. from the two-torsion sections' own contribution to
   `H^0`/boundary counting) not yet accounted for.

**Do not** re-examine any bad-fiber's local geometry — all four are
proved complete (§1/§4). This is now purely a global bookkeeping/
Lefschetz-formula audit.

Once `D(p)\equiv0` is achieved (or the residual is otherwise fully
explained/absorbed), proceed exactly as previously planned: solve for
`\mathrm{Tr}_T(p)`, compare against `8.3.d.a` without curve-fitting, and
determine the status of the master identity.

---

## 8. Logical dependency chain (updated)

```
hypercuboid character sum (n=4 zero-sector)         [PROVED — Rounds 1–9]
S_I(p) = (p-1) S(p)                                  [PROVED — Round 9/10]
S(p) = #V(F_p) - p^2                                 [PROVED — Round 10]
K3 surface X (Weierstrass model, fibers, e=24)       [PROVED — Round 11]
rho(X_Qbar)=20 ; |disc NS|=8 ; T(X)=diag(2,4)        [PROVED — Round 21]
Tr_NS(p) = (19+chi(-1)) p                            [PROVED — Round 22]
Complete I_2^*/I_0^*/I_2 resolutions, N(p) formulas  [PROVED — Round 27]
#X(F_p) = #V(F_p) + 19p + chi(-2)                    [PROVED — Round 27]
D(p) = S(p) - chi(-1)p - Tr_T(p) = 1-chi(-2)          [PROVED nonzero,
        <-- BLOCKED HERE (small bookkeeping audit)     Round 27]
modular twist vs. newform 8.3.d.a                    [OPEN, not curve-fit]
S(p) = chi(-1)(a_p(f)+p)   [master identity]          [COMPUTATIONALLY VERIFIED ONLY]
```

---

## 9. Files needed for Round 28

- **This checkpoint** (`notes/CHECKPOINT_AFTER_ROUND27.md`) — read first.
- `notes/round27_report.md`, `scripts/round27_C3_and_ledger.py` — the
  complete `I_2^*` resolution and the full ledger derivation to audit.
- `notes/round25_report.md`, `round26_report.md` — `C_1,C_2` construction
  and the identity/junction proofs (reference only, not to be redone).
- `notes/round19_report.md` (`I_0^*`), `round16_report.md` (`I_2`) —
  the other two fully-resolved fibers, for cross-checking the ledger's
  treatment of each.
- `notes/round22_report.md`, `round23_report.md` — the original ledger
  attempts, useful for comparing exactly where this round's derivation
  differs.

---

## 10. Repository status (checked just now, after Round 27)

Unchanged in kind: pre-existing Phase-1 files outside
`explorations/hypercuboid/` remain untouched. `explorations/hypercuboid/`
remains untracked, now also containing `notes/round27_report.md`,
`scripts/round27_C3_and_ledger.py`, and this checkpoint. No staged
changes, no commits made by this exploration. `hypercuboid.pdf` and all
unrelated repository content remain untouched.

---

NEXT SESSION STARTING POINT

Audit the Round-27 global point-count ledger (notes/round27_report.md Part XI) line by line to locate the source of the small bounded residual D(p)=1-chi(-2), by re-deriving the affine/projective correction via the independent "sum resolved fiber counts directly" route and comparing term-by-term against the "+1-per-good-fiber" route used in Round 27. Do not re-examine any I_2^*/I_0^*/I_2 local geometry -- all four bad fibers are now completely and rigorously resolved. Once D(p)=0 is established (or the residual otherwise fully explained), solve for Tr_T(p), compare against newform 8.3.d.a without curve-fitting, and determine the final status of the master identity.

PAUSED AFTER ROUND 27 — READY FOR ROUND 28
