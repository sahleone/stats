---
title: "Two-Sample Z-Test (Means, σ Known) — How-To"
author: MA235 Team
---

# Overview
Compare two independent population means when both population standard deviations are known.

## Assumptions
1. Random, independent samples.
2. Known σ₁ and σ₂.
3. Populations normal or sample sizes large (n ≥ 30).

## Hypotheses
- **H₀:** μ₁ = μ₂.
- **H₁:** μ₁ ≠ μ₂ (two-tailed) or μ₁ > μ₂ / μ₁ < μ₂.

## Steps
1. Gather n₁, n₂, x̄₁, x̄₂, σ₁, σ₂.
2. Compute test statistic:
   $$ z = \frac{\bar{x}_1 - \bar{x}_2}{\sqrt{\sigma_1^2/n_1 + \sigma_2^2/n_2}} $$
3. Critical value: z_{α/2} for two-tailed or z_{α} for one-tailed.
4. p-value: use standard normal distribution.
5. Decision: reject H₀ if |z| > z* or p-value < α.
6. Confidence interval: (x̄₁ − x̄₂) ± z_{α/2}·√(σ₁²/n₁ + σ₂²/n₂).
7. Effect size: d = (x̄₁ − x̄₂)/√((σ₁² + σ₂²)/2).
8. Conclude in context.

## Related Tests
- Two-sample t (equal variances) when σ unknown.
- Welch’s t-test when σ unknown and variances unequal.
