"""Welch's t-test demo."""
from __future__ import annotations

import math
from statistics import mean, pstdev


def welch_t(sample1: list[float], sample2: list[float]) -> tuple[float, float]:
    n1, n2 = len(sample1), len(sample2)
    s1 = pstdev(sample1) * math.sqrt(n1 / (n1 - 1))
    s2 = pstdev(sample2) * math.sqrt(n2 / (n2 - 1))
    se = math.sqrt(s1 ** 2 / n1 + s2 ** 2 / n2)
    t = (mean(sample1) - mean(sample2)) / se
    nu = (s1 ** 2 / n1 + s2 ** 2 / n2) ** 2 / ((s1 ** 2 / n1) ** 2 / (n1 - 1) + (s2 ** 2 / n2) ** 2 / (n2 - 1))
    return t, nu


def main() -> None:
    a = [52, 54, 50, 49, 55, 51, 53, 52, 54, 48, 50, 53, 51, 52]
    b = [48, 45, 47, 46, 49, 44, 45, 47, 46, 48]
    t, nu = welch_t(a, b)
    print(f"t={t:.2f}, nu={nu:.1f}")

if __name__ == "__main__":
    main()
