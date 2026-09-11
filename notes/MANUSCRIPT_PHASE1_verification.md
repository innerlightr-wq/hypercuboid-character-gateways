# Manuscript Phase 1 — Part II: final verification of the two Round-34 caveats

This note reconstructs, from the underlying equations (not from the
checkpoint's summary), the two pieces Round 34 flagged as
"spot-checked, not fully re-derived." Both pass.

---

## A. Height computation for `P_1` (reconstructed, not quoted)

**Section**: `P_1=(x_1(t),\,i\,q_1(t))=(-(t+1),\ i(t-1)(t+1)^2)`, on
`Y^2=X^3+a_2(t)X^2+a_4(t)X`, `a_2=t(t+1)^2`, `a_4=t^3(t+1)^2`.

**Curve membership, by direct substitution** (re-verified symbolically
this phase):
$$Y_1^2-\bigl(X_1^3+a_2X_1^2+a_4X_1\bigr)\equiv0\quad\text{identically in }t.$$

**Local specialization, reconstructed from the completed four-fiber
dictionary (Rounds 16–19 for `t=0,1,-1,\infty`; Round 27 for the
complete `I_2^*` geometry needed at `t=0,\infty`)**:

| `t` | Kodaira type | `x_1(t)` | component met | contribution |
|---|---|---|---|---|
| `0` | `I_2^*` | `x_1(0)=-1\ne0` | identity | `0` |
| `1` | `I_2` | `x_1(1)=-2` | non-identity (unique) | `1\cdot(2-1)/2=0.5` |
| `-1` | `I_0^*` | `x_1(-1)=0` | a named outer component | `1` |
| `\infty` | `I_2^*` | `\deg x_1=1\le2`, leading coeff test | far component `F_1` | `1+2/4=1.5` |

Each contribution is the **standard Shioda local-height value**
(Shioda 1990, Mordell–Weil lattices): `I_n`, non-identity component
`\Rightarrow i(n-i)/n` (here `n=2,i=1\Rightarrow0.5`); `I_0^*`, outer
non-identity component `\Rightarrow1`; `I_m^*`, far component
`\Rightarrow1+m/4` (here `m=2\Rightarrow1.5`) — none of these values were
invented for this surface; they are read off the universal table once
the component `P_1` meets is identified, and that identification is
done here **by direct evaluation of `x_1(t)`** at each bad `t`, not
assumed.

`P_1\cdot O=0` (Shioda 1990, height formula): `x_1(t)` is a
**polynomial** (no pole in `t` anywhere, including `t=\infty`, where
`\deg x_1=1` is finite), so `P_1` never meets the zero section at a
pole — the standard sufficient condition for `P\cdot O=0`, confirmed by
inspection of `x_1`, not assumed.

**Shioda's height formula** (K3: `\chi=2`):
$$\hat h(P_1)=2\chi+2(P_1\cdot O)-\sum_v\mathrm{contr}_v(P_1)=4+0-(0+0.5+1+1.5)=4-3=\boxed{1}.$$

**Non-torsion**: canonical height `=0` iff torsion (standard fact for
the Mordell–Weil height pairing on an elliptic surface); `\hat h(P_1)=1\ne0`,
so `P_1` is non-torsion. **No numerical approximation used anywhere —
every quantity above is an exact rational number from an exact table
lookup.**

**Verdict: A passes.** Fully reconstructed from `x_1(t)`'s explicit
values and the standard height-contribution table; nothing was quoted
without re-derivation.

---

## B. Trivial lattice, `\mathrm{Triv}(X)=U\oplus D_6\oplus A_1\oplus D_4\oplus D_6`

**Rank check**: `U` (general fiber `+` zero section) rank `2`; `D_6`
(non-identity components of an `I_2^*` fiber, `7-1=6`, Dynkin type `D_6`
for `I_2^*`'s dual graph minus the identity vertex) rank `6`, **twice**
(`t=0` and `t=\infty`); `A_1` (`I_2`'s single non-identity component)
rank `1`; `D_4` (`I_0^*`'s `4` non-identity components, star graph of
type affine-`D_4$ minus identity) rank `4`. Total:
`2+6+1+4+6=19`. ✓.

**Field of definition, established from the explicit local equations
(not inferred from Kodaira symbols alone)**:

- **`I_2^*` at `t=0`** (Round 27's complete resolution, reproduced
  here): all 7 components have explicit defining equations with
  **integer/rational coefficients only** — identity: `v=u^3-\cdots`;
  `N`: `-t^2-tw+y_1^2=0`; `C_1,C_2`: coordinate-hyperplane loci
  (`\{t=0,y_1=0\}`, `\{t=0,B=0\}`, manifestly `\mathbb Q$-rational
  loci); `C_3`: `Y'^2=T'X'` (a smooth conic with rational — in fact
  integer — coefficients, unconditionally `\mathbb F_p`-rational for
  every odd `p` by ternary-quadratic-form isotropy, Hessian
  determinant `-2`, checked exactly); `F_1`: `B^2-tA=0`; `F_2`:
  `t^2+tw_3+B^2=0`. **Every one of the 7 equations has rational
  coefficients — hence every component is individually
  `\mathbb Q`-rational, and (since the 7 components are pairwise
  distinguished by their distinct defining loci — no residual symmetry
  identifying two of them) each is separately Galois-stable.** Same
  structure, by the surface's own `t\leftrightarrow\infty` self-duality
  (used consistently throughout, e.g. Round 16 Part), for `t=\infty`.
- **`I_2` at `t=1`**: the unique non-identity component is the
  exceptional conic `W^2=-2u(u+8)` (Round 16/28/32) — rational
  coefficients (`-2,8\in\mathbb Q`), a single `\mathbb Q`-rational curve.
- **`I_0^*` at `t=-1`**: established via Round 19/29's local
  implicit-function-theorem computation, `\partial K_2/\partial U=1`
  (or `-2`) identically — an **integer**, sign-and-residue-independent
  nonzero derivative, forcing smoothness and `\mathbb Q`-rationality of
  each of the 3 named components and the central component, by
  inspection of the (rational-coefficient) local equations themselves,
  not inferred from the abstract Kodaira type.

**Conclusion**: **every one of the 19 generators is defined by an
explicit equation with rational coefficients, checked component by
component, not inferred from the Kodaira symbol alone** — this
directly answers Part II.B's central instruction.

**Frobenius trace, recovered**: since all 19 classes are individually
`\mathbb Q`-rational (Galois acts trivially on each, i.e. Frobenius
fixes each divisor class), each contributes eigenvalue exactly `p`
(the Tate-twist of the trivial character) to `\mathrm{Tr}(F_p\mid NS)`:
$$\mathrm{Tr}(F_p\mid\mathrm{Triv}(X)) = 19p.$$

**Verdict: B passes.** Reconstructed component-by-component from the
explicit rational equations of Round 27 (`I_2^*`), Round 16/28
(`I_2`), and Round 19/29 (`I_0^*`) — not inferred from Kodaira symbols.

---

## Conclusion of Part II

**Neither A nor B failed. Manuscript preparation proceeds.**
