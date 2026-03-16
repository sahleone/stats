---
title: "One-Sample T-Test — How-To"
author: MA235 Team
---

# Overview
Use the one-sample t-test when you want to compare a sample mean to a claimed population mean but the population standard deviation is unknown.

## Assumptions
1. Random sample or randomized experiment.
2. Observations are independent.
3. Population is approximately normal or sample size ≥ 30.
4. Population standard deviation is unknown (estimate with sample s).

## Hypotheses
- **H₀:** μ = μ₀.
- **H₁:** μ ≠ μ₀ (two-tailed), μ > μ₀ (right), or μ < μ₀ (left).

## Steps
1. **State hypotheses** from the claim.
2. **Set α** and choose tail direction.
3. **Check assumptions** (randomness, independence, normality/CLT).
4. **Compute stats:** x̄, s, n.
5. **Test statistic:** $$ t = \frac{\bar{x} - \mu_0}{s / \sqrt{n}} $$ with df = n − 1.
6. **Critical value:** find t* = t_{α/2, df} (two-tailed) or appropriate one-tailed value.
7. **p-value:** use t-distribution with df = n − 1.
8. **Decision:** Reject H₀ if |t| > t* or if p-value < α.
9. **Confidence interval:** x̄ ± t_{α/2,df}·s/√n.
10. **Effect size:** Cohen’s d = (x̄ − μ₀)/s.
11. **Conclusion:** Describe in context (mention CI + effect size).

## Decision Reminders
- Two-tailed: reject when |t| > t_{α/2,df}.
- Right-tailed: reject when t > t_{α,df}.
- Left-tailed: reject when t < −t_{α,df}.

## Related Tests
- One-sample z-test (σ known).
- Shapiro-Wilk (normality check).
- Wilcoxon Signed-Rank (nonparametric alternative).
