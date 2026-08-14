"""Resume-specific interview context — based on provided resume bullets only."""

from content.helpers import section, table, trap, tip


# Resume bullets as provided in master prompt — NOT invented
RESUME_BULLETS = [
    ("Dell Technologies", "Employer context for backend/distributed systems experience"),
    ("Layer 4/Layer 7 load balancing", "L4 packet-level vs L7 HTTP routing — health checks, SSL termination"),
    ("S3/REST API traffic", "Object storage integration, REST API design for cloud storage"),
    ("Active storage nodes", "Storage cluster with active node management"),
    ("Multi-Agent Systems", "LLM agent orchestration architecture"),
    ("LLM/RAG", "Retrieval-augmented generation pipelines"),
    ("Private cloud", "On-prem / private cloud deployment constraints"),
    ("Cloud storage APIs", "API layer for storage operations"),
    ("Cluster scaling", "Horizontal scaling of storage/compute clusters"),
    ("Health checks", "LB and service health probe patterns"),
    ("Multi-site VDC", "Virtual datacenter across sites"),
    ("Geographic replication", "Cross-region data replication"),
    ("Global failover", "DR and failover orchestration"),
    ("Spring Boot", "Java microservices framework"),
    ("Kafka", "Async messaging, event-driven architecture"),
    ("Microservices", "Service decomposition and communication"),
    ("Asynchronous Java", "CompletableFuture, reactive patterns"),
    ("Performance optimization", "Profiling, bottleneck identification"),
    ("AI migration agent", "AI-assisted migration tooling"),
]


def _resume_questions(topic: str, context: str) -> str:
    slug = topic.lower().replace(" ", "-").replace("/", "-")
    return f"""
<div class="pattern-card">
<h3>{topic}</h3>
<p><em>Context: {context}</em></p>
<table>
<tr><th>Type</th><th>Question</th></tr>
<tr><td>Basic</td><td>Explain {topic} and where you used it.</td></tr>
<tr><td>Deep Technical</td><td>Walk through the implementation details of {topic} in your project.</td></tr>
<tr><td>Architecture</td><td>How did {topic} fit into the overall system architecture?</td></tr>
<tr><td>Scaling</td><td>What bottlenecks did you hit with {topic} and how did you scale?</td></tr>
<tr><td>Failure</td><td>What happens when {topic} fails? How did you detect and recover?</td></tr>
<tr><td>Trade-off</td><td>What alternatives to {topic} did you consider and why did you choose this?</td></tr>
<tr><td>L5 Follow-up</td><td>How would you redesign {topic} for 10x scale or multi-region?</td></tr>
</table>
</div>"""


DANGEROUS_CLAIMS = [
    ("Layer 4/Layer 7 load balancing", "Must explain OSI layers, health check types, sticky sessions, SSL termination"),
    ("Geographic replication", "Must explain sync vs async replication, RPO/RTO, conflict resolution"),
    ("Global failover", "Must explain DNS failover, split-brain, quorum, data consistency during failover"),
    ("Kafka", "Must explain partitions, consumer groups, ordering guarantees, exactly-once semantics"),
    ("Multi-Agent Systems / LLM/RAG", "Must explain retrieval pipeline, chunking, embedding, latency, hallucination mitigation"),
    ("Performance optimization", "Must cite specific metrics before/after, profiling tools, bottleneck identified"),
    ("AI migration agent", "Must explain agent workflow, human-in-loop, validation, rollback strategy"),
]


def build_resume_section() -> str:
    body = """
<p><strong>Important:</strong> Questions below are generated from resume bullets you provided.
Do not claim experience you cannot defend. Upload <code>Pratham_Resume.pdf</code> for bullet-level customization.</p>"""
    body += "<h3>Resume Experience Map</h3>"
    body += table(["Topic", "Context"], RESUME_BULLETS)
    body += "<h3>Questions Google Can Ask From Your Resume</h3>"
    key_topics = [
        "Layer 4/Layer 7 load balancing", "Kafka", "Geographic replication",
        "Global failover", "LLM/RAG", "Multi-Agent Systems",
        "S3/REST API traffic", "Cluster scaling", "Spring Boot microservices",
        "AI migration agent", "Performance optimization",
    ]
    ctx_map = dict(RESUME_BULLETS)
    for t in key_topics:
        body += _resume_questions(t, ctx_map.get(t, "From resume"))
    body += "<h3>⚠️ Dangerous Claims — Defend or Soften</h3>"
    body += table(["Claim", "What you MUST be able to explain"], DANGEROUS_CLAIMS)
    body += trap("Saying 'I built Kafka' when you consumed/produced events — be precise about your role.")
    body += tip("Use STAR format: Situation, Task, Action, Result — with metrics where possible.")
    return section("resume", "Resume Deep Dive — Google Questions", body)
