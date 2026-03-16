# Hypothesis Testing Asset Guide & Decision Options

## Scope & Context
- Audience: MA235 Week 12–13 students transitioning from normal distribution review to formal hypothesis testing and the class project’s two-sample t-test deliverable.
- Goal: consolidate all legacy materials (Word/PDF homework, lecture notes, project instructions, slides) into a repo-tracked reference so we can decide whether to reuse, refresh, or fully rebuild assets that match the `CLAUDE.md` 6-file-per-topic standard.
- Inputs: Seven instructor-provided files that currently live outside the repo plus the two in-repo slide decks inside `hypothesis_testing/`. Quick text extractions live in `docs/hypothesis_testing/snippets/` for reference.

## Asset Inventory
| Asset | Current Location | Format | Coverage Snapshot | Issues / Gaps | Recommended Action |
| --- | --- | --- | --- | --- | --- |
| Week 12 lecture notes | `/Users/rhysjervis/Downloads/MA_235-44_stat_week_12.doc` | Word (`.doc`) | Introduces non-standard normal distribution, z-score workflow, and how to identify null vs research hypotheses. | Broken equation placeholders (“EMBED Equation”), references to textbook page numbers, no visuals, no alignment with repo formatting. | Pull concepts into modern `_notes.pdf` + Excel workbook; retire the `.doc` once migrated.
| Week 13 lecture notes | `/Users/rhysjervis/Downloads/MA_235-44_stat_week_13.doc` | Word (`.doc`) | Full text walkthrough of hypothesis test steps (claim → critical regions → z-formula) with HyperStat links. | Heavy reliance on external images/links, z-focus only (no t-tests), still uses “Do not reject” phrasing. | Convert to structured repo notes; replace external images with internal figures; broaden to two-sample t-test context.
| Week 12 homework prompt | `/Users/rhysjervis/Downloads/MA235 Week 12 HW.docx` | Word (`.docx`) | One-line instruction referencing Triola Section 9.1 #11a/#17/#21. | Requires textbook for problems, no rubric/solutions, not in Excel question bank format. | Rebuild as `hypothesis_testing_questions.xlsx` + `..._answers.xlsx` with embedded prompts so repo is self-contained.
| Hypothesis testing step checklist | `/Users/rhysjervis/Downloads/MA235_Hypothesis_Testing step 1.docx` | Word (`.docx`) | Plain-language mapping between claims and the correct H0/H1 pairing. | Duplicates Week 13 content, references missing “key words” file, lacks visuals/examples. | Integrate as “Key Words” sidebar/worksheet in repo; then archive the standalone doc.
| Project hypothesis test guidance | `/Users/rhysjervis/Downloads/MA235 Project hypothesis test guidance.docx` | Word (`.docx`) | Explains the MA235 project expectations: two groups, α = 0.05, pooled SE, critical value lookup, contextual conclusion text. | No mention of descriptive statistics, graphs, or deliverable format; formula placeholders not typeset. | Summarize in this guide and plan a dedicated `project_guidance.md` (future) with rubrics/examples.
| Chapter 8 slides | `/Users/rhysjervis/Downloads/MA235_PPT_ch08-1.pdf` | PDF (Triola ch. 8) | Pearson slides covering hypothesis definitions, Rare Event Rule, Gender Choice example, Section 8-2 components. | Outdated branding, example uses proportions instead of class project focus, not customizable. | Treat as conceptual background only; do not ship as-is. Pull only evergreen explanations.
| Hypothesis testing definitions sheet | `/Users/rhysjervis/Downloads/MA235_Stats_HypTstg_Definition.pdf` | PDF handout | One-page glossary defining H0, H1, α, β, Type I/II errors, decisions, conclusions. | Typo numbering (“6” repeated), lacks repo styling, not linked anywhere. | Recreate as part of `_notes.pdf` appendix or `supplementary/master_formula_sheet.pdf` addendum.
| Hypothesis Testing slides | `hypothesis_testing/hypothesis_testing.pptx` | PowerPoint | 8-slide overview tailored to MA235 project (H0/H1, α=.05, df=28, workflow). | No accompanying notes PDF, Excel, or exercises; uses single example. | Keep as baseline but update assets to match 6-file format and embed results chart. 
| Hypothesis Testing Q&A slides | `hypothesis_testing/hypothesis_testing_qa.pptx` | PowerPoint | 22-slide multiple-choice review with answers/explanations for α, errors, df, CI, randomness. | Also lacks supporting worksheets/notes; question order assumes live facilitation. | Convert into practice questions sheet + interactive PPT, aligning question numbers with new workbook.

### Observations & Overlaps
- Weeks 12–13 `.doc` files plus the Step 1 checklist repeat the same hypothesis identification rules; consolidating into a single repo module removes redundancy.
- The project guidance doc, in-repo PPT, and Q&A deck all assume the two-sample t-test with n=15 per group; other files still emphasize single-sample z-tests, so messaging is inconsistent.
- Homework instructions currently depend on textbook problems rather than repo-owned scenarios, making distribution difficult for students without the book.

## Gap Analysis vs 6-File Topic Structure
| Required Deliverable | Exists? | Notes |
| --- | --- | --- |
| `<topic>.xlsx` (notes workbook) | ✗ | No Excel workbook for hypothesis testing content; only the Chi-Square/ANOVA topics have built workbooks.
| `<topic>_notes.pdf` | ✗ | Legacy Word/PDF files are not in the modern layout; we need a compliant PDF derived from new workbook/PDF pipeline.
| `<topic>.pptx` | ✔️ | Core PPT exists but lacks speaker notes/consistency with new visuals. Needs refresh once notes are rebuilt.
| `<topic>_questions.xlsx` | ✗ | Homework references textbook problems only; we must author original repo questions with answers.
| `<topic>_answers.xlsx` | ✗ | Same as above—no worked answers in repo format.
| `<topic>_bonus.py` | ✗ | No Python script demonstrating the MA235 project t-test workflow.

**Implication:** Even with the two PPT decks, this topic is effectively “not built” per `CLAUDE.md`. We have subject-matter content but need to migrate it into the standardized pipeline.

## Decision Options (When to Build New Notes & Slides)
### Option 1 — Reuse & Annotate Legacy Files
- **Scope:** Keep existing PPT decks, attach PDFs of Week 12/13 notes plus the definition sheet as interim references.
- **Effort:** Low (1–2 days) to clean typos and hyperlink resources.
- **Pros:** Fastest path, minimal tooling.
- **Cons:** Fails repo standards; `.doc` files remain outside version control, inconsistent terminology (z-test vs t-test), no practice set.
- **Use when:** Need a stopgap for immediate teaching with no time for rebuild.

### Option 2 — Hybrid Refresh (Recommended)
- **Scope:** Modernize narrative content (notes PDF + workbook + glossary) while keeping existing PPT decks, and create question/answer Excel pairs derived from the Q&A prompts.
- **Effort:** Medium (3–4 builder passes) leveraging existing text plus repo templates.
- **Pros:** Aligns with 6-file structure except bonus Python; reuses current slides; students get self-contained practice assets.
- **Cons:** PPT visuals may still need updates later; project guidance remains in Markdown (not a formatted PDF) unless extended.
- **Use when:** You have time to rebuild textual/worksheet material now and defer slide polish/code automation to a later sprint.

### Option 3 — Full Rebuild
- **Scope:** Regenerate all six deliverables (Excel, PDF notes, Slides, Questions, Answers, Bonus Python) plus a new `project_guidance.md`, re-deriving examples from MA235 datasets.
- **Effort:** High (multi-week) but produces a completely standardized topic ready for automated builds.
- **Pros:** One source of truth, integrated with build scripts, ready for future semesters.
- **Cons:** Requires substantial authoring + tooling time.
- **Use when:** You want Hypothesis Testing to match the maturity of ANOVA topics before the next term.

## Project Guidance Summary (from legacy docs)
1. **Define groups:** Clearly state which designation is Group 1 vs Group 2 (parents vs non-parents, etc.). Document sampling process to justify randomness.
2. **State hypotheses:** Use H0: μ₁ = μ₂ vs H1: μ₁ ≠ μ₂ (two-tailed). Always include equality in H0.
3. **Estimate variability:** Compute each sample’s standard deviation, then pooled/combined standard error since σ is unknown.
4. **Compute t-statistic:** \( t = \frac{\bar{x}_1 - \bar{x}_2}{\sqrt{s_1^2/n_1 + s_2^2/n_2}} \) with n₁ = n₂ = 15.
5. **Critical value:** df ≈ n₁ + n₂ − 2 = 28; with α = 0.05 (two-tailed), t* ≈ ±2.048. Round df up if using conservative tables.
6. **Decision rule:** Reject H0 if |t| > t*; otherwise fail to reject. Never say “accept H0.”
7. **Conclusion template:** “At the 5% significance level, the sample data (do/do not) provide sufficient evidence to conclude that [plain-English claim].” Mention the computed t, df, and effect direction.
8. **Confidence intervals:** (From PPT Q&A) pair the hypothesis test with a 90% CI for each group mean to discuss estimation precision.

_TODO:_ Create a dedicated `project_guidance.md` later with dataset expectations, descriptive statistics checklist (mean/median/mode/SD), visualization requirements, and grading rubric.

## Reusable Repo Materials & Cross-Links
- `normal_distribution/normal_distribution_notes.pdf` and workbook already explain z-scores and Table A-2 usage—link these as prerequisites for Week 12 refresh.
- `two_sample_t_test_equal_var/` and `welchs_t_test/` folders (currently empty placeholders) will share formulas/examples with this module; coordinate examples to avoid duplicating effort.
- Supplementary PDFs (test selection flowchart, master formula sheet) can host the hypothesis glossary currently living in `MA235_Stats_HypTstg_Definition.pdf`.
- Scripts in `scripts/topic_registry.py` already define effect sizes, CI formulas, and “See Also” lists—reuse that metadata in the rebuilt workbook/notes.

## Next Checks Before Implementation
1. Confirm we can legally distribute/problem statements replacing textbook homework (create new contexts if needed).
2. Decide whether to import any figures from Chapter 8 slides or redraw in repo style.
3. Schedule build tasks: Excel first, then notes PDF + PPT, then questions/answers, finally bonus Python.
4. When assets are rebuilt, remove references to external Downloads in this guide to keep the repo self-contained.

_Run `rg 'MA235' docs/hypothesis_testing/ASSET_PLAN.md` after edits to ensure each provided file is referenced by name._
