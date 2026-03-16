#!/usr/bin/env python3
"""Minimal Markdown-to-PDF converter using fpdf."""
from __future__ import annotations

import argparse
import textwrap
from pathlib import Path

from fpdf import FPDF
from fpdf.errors import FPDFException
import textwrap

FONT_PATH = Path("/System/Library/Fonts/Supplemental/Arial Unicode.ttf")
FONT_NAME = "ArialUnicode"


def write_safe(pdf: FPDF, text: str, line_height: float = 6) -> None:
    for chunk in textwrap.wrap(text, width=60, break_long_words=True, break_on_hyphens=True):
        try:
            pdf.multi_cell(0, line_height, chunk)
        except FPDFException:
            for ch in chunk:
                if pdf.get_x() > pdf.w - pdf.r_margin - 4:
                    pdf.ln(line_height)
                pdf.cell(4, line_height, ch, border=0)
            pdf.ln(line_height)


def render_markdown(md_path: Path, pdf_path: Path) -> None:
    text = md_path.read_text(encoding="utf-8").splitlines()
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    if FONT_PATH.exists():
        pdf.add_font(FONT_NAME, "", str(FONT_PATH), uni=True)
        default_font = (FONT_NAME, "", 12)
    else:
        default_font = ("Helvetica", "", 12)
    pdf.set_font(*default_font)

    idx = 0
    if text and text[0].strip() == "---":
        idx += 1
        while idx < len(text) and text[idx].strip() != "---":
            idx += 1
        idx += 1  # skip closing ---

    while idx < len(text):
        line = text[idx]
        idx += 1
        stripped = line.strip()

        if not stripped:
            pdf.ln(5)
            continue

        if stripped.startswith("#"):
            level = len(stripped) - len(stripped.lstrip("#"))
            content = stripped[level:].strip()
            size = {1: 18, 2: 16, 3: 14}.get(level, 12)
            pdf.set_font(default_font[0], "", size)
            write_safe(pdf, content, line_height=8)
            pdf.ln(2)
            pdf.set_font(*default_font)
            continue

        if stripped.startswith(">"):
            content = stripped.lstrip(">").strip()
            pdf.set_font(default_font[0], "", 12)
            write_safe(pdf, content)
            pdf.set_font(*default_font)
            continue

        if stripped.startswith(('- ', '* ')):
            content = stripped[2:].strip()
            pdf.set_x(pdf.l_margin + 5)
            write_safe(pdf, f"- {content}")
            continue

        if stripped.split('.', 1)[0].isdigit():
            parts = stripped.split('.', 1)
            text = f"{parts[0].strip()}. {parts[1].strip() if len(parts) > 1 else ''}".strip()
            write_safe(pdf, text)
            continue

        if stripped.startswith('|') and stripped.endswith('|'):
            cells = [c.strip() for c in stripped.strip('|').split('|')]
            for cell in cells:
                write_safe(pdf, cell, line_height=5)
            pdf.ln(1)
            continue

        write_safe(pdf, stripped)

    pdf.output(str(pdf_path))


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert Markdown files to PDF")
    parser.add_argument("sources", nargs="+", help="Markdown files to convert")
    args = parser.parse_args()

    for src in args.sources:
        md_path = Path(src)
        if not md_path.exists():
            print(f"Skipping missing {md_path}")
            continue
        pdf_path = md_path.with_suffix('.pdf')
        render_markdown(md_path, pdf_path)
        print(f"Wrote {pdf_path}")


if __name__ == "__main__":
    main()
