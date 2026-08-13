"""Compact but complete subtopic text — romantic, interview-ready, ~150 pages total."""

import hashlib
import re

_ROMANTIC_LINES = [
    "Like remembering the little details on a perfect date — it just works. 💕",
    "Structured charm beats chaotic coding every time.",
    "Sweet, simple, and interview-panel approved.",
    "The kind of clarity that makes interviewers smile.",
    "Low drama, high guardrails — my favorite combo.",
]

_MISTAKE_LINES = [
    "Confusing it with a similar rule type — name the exact difference.",
    "Using Activity when Data Transform would do — guardrail violation.",
    "Forgetting class inheritance in the explanation.",
    "No real project example — always have one ready.",
    "Skipping the 'when NOT to use it' part of the answer.",
]

_CHAPTER_CONTEXT = {
    1: "platform layers", 2: "class hierarchy", 3: "rule resolution",
    4: "application stack", 5: "case lifecycle", 6: "flows and processes",
    7: "assignments", 8: "clipboard", 9: "data pages", 10: "data transforms",
    11: "activities", 12: "decision rules", 13: "declare rules", 14: "validation",
    15: "UI and Constellation", 16: "SLAs", 17: "integration", 18: "security",
    19: "agents", 20: "reporting", 21: "testing", 22: "performance",
    23: "DevOps", 24: "correspondence", 25: "CDH and AI", 26: "controls",
    27: "object persistence",
}


def _clean(text: str) -> str:
    return re.sub(r"\s+", " ", (text or "").strip())


def _pick(seed: str, options: list[str]) -> str:
    return options[int(hashlib.md5(seed.encode()).hexdigest(), 16) % len(options)]


def compact_subtopic_text(
    title: str,
    explain: str,
    details: str = "",
    interview_tip: str = "",
    chapter_num: int = 0,
) -> tuple[str, str, str, str, str]:
    """Return (definition, practice_line, romantic_line, mistake_line, tip_line)."""
    base = _clean(explain)
    extra = _clean(details)
    ctx = _CHAPTER_CONTEXT.get(chapter_num, "Pega runtime")

    if extra and len(extra) > 20:
        definition = f"{base} {extra}"
    else:
        definition = (
            f"{base} In {ctx}, <em>{title}</em> is configured in Dev Studio "
            f"and runs at request time against the clipboard (pyWorkPage / pxRequestor)."
        )

    practice = (
        f"<strong>In practice:</strong> Use {title} where business logic needs it — "
        f"trace with Tracer if behavior surprises you, check PAL if performance drops. "
        f"{_pick(title, _ROMANTIC_LINES)}"
    )

    romantic_line = (
        f"<strong>💋 Romantic take:</strong> {_pick(f'r:{title}', _ROMANTIC_LINES)}"
    )
    mistake_line = (
        f"<strong>⚠️ Watch out:</strong> {_pick(f'm:{title}', _MISTAKE_LINES)}"
    )

    tip = _clean(interview_tip) or f"Define {title}, give one real project example, name one guardrail."
    return definition, practice, romantic_line, mistake_line, tip
