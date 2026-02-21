#!/usr/bin/env bash
# Build the LaTeX example and convert to PNG for README.
#
# Requirements: pdflatex, magick (ImageMagick 7+) or convert (ImageMagick 6)
#
# Usage:
#   bash latex-example/build_image.sh

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TEX_DIR="${REPO_ROOT}/latex-example"
OUT_DIR="${REPO_ROOT}/docs/images"

mkdir -p "${OUT_DIR}"

# Compile LaTeX (may return non-zero due to warnings, so check PDF output)
echo "Compiling LaTeX..."
(cd "${TEX_DIR}" && pdflatex -interaction=nonstopmode example.tex > /dev/null 2>&1) || true
if [ ! -f "${TEX_DIR}/example.pdf" ]; then
    echo "Error: pdflatex failed to produce example.pdf" >&2
    exit 1
fi

# Convert PDF -> PNG
echo "Converting PDF to PNG..."
if command -v magick &> /dev/null; then
    magick -density 300 "${TEX_DIR}/example.pdf" -quality 95 -trim +repage \
        -bordercolor white -border 20x20 "${OUT_DIR}/latex-output.png"
elif command -v convert &> /dev/null; then
    convert -density 300 "${TEX_DIR}/example.pdf" -quality 95 -trim +repage \
        -bordercolor white -border 20x20 "${OUT_DIR}/latex-output.png"
else
    echo "Error: ImageMagick (magick or convert) not found." >&2
    exit 1
fi

# Clean up LaTeX intermediate files
rm -f "${TEX_DIR}/example.aux" "${TEX_DIR}/example.log" "${TEX_DIR}/example.pdf"

echo "Done: ${OUT_DIR}/latex-output.png"
