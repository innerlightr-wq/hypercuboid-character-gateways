# CHECKPOINT — Hypercuboid Arithmetic Exploration, after Round 24

This checkpoint exists so Round 25 can resume without re-reading all 24
prior round reports. Read this file first; consult individual
`round<N>_report.md` files only for derivation detail on a specific
point.

---

## 1. Current PROVED results

**Elementary/structural layer (Rounds 1–9):**
- Odd-cardinality vanishing (paper's own Prop 6.2), reconfirmed, not new.
- **Gateways, each with a proved scope**:
  - **A** — private coordinate ⟹ `Σ_S(p)=0`.
  - **B** — multiplicity-2 elimination identity (the classical
    `Σ_x χ((x-r1)(x-r2))` case analysis).
  - **C** — corank-1 minimal-dependency closure (`d` odd, `|S|=d+1`,
    rank `d`).
  - **E** — complementary-pair factorization (`|S|=2k`, `d=k+1` exactly,
    perfect complementary partition).
  - **F** — aggregate-coordinate/fiber conditioning (a *representation*
    gateway, not evaluation; re-exposes A/B/C/E on a fiber after
    conditioning on `Q=λ·x`).
  - **G** — global `S_n` coordinate-relabeling symmetry (full symmetric
    group on the *n* original coordinates, not just the `S_{n-1}`
    subgroup fixing the eliminated one). Proved via explicit polynomial
    identities `P_S(T_π x) = ε(π)·P_{S'}(x)`. Explained (as PROVED
    corollaries) both Round-7's Class-I/II relation
    (`Σ_I=χ(-1)Σ_{II}`) and Class-III's `p≡3(4)` vanishing.
- n=4 classification: 56/63 subsets resolved by A–F (Round 7); the
  3 residual isomorphism classes (I, II, III) reduced to Class I as the
  genuinely hard one via Gateway G (Round 8).

**Class-I reduction to an elliptic/K3 object (Rounds 9–11):**
- **PROVED**: `Σ_I(p) = (p-1)·S(p)`, where
  `S(p) = Σ_{x,t∈F_p} χ(x(x+1)t(t+1)(x+t))` (exact algebraic reduction
  via projectivization/homogeneity of the degree-6 form, cross-checked
  by an independent partial-elimination route).
- **PROVED**: `S(p) = #V(F_p) - p^2` for the affine surface
  `V: Y^2 = X(X+1)T(T+1)(X+T)`.
- **PROVED**: `V` fibers (over the `T`-line) as the "self-twisted
  Legendre elliptic surface" — twist of `E_t:y^2=x(x+1)(x+t)` by `t(t+1)`.
- **PROVED**: minimal Weierstrass model
  `a_2(t)=t(t+1)^2, a_4(t)=t^3(t+1)^2, a_6=0`; exact `c_4,c_6,\Delta,j`;
  minimality at every place; Kodaira fibers `I_2^*(t{=}0)`, `I_2(t{=}1)`,
  `I_0^*(t{=}{-1})`, `I_2^*(t{=}\infty)`; Euler number `e=24`.
- **PROVED**: the surface is an **elliptic K3 surface** (`e=24`, not 12
  — the Round-10 "rational surface" guess is KILLED, see §3).
- **PROVED**: full rational 2-torsion `(\mathbb Z/2)^2` on `E(\mathbb Q(t))`,
  with explicit torsion sections `T_1{=}(X{=}0)`, `T_2{=}(X{=}{-}t(t{+}1))`,
  `T_3{=}(X{=}{-}t^2(t{+}1))`.

**Geometric/arithmetic layer (Rounds 14–21):**
- **PROVED**: trivial lattice `\mathrm{Triv}(X)=U\oplus D_6\oplus A_1\oplus D_4\oplus D_6`,
  rank 19, `|\mathrm{disc}|=128`.
- **PROVED (local geometry, multiplicity-1 layer only — see §4 for the
  precise scope)**: complete, Jacobian-verified resolution of the
  multiplicity-1 components at `t=1` (`I_2`, 2 components, a genuine
  2-cycle not a tree — Round 16) and at `t=-1` (`I_0^*`, all 4
  multiplicity-1 components plus the rational central multiplicity-2
  component — Round 19, Round 23 clarification). At `t=0`/`t=\infty`
  (`I_2^*`), the 4 multiplicity-1 components (identity, `N`, `F_1`,
  `F_2`) are fully constructed and proved smooth (Rounds 17–18); the
  3 interior multiplicity-2 chain components are **NOT** constructed
  (this is the current bottleneck — see §5).
- **PROVED**: exact torsion-section locations at every bad fiber, with
  an independent height-sums-to-4 consistency check passing exactly
  for `T_1,T_2,T_3` (Rounds 16–19).
- **PROVED**: `P\cdot O=0` is forced for any canonical-height-1 section
  (Round 16, via the Shioda height formula's achievable-value bound).
- **PROVED**: exhaustive elimination of all 23 canonical-height-1
  `\mathbb Q(t)`-rational patterns (Round 20; one solver bug caught and
  fixed mid-round before finalizing).
- **PROVED**: exactly **4 distinct** polynomials among those (not 6 —
  Round 20's summary had an arithmetic slip, corrected in Round 21)
  each satisfy `R_X(t) = -q(t)^2` for a polynomial `q`, hence define
  genuine sections over `\mathbb Q(i)(t)` (not `\mathbb Q(t)`).
- **PROVED**: these 4 points form a **single torsion orbit** of one
  non-torsion generator (explicit chord-and-tangent group-law
  verification, Round 21).
- **PROVED**: the orbit representative `P_1=(-(t+1),\,i(t-1)(t+1)^2)`
  has **canonical height exactly 1** (checked against the complete
  4-fiber dictionary) and is **non-torsion**.
- **PROVED**: `\mathrm{rank}\,MW(X/\mathbb Q(i)(t))=1` exactly, and — since
  the trivial lattice (rank 19) is unaffected by this unramified
  constant-field extension and every K3 satisfies `\rho\le20` — this
  **forces `\rho(X_{\overline{\mathbb Q}})=20` exactly**.
- **PROVED**: `|\mathrm{disc}(NS(X_{\overline{\mathbb Q}}))|=8` exactly
  (`=128\cdot1/16`), and by the class-number-one uniqueness of
  discriminant `-8`, **`T(X_{\overline{\mathbb Q}})\cong\mathrm{diag}(2,4)`**.
- **PROVED**: complex conjugation acts on the generator by
  `\sigma(P_1)=-P_1` exactly (direct symbolic substitution `i\to-i`).
- **PROVED (Round 22)**: **all 19 trivial-lattice divisor classes are
  individually defined over `\mathbb Q`** (every explicit blow-up chart used
  only rational coefficients), so combined with the previous item:
  $$\boxed{\mathrm{Tr}_{NS}(p) = (19+\chi(-1))\,p \quad\text{EXACTLY, PROVED.}}$$
  This is the cleanest, most load-bearing new result of the geometric
  phase — reconfirmed unchanged in Rounds 23–24.

---

## 2. Computationally verified but NOT proved

**The master identity** (the central target of Rounds 11–24):
$$S(p) = \chi(-1)\bigl(a_p(f) + p\bigr)$$
and its equivalent elliptic-curve form
$$S(p) = -\chi(2)\,p + \chi(-1)\,a_p(E)^2$$
for `E: y^2=x^3+4x^2+2x` (CM by `\mathbb Q(\sqrt{-2})`) and `f` = LMFDB
newform **8.3.d.a** (weight 3, level 8, CM by `\mathbb Q(\sqrt{-2})`).

**Verification extent**: exact match at every prime `3\le p<500` (Round
19/20 scale) plus a broader check to `p<150` cross-validated against
raw LMFDB API trace data (not an AI-summarized/paraphrased source — a
real transcription error in an intermediate summarized fetch was caught
and fixed in Round 13). Zero exceptions found, in all four residue
classes mod 8, including the edge case `p=3`.

**Status: NOT proved.** The remaining gap is purely geometric/
cohomological (see §5), not numerical. Do not treat the extensive
verification as a substitute for the proof — it is strong evidence, not
a theorem.

**Also computationally verified, not proved**: the Sym²-decomposition
relation `a_p(f) = a_p(E)^2 - p(1+\chi(-2))` (Round 13, a standard
classical mechanism correctly instantiated and checked against real
LMFDB data — very likely true, but not re-derived from a cited theorem
statement with full rigor in this project).

---

## 3. Important corrections and KILLED hypotheses — DO NOT RETRY

- **Rational elliptic surface hypothesis** (Round 10) — **KILLED**
  (Round 11 corrected the discriminant-degree estimate from 12 to 16;
  actual Euler number is 24; the surface is K3, not rational).
- **`t=-1` singular-fiber misconception** — an early instinct to treat
  `t=-1` as a singular value of the cubic `x(x+1)(x+t)` is **wrong**:
  the actual singular values are `t=0,1`; `t=-1` is smooth for that
  cubic but happens to be weight-zero in `S(p)`'s original derivation
  (Round 10/11). Separately, `t=-1` **is** a genuine bad fiber of the
  *surface* (`I_0^*`) for unrelated reasons (the twisting factor
  `t(t+1)` vanishes there) — don't conflate the two facts.
- **Direct pointwise-substitution proof attempts for the master
  identity** — **KILLED** (Round 12): a concrete degree-mismatch
  obstruction (`S(p)`'s defining quintic has degree 5; the target
  `h(x)h(y)` product has degree 6) rules out any simple algebraic
  change-of-variables proof. Any future proof attempt must go through
  genuine Fourier/Jacobi-sum machinery or the geometric route, not
  pointwise substitution.
- **Height-1 `\mathbb Q(t)`-rational section** — **KILLED exhaustively**
  (Round 20, all 23 patterns, exact algebra, one solver bug caught and
  fixed before finalizing). Do not re-search this space.
- **Round-20 "6 candidates" count** — **CORRECTED to 4** (Round 21):
  the 23 raw patterns collapse to exactly 4 distinct polynomials with
  multiplicities 3,3,3,1. The underlying case-by-case table was always
  correct; only a summary sentence in Round 20 was wrong.
- **The `-q(t)^2` failures are not dead ends** — they are genuine
  sections **over `\mathbb Q(i)(t)`**, with `y(t)=i\,q(t)`. This is the
  single most important positive pivot of the whole geometric phase
  (Round 21) — do not re-flag these as "failed" candidates.
- **"Simple Tate-cubic root ⟹ automatically smooth" folklore** —
  **KILLED at least once** (Round 17): tested directly for the `I_2^*`
  `T=-1` direction and found singular; the correct chart needed an
  extra `Y=t^2\tau` rescaling with `\sigma` left dependent (Round 18).
  Do not assume a simple root is automatically resolved without
  checking.
- **"`I_2` fiber graph is a tree"** — **KILLED** (caught mid-Round-20/22):
  `I_2` (type `A_1`, 2 components) is a **2-cycle** (2 edges between the
  same 2 nodes), not a tree (1 edge). Resolved point count is `2p`, not
  `2p+1`.
- **"Missing second fork near identity in `I_2^*`"** — **KILLED**
  (Round 24): the affine-`D_6` diagram's two 2-node forks are
  `\{$identity`, N\}` and `\{F_1,F_2\}` — nothing is missing at the
  multiplicity-1 layer. (What *is* still missing is the 3-node interior
  chain connecting the two forks — see §5.)
- **Shallow intermediate substitution `X=tX'` (Y unscaled) as a route
  to the `I_2^*` interior chain** — **KILLED** (Round 24, verified
  singular by explicit Jacobian at the origin). Do not retry this exact
  substitution; a genuinely different blow-up strategy is needed (§7).
- **A momentary "hidden elliptic curve" scare at `I_0^*`'s central
  component** — **KILLED/false alarm** (Round 23): the center is simply
  the ordinary rational `\mathbb P^1` from the first blow-up (`X=uT'`,
  parametrized by `T'`), not anything exotic.

---

## 4. Current geometric state

**Weierstrass model** (frozen, unchanged since Round 11):
$$y^2 = x^3 + t(t+1)^2\,x^2 + t^3(t+1)^2\,x \qquad(a_1=a_3=a_6=0)$$
Bad fibers: `I_2^*` at `t=0`, `I_2` at `t=1`, `I_0^*` at `t=-1`,
`I_2^*` at `t=\infty` (proved isomorphic to the `t=0` local model via
`t=1/u`, `k=2` rescaling — Round 17/18).

**Completed local geometry:**
- **`t=1` (`I_2`)**: COMPLETE. 2 components, a 2-cycle graph, both
  proved rational (explicit conic with a rational point). `T_1\to`
  identity, `T_2,T_3\to` the shared non-identity component (at distinct
  points `u=-3,-5`).
- **`t=-1` (`I_0^*`)**: COMPLETE. 5 components (4 multiplicity-1 + 1
  multiplicity-2 center), star graph (all attach to the center), all 5
  proved rational. `T_1,T_2,T_3\to\tau=0,1,-1$ respectively; identity
  `\to\tau=\infty`.
- **`t=0` and `t=\infty` (`I_2^*` each)**: **PARTIAL.** The 4
  multiplicity-1 components (identity, `N`, `F_1`, `F_2`) are fully
  constructed and proved smooth via two explicit charts (`X=t^2X_1,
  Y=t^3Y_1` giving `F_1,F_2`; `Y=t^2\tau` with `\sigma` dependent giving
  `N`). Torsion assignment: `T_2\to N`, `T_1,T_3\to F_1,F_2`
  (resolved from a 2-fold ambiguity via the height-sums-to-4 check,
  Round 18). **The 3 interior multiplicity-2 chain components
  (connecting the `\{O,N\}` fork to the `\{F_1,F_2\}` fork) have NOT
  been explicitly constructed.** Their fields of definition and
  Frobenius action are therefore unknown.

---

## 5. Exact current bottleneck (read this first when resuming)

> **The immediate unresolved task is NOT discovering another global
> pattern.** It is completing, or otherwise rigorously accounting for,
> **the three interior multiplicity-2 components of the `I_2^*`
> resolution** (at `t=0`, and by the proved isomorphism also at
> `t=\infty`), and determining their arithmetic/Frobenius contribution
> to the resolved-fiber point count.

This single gap is what blocks closing the Round-22/23 affine-to-
projective bookkeeping identity
$$\#X(\mathbb F_p) = \#V(\mathbb F_p) + (\text{explicit correction from every bad fiber}),$$
which in turn is the only thing standing between the already-proved
`\mathrm{Tr}_{NS}(p)=(19+\chi(-1))p` and an independently-derived
`\mathrm{Tr}_T(p)` (which could then be compared, without curve-fitting,
against `8.3.d.a`'s actual coefficients to settle the modular twist and
the master identity).

Nothing else is currently blocking — the K3 classification, the
Mordell–Weil/Picard-rank result, the transcendental-lattice
identification, and the NS Frobenius trace are all already PROVED (§1).

---

## 6. Round-24 outcome (for continuity)

- Clarified (killed a false worry): the multiplicity-1 fork structure
  of `I_2^*` is complete and correctly paired (`\{O,N\}`, `\{F_1,F_2\}`)
  — nothing is missing at that layer.
- The three interior multiplicity-2 chain components remain unbuilt.
- The natural first attempt at exposing them — the shallow substitution
  `X=tX'` with `Y` left unscaled — was tested and found singular at the
  origin by explicit Jacobian computation (a real, verified negative
  result, not an assumption).
- Therefore Round 24 ended with verdict **ROUND24-D** (`I_2^*`
  resolution itself remains incomplete).

---

## 7. Planned Round 25 strategy

**Preferred approach**: successive **ordinary** (non-weighted)
blow-ups, explicitly tracking, at every stage:
- the exceptional `\mathbb P^1`;
- the strict transform of the previous total space;
- any remaining singular point(s);
- the multiplicity of each new component in the fiber divisor;
- intersections among all components found so far;
- the field of definition of each new piece.

**Do not** simply repeat weighted scalar substitutions (e.g. `X=t^2X_1,
Y=t^3Y_1` in one step) — they resolve the singularity correctly for
smoothness/height purposes but hide the intermediate exceptional
divisors needed for an honest point count.

**Escape hatch** (use if explicit chart-by-chart construction again
proves disproportionately difficult): fall back to citing rigorous
minimal-regular-model / Tate's-algorithm-derived general results for
the component fields of definition, Frobenius action, and resolved-
fiber point count of an `I_n^*` fiber — but **label any such fact
explicitly as theorem-derived (with the precise reference/theorem
invoked) versus explicitly constructed here**, so future rounds always
know which parts of the geometry were verified by hand for this
specific surface and which were imported from general theory.

---

## 8. Logical dependency chain

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
Tr_T(p) = ?  <-- BLOCKED HERE (I_2^* interior chain)  [OPEN — Rounds 22-24]
        |
        v
modular twist vs. newform 8.3.d.a                    [OPEN, not curve-fit]
        |
        v
S(p) = chi(-1)(a_p(f)+p)   [master identity]          [COMPUTATIONALLY VERIFIED ONLY]
```
Every arrow down to and including `Tr_NS(p)` is **PROVED**. The arrow
from `Tr_NS(p)` to `Tr_T(p)` is the single **OPEN** link (blocked on §5).
Everything below that remains **OPEN / COMPUTATIONALLY VERIFIED ONLY**
until it closes.

---

## 9. Files needed tomorrow

- **This checkpoint** (`notes/CHECKPOINT_AFTER_ROUND24.md`) — read first.
- `notes/round17_report.md`, `round18_report.md` — the two successful
  multiplicity-1 `I_2^*` chart constructions at `t=0` (method to adapt).
- `notes/round19_report.md` — the completed `I_0^*` resolution (a
  simpler worked example of the same general technique, useful as a
  template/sanity check).
- `notes/round22_report.md`, `round23_report.md`, `round24_report.md` —
  the full history of the point-count bookkeeping attempts, including
  the killed intermediate-chart approach (don't repeat it).
- `scripts/round17_t0_blowup.py`, `scripts/round18_t2_chart.py` — the
  working symbolic code for the multiplicity-1 charts (reuse the
  pattern: define the substitution, divide by the right power of `t`,
  check the Jacobian at the point of interest).
- `scripts/round19_t_minus1.py` — worked `I_0^*` resolution code.
- `scripts/round22_point_count.py`, and the inline computation in
  Round 23's session (Euler-characteristic cross-check
  `\chi=2r-E`) — reusable verification tooling for whatever new
  component count is proposed.
- `scripts/core.py` — foundational `ZeroSectorSystem`/`chi_columns`
  machinery, still valid throughout, unrelated to the current bottleneck
  but needed if any direct finite-field cross-check of `S(p)` is wanted.

---

## 10. Repository status (checked just now)

- **Changed (tracked) files outside `explorations/hypercuboid/`**:
  `MILESTONE_STATUS.md`, `docs/RESEARCH_STATUS.md`,
  `experiments/multistratum_eviction.py`,
  `results/milestone2_multistratum/summary.json`,
  `src/kv_efficiency/eviction.py`, `tests/test_eviction.py` — these are
  **pre-existing modifications from the earlier (Phase 1, KV-cache)
  work**, not touched by this exploration.
- **Untracked files outside `explorations/hypercuboid/`**:
  `PAUSE_NOTE.md`, several `experiments/*.py`, `hypercuboid.pdf`,
  `manuscript/figures/*.png`, and several `results/*` paths — again all
  pre-existing from Phase 1, **not created or modified by this
  exploration**.
- **`explorations/hypercuboid/`**: untracked (as it has been every
  round), containing exactly the `notes/`, `scripts/`, and `results/`
  files listed at the top of this session plus this checkpoint file.
- **Staged changes**: none (`git diff --cached` empty).
- **Commits made by this exploration**: none.
- **Confirmed**: `hypercuboid.pdf` and all unrelated repository content
  remain exactly as they were before this exploration began — untouched
  by every round including this checkpoint.

---

NEXT SESSION STARTING POINT

Complete the arithmetic of the I_2^* interior chain by successive ordinary blow-ups (or rigorous minimal-model theory if explicit construction remains inefficient), obtain the exact resolved-fiber point count, and then test whether this closes the affine/projective bookkeeping required for the master identity.

PAUSED AFTER ROUND 24 — READY FOR ROUND 25
