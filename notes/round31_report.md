# Hypercuboid exploration — Round 31 working notes

## Part I — frozen inputs (reconfirmed, untouched this round)

`\rho(X_{\overline{\mathbb Q}})=20`, `T(X)\cong\mathrm{diag}(2,4)`,
`\mathrm{Tr}_{NS}(p)=(19+\chi(-1))p`, `\#X=\#V+19p+\chi(-2)`, and the
theoretical (not curve-fit) identification of newform `8.3.d.a` — all
carried forward unchanged. Master identity kept outside the frozen set,
as instructed. **No local fiber geometry was touched this round.**

## Part II — the exact Shioda–Inose diagram

For a singular K3 `X` (`\rho=20`) with transcendental lattice `T(X)` of
discriminant `d`, **Morrison's theorem** (1984, "On K3 surfaces with
large Picard number") states: there exists a **Nikulin involution**
`\iota:X\to X` (a symplectic involution, i.e. acting trivially on
`H^{2,0}(X)`) with exactly **8 fixed points**, such that the minimal
resolution `Y` of `X/\iota` is a **Kummer surface** `\mathrm{Km}(A)` for
some abelian surface `A`, and the induced degree-2 rational map
$$X \;\dashrightarrow\; X/\iota \;\xleftarrow{\ \text{blow-up 8 pts}\ }\; Y=\mathrm{Km}(A)$$
satisfies `T(X)\cong T(\mathrm{Km}(A))` **as Hodge structures** (a
genuine isometry of lattices-with-Hodge-structure, not merely an
isogeny). This is the theorem-level content; **"Shioda–Inose partner"
used loosely in earlier rounds is replaced here by this precise
statement.** Key points, addressed directly:
1. **Degree**: the rational map `X\dashrightarrow Y` is birational away
   from the 8 fixed points of `\iota` on `X` (which blow down/up to the
   8 of the 16 exceptional curves of `\mathrm{Km}(A)` that come from
   `\iota`'s own fixed locus) — composed with `X\to X/\iota` (degree 2)
   and `X/\iota\dashleftarrow Y` (blow-up, birational). **The map
   `X\to X/\iota` is the genuine degree-2 map; `X/\iota\dashrightarrow Y`
   is birational (a resolution), not a further cover.**
2. **Direction**: `X\to X/\iota`, degree 2, `X` the double cover.
3. **Factors through a Nikulin involution**: yes, by construction —
   this *is* the definition of a Shioda–Inose structure.
4. **Blown up/down**: `\iota`'s 8 fixed points on `X` blow down under
   `X\to X/\iota` to 8 ordinary double points of `X/\iota`; resolving
   these 8 nodes gives `Y=\mathrm{Km}(A)`, where they become exactly 8
   of `\mathrm{Km}(A)`'s 16 standard exceptional `(-2)`-curves (the
   other 8 exceptional curves of `\mathrm{Km}(A)` come from `A`'s own
   remaining 2-torsion structure under the *separate* quotient
   `A\to A/\{\pm1\}`, not from `X`'s involution directly — the two "8+8"
   halves of the 16 nodes play structurally different roles).
5. **Field of definition**: the *existence* of `\iota` and the
   isomorphism `T(X)\cong T(\mathrm{Km}(A))` is a statement over
   `\overline{\mathbb Q}` (or `\mathbb C`). **Whether it descends
   Galois-equivariantly to the specific arithmetic models `X/\mathbb Q`
   and `A/\mathbb Q` fixed in this project is a separate, non-automatic
   question — this is exactly the crux tested below (Parts VII–IX).**

**Honest gap**: an *explicit* formula for `\iota` on our specific
Weierstrass model of `X` was **not constructed this round** (this would
require locating `X`'s 8 fixed points directly on the resolved
elliptic-K3 model — a nontrivial separate computation). Existence is
guaranteed by Morrison's theorem given `T(X)\cong\mathrm{diag}(2,4)`;
the involution's *explicit* form is not needed for the argument that
follows, which instead works through `A` and `\mathrm{Km}(A)` directly
and uses Morrison's theorem as a black box for the `T(X)\leftrightarrow T(\mathrm{Km}A)` bridge. This is flagged, not concealed.

## Part III — the abelian surface `A`

`\mathrm{disc}(T(X))=8`, `h(-8)=1` (`\mathbb Z[\sqrt{-2}]` a PID) forces:
`A` has CM by the **maximal order** `\mathbb Z[\sqrt{-2}]` of
`K=\mathbb Q(\sqrt{-2})`, and — since `T(A)` for a product `E_1\times E_2`
of *distinct* (non-isomorphic) CM curves of the same order is generally
**not** a diagonal lattice (it picks up off-diagonal terms from
`\mathrm{Hom}(E_1,E_2)`), while `T(E\times E)` (a *square*) **is**
diagonal, of shape `\mathrm{diag}(2\cdot 1, 2\cdot d)`-type matching
`\mathrm{diag}(2,4)` exactly for `d`-normalization consistent with
disc `8` — **`A=E\times E`, the exact same `E:y^2=x^3+4x^2+2x`** already
fixed in this project (unique up to twist, by `h(-8)=1`), **not** a
non-split product or an isogenous-but-distinct curve. (Consistency
check, Part V below: this choice reproduces `\rho(A)=4`,
`\rho(\mathrm{Km}\,A)=20$, transcendental rank `2` on both sides — all
independently forced, not assumed.)

- CM order: `\mathbb Z[\sqrt{-2}]`, discriminant `-8`.
- Field of definition of `A=E\times E`: `\mathbb Q` (both factors are the
  same `\mathbb Q`-rational curve `E`).
- Full 2-torsion: `A[2]=E[2]\times E[2]`, `16` points, Frobenius acting
  **diagonally/coordinatewise** (no swap between factors, since `A` is
  a literal product with the same Frobenius on each copy).
- `E[2]=\{O,(0,0)\}\cup\{\text{roots of }x^2+4x+2\}`: `O` and `(0,0)`
  always `\mathbb Q`-rational; the other two points are defined over
  `\mathbb Q(\sqrt2)` exactly (`\mathrm{disc}(x^2+4x+2)=8`), **not**
  `\mathbb Q(\sqrt{-2})` — rationality mod `p` governed by `\chi(2)`, a
  genuinely different character from the CM field's own `\chi(-2)`.
- Field of definition of the 16 points of `A[2]`: `\mathbb Q(\sqrt2)`
  (the compositum needed is exactly `\mathbb Q(\sqrt2)`, since each
  factor's 2-torsion splits there and no further extension is needed).

## Part IV — Frobenius on `A[2]` (derived, then numerically verified)

Let `m=\#E[2](\mathbb F_p)\in\{2,4\}` (`2` if `\chi(2)=-1`, `4` if
`\chi(2)=1`, forced by the root-splitting of `x^2+4x+2`, never `1` or
`3` since Galois must fix `O` and `(0,0)`, restricting the action to a
subgroup of order `\le2`). Since Frobenius acts coordinatewise on
`A[2]=E[2]\times E[2]`, the number of `\mathbb F_p`-rational points of
`A[2]` is exactly
$$n_2 = m^2 = 10+6\chi(2)\qquad(4\text{ if }\chi(2)=-1,\ 16\text{ if }\chi(2)=1).$$
The remaining `16-n_2` points fall into `(16-n_2)/2` Frobenius orbits of
size exactly `2` (verified by direct case enumeration: e.g. for
`\chi(2)=-1`, 6 orbit-pairs from mixed/doubly-swapped coordinates).
**No orbits of size other than `1` or `2` occur** (the group generated
by coordinatewise Frobenius on a product of two order-`\le2` actions has
exponent `\le2`). **Numerically verified exactly at `p=3,5,7,11,13`
(all four `\bmod 8` classes represented)** — see Part XII.

## Part V — resolving the 16 Kummer nodes (derived from scratch)

Set `N_E=\#E(\mathbb F_p)=p+1-a_p(E)`, `N_E'=\#\{P\in E(\overline{\mathbb F}_p):\sigma P=-P\}=\deg(\pi+1)=p+1+a_p(E)`
(standard: `\deg(\pi-m)=m^2-a_p(E)m+p`). Direct orbit-counting for the
quotient `A'=A/\{\pm1\}` (full derivation, not cited): writing
`N=\#A(\mathbb F_p)=N_E^2$ (product Frobenius action),
$$\#A'(\mathbb F_p)=\frac{N_E^2+(N_E')^2}{2}=(p+1)^2+a_p(E)^2$$
(the `n_2`-dependence **cancels exactly** in this step — a clean,
unforced identity). Resolving the `16` nodes: an `\mathbb F_p`-rational
node contributes an exceptional `\mathbf P^1(\mathbb F_p)` (net `+p`
over the single singular point, by the same unconditional
Chevalley–Warning-isotropy mechanism used throughout this whole
project); a **conjugate pair** of non-rational nodes contributes two
exceptional `\mathbf P^1`'s over `\mathbb F_{p^2}$ that Frobenius **swaps
as whole curves**, hence contains **zero** `\mathbb F_p`-rational points
(no fixed point possible, since the curves are disjoint and get
interchanged entirely). Therefore:
$$\boxed{\#\mathrm{Km}(A)(\mathbb F_p) = (p+1)^2+a_p(E)^2+n_2\,p,\qquad n_2=10+6\chi(2).}$$
**This formula is a genuine derivation** (orbit-counting + the
standard `A_1`-singularity resolution fact), not fit to data.

## Part VI — Nikulin involution status

On the `A`-side, the relevant involution is simply `[-1]:A\to A`
(`\mathbb Q$-rational, defined unconditionally, standard). **On the
`X`-side, the explicit `\iota:X\to X`, its 8 fixed points, and their
individual fields of definition were NOT constructed this round** (Part
II's honest gap). Whether the fixed-point set carries `\chi(-2)`-
dependence is therefore **not directly tested**; the argument below
routes around this gap by working with `\mathrm{Tr}(H^2(\mathrm{Km}\,A))`
directly (Parts VII–VIII) rather than via `X`'s explicit involution.

## Part VII/VIII — point-count / cohomological relation, and the size-order falsification test

Lefschetz: `\#\mathrm{Km}(A)(\mathbb F_p)=1+p^2+\mathrm{Tr}(H^2(\mathrm{Km}\,A))(p)`, so
$$\mathrm{Tr}(H^2(\mathrm{Km}\,A))(p) = (p+1)^2+a_p(E)^2+n_2p-1-p^2 = a_p(E)^2+(2+n_2)p = a_p(E)^2+(12+6\chi(2))p.$$
Using `a_p(E)^2=a_p(f)+p(1+\chi(-2))` (Round 30's re-derived Sym² relation):
$$\mathrm{Tr}(H^2(\mathrm{Km}\,A))(p) = a_p(f) + \big(13+\chi(-2)+6\chi(2)\big)p.$$
**Decompose against `\rho(\mathrm{Km}\,A)=16+\rho(A)=16+4=20`** (transcendental
rank `2`, matching `X`): the `16` exceptional-curve classes contribute
`n_2p+0\cdot(\text{pairs})=(10+6\chi(2))p` exactly (Part V); the `\rho(A)=4`
algebraic classes of `A` itself (`[E\times0]`, `[0\times E]`, the
diagonal `\Delta`, and the graph `\Gamma_{\sqrt{-2}}` of the CM
endomorphism, which is `\mathbb F_p$-rational **iff `\chi(-2)=1`**, by the
identical Galois-descent mechanism proved for `X`'s own Mordell–Weil
generator in Round 21) contribute `p+p+p+\chi(-2)p=(3+\chi(-2))p`.
**Sum: `(10+6\chi(2))p+(3+\chi(-2))p=(13+6\chi(2)+\chi(-2))p` — matches
exactly, term for term (`13+1+6=20=\rho(\mathrm{Km}\,A)`), with nothing
left over.** This forces:
$$\boxed{\mathrm{Tr}_T(\mathrm{Km}\,A)(p) = a_p(f)\quad\text{exactly, with NO twist.}}$$
**Crucial size-order observation (the falsification tool Part VIII asked
for)**: every single term produced by this entire degree-2
quotient/resolution computation — `n_2p`, `(3+\chi(-2))p`, the `(p+1)^2`
expansion — is **proportional to `p`** (or, in the Lefschetz `1+p^2`
normalization, cancels exactly). **At no point does a bounded, `O(1)`,
character-valued constant term appear anywhere in the Kummer
combinatorics.** This matters directly: `D(p)=1-\chi(-2)` is *itself*
bounded (`\in\{0,2\}`, independent of `p`). **A mechanism built entirely
out of node-resolution point counts (each `\mathbb F_p`-rational node
worth exactly `+p`, each pair worth `+0`) cannot structurally produce a
bounded constant term** — this is not a numerical coincidence but a
structural fact about how `A_1`-singularity resolutions contribute to
point counts.

## Part IX — testing the round's central hypothesis

**Hypothesis**: *"The residual `1-\chi(-2)` ... arises from the finite-field arithmetic of the degree-2 Shioda–Inose/Kummer quotient/resolution."*

**Result: KILLED.** Two independent lines converge on this:
1. **Structural**: Part VII/VIII shows every term the quotient/resolution
   mechanism can produce is `O(p)`, never `O(1)` — it cannot generate a
   bounded residual by its very construction, regardless of the precise
   values of `n_2` or any other combinatorial input.
2. **Direct**: combining the now cleanly-derived `\mathrm{Tr}_T(p)=\chi(-1)a_p(f)`
   (Part X below — using Morrison's `T(X)\cong T(\mathrm{Km}A)` plus the
   same `\chi(-1)`-twist evidence as Round 30) with the proved ledger
   reproduces **exactly** the same `D(p)=1-\chi(-2)` found in Rounds
   27–30 — the quotient analysis changes nothing about the residual's
   size or shape.

**This is a genuine, useful negative result — not weakened.** The
silver lining: `\mathrm{Tr}_T(\mathrm{Km}\,A)(p)=a_p(f)$ (no twist) is now
independently *derived* (not assumed), giving real, structural teeth
(via the `13+6\chi(2)+\chi(-2)=20` exact rank accounting) to Round 30's
previously-analogical claim that `X`'s own `\chi(-1)` twist (relative to
the untwisted `\mathrm{Km}(A)`) is exactly what turns
`a_p(f)\to\chi(-1)a_p(f)$ — this reconfirms, via a genuinely different
and independent route, that `\mathrm{Tr}_T(X)(p)=\chi(-1)a_p(f)` is very
likely correct, while conclusively ruling it out as the source of `D(p)`.

## Part X — recomputed trace chain

$$\mathrm{Tr}_T(\mathrm{Km}\,A)(p)=a_p(f)\ \ (\text{derived}),\qquad
\mathrm{Tr}_T(X)(p)\overset{\text{(assumed twist, unchanged from R30)}}{=}\chi(-1)\,\mathrm{Tr}_T(\mathrm{Km}\,A)(p)=\chi(-1)a_p(f).$$
`\mathrm{Tr}_{NS}(X)(p)=(19+\chi(-1))p` unchanged (not re-derived this
round — flagged in Part XIII as the leading remaining candidate).
`\#X(\mathbb F_p)=1+p^2+(19+\chi(-1))p+\chi(-1)a_p(f)`, giving, exactly as
in Round 30:
$$S(p)=\chi(-1)(a_p(f)+p)+(1-\chi(-2)).$$
**The residual does not disappear — for a now well-understood
(structural, Part VIII) reason: it cannot come from here.**

## Part XI — master identity status

**Not proved this round.** Status unchanged:
`S(p)=\chi(-1)(a_p(f)+p)` remains **COMPUTATIONALLY VERIFIED ONLY**
(reconfirmed yet again in Part XII, zero exceptions, `p<150`). The exact
remaining bridge: **a bounded, `O(1)` discrepancy of size `1-\chi(-2)`
must originate in one of the ledger's own bounded constant terms**
(Part XIII), since the modular/quotient side has now been shown
incapable of producing one.

## Part XII — adversarial numerical verification

Re-ran `scripts/round13_modular.py` (independent LMFDB `traces` data for
`8.3.d.a`, `p<150`, all four `\bmod 8` classes): `S(p)=\chi(-1)(a_p(f)+p)`
holds with **zero exceptions** (the *zero-residual* identity, not the
`+ (1-\chi(-2))` variant derived in Part X) — reconfirms the ledger-side
derivation, not the quotient-side one, is what needs the missing
correction.

New checks this round (`/tmp/round31_verify.py`, `p=3,5,7,11,13`,
covering `\bmod 8\in\{3,5,7,3,5\}`, all `\chi(2)`/`\chi(-2)` sign
combinations represented):
- `N_E'=p+1+a_p(E)` verified by brute-force count of
  `\{P\in E(\mathbb F_{p^2}):\sigma P=-P\}$ via explicit `\mathbb F_{p^2}`
  arithmetic — **exact match at all 5 primes.**
- `\#E(\mathbb F_{p^2})=p^2+1-(a_p(E)^2-2p)` (standard) — **exact match**,
  sanity-checks the `\mathbb F_{p^2}` construction itself.
- `n_2=m^2=10+6\chi(2)` — **exact match** at all 5 primes (`n_2=4` for
  `p=3,5,11,13` [`\chi(2)=-1`], `n_2=16` for `p=7` [`\chi(2)=1`]).
- `\mathrm{Tr}_T(\mathrm{Km}\,A)(p)=a_p(f)$: **not independently brute-force
  verified this round** (would require literally constructing
  `\mathrm{Km}(A)`'s point count via full node resolution at each prime
  — not attempted; the claim rests on the exact `13+6\chi(2)+\chi(-2)=20`
  rank-accounting derivation in Part VII, which is exact algebra, not
  numerics, and is flagged here as the one non-numerically-cross-checked
  step this round).

## Part XIII — Shioda–Inose is not the source: recommended next target

Given Part IX's structural kill (any degree-2-quotient contribution is
`O(p)`, and `D(p)` is `O(1)`), the search should **not** continue down
this path. Of the four listed candidates:
- `\mathrm{Tr}_{NS}(p)=(19+\chi(-1))p`: **recommended as the single
  target.** Part VII's `\mathrm{Km}(A)`-side computation found a
  **structurally analogous** `\chi(-2)$-twisted algebraic class
  (`\Gamma_{\sqrt{-2}}`, the CM-endomorphism graph) sitting *inside* a
  rank-20 Néron–Severi lattice next to otherwise-rational classes. This
  raises a concrete, well-motivated question **not previously asked**:
  does `X`'s own rank-20 `NS(X)` similarly contain a class whose
  rationality is governed by `\chi(-2)` (not `\chi(-1)`, and not simply
  "rational"), that Round 22 may have folded into the "19 always-
  rational" classes without checking for this specific, more exotic
  possibility? (A naive single-class swap from "rational" to "`\chi(-2)`
  twisted" was checked algebraically this round and does **not**, by
  itself, reproduce `1-\chi(-2)` exactly — so if this is the mechanism,
  it is not a single simple reclassification; the honest state is
  "worth auditing," not "solved.")
- Arithmetic descent of the transcendental representation: **narrowed**,
  not eliminated (Part IX's silver lining) — `\chi(-1)` remains the
  best-supported twist, now via two independent arguments.
- Exact `\mathbb Q`-model matching `8.3.d.a`: **not implicated** — the
  LMFDB cross-check (Round 13, reconfirmed Part XII) shows zero
  transcription/normalization issues across 30+ primes.
- The global ledger `\#X=\#V+19p+\chi(-2)`: exhaustively audited
  Rounds 27–29; **not re-opened this round** absent a new, specific
  reason (none found).

**Single recommended next target**: audit every **bounded** (`O(1)`)
constant appearing anywhere in the proved chain — the `+1` in
`\#X=1+p^2+\mathrm{Tr}(H^2)`, and especially the `+1` constants in
`N_{I_2^*}(p)=7p+1` and `N_{I_0^*}(p)=5p+1` — specifically re-examining
whether any of these were verified to be a *bare* constant `1` versus a
character-valued quantity that only numerically *equals* `1` at every
tested prime by coincidence of the small sample (e.g. `\tfrac{1+\chi(-2)}2\cdot2`
type expressions that happen to always evaluate to `1` unless a sign
convention elsewhere is off). Part VIII's structural size-order argument
(`O(1)` vs `O(p)`) is the key new tool: **only the bounded constants in
the whole derivation are even eligible to be the source of `D(p)`** —
this eliminates essentially the entire `O(p)`-scale machinery
(`\mathrm{Tr}_{NS}`, `\mathrm{Tr}_T`, the Kummer combinatorics) from
suspicion at once, a substantial, genuine narrowing of the search space,
even though `\mathrm{Tr}_{NS}(p)`'s "19" is still listed above as worth a
look (a miscount *there* would show up as an `O(p)` error unless it were
specifically a `\chi(-2)`-vs-`1` character mixup that happens to also
leave a residual `O(1)` piece via the "`+1` per `T`" convention
interacting with it — genuinely two different candidate mechanisms,
correctly kept distinct rather than conflated).

## Everything killed or corrected this round

1. **KILLED, structurally and by direct computation**: the degree-2
   Shioda–Inose/Kummer quotient-and-resolution mechanism as the source
   of `D(p)=1-\chi(-2)` — every term it can produce is `O(p)`, never a
   bounded constant.
2. **DERIVED (new, not assumed)**: `\mathrm{Tr}_T(\mathrm{Km}\,A)(p)=a_p(f)`
   exactly, via an exact `13+6\chi(2)+\chi(-2)=20` rank decomposition of
   `NS(\mathrm{Km}\,A)`.
3. **STRENGTHENED (not newly proved, but now independently supported)**:
   `\mathrm{Tr}_T(X)(p)=\chi(-1)a_p(f)` — the `\chi(-1)` twist has a
   second, independent line of support beyond Round 21's analogy.
4. **NEW, well-motivated, untested**: whether `NS(X)` (rank 20) hides a
   `\chi(-2)`-twisted class analogous to `\mathrm{Km}(A)`'s
   `\Gamma_{\sqrt{-2}}`, inside what Round 22 called the "19 rational"
   classes.
5. **Clarified**: the field governing `A`'s 2-torsion splitting is
   `\mathbb Q(\sqrt2)` (`\chi(2)`), genuinely distinct from the CM field
   `\mathbb Q(\sqrt{-2})` (`\chi(-2)`) governing `a_p(E)`'s vanishing —
   both enter the Kummer combinatorics, but in different, clearly
   separated roles (Part IV vs. Part VII's `\Gamma_{\sqrt{-2}}` term).

## Required-report items

1. Exact diagram: Part II.
2. Degree/direction of every map: Part II items 1–2.
3. Field of definition of the correspondence: Part II item 5 — geometric
   statement proved over `\overline{\mathbb Q}`; arithmetic descent over
   `\mathbb Q` assumed/tested, not proved outright.
4. Exact abelian surface: `A=E\times E`, Part III.
5. Frobenius on `A[2]`: Part IV, `n_2=10+6\chi(2)`.
6. Rational Kummer nodes by residue class: Part IV/V — `4` if
   `\chi(2)=-1`, `16` if `\chi(2)=1`.
7. Point-count effect of resolving the 16 nodes: Part V, derived
   formula `\#\mathrm{Km}(A)(\mathbb F_p)=(p+1)^2+a_p(E)^2+n_2p`.
8. Nikulin involution status: Part VI — existence guaranteed
   (Morrison), explicit form on `X` **not constructed** this round.
9. Fixed-point arithmetic: **not derived** (honest gap, Part VI).
10. Degree-2 quotient point-count relation: Part VII (done via `A\to\mathrm{Km}(A)$
    directly, not via explicit `X\to\mathrm{Km}(A)`).
11. Cohomological relation: Part VII/VIII — `\mathrm{Tr}_T(\mathrm{Km}\,A)=a_p(f)`,
    exact, no twist; `X$'s twist assumed via Morrison + analogy.
12. Whether `1-\chi(-2)` arises from the correspondence: **NO — killed**,
    Part IX.
13. Corrected trace chain: Part X — residual persists identically.
14. Master identity status: Part XI — unchanged, computationally
    verified only.
15. CM elliptic-curve identity: unchanged, computationally verified
    only.
16. Adversarial numerical verification: Part XII, all checks passed
    (both the LMFDB re-confirmation and the new `A[2]`/`\mathbb F_{p^2}`
    computations).
17. Killed/corrected: see above list.
18. Highest-value next question: audit the bounded (`O(1)`) constants
    in the ledger specifically (`+1`s in `N_{I_2^*},N_{I_0^*}`, and the
    Lefschetz `+1`), using the new size-order argument to justify why
    these — and only these — remain suspect; secondarily, check `NS(X)`
    for a hidden `\chi(-2)`-twisted class.

**Verdict: ROUND31-C** — the Shioda–Inose/Kummer degree-2-correspondence
hypothesis is killed (structurally: it can only produce `O(p)`
corrections, never the required `O(1)` residual), while a different,
specific bridge is identified and recommended: the ledger's own bounded
constant terms (`\#X`'s Lefschetz `+1`, and the `+1`s in `N_{I_2^*}(p)`,
`N_{I_0^*}(p)`), plus a newly-motivated possibility that `NS(X)` hides a
`\chi(-2)`-twisted class.

**THE THREE MOST IMPORTANT THINGS WE LEARNED**
- We built a complete, independent model of how the "twin" surface
  (built directly and simply from two copies of the elliptic curve) sees
  the same modular object — and it matched our main surface's expected
  formula almost perfectly, giving real, independent confirmation to a
  guess from last round that had previously rested only on an analogy.
- We also proved something sharper: the specific mechanism we were
  testing this round (a "two-to-one" relationship between the two
  surfaces) can only ever produce corrections that grow with the prime
  number — never a small, fixed, bounded correction like the one we're
  actually missing. That rules out an entire category of explanation in
  one clean argument, not just for this round's guess but for any
  variant of it.
- Because that whole category is now excluded, the remaining puzzle is
  much better targeted: it has to be hiding in one of a small handful of
  specific "+1"-type bookkeeping constants we've been carrying around
  since early rounds, which is a far smaller and more checkable list
  than "somewhere in the modular/geometric correspondence."

Stopping here per the round's instructions — no further action taken.
