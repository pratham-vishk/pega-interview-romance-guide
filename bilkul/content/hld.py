"""High-Level Design / System Design framework."""

from content.helpers import bullets, section, table, tip, curiosity


BUILDING_BLOCKS = [
    ("Client", "User-facing app", "No entry point", "CDN cache static assets"),
    ("CDN", "Edge cache for static content", "High latency, origin overload", "Geographic distribution"),
    ("DNS", "Resolve domain to IP", "Users can't find service", "GeoDNS routing"),
    ("Load Balancer", "Distribute traffic L4/L7", "Single server bottleneck", "Round-robin, least conn, health checks"),
    ("API Gateway", "Auth, rate limit, routing", "Services exposed directly", "Per-route policies"),
    ("Service", "Business logic microservice", "No functionality", "Horizontal scale, stateless"),
    ("Cache", "Redis/Memcached hot data", "DB overload", "TTL, eviction, cache-aside"),
    ("Database", "Persistent storage", "No durability", "Replication, sharding"),
    ("Kafka", "Durable event streaming", "Tight coupling, lost events", "Partitions, consumer groups"),
    ("Object Storage", "S3 blobs/media", "DB bloat", "Cheap durable storage"),
    ("Search", "Elasticsearch full-text", "Slow SQL LIKE queries", "Inverted index"),
    ("Monitoring", "Metrics, logs, traces", "Blind to failures", "Prometheus, Grafana, alerting"),
]

HLD_CONCEPTS = [
    ("Requirement clarification", "Scope the problem before designing"),
    ("Functional requirements", "What the system must do"),
    ("Non-functional requirements", "Scale, latency, availability, consistency"),
    ("QPS estimation", "DAU × actions/day ÷ 86400"),
    ("Storage estimation", "Records × size × retention"),
    ("API design", "REST/gRPC endpoints, idempotency keys"),
    ("Caching", "Cache-aside, write-through, TTL strategy"),
    ("Load balancing", "L4 vs L7 — your resume: Dell L4/L7 experience"),
    ("Kafka", "Async decoupling, replay, ordering per partition"),
    ("Replication", "Leader-follower, read replicas"),
    ("Sharding", "Partition by user_id hash"),
    ("Consistency", "Strong vs eventual — CAP trade-off"),
    ("Idempotency", "Safe retries with idempotency keys"),
    ("Rate limiting", "Token bucket, sliding window"),
    ("Circuit breaker", "Fail fast when downstream unhealthy"),
    ("Backpressure", "Slow consumers don't crash producers"),
    ("Observability", "Metrics, logs, distributed tracing"),
]

SYSTEM_DESIGNS = [
    "URL Shortener", "Rate Limiter", "Notification System", "File Storage", "Chat System",
    "YouTube", "Instagram", "Uber", "Food Delivery", "Ticket Booking",
    "Payment System", "Distributed Job Scheduler", "Metrics/Logging Platform",
    "Web Crawler", "Search Autocomplete",
]


def _system_design_card(name: str, difficulty: str) -> str:
    return f"""
<div class="pattern-card">
<h3>{name} <span class="badge">{difficulty}</span></h3>
<h4>Requirements</h4>
<p>Clarify functional + NFR: scale, latency p99, availability SLA, consistency needs.</p>
<h4>Capacity Estimation</h4>
<p>QPS, storage/year, bandwidth. Show math on whiteboard.</p>
<h4>API</h4>
<p>Core endpoints with request/response. Idempotency for writes.</p>
<h4>High-Level Architecture</h4>
<p>Client → CDN → LB → API Gateway → Services → Cache/DB/Kafka</p>
<h4>Data Model</h4>
<p>Key tables/documents, indexes, shard key.</p>
<h4>Scaling</h4>
<p>Horizontal service scale, DB sharding, read replicas, async via Kafka.</p>
<h4>Failure Handling</h4>
<p>Retries with backoff, circuit breaker, dead letter queue, failover.</p>
<h4>L4 Follow-up</h4>
<p>How cache invalidation works? What happens when DB primary fails?</p>
<h4>L5 Follow-up</h4>
<p>Multi-region consistency? Cost optimization? Hot key problem?</p>
<label><input type="checkbox" id="sd-done-{name.lower().replace(' ','-')}" data-track> Completed {name} design (+50 XP)</label>
</div>"""


def build_hld_section() -> str:
    body = curiosity("Why does Kafka exist if REST APIs already exist? REST is sync request-response; Kafka is durable async log for decoupling, replay, and burst absorption.")
    body += "<h3>HLD Framework — 28 Concepts</h3>"
    rows = [(c[0], c[1]) for c in HLD_CONCEPTS]
    body += table(["Concept", "Why / What problem"], rows)
    body += "<h3>Architecture Building Blocks</h3>"
    block_rows = [(b[0], f"{b[1]} | Without it: {b[2]} | Scale: {b[3]}") for b in BUILDING_BLOCKS]
    body += table(["Component", "Role / Failure / Scaling"], block_rows)
    body += """
<div class="diagram-box">
<pre style="text-align:left;font-size:8pt;">
Client → CDN → DNS → Load Balancer → API Gateway
                                        ↓
                              ┌─────────┴─────────┐
                              Service A    Service B
                                  ↓            ↓
                              Cache ←────→ Database
                                  ↓
                               Kafka → Workers → Object Storage
                                  ↓
                            Monitoring / Search
</pre>
</div>"""
    body += "<h3>System Design Questions (15)</h3>"
    for i, sd in enumerate(SYSTEM_DESIGNS):
        diff = "L4" if i < 8 else "L4/L5"
        body += _system_design_card(sd, diff)
    body += tip("L4: end-to-end design with trade-offs. L5: deep dives on consistency, cost, org-scale migration, failure domains.")
    return section("hld", "High-Level Design (HLD / System Design)", body)
