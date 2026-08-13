"""Shared CSS for the Pega interview guide PDF."""

STYLES = """
  @page { margin: 14mm 12mm; size: A4; }
  * { box-sizing: border-box; }
  body {
    font-family: 'DejaVu Sans', 'Georgia', serif;
    color: #2d1b2e;
    line-height: 1.55;
    font-size: 9.5pt;
    margin: 0; padding: 0;
  }
  .cover {
    page-break-after: always;
    min-height: 94vh;
    display: flex; flex-direction: column;
    justify-content: center; align-items: center;
    text-align: center;
    background: linear-gradient(145deg, #fff5f7 0%, #fce4ec 40%, #f3e5f5 100%);
    padding: 36px; border: 3px double #c2185b;
  }
  .cover h1 { font-size: 24pt; color: #880e4f; margin-bottom: 6px; }
  .cover .subtitle { font-size: 12pt; color: #6a1b4a; font-style: italic; }
  .cover .dedication { font-size: 10pt; max-width: 520px; color: #4a148c; margin-top: 20px; padding-top: 18px; border-top: 1px solid #ce93d8; line-height: 1.6; }
  h2 { color: #ad1457; font-size: 14pt; border-bottom: 2px solid #f8bbd0; padding-bottom: 5px; margin-top: 18px; page-break-after: avoid; }
  h3 { color: #6a1b4a; font-size: 11pt; margin-top: 14px; page-break-after: avoid; }
  h4 { color: #880e4f; font-size: 10pt; margin-top: 10px; page-break-after: avoid; }
  .flirt-box {
    background: linear-gradient(135deg, #fff0f3 0%, #fce4ec 100%);
    border-left: 4px solid #e91e63;
    padding: 10px 14px; margin: 10px 0;
    border-radius: 0 8px 8px 0;
    font-style: italic; color: #4a148c;
    page-break-inside: avoid;
  }
  .diagram-box {
    text-align: center;
    margin: 12px 0;
    padding: 8px;
    background: #fafafa;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    page-break-inside: avoid;
    page-break-before: auto;
  }
  .diagram-box img {
    display: block;
    margin: 0 auto;
    max-width: 100%;
    max-height: 175mm;
    width: auto;
    height: auto;
    object-fit: contain;
  }
  .diagram-caption { font-size: 8.5pt; color: #666; font-style: italic; margin-top: 6px; page-break-before: avoid; }
  .curiosity-teaser {
    background: linear-gradient(135deg, #fff8e1 0%, #fce4ec 100%);
    border: 1px solid #f48fb1;
    border-radius: 10px;
    padding: 10px 14px;
    margin: 16px 0;
    text-align: center;
    font-size: 9.5pt;
    color: #6a1b4a;
    page-break-inside: avoid;
  }
  .qa-block {
    background: #fafafa; border: 1px solid #e0e0e0; border-radius: 8px;
    padding: 8px 10px; margin: 8px 0; page-break-inside: avoid;
  }
  .question { font-weight: bold; color: #1565c0; margin-bottom: 3px; font-size: 9.5pt; }
  .answer { color: #333; font-size: 9.5pt; }
  .tip { background: #e8f5e9; border-left: 4px solid #43a047; padding: 8px 12px; margin: 8px 0; font-size: 9pt; page-break-inside: avoid; }
  .warning { background: #fff3e0; border-left: 4px solid #fb8c00; padding: 8px 12px; margin: 8px 0; font-size: 9pt; page-break-inside: avoid; }
  table { width: 100%; border-collapse: collapse; margin: 8px 0; font-size: 8.5pt; page-break-inside: avoid; }
  th { background: #f8bbd0; color: #4a148c; padding: 5px 7px; text-align: left; }
  td { border: 1px solid #e0e0e0; padding: 4px 6px; vertical-align: top; }
  tr:nth-child(even) { background: #fafafa; }
  ul, ol { margin: 5px 0; padding-left: 18px; }
  li { margin: 2px 0; }
  .toc { page-break-after: always; }
  .chapter { page-break-before: always; }
  .subtopic-block {
    margin: 10px 0 14px 0;
    padding: 0 0 8px 0;
    border-bottom: 1px dotted #f8bbd0;
    page-break-inside: avoid;
  }
  .subtopic-block p { margin: 4px 0; }
  code, .mono { font-family: 'DejaVu Sans Mono', monospace; background: #f5f5f5; padding: 1px 4px; border-radius: 3px; font-size: 8.5pt; }
  .cheat { font-size: 8pt; columns: 2; column-gap: 16px; }
  .teaser { text-align: center; font-style: italic; color: #c2185b; margin: 16px 0; padding: 10px; border: 1px dashed #f48fb1; border-radius: 8px; }
  .master-checklist { font-size: 8.5pt; columns: 2; column-gap: 16px; }
  .master-checklist li { break-inside: avoid; }
  .easy-box {
    background: #e8eaf6;
    border-left: 4px solid #5c6bc0;
    padding: 10px 14px;
    margin: 10px 0;
    font-size: 9pt;
    color: #283593;
    page-break-inside: avoid;
  }
  .easy-box strong { color: #1a237e; }
  .flirty-example {
    background: linear-gradient(135deg, #fff0f5 0%, #f8bbd0 100%);
    border: 1px dashed #e91e63;
    border-radius: 10px;
    padding: 10px 14px;
    margin: 10px 0;
    font-size: 9pt;
    color: #880e4f;
    page-break-inside: avoid;
  }
  .footer-note {
    text-align: center;
    font-size: 8pt;
    color: #888;
    margin-top: 20px;
    padding-top: 10px;
    border-top: 1px solid #eee;
  }
"""
