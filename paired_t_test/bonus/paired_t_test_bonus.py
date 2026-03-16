"""Paired t-test example."""
from __future__ import annotations

import math


def paired_t(before: list[float], after: list[float]) -> tuple[float, float, int]:
    diffs = [b - a for b, a in zip(before, after)]
    n = len(diffs)
    dbar = sum(diffs) / n
    sd = math.sqrt(sum((d - dbar) ** 2 for d in diffs) / (n - 1))
    t = dbar / (sd / math.sqrt(n))
    return dbar, t, n - 1


def main() -> None:
    before = [78, 82, 80, 76, 85, 79, 81, 77, 83, 80]
    after = [72, 78, 75, 70, 80, 74, 78, 71, 79, 74]
    dbar, t, df = paired_t(before, after)
    print(f"mean diff={dbar:.2f}, t={t:.2f}, df={df}")

if __name__ == "__main__":
    main()
