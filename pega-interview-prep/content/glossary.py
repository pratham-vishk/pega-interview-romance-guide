"""Pega glossary appendix — fills gaps and adds quick revision pages."""


def build_glossary_appendix() -> str:
    terms = [
        ("Access Group", "Bundles app, portal, roles, and work pools for an operator."),
        ("Access When", "ABAC rule — condition for granting access to cases or rules."),
        ("Activity", "Procedural rule with steps — use sparingly; prefer DT."),
        ("Agent", "Background process for async work — SLAs, email, queues."),
        ("App Studio", "Guided low-code UI for business developers."),
        ("Assignment", "Task waiting for user or system action."),
        ("Branch", "Isolated ruleset stream for parallel development."),
        ("Case Type", "Template for a business process — loan, claim, etc."),
        ("Circumstance", "Rule variant by date or property value."),
        ("Class Group", "Work pool — case types sharing pc_work table."),
        ("Clipboard", "In-memory pages during a Pega request."),
        ("Commit", "Persist staged DB changes in current transaction."),
        ("Connect-REST", "Outbound REST integration from Pega."),
        ("Constellation", "Modern React-based UI architecture."),
        ("Data Page", "Declarative cached data access — D_Name pattern."),
        ("Data Transform", "Declarative clipboard mapping rule."),
        ("Decision Table", "Grid of conditions → results."),
        ("Declare Expression", "Auto-computed property — forward chaining."),
        ("Dev Studio", "Full IDE for technical developers."),
        ("Directed Inheritance", "Manual parent class for cross-branch reuse."),
        ("Flow", "Backend process automation in a case."),
        ("Flow Action", "User-facing button + screen on a case."),
        ("FUA", "Full Rule Assembly — cached resolved rule."),
        ("Guardrails", "Best-practice warnings for risky designs."),
        ("Harness", "Traditional UI screen container."),
        ("Job Scheduler", "Modern scheduled background task (replaces some agents)."),
        ("MapValue", "One-input → one-output lookup rule."),
        ("Obj-Open", "Load DB instance onto clipboard."),
        ("Obj-Save", "Write clipboard page to database."),
        ("Operator", "Pega user account — Operator ID."),
        ("Page Group", "Named map of pages — string keys."),
        ("Page List", "Ordered list of pages — integer index."),
        ("Pattern Inheritance", "Automatic parent from class namespace."),
        ("Privilege", "Atomic permission — can create case, etc."),
        ("Property", "Field on a clipboard page."),
        ("pxRequestor", "Logged-in user context page."),
        ("pyWorkPage", "Current case data page."),
        ("pzInsKey", "Unique instance handle / DB key."),
        ("Queue-For-Agent", "Defer work to background agent queue."),
        ("RAP", "Ruleset Archive Package — export zip for deployment."),
        ("Report Definition", "SQL-based reporting rule."),
        ("Role", "Bundle of privileges assigned to operators."),
        ("Rule Resolution", "10-step algorithm to find the right rule."),
        ("Ruleset", "Versioned collection of rules — App:01-01-01."),
        ("Section", "Traditional UI fragment / layout."),
        ("Service-REST", "Inbound REST API exposed by Pega."),
        ("SLA", "Service Level Agreement — goal, deadline, escalation."),
        ("Split-ForEach", "Flow shape looping over a page list."),
        ("Split-Join", "Parallel flow branches that merge."),
        ("Stage", "Major phase in case lifecycle."),
        ("Tracer", "Rule-by-rule execution trace tool."),
        ("PAL", "Performance Analyzer — runtime metrics."),
        ("Utility Shape", "Flow step with no assignment — auto."),
        ("Validate Rule", "Server-side validation on flow action."),
        ("View", "Constellation UI component."),
        ("When Rule", "Boolean condition — true/false."),
        ("Workbasket", "Team shared assignment queue."),
        ("Worklist", "Personal assignment queue."),
    ]
    rows = "".join(
        f"<tr><td><strong>{k}</strong></td><td>{v}</td></tr>" for k, v in terms
    )
    return f"""
<div class="chapter" id="glossary">
<h2>📖 Appendix: Pega Glossary — Quick Revision</h2>
<div class="flirt-box">Fifty terms, fifty wins. Skim this the morning of your interview like a love note to yourself. 💕</div>
<table>{rows}</table>
</div>"""
