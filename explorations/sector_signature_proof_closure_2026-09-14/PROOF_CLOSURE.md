# Proof closure — characteristic-3 fiber justification, rank-zero descent, and Class II's actual model

Repository: `/Users/eliasdejesus/Desktop/hypercuboid-character-gateways`, branch `main`, clean except pre-existing untracked `explorations/` (all five prior audit subdirectories present, untouched — see `git status`). No tracked file modified, no commits, no push, no manuscript edits, no Lean. No `AGENTS.md` exists (checked again). New work: `explorations/sector_signature_proof_closure_2026-09-14/{01_full_tate_classification.py, 02_tate_algorithm_step6_check.py, 03_class_II_full_weierstrass_chain.py, PROOF_CLOSURE.md, INSERTIONS_FINAL.md}`.

**Inputs read**: `explorations/sector_signature_final_check_2026-09-14/FINAL_VALIDATION.md`, `explorations/sector_signature_validation_2026-09-14/PROPOSED_INSERTIONS_REVISED.md` (target of this round's corrections), plus the manuscript sections already cited in prior rounds (Weierstrass models, Proposition "Picard rank and lattices," the Gateway relation).

---

## 1. Complete characteristic-3 fiber justification

**Commands**: `python3 01_full_tate_classification.py`, `python3 02_tate_algorithm_step6_check.py`.

### 1.1 The multiplicative fiber ($T=1$, Classes I/II only): Tate Step 2

Local equation: $Y^2=X^3+a_2(T)X^2+a_4(T)X$ at $T=1$; local parameter $\pi=(T-1)$. **Script `01` Step 1** verifies $v_{T=1}(a_2)=0$ at both $\mathbf Q$ and mod 3 — $a_2$ is a unit, so $b_2=4a_2$ is a unit, which is Tate's Step 2 criterion for **non-additive** reduction: type $I_n$, $n=v(\Delta)$ directly, **with no further step and no characteristic restriction whatsoever** (this step never involves ramification — split/nonsplit multiplicative reduction differ only by an unramified twist, changing neither the type label nor the conductor). Result: $n=2$ at both $\mathbf Q$ and mod 3. **Minimality**: the discriminant valuation ($2$) is already far below the Kraus threshold ($v(\Delta)\ge12$), confirmed in the prior round and unaffected here.

### 1.2 The potentially-multiplicative fibers ($T=0,\infty$ both sectors; $T=-1$, Class III)

**Theorem used** (classical Kodaira–Néron / Tate-curve theory, characteristic-independent in its statement — e.g. Silverman, *Advanced Topics in the Arithmetic of Elliptic Curves*, V.5): additive reduction with $v(j)<0$ is **potentially multiplicative**, and the field stabilizing it (making the reduction actually multiplicative) is always a **ramified quadratic extension** — because the reduction is (a twist of) a Tate curve, whose automorphism group over the algebraic closure is exactly $\{\pm1\}$, with no further enhancement possible. The resulting type is $I_n^*$, $n=-v(j)=v(\Delta)-6$ (matching the $I_n^*$ definition once minimality is confirmed). **This mechanism never involves the $j=0,1728$ automorphism-enhancement subtlety** — that subtlety is specific to *potentially good* reduction (§1.3).

**`01` Step 2** computes $v(j)=3v(c_4)-v(\Delta)$ at every such point, over $\mathbf Q$ and mod 3: **every one gives $v(j)=-2$ identically, at both fields**, hence $n=2$, type $I_2^*$, matching the characteristic-0 label exactly. (At $T=-1$, Class III, and at $T=0,\infty$, Class I/II, $v(c_4)$ itself does *not* shift mod 3 — only $T=-1$ for Classes I/II, handled separately below, shows the $c_4,c_6$ valuation jump.)

**Tameness / wild contribution**: the stabilizing extension has ramification index **exactly 2** (not "$\le2$" or inferred from a table) — established by the theorem's own mechanism (a Tate curve's automorphism group is $\{\pm1\}$, order 2, full stop). Tame $\iff p\nmid2\iff p\ne2$. At $p=3$: tame, **wild part $=0$** (the extension itself accounts for the entire ramification; there is no residual wild sub-extension). Cross-check via Ogg's formula $v(\Delta)=f_p+m_p-1$: for $I_2^*$ ($m_p=7$ components), $f_p=8-6=2$ — the standard conductor exponent for potentially multiplicative reduction at any tame prime, confirming no wild contribution.

### 1.3 The one potentially-good fiber ($T=-1$, Classes I/II): the genuine char-3 check

**Script `01` Step 3** finds $j(T=-1)=1728$ **exactly, over $\mathbf Q$** — the curve hits the extra-automorphism locus ($\operatorname{Aut}=\mathbf Z/4$ generically), and $1728\equiv0\pmod3$ coincides with $j=0$'s residue mod 3 (a genuine characteristic-3 coincidence, checked directly, not assumed away). **The standard $y^2=x^3+Ax$ shortcut table is explicitly stated only for $p>3$ in the literature — it does not apply here without independent verification.**

**Resolution — Tate's algorithm Step 6, run explicitly** (`02_tate_algorithm_step6_check.py`), not the $j$-invariant/table shortcut: local equation at $T=-1$ (local parameter $\pi=T+1$) has $a_2,a_4$ both vanishing there already (verified: $(T+1)^2\mid a_2$ and $(T+1)^2\mid a_4$, so the origin is already the singular point, Step 2 trivial), $a_6=0$ so $\pi^3\mid b_8=-a_4^2$ (types II, III ruled out directly, both fields) and $\pi^3\mid b_6=0$ (type IV ruled out). Step 6's discriminating cubic is
$$P(Y)=Y^3+a_2'Y^2+a_4'Y,\qquad a_2'=a_2/\pi,\ a_4'=a_4/\pi^2,$$
computed exactly: $P(Y)=Y^3-Y=Y(Y-1)(Y+1)$ — **the same fixed cubic over both $\mathbf Q$ and mod 3**, with $\operatorname{disc}(P)=4$ (over $\mathbf Q$) and $\equiv1\pmod3$ (nonzero). **Distinct roots at both fields** $\Rightarrow$ Tate's algorithm **terminates at Step 6/7 with type $I_0^*$**, unconditionally — no further step is needed, and the $j=1728$/enhanced-automorphism concern is resolved directly by the algorithm itself rather than sidestepped.

**Bonus generalization, stated carefully**: $\operatorname{disc}(P)=4$ is a *fixed integer*, vanishing only at $p=2$ — so this Step-6 argument in fact certifies type $I_0^*$ at **every odd prime**, not merely $p=3$; this is a structural fact about the fixed cubic $Y^3-Y$, not a prime-by-prime sweep (see §1.5).

**Wild contribution**: ramification index of the stabilizing extension is again exactly 2 (a quadratic twist, standard for $j\ne0$ potentially-good curves reached this way — confirmed, not merely asserted, by Step 6 terminating with a *distinct-root* cubic, which is precisely the criterion Tate's algorithm uses to confirm the $I_0^*$/quadratic-twist case rather than continuing toward the quartic/sextic-twist types II\*,III\*,IV\*). Tame at $p=3$ ($p\nmid2$); Ogg check: $m_p=5$ for $I_0^*$, $f_p=6-4=2$, matching the tame value.

### 1.4 Reconciling "four mixed vs. three uniform" with the prior round's insertion text

**Checked directly** (`grep` across all prior reports, recorded here): the phrase "the four bad fibers" in `PROPOSED_INSERTIONS_REVISED.md`'s Insertion E appears **only** in the remark targeted at `manuscript/hypercuboid_character_sums.tex` (Classes I/II's own paper), which genuinely has four bad points ($T=0,1,-1,\infty$). It is **not** a claim that Class III also has four — Class III's own three points ($T=0,-1,\infty$) are correctly described elsewhere (`FINAL_VALIDATION.md`'s table lists them as three, combined into one row since their data is identical). **No discrepancy exists**; this was a scoping-clarity issue (the sentence, read in isolation from its target-manuscript header, could be misread as covering both sectors). **Corrected in `INSERTIONS_FINAL.md`** below by writing "Classes I/II's own four bad fibers" explicitly, removing the ambiguity.

### 1.5 Exact characteristic range of Insertion E

**Stated precisely, not left implicit**: the fiber-type classification (§1.1–1.3) is valid at **every odd prime $p$**, by the following non-sweep argument:
- Bad-point locations ($\{0,1,-1\}$ or $\{0,-1\}$) remain pairwise distinct mod $p$ for every odd $p$ (their pairwise differences are the fixed integers $1,2,1$; only $p=2$ divides any of them) — elementary, checked once, not per-prime.
- The leading coefficient of $\Delta$ is the fixed integer $16=2^4$; nonzero mod $p$ for every odd $p$ — elementary, checked once.
- §1.1's argument (multiplicative point) is characteristic-free.
- §1.2's argument (potentially-multiplicative points) needs only $p\ne2$ for tameness — a general theorem, not a per-prime check.
- §1.3's argument (the one potentially-good point) reduces to the fixed integer $\operatorname{disc}(Y^3-Y)=4$, nonzero for every odd $p$.

**$p=3$ is not distinguished by the fiber-type conclusion** (identical to characteristic 0 everywhere) — it is distinguished only by the *intermediate*, type-irrelevant fact that $\operatorname{ord}(c_4),\operatorname{ord}(c_6)$ individually shift at $T=-1$ specifically at $p=3$ (traced, in the prior round, to the coefficients $24,216$ in the $c_4,c_6\to a_2,a_4$ formulas both being divisible by 3 — a fact about *this specific family's auxiliary quantities*, not about the classification theorem). This is **not promoted beyond what is proved**: the "every odd $p$" claim rests on citable theorems plus two fixed-integer factorizations, not on checking primes one at a time; it is recorded as a genuine generalization, separate from (and not requiring) any further per-prime sweep.

**$p=2$**: explicitly excluded, for the *already-documented, independent* reasons (bad-point collision at $p=2$; the ramification index-2 twists of §1.2/§1.3 are wild, not tame, at $p=2$) — not re-derived in this round, correctly out of scope here.

---

## 2. The original-surface rank-zero descent, made complete

**Commands**: reuses `explorations/sector_signature_final_check_2026-09-14/02_field_scope_of_twist_and_rank.py` (§1–2 of that script; not re-run, since nothing there needs correction — cited).

**The curve and fields, named exactly**: $X_T:\ Y^2=X^3+a_2(T)X^2+a_4(T)X$, $a_2=T(T+1)^2,a_4=T^3(T+1)^2$, defined over $\mathbf Q(T)$. Fields in play: $\mathbf Q(T)\subset\mathbf Q(i)(T)\subset\overline{\mathbf Q}(T)$.

**$P_1$'s coordinates and non-torsion status**: $P_1=(-(T{+}1),\,i(T{-}1)(T{+}1)^2)$, verified on the curve (prior round, re-cited not re-run: `sp.simplify(Y_1^2 - (X_1^3+a_2X_1^2+a_4X_1))==0`). Non-torsion: height $\hat h(P_1)=1\ne0$ (Shioda's height-pairing computation, in the manuscript's own Proposition "Picard rank and lattices," not re-derived here — cited).

**Geometric rank established independently**: $\operatorname{rk}\operatorname{Triv}(X)=19$ (Kodaira fiber data, now *fully* justified through §1's complete Tate-algorithm argument, not merely the node/cusp shortcut) $+$ the universal Hodge bound $\rho(X_{\overline{\mathbf Q}})\le20$ (a fact about K3 surfaces in general, not about $X$) $+$ $\hat h(P_1)\ne0\Rightarrow\operatorname{rk}\mathrm{MW}(X/\overline{\mathbf Q}(T))\ge1$, sandwiched to $=20,=1$ exactly. **Independent** in the precise sense that neither the ceiling nor the floor uses the other; this is unchanged from the prior rounds, restated here with §1's now-complete fiber justification underpinning $\operatorname{rk}\operatorname{Triv}=19$.

**Conjugation as a group-law statement**: for a curve in the reduced form $Y^2=X^3+a_2X^2+a_4X+a_6$ ($a_1=a_3=0$), the inverse of a point $(X,Y)$ under the group law is $(X,-Y)$ — the standard, elementary inverse formula for this Weierstrass shape (no computation needed; it is the definition of the group law for a curve with no $XY$ or $Y$-linear term). Since $\sigma(X(P_1))=X(P_1)$ (real coefficients) and $\sigma(Y(P_1))=-Y(P_1)$ (verified symbolically, prior round), **$\sigma(P_1)=(X(P_1),-Y(P_1))=-P_1$ is a literal group-law statement**, not merely a coordinate observation.

**The descent argument on $\mathrm{MW}\otimes\mathbf Q$** (a rational vector space — no primitive integral generator needed, per the task's own allowance): $\mathrm{MW}(X/\overline{\mathbf Q}(T))\otimes\mathbf Q$ is $1$-dimensional (rank 1, established above), spanned by the class of $P_1$ (nonzero in $\mathrm{MW}\otimes\mathbf Q$ since $P_1$ is non-torsion). $\operatorname{Gal}(\mathbf Q(i)/\mathbf Q)=\{1,\sigma\}$ acts $\mathbf Q$-linearly on $\mathrm{MW}(X/\mathbf Q(i)(T))\otimes\mathbf Q$ (a sub-$\mathbf Q$-vector-space of the same 1-dimensional space, hence equal to it since $P_1\in\mathrm{MW}(X/\mathbf Q(i)(T))$); $\sigma$ acts on the spanning class $[P_1]$ by $\sigma[P_1]=[-P_1]=-[P_1]$, i.e. as multiplication by $-1$ on this $1$-dimensional space. The **Galois-invariant subspace** $\bigl(\mathrm{MW}(X/\mathbf Q(i)(T))\otimes\mathbf Q\bigr)^\sigma$ is exactly the $(+1)$-eigenspace of "multiplication by $-1$" on a $1$-dimensional $\mathbf Q$-vector space, which is $\{0\}$ (since $2\ne0$ in $\mathbf Q$). By Galois descent, $\mathrm{MW}(X/\mathbf Q(T))\otimes\mathbf Q=\bigl(\mathrm{MW}(X/\mathbf Q(i)(T))\otimes\mathbf Q\bigr)^\sigma=\{0\}$, i.e. $\operatorname{rk}\mathrm{MW}(X/\mathbf Q(T))=0$ **exactly**.

**Rank zero $\ne$ no rational points**: the manuscript's own torsion lemma (Lemma "Mordell–Weil torsion," prior rounds, not re-derived) already establishes $\mathrm{MW}(X/\mathbf Q(T))_{\mathrm{tors}}\supseteq E_T[2]\cong(\mathbf Z/2)^2$ is defined over $\mathbf Q(T)$ itself (the lemma's own remark: "*This also settles the torsion over every field between $\mathbf Q(t)$ and $\overline{\mathbf Q}(t)$*"). So $\mathrm{MW}(X/\mathbf Q(T))\cong(\mathbf Z/2)^2$ **exactly** (rank $0$, full known torsion) — not the trivial group. No further torsion classification is needed or attempted (none of the $(\mathbf Z/2)^2$ points are new; they were already established, only now correctly not conflated with "no rational points").

---

## 3. Class II's actual Weierstrass model, identified with the abstract twist — completed

**Commands**: `python3 03_class_II_full_weierstrass_chain.py`, plus the follow-up invariant/translation computations recorded inline below (not saved as a separate numbered script — reused the same session's `python3 -c` calls, reproducible from the exact code blocks quoted here).

### 3.1 The complete forward chain

Starting object: Class II's own quintic, $Q_{II}(u,v)=v(u{+}1)(u{+}v)(v{+}1)(u{+}v{+}1)$ (dehomogenizing $P_{II}$ via $x_1{=}1$; $u,v$ its own native coordinates, open set $u,v\in\mathbf A^2$, no exclusion).

1. **Prefactor/cubic split** (Target 1's method, reused): prefactor $v(v{+}1)$ (matching every sector's shared shape), cubic $(u{+}1)(u{+}v)(u{+}v{+}1)$ — roots $\{-1,-v,-(v{+}1)\}$, **notably missing the "root at $0$"** every other sector's cubic has. This is Class II's own genuine structural difference, not an error.
2. **Complete the cube** (identical procedure to both other sectors, monic-checked, not assumed): $u=u_p/[v(v{+}1)]$, $Y=Y_p/[v(v{+}1)]$, giving Class II's own minimal-form coefficients
$$a_2^{II}(v)=2v(v{+}1)^2,\quad a_4^{II}(v)=v^2(v{+}1)^2(v^2{+}3v{+}1),\quad a_6^{II}(v)=v^4(v{+}1)^4\ (\textbf{nonzero}).$$
**No base-parameter change**: $v=T$ throughout (Class II's own base parameter *is* Class I's $T$, confirmed already in the prior round's affine bridge $u=-(x{+}T{+}1),\,v=T$).
3. **Invariant identification** (the decisive check): computing $(c_4,c_6,\Delta)$ from $(a_2^{II},a_4^{II},a_6^{II})$ gives, **exactly** (`sympy` identity, both directions):
$$c_4^{II}=c_4^{I},\qquad c_6^{II}=-c_6^{I},\qquad \Delta^{II}=\Delta^{I}.$$
This is precisely the classical transformation law $(c_4,c_6,\Delta)\mapsto(d^2c_4,d^3c_6,d^6\Delta)$ for a quadratic twist by $d=-1$ ($d^2{=}1,d^3{=}{-}1,d^6{=}1$) — **confirming Class II's own actual completed model is the $-1$-twist of $X$, via the standard invariants, not merely via the pre-completion affine correspondence** (which was all the prior round had shown).
4. **The explicit translation** (since $(c_4,c_6)$ determine an $a_1{=}a_3{=}0$ curve up to translation only, once matched): tried each of the cubic's three roots as a translation constant; $u_p=X_{\mathrm{new}}-T(T{+}1)^2$ (i.e. translating by the root $-T(T{+}1)^2$) gives **exactly** $(a_2,a_4,a_6)=(-a_2^I(T),\,a_4^I(T),\,0)$ — matching, term for term, the abstract twist's standard form. **No further scaling ($u\ne1$) or denominator is needed** — this is a pure translation.

**Summary of the full chain** (forward, $x,T\to$ the abstract-twist presentation $(X,Y)$):
$$u=-(x{+}T{+}1)\ \xrightarrow{\times T(T+1)}\ u_p \ \xrightarrow{\ -T(T+1)^2\ }\ X_{\mathrm{new}}=u_p+T(T{+}1)^2\ \xrightarrow{\ \text{sign}\ }\ X=-X_{\mathrm{new}},$$
with $Y$ tracked correspondingly ($Y\mapsto Y\cdot T(T{+}1)$ under the cube-completion scaling, unchanged by translation and by the $X$-only sign flip). Every step's constant is a polynomial in $T$ over $\mathbf Z$ — **no square root, no $i$, no further twist** anywhere in the chain.

### 3.2 Transporting $P_1$ through the complete chain

Starting from the already-verified transported point on the abstract twist, $(X,Y)=(-(T{+}1),\,-T^3{-}T^2{+}T{+}1)$ (prior round), traced **backward** through every step of §3.1's chain (inverse translation, inverse scaling, inverse affine bridge) gives Class II's own native coordinates:
$$u=\frac{-(T^2{+}T{-}1)}{T},\qquad Y_{\mathrm{native}}=\frac{-(T{-}1)(T{+}1)}{T}.$$

**Verified directly** (not inferred): $Y_{\mathrm{native}}^2=Q_{II}(u,T)$ **exactly** (both sides equal $(T{-}1)^2(T{+}1)^2/T^2$, `sympy` identity) — the point lies on Class II's own *original* quintic, and also on Class II's own *completed* Weierstrass model (checked separately, exact identity). **No $i$ appears anywhere** in $u$ or $Y_{\mathrm{native}}$ — genuinely $\mathbf Q(T)$-rational (as a point with coordinates in the *function field* $\mathbf Q(T)$; the pole at $T=0$ is an ordinary feature of a rational function, not an obstruction to rationality over $\mathbf Q(T)$).

**Height / non-torsion**: every map in the §3.1 chain (translation, the cube-completion scaling by the unit-at-generic-$T$ quantity $T(T{+}1)$, the $X$-only sign flip) is an **isomorphism of elliptic curves over $\mathbf Q(T)$ itself** (no field extension anywhere in the chain — contrast with the twist map $(X,Y)\mapsto(X,iY)$ used earlier, which *does* need $\mathbf Q(i)$). Height is invariant under any such isomorphism (standard; the height pairing is defined via intersection theory on the elliptic surface, unaffected by a $\mathbf Q(T)$-isomorphism of Weierstrass models). Hence the transported point has height $1\ne0$: **non-torsion**, confirmed by the same height-invariance argument used in the prior round, now applying to a genuine $\mathbf Q(T)$-isomorphism rather than the abstract twist alone.

### 3.3 Conclusion: the identification is complete, the caveat is resolved

The prior round's caveat ("not independently re-verified... whether this affine isomorphism extends... through the completing-the-cube step") is **resolved**: §3.1's invariant computation ($c_4,c_6,\Delta$ matching the exact $-1$-twist law) and explicit translation **prove** Class II's own actual Weierstrass model is isomorphic, over $\mathbf Q(T)$, to the abstract twist $X^{(-1)}$. **The rank-1-over-$\mathbf Q(T)$ result may now be attributed directly to "Class II's own surface" by name**, not only to "the abstract twist of $X$."

---

## Final table: fiber types and rank claims, each with its field and hypotheses

| Claim | Field / hypotheses | Status |
|---|---|---|
| $I_2$ at $T{=}1$ (I/II) | any residue characteristic (Tate Step 2, unconditional) | proved, §1.1 |
| $I_2^*$ at $T{=}0,\infty$ (I/II); $T{=}0,-1,\infty$ (III) | potentially multiplicative, tame iff $p\ne2$; proved at every odd $p$ | proved, §1.2 |
| $I_0^*$ at $T{=}-1$ (I/II) | potentially good, $j{=}1728$; Tate Step 6, proved at every odd $p$ via the fixed cubic $Y^3{-}Y$ | proved, §1.3 |
| All types unchanged at $p=3$ specifically (and every odd $p$) | as above | proved, §1 |
| $p=2$ | excluded (bad-point collision; wild ramification of the needed twists) | out of scope, documented |
| $\operatorname{rk}\mathrm{MW}(X/\overline{\mathbf Q}(T))=1$ | geometric rank, Shioda–Tate + Hodge bound + $\hat h(P_1)\ne0$ | proved (manuscript + §2) |
| $\operatorname{rk}\mathrm{MW}(X/\mathbf Q(i)(T))=1$ | $P_1\in\mathrm{MW}(X/\mathbf Q(i)(T))$, same ceiling | proved, §2 |
| $\operatorname{rk}\mathrm{MW}(X/\mathbf Q(T))=0$; torsion $=(\mathbf Z/2)^2$ | Galois descent on $\mathrm{MW}\otimes\mathbf Q$, $\sigma(P_1)=-P_1$ | proved, §2 |
| $\operatorname{rk}\mathrm{MW}(X_{\rm III}/\overline{\mathbf Q}(T))=0$, and over $\mathbf Q(T)$ | $\operatorname{Triv}$ rank $=20=$ ceiling; rank over any subfield $\le$ geometric rank $=0$ | proved (prior rounds) |
| $\operatorname{rk}\mathrm{MW}(X^{(-1)}/\mathbf Q(T))=1$, **as Class II's own surface** | explicit $\mathbf Q(T)$-isomorphism (§3.1), transported non-torsion point (§3.2) | proved, §3 (upgraded from "abstract twist only") |

## Corrections to earlier summaries

- **`FINAL_VALIDATION.md`'s node/cusp table** is not wrong but was **incomplete** as a full Kodaira-type justification (correctly flagged by this round's task): the exact index $n$ and the ruling-out of the exceptional types (II, III, IV and duals) needed the $j$-invariant dichotomy and, at one point, Tate's actual Step 6 — both now supplied (§1).
- **`PROPOSED_INSERTIONS_REVISED.md`'s Insertion C caveat** ("not independently re-verified... completing-the-cube compatibility") is **resolved**: §3 completes it. The insertion text in `INSERTIONS_FINAL.md` below drops the caveat and attributes the rank-1 result to Class II directly.
- **The "four bad fibers" phrasing** is clarified (§1.4) as correctly scoped to Classes I/II only; no discrepancy, wording tightened in `INSERTIONS_FINAL.md`.
- No numeric or symbolic claim from any earlier round was found to be incorrect.

## Remaining blockers

**None identified.** Every caveat flagged by the prior two rounds is resolved in this round with an explicit, verified argument.
