"""HTML building blocks for rich Pega interview chapters."""

from content.romantic_expander import expand_subtopic

def simple(text: str) -> str:
    return f'<div class="easy-box"><strong>💡 In Simple Words:</strong> {text}</div>'

def flirt_ex(text: str) -> str:
    return f'<div class="flirty-example"><strong>💋 Flirty Real Example:</strong> {text}</div>'

def subtopic(
    title: str,
    explain: str,
    details: str = "",
    interview_tip: str = "",
    chapter_num: int = 0,
) -> str:
    rich = expand_subtopic(chapter_num, title, explain, details, interview_tip)
    return f"""<div class="subtopic-block">
<h4>▸ {title}</h4>
<p><strong>What it is:</strong> {rich["what"]}</p>
<p>{rich["how"]}</p>
{rich["romantic"]}
{rich["pitfall"]}
{rich["tip"]}</div>"""

def cheat(title: str, rows: list[tuple[str, str]]) -> str:
    trs = "".join(f"<tr><td><strong>{k}</strong></td><td>{v}</td></tr>" for k, v in rows)
    return f'<h3>📋 Cheat Sheet — {title}</h3><table><tr><th>Term</th><th>Remember This</th></tr>{trs}</table>'

def qa(q: str, a: str) -> str:
    return f'<div class="qa-block"><div class="question">Q: {q}</div><div class="answer">{a}</div></div>'

def section(title: str, body: str) -> str:
    return f"<h3>{title}</h3>{body}"

def bullets(items: list[str]) -> str:
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"

def chapter_wrap(num: int, title: str, body: str, teaser_idx: int) -> str:
    from content.flirty_content import flirt_box, curiosity_teaser
    return f'<div class="chapter" id="ch{num}"><h2>Chapter {num}: {title}</h2>{flirt_box(num)}{body}{curiosity_teaser(teaser_idx)}</div>'

def render_subtopics(items: list[tuple], chapter_num: int = 0) -> str:
    """Each item: (title, explain, details, interview_tip) - tip optional"""
    out = (
        "<h3>📖 Every Subtopic — Complete Explanation (Nothing Skipped)</h3>"
        "<p><em>Each topic below: what it is · how it works · romantic analogy · pitfalls · interview tip.</em></p>"
    )
    for item in items:
        title, explain = item[0], item[1]
        details = item[2] if len(item) > 2 else ""
        tip = item[3] if len(item) > 3 else ""
        out += subtopic(title, explain, details, tip, chapter_num)
    return out
