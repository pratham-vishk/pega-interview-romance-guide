"""HTML building blocks for Interview OS."""

from html import escape


def h(text: str) -> str:
    return escape(str(text))


def section(id_: str, title: str, body: str, css_class: str = "section") -> str:
    return f'<div class="{css_class}" id="{h(id_)}"><h2>{h(title)}</h2>{body}</div>'


def subsection(title: str, body: str) -> str:
    return f"<h3>{h(title)}</h3>{body}"


def bullets(items: list[str]) -> str:
    return "<ul>" + "".join(f"<li>{item}</li>" for item in items) + "</ul>"


def table(headers: list[str], rows: list[list[str]]) -> str:
    th = "".join(f"<th>{h(c)}</th>" for c in headers)
    trs = "".join(
        "<tr>" + "".join(f"<td>{cell}</td>" for cell in row) + "</tr>"
        for row in rows
    )
    return f"<table><tr>{th}</tr>{trs}</table>"


def code_block(code: str, lang: str = "java") -> str:
    return f'<div class="code-block" data-lang="{h(lang)}">{h(code)}</div>'


def signal_box(text: str) -> str:
    return f'<div class="signal-box"><strong>🎯 Recognition Signals:</strong> {text}</div>'


def curiosity(text: str) -> str:
    return f'<div class="curiosity">🤔 {text}</div>'


def tip(text: str) -> str:
    return f'<div class="tip">💡 {text}</div>'


def trap(text: str) -> str:
    return f'<div class="trap">⚠️ Trap: {text}</div>'


def interview(text: str) -> str:
    return f'<div class="interview">🎤 Interview: {text}</div>'


def when_not(text: str) -> str:
    return f'<div class="when-not"><strong>When NOT to use:</strong> {text}</div>'


def quiz(question: str, answer: str, qid: str) -> str:
    return f"""
<div class="quiz" id="quiz-{h(qid)}">
  <strong>Quiz:</strong> {question}
  <button class="btn quiz-reveal" type="button">Reveal Answer</button>
  <div class="quiz-answer">{answer}</div>
</div>"""


def checklist_item(cid: str, label: str) -> str:
    return f'<label><input type="checkbox" id="{h(cid)}" data-track> {label}</label>'


def checklist(items: list[tuple[str, str]]) -> str:
    return '<div class="checklist">' + "".join(checklist_item(c, l) for c, l in items) + "</div>"
