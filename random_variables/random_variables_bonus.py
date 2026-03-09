"""
Random Variables — Bonus Python Script
=======================================
Demonstrates expected value, variance, and standard deviation
for discrete random variables. Reproduces the worked example
and both practice questions from the Excel lecture notes.

Required packages: numpy, matplotlib
"""

import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# WORKED EXAMPLE: Number of Pets per Household
# ============================================================
print("=" * 60)
print("WORKED EXAMPLE: Number of Pets per Household")
print("=" * 60)

x = np.array([0, 1, 2, 3, 4])
p = np.array([0.30, 0.35, 0.20, 0.10, 0.05])

# Step 1: Verify valid distribution
print(f"\nStep 1: Verify valid distribution")
print(f"  Σ P(X=x) = {p.sum():.2f}  {'✓ Valid' if abs(p.sum()-1)<1e-9 else '✗ Invalid'}")

# Step 2: E(X)
ex = np.sum(x * p)
print(f"\nStep 2: E(X) = Σ xᵢ · P(X=xᵢ)")
print(f"  {'x':<6} {'P(X=x)':<10} {'x·P(X=x)':<12}")
print(f"  {'-'*28}")
for xi, pi in zip(x, p):
    print(f"  {xi:<6} {pi:<10.2f} {xi*pi:<12.4f}")
print(f"  {'':6} {'':10} {'─'*12}")
print(f"  {'':6} {'E(X) =':<10} {ex:<12.4f}")

# Step 3: E(X²)
ex2 = np.sum(x**2 * p)
print(f"\nStep 3: E(X²) = Σ xᵢ² · P(X=xᵢ) = {ex2:.4f}")

# Step 4: Var(X)
var_x = ex2 - ex**2
print(f"\nStep 4: Var(X) = E(X²) − [E(X)]²")
print(f"  = {ex2:.4f} − ({ex:.4f})²")
print(f"  = {ex2:.4f} − {ex**2:.4f}")
print(f"  = {var_x:.4f}")

# Step 5: Standard deviation
sd_x = np.sqrt(var_x)
print(f"\nStep 5: σ = √Var(X) = √{var_x:.4f} = {sd_x:.4f}")

# Step 6: Interpretation
print(f"\nInterpretation:")
print(f"  Mean: {ex:.2f} pets per household")
print(f"  SD:   {sd_x:.2f} pets (typical deviation from the mean)")

# ============================================================
# QUESTION 1: Customer Orders
# ============================================================
print("\n\n" + "=" * 60)
print("QUESTION 1: Customer Orders")
print("=" * 60)

x1 = np.array([1, 2, 3, 4, 5])
p1 = np.array([0.25, 0.35, 0.20, 0.12, 0.08])

print(f"\n(a) Σ P = {p1.sum():.2f}  ✓ Valid")

ex1 = np.sum(x1 * p1)
print(f"\n(b) E(X) = {ex1:.4f}")

ex1_2 = np.sum(x1**2 * p1)
var1 = ex1_2 - ex1**2
sd1 = np.sqrt(var1)
print(f"\n(c) E(X²) = {ex1_2:.4f}")
print(f"    Var(X) = {ex1_2:.4f} - {ex1:.4f}² = {var1:.4f}")
print(f"    σ = {sd1:.4f}")

e_rev = 8 * ex1 + 3
print(f"\n(d) E(Revenue) = 8·E(X) + 3 = 8({ex1:.2f}) + 3 = ${e_rev:.2f}")

# ============================================================
# QUESTION 2: Apartment Maintenance Calls
# ============================================================
print("\n\n" + "=" * 60)
print("QUESTION 2: Apartment Maintenance Calls")
print("=" * 60)

x2 = np.array([0, 1, 2, 3, 4, 5])
p2 = np.array([0.15, 0.30, 0.25, 0.15, 0.10, 0.05])

print(f"\n(a) Σ P = {p2.sum():.2f}  ✓ Valid")

ex2_val = np.sum(x2 * p2)
print(f"\n(b) E(X) = {ex2_val:.4f}")

ex2_sq = np.sum(x2**2 * p2)
var2 = ex2_sq - ex2_val**2
sd2 = np.sqrt(var2)
print(f"\n(c) E(X²) = {ex2_sq:.4f}")
print(f"    Var(X) = {var2:.4f}")
print(f"    σ = {sd2:.4f}")

e_cost = 45 * ex2_val
sd_cost = 45 * sd2
print(f"\n(d) E(Cost) = 45 × {ex2_val:.2f} = ${e_cost:.2f}")
print(f"    SD(Cost) = 45 × {sd2:.4f} = ${sd_cost:.2f}")

p_ge3 = p2[3:].sum()
print(f"\n(e) P(X ≥ 3) = {p2[3]:.2f} + {p2[4]:.2f} + {p2[5]:.2f} = {p_ge3:.2f}")
print(f"    30% chance of 3+ calls in a day.")

# ============================================================
# VISUALIZATION
# ============================================================
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Plot 1: Worked example
axes[0].bar(x, p, color='steelblue', edgecolor='black', alpha=0.8)
axes[0].axvline(ex, color='red', linestyle='--', linewidth=2,
                label=f'E(X) = {ex:.2f}')
axes[0].set_xlabel('Number of Pets (x)')
axes[0].set_ylabel('P(X = x)')
axes[0].set_title('Pets per Household')
axes[0].legend()
axes[0].set_xticks(x)

# Plot 2: Customer orders
axes[1].bar(x1, p1, color='coral', edgecolor='black', alpha=0.8)
axes[1].axvline(ex1, color='red', linestyle='--', linewidth=2,
                label=f'E(X) = {ex1:.2f}')
axes[1].set_xlabel('Items per Order (x)')
axes[1].set_ylabel('P(X = x)')
axes[1].set_title('Customer Orders')
axes[1].legend()
axes[1].set_xticks(x1)

# Plot 3: Maintenance calls
axes[2].bar(x2, p2, color='mediumseagreen', edgecolor='black', alpha=0.8)
axes[2].axvline(ex2_val, color='red', linestyle='--', linewidth=2,
                label=f'E(X) = {ex2_val:.2f}')
axes[2].set_xlabel('Calls per Day (x)')
axes[2].set_ylabel('P(X = x)')
axes[2].set_title('Maintenance Calls')
axes[2].legend()
axes[2].set_xticks(x2)

plt.tight_layout()
plt.savefig('/home/claude/random_variables_plot.png', dpi=150)
plt.close()
print("\n\nPlot saved: random_variables_plot.png")
