---
title: "One-Sample Proportion Z-Test — How-To"
author: MA235 Team
---

# Overview
Tests whether a population proportion differs from a hypothesized value using the normal approximation to the binomial.

## Assumptions
1. Random sample with categorical (success/failure) outcomes.
2. Observations are independent.
3. Sample size large enough: n·p₀ ≥ 5 and n·(1 − p₀) ≥ 5.

## Hypotheses
- **H₀:** p = p₀.
- **H₁:** p ≠ p₀ (two-tailed) or p > p₀ / p < p₀.

## Procedure
1. Count successes x and sample size n; compute p̂ = x/n.
2. Check assumptions (normal approximation valid).
3. Test statistic:
   $$ z = \frac{\hat{p} - p_0}{\sqrt{p_0(1 - p_0)/n}} $$
4. Critical value: use z_{α/2} for two-tailed or z_{α} for one-tailed.
5. p-value: normal distribution tail probability.
6. Decision: reject H₀ if z lies in rejection region or p-value < α.
7. Confidence interval: p̂ ± z_{α/2}·√(p̂(1 − p̂)/n).
8. Effect size: Cohen’s h = 2·arcsin(√p̂) − 2·arcsin(√p₀).
9. Interpret result in terms of proportions.

## Related Tests
- Two-proportion z-test for comparing two groups.
- Chi-square goodness-of-fit for multiple categories.
