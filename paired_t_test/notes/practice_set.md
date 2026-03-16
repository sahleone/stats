---
title: "Paired T-Test — Practice"
author: MA235 Team
---

# Problems
1. **Blood Pressure Medication.** Before-after systolic readings for 10 patients yield d̄ = −7.5 mmHg, s_d = 5.2. Test α = 0.05 right-tailed.
2. **Study Habit Intervention.** Six students take diagnostic test twice; d̄ = 3.0, s_d = 2.5. Test α = 0.10 two-tailed.
3. **Machine Calibration.** Eight machines measured before vs after calibration: d̄ = 1.5 minutes (before − after), s_d = 1.8. Test α = 0.01 left-tailed (did time decrease?).
4. **Paired Weights.** Twelve clients weigh in before vs after diet: d̄ = 4.8 lb, s_d = 6.2. Test α = 0.05 and compute 95% CI.

# Solutions
1. t = −7.5 / (5.2/√10) ≈ −4.55 (if d defined after − before; adjust sign). Assuming d = after − before, t = (−7.5)/(5.2/√10) = −4.55 ⇒ reject.
2. t = 3.0/(2.5/√6) ≈ 2.94, df=5 ⇒ p≈0.03 <0.10 ⇒ reject.
3. t = 1.5/(1.8/√8) ≈ 2.36; left-tailed critical at α=0.01 is −3.499, so t>0 ⇒ fail to reject (insufficient at 0.01).
4. t = 4.8/(6.2/√12) ≈ 2.68 ⇒ reject; 95% CI = 4.8 ± 2.201·6.2/√12 ⇒ (1.8, 7.8) lb.
