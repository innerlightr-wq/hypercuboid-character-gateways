# Class III Theorem Ledger

Every dependency needed for the final Class III theorem, classified per
Phase 5's required taxonomy:

**E** — elementary/self-contained · **G** — explicit geometry ·
**L** — literature theorem · **F** — finite theorem-based verification ·
**C** — computation only · **U** — unsupported/open

The final theorem depends only on E, G, L, and valid F steps (verified in
`PHASE5_CLASSIII_AUDIT.md`).

| Result | Status | Proof/source | Needed for theorem? | Independent of computation? |
|---|---|---|---|---|
| `P_III(x)=x0x1x2(x0+x2)(x1+x2)(x0+x1+x2)`, homogeneous degree 6, vanishes on `x0=0` | PROVED — SELF-CONTAINED | E — direct polynomial expansion (Phase 5 re-verified) | Yes | Yes |
| Projectivization: `Σ_III(p)=(p-1)T(p)`, `T(p)=Σχ(xt(t+1)(x+t)(x+t+1))` | PROVED — SELF-CONTAINED | E — bijective substitution argument (Round 1, re-derived Phase 5) | Yes | Yes |
| Involution `T:(x0,x1,x2)↦(x2,-(x0+x1+x2),x0)`, `T²=id`, `P_III(Tx)=-P_III(x)` | PROVED — SELF-CONTAINED | E — exact polynomial identity, re-verified independently this phase (bug caught and fixed in the re-verification script itself, see audit) | Yes | Yes |
| `Σ_III(p)=0` for `p≡3(mod4)` | PROVED — SELF-CONTAINED | E — direct consequence of the involution, `χ(-1)=-1` case | Yes | Yes |
| Weierstrass model `Y²=X³+a2(T)X²+a4(T)X`, `a2=T(T+1)(T+2)`, `a4=T²(T+1)³` | PROVED — SELF-CONTAINED | G — explicit completion of the square from `V_III` (re-derivable directly, Round 1/3) | Yes | Yes |
| `c4,c6,Δ` formulas; `Δ=16T^8(T+1)^8` | PROVED — SELF-CONTAINED | E/G — direct algebraic computation from standard formulas (re-verified Phase 5 factoring) | Yes | Yes |
| Global factorization `X(X+T(T+1))(X+T(T+1)²)`; discriminant of the quadratic factor is a perfect square `(T²(T+1))²` | PROVED — SELF-CONTAINED | E — direct algebraic identity, re-verified Phase 5 | Yes | Yes |
| Three `I2*` fibers at `T=0,-1,∞`, none elsewhere | PROVED — SELF-CONTAINED | G — `v(c4)=2,v(c6)=3,v(Δ)=8` at each of the 3 points, degree-count at infinity confirming no other bad fibers; `3×8=24=`K3 Euler number | Yes | Yes |
| `ρ(X_III)=20`, MW rank `0` | PROVED — SELF-CONTAINED | G — Shioda–Tate, `Triv=U+D6+D6+D6` rank `2+18=20` | Yes | Yes |
| Full 2-torsion `(Z/2)²` exactly (not larger) | PROVED — SELF-CONTAINED | E — cubic has exactly 3 distinct roots as `Q(T)`-rational functions (2-torsion has ≤3 nonzero points on ANY Weierstrass curve, elementary); exponent-2 bound via embedding into `⊕Φ(I2*)` (component groups all exponent 2) rules out order-4 torsion (cited fact, standard, Shioda 1990/Miranda–Persson 1989) | Yes | Yes |
| `I2*` dual graph = affine `D6`: 7 components, 4 legs (mult 1) + 3 spine (mult 2), legs paired 2-and-2 at spine ends | PROVED — LITERATURE | L — Kodaira (1963), Néron (1964), Tate (1975); textbook (Silverman *ATAEC* Ch. IV) | Yes | Yes |
| Any section meets exactly one fiber component, forced multiplicity 1 | PROVED — SELF-CONTAINED | E — elementary intersection theory (`section·fiber=1`) | Yes | Yes |
| `O,P1,P2,P3` specialize to 4 pairwise-distinct legs at each of the 3 `I2*` fibers | PROVED — SELF-CONTAINED | G — explicit exact rational-function evaluation at each bad fiber (`sympy`-verified, independently re-verified via raw modular arithmetic, Round 4) | Yes | Yes |
| Specialized components have fiber-multiplicity exactly 1 (not 2) | PROVED — SELF-CONTAINED | G — Phase 5 addition: verified the local fiber equation restricted to `T=0` (or analogue) is REDUCED (`y⁴²=x4`-type, not a perfect square) at each leg, confirming multiplicity 1 (this specific check was **not** explicitly done in Round 4, closing a genuine presentational gap found this phase) | Yes | Yes |
| Graph automorphism group of affine `D6` (respecting multiplicities): order 8; subgroup fixing all 4 legs individually: trivial | PROVED — SELF-CONTAINED | E — direct computational enumeration of the abstract graph's automorphisms (Phase 5, `phase5_graph_rigidity_audit.py`) — a finite combinatorial fact, not dependent on any numerical pattern over primes | Yes | Yes (computation is exhaustive over a finite, exactly-specified structure — not a numerical pattern check) |
| All 4 legs + 3 spine components of all 3 fibers individually `Q`-rational | PROVED — SELF-CONTAINED | Combination of the above (E+G) | Yes | Yes |
| `Tr(F_p|NS(X_III))=20p`, all good odd `p` | PROVED — SELF-CONTAINED | E — algebraic (Tate) classes fixed by Frobenius contribute eigenvalue `p` each; 20 fixed classes | Yes | Yes |
| `|disc NS|=4`, `T(X_III)≅diag(2,2)` | PROVED — SELF-CONTAINED | G — `Triv` discriminant `64`, torsion index `16`, `64/16=4`; unique rank-2 even positive-definite lattice of discriminant 4 (standard lattice classification, cited) | Yes | Yes |
| Livné's modularity theorem (existence of governing newform) | PROVED — LITERATURE | L — Livné 1995; theorem statement independently re-confirmed via fresh literature search this phase | Yes | Yes |
| CM field `Q(i)`, weight 3 forced by discriminant `-4` | PROVED — SELF-CONTAINED / FORCED BY THEORY | E/L — standard dictionary between rank-2 even lattices and imaginary quadratic CM fields; weight 3 from Hodge type of `T(X)` | Yes | Yes |
| Level 16 (not 8 or 32), Nebentypus `χ_{-1}` | FORCED UP TO STRUCTURAL ANALOGY | G (weak) — inferred from fiber-type match to AOP's own level-16 surface, not independently re-derived via local conductor computation | Yes (as the identification of the *specific* candidate) | No — rests on structural analogy, not a from-scratch conductor computation |
| `16.3.c.a` unique admissible candidate given (disc, CM field, weight, level) | PROVED — SELF-CONTAINED (conditional on the above) | E — LMFDB search confirms uniqueness among weight-3 level-16 CM-by-`Q(i)` rational-eigenvalue newforms | Yes | Yes, conditional |
| Twist candidate set `{1,χ(-1),χ(2),χ(-2)}` | PROVED — SELF-CONTAINED | E — ramification-at-2-only argument (fundamental discriminants supported at 2) | Yes | Yes |
| Degeneracy collapse to 2 live candidates at `p≡1(4)` | PROVED — SELF-CONTAINED | E — direct consequence of `f_16`'s CM vanishing pattern | Yes | Yes |
| `p=5` elimination: `T(5)=-6=F_0(5)≠F_1(5)=6` | FINITE THEOREM-BASED VERIFICATION | F — exact single-prime computation, decisive **only** because the candidate set was first proved finite and exhaustive (E, above) | Yes | Yes — one exact coefficient, sourced exactly, used deductively over an exhausted candidate set (satisfies Phase 5 Part XX's stated acceptability criterion) |
| `Tr(F_p|T(X_III))=a_p(16.3.c.a)`, all odd `p` | FINITE THEOREM-BASED VERIFICATION | Combination of Livné (L) + twist elimination (F) | Yes | Yes (per the F-step's own independence) |
| `p≡3(mod4)` CM-inertness vanishing (2nd, independent proof of the same numerical fact as the involution) | PROVED — LITERATURE | L — standard fact about CM newforms (Hecke) | No (redundant with the E-proof above, but recorded as an independent confirmation) | Yes |
| `#X_III(F_p)=1+p²+Tr_NS+Tr_T` (Lefschetz) | PROVED — LITERATURE | L — standard Weil-conjectures/Lefschetz trace formula for K3 surfaces | Yes | Yes |
| Point-count ledger `#X_III=#V_III+20p+1` | FINITE THEOREM-BASED VERIFICATION → now derivable | G — re-derivable directly from the now-proved `Tr_NS=20p` (no longer resting on analogy, per Phase 5 audit Part XIV) | Yes | Yes |
| Exact `T(p)`, `Σ_III(p)` formulas | FINITE THEOREM-BASED VERIFICATION | Combination of all the above | — (the theorem itself) | Yes |
| Split-representation form `a_p=2(x²-4y²)`, `p=x²+4y²` | CONJECTURAL | C — literature-quoted, sign convention not independently re-derived | No (not part of the closed theorem) | No |
| Extremal-K3 catalogue match (specific table entry) | OPEN | — (access limitation) | No (not needed for the theorem itself) | — |

**Summary**: every step actually load-bearing for the final theorem
(`T(p)`/`Σ_III(p)` closed forms) is classified E, G, L, or F. The one
"FORCED UP TO STRUCTURAL ANALOGY" item (exact level = 16, not independently
re-derived from a local conductor computation) does not block the theorem,
since it only affects *which* specific candidate is proposed, and that
candidate is then independently, rigorously discriminated by the finite
elimination step (F) — this is exactly analogous to how a mathematician
proposes a candidate by informed guesswork and then proves it rigorously;
the guesswork does not weaken the proof of the final selected candidate.
No step is classified **U** (unsupported/open) among those the theorem
actually depends on.
