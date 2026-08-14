"""Premium engineering aesthetic for Google SWE Interview OS."""

STYLES = """
  @page { margin: 14mm 12mm; size: A4; }
  * { box-sizing: border-box; }
  :root {
    --bg: #0f1419;
    --surface: #1a2332;
    --surface2: #243044;
    --accent: #4285f4;
    --accent2: #34a853;
    --warn: #fbbc04;
    --danger: #ea4335;
    --text: #e8eaed;
    --muted: #9aa0a6;
    --border: #3c4043;
  }
  body {
    font-family: 'DejaVu Sans', 'Segoe UI', system-ui, sans-serif;
    background: var(--bg);
    color: var(--text);
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
    background: linear-gradient(160deg, #0f1419 0%, #1a2332 50%, #0d2137 100%);
    padding: 40px;
    border: 2px solid var(--accent);
  }
  .cover h1 { font-size: 22pt; color: #fff; margin: 12px 0 6px; letter-spacing: -0.5px; }
  .cover .subtitle { font-size: 11pt; color: var(--accent); max-width: 520px; }
  .cover .tagline { font-size: 9.5pt; color: var(--muted); margin-top: 20px; }
  .badge { display: inline-block; background: var(--accent); color: #fff; padding: 4px 12px; border-radius: 20px; font-size: 8pt; font-weight: bold; margin: 4px; }
  h2 { color: #8ab4f8; font-size: 14pt; border-bottom: 2px solid var(--accent); padding-bottom: 6px; margin-top: 20px; page-break-after: avoid; }
  h3 { color: #aecbfa; font-size: 11pt; margin-top: 14px; page-break-after: avoid; }
  h4 { color: var(--accent2); font-size: 10pt; margin-top: 10px; }
  .section { page-break-before: always; padding: 8px 0; }
  .section:first-of-type { page-break-before: auto; }
  .toc { page-break-after: always; }
  .toc a { color: #8ab4f8; text-decoration: none; }
  .toc li { margin: 4px 0; }
  .pattern-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-left: 4px solid var(--accent);
    border-radius: 8px;
    padding: 12px 14px;
    margin: 12px 0;
    page-break-inside: avoid;
  }
  .pattern-card.hard { border-left-color: var(--danger); }
  .pattern-card.medium { border-left-color: var(--warn); }
  .pattern-header { display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 6px; }
  .pattern-num { background: var(--accent); color: #fff; padding: 2px 8px; border-radius: 4px; font-size: 8pt; font-weight: bold; }
  .pattern-category { color: var(--muted); font-size: 8pt; text-transform: uppercase; letter-spacing: 0.5px; }
  .signal-box {
    background: #1e3a5f;
    border: 1px solid #4285f4;
    border-radius: 6px;
    padding: 8px 12px;
    margin: 8px 0;
    font-size: 9pt;
  }
  .when-not { background: #3d1f1f; border-left: 3px solid var(--danger); padding: 6px 10px; margin: 6px 0; font-size: 9pt; }
  .curiosity {
    background: linear-gradient(135deg, #1a2332 0%, #2d1b4e 100%);
    border: 1px dashed #9c27b0;
    border-radius: 10px;
    padding: 10px 14px;
    margin: 12px 0;
    font-style: italic;
    color: #ce93d8;
  }
  .code-block {
    background: #0d1117;
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 10px 12px;
    font-family: 'DejaVu Sans Mono', monospace;
    font-size: 7.8pt;
    line-height: 1.45;
    overflow-x: auto;
    white-space: pre-wrap;
    page-break-inside: avoid;
    color: #c9d1d9;
  }
  .grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }
  .grid-3 { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 8px; }
  table { width: 100%; border-collapse: collapse; margin: 8px 0; font-size: 8.5pt; page-break-inside: avoid; }
  th { background: var(--surface2); color: #8ab4f8; padding: 6px 8px; text-align: left; border: 1px solid var(--border); }
  td { border: 1px solid var(--border); padding: 5px 7px; vertical-align: top; }
  tr:nth-child(even) td { background: var(--surface); }
  .tip { background: #1b3d2f; border-left: 4px solid var(--accent2); padding: 8px 12px; margin: 8px 0; font-size: 9pt; }
  .trap { background: #3d2a1f; border-left: 4px solid var(--warn); padding: 8px 12px; margin: 8px 0; font-size: 9pt; }
  .interview { background: #1f2a44; border-left: 4px solid #8ab4f8; padding: 8px 12px; margin: 8px 0; font-size: 9pt; }
  .diagram-box { text-align: center; margin: 10px 0; padding: 8px; background: var(--surface); border: 1px solid var(--border); border-radius: 6px; page-break-inside: avoid; }
  .diagram-box img, .diagram-box svg { max-width: 100%; max-height: 120mm; }
  .diagram-caption { font-size: 8pt; color: var(--muted); font-style: italic; margin-top: 6px; }
  .day-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 14px;
    margin: 12px 0;
    page-break-inside: avoid;
  }
  .day-card h3 { margin-top: 0; color: var(--accent); }
  .xp-bar { height: 8px; background: var(--surface2); border-radius: 4px; overflow: hidden; margin: 6px 0; }
  .xp-fill { height: 100%; background: linear-gradient(90deg, var(--accent), var(--accent2)); width: 0%; }
  .checklist label { display: block; margin: 4px 0; font-size: 9pt; cursor: pointer; }
  .checklist input[type=checkbox] { margin-right: 8px; accent-color: var(--accent); }
  .quiz { background: var(--surface2); border-radius: 8px; padding: 12px; margin: 10px 0; }
  .quiz-answer { display: none; margin-top: 8px; padding: 8px; background: #1b3d2f; border-radius: 4px; }
  .quiz.revealed .quiz-answer { display: block; }
  .btn { background: var(--accent); color: #fff; border: none; padding: 6px 14px; border-radius: 6px; cursor: pointer; font-size: 9pt; }
  .btn:hover { opacity: 0.9; }
  .progress-tracker { position: sticky; top: 0; background: var(--surface); border-bottom: 1px solid var(--border); padding: 8px 16px; z-index: 100; display: flex; gap: 16px; align-items: center; flex-wrap: wrap; font-size: 8.5pt; }
  .level-badge { background: var(--accent2); color: #000; padding: 2px 10px; border-radius: 12px; font-weight: bold; }
  .cheat-sheet { font-size: 7.8pt; columns: 2; column-gap: 14px; line-height: 1.35; }
  .cheat-sheet li { break-inside: avoid; }
  .nav-sidebar { display: none; }
  @media screen {
    body { padding-top: 48px; max-width: 1100px; margin: 0 auto; padding-left: 16px; padding-right: 16px; }
    .nav-sidebar { display: block; position: fixed; left: 0; top: 48px; width: 200px; height: calc(100vh - 48px); overflow-y: auto; background: var(--surface); border-right: 1px solid var(--border); padding: 12px; font-size: 8pt; }
    .nav-sidebar a { display: block; color: var(--muted); text-decoration: none; padding: 4px 0; }
    .nav-sidebar a:hover { color: var(--accent); }
    body.has-sidebar { margin-left: 210px; }
    .pattern-card:hover { border-color: var(--accent); }
  }
  .mock-scorecard td input { width: 40px; }
  .reflection { border: 1px dashed var(--border); min-height: 60px; padding: 8px; margin: 8px 0; border-radius: 6px; }
  .footer { text-align: center; font-size: 8pt; color: var(--muted); margin: 24px 0; padding-top: 12px; border-top: 1px solid var(--border); }
  ul, ol { margin: 6px 0; padding-left: 18px; }
  li { margin: 3px 0; }
  a { color: #8ab4f8; }
"""

INTERACTIVE_JS = """
(function() {
  const STORAGE_KEY = 'bilkul-interview-os';
  function load() {
    try { return JSON.parse(localStorage.getItem(STORAGE_KEY) || '{}'); }
    catch { return {}; }
  }
  function save(data) {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(data));
    updateUI(data);
  }
  function updateUI(data) {
    const xp = data.xp || 0;
    const level = Math.min(6, Math.floor(xp / 500) + 1);
    const levels = ['Pattern Explorer','Pattern Recognizer','Problem Solver','Interview Solver','System Designer','Google Ready'];
    document.querySelectorAll('[data-xp-display]').forEach(el => el.textContent = xp);
    document.querySelectorAll('[data-level-display]').forEach(el => el.textContent = levels[level - 1] || levels[0]);
    document.querySelectorAll('[data-xp-bar]').forEach(el => {
      el.style.width = ((xp % 500) / 500 * 100) + '%';
    });
    (data.checked || []).forEach(id => {
      const cb = document.getElementById(id);
      if (cb) cb.checked = true;
    });
  }
  document.addEventListener('change', e => {
    if (e.target.matches('input[type=checkbox][data-track]')) {
      const data = load();
      data.checked = data.checked || [];
      const id = e.target.id;
      if (e.target.checked && !data.checked.includes(id)) {
        data.checked.push(id);
        data.xp = (data.xp || 0) + 10;
      } else if (!e.target.checked) {
        data.checked = data.checked.filter(x => x !== id);
      }
      save(data);
    }
  });
  document.querySelectorAll('.quiz-reveal').forEach(btn => {
    btn.addEventListener('click', () => {
      btn.closest('.quiz').classList.add('revealed');
      const data = load();
      data.xp = (data.xp || 0) + 5;
      save(data);
    });
  });
  document.querySelectorAll('[data-add-xp]').forEach(btn => {
    btn.addEventListener('click', () => {
      const data = load();
      data.xp = (data.xp || 0) + parseInt(btn.dataset.addXp || '20', 10);
      save(data);
    });
  });
  updateUI(load());
})();
"""
