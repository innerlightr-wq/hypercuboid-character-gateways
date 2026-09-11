# Referee Audit — `hypercuboid_character_sums.tex`

Manuscript Phase 3. Adversarial, skeptical read. This audit found the
manuscript's mathematics sound but uncovered a **major, previously
unnoticed prior-literature overlap** (Part XIV) that changes the
recommendation. Reported plainly, not softened.

---

## Summary

The manuscript proves, for `E:y^2=x^3+4x^2+2x` and `f=` LMFDB
`8.3.d.a`,
$$S(p)=\chi(-1)(a_p(f)+p)=-\chi(2)p+\chi(-1)a_p(E)^2$$
via an elementary reduction of a finite-field hypercuboid character sum
to a K3-surface point count, followed by a full Picard-lattice and
modularity argument. **The proof chain, on its own terms, is correct**
— every step was independently reconstructed in this audit and
survived. **However**, this audit located a 2002 paper — S. Ahlgren,
K. Ono, D. Penniston, *"Zeta functions of an infinite family of K3
surfaces,"* Amer. J. Math. **124** (2002), no. 2, 353–368 — whose
Theorem 2.1, specialized at `\lambda=1`, gives **exactly** the
manuscript's `S(p)` formula (confirmed numerically, ten primes, zero
discrepancy), and whose Theorem 1.2 already establishes the `\lambda=1`
surface is singular with CM by `\Q(\sqrt{-2})`. **This is the single
most important finding of this audit** and is reported in full in Part
XIV below.

---

## Part I — referee read

**Claim**: exact evaluation, for every odd prime, of two of three
residual character-sum classes from a finite-field hypercuboid
construction, via a discriminant-8 singular K3 surface and its
associated weight-3 CM newform.

**Genuinely proved in the manuscript**: the character-sum reduction
(Lemma 3.1), the affine point count (Lemma 3.2), the Weierstrass/Kodaira
classification (Prop. 4.1), the corrected `I_2`-fiber point count and
global ledger (Prop. 5.1–5.2), the height/Picard-rank computation
(Prop. 6.1), the algebraic Frobenius trace (Prop. 7.1), the twist
elimination (Prop. 7.2), and the resulting Main Theorem and corollaries.

**Imported from the literature**: Shioda–Tate, Shioda's height pairing,
the singular-K3 classification (Torelli + Shioda–Inose), Livné's
modularity theorem, the CM symmetric-square decomposition.

**Where a skeptical reader is most likely to object** (identified before
reading the claim ledger, confirmed below): (1) whether `\hat h(P_1)=1`
and the resulting `|\disc NS|=8` are correctly derived, specifically
whether the torsion-subgroup order used in the discriminant formula is
actually proved rather than asserted (Part VII); (2) whether the
"single prime suffices" twist argument (Part XI) is rigorous or a
disguised numerical fit; (3) — the finding that turned out to matter
most — **whether this exact evaluation already exists in the
literature** (Part XIV).

---

## Part II — Main Theorem audit

Reconstructed independently, step by step:

| Step | Classification |
|---|---|
| `\#X=\#V+19p+1` | Self-contained proof in manuscript |
| `\mathrm{Tr}(F_p\mid NS)=(19+\chi(-1))p` | Self-contained proof in manuscript |
| `\mathrm{Tr}(F_p\mid T)=\chi(-1)a_p(f)` | Self-contained proof + literature theorem (Livné) |
| Lefschetz combination `\Rightarrow S(p)=\chi(-1)(a_p(f)+p)` | Self-contained (pure algebra) |
| Sym² substitution `\Rightarrow S(p)=-\chi(2)p+\chi(-1)a_p(E)^2` | Self-contained + literature (Ribet/CM theory) |

**No unsupported assertion found in this chain.** Every step is either
proved in the text or traced to a named, checked citation.
**Independently re-verified numerically** (fresh run this phase, not
reused from Phase 2's cache) at 10+ primes across all four `\bmod8`
classes — see Part XVIII.

---

## Part III — character-sum reduction audit

`\Sigma_I(p)=(p-1)S(p)`: re-verified homogeneity (`P(zv)=z^6P(v)`,
`z^6` a square — correct), the origin (`\chi(0)=0`, correctly excluded),
the `x_0=0` hyperplane (correctly shown to contribute `0`, not omitted
by oversight), the `p^2` count of `x_0=1` representatives (no
repetition, no exceptional direction missed), and the orbit size `p-1`
(correct — the number of nonzero scalars). **No gap found.**

**Class-I/Class-II relation**: independently re-derived from the raw
index sets (Part 4 of this session's own working, reproduced below):
`\Sigma_I` uses forms indexed `\{0,1,2,3,4,5\}` (excludes `L_6=x_0+x_1+x_2`,
i.e. `-A_4`); `\Sigma_{II}` uses `\{0,1,3,4,5,6\}` (excludes `L_2=x_2=A_3`).
Both exclude a "coordinate-type" form (one of the four `A_i`, up to sign),
consistent with them forming one `S_4`-orbit together with the
analogous exclusions of `A_1,A_2`. Class III (`\S10`) excludes a
different, "pairing-type" form (index 3, `L_3=A_1+A_2`) — a genuinely
different orbit, consistent with the manuscript's claim that no relation
connects Class III to Classes I/II.

**Minor exposition finding** (see Part XVI, Minor Issues): the
manuscript's own phrase "omitting two forms related by a double
transposition" (used both in `\S2` and `\S10` for Class III) is
ambiguous/inaccurate as literally read — Class III, like I and II,
excludes exactly **one** form from the six-element product (matching the
paper's own general "6-element subsets" framing one sentence earlier in
`\S2`); the "two forms related by..." phrasing more likely means "the
omitted form is one of a pair swapped by `\pi`," but as written it
reads as if two forms are omitted, which would contradict the general
framing. **This does not affect the correctness of Prop. 10.1's proof**
(which only uses the polynomial `P_{III}` and the involution `T`,
independent of this phrasing), but is a genuine clarity bug — flagged
as a safe correction (Part XX).

---

## Part IV — K3 model audit

Independently recomputed `c_4,c_6,\Delta` from `a_2=t(t+1)^2,a_4=t^3(t+1)^2,a_6=0`
via the standard `b_2,b_4,b_6,b_8` formulas (fresh symbolic computation
this phase, not reused): confirmed
`c_4=16t^2(t+1)^2(t^2-t+1)`, `c_6=-32t^3(t-2)(t+1)^4(2t-1)`,
`\Delta=16t^8(t-1)^2(t+1)^6` exactly. Confirmed the Tate-valuation
classification at all four bad fibers `(2,3,8)\to I_2^*`,
`(0,0,2)\to I_2`, `(2,4,6)\to I_0^*`, and (via the weight-`(8,12,24)`
scaling at infinity) `(2,3,8)\to I_2^*`. Confirmed `e(X)=8+2+6+8=24`.
**Confirmed the "K3, not rational surface" conclusion is fully
justified**: the base curve is `\mathbb P^1` (genus `0`), which forces
irregularity `q(X)=0` automatically for any elliptic surface with
section over `\mathbb P^1` (a standard, general fact, not specific to
this surface); combined with `\chi(\mathcal O_X)=e/12=2`, this gives
`p_g=\chi-1+q=1`, and `(q,p_g)=(0,1)` with trivial canonical bundle
(from the elliptic fibration's own dualizing-sheaf structure) is the
standard characterization of K3 — **this reasoning is sound but is
stated tersely in the manuscript** ("confirming the K3 classification");
a referee would likely ask for one more sentence spelling out the
`q=0` step explicitly. **Minor exposition issue, not a gap.**

---

## Part V — point-count ledger audit (high risk, re-verified in full)

Independently re-derived `N_{I_2}(p)=2p+1-\chi(-2)` from the raw local
equation `Y^2=X'(X'-2)(X'+8\varepsilon)` at `t=1`: the node's tangent
cone gives branch directions `s=\pm\sqrt{-2}`; the blown-up exceptional
conic `W^2=-2u(u+8)`'s points at infinity satisfy `(W/u)^2\to-2`,
**the same locus** — confirmed this is a standard, general fact about
blowing up a node (the exceptional curve meets the strict transform
exactly along the node's tangent directions), not an ad hoc claim. The
intersection `C_1\cap C_2` is therefore a genuine degree-2 closed point,
split iff `\chi(-2)=1`. Inclusion–exclusion gives
`N_{I_2}(p)=(p+1)+(p+1)-(1+\chi(-2))=2p+1-\chi(-2)`. **Reconfirmed by
fresh script execution this phase** (Part XVIII): exact match at
`p=3,5,7,11,13,17,19,23`, correctly showing `N_{I_2}\ne2p` precisely
when `\chi(-2)=-1`.

`N_{I_2^*}(p)=7p+1`, `N_{I_0^*}(p)=5p+1`: re-examined the tree-union
argument; both survive (trees have no analogous intersection-splitting
subtlety, since every junction was separately shown unconditionally
rational via either ternary-quadratic-form isotropy or an explicit
nonzero integer implicit derivative — genuinely different, and
individually checked, mechanisms).

`\#X(\Fp)=\#V(\Fp)+19p+1`: re-derived fiber-by-fiber independently;
matches. **This section survives audit. The paper does NOT need to
stop here.**

---

## Part VI — height and Picard-rank audit

Re-verified `P_1=(-(t+1),i(t-1)(t+1)^2)` lies on `X` by direct symbolic
expansion (fresh computation this phase):
`X_1^3+a_2X_1^2+a_4X_1=-(t-1)^2(t+1)^4`, matching `Y_1^2=i^2(t-1)^2(t+1)^4`
exactly. Re-verified `\sigma(Y_1)=-Y_1` under `i\mapsto-i`. Re-verified
the four local-contribution values (`0,0.5,1,1.5`) against the standard
Shioda tables for the fiber types actually met (determined by evaluating
`x_1(t)` at each bad fiber, not assumed). `\hat h(P_1)=4-3=1`. Given
`\rho\le20` always and `\rho\ge19+1=20` from this non-torsion section,
`\rho(X_{\Qbar})=20` **exactly**, forced, no gap.

**No hidden field-of-definition issue found**: the manuscript is
explicit and correct that `P_1` is `\Q(i)(t)`-rational, not
`\Q(t)`-rational, and that this specific fact (not merely the
*existence* of a height-1 section) is what drives the later `\chi(-1)`
twist — this distinction is handled correctly throughout.

---

## Part VII — NS discriminant and transcendental lattice audit

**A genuine, moderate finding.** The manuscript computes
`|\disc\,NS(X)|=|\disc\,\Triv(X)|\cdot\hat h(P_1)/|\mathrm{MW}_{\mathrm{tors}}|^2=128\cdot1/16=8`,
using `|\mathrm{MW}_{\mathrm{tors}}|=4` (i.e. torsion exactly
`(\Z/2)^2`) via the phrase "the torsion-correction factor 16 from the
visible `(\Z/2)^2` structure." **This establishes a LOWER bound on
torsion correctly** (the three nonzero 2-torsion `x`-coordinates of the
generic fiber are roots of `X^2+a_2X+a_4=0`, whose discriminant
`t^2(t+1)^2(t-1)^2` is a perfect square — so all of `E_t[2]` is
`\Q(t)`-rational, directly verifiable, confirming `\mathrm{MW}_{\mathrm{tors}}\supseteq(\Z/2)^2`)
— **but the manuscript does not prove this is the COMPLETE torsion
subgroup** (that no larger torsion, e.g. from 4-torsion or an
additional independent 2-torsion-like structure, exists). This is
exactly the kind of gap a careful referee flags: the discriminant
computation is only as good as the torsion computation, and "visible"
is not "proved complete."

**Assessment of severity**: low-to-moderate. The final numerical
conclusion (`|\disc\,NS|=8`) is extremely well corroborated by
everything downstream — in particular, the eventual exact match (Part
II, XI) against the specific tabulated newform `8.3.d.a` across 20+
primes would be a remarkable coincidence if the discriminant, and hence
the identified CM field, were actually wrong. **This is not a proof
error; it is a missing lemma or missing citation.** A referee would
very likely accept the paper conditional on adding either (a) a short
proof that `\mathrm{MW}_{\mathrm{tors}}` is exactly `(\Z/2)^2` (e.g. via
a standard torsion-injects-into-component-group argument, not currently
in the manuscript), or (b) an explicit citation to where this exact
fact is established for this exact surface (if it already is,
elsewhere in the supporting repository).

**Evenness/orientation, explicitly checked**: `T(X)`, as the orthogonal
complement of `NS(X)` inside the unimodular, even K3 lattice
`H^2(X,\Z)`, is automatically even — this does not need separate proof
(inherited from the ambient lattice) and the manuscript's silence on
this point is not a gap, just an implicit standard fact. **Orientation**:
`h(-8)=1` counts *proper* (`SL_2(\Z)`) equivalence classes of the
associated binary quadratic form, which is exactly the invariant
governing *oriented* lattice isomorphism classes in the singular-K3
classification (Pjatecki\u{i}-\u{S}apiro–\u{S}afarevi\v{c}/Shioda–Inose) —
confirmed this is the correct invariant for the argument as used, not a
weaker (unoriented) class number that would leave residual ambiguity.

---

## Part VIII — NS Frobenius trace audit

Re-verified: the 19 trivial-lattice generators are each defined by an
explicit rational-coefficient local equation (traced to the specific
tables in Rounds 27/16/19 of the underlying project, reproduced in
Appendix B) — genuinely `\Q`-rational, not merely asserted from the
Kodaira type. The 20th class (from `P_1`) is `\Q(i)`-rational, not
`\Q`-rational (Part VI). `\sigma$ acts by `-1` on it (direct
computation). **No divisor class omitted or double-counted**: the 19
trivial-lattice generators and the `P_1`-class are linearly independent
by Shioda–Tate's own orthogonal-decomposition structure (trivial lattice
vs. Mordell–Weil quotient), and `19+1=20=\rho` exactly, with no room for
a 21st class or a missed dependency. **This section survives audit
cleanly.**

---

## Part IX — direct verification of the two flagged secondary references

**Pjatecki\u{i}-\u{S}apiro–\u{S}afarevi\v{c} (1971)**: the 1971 original
and a full read of the relevant chapter of Huybrechts' *Lectures on K3
Surfaces* were not obtained within this session's budget (both fetched
but not cleanly extracted). **Corroborated instead via aggregated,
independent secondary sourcing**, converging on: *the map `X\mapsto T(X)`
gives a bijection between isomorphism classes of singular K3 surfaces
and isomorphism classes of positive-definite oriented even rank-2
lattices*, with Pjatecki\u{i}-\u{S}apiro–\u{S}afarevi\v{c} supplying
injectivity (the Torelli theorem: isomorphic Hodge structures imply
isomorphic surfaces) and Shioda–Inose supplying surjectivity. This
**matches the manuscript's usage exactly**. Status: corroborated via
multiple independent secondary sources, not a fresh primary-source read
— one notch weaker than the Livné verification (Part X), and weaker
than requested by this round's Part IX instruction ("do not leave these
as bibliography-only checks"). **Recommend**: a human co-author with
library access should pull the actual 1971 Torelli-theorem statement
(or the relevant page of Huybrechts) before submission.

**Ribet (1977)**: **found and read directly** a paper explicitly
building on this material (M. Amir, L. Hong, arXiv:2007.09803, "On
`L`-functions of modular elliptic curves and certain `K3` surfaces"),
which states: *"By the theory of Inose and Shioda, ... symmetric squares
of elliptic curves with complex multiplication offer K3 surfaces that
correspond to weight 3 CM newforms."* **Attribution nuance, worth
noting precisely**: Ribet's 1977 paper is most directly the source for
the *converse* fact (a rational-coefficient weight-3 newform must have
CM), which the manuscript already correctly attributes to reference [6]
(Schütt). The *forward* `\mathrm{Sym}^2` decomposition itself is more
properly classical CM/Hecke-character theory (via Weil's converse
theorem) than specifically "Ribet's theorem." **This is a minor
citation-precision issue**: citing Ribet for this specific direction is
defensible (his paper's framework covers it) but a more precise
citation would name it as classical CM theory, possibly alongside
Shimura, rather than attributing the specific decomposition to Ribet
alone.

---

## Part X — Livné/Schütt modularity audit (re-confirmed, not reused from Round 34's summary)

Re-read the fetched primary source (Schütt, arXiv:0804.1558) fresh this
phase (not relying on Round 34's write-up): Theorem 4 there (attributed
to Livné) states singular K3 modularity up to twist, applicable
**regardless of whether `NS(X)` is `\Q`-rational** — directly applicable
to our `\rho(X/\Q)=19` case, exactly as the manuscript states. **New
supporting find this phase**: Schütt's own worked example in a
companion paper (*"Arithmetic of a Singular K3 Surface,"* Michigan Math.
J. 56 (2008), discriminant **3**, not 8) uses the **identical general
method** — Livné's theorem, then distinguishing among finitely many
twist candidates by comparing Fourier coefficients at a small number of
primes (there: 3 candidates, distinguished at `p=7`) — confirming this
is the field's own standard, accepted technique, not a nonstandard
shortcut invented for this manuscript. **This directly and positively
supports Part XI's audit** (below).

---

## Part XI — twist-proof audit (re-examined adversarially, again)

Reconstructed the ramification argument (`X` bad only at `2`,
`\mathrm{disc}(E)\propto2^5`, hence `\chi_0` unramified outside
`\{2,\infty\}`, exactly 4 fundamental discriminants) — sound, re-derived
independently. Reconstructed the degeneracy (`a_p(f)=0` at inert primes,
`\chi(-1)\chi(2)=\chi(-2)` — elementary, re-checked) collapsing 4
candidates to 2. **Re-did the `p=3` computation completely by hand**:
`\chi(-1)(3)=-1` (QRs mod 3 are `\{1\}`, `2\notin`); `S(3)=-1` (9-term
sum, hand-checkable); `a_3(f)=-2` (external, see Part XII). Both
candidate predictions computed by hand: `F_0` predicts `-5`, `F_1`
predicts `-1` — matches `F_1`. **Given the independently-reconfirmed 2-
candidate exhaustiveness, this genuinely is a valid elimination, not
disguised curve-fitting** — confirmed again this phase, and now further
corroborated by Part X's finding that this exact style of argument
(few-prime elimination against a proven-finite candidate set) is
standard published practice in this specific sub-field. **No break
found. This is the third independent audit of this specific step
(Rounds 33, 34, and this phase) to reach the same conclusion.**

---

## Part XII — `a_3(f)=-2` source verification

Sourced from the LMFDB raw API (`mf_newforms`, `traces` field for
`8.3.d.a`), not an AI-summarized fetch — reproducible via
`curl -s "https://www.lmfdb.org/api/mf_newforms/?level=8&weight=3&_format=json&_fields=label,traces"`.
**A reader could reproduce this exactly.** No CM short-cut computation
was substituted (this would require correctly resolving the Hecke
character's sign convention independently, a nontrivial undertaking —
flagged in Phase 2 as a possible but non-essential polish item, not
attempted this phase). **Plainly stated**: this single coefficient is
externally sourced from a database, used deductively in an elimination
argument (not inductively), and this is disclosed accurately in the
manuscript's own Appendix E.

---

## Part XIII — CM/symmetric-square identity audit

Re-derived independently: `\mathrm{Tr}(\mathrm{Sym}^2)=\alpha^2+\alpha\beta+\beta^2=(\alpha+\beta)^2-\alpha\beta=a_p(E)^2-p`
(pure linear algebra, no citation needed) and
`\mathrm{Tr}(\Lambda^2)=\alpha\beta=p` (always algebraic, the
polarization class). The CM-specific input is exactly, and only, the
*splitting* `\mathrm{Sym}^2(\rho_E)\cong\rho_f\oplus(\chi_K\cdot\mathrm{cyc})`
— correctly isolated in the manuscript as the one non-elementary
ingredient. **Checked both cases**: inert (`\chi(-2)=-1`):
`a_p(f)=a_p(E)^2-2p`, and since `a_p(E)=0$ at inert primes (standard CM
vanishing, independently true), both sides are `0-2p+... ` wait — direct
check: `a_p(E)=0\Rightarrow a_p(E)^2-p(1+\chi(-2))=0-p(1-1)=0=a_p(f)`,
consistent (`a_p(f)=0` at inert primes too, as required). Split
(`\chi(-2)=1`): `a_p(f)=a_p(E)^2-2p`, a nontrivial, checkable identity
at any specific split prime (verified numerically, Part XVIII). **No
issue found.**

---

## Part XIV — novelty audit (the central finding of this phase)

Searched, per the round's instruction, across: Schütt's low-discriminant
tables; Shioda–Inose/Kummer classifications; Jacobsthal-sum literature;
finite-field hypergeometric literature; CM weight-3 modular-form
literature.

1. **This exact Weierstrass K3 model / equivalent under rational change
   of variables**: **IMMEDIATE COROLLARY OF KNOWN RESULT.** S. Ahlgren,
   K. Ono, D. Penniston, *"Zeta functions of an infinite family of K3
   surfaces,"* Amer. J. Math. **124** (2002), no. 2, 353–368 (fetched
   and read directly, full PDF obtained from the author's own posted
   copy). This paper studies `X_\lambda: s^2=xy(x+1)(y+1)(x+\lambda y)`.
   **At `\lambda=1`, this is literally `s^2=xy(x+1)(y+1)(x+y)`, the same
   polynomial (up to renaming variables) as the manuscript's own
   `S(p)`'s summand.** Their **Theorem 2.1** states, for
   `A(\lambda,q):=\sum_{x,y}\phi_q(xy(x+1)(y+1)(x+\lambda y))`:
   $$A(\lambda,q)=\phi_q(\lambda+1)\bigl(a(\lambda,q)^2-q\bigr),\qquad a(\lambda,q):=-\sum_x\phi_q\Bigl((x-1)\bigl(x^2-\tfrac1{\lambda+1}\bigr)\Bigr).$$
   **Verified numerically this phase, fresh computation, 10 primes,
   zero discrepancy**: `A(1,p)=S(p)` exactly (same sum, confirmed), and
   AOP's Theorem 2.1 at `\lambda=1` reproduces `S(p)` exactly. Moreover,
   `a(1,p)=\chi(-1)(p)\,a_p(E)` exactly at every tested prime (AOP's
   elliptic curve `E_1:y^2=(x-1)(x^2-\tfrac12)` is the `\chi(-1)`-twist
   of the manuscript's own `E`), and substituting this into AOP's
   formula, using `\chi(-1)\chi(2)=\chi(-2)` on the support of `a_p(E)`,
   gives **exactly** the manuscript's own `-\chi(2)p+\chi(-1)a_p(E)^2`.
   **These are the same theorem, arrived at by different elliptic-curve
   normalizations of the same underlying fact.**
2. **Singularity/CM identification at `\lambda=1`**: also **already
   established** — AOP's **Theorem 1.2** proves `X_\lambda` is singular
   iff `\lambda\in\{1,8,1/8,-4,-1/4,-64,-1/64\}`, **including `\lambda=1`
   explicitly**; a citing paper (Amir–Hong, arXiv:2007.09803, read
   directly) reports AOP's associated newform at `\lambda=1` as an
   eta-product with **CM by `\Q(\sqrt{-2})`, twisted by `\chi_{-4}`**
   (`=\chi(-1)` in this manuscript's notation) — the same CM field and
   apparently the same twist character the manuscript derives
   independently via the K3 lattice/Livné route.
3. **Discriminant-8 singular K3 classifications (Schütt's tables)**:
   not independently located this phase (the specific table was not
   found via search), but is now superseded in relevance by finding #1.
4. **Jacobsthal-sum literature**: searched directly (arXiv:2102.07086,
   "Generalizations of Jacobsthal sums and hypergeometric series over
   finite fields," fetched and read); studies a **different** family of
   character sums (hyperelliptic curves `y^2=(x^m+a)(x^m+b)(x^m+c)`
   type); **RELATED BUT NOT EQUIVALENT** — no overlap found with `S(p)`
   specifically.
5. **Finite-field hypergeometric literature (Greene-style)**: broad,
   conceptually adjacent field (character sums, CM elliptic curves,
   weight-3 newforms all appear), but no exact match to `S(p)` located;
   **RELATED BUT NOT EQUIVALENT** at the level of search performed.
6. **Finite-field hypercuboid residue systems with this evaluation,
   and formulas equivalent to Class I/II specifically**: **NOT FOUND**
   — no evidence anywhere in this search that the *hypercuboid*
   motivating construction, the `\Sigma_I/\Sigma_{II}` reduction, or the
   Gateway relation `\Sigma_{II}=\chi(-1)\Sigma_I$ appear anywhere in
   the literature searched. This is the one genuinely
   **unduplicated** piece of the manuscript's content as far as this
   audit could determine — **not claimed as proof of novelty** (per the
   round's explicit instruction not to infer novelty from "not found"),
   but it is the part of the paper this audit found no overlap for
   after a real search, as opposed to the K3/modularity content, where a
   direct, near-exact overlap *was* found.

**Overall novelty classification for the manuscript's Main Theorem**:
**IMMEDIATE COROLLARY OF KNOWN RESULT** (Ahlgren–Ono–Penniston 2002,
Theorems 1.2 and 2.1, combined with a curve-twist identification). The
manuscript's independent K3-surface/Picard-lattice/Livné-theorem proof
route is a **genuinely different method** reaching the same conclusion
— this has some independent value (an alternative, geometric derivation,
methodologically distinct from AOP's elementary Jacobi-sum manipulation)
but **the manuscript, as currently written, does not cite AOP at all and
implicitly presents the `S(p)` evaluation as new** (it is careful never
to use the words "new" or "first," but the omission of the one directly
overlapping prior result is, in effect, a novelty overclaim by silence).
**This is a major finding requiring the paper to be substantially
reframed before release** — see Recommendation.

---

## Part XV — claim-strength audit

Checked every use of "exact," "all odd primes" (correctly always "every
odd prime"), "singular K3," "modular," "CM," "correspondence,"
"evaluation," "open," "derived," "proved." **No individual instance
found stronger than what its local proof supports** — e.g., "proved" is
used consistently only for items in the Claim Ledger's PROVED rows, and
"we determine" (used for the Picard lattice, etc.) is technically
accurate (the manuscript does determine these, correctly, even though —
per Part XIV — the *facts themselves* were already determined by
others). **The claim-strength problem this audit found is not
sentence-level overclaiming; it is a document-level omission** (missing
citation to directly overlapping prior work) that no single-sentence
"claim strength" check would catch — flagged here explicitly since it
falls between the round's Part XIV and Part XV categories.

---

## Part XVI — exposition audit

The logical chain `\Sigma_I\to S(p)\to V\to X\to NS/T\to f` is
followable by a specialist reader; motivations are adequate; no proof is
deferred so far that the main text becomes unverifiable on its own (all
five appendices contain full derivations, confirmed Phase 2). **Two
issues found this phase**:
- The Class III "omitting two forms" phrasing (Part III above) —
  genuinely confusing on a careful read, safe to fix.
- The K3-vs-rational-surface justification (`q(X)=0` from base
  `\mathbb P^1`) is terser than ideal (Part IV) — not incorrect, could
  be one sentence longer; **not fixed this phase** (a content addition,
  not a safe typo-level fix, per Part XX's scope).

No main-text material judged better suited to an appendix, and no
appendix material judged better suited to the main text — the Phase 2
split (full derivations in appendices, compressed statements + proof
sketches in the main text) holds up under this fresh read.

---

## Part XVII — Class III audit

Confirmed: the manuscript does **not** imply Class III is solved.
`\Sigma_{III}(p)=0$ at `p\equiv3\pmod4` is proved by an independent
mechanism (re-verified, Part III); `p\equiv1\pmod4` is explicitly named
open in the abstract, introduction, `\S10`'s Open Problem environment,
and the Limitations section — four separate, consistent statements, no
contradiction or overclaim found anywhere.

---

## Part XVIII — reproducibility audit

Ran, fresh this phase (not reused): `round32_I2_intersection_fix.py`
(the `N_{I_2}(p)` formula, 8 primes) — **passes, exact match**.
`round32_full_chain_check.py`, `round33_twist_proof_check.py` (the full
Main Theorem, 12–20 primes) — **passes, exact match, `ALL MATCH: True`**.
`round34_audit_sigmaI.py` (`\Sigma_I(p)=(p-1)S(p)` from the raw
3-variable sum) — **passes**. **No script's output is logically
necessary for any proof** — confirmed again by inspection: every script
recomputes a quantity whose formula is already proved in the manuscript
text, purely as a numerical check.

**One minor reproducibility issue found this phase**: `round32_full_chain_check.py`
and `round33_twist_proof_check.py` hardcode a dependency on a cached
file (`/tmp/newform_8_3_d_a.json`) with **no graceful error message** if
absent (unlike `round13_modular.py`, which has a clear `SystemExit`
pointing to the exact `curl` command needed) — a fresh user cloning the
repository and running these two scripts directly would hit a bare
`FileNotFoundError`. **Minor, easily fixed, not fixed this phase**
(a script edit, outside this round's "manuscript-only safe corrections"
scope) — flagged for a future housekeeping pass.

---

## Major mathematical issues

**None that invalidate the theorem.** The one genuinely major issue
found this phase is **not a mathematical-correctness issue** but a
**novelty/prior-literature issue** (Part XIV): the Main Theorem is an
immediate corollary of Ahlgren–Ono–Penniston (2002), uncited.

## Minor mathematical issues

1. **`\mathrm{MW}_{\mathrm{tors}}=(\Z/2)^2` asserted, not proved
   complete** (Part VII) — the discriminant-8 conclusion is very likely
   correct (strongly corroborated downstream) but the manuscript's own
   proof of it has a gap at this one step; needs an added lemma or
   citation.
2. **Ribet citation slightly imprecise** (Part IX) — defensible but
   could more precisely credit classical CM/Hecke-character theory
   alongside Ribet.
3. **Pjatecki\u{i}-\u{S}apiro–\u{S}afarevi\v{c} not independently
   fetched and read** (Part IX) — corroborated via secondary sourcing
   only; recommend a direct primary-source check before submission.
4. **K3-vs-rational-surface justification terse** (Part IV) — correct
   but under-explained by one sentence.

## Reference issues

See Part IX. Two secondary references (of eight total) remain at a
"bibliographically confirmed, not directly read" or "read via a citing
paper, with an attribution nuance" status. The single most important
reference in the paper (Livné, via Schütt) **was** directly verified,
both in Round 34 and reconfirmed fresh this phase.

## Novelty issues

**Major** — see Part XIV in full. The manuscript needs, at minimum: (a)
an explicit citation to Ahlgren–Ono–Penniston (2002); (b) a clear
statement of the precise relationship (their Theorem 2.1 at `\lambda=1`,
combined with the curve-twist identification `a(1,p)=\chi(-1)(p)a_p(E)`,
gives the manuscript's `S(p)` formula); (c) an honest reframing of the
paper's contribution — most plausibly as an independent, K3-geometric
proof of (part of) a known result, motivated by and newly connected to
the hypercuboid character-sum construction (which this audit's search
found no overlap for), rather than as a new evaluation of `S(p)` itself.

## Exposition issues

See Part XVI. Minor: the Class III "omitting two forms" phrasing (fixed
this phase, see below) and the terse K3-classification justification
(not fixed, content addition out of scope).

## Reproducibility

All checked scripts run and reproduce every claimed formula exactly.
One minor issue (two scripts' silent dependency on a cached file, no
fresh-clone error message) — not fixed this phase, flagged for later.

---

## Required revisions

1. **(Major, before any submission)**: add the Ahlgren–Ono–Penniston
   (2002) citation and an honest discussion of the relationship between
   this manuscript's Main Theorem and AOP's Theorem 2.1/1.2. This likely
   requires restructuring the Introduction and Discussion, and possibly
   the abstract.
2. **(Minor)**: add either a proof or a citation establishing
   `\mathrm{MW}_{\mathrm{tors}}=(\Z/2)^2$ exactly (not just `\supseteq`).
3. **(Minor)**: directly verify the Pjatecki\u{i}-\u{S}apiro–\u{S}afarevi\v{c}
   citation against a primary source; refine the Ribet citation's
   precision.
4. **(Minor)**: one added sentence justifying `q(X)=0` in the K3
   classification (Prop. 4.1's proof sketch).
5. **(Trivial, safe, done this phase)**: fix the Class III "omitting two
   forms" phrasing.

## Recommendation

**PHASE3-C** — substantive repair required before release. Not because
any theorem is false (every mathematical claim in the manuscript
independently re-verified correct in this audit), but because the paper
omits a directly, near-exactly overlapping 2002 published result, which
a real arithmetic-geometry referee would treat as a serious, immediate,
likely paper-blocking issue until addressed — this is squarely a
"substantive repair required" situation, not a copy-edit or minor
citation-formatting matter.

---

## Safe corrections made this phase

Per Part XX's explicit scope (typos, broken cross-references,
citation-format fixes, notation consistency, the existing overfull-hbox
issue) and **not** touching any mathematical content:

1. Clarified the Class III "omitting two forms related by a double
   transposition" phrasing (both occurrences, `\S2` and `\S10`) to
   correctly read as omitting **one** form, consistent with the general
   6-element-subset framing — a wording/notation-consistency fix, no
   mathematical content changed.

No other safe corrections were needed: cross-references, equation
references, and citation formatting were all already correct (re-
verified, Part XVIII / self-audit rerun below). The one remaining
overfull-hbox warning (13.7pt, one paragraph) was left as-is, exactly as
disclosed in Phase 2 — attempting further tightening risks disturbing
wording in a paragraph this audit specifically re-examined for
correctness (Part XI), so it was left untouched this phase.

**No substantive mathematical issue was silently repaired.** The
`\mathrm{MW}_{\mathrm{tors}}` gap, the reference-precision issues, and
above all the AOP novelty finding are all left exactly as found, for a
separate, deliberate repair phase.
