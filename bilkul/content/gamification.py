"""Gamification: XP, levels, boss battles, checklist."""

from content.helpers import checklist, section, table


LEVELS = [
    (1, "Pattern Explorer", 0, "Learn first 15 patterns"),
    (2, "Pattern Recognizer", 500, "30s recognition on 30 patterns"),
    (3, "Problem Solver", 1500, "Solve 20 mediums without hints"),
    (4, "Interview Solver", 3000, "Complete 5 mock DSA rounds"),
    (5, "System Designer", 5000, "Complete 8 system designs"),
    (6, "Google Ready", 8000, "Pass full mock + checklist 90%"),
]

XP_RULES = [
    ("Pattern learned (checkbox)", 10),
    ("Problem solved without help", 20),
    ("Hard problem solved", 40),
    ("Pattern recognized <30s", 25),
    ("System design completed", 50),
    ("Mock interview completed", 100),
    ("Day boss battle complete", 100),
    ("Quiz answer revealed (recall)", 5),
]


def build_gamification() -> str:
    body = """
<div class="progress-tracker">
  <span class="level-badge">Level: <span data-level-display>Pattern Explorer</span></span>
  <span>XP: <span data-xp-display>0</span> / 8000</span>
  <div class="xp-bar" style="flex:1;max-width:200px"><div class="xp-fill" data-xp-bar></div></div>
  <span>Streak: track manually 🔥</span>
</div>"""
    body += "<h3>XP Rules</h3>" + table(["Action", "XP"], [(a, f"+{x}") for a, x in XP_RULES])
    body += "<h3>Level Progression</h3>" + table(
        ["Level", "Title", "XP Required", "Unlock"],
        [(str(l), t, str(xp), u) for l, t, xp, u in LEVELS],
    )
    body += "<h3>Boss Battles</h3><ul>"
    body += "<li>Day 1 Boss: 10 pattern recognition in 5 min</li>"
    body += "<li>Day 4 Boss: Graph problem + Dijkstra from memory</li>"
    body += "<li>Day 6 Boss: Parking Lot LLD in 45 min</li>"
    body += "<li>Day 7 Boss: Full mock interview</li></ul>"
    body += "<h3>Weakness Tracker</h3>"
    body += checklist([
        ("weak-dp", "DP — state definition"),
        ("weak-graph", "Graph — Dijkstra / Topo"),
        ("weak-tree", "Tree — LCA / Tree DP"),
        ("weak-heap", "Heap — K-way merge"),
        ("weak-sd", "System Design — estimation"),
        ("weak-lld", "LLD — concurrency"),
    ])
    body += "<h3>GOOGLE READY Checklist</h3>"
    body += checklist([
        ("ready-patterns", "Recognize 45+ patterns in 30 seconds"),
        ("ready-java", "Code BFS, DFS, BS, Heap, UF from memory"),
        ("ready-dp", "Solve 5 DP mediums with clear state definition"),
        ("ready-lld", "Complete 3 LLD designs with SOLID"),
        ("ready-hld", "Complete 5 system designs with estimation"),
        ("ready-resume", "Defend every resume bullet with STAR + metrics"),
        ("ready-comm", "Think aloud clearly under pressure"),
        ("ready-mock", "Score ≥70% on full mock interview"),
    ])
    return section("gamification", "Gamification & Progress", body)
