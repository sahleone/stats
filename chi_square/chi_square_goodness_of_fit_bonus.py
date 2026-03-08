"""
Chi-Square Goodness-of-Fit Test — Bonus Python Script
=====================================================
This script demonstrates the chi-square goodness-of-fit test using the same
examples from the Excel lecture notes. It walks through each step so you can
see how to perform the test in Python.

Required packages: numpy, scipy, matplotlib
"""

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# ============================================================
# WORKED EXAMPLE: Is a Die Fair?
# ============================================================
print("=" * 65)
print("WORKED EXAMPLE: Is a Die Fair?")
print("=" * 65)

# Step 1: State the hypotheses
print("\nStep 1: State the Hypotheses")
print("  H₀: The die is fair (each face has probability 1/6).")
print("  H₁: The die is NOT fair.")

# Step 2: Set up the data
print("\nStep 2: Set Up the Data")
observed = np.array([25, 17, 15, 23, 24, 16])  # counts for faces 1-6
n = observed.sum()  # total rolls
print(f"  Total rolls: n = {n}")

# Under H₀, each face has probability 1/6
expected = np.array([n / 6] * 6)

print(f"\n  {'Face':<8} {'Observed':<12} {'Expected':<12} {'(O-E)²/E':<12}")
print(f"  {'-'*44}")
for i in range(6):
    contrib = (observed[i] - expected[i])**2 / expected[i]
    print(f"  {i+1:<8} {observed[i]:<12} {expected[i]:<12.2f} {contrib:<12.4f}")

# Step 3: Calculate the test statistic
chi2_components = (observed - expected)**2 / expected
chi2_stat = chi2_components.sum()
print(f"\nStep 3: Test Statistic")
print(f"  χ² = Σ (O - E)² / E = {chi2_stat:.4f}")

# Step 4: Degrees of freedom
k = len(observed)  # number of categories
df = k - 1
print(f"\nStep 4: Degrees of Freedom")
print(f"  df = k - 1 = {k} - 1 = {df}")

# Step 5: Critical value and p-value
alpha = 0.05
chi2_critical = stats.chi2.ppf(1 - alpha, df)
p_value = 1 - stats.chi2.cdf(chi2_stat, df)
print(f"\nStep 5: Critical Value")
print(f"  At α = {alpha} with df = {df}: χ²_critical = {chi2_critical:.3f}")
print(f"  p-value = {p_value:.4f}")

# Step 6: Decision
print(f"\nStep 6: Decision")
print(f"  χ²_calc = {chi2_stat:.4f}  vs  χ²_critical = {chi2_critical:.3f}")
if chi2_stat > chi2_critical:
    print("  Since χ²_calc > χ²_critical, we REJECT H₀.")
else:
    print("  Since χ²_calc < χ²_critical, we FAIL TO REJECT H₀.")

# Step 7: Conclusion
print(f"\nStep 7: Conclusion")
print("  At the 0.05 significance level, there is not sufficient evidence")
print("  to conclude that the die is unfair.")

# Quick verification using scipy's built-in function
print("\n--- Verification with scipy.stats.chisquare() ---")
stat, pval = stats.chisquare(f_obs=observed, f_exp=expected)
print(f"  χ² = {stat:.4f},  p-value = {pval:.4f}")

# ============================================================
# PRACTICE QUESTION 1: M&M Color Distribution
# ============================================================
print("\n\n" + "=" * 65)
print("PRACTICE QUESTION 1: M&M Color Distribution")
print("=" * 65)

observed_mm = np.array([50, 35, 44, 30, 25, 16])
colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Brown"]
proportions = np.array([0.20, 0.20, 0.20, 0.15, 0.15, 0.10])
n_mm = observed_mm.sum()
expected_mm = proportions * n_mm

print(f"\n  n = {n_mm}")
print(f"\n  {'Color':<10} {'Observed':<12} {'Expected':<12} {'(O-E)²/E':<12}")
print(f"  {'-'*46}")
for i in range(len(colors)):
    contrib = (observed_mm[i] - expected_mm[i])**2 / expected_mm[i]
    print(f"  {colors[i]:<10} {observed_mm[i]:<12} {expected_mm[i]:<12.1f} {contrib:<12.4f}")

chi2_mm = np.sum((observed_mm - expected_mm)**2 / expected_mm)
df_mm = len(colors) - 1
crit_mm = stats.chi2.ppf(1 - 0.05, df_mm)
p_mm = 1 - stats.chi2.cdf(chi2_mm, df_mm)

print(f"\n  χ² = {chi2_mm:.4f}")
print(f"  df = {df_mm}")
print(f"  χ²_critical (α=0.05) = {crit_mm:.3f}")
print(f"  p-value = {p_mm:.4f}")
print(f"\n  Decision: {'REJECT H₀' if chi2_mm > crit_mm else 'FAIL TO REJECT H₀'}")

# ============================================================
# PRACTICE QUESTION 2: Customer Arrival Patterns
# ============================================================
print("\n\n" + "=" * 65)
print("PRACTICE QUESTION 2: Customer Arrival Patterns")
print("=" * 65)

observed_cust = np.array([120, 90, 95, 85, 110])
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
n_cust = observed_cust.sum()
expected_cust = np.array([n_cust / 5] * 5)

print(f"\n  n = {n_cust}")
print(f"\n  {'Day':<14} {'Observed':<12} {'Expected':<12} {'(O-E)²/E':<12}")
print(f"  {'-'*50}")
for i in range(len(days)):
    contrib = (observed_cust[i] - expected_cust[i])**2 / expected_cust[i]
    print(f"  {days[i]:<14} {observed_cust[i]:<12} {expected_cust[i]:<12.1f} {contrib:<12.4f}")

chi2_cust = np.sum((observed_cust - expected_cust)**2 / expected_cust)
df_cust = len(days) - 1
alpha_cust = 0.10
crit_cust = stats.chi2.ppf(1 - alpha_cust, df_cust)
p_cust = 1 - stats.chi2.cdf(chi2_cust, df_cust)

print(f"\n  χ² = {chi2_cust:.4f}")
print(f"  df = {df_cust}")
print(f"  χ²_critical (α=0.10) = {crit_cust:.3f}")
print(f"  p-value = {p_cust:.4f}")
print(f"\n  Decision: {'REJECT H₀' if chi2_cust > crit_cust else 'FAIL TO REJECT H₀'}")

# ============================================================
# VISUALIZATION: Chi-Square Distribution
# ============================================================
# This plot shows the chi-square distribution with the rejection region
# shaded, for the worked example (df=5, α=0.05).

x = np.linspace(0, 25, 500)
y = stats.chi2.pdf(x, df=5)

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(x, y, 'b-', linewidth=2, label='χ² distribution (df=5)')

# Shade rejection region
x_reject = np.linspace(chi2_critical, 25, 300)
y_reject = stats.chi2.pdf(x_reject, df=5)
ax.fill_between(x_reject, y_reject, alpha=0.3, color='red', label=f'Rejection region (α=0.05)')

# Mark the test statistic
ax.axvline(chi2_stat, color='green', linestyle='--', linewidth=2,
           label=f'χ²_calc = {chi2_stat:.2f}')
ax.axvline(chi2_critical, color='red', linestyle='-', linewidth=1.5,
           label=f'χ²_critical = {chi2_critical:.2f}')

ax.set_xlabel('χ² value', fontsize=12)
ax.set_ylabel('Probability Density', fontsize=12)
ax.set_title('Chi-Square Goodness-of-Fit Test (Worked Example)', fontsize=13)
ax.legend(fontsize=10)
ax.set_ylim(bottom=0)
plt.tight_layout()
plt.savefig('/home/claude/chi_square_gof_plot.png', dpi=150)
plt.close()
print("\n\nPlot saved: chi_square_gof_plot.png")
