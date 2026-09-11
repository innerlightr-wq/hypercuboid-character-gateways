# Class III Sequel — Phase 2A Draft Audit

Adversarial self-review of `class3_hypercuboid_k3.tex` (Sections 1–5, per
the manuscript blueprint's §1–§4 content plan), carried out before
finalizing the draft, per the round's explicit Part VIII instruction. Each
of the eight listed attack targets was checked with a **fresh** symbolic
computation, not by re-reading the prose for plausibility.

## 1. Projectivization factor — **BUG FOUND AND FIXED**

Fresh check: substituted `x0=1, x1=t, x2=x` (the exact renaming as
originally drafted) into `P_III` and compared against the target `T(p)`
summand `x·t(t+1)(x+t)(x+t+1)` via `sympy`. **The difference was nonzero**:
```
P_III(1,t,x) - target = -t^4x - t^3x^2 - t^3x + t^2x^3 + tx^4 + tx^3  ≠ 0
```
Diagnosis: the draft's "Renaming `x1=t, x2=x`" step had the two variables
swapped. `P_III(1,x1,x2) = x1x2(1+x2)(x1+x2)(1+x1+x2)`; substituting
`x1=t,x2=x` gives `tx(1+x)(t+x)(1+t+x)`, in which the factor `(1+x)` does
**not** match the target's `(t+1)`. The correct renaming is `x1=x, x2=t`:
substituting gives `xt(1+t)(x+t)(1+x+t) = xt(t+1)(x+t)(x+t+1)`, which
**does** match exactly (`sympy`-confirmed, difference identically `0`).

**Fix applied**: the LaTeX was corrected to renaming `x1=x, x2=t` (not the
reverse), with an explicit clarifying parenthetical added at the point of
renaming, warning against the reverse assignment by name — precisely so a
future reader attempting the same substitution the wrong way around will
see immediately why it fails. Recompiled and re-verified: the corrected
statement now holds as an exact polynomial identity.

**This is exactly the kind of error the adversarial self-review step
exists to catch.** The underlying mathematical fact
(`Σ_III(p)=(p-1)T(p)`) was never in doubt — it is independently confirmed
by the affine slice being a *bijective* reparametrization of the same
`p²` lines regardless of which coordinate is called `x` and which is
called `t` — but the specific labeled substitution as first drafted was
wrong, and would have made the proof, as literally written, false.

## 2. Involution fixed points

Fresh check (independent of Phase 5's own re-verification, redone again
here specifically for this draft): computed `τ∘τ` by genuine function
composition (not naive symbolic substitution into an unevaluated
expression, the exact trap that produced a bug during Phase 5's own
re-verification of this same fact) — confirmed `τ∘τ = id`. Confirmed
`P_III(τx)+P_III(x)` expands to `0` identically. Confirmed the fixed
locus (`x2=x0, x1=-x0`) gives `P_III=0` there, via the vanishing of the
factor `(x1+x2)`. **No error found.** The draft's proof text matches
these fresh computations exactly.

## 3. K3 classification

Fresh check: `c4,c6,Δ` re-derived independently (matching Round 3's and
Phase 5's prior derivations, a third independent derivation); valuations
at `T=0,-1,∞` re-confirmed; Euler-number cross-check `3×8=24` re-confirmed
arithmetically; trivial-lattice rank `2+18=20` matching the Hodge bound
`h^{1,1}=20` re-confirmed. **No error found.**

## 4. Torsion completeness

Fresh check: the three pairwise root differences (`T(T+1)`, `T(T+1)²`,
`T²(T+1)`) re-verified nonzero as polynomials, vanishing only at `T=0,-1`.
The two-step argument (cubic has ≤3 roots, ruling out larger 2-torsion;
exponent-2 embedding into `⊕Φ(I2*)`, ruling out order-4-or-higher torsion)
re-checked for logical soundness — no gap found. **No error found.**

## 5. Multiplicity-one claim

This is the gap Phase 5's audit already found and closed (Round 4 never
verified it at all); this draft's Lemma~5.3 states it explicitly with a
proof sketch. **Fresh, additional check performed for this draft**: redid
the second-level blow-up in an **independent chart** (`X`-dominant:
`T=X₄t₂, Y₄=X₄y₂`) rather than the `T`-dominant chart used in the paper's
own proof sketch, to cross-check the same conclusion by a different route.
Result: `F` at `X4=0` gives `-t2+y2²` — again a **reduced** curve (linear
in `t2`, not a perfect square), confirming multiplicity 1 by an
independent computational path. **No error found; additionally
strengthened.**

## 6. Distinct-leg specialization

Fresh check: recomputed `x1(P1)=0`, `x1(P2)=-(T+1)`, `x1(P3)=-(T+1)²`
(all equal `-1` at `T=0`, correctly landing on the "double" branch
together, while `P1` lands separately at `x1=0`); recomputed the
second-level coordinates `x3(P2)=-1`, `x3(P3)=-2` exactly (not
approximately). All values match Round 4's and Phase 5's prior
computations exactly (fourth independent re-derivation across the
project's history, now including this draft's own check). **No error
found.**

## 7. Graph rigidity

Fresh check: the draft's Lemma~5.7 proof was written from scratch for
this manuscript (not copied from Round 4's prose, which relied more
heavily on citing the exhaustive computational check) — using only the
tree structure and uniqueness-of-adjacency argument, as the round's
instruction required ("not merely computationally"). Re-verified the
logic step by step: leaf uniqueness in a tree ⟹ `φ(S1)=S1`, `φ(S3)=S3`;
`S2` as the unique common neighbor of `S1,S3` ⟹ `φ(S2)=S2`. Cross-checked
against the exhaustive 5040-permutation computation from Phase 5
(cited in Remark~5.8 as an independent check, not the proof) — the two
methods agree. **No error found.**

## 8. NS basis rank

Fresh check: `2 (O,F) + 3×6 (non-identity fiber components) = 20`,
matching Shioda–Tate's `2+Σ(m_v-1)+rank(MW) = 2+18+0=20`. Re-confirmed the
torsion-affects-index-not-rank argument is logically sound (torsion
sections are `Z`-linear combinations of already-counted trivial-lattice
generators). **No error found.**

---

## Summary

**One substantive error was found and fixed**: a variable-labeling bug in
the projective-reduction lemma's proof (§2) that would have made the
proof, as originally drafted, literally false (though the theorem
statement itself was always true). It was caught by exactly the process
this phase's instructions specified — redoing the computation fresh
rather than trusting the prose — and fixed with an explicit warning
comment in the corrected text to prevent recurrence.

No other error was found across the remaining seven attack targets,
including one genuine strengthening (Target 5, the independent-chart
cross-check of the multiplicity-one claim) beyond what Phase 5's original
audit performed.

**This draft is judged safe to proceed to Phase 2B** on the condition that
the fix documented above is understood to be part of the finalized
Section 2 text — it has been applied to `class3_hypercuboid_k3.tex` and
the file recompiles cleanly (10 pages, no undefined references, no
errors) with the fix in place.
