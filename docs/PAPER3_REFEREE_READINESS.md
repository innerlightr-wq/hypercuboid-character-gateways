# Paper 3 — referee readiness

Verdict up front: **classification B**, citation and exposition revision only, with one factual
sentence to correct. The mathematics reproduces end to end. **No Zenodo version was created and no
theorem, abstract, introduction or conclusion was rewritten.**

## Strongest contribution, in one sentence

> We identify the Class III hypercuboid character sum with the Frobenius trace on the transcendental
> lattice of an explicit discriminant-4 singular K3 surface, determine that lattice to be `diag(2,2)`
> by a fiber-component rationality argument that needs no resolution of any singular fiber, and obtain
> the closed evaluation `Sigma_III(p) = (p-1) a_p(eta^6(4z))` for `p = 1 mod 4`.

The graph-rigidity lemma is the technical novelty; the modular form is not claimed as new anywhere,
and the paper is scrupulous about that.

## What reproduces (independent verification, this pass)

Everything below was recomputed without using the paper's own scripts.

* **The Weierstrass reduction.** Completing the cube gives `X^3+(T+2)X^2+(T+1)X`; multiplying by
  `u^2` and setting `X' = uX`, `Y' = uY` with `u = T(T+1)` gives exactly the paper's
  `a_2 = T(T+1)(T+2)`, `a_4 = T^2(T+1)^3`, `a_6 = 0`. Verified symbolically.
* **The invariants.** `c_4 = 16T^2(T+1)^2(T^2+T+1)`, `c_6 = -32T^3(T-1)(T+1)^3(T+2)(2T+1)`,
  `Delta = 16T^8(T+1)^8` — all three match the manuscript verbatim.
* **The fibers.** At `T=0` and `T=-1`: `v(c_4)=2`, `v(c_6)=3`, `v(Delta)=8`, so `n = 8-6 = 2`, type
  `I_2^*`, minimal because `v(c_4) = 2 < 4`. At infinity `deg Delta = 16`, so `v_inf = 24-16 = 8`,
  again `I_2^*`. `Delta` has no other root. Exactly three bad fibers.
* **The lattice chain.** `D_6` has rank 6 and determinant 4; `rank Triv = 2 + 3*6 = 20`; hence
  `rho = 20` and `rank MW = 0` are both forced by `rho <= 20`; `|disc NS| = 4^3/4^2 = 64/16 = 4`; and
  `diag(2,2)` is the **unique** even positive-definite rank-2 lattice of determinant 4 (class number of
  discriminant `-4` is 1) — so `T(X) = diag(2,2)` and the CM field is `Q(i)`.
* **The graph rigidity.** The `I_2^*` dual graph is a tree on 7 vertices with 6 edges. Exhaustive
  search over all `7! = 5040` vertex permutations: exactly **8** preserve multiplicities and adjacency,
  and exactly **1** of those fixes the four legs individually — the identity. This confirms the
  manuscript's Appendix F claim precisely.
* **The twist elimination.** `chi(2)` at `p=5` is `-1`; `a_5 = -6`; so `F_0(5) = -6 = T(5)` survives
  and `F_1(5) = +6` is eliminated. One prime suffices because the candidate set was first reduced to
  two hypotheses by ramification and CM vanishing.
* **The modular identification, computed from the eta product rather than from a label.** Expanding
  `eta^6(4z) = q * prod (1-q^{4n})^6` directly and comparing with the character sum:
  **`T(p) = a_p` at every one of 21 primes from 3 to 113**, including all `p = 3 mod 4` where both
  vanish. And **`Sigma_III(p) = (p-1) a_p`** at all 15 primes where `Sigma_III` was computed directly
  from its 3-variable definition (`p <= 61`). No LMFDB lookup was used.

That last check is the most persuasive item in the whole package and deserves to be stated in the
paper as what it is: a comparison against the eta product, not a label match.

## Build status

**The manuscript could not be rebuilt: this machine has no TeX installation** (no `pdflatex`,
`xelatex`, `lualatex`, `latexmk`, `tectonic`, `bibtex` or `biber`, and no texmf tree). So no claim is
made here that the source compiles to the deposited PDF. What was verified instead, by static analysis
of the `.tex`:

* 49 labels, 44 references, **no undefined references**;
* 11 citation keys, 11 `\bibitem`s, **no missing citations and no uncited bibitems** (after this pass's
  addition of Paper 1);
* the theorem environments in the source match, in order and in wording, the statements in the
  deposited PDF's extracted text.

The repository PDF is byte-identical to the audited deposit (`sha256 ba37532b…9d9eb7`). A build should
be run before submission; nothing in the static check suggests it would fail.

## The one thing that must be corrected

**§2.1 says the `S_4` action has "exactly three orbits" on the seven six-element subsets. It has
two.** Verified by direct enumeration: the seven forms correspond to the seven complement-pairs of
`{1,2,3,4}`, four of shape `(1,3)` and three of shape `(2,2)`, and `S_4` is transitive on each — orbit
sizes **4 and 3**.

The sentence is also internally inconsistent with the next one, which says Classes I and II *both*
omit a singleton-type form — i.e. both lie in the size-4 orbit. The three *classes* arise because that
orbit splits `3 + 1` according to whether the omitted representative involves the eliminated
coordinate `A_4`, and crossing the split costs exactly one factor of `chi(-1)` — which is precisely
Paper 2's Gateway relation `Sigma_II = chi(-1) Sigma_I`.

Suggested replacement (not applied — it is a mathematical statement, not a typo):

> The natural `S_4`-symmetry permuting `A_1,…,A_4` acts on the seven six-element subsets with two
> orbits, of sizes four and three, according to whether the omitted form corresponds to a
> `(1,3)`- or a `(2,2)`-shaped complement pair. The size-four orbit splits further, `3+1`, according to
> whether the omitted representative involves the eliminated coordinate `A_4`; crossing that split
> multiplies the sum by `chi(-1)`, which is the Gateway relation of [ClassesI_II]. This yields the
> three character-sum classes `Sigma_I`, `Sigma_II`, `Sigma_III`, of which Class III — omitting the
> `(2,2)`-type form `L_3 = x_0+x_1` — is in a genuinely different orbit, with no permutation relating
> it to Classes I or II.

Nothing downstream is affected: `Sigma_III` is defined by an explicit formula and every later result
concerns it alone.

## Referee objections, and the answers available

**"This surface is probably already known — it is AOP's `lambda = 8` surface."** Answerable, and more
sharply than the paper currently does. The manuscript says the two "are provably non-isomorphic (the
two-variable sums `T(p)` and `A(8,p)` disagree at essentially every tested prime)". That is a numerical
claim where a structural one is available: since `A(lambda,q) = chi(lambda+1)(a(lambda,q)^2 - q)` and
`chi(9) = 1`, one has `A(8,p) = a(8,p)^2 - p`; at `p = 3 mod 4`, `a(8,p) = 0` so `A(8,p) = -p`, while
the paper proves `T(p) = 0`. **So `T(p) != A(8,p)` for every `p = 3 mod 4`, with no computation** — and
one prime of good reduction already forces non-isomorphism over `Q`. Verified numerically too:
`T(p) != A(8,p)` at all 14 primes tested. Recommend replacing "essentially every tested prime" with
this argument; also add the one-line reason that for K3 surfaces birational implies isomorphic, which
is why the stronger word is justified.

**"The Picard lattice is not proved saturated."** Answerable. `NS/Triv` is the Mordell–Weil torsion,
and the paper proves torsion completeness — that it is all of `(Z/2)^2`, not merely contains it. That
is what supplies the `16` in `64/16 = 4`. A referee will read this proposition closely; it is the load
bearing step and it is present.

**"The modular identification is only numerical."** Not answerable by the numerics alone, and the
paper does not rely on them: Livné supplies modularity up to quadratic twist, ramification at `{2}`
forces a four-element candidate set *before any value is consulted*, CM vanishing collapses it to two,
and one prime decides. That is a finite check inside an exhaustive criterion, which is legitimate. The
paper already flags the distinction explicitly. Keep that flag prominent.

**"AOP may already cover this case."** Answerable. AOP study their own one-parameter family
`X_lambda` with no hypercuboid motivation and no Class III notion; their form here is their
`lambda = 8` member. Paper 3's surface has a different Weierstrass model, a different fiber
configuration, and a different point count. The paper's §"AOP-precise" enumerates six possible senses
of overlap and addresses each — good practice, and it should stay.

**"The non-isomorphism argument proves too little."** Currently the weakest wording in the paper; see
above for the fix that makes it a proof.

**"Class III terminology obscures a standard object."** Partly fair. `Sigma_III` is a prescribed
quadratic-character pattern on a hyperplane-arrangement complement, and the provenance audit
established that the `30 -> 15` / `14 -> 7` collapse is the standard quotient `F_2^n/<1>`, whose index
set is `PG(n-2,2)`. Recommend one sentence at first use translating the bespoke terms, and not leading
the introduction with hypercuboid motivation.

**"The paper depends on unpublished work."** Now answerable: Paper 1 is deposited
(`10.5281/zenodo.22216640`) and Paper 2 is deposited (`10.5281/zenodo.22711323`). This pass adds the
Paper 1 citation, which was missing. And no Paper 3 proof takes a theorem of either as a premise — §2.1
restates what is used.

**"The computations are not independently reproducible."** Answerable: every computational claim in
the paper was re-derived in this pass without using the paper's scripts, and all agreed.

## Remaining weaknesses, in order of how much they matter

1. The `S_4` orbit-count sentence is wrong (above). Must fix.
2. The non-isomorphism argument is stated numerically when a structural proof is available. Should fix
   — it converts the paper's own claim from "provably" plus a numerical parenthesis into an actual
   proof.
3. The introduction opens on hypercuboid combinatorics. The arithmetic geometry — the surface, the
   lattice, the newform — is the contribution, and should appear in the first paragraph. Restructuring
   proposed, not applied.
4. "Singular K3" is used without stating once that it means maximal Picard number rather than a
   singular variety. One sentence.
5. No build was possible here; run one before submission.
6. The paper cites `Huber` as "preprint" with no identifier. If it is now published, update it; if not,
   say "unpublished preprint" explicitly.

## Recommended revisions before submission

Apply in this order: fix the orbit count; strengthen the non-isomorphism argument to the `p = 3 mod 4`
structural form; add the "singular K3 = Picard number 20" sentence; move the arithmetic-geometric
contribution into the first paragraph of the introduction and demote the hypercuboid framing to a
sentence with a translation into standard language; state the eta-product verification as an eta-product
comparison rather than a label match; check the `Huber` reference's status; rebuild.

None of these is a mathematical gap. Classification **B**: the mathematics is sound and verified; the
work needed is citation, exposition and one factual correction.
