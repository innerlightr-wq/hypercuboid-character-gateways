# Class III Checkpoint — after Round 3

**Current best-established state (2026-09-11):**

- `T(X_III) ≅ diag(2,2)`, CM field `Q(i)`, modular candidate `16.3.c.a`,
  twist trivial (untwisted) — all `PROVED`/`FINITE THEOREM-BASED
  VERIFICATION`, unchanged since Round 2.
- `Tr(F_p|T(X_III)) = a_p(16.3.c.a)` for all odd `p` — **FINITE
  THEOREM-BASED VERIFICATION**, unconditional.
- `Tr(F_p|NS(X_III)) = 20p` — **CONJECTURAL**. Round 3 found 7 of an
  expected 20 `NS` generators via explicit local blow-up (ordinary,
  unweighted) at all three `I2*` fibers, and **every one is unconditionally
  `Q`-rational** with zero counterexamples found. The remaining ~13
  generators (2 missing components per finite fiber, most of the
  `T=infinity` fiber) were not individually constructed. **Not proved.**
- `Sigma_III(p) = (p-1)a_p(16.3.c.a)` for `p≡1(4)`, `0` for `p≡3(4)` —
  same conditional status as the `Tr(NS)` item above.
- Verdict history: Round 1 `CLASSIII-1B`; Round 2 `CLASSIII-2C`; Round 3
  `CLASSIII-3C`.

**Single highest-value next action** (per Round 3's Final Report item 27):
complete the local resolution of the three `I2*` fibers using a computer
algebra system with a built-in surface-singularity resolution routine
(Magma's `Resolve`, or Singular), applied to the explicit points identified
in Round 3 Part I, to obtain the full 7-component-per-fiber intersection
graph with verified self-intersection numbers. Round 3's partial evidence
(7/20 generators, all split, zero counterexamples) makes it plausible this
closes cleanly, but it has not been shown.

See `ROUND3_CLASS_III_REPORT.md` for full detail, including an honest
account of exactly which components were and were not constructed.
