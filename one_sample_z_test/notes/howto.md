---
title: "One-Sample Z-Test — How-To"
author: MA235 Team
---

# Overview
Use the one-sample z-test to decide whether a population mean equals a stated value when the population standard deviation σ is known (or sample size is large enough to treat s ≈ σ).

## Assumptions
1. Random sample or randomized experiment.
2. Observations are independent.
3. Population is normal or sample size ≥ 30 (Central Limit Theorem).
4. Population standard deviation σ is known.

## Hypotheses
- **Null (H₀):** μ = μ₀.
- **Alternative (H₁):** μ ≠ μ₀ (two-tailed), μ > μ₀ (right-tailed), or μ < μ₀ (left-tailed).

## Procedure
1. **State the claim** and express it as H₁; write H₀ with equality (μ = μ₀).
2. **Choose α** (commonly 0.05) and determine tail direction.
3. **Check assumptions** (randomness, independence, normality or large n, known σ).
4. **Compute descriptive statistics:** sample mean x̄ and size n.
5. **Calculate the test statistic:**
   $$ z = \frac{\bar{x} - \mu_0}{\sigma / \sqrt{n}} $$
6. **Critical value approach:** find z* (e.g., ±1.960 for α = 0.05 two-tailed) and compare |z| to z*.
7. **p-value approach:** compute p-value = 2·P(Z > |z|) for two-tailed (adjust for one-tailed).
8. **Decision:** Reject H₀ if z falls in the critical region or if p-value < α.
9. **Confidence interval:** report x̄ ± z_{α/2}·σ/√n to quantify the estimate.
10. **Effect size:** d = (x̄ − μ₀)/σ (interpret: 0.2 small, 0.5 medium, 0.8 large).
11. **Conclusion:** Write in context (“At the 5% level, there is/not sufficient evidence that...”).

> **Alt-text:** If you include a curve graphic, describe which tail(s) are shaded and what α represents.

## Decision Reference
- Critical region (two-tailed): reject H₀ when |z| > z_{α/2}.
- Critical region (right-tailed): reject H₀ when z > z_{α}.
- Critical region (left-tailed): reject H₀ when z < −z_{α}.
- p-value rule: reject when p-value < α.

## See Also
- `one_sample_t_test` — σ unknown.
- `shapiro_wilk_test` — verify normality when n is small.
- `welchs_t_test` — for comparing two means with unequal variances.
