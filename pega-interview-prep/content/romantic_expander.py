"""Expand thin subtopic stubs into full romantic, interview-ready explanations."""

import hashlib
import re

_ROMANTIC_OPENERS = [
    "Picture this, gorgeous —",
    "Think of it like planning the perfect date —",
    "Here's the tea, love —",
    "Between us —",
    "Sweetheart, imagine —",
    "Like a love letter written in rules —",
    "Real talk, darling —",
    "You and me at 2am studying Pega —",
]

_ROMANTIC_CLOSERS = [
    "That's the kind of clarity interviewers fall for. 💕",
    "Say it with confidence — you've got this.",
    "Drop that in interview and watch them smile.",
    "Romantic? Maybe. Correct? Absolutely.",
    "That's your 'I actually built this' moment.",
]

_PITFALL_STARTERS = [
    "Common mistake:",
    "Interview trap:",
    "Don't trip here:",
    "Red flag juniors miss:",
]

_CHAPTER_CONTEXT = {
    1: "platform architecture and how Pega layers work together",
    2: "class hierarchy, inheritance, and the rule resolution starting point",
    3: "rule resolution, versioning, and how Pega picks the right rule",
    4: "application stack, rulesets, versions, and deployment units",
    5: "case management, lifecycle, stages, and work objects",
    6: "flows, processes, flow actions, and automation shapes",
    7: "assignments, routing, workbaskets, and who gets the task",
    8: "clipboard pages, properties, and the in-memory data model",
    9: "data pages, sourcing, caching, and modern data access",
    10: "data transforms, mapping, and declarative clipboard changes",
    11: "activities, steps, and when (rarely) to use them",
    12: "decision rules — When, Decision Table, MapValue, Scorecard",
    13: "declare rules — expressions, constraints, triggers, indexes",
    14: "validation — validate rules, constraints, and error handling",
    15: "UI, portals, sections, views, and Constellation",
    16: "SLAs, urgency, goals, deadlines, and escalations",
    17: "integration — connectors, services, REST, and data types",
    18: "security — operators, roles, privileges, and access control",
    19: "agents, queues, and background processing",
    20: "reporting — report definitions, summaries, and drill-down",
    21: "testing — unit tests, scenario tests, and coverage",
    22: "performance, PAL, Tracer, and guardrails",
    23: "DevOps — branches, RAPs, pipelines, and deployment",
    24: "email, documents, correspondence, and attachments",
    25: "CDH, NBA, RPA, AI, and advanced Pega capabilities",
    26: "controls, field values, localization, and UI metadata",
    27: "object layer, persistence, Obj- methods, and database commits",
}


def _pick(seed: str, options: list[str]) -> str:
    idx = int(hashlib.md5(seed.encode()).hexdigest(), 16) % len(options)
    return options[idx]


def _clean(text: str) -> str:
    return re.sub(r"\s+", " ", (text or "").strip())


def _is_thin(details: str) -> bool:
    return len(_clean(details)) < 160


def _how_it_works(title: str, explain: str, details: str, chapter_num: int) -> str:
    ctx = _CHAPTER_CONTEXT.get(chapter_num, "Pega case and rule execution")
    base = _clean(explain)
    extra = _clean(details) if details and not _is_thin(details) else ""

    steps = (
        f"<strong>How it works:</strong> {base} "
        f"In the context of {ctx}, <em>{title}</em> is configured in Dev Studio (or App Studio where applicable) "
        f"and resolved at runtime using class inheritance, ruleset versioning, and the current clipboard context "
        f"(pyWorkPage, pxRequestor, or dedicated data pages). "
    )
    if extra:
        steps += extra + " "
    else:
        steps += (
            f"When a flow, flow action, activity, or integration calls it, Pega loads the rule, executes its logic, "
            f"and writes results back to the clipboard or returns a response — all within the same requestor session "
            f"unless an agent or async queue is involved. "
        )
    steps += (
        "Trace it in Tracer if you need proof; check PAL if you need performance numbers. "
        "That combo is how senior devs answer with receipts."
    )
    return steps


def _romantic_analogy(title: str, explain: str, chapter_num: int) -> str:
    opener = _pick(f"{chapter_num}:{title}", _ROMANTIC_OPENERS)
    closer = _pick(f"{title}:close", _ROMANTIC_CLOSERS)
    short = explain.split(".")[0].strip().lower()
    if not short:
        short = title.lower()
    return (
        f"<p class='flirt-sub'><strong>💋 Romantic analogy:</strong> {opener} "
        f"<em>{title}</em> is the thoughtful detail that keeps the whole {short} story on track — "
        f"like remembering her coffee order before she asks. Structured charm beats chaotic genius every time. "
        f"{closer}</p>"
    )


def _pitfalls(title: str, tip: str, chapter_num: int) -> str:
    starter = _pick(f"pitfall:{title}", _PITFALL_STARTERS)
    tip_text = _clean(tip) if tip else f"confusing {title} with a similar-sounding Pega concept"
    return (
        f"<p class='warning'><strong>⚠️ {starter}</strong> {tip_text}. "
        f"In interview, name the exact rule type, when you use it, and what you use <em>instead</em> when guardrails say no.</p>"
    )


def _interview_angle(title: str, explain: str, tip: str) -> str:
    tip_line = _clean(tip) if tip else f"Explain {title} with a real project example — case type, class, and outcome."
    return (
        f"<p class='tip'><strong>🎯 Interview gold:</strong> {tip_line} "
        f"Lead with one sentence definition, one real scenario, one guardrail you followed. "
        f"That's the CSA/SSA sweet spot.</p>"
    )


def expand_subtopic(
    chapter_num: int,
    title: str,
    explain: str,
    details: str = "",
    interview_tip: str = "",
) -> dict[str, str]:
    """Return rich HTML fragments for a comprehensive subtopic block."""
    what = _clean(explain)
    how = _how_it_works(title, explain, details, chapter_num)
    return {
        "what": what,
        "how": how,
        "romantic": _romantic_analogy(title, explain, chapter_num),
        "pitfall": _pitfalls(title, interview_tip, chapter_num),
        "tip": _interview_angle(title, explain, interview_tip),
    }
