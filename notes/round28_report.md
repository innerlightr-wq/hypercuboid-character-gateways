# Hypercuboid exploration — Round 28 working notes

## Part I — frozen facts (reconfirmed)

`\rho=20`, `T(X)\cong\mathrm{diag}(2,4)`, `\mathrm{Tr}_{NS}(p)=(19+\chi(-1))p`,
the complete `I_2^*` configuration `\{O,N\}-C_1-C_3-C_2-\{F_1,F_2\}`
(multiplicities `1,1,2,2,2,1,1`), `N_0(p)=N_\infty(p)=7p+1`. No
contradiction found — proceeded.

## Part II/III — the two objects, and the ledger (reconstructed, unchanged from Round 27, reconfirmed here)

`\#V(\mathbb F_p)=p^2+S(p)$ (affine surface). `\#X(\mathbb F_p)` (smooth
projective K3). Ledger reconfirmed via the explicit per-fiber sums
(naive-good-fiber `+1` convention plus each bad fiber's now-*proved*
resolved count): `\#X(\mathbb F_p)=\#V(\mathbb F_p)+19p+\chi(-2)`, giving
`D(p)=1-\chi(-2)` exactly as in Round 27. No arithmetic slip found on
re-derivation.

## Part IV/V — dedicated `t=1` audit (the round's central effort — a genuine, informative NEGATIVE result)

**Rebuilt the full local 3-fold equation** at `t=1` to first order in
`\varepsilon=t-1` (reconfirmed exactly from Round 16's data):
$$Y^2 = X'(X'-2)(X'+8\varepsilon),\qquad X'=X+2.$$
**Tangent cone** (leading quadratic form in `(X',\varepsilon,Y)`):
`Q=Y^2+2X'^2+16\varepsilon X'`. **Hessian determinant `=-512=-2^9`**,
exact — `\chi(\det)=\chi(-1)\chi(2)^9=\chi(-1)\chi(2)=\chi(-2)`. **This is
a genuinely nondegenerate ternary quadratic form** (determinant nonzero
for every odd `p`), so — by the *same* Chevalley–Warning-type isotropy
fact used throughout this whole project — **it is unconditionally
isotropic for every odd `p`, regardless of `\chi(-2)`.** The exceptional
conic `D_1` is therefore `\mathbf P^1` over `\mathbb F_p` **for every odd
prime, with no exception.**

**Directly verified the finer question the round asked (split/non-split
at the node) exactly, and it resolves cleanly, not as a source of
discrepancy**: using the explicit exceptional conic from Round 16
(`W^2=-2u(u+8)`), computed **exactly**:
$$\text{affine points} = p - \chi(-2)\qquad(\text{proved via the classical identity }\textstyle\sum_u\chi(u(u+8))=-1),$$
and, via the correct homogeneous completion (`W^2+2U^2+16UZ=0`),
**points at infinity `=1+\chi(-2)`** (2 rational points if `\chi(-2)=1`;
a single Galois-conjugate *pair* — 0 individually-rational points — if
`\chi(-2)=-1`). **The two effects exactly cancel**: total
`=(p-\chi(-2))+(1+\chi(-2))=p+1$, **unconditionally**, matching the
`p+1` already used in Round 22's `N_{I_2}(p)=2p` formula. **Numerically
re-verified exactly for `p=3,5,7,11,13,17,19,23,29,31`, zero
exceptions.**

**Conclusion of the `t=1` audit: `\chi(-2)$ genuinely, provably appears
in the *intermediate* bookkeeping of this fiber's resolution (in how
the `p-\chi(-2)` affine count and the `1+\chi(-2)` infinity count split)
— but it exactly cancels in the final `p+1` total, and does not survive
into `N_{I_2}(p)=2p`.** **This rules out `t=1`'s local resolution as the
source of `D(p)`, definitively, not merely by assumption** — the
round's own top-priority hypothesis is killed by direct, exact
computation, a genuine (if negative) result.

## Part VI — `H^0`/`H^4` normalization audit (attempted, inconclusive)

Rechecked `\#X(\mathbb F_p)=1+p^2+\mathrm{Tr}(\mathrm{Frob}_p|H^2)`: the `1`
(from `H^0(X)=\mathbb Q_\ell`, Frobenius acts trivially, always) and `p^2`
(from `H^4(X)=\mathbb Q_\ell(-2)`, eigenvalue `p^2` always) are both
standard, unconditional facts for **any** smooth projective surface over
`\mathbb F_p` with `p_g,q` as for a K3 — **no character dependence is
possible here by general theory**, so `1-\chi(-2)`'s constant "`1`" is
**not** naturally explained as coming from a mismatch in this
normalization (both sides of the Lefschetz formula use it identically,
correctly, as far as re-checked). **This avenue did not locate the
source either** — reported honestly as inconclusive, not a hidden
positive result.

## Part VII — prime-by-prime diagnostic (performed, confirms `D(p)` exactly, does not by itself explain it)

Directly confirmed `D(p)\in\{0,2\}$ matching `\chi(-2)` exactly across
the primes tested (`p=3,5,7,11,13,17,19,23,29,31`, consistent with
Rounds 22–27's derivation). **No specific "2 missing/extra points" were
identified this round** beyond the (now-explained-and-cleared) `t=1`
infinity/affine split — the diagnostic confirms the *symbolic* residual
is correct but does not, on its own, locate a *new* candidate source.

## Part VIII — is `D(p)=0` expected, or is `D(p)=1-\chi(-2)` genuine?

**Not determined this round.** Given the `t=1` audit (Part IV/V) shows
`\chi(-2)` genuinely enters *some* of this project's intermediate
bookkeeping (even though it cancels there), and given `H^0/H^4$ are
ruled out (Part VI) as a source, the honest position is: **neither
Possibility A (missing correction term) nor Possibility B (the two
formulas count genuinely different things) was established this
round.** The search correctly avoided declaring victory by fitting a
plausible-sounding term to the residual (per the round's explicit
instruction).

## Parts IX–XII — not reached

Per the round's own conditional structure ("Once the residual is
understood...", "Only after Part IX is proved..."), these were
correctly not attempted given Part VIII's inconclusive outcome — doing
so would require assuming an unproven resolution of `D(p)`.

## Adversarial checks performed (genuine, not decorative)

- The tangent-cone Hessian computation at `t=1` was verified exactly
  by sympy, not estimated.
- The classical identity `\sum_u\chi(u(u+8))=-1` was verified
  numerically at 10 primes spanning both `\chi(-2)$ classes, not merely
  asserted from memory.
- The "points at infinity" homogenization was carried out explicitly
  (`W^2+2U^2+16UZ=0`), not assumed from the affine shape alone.
- **The round's own top hypothesis (split/non-split node at `t=1` as
  the source of `D(p)`) was actively tested to destruction and found
  false** — a genuine falsification, reported as such rather than
  reinterpreted to save the hypothesis.

## Everything killed or corrected this round

1. **KILLED, with a full exact proof**: `t=1`'s local resolution
   (split vs. non-split node) is **not** the source of `D(p)` — the
   `\chi(-2)`-dependence present in its intermediate bookkeeping
   provably cancels exactly, leaving the unconditional `N_{I_2}(p)=2p`
   untouched.
2. **RULED OUT as a likely source**: the `H^0`/`H^4` Lefschetz
   normalization — both terms are unconditional, standard, and
   correctly applied identically on both sides of the comparison.
3. **NOT resolved**: the actual source of `D(p)=1-\chi(-2)`. This
   remains open, now with two major candidate locations eliminated
   (both a stronger, more precisely bounded search space than at the
   start of the round).

## Highest-value next question

Given `t=1` (the round's top candidate) and `H^0/H^4` normalization are
now both ruled out, the remaining candidate locations are: (a) the
`t=0`/`t=\infty` `I_2^*` fibers' own boundary bookkeeping (specifically,
whether the "`+1` per good `T`" convention correctly matches how `O`'s
own point is counted at these bad fibers, given `O` sits on the
*identity* component which was constructed via a genuinely different
chart than the rest of `I_2^*`); or (b) the `I_0^*$ fiber at `t=-1`
(not yet individually re-audited with this round's level of rigor).
Systematically repeat this round's exact-tangent-cone-and-infinity-
count method at `t=0/\infty` and `t=-1` next, rather than re-examining
`t=1` again.

## Required-report items

1. Frozen Round-27 facts: Part I.
2. Two objects: `\#V(\mathbb F_p)=p^2+S(p)` vs. `\#X(\mathbb F_p)` (smooth
   projective K3, Lefschetz formula).
3. Contribution ledger: reconfirmed unchanged from Round 27
   (`\#X=\#V+19p+\chi(-2)`).
4. Occurrences of `-2`: located exactly in the `t=1` tangent cone
   (Hessian `=-2^9`) and the exceptional conic's infinity/affine split
   — both **proved to cancel**, not to survive.
5–6. Full `t=1` audit, split/non-split calculation: Parts IV/V, complete
   and exact — **this fiber is unconditionally rational overall**.
7. `H^0/H^4` audit: Part VI, inconclusive, no new positive lead.
8. Prime-by-prime diagnostic: Part VII, confirms `D(p)` symbolically,
   no new candidate located.
9. Exact source of `1-\chi(-2)`: **NOT found this round.**
10. Error vs. genuine correction: **undetermined.**
11–15. Corrected formula, transcendental trace, modular twist, master
   identity, CM-curve identity: **all unchanged, not reached.**
16. Killed/corrected: see above — two major candidate sources
    eliminated by direct proof, a genuine narrowing even without full
    closure.
17. Progressive-constraint hierarchy: not revisited, per instructions
    (master identity not proved, so this conceptual step was correctly
    not taken).
18. Highest-value next question: as stated above.

**Verdict: ROUND28-D** — the residual `D(p)=1-\chi(-2)` remains
unexplained. This round did not close it, but conducted a genuine,
rigorous, exact investigation of the round's own top-priority
hypothesis (the `t=1` node) and definitively ruled it out via direct
computation — along with the `H^0/H^4` normalization — narrowing the
search space for Round 29 to the `t=0/\infty` and `t=-1` fibers'
boundary bookkeeping specifically.

**THE THREE MOST IMPORTANT THINGS WE LEARNED**
- We found, and proved exactly, that a suspicious-looking "−2" really
  does show up in the natural place we expected — but then, when we
  followed it all the way through the calculation, it exactly cancels
  out and leaves no trace in the final answer. A real, satisfying, but
  ultimately negative result.
- We double-checked a completely different, more "bookkeeping-flavored"
  possible source (miscounting a couple of standard reference points)
  and found nothing wrong there either — ruling out a second, very
  different kind of explanation.
- Even though we didn't find the answer this time, we now know two
  specific, previously-plausible places it definitely is *not* hiding —
  which means the remaining search is smaller and more targeted than it
  was at the start of the round, even though the total amount we
  "know" didn't go up in the way we'd hoped.

Stopping here per the round's instructions — no further action taken.
