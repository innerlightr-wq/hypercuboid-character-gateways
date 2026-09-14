# Manuscript-ready insertions — final, fully closed

Supersedes `explorations/sector_signature_final_check_2026-09-14/PROPOSED_INSERTIONS_REVISED.md`'s **C** and **E** (both fully closed this round, caveats removed); **A**, **B**, **D** carried forward unchanged (unaffected by this round's work). Nothing applied to any manuscript. **No literature-novelty claim is made for any insertion** — "new" below means only "absent from these two manuscripts as currently written"; no search for prior literature occurrences of these standard techniques (Tate's algorithm, Galois descent, quadratic twists) was performed.

---

## A. Class III coordinate bridge

**Target**: `class_iii/manuscript/class3_hypercuboid_k3.tex`, after the sentence introducing $V_{\rm III}$.
**Hypotheses**: none beyond the ambient odd-prime setting already in force.
**Classification**: repair of an omitted justification.
**Restriction**: none.
*(Text unchanged from the prior round — see `PROPOSED_INSERTIONS_REVISED.md` §A.)*

## B. Discriminant/collision lemma

**Target**: both manuscripts' Kodaira-classification appendices.
**Hypotheses**: the family $Y^2=T(T{+}1)X(X{+}1)(X{+}T{+}b)$, $b\in\{0,1\}$, exactly as each manuscript already defines it.
**Classification**: explanatory addition.
**Restriction**: identifies bad-fiber locations and $\Delta$-orders only, not Kodaira type (type still needs §1's classification, now supplied separately as Insertion E and its Class-III analogue).
*(Text unchanged from the prior round — see `PROPOSED_INSERTIONS_REVISED.md` §B.)*

---

## C. Twist interpretation — CLOSED this round, caveat removed

**Target**: `manuscript/hypercuboid_character_sums.tex`, §"Closed forms for Classes I and II," as a remark after the Gateway relation's proof.

**Hypotheses**: $P_1=(-(T{+}1),i(T{-}1)(T{+}1)^2)$ on $X$ (manuscript's own point, height $1$, Proposition "Picard rank and lattices"); $\operatorname{rk}\mathrm{MW}(X/\overline{\mathbf Q}(T))=1$ (same proposition).

**Classification**: explanatory addition, **plus** a new, fully independent base-field rank determination (not previously stated in any form, for either surface).

**Proposed text**:

> **Remark (quadratic-twist reading of the Gateway relation, and both surfaces' rank over $\mathbf Q(t)$).** Dehomogenizing $P_{II}$ via $x_1{=}1$ and completing the cube exactly as for Class I (Proposition~\ref{prop:X}'s own procedure, applied verbatim to Class II's own quintic) gives Class II's own minimal model, with invariants satisfying $c_4^{II}=c_4^{I}$, $c_6^{II}=-c_6^{I}$, $\Delta^{II}=\Delta^{I}$ — exactly the classical law for a quadratic twist by $-1$. An explicit translation ($X\mapsto X+T(T{+}1)^2$ in Class II's own completed coordinate) identifies Class II's model with the standard twist $Y^2=-(X^3{+}a_2X^2{+}a_4X)$ of $X$, over $\mathbf Q(t)$ itself, with no further extension.
>
> This resolves the base-field rank question left implicit by Proposition~\ref{prop:picard}: since $\sigma(P_1)=-P_1$ for $\sigma$ the nontrivial element of $\operatorname{Gal}(\mathbf Q(i)/\mathbf Q)$ (the group-law inverse $(X,Y)\mapsto(X,-Y)$ applied to $P_1$'s manifestly real $X$-coordinate and purely imaginary $Y$-coordinate), $\mathrm{MW}(X/\overline{\mathbf Q}(t))\otimes\mathbf Q$ — one-dimensional, spanned by $[P_1]$ — has $\sigma$ acting by $-1$, so its $\sigma$-invariants vanish: $\operatorname{rk}\mathrm{MW}(X/\mathbf Q(t))=0$ exactly (sharpening "no $\mathbf Q(t)$-rational point of height $1$" to a statement covering every height). Transporting $P_1$ through the twist identification above gives, in Class II's own native coordinates, the point $\bigl(u,Y\bigr)=\bigl(-\tfrac{T^2+T-1}{T},\,-\tfrac{(T-1)(T+1)}{T}\bigr)$ — verified to lie on Class II's own defining equation, with no $i$ in either coordinate, hence $\mathbf Q(t)$-rational; its height equals $P_1$'s (height is preserved by the $\mathbf Q(t)$-isomorphism just exhibited), hence non-torsion. **Consequently $\operatorname{rk}\mathrm{MW}(X_{II}/\mathbf Q(t))=1$ exactly, the opposite of $X$'s own rank $0$ over the same field** — the two surfaces, isomorphic over $\mathbf Q(i)(t)$, are genuinely different over $\mathbf Q(t)$ itself.

**Restriction**: none remaining — the prior round's compatibility caveat is closed (`PROOF_CLOSURE.md` §3).

---

## D. Fiber-to-rank explanation, with limitations

**Target**: both manuscripts' Picard-rank sections, as a joint remark.
**Hypotheses**: Shioda–Tate, the Hodge bound $\rho\le20$.
**Classification**: explanatory addition.
**Restriction**: unchanged; the one-clause addition proposed in the prior round (rank over any subfield $\le$ geometric rank, settling Class III's $\mathbf Q(t)$-rank with no separate argument) still applies and is retained.
*(Text unchanged from the prior round — see `PROPOSED_INSERTIONS_REVISED.md` §D, with its italicized clause included.)*

---

## E. Characteristic restriction — CLOSED this round, generalized and corrected

**Target**: `manuscript/hypercuboid_character_sums.tex`, Appendix "Weierstrass model and Kodaira classification," following the $(\operatorname{ord}c_4,\operatorname{ord}c_6,\operatorname{ord}\Delta)$ table.

**Hypotheses**: the family as given; $p$ an odd prime (the ambient hypothesis already in force throughout the manuscript).

**Classification**: repair of an omitted justification (confirms, via an actual local classification argument rather than a valuation-table lookup, that every stated Kodaira type is correct at every odd prime — no type changes anywhere).

**Proposed text**:

> **Remark (validity at every odd prime, with the $p=3$ case treated in full).** The classification above extends, fiber by fiber, to every odd prime $p$, by three separate arguments, none a prime-by-prime search: the $I_2$ fiber at $t=1$ is multiplicative reduction (Tate's algorithm, Step 2), valid at every residue characteristic unconditionally; the $I_2^*$ fibers at $t=0,\infty$ are potentially multiplicative reduction ($v(j)=-2$ at both, checked directly), stabilized by a ramified quadratic extension, tame — hence unaffected in type — at every $p\ne2$; the $I_0^*$ fiber at $t=-1$ has $j=1728$ exactly (an extra-automorphism locus requiring particular care, since the standard shortcut table for curves $y^2=x^3+Ax$ is stated only for $p>3$), resolved by running Tate's algorithm's own Step 6 directly: the discriminating cubic is $Y(Y-1)(Y+1)$, with discriminant the fixed integer $4$, nonzero — hence distinct roots, hence type $I_0^*$ confirmed — at every odd prime, $p=3$ included. Individual valuations $\operatorname{ord}(c_4),\operatorname{ord}(c_6)$ at $t=-1$ do shift under reduction mod $3$ specifically (from $2,4$ to $4,6$, a coincidence of the auxiliary factors $t^2{-}t{+}1$ and $t{-}2$ collapsing onto $(t{+}1)$ mod $3$ only), but this affects neither $\operatorname{ord}(\Delta)$, nor minimality (Kraus's criterion is never triggered, since $\operatorname{ord}(\Delta)=6<12$ regardless), nor the type itself, as just shown directly. All four of Classes I/II's own bad fibers are unaffected in type at $p=3$; the analogous statement for Class III's three bad fibers (all potentially multiplicative, no $j=0/1728$ subtlety, verified the same way) holds identically. $p=2$ remains outside this remark's scope, excluded for the independently-documented reasons given elsewhere in this paper (bad-fiber-location collision; the ramification-index-$2$ twists used above are wild, not tame, at $p=2$).

**Restriction**: explicitly **excludes $p=2$** (as stated in the text itself, consistent with the rest of the manuscript). Valid for **every odd prime**, not merely $p=3$ — this generalization rests on citable theorems (Tate's algorithm, the potentially-multiplicative/good dichotomy) plus two fixed-integer factorizations ($16=2^4$; $\operatorname{disc}(Y^3-Y)=4$), not on checking additional primes individually; no claim beyond what these arguments support is made.

---

## Final recommendation

**READY FOR INTEGRATION.**

Every insertion (A–E) is now supported by a complete, checked argument, with every previously-open caveat (the $p=3$ fiber classification beyond node/cusp; the base-field rank of both surfaces; the identification of the abstract twist with Class II's actual model) resolved in this round (`PROOF_CLOSURE.md`, §§1–3). No mathematical issue remains open. The only items left to the authors are style/scope decisions already noted in the prior round (whether B and D's added exposition length is worth including alongside the existing longer proofs) — not correctness questions.
