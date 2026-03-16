---
title: "Chi-Square Goodness-of-Fit Test — How-To"
author: MA235 Team
---

# Overview
Evaluate whether observed categorical frequencies follow a specified expected distribution.

## Assumptions
1. Random sample; observations are independent.
2. Expected counts ≥ 5 (combine categories if needed).
3. Categories are mutually exclusive and collectively exhaustive.

## Hypotheses
- **H₀:** Observed distribution matches expected proportions.
- **H₁:** Observed distribution differs from expectations.

## Procedure
1. Tabulate observed counts Oᵢ and expected counts Eᵢ = n·pᵢ.
2. Compute test statistic:
   $$ \chi^2 = \sum \frac{(O_i - E_i)^2}{E_i} $$
3. Degrees of freedom: df = k − 1 − m (k categories, m estimated parameters).
4. Critical value: χ²_{α, df}.
5. Decision: reject H₀ if χ² > χ²_{α, df}; p-value from chi-square distribution.
6. Effect size: Cohen’s w = √(Σ((O − E)²/E) / n).
7. Identify which categories contribute most (large |O − E|/E).
8. Conclude in context.

## Related Tests
- Two-proportion z (k = 2 case).
- Chi-square test of independence for contingency tables.
