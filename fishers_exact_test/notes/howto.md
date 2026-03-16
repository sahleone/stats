---
title: "Fisher's Exact Test — How-To"
author: MA235 Team
---

# Overview
Evaluates association in a 2×2 contingency table using exact hypergeometric probabilities (when sample sizes are small or expected counts < 5).

## Assumptions
1. 2×2 table with fixed margins (row/column totals).
2. Random sample; observations independent.

## Hypotheses
- **H₀:** Odds of success are equal in both groups (variables independent).
- **H₁:** Odds differ (choose two-tailed or directional alternative).

## Procedure
1. Arrange data in 2×2 table with counts a, b, c, d.
2. Compute table probability using hypergeometric formula:
   $$ P(a) = \frac{\binom{a+b}{a} \binom{c+d}{c}}{\binom{n}{a+c}} $$
3. For a two-tailed test, sum probabilities of tables with probability ≤ observed P(a) while keeping margins fixed.
4. For a one-tailed test, sum probabilities of tables as extreme in the specified direction.
5. Compare exact p-value to α.
6. Effect size: report odds ratio OR = (a·d)/(b·c) and confidence interval if desired.
7. Conclude whether association exists.

## Related Tests
- Chi-square test of independence (large samples).
