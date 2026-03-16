---
title: "Regression F-Test — How-To"
author: MA235 Team
---

# Overview
Evaluates whether the overall regression model explains significant variance (multiple predictors).

## Procedure
1. Fit regression with p predictors.
2. Compute SS_regression and SS_error.
3. F = (SS_regression/p) / (SS_error/(n − p − 1)).
4. Compare to critical F_{α, p, n−p−1} or use p-value.
5. Report R² and adjusted R².

## Assumptions
- Errors are independent, normally distributed, with constant variance.
- Model is linear in parameters.
