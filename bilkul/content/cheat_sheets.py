"""Final master cheat sheets."""

from content.helpers import section


CHEAT_SHEETS = {
    "DSA Pattern Recognition Map": """
<ul>
<li>Array sorted → BS / Two Ptr</li>
<li>Contiguous → Window / Prefix</li>
<li>Count/freq → HashMap</li>
<li>Top K → Heap</li>
<li>Next greater → Mono Stack</li>
<li>Intervals → Sort + Merge / Sweep</li>
<li>Tree → DFS/BFS/DP</li>
<li>Graph shortest unweighted → BFS</li>
<li>Weighted → Dijkstra</li>
<li>Deps → Topo</li>
<li>Connectivity → UF</li>
<li>All combos → Backtrack</li>
<li>Optimal substructure → DP</li>
<li>Min-max answer → BS on Answer</li>
</ul>""",
    "Big-O Cheat Sheet": """
<table>
<tr><th>Structure</th><th>Access</th><th>Search</th><th>Insert</th><th>Delete</th></tr>
<tr><td>Array</td><td>O(1)</td><td>O(n)</td><td>O(n)</td><td>O(n)</td></tr>
<tr><td>HashMap</td><td>—</td><td>O(1)*</td><td>O(1)*</td><td>O(1)*</td></tr>
<tr><td>Balanced BST</td><td>—</td><td>O(log n)</td><td>O(log n)</td><td>O(log n)</td></tr>
<tr><td>Heap</td><td>min O(1)</td><td>O(n)</td><td>O(log n)</td><td>O(log n)</td></tr>
</table>
<p>Sort: O(n log n). BFS/DFS: O(V+E). Dijkstra: O((V+E) log V). UF: α(n).</p>""",
    "Java DSA Templates": """
<p>HashMap freq · Deque stack · PriorityQueue heap · BS template · BFS queue · DFS recursive · UF · Dijkstra PQ</p>
<p>See Java Templates section for full code.</p>""",
    "LLD Design Principles": """
<ul><li>SOLID</li><li>Composition > Inheritance</li><li>Interface segregation</li><li>DI via constructor</li><li>Immutability where possible</li></ul>""",
    "Design Patterns Map": """
<p>Creational: Factory, Builder | Structural: Adapter, Decorator, Facade | Behavioral: Strategy, Observer, Command, State</p>""",
    "HLD Building Blocks": """
<p>CDN → LB → Gateway → Service → Cache/DB/Kafka → Monitoring</p>""",
    "System Design Checklist": """
<ol>
<li>Requirements (functional + NFR)</li><li>Estimation (QPS, storage)</li><li>API design</li>
<li>Architecture diagram</li><li>Data model</li><li>Scaling</li><li>Caching</li>
<li>Async (Kafka)</li><li>Failure handling</li><li>Consistency</li><li>Security</li><li>Monitoring</li>
</ol>""",
    "Google Interview Checklist": """
<ul>
<li>Clarify input/output/constraints</li><li>Brute force first</li><li>Optimize with pattern</li>
<li>State complexity</li><li>Code cleanly in Java</li><li>Test edge cases</li><li>Think aloud</li>
</ul>""",
    "What to Say When Stuck": """
<ul>
<li>"Let me clarify the constraints..."</li>
<li>"Brute force would be O(n²) by..."</li>
<li>"The bottleneck is... I'm thinking [pattern] because..."</li>
<li>"Let me trace through an example..."</li>
<li>"Edge case: empty input / single element / duplicates"</li>
</ul>""",
    "Last-Day Revision Sheet": """
<ol>
<li>30s diagnosis framework</li><li>Top 10 patterns you miss</li><li>Java templates on paper</li>
<li>2 system designs sketched</li><li>Resume STAR stories</li><li>Sleep well</li>
</ol>""",
}


def build_cheat_sheets() -> str:
    body = ""
    for i, (title, content) in enumerate(CHEAT_SHEETS.items(), 1):
        body += f'<div class="pattern-card" id="cheat-{i}"><h3>{title}</h3><div class="cheat-sheet">{content}</div></div>'
    return section("cheat-sheets", "Final Master Cheat Sheets", body)
