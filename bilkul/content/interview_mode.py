"""Google Interview Simulation Mode."""

from content.helpers import quiz, section, tip


DSA_PROBLEMS = [
    {
        "id": "sim-1",
        "statement": "Given an array of integers, return indices of the two numbers that add up to target. Exactly one solution exists.",
        "pattern": "Frequency Map / HashMap",
        "hints": [
            "What information do you need at each index?",
            "Can you avoid checking all pairs?",
            "Store complement in a map as you iterate.",
        ],
        "solution": "O(n) HashMap: for each nums[i], check if target-nums[i] exists in map.",
    },
    {
        "id": "sim-2",
        "statement": "Given a string, find the length of the longest substring without repeating characters.",
        "pattern": "Sliding Window — Variable",
        "hints": [
            "Is the answer contiguous?",
            "What makes a window invalid?",
            "Shrink from left when duplicate found.",
        ],
        "solution": "Variable sliding window with HashMap char→last index. O(n).",
    },
    {
        "id": "sim-3",
        "statement": "Design a rate limiter that allows at most N requests per user per minute.",
        "pattern": "HLD — Rate Limiter",
        "hints": [
            "Clarify: per user? distributed?",
            "Token bucket vs sliding window?",
            "Where to store counters?",
        ],
        "solution": "Redis sliding window or token bucket; key=user_id:minute; return 429 when exceeded.",
    },
]


def build_interview_mode() -> str:
    body = tip("Interview Mode: cover the 'Pattern' and 'Solution' columns. Think aloud first. Reveal hints only when stuck.")
    body += "<h3>DSA Simulation</h3>"
    for p in DSA_PROBLEMS:
        hints_html = "<ol>" + "".join(f"<li>{h}</li>" for h in p["hints"]) + "</ol>"
        body += f"""
<div class="pattern-card" id="{p['id']}">
<h4>Problem (Pattern Hidden)</h4>
<p>{p['statement']}</p>
<p><strong>Think aloud. What do you notice?</strong></p>
<div class="reflection" contenteditable="true">Your approach notes...</div>
<details><summary>Hint 1 (click only if stuck)</summary>{p['hints'][0]}</details>
<details><summary>Hint 2</summary>{p['hints'][1]}</details>
<details><summary>Hint 3</summary>{p['hints'][2]}</details>
<details><summary>Reveal Pattern</summary><strong>{p['pattern']}</strong></details>
<details><summary>Reveal Solution</summary>{p['solution']}</details>
<button class="btn" data-add-xp="100" type="button">Mark Mock Complete (+100 XP)</button>
</div>"""

    body += "<h3>System Design Simulation</h3>"
    body += """
<div class="pattern-card">
<h4>Design a Chat System (like Google Chat)</h4>
<p><strong>Do NOT look at architecture yet. Answer these first:</strong></p>
<ol>
<li>What requirements do you clarify? (1:1, groups, online status, history?)</li>
<li>What scale? (DAU, messages/sec)</li>
<li>What API endpoints?</li>
<li>What storage for messages?</li>
<li>How real-time delivery? (WebSocket, push)</li>
<li>What fails? How recover?</li>
</ol>
<div class="reflection" contenteditable="true">Your design notes...</div>
<details><summary>Reveal Architecture Hints</summary>
<p>WebSocket gateway → Chat Service → Message DB (sharded by conversation_id) → Kafka for async (notifications, search indexing) → Redis for presence/online status.</p>
</details>
<button class="btn" data-add-xp="100" type="button">Mark SD Mock Complete (+100 XP)</button>
</div>"""

    body += "<h3>Mock Interview Scorecard</h3>"
    body += """
<table class="mock-scorecard">
<tr><th>Criteria</th><th>Score (1-5)</th></tr>
<tr><td>Problem understanding</td><td><input type="number" min="1" max="5"></td></tr>
<tr><td>Pattern recognition</td><td><input type="number" min="1" max="5"></td></tr>
<tr><td>Brute force → optimization</td><td><input type="number" min="1" max="5"></td></tr>
<tr><td>Correctness</td><td><input type="number" min="1" max="5"></td></tr>
<tr><td>Complexity analysis</td><td><input type="number" min="1" max="5"></td></tr>
<tr><td>Code quality (Java)</td><td><input type="number" min="1" max="5"></td></tr>
<tr><td>Communication</td><td><input type="number" min="1" max="5"></td></tr>
</table>"""
    body += quiz("After mock: what pattern did you miss most?", "Log it in Weakness Tracker and schedule spaced revision.", "mock-debrief")
    return section("interview-mode", "Google Interview Simulation Mode", body)
