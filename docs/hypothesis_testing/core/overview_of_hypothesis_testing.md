---
title: "Hypothesis Testing Overview"
author: MA235 Team
---

# Purpose
Hypothesis testing evaluates whether sample evidence is strong enough to challenge a claim about a population parameter. Every test follows the same high-level structure: state hypotheses, choose a significance level, compute a test statistic, and compare it to a rejection threshold (critical region or p-value).

# Hypotheses
- **Null (H₀):** Represents "no effect" or the status quo; always includes equality ( =, ≤, ≥ ).
- **Alternative (H₁):** Represents the research claim; can be two-tailed (≠), left-tailed (<), or right-tailed (>).

# Critical Regions & Tail Types
- **Two-tailed:** Shaded regions on both ends of the curve (± critical); reject H₀ when statistic ≤ −t* or ≥ +t*.
- **Left-tailed:** Shaded region on the left; reject H₀ when statistic ≤ critical value.
- **Right-tailed:** Shaded region on the right; reject H₀ when statistic ≥ critical value.

> **Alt-text:** Each diagram shows a bell curve with shaded rejection areas corresponding to the row description.

# Significance Level (α)
α is the probability of committing a Type I error. Common choices: 0.10, 0.05, 0.01. Split α across tails for two-tailed tests.

# Test Statistic
General form: (estimate − hypothesized value) / standard error. The distribution (z, t, χ², F) depends on the test, sample size, and assumptions.

# Decision Approaches
1. **Critical Value Approach:** Compute the critical value(s) using α and df; reject if statistic falls in rejection region.
2. **p-Value Approach:** Compute p-value; reject if p-value < α.

# Workflow
1. Translate the claim into H₀/H₁.
2. Set α and determine tail direction.
3. Check assumptions (randomness, independence, distribution requirements).
4. Gather data and compute descriptive stats.
5. Calculate the test statistic.
6. Find critical value(s) or p-value.
7. State decision (reject / fail to reject) and interpret in context.
8. Pair with a confidence interval when possible for estimation insight.

# Related Resources
- See `type1_type2_errors.pdf` for error definitions.
- See `test_power_and_examples.pdf` for power analysis.
- Consult per-topic how-to PDFs for assumptions and formulas.
