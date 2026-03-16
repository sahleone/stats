---
title: "Two-Sample T-Test (Equal Variances) — How-To"
author: MA235 Team
---

# Overview
Use this test to compare two independent group means when population variances can be treated as equal.

## Assumptions
1. Each sample is collected randomly and independently.
2. Observations within each group are independent.
3. Populations are approximately normal (or n ≥ 30 per group).
4. Population variances are equal (check with an F-test or prior knowledge).

## Hypotheses
- **H₀:** μ₁ = μ₂.
- **H₁:** μ₁ ≠ μ₂ (two-tailed) or μ₁ > μ₂ / μ₁ < μ₂ (directional).

## Procedure
1. **State hypotheses** and identify the comparison direction.
2. **Choose α** and determine tail type.
3. **Check assumptions** (normality, independence, equal variances).
4. **Compute descriptive stats**: x̄₁, x̄₂, s₁, s₂, n₁, n₂.
5. **Pooled standard deviation:**
   $$ s_p = \sqrt{\frac{(n_1-1)s_1^2 + (n_2-1)s_2^2}{n_1 + n_2 - 2}} $$
6. **Test statistic:**
   $$ t = \frac{\bar{x}_1 - \bar{x}_2}{s_p \sqrt{1/n_1 + 1/n_2}} $$
   with df = n₁ + n₂ − 2.
7. **Critical value:** t* = t_{α/2, df} (two-tailed) or t_{α, df} (one-tailed).
8. **p-value:** use t-distribution with df.
9. **Decision:** Reject H₀ if |t| > t* or p-value < α.
10. **Confidence interval:** (x̄₁ − x̄₂) ± t_{α/2,df}·s_p·√(1/n₁ + 1/n₂).
11. **Effect size:** d = (x̄₁ − x̄₂)/s_p.
12. **Conclusion:** State in context with CI and effect size.

## Related Tests
- Welch’s t-test: unequal variances.
- Mann-Whitney U: nonparametric alternative.
- F-test two variances: verify equal variance assumption.
