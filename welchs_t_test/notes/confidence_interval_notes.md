---
title: "Welch's T-Test — Confidence Interval"
author: MA235 Team
---

# Formula
$$ (\bar{x}_1 - \bar{x}_2) \pm t_{\alpha/2, \nu} \cdot \sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}} $$
with ν from the Welch-Satterthwaite formula.

# Example
Streaming data: difference = 4, SE = √(4.1²/14 + 6.3²/10) ≈ 3.33, ν ≈ 16.3, t* ≈ 2.12 ⇒ 4 ± 2.12·3.33 = (−2.1, 10.1).

# Interpretation
Interval includes 0 ⇒ cannot conclude a difference at α = 0.05.
