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


def resize_diagram_pngs(diagrams_dir: Path, max_height: int = 1600) -> None:
    """Scale down tall PNG diagrams so they fit on one PDF page."""
    try:
        from PIL import Image
    except ImportError:
        return
    for png in diagrams_dir.glob("*.png"):
        try:
            img = Image.open(png)
            if img.height > max_height:
                ratio = max_height / img.height
                new_size = (max(1, int(img.width * ratio)), max_height)
                img = img.resize(new_size, Image.Resampling.LANCZOS)
                img.save(png, optimize=True)
                print(f"  Resized {png.name} → {new_size[0]}x{new_size[1]}")
        except Exception as e:
            print(f"  Resize skip {png.name}: {e}")


def render_mermaid_diagrams() -> dict[str, str]:
    """Render all .mmd files to PNG via mermaid-cli (labels render correctly in PDF)."""
    diagrams: dict[str, str] = {}
    config = DIAGRAMS_DIR / "mermaid-config.json"
    mmd_files = sorted(DIAGRAMS_DIR.glob("*.mmd"))
    if not mmd_files:
        print("No mermaid files found.")
        return diagrams

    for mmd in mmd_files:
        png = mmd.with_suffix(".png")
        key = mmd.stem

        if not png.exists() or png.stat().st_mtime < mmd.stat().st_mtime:
            cmd = [
                "npx", "-y", "@mermaid-js/mermaid-cli@11.4.0",
                "-i", str(mmd),
                "-o", str(png),
                "-b", "white",
                "-w", "720",
                "-s", "1.4",
            ]
            if config.exists():
                cmd.extend(["-c", str(config)])
            print(f"Rendering {mmd.name} → PNG...")
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            if result.returncode != 0:
                print(f"  Warning: {mmd.name}: {result.stderr[:200]}")

        if png.exists():
            diagrams[key] = str(png.resolve())
            print(f"  OK: {key}")
    resize_diagram_pngs(DIAGRAMS_DIR)
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

    # Verify topic coverage
    verify_script = BASE / "verify_coverage.py"
    if verify_script.exists():
        print("Step 4: Verifying topic coverage...")
        subprocess.run([sys.executable, str(verify_script)], check=False)

    print("\nDone! Your one-stop Pega interview guide is ready.")


if __name__ == "__main__":
    main()
