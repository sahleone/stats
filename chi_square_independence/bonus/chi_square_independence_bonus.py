"""Chi-square independence helper."""
from __future__ import annotations

import numpy as np


def chi_square_independence(table: list[list[int]]) -> tuple[float, float]:
    arr = np.array(table, dtype=float)
    row_totals = arr.sum(axis=1)
    col_totals = arr.sum(axis=0)
    n = arr.sum()
    expected = np.outer(row_totals, col_totals) / n
    chi2 = ((arr - expected) ** 2 / expected).sum()
    df = (arr.shape[0] - 1) * (arr.shape[1] - 1)
    return chi2, df


def main() -> None:
    table = [[30, 20], [25, 35]]
    chi2, df = chi_square_independence(table)
    print(f"chi²={chi2:.2f}, df={df}")

if __name__ == "__main__":
    main()
