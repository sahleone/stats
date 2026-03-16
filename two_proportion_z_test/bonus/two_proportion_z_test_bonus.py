"""Two-proportion z-test demo."""
from __future__ import annotations

import math


def two_proportion_z(x1: int, n1: int, x2: int, n2: int) -> float:
    p1 = x1 / n1
    p2 = x2 / n2
    p_pool = (x1 + x2) / (n1 + n2)
    se = math.sqrt(p_pool * (1 - p_pool) * (1 / n1 + 1 / n2))
    return (p1 - p2) / se


def main() -> None:
    z = two_proportion_z(90, 150, 70, 160)
    print(f"z = {z:.2f}")

if __name__ == "__main__":
    main()
