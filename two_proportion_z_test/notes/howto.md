---
title: "Two-Proportion Z-Test — How-To"
author: MA235 Team
---

# Overview
Determines whether two population proportions differ using independent binomial samples.

## Assumptions
1. Samples are random, independent, and categorical.
2. Normal approximation holds: n₁·p̂₁ ≥ 5, n₁·(1 − p̂₁) ≥ 5, n₂·p̂₂ ≥ 5, n₂·(1 − p̂₂) ≥ 5.

## Hypotheses
- **H₀:** p₁ = p₂.
- **H₁:** p₁ ≠ p₂, p₁ > p₂, or p₁ < p₂.

## Procedure
1. Compute sample proportions p̂₁ = x₁/n₁, p̂₂ = x₂/n₂.
2. Pooled proportion: p̂ = (x₁ + x₂)/(n₁ + n₂).
3. Test statistic:
   $$ z = \frac{\hat{p}_1 - \hat{p}_2}{\sqrt{\hat{p}(1 - \hat{p})(1/n_1 + 1/n_2)}} $$
4. Critical value: z_{α/2} (two-tailed) or z_{α} (one-tailed).
5. p-value: standard normal tail probability.
6. Decision: reject H₀ if |z| > z* or p-value < α.
7. Confidence interval: (p̂₁ − p̂₂) ± z_{α/2}·√(p̂₁(1 − p̂₁)/n₁ + p̂₂(1 − p̂₂)/n₂).
8. Effect size: Cohen’s h = 2·arcsin(√p̂₁) − 2·arcsin(√p̂₂).
9. Conclusion: describe practical difference.

## Related Tests
- Fisher’s Exact Test for small samples.
- Chi-square test of independence for contingency tables.
