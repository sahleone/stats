#!/usr/bin/env python3
"""Scaffold hypothesis-testing topic folders from templates."""
from __future__ import annotations

import argparse
import shutil
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
TEMPLATES = REPO_ROOT / "templates"

def copy(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    print(f"Created {dst.relative_to(REPO_ROOT)}")

def main() -> None:
    parser = argparse.ArgumentParser(description="Create topic scaffold")
    parser.add_argument("--topic", required=True, help="snake_case topic folder name")
    args = parser.parse_args()

    topic_dir = REPO_ROOT / args.topic
    if topic_dir.exists():
        print(f"Topic directory {topic_dir} already exists. Continuing...")
    topic_dir.mkdir(parents=True, exist_ok=True)

    excel_dir = topic_dir / "excel"
    notes_dir = topic_dir / "notes"
    slides_dir = topic_dir / "slides"
    bonus_dir = topic_dir / "bonus"
    practice_dir = topic_dir / "practice"
    answers_dir = topic_dir / "answers"
    for d in (excel_dir, notes_dir, slides_dir, bonus_dir, practice_dir, answers_dir):
        d.mkdir(exist_ok=True)

    # Excel template
    excel_template = TEMPLATES / "topic_template.xlsx"
    if excel_template.exists():
        copy(excel_template, excel_dir / f"{args.topic}.xlsx")

    # Markdown note templates
    markdown_templates = {
        "howto_template.md": "howto.md",
        "worked_examples_template.md": "worked_examples.md",
        "practice_set_template.md": "practice_set.md",
        "confidence_interval_notes_template.md": "confidence_interval_notes.md",
    }
    for src_name, dst_name in markdown_templates.items():
        src = TEMPLATES / src_name
        if src.exists():
            copy(src, notes_dir / dst_name)

    # Slide master
    ppt_template = TEMPLATES / "topic_master.pptx"
    if ppt_template.exists():
        copy(ppt_template, slides_dir / f"{args.topic}.pptx")

    # Bonus script
    py_template = TEMPLATES / "topic_bonus.py"
    if py_template.exists():
        copy(py_template, bonus_dir / f"{args.topic}_bonus.py")

    print("Scaffold complete. Fill in placeholders and export PDFs when ready.")

if __name__ == "__main__":
    main()
