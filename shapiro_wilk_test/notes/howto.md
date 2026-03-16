---
title: "Shapiro-Wilk Test — How-To"
author: MA235 Team
---

# Overview
Assesses normality by comparing ordered sample values to expected normal order statistics.

## Procedure
1. Sort data x₁ ≤ x₂ ≤ … ≤ xₙ.
2. Compute W = (Σ aᵢ x_(n+1−i))² / Σ (xᵢ − x̄)², where aᵢ are constants (software handles).
3. Obtain p-value from W and sample size n.
4. Decision: reject H₀ if p < α (data not normal).
5. Always pair with visual checks (histogram, Q-Q plot).

## Assumptions
- Sample is random.
- Continuous distribution.

## Related
- Anderson-Darling, Kolmogorov-Smirnov tests for normality.
