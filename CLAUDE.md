# CLAUDE.md — Stats Repo: Hypothesis Testing Lecture Materials

## Overview

This repo contains undergraduate statistics lecture materials. Your job is to generate complete, publication-ready lecture materials for each hypothesis test topic listed below, plus several supplementary reference files. Work through them **one topic at a time**, committing after each.

**Note:** This file supersedes any previous conventions in REORGANIZE.md. The `_notes.pdf` replaces the old `_notes.docx` format. Each topic now produces 6 files (not 4). If any pre-existing files in this repo don't match the new structure, migrate them: split combined notes+questions files into separate files, rename to match the conventions below, and delete any orphaned duplicates.

---

## Environment Setup

Before generating any files, install all required Python packages:

```bash
pip install openpyxl fpdf2 python-pptx scipy matplotlib numpy pandas
```

For recalculating Excel formulas after creation, use the recalc script included in this repo (or environment):

```bash
python scripts/recalc.py <file.xlsx>
```

If `scripts/recalc.py` is not available, use LibreOffice directly:

```bash
libreoffice --headless --calc --convert-to xlsx <file.xlsx>
```

---

## Target Folder Structure

Every hypothesis test topic gets its own `snake_case` folder with **6 files**:

```
stats/
├── README.md
├── CLAUDE.md
├── supplementary/
│   ├── test_selection_flowchart.pdf
│   ├── master_formula_sheet.pdf
│   └── master_critical_value_tables.pdf
├── one_sample_z_test/
│   ├── one_sample_z_test.xlsx          # Excel notes (definitions, formulas, worked example)
│   ├── one_sample_z_test_notes.pdf     # PDF lecture notes (same content, print-ready)
│   ├── one_sample_z_test.pptx          # Lecture slides
│   ├── one_sample_z_test_questions.xlsx # Practice questions ONLY (no answers)
│   ├── one_sample_z_test_answers.xlsx   # Full worked answers to the practice questions
│   └── one_sample_z_test_bonus.py       # Python script reproducing all examples
├── one_sample_t_test/
│   └── ... (same 6-file pattern)
└── ...
```

---

## File Naming Rules

- All folder and file names: `snake_case`, lowercase, underscores, no numbered prefixes.
- Suffixes: `_notes.pdf`, `_questions.xlsx`, `_answers.xlsx`, `_bonus.py`.
- The main Excel file and pptx match the folder name exactly (e.g., `paired_t_test.xlsx`).
- `_notes.pdf` **replaces** the old `_notes.docx` convention. Do not generate .docx files.

---

## Complete Topic List (23 Topics)

Generate materials for each of the following in order. After finishing a topic, `git add` and `git commit` with message `feat: add <topic_name> materials`.

### One-Sample Tests
1. `one_sample_z_test` — One-Sample Z-Test (population mean, σ known)
2. `one_sample_t_test` — One-Sample T-Test (population mean, σ unknown)
3. `one_sample_proportion_z_test` — One-Sample Proportion Z-Test

### Two-Sample Tests
4. `two_sample_z_test` — Two-Sample Z-Test (independent means, σ known)
5. `two_sample_t_test_equal_var` — Two-Sample T-Test (independent means, equal variances assumed)
6. `welchs_t_test` — Welch's T-Test (independent means, unequal variances)
7. `paired_t_test` — Paired T-Test (dependent/matched samples)
8. `two_proportion_z_test` — Two-Proportion Z-Test

### Chi-Square Tests
9. `chi_square_goodness_of_fit` — Chi-Square Goodness-of-Fit Test
10. `chi_square_independence` — Chi-Square Test of Independence
11. `fishers_exact_test` — Fisher's Exact Test (2×2 tables with small expected counts)

### Normality Testing
12. `shapiro_wilk_test` — Shapiro-Wilk Test for Normality

### ANOVA
13. `one_way_anova` — One-Way ANOVA
14. `two_way_anova` — Two-Way ANOVA

### Nonparametric Tests
15. `sign_test` — Sign Test
16. `wilcoxon_signed_rank` — Wilcoxon Signed-Rank Test
17. `mann_whitney_u` — Mann-Whitney U Test
18. `kruskal_wallis` — Kruskal-Wallis Test

### Regression & Correlation
19. `correlation_t_test` — T-Test for Correlation Coefficient (ρ = 0)
20. `regression_slope_t_test` — T-Test for Regression Slope (β₁ = 0)
21. `regression_f_test` — F-Test for Overall Regression Significance

### Variance Tests
22. `chi_square_variance` — Chi-Square Test for a Single Variance
23. `f_test_two_variances` — F-Test for Equality of Two Variances

---

## Cross-Reference Map

Every topic's Notes sheet and PDF must include a **"Related Tests"** box at the bottom listing which other tests a student should look at next. Use the following map:

| Topic | Related Tests (include these in the "See Also" box) |
|-------|------------------------------------------------------|
| one_sample_z_test | one_sample_t_test (when σ is unknown), shapiro_wilk_test (to verify normality assumption) |
| one_sample_t_test | one_sample_z_test (when σ is known), paired_t_test (when data are matched pairs), shapiro_wilk_test (to verify normality), wilcoxon_signed_rank (nonparametric alternative) |
| one_sample_proportion_z_test | two_proportion_z_test (comparing two groups), chi_square_goodness_of_fit (multiple categories) |
| two_sample_z_test | two_sample_t_test_equal_var (when σ is unknown), welchs_t_test (unequal variances) |
| two_sample_t_test_equal_var | welchs_t_test (when equal variance assumption fails), f_test_two_variances (to check equal variance assumption), mann_whitney_u (nonparametric alternative), shapiro_wilk_test (to verify normality) |
| welchs_t_test | two_sample_t_test_equal_var (when variances are equal), mann_whitney_u (nonparametric alternative) |
| paired_t_test | one_sample_t_test (applied to differences), wilcoxon_signed_rank (nonparametric alternative), sign_test (nonparametric alternative with ordinal data) |
| two_proportion_z_test | one_sample_proportion_z_test (single proportion), chi_square_independence (more than 2 groups), fishers_exact_test (small samples) |
| chi_square_goodness_of_fit | one_sample_proportion_z_test (single proportion, 2 categories), shapiro_wilk_test (testing normality specifically) |
| chi_square_independence | fishers_exact_test (when expected counts < 5), two_proportion_z_test (2×2 table, equivalent test) |
| fishers_exact_test | chi_square_independence (when expected counts are all ≥ 5), two_proportion_z_test (large-sample alternative) |
| shapiro_wilk_test | one_sample_t_test (requires normality), paired_t_test (requires normality), one_way_anova (requires normality within groups) |
| one_way_anova | kruskal_wallis (nonparametric alternative), two_way_anova (two factors), two_sample_t_test_equal_var (only 2 groups), f_test_two_variances (checking homogeneity of variance) |
| two_way_anova | one_way_anova (single factor), kruskal_wallis (nonparametric, single factor) |
| sign_test | wilcoxon_signed_rank (more powerful nonparametric paired test), paired_t_test (parametric alternative) |
| wilcoxon_signed_rank | paired_t_test (parametric alternative), sign_test (less powerful alternative for ordinal data), mann_whitney_u (independent samples version) |
| mann_whitney_u | two_sample_t_test_equal_var (parametric alternative), welchs_t_test (parametric alternative), wilcoxon_signed_rank (paired version), kruskal_wallis (more than 2 groups) |
| kruskal_wallis | one_way_anova (parametric alternative), mann_whitney_u (only 2 groups) |
| correlation_t_test | regression_slope_t_test (equivalent for simple regression), regression_f_test (overall model significance) |
| regression_slope_t_test | correlation_t_test (equivalent test), regression_f_test (overall model significance) |
| regression_f_test | regression_slope_t_test (individual predictor), one_way_anova (comparing group means, related framework) |
| chi_square_variance | f_test_two_variances (comparing two variances) |
| f_test_two_variances | chi_square_variance (single variance), two_sample_t_test_equal_var (requires this test first to check assumption) |

---

## Content Requirements for Each Topic

### 1. Main Excel Notes (`<topic>.xlsx`)

Use openpyxl. One sheet per section. Professional formatting (Arial font, borders, header fills, column widths set for readability).

**Sheet: "Notes"**
- Definition of the test (1–2 sentences: what it tests and when to use it)
- Hypotheses: H₀ and H₁ written out in both words and symbols. Show both two-tailed and one-tailed forms.
- Test statistic formula with every symbol defined
- Degrees of freedom formula (if applicable)
- Decision rule: reject H₀ when... (critical value approach AND p-value approach)
- Assumptions / conditions (numbered list in cells)
- **Confidence interval formula**: Show the corresponding confidence interval formula for the parameter being tested. For example:
  - Z-test for mean: x̄ ± z_(α/2) · σ/√n
  - T-test for mean: x̄ ± t_(α/2, df) · s/√n
  - Proportion: p̂ ± z_(α/2) · √(p̂(1−p̂)/n)
  - Difference of means: (x̄₁ − x̄₂) ± t · SE
  - For tests where a CI doesn't naturally apply (e.g., chi-square goodness-of-fit, Shapiro-Wilk), write "Not applicable for this test" and briefly explain why.
- **Effect size**: Define and show the formula for the appropriate effect size measure:
  - Z-tests and t-tests: Cohen's d = (x̄ − μ₀) / s (one-sample) or d = (x̄₁ − x̄₂) / s_pooled (two-sample)
  - Paired t-test: Cohen's d = d̄ / s_d
  - Proportions: Cohen's h = 2·arcsin(√p₁) − 2·arcsin(√p₂)
  - Chi-square independence: Cramér's V = √(χ²/(n·min(r−1, c−1)))
  - Chi-square goodness-of-fit: Cohen's w = √(Σ(p_observed − p_expected)² / p_expected)
  - ANOVA: η² = SS_between / SS_total (eta-squared)
  - Correlation: r² (coefficient of determination)
  - Regression: R² and adjusted R²
  - Nonparametric: r = Z / √n (rank-biserial or matched-pairs rank-biserial as appropriate)
  - Include interpretation guidelines (e.g., d: 0.2 = small, 0.5 = medium, 0.8 = large)
- **Type I and Type II error interpretation**: Two clearly written sentences explaining what each error means *in the specific context of this test*. Do not use generic language — tailor it. For example:
  - One-sample t-test about average exam score:
    - "Type I error: Concluding that the average exam score has changed from 72 when in reality it has not (false alarm)."
    - "Type II error: Failing to detect that the average exam score has changed from 72 when in reality it has (missed finding)."
  - Chi-square test of independence:
    - "Type I error: Concluding that gender and study preference are associated when they are actually independent."
    - "Type II error: Failing to detect an association between gender and study preference when one actually exists."
- Notation summary table (symbol → meaning)
- Relevant critical value mini-table (z, t, χ², or F as appropriate) — for quick reference only; full tables are in the supplementary folder
- **"See Also" box**: List the related tests from the Cross-Reference Map above, with a one-line explanation of when to use each alternative. Format as a small bordered table at the bottom of the sheet.

**Sheet: "Worked Example"**
- A realistic, easy-to-follow problem statement
- Full step-by-step solution (9–11 steps):
  1. State hypotheses
  2. Identify known values
  3. Check assumptions (briefly confirm they are met for this data)
  4. Compute test statistic
  5. Find df (if applicable)
  6. Find critical value
  7. Compare / compute p-value
  8. Decision (reject or fail to reject)
  9. **Compute the confidence interval** (show the formula, plug in values, state the interval)
  10. **Compute effect size** (show formula, plug in values, interpret: small/medium/large)
  11. Plain-English conclusion (include the CI and effect size in the conclusion sentence)
- Use **Excel formulas** (not hardcoded Python calculations) wherever possible so the spreadsheet is dynamic
- Highlight the final test statistic and decision cells with a yellow fill
- **One of the two practice questions must be one-tailed** (see Practice Questions below)

### 2. PDF Lecture Notes (`<topic>_notes.pdf`)

Generate using reportlab or fpdf2. The PDF should contain the **same content** as the Excel "Notes" sheet, reformatted for printing/reading:

- Title page or header with the test name
- Clear section headings: Definition, Hypotheses, Test Statistic, Degrees of Freedom, Decision Rule, Confidence Interval, Effect Size, Type I & Type II Errors, Assumptions, Notation, Related Tests
- Formulas rendered clearly (use Unicode math symbols: Σ, μ, σ, χ², √, ≠, ≤, ≥, H₀, H₁, etc.)
- A brief **"When to Use This Test vs Alternatives"** paragraph (e.g., "Use the one-sample t-test instead of the z-test when σ is unknown. If the normality assumption is violated, consider the Wilcoxon signed-rank test as a nonparametric alternative."). Use the cross-reference map to write this paragraph.
- The same worked example from the Excel file, fully written out (including CI and effect size steps)
- **Type I and Type II error interpretation** — same context-specific sentences from the Excel notes
- **"See Also" section** at the end of the PDF listing related tests with brief one-line descriptions
- Page numbers in footer
- Professional font (Helvetica or Times), 11–12pt body text, 14–16pt headings

### 3. Lecture Slides (`<topic>.pptx`)

Generate using python-pptx. 10–14 slides per deck:

- Slide 1: Title slide with test name and subtitle "Undergraduate Statistics"
- Slide 2: "When Do We Use This Test?" — plain-English description and real-world scenario
- Slide 3: Hypotheses (two-tailed and one-tailed forms)
- Slide 4: Test statistic formula with notation defined
- Slide 5: Decision rule (critical value and p-value approaches)
- Slide 6: Assumptions / conditions
- Slide 7: Confidence interval formula and interpretation
- Slide 8: Effect size formula and interpretation scale
- Slides 9–11: Worked example broken across slides (problem → setup → calculation → conclusion with CI and effect size)
- Slide 12: Type I and Type II errors — what each means in context
- Slide 13: "Common Mistakes to Avoid" — 3–4 bullet points of typical student errors
- Slide 14: Summary / key takeaways + "See Also" list of related tests

Use a clean colour scheme (dark blue headings, white background, readable font sizes ≥ 20pt).

### 4. Practice Questions (`<topic>_questions.xlsx`)

**This file contains ONLY the questions — no solutions.**

- Sheet: "Questions"
- 2 practice problems per topic
- **Question 1 must be two-tailed.** Question 2 must be **one-tailed** (either left-tailed or right-tailed — vary across topics).
- Each problem should have a different context/scenario from the worked example and from each other
- Include all necessary data (sample means, sizes, standard deviations, observed counts, etc.)
- State the significance level (vary between α = 0.01, 0.05, 0.10 across problems)
- End each problem with: "Show all steps: state hypotheses, compute test statistic, find critical value / p-value, compute the confidence interval, compute the effect size, make a decision, and state your conclusion in plain English."
- Include a data table if applicable (e.g., contingency table, paired data, ANOVA groups)

### 5. Answers (`<topic>_answers.xlsx`)

**Full worked solutions to every practice question.**

- One sheet per answer ("Answer 1", "Answer 2")
- Mirror the same step-by-step structure as the worked example (all 11 steps, including CI and effect size)
- **For the one-tailed question (Answer 2):** clearly show how the critical value and p-value differ from the two-tailed case. Add a note cell explaining: "For a one-tailed test, the entire α area is in one tail, so the critical value is z_(α) or t_(α,df) instead of z_(α/2) or t_(α/2,df). The p-value is halved compared to the two-tailed p-value (if the test statistic is in the hypothesized direction)."
- Include **Type I and Type II error interpretation** tailored to the specific question context (not the worked example context — write new sentences that match the question scenario)
- Use **Excel formulas** for all calculations (not hardcoded numbers)
- Highlight the final test statistic, CI, effect size, and decision with yellow fill
- Every intermediate value shown — never skip a step

### 6. Bonus Python Script (`<topic>_bonus.py`)

A single well-commented `.py` file that:

- Has a docstring at the top explaining what the script covers
- Imports: numpy, scipy.stats, matplotlib.pyplot, pandas as needed
- Reproduces the worked example with full printed step-by-step output, **including CI and effect size**
- Reproduces both practice questions with printed solutions (both two-tailed and one-tailed)
- For the one-tailed question, explicitly prints: the one-tailed critical value, the one-tailed p-value, and a note comparing to the two-tailed equivalents
- Uses scipy's built-in test function (e.g., `stats.ttest_1samp`, `stats.chi2_contingency`) to verify hand calculations
- **Prints the confidence interval** using scipy or manual calculation
- **Prints the effect size** with interpretation label (small/medium/large)
- **Prints the Type I and Type II error interpretation** for each problem
- Generates at least one matplotlib visualization:
  - For z/t tests: normal/t distribution with rejection region shaded and test statistic marked. For one-tailed tests, shade only the relevant tail.
  - For chi-square tests: chi-square distribution with rejection region
  - For ANOVA: boxplots of group data + F distribution
  - For nonparametric: appropriate comparison plots
  - For regression: scatter plot with regression line + residual plot
  - For Shapiro-Wilk: Q-Q plot + histogram with normal overlay
  - For Fisher's exact: mosaic plot or stacked bar chart of the 2×2 table
- Saves the plot as `<topic>_plot.png` in the same folder
- All code should be beginner-friendly with comments explaining each step

---

## Supplementary Materials (Repo-Level)

Generate these **after all 23 topics are complete**. Place them in a `supplementary/` folder at the repo root.

### 1. Test Selection Flowchart (`supplementary/test_selection_flowchart.pdf`)

A single-page decision-tree PDF that helps students pick the right test. Generate using matplotlib, graphviz, or reportlab.

The flowchart should follow this decision logic:

```
START: What type of data do you have?
│
├── Categorical (counts/frequencies)
│   ├── One variable?
│   │   ├── Testing if proportions match a known distribution? → Chi-Square Goodness-of-Fit
│   │   └── Testing a single proportion against a value? → One-Sample Proportion Z-Test
│   └── Two variables (contingency table)?
│       ├── Expected counts all ≥ 5? → Chi-Square Test of Independence
│       └── Any expected counts < 5 (2×2 table)? → Fisher's Exact Test
│
├── Continuous / Numerical
│   ├── How many groups/samples?
│   │   ├── ONE sample
│   │   │   ├── Testing normality? → Shapiro-Wilk Test
│   │   │   ├── Testing a variance? → Chi-Square Variance Test
│   │   │   ├── σ known? → One-Sample Z-Test
│   │   │   └── σ unknown? → One-Sample T-Test
│   │   │       └── Normality violated? → Wilcoxon Signed-Rank Test
│   │   │
│   │   ├── TWO samples
│   │   │   ├── Paired / matched?
│   │   │   │   ├── Normality OK? → Paired T-Test
│   │   │   │   └── Normality violated? → Wilcoxon Signed-Rank Test (or Sign Test)
│   │   │   └── Independent?
│   │   │       ├── Comparing variances? → F-Test for Two Variances
│   │   │       ├── σ₁ and σ₂ known? → Two-Sample Z-Test
│   │   │       ├── Assume equal variances? → Two-Sample T-Test (Equal Var)
│   │   │       ├── Unequal variances? → Welch's T-Test
│   │   │       └── Normality violated? → Mann-Whitney U Test
│   │   │
│   │   └── THREE or more samples
│   │       ├── One factor?
│   │       │   ├── Normality + equal variances OK? → One-Way ANOVA
│   │       │   └── Assumptions violated? → Kruskal-Wallis Test
│   │       └── Two factors? → Two-Way ANOVA
│   │
│   └── Relationship between two variables?
│       ├── Testing correlation (ρ = 0)? → Correlation T-Test
│       ├── Testing slope (β₁ = 0)? → Regression Slope T-Test
│       └── Testing overall model? → Regression F-Test
```

Design requirements:
- Landscape orientation, single page
- Readable font (≥ 9pt at final size)
- Colour-coded branches: blue for parametric, green for nonparametric, orange for categorical
- Each terminal node shows the test name in a rounded box
- Title: "Which Hypothesis Test Should I Use?"
- Footer: "Undergraduate Statistics — Quick Reference"

### 2. Master Formula Sheet (`supplementary/master_formula_sheet.pdf`)

A **2-page** PDF cheat sheet. Generate using reportlab or fpdf2.

**Page 1: Test Formulas**

A compact table with one row per test and the following columns:

| Test | Test Statistic | df | Confidence Interval | Effect Size |
|------|---------------|-----|---------------------|-------------|
| One-Sample Z-Test | z = (x̄ − μ₀) / (σ/√n) | — | x̄ ± z_(α/2) · σ/√n | d = (x̄ − μ₀) / σ |
| One-Sample T-Test | t = (x̄ − μ₀) / (s/√n) | n − 1 | x̄ ± t_(α/2,df) · s/√n | d = (x̄ − μ₀) / s |
| ... | ... | ... | ... | ... |

Include all 23 tests. Use compact notation. Mark "N/A" for CI or effect size where not applicable.

**Page 2: Decision Rules & Quick Reference**

- Generic decision rules: "Reject H₀ if |test stat| > critical value" / "Reject H₀ if p-value < α"
- One-tailed vs two-tailed: brief note on how critical values and p-values change, with a small diagram showing one tail vs two tails
- Effect size interpretation scales:
  - Cohen's d: 0.2 = small, 0.5 = medium, 0.8 = large
  - η² (eta-squared): 0.01 = small, 0.06 = medium, 0.14 = large
  - r² (coefficient of determination): 0.01 = small, 0.09 = medium, 0.25 = large
  - Cramér's V: depends on df (include a small lookup grid)
  - Cohen's w: 0.1 = small, 0.3 = medium, 0.5 = large
  - Cohen's h: 0.2 = small, 0.5 = medium, 0.8 = large
- Common α values and corresponding z-critical values: α=0.10→1.645, α=0.05→1.960, α=0.01→2.576 (two-tailed) and α=0.10→1.282, α=0.05→1.645, α=0.01→2.326 (one-tailed)
- Type I vs Type II error summary: "Type I = false positive (reject a true H₀), probability = α. Type II = false negative (fail to reject a false H₀), probability = β. Power = 1 − β."
- Assumption checklist per test category:
  - t-tests: random sample, normality (or large n), independence
  - Chi-square: random sample, independence, expected counts ≥ 5
  - ANOVA: random sample, normality within groups, equal variances (homogeneity), independence
  - Nonparametric: random sample, independence (+ symmetry for Wilcoxon)
  - Regression: linearity, independence, normality of residuals, constant variance (homoscedasticity)

Design requirements:
- Page size: Letter (8.5 × 11 in), **landscape** orientation for maximum space
- Font: 8–9pt body to fit everything, 12pt title
- Dense but readable layout — use thin borders and alternating row shading
- Title: "Hypothesis Testing Formula Sheet — Quick Reference"
- Footer: page number + "Undergraduate Statistics"

### 3. Master Critical Value Tables (`supplementary/master_critical_value_tables.pdf`)

A multi-page PDF containing full statistical tables. Generate using reportlab or fpdf2. **Use scipy.stats to compute all values programmatically — do not hardcode.**

**Include these tables:**

1. **Standard Normal (Z) Table** — cumulative probabilities P(Z ≤ z) from z = −3.49 to z = 3.49 in increments of 0.01. Use the standard textbook format: rows = z value to tenths place (−3.4, −3.3, ..., 0.0, ..., 3.4), columns = hundredths place (0.00, 0.01, ..., 0.09). This will span 2–3 pages.

2. **Student's t Distribution Critical Values** — for df = 1 to 40 (by 1), then 50, 60, 80, 100, 120, ∞. Columns for common right-tail areas: 0.100, 0.050, 0.025, 0.010, 0.005. Compute using `scipy.stats.t.ppf(1 - alpha, df)`.

3. **Chi-Square Distribution Critical Values** — for df = 1 to 30 (by 1), then 40, 50, 60, 80, 100. Columns for right-tail areas: 0.100, 0.050, 0.025, 0.010, 0.005. Compute using `scipy.stats.chi2.ppf(1 - alpha, df)`.

4. **F Distribution Critical Values at α = 0.05** — Rows: denominator df (1, 2, 3, ..., 30, 40, 60, 120, ∞). Columns: numerator df (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 20, 24, 30, 40, 60, 120, ∞). Compute using `scipy.stats.f.ppf(1 - 0.05, dfn, dfd)`. This may need landscape orientation.

5. **F Distribution Critical Values at α = 0.01** — Same structure as above but for α = 0.01.

Design requirements:
- Page size: Letter; portrait for z/t/chi-square tables, landscape for F tables
- Title on each page identifying the table and the α level
- Clear row/column headers with sufficient spacing
- Font: 8–9pt monospace or tabular for the numbers, bold headers
- Round all values to 3 decimal places
- Page numbers in footer
- First page: a brief "How to Use These Tables" guide (2–3 sentences per table type)

---

## Style & Tone

- **Textbook-formal but simple.** Write as if the reader is an undergraduate seeing the material for the first time.
- **Never skip steps.** Every intermediate calculation must be shown explicitly.
- **Define everything.** If you use a symbol, define it. If you use a term, explain it.
- **Realistic examples.** Use scenarios students can relate to: exam scores, heights, reaction times, customer counts, medical outcomes, etc.
- **Consistent notation.** Use the same symbols across all topics (μ for population mean, x̄ for sample mean, s for sample std dev, σ for population std dev, n for sample size, α for significance level, p for p-value).
- **No duplicate scenarios.** Each topic's worked example, Question 1, and Question 2 must all use different real-world contexts. Additionally, avoid reusing the same scenario across different topics where possible — if the one-sample z-test uses "exam scores at a university," the one-sample t-test should use a different context like "battery lifespans" or "reaction times."

---

## Technical Instructions

### Excel Files (openpyxl)
- Font: Arial 11pt body, 12pt headers (bold, white text on #2F5496 fill)
- Subheadings: Arial 11pt bold, colour #2F5496
- Borders: thin borders on all data cells
- Column widths: set explicitly (no auto-fit relying on content)
- Highlighted cells: yellow fill (#FFF2CC) for key results (test statistic, decision, CI, effect size)
- Light blue fill (#D6E4F0) for row/column labels in data tables
- Green fill (#E2EFDA) for expected frequency tables in chi-square topics
- Wrap text enabled on all cells containing long text (definitions, conclusions)
- Row heights: set explicitly for rows with wrapped text (estimate ~16px per line)
- Use Excel formulas (`=SUM(...)`, `=(C5-D5)^2/D5`, etc.) — NOT hardcoded Python-computed values
- After creating each .xlsx, recalculate formulas using `scripts/recalc.py` and verify zero errors
- If recalc.py reports errors, fix them and recalculate again before committing

### PDF Files (reportlab or fpdf2)
- Page size: Letter (8.5 × 11 in) unless stated otherwise
- Margins: 1 inch all sides
- Body font: 11pt Helvetica or Times
- Headings: 14pt bold
- Include page numbers in footer
- Formulas in-line using Unicode characters (not LaTeX)
- For the "See Also" section, use the related test names as they appear in the cross-reference map

### PPTX Files (python-pptx)
- Slide size: Widescreen (13.333 × 7.5 in)
- Title font: 28–32pt bold
- Body font: 20–24pt
- Use a consistent colour scheme: dark blue (#2F5496) for headings, black for body text
- No excessive animations or transitions

### Python Bonus Files
- Shebang line: none needed
- Encoding: UTF-8
- Max line length: 90 characters
- Import block at top
- Sections separated by comment banners (`# === SECTION NAME ===`)
- All print output should be clearly labelled and formatted
- Verify that the script runs without errors before committing

---

## Workflow per Topic

```
1. Create the topic folder: mkdir -p <topic_name>/
2. Generate <topic>.xlsx           (notes + worked example, with CI + effect size + Type I/II errors + See Also)
3. Generate <topic>_notes.pdf      (PDF version of the notes, with all the same sections)
4. Generate <topic>.pptx           (lecture slides, 10–14 slides)
5. Generate <topic>_questions.xlsx (2 practice questions: Q1 two-tailed, Q2 one-tailed)
6. Generate <topic>_answers.xlsx   (full worked answers, all 11 steps including CI + effect size + Type I/II errors)
7. Generate <topic>_bonus.py       (Python demonstrations with CI + effect size + plots)
8. Run the bonus .py to verify it executes without errors
9. Recalculate all .xlsx files using scripts/recalc.py and verify zero formula errors
10. git add <topic_name>/
11. git commit -m "feat: add <topic_name> materials"
```

---

## After All 23 Topics Are Complete

### Step 1: Generate Supplementary Materials

```
1. mkdir -p supplementary/
2. Generate supplementary/test_selection_flowchart.pdf
3. Generate supplementary/master_formula_sheet.pdf
4. Generate supplementary/master_critical_value_tables.pdf
5. git add supplementary/
6. git commit -m "feat: add supplementary reference materials"
```

### Step 2: Update README.md

Update `README.md` with a full table of contents:

```markdown
# Stats — Undergraduate Statistics Lecture Materials

## Hypothesis Tests

| # | Topic | Excel | PDF Notes | Slides | Questions | Answers | Python |
|---|-------|-------|-----------|--------|-----------|---------|--------|
| 1 | One-Sample Z-Test | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 2 | One-Sample T-Test | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| ... | ... | ... | ... | ... | ... | ... | ... |
| 23 | F-Test for Two Variances | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

## Supplementary Materials

| File | Description |
|------|-------------|
| [Test Selection Flowchart](supplementary/test_selection_flowchart.pdf) | Decision tree: which test should I use? |
| [Master Formula Sheet](supplementary/master_formula_sheet.pdf) | 2-page cheat sheet of all formulas, CIs, and effect sizes |
| [Critical Value Tables](supplementary/master_critical_value_tables.pdf) | Full z, t, χ², and F tables |
```

Commit with message: `docs: update README with full topic index and supplementary materials`.

---

## Handling Pre-Existing Files

If any files already exist in this repo from earlier work:

1. **Check if they match the new 6-file structure.** If a topic has a combined notes+questions .xlsx, split it into separate `<topic>.xlsx` (notes only) and `<topic>_questions.xlsx` (questions only).
2. **Rename files** to match the naming conventions above.
3. **Move files** into the correct topic folder using `git mv`.
4. **Generate any missing files** for that topic (e.g., if the PDF or slides don't exist yet, create them).
5. **Do not regenerate files that already exist and are correct** — only fill in gaps.
6. **Verify all existing Excel files** have zero formula errors after moving.

---

## Important Reminders

- **Questions and answers are ALWAYS separate files.** Students get the questions file; the answers file is for self-checking or instructor use.
- **PDF notes are a print-friendly version of the Excel notes content.** They exist so students can read the material without needing Excel.
- **Every file must be self-contained.** A student should be able to open any single file and have it make sense without needing the others.
- **Accuracy is critical.** Double-check every formula, every critical value lookup, every p-value. Cross-verify hand calculations against scipy output in the bonus Python file.
- **Do not create placeholder or empty files.** Every file must be complete and usable.
- **Confidence intervals and effect sizes are mandatory** in every worked example and answer — not optional.
- **Type I and Type II errors must be context-specific** — never use generic boilerplate language. Tailor them to the scenario in each worked example and each practice question.
- **One-tailed tests must be demonstrated** — Question 2 for every topic is one-tailed, with the answer explicitly explaining how the critical value and p-value differ from the two-tailed case.
- **Cross-references must be included** in every Notes sheet, PDF, and final slide — use the cross-reference map above.
- **Supplementary materials are generated last**, after all 23 topic folders are complete.
