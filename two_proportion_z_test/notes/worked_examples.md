---
title: "Two-Proportion Z-Test — Worked Examples"
author: MA235 Team
---

# Example 1: Campaign Response
Sample 1: x₁=90, n₁=150 (p̂₁=0.60). Sample 2: x₂=70, n₂=160 (p̂₂=0.4375). Test α=0.05 two-tailed.

- Pooled p̂ = (90+70)/(150+160) = 0.518.
- z = (0.60 − 0.4375)/√(0.518·0.482·(1/150 + 1/160)) ≈ 2.78.
- Since |2.78| > 1.960, reject H₀; difference significant.
- 95% CI: (0.60 − 0.4375) ± 1.960·√(0.60·0.40/150 + 0.4375·0.5625/160) ⇒ (0.05, 0.25).

# Example 2: Treatment Success (Right-Tailed)
x₁=45, n₁=60 (p̂₁=0.75). x₂=38, n₂=65 (p̂₂=0.585). Test H₁: p₁ > p₂ at α=0.01.

- Pooled p̂ = (45+38)/(60+65) ≈ 0.664.
- z = (0.75 − 0.585)/√(0.664·0.336·(1/60 + 1/65)) ≈ 2.33.
- Critical z = 2.326 ⇒ barely reject H₀ (p≈0.010).
- Conclusion: Treatment has higher success at the 1% level (just significant).
