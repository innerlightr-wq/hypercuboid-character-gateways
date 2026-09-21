# Incidence Structure Lemma — the prime-incidence statistic `m_q` and its realizable spectrum

**Status: elementary, proved, and verified exhaustively. Novelty NOT established — see §6.**

This note records a structure lemma for the mod-`q` incidence statistic of the
complement-reduced hypercuboid arrangement, together with the exact spectrum of
values that statistic can take. It is self-contained and independent of the
K3/modularity machinery: it uses only the definition of the forms in
`scripts/core.py` and elementary counting.

Its practical content is that a question which looks like finite geometry — *which
intersection strata of the `15`-form arrangement are realizable?* — collapses to a
one-line identity plus a small subset-sum table.

---

## 1. Setup

Exactly the setup of `scripts/core.py` and Appendix C.1–C.2 of the manuscript. Fix
`n >= 2`, put `d = n - 1`, and eliminate the zero-sector constraint by
`A_n = -(A_1 + ... + A_{n-1})`. The `2^{n-1} - 1 = 2^d - 1` representative forms are

```
L_J(x) = sum_{j in J} x_j ,    nonempty J subseteq [d] = {1, ..., d},   x in F_q^d.
```

For `q` an odd prime and `x in F_q^d` define the **prime-incidence statistic**

```
m_q(x) = #{ nonempty J subseteq [d] : L_J(x) = 0 in F_q }.
```

For the spectrum computations of §3 we restrict to `x != 0`. (In the integral
setting this is automatic: if `x in Z^d` is primitive then `x mod q != 0` for
every prime `q`.) The lemma of §2 does **not** need that restriction — see
Remark 2.1.

Two derived quantities:

```
Z = { j in [d] : x_j = 0 },                z = |Z|          (0 <= z <= d-1 when x != 0)
S'= { J subseteq [d] \ Z : L_J(x) = 0 },   s = |S'| >= 1
```

Note `S'` **includes** the empty set, so `s >= 1` always; `S'` is computed using
only the nonzero coordinates of `x`.

---

## 2. The lemma

> **Lemma (incidence structure).** For every odd prime `q` and every nonzero
> `x in F_q^d`,
>
> ```
> m_q(x) = 2^z * s - 1 .
> ```

*Proof.* The zero coordinates contribute nothing to any form: for any
`J subseteq [d]`, `L_J(x) = L_{J \ Z}(x)`, because each `j in J n Z` adds `x_j = 0`.
The map `J |-> (J \ Z, J n Z)` is a bijection
`2^{[d]} -> 2^{[d] \ Z} x 2^{Z}`, and under it `L_J(x) = 0` holds if and only if
`J \ Z in S'`, with the second component unconstrained. Hence

```
#{ J subseteq [d] : L_J(x) = 0 } = |S'| * 2^{|Z|} = 2^z * s .
```

The empty set always satisfies `L_empty(x) = 0` and is excluded from `m_q`, so
subtracting `1` gives the claim. ∎

The lemma says the vanishing set factors as a product, `S = S' x 2^Z`. The
geometric reading: the stratum through `x` is a cone over the stratum determined
by the nonzero coordinates, with the zero coordinates contributing a free Boolean
factor. **`(z, s)` is therefore the natural state vector** for incidence questions
— it is forced by the lemma rather than chosen.

### Remark 2.1 — what the proof actually uses

The proof is a bijection between subsets, not a field computation: it uses no
property of `F_q` beyond addition and the identity element. The identity therefore
holds verbatim with `F_q` replaced by **any abelian group** `A`, for every
`x in A^d`, with no hypothesis at all:

* **primality is not used** — it holds over `Z/n` for composite `n`;
* **odd characteristic is not used** — it holds in characteristic `2`;
* **commutative-ring or field structure is not used** — only the additive group
  matters, so non-cyclic `A` such as `(Z/2)^2` is fine;
* **`x != 0` is not used** — at `x = 0` one has `z = d`, `[d] \ Z = empty`,
  `S' = {empty}` and `s = 1`, so the formula returns `2^d - 1`, which is exactly
  the number of nonempty `J`, all of which do vanish.

The hypotheses "`q` an odd prime" and "`x != 0`" are retained in the statement
above **only to match the surrounding hypercuboid setting**, where `q` is the
modulus of the Legendre symbol and `x` is the reduction of a primitive integer
vector. Nothing downstream in this repository uses the more general form, and no
novelty attaches to it; it is recorded so that the hypotheses are not mistaken
for load-bearing ones.

The contrast with §3 is the point worth keeping: the *factorization* is
characteristic-free, but the *spectrum* is not. `T_k(q)` is a genuine statement
about the field, and the `q = 3` row of the table below shows that dependence is
real.

---

## 3. The realizable spectrum

Define, for `k >= 1`,

```
T_k(q) = { |S'| : S' computed from some k-tuple of NONZERO values in F_q^* }.
```

`T_k(q)` is invariant under scaling and permutation of the tuple, so it is cheap
to tabulate (fix the first value to `1`).

> **Corollary.** The realizable values of `m_q` on `F_q^d \ {0}` are exactly
>
> ```
> S_d(q) = { 2^z * s - 1  :  0 <= z <= d-1,  s in T_{d-z}(q) } .
> ```

Tabulated values (exact, by enumeration):

| `k` | `q = 3` | `q = 5` | `q = 7` | `q = 11` | `q = 13` |
|---|---|---|---|---|---|
| 1 | `{1}` | `{1}` | `{1}` | `{1}` | `{1}` |
| 2 | `{1,2}` | `{1,2}` | `{1,2}` | `{1,2}` | `{1,2}` |
| 3 | `{2,3}` | `{1,2,3}` | `{1,2,3}` | `{1,2,3}` | `{1,2,3}` |
| 4 | `{5,6}` | `{1,2,3,4,6}` | `{1,2,3,4,6}` | `{1,2,3,4,6}` | `{1,2,3,4,6}` |
| 5 | `{10,11}` | `{2,5,6,7,8,10}` | `{1,...,8,10}` | `{1,...,8,10}` | `{1,...,8,10}` |
| 6 | `{21,22}` | `{7,10,12,13,14,15,20}` | `{1,2,5,...,12,14,15,20}` | `{1,...,12,14,15,20}` | `{1,...,12,14,15,20}` |

`T_k(q)` stabilizes in `q`, but **not** at `q > k`: `T_6(7)` is missing `3` and `4`,
while `T_6(q)` agrees for `q = 11, 13, 17`. The onset must be read off the table,
not assumed. Small `q` is genuinely different (the `q = 3` column).

Resulting spectra. The `q` threshold in each row is the **observed** onset of
stabilization over the primes checked, not a proved bound:

| `n` | `d` | forms | `S_d(q)`, for `q >=` | spectrum | absent from `[0, 2^d-2]` |
|---|---|---|---|---|---|
| 4 | 3 | 7 | `5` | `{0,1,2,3}` | `4,5,6` |
| 5 | 4 | **15** | `5` | **`{0,1,2,3,5,7}`** | **`4,6`** and `8..14` |
| 6 | 5 | 31 | `7` | `{0,...,7,9,11,15}` | `8,10,12,13,14,16..30` |
| 7 | 6 | 63 | `11` | `{0,...,11,13,14,15,19,23,31}` | `12,16,17,18,20,21,22,24..30,32..62` |

Below the stated threshold the spectrum differs: e.g. `d = 6` at `q = 7` omits
`m = 2`, and `d = 5` at `q = 5` omits `m = 0` and `2`.

### Why `4` and `6` are absent at `n = 5`

This is the case of direct interest to the paper (`d = 4`, the 15 forms). Running
the corollary:

```
z=0, k=4 : s in {1,2,3,4,6}  ->  m+1 in {1,2,3,4,6}
z=1, k=3 : s in {1,2,3}      ->  m+1 in {2,4,6}
z=2, k=2 : s in {1,2}        ->  m+1 in {4,8}
z=3, k=1 : s in {1}          ->  m+1 in {8}
```

so `m + 1 in {1,2,3,4,6,8}` and `m in {0,1,2,3,5,7}`. The absent values `m = 4, 6`
correspond to `m + 1 = 5, 7`. These are **odd and greater than 3**, so they would
force `z = 0` and `s in {5,7}`, and `T_4(q) = {1,2,3,4,6}` contains neither.

That is the whole explanation. No finite-geometry input is required.

This holds for every `q >= 5`, verified directly to `q = 47`. At `q = 3` the
spectrum is `{3,4,5,7}` instead, so `m = 4` **does** occur: the hypothesis on `q`
is necessary, not cosmetic.

---

## 4. Verification

Two independent checks, both exhaustive within their stated range:

1. **The lemma.** Brute-force `m_q(x)` against `2^z * s - 1` on **every** nonzero
   `x in F_q^d`, for `q in {3,5,7,11,13}` and `d in {2,3,4,5}` subject to
   `q^d <= 4 * 10^5` — **603,204 points, all pass**.
2. **The spectrum.** The `d = 4` spectrum was also obtained independently by
   direct enumeration of `m_q(x)` over all nonzero `x in F_q^4` for
   `q = 3,5,7,...,47`, giving `{0,1,2,3,5,7}` for every `q >= 5` and `{3,4,5,7}`
   for `q = 3`, in agreement with the corollary. The same enumeration gives the
   multiplicities: per `PG(3,q)` there are exactly `10` points with `m = 7` and
   exactly `15` with `m = 5`, uniformly in `q`.

These are finite computations, not proofs of the general-`n` pattern; the lemma
itself (§2) is proved for all `n` and all odd `q`.

---

## 5. Relation to existing material in this repository

* `docs/CONSTRAINT_TABLE.md` records that the 15 representatives are the nonzero
  elements of `F_2^5 / <(1,1,1,1,1)>`, i.e. the 15 points of `PG(3,2)`, equivalently
  the coordinates of the `[15,4]` binary simplex code; and that for `n = 4` the
  same construction gives the Fano plane `PG(2,2)`.
* `docs/NOVELTY_AND_PROVENANCE.md` identifies the 15-form arrangement as the
  **resonance arrangement `R_4`** (`Kuhne2023`).

The lemma is compatible with both readings and supersedes neither. It is worth
recording because it replaces the indirect route — *"`m_q` is a hyperplane-section
size of the `PG(3,2)` configuration inside `PG(3,q)`, hence a size of a rank-`<= d-1`
flat of the matroid"* — with a direct formula that is elementary, uniform in `n`,
and immediately computable. The two descriptions agree wherever both have been
checked.

**This note makes no claim about the character sums.** `m_q` records only *which*
forms vanish mod `q`; it says nothing about `chi` values, and nothing here bears on
`Sigma_I`, `Sigma_II`, `Sigma_III` or the Gateway relation.

---

## 6. Novelty — not established

The lemma is elementary, and the objects it describes are standard: the vanishing
sets are the flats of the arrangement's matroid, and `T_k(q)` is a zero-sum
subset-counting statistic. The resonance-arrangement literature (`Kuhne2023` and
its antecedents) computes the combinatorics of `R_n` in detail, and it is entirely
plausible that the flat-size spectrum, or an equivalent of `T_k(q)`, already
appears there or in the coding-theory literature on the simplex code.

**No literature search was performed for this note.** Nothing here should be
described as new until that check is done. It is recorded as a convenience result
with a complete proof and an exhaustive verification, not as a contribution.

---

## 7. Provenance

Derived and verified September 2026 during an exploratory audit that was otherwise
negative (the audit's own hypothesis was falsified; this lemma is the part worth
keeping).

Reproduce with

```bash
python3 scripts/incidence_lemma_check.py
```

which re-runs every claim in §3 and §4 from the definitions in §1: the lemma by
exhaustive brute force, the `T_k(q)` tables, the spectra **cross-checked against
direct enumeration of `m_q`**, and the stabilization caveat. Exit status `0` on
success. No script output is a logically necessary step in the proof of §2.
