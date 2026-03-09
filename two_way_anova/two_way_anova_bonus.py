"""
Two-Way ANOVA — Bonus Python Script
====================================
Demonstrates two-way ANOVA with interaction. Covers the worked example
(exercise × diet on weight loss) and both practice questions.

Required packages: numpy, scipy, pandas, matplotlib
"""
import numpy as np
from scipy import stats
import pandas as pd
import matplotlib.pyplot as plt

def two_way_anova(data_dict, factor_a_name="A", factor_b_name="B", alpha=0.05):
    """
    data_dict: {(a_level, b_level): [values], ...}
    Performs balanced two-way ANOVA manually.
    """
    a_levels = sorted(set(k[0] for k in data_dict))
    b_levels = sorted(set(k[1] for k in data_dict))
    a, b = len(a_levels), len(b_levels)
    n = len(list(data_dict.values())[0])
    N = a * b * n

    all_vals = np.concatenate(list(data_dict.values()))
    grand_mean = np.mean(all_vals)

    # Cell means
    cell_means = {k: np.mean(v) for k, v in data_dict.items()}
    # Marginal means
    a_means = {ai: np.mean([cell_means[(ai, bj)] for bj in b_levels]) for ai in a_levels}
    b_means = {bj: np.mean([cell_means[(ai, bj)] for ai in a_levels]) for bj in b_levels}

    # Sums of squares
    ss_a = b * n * sum((a_means[ai] - grand_mean)**2 for ai in a_levels)
    ss_b = a * n * sum((b_means[bj] - grand_mean)**2 for bj in b_levels)
    ss_ab = n * sum((cell_means[(ai,bj)] - a_means[ai] - b_means[bj] + grand_mean)**2
                     for ai in a_levels for bj in b_levels)
    ss_e = sum(np.sum((np.array(data_dict[(ai,bj)]) - cell_means[(ai,bj)])**2)
               for ai in a_levels for bj in b_levels)
    ss_t = ss_a + ss_b + ss_ab + ss_e

    df_a, df_b, df_ab, df_e = a-1, b-1, (a-1)*(b-1), N - a*b
    ms_a, ms_b, ms_ab, ms_e = ss_a/df_a, ss_b/df_b, ss_ab/df_ab, ss_e/df_e
    f_a, f_b, f_ab = ms_a/ms_e, ms_b/ms_e, ms_ab/ms_e
    p_a = 1-stats.f.cdf(f_a, df_a, df_e)
    p_b = 1-stats.f.cdf(f_b, df_b, df_e)
    p_ab = 1-stats.f.cdf(f_ab, df_ab, df_e)

    print(f"\n  Grand Mean = {grand_mean:.4f}")
    print(f"  Design: {a}×{b}, n={n}, N={N}")
    print(f"\n  Cell Means:")
    for ai in a_levels:
        for bj in b_levels:
            print(f"    {factor_a_name}={ai}, {factor_b_name}={bj}: {cell_means[(ai,bj)]:.2f}")
    print(f"\n  Marginal Means ({factor_a_name}): {dict((k,f'{v:.2f}') for k,v in a_means.items())}")
    print(f"  Marginal Means ({factor_b_name}): {dict((k,f'{v:.2f}') for k,v in b_means.items())}")

    print(f"\n  ANOVA Table:")
    print(f"  {'Source':<16} {'SS':>10} {'df':>4} {'MS':>10} {'F':>10} {'p-value':>10}")
    print(f"  {'-'*62}")
    print(f"  {factor_a_name:<16} {ss_a:>10.4f} {df_a:>4} {ms_a:>10.4f} {f_a:>10.4f} {p_a:>10.6f}")
    print(f"  {factor_b_name:<16} {ss_b:>10.4f} {df_b:>4} {ms_b:>10.4f} {f_b:>10.4f} {p_b:>10.6f}")
    print(f"  {factor_a_name}×{factor_b_name:<13} {ss_ab:>10.4f} {df_ab:>4} {ms_ab:>10.4f} {f_ab:>10.4f} {p_ab:>10.6f}")
    print(f"  {'Error':<16} {ss_e:>10.4f} {df_e:>4} {ms_e:>10.4f}")
    print(f"  {'Total':<16} {ss_t:>10.4f} {N-1:>4}")

    f_crit = stats.f.ppf(1-alpha, 1, df_e) if df_a==1 and df_b==1 else None
    if f_crit:
        print(f"\n  F_critical({alpha}, 1, {df_e}) = {f_crit:.4f}")

    eta_a = ss_a/ss_t; eta_b = ss_b/ss_t; eta_ab = ss_ab/ss_t
    print(f"\n  η²_A = {eta_a:.4f}, η²_B = {eta_b:.4f}, η²_AB = {eta_ab:.4f}")

    for name, f_val, p_val in [(factor_a_name,f_a,p_a),(factor_b_name,f_b,p_b),
                                (f"{factor_a_name}×{factor_b_name}",f_ab,p_ab)]:
        print(f"  {name}: {'REJECT H₀' if p_val < alpha else 'Fail to reject H₀'} (p={p_val:.6f})")

    return cell_means, a_levels, b_levels

# ============================================================
print("="*60)
print("WORKED EXAMPLE: Exercise × Diet on Weight Loss")
print("="*60)
data_we = {
    ("Cardio","Low-Carb"): [5.2,6.1,5.8,6.5],
    ("Cardio","Standard"): [3.5,4.0,3.8,4.2],
    ("Weights","Low-Carb"): [4.0,4.5,4.2,4.8],
    ("Weights","Standard"): [2.5,3.0,2.8,3.2],
}
cm_we, al_we, bl_we = two_way_anova(data_we, "Exercise", "Diet")

# ============================================================
print("\n\n"+"="*60)
print("QUESTION 1: Temperature × Material on Battery Life")
print("="*60)
data_q1 = {
    ("Cold","TypeX"): [48,50,46],
    ("Cold","TypeY"): [52,55,53],
    ("Hot","TypeX"): [35,38,36],
    ("Hot","TypeY"): [42,40,44],
}
cm_q1, al_q1, bl_q1 = two_way_anova(data_q1, "Temp", "Material")

# ============================================================
print("\n\n"+"="*60)
print("QUESTION 2: Caffeine × Sleep on Reaction Time")
print("="*60)
data_q2 = {
    ("Caffeine","8hr"): [220,215,225,210],
    ("Caffeine","4hr"): [260,270,255,265],
    ("Placebo","8hr"): [250,245,255,240],
    ("Placebo","4hr"): [310,300,320,305],
}
cm_q2, al_q2, bl_q2 = two_way_anova(data_q2, "Caffeine", "Sleep", alpha=0.01)

# ============================================================
# VISUALIZATION: Interaction Plots
# ============================================================
fig, axes = plt.subplots(1, 3, figsize=(16, 5))

def interaction_plot(ax, cell_means, a_levels, b_levels, a_name, b_name, title):
    for ai in a_levels:
        vals = [cell_means[(ai, bj)] for bj in b_levels]
        ax.plot(b_levels, vals, 'o-', linewidth=2, markersize=8, label=f'{a_name}={ai}')
    ax.set_xlabel(b_name); ax.set_ylabel('Mean Response')
    ax.set_title(title, fontsize=11); ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

interaction_plot(axes[0], cm_we, al_we, bl_we, "Exercise", "Diet", "Exercise × Diet")
interaction_plot(axes[1], cm_q1, al_q1, bl_q1, "Temp", "Material", "Temp × Material")
interaction_plot(axes[2], cm_q2, al_q2, bl_q2, "Caffeine", "Sleep", "Caffeine × Sleep")

plt.tight_layout()
plt.savefig('/home/claude/two_way_anova_plot.png', dpi=150)
plt.close()
print("\n\nPlot saved: two_way_anova_plot.png")
