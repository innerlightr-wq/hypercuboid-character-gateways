# External Referee Report

**Manuscript**: "Class III Hypercuboid Character Sums and a Discriminant-4
Singular K3 Surface," E. De Jesús (draft, 21 pages).

**Basis for this report**: a cover-to-cover read of the manuscript PDF,
followed by independent recomputation — using no repository script, only
fresh symbolic/numeric computation built from the manuscript's own stated
definitions and equations — of every load-bearing claim. Round reports,
checkpoints, and internal audit files were not consulted, per the review's
instructions; the one exception is that the manuscript's own text cites
two internal files by name (`PHASE2A_DRAFT_AUDIT.md`,
`PHASE2B_DRAFT_AUDIT.md`) as the source of two named historical
corrections — these citations were noted but not opened, since the
manuscript's own text already states what was corrected and why, in
enough detail to evaluate the corrected result on its own.

---

## Summary

The manuscript proves, for every odd prime $p$,
$$\Sigma_{\rm III}(p) = \begin{cases}(p-1)\,a_p(f) & p\equiv1\pmod4\\0&p\equiv3\pmod4\end{cases}$$
where $\Sigma_{\rm III}(p)$ is a specific three-variable finite-field
character sum arising from a "hypercuboid" combinatorial construction
(inherited from a companion paper), and $f=\eta^6(4z)=\texttt{16.3.c.a}$
is a previously-known weight-3 CM newform (Ahlgren–Ono–Penniston's own
modular form, explicitly and repeatedly not claimed as new). The proof
route is: elementary reduction $\to$ elliptic K3 surface $\to$
Néron–Severi rationality (the paper's distinctive technical contribution)
$\to$ transcendental lattice/CM identification $\to$ Livné modularity +
finite twist elimination $\to$ point-count identity $\to$ final formula.

**The mathematical route is sound.** The central claim of the paper
(Néron–Severi rationality of $X_{\rm III}$'s reducible fibers, via full
rational $2$-torsion and graph rigidity, without resolving any fiber
explicitly) survives independent scrutiny, including an active attempt
to construct a counterexample automorphism (none exists). **One genuine
expository gap was found**: the manuscript's own explicitly-stated
standard for verifying fiber-component multiplicity ("we include this
explicitly, rather than inferring it," Remark 5.4) is met for only one
of the four marked leg components (the one meeting $P_1$); the analogous
computation for the two components meeting $P_2, P_3$ is asserted, not
shown, and a cross-reference pointing to where it should appear
("Appendix D") is misdirected — that appendix contains no such
computation. I independently performed the missing computation using
data already in the paper, and it checks out exactly as claimed. This is
a real gap in the written proof, fixable without new mathematical ideas.

---

## Part I — Referee summary

1. **Main theorem**: as stated above (Theorem 8.6).
2. **Mathematical route**: elementary algebra (character sum reduction,
   mod-4 vanishing) $\to$ explicit algebraic geometry (Weierstrass model,
   Kodaira fiber types, torsion, graph rigidity, lattice discriminant)
   $\to$ cited modularity theorem (Livné) $\to$ elementary/finite
   arithmetic (twist elimination) $\to$ cohomological bookkeeping
   (Lefschetz trace formula, point-count ledger).
3. **Elementary parts** (no cited external theorem needed): the
   projective reduction (§2), the mod-4 involution (§3), the Weierstrass
   completion-of-the-cube and invariant formulas (§4.1–4.2), the
   torsion-point factorization (§4.4), most of the graph-rigidity
   argument (§5, given the cited dual-graph structure).
4. **Elliptic-surface/K3-geometry parts**: Kodaira fiber-type
   classification via Tate's valuation criterion (§4.2), Shioda–Tate rank
   formula (§4.3), Shioda's torsion-injectivity theorem (§4.4), the
   Néron–Severi/trivial-lattice discriminant machinery (§5, Appendix D).
5. **External-modularity-theorem parts**: Livné's singular-K3 modularity
   theorem (§6.2) — existence only, not identification; the
   Shioda–Inose correspondence between rank-2 even lattices and CM data
   (§6.1).
6. **Finite theorem-based coefficient discrimination**: the twist
   elimination at $p=5$ (§7.3) — explicitly and correctly framed
   throughout as deductive elimination over an already-proved-exhaustive
   two-element candidate set, not a numerical pattern match (the
   manuscript itself makes this point explicitly in Remark 7.4, which I
   independently agree is the correct characterization).

**On the author's own contribution claims**: the manuscript repeatedly
and explicitly disclaims novelty for the modular form, for the general
K3/modularity machinery, and (candidly) for the exact level of the
newform (stated as resting on a literature/LMFDB search rather than an
independent conductor computation, §6.3). It claims novelty specifically
for (a) the hypercuboid reduction producing this sum, (b) the specific K3
surface $X_{\rm III}$, and (c) the graph-rigidity technique for proving
$\NS$-rationality. Having independently searched (Part XVI below) and
found no prior source for any of these three, I find this framing
accurate, not inflated.

---

## Part II — Proof dependency chain

| Arrow | Classification |
|---|---|
| Class III sum $\to$ projective reduction | SELF-CONTAINED (independently reverified, §III below) |
| $\to$ two-variable sum $T(p)$ | SELF-CONTAINED |
| $\to$ elliptic K3 surface, Weierstrass model | SELF-CONTAINED |
| $\to$ three $I_2^*$ fibers | SELF-CONTAINED (Tate's algorithm criterion applied explicitly, not table-quoted) |
| $\to$ full rational 2-torsion | SELF-CONTAINED |
| $\to$ torsion completeness $(\Z/2)^2$ | SELF-CONTAINED + LITERATURE THEOREM (Shioda's injectivity theorem, cited) |
| $\to$ 4 distinct legs, all $\Q$-rational | SELF-CONTAINED for 1 of 4 legs (multiplicity independently verified); **ASSERTED, not shown, for 2 of 4 legs** — see Major Issue 1 |
| $\to$ graph rigidity | SELF-CONTAINED (independently reconstructed and confirmed exhaustively, Part VII below) |
| $\to$ $\NS$-rationality, $\Tr(F_p|\NS)=20p$ | SELF-CONTAINED, given the above |
| $\to$ $\mathrm{disc}(\NS)=4$ | SELF-CONTAINED (independently rebuilt from scratch, Part IX below) |
| $\to$ $T(X)\cong\mathrm{diag}(2,2)$ | SELF-CONTAINED |
| $\to$ CM by $\Q(i)$ | SELF-CONTAINED, given $h(-4)=1$ (a standard, checkable fact) |
| $\to$ weight-3 level-16 form | LITERATURE THEOREM (Livné, existence) + FINITE EXACT VERIFICATION (level/candidate identified by search, not derived — disclosed honestly) |
| $\to$ quadratic-twist elimination | FINITE EXACT VERIFICATION (candidate set proved exhaustive by elementary ramification argument; single-prime elimination is deductive, correctly characterized as such) |
| $\to$ point-count identity | SELF-CONTAINED (independently rebuilt two ways, Part XIV below) |
| $\to$ exact Class III formula | SELF-CONTAINED, given all of the above |

**No arrow is classified UNSUPPORTED.** One arrow (the 4-distinct-legs
step) is classified SELF-CONTAINED only in part, with a real gap flagged
as Major Issue 1.

---

## Part III — Projective reduction (independently recomputed)

Built `P_III` fresh from Definition 2.1 and independently verified in
`sympy`: homogeneity $P(zv)=z^6P(v)$ holds identically; the claimed
correct substitution ($x_1\mapsto x,\,x_2\mapsto t$) gives
$P_{\rm III}(1,x,t) - xt(t+1)(x+t)(x+t+1) \equiv 0$ exactly; the
manuscript's own flagged *incorrect* substitution ($x_1\mapsto
t,\,x_2\mapsto x$) genuinely does **not** vanish (I computed the nonzero
residual explicitly: $-t^4x-t^3x^2-t^3x+t^2x^3+tx^4+tx^3$), confirming
the manuscript's own account of what went wrong in an earlier draft and
that the printed, corrected version is right. $P_{\rm III}(0,x_1,x_2)=0$
confirmed. **No exceptional stratum is mishandled**: the zero-vector and
$x_0=0$ hyperplane both correctly contribute $0$, and every other point
is covered exactly once by the affine parametrization. **Verdict: holds.**

---

## Part IV — Mod-4 involution (independently recomputed)

Independently verified $\tau\circ\tau=\mathrm{id}$ via genuine function
composition (not a naive substitution into an unevaluated symbolic
expression — the exact trap the manuscript's own account says caused an
error in an earlier verification attempt); confirmed
$P_{\rm III}(\tau x)+P_{\rm III}(x)\equiv0$ identically; confirmed the
fixed locus gives $P_{\rm III}=0$ there (via the vanishing of the factor
$x_1+x_2$, correctly identified in the text). The vanishing conclusion
for $p\equiv3\pmod4$ follows immediately and unconditionally. **This
proof is fully independent of the modular argument**: it never
references $T$, $V_{\rm III}$, $X_{\rm III}$, or any modular form; I
confirmed this by checking that no symbol outside $\{x_0,x_1,x_2,\chi,p\}$
appears anywhere in Proposition 3.1's statement or proof. **Verdict: holds.**

---

## Part V — K3 model (independently recomputed)

Rather than re-verifying the manuscript's stated $c_4,c_6,\Delta$ against
themselves, I re-derived them from the *original* affine equation
$V_{\rm III}:Y^2=X(X+1)T(T+1)(X+T+1)$ independently, performing the
cube-completion and rescaling myself. Result: exact match with the
manuscript's stated $a_2,a_4,c_4,c_6,\Delta$ (verified as an exact
polynomial identity, difference $=0$). Independently confirmed
$v_T(c_4)=2,v_T(c_6)=3,v_T(\Delta)=8$ at $T=0$ (series expansion,
computed directly, not read off a table); the symmetric argument at
$T=-1$ is manifest from $\Delta$'s $(T+1)^8$ factor. At $T=\infty$,
independently confirmed $\deg c_4=6,\deg c_6=9,\deg\Delta=16$, giving
$v_\infty(\Delta)=24-16=8$ under the stated K3 total-degree bound.
Minimality ($v(c_4)<4$ at each place) checked. Euler-number check
$3\times8=24$ confirmed arithmetically. **Verdict: holds — and the
independent re-derivation from the original (not the already-simplified)
equation is a stronger check than merely re-verifying stated formulas
against themselves.**

---

## Part VI — Full rational 2-torsion (independently recomputed)

Verified $X^3+a_2X^2+a_4X = X(X+T(T+1))(X+T(T+1)^2)$ as an exact
polynomial identity. Verified the three pairwise root differences
($T(T+1)$, $T(T+1)^2$, $T^2(T+1)$) are nonzero polynomials, vanishing
only at $T=0,-1$. The "no larger 2-torsion" step (any 2-torsion point has
$y=0$, hence is a root of a cubic, hence there are at most 3 nonzero
ones) is elementary and correct. The "no torsion of order $>2$" step
correctly invokes Shioda's injectivity theorem plus the observation that
$\Phi(I_2^*)\cong(\Z/2)^2$ is exponent-2 at all three bad fibers — this
is a valid, standard argument, and I did not find a gap in it (Shioda's
theorem is cited, not re-proved, appropriately, since it is a genuinely
external classical fact). **Verdict: holds.**

---

## Part VII — Graph rigidity (attacked directly)

This is the manuscript's central claim, and I gave it the most scrutiny.

**Items 1–3** (exactly four multiplicity-one legs exist in an $I_2^*$
dual graph; a section meets exactly one component, of multiplicity 1;
$O,P_1,P_2,P_3$ meet four pairwise-distinct legs): item 1 is a correctly
cited classical fact (Kodaira/Néron/Tate); item 2 is proved correctly and
elementarily in the manuscript (Lemma 5.5, an immediate consequence of
$\sigma\cdot F=1$); item 3's *coordinate computation* (which points land
where) I independently reproduced and confirmed exactly
($x_1(P_1)=0$; $x_1(P_2)=-(T+1)$, $x_1(P_3)=-(T+1)^2$, both $=-1$ at
$T=0$, requiring a second blow-up level where they separate to $x_3=-1,-2$
respectively).

**Item 4** (those four legs are individually $\Q$-rational, i.e.
genuinely of multiplicity 1, not mislabeled spine nodes): **this is where
I found a genuine gap.** The manuscript's Remark 5.4 explicitly states
the standard it holds itself to: *"a point could in principle resolve
cleanly into a single smooth exceptional curve that is nonetheless a
multiplicity-2 ('spine') component... Lemma 5.3 rules this out by direct
computation rather than by assumption."* Lemma 5.3 then performs this
check — showing the tangent-cone-restriction is the reduced curve
$y_4^2-x_4=0$, not a perfect square — **only for the leg meeting
$P_1$** (the $x_1=0$ point). For the legs meeting $P_2$ and $P_3$ (the
$x_3=-1,-2$ points), Lemma 5.6's proof *asserts* "two further, pairwise
distinct, multiplicity-one components" and cites "(Appendix~D)" for the
supporting computation — but Appendix D ("Graph rigidity and the
Néron–Severi lattice") contains no blow-up or tangent-cone computation
at all; it is entirely about the abstract graph and the discriminant. I
could not find the claimed verification anywhere in the manuscript for
these two points.

I performed the missing computation myself, using only the Weierstrass
data already in the paper (the same first blow-up $F_1$ given in Lemma
5.3's proof sketch, continued to the second level at $x_1=-1$): the
tangent cones at $x_3=-1$ and $x_3=-2$ are $Tx_4+y_3^2$ and $-Tx_4+y_3^2$
respectively — both rank-3 nondegenerate, confirming multiplicity 1 at
both points, exactly as the manuscript claims. **The underlying
mathematical fact is therefore correct.** But as written, the manuscript
does not demonstrate it, contradicting its own stated evidentiary
standard for exactly this step. See Major Issue 1.

**Item 5** (fixing the four legs pointwise forces the automorphism group
of the graph to be trivial): I rebuilt the abstract graph from scratch
(not importing the manuscript's own script or its stated vertex/edge
list beyond the bare structural description in Lemma 5.2/Appendix D:
tree, legs $L_1,L_2$ at one end, spine $S_1$-$S_2$-$S_3$, legs $L_3,L_4$
at the other) and exhaustively enumerated all $7!=5040$ permutations,
filtering for multiplicity- and edge-preservation. Result: exactly 8
automorphisms of the unmarked graph; exactly 1 (the identity) fixes all
four legs individually. **I actively tried to construct a surviving
nontrivial automorphism and found none — the claim is correct.** The
manuscript's own hand-proof (Lemma 5.7, using only leaf-uniqueness and
the uniqueness of $S_2$ as the common neighbor of $S_1,S_3$) is, on
inspection, a complete and correct proof on its own terms; it does not
need the computational enumeration, which is properly relegated to a
corroborating remark rather than treated as the proof itself (a good
practice the manuscript correctly follows).

**Item 6** (spine components individually $\Q$-rational): follows validly
from items 4–5, contingent on item 4's gap being closed.

---

## Part VIII — NS basis and Frobenius trace

Rank count $2+3\times6=20$ is simple arithmetic, correct. No generator
redundancy: the 20 generators (zero section, fiber class, 18 non-identity
fiber components) are the standard Shioda–Tate generating set, and the
manuscript correctly notes torsion sections are $\Z$-linear combinations
of these, not independent generators — this is standard and correctly
stated (torsion affects the *index* $[\NS:\Triv^{\rm sat}]$, not the
rank). The convention "$\Tr(F_p|\NS)=20p$" (each Frobenius-fixed
algebraic class contributes eigenvalue exactly $p$, not $1$) is standard
Weil-conjecture bookkeeping for algebraic cycle classes in $H^2$ of a
surface over $\F_p$ — correctly invoked, consistent with its use in
Appendix F's $H^0$–$H^4$ decomposition (where $H^0$ contributes $1$ and
$H^4$ contributes $p^2$, correctly distinguishing degree-0, degree-2, and
degree-4 Tate-twist normalizations). **Verdict: holds**, modulo Major
Issue 1's dependency.

---

## Part IX — Discriminant computation (independently rebuilt)

Built the $D_6$ Cartan matrix from scratch (standard definition: $2$s on
the diagonal, $-1$s for adjacent simple roots in the $D_6$ Dynkin
diagram, with the characteristic fork at one end) and computed its
determinant independently: $4$. Computed $\mathrm{disc}(U)=-1$. Computed
$\mathrm{disc}(\Triv)=(-1)\cdot4^3=-64$. Computed
$|\mathrm{disc}(\NS)|=64/|\mathrm{MW}_{\rm tors}|^2=64/16=4$. All match
the manuscript exactly. No sign error, no squaring error, and — checked
specifically, since the manuscript itself flags this as a place a prior
draft went wrong — **no confusion between the $\NS$ and transcendental
discriminants**: the manuscript correctly computes $|\mathrm{disc}(\NS)|$
first, purely from lattice data, and only afterward (§6) invokes the
standard fact that $|\mathrm{disc}(T)|=|\mathrm{disc}(\NS)|$ for
orthogonal complements in a unimodular lattice — the direction of
reasoning (geometry $\to$ NS $\to$ T, never reversed) is maintained
throughout, as the manuscript itself claims. **Verdict: holds.**

---

## Part X — Transcendental lattice

Given rank 2, even, positive-definite, $|\det|=4$: verified $4ac-b^2=4$
with $a=c=1,b=0$ gives $\mathrm{diag}(2,2)$, and — the specific point
flagged by the manuscript as historically error-prone — verified the
*associated primitive quadratic form* uses **half** the diagonal Gram
entries: $(a,b,c)=(1,0,1)$ (not the raw diagonal entries $(2,0,2)$, which
would give the wrong discriminant $-16$). Checked $b^2-4ac=-4$
arithmetically. This convention was independently verified against a
fresh literature search of the Shioda–Inose correspondence, which states
the relevant matrices explicitly as $\begin{pmatrix}2a&b\\b&2c\end{pmatrix}$
— confirming the manuscript's corrected convention matches the primary
source, not merely being self-consistent. Is `diag(2,2)` uniquely forced
by rank+definiteness+discriminant alone? For discriminant $-4$ specifically,
yes: class number $h(-4)=1$ means there is exactly one $\mathrm{SL}_2(\Z)$-class
of forms, so the identification is not merely *a* valid answer but *the
only* one. **Verdict: holds.**

---

## Part XI — CM identification

$h(-4)=1$ is a standard, well-known fact (the ring of Gaussian integers
$\Z[i]$ has class number 1), independently checkable by the classical
reduction algorithm for binary quadratic forms of discriminant $-4$
(only $(1,0,1)$ satisfies $|b|\le a\le c$). The relevant order is the
*maximal* order ($\Z[i]$ itself, since the discriminant $-4$ is a
fundamental discriminant, not a proper multiple of one). No orientation
subtlety arises at class number 1 (orientation issues in the
lattice-to-form dictionary matter when the class group is nontrivial;
here it is trivial). The singular-K3 classification (Shioda–Inose) is
applied correctly: transcendental lattice isomorphism class $\to$ unique
quadratic form class $\to$ unique CM field, in that order, with no step
skipped. **Verdict: holds.**

---

## Part XII — Modularity theorem usage

Livné's theorem, as stated in the manuscript (Theorem 6.1), matches an
independently retrieved paraphrase of the actual 1995 paper (singular K3
over $\Q$ with transcendental-lattice discriminant $-D$ $\Rightarrow$
existence of a weight-3 newform with CM by $\Q(\sqrt{-D})$, level
determined by the conductor of the Galois representation on $T(X)$) —
the manuscript's statement is faithful to this, not a stretched or
overloaded paraphrase. Hypotheses (singular K3 over $\Q$, rank-2 $T(X)$,
discriminant $-4$) are each explicitly checked against results proved
earlier in the same manuscript, not merely asserted. **The exact level
($16$, as opposed to $8$ or $32$) is honestly flagged as identified by a
literature/LMFDB search for the unique matching candidate, not derived
from an independent conductor computation specific to $X_{\rm III}$** —
this is disclosed plainly (§6.3, and again in the Complete Proof
Ledger-style remark embedded in Appendix E) and does not misrepresent
itself as a from-scratch derivation. Whether this constitutes "forced by
theory" or "forced up to twist" in the strictest sense: the CM field,
weight, and discriminant are forced by theory; the specific level is
forced *up to* the search's completeness (i.e., contingent on no other
level-16 candidate with the right CM field and rational eigenvalues
existing — a fact the search claims but a referee cannot independently
verify without LMFDB access). This is a reasonable, disclosed limitation,
not a hidden one. **Verdict: holds, with the limitation appropriately
disclosed rather than concealed.**

---

## Part XIII — Quadratic-twist elimination

Independently re-derived the candidate set from ramification theory: a
quadratic twist of a form unramified outside $\{2\}$ must itself be
unramified outside $\{2\}$, and the fundamental discriminants supported
only at the prime $2$ are exactly $\{1,-4,8,-8\}$ — I verified this is a
complete list (the classical fact that $\Q(\sqrt{d})$ ramifies only at 2
iff $d\in\{-4,8,-8\}$, plus the trivial case $d=1$) rather than accepting
the manuscript's four-element set on faith. The CM-vanishing collapse
($a_p(f)=0$ at inert primes, hence all four candidates agree there) and
the split-prime collapse ($\chi(-1)(p)=1,\ \chi(-2)(p)=\chi(2)(p)$ at
$p\equiv1\bmod4$, collapsing $4\to2$) are both elementary identities,
independently verified. **The single coefficient at $p=5$ is logically
sufficient precisely because, and only because, the candidate set was
already proved exhaustive beforehand** — I confirm this is exactly the
manuscript's own stated logic (Remark 7.4), and I independently verified
there is no gap in it: with an exhaustive 2-element set $\{F_0,F_1\}$ and
one prime where they provably differ, refuting one deductively
establishes the other, with no room for a third unconsidered possibility.
**No major gap found here.**

---

## Part XIV — Point-count ledger

Independently rebuilt $\#X_{\rm III}(\F_p)=1+p^2+20p+a_p(f)$ two ways:
(a) via the $H^0$–$H^4$ Lefschetz decomposition (Appendix F), checking
each cohomological degree's contribution separately — $H^0\to1$ (trivial
Frobenius action, rank 1), $H^1,H^3\to0$ (K3 Betti numbers), $H^2\to
20p+a_p(f)$ (the two pieces already established), $H^4\to p^2$ (top-degree
Tate twist) — and (b) via the direct affine/projective fiber-sum route
(§8), independently checking the "exactly $p$ points" claim at each
finite bad fiber (confirmed: $T(T+1)=0$ kills the affine equation's
right-hand side identically at $T=0,-1$, giving $Y=0$ for each of $p$
values of $X$ — verified by direct substitution, not assumed) and the
"$7p+1$ per resolved $I_2^*$ fiber" claim (seven rational $\Pp^1$'s,
$p+1$ points each, minus 6 double-counted nodes — a correct, standard
combinatorial count given component rationality). Both routes give the
identical formula; I found **no missing $+1$, no extra factor of $p$, no
fiber-count error** (I specifically checked the $p-2$ good-finite-fiber
count against $3$ bad fibers total out of $p+1$ points of
$\Pp^1(\F_p)$ — arithmetic confirmed: $(p+1)-3=p-2$). **The Classes I/II
ledger is not assumed to transfer** — the manuscript explicitly re-derives
every constant for this surface's own (three-bad-fiber) configuration,
and I independently confirm none of the constants match by coincidental
reuse of the companion paper's (four-bad-fiber) numbers. **Verdict: holds.**

---

## Part XV — Final formula

Derived independently from the audited pieces: $p\equiv3\bmod4$ gives
$T(p)=0$ two ways — (i) the elementary involution (Part IV, entirely
self-contained, no reference to $X_{\rm III}$), and (ii) CM-inertness of
$f$ at primes inert in $\Q(i)$ (a fact about the newform's induced Galois
representation, no reference to the raw sum or $\tau$). I confirmed these
really are logically independent by checking that neither proof's text
references the other's objects. $p\equiv1\bmod4$ gives
$T(p)=a_p(f)$ via the twist-elimination + point-count-ledger route (Parts
XIII–XIV). Combining with Lemma 2.2 gives the boxed main theorem exactly
as stated. **Verdict: holds.**

---

## Part XVI — Literature priority audit

| Target | Finding | Classification |
|---|---|---|
| Exact Class III sum $\Sigma_{\rm III}(p)$ | Not located in any search | NOT FOUND |
| Exact two-variable sum $T(p)$ | Not located | NOT FOUND |
| Exact K3 model $X_{\rm III}$ | Not located | NOT FOUND |
| Equivalent birational model | Not located; AOP's own $\lambda=8$ surface is a *different* model (confirmed: manuscript states $T(p)\ne A(8,p)$ at essentially every tested prime — a claim I did not independently re-verify against AOP's formula, but which is stated as a numerical fact, not a proof, and is consistent with the two surfaces having different Weierstrass models) | RELATED (not birationally equivalent, on the evidence given) |
| Three-$I_2^*$ extremal K3 surfaces | A general search found extremal-K3 classification literature (Miranda–Persson, Shimada) but no specific hit for the $3\times I_2^*$, $(\Z/2)^2$-torsion configuration | NOT FOUND (search-scope limited, honestly acknowledged by the manuscript itself) |
| $T=\mathrm{diag}(2,2)$ | Standard discriminant-4 singular K3 surfaces are known to exist in the literature (as a lattice-isomorphism class); no source found identifying $X_{\rm III}$ specifically with any of them | SAME TRANSCENDENTAL LATTICE ONLY |
| $\eta^6(4z)$ | Confirmed (matches the manuscript's own citations) as AOP's own form, also independently tied to the quartic Fermat K3 by Huber–Liu–McLaughlin et al. | SAME MODULAR FORM ONLY |
| AOP $\lambda=8$ | Confirmed as the direct source of the modular form; not claimed by the manuscript, correctly, to be the same surface | SAME MODULAR FORM ONLY, not birationally equivalent |
| Finite-field hypergeometric equivalents | Not specifically checked against Greene's framework by this reviewer; the manuscript does not claim a hypergeometric-series interpretation, so this is not a gap in the manuscript's own claims | N/A to this manuscript's claims |

**No claim of novelty stronger than this search supports was found
anywhere in the manuscript.** The manuscript is explicit, repeatedly,
that "NOT FOUND" reflects search-scope limitations (no institutional
database/table access), not a positive novelty claim — this is the
correct way to report such findings, and I concur with the manuscript's
own self-assessment on this point.

---

## Part XVII — Novelty and contribution assessment

Best description: **E (combination)**, specifically weighted as: (C) is
the strongest single element — a new graph-rigidity technique for proving
$\NS$-rationality without explicit fiber resolution, which (per the
literature search above) does not appear to be used this way in either
AOP's or the companion paper's own treatment — combined with modest
instances of (A) (a new reduction of a new sum, following an already-known
technique from the companion paper) and (B) (a new geometric proof route
for an evaluation whose *shape* parallels an already-known one, AOP's
$\lambda=8$ case, though for a provably different surface). I do **not**
find this to be (D) (a known result in different notation) — the surface,
the sum, and the specific NS-rationality argument all appear, on the
evidence available, to be genuinely new presentations, not restatements.
This assessment is conservative and matches the manuscript's own stated
self-assessment closely (§9.1, §10) — I did not find the manuscript
overclaiming relative to what an independent read supports.

---

## Part XVIII — Exposition audit

- **Introduction honesty**: accurate. The "what is known vs. what is
  proved" distinction (Remark 6.2) is a model of the kind of disclosure
  this area of mathematics needs, and is applied consistently.
- **Graph-rigidity argument understandability**: good — the five-step
  structure (legs identified, sections marked, Galois fixes legs, graph
  rigidity, conclusion) is easy to follow, and Figure 1 is genuinely
  useful (a reader can verify the rigidity argument by eye against the
  figure).
- **Notation stability**: stable throughout; $T$ (base coordinate) vs.
  $p$ (prime) is maintained without confusion, and the one place this
  could mislead a reader (footnote-level remark in §4.1 explaining the
  choice to keep $T$ rather than relabel to $t$) is handled proactively.
- **Appendices vs. main text**: appendices genuinely expand compressed
  steps rather than duplicating the main text — I found no appendix that
  merely restates a main-text result without adding computational detail.
- **Overclaiming language**: searched specifically for "new," "first,"
  "unique," "exact," "for all odd primes," "independent proof." No
  instance was found asserting an unsupported claim; every use of "new"
  found is a *disclaimer* of novelty ("not claimed as new," "no claim to
  any new general theorem"), and "unique" is used correctly in its
  technical sense (unique candidate, unique reduced form) with
  justification given at each use. "For all odd primes" is used
  correctly — the theorem genuinely does hold for all odd $p$, with
  $p=2$ separately and correctly excluded as the surface's only bad
  prime.
- **One exposition defect found**: the misdirected cross-reference
  ("(Appendix~D)" where the intended target — a blow-up computation — does
  not exist in Appendix D at all) discussed in Part VII. This is a real
  defect a careful reader will trip over.

---

## Part XIX — Reproducibility check

The manuscript's own reproducibility table (Appendix F, 4 primes) is
explicitly and correctly labeled illustrative, not evidentiary — I
independently recomputed $T(p)$ for all four listed primes ($5,13,17,29$)
directly from the manuscript's Definition 2.2 formula and confirmed exact
agreement with the listed $a_p(f)$ values (the latter read directly off
the manuscript's own printed $q$-expansion of $f$ for $p=5$; for
$p=13,17,29$ I relied on the manuscript's stated values, not an
independent LMFDB lookup, since re-deriving Hecke eigenvalues of a
weight-3 CM newform from scratch is outside the scope of a reasonable
referee check and the $p=5$ value — the only one load-bearing for the
proof — is independently confirmed). **No theorem in the manuscript
relies on a prime sweep**: the only prime consulted in the actual proof
chain is $p=5$, used exactly once, deductively, as the manuscript itself
insists (Remark 7.4) and as I independently confirm is the correct
characterization of its role.

---

## Correctness assessment

The manuscript's main theorem is **correct**, and its proof is
**substantially complete**, with one identified, narrow, fixable gap
(Major Issue 1 below). No error was found in any computation I
independently reproduced. The one gap found is an *incompleteness of
exposition* (a claimed computation not shown, for 2 of 4 symmetric cases,
where the shown case and the unshown cases are structurally identical),
not a mathematical error — I closed the gap myself in a few minutes using
only data already present in the paper, and the result matches the
paper's claim exactly.

---

## Major issues

**1. Fiber-multiplicity verification for the $P_2,P_3$ legs is asserted,
not shown, and the supporting cross-reference is misdirected.**
Lemma 5.6's proof (main text, §5) and the corresponding passage in
Appendix C both claim the components met by $P_2,P_3$ are "multiplicity-one,"
but only the $P_1$-component's multiplicity is verified by explicit
tangent-cone computation (Lemma 5.3, cross-checked in two independent
charts in Appendix C). Lemma 5.6's proof cites "(Appendix~D)" for the
$P_2/P_3$ computation, but Appendix D contains no blow-up or tangent-cone
material — it is entirely about the abstract graph and the discriminant.
This directly contradicts the manuscript's own stated evidentiary
standard (Remark 5.4: multiplicity-1 must be shown "by direct
computation rather than by assumption"). **This must be fixed before
publication**: add the tangent-cone computation for $x_3=-1$ and
$x_3=-2$ (structurally identical to the existing computation for $x_1=0$)
to Appendix C, and correct the cross-reference in Lemma 5.6's proof. I
performed this computation independently (see Part VII above) and
confirm it supports the manuscript's claim — the fix is expository, not
a new mathematical result, but it is necessary: as currently written, a
careful reader cannot verify Proposition 5.1 (the paper's central
result) without either trusting an unshown claim or redoing the
computation themselves.

No other major issue was found.

---

## Minor issues

1. The reproducibility table's $p=13,17,29$ values for $a_p(f)$ are
   stated without an in-text derivation or explicit LMFDB citation
   pointer at that exact location (the general LMFDB label is given
   earlier, but a reader wanting to check these three specific values
   would need to consult LMFDB directly — reasonable, but could be made
   more explicit with a footnote).
2. §9's comparison table and the associated "not a general law" caveat
   are well-handled, but the table's "NS-rationality mechanism" row
   compresses a very large difference in technique (explicit twist
   isomorphism vs. graph rigidity) into a few words; a one-sentence
   parenthetical pointing to §5 vs. the companion paper's relevant
   section would help a reader unfamiliar with both papers.
3. Remark 6.2's "known vs. proved" framing is excellent but appears only
   once; a reader skimming only §7–8 (the twist/point-count sections)
   would benefit from one more brief restatement that the modular form
   itself remains not-new throughout those sections too (the manuscript
   does say this in the abstract and introduction, so this is a very
   minor readability point, not a substantive gap).

---

## Literature/priority assessment

See Part XVI. No prior exact result found for the sum, the surface, or
the technique; the modular form and the general machinery are correctly
and consistently attributed to their known sources throughout. The
manuscript's own novelty claims are calibrated conservatively and match
what an independent search supports.

---

## Exposition

See Part XVIII. Generally strong; one misdirected cross-reference found
(tied to Major Issue 1) and three minor readability suggestions.

---

## Reproducibility

See Part XIX. The proof does not depend on any numerical pattern; the
one prime actually used in the proof ($p=5$) was independently
reconfirmed.

---

## Required revisions

1. **(Major)** Add the explicit tangent-cone/multiplicity verification
   for the $P_2$- and $P_3$-leg components (at $T=0$; the analogous
   computation should also be added, or explicitly noted as identical in
   structure, for $T=-1,\infty$) to Appendix C, matching the standard
   already met for the $P_1$-leg in Lemma 5.3. Correct the "(Appendix~D)"
   cross-reference in Lemma 5.6's proof to point to the corrected
   location.
2. **(Minor)** Add an explicit pointer (footnote or inline citation) for
   the $a_{13}(f),a_{17}(f),a_{29}(f)$ values used in the illustrative
   reproducibility table.
3. **(Minor, optional)** Expand the "NS-rationality mechanism" row's
   comparison in §9 with a one-sentence pointer to the relevant sections
   of each paper.

---

## Recommendation

**MINOR REVISION.**

The theorem is correct and the proof, once the one identified gap is
closed (a closure I have already independently verified succeeds using
data already in the manuscript), is complete. Nothing found in this
review requires new mathematics, a change to any theorem statement, or a
re-examination of any other part of the argument. The revision required
is narrow, specific, and does not place the paper's main result at risk.

---

# Final Report

1. Main theorem reconstructed? **Yes**, independently, from the
   manuscript's own stated definitions, matching exactly.
2. Projective reduction status: **Holds**, independently recomputed.
3. Involution status: **Holds**, independently recomputed, confirmed
   fully independent of the modular argument.
4. K3 classification status: **Holds**, independently re-derived from
   the original (not pre-simplified) equation.
5. Torsion status: **Holds**, both completeness steps independently
   checked.
6. Graph-rigidity status: **Holds for the abstract graph argument**
   (exhaustively confirmed, no surviving automorphism found by active
   search); **one supporting lemma (multiplicity-1 for 2 of 4 legs) has
   a real expository gap**, independently closed by this review but not
   shown in the manuscript as written.
7. NS basis/rationality status: **Holds**, contingent on Major Issue 1's
   fix.
8. Exact $\Tr_{\NS}$ status: **Holds** ($=20p$), given the above.
9. Discriminant status: **Holds**, independently rebuilt from a
   from-scratch $D_6$ Cartan matrix; $|\mathrm{disc}\,\NS|=4$ confirmed.
10. $T(X)$ status: **Holds**, $\mathrm{diag}(2,2)$, uniquely forced given
    $h(-4)=1$.
11. CM identification status: **Holds**, $\Q(i)$, verified against a
    fresh literature check of the Shioda–Inose convention.
12. Modularity theorem status: **Holds**; hypotheses correctly checked;
    exact level honestly disclosed as search-identified, not
    independently derived.
13. Twist elimination status: **Holds**; candidate set independently
    re-derived from ramification theory, not merely accepted.
14. $p=5$ sufficiency status: **Holds**; correctly and explicitly
    characterized as deductive elimination, not pattern-matching, and I
    independently confirm this characterization is accurate.
15. Point-count ledger status: **Holds**, independently rebuilt two
    structurally different ways, agreeing.
16. Final Class III theorem status: **Holds**, given items 1–15 (with
    item 6's gap noted as needing a written fix, not a mathematical one).
17. Literature-overlap status: no prior exact result found for the sum,
    the surface, or the technique; novelty claims appropriately
    calibrated.
18. Novelty/contribution assessment: (E) combination, weighted toward
    (C) the graph-rigidity technique as the strongest single element.
19. Major issues: **one** (multiplicity-1 verification gap for 2 of 4
    legs, plus a misdirected cross-reference).
20. Minor issues: **three** (documentation/pointer suggestions, none
    mathematical).
21. Referee recommendation: **MINOR REVISION.**
22. Safe for preprint release? **Not yet as currently written** — the
    one major issue should be fixed first, since it is exactly the kind
    of gap a future external referee would flag, and fixing it is quick
    and low-risk (I have already verified the fix succeeds).
23. Highest-value next action: add the missing tangent-cone computation
    for the $P_2,P_3$ legs to Appendix C (using the derivation already
    performed independently in this review) and correct the
    cross-reference in Lemma 5.6's proof; after that specific, narrow
    fix, the manuscript should be considered ready for preprint release.

### Verdict: **CLASSIII-REF-B**

Minor revision required. The mathematics is sound and the main theorem
survives independent, adversarial reconstruction — including an active,
successful attempt to break the paper's central and most distinctive
argument (graph rigidity), which held. One specific, narrow, and already-
verified-closeable gap in the written exposition (not in the underlying
mathematics) should be fixed before release.

---

## THE THREE MOST IMPORTANT THINGS WE LEARNED

1. **A paper can state its own safety rule clearly and still fail to
   follow it in one spot, and the clearer the rule, the easier the slip
   is to catch.** This manuscript explicitly warns against exactly the
   mistake it then almost makes — claiming a component has multiplicity
   one without showing the check — and states plainly, in its own words,
   why that check matters. That very clarity is what made the omission,
   two paragraphs later, so easy for an outside reader to notice.

2. **Verifying a claim yourself is a different, stronger act than
   confirming an argument is plausible.** Everything in this review that
   was actually computed fresh — not just read and nodded along to — held
   up, including the one place worth worrying about. The gap that
   mattered wasn't a wrong idea; it was a right idea the author never
   actually finished writing down.

3. **A cross-reference that points to the wrong place is its own kind of
   bug, separate from whether the underlying claim is true.** The
   citation to "Appendix D" sent a reader looking for a computation that
   lives nowhere in the document. Fixing the missing computation and
   fixing the broken pointer are two different, equally necessary
   repairs — a reader can be let down by a paper being wrong, or just as
   easily by a paper being right somewhere it doesn't say it is.
