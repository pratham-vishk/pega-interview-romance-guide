"""Build all chapter HTML for the Pega interview guide."""

import base64
from pathlib import Path
from content.top50_interview import build_top50_chapter, build_verification_chapter
from content.full_chapters import build_all_full_chapters


def img(diagrams: dict, key: str, caption: str) -> str:
    path = diagrams.get(key, "")
    if not path:
        return ""
    p = Path(path)
    if not p.exists():
        return ""
    if p.suffix.lower() == ".png":
        b64 = base64.b64encode(p.read_bytes()).decode("ascii")
        src = f"data:image/png;base64,{b64}"
        return f"""
<div class="diagram-box">
  <img src="{src}" alt="{caption}"/>
  <div class="diagram-caption">📊 {caption}</div>
</div>"""
    from content.svg_fix import fix_svg_for_pdf
    svg_content = fix_svg_for_pdf(str(p))
    return f"""
<div class="diagram-box">
  {svg_content}
  <div class="diagram-caption">📊 {caption}</div>
</div>"""


def build_cover_and_toc() -> str:
    return """
<div class="cover">
  <div style="font-size:36pt">💕</div>
  <h1>Pega Interview<br>Romance Guide</h1>
  <p class="subtitle">Ultimate One-Stop Bible — Every Topic, Every Subtopic, Nothing Missed</p>
  <p><strong>27 Chapters · 473 Subtopics · 28 Diagrams · 250+ Q&amp;A · Romantic Full Explanations</strong></p>
  <p class="dedication">
    Hey gorgeous — this is the <em>complete</em> guide, not a teaser.<br><br>
    Every chapter explains <strong>every subtopic</strong> in simple romantic words: what it is, how it works, interview tip, flirty example, diagram, cheat sheet, and Q&amp;A.<br><br>
    Diagrams fit the page. Labels show. Topics don't get skipped. Start Chapter 1 — finish Chapter 27 — collect your offer. 💋
  </p>
</div>

<div class="toc">
<h2>📚 Complete Table of Contents</h2>
<p><strong>Each chapter includes:</strong> Simple explanation · Flirty example · Diagram · Cheat sheet · Interview Q&amp;A</p>
<ol>
<li>Platform &amp; Architecture — Complete Guide</li>
<li>Class Hierarchy &amp; Inheritance</li>
<li>Rules &amp; Rule Resolution (10 Steps)</li>
<li>Application Stack &amp; Rulesets</li>
<li>Case Management &amp; Lifecycle</li>
<li>Flows, Processes &amp; Flow Actions</li>
<li>Assignments &amp; Routing</li>
<li>Clipboard &amp; Data Model</li>
<li>Data Pages</li>
<li>Data Transforms</li>
<li>Activities</li>
<li>Decision Rules</li>
<li>Declare Rules</li>
<li>Validation Rules</li>
<li>UI &amp; Constellation</li>
<li>SLAs &amp; Urgency</li>
<li>Integration &amp; Data Types</li>
<li>Security Model</li>
<li>Agents &amp; Job Schedulers</li>
<li>Reporting</li>
<li>Testing Strategy</li>
<li>Performance &amp; Guardrails</li>
<li>DevOps &amp; Deployment</li>
<li>Email, Documents &amp; Correspondence</li>
<li>Advanced — CDH, RPA, AI</li>
<li>Controls, Field Values &amp; Localization</li>
<li>Object Layer &amp; Persistence</li>
<li>🏆 Master Interview Cheat Sheet</li>
<li>Top 50 Most-Asked Questions (Easy Answers)</li>
<li>200 Rapid-Fire Questions</li>
<li>Mock Interview Scenarios</li>
<li>Final Checklist &amp; STAR Stories</li>
<li>Topic Verification Matrix</li>
</ol>
</div>"""


def build_rapid_fire() -> str:
    return """
<div class="chapter" id="ch29">
<h2>Chapter 29: 200 Rapid-Fire Questions</h2>
<div class="flirt-box">200 questions. Zero mercy. You survive this chapter, you survive any interview panel in the world. Go get em, tiger. 🐯</div>
<div class="cheat"><ol>
<li>BPM? → Business Process Management</li>
<li>Case class prefix? → Work-</li>
<li>Default flow? → pyDefault</li>
<li>Case creator? → pxCreateOperator</li>
<li>Case status? → pyStatusWork</li>
<li>Assignment urgency? → pxUrgencyAssign</li>
<li>Last update? → pxUpdateDateTime</li>
<li>Rule base class? → Rule-</li>
<li>Ruleset version? → MM-mm-nn</li>
<li>FUA? → Full Rule Assembly cache</li>
<li>Work pool? → Class group</li>
<li>Commit time? → pxCommitDateTime</li>
<li>Assignment class? → Assign-</li>
<li>Current flow? → pyFlowName</li>
<li>Step page? → pyStepPage</li>
<li>Current stage? → pxCurrentStageLabel</li>
<li>Resolve? → Complete assignment</li>
<li>Spin-off? → Create child case</li>
<li>Cover case? → Parent of related cases</li>
<li>DCO? → Direct Capture of Objectives</li>
<li>Pega Express? → Rapid delivery methodology</li>
<li>PAL DB warning? → &gt;50 operations</li>
<li>Clipboard warning? → &gt;2MB</li>
<li>DB ops counter? → pxRDBIO</li>
<li>Field Value? → Dropdown key-value</li>
<li>Validate rule? → Server validation</li>
<li>Edit Validate? → Client+server validation</li>
<li>Constraint? → Declare Constraint</li>
<li>WorkBasket? → Team queue</li>
<li>Constellation? → Modern React UI</li>
<li>Cosmos? → Design system</li>
<li>DX API? → Digital Experience API</li>
<li>pxAPI? → Pega REST layer</li>
<li>Instance key? → pzInsKey</li>
<li>Object class? → pxObjClass</li>
<li>Open by handle? → Obj-Open-By-Handle</li>
<li>Linked page? → pxLinkedRefTo</li>
<li>Access role? → Rule-Access-Role-Obj</li>
<li>Access When? → Rule-Access-When</li>
<li>Thread? → pxThreadName</li>
<li>Page list index? → pxSubscript</li>
<li>Results page? → pxResults</li>
<li>RDB-List? → SQL in activity</li>
<li>Forward chaining? → Auto recalc declares</li>
<li>SLA queue? → System-Queue-ServiceLevel</li>
<li>Core ruleset? → Pega-Engine</li>
<li>Process ruleset? → Pega-ProCom</li>
<li>Root class? → @baseclass</li>
<li>Withdrawn rule? → Deprecated</li>
<li>Final rule? → Cannot override</li>
<li>Blocked rule? → Excluded from resolution</li>
<li>pyWorkPage? → Case data page</li>
<li>pxRequestor? → User session</li>
<li>pxThread? → Open assignments</li>
<li>MapValue? → 1:1 lookup</li>
<li>Scorecard? → Weighted scoring</li>
<li>Strategy? → CDH decisioning</li>
<li>Split-Join? → Parallel processing</li>
<li>Split-ForEach? → Loop page list</li>
<li>Utility shape? → Auto step no assignment</li>
<li>Subprocess? → Call another flow</li>
<li>Wait shape? → Pause for event/timer</li>
<li>Save Plan? → Persist editable DP</li>
<li>Auth Profile? → Outbound auth</li>
<li>Service Package? → Groups services</li>
<li>Product rule? → RAP contents</li>
<li>Skim? → Remove unreferenced rules</li>
<li>Scenario test? → E2E UI test</li>
<li>Unit test? → Single rule test</li>
<li>Tracer? → Rule execution trace</li>
<li>PAL? → Performance Analyzer</li>
<li>Declare Index? → Search index</li>
<li>Declare Trigger? → On Data- commit</li>
<li>Declare OnChange? → On property change</li>
<li>Proposition? → CDH offer</li>
<li>RPA? → Desktop automation</li>
<li>Job Scheduler? → Scheduled background task</li>
<li>Queue-For-Agent? → Async queue</li>
<li>Association? → Join in reports</li>
<li>Report Definition? → SQL report rule</li>
<li>Harness? → Screen container</li>
<li>Section? → UI fragment</li>
<li>View? → Constellation UI unit</li>
<li>Local flow action? → Same screen</li>
<li>Connector flow action? → New screen</li>
<li>Dynamic layout? → Responsive flex</li>
<li>Portal? → App shell</li>
<li>Access group? → App+roles+portal</li>
<li>Privilege? → Atomic permission</li>
<li>Role? → Privilege bundle</li>
<li>ABAC? → Property-based access</li>
<li>Circumstance? → Rule variant</li>
<li>Directed inheritance? → Explicit parent</li>
<li>Pattern inheritance? → Namespace parent</li>
<li>Data Type? → Managed Data- class</li>
<li>Connect-Kafka? → Outbound streaming</li>
<li>Data Flow? → Batch/stream pipeline</li>
<li>Feature toggle? → Runtime switch</li>
<li>Repository? → Git for rules</li>
<li>Deployment pipeline? → Dev→QA→Prod</li>
<li>GenAI Socrates? → AI in App Studio</li>
<li>Center-out? → Design once deploy everywhere</li>
<li>Pega Infinity? → Unified 8.x+ platform</li>
<li>NBAM? → Next Best Action Marketing</li>
<li>Obj-Save? → Write to DB</li>
<li>Obj-Open? → Read from DB</li>
<li>Obj-Delete? → Remove from DB</li>
<li>History-Work? → Audit trail</li>
<li>Index-Work? → Search index class</li>
<li>param page? → Parameters</li>
<li>pyStepPage? → Flow step context</li>
<li>pxCommitDateTime? → Last DB save</li>
<li>pxCreateDateTime? → Creation time</li>
<li>pxInsHandle? → Instance handle</li>
<li>OperatorID? → User page</li>
<li>Goal interval? → SLA first threshold</li>
<li>Deadline? → SLA must-complete</li>
<li>Passed deadline? → SLA overdue</li>
<li>SLA agent? → ServiceLevelEvents</li>
<li>Urgency default? → 10</li>
<li>Guardrail flow actions? → Max 5</li>
<li>Guardrail activities? → Avoid use DT</li>
<li>Inbound email? → Service Email</li>
<li>Correspondence? → Email template</li>
<li>Robot Studio? → RPA builder</li>
<li>Prediction Studio? → ML models</li>
<li>Admin Studio? → System admin</li>
<li>App Studio? → Business developer UI</li>
<li>Dev Studio? → Technical developer IDE</li>
<li>Built-on app? → Parent application</li>
<li>Branch merge? → Combine to target</li>
<li>RAP? → Rules export package</li>
<li>Test ruleset? → Isolated test rules</li>
<li>Property-Set? → Activity set value</li>
<li>Apply-DataTransform? → Run DT in activity</li>
<li>Page-Copy? → Copy clipboard page</li>
<li>Page-Merge? → Merge pages</li>
<li>Property-Map? → Map between pages</li>
<li>Show-Page? → Display harness</li>
<li>Log-Message? → Write to log</li>
<li>Nested If? → Legacy decision rule</li>
<li>Decision Tree? → Hierarchical decisions</li>
<li>Decision Table? → Grid conditions</li>
<li>When rule? → True/false condition</li>
<li>Auto-populate? → Property triggers DT</li>
<li>Reload once? → DP cache per session</li>
<li>Node cache? → DP shared per node</li>
<li>Editable DP? → Supports save plan</li>
<li>Read-only DP? → Lookup only</li>
<li>List DP? → Multiple results</li>
<li>Singleton DP? → Single object</li>
<li>OAuth 2.0? → Token auth</li>
<li>JWT? → JSON Web Token</li>
<li>Keystore? → Certificate store</li>
<li>Multi-tenancy? → Tenant isolation</li>
<li>Localization? → Multi-language labels</li>
<li>pxDPParameters? → DP params page</li>
<li>pyFlowName? → Current flow</li>
<li>pyCaseLinks? → Related cases</li>
<li>pyWorkParties? → Stakeholders</li>
<li>pxPartyRole? → Stakeholder role</li>
<li>pxSubStatus? → Case sub-status</li>
<li>pxUpdateOperator? → Last updater</li>
<li>pxRouteTo? → Routing target</li>
<li>pxApplication? → Current app</li>
<li>pxProcessName? → Current process</li>
<li>pxTaskName? → Current task</li>
<li>pxOrgUnit? → Org unit</li>
<li>pxDivision? → Division</li>
<li>Work group? → Operator group</li>
<li>Skin rule? → App look and feel</li>
<li>Theme? → Constellation styling</li>
<li>Widget? → Reusable UI component</li>
<li>Freeform layout? → Legacy — avoid</li>
<li>Declare Constraint? → Validation rule</li>
<li>Declare Expression? → Computed property</li>
<li>Connect-SOAP? → Outbound SOAP</li>
<li>Service-SOAP? → Inbound SOAP</li>
<li>Connect-SQL? → Direct DB query</li>
<li>Connect-MQ? → Message queue out</li>
<li>Data Set? → Data Flow source/sink</li>
<li>Stream? → Real-time processing</li>
<li>Adaptive model? → Self-learning ML</li>
<li>Text analyzer? → NLP feature</li>
<li>Champion-challenger? → A/B test strategy</li>
<li>Simulate? → Test CDH strategy</li>
<li>Arbitration? → Resolve strategy conflicts</li>
<li>Prioritization? → Rank propositions</li>
<li>Proposition filter? → Filter CDH offers</li>
<li>pxAPI create case? → REST case creation</li>
<li>pxUpdateCase? → REST case update</li>
<li>Dynamic system setting? → Config via DSS</li>
<li>Activity allow list? → Security restriction</li>
<li>Restricted activity? → Cannot call from UI</li>
<li>Call activity? → Invoke sub-activity</li>
<li>Branch activity? → Jump to label</li>
<li>Commit method? → Transaction commit</li>
<li>Rollback? → Undo transaction</li>
<li>Obj-Filter? → Filter page list</li>
<li>Obj-Sort? → Sort page list</li>
<li>Page-New? → Create clipboard page</li>
<li>Page-Remove? → Delete clipboard page</li>
<li>Queue-For-Agent? → Defer to agent</li>
<li>Connect-REST? → Outbound REST</li>
<li>Service-REST? → Inbound REST</li>
<li>Authentication Service? → Custom auth</li>
<li>Email Account? → SMTP config</li>
<li>Send Email shape? → Flow email step</li>
<li>PDF generation? → HTML to PDF</li>
<li>AttachAsPDF? → Attach doc to case</li>
<li>Guardrails score? → App health %</li>
<li>DCR? → Direct Capture Requirements</li>
<li>DCO? → Requirements workshop</li>
<li>Persona? → User role in App Studio</li>
<li>Stage SLA? → Per-stage time limit</li>
<li>Assignment SLA? → Per-task time limit</li>
<li>pxUrgencyWork? → Case urgency</li>
<li>pxCreateOpName? → Creator name</li>
<li>pxLastUpdateBy? → Last updater name</li>
<li>pxSaveDateTime? → Last save time</li>
<li>pxRefObjectKey? → Reference key</li>
<li>pxLinkedRefTo? → Linked page ref</li>
<li>pxObjClass? → Instance class</li>
<li>pxInsName? → Instance name</li>
</ol></div>
</div>"""


def build_mock_and_final() -> str:
    return """
<div class="chapter" id="ch30">
<h2>Chapter 30: Mock Interview Scenarios — With Full Answers</h2>
<div class="flirt-box">Real scenarios. Real answers. Read these out loud. Your confidence will thank you.</div>
<div class="qa-block"><div class="question">Scenario 1: Design a Loan Application case type from scratch.</div>
<div class="answer"><strong>Answer:</strong> Stages: Application → Document Collection → Underwriting → Approval → Disbursement. Data Model: Applicant (Page), Income, LoanAmount, CreditScore, Documents (Page List). Integrations: Credit Bureau via Connect-REST + Data Page with error handling. Decisions: Decision Table for eligibility (amount, score, employment). SLAs: 48hr underwriting deadline with escalation to manager. Security: Loan Officer creates, Underwriter reviews, Manager approves — separate roles and Access When by region. UI: Constellation views for each stage. Testing: Unit tests on DTs and Decision Table, scenario test for full lifecycle.</div></div>
<div class="qa-block"><div class="question">Scenario 2: Production case is very slow. Walk me through debugging.</div>
<div class="answer"><strong>Answer:</strong> 1) Run PAL before and after the slow action — check pxRDBIO (DB ops) and clipboard size. 2) If DB ops &gt; 50, use Tracer filtered by RDB methods. 3) Run DB Trace to see actual SQL. 4) Look for looping Activity calling Obj-Open per row (N+1). 5) Check Data Page load modes — should cache reference data. 6) Review guardrails compliance score. 7) Fix: replace loop with batch Data Page or Report Def with join.</div></div>
<div class="qa-block"><div class="question">Scenario 3: How would you migrate from traditional UI to Constellation?</div>
<div class="answer"><strong>Answer:</strong> 1) Enable Constellation on case type in Dev Studio. 2) Convert Sections to Views using conversion tool. 3) Replace Harnesses with Full Page forms. 4) Apply Cosmos Theme. 5) Test all flow actions work with DX API. 6) Run scenario tests for each user persona. 7) Deploy via branch → merge → RAP → pipeline. 8) Rollback plan: feature toggle to switch back.</div></div>
<div class="qa-block"><div class="question">Scenario 4: Implement region-based case access.</div>
<div class="answer"><strong>Answer:</strong> Create Access When rule: <code>.Region == OperatorID.pyRegion</code>. Apply to case type list view, individual case open, and sensitive flow actions. Add property security on SSN field — read-only unless Privilege 'ViewSSN'. Test with operators from different regions.</div></div>
<div class="qa-block"><div class="question">Scenario 5: Explain your typical day as a Pega developer.</div>
<div class="answer"><strong>Answer:</strong> Morning: check assigned stories, review guardrails on my branch. Dev: design/update case types, build Data Pages and DTs, configure integrations, write unit tests. Afternoon: code review teammates' branches, fix bugs using Tracer/PAL, update documentation. Deploy: merge branch, create RAP, push through Deployment Manager pipeline to QA.</div></div>
</div>

<div class="chapter" id="ch31">
<h2>Chapter 31: Final Checklist &amp; STAR Story Template</h2>
<div class="flirt-box">You read every chapter. Every diagram. Every cheat sheet. You're not going to an interview — you're going to collect what's yours. 💕</div>
<h3>☑ Night-Before Checklist</h3>
<ul>
<li>☑ Draw Rule Resolution 10-step flowchart from memory</li>
<li>☑ Draw Case Lifecycle state diagram</li>
<li>☑ Explain Data Page load sequence out loud</li>
<li>☑ Walk through REST integration (Connect-REST → Data Page → Case)</li>
<li>☑ Recite: Operator → Access Group → Role → Privilege → Access When</li>
<li>☑ Name all 8 flow shapes</li>
<li>☑ Compare DT vs Activity vs Data Page — when to use each</li>
<li>☑ Explain Constellation vs Traditional UI</li>
<li>☑ Describe DevOps pipeline: Branch → Merge → RAP → QA → Prod</li>
<li>☑ List 10 guardrails from memory</li>
<li>☑ Prepare 3 STAR stories from your real projects</li>
<li>☑ Review Master Cheat Sheet (Chapter 28)</li>
<li>☑ Skim Top 50 Q&amp;A (Chapter 29)</li>
</ul>
<h3>STAR Template</h3>
<div class="qa-block"><div class="question">S — Situation</div><div class="answer">"In my [project] at [company], we had [business problem]…"</div></div>
<div class="qa-block"><div class="question">T — Task</div><div class="answer">"I was responsible for [your role] and needed to [specific goal]…"</div></div>
<div class="qa-block"><div class="question">A — Action</div><div class="answer">"I designed [Case Type/Data Page/Integration] using [specific Pega rules]. I followed guardrails by [specific actions]…"</div></div>
<div class="qa-block"><div class="question">R — Result</div><div class="answer">"We reduced processing time by X%, achieved Y% guardrails compliance, deployed to production with zero defects…"</div></div>
<div class="teaser">💌 You are ready. Walk in like you already have the offer. Because honestly? You should.</div>
<div class="footer-note">Pega Interview Romance Guide — Complete Interview Bible · 28 Diagrams · 27 Full Chapters · Master Cheat Sheet · Top 50 + 200 Q&amp;A · CSA/SSA · 3+ Years</div>
</div>"""


def build_chapters(diagrams: dict) -> str:
    d = lambda k, c: img(diagrams, k, c)
    return (
        build_cover_and_toc()
        + build_all_full_chapters(d)
        + build_top50_chapter()
        + build_rapid_fire()
        + build_mock_and_final()
        + build_verification_chapter()
    )
