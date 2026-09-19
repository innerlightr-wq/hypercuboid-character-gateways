# Paper 3 — theorem dependency map

`class_iii/manuscript/class3_hypercuboid_k3.tex` (23 pp, PDF sha256 `ba37532b…9d9eb7`, byte-identical
to the audited deposit). Verification commands and outputs are in
[`PAPER3_REFEREE_READINESS.md`](PAPER3_REFEREE_READINESS.md) §Reproduction.

Legend for the classification column: **A** classical imported fact · **B** cited external theorem ·
**C** imported from Paper 1 · **D** imported from Paper 2 · **E** new proof local to Paper 3 ·
**F** computation · **G** interpretation.

## The spine

```
Sigma_III(p)  (Definition, §2)
   │  Lemma "Projective reduction"  [E, degree-6 homogeneity]
   ▼
Sigma_III(p) = (p-1) T(p),   T(p) = sum_{x,t} chi(x t(t+1)(x+t)(x+t+1))
   │
   ├── Proposition "Elementary mod-4 vanishing"  [E] ──► Sigma_III(p) = 0 for p = 3 mod 4
   │                                                      (independent of everything below)
   ▼
V_III : Y^2 = X(X+1)T(T+1)(X+T+1)          #V_III(F_p) = p^2 + T(p)   [A]
   │  complete the cube, scale by u = T(T+1)
   ▼
Y^2 = X^3 + T(T+1)(T+2)X^2 + T^2(T+1)^3 X          [E, verified]
   │  Tate's algorithm  [B: Tate1975, Kodaira1963, Neron1964]
   ▼
three I_2^* fibers at T = 0, -1, infinity; Delta = 16 T^8 (T+1)^8; no others
   │  Kodaira–Néron component groups (Z/2)^2 each
   ├── full rational 2-torsion (Z/2)^2 over Q(T)   [E + B: MirandaPersson1989]
   ├── Lemma "Four distinct legs at T=0"           [E]
   ├── Lemma "Graph rigidity"                      [E — the central new argument]
   ▼
every component of every reducible fiber is individually defined over Q   [E]
   │  Shioda–Tate  [B: Shioda1990]
   ▼
Triv = U + D_6 + D_6 + D_6, rank 20  ⇒  rho = 20 and rank MW = 0, both forced by rho <= 20
   │
   ▼
Tr(F_p | NS) = 20p  ·  |disc NS| = 4^3/|(Z/2)^2|^2 = 64/16 = 4
   │  singular-K3 classification  [B: ShiodaInose1977]
   ▼
T(X_III) = diag(2,2)  (unique even positive-definite rank-2 lattice of det 4)  ⇒  CM by Q(i)
   │  Livné modularity  [B: Livne1995]  +  twist elimination  [E, finite and exhaustive]
   ▼
Tr(F_p | T(X_III)) = a_p(16.3.c.a),  16.3.c.a = eta^6(4z)   [not claimed new: AOP2002, Huber]
   │  point-count ledger  [E + F]
   ▼
T(p) = a_p(16.3.c.a) for p = 1 mod 4      ⇒   MAIN THEOREM
Sigma_III(p) = (p-1) a_p(16.3.c.a) for p = 1 mod 4, and 0 for p = 3 mod 4
```

## Per-theorem table

**Lemma (Projective reduction)** · uses degree-6 homogeneity of the sextic and `chi(z^6)=1` · no
external citation · no Paper 1/2 dependency · no computation · outputs `Sigma_III=(p-1)T(p)` ·
**risk: none.** Classification E, but the technique is Paper 2's (cited there, applied fresh here).

**Proposition (Elementary mod-4 vanishing)** · uses an explicit coordinate involution sending the
integrand to `-1` times itself · no external citation · no dependency · no computation · outputs
`Sigma_III=0` for `p=3 mod 4` · **risk: none.** Independent of all geometry — a genuine strength, and
the paper is right to say so.

**Proposition (Three `I_2^*` fibers)** · uses Tate's algorithm on `c_4,c_6,Delta` · cites
`Tate1975`, `Kodaira1963`, `Neron1964` · computation: symbolic invariants · outputs the fiber
configuration and minimality · **risk: low** — reproduced exactly here.

**Corollary (Full rational 2-torsion) + Proposition (Torsion completeness)** · uses the
`a_6=0` factorization and `MirandaPersson1989` · outputs `MW_tors = (Z/2)^2` over `Q(T)` ·
**risk: low–moderate.** This is what supplies the index correction in the discriminant formula, so a
referee will read it closely; the paper does prove completeness rather than just exhibiting the three
sections.

**Lemma (Four distinct legs at `T=0`)** · uses the rationality of the zero section and the three
2-torsion sections, plus multiplicity bookkeeping · outputs: four pairwise distinct multiplicity-one
components are individually Galois-fixed · **risk: moderate** — the input to the rigidity argument.

**Lemma (Graph rigidity)** · uses only that the `I_2^*` dual graph is a tree (7 vertices, 6 edges)
with a 3-vertex spine and two legs at each end · no external citation · computation cited only as a
*check* (all `7! = 5040` permutations; automorphism group of order 8; exactly one fixes the four legs)
· outputs: Galois acts trivially on all seven components · **risk: low, and this is the paper's most
distinctive contribution.** Reproduced independently here: group order 8, exactly one leg-fixing
automorphism, the identity.

**Theorem (`Tr(F_p|NS) = 20p`, `disc NS = 4`, `T(X) = diag(2,2)`)** · uses Shioda–Tate
(`Shioda1990`), the component-group index, and the classification of rank-2 even positive-definite
lattices of determinant 4 · outputs the transcendental lattice and hence CM by `Q(i)` ·
**risk: moderate — this is the main referee target.** Reproduced: `rank Triv = 2+18 = 20`, so `rho=20`
and `rank MW = 0` are *both forced* by `rho <= 20`, not assumed; `64/16 = 4`; and `diag(2,2)` is the
unique class (class number of discriminant `-4` is 1).

**Theorem (Livné)** · quoted external theorem `Livne1995` · **risk: low** provided the hypotheses are
stated at the point of use.

**Lemma (Twist candidate set) + Lemma (Exhaustiveness) + Proposition (Twist elimination)** · uses
ramification at `{2}` to force the candidate set `{1, chi(-1), chi(2), chi(-2)}`, CM vanishing at
inert primes to collapse it to two testable hypotheses `F_0, F_1`, and one prime (`p=5`) to
discriminate · computation: `F_0(5) = -6 = T(5)`, `F_1(5) = +6` · **risk: low.** The logic is the right
shape — a finite check *inside* an exhaustive criterion, not a table standing in for a theorem — and
the paper says so explicitly.

**Theorem (Exact transcendental trace)** · combines Livné with twist elimination · outputs
`Tr(F_p|T(X_III)) = a_p(16.3.c.a)` for every odd `p` · **risk: moderate**, inherited from the two
inputs.

**Lemmas (Affine bad-fiber count, Good-fiber affine count) + Proposition (Ledger)** · uses explicit
fiber-by-fiber counting · computation: F · outputs the bridge from `Tr(F_p|T)` back to `T(p)` ·
**risk: low–moderate** — arithmetic bookkeeping, the classic place for an off-by-`p` slip. Verified
numerically end-to-end at 21 primes here.

**Theorem (Exact evaluation of `T(p)`) + Theorem (Main theorem)** · combines everything above ·
outputs the boxed evaluation · **risk: low given the inputs.** Verified numerically: `T(p) = a_p` at
all 21 primes tested from 3 to 113, and `Sigma_III(p) = (p-1)a_p` at all 15 primes where
`Sigma_III` was computed directly.

## Dependencies on Papers 1 and 2

**Paper 1** (`Collapse2026`, DOI `10.5281/zenodo.22216640`) supplies the collapse mechanism — its
Theorem 3.1 — underlying §2.1's seven-form reduction and the `p = 1 mod 4` condition. Paper 3 did not
cite it; **this pass adds the citation** (new bibitem, plus one in-text reference in §2.1). No result
depends on consulting it, because §2.1 restates what is used.

**Paper 2** (`ClassesI_II`) is cited 11 times. What is actually imported: the notation and the
hypercuboid setup (§2.1), the projectivization technique (applied fresh to a different polynomial),
and a lattice sanity check (§8.x). What is **not** imported: no theorem of Paper 2 is used as a
premise in any Paper 3 proof. Paper 3 is therefore already close to self-contained; the remaining
gaps are listed in the readiness document.

## Computation dependencies

Symbolic: the Weierstrass reduction, `c_4`, `c_6`, `Delta`, and the fiber valuations. Combinatorial:
the graph automorphism enumeration (a check, not a proof). Numerical: the point-count ledger, the
`p=5` twist discrimination, and the `T(p) = a_p` comparison. All were re-run independently in this
pass; see the readiness document.
