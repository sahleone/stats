"""Bonus analysis script template for hypothesis testing topics."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence, Tuple


def mean(values: Sequence[float]) -> float:
    return sum(values) / len(values)


def stdev(values: Sequence[float]) -> float:
    m = mean(values)
    return (sum((x - m) ** 2 for x in values) / (len(values) - 1)) ** 0.5


@dataclass
class Sample:
    values: Sequence[float]

    @property
    def n(self) -> int:
        return len(self.values)

    @property
    def mean(self) -> float:
        return mean(self.values)

    @property
    def stdev(self) -> float:
        return stdev(self.values)


def compute_test_statistic(sample1: Sample, sample2: Sample) -> Tuple[float, int]:
    """Replace with the formula for the specific test."""
    raise NotImplementedError("Fill in with the test-specific formula")


def confidence_interval(sample1: Sample, sample2: Sample, alpha: float) -> Tuple[float, float]:
    """Replace with confidence-interval logic for the topic."""
    raise NotImplementedError


def main() -> None:
    group1 = Sample(values=[...])
    group2 = Sample(values=[...])
    alpha = 0.05
    t_stat, df = compute_test_statistic(group1, group2)
    ci_low, ci_high = confidence_interval(group1, group2, alpha)
    print(f"Sample 1 mean: {group1.mean:.3f}, n={group1.n}")
    print(f"Sample 2 mean: {group2.mean:.3f}, n={group2.n}")
    print(f"Test statistic: {t_stat:.3f} with df={df}")
    print(f"Confidence interval ({100*(1-alpha):.1f}%): ({ci_low:.3f}, {ci_high:.3f})")


if __name__ == "__main__":
    main()
