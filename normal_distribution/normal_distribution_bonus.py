"""
The Normal Distribution — Bonus Python Script
==============================================
Demonstrates the normal distribution, z-scores, probability
calculations, and percentiles. Reproduces the worked example
(IQ scores) and both practice questions from the Excel notes.

Required packages: numpy, scipy, matplotlib
"""

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# ============================================================
# WORKED EXAMPLE: IQ Scores — X ~ N(100, 15²)
# ============================================================
print("=" * 60)
print("WORKED EXAMPLE: IQ Scores — X ~ N(100, 15²)")
print("=" * 60)

mu, sigma = 100, 15

# Part (a): P(X < 120)
z_a = (120 - mu) / sigma
p_a = stats.norm.cdf(z_a)
print(f"\n(a) P(X < 120)")
print(f"    Z = (120 − 100) / 15 = {z_a:.4f}")
print(f"    P(Z ≤ {z_a:.2f}) = {p_a:.4f}")
print(f"    About {p_a*100:.2f}% of people have IQ < 120.")

# Part (b): P(85 < X < 130)
z_b1 = (85 - mu) / sigma
z_b2 = (130 - mu) / sigma
p_b = stats.norm.cdf(z_b2) - stats.norm.cdf(z_b1)
print(f"\n(b) P(85 < X < 130)")
print(f"    Z₁ = (85 − 100) / 15 = {z_b1:.4f}")
print(f"    Z₂ = (130 − 100) / 15 = {z_b2:.4f}")
print(f"    P(Z ≤ {z_b2:.2f}) = {stats.norm.cdf(z_b2):.4f}")
print(f"    P(Z ≤ {z_b1:.2f}) = {stats.norm.cdf(z_b1):.4f}")
print(f"    P(85 < X < 130) = {p_b:.4f}")
print(f"    About {p_b*100:.2f}% of people have IQ between 85 and 130.")

# Part (c): 90th percentile
z_90 = stats.norm.ppf(0.90)
x_90 = mu + z_90 * sigma
print(f"\n(c) 90th Percentile")
print(f"    z for P(Z ≤ z) = 0.90: z = {z_90:.4f}")
print(f"    X = μ + z·σ = 100 + {z_90:.4f} × 15 = {x_90:.2f}")
print(f"    A person at the 90th percentile has IQ ≈ {x_90:.1f}.")

# Verify with scipy
print(f"\n--- Verification using scipy.stats.norm ---")
print(f"    P(X < 120)       = {stats.norm.cdf(120, mu, sigma):.4f}")
print(f"    P(85 < X < 130)  = {stats.norm.cdf(130, mu, sigma) - stats.norm.cdf(85, mu, sigma):.4f}")
print(f"    90th percentile   = {stats.norm.ppf(0.90, mu, sigma):.2f}")

# ============================================================
# QUESTION 1: Exam Scores — X ~ N(74, 9²)
# ============================================================
print("\n\n" + "=" * 60)
print("QUESTION 1: Exam Scores — X ~ N(74, 9²)")
print("=" * 60)

mu1, sigma1 = 74, 9

# (a) P(X > 90)
z1a = (90 - mu1) / sigma1
p1a = 1 - stats.norm.cdf(z1a)
print(f"\n(a) P(X > 90)")
print(f"    Z = (90 − 74)/9 = {z1a:.4f}")
print(f"    P(Z > {z1a:.2f}) = 1 − {stats.norm.cdf(z1a):.4f} = {p1a:.4f}")
print(f"    About {p1a*100:.2f}% scored above 90.")

# (b) P(65 < X < 85)
z1b_lo = (65 - mu1) / sigma1
z1b_hi = (85 - mu1) / sigma1
p1b = stats.norm.cdf(z1b_hi) - stats.norm.cdf(z1b_lo)
print(f"\n(b) P(65 < X < 85)")
print(f"    Z₁ = {z1b_lo:.4f},  Z₂ = {z1b_hi:.4f}")
print(f"    P = {stats.norm.cdf(z1b_hi):.4f} − {stats.norm.cdf(z1b_lo):.4f} = {p1b:.4f}")
print(f"    About {p1b*100:.2f}% scored between 65 and 85.")

# (c) 95th percentile
x1c = stats.norm.ppf(0.95, mu1, sigma1)
print(f"\n(c) 95th percentile")
print(f"    z = {stats.norm.ppf(0.95):.4f}")
print(f"    X = 74 + {stats.norm.ppf(0.95):.4f} × 9 = {x1c:.2f}")

# (d) Number below 60
z1d = (60 - mu1) / sigma1
p1d = stats.norm.cdf(z1d)
n_below = 200 * p1d
print(f"\n(d) P(X < 60)")
print(f"    Z = {z1d:.4f},  P = {p1d:.4f}")
print(f"    Expected: 200 × {p1d:.4f} ≈ {n_below:.1f} students")

# ============================================================
# QUESTION 2: Manufacturing — X ~ N(5.00, 0.03²)
# ============================================================
print("\n\n" + "=" * 60)
print("QUESTION 2: Manufacturing — X ~ N(5.00, 0.03²)")
print("=" * 60)

mu2, sigma2 = 5.00, 0.03

# (a) P(4.95 < X < 5.05)
p2a = stats.norm.cdf(5.05, mu2, sigma2) - stats.norm.cdf(4.95, mu2, sigma2)
print(f"\n(a) P(4.95 < X < 5.05)")
print(f"    Z₁ = {(4.95-mu2)/sigma2:.4f},  Z₂ = {(5.05-mu2)/sigma2:.4f}")
print(f"    P = {p2a:.4f}  ({p2a*100:.2f}%)")

# (b) Rejection rate
p_low = stats.norm.cdf(4.94, mu2, sigma2)
p_high = 1 - stats.norm.cdf(5.06, mu2, sigma2)
p2b = p_low + p_high
print(f"\n(b) Rejection rate")
print(f"    P(X < 4.94) = {p_low:.4f}")
print(f"    P(X > 5.06) = {p_high:.4f}")
print(f"    Total rejection = {p2b:.4f}  ({p2b*100:.2f}%)")

# (c) Max σ for ≤ 1% rejection
sigma_max = 0.06 / 2.576
print(f"\n(c) Max σ for ≤ 1% rejection")
print(f"    Distance from mean to limit = 0.06")
print(f"    z for 0.5% tail = 2.576")
print(f"    σ_max = 0.06 / 2.576 = {sigma_max:.4f} cm")

# (d) Empirical rule
lower_95 = mu2 - 2 * sigma2
upper_95 = mu2 + 2 * sigma2
print(f"\n(d) 95% interval (Empirical Rule)")
print(f"    μ ± 2σ = {mu2} ± {2*sigma2}")
print(f"    [{lower_95:.2f}, {upper_95:.2f}]")

# ============================================================
# VISUALIZATION
# ============================================================
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Plot 1: IQ distribution with P(X < 120) shaded
x_plot = np.linspace(mu - 4*sigma, mu + 4*sigma, 500)
y_plot = stats.norm.pdf(x_plot, mu, sigma)
axes[0, 0].plot(x_plot, y_plot, 'b-', linewidth=2)
x_fill = np.linspace(mu - 4*sigma, 120, 300)
axes[0, 0].fill_between(x_fill, stats.norm.pdf(x_fill, mu, sigma),
                         alpha=0.3, color='steelblue', label=f'P(X < 120) = {p_a:.4f}')
axes[0, 0].axvline(120, color='red', linestyle='--', label='X = 120')
axes[0, 0].axvline(mu, color='gray', linestyle=':', label=f'μ = {mu}')
axes[0, 0].set_title('IQ Scores: P(X < 120)', fontsize=12)
axes[0, 0].set_xlabel('IQ Score')
axes[0, 0].set_ylabel('Density')
axes[0, 0].legend(fontsize=8)

# Plot 2: Empirical Rule illustration
x_emp = np.linspace(mu - 4*sigma, mu + 4*sigma, 500)
y_emp = stats.norm.pdf(x_emp, mu, sigma)
axes[0, 1].plot(x_emp, y_emp, 'b-', linewidth=2)
colors = ['#4CAF50', '#FFC107', '#FF5722']
labels = ['68% (μ±1σ)', '95% (μ±2σ)', '99.7% (μ±3σ)']
for i, (k, c, l) in enumerate(zip([1, 2, 3], colors, labels)):
    lo, hi = mu - k*sigma, mu + k*sigma
    xf = np.linspace(lo, hi, 300)
    axes[0, 1].fill_between(xf, stats.norm.pdf(xf, mu, sigma),
                             alpha=0.2, color=c, label=l)
axes[0, 1].set_title('Empirical Rule (68-95-99.7)', fontsize=12)
axes[0, 1].set_xlabel('IQ Score')
axes[0, 1].legend(fontsize=8)

# Plot 3: Exam scores — between 65 and 85
x3 = np.linspace(mu1 - 4*sigma1, mu1 + 4*sigma1, 500)
y3 = stats.norm.pdf(x3, mu1, sigma1)
axes[1, 0].plot(x3, y3, 'b-', linewidth=2)
xf3 = np.linspace(65, 85, 300)
axes[1, 0].fill_between(xf3, stats.norm.pdf(xf3, mu1, sigma1),
                         alpha=0.3, color='coral', label=f'P(65<X<85) = {p1b:.4f}')
axes[1, 0].axvline(mu1, color='gray', linestyle=':')
axes[1, 0].set_title('Exam Scores: P(65 < X < 85)', fontsize=12)
axes[1, 0].set_xlabel('Exam Score')
axes[1, 0].set_ylabel('Density')
axes[1, 0].legend(fontsize=8)

# Plot 4: Manufacturing — rejection regions
x4 = np.linspace(mu2 - 4*sigma2, mu2 + 4*sigma2, 500)
y4 = stats.norm.pdf(x4, mu2, sigma2)
axes[1, 1].plot(x4, y4, 'b-', linewidth=2)
# Accepted region
xf_acc = np.linspace(4.94, 5.06, 300)
axes[1, 1].fill_between(xf_acc, stats.norm.pdf(xf_acc, mu2, sigma2),
                         alpha=0.3, color='green', label='Accepted')
# Rejection regions
xf_lo = np.linspace(mu2 - 4*sigma2, 4.94, 200)
xf_hi = np.linspace(5.06, mu2 + 4*sigma2, 200)
axes[1, 1].fill_between(xf_lo, stats.norm.pdf(xf_lo, mu2, sigma2),
                         alpha=0.4, color='red', label='Rejected')
axes[1, 1].fill_between(xf_hi, stats.norm.pdf(xf_hi, mu2, sigma2),
                         alpha=0.4, color='red')
axes[1, 1].set_title(f'Bolt Lengths: {p2b*100:.2f}% Rejected', fontsize=12)
axes[1, 1].set_xlabel('Length (cm)')
axes[1, 1].set_ylabel('Density')
axes[1, 1].legend(fontsize=8)

plt.tight_layout()
plt.savefig('/home/claude/normal_distribution_plot.png', dpi=150)
plt.close()
print("\n\nPlot saved: normal_distribution_plot.png")
