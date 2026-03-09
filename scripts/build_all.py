"""
build_all.py — Orchestrator for building stats lecture materials.

This script provides a command-line interface for generating topic materials.
It is primarily meant as a helper for Claude Code, but can also be used
by the instructor directly.

Usage:
    python scripts/build_all.py --topic one_sample_z_test   # Build one topic
    python scripts/build_all.py --all                       # Build all topics
    python scripts/build_all.py --list                      # List all topics
    python scripts/build_all.py --status                    # Show build status
    python scripts/build_all.py --supplementary             # Build supplementary PDFs

This script does NOT contain the actual content generation logic.
Claude Code should use this as a framework and fill in the
generate_topic_files() function for each topic, or generate each
topic's files directly following CLAUDE.md instructions.
"""

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

# Add scripts/ to path so we can import our modules
sys.path.insert(0, str(Path(__file__).parent))

from topic_registry import TOPIC_ORDER, TOPICS, get_topic


def get_expected_files(topic_key):
    """Return list of expected file paths for a topic."""
    return [
        f"{topic_key}/{topic_key}.xlsx",
        f"{topic_key}/{topic_key}_notes.pdf",
        f"{topic_key}/{topic_key}.pptx",
        f"{topic_key}/{topic_key}_questions.xlsx",
        f"{topic_key}/{topic_key}_answers.xlsx",
        f"{topic_key}/{topic_key}_bonus.py",
    ]


def check_topic_status(topic_key):
    """Check which files exist for a topic. Returns (existing, missing)."""
    files = get_expected_files(topic_key)
    existing = [f for f in files if Path(f).exists() and Path(f).stat().st_size > 0]
    missing = [f for f in files if f not in existing]
    return existing, missing


def recalc_xlsx(filepath):
    """Recalculate formulas in an xlsx file. Returns True if successful."""
    recalc_script = Path("scripts/recalc.py")
    if not recalc_script.exists():
        print(f"  WARNING: scripts/recalc.py not found, skipping recalc for {filepath}")
        return True

    try:
        result = subprocess.run(
            [sys.executable, str(recalc_script), filepath],
            capture_output=True, text=True, timeout=60
        )
        data = json.loads(result.stdout)
        if data.get("total_errors", 0) > 0:
            print(f"  ERROR: {filepath} has {data['total_errors']} formula error(s)")
            print(f"         {json.dumps(data.get('error_summary', {}), indent=2)}")
            return False
        print(f"  OK: {filepath} — {data.get('total_formulas', 0)} formulas, 0 errors")
        return True
    except Exception as e:
        print(f"  WARNING: recalc failed for {filepath}: {e}")
        return True


def run_bonus_py(filepath):
    """Run a bonus Python script and check for errors."""
    try:
        result = subprocess.run(
            [sys.executable, filepath],
            capture_output=True, text=True, timeout=120,
            cwd=str(Path(filepath).parent)
        )
        if result.returncode != 0:
            print(f"  ERROR: {filepath} failed:")
            print(f"         {result.stderr[:500]}")
            return False
        print(f"  OK: {filepath} ran successfully")
        return True
    except subprocess.TimeoutExpired:
        print(f"  ERROR: {filepath} timed out (>120s)")
        return False


def build_topic(topic_key):
    """
    Build all 6 files for a single topic.

    NOTE: This function creates the folder and placeholder structure.
    The actual content generation should be done by Claude Code using
    the topic_registry data and style helpers.
    """
    topic = get_topic(topic_key)
    print(f"\n{'='*60}")
    print(f"Building: {topic['display_name']} ({topic_key})")
    print(f"{'='*60}")

    # Create folder
    os.makedirs(topic_key, exist_ok=True)

    # Check what already exists
    existing, missing = check_topic_status(topic_key)
    if existing:
        print(f"  Already exist: {len(existing)} file(s)")
        for f in existing:
            print(f"    ✓ {f}")
    if missing:
        print(f"  Need to create: {len(missing)} file(s)")
        for f in missing:
            print(f"    ✗ {f}")
    else:
        print("  All files present!")

    # Print topic metadata for reference
    print(f"\n  Category:      {topic['category']}")
    print(f"  Distribution:  {topic['distribution']}")
    print(f"  Effect size:   {topic['effect_size_name']}")
    print(f"  scipy:         {topic['scipy_function']}")
    print(f"  See also:      {', '.join(t[0] for t in topic['see_also'])}")

    print(f"\n  >>> Claude Code: generate the missing files for {topic_key}.")
    print(f"  >>> Use: from scripts.topic_registry import get_topic")
    print(f"  >>> Use: from scripts.excel_styles import *")
    print(f"  >>> Use: from scripts.pdf_styles import StatsNotesPDF")
    print(f"  >>> Use: from scripts.pptx_styles import StatsPresentation")

    return missing


def verify_topic(topic_key):
    """Verify all files for a topic: existence, xlsx recalc, py execution."""
    print(f"\nVerifying: {topic_key}")
    existing, missing = check_topic_status(topic_key)

    if missing:
        print(f"  MISSING {len(missing)} file(s): {', '.join(Path(f).name for f in missing)}")
        return False

    all_ok = True

    # Recalculate xlsx files
    for f in existing:
        if f.endswith(".xlsx"):
            if not recalc_xlsx(f):
                all_ok = False

    # Run bonus.py
    for f in existing:
        if f.endswith("_bonus.py"):
            if not run_bonus_py(f):
                all_ok = False

    return all_ok


def print_status():
    """Print a status table of all topics."""
    print(f"\n{'#':<4} {'Topic':<35} {'xlsx':>5} {'pdf':>5} {'pptx':>5} {'Q':>5} {'A':>5} {'py':>5} {'Status':>8}")
    print("-" * 78)

    complete = 0
    partial = 0
    empty = 0

    for i, key in enumerate(TOPIC_ORDER, 1):
        existing, missing = check_topic_status(key)
        files = get_expected_files(key)

        marks = []
        for f in files:
            marks.append("  ✓" if f in existing else "  -")

        if len(missing) == 0:
            status = "DONE"
            complete += 1
        elif len(existing) > 0:
            status = "PARTIAL"
            partial += 1
        else:
            status = "TODO"
            empty += 1

        name = TOPICS[key]["display_name"]
        if len(name) > 33:
            name = name[:30] + "..."
        print(f"{i:<4} {name:<35} {''.join(marks)} {status:>8}")

    print("-" * 78)
    total = len(TOPIC_ORDER)
    print(f"Complete: {complete}/{total}  |  Partial: {partial}/{total}  |  TODO: {empty}/{total}")

    # Check supplementary
    supp_files = [
        "supplementary/test_selection_flowchart.pdf",
        "supplementary/master_formula_sheet.pdf",
        "supplementary/master_critical_value_tables.pdf",
    ]
    supp_exist = sum(1 for f in supp_files if Path(f).exists())
    print(f"\nSupplementary: {supp_exist}/{len(supp_files)} files")


def list_topics():
    """Print all topics with their numbers and categories."""
    current_cat = None
    for i, key in enumerate(TOPIC_ORDER, 1):
        topic = TOPICS[key]
        if topic["category"] != current_cat:
            current_cat = topic["category"]
            print(f"\n  {current_cat}")
            print(f"  {'-'*40}")
        print(f"    {i:>2}. {key:<35} {topic['display_name']}")


def main():
    parser = argparse.ArgumentParser(
        description="Build stats lecture materials"
    )
    parser.add_argument("--topic", type=str, help="Build a specific topic by key name")
    parser.add_argument("--all", action="store_true", help="Build all topics")
    parser.add_argument("--list", action="store_true", help="List all topics")
    parser.add_argument("--status", action="store_true", help="Show build status")
    parser.add_argument("--verify", type=str, nargs="?", const="all",
                        help="Verify topic(s): --verify [topic_key|all]")
    parser.add_argument("--supplementary", action="store_true",
                        help="Build supplementary materials")

    args = parser.parse_args()

    if args.list:
        list_topics()
    elif args.status:
        print_status()
    elif args.verify:
        if args.verify == "all":
            all_ok = True
            for key in TOPIC_ORDER:
                if not verify_topic(key):
                    all_ok = False
            sys.exit(0 if all_ok else 1)
        else:
            sys.exit(0 if verify_topic(args.verify) else 1)
    elif args.topic:
        if args.topic not in TOPICS:
            print(f"Unknown topic: {args.topic}")
            print(f"Use --list to see available topics")
            sys.exit(1)
        build_topic(args.topic)
    elif args.all:
        for key in TOPIC_ORDER:
            build_topic(key)
    elif args.supplementary:
        print("Building supplementary materials...")
        print("Run: python scripts/build_supplementary.py")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
