"""Fisher's exact test example using scipy if available."""
from __future__ import annotations

try:
    from scipy.stats import fisher_exact
except ImportError:
    fisher_exact = None


def main() -> None:
    table = [[4, 1], [1, 4]]
    if fisher_exact:
        oddsratio, p_value = fisher_exact(table, alternative="two-sided")
        print(f"OR={oddsratio:.2f}, p={p_value:.3f}")
    else:
        print("scipy not available; compute hypergeometric probability manually.")

if __name__ == "__main__":
    main()
