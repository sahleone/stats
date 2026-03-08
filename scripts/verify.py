"""
verify.py — Verify that all expected topic files exist and Excel files have zero errors.

Usage:
    python scripts/verify.py                  # Check all topics
    python scripts/verify.py one_sample_z_test  # Check one topic
    python scripts/verify.py --summary        # Print summary table only

Run from the repo root.
"""

import json
import os
import subprocess
import sys
from pathlib import Path

TOPICS = [
    "one_sample_z_test",
    "one_sample_t_test",
    "one_sample_proportion_z_test",
    "two_sample_z_test",
    "two_sample_t_test_equal_var",
    "welchs_t_test",
    "paired_t_test",
    "two_proportion_z_test",
    "chi_square_goodness_of_fit",
    "chi_square_independence",
    "fishers_exact_test",
    "shapiro_wilk_test",
    "one_way_anova",
    "two_way_anova",
    "sign_test",
    "wilcoxon_signed_rank",
    "mann_whitney_u",
    "kruskal_wallis",
    "correlation_t_test",
    "regression_slope_t_test",
    "regression_f_test",
    "chi_square_variance",
    "f_test_two_variances",
]

SUPPLEMENTARY_FILES = [
    "supplementary/test_selection_flowchart.pdf",
    "supplementary/master_formula_sheet.pdf",
    "supplementary/master_critical_value_tables.pdf",
]


def get_expected_files(topic):
    return [
        f"{topic}/{topic}.xlsx",
        f"{topic}/{topic}_notes.pdf",
        f"{topic}/{topic}.pptx",
        f"{topic}/{topic}_questions.xlsx",
        f"{topic}/{topic}_answers.xlsx",
        f"{topic}/{topic}_bonus.py",
    ]


def check_xlsx_errors(filepath):
    """Run recalc.py on an xlsx file and return error count."""
    recalc_script = Path("scripts/recalc.py")
    if not recalc_script.exists():
        return None, "recalc.py not found"

    try:
        result = subprocess.run(
            [sys.executable, str(recalc_script), filepath],
            capture_output=True, text=True, timeout=60
        )
        if result.returncode != 0:
            return None, f"recalc failed: {result.stderr[:200]}"

        data = json.loads(result.stdout)
        return data.get("total_errors", 0), data.get("status", "unknown")
    except subprocess.TimeoutExpired:
        return None, "recalc timed out"
    except json.JSONDecodeError:
        return None, "recalc output not valid JSON"
    except Exception as e:
        return None, str(e)


def check_py_runs(filepath):
    """Check if a Python script runs without errors."""
    try:
        result = subprocess.run(
            [sys.executable, filepath],
            capture_output=True, text=True, timeout=120,
            cwd=str(Path(filepath).parent)
        )
        return result.returncode == 0, result.stderr[:300] if result.returncode != 0 else ""
    except subprocess.TimeoutExpired:
        return False, "script timed out (>120s)"
    except Exception as e:
        return False, str(e)


def verify_topic(topic, verbose=True):
    """Verify all files for a single topic. Returns (passed, total, issues)."""
    files = get_expected_files(topic)
    passed = 0
    total = len(files)
    issues = []

    for f in files:
        if not Path(f).exists():
            issues.append(f"  MISSING: {f}")
            continue

        size = Path(f).stat().st_size
        if size == 0:
            issues.append(f"  EMPTY:   {f} (0 bytes)")
            continue

        passed += 1

        # Extra checks for xlsx files
        if f.endswith(".xlsx"):
            errors, status = check_xlsx_errors(f)
            if errors is None:
                issues.append(f"  WARN:    {f} — could not verify formulas ({status})")
            elif errors > 0:
                issues.append(f"  ERRORS:  {f} — {errors} formula error(s) ({status})")
                passed -= 1

        # Extra check for bonus.py
        if f.endswith("_bonus.py"):
            runs_ok, err_msg = check_py_runs(f)
            if not runs_ok:
                issues.append(f"  FAIL:    {f} — script error: {err_msg}")
                passed -= 1

    if verbose:
        status = "OK" if passed == total and not issues else "ISSUES"
        print(f"\n[{status}] {topic} ({passed}/{total} files)")
        for issue in issues:
            print(issue)

    return passed, total, issues


def verify_supplementary(verbose=True):
    """Verify supplementary materials exist."""
    passed = 0
    total = len(SUPPLEMENTARY_FILES)
    issues = []

    for f in SUPPLEMENTARY_FILES:
        if not Path(f).exists():
            issues.append(f"  MISSING: {f}")
        elif Path(f).stat().st_size == 0:
            issues.append(f"  EMPTY:   {f}")
        else:
            passed += 1

    if verbose:
        status = "OK" if passed == total else "ISSUES"
        print(f"\n[{status}] supplementary ({passed}/{total} files)")
        for issue in issues:
            print(issue)

    return passed, total, issues


def print_summary(results):
    """Print a markdown-style summary table."""
    print("\n" + "=" * 75)
    print("SUMMARY")
    print("=" * 75)
    print(f"\n{'Topic':<35} {'Excel':>6} {'PDF':>6} {'PPTX':>6} {'Q':>6} {'A':>6} {'Py':>6}")
    print("-" * 75)

    total_ok = 0
    total_all = 0

    for topic in TOPICS:
        files = get_expected_files(topic)
        statuses = []
        for f in files:
            if Path(f).exists() and Path(f).stat().st_size > 0:
                statuses.append("  Y")
                total_ok += 1
            else:
                statuses.append("  -")
            total_all += 1

        name = topic.replace("_", " ").title()
        if len(name) > 33:
            name = name[:30] + "..."
        print(f"{name:<35} {''.join(statuses)}")

    # Supplementary
    print("-" * 75)
    supp_statuses = []
    for f in SUPPLEMENTARY_FILES:
        if Path(f).exists() and Path(f).stat().st_size > 0:
            supp_statuses.append("Y")
            total_ok += 1
        else:
            supp_statuses.append("-")
        total_all += 1
    print(f"{'Supplementary':<35}   {'  '.join(supp_statuses)}")

    print("-" * 75)
    pct = (total_ok / total_all * 100) if total_all > 0 else 0
    print(f"\nTotal: {total_ok}/{total_all} files present ({pct:.0f}%)")


def main():
    args = sys.argv[1:]

    if "--summary" in args:
        print_summary(None)
        return

    if args and args[0] in TOPICS:
        topics_to_check = [args[0]]
    elif args and args[0] not in ("--all",):
        print(f"Unknown topic: {args[0]}")
        print(f"Available: {', '.join(TOPICS)}")
        sys.exit(1)
    else:
        topics_to_check = TOPICS

    print("=" * 60)
    print("Stats Repo Verification")
    print("=" * 60)

    all_passed = 0
    all_total = 0
    all_issues = []

    for topic in topics_to_check:
        p, t, issues = verify_topic(topic)
        all_passed += p
        all_total += t
        all_issues.extend(issues)

    if len(topics_to_check) == len(TOPICS):
        p, t, issues = verify_supplementary()
        all_passed += p
        all_total += t
        all_issues.extend(issues)

    print("\n" + "=" * 60)
    pct = (all_passed / all_total * 100) if all_total > 0 else 0
    print(f"RESULT: {all_passed}/{all_total} checks passed ({pct:.0f}%)")

    if all_issues:
        print(f"\n{len(all_issues)} issue(s) found.")
        sys.exit(1)
    else:
        print("\nAll checks passed!")
        sys.exit(0)


if __name__ == "__main__":
    main()
