"""Render Pattern Cards from patterns_data."""

from content.helpers import (
    bullets, code_block, curiosity, h, interview, signal_box, trap, when_not,
)
from content.patterns_data import Pattern, get_all_patterns


def render_example(ex, level: str) -> str:
    return f"<li><strong>{h(ex.title)}</strong> ({level}): {h(ex.problem)} — <em>{h(ex.approach)}</em></li>"


def render_pattern_card(p: Pattern) -> str:
    diff = "hard" if p.num >= 55 else ("medium" if p.num >= 25 else "")
    examples = ""
    if p.examples_easy:
        examples += "<h4>Easy Examples</h4><ul>" + "".join(render_example(e, "Easy") for e in p.examples_easy) + "</ul>"
    if p.examples_medium:
        examples += "<h4>Medium Examples</h4><ul>" + "".join(render_example(e, "Medium") for e in p.examples_medium) + "</ul>"
    if p.examples_hard:
        examples += "<h4>Hard / Interview Examples</h4><ul>" + "".join(render_example(e, "Hard") for e in p.examples_hard) + "</ul>"

    triggers = ", ".join(f'"{t}"' for t in p.triggers[:8])
    algo = bullets(p.algorithm) if p.algorithm else ""
    mistakes = bullets(p.mistakes) if p.mistakes else ""
    edges = bullets(p.edge_cases) if p.edge_cases else ""

    return f"""
<div class="pattern-card {diff}" id="pattern-{p.num}">
  <div class="pattern-header">
    <span class="pattern-num">#{p.num}</span>
    <span class="pattern-category">{h(p.category)}</span>
    <label><input type="checkbox" id="pattern-done-{p.num}" data-track> Mastered (+10 XP)</label>
  </div>
  <h3>{h(p.name)}</h3>
  {curiosity(f"Why does {p.name} work? {p.intuition}")}
  <p><strong>Mental Model:</strong> {h(p.mental_model)}</p>
  {signal_box(triggers)}
  <p><strong>When to use:</strong> {h(p.when_use)}</p>
  {when_not(h(p.when_not))}
  <div class="grid-2">
    <div>
      <h4>Brute Force</h4><p>{h(p.brute_force)}</p>
      <h4>Key Observation</h4><p>{h(p.observation)}</p>
    </div>
    <div>
      <h4>Optimal Approach</h4><p>{h(p.optimal)}</p>
      <h4>Complexity</h4><p>Time: <code>{h(p.time)}</code> · Space: <code>{h(p.space)}</code></p>
    </div>
  </div>
  <h4>Algorithm</h4>{algo}
  <h4>Java Template</h4>{code_block(p.java_template)}
  <h4>Common Mistakes</h4>{mistakes}
  <h4>Edge Cases</h4>{edges}
  {examples}
  <p><strong>30-Second Recognition:</strong> {h(p.recognize_30s)}</p>
  {trap(h(p.trap))}
  {interview(f"Follow-up: {p.followup} · Variation: {p.variation}")}
</div>"""


def build_pattern_section() -> str:
    patterns = get_all_patterns()
    by_cat: dict[str, list[Pattern]] = {}
    for p in patterns:
        by_cat.setdefault(p.category, []).append(p)

    body = "<p><em>64 reusable frameworks — not 300 random problems. Some problems combine multiple patterns.</em></p>"
    for cat, plist in by_cat.items():
        body += f"<h3>{h(cat)}</h3>"
        for p in plist:
            body += render_pattern_card(p)
    return body
