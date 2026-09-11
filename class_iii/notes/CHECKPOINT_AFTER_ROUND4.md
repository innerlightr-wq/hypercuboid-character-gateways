# Class III Checkpoint — after Round 4

**Current best-established state (2026-09-11):**

- **`Tr(F_p|NS(X_III)) = 20p`, for every good odd prime — PROVED —
  SELF-CONTAINED.** Closed this round via: (1) the elementary fact that any
  section of the fibration meets exactly one fiber component at
  multiplicity 1; (2) the standard fact that `I2*`'s dual graph (affine
  `D6`) has exactly 4 multiplicity-1 "leg" components; (3) explicit,
  sympy-verified computation that the four sections `O, P1, P2, P3` (all
  `Q(T)`-rational, using the full-rational-2-torsion fact from Round 3)
  specialize to 4 pairwise-distinct legs at each of the three `I2*` fibers;
  (4) graph rigidity, forcing the 3 spine components per fiber to also be
  individually `Q`-rational once all 4 legs are individually fixed. No
  blow-up-chart completion of the spine was needed.
- `Tr(F_p|T(X_III)) = a_p(16.3.c.a)` for all odd `p` — **FINITE
  THEOREM-BASED VERIFICATION**, unchanged since Round 2 (twist forced
  trivial by elimination at `p=5` over a theorem-restricted candidate set).
- `T(p)`, `Σ_III(p)` closed forms — now **unconditional** (previously
  conditional on the now-proved `NS` trace).
- Verdict history: Round 1 `CLASSIII-1B`; Round 2 `CLASSIII-2C`; Round 3
  `CLASSIII-3C`; Round 4 **`CLASSIII-4A`**.

**Only remaining open item**: confirm `X_III`'s exact place (or absence) in
the Miranda–Persson/Shioda extremal-K3 catalogue via direct table access —
a literature-completeness question, not a mathematical gap.

See `ROUND4_CLASS_III_REPORT.md` for the full closing argument, including
an honest side-note about an unreconciled "extra chart" anomaly found while
probing Round 3's abandoned blow-up-construction approach (does not affect
the proof, which does not depend on that construction).
