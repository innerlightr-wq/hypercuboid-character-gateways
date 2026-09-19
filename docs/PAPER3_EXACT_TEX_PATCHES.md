# Paper 3 — exact TeX patches

Edits only. Reasoning lives in [`PAPER3_MAC_REVISION_PACKET.md`](PAPER3_MAC_REVISION_PACKET.md).

Target: `class_iii/manuscript/class3_hypercuboid_k3.tex` (line numbers as of commit `b8e6cff`).
Work top-down; line numbers below the first insertion will drift, so locate by the quoted OLD TEXT, not
by line number alone.

---

## PATCH 0 — verify only

**STATUS** ALREADY APPLIED in `b8e6cff`. **LOCATION** §2.1 and the bibliography.

Confirm both are present before starting, then move on:

1. `\bibitem{Collapse2026}` exists, after `\bibitem{Huber}`;
2. §2.1's opening reads `...whose notation we follow exactly; the underlying collapse mechanism is
   \cite{Collapse2026}, Theorem~3.1)...`.

**NUMBERING** none. **CITATIONS** none new.

---

## PATCH 1 — `S_4` orbit count

**STATUS** REQUIRED. **LOCATION** §2.1, lines 138–142.

**OLD TEXT**
```
A_4=-(x_0+x_1+x_2)$. The natural $S_4$-symmetry permuting $A_1,\dots,A_4$
acts on the seven six-element subsets of these seven forms with exactly
three orbits, giving the three character-sum classes $\Sigma_I,\Sigma_{II},
\Sigma_{III}$. Classes I and II each omit a form associated to a
\emph{singleton}-type element of the permutation action; Class~III omits
```

**NEW TEXT**
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
Classes I and II each omit a form associated to a
\emph{singleton}-type element of the permutation action; Class~III omits
```

**CITATIONS** `\cite{ClassesI_II}` (already present in the bibliography).
**NUMBERING** none. **CROSS-REFS** none.

---

## PATCH 2 — non-isomorphism, over `Q`

**STATUS** REQUIRED. **LOCATION** §9 ("Comparison with Classes I/II"), lines 1213–1217.

**OLD TEXT**
```
\cite{AOP2002}'s own surface at $\lambda=8$ has a different Weierstrass
model and fiber configuration from $X_{\rm III}$, and the two are provably
non-isomorphic (the two-variable sums $T(p)$ and $A(8,p)$ disagree at
essentially every tested prime); possibilities (iii) and (vi) do not
apply.
```

**NEW TEXT**
```
\cite{AOP2002}'s own surface at $\lambda=8$ has a different Weierstrass
model and fiber configuration from $X_{\rm III}$, and the two are
non-isomorphic over $\Q$, for a structural reason requiring no numerical
search. Since $\lambda+1=9$ is a square, $\chi(9)=1$ for every odd $p$,
so \cite{AOP2002}'s evaluation reads $A(8,p)=a(8,p)^2-p$; at
$p\equiv3\pmod4$ the inner sum $a(8,p)$ vanishes, giving $A(8,p)=-p\neq0$,
whereas $T(p)=0$ for exactly those $p$ by
Proposition~\ref{prop:involution}. The two affine surfaces therefore have
different numbers of $\Fp$-points at every prime $p\equiv3\pmod4$, all of
which are primes of good reduction for both; hence they are not isomorphic
over $\Q$, and a fortiori not isomorphic as elliptic surfaces over
$\Q(T)$. Over $\overline\Q$ we make no such claim: both are singular K3
surfaces with transcendental lattice of discriminant $4$, which does not
distinguish them. Possibilities (iii) and (vi) do not apply.
```

**CITATIONS** none new. **NUMBERING** none. **CROSS-REFS** adds `\ref{prop:involution}` (label exists).

**Note.** If the surrounding sentence elsewhere says "not isomorphic **or birational**", delete
"or birational" — the argument does not address birational maps and the clause is not needed.

---

## PATCH 3 — Livné → every odd prime

**STATUS** REQUIRED. **LOCATION** §6, immediately after the "Hypothesis check for `$X_{\rm III}$`"
paragraph (insert after line ~868, before `\subsection{Identifying the candidate newform}`).

**OLD TEXT** — none; this is an insertion.

**NEW TEXT**
```
\begin{remark}[From ``almost all'' to every odd prime]
\label{rem:chebotarev}
Theorem~\ref{thm:livne} gives the trace identity only for almost all
primes of good reduction, whereas Theorem~\ref{thm:trans-trace} asserts it
for every odd $p$. The upgrade is standard. The representations
$\rho_T$ on $T(X_{\rm III})\otimes\Q_\ell$ and $\rho_f$ attached to $f$
are both $2$-dimensional and semisimple, and both are unramified outside
$\{2\}$: $\rho_T$ because $X_{\rm III}$ has good reduction at every odd
prime (Section~\ref{sec:badprimes}), and $\rho_f$ because $f$ has
$2$-power level. Two semisimple $\ell$-adic representations whose traces
agree on a set of primes of density $1$ have isomorphic semisimplifications,
by the Chebotarev density theorem together with the Brauer--Nesbitt theorem
\cite{Serre1997}; isomorphic representations have equal Frobenius traces at
every unramified prime. Since every odd prime is unramified for both, the
identity holds at every odd $p$, with no exceptional set.
\end{remark}
```

**CITATIONS** new `\bibitem{Serre1997}` — see Patch 14.
**NUMBERING** **one** printed number changes: the "Known vs. proved" remark goes `6.2 → 6.3`. The new
remark becomes `6.2`. Nothing in §7 onward moves (the counter resets per section).
**CROSS-REFS** uses `thm:livne`, `thm:trans-trace`, `sec:badprimes` — all exist.

---

## PATCH 4 — "singular K3" at first use

**STATUS** RECOMMENDED. **LOCATION** §1, at the first body occurrence (line ~52, "...realized, via an
explicit singular K3 surface, in terms of..."). If Patch 5 is applied first, fold this in there instead.

**NEW TEXT** (insert as a following sentence)
```
Throughout, ``singular K3 surface'' is used in the standard
arithmetic-geometric sense of a K3 surface whose geometric Picard number
attains the maximum $20$ \cite{ShiodaInose1977}; the surfaces in question
are smooth projective, and the affine models from which they are
constructed are not.
```

**CITATIONS** `\cite{ShiodaInose1977}` (present). **NUMBERING** none.

---

## PATCH 5 — introduction opening

**STATUS** RECOMMENDED. **LOCATION** §1, replacing the first three paragraphs (from "This paper is a
sequel to..." up to "...the genuine open problem of that paper."). Keep that paragraph as the fourth.

**NEW TEXT** — see `PROPOSED REVISED INTRODUCTION OPENING` in the packet; reproduced there in full.

**CITATIONS** `\cite{AOP2002}` (present). **NUMBERING** none.
**CROSS-REFS** uses `\ref{sec:AOP-precise}` — **confirm this label exists**; if the section carries a
different label, substitute it.

---

## PATCH 6 — self-contained Class III definition

**STATUS** RECOMMENDED. **LOCATION** §2, immediately after Definition 2.1 (line ~148ff).

**NEW TEXT** — see `CLASS III FOR AN OUTSIDE READER` in the packet.

**CITATIONS** none. **NUMBERING** none (plain prose, not an environment).

---

## PATCH 7 — graph-rigidity exposition

**STATUS** RECOMMENDED. **LOCATION** §5, as a short orienting paragraph before Lemma 5.7
(`lem:rigidity`, line ~618).

**NEW TEXT** — the MAIN-TEXT VERSION in the packet. Keep the existing Lemma, proof, and the remark
recording the exhaustive `5040`-permutation check **verbatim**, including its bold sentence saying the
computation is a check and not the proof.

**CITATIONS** none. **NUMBERING** none (prose only).

---

## PATCH 8 — NS saturation

**STATUS** RECOMMENDED. **LOCATION** §5, in "Lattice consequences" (line ~761).

**NEW TEXT** — the `NS` saturation paragraph in the packet.

**CITATIONS** `\cite{Shioda1990}` (present). **NUMBERING** none.

---

## PATCH 9 — transcendental lattice and CM

**STATUS** RECOMMENDED. **LOCATION** §6, before the Livné theorem (line ~800–845).

**NEW TEXT** — the transcendental-lattice and CM paragraphs in the packet.

**CITATIONS** `\cite{ShiodaInose1977}` (present). **NUMBERING** none.

---

## PATCH 10 — eta-product presentation

**STATUS** RECOMMENDED. **LOCATION** §6, "Identifying the candidate newform" (line ~871 onward).

**NEW TEXT** — SR 2's wording in the packet: the form is introduced as
`f(z)=\eta^6(4z)=q\prod_{n\ge1}(1-q^{4n})^6=\sum a_nq^n`, with weight, level, Nebentypus and CM field
given, the LMFDB label secondary, and the explicit note that `f` is singled out on structural grounds
before any coefficient is compared.

**CITATIONS** none new. **NUMBERING** none.

---

## PATCH 11 — AOP comparison

**STATUS** RECOMMENDED. **LOCATION** §9, the six-possibility discussion (lines ~1200–1232).

**NEW TEXT** — keep the existing structure; apply Patch 2 inside it, and adopt the wording of
`EXACT RELATION TO AHLGREN--ONO--PENNISTON` in the packet for the surrounding claims.

**CITATIONS** `\cite{AOP2002}`, `\cite{Huber}` (both present; `Huber` corrected in Patch 14).
**NUMBERING** none.

---

## PATCH 12 — abstract

**STATUS** RECOMMENDED. **LOCATION** the `abstract` environment (lines 37–39).

**NEW TEXT** — `PROPOSED REVISED ABSTRACT` in the packet, in full.

**CITATIONS** none (the abstract cites no keys). **NUMBERING** none.

---

## PATCH 13 — discussion / conclusion

**STATUS** RECOMMENDED. **LOCATION** §10 "Discussion" (lines 1234–1254).

**NEW TEXT** — `PROPOSED REVISED CONCLUSION` in the packet. Two changes only: lead with the result, and
carry Patch 2's field qualification.

**CITATIONS** `\cite{ClassesI_II}`, `\cite{AOP2002}` (present). **NUMBERING** none.

---

## PATCH 14 — bibliography

**STATUS** REQUIRED (Huber correction) + REQUIRED (Serre addition, if Patch 3 is applied).

### 14a — correct the Huber entry

**OLD TEXT**
```
\bibitem{Huber}
T.~Huber, Z.-G.~Liu, et al., \emph{On the vanishing of the coefficients
of CM eta quotients}, preprint. Independent literature confirmation
(outside \cite{AOP2002}) that $\eta^6(4z)=\texttt{16.3.c.a}$ is a CM
newform by $\Q(i)$, there associated with the quartic Fermat K3 surface
-- a \emph{third} variety, distinct from both $X_8$ and $X_{\rm III}$,
sharing the same trace formula (Remark~\ref{rem:known-vs-proved}).
```

**NEW TEXT**
```
\bibitem{Huber}
T.~Huber, C.~Liu, J.~McLaughlin, D.~Ye, M.~Yuan, S.~Zhang, \emph{On the
vanishing of the coefficients of CM eta quotients}, Proc. Edinburgh Math.
Soc. \textbf{66} (2023), no.~4, 1202--1216,
\url{https://doi.org/10.1017/S0013091523000627}. Independent literature
confirmation (outside \cite{AOP2002}) that $\eta^6(4z)=\texttt{16.3.c.a}$
is a CM newform by $\Q(i)$, there associated with the quartic Fermat K3
surface -- a \emph{third} variety, distinct from both $X_8$ and $X_{\rm
III}$, sharing the same trace formula
(Remark~\ref{rem:known-vs-proved}).
```

Two corrections: the work is **published**, not a preprint; and the second author is **C. (Chang) Liu**,
not "Z.-G. Liu" — a different mathematician. Verified against registered DOI metadata.

### 14b — add Serre (only if Patch 3 is applied)

**NEW TEXT** — append after `\bibitem{Collapse2026}`
```
\bibitem{Serre1997}
J.-P.~Serre, \emph{Abelian $\ell$-Adic Representations and Elliptic
Curves}, A K Peters, Wellesley, MA, 1997 (originally Benjamin, New York,
1968), \url{https://doi.org/10.1201/9781439863862}. Cited for the standard
fact that semisimple $\ell$-adic representations with equal Frobenius
traces on a density-one set of primes are isomorphic (Chebotarev together
with Brauer--Nesbitt), used in Remark~\ref{rem:chebotarev}.
```

**NUMBERING** the bibliography gains one entry, becoming `[12]`; existing `[1]`–`[11]` are unchanged
because both additions are appended at the end.

---

# Order

0 (verify) → 1 → 2 → 3 → 14a → 14b → 4 → 5 → 6 → 7 → 8 → 9 → 10 → 11 → 12 → 13.

Required first (1, 2, 3, 14), then the expository ones. Doing 14 early means the build never runs with a
dangling `\cite{Serre1997}`.

# After the last patch

Build twice, then confirm: Main Theorem prints as **8.6**, Exact transcendental trace as **7.5**, the
"Known vs. proved" remark as **6.3**, the new Chebotarev remark as **6.2**, and the bibliography has
**12** entries. Then run the rest of `MAC BUILD AND PDF CHECKLIST`.
