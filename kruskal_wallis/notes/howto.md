---
title: "Kruskal-Wallis Test — How-To"
author: MA235 Team
---

# Overview
Extends the Mann-Whitney test to k > 2 independent groups using ranks.

## Procedure
1. Combine all observations, rank them, handle ties with average ranks.
2. For each group i, compute rank sum Rᵢ and size nᵢ.
3. Test statistic:
   $$ H = \frac{12}{N(N+1)} \sum \frac{R_i^2}{n_i} - 3(N+1) $$
4. Degrees of freedom: k − 1; approximate χ² distribution.
5. Decision: reject H₀ if H > χ²_{α, k−1}.
6. Effect size: η² = (H − k + 1)/(N − k).
7. If significant, run post-hoc tests (Dunn/Tukey on ranks).

## Assumptions
- Independent random samples.
- Response at least ordinal; distributions have similar shapes.

## Related Tests
- One-way ANOVA (parametric alternative).
- Dunn’s test (post-hoc).
