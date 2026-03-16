"""Two-sample z-test with known variances."""
from __future__ import annotations

import math


def two_sample_z(xbar1: float, xbar2: float, sigma1: float, sigma2: float, n1: int, n2: int) -> float:
    se = math.sqrt(sigma1 ** 2 / n1 + sigma2 ** 2 / n2)
    return (xbar1 - xbar2) / se


def main() -> None:
    z = two_sample_z(82, 78, 5, 6, 40, 35)
    print(f"z = {z:.2f}")

if __name__ == "__main__":
    main()
