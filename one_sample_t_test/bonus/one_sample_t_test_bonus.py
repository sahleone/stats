"""One-sample t-test bonus script."""
from __future__ import annotations

import math
from statistics import mean, pstdev


def t_test(sample: list[float], mu0: float) -> tuple[float, float, int]:
    n = len(sample)
    xbar = mean(sample)
    s = pstdev(sample) * math.sqrt(n / (n - 1))
    se = s / math.sqrt(n)
    t = (xbar - mu0) / se
    df = n - 1
    return xbar, t, df

def main() -> None:
    data = [84, 79, 88, 75, 82, 90, 77, 81, 83, 86, 80, 78]
    mu0 = 85
    alpha = 0.05
    xbar, t_stat, df = t_test(data, mu0)
    print(f"sample mean={xbar:.2f}, t={t_stat:.2f}, df={df}")
    print("Reject H0" if abs(t_stat) > 2.201 else "Fail to reject H0")

if __name__ == "__main__":
    main()
