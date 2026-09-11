# Class III Sequel — Minimal Proof Chain (Manuscript Ledger)

This is the **manuscript-ready** proof chain: the shortest clean sequence
from the raw sum to the final theorem, stripped of discovery history,
false starts, and round-by-round narrative. (The full audit trail — every
round, every self-correction, every falsification battery — remains
preserved in the parent directory's `CLASSIII_THEOREM_LEDGER.md` and the
`ROUND*`/`PHASE5` reports; this file is a *different document*, the
distillation meant for the paper itself.)

Each step states the result, the proof method in one sentence, and the
section of the planned manuscript (see `CLASSIII_MANUSCRIPT_BLUEPRINT.md`)
where it belongs.

| # | Result | Proof method (one sentence) | Manuscript §|
|---|---|---|---|
| 1 | `Σ_III(p) = Σ_{x∈F_p^3} χ(P_III(x))`, `P_III` homogeneous degree 6, vanishing on `x0=0` | Definition, inherited from the parent hypercuboid classification | §1 |
| 2 | `Σ_III(p) = (p-1) T(p)`, `T(p)=Σ_{x,t}χ(xt(t+1)(x+t)(x+t+1))` | Projectivization: homogeneity of even degree removes the sign ambiguity; direct bijective substitution reduces to two variables | §1 |
| 3 | `Σ_III(p)=0` for `p≡3 (mod 4)` | Explicit coordinate involution `T:(x0,x1,x2)↦(x2,-(x0+x1+x2),x0)` satisfies `P_III(Tx)=-P_III(x)` identically; relabeling gives `Σ_III=χ(-1)Σ_III` | §2 |
| 4 | `V_III : Y²=X(X+1)T(T+1)(X+T+1)` realizes `T(p)` as a point count | Standard character-sum-to-affine-curve dictionary | §3 |
| 5 | Minimal Weierstrass model `Y²=X³+a2(T)X²+a4(T)X`, `a2=T(T+1)(T+2)`, `a4=T²(T+1)³`; three `I2*` fibers at `T=0,-1,∞`, none elsewhere | Completing the cube; `c4,c6,Δ` valuations at each point; Euler-number check `3×8=24` | §3 |
| 6 | `ρ(X_III)=20`, `MW`-rank `0` | Shioda–Tate on `Triv=U+D6+D6+D6` | §3 |
| 7 | Full 2-torsion `X(X+T(T+1))(X+T(T+1)²)`, `MW_tors=(Z/2)²` exactly | Exact cubic factorization; elementary "≤3 roots ⟹ no larger 2-torsion" plus cited exponent-2 embedding bound ruling out order-4 torsion | §4 |
| 8 | All 21 fiber components (7 × 3 fibers) individually `Q`-rational; `Tr(F_p|NS)=20p` | **Graph-rigidity argument**: `O` + 3 torsion sections land on the 4 distinct multiplicity-1 legs of each `I2*` fiber; the affine-`D6` automorphism group (order 8) has trivial stabilizer once all 4 legs are individually fixed | §4 |
| 9 | `\|disc NS\|=4`; `T(X_III)≅diag(2,2)` | Lattice arithmetic from Shioda–Tate + torsion index; uniqueness via `h(-4)=1` | §5 |
| 10 | Existence of a governing weight-3, CM-by-`Q(i)` newform | Livné's singular-K3 modularity theorem | §6 |
| 11 | The newform is `f_16=16.3.c.a`, untwisted | Twist candidate set `{1,χ(-1),χ(2),χ(-2)}` forced by ramification; CM-degeneracy collapses to 2 candidates on the support; `p=5` discriminates | §6 |
| 12 | `Tr(F_p|T(X_III)) = a_p(f_16)`, all odd `p` (auto-zero at `p≡3(4)` by CM-inertness) | Combine 10–11 | §6 |
| 13 | `T(p) = a_p(f_16)` (`p≡1(4)`), `0` (`p≡3(4)`); `Σ_III(p) = (p-1)a_p(f_16)` (`p≡1(4)`), `0` (`p≡3(4)`) | Lefschetz trace formula, combining steps 8 and 12 with the point-count ledger | §7 |

**What was deliberately removed from this chain** (kept only in the
supporting audit trail, not the paper):
- The abandoned Round 3 hand blow-up sequence (superseded by step 8's
  graph-rigidity route — see `CLASSIII_APPENDIX_PLAN.md` for its
  disposition).
- The "extra chart anomaly" and other mid-investigation false leads.
- All round-numbered self-corrections (ledger-correction of the `p-2` vs
  `p-3` fiber count, the script bug caught in Phase 5, etc.) — real and
  worth documenting in the reproducibility appendix, but not part of the
  theorem's logical structure.
- Multi-prime falsification batteries (33 primes, 15 primes, etc.) — these
  are regression checks, not proof steps; the proof needs only the single
  `p=5` discriminator (step 11) plus the exact algebraic identities
  (steps 1–9, 12).

**Two steps rest on a cited (not re-proved) literature theorem**: step 8's
minor citation (any section meets exactly one fiber component, forced
multiplicity 1 — genuinely elementary, could be proved in a footnote) and
the affine-`D6` dual graph structure (Kodaira/Néron/Tate, textbook); step
10 (Livné 1995). Step 11's exact *level* (16, not 8 or 32) rests on
structural analogy to Ahlgren–Ono–Penniston's own level-16 surface rather
than an independent conductor computation — this should be stated plainly
in §6 as the one place the paper reasons "by analogy" before switching to
rigorous elimination for the twist itself.
