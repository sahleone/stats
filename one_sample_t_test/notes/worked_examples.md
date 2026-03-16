---
title: "One-Sample T-Test — Worked Examples"
author: MA235 Team
---

# Example 1: Quiz Score Claim
**Problem.** Instructor claims average quiz score is 85. Twelve quizzes yield x̄ = 81.6, s = 6.3. Test at α = 0.05 two-tailed.

**Solution.**
- H₀: μ = 85, H₁: μ ≠ 85.
- df = 11, t* = ±2.201.
- t = (81.6 − 85)/(6.3/√12) ≈ −1.86.
- p-value ≈ 0.090 (> 0.05) ⇒ fail to reject H₀.
- 95% CI: 81.6 ± 2.201·6.3/√12 ⇒ (77.6, 85.6).
- Effect size d = (81.6 − 85)/6.3 = −0.54 (medium).
- Conclusion: Evidence insufficient to show the mean differs from 85.

# Example 2: Coffee Temperature Safety
**Problem.** Safety spec says mean dispensing temp should be 140°F. A shop samples 15 cups: x̄ = 142.3°F, s = 3.5°F. Test right-tailed (H₁: μ > 140) at α = 0.01.

**Solution.**
- df = 14; t* = 2.624.
- t = (142.3 − 140)/(3.5/√15) ≈ 2.89.
- p ≈ 0.006 < 0.01 ⇒ reject H₀.
- 99% CI (two-tailed for reporting): 142.3 ± 2.977·3.5/√15 ⇒ (139.6, 145.0) — partially above 140.
- d = (142.3 − 140)/3.5 ≈ 0.66 (medium-large).
- Conclusion: Coffee is significantly hotter than 140°F; adjust machine.
