"""
One-Way ANOVA — Bonus Python Script
====================================
Demonstrates one-way analysis of variance with the worked example
(teaching methods) and both practice questions from the Excel notes.

Required packages: numpy, scipy, matplotlib, pandas
"""
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def one_way_anova_manual(groups, alpha=0.05):
    """Perform one-way ANOVA step by step and print results."""
    k = len(groups)
    ns = [len(g) for g in groups]
    N = sum(ns)
    means = [np.mean(g) for g in groups]
    grand_mean = np.mean(np.concatenate(groups))

    ss_between = sum(n * (m - grand_mean)**2 for n, m in zip(ns, means))
    ss_within = sum(np.sum((g - np.mean(g))**2) for g in groups)
    ss_total = ss_between + ss_within

    df_between = k - 1
    df_within = N - k
    ms_between = ss_between / df_between
    ms_within = ss_within / df_within
    F_stat = ms_between / ms_within
    p_value = 1 - stats.f.cdf(F_stat, df_between, df_within)
    F_crit = stats.f.ppf(1 - alpha, df_between, df_within)
    eta_sq = ss_between / ss_total

    print(f"  Grand Mean = {grand_mean:.2f}")
    print(f"  Group Means: {[f'{m:.2f}' for m in means]}")
    print(f"  Group Sizes: {ns}, N={N}, k={k}")
    print(f"\n  ANOVA Table:")
    print(f"  {'Source':<12} {'SS':>10} {'df':>5} {'MS':>10} {'F':>10}")
    print(f"  {'-'*50}")
    print(f"  {'Between':<12} {ss_between:>10.2f} {df_between:>5} {ms_between:>10.2f} {F_stat:>10.4f}")
    print(f"  {'Within':<12} {ss_within:>10.2f} {df_within:>5} {ms_within:>10.2f}")
    print(f"  {'Total':<12} {ss_total:>10.2f} {N-1:>5}")
    print(f"\n  F_calc = {F_stat:.4f}")
    print(f"  F_critical (α={alpha}) = {F_crit:.4f}")
    print(f"  p-value = {p_value:.6f}")
    print(f"  η² = {eta_sq:.4f} ({'small' if eta_sq<0.06 else 'medium' if eta_sq<0.14 else 'large'} effect)")
    print(f"\n  Decision: {'REJECT H₀' if F_stat > F_crit else 'FAIL TO REJECT H₀'}")
    return F_stat, p_value, eta_sq, groups

# ============================================================
print("=" * 60)
print("WORKED EXAMPLE: Teaching Methods")
print("=" * 60)
A = np.array([78, 85, 82, 80, 75])
B = np.array([90, 88, 92, 85, 95])
C_grp = np.array([70, 72, 68, 74, 66])
one_way_anova_manual([A, B, C_grp])
print("\n--- scipy verification ---")
F, p = stats.f_oneway(A, B, C_grp)
print(f"  F={F:.4f}, p={p:.6f}")

# ============================================================
print("\n\n" + "=" * 60)
print("QUESTION 1: Fertilizer Types")
print("=" * 60)
fA = np.array([45,48,42,50,44])
fB = np.array([55,60,58,52,55])
fC = np.array([50,47,49,51,53])
fD = np.array([62,65,60,58,65])
one_way_anova_manual([fA, fB, fC, fD])
print("\n--- scipy verification ---")
F, p = stats.f_oneway(fA, fB, fC, fD)
print(f"  F={F:.4f}, p={p:.6f}")

# ============================================================
print("\n\n" + "=" * 60)
print("QUESTION 2: Study Environments")
print("=" * 60)
lib = np.array([88,92,85,90,87,91])
cof = np.array([78,82,76,80,74,84])
home = np.array([80,85,82,79,83,81])
one_way_anova_manual([lib, cof, home], alpha=0.01)
print("\n--- scipy verification ---")
F, p = stats.f_oneway(lib, cof, home)
print(f"  F={F:.4f}, p={p:.6f}")

# ============================================================
# VISUALIZATION
# ============================================================
fig, axes = plt.subplots(1, 3, figsize=(16, 5))

# Plot 1: Worked Example boxplots
axes[0].boxplot([A, B, C_grp], labels=['Method A','Method B','Method C'])
for i, grp in enumerate([A, B, C_grp], 1):
    axes[0].scatter([i]*len(grp), grp, alpha=0.6, zorder=5)
axes[0].set_title('Teaching Methods', fontsize=12)
axes[0].set_ylabel('Exam Score')
axes[0].axhline(np.mean(np.concatenate([A,B,C_grp])), color='red', ls='--', alpha=0.5, label='Grand Mean')
axes[0].legend(fontsize=8)

# Plot 2: Fertilizer boxplots
axes[1].boxplot([fA,fB,fC,fD], labels=['A','B','C','D'])
for i, grp in enumerate([fA,fB,fC,fD], 1):
    axes[1].scatter([i]*len(grp), grp, alpha=0.6, zorder=5)
axes[1].set_title('Fertilizer Types', fontsize=12)
axes[1].set_ylabel('Yield (kg)')

# Plot 3: F-distribution
x = np.linspace(0, 15, 500)
y = stats.f.pdf(x, 2, 12)
axes[2].plot(x, y, 'b-', lw=2, label='F(2, 12)')
F_crit = stats.f.ppf(0.95, 2, 12)
xr = np.linspace(F_crit, 15, 300)
axes[2].fill_between(xr, stats.f.pdf(xr, 2, 12), alpha=0.3, color='red', label='Rejection region')
F_worked = 39.78  # approximate
axes[2].axvline(F_crit, color='red', ls='-', lw=1.5, label=f'F_crit={F_crit:.2f}')
axes[2].set_title('F Distribution (Worked Example)', fontsize=12)
axes[2].set_xlabel('F value'); axes[2].set_ylabel('Density')
axes[2].legend(fontsize=8); axes[2].set_ylim(bottom=0)

plt.tight_layout()
plt.savefig('/home/claude/one_way_anova_plot.png', dpi=150)
plt.close()
print("\n\nPlot saved: one_way_anova_plot.png")
