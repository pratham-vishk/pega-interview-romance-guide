"""HTML building blocks for rich Pega interview chapters."""

def simple(text: str) -> str:
    return f'<div class="easy-box"><strong>💡 In Simple Words:</strong> {text}</div>'

def flirt_ex(text: str) -> str:
    return f'<div class="flirty-example"><strong>💋 Flirty Real Example:</strong> {text}</div>'

def cheat(title: str, rows: list[tuple[str, str]]) -> str:
    trs = "".join(f"<tr><td><strong>{k}</strong></td><td>{v}</td></tr>" for k, v in rows)
    return f'<h4>📋 Cheat Sheet — {title}</h4><table><tr><th>Term</th><th>Remember This</th></tr>{trs}</table>'

def qa(q: str, a: str) -> str:
    return f'<div class="qa-block"><div class="question">Q: {q}</div><div class="answer">{a}</div></div>'

def section(title: str, body: str) -> str:
    return f"<h3>{title}</h3>{body}"

def bullets(items: list[str]) -> str:
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"

def chapter_wrap(num: int, title: str, hook_fn, body: str, teaser_idx: int) -> str:
    from content.flirty_content import flirt_box, curiosity_teaser
    return f'<div class="chapter" id="ch{num}"><h2>Chapter {num}: {title}</h2>{flirt_box(num)}{body}{curiosity_teaser(teaser_idx)}</div>'
