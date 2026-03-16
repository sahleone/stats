"""Regression slope t-test using scipy if available."""
from __future__ import annotations

try:
    from scipy import stats
except ImportError:
    stats = None


def main() -> None:
    x = [1,2,3,4,5,6,7,8,9,10]
    y = [3,4,4,5,6,7,8,9,10,11]
    if stats:
        slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
        print(f"b1={slope:.2f}, SE={std_err:.2f}, p={p_value:.3f}")
    else:
        print("Install scipy to compute regression slope test.")

if __name__ == "__main__":
    main()
