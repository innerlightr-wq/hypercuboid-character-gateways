# Paper 3, stage by stage — what each object is and why it appears

Written for the author. Plain language, but nothing fudged. Each stage says what the object *is*, why
it shows up *here*, which theorem carries you to the next stage, what is standard, what the paper
contributes, and what you should be able to say out loud if a referee stops you in a corridor.

---

## 1. The Class III sum

**What it is.** A single number attached to each odd prime `p`:

```
Sigma_III(p) = sum over all (x0,x1,x2) in F_p^3  of  chi( x0 x1 x2 (x0+x2)(x1+x2)(x0+x1+x2) )
```

where `chi` is the Legendre symbol (`+1` on nonzero squares, `-1` on non-squares, `0` at zero). You are
multiplying six linear forms together and asking, on average, whether the product is a square.

**Why it appears here.** The hypercuboid setup has seven linear forms. Choosing six of them (i.e.
omitting one) gives a character sum. The seven choices fall into `S_4`-orbits, and Class III is the
one that omits a form of "pair type" — the form `x0+x1`, fixed up to sign by the double transposition
`(13)(24)`.

**Theorem to the next stage.** The projective reduction: the sextic is homogeneous of degree 6, so
`chi` is constant along lines through the origin, giving `Sigma_III(p) = (p-1) T(p)` with

```
T(p) = sum over (x,t) in F_p^2  of  chi( x t(t+1)(x+t)(x+t+1) ).
```

**Standard / contributed.** The technique is standard (and is Paper 2's); the application to this
particular sextic is local to Paper 3.

**Say out loud.** "Because the sextic is homogeneous of even degree, the character is constant on
punctured lines, so a 3-variable sum collapses to `(p-1)` times a 2-variable sum."

---

## 2. The quadratic character, and why `p mod 4` matters at all

**What it is.** `chi(-1) = +1` exactly when `p = 1 mod 4`. That is Euler's criterion, nothing deeper.

**Why it appears here.** Two separate places, and they should not be conflated.

* In the *setup*: the hypercuboid conditions come in complementary pairs whose sums differ by a sign,
  so they can all be squares at once only if `-1` is a square. That is Paper 1's Theorem 3.1.
* In the *answer*: `Sigma_III(p) = 0` for `p = 3 mod 4`, proved by an explicit coordinate involution
  that sends the integrand to `-1` times itself. If a quantity equals `chi(-1)` times itself and
  `chi(-1) = -1`, it is zero.

**Standard / contributed.** Both are elementary. The involution is the paper's own, and — worth
saying — it needs no geometry at all.

**Say out loud.** "Half the theorem is elementary: for `p = 3 mod 4` a sign-reversing involution kills
the sum outright. The geometry is only needed for `p = 1 mod 4`."

---

## 3. From a character sum to a surface

**What it is.** The identity `#{y : y^2 = c} = 1 + chi(c)` turns a character sum into a point count.
Summing it over all `(X,T)` gives

```
V_III : Y^2 = X(X+1) T(T+1) (X+T+1),        #V_III(F_p) = p^2 + T(p).
```

**Why it appears here.** This is the only move in the paper that changes the *kind* of object: after
it, you are doing geometry, and `T(p)` is a point count.

**Theorem to the next stage.** None needed — it is an identity, valid at `c=0` too.

**Say out loud.** "`T(p)` is not merely *like* a point count; it *is* the point count of an explicit
affine surface, minus `p^2`."

---

## 4. The elliptic fibration

**What it is.** Regard `T` as a parameter. For each fixed `T`, the equation in `(X,Y)` is a cubic —
an elliptic curve. So the surface is fibred by elliptic curves over the `T`-line.

**Why it appears here.** Elliptic fibrations are the one setting where the Picard lattice of a K3 can
be computed by hand, via Shioda–Tate. Without the fibration there is no route to the lattice.

**Theorem to the next stage.** Completing the cube and scaling by `u = T(T+1)` gives the minimal
Weierstrass form

```
Y^2 = X^3 + T(T+1)(T+2) X^2 + T^2(T+1)^3 X,
```

whose discriminant is `Delta(T) = 16 T^8 (T+1)^8`. Tate's algorithm then reads off the bad fibers:
type `I_2^*` at `T = 0`, `T = -1` and `T = infinity`, and nothing else.

**Standard / contributed.** The machinery is textbook (Kodaira, Néron, Tate). The specific model and
its fiber configuration are the paper's.

**Say out loud.** "Three `I_2^*` fibers, at `0`, `-1` and infinity. `v(Delta) = 8` at each, and
`v(Delta) = n+6` gives `n = 2`."

---

## 5. The Néron–Severi lattice

**What it is.** `NS(X)` is the group of algebraic curve classes on the surface, with the intersection
form. Its rank `rho` measures how many independent algebraic curves the surface carries.

**Why it appears here.** Because `NS` and its orthogonal complement split the interesting cohomology,
and the Frobenius trace on `NS` is completely computable when every component is rational.

**Theorem to the next stage.** Shioda–Tate:

```
rho = rank(Triv) + rank(MW),        Triv = U + D_6 + D_6 + D_6,  rank 2 + 18 = 20.
```

Every K3 has `rho <= 20`. So `rho = 20` **and** `rank MW = 0` are both *forced* — neither is assumed.
That is the cleanest structural point in the paper and worth saying first.

**Standard / contributed.** Shioda–Tate is standard. What is the paper's own is proving that every
component of every reducible fiber is individually defined over `Q` — see the next stage — because
without that you cannot claim `Tr(F_p | NS) = 20p`.

**Say out loud.** "The trivial lattice alone already has rank 20, so Picard number 20 and
Mordell–Weil rank 0 both follow from the K3 bound. Nothing is assumed."

---

## 6. The graph-rigidity argument — the distinctive part

**What it is.** The seven components of an `I_2^*` fiber form a tree: a three-vertex spine with two
legs attached at each end. Galois can only permute components by a symmetry of this tree that
preserves multiplicities. That symmetry group has order 8.

**Why it appears here.** You need every component to be Galois-fixed to get `Tr(F_p | NS) = 20p`. The
usual route is to resolve the singular fiber explicitly and inspect. The paper avoids that entirely.

**The argument.** The zero section and the three rational 2-torsion sections meet four *distinct*
multiplicity-one components — the four legs. So Galois fixes those four. A tree automorphism fixing
all four legs must be the identity: each leg is a leaf with a unique neighbour, which pins both spine
ends, and the middle spine vertex is the unique common neighbour of the two ends. Hence Galois acts
trivially on all seven components.

**Standard / contributed.** This is **the paper's central new technique**, and it is genuinely neat:
five lines of graph theory replacing an explicit resolution. The exhaustive check over all `5040`
permutations is offered as confirmation, and the paper is explicit that it is a check and not the
proof.

**Say out loud.** "Four rational sections mark four distinct legs; a tree automorphism fixing four
marked leaves is the identity; so Galois fixes every component. No resolution required."

---

## 7. The transcendental lattice, and CM

**What it is.** `T(X)` is what is left of the second cohomology after removing `NS` — the orthogonal
complement. Here it has rank 2.

**Why it appears here.** Rank-2 transcendental lattice is the definition of a *singular* K3 surface
(the term means maximal Picard number 20, **not** that the surface is singular as a variety — worth
stating once in the paper to prevent a referee misreading).

**Theorem to the next stage.** `|disc NS| = |disc Triv| / |MW_tors|^2 = 64/16 = 4`, so `T(X)` is even,
positive definite, rank 2, determinant 4. There is exactly one such lattice up to isomorphism,
`diag(2,2)`, because the class number of discriminant `-4` is 1. Its CM field is `Q(sqrt(-4)) = Q(i)`
by the Shioda–Inose classification.

**Standard / contributed.** The classification is standard. The computation of *which* lattice occurs
here is the paper's.

**Say out loud.** "Determinant 4, even, positive definite, rank 2 — that is `diag(2,2)` and nothing
else, so the CM field is `Q(i)`."

---

## 8. The weight-3 modular form

**What it is.** `16.3.c.a = eta^6(4z) = q * prod (1 - q^{4n})^6`. Weight 3, level 16, CM by `Q(i)`.
Its coefficient `a_p` vanishes whenever `p = 3 mod 4` (those primes are inert in `Q(i)`).

**Why it appears here.** Livné's theorem says the transcendental part of a singular K3 over `Q` is
modular of weight 3 — but only *up to a quadratic twist*. So you get the right form only after pinning
the twist down.

**Theorem to the next stage.** Twist elimination. Bad reduction only at `2` forces the twisting
character to have conductor dividing `8`, giving exactly four candidates. CM vanishing collapses them
to two testable hypotheses. One prime — `p = 5`, where the sum is `-6` and the twisted candidate would
give `+6` — eliminates the wrong one. Therefore `Tr(F_p | T(X)) = a_p(16.3.c.a)`, untwisted.

**Standard / contributed.** The form is **not new** and the paper says so repeatedly: it is
Ahlgren–Ono–Penniston's own form, and it also occurs for the quartic Fermat K3. What the paper
contributes is that *this* surface has it, untwisted, and the finite exhaustive argument that fixes
the twist before any number is looked at.

**Say out loud.** "Livné gives modularity up to a quadratic twist. Ramification at 2 leaves four
candidate twists, CM collapses them to two, and one prime decides. The form itself is AOP's — we
claim the surface, not the form."

---

## 9. The final identity

Putting the chain together:

```
Sigma_III(p) = (p-1) a_p(16.3.c.a)   for p = 1 mod 4,        Sigma_III(p) = 0   for p = 3 mod 4.
```

And note the internal consistency check the paper points out: the `p = 3 mod 4` case is proved twice,
once by the elementary involution and once by CM vanishing at inert primes. Two different mechanisms,
same answer. Had they disagreed, something in the geometry would have been wrong.

**Say out loud, as the whole paper in three sentences.** "A combinatorial residue condition produces a
six-fold product of linear forms. Its character sum is the point count of an explicit affine surface,
whose elliptic fibration has three `I_2^*` fibers; the trivial lattice already has rank 20, so the
Picard number is maximal and Mordell–Weil is trivial, and a short graph-rigidity argument shows every
fiber component is rational. That pins the transcendental lattice to `diag(2,2)`, hence CM by `Q(i)`,
and Livné plus a finite twist elimination identifies the trace with the weight-3 CM newform
`eta^6(4z)` — giving a closed form for the sum at every odd prime."

---

## What you should be ready for

The two questions most likely to come first:

1. *"Is your surface just Ahlgren–Ono–Penniston's `lambda = 8` surface?"* — No, and you can show it in
   one line: for every `p = 3 mod 4` your `T(p) = 0` while their `A(8,p) = -p`. Different point counts
   at a prime of good reduction means the surfaces are not isomorphic over `Q`.
2. *"Is the Picard lattice really saturated?"* — Yes, and that is exactly what the torsion computation
   is for: `NS/Triv` is the torsion of Mordell–Weil, which the paper proves is all of `(Z/2)^2`, giving
   the index-squared divisor `16` in `64/16 = 4`.

---

# BEFORE I SUBMIT, I SHOULD BE ABLE TO EXPLAIN

Short, rigorous answers. If any box is unticked, that is the one a referee will find.

- [ ] **What exactly is the Class III sum?** `Σ_III(p) = Σ_{x∈F_p³} χ(x₀x₁x₂(x₀+x₂)(x₁+x₂)(x₀+x₁+x₂))`,
      `χ` the Legendre symbol. Six linear forms, three variables, one integer per prime.
- [ ] **Why does it become a surface point count?** Because `#{y : y² = c} = 1 + χ(c)`, valid at `c = 0`
      too. Summing that identity turns a character sum into a point count, here of
      `Y² = X(X+1)T(T+1)(X+T+1)`, with `T(p) = #V_III(F_p) − p²`.
- [ ] **What makes the surface K3?** The smooth projective model of that affine surface has trivial
      canonical bundle and `h¹(O) = 0`. Concretely, it is the elliptic surface attached to the
      Weierstrass model whose fiber degrees sum to Euler number 24 — the K3 condition for an elliptic
      surface over `P¹`.
- [ ] **What is an elliptic fibration?** A map to `P¹` whose general fiber is a genus-1 curve with a
      marked point. Here: fix `T`, and the equation in `(X,Y)` is a cubic.
- [ ] **What does `I_2*` mean?** A Kodaira fiber type: seven components, arranged as a three-vertex
      spine of multiplicity 2 with two multiplicity-1 legs at each end; Euler number 8; root lattice
      `D_6`. Tate's criterion identifies it by `v(c₄) ≥ 2`, `v(c₆) ≥ 3`, `v(Δ) = n + 6` with `n = 2`.
- [ ] **Why do three such fibers already force Picard number 20?** Each contributes `D_6`, rank 6, so
      with the general fiber and zero section the trivial lattice has rank `2 + 18 = 20`. A complex K3
      has Picard number at most 20. A rank-20 sublattice therefore *is* everything.
- [ ] **What is the Mordell–Weil group?** The group of sections of the fibration, equivalently the
      rational points of the generic fiber over `Q(T)` (or `Q̄(T)`).
- [ ] **Why does MW rank become zero?** Shioda–Tate says `ρ = rank Triv + rank MW`. With `ρ = 20` and
      `rank Triv = 20`, the rank of MW is 0. Forced, not assumed.
- [ ] **What is the Néron–Severi lattice?** The group of divisor classes with the intersection form —
      the algebraic part of `H²`.
- [ ] **What does saturation mean?** That you have `NS` itself, not a finite-index sublattice. `Triv` sits
      inside `NS` with index equal to the order of the Mordell–Weil torsion; if you compute the
      discriminant of `Triv` and forget the index, you get the wrong answer by the square of it.
- [ ] **Why is its discriminant 4?** `|disc Triv| = |disc U| · |disc D_6|³ = 1 · 4³ = 64`, and the index
      is `#MW_tors = 4`, so `|disc NS| = 64/4² = 4`. The step that makes this legitimate is *torsion
      completeness* — proving the torsion is all of `(Z/2)²`.
- [ ] **What is the transcendental lattice?** `T(X) = NS(X)^⊥` inside `H²(X,Z)`. Since `H²` is unimodular
      of rank 22 and `ρ = 20`, it has rank 2 and `|disc T| = |disc NS| = 4`.
- [ ] **Why is it `diag(2,2)`?** It is even, positive definite, rank 2, determinant 4, and there is
      exactly one such lattice up to isometry — equivalently, the class number of binary quadratic
      forms of discriminant `−4` is one.
- [ ] **What does "singular K3" mean?** Maximal geometric Picard number, 20. **Not** a surface with
      singular points — `X_III` is smooth projective. (The affine model `V_III` *is* singular; that is
      why the terminology needs stating once.)
- [ ] **Why does this lattice imply CM by `Q(i)`?** By the Shioda–Inose classification a singular K3
      corresponds to its transcendental lattice, a positive-definite even binary form, and the CM field
      is the imaginary quadratic field of that form's discriminant. Discriminant `−4` gives `Q(i)`.
- [ ] **What is a weight-3 modular form?** A holomorphic function on the upper half plane transforming
      by `(cz+d)³` under a congruence subgroup, with a `q`-expansion. "CM by `Q(i)`" means its
      coefficients come from a Hecke character of `Q(i)`, which forces `a_p = 0` at primes inert in
      `Q(i)`, i.e. `p ≡ 3 mod 4`.
- [ ] **Why is `η⁶(4z)` relevant?** It is the unique weight-3 newform with CM by `Q(i)`, rational
      eigenvalues and 2-power level — and 2-power level is forced because the surface has good reduction
      at every odd prime. Explicitly `η⁶(4z) = q∏(1−q^{4n})⁶`.
- [ ] **What does Frobenius trace mean here?** Frobenius acts on `H²` of the reduction, preserving the
      splitting into `NS` and `T`. Its trace on the rank-2 piece `T` is a single integer per prime, and
      that integer is what the character sum computes.
- [ ] **What does Livné's theorem accomplish?** It says that rank-2 piece is modular: its Frobenius
      traces are the Hecke eigenvalues of a weight-3 CM newform — **up to a quadratic twist**, and a
      priori only at almost all good primes. Both gaps then have to be closed: the twist by an
      exhaustive four-candidate argument, the exceptional set by Chebotarev.
- [ ] **What did AOP prove?** They computed zeta functions for their own one-parameter family of K3
      surfaces and evaluated the associated two-variable character sums by a direct Jacobi-sum
      computation; `η⁶(4z)` is the form they attach to their surface at `λ = 8`.
- [ ] **What exactly does this paper add beyond AOP?** This surface — not a member of their family, with
      a different Weierstrass model, a different fiber configuration, and different point counts at
      every `p ≡ 3 mod 4`, so not isomorphic to theirs over `Q`. Its lattice data. The
      fiber-rationality technique that avoids resolving any fiber. And the closed evaluation of
      `Σ_III`. Not the modular form, and not any general theorem.
- [ ] **What is the weakest point of my paper?** Honest answer: the `Q` versus `Q̄` distinction in the
      non-isomorphism claim, and the "almost all primes" to "every odd prime" upgrade after Livné. Both
      are addressed in `PAPER3_MAC_REVISION_PACKET.md` as REQUIRED 2 and REQUIRED 3.

---

# The two subtle corrections, explained

These are the two places where the manuscript said slightly more than it had proved. Neither is a hole
in the mathematics; both are about saying the right thing. Understand these before defending the paper,
because they are the two questions a good referee asks first.

## Why "over `Q`" matters

A surface can be *the same shape* and yet *a different object arithmetically.* Take the two surfaces at
issue: yours, `X_III`, and Ahlgren–Ono–Penniston's at `λ = 8`. Both are singular K3 surfaces whose
transcendental lattice has discriminant 4 — and by the Shioda–Inose correspondence a singular K3 over
`C` is determined up to isomorphism by that lattice. So over `Q̄` they are very probably the *same*
surface.

What differs is the `Q`-structure. Two varieties over `Q` that become isomorphic over `Q̄` are called
**forms**, or twists, of each other: the same geometry, glued to the rationals differently. The
difference shows up in Frobenius. If two surfaces over `Q` really were isomorphic over `Q`, then
reducing mod any prime of good reduction would give isomorphic surfaces over `F_p`, so they would have
*the same number of `F_p`-points.* Yours and theirs do not: at every `p ≡ 3 mod 4` your two-variable sum
`T(p)` is `0` while theirs is `−p`. Different point counts at a good prime, so no isomorphism over `Q`.

But that argument says nothing about `Q̄`, because a `Q̄`-isomorphism need not be defined over `Q` — and
here the lattice invariants positively suggest a `Q̄`-isomorphism does exist. So the honest claim is:
**not isomorphic over `Q`; probably isomorphic over `Q̄`; and the paper should say the first and not
imply the second.** That is actually a more interesting statement than a flat "different surfaces": you
have found a distinct rational model of a known geometric object, arising from a completely different
character sum.

The analogy worth holding on to: `y² = x³ − x` and `y² = −x³ + x` are different elliptic curves over
`Q` — different point counts, different `L`-functions — but they become isomorphic over `Q(i)`. Same
shape, different arithmetic.

## Why "almost all primes" becomes "all unramified primes"

Livné's theorem hands you a comparison of two objects: Frobenius acting on your surface's transcendental
lattice, and the Hecke eigenvalues of a weight-3 modular form. It says the traces agree **for almost all
primes of good reduction** — i.e. all but finitely many, with no control over which.

That "almost" is unsatisfying, and it is also removable, for a reason worth internalising. Both objects
are really the same *kind* of thing: a 2-dimensional representation of the Galois group, i.e. a rule
assigning a 2×2 matrix to each Frobenius element. The traces of those matrices are the numbers being
compared.

Now, two facts. First, **Brauer–Nesbitt**: a semisimple representation is determined, up to isomorphism,
by its character — the traces know everything. Second, **Chebotarev density**: the Frobenius elements at
primes in any density-one set are dense enough in the Galois group to pin down a continuous function on
it. Put them together: if the traces agree at a set of primes of density 1, then the two
representations are *isomorphic*, not merely numerically close. And isomorphic representations have
equal traces at **every** prime where both are unramified — no exceptions left, because there is now
literally one representation, described twice.

The last step is bookkeeping, and your paper already has it: your surface has good reduction at every
odd prime, and the modular form has level a power of 2, so both are unramified at every odd prime. Hence
the identity holds at every odd prime, full stop. The finitely many exceptions Livné allowed are ruled
out not by checking them, but by upgrading the statement from "these numbers agree often" to "these are
the same object".

**The moral of both corrections is the same.** In each case the manuscript had the right theorem and
described it slightly too loosely — once by omitting a field, once by inheriting an "almost all" it did
not need to keep. Fixing them makes the paper stronger, not weaker: the first turns a numerical remark
into a proof, and the second removes an exceptional set entirely.
