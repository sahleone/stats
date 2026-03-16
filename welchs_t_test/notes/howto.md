---
title: "Welch's T-Test — How-To"
author: MA235 Team
---

# Overview
Welch's t-test compares two independent means when population variances are unequal. It adjusts the degrees of freedom via the Welch–Satterthwaite equation.

## Assumptions
1. Two samples are independent and randomly selected.
2. Observations within each group are independent.
3. Populations are approximately normal (or sample sizes ≥ 30).
4. Variances may differ; no pooling required.

## Hypotheses
- **H₀:** μ₁ = μ₂
- **H₁:** μ₁ ≠ μ₂ (two-tailed) or μ₁ > μ₂ / μ₁ < μ₂.

## Steps
1. Identify x̄₁, x̄₂, s₁, s₂, n₁, n₂.
2. Compute the test statistic:
   $$ t = \frac{\bar{x}_1 - \bar{x}_2}{\sqrt{s_1^2/n_1 + s_2^2/n_2}} $$
3. Degrees of freedom:
   $$ \nu = \frac{(s_1^2/n_1 + s_2^2/n_2)^2}{(s_1^2/n_1)^2/(n_1-1) + (s_2^2/n_2)^2/(n_2-1)} $$
4. Critical value: use t_{α/2, ν} (two-tailed) or t_{α, ν} (one-tailed).
5. p-value: compute from t-distribution with ν df.
6. Decision: reject H₀ if |t| > t* or p-value < α.
7. Confidence interval: (x̄₁ − x̄₂) ± t_{α/2,ν}·√(s₁²/n₁ + s₂²/n₂).
8. Effect size: d = (x̄₁ − x̄₂)/√((s₁² + s₂²)/2).
9. State conclusion in context.

## Related Tests
- Two-sample t (equal variances) when variances match.
- Mann-Whitney U for nonparametric comparison.
