# Pega Interview Romance Guide 💕

Complete one-stop Pega interview preparation PDF for developers with **3+ years experience** (CSA / SSA level).

## Download PDF

**[Download Pega_Interview_Romance_Guide.pdf](pega-interview-prep/Pega_Interview_Romance_Guide.pdf)**

## What's Inside

- **32 chapters** — every major Pega concept
- **23 diagrams** — flowcharts, sequence diagrams, state diagrams, mind maps
- **Top 50 interview Q&A** — easy-language answers
- **200 rapid-fire questions** — quick revision
- **4 mock interview scenarios**
- **Topic verification matrix** — nothing missed

## Topics Covered

Platform & Architecture · Class Hierarchy · Rule Resolution · Case Management · Flows · Clipboard · Data Pages · Data Transforms · Activities · Decision Rules · Declare Rules · Validation · UI & Constellation · SLAs · Integration · Security · Agents · Reporting · Testing · Performance · DevOps · CDH/RPA/AI · and more.

## Regenerate PDF

```bash
pip install weasyprint
python3 generate_pega_pdf.py
python3 pega-interview-prep/verify_coverage.py
```

## Structure

```
pega-interview-prep/
  Pega_Interview_Romance_Guide.pdf   # Final PDF
  diagrams/                          # Mermaid source + SVG
  content/                           # Chapter HTML builders
  verify_coverage.py                 # Topic verification script
generate_pega_pdf.py                 # PDF generator
```

## Author

Prepared for Pega developers preparing for CSA/SSA interviews.
