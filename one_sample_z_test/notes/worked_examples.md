---
title: "One-Sample Z-Test — Worked Examples"
author: MA235 Team
---

# Example 1: Battery Life Claim
**Problem.** A manufacturer claims the mean battery life is 10 hours. Past data show σ = 1.2 hours. A random sample of 36 batteries averages 9.6 hours. Test H₀: μ = 10 vs H₁: μ ≠ 10 at α = 0.05.

**Solution.**
1. H₀: μ = 10, H₁: μ ≠ 10.
2. σ = 1.2, n = 36, α = 0.05, z* = ±1.960.
3. Assumptions satisfied (random, n ≥ 30).
4. z = (9.6 − 10)/(1.2/√36) = −2.0.
5. p-value = 2·P(Z < −2.0) ≈ 0.0455.
6. Decision: reject H₀ (|−2.0| > 1.960).
7. CI: 9.6 ± 1.960·1.2/√36 = 9.6 ± 0.392 ⇒ (9.208, 9.992).
8. Effect size: d = (9.6 − 10)/1.2 = −0.33 (medium).
9. Conclusion: At α = 0.05, evidence suggests the mean battery life differs from 10 hours (CI excludes 10 on upper side barely, effect moderate).

# Example 2: Commute Time Increase
**Problem.** Historical average commute time was 38 minutes with σ = 6 minutes. After a route change, 40 commuters average 40.5 minutes. Test if the mean increased (right-tailed) at α = 0.01.

**Solution.**
1. H₀: μ = 38, H₁: μ > 38.
2. σ = 6, n = 40, α = 0.01, critical z = 2.326.
3. Assumptions: random sample, n ≥ 30.
4. z = (40.5 − 38)/(6/√40) ≈ 2.64.
5. p-value = P(Z > 2.64) ≈ 0.0041.
6. Decision: reject H₀ (2.64 > 2.326).
7. CI (99% two-tailed for reporting): 40.5 ± 2.576·6/√40 ⇒ (38.55, 42.45).
8. Effect size: d = (40.5 − 38)/6 = 0.42 (medium).
9. Conclusion: Commute times increased significantly at the 1% level.
