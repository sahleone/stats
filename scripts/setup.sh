#!/usr/bin/env bash
# setup.sh — Install all dependencies needed to build stats lecture materials.
# Run this once before using any build scripts.
#
# Usage:
#   chmod +x setup.sh
#   ./setup.sh

set -e

echo "=== Stats Repo Setup ==="

# Python packages
echo ""
echo "Installing Python packages..."
pip install --break-system-packages -r requirements.txt

# Verify LibreOffice is available (needed for Excel formula recalculation)
echo ""
if command -v libreoffice &> /dev/null; then
    LO_VERSION=$(libreoffice --version 2>/dev/null | head -1)
    echo "LibreOffice found: $LO_VERSION"
else
    echo "WARNING: LibreOffice is not installed."
    echo "  It is required for recalculating Excel formulas."
    echo "  Install it with:"
    echo "    Ubuntu/Debian: sudo apt-get install libreoffice-calc"
    echo "    macOS:         brew install --cask libreoffice"
    echo ""
    echo "  The build scripts will still generate files, but formula"
    echo "  values will not be recalculated until LibreOffice is available."
fi

# Verify key Python imports
echo ""
echo "Verifying Python imports..."
python3 -c "
import openpyxl, fpdf, pptx, scipy, matplotlib, numpy, pandas
print('  openpyxl:    ' + openpyxl.__version__)
print('  fpdf2:       ' + fpdf.__version__)
print('  python-pptx: ' + pptx.__version__)
print('  scipy:       ' + scipy.__version__)
print('  matplotlib:  ' + matplotlib.__version__)
print('  numpy:       ' + numpy.__version__)
print('  pandas:      ' + pandas.__version__)
print()
print('All imports OK.')
"

echo ""
echo "=== Setup complete ==="
echo ""
echo "Next steps:"
echo "  1. Review CLAUDE.md for full build instructions"
echo "  2. Run: python scripts/build_all.py --topic one_sample_z_test"
echo "     or let Claude Code generate topics following CLAUDE.md"
echo "  3. Run: python scripts/verify.py  (after building topics)"
