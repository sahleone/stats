"""Correlation t-test example using scipy if available."""
from __future__ import annotations

try:
    from scipy import stats
except ImportError:
    stats = None


def main() -> None:
    x = [5, 7, 6, 9, 8, 4, 10, 11, 7, 9]
    y = [68, 72, 70, 78, 76, 65, 82, 85, 71, 79]
    if stats:
        r, p = stats.pearsonr(x, y)
        print(f"r={r:.2f}, p={p:.3f}")
    else:
        print("Install scipy to compute correlation p-values.")

if __name__ == "__main__":
    main()
