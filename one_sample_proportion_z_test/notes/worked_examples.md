---
title: "One-Sample Proportion Z-Test — Worked Examples"
author: MA235 Team
---

# Example 1: Brand Preference
Claim: 60% prefer Brand A. In n = 200, x = 132 prefer Brand A (p̂ = 0.66). Test H₀: p = 0.60 vs H₁: p > 0.60 at α = 0.05.

- Assumptions: n·p₀ = 120, n·(1−p₀) = 80 ≥ 5.
- z = (0.66 − 0.60)/√(0.60·0.40/200) ≈ 2.19.
- Critical z = 1.645 (right-tailed). Since 2.19 > 1.645, reject H₀.
- p-value ≈ 0.014.
- 95% CI: 0.66 ± 1.960·√(0.66·0.34/200) ⇒ (0.59, 0.73).
- Effect size h ≈ 0.13 (small).

# Example 2: Defect Rate Drop
H₀: p = 0.03 vs H₁: p < 0.03. Sample n = 400, x = 18 defects (p̂ = 0.045). α = 0.01.

- z = (0.045 − 0.03)/√(0.03·0.97/400) ≈ 2.22.
- Because p̂ > p₀, evidence points opposite direction; fail to reject H₀ (left-tailed test needs negative z).
- 99% CI: 0.045 ± 2.576·√(0.045·0.955/400) ⇒ (0.028, 0.062).
- Conclusion: No evidence for reduction; defects may be higher than 3%.
