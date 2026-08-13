#!/usr/bin/env python3
"""Verify all required Pega topics appear in the generated guide."""

from pathlib import Path

REQUIRED_TOPICS = [
    "Rule Resolution", "Data Page", "Data Transform", "Activity", "Case Type",
    "Flow Action", "Declare Expression", "Decision Table", "When rule", "SLA",
    "Connect-REST", "Service-REST", "Access Group", "Constellation", "Guardrails",
    "PAL", "Tracer", "RAP", "Deployment Manager", "Agent", "Job Scheduler",
    "Report Definition", "Unit Test", "Circumstance", "Worklist", "Workbasket",
    "pyWorkPage", "pxRequestor", "Split-Join", "Validation", "ABAC", "CDH",
    "RPA", "Data Flow", "GenAI", "Feature Toggle", "Obj-Save", "pzInsKey",
    "Class Group", "Pattern inheritance", "Directed inheritance", "FUA",
    "Scorecard", "MapValue", "Queue-For-Agent", "OAuth", "Data Type",
    "Correspondence", "DX API", "Pega Express",
]

HTML = Path("/agent/pega-interview-prep/pega-interview-romance-guide.html")

def main():
    if not HTML.exists():
        print("HTML not found. Run generate_pega_pdf.py first.")
        return 1
    text = HTML.read_text(encoding="utf-8").lower()
    missing = [t for t in REQUIRED_TOPICS if t.lower() not in text]
    found = len(REQUIRED_TOPICS) - len(missing)
    print(f"Topic verification: {found}/{len(REQUIRED_TOPICS)} required topics found")
    if missing:
        print("Missing:", ", ".join(missing))
        return 1
    print("All required topics verified ✅")
    # Count diagrams
    svg_count = text.count("<svg")
    png_count = text.count("data:image/png;base64")
    qa_count = text.count('class="question"')
    print(f"Diagrams embedded: {png_count + svg_count} ({png_count} PNG)")
    print(f"Q&A blocks: {qa_count}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
