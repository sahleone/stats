---
title: "Paired T-Test — Confidence Interval"
author: MA235 Team
---

# Formula
$$ \bar{d} \pm t_{\alpha/2, n-1} \cdot \frac{s_d}{\sqrt{n}} $$
where d̄ is the mean difference and s_d is the standard deviation of differences.

# Example
Heart-rate data: d̄ = 6.1, s_d = 4.0, n = 12 ⇒ 95% CI = 6.1 ± 2.201·4.0/√12 ⇒ (3.6, 8.6).

# Interpretation
If 0 lies outside the interval, the two-tailed paired t-test at α matches the CI decision (reject H₀ when 0 not in CI).
