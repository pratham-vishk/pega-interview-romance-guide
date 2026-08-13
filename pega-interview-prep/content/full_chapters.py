"""Render comprehensive chapters from all_topics data."""

from content.all_topics import CHAPTERS
from content.helpers import simple, flirt_ex, cheat, qa, render_subtopics, chapter_wrap


def build_all_full_chapters(d) -> str:
    """d is callable: d(diagram_key, caption) -> HTML for diagram."""
    parts = []
    for num in sorted(CHAPTERS.keys()):
        parts.append(render_chapter(num, CHAPTERS[num], d))
    parts.append(master_cheat_sheet())
    return "\n".join(parts)


def render_chapter(num: int, ch: dict, d) -> str:
    body_parts = [
        simple(ch["intro_simple"]),
        flirt_ex(ch["flirty"]),
    ]
    for key, caption in ch.get("diagrams", []):
        body_parts.append(d(key, caption))
    body_parts.append(render_subtopics(ch["subtopics"]))
    body_parts.append(cheat(ch["title"].split("—")[0].strip(), ch["cheat"]))
    for q, a in ch["qa"]:
        body_parts.append(qa(q, a))
    teaser_idx = (num - 1) % 5
    return chapter_wrap(num, ch["title"], "\n".join(body_parts), teaser_idx)


def master_cheat_sheet():
    return """
<div class="chapter" id="master-cheat">
<h2>🏆 Master Interview Cheat Sheet — Every Topic One Glance</h2>
<div class="flirt-box">You survived 27 chapters and hundreds of subtopics. This page is your morning-of-interview love note. Read it. Own the room. 💕</div>
<table>
<tr><th>Topic</th><th>Complete One-Line Answer</th></tr>
<tr><td>Rule Resolution</td><td>10 steps: class → name → ruleset → remove NA/blocked → specificity → version → circumstance → available → FUA cache</td></tr>
<tr><td>Data Page</td><td>Smart cached fetcher — readonly/editable/list/singleton — prefer over activity</td></tr>
<tr><td>Data Transform</td><td>Declarative mapping — Set/When/ForEach — always before activity</td></tr>
<tr><td>Flow vs Flow Action</td><td>Flow = backend automation. Flow Action = user button + screen</td></tr>
<tr><td>Worklist vs Basket</td><td>Personal queue vs team shared pool</td></tr>
<tr><td>Page List vs Group</td><td>Integer index ordered vs string key unordered</td></tr>
<tr><td>When vs Dec Table</td><td>One condition vs grid of combinations</td></tr>
<tr><td>Declare Expression</td><td>Auto-computed property — forward chaining</td></tr>
<tr><td>Connect vs Service</td><td>Outbound vs inbound integration</td></tr>
<tr><td>Security chain</td><td>Operator → Access Group → Role → Privilege → Access When</td></tr>
<tr><td>SLA intervals</td><td>Goal → Deadline → Passed Deadline + urgency increase</td></tr>
<tr><td>Constellation</td><td>React UI — Views, Theme, DX API — replaces Section/Harness</td></tr>
<tr><td>PAL / Tracer</td><td>PAL first for metrics. Tracer for step-by-step rule trace</td></tr>
<tr><td>RAP / DevOps</td><td>Export zip → import via Deployment Manager pipeline</td></tr>
<tr><td>Guardrail #1</td><td>Prefer Data Transform over Activity — always say it</td></tr>
<tr><td>pyWorkPage</td><td>Current case data on clipboard</td></tr>
<tr><td>pxRequestor</td><td>Logged-in user session context</td></tr>
<tr><td>pxThread</td><td>Open assignments in session</td></tr>
<tr><td>pzInsKey</td><td>Unique instance key — Obj-Open-By-Handle</td></tr>
<tr><td>N+1 problem</td><td>Loop DB calls — fix with batch Data Page or Report Def join</td></tr>
<tr><td>Branch / Merge</td><td>Parallel dev stream — merge to target ruleset when ready</td></tr>
<tr><td>Circumstance</td><td>Rule variant by date or property value</td></tr>
<tr><td>Pattern inheritance</td><td>Auto parent from class namespace</td></tr>
<tr><td>Directed inheritance</td><td>Manual parent class for cross-app reuse</td></tr>
<tr><td>Class Group</td><td>Work pool — case types share pc_work table</td></tr>
<tr><td>FUA</td><td>Cached compiled rule after first resolution</td></tr>
<tr><td>Split-Join</td><td>Parallel branches then merge</td></tr>
<tr><td>Split-ForEach</td><td>Loop page list in flow</td></tr>
<tr><td>Queue-For-Agent</td><td>Defer processing to background agent</td></tr>
<tr><td>CDH / NBA</td><td>Next-Best-Action via Decision Strategies</td></tr>
</table>
</div>"""
