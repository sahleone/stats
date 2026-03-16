---
title: "Two-Sample T-Test (Equal Variances) — Worked Examples"
author: MA235 Team
---

# Example 1: Marketing Leads
**Problem.** Campaign A (n₁ = 18) produced x̄₁ = 45 leads, s₁ = 5.2. Campaign B (n₂ = 20) produced x̄₂ = 41 leads, s₂ = 6.0. Test H₀: μ₁ = μ₂ vs H₁: μ₁ ≠ μ₂ at α = 0.05.

**Solution.**
- Pooled sₚ = sqrt(((17)(5.2²) + (19)(6.0²)) / 36) ≈ 5.62.
- t = (45 − 41) / (5.62·√(1/18 + 1/20)) ≈ 2.32.
- df = 36, critical t = ±2.028 → |t| > t* ⇒ reject H₀.
- 95% CI: (45 − 41) ± 2.028·5.62·√(1/18 + 1/20) ⇒ (1.0, 6.0) leads.
- d = (45 − 41)/5.62 ≈ 0.71 (medium-large).
- Conclusion: Campaign A outperforms B.

# Example 2: Diet Comparison (Right-Tailed)
**Problem.** Diet 1 (n₁ = 12) mean loss 8.1 kg, s₁ = 2.0; Diet 2 (n₂ = 10) mean loss 6.5 kg, s₂ = 1.7. Test H₀: μ₁ = μ₂ vs H₁: μ₁ > μ₂ at α = 0.01.

**Solution.**
- sₚ = sqrt(((11)(2.0²) + (9)(1.7²)) / 20) ≈ 1.87.
- t = (8.1 − 6.5) / (1.87·√(1/12 + 1/10)) ≈ 2.44.
- df = 20, right-tailed critical t = 2.528 ⇒ t < crit ⇒ fail to reject H₀ at 1%; evidence insufficient despite practical difference.
- 95% CI: (1.6 ± 2.086·1.87·√(1/12 + 1/10)) ≈ (−0.1, 3.3) kg includes 0.
- d ≈ 0.86.
- Conclusion: Not significant at 1%; would be significant at α=0.05.
