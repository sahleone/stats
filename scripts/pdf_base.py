"""Shared NotesPDF base class for all _notes.pdf generators."""
import os, glob
from fpdf import FPDF

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

_FONT_DIR = glob.glob(
    "/Library/Frameworks/Python.framework/Versions/*/lib/python*/site-packages/matplotlib/mpl-data/fonts/ttf"
)[0]
DEJAVU = os.path.join(_FONT_DIR, "DejaVuSans.ttf")
DEJAVU_B = os.path.join(_FONT_DIR, "DejaVuSans-Bold.ttf")

DARK_BLUE = (47, 84, 150)
BLACK = (0, 0, 0)
GRAY_BG = (240, 240, 240)
F = "DejaVu"


class NotesPDF(FPDF):
    def __init__(self):
        super().__init__("P", "mm", "Letter")
        self.add_font(F, "", DEJAVU)
        self.add_font(F, "B", DEJAVU_B)
        self.set_auto_page_break(auto=True, margin=25)
        self.add_page()
        self.set_left_margin(25.4)
        self.set_right_margin(25.4)
        self.set_top_margin(25.4)
        self.set_y(25.4)

    def header(self):
        pass

    def footer(self):
        self.set_y(-15)
        self.set_font(F, "", 9)
        self.set_text_color(100, 100, 100)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

    def add_title(self, title, subtitle):
        self.set_font(F, "B", 18)
        self.set_text_color(*DARK_BLUE)
        self.cell(0, 12, title, new_x="LMARGIN", new_y="NEXT", align="C")
        self.set_font(F, "", 12)
        self.set_text_color(100, 100, 100)
        self.cell(0, 8, subtitle, new_x="LMARGIN", new_y="NEXT", align="C")
        self.ln(4)
        self.draw_hrule()

    def section(self, title):
        if self.get_y() > 245:
            self.add_page()
        self.ln(3)
        self.draw_hrule()
        self.ln(2)
        self.set_font(F, "B", 14)
        self.set_text_color(*DARK_BLUE)
        self.multi_cell(0, 7, title)
        self.ln(2)

    def body(self, text):
        self.set_font(F, "", 11)
        self.set_text_color(*BLACK)
        self.multi_cell(0, 5.5, text)
        self.ln(2)

    def bold_body(self, text):
        self.set_font(F, "B", 11)
        self.set_text_color(*BLACK)
        self.multi_cell(0, 5.5, text)
        self.ln(1)

    def formula(self, text):
        self.set_font(F, "", 12)
        self.set_text_color(*BLACK)
        w = min(self.get_string_width(text) + 16, self.w - 2 * self.l_margin)
        x = (self.w - w) / 2
        self.set_fill_color(*GRAY_BG)
        self.set_xy(x, self.get_y())
        self.cell(w, 8, text, fill=True, align="C")
        self.ln(10)

    def bullet(self, text):
        self.set_font(F, "", 11)
        self.set_text_color(*BLACK)
        self.cell(6, 5.5, "\u2022")
        self.multi_cell(0, 5.5, text)
        self.ln(1)

    def numbered(self, num, text):
        self.set_font(F, "B", 11)
        self.set_text_color(*BLACK)
        self.cell(8, 5.5, f"{num}.")
        self.set_font(F, "", 11)
        self.multi_cell(0, 5.5, text)
        self.ln(1)

    def draw_hrule(self):
        self.set_draw_color(180, 180, 180)
        self.line(self.l_margin, self.get_y(),
                  self.w - self.r_margin, self.get_y())
        self.ln(2)

    def check_page_break(self, h=40):
        if self.get_y() + h > self.h - 25:
            self.add_page()

    def save(self, topic):
        out = os.path.join(BASE, topic, f"{topic}_notes.pdf")
        self.output(out)
        sz = os.path.getsize(out)
        print(f"  Created {topic}_notes.pdf  ({sz:,} bytes)")
        return out
