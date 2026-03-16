---
title: "One-Sample T-Test — Practice"
author: MA235 Team
---

# Problems
1. **Sodium Content.** Target mean 480 mg. Sample of 9 cans: x̄ = 493 mg, s = 18 mg. Test at α = 0.05 if mean increased.
2. **Website Load Time.** Old mean 2.8 s. Sample of 16 loads: x̄ = 2.5 s, s = 0.6 s. Test at α = 0.01 two-tailed.
3. **Blood Pressure Drug.** Baseline systolic mean 130 mmHg. Ten patients after treatment: x̄ = 126, s = 7. Test if mean decreased at α = 0.05.
4. **Lamp Lifetimes.** Claimed mean 1200 hours. Sample 20 bulbs: x̄ = 1185, s = 90. Test α = 0.10; compute 90% CI.

# Solutions
1. t = (493 − 480)/(18/√9) = 2.17, df=8 ⇒ p ≈ 0.032 < 0.05 ⇒ reject (mean higher).
2. t = (2.5 − 2.8)/(0.6/4) = −2.0, df=15 ⇒ p ≈ 0.064 > 0.01 ⇒ fail to reject (no evidence of change at 1%).
3. t = (126 − 130)/(7/√10) = −1.81, df=9 ⇒ p ≈ 0.051 ≈ α; borderline, fail to reject at 0.05.
4. t = (1185 − 1200)/(90/√20) = −0.75 ⇒ fail to reject; 90% CI = 1185 ± 1.729·90/√20 ≈ (1149, 1221).
