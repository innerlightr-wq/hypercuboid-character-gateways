# Hypercuboid exploration — Round 2 working notes

Full narrative report delivered in chat; this file holds the durable
mathematical derivations and the raw classification data pointers so
every conclusion can be reproduced without re-deriving it from scratch.

## Part I — formalization (restated precisely)

Sigma_S(p) = sum_{x in F_p^d} chi( prod_{J in S} L_J(x) ), L_J(x) = sum_{j
in J} x_j, S a set of nonempty subsets J subseteq [d] = {0,...,d-1} (d =
n-1). Incidence matrix: rows = forms in S, columns = coordinates,
0/1-valued. m_k(S) = column sum at coordinate k.

Proven invariances (conservative — only what was actually checked):
- **Coordinate permutation** (sigma in S_d acting on labels, inducing
  J -> sigma(J) on the whole representative-form family): Sigma_S(p) =
  Sigma_{sigma(S)}(p), because x -> x_{sigma^{-1}}) is a bijection of
  F_p^d carrying the product of forms in S to the product of forms in
  sigma(S). **Used** to interpret the n=5 "different-labeled 4-cycle"
  adversarial test (Part XI, case 4) as a genuine confirmation, not
  assumed elsewhere to quotient the n=4 exhaustive search (that search was
  run over ALL 63 subsets, no symmetry reduction applied, so the 87.3%
  resolved figure is not an artifact of under-sampling orbits).
- **General bijective change of variables**: trivially, Sigma_S(p) is
  invariant under ANY bijection of the domain F_p^d (it's just relabeling
  the summation index) — used explicitly in the multiplicity-2 derivation
  (Part III) to justify the hyperplane substitution.
- **NOT used**: multiplying individual forms by field constants (does not
  apply — our forms are fixed, not free up to scalar) and general GL_d
  changes of variables (would leave the "standard 0/1-subset-sum form"
  family, not used to quotient anything).

## Part II — Multiplicity-1 lemma (full proof)

**Lemma.** Let L_1,...,L_m be affine-linear forms on F_p^d (L_i(x) =
c_i . x + b_i). If some coordinate x_k has nonzero coefficient in EXACTLY
ONE L_i (say L_{i0}), then sum_{x in F_p^d} chi(prod_i L_i(x)) = 0 exactly.

**Proof.** Fix y = all coordinates except x_k. D(y) = prod_{i != i0}
L_i(x)|_{x_{-k}=y} (independent of x_k). L_{i0}(x) = a*x_k + e(y), a != 0.
sum_{x_k} chi(D(y)*(a*x_k+e(y))) = chi(D(y)) * sum_{x_k} chi(a*x_k+e(y)).
As x_k ranges over F_p, a*x_k+e(y) ranges bijectively over ALL of F_p, so
the inner sum = sum_{z in F_p} chi(z) = 0 exactly (standard fact). This
holds for EVERY fixed y (including where D(y)=0, trivially). Sum over y of
0 is 0. QED.

**Scope (Part II.A/B/C):** the proof uses only affine-linearity and one
coefficient being nonzero-and-unique; it applies verbatim to (A) the
homogeneous zero-sector forms, (B) the mixed {L_J, 1-L_J} normalized
affine family (same coefficient pattern, different constant term — the
proof never used b_i), and (C) ANY finite collection of affine-linear
forms over any F_p. Strongest correct statement: (C), stated as a fully
general lemma about affine hyperplane arrangements. This is an ELEMENTARY
fact (rediscovery-filter classification: standard technique, essentially
the same idea used in the paper's own Theorem 5.1 proof) — not claimed as
a new discovery, only as a clean generalization of the paper's Prop 6.2
beyond odd cardinality.

## Part III — Multiplicity-2 elimination identity (full derivation)

Coordinate x occurs in exactly two forms L_a = a*x + A(y), L_b = b*x+B(y)
(A,B homogeneous linear in y, a,b != 0). Factor: L_a*L_b = ab*(x-r1)(x-r2),
r1=-A(y)/a, r2=-B(y)/b. Classical fact (derived from scratch, not just
cited): for fixed r1,r2 in F_p,
    sum_x chi((x-r1)(x-r2)) = -1  if r1 != r2,  p-1  if r1=r2.
(Proof: shift x'=x-r1; the r1!=r2 case reduces, via x'=Delta*u with
Delta=r2-r1, to a Delta-INDEPENDENT constant K = sum_u chi(u^2-u); complete
the square, u^2-u=(u-1/2)^2-1/4, a shifted sum_v chi(v^2-1/4); standard
identity sum_v chi(v^2-c) = -1 for c!=0 (discriminant of v^2-c is 4c!=0)
gives K=-1. The r1=r2 case is direct: chi((x-r)^2)=1 for x!=r, 0 for x=r,
giving p-1.)

So sum_x chi(L_a L_b) = chi(ab)*[-1 + p*1{A(y)=B(y)}]. Writing
D(y) = b*A(y)-a*B(y) (homogeneous linear in y): A(y)=B(y) <=> D(y)=0.

**Case analysis (the four cases requested in Part III):**
1. D nonconstant, D(y)=0 has solutions but isn't everything: for a
   HOMOGENEOUS D this is automatic once D is not identically zero (a
   nonzero linear functional's zero set is always a genuine hyperplane,
   never empty, never everything) — this is the ONLY case that occurs for
   the zero-sector system (proof below), and is case "4" (coincide on a
   lower-dimensional y-condition) in the prompt's list.
2. D identically zero (case "3", forced coincidence): only possible if
   L_a, L_b were proportional on the y-part; **proved impossible** for the
   zero-sector's own forms when both already contain the shared coordinate
   (if A=B as functions of y AND both L_a,L_b contain coordinate k, then
   J_a\{k}=J_b\{k} together with k in both forces J_a=J_b, contradicting
   L_a != L_b) — but the engine does NOT assume this; it checks D
   explicitly at every recursion depth (needed because after one
   hyperplane substitution the descendant forms are no longer pure 0/1
   zero-sector forms, and coincidence could in principle reappear; it did
   not, in every case tested).
3. "D is a nonzero CONSTANT" (case "1"/empty coincidence locus, only
   possible for genuinely AFFINE forms with a nonzero constant term):
   does not arise for the (homogeneous) zero sector at all; would need
   checking separately for the normalized affine sector, not pursued this
   round (out of the paper's own stated priority and this round's brief).

**Resulting exact recursive identity** (homogeneous case, D not identically
zero — i.e., the only case that occurs):
    Sigma_S(p) = -chi(ab)*Sigma_{S'}(p) + p*chi(ab)*Sigma_{S'|_H}(p)
S' = S \ {L_a,L_b} in the (d-1)-dim y-space; the H-term is obtained by
solving D(y)=0 for one coordinate (EXACT rational arithmetic, since the
solving coefficient need not be +-1 — this generalization, using Python's
Fraction type, was required after a real coefficient-magnitude-2 case was
found during n=4 classification; see "bug/limitation log" below) and
substituting into the other forms, landing in dimension d-2.

**Where chi(-1) comes from, precisely** (answering Part IX): chi(-1) is
NOT injected by any rule — it only ever appears because the DEEPEST level
of an H-branch recursion can terminate at a single remaining coordinate v
with exactly two forms {v, -v} (or more generally {c*v, -c*v}), i.e. an
H-branch where D happens to force one variable to be the negative of
another; the sum_x chi((x-r1)(x-r2)) formula with r1=0,r2=0 -> reduces to
sum_v chi(-v^2) = chi(-1)*sum_v chi(v^2) = chi(-1)*(p-1). Every chi(c) that
appears anywhere in this system's recursion is a genuine consequence of an
accumulated chi(ab) product at some step, tracked exactly by the engine's
symbolic chi_arg (an integer, canonicalized to its squarefree part,
representing chi(that integer) — a direct generalization of the "just
chi(-1)" special case Round 1 found by hand, since chi is completely
multiplicative and a product of chi(a_1)*chi(a_2)*... collapses to one
chi(a_1*a_2*...) argument).

## Bug / limitation log

- First engine draft restricted a,b (the two multiplicity-2 leading
  coefficients) to {+-1} and the hyperplane-solving pivot coefficient to
  {+-1}, flagging anything else "UNRESOLVED (engine limitation)". Running
  it on the full n=4 classification (Part V) produced exactly this failure
  on subset (0,3,4,5): after one elimination, a residual pair of 1-D forms
  with coefficients a=1, b=2 appeared (NOT an engine bug -- a genuine
  consequence of two prior substitutions both landing nonzero contributions
  on the same surviving variable). Generalized chi(ab) to an arbitrary
  integer character-argument (multiplicativity of chi makes this exact and
  cheap: chi(a)*chi(b)=chi(ab)), and generalized the pivot-solving step to
  exact `fractions.Fraction` arithmetic (chi(num/den) = chi(num*den) mod p,
  since chi(den)^2=1). This raised the n=4 resolved fraction from
  45/63 (naive rank-based count, Round 1) to 52/63 (first engine draft) to
  **55/63 (87.3%) after the generalization**, with zero direct-enumeration
  mismatches at every stage. See `results/classify_n4.json` for the full
  per-subset record (including confluence-order test results).

## Where results live

- `scripts/elimination_engine.py` — the engine (SymValue algebra + the
  recursive `eliminate()`).
- `scripts/verify_engine.py` — direct-enumeration cross-checker; also
  reproduces the three Round-1 closed forms exactly (Part IX requirement).
- `scripts/classify_n4.py` / `results/classify_n4.json` — full n=4
  exhaustive classification (63 records) + confluence test.
- `scripts/adversarial_n5.py` — Part XI n=5 targeted tests (10 cases).
