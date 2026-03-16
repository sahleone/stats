---
title: "Mann-Whitney U Test — How-To"
author: MA235 Team
---

# Overview
Compares two independent samples using ranks; detects shifts in medians without assuming normality.

## Steps
1. Combine all observations and assign ranks (ties get average ranks).
2. Sum ranks for each group (R₁, R₂).
3. Compute U statistics: U₁ = n₁n₂ + n₁(n₁+1)/2 − R₁, U₂ = n₁n₂ − U₁.
4. Test statistic U = min(U₁, U₂).
5. For small samples, compare U to critical value from tables; for larger samples, use normal approximation (with tie correction):
   $$ Z = \frac{U - n_1 n_2 / 2}{\sqrt{n_1 n_2 (n_1 + n_2 + 1)/12}} $$
6. Decision: reject H₀ if U ≤ critical or |Z| > z_{α/2}.
7. Effect size: r = Z/√(n₁ + n₂) or rank-biserial correlation.

## Assumptions
- Two independent random samples.
- Response is ordinal or continuous.
- Distributions have similar shapes (for median interpretation).
