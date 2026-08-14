"""Assemble complete Interview OS HTML."""

from content.cheat_sheets import build_cheat_sheets
from content.day_plans import build_day_plans, build_next_83_days
from content.gamification import build_gamification
from content.hld import build_hld_section
from content.interview_mode import build_interview_mode
from content.java_templates import build_java_section
from content.lld import build_lld_section
from content.pattern_cards import build_pattern_section
from content.recognition import build_diagnosis_cheatsheet, build_recognition_section
from content.resume_context import build_resume_section
from content.styles import INTERACTIVE_JS, STYLES


def build_toc() -> str:
    sections = [
        ("philosophy", "Core Philosophy"),
        ("recognition", "Pattern Recognition Engine"),
        ("patterns", "DSA Pattern Cards (64)"),
        ("java-templates", "Java Templates"),
        ("lld", "Low-Level Design"),
        ("hld", "High-Level Design"),
        ("resume", "Resume Deep Dive"),
        ("7-day-plan", "7-Day Plan"),
        ("interview-mode", "Interview Simulation"),
        ("gamification", "Gamification"),
        ("next-83", "Next 83 Days"),
        ("cheat-sheets", "Master Cheat Sheets"),
    ]
    items = "".join(f'<li><a href="#{sid}">{title}</a></li>' for sid, title in sections)
    return f"""
<div class="toc" id="toc">
<h2>📋 Interview Operating System — Navigation</h2>
<p>Click to jump. Checkboxes save progress in browser (localStorage).</p>
<ol>{items}</ol>
</div>"""


def build_philosophy() -> str:
    return """
<div class="section" id="philosophy">
<h2>Core Philosophy</h2>
<div class="curiosity">Why compress DSA into ~50 patterns? Because interviews test recognition + reasoning, not memorizing 300 solutions.</div>
<p><strong>Your goal in 7 days:</strong> Build a mental framework to answer:</p>
<ol>
<li>What pattern is this?</li>
<li>Why does that pattern apply?</li>
<li>What is the brute-force solution?</li>
<li>What observation eliminates brute force?</li>
<li>What data structure/algorithm should I use?</li>
<li>What is optimal time and space complexity?</li>
<li>What edge cases can break my solution?</li>
<li>How would I explain this in a Google interview?</li>
<li>How would I extend if constraints change?</li>
</ol>
<p><em>These are reusable frameworks — some problems combine multiple patterns. Deep understanding beats excessive content.</em></p>
<h3>L4 vs L5 Expectations</h3>
<table>
<tr><th>L4</th><th>L5</th></tr>
<tr><td>Recognize patterns, optimal solutions, clean Java</td><td>Trade-off analysis, scale 10x, org-level decisions</td></tr>
<tr><td>Complete LLD with SOLID</td><td>Multi-tenant, observability, migration strategy</td></tr>
<tr><td>End-to-end HLD with estimation</td><td>Multi-region consistency, cost, failure domains</td></tr>
</table>
</div>"""


def build_nav() -> str:
    return """
<nav class="nav-sidebar">
<strong>Quick Nav</strong>
<a href="#toc">TOC</a>
<a href="#philosophy">Philosophy</a>
<a href="#recognition">Recognition</a>
<a href="#patterns">Patterns</a>
<a href="#java-templates">Java</a>
<a href="#lld">LLD</a>
<a href="#hld">HLD</a>
<a href="#resume">Resume</a>
<a href="#7-day-plan">7-Day Plan</a>
<a href="#interview-mode">Mock</a>
<a href="#cheat-sheets">Cheats</a>
</nav>"""


def build_cover() -> str:
    return """
<div class="cover">
<span class="badge">BILKUL</span>
<h1>GOOGLE SWE 90-DAY<br>INTERVIEW OPERATING SYSTEM</h1>
<p class="subtitle">7-Day Pattern Mastery + LLD + HLD + Interview Simulation</p>
<p class="tagline">From Pattern Recognition → Problem Solving → System Design → Interview Ready</p>
<p>
<span class="badge">64 Patterns</span>
<span class="badge">Java Templates</span>
<span class="badge">LLD + HLD</span>
<span class="badge">Resume Deep Dive</span>
<span class="badge">Mock Interviews</span>
</p>
<p class="tagline">Target: Google SWE L4 (L5 stretch) · Java Backend · 8-10 hrs/day × 7 days first pass</p>
<p class="tagline"><strong>Optimized for active learning, recall, recognition — not passive reading.</strong></p>
</div>"""


def build_html() -> str:
    parts = [
        build_cover(),
        build_toc(),
        build_philosophy(),
        build_recognition_section(),
        build_diagnosis_cheatsheet(),
        f'<div class="section" id="patterns"><h2>DSA Pattern Cards</h2>{build_pattern_section()}</div>',
        build_java_section(),
        build_lld_section(),
        build_hld_section(),
        build_resume_section(),
        build_day_plans(),
        build_interview_mode(),
        build_gamification(),
        build_next_83_days(),
        build_cheat_sheets(),
        '<div class="footer">Bilkul · Google SWE Interview OS · Built for Pratham · Not affiliated with Google</div>',
    ]
    body = build_nav() + "".join(parts)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Google SWE 90-Day Interview Operating System — Bilkul</title>
<style>{STYLES}</style>
</head>
<body class="has-sidebar">
{body}
<script>{INTERACTIVE_JS}</script>
</body>
</html>"""
