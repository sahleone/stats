"""Shapiro-Wilk test using scipy if available."""
from __future__ import annotations

try:
    from scipy import stats
except ImportError:
    stats = None


def main() -> None:
    data = [5.2, 4.9, 5.1, 5.0, 5.3, 5.2, 5.4, 5.1]
    if stats:
        stat, p = stats.shapiro(data)
        print(f"W={stat:.3f}, p={p:.3f}")
    else:
        print("Install scipy to run shapiro().")

if __name__ == "__main__":
    main()
