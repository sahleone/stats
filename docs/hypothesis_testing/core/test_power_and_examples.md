---
title: "Test Power and Examples"
author: MA235 Team
---

# Power Basics
- **Power (1 − β):** Probability the test correctly rejects a false H₀.
- Depends on α, effect size, sample size, and population variability.
- Higher power means a lower chance of missing a real effect.

# General Steps for Power Analysis
1. Specify H₀ and H₁ (including effect size of interest, e.g., difference Δ).
2. Choose α and tail direction.
3. Determine sample size (n) and distribution parameters.
4. Compute the noncentrality parameter or standardized effect.
5. Calculate β (probability of failing to reject) using statistical software or tables; power = 1 − β.

# Example 1 — One-Sample z-Test
- H₀: μ = 72, H₁: μ ≠ 72, σ known = 10, n = 36, α = 0.05.
- Critical z ≈ ±1.96; margin = 1.96 × (10/√36) ≈ 3.27.
- If true mean is 75 (Δ = 3), z-shift = Δ / (σ/√n) = 3 / (10/6) = 1.8.
- β ≈ P(|Z| < 1.96 − 1.8) ≈ 0.36 → Power ≈ 0.64.

# Example 2 — Two-Sample t-Test (Equal Variances)
- H₀: μ₁ = μ₂, H₁: μ₁ ≠ μ₂, σ assumed equal with s = 12, n₁ = n₂ = 15, α = 0.05.
- df = 28, critical t ≈ ±2.048.
- If true difference Δ = 8, standard error = s√(2/n) ≈ 4.38, noncentrality λ = Δ/SE ≈ 1.83.
- Approximate power via noncentral t or software (≈ 0.62). Increasing to n = 25 per group boosts power near 0.85.

# Example 3 — Chi-Square Goodness-of-Fit
- H₀: observed proportions match expected; α = 0.05, df = k − 1.
- Power depends on effect size w = √Σ((p_obs − p_exp)²/p_exp).
- With w = 0.3 (medium) and df = 4, n ≈ 88 yields power ≈ 0.80.

# Notes on Nonparametric Tests
Closed-form power formulas may not exist; rely on simulation or reference tables. Document limitations in each topic’s notes.

# Improving Power
- Increase sample size.
- Reduce measurement noise.
- Use one-tailed tests when justified (and pre-specified).
- Accept slightly higher α only if Type I consequences are tolerable.

# Checklist
- Report assumed effect size and α when stating power.
- Mention how power influenced sample-size decisions.
- For the MA235 project, remind students that n=15 per group fixes power; interpreting results should note this limitation.
