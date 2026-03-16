---
title: "Chi-Square Test of Independence — How-To"
author: MA235 Team
---

# Overview
Tests whether two categorical variables (rows vs columns) are associated.

## Assumptions
1. Random sample; observations contribute to one cell only.
2. Expected count in each cell ≥ 5 (combine categories if needed).

## Hypotheses
- **H₀:** Variables are independent.
- **H₁:** Variables are not independent.

## Procedure
1. Build an r × c contingency table of observed counts Oᵢⱼ.
2. Compute expected counts Eᵢⱼ = (rowᵢ total × colⱼ total) / n.
3. Test statistic: χ² = Σ (Oᵢⱼ − Eᵢⱼ)² / Eᵢⱼ.
4. Degrees of freedom: (r − 1)(c − 1).
5. Critical value: χ²_{α, (r−1)(c−1)}.
6. Decision: reject H₀ if χ² > critical value; p-value from χ² distribution.
7. Effect size: Cramér’s V = √(χ² / (n·min(r−1, c−1))).
8. Examine standardized residuals to see which cells drive the association.
9. State conclusion in context (describe relationship).

## Related Tests
- Two-proportion z-test (2×2 case).
- Fisher’s Exact Test for small 2×2 tables.
