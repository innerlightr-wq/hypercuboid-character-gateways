# Hypercuboid exploration — Round 32 working notes

## Part I — frozen O(p) information (untouched)

`\rho(X)=20`, `T(X)=\mathrm{diag}(2,4)`, `\mathrm{Tr}_{NS}(p)=(19+\chi(-1))p`,
the complete Kodaira types/multiplicities, and Round 31's Kummer/CM
results — all frozen, `p`-coefficients not revisited. **This round finds
its result entirely within the constant (`O(1)`) terms**, exactly as
scoped.

## Part II — constant-term ledger, `\#X(\mathbb F_p)-\#V(\mathbb F_p)`, fiber by fiber

Rebuilt **from sets, not Euler characteristics**: for each `t\in\mathbb P^1(\mathbb F_p)`,
compare the *resolved fiber* `X_t(\mathbb F_p)` against the *naive affine
count* `V_t^{\text{naive}}(\mathbb F_p)=\#\{(x,y):y^2=t(t+1)x(x+1)(x+t)\}`
(literally plugging `t` into the defining equation, no resolution).

| source | resolved `X_t(\mathbb F_p)` | naive `V_t^{\text{naive}}` | contribution `Ap+B` |
|---|---|---|---|
| generic `t` (`p-3` values) | `p+1-a_t` (elliptic curve) | `p-a_t` | `1\cdot p + (-3)` total over all `p-3` of them |
| `t=0` (`I_2^*`) | `7p+1` | `p` (since `y^2=0`) | `6p+1` |
| `t=1` (`I_2`) | `N_{I_2}(p)` | `p-\chi(-2)` (character sum, Part VIII) | see Part V |
| `t=-1` (`I_0^*`) | `5p+1` | `p` (since `y^2=0`) | `4p+1` |
| `t=\infty` | `7p+1` | (not part of `V` at all) | `7p+1`, wholesale |

No bundled corrections: every `+1`, every naive count, tracked
individually as above; Part V isolates the one entry that needed
correcting.

## Part III — `I_2^*` constant, re-derived from unions (reconfirmed, unconditional)

The 7 components (`\{O,N\}-C_1-C_3-C_2-\{F_1,F_2\}`, multiplicities
`1,1,2,2,2,1,1`) form a **tree** (6 edges). For a tree of `\mathbf P^1`'s,
`\#(\bigcup C_i)(\mathbb F_p)=\sum_i\#C_i(\mathbb F_p)-\sum_{\text{edges}}\#(\text{node})(\mathbb F_p)`
(each edge subtracted exactly once, no double-subtraction issue since a
tree has no cycles). With 7 components each contributing `p+1` if
counted with multiplicity 1, **but** components of multiplicity `\ge2`
in the fiber divisor are *reduced* curves as sets (multiplicity affects
the divisor, not the point count) — so as a **set** the union is over 7
genuinely distinct rational curves, each `\cong\mathbf P^1_{\mathbb F_p}`
(established Rounds 24–27 via the Chevalley–Warning isotropy mechanism,
**unconditional for every odd `p`**), giving `7(p+1)` before
subtraction. **6 edges, each an intersection point**: Rounds 26/27
explicitly verified **each of these 6 junction points individually**
(not just each component's own total) is `\mathbb F_p`-rational —
critically, **including the previously-gap-prone `A=\infty` junction**
(Round 26/27) and the identity–`C_1` junction (Round 26, "Case A,
smooth and transverse"). `7(p+1)-6=7p+1`. **Re-checked this round
specifically for hidden `\chi(-2)`-dependence in any of the 6 junctions**:
none found — every junction's rationality proof (Rounds 24–27) rested on
either (a) the Chevalley–Warning ternary-isotropy mechanism (unconditional
for any nondegenerate form in `\ge3` variables, no character can enter)
or (b) an implicit-function-theorem argument with a nonzero *integer*
partial derivative (Round 29's `\partial K/\partial\varepsilon\in\{1,-2,-2\}`
pattern — again unconditional, no residue-class dependence). **`+1`
confirmed genuinely unconditional at both `t=0` and `t=\infty`,
independently.**

## Part IV — `I_0^*` constant, re-derived from unions (reconfirmed, unconditional)

5 components (1 center, multiplicity 2; 4 outer legs, multiplicity 1),
a **star graph**, 4 edges. `4(p+1)-4=4p+4`... wait — **the standard
star-graph union count is `(\text{center})+\sum(\text{legs})-4\cdot(\text{shared node count})`**:
5 components, `5(p+1)`, minus 4 edges (center meets each leg at 1 point)
`=5p+5-4=5p+1`. ✓ matches. **All 4 center–leg junctions, plus the 3
named components' own `\rho=\infty` points (the gap Round 29 closed),
were re-examined this round for `\chi(-2)`-dependence specifically**:
Round 29's `\partial K_2/\partial U=1$ identically (all three cases) is
an **integer, sign-independent, character-free** derivative — genuinely
no room for `\chi(-2)` to enter. **`+1` reconfirmed unconditional.**

## Part V — `I_2` constant: re-derived set-theoretically — **THE SOURCE FOUND**

`I_2`'s dual graph is a **2-cycle** (`C_1,C_2` meeting at **2** points,
not 1) — this is the key structural difference from the tree cases
above, and the round's instruction to "keep the affine exceptional conic
and points at infinity separate until the last line" is exactly what
exposes the issue.

**Reconstructing from the actual Round 16/28 equations** (not
re-guessed): near `t=1`, `X=X'-2`, the surface is
`Y^2=X'(X'-2)(X'+8\varepsilon)` (`\varepsilon=t-1`). At `\varepsilon=0`:
`Y^2=X'^2(X'-2)`, a **nodal cubic**, node at `(X',Y)=(0,0)`.

**Component `C_1`** (strict transform / normalization of this nodal
cubic): parametrize by slope `s=Y/X'`: `s^2=X'-2\Rightarrow X'=s^2+2,\ Y=s(s^2+2)`,
an honest `\mathbf P^1_s` — `\#C_1(\mathbb F_p)=p+1$ (unconditional). The
node's **two branches** are the two preimages of `(X',Y)=(0,0)`, i.e.
`s^2=-2\Rightarrow s=\pm\sqrt{-2}` — **individually `\mathbb F_p`-rational
iff `\chi(-2)=1`**, else a Galois-conjugate pair.

**Component `C_2`** (exceptional conic from blowing up the node): the
weighted substitution `X'=\varepsilon u,\ Y=\varepsilon w` into the full
equation gives `w^2=u(u+8)(\varepsilon u-2)`, and at `\varepsilon=0`:
`W^2=-2u(u+8)` (Round 28's conic, `W=w$). `\#C_2(\mathbb F_p)=p+1`
(Round 28, reconfirmed this round: affine `=p-\chi(-2)`, points at
infinity `=1+\chi(-2)`, verified exactly at `p=3,5,7,11,13,17,19,23`).
**The points at infinity of this conic satisfy, dividing `W^2=-2u(u+8)`
by `u^2$ as `u\to\infty`: `(W/u)^2\to-2$** — **individually `\mathbb F_p`-
rational iff `\chi(-2)=1`**, else a Galois-conjugate pair — **exactly
the same condition as `C_1`'s node-branch points.**

**These are the SAME two points**: `C_1`'s node-tangent directions
(`s=\pm\sqrt{-2}`, from the tangent cone of the nodal cubic at its
singular point) and `C_2`'s points at infinity (the directions the
blow-up chart "escapes to" as it reconnects with the original curve)
are, by the standard general fact about blowing up a node, **one and the
same locus — `C_1\cap C_2`, the 2 geometric points where the resolved
fiber's two components actually meet.**

**Therefore `\#(C_1\cap C_2)(\mathbb F_p) = 2$ if `\chi(-2)=1`, and
`=0` (non-rational conjugate pair) if `\chi(-2)=-1$ — genuinely
`\chi(-2)`-dependent, unlike every junction checked in Parts III/IV.**

$$N_{I_2}(p) = \#C_1(\mathbb F_p)+\#C_2(\mathbb F_p)-\#(C_1\cap C_2)(\mathbb F_p)
= (p+1)+(p+1)-(1+\chi(-2)) = \boxed{2p+1-\chi(-2)}.$$

**This is NOT `2p$ unconditionally** (Round 22/28's stated formula) —
it equals `2p` only when `\chi(-2)=1`, and `2p+2` when `\chi(-2)=-1`.
**Round 28's own computation was correct as far as it went** (it
rigorously established `\#C_2(\mathbb F_p)=p+1` unconditionally, and
correctly found the conic's *own* affine/infinity split cancels) — but
it **did not go the additional step of checking whether the conic's
points at infinity coincide with `C_1\cap C_2`**, and hence whether they
should be *subtracted* (as shared/double-counted points) in the full
union formula for `N_{I_2}(p)`. **This is the source.** Verified
numerically (`/tmp/round32_verify.py`, `p=3,5,7,11,13,17,19,23`): the
corrected formula gives `N_{I_2}=2p` exactly when `\chi(-2)=1`
(`p=3,11,17,19`) and `N_{I_2}=2p+2` when `\chi(-2)=-1`
(`p=5,7,13,23`), never `2p` there.

## Part VI — base compactification

`t=\infty`'s fiber (`I_2^*`, `7p+1`) is not a correction to any `V_t`
— it is **wholesale new** (already tracked as such in Part II's table,
row 5), since `V` only has `t\in\mathbb A^1`. No double-counting found:
`t=\infty` is not "implicitly" present anywhere else in `V`'s count.

## Part VII — Lefschetz constants, normalization traced

`\#X(\mathbb F_p)=1+p^2+\mathrm{Tr}(\mathrm{Frob}_p|H^2)`: `H^0(X,\mathbb Q_\ell)=\mathbb Q_\ell`
(rank 1, Frobenius acts as identity — trivial for any geometrically
connected smooth projective variety, `X` is a K3, `h^{0,0}=1$, unconditional)
gives the **first** `+1$; `H^4(X,\mathbb Q_\ell)=\mathbb Q_\ell(-2)` (rank 1, Poincaré
dual to `H^0`, Frobenius eigenvalue exactly `p^2`, unconditional) gives
the `p^2` term. **Exactly one `+1`, not zero or two** — confirmed by
explicit normalization tracing, not merely quoted.

## Part VIII — character-sum constant, re-audited

`\#V=p^2+S(p)` via `\#\{(x,t,y):y^2=f(x,t)\}=\sum_{x,t}(1+\chi(f(x,t)))=p^2+S(p)`.
Classified the zero locus `f(x,t)=0`: `x=0`, `x=-1`, `t=0`, `t=-1`,
`x=-t` (5 lines in the `(x,t)`-plane) and their pairwise intersections
(`(x,t)\in\{(0,0),(0,-1),(-1,0),(-1,-1),(0,0)_{x=-t\cap x=0},(-1,1)_{x=-t\cap x=-1}\}`,
etc. — a finite, explicit set). **`1+\chi(0)=1`** is used at every point
of this locus uniformly (a single point contributes exactly `1`,
matching `\#\{y:y^2=0\}=1`) — **this introduces no hidden correction**:
it is a completely general, character-independent fact (`y^2=0\iff y=0`,
exactly one solution, for any field), used identically regardless of
*why* `f(x,t)=0$ at that point. No new issue found here — consistent
with Round 29's from-scratch re-derivation.

## Part IX — prime-by-prime constant ledger

| `p` | `\chi(-2)` | good-fiber `B` | `t{=}0` `B` | `t{=}1$ `B` (corrected) | `t{=}{-}1` `B` | `t{=}\infty` `B` | **total `B`** |
|---|---|---|---|---|---|---|---|
| 3  | `+1` | `-3` | `1` | `1` | `1` | `1` | **`1`** |
| 5  | `-1` | `-3` | `1` | `1` | `1` | `1` | **`1`** |
| 7  | `-1` | `-3` | `1` | `1` | `1` | `1` | **`1`** |
| 11 | `+1` | `-3` | `1` | `1` | `1` | `1` | **`1`** |
| 13 | `-1` | `-3` | `1` | `1` | `1` | `1` | **`1`** |
| 17 | `+1` | `-3` | `1` | `1` | `1` | `1` | **`1`** |

(the `t=1` column's constant is `+1` **unconditionally** once
`N_{I_2}(p)=2p+1-\chi(-2)` replaces `2p$ — contribution
`=(2p+1-\chi(-2))-(p-\chi(-2))=p+1`, constant part `1`, in **both**
`\chi(-2)` regimes, confirmed directly in this table). **Total constant
`B=1` for every tested prime in both `\chi(-2)` regimes — the row that
used to differ (`t=1`) no longer does, once corrected.**

## Part X — reverse-engineering the two missing points

For `\chi(-2)=-1` primes, `D(p)=2` (old ledger) is now explained: **the
two missing points are precisely the two Galois-conjugate points where
the `I_2` fiber's two components meet** (`C_1\cap C_2`, Part V) — when
`\chi(-2)=-1` these are a single degree-2 closed point (not two rational
points), so the naive inclusion–exclusion subtraction of "`2`" was
**wrong by exactly `2`** in that regime (should subtract `0`, not `2`,
since there are zero individually-rational intersection points to avoid
double-counting). **These are genuine, already-identified geometric
objects** — not invented for this purpose.

## Part XI — closed-point interpretation

**Confirmed exactly**: `C_1\cap C_2` is precisely such a degree-2 closed
point — split (2 rational points) iff `\chi(-2)=1`, inert (0 rational
points, one closed point of degree 2) iff `\chi(-2)=-1`. This is not a
new object invented to fit the character; it is the **already-existing**
node-resolution intersection locus, whose rationality was correctly
computed piecewise by Round 28 (as part of `C_2`'s own point count) but
never checked **against `C_1`** for the union-formula purposes of
`N_{I_2}(p)` itself.

## Part XII — is an `O(1)` correction compatible with the transcendental representation?

**No — and this is exactly why the error had to be geometric.**
`\mathrm{Tr}_{NS}(p)$ is forced to be an **exact integer multiple of
`p`**: `NS(X_{\bar{\mathbb F}_p})` is a rank-20 lattice on which Frobenius
acts as a genuine lattice automorphism; Tate-twisting, its eigenvalues
have absolute value exactly `1` (purity, before the twist) — an
**algebraic integer all of whose conjugates have absolute value 1 is a
root of unity** (Kronecker's theorem), so Frobenius on `NS` has **finite
order**, and (since only real quadratic twists occur here) eigenvalues
`\pm1` — `\mathrm{Tr}_{NS}(p)/p\in\mathbb Z` unconditionally, **no bounded
non-multiple-of-`p`** correction is structurally possible. Separately,
`\mathrm{Tr}_T(p)` is constrained by **Livné's classification theorem**
(already invoked Round 22/30 to identify `8.3.d.a`): `T(X)\otimes\mathbb Q_\ell`
is *isomorphic*, as a compatible system of Galois representations, to
`\rho_f\otimes\chi` for a **single fixed** quadratic character `\chi` —
isomorphic representations have **identically equal** traces at every
good prime, with **no room for any further additive term**, bounded or
not. **Conclusion: neither `\mathrm{Tr}_{NS}` nor `\mathrm{Tr}_T` can
harbor a bounded, non-`p`-proportional residual — the only remaining
place such a term *can* legally live is `H^0`'s constant (fixed at
exactly `1`, unconditional, Part VII) or the geometric ledger's own
constant, i.e. exactly where Part V found it.**

## Part XIII — consistency triangle

- **A (geometry)**: `\#X-\#V` — **old**: `19p+\chi(-2)` (Round 27).
  **corrected this round**: `19p+1` (Part II/V, re-derived from sets).
- **B (cohomology)**: `1+p^2+\mathrm{Tr}_{NS}+\mathrm{Tr}_T-\#V = 1+(19+\chi(-1))p+\chi(-1)a_p(f)-S(p)`.
  Using the true (bulletproof, Part IX/XII of Rounds 30-31) `S(p)=\chi(-1)(a_p(f)+p)`:
  `B=1+(19+\chi(-1))p+\chi(-1)a_p(f)-\chi(-1)a_p(f)-\chi(-1)p=19p+1`.
- **C (direct arithmetic)**: `S(p)=\chi(-1)(a_p(f)+p)`, computationally
  bulletproof, `p<150`, zero exceptions (re-confirmed this round, see
  numeric table below).

**Result: the *corrected* `A` (`19p+1`) matches `B` (`19p+1`) exactly.
The *old* `A` (`19p+\chi(-2)`) is the outlier — it agreed with neither
`B` nor the geometry once `N_{I_2}(p)`'s intersection points are
correctly accounted for.** The faulty edge, isolated: **the old
`N_{I_2}(p)=2p` claim** (Round 22/28), specifically its implicit
assumption that `C_1\cap C_2` is always 2 rational points.

**Direct numerical confirmation** (`/tmp/round32_full_check.py`, LMFDB
`8.3.d.a` traces, `p\in\{3,\dots,41\}`): forcing `\mathrm{Tr}_T(p)` from
the **corrected** ledger (`19p+1`) via
`\mathrm{Tr}_T(p)=S(p)-\chi(-1)p` reproduces `\chi(-1)a_p(f)` **exactly**
at **every** tested prime, both `\chi(-2)` regimes — **zero residual.**

## Part XIV — master identity

$$\boxed{S(p) = \chi(-1)(a_p(f)+p)} \qquad\text{equivalently}\qquad \boxed{S(p)=-\chi(2)p+\chi(-1)a_p(E)^2}$$
now follow **exactly** from: (1) `\#V=p^2+S(p)` [proved, elementary];
(2) the **corrected** ledger `\#X=\#V+19p+1` [Part II/V, re-derived from
sets this round, with the one-line `N_{I_2}(p)` fix]; (3)
`\mathrm{Tr}_{NS}(p)=(19+\chi(-1))p` [proved, Round 22]; (4)
`\mathrm{Tr}_T(p)=\chi(-1)a_p(f)$ [Livné's theorem forces `\mathrm{Tr}_T(p)=\chi\cdot a_p(f)`
for a *fixed* character `\chi`; **`\chi=\chi(-1)` specifically is
supported by three independent lines of reasoning (Round 21's proved
Galois action on the algebraic Mordell–Weil generator; Round 30's
elimination of the "no twist" alternative; Round 31's clean, independent
`\mathrm{Tr}_T(\mathrm{Km}\,A)=a_p(f)` Kummer-side computation combined
with the expected quadratic-twist relationship between `X`'s and
`\mathrm{Km}(A)`'s arithmetic models) — but has not been proved by a
single direct computation of Galois action on a transcendental cycle/period
of `X` itself, the way Round 21 did for the algebraic class.** This is
the **one remaining logical bridge**, narrower and more sharply defined
than anything in Rounds 27–31: not "why is there a residual" but "prove,
not just support by convergent evidence, that `\chi=\chi(-1)` specifically."

**Do not declare fully proved on numerical grounds alone** — the
`N_{I_2}(p)$ correction (1)-(3) is now a complete, from-scratch,
numerically-confirmed derivation with no numerical fitting involved (it
was derived from the actual blow-up equations, then checked); (4)'s
`\chi(-1)` identification remains the one piece resting partly on
convergent-but-indirect evidence rather than a single direct proof.

## Everything killed or corrected this round

1. **CORRECTED (a genuine error found, not merely a residual)**:
   `N_{I_2}(p)=2p` (Round 22/28) is **false** whenever `\chi(-2)=-1`; the
   correct unconditional formula is `N_{I_2}(p)=2p+1-\chi(-2)`. Source:
   the fiber's two intersection points (`C_1\cap C_2`) form a
   `\chi(-2)$-dependent degree-2 closed point, previously assumed
   rational in both cases.
2. **CORRECTED accordingly**: `\#X(\mathbb F_p)=\#V(\mathbb F_p)+19p+\chi(-2)`
   (Round 27) is replaced by `\#X(\mathbb F_p)=\#V(\mathbb F_p)+19p+1`.
3. **RECONFIRMED, not the source**: `I_2^*` and `I_0^*`'s `+1` constants
   (Parts III/IV) — genuinely unconditional, no hidden `\chi(-2)`, both
   fibers being TREES (not cycles) where this specific failure mode
   cannot occur.
4. **PROVED, new tool**: `\mathrm{Tr}_{NS}(p)` is always an exact integer
   multiple of `p` (Kronecker's theorem applied to the finite-order
   Frobenius action on `NS`); `\mathrm{Tr}_T(p)` is forced by Livné's
   theorem to equal `\chi\cdot a_p(f)` exactly for a fixed `\chi`, no
   additive room — jointly proving any bounded residual **must** be
   geometric, correctly predicting where Part V's error was found.

## Required-report items

1. Full constant-term ledger: Part II.
2. Independent `I_2^*` constant derivation: Part III, `+1` unconditional.
3. Independent `I_0^*` constant derivation: Part IV, `+1` unconditional.
4. Independent `I_2` constant derivation: Part V — **`N_{I_2}(p)=2p+1-\chi(-2)`**,
   not `2p`.
5. Base-compactification constant: Part VI, `t=\infty` wholesale, no
   double-count.
6. Lefschetz `H^0/H^4` constants: Part VII, exactly one `+1`.
7. Character-sum zero-locus audit: Part VIII, clean.
8. Prime-by-prime constant table: Part IX, total `B=1` uniformly once
   corrected.
9. First source of `\chi(-2)`-dependent constant: the `t=1` (`I_2`)
   intersection points, Part V.
10. Discrepancy corresponds to actual geometric points: **YES** — the
    two conjugate points `C_1\cap C_2`, Part X.
11. Closed-point interpretation: **confirmed exactly**, Part XI.
12. Geometric ledger survives: **corrected version survives**
    (`19p+1`); the old `19p+\chi(-2)` version does not.
13. `O(1)` correction compatible with `\mathrm{Tr}_T`: **NO** (Part
    XII) — which is exactly why the true source had to be, and was
    found to be, geometric.
14. Consistency-triangle result: Part XIII — corrected `A` matches `B`
    exactly; old `A` was the faulty edge.
15. Master-identity status: Part XIV — algebraic structure now fully
    derived; one bridge remains (independent proof of the `\chi(-1)`
    twist on `T(X)` specifically, not just convergent support).
16. Killed/corrected: see above, item 1 is the headline finding.
17. Highest-value next question: prove `\mathrm{Tr}_T(p)=\chi(-1)a_p(f)`
    (not just `\chi\cdot a_p(f)` for some unspecified `\chi`) via a
    direct computation of the Galois action on an explicit
    transcendental cycle or period of `X`, mirroring Round 21's proof
    for the algebraic Mordell–Weil generator — the one remaining gap
    between "extremely well-supported" and "proved."

**Verdict: ROUND32-B** — the constant discrepancy is identified and
**fully explained** (a genuine, previously-undetected error in
`N_{I_2}(p)`'s intersection-point count, now corrected and confirmed
both symbolically and numerically to make `\#X=\#V+19p+1` exactly
consistent with `\mathrm{Tr}_{NS}`, the true `S(p)$, and
`\mathrm{Tr}_T(p)=\chi(-1)a_p(f)`) — but one specific, narrower proof
bridge remains: an independent, from-first-principles proof (not
convergent-evidence support) that the transcendental twist is
**specifically** `\chi(-1)`, not merely *some* fixed quadratic character.

**THE THREE MOST IMPORTANT THINGS WE LEARNED**
- We finally found the actual bug, not just another negative result: one
  of the small building-block formulas from many rounds ago undercounted
  by exactly 2 points at exactly the primes where it mattered, because
  two points where two curve-pieces cross were silently assumed to
  always be "real" (rational) when sometimes they're a linked pair that
  isn't individually real at all.
- We proved, using a clean and completely general argument (not specific
  to this surface), that the missing piece COULD ONLY be hiding in the
  plain geometric point-counting — not in either of the two "deeper"
  modular/algebraic quantities we'd been suspecting in recent rounds.
  That's what let us go looking in exactly the right place.
- Once we fixed that one formula, everything else in the whole chain —
  built up over more than fifteen rounds — clicked into place with zero
  leftover discrepancy, at every prime we checked. The remaining
  question is narrow and specific: nail down one particular twist choice
  with a direct proof instead of strong-but-indirect evidence.

Stopping here per the round's instructions — no further action taken.
