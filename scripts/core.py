"""Core exact arithmetic for the zero-diagonal hypercuboid character system.

All arithmetic is exact integer/modular arithmetic. numpy is used only as a
vectorized container for exact integers in {-1,0,1} (Legendre symbol values)
and exact residues mod p -- never floating point for any arithmetic that
feeds into a reported number.

Setup (matches the paper, Section 3 / Appendix C.1-C.2):
  n >= 2. Zero sector: A_n = -(A_1+...+A_{n-1}) eliminates the D_full=0
  constraint exactly. The 2^{n-1}-1 representative forms are
      L_J(x) = sum_{j in J} x_j,   nonempty J subseteq [n-1] = {1,...,n-1}.
  A tuple x in F_p^{n-1} is "zero-sector clean" iff chi(L_J(x)) = 1 for
  every nonempty J (equivalently every representative form is a nonzero
  quadratic residue) AND the resulting A_1,...,A_n are pairwise distinct.
"""

from __future__ import annotations

import itertools
from dataclasses import dataclass

import numpy as np


def legendre_table(p: int) -> np.ndarray:
    """Exact Legendre symbol chi(a) for a = 0..p-1, as an int8 array.

    chi(0) = 0, chi(a) = 1 if a is a nonzero QR mod p, else -1.
    Computed via exact modular exponentiation (pow with modulus), not
    floating point.
    """
    table = np.empty(p, dtype=np.int8)
    table[0] = 0
    e = (p - 1) // 2
    for a in range(1, p):
        r = pow(a, e, p)
        # r is 1 (QR) or p-1 (nonresidue), exactly, by Euler's criterion.
        table[a] = 1 if r == 1 else -1
    return table


def all_nonempty_subsets(m: int) -> list[tuple[int, ...]]:
    """All nonempty subsets of {0,...,m-1} as sorted index tuples."""
    out = []
    for k in range(1, m + 1):
        out.extend(itertools.combinations(range(m), k))
    return out


@dataclass(frozen=True)
class ZeroSectorSystem:
    """The 2^(n-1)-1 representative forms L_J for a given n, indexed 0..m-1."""

    n: int  # number of original coordinates A_1..A_n
    subsets: tuple[frozenset, ...]  # subsets J of {0,...,n-2}, one per form

    @staticmethod
    def build(n: int) -> "ZeroSectorSystem":
        d = n - 1
        subs = []
        for k in range(1, d + 1):
            for J in itertools.combinations(range(d), k):
                subs.append(frozenset(J))
        return ZeroSectorSystem(n=n, subsets=tuple(subs))

    @property
    def m(self) -> int:
        return len(self.subsets)  # 2^(n-1) - 1

    @property
    def d(self) -> int:
        return self.n - 1


def chi_columns(sys: ZeroSectorSystem, p: int) -> np.ndarray:
    """Exact chi(L_J(x)) for every x in F_p^d and every form J.

    Returns an int8 array of shape (p**d, m). Row order is the standard
    mixed-radix enumeration of F_p^d (x_0 varies slowest).
    """
    d = sys.d
    m = sys.m
    leg = legendre_table(p)

    # Build the coordinate grid exactly (integers 0..p-1 per axis), via
    # numpy meshgrid on exact integer arrays (no floating point).
    axes = [np.arange(p, dtype=np.int64) for _ in range(d)]
    grids = np.meshgrid(*axes, indexing="ij")
    coords = np.stack([g.reshape(-1) for g in grids], axis=1)  # (p^d, d)

    cols = np.empty((p**d, m), dtype=np.int8)
    for j, J in enumerate(sys.subsets):
        idx = sorted(J)
        s = coords[:, idx].sum(axis=1) % p
        cols[:, j] = leg[s]
    return cols, coords


def sigma_S(chi_cols: np.ndarray, S_idx: tuple[int, ...]) -> int:
    """Exact Sigma_S(p) = sum_x chi(prod_{J in S} L_J(x))."""
    if len(S_idx) == 0:
        return chi_cols.shape[0]
    prod = chi_cols[:, S_idx[0]].astype(np.int64)
    for j in S_idx[1:]:
        prod = prod * chi_cols[:, j].astype(np.int64)
    return int(prod.sum())


def clean_count_zero_sector(sys: ZeroSectorSystem, p: int) -> int:
    """Exact N_0^clean(p, n): count x with every L_J(x) a nonzero QR and
    the resulting n coordinates pairwise distinct. Fully vectorized
    (no per-row Python loop) so it stays fast for the largest feasible p."""
    cols, coords = chi_columns(sys, p)
    all_qr = np.all(cols == 1, axis=1)
    idx = np.nonzero(all_qr)[0]
    if idx.size == 0:
        return 0
    sub = coords[idx]  # (k, d)
    last = (-sub.sum(axis=1)) % p
    A = np.concatenate([sub, last[:, None]], axis=1)  # (k, n)
    A_sorted = np.sort(A, axis=1)
    distinct = np.all(np.diff(A_sorted, axis=1) != 0, axis=1)
    return int(distinct.sum())


def coeff_matrix(sys: ZeroSectorSystem, S_idx: tuple[int, ...]) -> np.ndarray:
    """0/1 coefficient matrix (|S| x d) of the forms L_J for J indices in S."""
    d = sys.d
    rows = []
    for j in S_idx:
        v = [0] * d
        for i in sys.subsets[j]:
            v[i] = 1
        rows.append(v)
    return np.array(rows, dtype=np.int64)


def matrix_rank_mod(M: np.ndarray, modulus: int | None = None) -> int:
    """Exact rank over Q (integer matrix) via sympy, or over F_2 if requested."""
    import sympy

    if modulus is None:
        return sympy.Matrix(M.tolist()).rank()
    return sympy.Matrix(M.tolist()).rank_mod(modulus) if hasattr(
        sympy.Matrix(M.tolist()), "rank_mod"
    ) else _rank_gf(M, modulus)


def _rank_gf(M: np.ndarray, p: int) -> int:
    """Exact rank of integer matrix M over GF(p), simple Gaussian elimination."""
    A = M.astype(np.int64) % p
    rows, cols = A.shape
    rank = 0
    for col in range(cols):
        piv = None
        for r in range(rank, rows):
            if A[r, col] % p != 0:
                piv = r
                break
        if piv is None:
            continue
        A[[rank, piv]] = A[[piv, rank]]
        inv = pow(int(A[rank, col]), p - 2, p)
        A[rank] = (A[rank] * inv) % p
        for r in range(rows):
            if r != rank and A[r, col] != 0:
                A[r] = (A[r] - A[r, col] * A[rank]) % p
        rank += 1
        if rank == rows:
            break
    return rank


PRIMES_1MOD4 = [5, 13, 17, 29, 37, 41, 53, 61, 73, 89, 97, 101, 109, 113]
PRIMES_3MOD4 = [3, 7, 11, 19, 23, 31, 43, 47, 59, 67, 71, 79, 83, 103, 107]
