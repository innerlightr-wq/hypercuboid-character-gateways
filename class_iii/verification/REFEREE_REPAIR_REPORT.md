# Class III Manuscript — Referee Repair Report

Repairs the single Major Issue identified in
`EXTERNAL_REFEREE_REPORT.md` (verdict `CLASSIII-REF-B`). No other change
was made to the manuscript.

## The exact issue repaired

The referee found that Lemma 5.6's proof (four distinct legs at `T=0`)
and its transfer to `T=-1,∞` (Remark 5.9) asserted, but did not show,
that the components met by `P2` and `P3` have fiber-multiplicity exactly
1 — the tangent-cone computation demonstrating this was carried out
explicitly (Lemma 5.3) only for the component met by `P1`. The
cross-reference pointing to where the `P2/P3` computation should appear
("Appendix D") was also wrong: Appendix D contains no blow-up or
tangent-cone material at all.

## What was added

**Appendix C** now contains:

1. **Lemma C.1** (General multiplicity criterion) — proved once, in full:
   if a singular point's local equation has tangent cone `y²-cTu` for a
   nonzero constant `c` (with every other term carrying either an
   explicit `T²` factor or total degree `≥4`), the resulting exceptional
   curve has fiber-multiplicity exactly 1. This isolates exactly the
   structural fact common to every instance, so it need not be reproved
   nine times.
2. **A table of all nine tangent-cone computations** — `P1, P2, P3` at
   each of `T=0, -1, ∞` — each independently carried out (not inferred by
   symmetry) and each shown to have the required `c=±1≠0` form.
3. **Lemma C.2** (Complete multiplicity verification) — covers all
   twelve marked components (the four legs met by `O,P1,P2,P3` at each
   of the three fibers): the nine `P1/P2/P3` cases via Lemma C.1, and the
   three `O` cases via the separate, more elementary argument (Lemma 5.5:
   any section meets exactly one component, necessarily multiplicity 1)
   — explicitly distinguished from the tangent-cone argument, since `O`
   never enters the blown-up region at all.

**Main text (§5)**:
- Lemma 5.6's proof now cites "Appendix~C, Lemma~C.2" (not "Appendix D")
  for the `P2/P3` computation, and states explicitly that multiplicity
  was "verified explicitly for both, not inferred, exactly as for `P1`'s
  leg."
- Remark 5.9 ("Transfer to `T=-1,∞`") was rewritten. It previously
  claimed "the identical argument applies verbatim" — on inspection this
  overstated the case: no coordinate automorphism of `V_III` carries
  `T=0` literally to `T=-1` or `T=∞` (the natural candidate,
  `T↦-1-T, X↦-X-1`, sends the equation to its own quadratic twist by
  `-1`, not to itself — checked explicitly, see the "adversarial check"
  section below). The corrected remark states plainly that the `T=-1`
  and `T=∞` computations are separate and explicit, gives the actual
  specialization coordinates found at each, and identifies precisely what
  *is* shared across the three fibers (the structural pattern proved
  once in Lemma C.1, and the purely abstract graph fact Lemma 5.7) versus
  what is not (no single derivation is being transported).

## Cases explicitly checked (all nine, verified fresh for this repair)

| Fiber | Point | Local coordinate | Tangent cone |
|---|---|---|---|
| $T=0$ | $P_1$ | $x_1=0$ | $y_1^2-Tx_1$ |
| $T=0$ | $P_2$ | $x_3=-1$ | $y_3^2+Tx_4$ |
| $T=0$ | $P_3$ | $x_3=-2$ | $y_3^2-Tx_4$ |
| $T=-1$ | $P_2$ | $x_1=1$ | $y_1^2-sx_2$ |
| $T=-1$ | $P_1$ | $x_3=0$ | $y_3^2-sx_4$ |
| $T=-1$ | $P_3$ | $x_3=1$ | $y_3^2+sx_4$ |
| $T=\infty$ | $P_3$ | $x_1=-1$ | $y_1^2-Sx_2$ |
| $T=\infty$ | $P_1$ | $x_3=0$ | $y_3^2-Sx_4$ |
| $T=\infty$ | $P_2$ | $x_3=-1$ | $y_3^2+Sx_4$ |

Every entry independently computed by carrying out the same two-step
blow-up procedure (first blow-up centered at the finite singular point of
each fiber's local Weierstrass model, second blow-up where the first
exceptional curve retains a singular point) using each fiber's own
specific local data — none derived from another fiber's computation.

## Was symmetry used, and is it valid?

**No global symmetry was used to shortcut any of the nine computations.**
The one candidate symmetry considered (`T↦-1-T, X↦-X-1`) was checked and
found to send `V_III`'s defining equation to its own quadratic twist by
`-1`, not to itself — so it does **not** literally identify the `T=0`
fiber's local picture with the `T=-1` fiber's, and was correctly not used
as a shortcut. What *is* legitimately shared across all nine cases is
Lemma C.1, an abstract statement about a certain shape of tangent cone
implying multiplicity 1 — this is not a symmetry of the surface, but a
general algebraic fact, proved once and then checked (not assumed) to
apply at each of the nine specific points by exhibiting each one's actual
tangent cone.

## Multiplicity-one status of $O, P_1, P_2, P_3$

All four sections, at all three fibers (twelve components total): **fiber-multiplicity
exactly 1, fully verified** — nine cases via Lemma C.1 (explicit tangent
cone shown for each), three cases (the three $O$'s) via the independent,
more elementary Lemma 5.5 argument.

## Distinct-leg status

Unchanged and re-confirmed: at each fiber, the four marked points land on
four pairwise distinct components (different local coordinates at
different resolution levels, as already tabulated in the specialization
table). This repair adds *why* each of those four components is
genuinely a leg (multiplicity 1) rather than a mislabeled spine node; it
does not change which four components are marked.

## Graph-rigidity dependency status

Fully supported at every arrow now:
`rational 2-torsion sections` (Corollary 4.4, unchanged) →
`four distinct specialization points` (Lemma 5.6/Remark 5.9, unchanged
coordinates, corrected justification) →
`four distinct multiplicity-one legs` (**now fully shown**, Lemma C.1/C.2) →
`four individually Q-rational legs` (Step 3, unchanged, correctly
depends on the now-complete multiplicity result) →
`affine-D6 graph rigidity` (Lemma 5.7, unchanged, independently
re-confirmed adversarially below) →
`all seven components Q-rational` (Proposition 5.1, unchanged conclusion,
now fully supported) →
`all 18 non-identity fiber components Q-rational` →
`NS defined over Q` → `Tr(F_p|NS)=20p` (Theorem 5.10, unchanged
statement, now unconditionally supported).

## NS rationality / $\Tr_{\NS}$ status

Both fully supported. `Tr(F_p|NS)=20p` no longer rests on an unshown
claim for any of the 21 fiber components (7 per fiber × 3 fibers): 12
legs via the repaired Lemma C.2, 9 spine components via graph rigidity
applied at each fiber (itself now resting on fully-verified leg data).

## Adversarial check on the repaired argument

1. **One of the four sections meets a multiplicity-2 spine component?**
   No — all nine `P1/P2/P3` tangent cones have `c=±1≠0` (checked, not
   assumed); `c=0` is the only value that would signal a degenerate
   (spine-type) tangent cone, and it never occurs.
2. **Two marked sections meet the same leg?** No — within each fiber,
   the four marked points are at pairwise-distinct (coordinate, level)
   pairs (re-confirmed by direct inspection of the specialization
   table's three columns, each checked individually).
3. **A claimed local component is nonreduced?** No — Lemma C.1's proof
   shows that whenever `c≠0`, the restriction is `y'²-cu'`, linear in
   `u'` and therefore automatically reduced; this was verified to hold at
   all nine points.
4. **Galois can still exchange two spine components?** No — Lemma 5.7
   (unchanged, independently re-confirmed by exhaustive enumeration in
   the prior referee audit: exactly 8 automorphisms of the unmarked
   graph, exactly 1 — the identity — compatible with all four legs
   individually fixed) rules this out completely, and this conclusion now
   applies validly at all three fibers since the leg-fixing hypothesis
   is fully established at each.
5. **The four-leg marking leaves a nontrivial affine-D6 automorphism?**
   No — same as item 4.
6. **`Tr(F_p|NS)=20p` depends on an unproved rationality assertion?**
   No — this was the referee's exact finding, and it is now closed: every
   one of the 21 components' rationality is fully supported, either
   directly (12 legs) or via the (now fully justified) graph-rigidity
   step (9 spine components).

**No attack succeeded.** No mathematical failure was found; the repair
is complete.

## Files modified

Only `explorations/class_iii/manuscript/class3_hypercuboid_k3.tex`. No
other file (including the published Classes I/II manuscript, any round
report, checkpoint, or other audit file) was touched.

## Final page count

23 pages (up from 21; the increase is entirely the new Lemma C.1, the
nine-row table, and Lemma C.2 in Appendix C, plus the corrected/expanded
Remark 5.9).

## Compile status

Clean: three full `pdflatex` passes, zero errors, zero undefined
references, zero undefined citations. Only pre-existing cosmetic
`hyperref` "Token not allowed in a PDF string" warnings remain (these
concern PDF bookmark strings containing math and do not affect document
content or correctness; they were present before this repair too).

## Mathematical changes to the theorem

**None.** The theorem statement (Theorem 8.6), the definitions, the
abstract, the introduction, the modularity/twist argument (§6–7), the
point-count argument (§8), the comparison section (§9), and the
discussion (§10) are byte-for-byte unchanged. This was a proof-completeness
repair confined entirely to the justification of one supporting lemma
(Lemma 5.6) and its two Appendix C/D cross-references; no claim anywhere
in the paper was strengthened, weakened, or altered.

## Remaining vulnerabilities

None identified. The referee's one Major Issue is closed; the three
Minor Issues from the referee report (documentation/pointer suggestions
for the reproducibility table and the comparison-table row) remain
optional and do not block release.

## Safe for preprint release?

Yes.
