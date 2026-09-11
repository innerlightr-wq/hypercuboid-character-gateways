# Hypercuboid exploration — Round 19 working notes

## Part I — freeze and t=-1 model (PROVED, reconfirmed)

`u=t+1`. `a_2=u^2(u-1)`, `a_4=u^2(u-1)^3` (verified). `v_u(c_4)=2,
v_u(c_6)=4, v_u(\Delta)=6` — matches Round 11/14's `I_0^*` exactly.

## Part II/III — I_0^* completely resolved (PROVED, Goal A achieved)

Tate cubic (substitution `X=uT'`): exactly `Q(T',0)=T'(T'-1)(T'+1)` —
**three distinct roots**, the terminal case per Tate's algorithm (no
further blow-up needed, unlike `I_2^*`'s double root). For each root
`\tau\in\{0,1,-1\}`, substituting `T'=\tau+\varepsilon`, `Y=u^2\rho`
gives `K(u,\varepsilon,\rho)=\rho^2u-Q(\tau+\varepsilon,u)`, verified
**smooth by explicit Jacobian at every one of the three roots**
(`\partial K/\partial\varepsilon\in\{1,-2,-2\}$, all nonzero). **Four
multiplicity-1 components total**: identity (`X=O(1)`) plus three
symmetric named components (one per root), **all with the same Shioda
contribution `1`** (standard for `D_4`/`I_0^*`, and reconfirmed here by
explicit local construction, not assumed). `e(I_0^*)=6`: reconfirmed
from `v(\Delta_{\min})=6` (unchanged, standard formula, not
independently re-summed from an explicit intersection graph this
round — the multiplicity-2 central component, unreachable by any
section, was not separately constructed, exactly as in Round 18's
treatment of `I_2^*`'s chain).

## Part IV — torsion tracking and consistency (PROVED)

`T_1\to\tau=0`, `T_2\to\tau=1`, `T_3\to\tau=-1$ (limits of `X/u`,
computed exactly). **All three land on distinct, smooth components** —
consistent with bijective specialization and with every one of Round
16's torsion-height solutions (all had `(1,1,1)` at `I_0^*`, unaffected
by which specific root each `T_i` hits, since all three give the same
contribution).

**Full four-fiber height check (all four bad fibers now explicit)**:
$$T_1:\ 1.5(t{=}0)+0(t{=}1)+1(t{=}{-}1)+1.5(t{=}\infty)=4$$
$$T_2:\ 1+0.5+1+1.5=4$$
$$T_3:\ 1.5+0.5+1+1.0=4$$
**All exactly 4 — full independent confirmation, no contradiction.**

## Part V — complete t=-1 valuation dictionary (PROVED)

| `v_{-1}(x)` | condition | component | `\mathrm{contr}_{-1}` |
|---|---|---|---|
| `<0` | pole | meets `O` | **excluded** (violates `P\cdot O=0`) |
| `0` | `x(-1)\ne0` | identity | `0` |
| `\ge1` | `x(t)/(t+1)\to\tau\in\{0,1,-1\}` | named (any of 3) | `1` |
| `\ge1` | limit `\notin\{0,1,-1\}` | — | **ALGEBRAICALLY IMPOSSIBLE** (forces a fractional power of `u`, same mechanism as the `I_2^*` exclusions) |

## Part VI — the master global consequence (the round's central new result)

Since `P\cdot O=0` is proved (Round 16) and a pole in `x(t)$ at *any*
finite `t$ (good or bad fiber) would force `P` to meet `O` there,
**`x(t)$ must be a polynomial — no finite poles anywhere.** Combined
with the `t=0\leftrightarrow\infty` isomorphism (Round 17/18) and its
dictionary, the component required *at infinity* forces an **exact
degree bound**, using `x_\infty(u)=x(t)\cdot u^4=x(t)/t^4`:

| component @ `\infty` | condition on `x_\infty` | degree consequence |
|---|---|---|
| identity | `x_\infty(0)\ne0` | `\deg(x)=4` exactly, leading coeff free (nonzero) |
| "N" | `v_0(x_\infty)=1`, leading coeff `=-1` | `\deg(x)=3` exactly, **leading coeff `=-1`** |
| "F" | `v_0(x_\infty)\ge2` | `\deg(x)\le2` |

**This proves the height-1 section search is a genuinely finite,
exact-algebra problem — not merely a "reasonable guess" bounded search
as in Round 15.** Round 15's degree-`\le4` search is now understood,
retroactively, to have covered *exactly* the relevant polynomial
family (modulo needing all rational, not just small integer,
coefficients).

## Part VII/VIII — divisor theory applied: two patterns exactly eliminated

**Pattern (identity@0, "N"@1, named@`-1`, "F"@`\infty`)**: forces
`\deg(x)\le2` with the `t=\infty$ sub-choice `C\in\{0,-1\}` (leading
coeff of the degree-2 term), plus `x(-1)=0` (named), `x(1)=-2` ("N" at
`I_2`), `x(0)\ne0` (identity). **Solving the resulting linear system
exactly** (not searching) gives a **unique** candidate for `C=0`:
`x(t)=-(t+1)`. **Verified directly**: `\text{RHS}=-(t-1)^2(t+1)^4` — a
**negative** perfect square (`Y=i(t-1)(t+1)^2`, defined only over
`\mathbb Q(i)(t)`, not `\mathbb Q(t)`) — **FAILS.** (The `C=-1` sub-branch is
separately shown incompatible with `x(0)\ne0`.) **This entire pattern
is PROVED to have no solution** — an exact elimination, not a search
failure.

**Pattern (identity@0, identity@1, named@`-1`, "F"@`\infty`)**: forces
`\deg(x)\le2`, `x(-1)=0`, `x(0)\ne0` (E free, nonzero), `x(1)\ne-2`
(open condition, generically satisfied). Solving `x(-1)=0` leaves a
one-parameter family `x(t)=Ct^2+(C+E)t+E$ for each `C\in\{0,-1\}`.
**Symbolic factorization (exact, all `E`, not case-by-case)**:
- `C=0`: `\text{RHS}=E(E+t)(E+t^2)(t+1)^3` — this is exactly Round 12's
  already-analyzed `X=E(t+1)` family, proved there to admit **no**
  perfect square for any `E` (the `(t+1)^3` factor's odd multiplicity
  cannot be cured).
- `C=-1`: `\text{RHS}=-E(t-E)(t+1)^3(t^2-t+E)`. The `(t+1)^3` factor's
  odd multiplicity can only be repaired if `(t-E)` or `(t^2-t+E)`
  themselves acquire a factor of `(t+1)` — solved exactly: `E=-1` or
  `E=-2`, the **only two possible exceptions**. **Both checked
  directly and both fail**: `E=-1$ gives `\text{RHS}=(t+1)^4(t^2-t-1)`
  (the residual quadratic has discriminant `5`, not a perfect square);
  `E=-2` gives `\text{RHS}=2(t-2)(t+1)^4(t+2)` (residual `2(t^2-4)`,
  not a perfect square). **No value of `E` works for either `C` — this
  entire pattern is PROVED to have no solution**, exhaustively over
  *all* `E\in\mathbb Q`, not merely small integers.

## Part IX — torsion orbits: not systematically computed for all 23 this round

Given the two exact eliminations above required pattern-specific
algebra, a full orbit computation for the remaining ~21 patterns was
**not completed** in the time available — an honest scope limit, not a
claim of completeness.

## Part X — exact symbolic solve: attempted at full generality, found intractable; succeeded at reduced (deg-`\le2`) scale

A full symbolic system for the unrestricted `\deg(x)=4` case (12
unknowns: 5 coefficients of `x`, 7 of a candidate square-root `y`, 13
polynomial-coefficient equations) was set up but **judged
computationally intractable to run to a Groebner-basis conclusion
within this round's time budget** — reported honestly rather than
either faking a bounded search as exhaustive or letting a computation
run indefinitely. **The `\deg(x)\le2` (F-at-infinity) sub-cases, by
contrast, were fully and exactly solved** (Part VII/VIII) — these are
the patterns for which the new degree bound (Part VI) is most powerful,
since it collapses them to a 2–3 parameter linear/low-degree system.

## Part XI — Mordell–Weil rank: still open (no section found, none of the checked patterns survive)

**No non-torsion section found this round.** Two patterns were
*proved* to have none; the majority of the 23 remain unclassified with
full rigor pending either (a) the same exact-algebra treatment
extended to the `\deg=3` ("N"-at-infinity) and `\deg=4` (identity-at-
infinity) sub-cases, or (b) a completed Groebner-basis run. **The
implication is NOT drawn that `\mathrm{rank}(MW)=0`** — per the
round's own explicit instruction, eliminating specific patterns does
not by itself prove no height-1 section exists overall.

## Part XII — master identity: unchanged

`S(p)=\chi(-1)(a_p(f)+p)` remains COMPUTATIONALLY VERIFIED ONLY. No
geometric progress this round bears on it beyond what was already
conditional in Round 13–18.

## Part XIII — falsification discipline

- The `I_0^*` smoothness claims were verified by explicit Jacobian
  computation at all three roots (not assumed from the "simple root"
  folklore that failed for `I_2^*` in Round 17 — here it was tested
  and found to hold, a genuine positive confirmation, not a repeat of
  the earlier error).
- Both "eliminated" patterns were checked by **direct substitution**
  into the original Weierstrass equation and exact factorization —
  not by numerical approximation.
- The `-(t+1)$ candidate's failure was diagnosed precisely (negative
  perfect square ⟹ `\mathbb Q(i)(t)`-only point), matching the exact same
  failure mode caught in Round 12/15 — a recurring, now well-understood
  phenomenon, not a new mystery each time.

## Everything killed or corrected this round

1. **PROVED, new**: `I_0^*` is completely resolved at `t=-1` — all four
   components explicit and verified smooth; torsion tracked exactly.
2. **PROVED, new, major**: `x(t)$ must be a polynomial of degree
   `\le4`, with the *exact* degree pinned down by which component is
   required at `t=\infty` — this converts the entire remaining search
   from "informed guessing" (Round 15) into finite, exact algebra.
3. **PROVED, new**: two of the 23 patterns have **no solution**,
   established by exact symbolic factorization over all rational
   coefficients (not bounded search).
4. **Not killed**: the other ~21 patterns, `\rho\in\{19,20\}`, and the
   modular attachment all remain open.

## Highest-value next question

Extend Part VII/VIII's exact-elimination methodology to the `\deg(x)=3`
("N"-at-infinity) and `\deg(x)=4` (identity-at-infinity) sub-cases for
the remaining ~21 patterns — each is now a small, well-posed, finite
polynomial system (3–5 unknowns) rather than an open-ended search, and
the `\deg\le2` cases handled this round suggest the same factorization
techniques (forcing shared roots to repair odd multiplicities, then
checking the finitely many resulting special values) will likely
resolve most or all of them.

## Required-report items

1. `u^2W^2=u^2T'^3+u^2(u-1)T'^2... ` — see Part I/II for the exact
   `Q(T',u)` form.
2. Complete blow-up sequence: Part II.
3. Component diagram: 4 multiplicity-1 components (identity + 3
   symmetric named), multiplicity-2 central node not separately
   constructed (unreachable by sections).
4. Identity component: standard `X=O(1)`; component group `(\mathbb Z/2)^2`.
5. `T_1\to\tau{=}0,\ T_2\to\tau{=}1,\ T_3\to\tau{=}{-}1`.
6. All three named components: contribution `1` each.
7. Dictionary: Part V table.
8. Four-fiber master dictionary: assembled in Parts II/V plus Rounds
   16–18 (`t=0,1,\infty`).
9. Torsion-height consistency: **PASSED exactly** (all three `=4`).
10–13. Of the 23 patterns: **2 proved to have no solution** (exact
    algebra); the rest not yet individually classified.
14. Torsion orbits: not computed this round.
15. Exact divisor form: derived and solved explicitly for the two
    treated patterns (Part VII/VIII); not yet done for the rest.
16. Finite symbolic ansatz: **YES, proved to exist and be genuinely
    finite** (Part VI) — the main structural achievement of this round.
17. Non-torsion section found: **No.**
18–21. MW rank, `\rho`, `NS(X)`, `T(X)`: all unchanged, open.
22–23. Modular attachment, master identity: unchanged, conditional /
    computationally verified only.
24. Killed/corrected: see above.
25. Highest-value next question: as stated above.

**Verdict: ROUND19-C** — the `I_0^*` fiber is completely solved, and —
via the new proved degree bound on `x(t)$ — the global height-1 problem
is now rigorously reduced to a **genuinely finite, exact algebraic
search** (not a heuristic bounded one); two of the 23 canonical
patterns were exactly eliminated within that finite search this round,
with the remainder awaiting the same treatment.

**THE THREE MOST IMPORTANT THINGS WE LEARNED**
- The last of the four "trouble spots" on the surface turned out to be
  the easiest one — everything about it checked out cleanly on the
  first attempt, a nice contrast to the near-miss two rounds ago.
- We proved something that turns the entire remaining search from
  "try reasonable-looking numbers and see" into "solve a small, exact
  algebra problem with a guaranteed finite answer" — a genuine change
  in kind, not just more of the same searching.
- Using that new tool, we conclusively ruled out two specific
  candidate answers for good, with a real proof rather than just not
  finding them — a small but solid down payment on the larger question
  of whether the special point we're looking for exists at all.

Stopping here per the round's instructions — no further action taken.
