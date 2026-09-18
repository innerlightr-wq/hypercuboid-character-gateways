# Audit of the character-sum asymptotic

The asymptotic paper has been located. This document records its exact theorem, the exact proof
route, a correctness check, and — the point of the exercise — **whether the error term can be
sharpened.** Short answer: the main term can be made exact, the error exponent cannot be improved,
and the `O(p^2)` suggested by the previous audit is not attainable. That suggestion is withdrawn
here.

No PDF was edited.

## 1. The paper

**"Zero-Diagonal Complement Collapse and Character-Sum Asymptotics in Clean Finite-Field Hypercuboid
Residue Systems"**, Elias De Jesús, 15 pages, pdfTeX, created 2026-08-31.

SHA-256 `7994b538772237663aec70940278467a60c2512f65c894f006b80df5f4b03bbb`. No DOI, Zenodo ID or arXiv
number appears anywhere in it — it is an undeposited note, and it is **not committed to this
repository**.

It contains, at the numbering the repository's scripts cite:

* **Theorem 6.1** (Zero-diagonal clean asymptotic) — §6;
* **Proposition 6.2** (Exact vanishing of odd homogeneous character moments) — §6;
* **Appendix C.5** (Additional symmetry of the zero sector);
* **Section 9** (Computational diagnostics), which contains the small-`p` caution.

**All four references in `scripts/baseline_verification.py` are therefore correct, not stale.** The
previous audit's "documentation defect" is resolved: nothing was mis-numbered, the cited paper simply
was not in the repository. That earlier finding is corrected.

## 2. The exact theorem

> **Theorem 6.1 (Zero-diagonal clean asymptotic).** `N_0^clean(p,5) = 0` for `p ≡ 3 (mod 4)`; and, as
> `p → ∞` along `p ≡ 1 (mod 4)`,
> ```
> N_0^clean(p,5) = 2^{-15} p^4 + O(p^{7/2}).
> ```

Hypotheses and scope, as stated in the paper: `p` odd (`p = 2` excluded globally); "clean" is
Definition 2.1 — `A ∈ (QR_p^×)^n` with the `A_i` pairwise distinct and `D_I(A) ∈ QR_p^×` for every
nonempty proper `I ⊊ [n]`; ambient dimension 4 (parametrised by `A_1..A_4` with
`A_5 = −Σ_{i≤4}A_i`); 15 conditions; the implied constant depends on `m` (hence on `n`), and is
**explicit** — see §3. The statement is asymptotic; existence of a clean tuple follows only once `p`
exceeds the crossover, which the paper does not compute but explicitly flags in §9.

The engine is:

> **Theorem 5.1 (General character-count asymptotic).** For `d ≥ 1`, `p` odd, and `ℓ_1,…,ℓ_m`
> pairwise non-associate nonconstant affine-linear forms on `A^d(F_p)`, with
> `N_ε(p) = #{x ∈ F_p^d : ℓ_i(x) ≠ 0, χ(ℓ_i(x)) = ε_i ∀i}`,
> ```
> N_ε(p) = 2^{-m} p^d + O_m(p^{d−1/2}),
> ```
> explicitly for `d ≥ 2`:  `|N_ε(p) − 2^{-m}p^d| ≤ (m−1)p^{d−1/2} + (C(m,2) + m)p^{d−1}`.

## 3. How `p^{7/2}` is actually proved

Traced line by line. It is **not** a multivariate theorem; it is one-variable Weil applied fibrewise.

1. **Exact indicator.** `1_{QR}(t) = (1 + χ(t) − 1_{t=0})/2`, so `N_ε` equals a "formal" version minus
   a correction supported on `Z = ⋃_i{ℓ_i = 0}`, with `|Z| ≤ m p^{d−1}`. The paper folds this into the
   final constant rather than leaving it as a remark.
2. **Expansion.** `N_ε^formal = 2^{-m} Σ_{S⊆[m]} (∏_{i∈S}ε_i) Σ_S(p)` with
   `Σ_S(p) = Σ_x χ(∏_{i∈S}ℓ_i(x))` and `Σ_∅ = p^d`. So there are `2^m − 1` nontrivial terms.
3. **One variable summed nontrivially.** For nonempty `S`, pick `ℓ_{i_0} ∈ S` and a variable `x_k` it
   depends on; let `S_k` be the forms in `S` depending on `x_k`, `r' = |S_k| ≥ 1`. For fixed values of
   the other `d−1` variables the restriction to the `x_k`-line is a polynomial of degree `r'`, and two
   forms `ℓ_i = c_ix_k + d_i`, `ℓ_j = c_jx_k + d_j` share a root iff `c_jd_i − c_id_j = 0`.
4. **Degenerate fibres.** The paper shows `c_jd_i − c_id_j` cannot vanish identically without the two
   forms being associate — and handles the proportional-but-non-associate case explicitly, noting it
   occurs *exactly* for the 15 pairs `(L_J, 1 − L_J)` of §7, where constant-matching fails, so the bad
   locus is **empty**. Otherwise the bad locus is a hyperplane in the other variables: `O(p^{d−2})`
   choices, bounded trivially by `p` each.
5. **Weil on the good fibres.** The restriction is squarefree of degree `r' ≤ m`, so
   `|Σ_{x_k}χ(·)| ≤ (r'−1)√p ≤ (m−1)√p`. The other `d−1` variables are summed trivially: `p^{d−1}`
   choices. Hence `|Σ_S| ≤ (m−1)p^{d−1/2} + C(m,2)p^{d−1}`.
6. **No `2^m` blowup.** Summing over the `2^m − 1` nonempty `S` with the prefactor `2^{-m}` uses
   `2^{-m}(2^m − 1) < 1`, so the aggregate bound keeps the single-term constant.

**`4 − 1/2 = 7/2`** is therefore: one Weil saving in the one variable `x_k`, times `p^3` from summing
the other three trivially. The one-variable input is the classical bound; `Schmidt1976` gives it by an
elementary (non-cohomological) route, which matches the level of machinery the paper actually uses,
and `IwaniecKowalski2004` §11–12 is the standard modern reference for character sums of this shape.

**Is it rigorous as written?** Yes. The two places such an argument usually leaks — the `χ(0)` zero
locus and the fibres where the restricted polynomial fails to be squarefree — are both handled
explicitly and quantitatively, and the `2^m` prefactor is dealt with correctly. The degenerate-fibre
analysis at step 4 is the delicate part and it is done properly, including the case that actually
arises.

**Does the paper claim optimality?** No, and it is careful about this. Remark 6.3 says Proposition 6.2
"does not improve the exponent in Theorem 6.1 … nor does it materially tighten the stated constant",
and **Open Problem 11.1 asks precisely "Is the true error genuinely `O(p^{7/2})`, or does a sharper
argument give `O(p^3)` or better?"** Open Problems 11.3 and 11.6 ask the same for even-cardinality
cancellation and for Corollary 7.3. Deligne is never invoked; the only analytic citation is Weil 1948.

## 4. The proposed Deligne improvement does not work

The previous audit suggested `O(p^{7/2})` might improve to about `O(p^2)` because the ambient
dimension is 4. **That is withdrawn.** Three independent obstructions, checked rather than assumed.

### 4.1 The cone forces a factor of `p − 1` that cannot oscillate

Every form is homogeneous, and so are the distinctness conditions `A_i − A_j`, so the clean domain
`D` is a cone minus the origin: `x ∈ D ⟺ λx ∈ D` for `λ ≠ 0`. For even `|S|`, `F_S` is homogeneous of
even degree, hence `χ(F_S(λx)) = χ(F_S(x))`, so

```
T_S := Σ_{x∈D} ∏_{J∈S} χ(L_J(x))  =  (p−1) · Σ_{projective points of D} χ(F_S(v_ℓ)).
```

**Verified: `(p−1)` divides every even `T_S` exactly**, at all ten primes tested (the quotients are
24, 48, 144, 168, 408, 792, 912, 1560, 1968, 2264 at `p = 11,…,43`). The residual sum ranges over
`≈ p^3` projective points, so even granting full square-root cancellation there — `O(p^{3/2})` — the
best conceivable bound is

```
|T_S| = (p−1) · O(p^{3/2}) = O(p^{5/2}).
```

**`O(p^2)` is arithmetically impossible for these terms.** `O(p^{5/2})` is the floor.

### 4.2 Small subsets have character-blind directions, so nonresonance fails

The terms are Kummer (order-2) local systems on the complement of the arrangement, with nontrivial
monodromy only around the hyperplanes in `S`. Square-root cancellation in *all* four dimensions needs
cohomological concentration in the middle degree, which needs the system to be nonresonant and
geometrically nontrivial in every direction (`STV1995`). That fails concretely: the worst `|S| = 2`
subset found is `S = {x_1, x_2 + x_3}`, and

```
χ(F_S) = χ(x_1(x_2+x_3))   does not involve x_4 at all.
```

That direction is summed with no cancellation available, by construction. So there is no theorem of
the "nondegenerate `d`-dimensional sum ⇒ `O(p^{d/2})`" type to apply — the hypotheses are violated,
not merely unverified. Citing "Deligne" here would be citing a theorem whose hypotheses fail.

### 4.3 Empirically the terms really are of order `p^{7/2}`

Computed `max_S |T_S|` over the clean domain for `|S| = 2, 4, 6` at `p = 17,…,43` and fitted
`max|T_S| ~ C p^α` by log-log least squares over `p ≥ 23`:

| `|S|` | fitted `α` |
|---|---|
| 2 | 3.39 |
| 4 | 3.79 |
| 6 | 3.91 |

The range is short and the maxima fluctuate, so these exponents should not be read as precise. But
they are **consistent with the proven `7/2` and flatly inconsistent with `2` or `5/2`.** There is no
empirical sign that the bound is soft.

## 5. What *can* be sharpened: the main term becomes exact

The 15 forms `L_J` are all nonzero `0/1` forms in four variables — that is, the **resonance
arrangement `R_4`** (`Kuhne2023`), which the paper does not name. Computing its characteristic
polynomial directly and verifying against exact point counts at eleven primes (`7 ≤ p ≤ 43`, fitted on
five and predicting all eleven):

```
χ_{R_4}(p) = p^4 − 15p^3 + 80p^2 − 170p + 104 = (p−4)(p−1)(p^2 − 10p + 26).
```

Adjoining the 10 distinctness hyperplanes `A_i = A_j` gives the **clean ambient domain**, and it
factors:

```
|D| = p^4 − 25p^3 + 215p^2 − 695p + 504 = (p−1)(p−7)(p−8)(p−9),
```
also verified at all eleven primes. So the excluded locus is not merely `O(p^3)` — it is exact.

Because `D` is a cone, Proposition 6.2's argument applies verbatim over `D`: **`T_S = 0` exactly for
every odd `|S|`, over the restricted domain too** (verified: the odd-`|S|` maximum is `0` at every
prime tested). Hence the exact identity

```
N_0^clean(p,5) = 2^{-15}(p−1)(p−7)(p−8)(p−9) + 2^{-15} Σ_{|S| even, S ≠ ∅} T_S .
```

**This is the available sharpening.** It replaces `2^{-15}p^4` by a polynomial that is exactly right,
absorbing the `p^3`, `p^2` and `p^1` terms instead of hiding them in the error, and it reduces the
number of terms needing an estimate from `2^15 − 1 = 32767` to `2^14 − 1 = 16383`. It requires no new
analysis. It does **not** change the error exponent.

## 6. Best justified form, and the threshold

| Form | Justified? |
|---|---|
| `2^{-15}p^4 + O(p^{7/2})` | **yes — the paper's theorem, correct as proved** |
| `2^{-15}(p−1)(p−7)(p−8)(p−9) + O(p^{7/2})` | **yes — strictly sharper, no new analysis** |
| `… + O(p^3)` | only if even-`|S|` aggregate cancellation is proved (the paper's Open Problem 11.3); no evidence for it |
| `… + O(p^{5/2})` | the floor from §4.1; would need a vanishing theorem that does not apply to all `S` |
| `2^{-15}p^4 + O(p^2)` | **no — impossible; withdrawn** |

**Threshold, from the paper's own explicit constants.** With `m = 15`, `d = 4`, plus the 10
distinctness hyperplanes, the bound is `14p^{7/2} + 130p^3`, and a nonzero count needs

```
p^4/32768 > 14 p^{7/2} + 130 p^3 .
```

The binding term is the first: `√p > 2^{15}·14 = 458,752`, i.e.

```
p > 2.10 × 10^11      (solving the full inequality: p ≳ 2.14 × 10^11).
```

The previous audit's "`≈10^9`" used an implied constant of 1 and was therefore two orders too
optimistic; the rigorous figure from the stated constants is **`2.1 × 10^11`**. The `p^3` term alone
would need only `p > 32768 · 130 ≈ 4.3 × 10^6`, so **if** the exponent could be pushed to 3 the
threshold would fall by about five orders of magnitude — which is what makes Open Problem 11.1 worth
caring about, and what §4 says cannot currently be delivered.

## 7. Small-`p` behaviour

`N_0^clean(p,5) = 0` for all 17 primes to 73, in both residue classes. Against a threshold of
`2×10^11` this is uninformative, exactly as §9 of the paper says. The earlier observation that every
small-`p` all-QR solution lies on a deep diagonal (coincidence patterns `(4,1)`, `(3,2)`, `(3,1,1)` at
`p = 23, 47, 73`) appears in **none of the three papers**; it is classified as a **new computational
observation**, plausibly a finite-`p` phenomenon, and deliberately not promoted to a conjecture. Its
only interpretive weight is to show why the implied constant is large: on a deep diagonal the 15
conditions collapse to two or three, so the degenerate strata are far denser than the generic locus
and dominate at accessible `p`.

## 8. What an improvement would need

Precisely one of:

1. **Aggregate even-`|S|` cancellation** — a proof that `Σ_{|S| even}T_S` is smaller than the sum of
   the individual bounds. This is the paper's Open Problem 11.3 and the only route that could reach
   `O(p^3)`.
2. **A vanishing theorem for Kummer systems on the resonance-arrangement complement**, applicable
   subset by subset — which must handle the subsets whose product omits a variable (§4.2), where it
   cannot hold in the naive form. `STV1995` is the right framework in which to state the hypotheses;
   `Kuhne2023` supplies the arrangement's combinatorics.

Neither is available off the shelf, and §4.1 caps whatever they could give at `O(p^{5/2})`.
