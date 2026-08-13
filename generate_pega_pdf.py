#!/usr/bin/env python3
"""Generate comprehensive Pega interview prep PDF with Mermaid diagrams."""

import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "pega-interview-prep"))

from content.styles import STYLES
from content.chapters import build_chapters

BASE = Path(__file__).parent / "pega-interview-prep"
DIAGRAMS_DIR = BASE / "diagrams"
OUTPUT_DIR = BASE
HTML_PATH = OUTPUT_DIR / "pega-interview-romance-guide.html"
PDF_PATH = OUTPUT_DIR / "Pega_Interview_Romance_Guide.pdf"


def render_mermaid_diagrams() -> dict[str, str]:
    """Render all .mmd files to SVG via mermaid-cli."""
    diagrams: dict[str, str] = {}
    mmd_files = sorted(DIAGRAMS_DIR.glob("*.mmd"))
    if not mmd_files:
        print("No mermaid files found.")
        return diagrams

    for mmd in mmd_files:
        svg = mmd.with_suffix(".svg")
        key = mmd.stem  # e.g. 01-rule-resolution

        if not svg.exists() or svg.stat().st_mtime < mmd.stat().st_mtime:
            cmd = [
                "npx", "-y", "@mermaid-js/mermaid-cli@11.4.0",
                "-i", str(mmd),
                "-o", str(svg),
                "-b", "white",
                "-w", "900",
            ]
            print(f"Rendering {mmd.name}...")
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            if result.returncode != 0:
                print(f"  Warning: {mmd.name}: {result.stderr[:200]}")

        if svg.exists():
            diagrams[key] = str(svg.resolve())
            print(f"  OK: {key}")
    return diagrams


def build_html(diagrams: dict[str, str]) -> str:
    chapters = build_chapters(diagrams)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Pega Interview Romance Guide — Complete One-Stop Edition</title>
<style>{STYLES}</style>
</head>
<body>
{chapters}
</body>
</html>"""


def generate_pdf(html_path: Path, pdf_path: Path) -> None:
    from weasyprint import HTML
    HTML(filename=str(html_path)).write_pdf(str(pdf_path))


def main():
    print("=== Pega Interview PDF Generator ===\n")
    print("Step 1: Rendering Mermaid diagrams...")
    diagrams = render_mermaid_diagrams()
    print(f"  {len(diagrams)} diagrams ready.\n")

    print("Step 2: Building HTML...")
    html = build_html(diagrams)
    HTML_PATH.write_text(html, encoding="utf-8")
    print(f"  HTML: {HTML_PATH} ({len(html)/1024:.1f} KB)\n")

    print("Step 3: Generating PDF...")
    generate_pdf(HTML_PATH, PDF_PATH)
    size_kb = PDF_PATH.stat().st_size / 1024
    print(f"  PDF: {PDF_PATH} ({size_kb:.1f} KB)\n")
    print("Done! Your one-stop Pega interview guide is ready.")


if __name__ == "__main__":
    main()
