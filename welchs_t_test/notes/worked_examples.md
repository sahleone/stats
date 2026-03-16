---
title: "Welch's T-Test — Worked Examples"
author: MA235 Team
---

# Example 1: Streaming Time
Sample A (n₁ = 14): x̄₁ = 52 min, s₁ = 4.1. Sample B (n₂ = 10): x̄₂ = 48 min, s₂ = 6.3. Test α = 0.05, two-tailed.

- t = (52 − 48)/√(4.1²/14 + 6.3²/10) ≈ 1.80.
- ν ≈ 16.3, t* ≈ ±2.12 ⇒ |t| < t* ⇒ fail to reject H₀.
- 95% CI ≈ (−0.9, 8.9) minutes.

# Example 2: Assembly Output
Line A (n₁ = 9): x̄₁ = 105, s₁ = 5. Line B (n₂ = 13): x̄₂ = 98, s₂ = 3. Test α = 0.01, right-tailed.

- t = (105 − 98)/√(5²/9 + 3²/13) ≈ 4.15.
- ν ≈ 12.5, one-tailed critical t ≈ 2.68 ⇒ reject H₀.
- 99% CI (two-tailed) ≈ (3.3, 10.7).
- Conclusion: Line A has higher mean output.
