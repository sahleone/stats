"""Wilcoxon signed-rank helper using scipy if available."""
from __future__ import annotations

try:
    from scipy.stats import wilcoxon
except ImportError:
    wilcoxon = None


def main() -> None:
    before = [78, 82, 80, 76, 85, 79, 81, 77, 83, 80]
    after = [72, 78, 75, 70, 80, 74, 78, 71, 79, 74]
    if wilcoxon:
        stat, p_value = wilcoxon(before, after, zero_method="wilcox", alternative="two-sided")
        print(f"W statistic={stat:.1f}, p={p_value:.3f}")
    else:
        print("Install scipy to compute the Wilcoxon signed-rank test.")

if __name__ == "__main__":
    main()
