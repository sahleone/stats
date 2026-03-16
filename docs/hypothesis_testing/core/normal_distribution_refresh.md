---
title: "Normal Distribution Refresher"
author: MA235 Team
---

# Standardization
To convert any normal variable X ~ N(μ, σ) to the standard normal Z:
$$ Z = \frac{X - \mu}{\sigma} $$
Use this to look up probabilities in Table A-2 or compute with technology.

# Steps for Probability Questions
1. Sketch the bell curve and mark μ.
2. Plot the value(s) of interest and shade the region described.
3. Convert raw scores to z-scores using the formula above.
4. Use the z-table to find cumulative probabilities.
5. For "between" probabilities, subtract the two cumulative results.

# Common Scenarios
- **Below a value:** Use the z-table value directly (area to the left).
- **Above a value:** 1 − table value.
- **Between a and b:** Table(b) − Table(a).

# Example
If heights follow μ = 68 in, σ = 3 in, find P(X > 72).
- z = (72 − 68)/3 ≈ 1.33.
- Table gives 0.9082 below; so above is 1 − 0.9082 = 0.0918.

# Connection to Hypothesis Testing
- Week 12 notes rely on z-table usage before moving to t-tests.
- Understanding shading and symmetry helps interpret critical regions.

# Tips
- Areas are always positive; use symmetry (P(Z < −z) = P(Z > z)).
- Carry z to two decimals unless technology provides more precision.
- When σ is unknown and n is small, switch to the t-distribution (covered in topic-specific notes).
