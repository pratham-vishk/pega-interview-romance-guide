#!/usr/bin/env python3
"""Generate Google SWE Interview OS — interactive HTML + PDF."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from content.build import build_html

BASE = Path(__file__).parent
HTML_PATH = BASE / "google-swe-interview-os.html"
PDF_PATH = BASE / "Google_SWE_Interview_OS.pdf"


def generate_pdf(html_path: Path, pdf_path: Path) -> None:
    from weasyprint import HTML
    HTML(filename=str(html_path)).write_pdf(str(pdf_path))


def main() -> None:
    print("Building Google SWE Interview OS...")
    html = build_html()
    HTML_PATH.write_text(html, encoding="utf-8")
    print(f"  HTML: {HTML_PATH} ({len(html):,} bytes)")

    try:
        generate_pdf(HTML_PATH, PDF_PATH)
        print(f"  PDF:  {PDF_PATH}")
    except Exception as e:
        print(f"  PDF generation skipped: {e}")
        print("  Open HTML in browser for full interactivity.")

    print("Done.")


if __name__ == "__main__":
    main()
