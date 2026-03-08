"""
build_supplementary.py — Generate the three supplementary reference PDFs.

1. test_selection_flowchart.pdf  — Decision tree for choosing a test
2. master_formula_sheet.pdf      — 2-page cheat sheet of all formulas
3. master_critical_value_tables.pdf — Full z, t, χ², F tables

Usage:
    python scripts/build_supplementary.py              # Build all three
    python scripts/build_supplementary.py --flowchart  # Flowchart only
    python scripts/build_supplementary.py --formulas   # Formula sheet only
    python scripts/build_supplementary.py --tables     # Critical value tables only

Run from the repo root.
"""

import argparse
import os
import sys
from pathlib import Path

import numpy as np
from scipy import stats
from fpdf import FPDF

sys.path.insert(0, str(Path(__file__).parent))
from topic_registry import TOPIC_ORDER, TOPICS

OUTPUT_DIR = "supplementary"

# Unicode font paths (DejaVuSans supports Greek, math symbols, etc.)
FONT_DIR = "/usr/share/fonts/truetype/dejavu"
FONT_REGULAR = os.path.join(FONT_DIR, "DejaVuSans.ttf")
FONT_BOLD = os.path.join(FONT_DIR, "DejaVuSans-Bold.ttf")
FONT_ITALIC = os.path.join(FONT_DIR, "DejaVuSans-Oblique.ttf")
FONT_MONO = os.path.join(FONT_DIR, "DejaVuSansMono.ttf")
FONT_MONO_BOLD = os.path.join(FONT_DIR, "DejaVuSansMono-Bold.ttf")


def setup_unicode_fonts(pdf):
    """Register DejaVuSans as a Unicode font family in fpdf2."""
    if os.path.exists(FONT_REGULAR):
        pdf.add_font("DejaVu", "", FONT_REGULAR)
        pdf.add_font("DejaVu", "B", FONT_BOLD)
        pdf.add_font("DejaVu", "I", FONT_ITALIC)
        if os.path.exists(FONT_MONO):
            pdf.add_font("DejaVuMono", "", FONT_MONO)
        if os.path.exists(FONT_MONO_BOLD):
            pdf.add_font("DejaVuMono", "B", FONT_MONO_BOLD)
        return "DejaVu", "DejaVuMono"
    else:
        return "Helvetica", "Courier"


# ============================================================
# 1. MASTER FORMULA SHEET
# ============================================================

def build_formula_sheet():
    """Generate a 2-page landscape formula cheat sheet."""
    print("Building master formula sheet...")

    pdf = FPDF(orientation='L', unit='mm', format='Letter')
    pdf.set_auto_page_break(auto=True, margin=15)
    F, FM = setup_unicode_fonts(pdf)

    # --- PAGE 1: Test Formulas Table ---
    pdf.add_page()
    pdf.set_font(F, 'B', 14)
    pdf.set_text_color(47, 84, 150)
    pdf.cell(0, 8, 'Hypothesis Testing Formula Sheet', new_x="LMARGIN", new_y="NEXT")
    pdf.set_font(F, '', 8)
    pdf.set_text_color(128, 128, 128)
    pdf.cell(0, 5, 'Undergraduate Statistics — Quick Reference (Page 1: Formulas)', new_x="LMARGIN", new_y="NEXT")
    pdf.ln(2)

    # Table headers
    col_widths = [8, 42, 62, 28, 52, 42, 30]
    headers = ['#', 'Test', 'Test Statistic', 'df', 'Confidence Interval', 'Effect Size', 'Scale']

    pdf.set_font(F, 'B', 7)
    pdf.set_fill_color(47, 84, 150)
    pdf.set_text_color(255, 255, 255)
    for i, (w, h) in enumerate(zip(col_widths, headers)):
        pdf.cell(w, 6, h, border=1, fill=True, align='C')
    pdf.ln()

    # Table rows
    pdf.set_text_color(0, 0, 0)
    row_num = 0
    for key in TOPIC_ORDER:
        t = TOPICS[key]
        row_num += 1
        is_alt = row_num % 2 == 0

        if is_alt:
            pdf.set_fill_color(240, 245, 255)
        else:
            pdf.set_fill_color(255, 255, 255)

        # Get the first line of formulas only (for compactness)
        stat = t["test_stat_formula"].split('\n')[0]
        df = (t["df_formula"] or "—").replace("Not applicable", "—").split('(')[0].strip()
        ci = (t["ci_formula"] or "—").split('(')[0].strip()
        if len(ci) > 35:
            ci = ci[:32] + "..."
        es = t["effect_size_formula"]
        if isinstance(es, str) and len(es) > 28:
            es = es[:25] + "..."

        # Effect size scale
        scale = t["effect_size_scale"]
        if isinstance(scale, dict) and "small" in scale:
            scale_str = f"{scale.get('small','')}/{scale.get('medium','')}/{scale.get('large','')}"
        elif isinstance(scale, dict) and "note" in scale:
            scale_str = "context"
        elif isinstance(scale, dict):
            scale_str = str(list(scale.values())[:3])
        else:
            scale_str = "—"

        pdf.set_font(F, '', 6.5)
        row_data = [str(row_num), t["display_name"], stat, df, ci, es, scale_str]
        for w, val in zip(col_widths, row_data):
            pdf.cell(w, 5.5, val, border=1, fill=is_alt, align='L')
        pdf.ln()

    # --- PAGE 2: Decision Rules & Quick Reference ---
    pdf.add_page()
    pdf.set_font(F, 'B', 14)
    pdf.set_text_color(47, 84, 150)
    pdf.cell(0, 8, 'Hypothesis Testing — Decision Rules & Quick Reference', new_x="LMARGIN", new_y="NEXT")
    pdf.set_font(F, '', 8)
    pdf.set_text_color(128, 128, 128)
    pdf.cell(0, 5, 'Undergraduate Statistics — Quick Reference (Page 2)', new_x="LMARGIN", new_y="NEXT")
    pdf.ln(3)

    pdf.set_text_color(0, 0, 0)

    sections = [
        ("Decision Rules", [
            "Two-tailed: Reject H\u2080 if |test stat| > critical value, or if p-value < \u03b1",
            "Left-tailed: Reject H\u2080 if test stat < \u2212critical value, or if p-value < \u03b1",
            "Right-tailed: Reject H\u2080 if test stat > critical value, or if p-value < \u03b1",
        ]),
        ("One-Tailed vs Two-Tailed", [
            "Two-tailed: \u03b1 is split across both tails. Critical value uses \u03b1/2.",
            "One-tailed: Entire \u03b1 is in one tail. Critical value uses \u03b1 directly.",
            "One-tailed p-value = (two-tailed p-value) / 2, if test stat is in the hypothesized direction.",
        ]),
        ("Common Critical Z-Values", [
            "Two-tailed:  \u03b1=0.10 \u2192 z=1.645  |  \u03b1=0.05 \u2192 z=1.960  |  \u03b1=0.01 \u2192 z=2.576",
            "One-tailed:  \u03b1=0.10 \u2192 z=1.282  |  \u03b1=0.05 \u2192 z=1.645  |  \u03b1=0.01 \u2192 z=2.326",
        ]),
        ("Type I and Type II Errors", [
            "Type I Error (\u03b1): Rejecting H\u2080 when it is actually true (false positive). P(Type I) = \u03b1.",
            "Type II Error (\u03b2): Failing to reject H\u2080 when it is actually false (false negative). P(Type II) = \u03b2.",
            "Power = 1 \u2212 \u03b2 = probability of correctly rejecting a false H\u2080.",
        ]),
        ("Effect Size Interpretation", [
            "Cohen's d (t-tests): 0.2 = small, 0.5 = medium, 0.8 = large",
            "Cohen's h (proportions): 0.2 = small, 0.5 = medium, 0.8 = large",
            "Cohen's w (chi-square GoF): 0.1 = small, 0.3 = medium, 0.5 = large",
            "\u03b7\u00b2 eta-squared (ANOVA): 0.01 = small, 0.06 = medium, 0.14 = large",
            "r\u00b2 (correlation/regression): 0.01 = small, 0.09 = medium, 0.25 = large",
            "Cram\u00e9r's V (chi-square independence): depends on df\u2014see tables",
            "Rank-biserial r (nonparametric): 0.1 = small, 0.3 = medium, 0.5 = large",
        ]),
        ("Assumption Checklists", [
            "Z/T-tests: random sample, independence, normality (or n \u2265 30 by CLT)",
            "Two-sample t (equal var): + equal population variances (check with F-test)",
            "Chi-square tests: random sample, independence, all expected counts \u2265 5",
            "Fisher's exact: use when expected counts < 5 in a 2\u00d72 table",
            "ANOVA: random sample, independence, normality within groups, equal variances",
            "Nonparametric: random sample, independence (+ symmetry for Wilcoxon)",
            "Regression: linearity, independence, normality of residuals, constant variance (LINE)",
        ]),
    ]

    for title, items in sections:
        pdf.set_font(F, 'B', 9)
        pdf.set_text_color(47, 84, 150)
        pdf.cell(0, 6, title, new_x="LMARGIN", new_y="NEXT")
        pdf.set_font(F, '', 7.5)
        pdf.set_text_color(0, 0, 0)
        for item in items:
            pdf.cell(4, 4.5, '', new_x="END")
            pdf.cell(0, 4.5, f"\u2022 {item}", new_x="LMARGIN", new_y="NEXT")
        pdf.ln(2)

    # Footer
    pdf.set_y(-12)
    pdf.set_font(F, 'I', 7)
    pdf.set_text_color(160, 160, 160)
    pdf.cell(0, 5, 'Undergraduate Statistics', align='L')

    filepath = os.path.join(OUTPUT_DIR, "master_formula_sheet.pdf")
    pdf.output(filepath)
    print(f"  Saved: {filepath}")


# ============================================================
# 2. MASTER CRITICAL VALUE TABLES
# ============================================================

def build_critical_value_tables():
    """Generate multi-page PDF with z, t, chi-square, and F tables."""
    print("Building master critical value tables...")

    pdf = FPDF(orientation='P', unit='mm', format='Letter')
    pdf.set_auto_page_break(auto=True, margin=15)
    F, FM = setup_unicode_fonts(pdf)
    pdf.add_page()
    pdf.set_font(F, 'B', 16)
    pdf.set_text_color(47, 84, 150)
    pdf.cell(0, 10, 'Statistical Tables', new_x="LMARGIN", new_y="NEXT")
    pdf.ln(3)
    pdf.set_font(F, '', 10)
    pdf.set_text_color(0, 0, 0)

    how_to = [
        ("Z-Table (Standard Normal)", "Shows P(Z \u2264 z). To find a critical value, look up the desired cumulative probability. For a two-tailed test at \u03b1 = 0.05, find z where P(Z \u2264 z) = 0.975, giving z = 1.96."),
        ("T-Table", "Shows critical values t such that P(T > t) equals the column header. Read across the row for your degrees of freedom (df) and down the column for your significance level."),
        ("Chi-Square Table", "Shows critical values \u03c7\u00b2 such that P(\u03c7\u00b2 > value) equals the column header. Use df = k\u22121 for goodness-of-fit or df = (r\u22121)(c\u22121) for independence."),
        ("F-Table", "Shows critical values for the F-distribution. Numerator df is across the top, denominator df is down the side. Separate tables are provided for \u03b1 = 0.05 and \u03b1 = 0.01."),
    ]
    for title, text in how_to:
        pdf.set_font(F, 'B', 10)
        pdf.cell(0, 7, title, new_x="LMARGIN", new_y="NEXT")
        pdf.set_font(F, '', 9)
        pdf.multi_cell(0, 5, text)
        pdf.ln(2)

    # --- Z-TABLE ---
    pdf.add_page()
    pdf.set_font(F, 'B', 12)
    pdf.set_text_color(47, 84, 150)
    pdf.cell(0, 8, 'Standard Normal (Z) Table \u2014 P(Z \u2264 z)', new_x="LMARGIN", new_y="NEXT")
    pdf.ln(2)

    hundredths = [f".0{i}" if i < 10 else f".{i}" for i in range(10)]
    col_w = 15.5
    row_h = 4.2

    # Column headers
    pdf.set_font(F, 'B', 7)
    pdf.set_fill_color(47, 84, 150)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(col_w, row_h, 'z', border=1, fill=True, align='C')
    for h in hundredths:
        pdf.cell(col_w, row_h, h, border=1, fill=True, align='C')
    pdf.ln()

    pdf.set_text_color(0, 0, 0)
    pdf.set_font(FM, '', 6.5)

    z_rows = np.arange(-3.4, 3.5, 0.1)
    for z_base in z_rows:
        # Check if we need a new page
        if pdf.get_y() > 250:
            pdf.add_page()
            pdf.set_font(F, 'B', 10)
            pdf.set_text_color(47, 84, 150)
            pdf.cell(0, 7, 'Standard Normal (Z) Table (continued)', new_x="LMARGIN", new_y="NEXT")
            pdf.ln(1)
            pdf.set_font(F, 'B', 7)
            pdf.set_fill_color(47, 84, 150)
            pdf.set_text_color(255, 255, 255)
            pdf.cell(col_w, row_h, 'z', border=1, fill=True, align='C')
            for h in hundredths:
                pdf.cell(col_w, row_h, h, border=1, fill=True, align='C')
            pdf.ln()
            pdf.set_text_color(0, 0, 0)
            pdf.set_font(FM, '', 6.5)

        z_label = f"{z_base:.1f}"
        is_alt = int(round((z_base + 3.4) * 10)) % 2 == 0
        if is_alt:
            pdf.set_fill_color(245, 248, 255)
        else:
            pdf.set_fill_color(255, 255, 255)

        pdf.set_font(FM, 'B', 6.5)
        pdf.cell(col_w, row_h, z_label, border=1, fill=True, align='C')
        pdf.set_font(FM, '', 6.5)
        for j in range(10):
            z = z_base + j * 0.01
            p = stats.norm.cdf(z)
            pdf.cell(col_w, row_h, f"{p:.4f}", border=1, fill=is_alt, align='C')
        pdf.ln()

    # --- T-TABLE ---
    pdf.add_page()
    pdf.set_font(F, 'B', 12)
    pdf.set_text_color(47, 84, 150)
    pdf.cell(0, 8, "Student's t Distribution \u2014 Critical Values (Right-Tail Area)", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(2)

    t_alphas = [0.100, 0.050, 0.025, 0.010, 0.005]
    t_dfs = list(range(1, 41)) + [50, 60, 80, 100, 120]
    t_col_w = 22
    t_first_w = 18

    pdf.set_font(F, 'B', 8)
    pdf.set_fill_color(47, 84, 150)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(t_first_w, 5.5, 'df', border=1, fill=True, align='C')
    for a in t_alphas:
        pdf.cell(t_col_w, 5.5, f"\u03b1 = {a:.3f}", border=1, fill=True, align='C')
    pdf.ln()

    pdf.set_text_color(0, 0, 0)
    pdf.set_font(FM, '', 7.5)
    for i, df in enumerate(t_dfs):
        is_alt = i % 2 == 0
        if is_alt:
            pdf.set_fill_color(245, 248, 255)
        else:
            pdf.set_fill_color(255, 255, 255)

        pdf.set_font(FM, 'B', 7.5)
        pdf.cell(t_first_w, 5, str(df), border=1, fill=True, align='C')
        pdf.set_font(FM, '', 7.5)
        for a in t_alphas:
            val = stats.t.ppf(1 - a, df)
            pdf.cell(t_col_w, 5, f"{val:.3f}", border=1, fill=is_alt, align='C')
        pdf.ln()

    # Infinity row
    pdf.set_font(FM, 'B', 7.5)
    pdf.cell(t_first_w, 5, '\u221e', border=1, align='C')
    pdf.set_font(FM, '', 7.5)
    for a in t_alphas:
        val = stats.norm.ppf(1 - a)
        pdf.cell(t_col_w, 5, f"{val:.3f}", border=1, align='C')
    pdf.ln()

    # --- CHI-SQUARE TABLE ---
    pdf.add_page()
    pdf.set_font(F, 'B', 12)
    pdf.set_text_color(47, 84, 150)
    pdf.cell(0, 8, 'Chi-Square Distribution \u2014 Critical Values (Right-Tail Area)', new_x="LMARGIN", new_y="NEXT")
    pdf.ln(2)

    chi_alphas = [0.100, 0.050, 0.025, 0.010, 0.005]
    chi_dfs = list(range(1, 31)) + [40, 50, 60, 80, 100]
    chi_col_w = 22
    chi_first_w = 18

    pdf.set_font(F, 'B', 8)
    pdf.set_fill_color(47, 84, 150)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(chi_first_w, 5.5, 'df', border=1, fill=True, align='C')
    for a in chi_alphas:
        pdf.cell(chi_col_w, 5.5, f"\u03b1 = {a:.3f}", border=1, fill=True, align='C')
    pdf.ln()

    pdf.set_text_color(0, 0, 0)
    pdf.set_font(FM, '', 7.5)
    for i, df in enumerate(chi_dfs):
        is_alt = i % 2 == 0
        if is_alt:
            pdf.set_fill_color(245, 248, 255)
        else:
            pdf.set_fill_color(255, 255, 255)

        pdf.set_font(FM, 'B', 7.5)
        pdf.cell(chi_first_w, 5, str(df), border=1, fill=True, align='C')
        pdf.set_font(FM, '', 7.5)
        for a in chi_alphas:
            val = stats.chi2.ppf(1 - a, df)
            pdf.cell(chi_col_w, 5, f"{val:.3f}", border=1, fill=is_alt, align='C')
        pdf.ln()

    # --- F-TABLE (α = 0.05) ---
    _build_f_table(pdf, 0.05, F, FM)

    # --- F-TABLE (α = 0.01) ---
    _build_f_table(pdf, 0.01, F, FM)

    # Footer on last page
    pdf.set_y(-12)
    pdf.set_font(F, 'I', 7)
    pdf.set_text_color(160, 160, 160)
    pdf.cell(0, 5, 'Generated with scipy.stats \u2014 Undergraduate Statistics', align='C')

    filepath = os.path.join(OUTPUT_DIR, "master_critical_value_tables.pdf")
    pdf.output(filepath)
    print(f"  Saved: {filepath}")


def _build_f_table(pdf, alpha, F="DejaVu", FM="DejaVuMono"):
    """Build an F-distribution critical value table page."""
    pdf.add_page('L')  # Landscape for F-table
    pdf.set_font(F, 'B', 11)
    pdf.set_text_color(47, 84, 150)
    pdf.cell(0, 8, f'F Distribution \u2014 Critical Values (\u03b1 = {alpha})', new_x="LMARGIN", new_y="NEXT")
    pdf.set_font(F, '', 7)
    pdf.set_text_color(128, 128, 128)
    pdf.cell(0, 4, 'Numerator df across top, denominator df down side', new_x="LMARGIN", new_y="NEXT")
    pdf.ln(1)

    num_dfs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 20, 24, 30, 40, 60, 120]
    den_dfs = list(range(1, 31)) + [40, 60, 120]
    f_col_w = 13
    f_first_w = 12

    # Header row
    pdf.set_font(F, 'B', 6)
    pdf.set_fill_color(47, 84, 150)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(f_first_w, 4.5, 'df2\\df1', border=1, fill=True, align='C')
    for d1 in num_dfs:
        pdf.cell(f_col_w, 4.5, str(d1), border=1, fill=True, align='C')
    pdf.ln()

    pdf.set_text_color(0, 0, 0)
    pdf.set_font(FM, '', 5.5)
    for i, d2 in enumerate(den_dfs):
        if pdf.get_y() > 185:
            pdf.add_page('L')
            pdf.set_font(F, 'B', 9)
            pdf.set_text_color(47, 84, 150)
            pdf.cell(0, 6, f'F Distribution \u03b1 = {alpha} (continued)', new_x="LMARGIN", new_y="NEXT")
            pdf.ln(1)
            pdf.set_font(F, 'B', 6)
            pdf.set_fill_color(47, 84, 150)
            pdf.set_text_color(255, 255, 255)
            pdf.cell(f_first_w, 4.5, 'df2\\df1', border=1, fill=True, align='C')
            for d1 in num_dfs:
                pdf.cell(f_col_w, 4.5, str(d1), border=1, fill=True, align='C')
            pdf.ln()
            pdf.set_text_color(0, 0, 0)
            pdf.set_font(FM, '', 5.5)

        is_alt = i % 2 == 0
        if is_alt:
            pdf.set_fill_color(245, 248, 255)
        else:
            pdf.set_fill_color(255, 255, 255)

        pdf.set_font(FM, 'B', 5.5)
        pdf.cell(f_first_w, 4, str(d2), border=1, fill=True, align='C')
        pdf.set_font(FM, '', 5.5)
        for d1 in num_dfs:
            val = stats.f.ppf(1 - alpha, d1, d2)
            if val >= 100:
                txt = f"{val:.1f}"
            else:
                txt = f"{val:.2f}"
            pdf.cell(f_col_w, 4, txt, border=1, fill=is_alt, align='C')
        pdf.ln()


# ============================================================
# 3. TEST SELECTION FLOWCHART
# ============================================================

def build_flowchart():
    """Generate a test selection flowchart using matplotlib."""
    print("Building test selection flowchart...")

    try:
        import matplotlib.pyplot as plt
        import matplotlib.patches as mpatches
    except ImportError:
        print("  ERROR: matplotlib required. pip install matplotlib")
        return

    fig, ax = plt.subplots(figsize=(22, 14))
    ax.set_xlim(0, 22)
    ax.set_ylim(0, 14)
    ax.axis('off')

    # Colours
    C_DECISION = '#E3F2FD'    # light blue — decision nodes
    C_PARAM = '#BBDEFB'       # blue — parametric tests
    C_NONPARAM = '#C8E6C9'   # green — nonparametric tests
    C_CATEG = '#FFE0B2'       # orange — categorical tests
    C_REGR = '#E1BEE7'        # purple — regression tests
    C_BORDER = '#37474F'

    def draw_box(x, y, w, h, text, color, fontsize=7, bold=False):
        rect = mpatches.FancyBboxPatch(
            (x, y), w, h, boxstyle="round,pad=0.15",
            facecolor=color, edgecolor=C_BORDER, linewidth=0.8
        )
        ax.add_patch(rect)
        weight = 'bold' if bold else 'normal'
        ax.text(x + w/2, y + h/2, text, ha='center', va='center',
                fontsize=fontsize, fontweight=weight, wrap=True)

    def draw_arrow(x1, y1, x2, y2, label=None):
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                     arrowprops=dict(arrowstyle='->', color=C_BORDER, lw=1))
        if label:
            mx, my = (x1+x2)/2, (y1+y2)/2
            ax.text(mx, my + 0.15, label, fontsize=6, ha='center',
                    color='#666', style='italic')

    # Title
    ax.text(11, 13.6, 'Which Hypothesis Test Should I Use?',
            ha='center', fontsize=16, fontweight='bold', color='#1565C0')
    ax.text(11, 13.2, 'Undergraduate Statistics — Quick Reference',
            ha='center', fontsize=9, color='#666')

    # START node
    draw_box(9, 12.2, 4, 0.7, 'What type of data?', C_DECISION, 9, bold=True)

    # --- CATEGORICAL BRANCH (left) ---
    draw_arrow(9, 12.55, 4, 12.55, 'Categorical')
    draw_box(2, 12.2, 4, 0.7, 'How many variables?', C_DECISION, 8)

    # One variable
    draw_arrow(3, 12.2, 3, 11.3)
    draw_box(1.5, 10.8, 3, 0.7, 'One variable', C_DECISION, 7)
    draw_arrow(2, 10.8, 1.2, 10.0)
    draw_box(0, 9.5, 2.4, 0.7, 'Chi-Square\nGoodness-of-Fit', C_CATEG, 6.5, bold=True)
    draw_arrow(4, 10.8, 4.8, 10.0)
    draw_box(3.5, 9.5, 2.6, 0.7, 'Proportion\nZ-Test', C_CATEG, 6.5, bold=True)

    # Two variables
    draw_arrow(5, 12.2, 5, 11.3)
    draw_box(4.5, 10.8, 3, 0.7, 'Two variables\n(contingency table)', C_DECISION, 6.5)
    draw_arrow(5.2, 10.8, 4.5, 9.7)
    draw_box(3.2, 9.0, 2.6, 0.7, 'All E \u2265 5?\nChi-Square\nIndependence', C_CATEG, 5.5, bold=True)
    draw_arrow(6.8, 10.8, 7.5, 9.7)
    draw_box(6.2, 9.0, 2.6, 0.7, "E < 5?\nFisher's\nExact Test", C_CATEG, 5.5, bold=True)

    # --- CONTINUOUS BRANCH (right) ---
    draw_arrow(13, 12.55, 15, 12.55, 'Continuous')
    draw_box(14, 12.2, 4, 0.7, 'How many groups?', C_DECISION, 8)

    # ONE SAMPLE
    draw_arrow(14.5, 12.2, 11.5, 11.1)
    draw_box(10, 10.5, 3, 0.7, 'ONE sample', C_DECISION, 8)
    draw_arrow(10.5, 10.5, 9.5, 9.5)
    draw_box(8.5, 8.8, 2, 0.7, '\u03c3 known?\nZ-Test', C_PARAM, 6.5, bold=True)
    draw_arrow(11.5, 10.5, 11.5, 9.5)
    draw_box(10.5, 8.8, 2, 0.7, '\u03c3 unknown?\nT-Test', C_PARAM, 6.5, bold=True)
    draw_arrow(12.5, 10.5, 13.5, 9.5)
    draw_box(13, 8.8, 2.2, 0.7, 'Normality?\nShapiro-Wilk', C_NONPARAM, 6, bold=True)

    # TWO SAMPLES
    draw_arrow(16, 12.2, 16, 11.1)
    draw_box(14.8, 10.5, 3, 0.7, 'TWO samples', C_DECISION, 8)

    draw_arrow(15.2, 10.5, 14.5, 9.5, 'Paired')
    draw_box(13.5, 8.0, 2, 0.7, 'Paired\nT-Test', C_PARAM, 6.5, bold=True)
    draw_arrow(13.8, 8.0, 13.5, 7.0)
    draw_box(12.3, 6.3, 2.4, 0.7, 'Non-normal?\nWilcoxon\nSigned-Rank', C_NONPARAM, 5.5, bold=True)

    draw_arrow(17, 10.5, 18, 9.5, 'Independent')
    draw_box(16.8, 8.0, 2.4, 0.7, 'Equal var?\n2-Sample\nT-Test', C_PARAM, 5.5, bold=True)
    draw_arrow(19.5, 9.0, 19.8, 8.0)
    draw_box(19.2, 7.3, 2.2, 0.7, "Unequal var?\nWelch's\nT-Test", C_PARAM, 5.5, bold=True)
    draw_arrow(19.5, 7.3, 19.5, 6.3)
    draw_box(18.5, 5.6, 2, 0.7, 'Non-normal?\nMann-Whitney\nU', C_NONPARAM, 5.5, bold=True)

    # THREE+ SAMPLES
    draw_arrow(17.5, 12.2, 19.5, 11.1)
    draw_box(18.5, 10.5, 3, 0.7, '3+ samples', C_DECISION, 8)

    draw_arrow(19, 10.5, 18.2, 9.5)
    draw_box(16.8, 9.0, 2.8, 0.5, 'One-Way\nANOVA', C_PARAM, 6, bold=True)
    draw_arrow(20.5, 10.5, 21, 9.5)
    draw_box(20, 9.0, 2, 0.5, 'Two-Way\nANOVA', C_PARAM, 6, bold=True)
    draw_arrow(17.5, 9.0, 17, 8.2)
    draw_box(15.8, 7.6, 2.4, 0.6, 'Non-normal?\nKruskal-\nWallis', C_NONPARAM, 5.5, bold=True)

    # RELATIONSHIP branch
    draw_arrow(16, 12.2, 16, 5.2)
    draw_box(14.8, 4.5, 3, 0.7, 'Relationship\nbetween two variables?', C_DECISION, 6.5)
    draw_arrow(15, 4.5, 12, 3.8)
    draw_box(10.5, 3.2, 3, 0.6, 'Correlation\nT-Test (\u03c1 = 0)', C_REGR, 6, bold=True)
    draw_arrow(16.3, 4.5, 16.3, 3.8)
    draw_box(15, 3.2, 2.6, 0.6, 'Slope T-Test\n(\u03b2\u2081 = 0)', C_REGR, 6, bold=True)
    draw_arrow(17.5, 4.5, 19, 3.8)
    draw_box(18, 3.2, 2.5, 0.6, 'Regression\nF-Test', C_REGR, 6, bold=True)

    # Legend
    legend_items = [
        (C_DECISION, 'Decision Node'),
        (C_PARAM, 'Parametric Test'),
        (C_NONPARAM, 'Nonparametric Test'),
        (C_CATEG, 'Categorical Test'),
        (C_REGR, 'Regression/Correlation'),
    ]
    for i, (color, label) in enumerate(legend_items):
        x_leg = 0.3
        y_leg = 2.0 - i * 0.4
        rect = mpatches.FancyBboxPatch(
            (x_leg, y_leg), 0.5, 0.3, boxstyle="round,pad=0.05",
            facecolor=color, edgecolor=C_BORDER, linewidth=0.5
        )
        ax.add_patch(rect)
        ax.text(x_leg + 0.7, y_leg + 0.15, label, fontsize=7, va='center')

    plt.tight_layout()
    filepath = os.path.join(OUTPUT_DIR, "test_selection_flowchart.pdf")
    plt.savefig(filepath, dpi=200, bbox_inches='tight')
    plt.close()
    print(f"  Saved: {filepath}")


# ============================================================
# MAIN
# ============================================================

def main():
    parser = argparse.ArgumentParser(description="Build supplementary reference PDFs")
    parser.add_argument("--flowchart", action="store_true", help="Build flowchart only")
    parser.add_argument("--formulas", action="store_true", help="Build formula sheet only")
    parser.add_argument("--tables", action="store_true", help="Build critical value tables only")
    args = parser.parse_args()

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    build_specific = args.flowchart or args.formulas or args.tables

    if not build_specific or args.formulas:
        build_formula_sheet()
    if not build_specific or args.tables:
        build_critical_value_tables()
    if not build_specific or args.flowchart:
        build_flowchart()

    print("\nDone! All supplementary files are in supplementary/")


if __name__ == "__main__":
    main()
