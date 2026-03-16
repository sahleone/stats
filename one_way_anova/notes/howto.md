---
title: "One-Way ANOVA — How-To"
author: MA235 Team
---

# Overview
One-way ANOVA compares k independent group means using the F statistic.

## Assumptions
1. Random, independent samples.
2. Approximately normal distribution within each group.
3. Equal variances across groups (homoscedasticity).

## Hypotheses
- **H₀:** μ₁ = μ₂ = ... = μ_k.
- **H₁:** At least one mean differs.

## Steps
1. Compute group means x̄ᵢ, group sizes nᵢ, overall mean x̄.
2. SS_between = Σ nᵢ (x̄ᵢ − x̄)².
3. SS_within = Σ Σ (xᵢⱼ − x̄ᵢ)².
4. df_between = k − 1; df_within = N − k.
5. MS_between = SS_between/df_between; MS_within = SS_within/df_within.
6. F = MS_between / MS_within.
7. Critical value: F_{α, df_between, df_within}.
8. Decision: reject if F > critical or p-value < α.
9. Effect size: η² = SS_between / SS_total.
10. If significant, run post-hoc tests (Tukey, Bonferroni) to pinpoint differences.

## Related Tests
- Kruskal-Wallis (nonparametric alternative).
- F-test two variances (assumption check).
