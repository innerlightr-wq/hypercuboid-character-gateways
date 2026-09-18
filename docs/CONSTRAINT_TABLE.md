# The 30 raw conditions and their 15 representatives (n = 5)

Generated, not hand-written. Companion to `NOVELTY_AND_PROVENANCE.md` §4 and Table 3.

Setup: `A_i = x_i` for `i < 5`, `A_5 = -(x_1+x_2+x_3+x_4)`, so `A_1+...+A_5 = 0`.
For a nonempty proper `S` the diagonal sum is `D_S = sum_{i in S} A_i`, and the
zero-sector relation gives `D_{S^c} = -D_S` exactly, hence
`chi(D_{S^c}) = chi(-1) chi(D_S)`: the two conditions coincide iff `p = 1 mod 4`.

The canonical representative of each pair is the member **not** containing the index 5;
its diagonal sum is then the repository's form `L_J` with `J = S` viewed inside `[4]`.

| # | Raw condition `S` | Paired / complement `S^c` | Canonical representative | `L_J` in coordinates | Reason equivalent | Independent mod squares? |
|---|---|---|---|---|---|---|
| 1 | `D_{1}` | `D_{2,3,4,5}` | `{1}` | `x1` | `D_{2,3,4,5} = -D_{1}` | yes — distinct linear form |
| 2 | `D_{2}` | `D_{1,3,4,5}` | `{2}` | `x2` | `D_{1,3,4,5} = -D_{2}` | yes — distinct linear form |
| 3 | `D_{3}` | `D_{1,2,4,5}` | `{3}` | `x3` | `D_{1,2,4,5} = -D_{3}` | yes — distinct linear form |
| 4 | `D_{4}` | `D_{1,2,3,5}` | `{4}` | `x4` | `D_{1,2,3,5} = -D_{4}` | yes — distinct linear form |
| 5 | `D_{1,2}` | `D_{3,4,5}` | `{1,2}` | `x1+x2` | `D_{3,4,5} = -D_{1,2}` | yes — distinct linear form |
| 6 | `D_{1,3}` | `D_{2,4,5}` | `{1,3}` | `x1+x3` | `D_{2,4,5} = -D_{1,3}` | yes — distinct linear form |
| 7 | `D_{1,4}` | `D_{2,3,5}` | `{1,4}` | `x1+x4` | `D_{2,3,5} = -D_{1,4}` | yes — distinct linear form |
| 8 | `D_{2,3}` | `D_{1,4,5}` | `{2,3}` | `x2+x3` | `D_{1,4,5} = -D_{2,3}` | yes — distinct linear form |
| 9 | `D_{2,4}` | `D_{1,3,5}` | `{2,4}` | `x2+x4` | `D_{1,3,5} = -D_{2,4}` | yes — distinct linear form |
| 10 | `D_{3,4}` | `D_{1,2,5}` | `{3,4}` | `x3+x4` | `D_{1,2,5} = -D_{3,4}` | yes — distinct linear form |
| 11 | `D_{1,2,3}` | `D_{4,5}` | `{1,2,3}` | `x1+x2+x3` | `D_{4,5} = -D_{1,2,3}` | yes — distinct linear form |
| 12 | `D_{1,2,4}` | `D_{3,5}` | `{1,2,4}` | `x1+x2+x4` | `D_{3,5} = -D_{1,2,4}` | yes — distinct linear form |
| 13 | `D_{1,3,4}` | `D_{2,5}` | `{1,3,4}` | `x1+x3+x4` | `D_{2,5} = -D_{1,3,4}` | yes — distinct linear form |
| 14 | `D_{2,3,4}` | `D_{1,5}` | `{2,3,4}` | `x2+x3+x4` | `D_{1,5} = -D_{2,3,4}` | yes — distinct linear form |
| 15 | `D_{1,2,3,4}` | `D_{5}` | `{1,2,3,4}` | `x1+x2+x3+x4` | `D_{5} = -D_{1,2,3,4}` | yes — distinct linear form |

Rows: **15** = `2^4 - 1`, covering all **30** = `2^5 - 2` raw conditions in
fixed-point-free pairs. Every representative is a distinct, pairwise non-proportional
linear form, so every nonempty product of them is squarefree and the 15 characters are
independent modulo squares: the square-class rank is exactly **15**.

Geometric reading: the 15 rows are the nonzero elements of `F_2^5 / <(1,1,1,1,1)>`,
i.e. the 15 points of `PG(3,2)`; equivalently the 15 coordinates of the `[15,4]` binary
simplex code. For `n = 4` the same construction gives 7 rows, the Fano plane `PG(2,2)`.
