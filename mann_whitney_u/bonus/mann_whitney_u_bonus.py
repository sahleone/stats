"""Mann-Whitney U test via scipy if available."""
from __future__ import annotations

try:
    from scipy.stats import mannwhitneyu
except ImportError:
    mannwhitneyu = None


def main() -> None:
    a = [12, 15, 14, 11, 13, 16, 14]
    b = [9, 10, 11, 8, 9, 7, 10, 12]
    if mannwhitneyu:
        stat, p = mannwhitneyu(a, b, alternative="greater")
        print(f"U={stat:.1f}, p={p:.3f}")
    else:
        print("Install scipy to run mannwhitneyu().")

if __name__ == "__main__":
    main()
