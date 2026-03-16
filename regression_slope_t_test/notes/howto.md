---
title: "Regression Slope t-Test — How-To"
author: MA235 Team
---

# Overview
Tests whether the slope coefficient β₁ is significantly different from zero in simple linear regression.

## Procedure
1. Fit regression model y = β₀ + β₁x + ε.
2. Obtain slope estimate b₁ and standard error SE(b₁).
3. Compute t = b₁/SE(b₁) with df = n − 2.
4. Compare to t_{α/2, n−2} (two-tailed) or t_{α, n−2} (one-tailed).
5. Report confidence interval for slope and R².

## Assumptions
- Errors have mean 0, constant variance, normal distribution.
- Observations independent.
- Relationship is linear.
