"""Kruskal-Wallis demo using scipy if available."""
from __future__ import annotations

try:
    from scipy.stats import kruskal
except ImportError:
    kruskal = None


def main() -> None:
    g1 = [4, 5, 6, 7, 5]
    g2 = [6, 8, 7, 9, 8]
    g3 = [3, 4, 5, 4, 3]
    if kruskal:
        stat, p = kruskal(g1, g2, g3)
        print(f"H={stat:.2f}, p={p:.3f}")
    else:
        print("Install scipy to run kruskal().")

if __name__ == "__main__":
    main()
