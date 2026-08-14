"""7-day intensive plan + next 83 days."""

from content.helpers import bullets, checklist, quiz, section, table, tip


DAYS = [
    {
        "day": 1,
        "title": "Arrays + Hashing + Two Pointers + Sliding Window",
        "patterns": "1-10",
        "problems": 12,
        "categories": ["Frequency Map", "Prefix Sum", "Two Pointers", "Sliding Window fixed/variable", "Kadane", "Intervals"],
        "blocks": ["2h Pattern Cards 1-10", "2h Recognition drills", "2h Solve 6 mediums", "1h Active recall quiz", "1h Revision + EOD test"],
        "recall": ["When HashMap vs Prefix Sum?", "Fixed vs variable sliding window?", "Two pointer on unsorted?"],
        "pass": "Recognize 8/10 patterns in 30s; solve 4/6 mediums with optimal complexity",
    },
    {
        "day": 2,
        "title": "Binary Search + Linked List + Stack + Queue + Heap",
        "patterns": "11-30",
        "problems": 12,
        "categories": ["Binary Search variants", "Linked List", "Monotonic Stack/Queue", "Heap Top-K", "K-way Merge"],
        "blocks": ["2h Patterns 11-30 cards", "2h Java templates practice", "2h 6 problems", "1h Monotonic stack drills", "1h EOD test"],
        "recall": ["BS on answer vs classic BS?", "When monotonic stack?", "Min-heap for top K largest?"],
        "pass": "Implement 5 templates from memory; 4/6 problems optimal",
    },
    {
        "day": 3,
        "title": "Trees + BST + Recursion + Backtracking",
        "patterns": "31-49",
        "problems": 10,
        "categories": ["DFS/BFS tree", "LCA", "BST", "Backtracking subsets/perms"],
        "blocks": ["2h Tree patterns", "2h Backtracking framework", "2h 5 tree + 3 backtrack problems", "1h Recursion → iterative", "1h EOD test"],
        "recall": ["BST validation approach?", "Backtrack template?", "When tree DP?"],
        "pass": "Solve LCA + one backtracking medium; explain recursion stack depth",
    },
    {
        "day": 4,
        "title": "Graphs + BFS + DFS + Topo Sort + DSU + Shortest Path",
        "patterns": "38-45",
        "problems": 10,
        "categories": ["Grid BFS", "Topo sort", "Union Find", "Dijkstra", "Cycle detection"],
        "blocks": ["2h Graph patterns", "2h Template coding", "2h 6 graph problems", "1h Dijkstra vs BFS", "1h EOD test"],
        "recall": ["BFS vs Dijkstra?", "When Union Find?", "Detect cycle directed?"],
        "pass": "Implement Dijkstra + Topo from memory; 4/6 graph problems",
    },
    {
        "day": 5,
        "title": "Greedy + DP + Trie + Bit Manipulation + Advanced",
        "patterns": "50-64",
        "problems": 10,
        "categories": ["Greedy proof", "1D/2D DP", "Knapsack", "Trie", "Bit tricks", "Combo patterns"],
        "blocks": ["2h DP state definition drills", "2h Advanced patterns", "2h 6 DP/Greedy problems", "1h Bit manipulation", "1h EOD test"],
        "recall": ["Define DP state before code?", "Greedy vs DP decision?", "When trie?"],
        "pass": "Solve 3 DP mediums; explain state transition aloud",
    },
    {
        "day": 6,
        "title": "LLD Framework + Design Patterns + 3 Major Problems",
        "patterns": "LLD",
        "problems": 3,
        "categories": ["SOLID", "11 design patterns", "Parking Lot", "Elevator", "Rate Limiter"],
        "blocks": ["2h SOLID + patterns", "2h Parking Lot full design", "2h Elevator + Rate Limiter", "1h UML practice", "1h Mock LLD"],
        "recall": ["SRP example?", "Strategy vs Factory?", "Rate limiter algorithms?"],
        "pass": "Complete Parking Lot class diagram + Java skeleton in 45 min",
    },
    {
        "day": 7,
        "title": "HLD Framework + 5 System Designs + Full Mock Interview",
        "patterns": "HLD",
        "problems": 5,
        "categories": ["URL Shortener", "Chat", "YouTube", "Uber", "Notification System"],
        "blocks": ["2h HLD framework review", "3h 5 system designs (35 min each)", "2h Full mock (DSA + SD)", "1h Cheat sheet revision", "1h GOOGLE READY checklist"],
        "recall": ["Estimate QPS formula?", "Kafka use case?", "Cache invalidation?"],
        "pass": "Complete 2 system designs end-to-end; mock interview score ≥70%",
    },
]


def build_day_plans() -> str:
    body = "<p><strong>8–10 focused hours/day.</strong> Goal: complete mental map, not 300 problems.</p>"
    for d in DAYS:
        cid_base = f"day{d['day']}"
        items = [(f"{cid_base}-block-{i}", b) for i, b in enumerate(d["blocks"])]
        body += f"""
<div class="day-card" id="day-{d['day']}">
<h3>DAY {d['day']}: {d['title']}</h3>
<p><strong>Patterns:</strong> {d['patterns']} · <strong>Problems:</strong> {d['problems']}</p>
<h4>Learning Blocks</h4>{checklist(items)}
<h4>Problem Categories</h4>{bullets(d['categories'])}
<h4>Active Recall</h4>{bullets(d['recall'])}
<h4>30-Min Revision</h4>
<p>Re-read pattern cards for today. Close laptop. Recite triggers from memory.</p>
<h4>End-of-Day Test</h4>
<p>5 recognition drills + 2 problems timed (45 min each for Day 7 mock).</p>
<h4>Pass Criteria</h4>
<p>{d['pass']}</p>
<div class="reflection" contenteditable="true">Daily reflection: What was hardest? What pattern did I miss?</div>
<label><input type="checkbox" id="{cid_base}-complete" data-track> Day {d['day']} Complete (+100 XP Boss Battle)</label>
</div>"""
        body += quiz(
            f"Day {d['day']}: Name 3 pattern triggers from today's topics.",
            f"Review patterns {d['patterns']}: {', '.join(d['categories'][:3])}",
            f"day{d['day']}-quiz",
        )
    return section("7-day-plan", "7-Day Ultra-Intensive Plan", body)


def build_next_83_days() -> str:
    phases = [
        ("Days 8-21", "Spaced repetition — revisit each pattern category every 3 days"),
        ("Days 22-45", "Problem solving — 3 mediums/day, focus weak patterns"),
        ("Days 46-60", "System design depth — 1 design/day with follow-ups"),
        ("Days 61-75", "Mock interviews — 3x/week full loop"),
        ("Days 76-90", "Resume deep dives + Google-specific prep + rest"),
    ]
    body = "<h3>After the 7-Day First Pass</h3>"
    body += table(["Phase", "Focus"], phases)
    body += bullets([
        "Weekly: 1 full mock interview (DSA + LLD or HLD)",
        "Daily: 30 min pattern flashcards",
        "Track weak patterns in Weakness Tracker",
        "Revisit resume bullets with STAR stories",
        "Target: 80+ problems with pattern recognition, not 300 blind solves",
    ])
    return section("next-83", "Next 83 Days — Repetition & Depth", body)
