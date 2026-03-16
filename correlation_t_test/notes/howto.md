---
title: "Correlation t-Test — How-To"
author: MA235 Team
---

# Overview
Tests whether the Pearson correlation coefficient differs from zero.

## Procedure
1. Calculate sample correlation r from paired data.
2. Compute t-statistic: t = r√(n − 2)/√(1 − r²) with df = n − 2.
3. Compare t to t_{α/2, n−2} (two-tailed) or t_{α, n−2} (one-tailed).
4. Report r, r², t, df, p-value, and confidence interval for ρ using Fisher z-transform.

## Assumptions
- Pairs are independent.
- Relationship is linear.
- Both variables approximately normal (bivariate normality).
