"""Two-sample t-test (equal variances) example."""
from __future__ import annotations

import math
from statistics import mean, pstdev


def pooled_std(sample1: list[float], sample2: list[float]) -> float:
    n1, n2 = len(sample1), len(sample2)
    s1 = pstdev(sample1) * math.sqrt(n1 / (n1 - 1))
    s2 = pstdev(sample2) * math.sqrt(n2 / (n2 - 1))
    return math.sqrt(((n1 - 1) * s1 ** 2 + (n2 - 1) * s2 ** 2) / (n1 + n2 - 2))


def t_stat(sample1: list[float], sample2: list[float], sp: float) -> float:
    n1, n2 = len(sample1), len(sample2)
    return (mean(sample1) - mean(sample2)) / (sp * math.sqrt(1 / n1 + 1 / n2))


def main() -> None:
    grp1 = [45, 47, 44, 46, 43, 48, 45, 44, 46, 47, 45, 42, 44, 46, 47, 45, 44, 43]
    grp2 = [41, 40, 39, 42, 40, 41, 38, 39, 40, 41, 37, 39, 40, 42, 38, 39, 41, 40, 39, 38]
    sp = pooled_std(grp1, grp2)
    t = t_stat(grp1, grp2, sp)
    df = len(grp1) + len(grp2) - 2
    print(f"x̄1={mean(grp1):.2f}, x̄2={mean(grp2):.2f}, pooled s={sp:.2f}")
    print(f"t={t:.2f}, df={df}")

if __name__ == "__main__":
    main()
