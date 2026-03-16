# Hypothesis Testing Template Library

Use these starter files whenever you spin up a new hypothesis-testing topic. Each template already reflects the repo formatting, accessibility defaults, and naming conventions outlined in `CLAUDE.md`.

## Files
- `topic_template.xlsx` — Excel workbook scaffold (Notes, Worked Example, Practice 1, Practice 2 sheets).
- `howto_template.md` — Markdown source for the "How-To" PDF (assumptions + procedure).
- `worked_examples_template.md` — Markdown source for multi-step worked examples.
- `practice_set_template.md` — Markdown source for practice problems with solution section at the end.
- `confidence_interval_notes_template.md` — Markdown source for CI-specific notes.
- `topic_master.pptx` — Slide master with approved fonts/colors/layouts.
- `topic_bonus.py` — Python skeleton for the bonus script.

## Usage
1. Copy the relevant template into your topic folder (e.g., `cp templates/topic_template.xlsx hypothesis_testing/one_sample_t_test/excel/`).
2. Rename the copy to match the topic (e.g., `one_sample_t_test.xlsx`).
3. Fill in the placeholders, following the inline comments for required sections.
4. When exporting Markdown → PDF, run `pandoc <file>.md -o <file>.pdf --pdf-engine=xelatex --metadata=title:"..."` (or your preferred tool) and ensure tagged-PDF output is enabled.
5. For slides, open `topic_master.pptx`, choose "Save As", and start editing the duplicate.
6. Keep the templates pristine—never edit them directly; update the source here if the standard changes.

## Fonts & Colors
- Body text: Calibri or Arial, 12 pt minimum in PDFs, 18 pt minimum on slides.
- Heading text: Calibri Light or Arial Bold, 16 pt+ (PDF) / 28 pt+ (slides).
- Primary color palette (Meets WCAG AA):
  - Dark Navy `#0B1D3A`
  - Teal `#14B8A6`
  - Accent Blue `#1C7293`
  - Slate `#334155`
- Do not introduce new colors unless you verify contrast at contrast-ratio.com.

## Accessibility Reminders
- Provide alt-text for every figure/table placeholder in Markdown and slides.
- Use semantic headings in Markdown (H1–H3) so tagged PDFs inherit correct structure.
- In Excel, keep header rows marked as "Print Titles" and avoid color-only cues.
- In slides, include presenter notes summarizing visuals for screen-reader exports.

## Automation (optional)
A helper script (`scripts/new_topic.py`) can copy these templates automatically. Run `python scripts/new_topic.py --topic two_sample_t_test_equal_var` to scaffold the directories/files; edit the script if we add new template files.
