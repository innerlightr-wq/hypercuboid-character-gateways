# Hypercuboid exploration — Round 1 report (working notes)

Full narrative report delivered in chat. This file is the durable record:
research map, Track E candidate-pattern table, and the bug caught/fixed
during Track B. Nothing here modifies or reinterprets the paper itself.

## Track E candidate-pattern table

| # | Proposed rule | Smallest example | Primes tested | Dims tested | p mod 4 classes | Counterexample search | First counterexample | Status |
|---|---|---|---|---|---|---|---|---|
| 1 | Odd-cardinality S ⟹ Σ_S(p)=0 exactly | n=3, \|S\|=1 | 32(n=3)+512(n=4)+131072(n=5) (S,p) pairs | n=3,4,5 | both | exhaustive over all odd S at all tested primes | none | KNOWN CONSEQUENCE (paper's own Prop 6.2 / App C.5 — reproduced as baseline, not claimed new) |
| 2 | S has a "private" coordinate (some k with r_k(S)=1) ⟹ Σ_S(p)=0 exactly, for ANY parity of \|S\| | n=4, \|S\|=2 | 33 subsets × 16 primes (n=4, exhaustive); spot-checked n=5 | both | n=4 exhaustive, n=5 spot-check | exhaustive at n=4; none found | none | **CANDIDATE THEOREM** — elementary proof found and verified (affine shift telescoping: Σ_{x_k} χ(D·(x_k+c)) = χ(D)·Σ_y χ(y) = 0, independent of the other d-1 variables' values). Elementary in *method* (rediscovery-filter: linear substitution + Σχ=0), but the exact scope (which S qualify) and its extension beyond Prop 6.2 is new to this exploration. |
| 3 | S has NO private coordinate but exactly one coordinate with r_k=2, "cycle-covering" structure (e.g. S=(0,1,2,full-sum), n=4) ⟹ Σ_S(p) = χ(-1)·p·(p-1) or Σ_S(p)=p·(p-1) exactly, depending on structure | n=4, \|S\|=4, e.g. (0,1,2,6) | 16 primes, exact match at all 16 | n=4 (4 examples), n=5 (2 examples, one with a free extra coordinate) | both | targeted, 16-30 primes per example | none | **CANDIDATE THEOREM** for the specific worked examples (hand-derived closed form via Σχ((x-r1)(x-r2))=-1 or p-1, verified exactly at every tested prime); the FULLY GENERAL classification (which sign/constant for which combinatorial S) is NOT resolved this round — flagged as the top Round-2 target. |
| 4 | S=(4,5,8,9) "4-cycle" in n=5 (d=4): Σ_S(p) = p^2(p-1) exactly | n=5, \|S\|=4 | 14 primes, exact match at all 14 | n=5 | both | targeted | none | CANDIDATE LEMMA — one confirmed instance of the pattern-3 family one dimension up; consistent with a |Σ_S| = p^{d-2}(p-1) scaling law across d=3,4, not yet proven in general |
| 5 | Shallow/unit-square lifting is COMPLETE for the zero sector under the exact-elimination parametrization: every clean-mod-p tuple has ALL p^{(n-1)(k-1)} digit-lifts clean mod p^k, no obstruction | n=3 (12/12 bases, p=13, exhaustive to mod p^2), n=4 (5/5 bases, p=53, exhaustive to mod p^2) | 13, 53 | n=3, n=4 | — | exhaustive per base (169 and 148877 lifts respectively, ALL checked) | none (after bug fix) | KNOWN CONSEQUENCE — proven via elementary group theory (odd-order kernel of prime-power reduction lies in the index-2 squares subgroup) + verified exhaustively. **A real implementation bug (wrong Euler-criterion exponent for a prime-power modulus) initially produced a false "obstruction" signal; caught and fixed before this was reported — see below.** |

## Bug caught and fixed during Track B

First implementation of `legendre(a, modulus)` for `modulus = p**k`, `k>=2`
used the exponent `(modulus-1)//2`, which is the correct Euler-criterion
exponent only when `modulus` is *prime*. For a prime power, the
multiplicative group has order `phi(p**k) = p**(k-1)*(p-1)`, not
`p**k - 1`, so the correct exponent is `phi(p**k)//2`. The bug produced a
false "1/169 lifts clean" result at n=3, p=13, which looked like a dramatic
prime-power obstruction. Isolating it to a single fixed unit (`a=1`, whose
lifts `1, 14, 27, ...` should all trivially be QR since `1` itself is
always a square) showed 12 of 13 lifts reporting as non-residues — an
impossible result for unit lifts of a square that immediately flagged the
exponent as wrong. Fixed in `track_b_lifting.py`'s `legendre()`. Full
re-run after the fix confirmed the original hand-derived group-theory
argument exactly (see main report).
