# Stats — Undergraduate Statistics Lecture Materials

## Hypothesis Tests

| # | Topic | Excel | PDF Notes | Slides | Questions | Answers | Python |
|---|-------|-------|-----------|--------|-----------|---------|--------|
| 1 | One-Sample Z-Test | - | - | - | - | - | - |
| 2 | One-Sample T-Test | - | - | - | - | - | - |
| 3 | One-Sample Proportion Z-Test | - | - | - | - | - | - |
| 4 | Two-Sample Z-Test | - | - | - | - | - | - |
| 5 | Two-Sample T-Test (Equal Var) | - | - | - | - | - | - |
| 6 | Welch's T-Test | - | - | - | - | - | - |
| 7 | Paired T-Test | - | - | - | - | - | - |
| 8 | Two-Proportion Z-Test | - | - | - | - | - | - |
| 9 | Chi-Square Goodness-of-Fit | :white_check_mark: | - | - | - | :white_check_mark: | :white_check_mark: |
| 10 | Chi-Square Independence | :white_check_mark: | - | - | - | :white_check_mark: | :white_check_mark: |
| 11 | Fisher's Exact Test | - | - | - | - | - | - |
| 12 | Shapiro-Wilk Test | - | - | - | - | - | - |
| 13 | One-Way ANOVA | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| 14 | Two-Way ANOVA | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| 15 | Sign Test | - | - | - | - | - | - |
| 16 | Wilcoxon Signed-Rank | - | - | - | - | - | - |
| 17 | Mann-Whitney U | - | - | - | - | - | - |
| 18 | Kruskal-Wallis | - | - | - | - | - | - |
| 19 | Correlation T-Test | - | - | - | - | - | - |
| 20 | Regression Slope T-Test | - | - | - | - | - | - |
| 21 | Regression F-Test | - | - | - | - | - | - |
| 22 | Chi-Square Variance | - | - | - | - | - | - |
| 23 | F-Test Two Variances | - | - | - | - | - | - |

## Foundational Topics

| Topic | Excel | PDF Notes | Slides | Questions | Answers | Python |
|-------|-------|-----------|--------|-----------|---------|--------|
| Normal Distribution | :white_check_mark: | :white_check_mark: | - | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| Random Variables | :white_check_mark: | :white_check_mark: | - | :white_check_mark: | :white_check_mark: | :white_check_mark: |

## Supplementary Materials

| File | Description |
|------|-------------|
| [Test Selection Flowchart](supplementary/test_selection_flowchart.pdf) | Decision tree: which test should I use? |
| [Master Formula Sheet](supplementary/master_formula_sheet.pdf) | 2-page cheat sheet of all formulas, CIs, and effect sizes |
| [Critical Value Tables](supplementary/master_critical_value_tables.pdf) | Full z, t, chi-square, and F tables |

## Pre-Existing Materials

These files predate the 6-file-per-topic structure and will be migrated as topics are built.

| Folder | File | Description |
|--------|------|-------------|
| chi_square | `chi_square_answer_key.docx` | Answer key (legacy) |
| chi_square | `chi_square_detailed_examples.docx` | Detailed examples (legacy) |
| chi_square | `chi_square_practice_questions.docx` | Practice questions (legacy) |
| contingency_tables | `contingency_tables.pptx` | Contingency tables slides |
| contingency_tables | `contingency_tables.pdf` | Contingency tables reference |
| hypothesis_testing | `hypothesis_testing.pptx` | Hypothesis testing overview slides |
| hypothesis_testing | `hypothesis_testing_qa.pptx` | Hypothesis testing Q&A slides |
| normal_clt | `normal_clt.pptx` | Normal distribution and CLT slides |

## Build Scripts

| Script | Description |
|--------|-------------|
| `scripts/build_all.py` | Orchestrator for building topic materials |
| `scripts/build_supplementary.py` | Generates supplementary PDFs |
| `scripts/topic_registry.py` | Central registry of all 23 topics with metadata |
| `scripts/excel_styles.py` | Shared Excel formatting helpers |
| `scripts/pdf_styles.py` | Shared PDF formatting helpers |
| `scripts/pptx_styles.py` | Shared PowerPoint formatting helpers |
| `scripts/recalc.py` | Excel formula recalculation |
| `scripts/verify.py` | Verification script |
| `scripts/soffice.py` | LibreOffice helper |
| `scripts/setup.sh` | Environment setup |
| `scripts/requirements.txt` | Python dependencies |

### Quick Start

```bash
bash scripts/setup.sh                          # Install dependencies
python scripts/build_all.py --status           # Show build progress
python scripts/build_all.py --topic <name>     # Build one topic
python scripts/build_all.py --verify all       # Verify all files
```
