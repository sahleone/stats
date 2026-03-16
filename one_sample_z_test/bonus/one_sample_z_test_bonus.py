"""One-sample z-test bonus script."""
from __future__ import annotations

import math
from statistics import mean


def z_test(sample: list[float], mu0: float, sigma: float) -> tuple[float, float]:
    n = len(sample)
    xbar = mean(sample)
    se = sigma / math.sqrt(n)
    z = (xbar - mu0) / se
    return xbar, z


def main() -> None:
    sample = [9.4, 9.8, 9.7, 9.3, 9.9, 9.5, 9.6, 9.7, 9.4, 9.8]
    mu0 = 10.0
    sigma = 1.2
    alpha = 0.05
    xbar, z = z_test(sample, mu0, sigma)
    print(f"Sample mean = {xbar:.2f}, n={len(sample)}")
    print(f"z-statistic = {z:.2f}")
    if abs(z) > 1.96:
        print("Reject H0 at alpha=0.05 (two-tailed)")
    else:
        print("Fail to reject H0 at alpha=0.05")


if __name__ == "__main__":
    main()
