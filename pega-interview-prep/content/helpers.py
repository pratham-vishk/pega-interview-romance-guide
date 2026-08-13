"""HTML building blocks for rich Pega interview chapters."""

from content.romantic_expander import compact_subtopic_text

def simple(text: str) -> str:
    return f'<div class="easy-box"><strong>💡 In Simple Words:</strong> {text}</div>'

def flirt_ex(text: str) -> str:
    return f'<div class="flirty-example"><strong>💋 Flirty Real Example:</strong> {text}</div>'

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
    """Readable blocks — every subtopic covered, ~150-page sweet spot."""
    out = (
        "<h3>📖 All Subtopics — Complete Coverage</h3>"
        "<p><em>Every topic below: definition, how it works, and interview tip.</em></p>"
    )
    for item in items:
        title, explain = item[0], item[1]
        details = item[2] if len(item) > 2 else ""
        tip = item[3] if len(item) > 3 else ""
        answer, practice, romantic, mistake, tip_cell = compact_subtopic_text(
            title, explain, details, tip, chapter_num
        )
        out += (
            f'<div class="subtopic-compact">'
            f'<strong>{title}</strong> — {answer}'
            f'<br>{practice}'
            f'<br>{romantic}'
            f'<br>{mistake}'
            f'<br><span class="subtopic-tip">🎯 Interview: {tip_cell}</span>'
            f"</div>"
        )
    return out
