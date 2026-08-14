"""Pattern recognition engine + 30-second diagnosis."""

from content.helpers import bullets, code_block, quiz, section, table, tip


def build_recognition_section() -> str:
    tree = """
<div class="diagram-box">
<pre style="text-align:left;font-size:8pt;color:#c9d1d9;">
START: Read problem
│
├─ Input sorted? ──────────────────► Binary Search / Two Pointers
├─ Contiguous subarray/substring? ─► Sliding Window / Prefix Sum
├─ Exact count / sum / complement? ► HashMap / Prefix + Hash
├─ Next greater/smaller element? ──► Monotonic Stack
├─ Top K / Kth / merge K sorted? ──► Heap / K-way Merge
├─ Tree / BST? ────────────────────► DFS / BFS / Tree DP / LCA
├─ Grid / islands / matrix? ───────► BFS/DFS Grid
├─ Shortest path unweighted? ──────► BFS
├─ Weighted non-negative edges? ─► Dijkstra
├─ Dependencies / ordering? ───────► Topological Sort
├─ Dynamic connectivity? ──────────► Union Find
├─ All combinations/permutations? ► Backtracking
├─ Optimal overlapping substructure?► DP
├─ Greedy local choice provable? ──► Greedy
├─ Minimize max / maximize min? ───► Binary Search on Answer
├─ Prefix queries on strings? ─────► Trie
└─ Still stuck? ───────────────────► Brute force → find bottleneck → optimize
</pre>
<div class="diagram-caption">Pattern Recognition Decision Tree</div>
</div>"""

    diagnosis = """
<h3>30-Second DSA Diagnosis Framework</h3>
<p>For every new problem, answer these in order:</p>
<ol>
<li><strong>Input?</strong> Array, string, tree, graph, matrix, stream?</li>
<li><strong>Output?</strong> Value, index, count, list, boolean?</li>
<li><strong>Ordering important?</strong> Yes → sort/pointers; No → hash/set</li>
<li><strong>Sorted?</strong> Yes → BS/two pointers</li>
<li><strong>Contiguous?</strong> Yes → sliding window/prefix</li>
<li><strong>Existence / count / min / max?</strong> Maps to hash, BS, heap, DP</li>
<li><strong>All possibilities?</strong> Backtracking</li>
<li><strong>Repeated substructure?</strong> DP</li>
<li><strong>Monotonic property?</strong> BS on answer, two pointers, monotonic stack</li>
<li><strong>Constraints?</strong> n≤20 → bitmask; n≤10⁵ → O(n) or O(n log n)</li>
</ol>"""

    mapping = table(
        ["Answer Pattern", "Likely Techniques"],
        [
            ["Sorted + find", "Binary Search, Two Pointers"],
            ["Contiguous + constraint", "Sliding Window, Prefix Sum"],
            ["Count / frequency", "HashMap, Prefix + Hash"],
            ["Top K", "Heap, QuickSelect"],
            ["Tree path/subtree", "DFS, Tree DP"],
            ["Shortest unweighted", "BFS"],
            ["Dependencies", "Topological Sort, DFS cycle"],
            ["All subsets/perms", "Backtracking"],
            ["Min-max optimization", "DP, Greedy, BS on Answer"],
        ],
    )

    quizzes = quiz(
        "Array is sorted, find two numbers with given sum. First pattern?",
        "Two Pointers (or HashMap if unsorted). Sorted → opposite pointers O(n).",
        "diag-1",
    ) + quiz(
        "Find shortest path in unweighted grid with obstacles.",
        "BFS from source — first visit = shortest steps.",
        "diag-2",
    )

    return section(
        "recognition",
        "Pattern Recognition Engine",
        tree + diagnosis + mapping + quizzes,
    )


def build_diagnosis_cheatsheet() -> str:
    return """
<div class="cheat-sheet" id="diagnosis-cheatsheet">
<h3>1-Page: 30-Second Diagnosis</h3>
<ul>
<li>Sorted? → BS / Two Ptr</li>
<li>Contiguous? → Window / Prefix</li>
<li>Count? → HashMap</li>
<li>Top K? → Heap</li>
<li>Next greater? → Mono Stack</li>
<li>Tree? → DFS/BFS</li>
<li>Grid? → BFS/DFS 4-dir</li>
<li>Shortest unweighted? → BFS</li>
<li>Weighted? → Dijkstra</li>
<li>Deps? → Topo Sort</li>
<li>Components? → UF/DFS</li>
<li>All combos? → Backtrack</li>
<li>Optimal substructure? → DP</li>
<li>Min max answer? → BS on Answer</li>
</ul>
</div>"""
