---
title: "Chi-Square Goodness-of-Fit Test — Worked Examples"
author: MA235 Team
---

# Example 1: Die Fairness
Observed counts from 120 rolls: [18, 19, 23, 20, 21, 19]. Expected = 20 each.

- χ² = Σ((O − 20)²/20) ≈ 1.8.
- df = 5, χ²_{0.05,5} = 11.07 ⇒ fail to reject; die appears fair.

# Example 2: Survey Preferences
Categories A/B/C expected 50%/30%/20% (p = 0.5,0.3,0.2). Observed counts (n=200): [120, 50, 30].

- Expected E = [100, 60, 40].
- χ² = ((120−100)²/100) + ((50−60)²/60) + ((30−40)²/40) = 4 + 1.67 + 2.5 = 8.17.
- df = 2, χ²_{0.05,2} = 5.99 ⇒ reject H₀.
- Categories A and C deviate most (positive residuals).
