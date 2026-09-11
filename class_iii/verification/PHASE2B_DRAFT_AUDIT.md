# Class III Sequel — Phase 2B Draft Audit

Adversarial self-review of the newly-drafted Sections 6–10 of
`class3_hypercuboid_k3.tex`, plus a mandatory re-audit of the Section 4→5
transition per this round's Part I instruction. Each item below was
checked with a **fresh** computation, independent of the prose.

## Part I re-audit: Section 4→5 transition

1. **`ρ(X_III)=20`**: re-confirmed via `Triv=U+D6+D6+D6`, rank `2+18=20`,
   matching the Hodge bound `h^{1,1}=20` with equality (forcing
   `ρ(X_Qbar)=20` exactly, not merely `≤20`). No error.
2. **`MW_tors≅(Z/2)²`**: re-confirmed via the two-step elementary+cited
   argument (Section 4 of the manuscript). No error.
3. **Shioda discriminant formula ⟹ `|disc NS|=4`**: re-derived fresh —
   `disc(D6)=4` confirmed by direct computation of the `D6` Cartan
   matrix determinant (`sympy`, 6×6 matrix, det `=4`), not merely cited;
   `disc(Triv)=(-1)·4³=-64`; `|disc NS|=64/16=4`. No error.
4. **`T(X_III)≅diag(2,2)`, and — critically — the associated CM field**:
   this is where a **genuine, substantive error was found**, in text
   that had already compiled cleanly in Phase 2A. See below.

### Error found: quadratic-form/discriminant bookkeeping in the (already-compiled) Section 5 text

The Phase 2A text read: *"...classified... by reduced binary quadratic
forms $ax^2+bxy+cy^2$ of discriminant $b^2-4ac=-4$ with $|b|\leq a\leq
c$, of which exactly one exists, $(a,b,c)=(2,0,2)$..."* — **this is
wrong**: $(2,0,2)$ has discriminant $0-4(2)(2)=-16$, not $-4$.

Fresh re-derivation (prompted directly by this round's Part I instruction
to show the determinant calculation explicitly rather than hiding it
behind "standard computation" — exactly the instruction that surfaced
this): for a rank-2 **even** lattice, the Gram matrix necessarily has the
form $\begin{pmatrix}2a&b\\b&2c\end{pmatrix}$ (diagonal entries even by
definition of "even lattice"), and the *associated primitive quadratic
form* is $Q(x,y)=ax^2+bxy+cy^2$ — **not** the Gram matrix's raw diagonal
entries. For $T(X_{\rm III})=\mathrm{diag}(2,2)$: $2a=2\Rightarrow a=1$,
$2c=2\Rightarrow c=1$, $b=0$, giving $(a,b,c)=(1,0,1)$, discriminant
$0-4=-4$ — **correct**. Cross-checked against the companion Classes I/II
paper's own $T(X)=\mathrm{diag}(2,4)$: this convention gives
$(a,b,c)=(1,0,2)$, discriminant $-8$, matching their stated
"discriminant-8" result exactly — confirming the corrected convention is
the one actually used consistently across both papers (the erroneous
$(2,0,2)$ reading was never used anywhere else in either manuscript, so
this was an isolated slip, not a systemic convention error).

**Fix applied**: `class3_hypercuboid_k3.tex`'s Section 5 "Lattice
consequences" paragraph was rewritten to derive `diag(2,2)` directly from
the determinant equation `4ac-b²=4` (shown explicitly, not hidden), and
the quadratic-form-to-CM-field reduction was moved into the new Section 6
with the half-diagonal convention stated explicitly and flagged with a
parenthetical warning against the natural mistake. Recompiled and
re-verified: the corrected text is internally consistent and matches the
companion paper's own convention.

**Consequence for the paper's final conclusions**: none. `T(X_{\rm
III})\cong\mathrm{diag}(2,2)$ and the CM field $\Q(i)$ were always the
correct final answers (independently confirmed via the direct
$4ac-b^2=4$ computation, via the cross-check against the companion
paper's convention, and via consistency with $h(-4)=1$); only the
*intermediate labeled quadratic form* used to justify the CM-field step
was wrong, exactly parallel in kind to Phase 2A's variable-labeling bug
in the projectivization lemma.

## Part IX: adversarial falsification attempts

1. **`|disc NS|=4`**: attempted to break by recomputing `disc(D6)`
   independently (Cartan matrix determinant, not looked up) — got `4`,
   matching. Attempted alternate torsion order (would `|MW_tors|=2` or
   `8` change the answer?) — no, torsion completeness (independently
   re-proved, Section 4) pins `|MW_tors|=4` exactly. **Survives.**
2. **`T(X)=diag(2,2)`**: the error found above was exactly an attempt to
   falsify this step's *justification*; the conclusion itself survives
   (see above), only the intermediate bookkeeping needed repair.
   **Survives, after fix.**
3. **CM-field identification**: attempted to find an alternative
   reduced form of discriminant $-4$ that might give a different field —
   none exists ($h(-4)=1$, verified: the reduction algorithm for binary
   quadratic forms has a unique output for discriminant $-4$, and
   $(1,0,1)$ satisfies $|b|\le a\le c$). **Survives.**
4. **Allowed-twist set**: attempted to find a fifth candidate character
   unramified outside $\{2\}$ — the fundamental discriminants supported
   only at $2$ are exactly $\{1,-4,8,-8\}$ (a finite, classical fact
   about quadratic fields, not an assumption); no fifth candidate exists.
   **Survives.**
5. **`p=5` discriminator**: independently recomputed `T(5)=-6` via the
   raw 25-term sum (not looked up from an earlier round's cached output),
   recomputed `a_5(16.3.c.a)=-6` against the cached LMFDB data, and
   recomputed `χ(2)(5)=-1` from the definition (`5 mod 8 = 5 ≠ 1`).
   Attempted to find a computational error in any of the three — none
   found. **Survives.**
6. **Untwisted claim**: attempted to find a logical gap between "F₁
   refuted at p=5" and "F₀ is THE answer" — none: Lemma 7.2 proves
   exhaustively that only F₀, F₁ survive collapse, so refuting F₁ leaves
   only F₀, a valid elimination (not an inference from absence of
   counterevidence). **Survives.**
7. **Point-count ledger constants**: independently re-derived (not
   copied) and independently numerically verified for 5 primes
   (`p=5,7,11,13,17`) via a freshly-written script computing
   `#V_III(F_p)` by direct brute force and comparing against `p²+T(p)`,
   and separately verifying the affine bad-fiber count is exactly `p` at
   both `T=0` and `T=-1` (not assumed — checked that `T(T+1)=0` kills the
   right-hand side identically at both points, a two-line elementary
   fact, then confirmed the resulting affine count is exactly `p` by
   direct enumeration). All matched. **Survives.**
8. **Final `Σ_III(p)` formula**: follows deductively from Lemma 2.2 (already
   audited, Phase 2A) and Theorem 8.5 (this round); no independent
   falsification target beyond its two inputs, both of which survived
   items 1–7 above. **Survives.**

## Summary

**One substantive error was found and fixed**: a quadratic-form
discriminant bookkeeping mistake in the Phase 2A-drafted Section 5 text
(`(a,b,c)=(2,0,2)` instead of the correct `(1,0,1)`), caught specifically
because this round's Part I instruction demanded the determinant
calculation be shown explicitly rather than hidden behind "standard
computation" — precisely the discipline that exposed it. The paper's
final conclusions (`T(X_{\rm III})\cong\mathrm{diag}(2,2)$, CM field
`Q(i)`) were never in doubt and remain unchanged; only the intermediate
justification was repaired.

All eight items of the Part IX falsification list were attacked directly
and none produced a surviving counterexample.

**This draft is judged ready to proceed toward a final referee audit**,
with the fix documented above applied and the file recompiling cleanly
(15 pages, no errors, no undefined references).
