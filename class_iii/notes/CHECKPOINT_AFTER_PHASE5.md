# Class III Checkpoint — after Phase 5 (Independent Audit)

**Current best-established state (2026-09-11):**

- The Class III theorem — `Σ_III(p)=(p-1)a_p(16.3.c.a)` for `p≡1(mod4)`,
  `0` for `p≡3(mod4)`, all odd `p` — **survives independent, adversarial
  reconstruction from first principles.** Verdict: **CLASSIII-P5A**.
- Every load-bearing proof step was reclassified under the E/G/L/F
  taxonomy; nothing the theorem depends on is unsupported (**U**). Full
  table: `CLASSIII_THEOREM_LEDGER.md`.
- **Two things were found and fixed during this audit** (not previously
  known):
  1. A coding bug in a fresh re-verification of the `p≡3(mod4)`
     involution (caught immediately by a sanity check, fixed, math
     unaffected).
  2. A genuine, previously-unverified assumption inside Round 4's
     graph-rigidity argument: Round 4 confirmed each troublesome fiber
     point resolves cleanly in one blow-up, but never separately checked
     that the resulting curve has fiber-**multiplicity 1** (as opposed to
     being a mislabeled spine node). This phase verified it directly
     (`scripts/phase5_leg_multiplicity_audit.py`) — confirmed correct,
     closing a real gap.
- The graph-automorphism claim underlying `Tr(F_p|NS)=20p` was verified
  **exhaustively** (all `5040` vertex permutations checked by computer,
  not argued in prose): exactly 8 automorphisms of the unmarked
  affine-`D6` graph, exactly 1 (identity) compatible with all 4 marked
  legs — confirming Round 4's central claim with no loophole found.
- **Computation independence**: the theorem is provable without trusting
  any numerical *pattern* — exactly 3 indispensable, exactly-sourced
  computational facts (`a_5(16.3.c.a)=-6`; `T(5)=-6`; `χ(2)(5)=-1`), used
  deductively after the twist candidate set was proved finite and
  exhaustive.
- **Publication recommendation**: **Option C** — a separate Class III
  sequel paper, not an integration into the existing Classes I/II
  manuscript (which remains untouched and unmodified).
- Verdict history: Round 1 `CLASSIII-1B`; Round 2 `CLASSIII-2C`; Round 3
  `CLASSIII-3C`; Round 4 `CLASSIII-4A`; Phase 5 **`CLASSIII-P5A`**.

**Only remaining open item** (unchanged since Round 4): confirm `X_III`'s
exact place in the Miranda–Persson/Shioda extremal-K3 catalogue via direct
table access — a literature-completeness question, not a mathematical gap,
and does not block publication.

**Single highest-value next action**: write the Class III sequel
manuscript (LaTeX), built around this audit's strengthened graph-rigidity
NS-rationality argument as its central technical contribution.

See `PHASE5_CLASSIII_AUDIT.md` for the full 22-part audit and 29-item
final report.
