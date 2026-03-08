"""
pdf_styles.py — Shared PDF formatting helpers using fpdf2.

Provides a pre-configured StatsNotesPDF class that handles page layout,
headers, footers, consistent fonts, and common section patterns used
across all 23 topic PDFs.

Usage:
    from scripts.pdf_styles import StatsNotesPDF

    pdf = StatsNotesPDF(title="One-Sample Z-Test")
    pdf.add_page()
    pdf.write_section("Definition", "The one-sample z-test...")
    pdf.write_formula("z = (x̄ − μ₀) / (σ / √n)")
    pdf.write_worked_step(1, "State the Hypotheses", "H₀: μ = 72 ...")
    pdf.output("one_sample_z_test_notes.pdf")
"""

from fpdf import FPDF
import os

# Unicode font paths
FONT_DIR = "/usr/share/fonts/truetype/dejavu"
FONT_REGULAR = os.path.join(FONT_DIR, "DejaVuSans.ttf")
FONT_BOLD = os.path.join(FONT_DIR, "DejaVuSans-Bold.ttf")
FONT_ITALIC = os.path.join(FONT_DIR, "DejaVuSans-Oblique.ttf")
FONT_MONO = os.path.join(FONT_DIR, "DejaVuSansMono.ttf")


class StatsNotesPDF(FPDF):
    """Pre-configured PDF class for stats lecture notes."""

    def __init__(self, title="Hypothesis Test Notes", **kwargs):
        super().__init__(orientation='P', unit='mm', format='Letter', **kwargs)
        self.doc_title = title
        self.set_auto_page_break(auto=True, margin=25)
        self.set_margins(25.4, 25.4, 25.4)  # 1 inch = 25.4mm
        # Register Unicode fonts
        self.F = "Helvetica"
        self.FM = "Courier"
        if os.path.exists(FONT_REGULAR):
            self.add_font("DejaVu", "", FONT_REGULAR)
            self.add_font("DejaVu", "B", FONT_BOLD)
            self.add_font("DejaVu", "I", FONT_ITALIC)
            if os.path.exists(FONT_MONO):
                self.add_font("DejaVuMono", "", FONT_MONO)
            self.F = "DejaVu"
            self.FM = "DejaVuMono"
        self.add_page()
        self._write_title()

    # ---- Header / Footer ----

    def header(self):
        if self.page_no() > 1:
            self.set_font(self.F, 'I', 9)
            self.set_text_color(128, 128, 128)
            self.cell(0, 8, self.doc_title, align='L')
            self.ln(4)
            self.set_draw_color(200, 200, 200)
            self.line(25.4, self.get_y(), self.w - 25.4, self.get_y())
            self.ln(4)

    def footer(self):
        self.set_y(-20)
        self.set_font(self.F, 'I', 9)
        self.set_text_color(128, 128, 128)
        self.set_draw_color(200, 200, 200)
        self.line(25.4, self.get_y(), self.w - 25.4, self.get_y())
        self.ln(2)
        self.cell(0, 8, f'Undergraduate Statistics', align='L')
        self.cell(0, 8, f'Page {self.page_no()}', align='R')

    # ---- Title ----

    def _write_title(self):
        self.set_font(self.F, 'B', 20)
        self.set_text_color(47, 84, 150)
        self.cell(0, 14, self.doc_title, new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(47, 84, 150)
        self.line(25.4, self.get_y(), self.w - 25.4, self.get_y())
        self.ln(8)

    # ---- Section Helpers ----

    def write_section(self, heading, body):
        """Write a section heading followed by body text."""
        self._check_space(30)
        self.set_font(self.F, 'B', 14)
        self.set_text_color(47, 84, 150)
        self.cell(0, 9, heading, new_x="LMARGIN", new_y="NEXT")
        self.ln(2)
        self.set_font(self.F, '', 11)
        self.set_text_color(0, 0, 0)
        self.multi_cell(0, 6, body)
        self.ln(4)

    def write_subsection(self, heading, body):
        """Write a subsection heading followed by body text."""
        self._check_space(25)
        self.set_font(self.F, 'B', 12)
        self.set_text_color(47, 84, 150)
        self.cell(0, 8, heading, new_x="LMARGIN", new_y="NEXT")
        self.ln(1)
        self.set_font(self.F, '', 11)
        self.set_text_color(0, 0, 0)
        self.multi_cell(0, 6, body)
        self.ln(3)

    def write_formula(self, formula_text, label=None):
        """Write a formula in a shaded box."""
        self._check_space(20)
        if label:
            self.set_font(self.F, 'B', 11)
            self.set_text_color(47, 84, 150)
            self.cell(0, 7, label, new_x="LMARGIN", new_y="NEXT")
            self.ln(1)

        x = self.get_x()
        y = self.get_y()
        box_w = self.w - 2 * 25.4
        self.set_fill_color(242, 242, 242)
        self.set_font(self.FM, '', 11)
        self.set_text_color(0, 0, 0)

        # Calculate height needed
        lines = formula_text.split('\n')
        box_h = max(12, len(lines) * 7 + 6)

        self.rect(x, y, box_w, box_h, 'F')
        self.set_xy(x + 4, y + 3)
        for i, line in enumerate(lines):
            self.cell(0, 7, line, new_x="LMARGIN", new_y="NEXT")
            if i < len(lines) - 1:
                self.set_x(x + 4)

        self.set_y(y + box_h + 4)
        self.set_font(self.F, '', 11)

    def write_worked_step(self, step_num, title, body):
        """Write a numbered step in a worked example."""
        self._check_space(20)
        self.set_font(self.F, 'B', 11)
        self.set_text_color(47, 84, 150)
        self.cell(0, 7, f"Step {step_num}: {title}", new_x="LMARGIN", new_y="NEXT")
        self.ln(1)
        self.set_font(self.F, '', 11)
        self.set_text_color(0, 0, 0)
        self.multi_cell(0, 6, body)
        self.ln(3)

    def write_definition_list(self, items):
        """
        Write a list of defined terms.
        items: list of (term, definition) tuples.
        """
        self._check_space(15)
        for term, definition in items:
            self.set_font(self.F, 'B', 11)
            self.set_text_color(0, 0, 0)
            self.cell(40, 7, term, new_x="END")
            self.set_font(self.F, '', 11)
            self.cell(0, 7, f"  {definition}", new_x="LMARGIN", new_y="NEXT")
        self.ln(3)

    def write_type_errors(self, type1, type2):
        """Write Type I and Type II error interpretations."""
        self._check_space(30)
        self.set_font(self.F, 'B', 14)
        self.set_text_color(47, 84, 150)
        self.cell(0, 9, "Type I and Type II Errors", new_x="LMARGIN", new_y="NEXT")
        self.ln(2)

        self.set_font(self.F, 'B', 11)
        self.set_text_color(0, 0, 0)
        self.cell(0, 7, "Type I Error (\u03b1):", new_x="LMARGIN", new_y="NEXT")
        self.set_font(self.F, '', 11)
        self.multi_cell(0, 6, type1)
        self.ln(2)

        self.set_font(self.F, 'B', 11)
        self.cell(0, 7, "Type II Error (\u03b2):", new_x="LMARGIN", new_y="NEXT")
        self.set_font(self.F, '', 11)
        self.multi_cell(0, 6, type2)
        self.ln(4)

    def write_see_also(self, references):
        """
        Write a See Also section.
        references: list of (test_name, description) tuples.
        """
        self._check_space(25)
        self.set_font(self.F, 'B', 14)
        self.set_text_color(47, 84, 150)
        self.cell(0, 9, "See Also (Related Tests)", new_x="LMARGIN", new_y="NEXT")
        self.ln(2)

        self.set_font(self.F, '', 11)
        self.set_text_color(0, 0, 0)
        for name, desc in references:
            self.set_font(self.F, 'B', 11)
            bullet = f"\u2022 {name}: "
            self.cell(self.get_string_width(bullet) + 2, 7, bullet, new_x="END")
            self.set_font(self.F, '', 11)
            self.multi_cell(0, 6, desc)
            self.ln(1)
        self.ln(3)

    def write_note_box(self, text, fill_color=(255, 243, 224)):
        """Write text in a coloured note box."""
        self._check_space(20)
        x = self.get_x()
        y = self.get_y()
        box_w = self.w - 2 * 25.4
        self.set_fill_color(*fill_color)
        self.set_font(self.F, '', 10)
        self.set_text_color(0, 0, 0)

        lines = text.split('\n')
        box_h = max(12, len(lines) * 6 + 6)

        self.rect(x, y, box_w, box_h, 'F')
        self.set_xy(x + 4, y + 3)
        for i, line in enumerate(lines):
            self.cell(0, 6, line, new_x="LMARGIN", new_y="NEXT")
            if i < len(lines) - 1:
                self.set_x(x + 4)

        self.set_y(y + box_h + 4)

    # ---- Internal ----

    def _check_space(self, needed_mm):
        """Add a new page if not enough vertical space remains."""
        if self.get_y() + needed_mm > self.h - 25:
            self.add_page()
