"""Sign test helper."""
from __future__ import annotations

from math import comb


def binom_prob(n: int, k: int) -> float:
    return comb(n, k) / 2**n


def two_tailed_p(n: int, x: int) -> float:
    tail = min(x, n - x)
    p = sum(binom_prob(n, k) for k in range(0, tail + 1))
    return min(1.0, 2 * p)

if __name__ == "__main__":
    n = 9
    x = 8
    print(f"two-tailed p = {two_tailed_p(n, x):.4f}")
