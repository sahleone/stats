"""
Chi-Square Test of Independence — Bonus Python Script
=====================================================
This script demonstrates the chi-square test of independence using the same
examples from the Excel lecture notes. It walks through each step so you can
see how to perform the test in Python with contingency tables.

Required packages: numpy, scipy, pandas, matplotlib
"""

import numpy as np
from scipy import stats
import pandas as pd
import matplotlib.pyplot as plt

# ============================================================
# WORKED EXAMPLE: Gender and Study Preference
# ============================================================
print("=" * 65)
print("WORKED EXAMPLE: Gender and Study Preference")
print("=" * 65)

# Step 1: State the hypotheses
print("\nStep 1: State the Hypotheses")
print("  H₀: Gender and study preference are independent.")
print("  H₁: Gender and study preference are NOT independent.")
print("  α = 0.05")

# Step 2: Set up the observed contingency table
print("\nStep 2: Observed Frequencies")
observed = np.array([
    [40, 30, 20],   # Male:   Alone, Group, Online
    [30, 50, 30],   # Female: Alone, Group, Online
])
rows = ["Male", "Female"]
cols = ["Alone", "Group", "Online"]

# Display as a pandas DataFrame for clarity
df_obs = pd.DataFrame(observed, index=rows, columns=cols)
df_obs["Row Total"] = df_obs.sum(axis=1)
print(df_obs.to_string())
print(f"  Col Totals: {observed.sum(axis=0)}")
print(f"  Grand Total: {observed.sum()}")

# Step 3: Compute expected frequencies
print("\nStep 3: Expected Frequencies")
print("  Formula: E_ij = (Row i Total × Col j Total) / Grand Total")
n = observed.sum()
row_totals = observed.sum(axis=1)
col_totals = observed.sum(axis=0)

expected = np.outer(row_totals, col_totals) / n
df_exp = pd.DataFrame(expected, index=rows, columns=cols)
print(df_exp.round(4).to_string())

# Step 4: Compute (O - E)^2 / E for each cell
print("\nStep 4: (O − E)² / E for Each Cell")
contributions = (observed - expected)**2 / expected
df_contrib = pd.DataFrame(contributions, index=rows, columns=cols)
print(df_contrib.round(4).to_string())

# Step 5: Test statistic
chi2_stat = contributions.sum()
print(f"\nStep 5: Test Statistic")
print(f"  χ² = Σ Σ (O - E)² / E = {chi2_stat:.4f}")

# Step 6: Degrees of freedom
r, c = observed.shape
df = (r - 1) * (c - 1)
print(f"\nStep 6: Degrees of Freedom")
print(f"  df = (r-1)(c-1) = ({r}-1)({c}-1) = {df}")

# Step 7: Critical value
alpha = 0.05
chi2_critical = stats.chi2.ppf(1 - alpha, df)
p_value = 1 - stats.chi2.cdf(chi2_stat, df)
print(f"\nStep 7: Critical Value")
print(f"  At α = {alpha} with df = {df}: χ²_critical = {chi2_critical:.3f}")
print(f"  p-value = {p_value:.4f}")

# Step 8: Decision
print(f"\nStep 8: Decision")
print(f"  χ²_calc = {chi2_stat:.4f}  vs  χ²_critical = {chi2_critical:.3f}")
if chi2_stat > chi2_critical:
    print("  Since χ²_calc > χ²_critical, we REJECT H₀.")
else:
    print("  Since χ²_calc < χ²_critical, we FAIL TO REJECT H₀.")

# Step 9: Conclusion
print(f"\nStep 9: Conclusion")
print("  At the 0.05 significance level, there is sufficient evidence to")
print("  conclude that gender and study preference are associated.")

# Quick verification using scipy's built-in function
print("\n--- Verification with scipy.stats.chi2_contingency() ---")
stat, pval, dof, exp_table = stats.chi2_contingency(observed)
print(f"  χ² = {stat:.4f},  p-value = {pval:.4f},  df = {dof}")

# ============================================================
# PRACTICE QUESTION 1: Smoking Status and Exercise Level
# ============================================================
print("\n\n" + "=" * 65)
print("PRACTICE QUESTION 1: Smoking Status and Exercise Level")
print("=" * 65)

observed_q1 = np.array([
    [30, 60, 70],   # Non-Smoker: Low, Moderate, High
    [50, 55, 35],   # Smoker:     Low, Moderate, High
])
rows_q1 = ["Non-Smoker", "Smoker"]
cols_q1 = ["Low", "Moderate", "High"]

print("\nObserved Frequencies:")
df_q1 = pd.DataFrame(observed_q1, index=rows_q1, columns=cols_q1)
df_q1["Row Total"] = df_q1.sum(axis=1)
print(df_q1.to_string())

stat_q1, pval_q1, dof_q1, exp_q1 = stats.chi2_contingency(observed_q1)

print(f"\nExpected Frequencies:")
df_exp_q1 = pd.DataFrame(exp_q1, index=rows_q1, columns=cols_q1)
print(df_exp_q1.round(2).to_string())

contrib_q1 = (observed_q1 - exp_q1)**2 / exp_q1
print(f"\n(O − E)² / E:")
print(pd.DataFrame(contrib_q1, index=rows_q1, columns=cols_q1).round(4).to_string())

crit_q1 = stats.chi2.ppf(0.95, dof_q1)
print(f"\n  χ² = {stat_q1:.4f}")
print(f"  df = {dof_q1}")
print(f"  χ²_critical (α=0.05) = {crit_q1:.3f}")
print(f"  p-value = {pval_q1:.4f}")
print(f"\n  Decision: {'REJECT H₀' if stat_q1 > crit_q1 else 'FAIL TO REJECT H₀'}")

# ============================================================
# PRACTICE QUESTION 2: Education Level and Job Satisfaction
# ============================================================
print("\n\n" + "=" * 65)
print("PRACTICE QUESTION 2: Education Level and Job Satisfaction")
print("=" * 65)

observed_q2 = np.array([
    [40, 35, 25],    # High School
    [30, 55, 65],    # Bachelor's
    [10, 40, 100],   # Graduate
])
rows_q2 = ["High School", "Bachelor's", "Graduate"]
cols_q2 = ["Low", "Medium", "High"]

print("\nObserved Frequencies:")
df_q2 = pd.DataFrame(observed_q2, index=rows_q2, columns=cols_q2)
df_q2["Row Total"] = df_q2.sum(axis=1)
print(df_q2.to_string())

stat_q2, pval_q2, dof_q2, exp_q2 = stats.chi2_contingency(observed_q2)

print(f"\nExpected Frequencies:")
df_exp_q2 = pd.DataFrame(exp_q2, index=rows_q2, columns=cols_q2)
print(df_exp_q2.round(2).to_string())

contrib_q2 = (observed_q2 - exp_q2)**2 / exp_q2
print(f"\n(O − E)² / E:")
print(pd.DataFrame(contrib_q2, index=rows_q2, columns=cols_q2).round(4).to_string())

crit_q2 = stats.chi2.ppf(0.99, dof_q2)
print(f"\n  χ² = {stat_q2:.4f}")
print(f"  df = {dof_q2}")
print(f"  χ²_critical (α=0.01) = {crit_q2:.3f}")
print(f"  p-value = {pval_q2:.6f}")
print(f"\n  Decision: {'REJECT H₀' if stat_q2 > crit_q2 else 'FAIL TO REJECT H₀'}")

# ============================================================
# VISUALIZATION: Stacked Bar Chart for Worked Example
# ============================================================
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Left plot: Observed vs Expected (Worked Example)
x = np.arange(len(cols))
width = 0.35
obs_male = observed[0]
obs_female = observed[1]
exp_male = expected[0]
exp_female = expected[1]

axes[0].bar(x - width/2, obs_male, width, label='Male (Observed)', color='steelblue')
axes[0].bar(x + width/2, obs_female, width, label='Female (Observed)', color='coral')
axes[0].bar(x - width/2, exp_male, width, label='Male (Expected)', color='steelblue',
            alpha=0.3, edgecolor='steelblue', linewidth=2)
axes[0].bar(x + width/2, exp_female, width, label='Female (Expected)', color='coral',
            alpha=0.3, edgecolor='coral', linewidth=2)
axes[0].set_xticks(x)
axes[0].set_xticklabels(cols)
axes[0].set_ylabel('Frequency')
axes[0].set_title('Gender vs Study Preference\n(Observed vs Expected)')
axes[0].legend(fontsize=8)

# Right plot: Chi-square distribution with test result
x_dist = np.linspace(0, 20, 500)
y_dist = stats.chi2.pdf(x_dist, df=df)
axes[1].plot(x_dist, y_dist, 'b-', linewidth=2, label=f'χ² distribution (df={df})')
x_reject = np.linspace(chi2_critical, 20, 300)
y_reject = stats.chi2.pdf(x_reject, df=df)
axes[1].fill_between(x_reject, y_reject, alpha=0.3, color='red', label='Rejection region')
axes[1].axvline(chi2_stat, color='green', linestyle='--', linewidth=2,
                label=f'χ²_calc = {chi2_stat:.2f}')
axes[1].axvline(chi2_critical, color='red', linestyle='-', linewidth=1.5,
                label=f'χ²_critical = {chi2_critical:.2f}')
axes[1].set_xlabel('χ² value')
axes[1].set_ylabel('Probability Density')
axes[1].set_title('Chi-Square Test of Independence')
axes[1].legend(fontsize=8)
axes[1].set_ylim(bottom=0)

plt.tight_layout()
plt.savefig('/home/claude/chi_square_independence_plot.png', dpi=150)
plt.close()
print("\n\nPlot saved: chi_square_independence_plot.png")
