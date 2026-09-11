# Hypercuboid exploration — Round 13 working notes

## Part I — freeze/audit (PROVED, reconfirmed)

Recomputed `S(p)`, `a_p(E)`, and `-\chi(2)p+\chi(-1)a_p(E)^2` at a sanity
set of primes; all match Round 11/12 exactly (no discrepancy — proceeded
to modular-form work).

## Part II — the weight-3 CM form (LITERATURE/DB FACT, verified twice, one correction caught)

Queried the LMFDB directly (`ModularForm/GL2/Q/holomorphic`, weight 3,
`cm_discs=-8`). **Exactly one** such newform exists:
- **Label `8.3.d.a`**, level `8`, weight `3`, nebentypus `8.d` (order 2,
  real, minimal), **CM field `\mathbb Q(\sqrt{-2})`**, dimension 1
  (rational coefficients), self-dual, `is_cm=true`, `cm_discs=[-8]`.
- `q`-expansion begins `q-2q^2-2q^3+4q^4+4q^6-8q^8-5q^9+14q^{11}-8q^{12}+16q^{16}+\cdots`

**A methodological finding worth recording explicitly**: an initial
`WebFetch`-summarized read of the LMFDB page (which passes page content
through a small auxiliary model) returned a coefficient table that was
**correct for small primes but silently wrong (sign-flipped) for
`p=59,67,83,89,97`**. This was caught by comparison against a formula
derived independently (Part III) and then **confirmed as an extraction
error, not a mathematical discrepancy**, by re-fetching the raw JSON
directly via LMFDB's API (`api/mf_newforms/?level=8&weight=3`, exact
`traces` array, no AI summarization in the loop) — the raw data matches
the independently-derived formula perfectly at every one of those primes.
**Lesson applied per this project's own discipline: verify tool-summarized
external content against a second, more direct source before trusting it,
especially for exact numerical claims.** All results below use the raw
API `traces` array, not the earlier summarized table.

## Part III — the symmetric-square decomposition (PROVED, classical mechanism, correctly applied)

For `E` (Frobenius eigenvalues `\alpha_p,\beta_p`, `\alpha_p+\beta_p=a_p(E)`,
`\alpha_p\beta_p=p`), `\mathrm{Sym}^2(\rho_E)` is reducible (classical, since
`E` has CM by `K=\mathbb Q(\sqrt{-2})`):
$$\mathrm{Sym}^2(\rho_E) \cong \rho_f \oplus \big(\chi_K\cdot\mathrm{cyc}\big),$$
where `\rho_f` is the 2-dimensional representation of our newform `f`
and `\chi_K` is `K`'s quadratic character (`=\chi(-2)` in our notation).
Trace bookkeeping (`\mathrm{tr}\,\mathrm{Sym}^2=\alpha^2+\alpha\beta+\beta^2=a_p(E)^2-p`
using `\alpha\beta=p`) gives, **exactly**:
$$a_p(f) = a_p(E)^2 - p\big(1+\chi(-2)\big).$$
**Verified against the RAW LMFDB trace data at every prime `3\le p<150`
tested (34 primes): zero exceptions.** (At inert primes, `\chi(-2)=-1`
and `a_p(E)=0`, giving `a_p(f)=0` automatically — matching the elementary
fact that CM-form coefficients vanish at inert primes, an independent
consistency check.) **PROVED** (standard representation-theoretic fact,
correctly instantiated and independently numerically confirmed).

## Part IV — database coefficient comparison → the master identity, simplified

Substituting Part III's relation into Round 11/12's master identity
`S(p)=-\chi(2)p+\chi(-1)a_p(E)^2` and simplifying purely algebraically
(`\chi(-1)\chi(-2)=\chi(2)` used once) collapses it to:
$$\boxed{S(p) = \chi(-1)\big(a_p(f)+p\big)}$$
**Full comparison table** (raw LMFDB `a_p(f)` vs. directly-computed
`S(p)`, all `3\le p<150`, `scripts/round13_modular.py`):

| p | p mod 8 | a_p(f) [LMFDB] | S(p) | χ(-1)(a_p(f)+p) | match |
|---|---|---|---|---|---|
| 3,5,7,...,149 (34 primes) | all four classes | (raw) | (direct) | (formula) | **True, every row** |

**Zero exceptions across all 34 primes tested, using externally-sourced,
independently-verified modular-form data — this is now a stronger
evidentiary status than "internally computationally verified": the
identity connects our object to a value tabulated by an independent
database with its own, unrelated derivation (classical Hecke theory),
not something we produced.**

## Part V — is this a known/classified K3? (PARTIAL — general theorem found, exact surface not pinpointed)

Located the relevant general theorem (Livné; see also Schütt's papers,
e.g. *Arithmetic of a singular K3 surface*, and the classification paper
on *CM newforms with rational coefficients*): **for a singular
(`\rho=20`) K3 surface `X/\mathbb Q` with transcendental lattice of
discriminant `d`, the `L`-series of the transcendental lattice is the
Mellin transform of a weight-3 Hecke eigenform with CM by
`\mathbb Q(\sqrt d)`; conversely (Schütt) imaginary quadratic fields of
class-group exponent `\le2` correspond bijectively to rational weight-3
CM newforms up to twist.** This is **exactly** the mechanism our data is
consistent with. **However**: a specific search for a paper describing
*this exact surface* (fiber configuration `I_2^*,I_2,I_0^*,I_2^*`,
Legendre-twist construction) did **not** turn up a match — one candidate
Schütt paper found (`math/0605560`) treats a **different** fiber
configuration (`[1,1,1,12,3^*]`, i.e. two `I_1`'s, an `I_{12}`, and an
`I_3^*}` — not ours) and was **ruled out** by direct comparison, not
assumed. **Classification: the general mechanism is LITERATURE-PROVED;
the specific surface's presence in the literature is NOT CONFIRMED**
(searched, not found, in the time available — absence is not proof of
absence, but no match was located).

## Part VI — resolving ρ: still not settled, but the evidence is now much stronger

`\rho=20` is required for Livné's theorem to apply directly (transcendental
rank exactly 2, matching `f`'s 2-dimensional representation). **Not
proved this round** — no non-torsion section was found (Round 12 already
excluded degree `\le2`; this round did not extend the search). **However,
the indirect evidence is now much stronger than a coincidence-tolerant
reading would allow**: the identity `S(p)=\chi(-1)(a_p(f)+p)` accounts
for **100% of `S(p)`'s value at every tested prime with zero residual**.
If `\rho` were `19` (transcendental rank 3), a generic third eigenvalue
direction would be expected to contribute an *additional*, independent
fluctuating term not captured by the 2-dimensional `f` alone — for that
extra contribution to vanish identically at all 34 tested primes without
being forced to by any argument found here would be a very specific
coincidence. **This is offered as strong circumstantial evidence for
`\rho=20`, explicitly labeled CONJECTURAL — not a proof.**

## Part VII — exact H² Frobenius decomposition (algebra done, geometric identification of terms NOT done)

If `\mathrm{Tr}(\mathrm{Frob}_p\mid H^2(X)) = \mathrm{Tr}_{NS}(p) + a_p(f)`
(the standard shape for a singular K3 with this transcendental type), then
matching against `S(p)=\chi(-1)(a_p(f)+p)` (Part IV) requires, after
full affine/projective bookkeeping (Part VIII — **not completed**),
`\mathrm{Tr}_{NS}(p)` to resolve to something with the shape
`[\chi(-1)-1]p` (zero at `p\equiv1(4)`, `-2p` at `p\equiv3(4)`) **for the
pieces of the algebraic bookkeeping matching this to work out cleanly** —
this is an **algebraically consistent target**, not a derived result: it
would correspond to roughly 2 of the 20 Néron–Severi divisor classes
being defined only over `\mathbb Q(i)$ (flipping sign under Frobenius
exactly when `\chi(-1)=-1`) while the rest are defined over `\mathbb Q`.
**No specific divisor classes were identified to confirm this** — flagged
honestly as the exact shape a full derivation would need to produce, not
something shown to hold.

## Part VIII — affine/projective bookkeeping: **NOT COMPLETED (same gap as Round 12)**

No progress beyond Round 12's honest accounting of what remains
(resolving `I_2^*`/`I_0^*` fibers, handling boundary/points-at-infinity,
accounting for the 2-torsion sections) — this remains the single
largest concrete piece of unfinished work blocking a full geometric
proof, and Round 13 did not attempt it (effort was spent on identifying
`f` and verifying Part III/IV instead, which was judged higher-value
given it was previously entirely open).

## Part IX — deriving the master identity: **achieved algebraically, contingent on the (unproved) geometric correspondence**

The chain **Part III (proved) + Part IV (verified against external data)**
gives a full, clean, *algebraic* derivation of
`S(p)=-\chi(2)p+\chi(-1)a_p(E)^2` **from** `S(p)=\chi(-1)(a_p(f)+p)` (or
vice versa — they are algebraically equivalent, shown by direct
substitution, not merely observed to agree numerically). **What is not
derived**: *why* `S(p)` (built purely from the character sum / affine
surface count) equals `\chi(-1)(a_p(f)+p)` in the first place — that
remains the single unproved link, now stated in its cleanest possible
form. **One unknown term, explicitly identified (not hidden under "up to
a correction")**: the precise geometric mechanism producing
`\mathrm{Tr}_{NS}(p)` together with the affine/projective correction,
such that their sum plus `a_p(f)` equals `S(p)` exactly.

## Part X — inert/split formulas (derived cleanly from the new, simpler form)

**Inert** (`\chi(-2)=-1`, `p\equiv5,7\pmod8`): `a_p(E)=0` (PROVED,
classical CM/Deuring) `\Rightarrow a_p(f)=0` (Part III, consistent with
the general CM-vanishing property) `\Rightarrow S(p)=\chi(-1)\cdot p`.
Since `\chi(-1)=1` at `p\equiv5(8)` and `\chi(-1)=-1` at `p\equiv7(8)`,
this reproduces `S(p)=\chi(-1)p`, matching Round 9's `-\chi(2)p` exactly
(as previously verified: `\chi(-1)=-\chi(2)` when `\chi(-2)=-1`).

**Split** (`\chi(-2)=+1`, `p\equiv1,3\pmod8`, `p=A(p)^2+2B(p)^2`):
`S(p)=\chi(-1)\big(a_p(f)+p\big)` with `a_p(f)=4A(p)^2-2p` (Part III with
`a_p(E)=\pm2A(p)`), giving the fully explicit closed form
$$S(p) = \chi(-1)\big(4A(p)^2 - p\big).$$

## Part XI — literature-equivalence audit

The **general mechanism** (Livné/Schütt) is a **known literature
theorem**, cited and correctly applied. The **specific identity**
`S(p)=\chi(-1)(a_p(f)+p)` for **this specific double character sum** is
**not found anywhere in the literature searched** — it is a genuine
reformulation/discovery of this exploration, built from a known general
framework. **Classification: KNOWN FRAMEWORK, NEW SPECIFIC INSTANCE
(not independently verified as already published).**

## Part XII — falsification (survived everything, including the caught error)

- All 34 primes `3\le p<150`, all four mod-8 classes: zero mismatches
  (raw LMFDB data).
- `p=3` (the project's recurring edge case): matches exactly.
- The one apparent "falsification" encountered this round (`p=59,67,83,
  89,97` mismatching an intermediate summarized table) was **correctly
  diagnosed as a data-extraction artifact, not a mathematical failure**,
  and resolved by going to the primary source — this is itself a
  successful falsification-discipline exercise (per the project's own
  standing methodology), not a weakening of the result.
- Sign convention for `a_p(E)`: irrelevant to the identity (only
  `a_p(E)^2` appears; independently re-confirmed).
- Bad reduction (`p=2`): correctly excluded/not claimed.

## Part XIII — what has actually been proved

**COMPUTATIONALLY VERIFIED ONLY — but with meaningfully stronger evidence
than before**, because the verification is now against an independently
tabulated, externally-sourced classical object (an LMFDB newform), not
just internal self-consistency. None of PROVED VIA MODULAR K3
IDENTIFICATION, PROVED VIA KNOWN LITERATURE THEOREM, or PROVED MODULO ONE
EXPLICIT GEOMETRIC IDENTIFICATION is fully earned: the one remaining gap
(`\rho=20` plus the full affine/projective/NS bookkeeping of Part
VII–VIII) was narrowed and precisely stated, but not closed. **Do not
use "essentially proved."**

## Part XIV — the structural-regime picture, reassessed once more

Round 13 supports a further-sharpened version of the Round 12 statement:
**the residual structure is not just "rigid enough to be represented by
a global arithmetic object with its own Frobenius law" — it is rigid
enough to be represented by an object *already cataloged in an existing
mathematical database*, discoverable by name and cross-checkable against
independently-computed data, rather than needing to be constructed from
scratch.** This is a meaningfully different (and stronger) kind of
"rigidity" than Round 11's classification (K3, Euler number 24) or Round
12's algebra (the eigenvalue rewriting) provided on their own — it says
the exploration's residual invariant is not merely *describable* by
arithmetic geometry, but is *identical to* a specific, previously-studied
classical object, up to a clean, verified linear formula.

## Everything killed or corrected this round

1. **CORRECTED (methodological)**: an AI-summarized web-fetch's
   coefficient table was wrong at 5 of the ~25 primes it reported deeper
   in its list; caught via cross-derivation and fixed via the raw API —
   explicitly logged so future rounds do not re-trust unverified
   large-table extractions from summarized fetches.
2. **NOT killed**: the master identity — simplified, re-verified, and now
   backed by external data.
3. **RULED OUT** (not just "not found"): the specific Schütt paper
   `math/0605560` as a description of our surface — its stated fiber
   configuration (`[1,1,1,12,3^*]`) is directly incompatible with ours
   (`I_2^*,I_2,I_0^*,I_2^*`), checked explicitly rather than assumed.

## Highest-value next question

**Prove `\rho=20`.** Given the extremely clean, database-confirmed
identity now in hand (`S(p)=\chi(-1)(a_p(f)+p)`, zero residual at every
tested prime), the entire remaining gap is squarely the Mordell–Weil /
Picard-number question already flagged in Round 12 — extend the section
search to degree 3–4, or find an independent argument (e.g., via the
Shioda–Inose/Kummer construction, or by locating this exact surface in
Schütt's classification tables by its transcendental discriminant rather
than its fiber configuration). Resolving this single question would
convert Round 13's "computationally verified, mechanism fully identified"
status into a genuine proof.
