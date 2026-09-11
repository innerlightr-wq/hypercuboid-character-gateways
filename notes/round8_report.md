# Hypercuboid exploration — Round 8 working notes

## Part I — independent reproduction of the two Round-7 facts

Reconstructed Class I `(0,1,2,3,4,5)`, Class II `(1,2,3,4,5,6)`, Class III
`(0,1,2,4,5,6)` independently from `core.py` and recomputed `Sigma_S(p)` by
direct enumeration at 28 primes spanning all four residues mod 8
(5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,
103,107,109,113). Both Round-7 statements reconfirmed with zero exceptions:
`Sigma_II(p) = chi(-1)*Sigma_I(p)` and `Sigma_III(p)=0` for every `p==3
mod4` (13/13), nonzero for every `p==1 mod4` (14/14). Not treated as proved
by this reproduction alone — see Part II for the actual proof.

## Part II/III — Track A: Gateway G, an exact global coordinate-relabeling mechanism (PROVED)

**Key idea.** The construction eliminates one of the `n` original
coordinates (`A_n = -(A_1+...+A_{n-1})`) to get the `d=n-1` free variables
`x`. This breaks the natural `S_n` symmetry (permuting *all* `n` original
coordinates `A_1,...,A_n`) down to the `S_{n-1}` subgroup fixing `A_n`,
which is all that Round 6 exploited. Round 8 restores the full `S_n`
action and asks what it does to `Sigma_S(p)`.

For `n=4`: each of the 7 representative forms `L_J` corresponds to a
bipartition of `{1,2,3,4}` (`L_J = -L_{J^c}` since `sum_i A_i=0`): the 4
singletons `A_1,A_2,A_3,-A_4` (`1|3` splits) and the 3 pairs (`2|2`
splits). `S_4` acts on these bipartitions via its action on `{1,2,3,4}`,
inducing a linear bijection `T_pi` of `F_p^3` for every `pi` in `S_4`
(realized concretely as: substitute `A_i -> A_{pi(i)}` for `i=1,2,3`, solve
for the new `x`). Every such `T_pi` is a genuine bijection of `F_p^d` for
every prime `p` (it is literally a coordinate permutation of the
`n`-tuple, restricted to the zero-sum hyperplane).

Writing `P_I, P_II, P_III` for the degree-6 products defining Classes
I/II/III, an exhaustive symbolic scan of all 24 permutations of `S_4`
(`scripts/gateway_g_symmetry.py`) found, via exact polynomial expansion
(sympy, verified to literal 0 — a genuine algebraic identity over
`Z[x_0,x_1,x_2]`, not a per-prime numerical match):

1. **Class I / Class II relation (PROVED).** For `pi` = the 4-cycle
   `(1 2 3 4)` (`A_1->A_2->A_3->A_4->A_1`, giving `T(x)=(A_2,A_3,A_4)`,
   `det(T)=-1`):
   $$P_I(T(x)) = -P_{II}(x) \quad\text{identically (all }x\text{, all }p\text{).}$$
   Since `T` is a bijection of `F_p^3`, relabeling the summation variable
   gives
   $$\Sigma_I(p)=\sum_x\chi(P_I(x))=\sum_x\chi(P_I(Tx))=\sum_x\chi(-P_{II}(x))=\chi(-1)\Sigma_{II}(p)$$
   for **every** odd prime `p` — not merely the 16-28 tested. This is
   exactly the Round-7 empirical relation, now with a full derivation.

2. **Class III vanishing (PROVED).** For `pi` = the double transposition
   `(1 3)(2 4)` (`T(x)=(A_3,A_4,A_1)`, `det(T)=1`, and `T` is a genuine
   involution: `T(T(x))=x`, verified symbolically):
   $$P_{III}(T(x)) = -P_{III}(x) \quad\text{identically.}$$
   Fixed-locus audit (required before accepting an involution argument):
   `T`'s fixed line is `x_2=x_0, x_1=-x_0`; `P_III` restricted to this line
   is the zero polynomial — the only value consistent with
   `P_{III}(x)=-P_{III}(x)` holding at a fixed point over any field where
   `2` is invertible (odd `p`), confirming the identity is internally
   consistent, not merely true "off" some exceptional locus.
   Relabeling as above: `Sigma_III(p) = chi(-1)*Sigma_III(p)` for every
   odd `p`. When `chi(-1)=-1` (`p==3 mod4`) this forces
   `Sigma_III(p)=0` exactly (since `2` is invertible); when `chi(-1)=1`
   (`p==1 mod4`) it is vacuous, matching the observed nonvanishing.

Both are now **PROVED EXACT MECHANISMS**, upgraded from Round 7's
"COMPUTATIONALLY VERIFIED, mechanism not derived."

The full 24-permutation scan found *no other* sign relations among
`P_I,P_II,P_III` beyond: the two above (`-1`, cross/self), their group
conjugates/inverses, and several trivial `+1` self-stabilizers (elements
of the setwise stabilizer of each class, already implied by the known
`S_3`-invariance and adding no new information). In particular: no
permutation forces `Sigma_I(p)=0` or `Sigma_II(p)=0` unconditionally
(consistent with both being generically nonzero), and no permutation
relates Class III to Class I or II (Class III's only nontrivial relation
is to itself).

## Track B — where does `chi(-1)` enter?

Directly identified, not inferred: `chi(-1)` enters because `chi` is
completely multiplicative and the polynomial identities above produce a
**literal integer scalar factor of exactly `-1`** multiplying the whole
product (`P(Tx) = (-1)*P'(x)`, an honest `-1` in `Z`, not an
expression that varies with `p` or with `x`). `chi` applied to that
constant factor is `chi(-1)` by definition — nothing subtler (not a
determinant sign: `det(T)` was `-1` for the Class I/II map but `+1` for
the Class III involution, so `det(T)` does **not** track the phenomenon;
not a quadratic-twist coefficient — no elliptic curve was ever
constructed). Mod-8/mod-12 refinement was tested (Part I's 28-prime table
spans all four residues mod 8: 1,3,5,7): both relations hold with **zero
exceptions** regardless of `p mod 8`, confirming the dependence is
genuinely and only on `p mod 4` (via `chi(-1)`), not a coarser reading of
a finer congruence. Given this fully elementary derivation, no elliptic
curve or quadratic-twist language was needed or invoked (the instruction
to derive the curve explicitly before using such language was honored by
finding that no curve is needed at all).

## Gateway G — definition, scope, and classification

**Gateway G (global coordinate-relabeling symmetry).** For a family with
`n` original coordinates, the full symmetric group `S_n` (not just the
`S_{n-1}` subgroup fixing the eliminated coordinate) acts on the
bipartition-indexed representative forms. For `pi in S_n` and subsets
`S, S'` of forms such that `pi` maps `S`'s bipartitions onto `S'`'s, there
is an exact sign `eps(pi) in {+1,-1}`, computable by symbolic expansion of
`P_S(T_pi(x)) - eps(pi)*P_{S'}(x)` to `0`, giving
`Sigma_S(p) = chi(eps(pi)) * Sigma_{S'}(p)` for every odd `p`.

- **Proof status:** PROVED (exact polynomial identities, sympy-verified,
  plus the required fixed-point consistency check for self-relations).
- **Scope, stated honestly:** proved and verified for `n=4` only, on the
  three specific classes needed. Generalization to arbitrary `n` is a
  natural conjecture (the bipartition/`S_n` structure exists for every
  `n`) but was **not** attempted symbolically for `n=5,6` this round —
  flagged as the natural next step, not claimed.
- **Not reducible to A/B/C/E/F.** A/B/C/E are evaluation gateways (they
  compute a value from a structural condition on one form family). F is a
  representation gateway (it changes basis to expose A/B/C/E on a fiber).
  G is neither: it produces an exact **relation** between two `Sigma`
  values (possibly the same one) via a *different* representation
  (relabeling which coordinate is eliminated), and — critically — it does
  not touch the fiber/aggregate structure F uses at all. It is best
  classified as a **third kind: a relational gateway.**
- **Nontrivial application:** explains both flagged Round-7 facts exactly;
  reduces the "true" unknown count for `{Sigma_I, Sigma_II}` from 2 to 1,
  and resolves `Sigma_III(p)` completely for half of all primes
  (`p==3 mod4`), conditionally on the sign of `chi(-1)` at the fixed
  locus check passing (it does).
- **What G does NOT do:** it does not evaluate `Sigma_I(p)`, `Sigma_II(p)`
  outright, nor `Sigma_III(p)` at `p==1 mod4`. Those closed forms remain
  open (F-FAILED/F-REDUCED per Round 7 still stands for the *evaluation*
  question; G answers a different question).

## Track C — statistical/diagnostic pass on the still-open values

Since Class I/II/III are not fully evaluated by G, a light diagnostic
pass (not proof) was run on `Sigma_I(p)` (Class II adds nothing new, being
`chi(-1)*Sigma_I` exactly). Comparing `Sigma_I(p)` to `p(p-1)` across 28
primes split by `p mod 8` uncovered a clean **new exact pattern**:

$$\Sigma_I(p) = -\chi(2)\cdot p(p-1) \qquad\text{exactly, whenever } p\equiv 5,7\pmod 8$$

verified with **zero exceptions across all 15/15 tested primes** with
`p mod 8 in {5,7}` (5,7,13,23,29,31,37,47,53,61,71,79,101,103,109), while
the ratio `Sigma_I(p)/(p(p-1))` is irregular (no constant, no simple
half-integer) for all 13/13 tested primes with `p mod8 in {1,3}`
(11,17,19,41,43,59,67,73,83,89,97,107,113). `Sigma_III(p)` was checked
against both `p(p-1)` and `p^2` at all tested `p==1 mod4`: **no comparable
clean sub-pattern found** — ratios are irregular throughout, so this
particular diagnostic does not extend to Class III.

This is reported as a **COMPUTATIONALLY VERIFIED PATTERN**, not proved —
no mechanism has been derived for why `p mod 8 in {5,7}` (equivalently,
by quadratic reciprocity for 2, exactly the primes with `chi(2)=-1`... but
note the *formula itself* also multiplies by `chi(2)`, so this is not
tautological: at `p==5(8)`, `chi(2)=-1,chi(-1)=1`, ratio `+1`; at
`p==7(8)`, `chi(2)=1,chi(-1)=-1`, ratio `-1`; both match
`-chi(2)*p(p-1)` while the *other* two mod-8 classes, where `chi(2)` takes
the *opposite* value in each pairing, do not obey any such clean rule).
This is flagged as a well-defined, promising target for a future round,
not chased further here to respect this round's bounded scope.

## Hierarchy assessment (local -> intermediate -> global -> statistical)

- **Local exact (A/B/C/E):** unchanged from Round 7 — do not apply to
  Classes I/II/III directly.
- **Intermediate structural exact (F):** unchanged — F-FAILED (Class I),
  F-REDUCED (Classes II/III), as in Round 7.
- **Global exact (new, this round — Gateway G):** PROVED for the two
  flagged relations. This is a genuinely new rung in the hierarchy,
  operating on relations between classes rather than within one.
- **Statistical (Track C):** produced one new *exact* (not merely
  statistical) sub-pattern for Class I at `p mod 8 in {5,7}`, and a
  genuine negative result for Class III (no analogous pattern found).
  The hierarchy is not strictly ordered by strength of conclusion — an
  exploration nominally in the "statistical" tier surfaced an exact
  result, while the "global" tier's tools (G) provably cannot fully
  evaluate any of the three classes. Reported honestly rather than
  forcing the hierarchy to be monotone.

## Adversarial checks performed

- Full 24-permutation exhaustive scan (not just the two found relations)
  for hidden extra sign relations among `P_I,P_II,P_III`: none beyond
  those reported and their trivial `+1` stabilizer echoes.
- Fixed-point/zero-locus consistency check for the Class III involution
  (required before accepting it): passed.
- `T`'s bijectivity and (for Class III) involution property verified
  symbolically, not assumed.
- Mod-8 and mod-12-flavored refinement check on both proved relations:
  zero exceptions at any mod-8 residue, ruling out a finer congruence
  masquerading as mod 4.
- Elliptic-curve / quadratic-twist avenue: explicitly not pursued once
  the elementary permutation mechanism gave a complete, exact proof of
  both target facts — invoking curve language would have been forcing an
  interpretation the algebra does not need, per the round's own
  instruction not to force it.
