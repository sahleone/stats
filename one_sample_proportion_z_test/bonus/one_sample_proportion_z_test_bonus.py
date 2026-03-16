"""One-sample proportion z-test."""
from __future__ import annotations

import math


def z_stat(x: int, n: int, p0: float) -> tuple[float, float]:
    p_hat = x / n
    se = math.sqrt(p0 * (1 - p0) / n)
    z = (p_hat - p0) / se
    return p_hat, z


def main() -> None:
    n = 200
    x = 132
    p0 = 0.60
    p_hat, z = z_stat(x, n, p0)
    print(f"p_hat={p_hat:.3f}, z={z:.2f}")
    if z > 1.645:
        print("Reject H0 at alpha=0.05 (right-tailed)")
    else:
        print("Fail to reject H0")

if __name__ == "__main__":
    main()
