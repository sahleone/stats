---
title: "Sign Test — How-To"
author: MA235 Team
---

# Overview
Nonparametric alternative to the paired t-test that uses only the direction (+/−) of paired differences. Tests whether the median difference equals zero.

## Assumptions
1. Pairs are independent and randomly selected.
2. Differences are continuous; ties (zero differences) are discarded.

## Hypotheses
- **H₀:** median difference = 0 (probability of positive sign is 0.5).
- **H₁:** median difference ≠ 0 (two-tailed) or > 0 / < 0.

## Procedure
1. Compute differences dᵢ = after − before (or vice versa). Drop pairs where dᵢ = 0.
2. Let n = number of nonzero differences; x = # positives.
3. Under H₀, X ~ Binomial(n, 0.5).
4. Two-tailed p-value: P(X ≤ min(x, n−x)) × 2 (or exact cumulative sum). One-tailed p-value uses appropriate tail.
5. For n ≥ 10, use normal approximation: z = (x − n/2)/√(n/4) with continuity correction.
6. Decision: reject H₀ if p-value < α.
7. Report effect size as proportion of positives/negatives or as Hodges-Lehmann median difference (optional).
8. Conclude in context.

## Related Tests
- Signed-rank (Wilcoxon) test — uses ranks for more power.
- Paired t-test — parametric alternative when normality holds.
