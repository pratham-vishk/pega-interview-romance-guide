"""Java interview templates and pitfalls."""

from content.helpers import code_block, section, table, tip, trap


TEMPLATES = {
    "HashMap Frequency": """Map<Integer, Integer> freq = new HashMap<>();
for (int x : nums) {
    freq.merge(x, 1, Integer::sum);
}""",
    "HashSet": """Set<Integer> seen = new HashSet<>();
for (int x : nums) {
    if (!seen.add(x)) { /* duplicate */ }
}""",
    "ArrayList": """List<Integer> list = new ArrayList<>();
list.add(x);
// list.get(i), list.size()""",
    "PriorityQueue (Min-Heap)": """PriorityQueue<Integer> minHeap = new PriorityQueue<>();
// Max-heap:
PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
// Custom comparator:
PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);""",
    "Deque": """Deque<Integer> dq = new ArrayDeque<>();
dq.offerLast(x);
dq.pollFirst();
dq.peekLast();""",
    "Stack via Deque": """Deque<Integer> stack = new ArrayDeque<>();
stack.push(x);  // offerFirst
int top = stack.pop();  // pollFirst""",
    "Binary Search": """int lo = 0, hi = n - 1;
while (lo <= hi) {
    int mid = lo + (hi - lo) / 2;
    if (nums[mid] == target) return mid;
    if (nums[mid] < target) lo = mid + 1;
    else hi = mid - 1;
}
return -1;""",
    "BFS": """Queue<int[]> q = new ArrayDeque<>();
boolean[][] vis = new boolean[rows][cols];
q.offer(new int[]{sr, sc});
vis[sr][sc] = true;
int[][] dirs = {{0,1},{1,0},{0,-1},{-1,0}};
while (!q.isEmpty()) {
    int[] cur = q.poll();
    for (int[] d : dirs) {
        int nr = cur[0] + d[0], nc = cur[1] + d[1];
        if (nr < 0 || nc < 0 || nr >= rows || nc >= cols || vis[nr][nc]) continue;
        vis[nr][nc] = true;
        q.offer(new int[]{nr, nc});
    }
}""",
    "DFS (Recursive)": """void dfs(int u, List<List<Integer>> adj, boolean[] vis) {
    vis[u] = true;
    for (int v : adj.get(u)) {
        if (!vis[v]) dfs(v, adj, vis);
    }
}""",
    "TreeNode": """class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int v) { val = v; }
}""",
    "ListNode": """class ListNode {
    int val;
    ListNode next;
    ListNode(int v) { val = v; }
}""",
    "Graph Adjacency List": """int n = nodes;
List<List<Integer>> adj = new ArrayList<>();
for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
for (int[] e : edges) {
    adj.get(e[0]).add(e[1]);
    adj.get(e[1]).add(e[0]); // undirected
}""",
    "Union Find": """class UnionFind {
    int[] parent, rank;
    UnionFind(int n) {
        parent = new int[n];
        rank = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;
    }
    int find(int x) {
        if (parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    }
    boolean union(int a, int b) {
        int ra = find(a), rb = find(b);
        if (ra == rb) return false;
        if (rank[ra] < rank[rb]) { int t = ra; ra = rb; rb = t; }
        parent[rb] = ra;
        if (rank[ra] == rank[rb]) rank[ra]++;
        return true;
    }
}""",
    "Dijkstra": """long[] dist = new long[n];
Arrays.fill(dist, Long.MAX_VALUE);
dist[src] = 0;
PriorityQueue<long[]> pq = new PriorityQueue<>((a, b) -> Long.compare(a[0], b[0]));
pq.offer(new long[]{0, src});
while (!pq.isEmpty()) {
    long[] cur = pq.poll();
    long d = cur[0];
    int u = (int) cur[1];
    if (d > dist[u]) continue;
    for (int[] e : adj.get(u)) {
        int v = e[0];
        long nd = d + e[1];
        if (nd < dist[v]) {
            dist[v] = nd;
            pq.offer(new long[]{nd, v});
        }
    }
}""",
    "Topological Sort (Kahn)": """int[] indeg = new int[n];
for (int[] e : edges) indeg[e[1]]++;
Queue<Integer> q = new ArrayDeque<>();
for (int i = 0; i < n; i++) if (indeg[i] == 0) q.offer(i);
List<Integer> order = new ArrayList<>();
while (!q.isEmpty()) {
    int u = q.poll();
    order.add(u);
    for (int v : adj.get(u)) {
        if (--indeg[v] == 0) q.offer(v);
    }
}""",
    "Trie": """class TrieNode {
    TrieNode[] children = new TrieNode[26];
    boolean isWord;
}
class Trie {
    TrieNode root = new TrieNode();
    void insert(String word) {
        TrieNode node = root;
        for (char c : word.toCharArray()) {
            int i = c - 'a';
            if (node.children[i] == null) node.children[i] = new TrieNode();
            node = node.children[i];
        }
        node.isWord = true;
    }
}""",
    "Backtracking": """List<List<Integer>> res = new ArrayList<>();
List<Integer> path = new ArrayList<>();
void backtrack(int idx) {
    if (/* goal */) { res.add(new ArrayList<>(path)); return; }
    for (int i = idx; i < n; i++) {
        path.add(nums[i]);
        backtrack(i + 1);
        path.remove(path.size() - 1);
    }
}""",
    "DP Memoization": """Map<String, Integer> memo = new HashMap<>();
int solve(int i, int j) {
    String key = i + "," + j;
    if (memo.containsKey(key)) return memo.get(key);
    int ans = /* recurse */;
    memo.put(key, ans);
    return ans;
}""",
    "DP Tabulation": """int[] dp = new int[n + 1];
dp[0] = base;
for (int i = 1; i <= n; i++) {
    dp[i] = Math.max(dp[i - 1], dp[i - 2] + nums[i]);
}
return dp[n];""",
}


PITFALLS = [
    ("Integer overflow", "Use long for sums/products; mid = lo + (hi-lo)/2"),
    ("Comparator", "PriorityQueue needs consistent comparator; avoid overflow in (a-b)"),
    ("PriorityQueue behavior", "peek() doesn't remove; poll() removes; default is min-heap"),
    ("StringBuilder", "Use for string concatenation in loops, not +="),
    ("Arrays.sort", "Primitives: Arrays.sort; objects need Comparator"),
    ("HashMap frequency", "freq.merge(k,1,Integer::sum) or getOrDefault"),
    ("Recursion depth", "Java ~1000-10000; deep trees need iterative"),
    ("Mutable objects", "Don't put mutable lists in HashSet keys"),
    ("equals/hashCode", "Custom objects in HashMap need both"),
    ("Primitive vs wrapper", "int[] faster; Integer in collections"),
]


def build_java_section() -> str:
    body = "<p>All DSA implementations use Java — your interview language.</p>"
    for name, code in TEMPLATES.items():
        body += f"<h3>{name}</h3>{code_block(code)}"
    body += "<h3>Java-Specific Pitfalls</h3>"
    body += table(["Pitfall", "Fix"], PITFALLS)
    body += trap("Using (a[0]-b[0]) comparator when values can overflow — use Integer.compare or Long.compare.")
    body += tip("In Google interviews, state time/space complexity after coding and mention edge cases aloud.")
    return section("java-templates", "Java Interview Templates", body)
