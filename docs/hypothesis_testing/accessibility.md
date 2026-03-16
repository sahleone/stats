# Hypothesis Testing Accessibility Checklist

Use this checklist before shipping any new materials (Excel, PDF, slides, Python output).

## Universal
- Text size ≥ 12 pt in PDFs, ≥ 18 pt on slides.
- Use approved color palette (see `templates/README.md`); verify contrast ratio ≥ 4.5:1 for body text.
- Provide descriptive alt-text for every figure, table, and chart.
- Headings follow a logical structure (H1 → H2 → H3) so tagged PDFs remain navigable.
- Avoid conveying information by color alone; pair with labels or patterns.

## Excel Workbooks
- Ensure header rows use Excel's "Format as Table" or bold text; enable "Repeat Header Rows" for printing.
- Name sheets descriptively (`Notes`, `Worked_Example`, `Practice_1`, etc.).
- Include text annotations for charts and shapes; right-click → "Alt Text".
- Keep formulas visible (no hard-coded values unless necessary).
- Tab order should move left-to-right, top-to-bottom.

## PDFs from Markdown/LaTeX
- Export using tagged-PDF option (`pandoc --pdf-engine=xelatex --metadata=lang=en`).
- Include document title/author metadata.
- Provide captions + alt-text for visual elements.
- For multi-column layouts, ensure reading order is linear (avoid multiple columns if possible).

## Slide Decks
- Use slide layouts from `templates/topic_master.pptx` only.
- Keep minimum 28 pt for headings, 18 pt for bullets.
- Ensure sufficient contrast between text and background.
- Add speaker notes describing charts/graphics for screen-reader exports.
- Check "Accessibility" pane in PowerPoint (Review → Check Accessibility) before saving.

## Python Scripts / Console Output
- When printing results, use clear text labels (no reliance on color). Provide context sentences for Type I/II errors, CI interpretation, etc.

Run through this list for every deliverable; note any exceptions in commit messages or documentation.
