---
title: "Paired T-Test — How-To"
author: MA235 Team
---

# Overview
The paired t-test analyzes the mean of paired differences (before–after, matched subjects) to determine whether the average change is zero.

## Assumptions
1. Pairs are meaningful and randomly selected.
2. Differences between pairs are independent.
3. Differences follow an approximately normal distribution (or n ≥ 30 pairs).

## Hypotheses
- **H₀:** μ_d = 0 (no mean change).
- **H₁:** μ_d ≠ 0 (two-tailed) or μ_d > 0 / μ_d < 0 for directional alternatives.

## Procedure
1. Compute each difference dᵢ = xᵢ(before) − xᵢ(after) (or vice versa, but stay consistent).
2. Calculate d̄, s_d, n.
3. Test statistic: $$ t = \frac{\bar{d}}{s_d / \sqrt{n}} $$ with df = n − 1.
4. Critical value: t_{α/2, n−1} for two-tailed; t_{α, n−1} for one-tailed.
5. p-value: use t-distribution with df = n − 1.
6. Decision: reject H₀ if |t| > t* or p-value < α.
7. Confidence interval: d̄ ± t_{α/2,df}·s_d/√n.
8. Effect size: d = d̄ / s_d.
9. Interpret in original measurement units (increase/decrease).

## Related Tests
- One-sample t-test (apply to differences).
- Wilcoxon Signed-Rank (nonparametric alternative).
- Sign test (when only direction matters).
