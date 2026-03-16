---
title: "Wilcoxon Signed-Rank Test — How-To"
author: MA235 Team
---

# Overview
Nonparametric paired test that considers both sign and magnitude (ranks) of differences.

## Procedure
1. Compute differences dᵢ = after − before; drop zeros.
2. Rank |dᵢ| (smallest rank 1; handle ties by averaging ranks).
3. Attach signs to ranks; sum positive ranks (W+) and negative ranks (W−).
4. Test statistic W = min(W+, W−) for two-tailed; compare to critical value for n pairs.
5. For n ≥ 10, use normal approximation: z = (W − μ_W)/σ_W with μ_W = n(n+1)/4 and σ_W = √(n(n+1)(2n+1)/24).
6. Decision: reject H₀ if W ≤ critical or |z| > z_{α/2}.
7. Effect size: rank-biserial r = 1 − (2W / [n(n+1)/2]).

## Assumptions
- Pairs are independent.
- Differences are symmetrically distributed.

## Related Tests
- Sign test (less powerful).
- Paired t-test (parametric).
