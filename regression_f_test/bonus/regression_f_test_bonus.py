"""Regression F-test demonstration using statsmodels if available."""
from __future__ import annotations

try:
    import statsmodels.api as sm
except ImportError:
    sm = None


def main() -> None:
    if sm is None:
        print("Install statsmodels to run regression F-test.")
        return
    import numpy as np
    x = np.column_stack([
        [1,2,3,4,5,6,7,8,9,10],
        [2,3,1,4,6,5,7,8,5,6],
        [5,3,6,2,7,4,5,6,7,8],
    ])
    y = np.array([10,12,13,15,17,18,20,21,19,22])
    x = sm.add_constant(x)
    model = sm.OLS(y, x).fit()
    print(model.summary())

if __name__ == "__main__":
    main()
