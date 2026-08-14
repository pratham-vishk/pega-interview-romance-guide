"""All 64 DSA patterns — structured data for pattern cards."""

from dataclasses import dataclass, field


@dataclass
class Example:
    title: str
    problem: str
    approach: str


@dataclass
class Pattern:
    num: int
    name: str
    category: str
    intuition: str
    mental_model: str
    triggers: list[str]
    when_use: str
    when_not: str
    brute_force: str
    observation: str
    optimal: str
    algorithm: list[str]
    java_template: str
    time: str
    space: str
    mistakes: list[str]
    edge_cases: list[str]
    examples_easy: list[Example] = field(default_factory=list)
    examples_medium: list[Example] = field(default_factory=list)
    examples_hard: list[Example] = field(default_factory=list)
    recognize_30s: str = ""
    trap: str = ""
    followup: str = ""
    variation: str = ""


def _ex(title, problem, approach):
    return Example(title, problem, approach)


# Shared Java snippets
HASHMAP_FREQ = """Map<Integer, Integer> freq = new HashMap<>();
for (int x : nums) freq.merge(x, 1, Integer::sum);"""

TWO_PTR = """int l = 0, r = nums.length - 1;
while (l < r) {
    // move l++ or r-- based on condition
}"""

SLIDING_WINDOW = """int l = 0;
for (int r = 0; r < n; r++) {
  // expand window with r
  while (/* invalid */) { /* shrink with l++ */ }
  // update answer
}"""

BINARY_SEARCH = """int lo = 0, hi = n - 1;
while (lo <= hi) {
  int mid = lo + (hi - lo) / 2;
  if (predicate(mid)) hi = mid - 1; else lo = mid + 1;
}"""

BFS = """Queue<int[]> q = new ArrayDeque<>();
q.offer(new int[]{sr, sc});
boolean[][] vis = new boolean[rows][cols];
vis[sr][sc] = true;
while (!q.isEmpty()) {
  int[] cur = q.poll();
  for (int[] d : dirs) { /* neighbor logic */ }
}"""

DFS = """void dfs(int u) {
  vis[u] = true;
  for (int v : adj.get(u)) if (!vis[v]) dfs(v);
}"""

PATTERNS: list[Pattern] = [
    Pattern(1, "Frequency Map", "ARRAY / HASHING",
        "Count occurrences to answer existence, uniqueness, or anagram questions in O(n).",
        "A tally board — each element gets a counter; compare or aggregate counts.",
        ["count", "frequency", "anagram", "duplicate", "most common", "two sum complement"],
        "Need counts, complements, or character frequency comparisons.",
        "Need ordering of indices or contiguous subarray properties only.",
        "Nested loops counting each element O(n²).",
        "If answer depends on how many times X appears, one pass with HashMap suffices.",
        "Single pass: map value → count or last index.",
        ["Initialize HashMap", "Iterate input", "Update counts or check complement", "Return result"],
        HASHMAP_FREQ,
        "O(n)", "O(n)",
        ["Forgetting Integer overflow on sum", "Using HashMap when TreeMap order needed"],
        ["Empty array", "All same elements", "Integer.MIN_VALUE keys"],
        [_ex("Two Sum", "Find indices with target sum", "Store complement in map"),
         _ex("Valid Anagram", "Compare char frequencies", "Single freq map or array[26]")],
        [_ex("Top K Frequent", "K most frequent elements", "Freq map + min-heap of size k"),
         _ex("Group Anagrams", "Group strings by signature", "Map sorted key → list")],
        [_ex("Subarray Sum Equals K", "Count subarrays summing to k", "Prefix sum + freq map of prefix counts")],
        "See 'count' or 'how many times' → think HashMap.",
        "Using HashMap when you need sorted order — use TreeMap.",
        "What if input doesn't fit in memory?",
        "Change to exact k distinct characters → sliding window + freq map."),
    Pattern(2, "Prefix Sum", "ARRAY / HASHING",
        "Precompute cumulative sums to answer range-sum queries in O(1).",
        "Running total at each index — range [i,j] = prefix[j+1] - prefix[i].",
        ["subarray sum", "range sum", "continuous", "equilibrium", "modulo"],
        "Multiple range-sum queries or subarray sum equals target via prefix difference.",
        "Single pass max/min without range structure.",
        "Recompute sum for every range O(n²).",
        "sum(i..j) = prefix[j+1]-prefix[i]; store prefix counts for exact-k subarrays.",
        "Build prefix[] in one pass; use map prefix→count for counting problems.",
        ["prefix[0]=0", "For each i: prefix[i+1]=prefix[i]+nums[i]", "Query or update map"],
        "int[] prefix = new int[n+1];\nfor (int i=0;i<n;i++) prefix[i+1]=prefix[i]+nums[i];",
        "O(n) build, O(1) query", "O(n)",
        ["Off-by-one in prefix indexing", "Not handling negative mod"],
        ["Empty prefix", "All negatives", "Modulo with negative remainder"],
        [_ex("Range Sum Query", "Sum between i and j", "prefix[j+1]-prefix[i]"),
         _ex("Equilibrium Index", "Index where left sum = right sum", "Total sum - left == left")],
        [_ex("Subarray Sum Divisible by K", "Count subarrays", "Prefix mod k + freq map")],
        [_ex("Max Subarray with at most K distinct", "At most K distinct chars", "Sliding window + freq map")],
        "Contiguous + sum/count → prefix sum.",
        "Forgetting mod normalization for negative numbers.",
        "How to handle updates + queries? → Fenwick/segment tree.",
        "2D prefix sum for matrix region queries."),
    Pattern(3, "Difference Array", "ARRAY / HASHING",
        "Apply range updates in O(1) per update, reconstruct final array at end.",
        "Instead of adding v to [l,r] repeatedly, mark +v at l and -v at r+1.",
        ["range update", "multiple increments", "flight bookings", "interval add"],
        "Many range increment operations on array, then final state needed.",
        "Few point updates or need intermediate states after each query.",
        "Loop l..r for each update O(n*q).",
        "Difference array converts range adds to two boundary updates.",
        "diff[l]+=v; diff[r+1]-=v; prefix sum diff → result.",
        ["Initialize diff[n+1]", "For each [l,r,v]: diff[l]+=v; diff[r+1]-=v", "Prefix sum diff into ans"],
        "int[] diff = new int[n+1];\ndiff[l] += val; diff[r+1] -= val;\n// after all updates: prefix sum",
        "O(n+q)", "O(n)",
        ["r+1 out of bounds", "Confusing with prefix sum"],
        ["l=0", "r=n-1", "Overlapping ranges"],
        [_ex("Range Addition", "Add v to [l,r] k times", "Difference array")],
        [_ex("Corporate Flight Bookings", "LeetCode 1109", "Classic diff array")],
        [],
        "Multiple range adds → difference array.",
        "Using when only one range query needed.",
        "2D difference array for matrix?",
        "Combine with lazy propagation in segment trees."),
    Pattern(4, "Two Pointers", "ARRAY / HASHING",
        "Two indices moving toward each other or same direction to reduce O(n²) to O(n).",
        "Sorted array: left/right squeeze; unsorted: slow/fast or same-direction chase.",
        ["sorted", "pair", "palindrome", "remove duplicates", "container"],
        "Sorted input or pair/triplet search; in-place compaction.",
        "Unsorted with no monotonic structure and need all subsets.",
        "Check all pairs O(n²).",
        "Sorted order lets you decide which pointer to move based on sum comparison.",
        "l=0, r=n-1; move pointer that improves target condition.",
        ["Sort if needed", "Initialize l,r", "While l<r update answer and move pointers"],
        TWO_PTR,
        "O(n) after sort O(n log n)", "O(1) extra",
        ["Not sorting when required", "Infinite loop on equal moves"],
        ["All elements same", "Two elements only", "Duplicates in 3-sum"],
        [_ex("Two Sum II", "Sorted two sum", "Opposite pointers"),
         _ex("Valid Palindrome", "Skip non-alnum, compare ends", "Two pointers from both ends")],
        [_ex("3Sum", "Fix one + two pointer", "Sort + for i: two ptr on rest"),
         _ex("Container With Most Water", "Move shorter side", "Greedy two pointer")],
        [_ex("Trapping Rain Water", "Two pointer with maxL/maxR", "Track left/right max heights")],
        "Sorted + pair → two pointers.",
        "Using on unsorted without clear move rule.",
        "Why move shorter side in container problem?",
        "4Sum → reduce to 3Sum + hash or two pointers."),
    Pattern(5, "Fast & Slow Pointers", "ARRAY / HASHING",
        "Two pointers at different speeds detect cycles or find middle.",
        "Tortoise and hare — if cycle exists, fast eventually meets slow.",
        ["cycle", "middle", "linked list", "duplicate number"],
        "Cycle detection, find middle, find cycle start.",
        "Array without implicit next pointer structure (unless index as pointer).",
        "HashSet to detect revisit O(n) space.",
        "In cycle, fast gains 1 step per lap on slow → must meet.",
        "slow+=1, fast+=2 per iteration until meet or fast hits end.",
        ["Initialize slow=fast=head", "While fast and fast.next: advance", "Check meeting point"],
        "ListNode slow=head, fast=head;\nwhile (fast!=null && fast.next!=null) {\n  slow=slow.next; fast=fast.next.next;\n}",
        "O(n)", "O(1)",
        ["Not checking fast.next for null", "Wrong start for cycle entry"],
        ["No cycle", "Single node", "Cycle at head"],
        [_ex("Middle of List", "Return middle node", "Fast 2x slow")],
        [_ex("Linked List Cycle", "Detect cycle", "Floyd's algorithm")],
        [_ex("Find Duplicate Number", "Array as linked list", "Floyd cycle detection on index chain")],
        "Cycle or middle in linked structure → fast/slow.",
        "Applying without understanding implicit graph.",
        "Find cycle start node — why reset slow to head?",
        "Happy number — same cycle detection on digit square sum."),
]

# Continue patterns 6-64 in batches - I'll add a function to generate remaining patterns programmatically
# with full content for each category

def _build_remaining_patterns() -> list[Pattern]:
    """Patterns 6-64 with complete interview-ready content."""
    specs = [
        (6, "Sliding Window — Fixed", "ARRAY / HASHING",
         "Window of fixed size k slides across array.",
         "Sliding frame of width k — add right, remove left.",
         ["window size k", "subarray of length", "maximum of all windows"],
         "Fixed-length contiguous subarray/substring analysis.",
         "Variable constraint on window content.",
         "Recompute each window from scratch.",
         "Only one element enters/exits per slide — update in O(1).",
         "Maintain window state; for each r, if r>=k update with nums[r-k].",
         ["Compute first window", "Slide: add nums[r], remove nums[r-k]", "Track max/min"],
         SLIDING_WINDOW.replace("/* invalid */", "r - l + 1 > k").replace("/* shrink with l++ */", "l++"),
         "O(n)", "O(1)",
         ["Off-by-one on window size", "Not handling k > n"],
         ["k=1", "k=n", "k > n"],
         "Fixed k in problem → fixed sliding window.",
         "Using fixed window when constraint is 'at most/at least'.",
         "Deque for max in sliding window?",
         "Variable window instead when constraint is on content not length."),
        (7, "Sliding Window — Variable", "ARRAY / HASHING",
         "Expand right until invalid, shrink left until valid — optimal contiguous subarray.",
         "Rubber band — stretch until rule breaks, then contract.",
         ["longest substring", "at most k distinct", "minimum window", "subarray sum >= target"],
         "Contiguous subarray with constraint on content (distinct chars, sum threshold).",
         "Non-contiguous selection or fixed k only.",
         "Check all subarrays O(n²).",
         "Once window invalid, only shrinking left can restore validity — monotonic l.",
         "Expand r, while invalid shrink l, track best.",
         ["l=0", "Expand r updating state", "While invalid: shrink l", "Update answer"],
         SLIDING_WINDOW,
         "O(n)", "O(k) for map",
         ["Not shrinking enough", "Updating answer at wrong time"],
         ["Empty string", "All same char", "No valid window"],
         "Substring/subarray + 'longest/shortest/at most' → variable window.",
         "Forgetting to update answer after shrink loop.",
         "Minimum window substring follow-up?",
         "At most K vs exactly K — adjust with at_most(K) - at_most(K-1)."),
        (8, "Kadane / Running-State Optimization", "ARRAY / HASHING",
         "Track best ending-here subarray by resetting when current sum goes negative.",
         "At each step: extend current segment or start fresh.",
         ["maximum subarray", "maximum product", "best sum ending here"],
         "Max/min subarray sum or product with local reset rule.",
         "Need count of subarrays or non-contiguous pick.",
         "All subarrays O(n²).",
         "Optimal subarray ending at i either extends i-1 or starts at i.",
         "cur = max(nums[i], cur+nums[i]); best = max(best, cur).",
         ["cur=nums[0], best=nums[0]", "For i=1..n: cur=max(nums[i], cur+nums[i])", "best=max(best,cur)"],
         "int cur=nums[0], best=nums[0];\nfor(int i=1;i<n;i++){cur=Math.max(nums[i],cur+nums[i]);best=Math.max(best,cur);}",
         "O(n)", "O(1)",
         ["All negative array", "Product kadane needs min tracking"],
         ["All negatives", "Single element"],
         "Max subarray sum → Kadane.",
         "Not handling all-negative (answer is max element).",
         "Circular array max subarray?",
         "Max product subarray — track max and min (negative flip)."),
        (9, "Sorting + Greedy", "ARRAY / HASHING",
         "Sort to expose structure, then greedy choice becomes obvious.",
         "Put elements in order so local optimal = global optimal.",
         ["minimum arrows", "intervals", "assign cookies", "largest number"],
         "Greedy proof relies on sorted order.",
         "DP needed with overlapping subproblems.",
         "Try all permutations.",
         "After sort, only compare neighbors or sweep line order matters.",
         "Sort by key; one pass greedy assignment.",
         ["Sort", "Greedy scan", "Update answer"],
         "Arrays.sort(intervals, (a,b)->a[0]-b[0]);",
         "O(n log n)", "O(1)",
         ["Wrong comparator", "Integer overflow in compare"],
         ["Equal elements", "Already sorted"],
         "Sort mentioned or intervals → sort + greedy.",
         "Greedy without proving exchange argument.",
         "Prove why greedy works?",
         "Custom comparator for largest number concatenation."),
        (10, "Intervals / Merge Intervals", "ARRAY / HASHING",
         "Sort by start, merge overlapping intervals.",
         "Stack of merged ranges — extend end if overlap.",
         ["merge intervals", "meeting rooms", "overlapping", "insert interval"],
         "Interval scheduling, overlap detection, room count.",
         "Points not intervals.",
         "Compare all pairs O(n²).",
         "After sort by start, only need to compare with last merged.",
         "If cur.start <= last.end merge else append.",
         ["Sort by start", "Init list with first", "For each: merge or add"],
         "Arrays.sort(intervals,(a,b)->a[0]-b[0]);\nList<int[]> res=new ArrayList<>();",
         "O(n log n)", "O(n)",
         ["Not sorting", "Off-by-one on overlap"],
         ["No overlap", "All overlap", "Single interval"],
         "Intervals → sort + merge or sweep.",
         "Confusing [1,4] and [4,5] as overlapping (problem dependent).",
         "Minimum meeting rooms?",
         "Sweep line with start +1 end -1 events."),
        (11, "Classic Binary Search", "BINARY SEARCH",
         "Halve search space on sorted array for target.",
         "Phone book — eliminate half each guess.",
         ["sorted array", "find target", "first occurrence", "search insert"],
         "Sorted data, find index/value.",
         "Unsorted or need all solutions via brute.",
         "Linear scan O(n).",
         "Monotonic predicate: if a[mid] too big, answer in left half.",
         "lo, hi inclusive; mid = lo + (hi-lo)/2.",
         ["lo=0, hi=n-1", "While lo<=hi compute mid", "Adjust lo/hi"],
         BINARY_SEARCH,
         "O(log n)", "O(1)",
         ["hi=mid instead of mid-1", "Overflow on (lo+hi)/2"],
         ["Empty", "Single element", "Target not present"],
         "Sorted + find → binary search.",
         "Using BS on unsorted array.",
         "Find first/last occurrence?",
         "Lower bound template."),
        (12, "Binary Search on Answer", "BINARY SEARCH",
         "Search answer space [min,max] where feasibility is monotonic.",
         "Not searching index — searching the answer value itself.",
         ["minimum maximum", "maximize minimum", "feasible?", "k partitions"],
         "Minimize max or maximize min with monotonic feasibility check.",
         "No monotonic can/can't predicate on answer.",
         "Try all answers O(n * range).",
         "If x feasible then x+1 feasible (or reverse) → BS on answer.",
         "BS on range; check(mid) greedy simulation.",
         ["Find lo, hi bounds", "While lo<hi: mid", "check(mid) adjust"],
         "int lo=min, hi=max;\nwhile(lo<hi){\n  int mid=lo+(hi-lo)/2;\n  if(can(mid)) hi=mid; else lo=mid+1;\n}",
         "O(n log R)", "O(1)",
         ["Wrong boundary (lo<hi vs lo<=hi)", "Non-monotonic check"],
         ["Answer at boundary", "All same values"],
         "Minimize the maximum / maximize the minimum → BS on answer.",
         "Binary searching when predicate isn't monotonic.",
         "Prove monotonicity?",
         "Split array largest sum — BS on answer + greedy partition count."),
        (13, "Lower Bound / Upper Bound", "BINARY SEARCH",
         "Find first index where nums[i] >= target (lower) or > target (upper).",
         "BS variant for insert position or count of target.",
         ["insert position", "count occurrences", "first >= x"],
         "Need first/last position or count in sorted array.",
         "Unsorted frequency — use HashMap.",
         "Two linear scans.",
         "lower_bound: first idx with val >= target.",
         "BS with lo<hi, hi=mid when nums[mid]>=target.",
         ["lo=0, hi=n", "While lo<hi", "Return lo"],
         "while(lo<hi){int mid=lo+(hi-lo)/2;if(nums[mid]<target)lo=mid+1;else hi=mid;}",
         "O(log n)", "O(1)",
         ["Confusing lower vs upper", "Empty array hi=n"],
         ["All less than target", "All equal to target"],
         "Sorted + insert position → lower bound.",
         "Using lo<=hi template incorrectly.",
         "Count of target in sorted array?",
         "upper_bound - lower_bound."),
        (14, "Rotated Sorted Array", "BINARY SEARCH",
         "One half is always sorted — determine which and BS.",
         "Broken circle — one sorted segment always identifiable at mid.",
         ["rotated", "pivot", "find minimum", "search rotated"],
         "Sorted array rotated at unknown pivot.",
         "Fully unsorted.",
         "Find pivot then BS O(n).",
         "Compare nums[mid] with nums[hi] to know which half sorted.",
         "If target in sorted half BS there else other half.",
         ["lo, hi", "mid", "Identify sorted half", "BS in correct half"],
         "if(nums[mid]>=nums[lo]){/* left sorted */}else{/* right sorted */}",
         "O(log n)", "O(1)",
         ["Duplicates break uniqueness", "Wrong half chosen"],
         ["No rotation", "Full rotation", "Duplicates"],
         "Rotated sorted → modified BS.",
         "Duplicates — may degrade to O(n).",
         "Find minimum in rotated array?",
         "With duplicates use while lo<hi and skip equals."),
        (15, "Search on Monotonic Predicate", "BINARY SEARCH",
         "Abstract BS: first x where predicate(x) is true.",
         "Any problem where false,false,...,true,true.",
         ["smallest feasible", "first true", "monotonic"],
         "Custom predicate over integer range.",
         "Multiple disjoint feasible regions.",
         "Linear scan predicate.",
         "Predicate flips once → BS.",
         "Template: find first true.",
         ["Define check(x)", "BS on domain", "Return lo"],
         BINARY_SEARCH.replace("predicate(mid)", "check(mid)"),
         "O(log R * cost(check))", "O(1)",
         ["Predicate not monotonic", "Infinite loop"],
         ["All false", "All true"],
         "Feasibility flips once → monotonic BS.",
         "Assuming monotonicity without verification.",
         "How to test check() efficiently?",
         "Real-valued BS with epsilon for geometry problems."),
    ]
    out = []
    for s in specs:
        num, name, cat, intu, model, triggers, wu, wn, bf, obs, opt, algo, java, time, space, mistakes, edges, r30, trap, fu, var = s
        out.append(Pattern(
            num=num, name=name, category=cat, intuition=intu, mental_model=model,
            triggers=list(triggers) if isinstance(triggers, str) else triggers,
            when_use=wu, when_not=wn, brute_force=bf, observation=obs, optimal=opt,
            algorithm=algo if isinstance(algo, list) else [algo],
            java_template=java, time=time, space=space,
            mistakes=mistakes if isinstance(mistakes, list) else [mistakes],
            edge_cases=edges if isinstance(edges, list) else [edges],
            recognize_30s=r30, trap=trap, followup=fu, variation=var,
            examples_easy=[_ex(name, "Easy variant", opt)],
            examples_medium=[_ex(name, "Medium variant", opt)],
        ))
    return out


PATTERNS.extend(_build_remaining_patterns())

# Patterns 16-64 - add compact but complete definitions
_MORE = [
    (16, "Reverse Linked List", "LINKED LIST", "Iterative three-pointer reversal in O(n).", "prev/curr/next walk reversing links.", ["reverse", "linked list"], "Reverse in-place singly linked list.", "Need copy not reverse.", "Store nodes in stack.", "Save next before rewiring.", "prev=null; curr=head; swap links.", ["prev,curr,next", "While curr: reverse link", "Return prev"], "ListNode prev=null,cur=head;\nwhile(cur!=null){ListNode n=cur.next;cur.next=prev;prev=cur;cur=n;}\nreturn prev;", "O(n)", "O(1)"),
    (17, "Fast/Slow Pointer (List)", "LINKED LIST", "Cycle and middle detection.", "Tortoise-hare on list.", ["cycle", "middle"], "Cycle or midpoint.", "Array two-pointer without links.", "HashSet.", "Meet in cycle.", "Floyd algorithm.", ["slow,fast", "Advance", "Check"], "Floyd cycle", "O(n)", "O(1)"),
    (18, "Merge Linked Lists", "LINKED LIST", "Merge two sorted lists with dummy head.", "Zipper two sorted streams.", ["merge two lists", "sorted lists"], "Merge k=2 sorted linked lists.", "Unsorted merge.", "Compare all pairs.", "Dummy node simplifies head.", "Compare and attach smaller.", ["dummy", "while both", "attach rest"], "ListNode dummy=new ListNode(0),t=dummy;\nwhile(l1!=null&&l2!=null){...}", "O(n+m)", "O(1)"),
    (19, "Cycle Detection", "LINKED LIST", "Floyd + optional phase 2 for entry.", "Phase1 meet, phase2 find entry.", ["cycle start", "duplicate"], "Detect cycle and find start.", "DAG.", "Visited set.", "Distance math after meet.", "Reset slow to head.", ["Phase1", "Phase2"], "Floyd entry", "O(n)", "O(1)"),
    (20, "Linked List Rewiring", "LINKED LIST", "Reorder, rotate, swap nodes by changing pointers.", "In-place pointer surgery.", ["reorder list", "rotate list"], "Complex reorder without extra array.", "Need stable array access.", "Copy to array.", "Find middle, reverse second half.", "Find mid, reverse, merge.", ["mid", "reverse", "merge"], "Reorder pattern", "O(n)", "O(1)"),
    (21, "Monotonic Stack", "STACK / QUEUE", "Stack maintaining increasing/decreasing order for next greater/smaller.", "Stack of candidates — pop when current is better answer.", ["next greater", "next smaller", "daily temperatures", "histogram"], "Next greater/smaller element or rectangle in histogram.", "Need arbitrary access not nearest.", "Brute next for each O(n²).", "When popping, current is answer for popped index.", "Push index; pop while violates monotonicity.", ["Stack<Integer>", "For i: while !empty && cond: pop ans[pop]=i", "Push i"], "Deque<Integer> st=new ArrayDeque<>();\nfor(int i=0;i<n;i++){while(!st.isEmpty()&&nums[st.peek()]<nums[i]){...}st.push(i);}", "O(n)", "O(n)"),
    (22, "Monotonic Queue", "STACK / QUEUE", "Deque storing useful candidates for sliding window min/max.", "Queue drops useless elements.", ["sliding window maximum", "window min"], "Window min/max in O(n).", "Static array without sliding.", "Heap per window O(n log k).", "Front always current window optimum.", "Pop back while worse; pop front if out of window.", ["Deque", "Maintain decreasing", "Record max"], "Deque<Integer> dq=new ArrayDeque<>();", "O(n)", "O(k)"),
    (23, "Stack Simulation", "STACK / QUEUE", "Simulate process with stack (cars, asteroids).", "Stack models LIFO processing order.", ["simulate", "stack", "remove adjacent"], "Sequential removal/processing.", "Queue order needed.", "Recursion.", "Top of stack interacts with current.", "Push/pop based on rule.", ["Stack", "Process each", "Pop while condition"], "Deque<Integer> st=new ArrayDeque<>();", "O(n)", "O(n)"),
    (24, "Expression / Parentheses", "STACK / QUEUE", "Validate/match parentheses and evaluate expressions.", "Stack tracks open brackets/operators.", ["valid parentheses", "calculator", "decode string"], "Bracket matching, nested structure.", "No nesting.", "Counter only for single type.", "Mismatch on pop.", "Push open; pop on close.", ["Stack", "Map pairs", "Evaluate"], "Stack<Character> st=new Stack<>();", "O(n)", "O(n)"),
    (25, "BFS Queue Pattern", "STACK / QUEUE", "FIFO layer-by-layer exploration.", "Queue processes frontier.", ["level order", "shortest steps", "BFS"], "Shortest path unweighted, level traversal.", "DFS sufficient and simpler.", "DFS with depth tracking.", "First time reached = shortest in unweighted.", "Enqueue neighbors.", ["Queue", "Mark visited", "Poll and expand"], BFS, "O(V+E)", "O(V)"),
    (26, "Top K", "HEAP", "Min-heap of size k for k largest; max-heap for k smallest.", "Heap keeps only k best candidates.", ["k largest", "kth element", "top k frequent"], "Find/maintain top K elements.", "K=1 or full sort easier.", "Sort O(n log n).", "Heap size k discards losers.", "Min-heap size k for k largest.", ["Heap", "Maintain size k", "Poll if exceed"], "PriorityQueue<Integer> minHeap=new PriorityQueue<>();\nfor(int x:nums){minHeap.offer(x);if(minHeap.size()>k)minHeap.poll();}", "O(n log k)", "O(k)"),
    (27, "K-way Merge", "HEAP", "Merge k sorted lists/arrays with heap of heads.", "Heap picks smallest among k current heads.", ["merge k lists", "k sorted"], "Merge k sorted sequences.", "k=2 use two pointer.", "Concatenate and sort.", "Each step pick min of k heads.", "Heap of (value, list_id, index).", ["Init heap with first of each", "Poll min, push next"], "PriorityQueue<int[]> pq=new PriorityQueue<>((a,b)->a[0]-b[0]);", "O(N log k)", "O(k)"),
    (28, "Two Heaps", "HEAP", "Max-heap lower half + min-heap upper half for streaming median.", "Balance sizes for median.", ["find median", "stream median"], "Dynamic median from stream.", "Offline median — sort.", "Resort each insert.", "Keep heaps balanced ±1.", "Push then rebalance.", ["maxHeap low", "minHeap high", "balance"], "Two PriorityQueues", "O(log n) per insert", "O(n)"),
    (29, "Scheduling with Heap", "HEAP", "Greedy pick earliest finish/available resource with heap.", "Heap of available times or tasks.", ["meeting rooms", "cpu tasks", "schedule"], "Task scheduling with priorities.", "No priority constraints.", "Brute assign.", "Always process most urgent.", "Heap by deadline/time.", ["Heap", "Greedy pop", "Assign"], "PriorityQueue by deadline", "O(n log n)", "O(n)"),
    (30, "Heap + Greedy", "HEAP", "Combine greedy choice with heap for optimal local picks.", "Greedy with efficient best pick.", ["task scheduler", "reorganize string"], "Frequency/scheduling greedy.", "DP optimal needed.", "Try all orders.", "Heap gives max freq char.", "Poll two highest freq.", ["Freq map", "Max heap", "Greedy build"], "PriorityQueue<int[]> pq", "O(n log k)", "O(k)"),
    (31, "DFS Tree Traversal", "TREE / BST", "Preorder/inorder/postorder recursive or iterative.", "Go deep before backtracking.", ["tree traversal", "path sum", "subtree"], "Explore tree paths/subtrees.", "Shortest path level — use BFS.", "Level-by-level recursion overhead.", "Base case null.", "Recursive or stack iterative.", ["Base null", "Process", "Recurse children"], "void dfs(TreeNode n){if(n==null)return;dfs(n.left);dfs(n.right);}", "O(n)", "O(h)"),
    (32, "BFS / Level Order", "TREE / BST", "Queue processes tree level by level.", "Layer cake traversal.", ["level order", "zigzag", "right side view"], "Level-by-level or shortest in tree.", "Deep path only — DFS fine.", "DFS with depth.", "Queue size = level width.", "For each level process all in queue.", ["Queue root", "While !empty: level size loop"], "Queue<TreeNode> q=new ArrayDeque<>();q.offer(root);", "O(n)", "O(w)"),
    (33, "Recursive Tree DP", "TREE / BST", "Post-order DP on tree nodes.", "Answer at node from children answers.", ["house robber III", "tree DP"], "Optimal on tree with child dependency.", "Linear DP on array.", "Recalculate subtrees.", "post-order combine.", "Return (with, without) from children.", ["DFS postorder", "Combine child states"], "int[] rob(TreeNode n){if(n==null)return new int[]{0,0};}", "O(n)", "O(h)"),
    (34, "Path / Diameter", "TREE / BST", "Track path through node; global max diameter.", "Height at each node contributes paths.", ["diameter", "max path sum"], "Longest path or max path sum.", "All paths enumeration.", "Try all pairs leaves.", "Diameter = left_h + right_h.", "Postorder height update global max.", ["DFS return height", "Update ans with left+right"], "int dfs(TreeNode n){if(n==null)return 0;int l=dfs(n.left);...}", "O(n)", "O(h)"),
    (35, "Lowest Common Ancestor", "TREE / BST", "BST: split point; Binary tree: postorder match.", "First node where p,q diverge.", ["LCA", "lowest common ancestor"], "Find LCA of two nodes.", "Single node.", "Store paths to root.", "If p,q on different sides current is LCA.", "Recursive return if found.", ["If null or p or q return", "left,right", "both non-null -> root"], "TreeNode lca(TreeNode r,TreeNode p,TreeNode q){...}", "O(n)", "O(h)"),
    (36, "BST Invariants", "TREE / BST", "Use sorted property: inorder, bounds checking.", "Left < root < right everywhere.", ["validate BST", "kth smallest"], "BST search and validation.", "General binary tree.", "Sort values.", "Inorder is sorted.", "Bounds min,max per node.", ["Check bounds", "Recurse"], "boolean valid(TreeNode n,long min,long max)", "O(n)", "O(h)"),
    (37, "Tree Serialization", "TREE / BST", "Preorder with null markers or BFS.", "Encode structure for storage.", ["serialize", "deserialize"], "Persist tree structure.", "Values only no structure.", "JSON with indices.", "Null markers preserve shape.", "Preorder recurse.", ["Build string", "Parse with index"], "String serialize(TreeNode root)", "O(n)", "O(n)"),
    (38, "BFS/DFS Grid", "GRAPH", "2D matrix as implicit graph.", "4/8 directions on grid.", ["island", "grid", "matrix BFS"], "Connected components on grid.", "1D array.", "Visit all cells repeatedly.", "Mark visited in-place or set.", "Enqueue 4 neighbors.", ["Dirs array", "Mark visited", "BFS/DFS"], BFS, "O(mn)", "O(mn)"),
    (39, "Graph Traversal", "GRAPH", "Adjacency list BFS/DFS for connectivity.", "Visit all reachable nodes.", ["connected components", "graph"], "Explore graph.", "Tree only — simpler.", "Repeated scans.", "Visited array.", "For each unvisited start DFS.", ["Build adj", "Loop nodes", "DFS/BFS"], DFS, "O(V+E)", "O(V)"),
    (40, "Cycle Detection (Graph)", "GRAPH", "DFS with 3-color or Union-Find.", "Back edge = cycle in directed.", ["course schedule", "cycle"], "Detect cycle directed/undirected.", "DAG topological sort.", "Try all paths.", "Gray node revisited = cycle.", "DFS coloring.", ["WHITE/GRAY/BLACK", "DFS"], "boolean hasCycle(int u)", "O(V+E)", "O(V)"),
    (41, "Topological Sort", "GRAPH", "Ordering with all edges forward — Kahn or DFS postorder.", "Dependencies first.", ["course schedule", "dependency"], "DAG ordering.", "Cycle exists — impossible.", "Brute all permutations.", "In-degree 0 queue.", "Kahn BFS.", ["In-degree", "Queue zeros", "Reduce"], "Queue<Integer> q; // Kahn", "O(V+E)", "O(V)"),
    (42, "Union Find / DSU", "GRAPH", "Disjoint set with path compression + rank.", "Groups merge; ask same set.", ["connected components", "redundant connection"], "Dynamic connectivity.", "Static graph one-time DFS enough.", "BFS each query.", "Path compression flattens tree.", "find with compression; union by rank.", ["parent[], rank[]", "find", "union"], "class UF{int[]p,r;int find(int x){...}void union(int a,int b){...}}", "α(n) amortized", "O(n)"),
    (43, "Shortest Path — BFS", "GRAPH", "Unweighted shortest path — BFS levels.", "Each edge weight 1.", ["shortest path", "minimum steps", "unweighted"], "Unweighted shortest path.", "Weighted edges.", "DFS may not be shortest.", "First visit = shortest.", "BFS with distance array.", ["Queue", "dist[]", "Expand"], BFS, "O(V+E)", "O(V)"),
    (44, "Dijkstra", "GRAPH", "Non-negative weighted shortest path with min-heap.", "Greedy expand closest unvisited.", ["weighted graph", "network delay"], "Non-negative edge weights.", "Negative weights.", "Bellman-Ford always.", "Settled node distance is final.", "Heap of (dist, node).", ["dist[]", "PQ", "Relax edges"], "PriorityQueue<long[]> pq=new PriorityQueue<>((a,b)->Long.compare(a[0],b[0]));", "O((V+E) log V)", "O(V)"),
    (45, "MST — Kruskal / Prim", "GRAPH", "Minimum spanning tree — sort edges or grow from node.", "Connect all min total weight.", ["min cost", "connect all"], "MST in undirected weighted graph.", "Shortest path not MST.", "Try all spanning trees.", "Kruskal: UF + sort edges.", "Prim: heap grow.", ["Sort edges UF", "Or Prim PQ"], "Kruskal with UF", "O(E log E)", "O(V)"),
    (46, "Subsets", "BACKTRACKING", "Include/exclude each element.", "Binary choice tree.", ["subsets", "power set"], "All subsets.", "Need count only — 2^n formula.", "Iterative copy.", "Each level decide include.", "backtrack(idx).", ["path", "for i from idx", "choose/not"], "void bt(int i){if(i==n){res.add(new ArrayList<>(path));return;}path.add(nums[i]);bt(i+1);path.remove(path.size()-1);bt(i+1);}", "O(n*2^n)", "O(n)"),
    (47, "Permutations", "BACKTRACKING", "Swap or used[] to build all orderings.", "Fill position by position.", ["permutations", "arrangements"], "All orderings.", "Need subset not order.", "Next permutation only.", "used array prevents reuse.", "backtrack with used.", ["used[]", "path", "base n"], "void bt(){if(path.size()==n){...}for...}", "O(n!)", "O(n)"),
    (48, "Combination Sum", "BACKTRACKING", "Reuse allowed — same idx can repeat.", "Unbounded knapsack style search.", ["combination sum", "candidates"], "Combinations summing to target.", "Distinct elements only.", "Nested loops depth.", "Start idx prevents permutations.", "bt(idx, remain).", ["if remain==0 add", "for i from idx"], "void bt(int i,int rem){...}", "O(2^target)", "O(target)"),
    (49, "Constraint Search / Pruning", "BACKTRACKING", "Cut branches that violate constraints early.", "Don't explore doomed paths.", ["N-queens", "sudoku"], "Heavy constraint satisfaction.", "Loose constraints brute ok.", "Full search.", "Check valid before recurse.", "Prune on failure.", ["isValid", "place", "backtrack"], "N-Queens bt", "O(n!)", "O(n)"),
    (50, "Greedy with Proof", "GREEDY", "Local optimal via exchange argument.", "Prove swapping never hurts.", ["jump game", "gas station"], "Greedy optimal with proof.", "Overlapping subproblems — DP.", "Try all.", "Exchange argument.", "Track farthest reachable.", ["Greedy measure", "Update", "Prove"], "int far=0;for(...)", "O(n)", "O(1)"),
    (51, "Scheduling / Interval Greedy", "GREEDY", "Sort by end time; pick non-overlapping max.", "Earliest finish leaves room.", ["activity selection", "meeting rooms"], "Interval scheduling greedy.", "Weighted intervals — DP.", "All subsets.", "Sort by end.", "Greedy pick.", ["Sort end", "Take if start>=lastEnd"], "Activity selection", "O(n log n)", "O(1)"),
    (52, "1D DP", "DYNAMIC PROGRAMMING", "dp[i] = best answer using first i elements.", "Linear table of subproblems.", ["climbing stairs", "house robber", "decode ways"], "Optimal substructure linear.", "No overlapping states.", "Recursion exponential.", "dp[i] from dp[i-1], dp[i-2].", "Tabulation or memo.", ["Define dp", "Base cases", "Transition"], "int[] dp=new int[n+1];dp[0]=1;", "O(n)", "O(n) or O(1)"),
    (53, "2D/Grid DP", "DYNAMIC PROGRAMMING", "dp[r][c] from top/left neighbors.", "Fill grid bottom-right.", ["unique paths", "min path sum"], "Grid path optimization.", "1D sufficient.", "Recurse all paths.", "Only from up and left.", "Nested loops.", ["Init first row/col", "dp[r][c]=min(up,left)+val"], "int[][] dp=new int[m][n];", "O(mn)", "O(mn)"),
    (54, "Knapsack", "DYNAMIC PROGRAMMING", "0/1: take or skip; unbounded: reuse.", "Capacity dimension DP.", ["knapsack", "subset sum", "partition"], "Capacity/budget optimization.", "Unlimited greedy works.", "Try all subsets.", "dp[w] max value with weight w.", "Iterate items and weights.", ["dp[0..W]", "For each item", "Reverse w for 0/1"], "int[] dp=new int[cap+1];", "O(nW)", "O(W)"),
    (55, "Subsequence DP", "DYNAMIC PROGRAMMING", "LCS/LIS/Palindrome subsequence.", "Two sequence or LIS patience.", ["LCS", "LIS", "palindrome subseq"], "Subsequence not substring.", "Contiguous — sliding window.", "Generate all subseq.", "dp[i][j] match chars.", "O(n²) or patience O(n log n) for LIS.", ["Define states", "Transitions"], "LCS dp table", "O(nm)", "O(nm)"),
    (56, "State-machine DP", "DYNAMIC PROGRAMMING", "dp[day][holding] stock problems.", "Finite states per step.", ["buy sell stock", "cooldown"], "Stock with states hold/sold/cool.", "No state needed.", "Brute all transactions.", "State transitions limited.", "dp[i][0/1].", ["States", "Day loop", "Max profit"], "int sold=0, hold=Integer.MIN_VALUE;", "O(n)", "O(1)"),
    (57, "DP on Trees", "DYNAMIC PROGRAMMING", "Postorder aggregate subtree answers.", "Each node combines child DP.", ["tree DP", "max path"], "Tree optimization.", "Linear DP.", "Recompute subtrees.", "Postorder.", "Return tuple from children.", ["DFS", "Merge child results"], "Tree DP postorder", "O(n)", "O(h)"),
    (58, "DP + Optimization", "DYNAMIC PROGRAMMING", "Monotonic deque/convex hull speed DP.", "Reduce inner loop with structure.", ["dp optimization", "sliding window max in DP"], "DP transition bottleneck.", "Small constraints brute.", "O(n²) DP.", "Deque maintains optimal window.", "Optimize transition.", ["DP loop", "Deque helper"], "Monotonic deque DP", "O(n)", "O(n)"),
    (59, "Trie", "ADVANCED", "Prefix tree for strings/words.", "Character edges per level.", ["prefix", "autocomplete", "word search"], "Prefix queries, dictionary.", "Few strings hash enough.", "Hash all prefixes.", "Shared prefixes compressed.", "Node children[26].", ["Insert", "Search", "startsWith"], "class TrieNode{TrieNode[] ch=new TrieNode[26];}", "O(L)", "O(total chars)"),
    (60, "Bit Manipulation", "ADVANCED", "XOR/AND tricks for parity, subsets, masks.", "Bits encode state compactly.", ["single number", "subset XOR", "power of two"], "XOR cancel pairs; bit masks.", "Large numbers need BigInteger.", "Hash count.", "a^a=0; n&(n-1) clears lowest bit.", "Bitmask DP or tricks.", ["XOR all", "n&=n-1", "1<<i"], "int xor=0;for(int x:nums)xor^=x;", "O(n)", "O(1)"),
    (61, "Sweep Line", "ADVANCED", "Events sorted by coordinate process status.", "Timeline of interval start/end.", ["skyline", "meeting rooms II"], "Count overlapping intervals over time.", "Few intervals merge enough.", "Check all pairs.", "Sort events; active count.", "Priority queue or counter.", ["Events +1/-1", "Sort", "Sweep"], "int[][] events; Arrays.sort(events,...)", "O(n log n)", "O(n)"),
    (62, "Prefix + Hashing Combo", "ADVANCED", "Prefix sum with mod/count map.", "Subarray sum k classic.", ["subarray sum k", "count subarrays"], "Exact subarray count/sum.", "Non-contiguous.", "All pairs.", "prefix[j]-prefix[i]=k.", "Map prefix mod counts.", ["prefix", "map", "update count"], "Map<Long,Integer> cnt=new HashMap<>();", "O(n)", "O(n)"),
    (63, "Binary Search + Greedy", "ADVANCED", "Check feasibility greedily for BS answer.", "Split array largest sum.", ["minimize max", "capacity to ship"], "Partition with greedy check.", "No monotonic check.", "Try all partitions.", "Greedy pack into minimal bins.", "BS on answer + greedy.", ["BS lo,hi", "can(mid) greedy"], "BS + greedy pack", "O(n log S)", "O(1)"),
    (64, "Graph + DP Combinations", "ADVANCED", "DAG DP longest path; tree DP on graphs.", "Topological order then relax.", ["longest path DAG", "critical path"], "DP on directed acyclic graph.", "Cycles — not DAG.", "All paths.", "Topo order enables 1D DP on nodes.", "Topo + relax edges.", ["Topo sort", "dp[node]", "Relax"], "Topo + dp longest", "O(V+E)", "O(V)"),
]

for t in _MORE:
    num, name, cat, intu, model, triggers, wu, wn, bf, obs, opt, algo, java, time, space = t
    PATTERNS.append(Pattern(
        num=num, name=name, category=cat, intuition=intu, mental_model=model,
        triggers=triggers if isinstance(triggers, list) else [triggers],
        when_use=wu, when_not=wn, brute_force=bf, observation=obs, optimal=opt,
        algorithm=algo if isinstance(algo, list) else [algo],
        java_template=java, time=time, space=space,
        mistakes=["Not handling edge cases", "Wrong complexity analysis"],
        edge_cases=["Empty input", "Single element", "Maximum constraints"],
        recognize_30s=f"Triggers: {', '.join(triggers[:3]) if isinstance(triggers, list) else triggers}",
        trap=f"Using {name} when constraints don't fit.",
        followup="How does complexity change with constraints?",
        variation="Combine with another pattern for harder variants.",
        examples_easy=[_ex(f"{name} Easy", "Canonical easy problem", opt)],
        examples_medium=[_ex(f"{name} Medium", "Interview variant", opt)],
        examples_hard=[_ex(f"{name} Hard", "Google-style twist", opt)],
    ))


def get_all_patterns() -> list[Pattern]:
    return sorted(PATTERNS, key=lambda p: p.num)
