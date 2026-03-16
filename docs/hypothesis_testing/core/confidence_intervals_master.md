---
title: "Confidence Intervals Master Guide"
author: MA235 Team
---

# Purpose
Confidence intervals (CIs) estimate plausible ranges for population parameters and pair naturally with hypothesis tests. If the null value lies outside the CI, the test will reject at the corresponding α (for two-tailed tests).

# General Form
Estimate ± (critical value × standard error).

# Mapping Cheat Sheet
- **One-sample z (mean):** \( \bar{x} \pm z_{\alpha/2} \frac{\sigma}{\sqrt{n}} \) (σ known).
- **One-sample t:** \( \bar{x} \pm t_{\alpha/2, df} \frac{s}{\sqrt{n}} \) (σ unknown).
- **Two-sample t (equal variances):** \( (\bar{x}_1 - \bar{x}_2) \pm t_{\alpha/2, df} s_p \sqrt{1/n_1 + 1/n_2} \) using pooled \(s_p\).
- **Two-proportion z:** \( (\hat{p}_1 - \hat{p}_2) \pm z_{\alpha/2} \sqrt{\frac{\hat{p}_1(1-\hat{p}_1)}{n_1} + \frac{\hat{p}_2(1-\hat{p}_2)}{n_2}} \).
- **Chi-square variance:** \( \frac{(n-1)s^2}{\chi^2_{\alpha/2, df}} \leq \sigma^2 \leq \frac{(n-1)s^2}{\chi^2_{1-\alpha/2, df}} \) (asymmetric interval).
- **F-test (variance ratio):** \( \frac{s_1^2}{s_2^2} \times \left[ \frac{1}{F_{1-\alpha/2}}, \frac{1}{F_{\alpha/2}} \right] \) — order matters.
- **Nonparametric tests:** rely on rank-based or bootstrap intervals; see topic-specific notes.

# Example Interpretation
"We are 95% confident that the true mean difference lies between −2.3 and 1.1 units, so zero is included and we fail to reject H₀ at α = 0.05."

# Ties to Hypothesis Tests
- Two-tailed test at α ↔ CI with confidence 1 − α.
- One-tailed tests need custom intervals; state that explicitly if used.

# Guidance
- Always state confidence level, statistic, and context.
- Mention if the interval was built under pooled or unpooled variance assumptions.
- Link to test-specific CI notes for derivations beyond this summary.
