# PAPER 3 — PUBLICATION REVISION STATUS

| Field | Value |
|---|---|
| Title | Class III Hypercuboid Character Sums and a Discriminant-4 Singular K3 Surface |
| Source | `class_iii/manuscript/class3_hypercuboid_k3.tex` (1887 lines + 13 added in `b8e6cff`) |
| PDF SHA-256 | `ba37532b68873b903fe692ff745cd06131395ad61103a27cd2aa9aca2f9d9eb7` (unchanged) |
| Zenodo | `10.5281/zenodo.22713447` |
| Paper date | 2026-09-11 |
| Repository commit | `b8e6cff` on `paper3-publication-readiness` (PR #3, open, mergeable) |
| Readiness classification | **B** — citation and exposition revision, plus three factual/rigour fixes |
| Build status | **NOT YET BUILT ON THIS MACHINE** |
| Reason | No TeX installation (no `pdflatex`, `xelatex`, `lualatex`, `latexmk`, `tectonic`, `bibtex`, `biber`, no texmf tree) |

> **This document prepares changes only. The authoritative TeX and PDF remain untouched until the Mac
> compilation phase.**

One exception, already committed and already on this branch: commit `b8e6cff` added the Paper 1
citation to the `.tex` (a new `\bibitem{Collapse2026}` appended after `\bibitem{Huber}`, plus one
in-text `\cite{Collapse2026}` in §2.1). **Patch 0 below is therefore already applied — do not apply it
twice.** No other `.tex` change has been made, and the PDF has not been touched.

Counts: **4 REQUIRED**, **5 STRONGLY RECOMMENDED**, **4 OPTIONAL POLISH**.

---

# The central mathematical claim

```
Sigma_III(p) = sum_{x in F_p^3} chi( x0 x1 x2 (x0+x2)(x1+x2)(x0+x1+x2) )
   │  projective reduction (degree-6 homogeneity)                      [technique standard]
   ▼
= (p-1) T(p),   T(p) = sum_{x,t} chi( x t(t+1)(x+t)(x+t+1) )
   │  1 + chi(c) point-count identity                                  [standard]
   ▼
T(p) = #V_III(F_p) - p^2,   V_III : Y^2 = X(X+1)T(T+1)(X+T+1)
   │  complete the cube, scale by u = T(T+1)                           [paper-local]
   ▼
Y^2 = X^3 + T(T+1)(T+2)X^2 + T^2(T+1)^3 X,   Delta = 16 T^8 (T+1)^8
   │  Tate's algorithm                                                 [imported: Tate, Kodaira, Neron]
   ▼
three I_2^* fibers at T = 0, -1, infinity; no others; minimal
   │  Shioda-Tate + the K3 bound rho <= 20                             [imported: Shioda]
   ▼
rank Triv = 2 + 3*6 = 20  =>  rho = 20 AND rank MW = 0, both FORCED
   │  full rational 2-torsion + GRAPH RIGIDITY                         [PAPER-LOCAL, the contribution]
   ▼
every component of every reducible fiber is defined over Q  =>  Tr(F_p | NS) = 20p
   │  component-group index / torsion completeness
   ▼
|disc NS| = 4^3 / |(Z/2)^2|^2 = 64/16 = 4
   │  singular-K3 lattice classification                               [imported: Shioda-Inose]
   ▼
T(X_III) = diag(2,2)  (unique class, disc -4 has class number 1)  =>  CM by Q(i)
   │  Livne + twist elimination + Chebotarev (see REQUIRED 3)          [imported + paper-local]
   ▼
Tr(F_p | T(X_III)) = a_p(f),   f = eta^6(4z) = 16.3.c.a               [form NOT new: AOP]
   │  point-count ledger                                               [paper-local]
   ▼
Sigma_III(p) = (p-1) a_p(eta^6(4z))  for p = 1 mod 4;  = 0 for p = 3 mod 4
```

**Standard / imported:** the `1+chi(c)` identity; Kodaira's fiber classification and Tate's algorithm;
Shioda–Tate; the K3 Lefschetz bound `rho <= 20`; the Shioda–Inose singular-K3 correspondence; Livné's
modularity theorem; the classification of rank-2 even positive-definite lattices; the newform
`eta^6(4z)` itself and its CM by `Q(i)`.

**Genuinely contributed by Paper 3:** the specific reduction of `Sigma_III` and its surface; the
Weierstrass model and its fiber configuration; **the graph-rigidity proof of component rationality
without resolving any fiber** (the technical novelty); the torsion-completeness step that makes the
discriminant computation a statement about `NS` rather than a sublattice; the exhaustive twist
elimination; the point-count ledger; and the resulting closed evaluation of `Sigma_III`.

---

# REQUIRED BEFORE SUBMISSION

## REQUIRED 1 — the `S_4` orbit count is wrong

**Location.** §2.1 "Hypercuboid origin", source lines 138–142.

**CURRENT TEXT** (lines 138–142, verbatim):

```
A_4=-(x_0+x_1+x_2)$. The natural $S_4$-symmetry permuting $A_1,\dots,A_4$
acts on the seven six-element subsets of these seven forms with exactly
three orbits, giving the three character-sum classes $\Sigma_I,\Sigma_{II},
\Sigma_{III}$. Classes I and II each omit a form associated to a
\emph{singleton}-type element of the permutation action; Class~III omits
```

**Why it is wrong.** The seven forms correspond to the seven complement-pairs of `{1,2,3,4}`: four of
shape `(1,3)` and three of shape `(2,2)`. `S_4` is transitive on each. So there are **two** orbits, of
sizes **4 and 3** — verified by direct enumeration over all 24 permutations. The sentence is also
internally inconsistent with the one immediately after it, which says Classes I and II *both* omit
singleton-type forms — i.e. both lie in the same orbit, so they cannot be two separate orbits.

**PROPOSED REPLACEMENT** (matching the manuscript's style):

```
A_4=-(x_0+x_1+x_2)$. The natural $S_4$-symmetry permuting $A_1,\dots,A_4$
acts on the seven six-element subsets of these seven forms with two
orbits, of sizes four and three, according to whether the omitted form
corresponds to a $(1,3)$- or a $(2,2)$-shaped complement pair. The
size-four orbit splits further, $3+1$, according to whether the omitted
representative involves the eliminated coordinate $A_4$; crossing that
split multiplies the sum by $\chi(-1)$, which is the Gateway relation
$\Sigma_{II}(p)=\chi(-1)\Sigma_I(p)$ of \cite{ClassesI_II}. This yields
the three character-sum classes $\Sigma_I,\Sigma_{II},\Sigma_{III}$.
Classes I and II each omit a form associated to a \emph{singleton}-type
element of the permutation action; Class~III omits
```

**Adjacent wording to check after the edit.** The sentence that follows ends "...a genuinely different
orbit, with no permutation relating Class III to Classes I or II." That remains **true and becomes
sharper** under the correction — Class III is the `(2,2)` orbit, genuinely separate — so leave it. But
note it is now the only place asserting orbit-separateness, so it carries more weight; consider
appending "(the $(2,2)$ orbit above)" for clarity. OPTIONAL.

> **No downstream theorem or computation changes.** `Sigma_III` is defined by an explicit formula in
> Definition 2.2, and every later result concerns it alone.

## REQUIRED 2 — the non-isomorphism argument should be a proof, not a prime count

**Location.** §"Comparison with Classes I/II" / the AOP-precise discussion, source lines 1213–1216.

**CURRENT TEXT** (verbatim):

```
\cite{AOP2002}'s own surface at $\lambda=8$ has a different Weierstrass
model and fiber configuration from $X_{\rm III}$, and the two are provably
non-isomorphic (the two-variable sums $T(p)$ and $A(8,p)$ disagree at
essentially every tested prime); possibilities (iii) and (vi) do not
apply.
```

**Why change it.** "Disagree at essentially every tested prime" is a numerical observation supporting
the word "provably", and "essentially every" invites the question of which primes it fails at. A
structural proof is available and needs no table.

**The argument, in the manuscript's own notation.** AOP define
`A(\lambda,q) = \chi(\lambda+1)\bigl(a(\lambda,q)^2 - q\bigr)` with
`a(\lambda,q) = -\sum_{x}\chi\bigl((x-1)(x^2 - 1/(\lambda+1))\bigr)`. At `\lambda = 8` one has
`\lambda+1 = 9`, so `\chi(9) = 1` for every odd `p` and `A(8,p) = a(8,p)^2 - p`. For `p \equiv 3 \pmod 4`
the inner sum vanishes, `a(8,p) = 0`, hence

```
A(8,p) = -p     for every p = 3 mod 4,
```

whereas Proposition (elementary mod-4 vanishing) gives `T(p) = 0` for exactly those `p`. Since
`-p \neq 0`, the two two-variable character sums differ at **every** prime `p \equiv 3 \pmod 4` — with
no computation at all. Verified numerically as well: `T(p) \neq A(8,p)` at all 14 primes tested in
`[5,61]`.

**PROPOSED REPLACEMENT:**

```
\cite{AOP2002}'s own surface at $\lambda=8$ has a different Weierstrass
model and fiber configuration from $X_{\rm III}$, and the two are
non-isomorphic over $\Q$ for a structural reason requiring no numerical
search. Since $\lambda+1=9$ is a square, $\chi(9)=1$ for every odd $p$
and \cite{AOP2002}'s evaluation reads $A(8,p)=a(8,p)^2-p$; at
$p\equiv3\pmod4$ the inner sum $a(8,p)$ vanishes, so $A(8,p)=-p\neq0$,
while $T(p)=0$ for exactly those $p$ by
Proposition~\ref{prop:involution}. The two affine surfaces therefore have
different numbers of $\Fp$-points at every prime $p\equiv3\pmod4$, all of
which are primes of good reduction for both; hence no isomorphism over
$\Q$ can exist, and a fortiori none as elliptic surfaces over $\Q(T)$.
Possibilities (iii) and (vi) do not apply.
```

**Citations needed.** None new; `\cite{AOP2002}` and `\ref{prop:involution}` already exist.

**Theorem numbering / cross-references.** Unchanged. One new `\ref` to an existing label.

## REQUIRED 3 — bridge Livné's "almost all primes" to "every odd prime"

**Location.** Between the Livné theorem (source ~line 848–859) and Theorem (Exact transcendental
trace) (source ~line 1014).

**The gap.** The manuscript's own statement of Livné's theorem concludes
`\Tr(\mathrm{Frob}_p \mid T(X)) = a_p(f)` **"for almost all primes `p` of good reduction"**. The
paper's Theorem (Exact transcendental trace) then asserts the equality **"for every odd prime
`p \neq 2`"**. Nothing in the manuscript bridges the two: searching the source for `Chebotarev`,
`semisimple`, `isomorphic as representations` and `Brauer` returns **no match**. A referee who knows
modular Galois representations will notice this on first reading.

**Why it is only an expositional gap.** The upgrade is standard and two sentences long. Both sides are
traces of 2-dimensional semisimple `\ell`-adic representations of `\mathrm{Gal}(\overline\Q/\Q)`
unramified outside `\{2\}` — for the surface because §"Bad primes" establishes good reduction at every
odd prime, for the newform because it has level a power of 2. Two semisimple representations whose
traces agree at a set of primes of density 1 are isomorphic (Chebotarev density together with
Brauer–Nesbitt), and isomorphic representations have equal traces at **every** unramified prime.

**PROPOSED ADDITION** — insert immediately after the "Hypothesis check for `X_III`" paragraph:

```
\begin{remark}[From ``almost all'' to every odd prime]
\label{rem:chebotarev}
Theorem~\ref{thm:livne} yields the trace identity only for almost all
primes of good reduction, whereas Theorem~\ref{thm:trans-trace} asserts it
for every odd $p$. The upgrade is standard. Both
$\rho_T:=\mathrm{Gal}(\overline\Q/\Q)\to\mathrm{GL}(T(X_{\rm
III})\otimes\Q_\ell)$ and the representation $\rho_f$ attached to $f$ are
$2$-dimensional and semisimple, and both are unramified outside $\{2\}$:
for $\rho_T$ because $X_{\rm III}$ has good reduction at every odd prime
(Section~\ref{sec:badprimes}), and for $\rho_f$ because $f$ has $2$-power
level. Two semisimple $\ell$-adic representations whose traces agree on a
set of primes of density $1$ are isomorphic, by Chebotarev density
together with the Brauer--Nesbitt theorem; isomorphic representations have
equal Frobenius traces at every unramified prime. Hence the identity holds
at every odd $p$, with no exceptional set.
\end{remark}
```

**Citations needed.** Optional but preferable: a standard reference for Brauer–Nesbitt /
Chebotarev-implies-isomorphism. `\cite{Livne1995}` alone is not the right citation for this step. See
`REFERENCES TO ADD OR MODIFY`.

**Theorem numbering.** Corrected in the final pass: the counter is declared
`\newtheorem{theorem}{Theorem}[section]`, so it **resets at every `\section`**. An insertion in §6
therefore shifts only the remaining items **of §6** — nothing in §7 onward and nothing in the
appendices. Exactly **one** printed number changes: `6.2 → 6.3`, the "Known vs. proved" remark. See
`THEOREM-NUMBER SHIFT MAP` below. (An earlier draft of this packet said the shift propagated "in that
section and beyond"; that was wrong.)

## REQUIRED 4 — build the manuscript

No build has been performed on this machine. See `MAC BUILD AND PDF CHECKLIST`.

---

# STRONGLY RECOMMENDED

## SR 1 — clarify "singular K3 surface" at first use

**Location.** First occurrence in the body is the introduction, source line 52 ("...realized, via an
explicit singular K3 surface, in terms of..."). The abstract uses it earlier still.

**PROPOSED ADDITION** — one sentence, at the first body occurrence:

```
Throughout, ``singular K3 surface'' is used in the standard
arithmetic-geometric sense of a K3 surface whose geometric Picard number
attains the maximum $20$ \cite{ShiodaInose1977}, not of a surface with
singular points; the surfaces $X$ and $X_{\rm III}$ are smooth projective.
```

**Reason.** The term is standard in the singular-K3 literature but actively misleading outside it, and
this paper *also* discusses genuinely singular affine models (`V_III`) and their resolutions — so the
collision is real, not hypothetical.

## SR 2 — present the newform as an eta product first, the label second

**Location.** §"Identifying the candidate newform" (source ~line 871 onwards).

**Reason.** An LMFDB label is a database identifier; `\eta^6(4z)` is a definition a referee can verify
independently. The audit's strongest reproducibility check came from expanding the eta product
directly, and the manuscript should present the object the same way round.

**PROPOSED WORDING:**

```
The relevant candidate is the weight-$3$ newform
\[
f(z)=\eta^6(4z)=q\prod_{n\ge1}(1-q^{4n})^6=\sum_{n\ge1}a_nq^n ,
\]
of level $16$, Nebentypus $\chi_{-1}$, with complex multiplication by
$\Q(i)$; in the LMFDB's labelling this is \texttt{16.3.c.a}. Weight-$3$
newforms with CM by $\Q(i)$ and rational Hecke eigenvalues are classified
by level, and $f$ is the unique such form of $2$-power level. Note that
$f$ is singled out here on structural grounds -- weight, level, Nebentypus
and CM field -- \emph{before} any coefficient is compared with a character
sum.
```

## SR 3 — revised abstract (drop-in replacement, see `PROPOSED REVISED ABSTRACT` below)

## SR 4 — revised introduction opening (see `PROPOSED REVISED INTRODUCTION OPENING` below)

## SR 5 — self-contained Class III definition (see `CLASS III FOR AN OUTSIDE READER` below)

---

# OPTIONAL POLISH

* **OP 1.** In §2.1, append "(the $(2,2)$ orbit above)" to the "genuinely different orbit" sentence
  after REQUIRED 1 lands.
* **OP 2.** Add the birational-K3 sentence (see `THE BIRATIONAL-K3 FACT`) — only if a referee's likely
  reading of "non-isomorphic" needs pre-empting; REQUIRED 2's wording already says "over `\Q`", so this
  is genuinely optional.
* **OP 3.** Reproducibility paragraph (see `ETA-PRODUCT REPRODUCIBILITY NOTE`).
* **OP 4.** Title: see `TITLE CHECK`. Recommendation is to keep the current title.

---

# PROPOSED REVISED ABSTRACT

Drop-in replacement for the `abstract` environment. It is shorter than the current one (which runs to a
single ~450-word paragraph), leads with the geometry, and states the AOP relationship in its own
sentence rather than in a subordinate clause.

```
\begin{abstract}
For an odd prime $p$ let
$\Sigma_{\rm III}(p)=\sum_{x\in\Fp^3}\chi\bigl(x_0x_1x_2(x_0+x_2)(x_1+x_2)(x_0+x_1+x_2)\bigr)$,
where $\chi$ is the Legendre symbol. An elementary projective reduction
gives $\Sigma_{\rm III}(p)=(p-1)T(p)$ for the two-variable sum
$T(p)=\sum_{x,t\in\Fp}\chi\bigl(x\,t(t+1)(x+t)(x+t+1)\bigr)$, and an
explicit coordinate involution gives $\Sigma_{\rm III}(p)=0$ for
$p\equiv3\pmod4$ with no recourse to arithmetic geometry.

For $p\equiv1\pmod4$ we realize $T(p)$ as a Frobenius trace. The affine
surface $Y^2=X(X+1)T(T+1)(X+T+1)$ carrying $T(p)$ has an elliptic
fibration over the $T$-line with exactly three fibers of Kodaira type
$I_2^*$ and full rational $2$-torsion $(\Z/2)^2$ over $\Q(T)$. Its trivial
lattice already has rank $20$, so the associated smooth projective surface
$X_{\rm III}$ has maximal geometric Picard number and trivial Mordell--Weil
rank. We prove that every component of every reducible fiber is
individually defined over $\Q$ by an argument that resolves no fiber:
the zero section and the three nonzero $2$-torsion sections occupy four
pairwise distinct multiplicity-one components, and the only automorphism of
the fiber's incidence graph fixing those four is the identity. This gives
$\Tr(F_p\mid\NS(X_{\rm III}))=20p$ for every odd $p$,
$\disc\NS(X_{\rm III})=4$, and hence
$T(X_{\rm III})\cong\mathrm{diag}(2,2)$ with complex multiplication by
$\Q(i)$.

Livn\'e's modularity theorem, together with a twist elimination that is
exhaustive over a four-element candidate set forced by ramification at $2$,
identifies the transcendental trace with the weight-$3$ CM newform
$f=\eta^6(4z)$ (LMFDB \texttt{16.3.c.a}). Combined with an independently
derived point-count ledger this yields
\[
\Sigma_{\rm III}(p)=(p-1)\,a_p(f)\ \ (p\equiv1\bmod4),\qquad
\Sigma_{\rm III}(p)=0\ \ (p\equiv3\bmod4).
\]
The newform $f$ is not new: it is the form Ahlgren, Ono and Penniston
attach to their own K3 surface at parameter $\lambda=8$, and it also occurs
for the quartic Fermat K3 surface. What is established here is that the
Class~III surface -- which has a different Weierstrass model, a different
fiber configuration, and different point counts at every $p\equiv3\pmod4$,
hence is not isomorphic over $\Q$ to theirs -- carries the same
transcendental representation, untwisted, and that the resulting evaluation
completes the four-coordinate finite-field hypercuboid classification left
open by the companion paper.
\end{abstract}
```

Changes of substance relative to the current abstract: the geometry now leads; "singular K3" is
avoided in the abstract entirely (replaced by "maximal geometric Picard number"); the AOP relationship
is a standalone sentence with the non-isomorphism reason attached; the eta product precedes the label.

---

# PROPOSED REVISED INTRODUCTION OPENING

Replacement for the first three paragraphs of §1 (current source lines 43–58ff, beginning "This paper
is a sequel to..."). The hypercuboid origin is **retained, not erased** — it moves to paragraph four.

```
\section{Introduction}
\label{sec:intro}

Fix an odd prime $p$ and let $\chi$ denote the Legendre symbol modulo $p$.
This paper evaluates the character sum
\[
\Sigma_{\rm III}(p)=\sum_{x\in\Fp^3}
\chi\bigl(x_0x_1x_2(x_0+x_2)(x_1+x_2)(x_0+x_1+x_2)\bigr),
\]
a sum over a product of six linear forms in three variables, in closed form
for every odd $p$. The answer is a Hecke eigenvalue: for $p\equiv1\pmod4$,
$\Sigma_{\rm III}(p)=(p-1)a_p(f)$ with $f=\eta^6(4z)$ the weight-$3$
newform of level $16$ with complex multiplication by $\Q(i)$, and
$\Sigma_{\rm III}(p)=0$ for $p\equiv3\pmod4$.

Sums of this shape -- a quadratic character applied to a product of linear
or quadratic forms -- have been evaluated in closed form when the
underlying variety is recognizably modular. The nearest precedent is
Ahlgren, Ono and Penniston \cite{AOP2002}, who computed the zeta functions
of a one-parameter family of K3 surfaces and, by a direct Jacobi-sum
computation, evaluated the associated two-variable character sums; the
form $\eta^6(4z)$ is the one they attach to their surface at
$\lambda=8$. The sum $\Sigma_{\rm III}$ is not among those they treat,
and is not obtained from theirs by a change of variables: its surface has
a different Weierstrass model and a different fiber configuration, and
already differs in point count at every $p\equiv3\pmod4$
(Section~\ref{sec:AOP-precise}).

Our route is geometric rather than Jacobi-sum-theoretic. After an
elementary projective reduction to a two-variable sum $T(p)$, we exhibit
$T(p)$ as a point count on an explicit affine surface, resolve that
surface into a singular K3 surface $X_{\rm III}$ -- here and throughout,
``singular'' in the standard sense of maximal geometric Picard number
$20$, not of a surface with singular points -- and compute its Picard and
transcendental lattices directly. The computation is unusually clean: three
$I_2^*$ fibers make the trivial lattice already of rank $20$, which forces
both maximal Picard number and trivial Mordell--Weil rank, and full
rational $2$-torsion plus a rigidity property of the fiber's incidence
graph forces every fiber component to be individually rational without
resolving any fiber. The transcendental lattice is then pinned to
$\mathrm{diag}(2,2)$, its CM field to $\Q(i)$, and -- via Livn\'e's
theorem and a finite, exhaustive twist elimination -- the Frobenius trace
to $a_p(f)$.

The sum $\Sigma_{\rm III}$ arises from a combinatorial question, and that
is how we came to it. [Existing hypercuboid paragraph follows here,
beginning ``This paper is a sequel to \emph{Finite-Field Hypercuboid
Character Sums\ldots}'' and continuing unchanged.]
```

**Note on `\ref{sec:AOP-precise}`.** Confirm that label exists; the audit found the section referred to
in prose as the AOP-precise discussion. If the label differs, adjust.

---

# CLASS III FOR AN OUTSIDE READER

Self-contained paragraph, for §2 immediately before or after Definition 2.2. A referee should not need
Papers 1 or 2.

```
For the reader coming to this sum directly: the seven forms
$L_J(x)=\sum_{j\in J}x_j$, indexed by the nonempty subsets
$J\subseteq\{1,2,3\}$, are exactly the nontrivial subset sums of the four
quantities $A_1=x_0$, $A_2=x_1$, $A_3=x_2$, $A_4=-(x_0+x_1+x_2)$, which sum
to zero; each such subset sum equals, up to sign, the sum over the
complementary subset, so the fourteen nontrivial subset sums of
$\{A_1,\dots,A_4\}$ reduce to these seven forms. Deleting one of the seven
and taking the quadratic character of the product of the remaining six
gives a character sum; up to the $S_4$-action permuting $A_1,\dots,A_4$
there are three such sums, and $\Sigma_{\rm III}$ is the one obtained by
deleting the form $L_{\{1,2\}}=x_0+x_1$, whose complement pair has shape
$(2,2)$. In conventional terms, $\Sigma_{\rm III}(p)$ is a quadratic
character sum over the complement of an arrangement of six hyperplanes in
$\mathbb{A}^3$, and no property of the combinatorial origin is used
anywhere in this paper beyond fixing which six forms appear.
```

---

# TRANSLATING THE BESPOKE TERMINOLOGY

First-use clarifications. None of the terms is removed; each is given its conventional reading
immediately.

| Term | First-use clarification to insert |
|---|---|
| **hypercuboid** | "The term \emph{hypercuboid} refers to the combinatorial origin of the constraint system (all subset sums of $n$ quantities required to be quadratic residues) and carries no geometric content in this paper." |
| **gateway** | Does **not** occur in Paper 3 (checked: zero occurrences). It is Paper 2's term. Nothing to do; do not introduce it. |
| **zero sector** / **$D_{\rm full}=0$** | "the \emph{zero sector}, i.e. the locus $\sum_iA_i=0$" — give the equation at first use. |
| **complement collapse** | "the \emph{complement collapse}: since $\sum_iA_i=0$ forces $D_{I^c}=-D_I$, each subset-sum condition is equivalent to its complement's precisely when $\chi(-1)=1$, so the $2^n-2$ conditions reduce to $2^{n-1}-1$ (\cite{Collapse2026}, Theorem 3.1)." |
| **Class III** | Covered by the self-contained paragraph above. |

---

# THE BIRATIONAL-K3 FACT

**Standard theorem.** Birationally equivalent smooth projective K3 surfaces are isomorphic. The reason
is that a K3 surface is minimal with trivial canonical class, so it is the unique smooth minimal model
in its birational class; for surfaces, a birational map between minimal models with nef canonical
divisor is an isomorphism.

**Status here.** REQUIRED 2's wording says "non-isomorphic over `\Q`", and the point-count argument
rules out isomorphism directly, so this fact is **not needed** for the proof. It is worth one clause
only if the manuscript wants to also exclude birational equivalence (which the current text does
mention). Suggested clause, if used:

```
(For K3 surfaces birational equivalence implies isomorphism, since a K3 is
its own unique smooth minimal model, so ruling out an isomorphism rules out
a birational map as well.)
```

**Citation.** No source currently in `references.bib` states this. It is textbook — Barth–Hulek–Peters–Van
de Ven, *Compact Complex Surfaces*, or Huybrechts, *Lectures on K3 Surfaces*, Ch. 1. **Neither is in the
repository bibliography**; adding one is a single entry and is listed below. If the clause is dropped,
no citation is needed. `VERIFY ON MAC/WEB` for the exact chapter/theorem number.

---

# EXACT RELATION TO AHLGREN–ONO–PENNISTON

Prepared as a section the manuscript can adopt more or less verbatim; the current text already says
most of this, and the only substantive change is REQUIRED 2.

**What AOP proved.** For their one-parameter family of K3 surfaces `X_\lambda`, they computed the zeta
functions and evaluated the associated two-variable character sums, obtaining
`A(\lambda,q)=\chi(\lambda+1)(a(\lambda,q)^2-q)` where `a(\lambda,q)` is an explicit one-variable
character sum. Their method is a direct Jacobi-sum computation. Their Theorem 1.2 identifies
`\eta^6(4z)` as the newform governing their surface at `\lambda = 8`.

**Which modular form is theirs.** `\eta^6(4z)` — entirely. Paper 3 claims **no** novelty for the form,
for its `q`-expansion, for its CM by `Q(i)`, or for its occurrence as a K3 trace form. It occurs
independently for the quartic Fermat K3 surface as well (`\cite{Huber}`).

**What Paper 3 addresses.** The surface `X_{\rm III}` produced by the Class III reduction — not a member
of AOP's family, with its own Weierstrass model, its own fiber configuration (three `I_2^*`), and its own
point counts. Paper 3 determines its Picard and transcendental lattices by a route AOP do not use, and
derives the closed evaluation of `\Sigma_{\rm III}`.

**What Paper 3 does not claim.** Not the modular form; not a new general theorem about K3 surfaces or
modular forms; not any consequence for the integer perfect-hypercuboid problem; and not that AOP
overlooked anything — their family simply does not contain this surface.

**Why the routes differ.** AOP evaluate a Jacobi sum and read off the zeta function. Paper 3 computes a
Picard lattice via Shioda–Tate, establishes component rationality by graph rigidity, obtains the
transcendental lattice from the discriminant, and invokes Livné. The two proofs share the *statement*
and nothing else: no Jacobi sum appears in Paper 3, and no lattice appears in AOP's derivation.

## Why the Class III case is not covered by AOP

Their parameter `\lambda` indexes their family; `\Sigma_{\rm III}` is not one of their sums, and the
surface carrying `T(p)` is not one of their `X_\lambda`. The decisive check is the one in REQUIRED 2:
`A(8,p) = -p` while `T(p) = 0` for every `p \equiv 3 \pmod 4`, so the two two-variable sums are not
equal and the surfaces are not isomorphic over `\Q`. Sharing the same *transcendental representation*
is compatible with this — two non-isomorphic singular K3 surfaces can have isometric transcendental
lattices, and here they do.

**Precision note.** The objects must not be conflated. `T(p)` and `A(8,p)` are **character sums**, equal
to affine **point counts** minus `p^2`. `\Tr(F_p \mid T(X))` is a **trace** on a rank-2 lattice.
`a_p(f)` is a **Fourier coefficient**. The chain relates them, but the non-isomorphism argument is about
the first pair only — point counts at good primes — which is exactly why it yields non-isomorphism.

## What one good prime proves

Precisely this: if two smooth projective surfaces over `\Q` are isomorphic over `\Q`, then for every
prime of good reduction for both the reductions are isomorphic over `\F_p`, hence have equal
`\F_p`-point counts. A single good prime with different counts therefore rules out isomorphism **over
`\Q`**. It does **not** by itself rule out isomorphism over `\overline\Q`, since a `\overline\Q`-isomorphism
need not descend. Do not overstate.

Geometric (`\overline\Q`) non-isomorphism, if wanted, would need a different invariant — and here the
lattice invariants do **not** supply it: both surfaces are singular K3 surfaces with transcendental
lattice of discriminant 4, and by the Shioda–Inose correspondence a singular K3 over `\overline\Q` is
determined up to isomorphism by its transcendental lattice, so if both have `T \cong \mathrm{diag}(2,2)`
they **are** isomorphic over `\overline\Q`. **The honest statement is therefore: the surfaces are
non-isomorphic over `\Q` but plausibly isomorphic over `\overline\Q`, and the paper should say exactly
that.** This is a real precision issue in the current wording, which says "provably non-isomorphic"
without a field. Fold this into REQUIRED 2: the replacement text above says "non-isomorphic over `\Q`",
and one further clause should be added:

```
Over $\overline\Q$ the two surfaces are not distinguished by their
transcendental lattices, both of discriminant $4$; the distinction claimed
here is over $\Q$, where the point counts differ.
```

This is the single most important wording change in the packet after REQUIRED 1: it converts a claim
that a referee could call false into one that is provably true.

---

# POLISHED EXPOSITIONS (ready to drop in)

## `rho = 20` and Mordell–Weil rank 0

```
The three $I_2^*$ fibers contribute root lattices $D_6$, of rank $6$ each,
and together with the class of a general fiber and the zero section they
span the trivial lattice
$\Triv(X_{\rm III})=U\oplus D_6\oplus D_6\oplus D_6$, of rank
$2+6+6+6=20$. Since the geometric Picard number of any complex K3 surface
is at most $20$ (Lefschetz $(1,1)$), and since
$\Triv(X_{\rm III})\subseteq\NS(X_{\rm III})$ already has rank $20$, we get
$\rho(X_{\rm III})=20$; and then Shioda--Tate,
$\rho=\rk\Triv+\rk MW$, forces $\rk MW(X_{\rm III}/\overline\Q(T))=0$.
Both conclusions are forced, neither assumed.
```

## `NS` saturation and `disc NS = 4`

```
It matters that we compute the discriminant of $\NS(X_{\rm III})$ itself
and not of a proper sublattice. With Mordell--Weil rank $0$, Shioda--Tate
identifies the quotient $\NS(X_{\rm III})/\Triv(X_{\rm III})$ with the
torsion subgroup $MW(X_{\rm III}/\Q(T))_{\rm tors}$, so
$[\NS:\Triv]=\#MW_{\rm tors}$ and
\[
|\disc\NS(X_{\rm III})|
=\frac{|\disc\Triv(X_{\rm III})|}{(\#MW_{\rm tors})^2}
=\frac{1\cdot4^3}{4^2}=4 .
\]
This is legitimate exactly because Proposition~\ref{prop:torsion-complete}
proves the torsion is \emph{all} of $(\Z/2)^2$ -- not merely that it
contains the three visible $2$-torsion sections. Without that
completeness the index, and hence the discriminant, would be only an upper
bound, and $T(X_{\rm III})$ would not be pinned down.
```

## The transcendental lattice

```
In the unimodular K3 lattice $H^2(X,\Z)$ the transcendental lattice
$T(X_{\rm III})=\NS(X_{\rm III})^\perp$ therefore has rank
$22-20=2$, is even, positive definite, and satisfies
$|\disc T(X_{\rm III})|=|\disc\NS(X_{\rm III})|=4$. Up to isometry there is
exactly one such lattice: a Gram matrix $\begin{pmatrix}2a&b\\b&2c\end{pmatrix}$
with $4ac-b^2=4$ is, after reduction, $\mathrm{diag}(2,2)$ -- equivalently,
the class number of binary quadratic forms of discriminant $-4$ is one.
Hence $T(X_{\rm III})\cong\mathrm{diag}(2,2)$, with no competing class.
```

## CM by `Q(i)`

```
By the Shioda--Inose classification \cite{ShiodaInose1977}, a singular K3
surface corresponds to its transcendental lattice, a positive-definite even
binary form, and the associated CM field is the imaginary quadratic field
of that form's discriminant. Here the discriminant is $-4$, so the field is
$\Q(\sqrt{-4})=\Q(i)$. This is a consequence of the classification, not an
observed numerical coincidence: the field is read off the lattice before
any Frobenius trace is computed.
```

## Graph rigidity — MAIN-TEXT VERSION

```
The dual graph of an $I_2^*$ fiber is a tree on seven vertices: a spine
$S_1-S_2-S_3$ of multiplicity-two components with two multiplicity-one
legs attached at each end, $L_1,L_2$ at $S_1$ and $L_3,L_4$ at $S_3$.
Galois acts on the fiber's components through an automorphism of this
graph preserving multiplicities. The zero section and the three nonzero
rational $2$-torsion sections meet four \emph{pairwise distinct}
multiplicity-one components (Lemma~\ref{lem:four-legs}), so those four
legs are individually Galois-fixed. But a tree automorphism fixing all
four legs is the identity: each leg is a leaf with a unique neighbor, so
fixing $L_1$ fixes $S_1$ and fixing $L_3$ fixes $S_3$, and $S_2$ is the
unique vertex adjacent to both. Hence Galois fixes all seven components,
and every component of the fiber is defined over $\Q$. Applying this at
each of the three $I_2^*$ fibers gives
$\Tr(F_p\mid\NS(X_{\rm III}))=20p$ for every odd $p$. No fiber is resolved
explicitly at any point in the argument.
```

## Graph rigidity — APPENDIX VERSION

Keep the manuscript's existing Appendix E material (Lemma "Graph rigidity" plus the remark recording
the exhaustive `7! = 5040` check and the order-8 automorphism group), with one addition: state that the
enumeration is a **check on** the lemma, not its proof. The manuscript already says exactly this in bold
— preserve that sentence verbatim; it is the right discipline and a referee will notice it favourably.

## Livné, for a referee who has not followed this project

```
Livn\'e's theorem provides modularity for the transcendental part of a
singular K3 surface over $\Q$: the Galois representation on
$T(X)\otimes\Q_\ell$ is $2$-dimensional, and its Frobenius traces are the
Hecke eigenvalues of a weight-$3$ newform with CM by the quadratic field
attached to $T(X)$ -- but only up to a quadratic twist, and a priori only
at almost all good primes. Three further steps close the gap. (i) The
level is constrained: $X_{\rm III}$ has good reduction at every odd prime
(Section~\ref{sec:badprimes}), so the representation is unramified outside
$\{2\}$ and the newform has $2$-power level; the unique weight-$3$ newform
with CM by $\Q(i)$, rational eigenvalues and $2$-power level is
$f=\eta^6(4z)$. (ii) The twist is pinned down: a quadratic twist of a form
unramified outside $\{2\}$ must be by a character of conductor dividing
$8$, giving exactly four candidates
$\{1,\chi_{-1},\chi_{2},\chi_{-2}\}$; CM vanishing at inert primes
collapses these to two testable hypotheses, and one prime distinguishes
them. (iii) The exceptional set is removed: two semisimple $2$-dimensional
$\ell$-adic representations unramified outside $\{2\}$ whose traces agree
at a density-one set of primes are isomorphic, so the identity holds at
every odd prime (Remark~\ref{rem:chebotarev}).
```

## Twist elimination, compactly

```
Write $F_0(p)=a_p(f)$ and $F_1(p)=\chi_2(p)a_p(f)$. By
Lemma~\ref{lem:twist-set} the twisting character has conductor dividing
$8$, so lies in $\{1,\chi_{-1},\chi_2,\chi_{-2}\}$. At $p\equiv3\pmod4$
all four predictions vanish, since $a_p(f)=0$ for $p$ inert in $\Q(i)$, so
no such prime can discriminate. At $p\equiv1\pmod4$ we have
$\chi_{-1}(p)=1$ and $\chi_{-2}(p)=\chi_2(p)$, so the four candidates
collapse to exactly $F_0$ and $F_1$ (Lemma~\ref{lem:exhaustive}). One
prime now suffices: at $p=5$, $\chi_2(5)=-1$ and $a_5(f)=-6$, so
$F_0(5)=-6$ and $F_1(5)=+6$, while $T(5)=-6$. Hence $F_1$ is eliminated
and $F_0$ -- the untwisted form -- is the trace formula. The candidate set
was fixed by ramification before any coefficient was consulted, so this is
a finite verification inside an exhaustive criterion, not a numerical
fit.
```

## Eta-product reproducibility note (OPTIONAL POLISH, for §"Reproducibility")

```
As an independent check, the $q$-expansion of $f$ was recomputed directly
from the product
$\eta^6(4z)=q\prod_{n\ge1}(1-q^{4n})^6$
-- not read from a database -- and compared with brute-force evaluations of
the character sums in exact integer arithmetic: $T(p)=a_p(f)$ at all $21$
primes $3\le p\le113$, and $\Sigma_{\rm III}(p)=(p-1)a_p(f)$ at all $15$
primes $p\le61$ where the three-variable sum was evaluated directly. These
are checks on the theorem, not ingredients of its proof, which rests on
Livn\'e's theorem together with the twist elimination of
Section~\ref{sec:twist}.
```

---

# PAPER 3 CLAIM LEDGER

| Claim | Status | Proof location | External dependency | Computational check | Publication-safe wording |
|---|---|---|---|---|---|
| `Sigma_III = (p-1)T(p)` | new proof, standard technique | Lemma (projective reduction) | none | verified, 15 primes | "an elementary projective reduction" |
| `Sigma_III = 0` for `p = 3 mod 4` | new proof, elementary | Prop (elementary mod-4 vanishing) | none | verified, 7 primes | "by an explicit coordinate involution, requiring no arithmetic geometry" |
| `T(p) = #V_III - p^2` | classical identity | §"Affine model" | none | — | "the standard character-sum-to-point-count dictionary" |
| Weierstrass model, `Delta = 16T^8(T+1)^8` | new computation | §"Weierstrass invariants" | — | reproduced symbolically | "explicit minimal Weierstrass model" |
| three `I_2^*` fibers, minimal, no others | new computation, standard method | Prop (three `I_2^*` fibers) | Tate1975, Kodaira1963, Neron1964 | reproduced | "Tate's algorithm gives" |
| `rho = 20` | forced, standard input | §"Lattice consequences" | Shioda1990 + Lefschetz | — | "forced by the rank-20 trivial lattice and the K3 bound" |
| `rank MW = 0` | forced | same | Shioda1990 | — | "forced, not assumed" |
| full rational `(Z/2)^2` torsion | new proof | Cor (full rational 2-torsion) | MirandaPersson1989 | — | "full rational 2-torsion over `Q(T)`" |
| torsion completeness | new proof | Prop (torsion completeness) | MirandaPersson1989 | — | "the torsion is all of `(Z/2)^2`" |
| component rationality | **new — the contribution** | Lemma (graph rigidity) + Prop | none | aut group order 8, verified | "without resolving any singular fiber" |
| `Tr(F_p \| NS) = 20p` | new | Thm (NS trace) | — | — | "unconditionally, for every odd `p`" |
| `disc NS = 4` | new | §"Lattice consequences" | Shioda1990 | `64/16 = 4` reproduced | "of the saturated lattice, via torsion completeness" |
| `T(X) = diag(2,2)` | new, classification standard | §"Transcendental lattice" | ShiodaInose1977 | uniqueness reproduced | "the unique even positive-definite rank-2 lattice of determinant 4" |
| CM by `Q(i)` | classification consequence | §"…and complex multiplication" | ShiodaInose1977 | — | "read off the lattice, not matched numerically" |
| `f = eta^6(4z) = 16.3.c.a` | **not new** | §"Identifying the candidate" | AOP2002, Huber | expansion reproduced | "Ahlgren–Ono–Penniston's own form; not claimed as new" |
| `Tr(F_p \| T) = a_p(f)`, every odd `p` | new, standard inputs | Thm (exact transcendental trace) | Livne1995 **+ Chebotarev (REQUIRED 3)** | 21 primes | "for every odd prime" — *only after REQUIRED 3* |
| point-count ledger | new | §"Exact evaluation" | — | reproduced end-to-end | "derived from scratch" |
| `Sigma_III(p) = (p-1)a_p(f)` | new | Thm (main) | all of the above | 15 primes | the paper's main theorem |
| not isomorphic to AOP's `X_8` | new, needs field qualification | §AOP-precise | AOP2002 | 14 primes + structural | "non-isomorphic **over `Q`**" — *see REQUIRED 2* |

---

# MAC TEX PATCH SEQUENCE

Apply in this order. Patch 0 is already done.

**Patch 0 — ALREADY APPLIED in `b8e6cff`.** Paper 1 citation: `\bibitem{Collapse2026}` appended after
`\bibitem{Huber}`, and one `\cite{Collapse2026}` added in §2.1. *Do not re-apply.* Verify it is present
before starting.

**Patch 1 — REQUIRED 1, the `S_4` orbit count.** §2.1, source lines 138–142. Replace as given above. No
theorem numbering change. No cross-reference change.

**Patch 2 — REQUIRED 2, the non-isomorphism argument.** §AOP-precise, source lines 1213–1216. Replace as
given, **including** the `\overline\Q` qualification clause. Adds one `\ref{prop:involution}` (label
exists). No numbering change.

**Patch 3 — REQUIRED 3, the Chebotarev remark.** Insert the `remark` environment after the "Hypothesis
check for `X_III`" paragraph (source ~line 868). **This shifts every subsequent theorem number in and
after that section.** All internal references are by `\label`, so they re-resolve; but expect the printed
numbers to differ from the deposited PDF. Optionally add the Brauer–Nesbitt citation.

**Patch 4 — SR 1, the singular-K3 clarification.** Insert one sentence at the first body use (source
~line 52), or at the start of §"Transcendental lattice". No numbering change.

**Patch 5 — SR 2, eta-product-first newform presentation.** §"Identifying the candidate newform", source
~line 871. Replace as given. No numbering change.

**Patch 6 — SR 3, the abstract.** Replace the whole `abstract` environment. No numbering change.

**Patch 7 — SR 4, the introduction opening.** Replace the first three paragraphs of §1; retain the
existing hypercuboid paragraph as paragraph four. Check `\ref{sec:AOP-precise}` resolves.

**Patch 8 — SR 5, the self-contained Class III paragraph.** Insert in §2 near Definition 2.2. No
numbering change.

**Patch 9 — OPTIONAL.** Terminology clarifications table; the birational-K3 clause; the eta-product
reproducibility paragraph; OP 1's parenthetical.

**Patch 10 — references.** See below.

After Patches 1–8, run the build checklist. Compare the new theorem numbering against the deposited PDF
and record the mapping if any number a reader might cite has shifted.

---

# REFERENCES TO ADD OR MODIFY

| Key | Data | Where cited | Reason | Status |
|---|---|---|---|---|
| `Collapse2026` | De Jesús, *Zero-Diagonal Complement Collapse in Clean Finite-Field Hypercuboid Residue Systems*, Zenodo (2026), `10.5281/zenodo.22216640` (concept DOI `10.5281/zenodo.20533894`) | §2.1 | Paper 1's Theorem 3.1 is the collapse mechanism | **already added in `b8e6cff`** |
| `ClassesI_II` | De Jesús, *Finite-Field Hypercuboid Character Sums and a Discriminant-8 Singular K3 Surface*, Zenodo (2026), `10.5281/zenodo.22711323` | present, 11 places | companion paper | **verified correct**; DOI resolves |
| `AOP2002` | Ahlgren, Ono, Penniston, *Zeta functions of an infinite family of K3 surfaces*, Amer. J. Math. **124** (2002), 353–368, `10.1353/ajm.2002.0007` | present | the evaluation and the newform | **verified** — DOI confirmed in the merged `references.bib` |
| `Livne1995` | Livné, Israel J. Math. **92** (1995), 149–156, `10.1007/BF02762074` | present | modularity | **verified** |
| `Shioda1990`, `ShiodaInose1977`, `MirandaPersson1989`, `Kodaira1963`, `Neron1964`, `Tate1975` | present | as cited | — | unchanged |
| `Huber` | **RESOLVED — published.** Huber, T.; Liu, Chang; McLaughlin, J.; Ye, D.; Yuan, M.; Zhang, S., *On the vanishing of the coefficients of CM eta quotients*, Proc. Edinburgh Math. Soc. **66** (2023), no. 4, 1202–1216, `10.1017/S0013091523000627` | Remark (known vs proved) | independent occurrence of the form | **Patch 14.** Current entry is stale *and* misattributed: it reads "Z.-G. Liu"; the coauthor is **Chang Liu**. |
| `Serre1997` **(new)** | Serre, J.-P., *Abelian ℓ-Adic Representations and Elliptic Curves*, A K Peters/CRC Press, 1997 (orig. Benjamin, 1968), `10.1201/9781439863862` | REQUIRED 3's remark | the standard arithmetic-geometry source for Chebotarev arguments on ℓ-adic representations | **RESOLVED — verified.** One citation, and not a pad: it supports the step that fixes the main theorem's prime scope |
| *new, optional* | Huybrechts, *Lectures on K3 Surfaces*, CUP 2016 — or Barth–Hulek–Peters–Van de Ven, *Compact Complex Surfaces* | the birational-K3 clause, if used | K3 minimality | **only if OP 2 is adopted**; `VERIFY` chapter number |

**Do not citation-pad.** Nothing else needs adding: the finite-field ancestry layer
(`Peralta1992`, `Hirschfeld1998`, `Kuhne2023` and the rest) belongs to the repository's
`references.bib` and the provenance documents, **not** to Paper 3, whose subject is the surface.

## Huber status — RESOLVED

Settled. The work is **published**, and the current entry is wrong twice over: it says "preprint" when
it appeared in 2023, and it names "Z.-G. Liu" when the coauthor is **Chang Liu** (Zhi-Guo Liu is a
different mathematician). Correct record, verified against the registered DOI metadata:

> T. Huber, C. Liu, J. McLaughlin, D. Ye, M. Yuan, S. Zhang, *On the vanishing of the coefficients of
> CM eta quotients*, Proc. Edinburgh Math. Soc. **66** (2023), no. 4, 1202–1216,
> `doi:10.1017/S0013091523000627`.

This matters beyond tidiness: the citation supports a novelty-scoping claim — that the newform occurs
independently for the quartic Fermat K3 — so a misattributed, unlocatable reference is exactly what a
referee would challenge. **Patch 14.**

---

# TITLE CHECK

**Recommendation: keep the current title.** It is accurate, it names both halves of the contribution,
and "Discriminant-4 Singular K3 Surface" is the phrase an arithmetic geometer will search for.

1. **Current** — *Class III Hypercuboid Character Sums and a Discriminant-4 Singular K3 Surface.*
   Accurate. Weakness: "Class III Hypercuboid" is internal vocabulary, so the first three words carry
   no information for an outside reader.
2. **Conservative alternative** — *A Discriminant-4 Singular K3 Surface and the Evaluation of a
   Quadratic Character Sum in Three Variables.* Leads with the object an editor recognizes; loses the
   link to the companion paper.
3. **Arithmetic-geometry-forward** — *A Singular K3 Surface with Transcendental Lattice
   `diag(2,2)` and a Class III Hypercuboid Character Sum.* Most searchable; slightly unwieldy.

Since the companion paper is titled in parallel and the two are meant to be read as a pair, (1) wins on
balance. Revisit only if a journal objects.

---

# PROPOSED REVISED CONCLUSION

The existing §Discussion is already well calibrated — it disclaims new general theorems, names the
machinery as classical, and separates the paper from the integer perfect-hypercuboid problem. Only two
changes are suggested; keep everything else.

```
\section{Discussion}

This paper evaluates $\Sigma_{\rm III}(p)$ in closed form for every odd
prime, resolving the Class~III sector left open by \cite{ClassesI_II} and
completing the four-coordinate case of the finite-field hypercuboid
classification. The central technical contribution is the proof that every
component of every reducible fiber of $X_{\rm III}$ is individually defined
over $\Q$, obtained from full rational $2$-torsion together with a rigidity
property of the fiber's incidence graph and \emph{without resolving any
fiber explicitly}; as far as our literature search has determined this is a
different route from both \cite{AOP2002}'s Jacobi-sum computation and
\cite{ClassesI_II}'s own method, and it should apply to other singular K3
surfaces with full rational $2$-torsion at their reducible fibers.

We claim no new general theorem about K3 surfaces or modular forms: the
machinery -- Kodaira's classification, Tate's algorithm, Shioda--Tate, the
Shioda--Inose correspondence, Livn\'e's modularity theorem -- is entirely
classical, and the newform $\eta^6(4z)$ is Ahlgren, Ono and Penniston's
own. What is new is the identification of \emph{this} surface, arising from
\emph{this} character sum, together with its lattice data and the resulting
evaluation. In particular $X_{\rm III}$ and \cite{AOP2002}'s surface at
$\lambda=8$ share a transcendental representation while differing over
$\Q$: their point counts disagree at every $p\equiv3\pmod4$, so they are
not isomorphic over $\Q$, though their transcendental lattices do not
distinguish them over $\overline\Q$.

This paper does not address the classical integer perfect-hypercuboid
problem, to which the finite-field system studied here and in
\cite{ClassesI_II} is a motivating but logically separate construction.
```

Changes: the opening sentence now leads with the *result* rather than with the sector; and the
AOP relationship is stated with the field qualification from REQUIRED 2. Nothing is added about
significance.

---

# MAC BUILD AND PDF CHECKLIST

Run in order. Do not skip the second build — theorem numbering and hyperref anchors settle only on a
second pass.

- [ ] `which pdflatex bibtex` (or `latexmk`, `xelatex`) — confirm the toolchain
- [ ] copy the source to a scratch directory and build there first, leaving the repository copy alone
- [ ] `pdflatex class3_hypercuboid_k3` — first pass; note errors only
- [ ] `pdflatex class3_hypercuboid_k3` — second pass; references and numbering settle
- [ ] check the log for `LaTeX Warning: Reference` (undefined references) — must be zero
- [ ] check the log for `Citation ... undefined` — must be zero
- [ ] check the log for `There were multiply-defined labels`
- [ ] scan `Overfull \hbox` warnings; fix only those that visibly break a line or a display
- [ ] confirm the bibliography lists **11** entries and that `Collapse2026` appears
- [ ] confirm every `\cite` resolves to a number, not `[?]`
- [ ] verify the theorem/proposition/lemma numbering against the deposited PDF and **record the shift
      caused by Patch 3** (the inserted remark) for anything a reader might cite
- [ ] read every displayed equation touched by a patch, character by character
- [ ] check `tikz` output (the fiber/graph diagrams) still renders and is positioned sanely
- [ ] check page breaks around the new abstract and introduction
- [ ] click every hyperlink and DOI in the PDF
- [ ] confirm the DOIs render as `https://doi.org/...` and resolve
- [ ] `shasum -a 256` the final PDF and record it in this packet
- [ ] diff the final PDF's extracted text against the intended patch list — confirm each patch landed
      and nothing else changed
- [ ] keep the pre-revision PDF; do **not** overwrite `class3_hypercuboid_k3.pdf` until the new build is
      accepted

---

# FINAL VALIDATION CHECKLIST (before any deposit or submission)

- [ ] all four REQUIRED edits applied
- [ ] paper builds cleanly, twice
- [ ] no undefined references, no missing citations
- [ ] theorem numbering correct, and any shift recorded
- [ ] `Huber` reference resolved or explicitly marked unpublished
- [ ] the Chebotarev remark present, so "every odd prime" is supported
- [ ] the non-isomorphism claim carries its field qualification
- [ ] `S_4` orbit count corrected
- [ ] supporting computations rerun (`class_iii/scripts/`)
- [ ] eta-product coefficient check reproduced
- [ ] graph automorphism check reproduced
- [ ] lattice arithmetic reproduced (`64/16 = 4`; uniqueness of `diag(2,2)`)
- [ ] repository commit hash recorded in the packet
- [ ] final PDF SHA-256 recorded
- [ ] source archived alongside the PDF
- [ ] provenance/reproducibility statement current
- [ ] AI-assistance disclosure adapted to the venue's policy
- [ ] Zenodo metadata checked (title matches the PDF title page — note Paper 1's deposit does **not**,
      which is the kind of mismatch to avoid here)
- [ ] journal formatting checked

---

# PROPOSED AI-ASSISTANCE DISCLOSURE

Venue-neutral; trim to fit whatever policy applies.

```
AI assistance. Large language model tools were used during this work for
exploratory reasoning, for developing and reviewing the verification
scripts, for literature and provenance auditing, for checking proofs, and
for manuscript editing. No output of such a tool was treated as
authoritative. Every mathematical claim in this paper was verified
independently of the tool that suggested it: the algebraic identities by
symbolic computation, the fiber configuration and lattice data by direct
calculation from the Weierstrass model, the graph-automorphism count by
exhaustive enumeration, and the modular identification by expanding the
eta product and comparing with brute-force character-sum evaluations in
exact integer arithmetic. Bibliographic data were checked against the
cited sources or their registered metadata rather than against any model's
recollection. The author reviewed all content and takes full
responsibility for it.
```

---

# PROPOSED REPRODUCIBILITY STATEMENT

```
Reproducibility. The computations supporting this paper are in the
repository https://github.com/innerlightr-wq/hypercuboid-character-gateways
(directory class_iii/), archived with the manuscript at
doi:10.5281/zenodo.22713447. All finite-field computations use exact
integer arithmetic: Legendre symbols via modular exponentiation, never
floating point. Reproducible items include the character sums
$\Sigma_{\rm III}(p)$ and $T(p)$ by direct enumeration; the Weierstrass
reduction and the invariants $c_4$, $c_6$, $\Delta$ symbolically; the
Kodaira fiber types by valuation; the $q$-expansion of $\eta^6(4z)$ from
its product form, compared against $T(p)$; the exhaustive automorphism
count for the $I_2^*$ dual graph; and the lattice arithmetic behind
$\disc\NS=4$ and $T(X_{\rm III})\cong\mathrm{diag}(2,2)$. These are checks
on results proved in the text, not substitutes for the proofs.
```

---

# PROPOSED DATA / CODE AVAILABILITY STATEMENT

```
Data and code availability. No external data were used; every quantity in
this paper is computed from the definitions. The scripts that reproduce the
computational checks are in the repository cited above and are archived
with the manuscript on Zenodo (doi:10.5281/zenodo.22713447). The manuscript
source is archived with the PDF. All results are reproducible from the
scripts with a standard Python installation and a computer algebra system
for the symbolic steps.
```

Note for honesty: do **not** state that the LaTeX build has been reproduced on Linux. It has not — this
machine has no TeX. Say only what was run.

---

# EDITOR COVER-LETTER CORE

```
We evaluate in closed form a quadratic character sum in three variables
over a finite field,
$\Sigma_{\rm III}(p)=\sum_{x\in\Fp^3}\chi(x_0x_1x_2(x_0+x_2)(x_1+x_2)(x_0+x_1+x_2))$,
showing that for $p\equiv1\pmod4$ it equals $(p-1)a_p(f)$ where
$f=\eta^6(4z)$ is the weight-3 newform of level 16 with complex
multiplication by $\Q(i)$, and that it vanishes identically for
$p\equiv3\pmod4$.

The route is geometric. The sum is the point count of an explicit affine
surface; its elliptic fibration has exactly three fibers of Kodaira type
$I_2^*$, which makes the trivial lattice of rank 20 and therefore forces
both maximal geometric Picard number and trivial Mordell-Weil rank. The
substantive step is showing that every component of every reducible fiber
is individually defined over $\Q$, which we obtain from full rational
2-torsion together with a rigidity property of the fiber's incidence graph
-- without resolving any singular fiber. This pins the transcendental
lattice to diag(2,2), hence the CM field to $\Q(i)$, and Livne's theorem
with a finite exhaustive twist elimination identifies the Frobenius trace
with $a_p(f)$.

The newform is not new: it is the one Ahlgren, Ono and Penniston attach to
their own K3 surface at parameter $\lambda=8$, and we claim no novelty for
it. Our surface is not theirs -- different Weierstrass model, different
fiber configuration, and different point counts at every $p\equiv3\pmod4$,
so not isomorphic over $\Q$ -- and their Jacobi-sum method does not
evaluate this sum. The contribution is the identification of this surface
and its lattice data, the fiber-rationality technique, and the resulting
evaluation.

Every computational claim is reproducible from scripts in a public
repository, in exact integer arithmetic; the modular identification was
checked by expanding the eta product directly rather than by consulting a
database.
```

---

# 150-WORD NONSPECIALIST SUMMARY

```
Fix a prime p and ask, for each triple of residues, whether a particular
product of six linear expressions is a square modulo p. Adding up +1 for
squares and -1 for non-squares gives a single integer for each prime. One
expects such a total to be small and irregular. It is not. We show it is
governed by geometry: the same count is the number of points on an explicit
algebraic surface, and that surface turns out to be a K3 surface with the
largest possible number of independent curve classes. For such surfaces a
small lattice of integers controls everything, and here that lattice is as
simple as it can be - the 2-by-2 identity doubled. That forces the count to
be a coefficient of a specific modular form, built from the Dedekind eta
function. The result is an exact formula for every odd prime, and zero for
every prime that is 3 modulo 4.
```

---

# HOW I WOULD EXPLAIN PAPER 3 TO A MATHEMATICIAN

Roughly three minutes, spoken.

> Start with a character sum. Fix an odd prime, take the Legendre symbol, and sum it over all triples
> in `F_p^3` of a product of six linear forms — three coordinates and three of their sums. You get an
> integer for each prime, and the question is what it is.
>
> The first move is free. The product is homogeneous of degree six, so the Legendre symbol is constant
> on lines through the origin, and the three-variable sum collapses to `(p−1)` times a two-variable
> sum. Call that `T(p)`. And half the answer is elementary: there's a coordinate involution that sends
> the integrand to minus itself, so for `p ≡ 3 mod 4` the sum is identically zero. No geometry needed.
>
> For `p ≡ 1 mod 4` you need geometry, and the bridge is the identity that the number of square roots
> of `c` is `1 + χ(c)`. Summing that turns `T(p)` into the point count of an explicit affine surface,
> `Y² = X(X+1)T(T+1)(X+T+1)`. Now treat `T` as a parameter: for each `T` you have a cubic in `X`, so
> the surface is fibred by elliptic curves, and you can run Tate's algorithm. The discriminant is
> `16T⁸(T+1)⁸`, and you get exactly three bad fibers — at `0`, `−1`, and infinity — each of Kodaira
> type `I_2*`.
>
> That's where it becomes clean. Each `I_2*` fiber contributes a `D_6`, rank six, and with the general
> fiber and the zero section the trivial lattice already has rank twenty. A K3 surface can't have Picard
> number more than twenty. So the Picard number *is* twenty and the Mordell–Weil rank *is* zero — both
> forced, nothing assumed.
>
> The one real piece of work is showing Frobenius acts on the Néron–Severi lattice by `p` times the
> identity, and for that every component of every bad fiber has to be rational. The usual way is to
> resolve the fibers and look. We don't. The dual graph of an `I_2*` fiber is a tree: a three-vertex
> spine with two legs at each end. The zero section and the three rational 2-torsion sections land on
> four *different* legs, so Galois fixes those four. And a tree automorphism that fixes all four legs is
> the identity — each leg is a leaf with a unique neighbour, that pins the spine ends, and the middle
> vertex is their only common neighbour. So Galois fixes all seven components. That's the paper's
> technique.
>
> From there it's bookkeeping with real content. The torsion is all of `(Z/2)²`, which is what makes the
> discriminant computation a statement about `NS` itself and not a sublattice: `64/16 = 4`. So the
> transcendental lattice is rank two, even, positive definite, determinant four — and there's exactly
> one such lattice, `diag(2,2)`, because the class number of discriminant `−4` is one. That gives CM by
> `Q(i)`.
>
> Then Livné: the transcendental part of a singular K3 over `Q` is modular of weight three — but only up
> to a quadratic twist. Bad reduction only at 2 cuts the candidate twists to four; CM vanishing at
> inert primes collapses those to two; and one prime, `p = 5`, decides between them. The answer is the
> untwisted form `η⁶(4z)`.
>
> So `Σ_III(p) = (p−1)a_p(η⁶(4z))` for `p ≡ 1 mod 4`, and zero otherwise. And note the consistency
> check: the vanishing at `p ≡ 3 mod 4` is proved twice, once by the elementary involution and once by
> CM vanishing. Different mechanisms, same answer.
>
> One thing I should say plainly: the modular form is not mine. It's Ahlgren, Ono and Penniston's — they
> attach it to their own K3 surface at `λ = 8`. My surface isn't theirs; the point counts differ at
> every `p ≡ 3 mod 4`, so they're not isomorphic over `Q`, though over `Q̄` their transcendental
> lattices don't tell them apart. What's mine is this surface, its lattice, the fiber-rationality
> argument, and the evaluation.

---

# REMAINING BEFORE MAC

Two items, both small and neither mathematical:

1. **`Huber` reference status** — publication state, full author list, and an identifier. Needs a web
   lookup. Marked `VERIFY ON MAC/WEB BEFORE SUBMISSION`.
2. **Two optional citations to select** — a standard reference for Brauer–Nesbitt / density-one traces
   (for REQUIRED 3's remark) and, only if OP 2 is adopted, a K3 minimality reference. Both are textbook;
   picking an edition and a theorem number needs a shelf or a browser.

Everything else — every mathematical decision, every replacement wording, the patch order, and the
verification results — is fixed in this packet.

---

# FINAL-PASS RESOLUTIONS

Four items were left open by the previous pass. All four are now settled; nothing mathematical remains.

## A. The theorem's prime scope is correct as written — no rewording needed

Audited specifically. The manuscript's Theorem (Exact transcendental trace) says "for every odd prime
`p \neq 2`", and the Main Theorem "for every odd prime `p`". **Both are right**, and the justification
already exists in the paper; only the bridge of REQUIRED 3 is missing.

Why "every odd prime" and not the narrower alternatives:

* **not "every odd prime of good reduction"** — because §"Bad primes" proves good reduction at *every*
  odd prime, so the two phrases coincide. The argument: `a_2(T)=T(T+1)(T+2)` and `a_4(T)=T^2(T+1)^3`
  have integral coefficients, `\Delta(T)=16T^8(T+1)^8`, and no odd prime divides all coefficients; so
  reducing mod any odd `\ell` leaves the same three `I_2^*` fibers at the same three points `T=0,-1,\infty`
  (these stay distinct mod every odd `\ell`). Bad reduction only at 2.
* **not "every odd unramified prime"** — same reason: both representations are unramified outside
  `\{2\}` (the surface by good reduction, the newform by 2-power level), so "unramified" and "odd"
  coincide here.
* **and `p=2` is excluded globally**, as the standing hypothesis.

So the exceptional set implicit in Livné's "almost all" is removed entirely by REQUIRED 3, and no
exceptional prime survives. **No change to either theorem statement.** This is worth one clause in the
paper, however, because a referee will ask: after the Chebotarev remark, add "and, since `X_{\rm III}`
has good reduction at every odd prime and `f` has 2-power level, every odd prime is unramified for both
representations, so no exceptional set remains."

## B. Brauer–Nesbitt: one citation, and it is needed

**Recommendation: cite `Serre1997` once, in REQUIRED 3's remark.** It is not implicit in the cited
Livné source in a usable way: Livné's *method* is a Faltings–Serre argument and so contains this kind of
reasoning, but the *statement quoted in Paper 3* concludes only "for almost all primes of good
reduction". A reader checking the quoted statement cannot get to "every odd prime" from it. Since that
upgrade is what fixes the scope of the paper's main theorem, it deserves a pointer rather than being
left as folklore.

Verified record: **Serre, Jean-Pierre, *Abelian ℓ-Adic Representations and Elliptic Curves*, A K
Peters/CRC Press, 1997** (originally Benjamin, 1968), `doi:10.1201/9781439863862`. This is the standard
arithmetic-geometry source for Chebotarev arguments on `\ell`-adic representations. Chapter I is the
relevant part; pin the exact proposition number on the Mac if a precise pointer is wanted — the fact
itself is standard and the chapter reference suffices.

Do **not** add a second citation for Brauer–Nesbitt as a pure representation-theory statement (Curtis–
Reiner and the like). One pointer is enough and two would be padding.

## C. The birational-K3 clause is **not needed** — keep it out

REQUIRED 2's replacement wording concludes "no isomorphism over `\Q` can exist, and a fortiori none as
elliptic surfaces over `\Q(T)`". It never asserts anything about birational maps, so the K3 minimality
fact is not load-bearing anywhere.

**Decision: omit it.** That removes the need for a Huybrechts or BHPV citation entirely, and avoids a
digression into minimal models in a paper that has no other need for them. If the current manuscript
text says "not isomorphic *or birational*", simply drop the word "birational" as part of Patch 2 rather
than defending it.

## D. Huber and Serre: both resolved above

---

# THEOREM-NUMBER SHIFT MAP

Computed from the source, not estimated. The counter is
`\newtheorem{theorem}{Theorem}[section]`, shared by `proposition`, `lemma`, `corollary`, `definition`,
`remark`, `openproblem`, and **reset at every `\section`**. The Chebotarev remark of REQUIRED 3 is
inserted at source line ~861, inside §6 ("Transcendental lattice and complex multiplication"), directly
after the "Hypothesis check for `X_III`" paragraph.

Consequently exactly **one** printed number changes:

| Current printed number | Item | Expected new number |
|---|---|---|
| 6.1 | Theorem [Livné] | **6.1** (unchanged — precedes the insertion) |
| *(new)* | Remark [from "almost all" to every odd prime] | **6.2** |
| 6.2 | Remark [Known vs. proved] | **6.3** |

**Everything else is unaffected** — all 35 other theorem-like items keep their printed numbers,
including every item of §7 (`7.1` Twist candidate set, `7.2` Exhaustiveness, `7.3` Twist elimination,
`7.4` remark, `7.5` Exact transcendental trace), every item of §8 (through `8.7` Main theorem), and
every appendix item. Cross-references are all by `\label`/`\ref` and re-resolve automatically.

**Build check:** after the build, confirm that the Main Theorem still prints as **8.6** and the Exact
transcendental trace as **7.5**. If either has moved, an unintended environment was added.
