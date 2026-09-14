# Contribution Map — private working note, not manuscript prose

Purpose: settle, once and precisely, what this paper actually
contributes now that Ahlgren–Ono–Penniston (2002) is known. Usable
later for a cover letter or preprint abstract-page description.

---

## Part I — AOP 2002, read closely

**S. Ahlgren, K. Ono, D. Penniston, "Zeta functions of an infinite
family of K3 surfaces," Amer. J. Math. 124 (2002), no. 2, 353–368.**
(Full PDF obtained from the author's own posted copy.)

**Family**: `X_\lambda:s^2=xy(x+1)(y+1)(x+\lambda y)`, `\lambda\in\Q\setminus\{0,-1\}`.
**Companion elliptic curves**: `E_\lambda:y^2=(x-1)(x^2-\frac1{\lambda+1})`.
**Character**: `\phi_p(x)=\left(\frac xp\right)`, the Legendre symbol — identical object to our `\chi`.

**Theorem 1.1** (local zeta function, any good `p`):
$$Z(X_\lambda/\Fp,T)=\frac1{(1-T)(1-p^2T)(1-pT)^{19}(1-\gamma\pi_{\lambda,p}^2T)(1-\gamma\bar\pi_{\lambda,p}^2T)},\qquad \gamma=\phi_p(\lambda+1),$$
`\pi_{\lambda,p},\bar\pi_{\lambda,p}` the Frobenius eigenvalues of `E_\lambda`.

**Theorem 2.1** (the character-sum identity, valid for `\lambda\not\equiv0,-1\pmod p`):
$$A(\lambda,q)=\phi_q(\lambda+1)\bigl(a(\lambda,q)^2-q\bigr),\qquad A(\lambda,q):=\sum_{x,y\in\Fq}\phi_q\bigl(xy(x+1)(y+1)(x+\lambda y)\bigr),\quad a(\lambda,q):=-\sum_{x\in\Fq}\phi_q\Bigl((x-1)\bigl(x^2-\tfrac1{\lambda+1}\bigr)\Bigr).$$

**Theorem 1.2** (singular locus, all `\lambda`, general theorem):
`X_\lambda` is modular (equivalently, per their §5, singular with CM) iff
`\lambda\in\{1,8,\tfrac18,-4,-\tfrac14,-64,-\tfrac1{64}\}`.

**At `\lambda=1` specifically**: `f_1=B\otimes\chi_{-4}` where
`B(z)=\eta^2(z)\eta(2z)\eta(4z)\eta^2(8z)=q-2q^2-2q^3+\cdots\in S_3(\Gamma_0(8),\chi_{-2})`
— level 8, weight 3, nebentypus `\chi_{-2}`, i.e. **exactly the
parameters of LMFDB `8.3.d.a`** (uniqueness of such a form given
`h(-8)=1`, the same uniqueness fact our own manuscript uses, confirms
`B=f`), twisted by `\chi_{-4}=\chi(-1)` in our notation.

**Proof method**: entirely elementary — a long, explicit Jacobi-sum
manipulation (Theorem 2.1's proof, §2) proving the character-sum
identity directly, with NO K3-surface geometry needed for that step;
separately (§3–4), an explicit double-cover-of-`\mathbf P^2`
construction of `X_\lambda`, an explicit elliptic fibration, and
Shioda's rank formula give the `\ge19` Picard bound directly and
combinatorially (not via a height-pairing/Mordell–Weil-lattice
computation the way our manuscript does it); singularity (Theorem 1.2)
is then proved via `E_\lambda`'s CM classification (**a table of the 13
class-number-1 `j`-invariants**) plus a citation to Ribet's theorem
(the *different* Ribet fact — large mod-`\ell` image for non-CM forms —
used to rule out the non-exceptional `\lambda`, not the Sym² splitting
fact our manuscript cites Ribet for).

### Equivalence map

| AOP | This manuscript |
|---|---|
| `\phi_q` | `\chi` |
| `A(\lambda,q)` at `\lambda=1` | `S(p)` — **literally the same sum**, verified by direct computation, 10 primes, exact match |
| `a(1,p)` | `\chi(2)(p)\,a_p(E)` — **PROVED exactly**, via an explicit isomorphism `E\to E_1`, `(x,y)\mapsto(x/2+1,\,y/(2\sqrt2))`, defined over `\Q(\sqrt2)` (Final Polish phase); coincides numerically with `\chi(-1)(p)a_p(E)` only because `\chi(-1)=\chi(2)` wherever `a_p(E)\ne0` |
| `E_1:y^2=(x-1)(x^2-\frac12)` | the `\chi(2)`-quadratic twist of our `E:y^2=x^3+4x^2+2x` (both `j=8000`) |
| `B(z)` | `f=8.3.d.a` (forced identical by `h(-8)=1` uniqueness, both level 8 weight 3 CM-by-`\Q(\sqrt{-2})`) |
| `f_1=B\otimes\chi_{-4}` | our `\mathrm{Tr}_T(p)=\chi(-1)a_p(f)` |
| `X_1` | our `X` (same affine equation; almost certainly the same K3 surface, not independently proved isomorphic beyond matching zeta functions) |

**Caveat, updated (Final Polish phase)**: this map is now established
by (a) the affine equations being literally identical; (b) an explicit,
verified isomorphism `E\to E_1` over `\Q(\sqrt2)` (short-Weierstrass
`(A,B)`-scaling by `u^2=\tfrac12`, `j=8000` on both sides, checked
symbolically — no longer just "strong evidence," an exact proof); and
(c) the resulting `\#X(\Fp)` formulas from both papers matching exactly
once this now-proved curve-twist identification is substituted. The
smooth projective models `X` and `X_1` themselves were not shown
isomorphic by an explicit map (unnecessary: two smooth projective K3
models of the same affine surface are automatically isomorphic, by
uniqueness of smooth projective models for K3 surfaces), so that
narrower point remains as before — only the elliptic-curve leg of the
comparison needed, and has now received, an explicit proof.

---

## Part II — overlap classification

| Result | Classification |
|---|---|
| `S(p)` formula | **IMMEDIATE COROLLARY OF AOP** (Thm 2.1 at `\lambda=1`, via curve-twist substitution) |
| `\Sigma_I(p)` formula | **IMMEDIATE COROLLARY OF AOP** (combines the above with our own elementary Lemma 1) |
| `\Sigma_{II}(p)` formula | **IMMEDIATE COROLLARY OF AOP** (combines the above with our own Gateway relation) |
| The K3 model itself (`V\to X`) | **ALREADY IN AOP** (their `X_1`, same affine equation) |
| Picard-rank `=20` at this specialization | **ALREADY IN AOP** (Theorem 1.2 lists `\lambda=1`) |
| The specific `19+\mathrm{rank}` computation method | **NEW DERIVATION OF KNOWN RESULT** — AOP get `\rho\ge19` combinatorially from an explicit double-`\mathbf P^2`-cover fibration and Shioda's rank formula; we get `\rho=20` via an explicit `\Q(i)(t)`-rational height-1 Mordell–Weil section and the height pairing. Different route to the same number. |
| `NS` Frobenius trace `(19+\chi(-1))p` | **NEW DERIVATION OF KNOWN RESULT** — AOP's Theorem 1.1's `19` rational classes are implicit in their `(1-pT)^{19}` factor; our explicit `\Q(i)`-descent-of-`P_1` mechanism explaining exactly *why* the 20th eigenvalue is `\chi(-1)p` (as opposed to AOP, who reach the same numerology via the `\gamma\pi^2,\gamma\bar\pi^2` factors without isolating an individual "extra `\Q(i)`-rational class" narrative) is a genuinely different, if not necessarily deeper, explanatory route. |
| The `\Q(i)`-section `P_1` itself | **POSSIBLY NEW GEOMETRIC OBSERVATION** — AOP's proof never constructs or needs an explicit Mordell–Weil generator; this specific section, and the direct verification `\sigma(P_1)=-P_1`, does not appear to be in AOP or any source found. |
| Corrected `I_2` fiber count `2p+1-\chi(-2)` | **HYPERCUBOID/K3-ROUTE-SPECIFIC CONSEQUENCE** — this is an artifact of *our* specific affine-to-projective point-counting route (via `\#V(\Fp)=p^2+S(p)` and the fiber ledger), not needed by, or present in, AOP's proof, which never separates an affine surface `V` from the projective `X` in this way. Genuinely a different bookkeeping path, though it computes a fact (the fiber's point count) that is, in principle, also recoverable from AOP's Theorem 1.1 by extracting the `t=1` term of their zeta function — not claimed as unreachable by their method, just not what their method actually does. |
| Class-I/Class-II symmetry relation (`\Sigma_{II}=\chi(-1)\Sigma_I`) | **HYPERCUBOID-SPECIFIC.** Not in AOP (which has no notion of "Class I/II/III" or hypercuboid symmetry classes at all). **NOT FOUND** anywhere in this audit's literature search. |
| The hypercuboid motivation, `\Sigma_I(p)=(p-1)S(p)` reduction itself | **HYPERCUBOID-SPECIFIC.** Not in AOP. **NOT FOUND** elsewhere. |
| Class-III vanishing (`p\equiv3\bmod4`) | **HYPERCUBOID-SPECIFIC**, proved by a mechanism with no AOP or K3-surface content at all — entirely independent, self-contained, elementary. |

---

## Part III — the paper's real contribution, stated plainly

**What is known before this paper**: the exact evaluation of `S(p)`
(equivalently `A(1,q)` in AOP's notation) — Ahlgren–Ono–Penniston,
2002, Theorems 1.2 and 2.1, combined with an elliptic-curve-twist
identification made explicit in this audit. This is not new.

**What is derived differently here**: a self-contained proof of the
same `S(p)` identity via the Picard-lattice/Mordell–Weil/Livné route,
starting from an explicit `\Q(i)(t)`-rational Mordell–Weil generator
`P_1` and its Galois action, rather than AOP's direct elementary
Jacobi-sum manipulation. This is a **genuinely different proof method**
(confirmed, Part IX below) reaching the same numerical conclusion — of
independent methodological interest, not claimed as a deeper or better
proof, simply a different one, and not previously published as far as
this audit's search could determine.

**What is hypercuboid-specific** (the part of the paper most plausibly
a genuine new contribution): the finite-field hypercuboid motivation
itself; the reduction `\Sigma_I(p)=(p-1)S(p)` connecting the
hypercuboid problem to AOP's sum in the first place; the Gateway
relation `\Sigma_{II}(p)=\chi(-1)\Sigma_I(p)`; and the resulting exact
Class-I/II formulas as *hypercuboid* consequences (even though `S(p)`
and `a_p(f)` themselves were already known).

**What remains open**: `\Sigma_{III}(p)` at `p\equiv1\pmod4` — not
addressed by AOP (which has no Class III notion), not addressed by this
paper, genuinely open.

**Recommended framing for the revised paper**: a paper about the
**hypercuboid character-sum classification**, which (a) reduces two of
its three residual classes to a *known* classical character-sum
identity (AOP 2002), honestly cited, and (b) gives, as a matter of
independent interest, a self-contained geometric derivation of that
known identity via the specific singular K3 surface the hypercuboid
reduction naturally produces — **not** a paper primarily about a new
exact evaluation of `S(p)`.

---

## For a future cover letter

*"We study a finite-field character-sum system arising from a
zero-diagonal symmetry classification of a clean hypercuboid residue
system. Two of the three resulting symmetry classes reduce to a
classical character sum whose exact evaluation was given by Ahlgren,
Ono, and Penniston (2002); we give here an independent, geometric
derivation of this evaluation via the specific discriminant-8 singular
K3 surface that the hypercuboid reduction naturally produces, and we
record the resulting exact hypercuboid formulas as corollaries. The
third symmetry class is shown to vanish for `p\equiv3\pmod4` by an
unrelated, self-contained argument; its value for `p\equiv1\pmod4`
remains open."*

---

## September 2026 addendum: the sector-signature integration round

Five new remarks and one new appendix were added, none changing any
previously-stated theorem or its proof — all are explanatory additions or
omitted-justification repairs, fully elementary (classified `E` in
`PROOF_DEPENDENCY.md`), each independently verified by exact symbolic
computation (`scripts/verify_char3_fiber_and_rank.py`), not by any Lean
formalization (none exists in this repository; Lean work, if ever
undertaken, is explicitly deferred to a separate session):

1. **The Class III coordinate bridge** (`\cite{ClassIII}`'s own Remark
   `rem:bridge`) — an explicit unimodular map connecting that paper's
   projective-reduction lemma to its stated affine model, previously
   unexhibited.
2. **The discriminant-factorization identity** (`rem:disc-factorization`,
   both papers) — `\Delta=16[t(t+1)]^6\cdot\operatorname{disc}_X\{0,-1,-(t+b)\}`,
   explaining Classes I/II's four *mixed* vs. `\cite{ClassIII}`'s three
   *uniform* bad fibers from where the moving root collides with the
   shared prefactor's own zero locus.
3. **Validity of the Kodaira classification at every odd prime**
   (`rem:char-p`, both papers) — going beyond a node/cusp shortcut to
   Tate's algorithm's actual Step 6 at the one delicate (`j=1728`) fiber,
   resolving a genuine characteristic-3 subtlety this round found and
   closed rather than sidestepped.
4. **The fiber-to-rank structural explanation** (`rem:fiber-to-rank` /
   `rem:rank-field`) — why Classes I/II's rank-1 claim needs an explicit
   Mordell–Weil generator while `\cite{ClassIII}`'s rank-0 claim needs
   only the Hodge-theoretic ceiling.
5. **Class II's own quadratic-twist identification and field-specific
   rank** (`rem:class2-twist`, Appendix `app:class2`) — Class II's own
   Weierstrass model (not merely an abstract construction) is proved,
   via the exact `(c_4,c_6,\Delta)$` twist law and an explicit
   translation, to be the `-1`-twist of `X`; a Galois-descent argument
   then gives `\rk\mathrm{MW}(X/\Q(t))=0$` while the transported section
   gives `\rk\mathrm{MW}(X_{II}/\Q(t))=1$` — the two surfaces, isomorphic
   over `\Q(i)(t)$`, are genuinely different over `\Q(t)$` itself.

Full derivations, source locations, and the computational verification
underlying each point are recorded in
`explorations/sector_signature_proof_closure_2026-09-14/PROOF_CLOSURE.md`
and the three preceding exploration rounds it closes out.
