"""Chi-square goodness-of-fit helper."""
from __future__ import annotations


def chi_square_stat(observed: list[int], expected: list[float]) -> float:
    return sum((o - e) ** 2 / e for o, e in zip(observed, expected))


def main() -> None:
    observed = [120, 50, 30]
    total = sum(observed)
    expected = [0.5 * total, 0.3 * total, 0.2 * total]
    chi2 = chi_square_stat(observed, expected)
    print(f"chi-square statistic = {chi2:.2f}")

if __name__ == "__main__":
    main()
