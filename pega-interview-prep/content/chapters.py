"""Build all chapter HTML for the Pega interview guide."""

from pathlib import Path
from content.top50_interview import build_top50_chapter, build_verification_chapter


def img(diagrams: dict, key: str, caption: str) -> str:
  path = diagrams.get(key, "")
  if not path:
    return ""
  p = Path(path)
  if not p.exists():
    return ""
  svg_content = p.read_text(encoding="utf-8")
  # Inline SVG for reliable WeasyPrint rendering
  return f"""
<div class="diagram-box">
  {svg_content}
  <div class="diagram-caption">Figure: {caption}</div>
</div>"""


def build_chapters(diagrams: dict) -> str:
    d = lambda k, c: img(diagrams, k, c)
    return f"""
<!-- COVER -->
<div class="cover">
  <div style="font-size:36pt">💕</div>
  <h1>Pega Interview<br>Romance Guide</h1>
  <p class="subtitle">The One-Stop, Nothing-Missed, Diagram-Packed Edition</p>
  <p><strong>3+ Years · CSA / SSA · Every Concept · Every Diagram</strong></p>
  <p class="dedication">
    Hey brilliant — this is your complete interview soulmate. 32 chapters, 23 diagrams,
    Top 50 Q&amp;A in easy language, 200+ rapid-fire questions, and zero topics left behind.
  </p>
</div>

<!-- MASTER CHECKLIST -->
<div class="toc">
<h2>Master Topic Checklist — Nothing Gets Missed</h2>
<p>Every item below is covered in this guide with explanation, Q&amp;A, and/or diagram.</p>
<ul class="master-checklist">
<li>☑ Pega Platform &amp; BPM Architecture</li>
<li>☑ App Studio / Dev Studio / Admin Studio / Prediction Studio</li>
<li>☑ Pega Infinity &amp; Center-Out Architecture</li>
<li>☑ Pega Cloud vs On-Premises</li>
<li>☑ Class Hierarchy (Pattern &amp; Directed Inheritance)</li>
<li>☑ Abstract vs Concrete Classes</li>
<li>☑ Class Groups &amp; Work Pools</li>
<li>☑ Rule Types (Complete Catalog)</li>
<li>☑ Rule Resolution (10 Steps)</li>
<li>☑ Rulesets, Versions &amp; Application Stack</li>
<li>☑ Circumstance (Date &amp; Template)</li>
<li>☑ Rule Availability (Available, Blocked, Final, Withdrawn)</li>
<li>☑ FUA / Rules Cache</li>
<li>☑ Case Type Anatomy</li>
<li>☑ Case Lifecycle &amp; Statuses</li>
<li>☑ Stages, Processes, Steps</li>
<li>☑ Parent / Child / Cover Cases</li>
<li>☑ Flow Shapes (All)</li>
<li>☑ Flow Actions (Local vs Connector)</li>
<li>☑ Subprocess, Utility, Wait, Split-Join, Split-ForEach</li>
<li>☑ Assignments &amp; Routing</li>
<li>☑ Worklist, Workbasket, Work Queue</li>
<li>☑ Clipboard &amp; Page Structure</li>
<li>☑ Property Types (All)</li>
<li>☑ Page List vs Page Group</li>
<li>☑ Embedded vs Linked Pages</li>
<li>☑ Data Pages (All Types &amp; Load Modes)</li>
<li>☑ Data Page Sources &amp; Parameters</li>
<li>☑ Savable Data Pages &amp; Save Plans</li>
<li>☑ Data Transforms (All Actions)</li>
<li>☑ Activities &amp; Key Methods</li>
<li>☑ Decision Rules (When, Table, Tree, MapValue, Scorecard)</li>
<li>☑ Decision Strategies &amp; CDH</li>
<li>☑ Declare Rules (Expression, Constraint, OnChange, Trigger, Index)</li>
<li>☑ Validation (Validate, Edit Validate, Constraint)</li>
<li>☑ UI: Section, Harness, Layout, Portal, Skin</li>
<li>☑ Constellation, Cosmos, Views, Widgets</li>
<li>☑ DX API &amp; pxAPI</li>
<li>☑ SLAs (Goal, Deadline, Passed Deadline)</li>
<li>☑ Urgency</li>
<li>☑ Connect-REST / SOAP / SQL / Kafka / MQ</li>
<li>☑ Service-REST / SOAP / Kafka</li>
<li>☑ Authentication (OAuth, JWT, Basic, API Key)</li>
<li>☑ Data Types</li>
<li>☑ Security: Operator, Access Group, Role, Privilege</li>
<li>☑ ABAC &amp; Access When</li>
<li>☑ Property Security</li>
<li>☑ Agents &amp; Job Schedulers</li>
<li>☑ Queue For Agent</li>
<li>☑ Report Definitions &amp; Associations</li>
<li>☑ Unit Testing &amp; Scenario Testing</li>
<li>☑ PAL, Tracer, Clipboard Inspector</li>
<li>☑ Guardrails (Complete List)</li>
<li>☑ DevOps: Branch, Merge, RAP, Product Rule</li>
<li>☑ Deployment Manager &amp; Pipelines</li>
<li>☑ Git Repository Integration</li>
<li>☑ Email &amp; Correspondence</li>
<li>☑ Document Generation</li>
<li>☑ RPA / Robotics</li>
<li>☑ Data Flows &amp; Stream Processing</li>
<li>☑ Prediction Studio &amp; ML</li>
<li>☑ GenAI in Pega</li>
<li>☑ DCR &amp; Pega Express</li>
<li>☑ Localization &amp; Field Values</li>
<li>☑ Feature Toggles</li>
<li>☑ Multi-Tenancy</li>
<li>☑ Object Persistence (Obj-Open/Save/Delete)</li>
<li>☑ Performance Debugging Methodology</li>
<li>☑ Validation Flow (Edit Validate → Validate → Constraint)</li>
</ul>

<h2>Table of Contents</h2>
<ol>
<li>Platform &amp; Architecture</li>
<li>Class Hierarchy &amp; Inheritance</li>
<li>Rules Catalog &amp; Rule Resolution</li>
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
<li>UI Layer — Traditional &amp; Constellation</li>
<li>SLAs &amp; Urgency</li>
<li>Integration &amp; Data Types</li>
<li>Security Model</li>
<li>Agents, Queues &amp; Job Schedulers</li>
<li>Reporting</li>
<li>Testing Strategy</li>
<li>Performance, PAL &amp; Guardrails</li>
<li>DevOps &amp; Deployment</li>
<li>Email, Documents &amp; Correspondence</li>
<li>Advanced: CDH, RPA, Data Flow, AI</li>
<li>Controls, Field Values &amp; Localization</li>
<li>Object Layer &amp; Persistence</li>
<li>Top 50 Most-Asked Questions (Easy Answers)</li>
<li>200 Rapid-Fire Questions</li>
<li>Mock Interview Scenarios</li>
<li>Final Checklist &amp; STAR Stories</li>
<li>Topic Verification Matrix</li>
</ol>
</div>

<!-- CH 1 -->
<div class="chapter" id="ch1">
<h2>Chapter 1: Platform &amp; Architecture</h2>
<div class="flirt-box">Before we get serious — let's talk architecture. Every great love story has layers, and Pega has six of them.</div>

<h3>Pega in One Sentence</h3>
<div class="easy-box"><strong>In simple words:</strong> Pega lets you build business apps (like banking, insurance, healthcare) by configuring <em>rules</em> instead of writing thousands of lines of code. Think of it as smart LEGO blocks for enterprise software.</div>
<p>Pega is a <strong>model-driven, low-code platform</strong> for BPM, CRM, and Case Management — rules are declarative, cases have lifecycles, and the engine resolves the right rule at runtime.</p>

<h3>Architecture Layers</h3>
<table>
<tr><th>Layer</th><th>Purpose</th><th>Key Rules</th></tr>
<tr><td>Presentation</td><td>User interaction</td><td>Section, Harness, View, Portal, Layout</td></tr>
<tr><td>Case / Process</td><td>Workflow orchestration</td><td>Case Type, Flow, Flow Action, Stage</td></tr>
<tr><td>Decision</td><td>Business logic</td><td>When, Decision Table, MapValue, Strategy</td></tr>
<tr><td>Data</td><td>Data access &amp; transform</td><td>Data Page, Data Transform, Report Definition</td></tr>
<tr><td>Integration</td><td>External systems</td><td>Connect-REST, Service-REST, Connect-Kafka</td></tr>
<tr><td>Security</td><td>Access control</td><td>Access Group, Role, Privilege, Access When</td></tr>
</table>

<h3>Studio Types</h3>
<table>
<tr><th>Studio</th><th>Users</th><th>Purpose</th></tr>
<tr><td>App Studio</td><td>Business developers, BAs</td><td>Low-code case design, personas, guided config</td></tr>
<tr><td>Dev Studio</td><td>Technical developers, SSA</td><td>Full rule editing, tracer, PAL, advanced config</td></tr>
<tr><td>Admin Studio</td><td>Admins</td><td>System config, agents, nodes, security audits</td></tr>
<tr><td>Prediction Studio</td><td>Data scientists</td><td>ML models, adaptive analytics, text analytics</td></tr>
</table>

<div class="qa-block"><div class="question">Q: What is Center-Out architecture?</div>
<div class="answer">Design <strong>data, logic, and decisions once</strong> at the center of the platform, then expose through any channel (web, mobile, API, chatbot). Avoids channel-specific silos. Constellation UI + Data Pages + Case Types embody this.</div></div>

<div class="qa-block"><div class="question">Q: Pega Cloud vs On-Prem?</div>
<div class="answer"><strong>Pega Cloud</strong> — Pega-managed infrastructure, auto-patching, scaling, DevOps built-in. <strong>On-Prem</strong> — customer manages servers, DB, patching. Same platform capabilities; deployment model differs.</div></div>

<div class="qa-block"><div class="question">Q: What is Pega Express?</div>
<div class="answer">Rapid delivery methodology: DCO workshops → MVP case types → iterative sprints. Delivers production apps in weeks using guardrails and templates.</div></div>
</div>

<!-- CH 2 -->
<div class="chapter" id="ch2">
<h2>Chapter 2: Class Hierarchy &amp; Inheritance</h2>
<div class="flirt-box">Know your family tree before introducing your rules to the world. Inheritance is how Pega avoids duplication — and how you avoid repeating yourself in interviews.</div>
{d("07-class-hierarchy", "Pega Class Hierarchy — Pattern Inheritance")}

<h3>Class Categories</h3>
<table>
<tr><th>Prefix</th><th>Purpose</th><th>Example</th></tr>
<tr><td>Work-</td><td>Case instances</td><td>Work-Cover-LoanApp</td></tr>
<tr><td>Data-</td><td>Data objects, reference data</td><td>Data-Customer</td></tr>
<tr><td>Rule-</td><td>All rule instances</td><td>Rule-Obj-Activity</td></tr>
<tr><td>Assign-</td><td>Assignment instances</td><td>Assign-Worklist</td></tr>
<tr><td>History-</td><td>Audit records</td><td>History-Work</td></tr>
<tr><td>Index-</td><td>Search indexes</td><td>Index-Work</td></tr>
<tr><td>System-</td><td>System objects</td><td>System-Queue-ServiceLevel</td></tr>
</table>

<div class="qa-block"><div class="question">Q: Pattern vs Directed inheritance?</div>
<div class="answer"><strong>Pattern</strong> — automatic parent from namespace (<code>Work-Cover-LoanApp</code> inherits <code>Work-Cover-</code>). <strong>Directed</strong> — explicit parent class outside namespace for cross-application reuse.</div></div>

<div class="qa-block"><div class="question">Q: Abstract vs Concrete class?</div>
<div class="answer"><strong>Abstract</strong> — no instances created; exists for inheritance. <strong>Concrete</strong> — instances can be created and persisted.</div></div>

<div class="qa-block"><div class="question">Q: What is a Class Group (Work Pool)?</div>
<div class="answer">Groups related case types under one DB table (<code>pc_work</code>). Defined in Application rule. Operators get access via Access Group work pool setting.</div></div>
</div>

<!-- CH 3 -->
<div class="chapter" id="ch3">
<h2>Chapter 3: Rules Catalog &amp; Rule Resolution</h2>
<div class="flirt-box">Rule Resolution is Pega's matchmaking algorithm — it finds THE ONE rule from thousands. Memorize this flowchart like it's our song.</div>
<div class="easy-box"><strong>In simple words:</strong> Imagine 10 versions of the same rule in different folders. Rule Resolution is Pega's brain figuring out which exact version to use right now — based on class, version, date, and conditions.</div>
{d("01-rule-resolution", "Rule Resolution — 10-Step Algorithm")}

<h3>Complete Rule Types Catalog</h3>
<table>
<tr><th>Category</th><th>Rule Types</th></tr>
<tr><td>Process</td><td>Case Type, Flow, Flow Action, Stage, Process</td></tr>
<tr><td>Data</td><td>Property, Data Page, Data Transform, Data Type, Report Definition</td></tr>
<tr><td>Decision</td><td>When, Decision Table, Decision Tree, MapValue, Scorecard, Strategy</td></tr>
<tr><td>Declare</td><td>Declare Expression, Constraint, OnChange, Trigger, Index</td></tr>
<tr><td>UI</td><td>Section, Harness, Layout, View, Portal, Skin, Control</td></tr>
<tr><td>Integration</td><td>Connect-REST, Service-REST, Connect-SOAP, Connect-Kafka, Auth Profile</td></tr>
<tr><td>Security</td><td>Access Group, Role, Privilege, Access When, Authentication Service</td></tr>
<tr><td>System</td><td>Activity, Agent, Job Scheduler, Application, Ruleset, Class</td></tr>
<tr><td>Validation</td><td>Validate, Edit Validate</td></tr>
<tr><td>Advanced</td><td>Data Flow, Data Set, Robotic Activity, Correspondence</td></tr>
</table>

<h3>Rule Availability States</h3>
<table>
<tr><th>State</th><th>Meaning</th></tr>
<tr><td>Available</td><td>Active, participates in resolution</td></tr>
<tr><td>Not Available</td><td>Saved but excluded from resolution</td></tr>
<tr><td>Blocked</td><td>Explicitly excluded (lower rules win)</td></tr>
<tr><td>Final</td><td>Cannot be overridden by child classes</td></tr>
<tr><td>Withdrawn</td><td>Deprecated, never resolved</td></tr>
</table>

<div class="qa-block"><div class="question">Q: What is Circumstance?</div>
<div class="answer">A <strong>variant</strong> of a rule for specific conditions. <strong>Date circumstance</strong> — effective date range. <strong>Template circumstance</strong> — property-based (e.g., Country=US). More specific circumstance wins.</div></div>

<div class="qa-block"><div class="question">Q: What is FUA?</div>
<div class="answer"><strong>Full Rule Assembly</strong> — cached, compiled version of a resolved rule. First call is slow (assembly); subsequent calls use cache. Flush on rule save or ruleset change.</div></div>
</div>

<!-- CH 4 -->
<div class="chapter" id="ch4">
<h2>Chapter 4: Application Stack &amp; Rulesets</h2>
{d("13-application-stack", "Application Stack — Ruleset Version Hierarchy")}

<div class="qa-block"><div class="question">Q: Ruleset version format?</div>
<div class="answer"><code>MM-mm-nn</code> (Major-minor-patch). Example: <code>MyApp:01-02-03</code>. Application rule lists rulesets in resolution order.</div></div>

<div class="qa-block"><div class="question">Q: What is a built-on application?</div>
<div class="answer">Your application <strong>inherits</strong> rulesets from a parent application (e.g., built on PegaRULES). Enables layering: platform → framework → implementation.</div></div>

<div class="qa-block"><div class="question">Q: What is a branch?</div>
<div class="answer">Parallel development stream for isolated feature work. Rules saved to branch ruleset. <strong>Merge</strong> combines into target ruleset. Prevents team conflicts.</div></div>
</div>

<!-- CH 5 -->
<div class="chapter" id="ch5">
<h2>Chapter 5: Case Management &amp; Lifecycle</h2>
<div class="flirt-box">Cases are love stories with a beginning, middle, and resolution. Know every status like you know every mood.</div>
{d("15-case-type-anatomy", "Case Type — Complete Anatomy Mind Map")}
{d("02-case-lifecycle", "Case Lifecycle State Diagram")}

<h3>Case Statuses</h3>
<table>
<tr><th>Status</th><th>Meaning</th></tr>
<tr><td>New</td><td>Created, not yet in active processing</td></tr>
<tr><td>Open</td><td>Active processing</td></tr>
<tr><td>Pending-...</td><td>Waiting for external event, timer, or dependency</td></tr>
<tr><td>Resolved-Completed</td><td>Successfully completed</td></tr>
<tr><td>Resolved-Cancelled</td><td>Withdrawn / cancelled</td></tr>
</table>

<div class="qa-block"><div class="question">Q: Parent vs Child vs Cover case?</div>
<div class="answer"><strong>Child case</strong> — separate case type linked to parent. <strong>Cover case</strong> — parent container holding multiple related subcases. <strong>Spin-off</strong> — create child from parent mid-flow.</div></div>

<div class="qa-block"><div class="question">Q: Case-wide vs Stage-specific actions?</div>
<div class="answer"><strong>Case-wide</strong> — available in all stages (Transfer, Update). <strong>Stage-specific</strong> — only in configured stage (Submit, Approve).</div></div>

<div class="qa-block"><div class="question">Q: What is a Wait shape?</div>
<div class="answer">Pauses flow until: timer expires, child case resolves, or external event received. Assignment becomes <code>Pending-...</code>.</div></div>
</div>

<!-- CH 6 -->
<div class="chapter" id="ch6">
<h2>Chapter 6: Flows, Processes &amp; Flow Actions</h2>
{d("03-flow-shapes", "Flow Shapes — Complete Process Flow")}
{d("18-save-case-sequence", "Sequence: Submit Assignment &amp; Save Case")}

<h3>All Flow Shapes</h3>
<table>
<tr><th>Shape</th><th>Purpose</th><th>Creates Assignment?</th></tr>
<tr><td>Assignment</td><td>Human task</td><td>Yes</td></tr>
<tr><td>Decision</td><td>Branch on When rule</td><td>No</td></tr>
<tr><td>Utility</td><td>Automated step (DT/Activity)</td><td>No</td></tr>
<tr><td>Subprocess</td><td>Call another flow</td><td>Depends</td></tr>
<tr><td>Wait</td><td>Pause for event/timer</td><td>Yes (pending)</td></tr>
<tr><td>Split-Join</td><td>Parallel branches, then join</td><td>Per branch</td></tr>
<tr><td>Split-ForEach</td><td>Loop over page list</td><td>Per iteration</td></tr>
<tr><td>Notify</td><td>Send notification</td><td>No</td></tr>
</table>

<div class="qa-block"><div class="question">Q: Flow vs Flow Action?</div>
<div class="answer"><strong>Flow</strong> — backend process (shapes). <strong>Flow Action</strong> — user-facing button (Approve, Submit) with UI section. Flow Action may call a flow or just update assignment.</div></div>

<div class="qa-block"><div class="question">Q: Local vs Connector Flow Action?</div>
<div class="answer"><strong>Local</strong> — stays on same screen (modal/inline). <strong>Connector</strong> — navigates to new assignment/harness.</div></div>
</div>

<!-- CH 7 -->
<div class="chapter" id="ch7">
<h2>Chapter 7: Assignments &amp; Routing</h2>
{d("11-assignment-routing", "Assignment Routing Decision Flow")}

<div class="qa-block"><div class="question">Q: Worklist vs Workbasket vs Work Queue?</div>
<div class="answer"><strong>Worklist</strong> — personal queue for one operator. <strong>Workbasket</strong> — shared team pool. <strong>Work Queue</strong> — named queue, can be routed dynamically.</div></div>

<div class="qa-block"><div class="question">Q: What is urgency?</div>
<div class="answer">Numeric priority (10–100). Increases as SLA deadlines approach. Higher urgency = higher in worklist sort order.</div></div>
</div>

<!-- CH 8 -->
<div class="chapter" id="ch8">
<h2>Chapter 8: Clipboard &amp; Data Model</h2>
{d("12-clipboard-structure", "Clipboard Page Structure")}

<h3>Property Types — Complete</h3>
<table>
<tr><th>Type</th><th>Description</th><th>Syntax</th></tr>
<tr><td>Text</td><td>String</td><td><code>.Name</code></td></tr>
<tr><td>Integer / Decimal</td><td>Numbers</td><td><code>.Amount</code></td></tr>
<tr><td>Date / DateTime</td><td>Temporal</td><td><code>.SubmittedDate</code></td></tr>
<tr><td>TrueFalse</td><td>Boolean</td><td><code>.IsActive</code></td></tr>
<tr><td>Page</td><td>Embedded object</td><td><code>.Customer</code></td></tr>
<tr><td>Page List</td><td>Ordered collection</td><td><code>.Items(1)</code></td></tr>
<tr><td>Page Group</td><td>Keyed collection</td><td><code>.Docs("ID1")</code></td></tr>
<tr><td>Value List / Group</td><td>Scalar collections</td><td><code>.Tags(1)</code></td></tr>
</table>

<div class="qa-block"><div class="question">Q: Page List vs Page Group?</div>
<div class="answer"><strong>Page List</strong> — integer-indexed, ordered. <strong>Page Group</strong> — string-keyed, unordered. Use list for sequences, group for named lookups.</div></div>

<div class="qa-block"><div class="question">Q: Embedded vs Linked pages?</div>
<div class="answer"><strong>Embedded</strong> — stored inside parent (serialized together). <strong>Linked</strong> — reference via <code>pxLinkedRefTo</code>; separate clipboard page.</div></div>
</div>

<!-- CH 9 -->
<div class="chapter" id="ch9">
<h2>Chapter 9: Data Pages</h2>
<div class="easy-box"><strong>In simple words:</strong> Instead of writing code to fetch customer data every time, you create a Data Page called <code>D_Customer</code>. Pega fetches it, caches it, and hands it to you — like a personal assistant who remembers what you asked for.</div>
{d("04-data-page-load", "Sequence: Data Page Load with Caching")}

<h3>Load Modes</h3>
<table>
<tr><th>Mode</th><th>Scope</th><th>Use When</th></tr>
<tr><td>Reload per interaction</td><td>Request</td><td>Always fresh data</td></tr>
<tr><td>Reload once per requestor</td><td>User session</td><td>User-specific reference data</td></tr>
<tr><td>Reload if older than X</td><td>Time-based</td><td>Semi-static data</td></tr>
<tr><td>Access group</td><td>Access group</td><td>Shared config per app role</td></tr>
<tr><td>Node</td><td>Cluster node</td><td>Expensive, rarely changing data</td></tr>
</table>

<div class="qa-block"><div class="question">Q: Data Page sources?</div>
<div class="answer">Report Definition, Activity, Connector (REST), Lookup (DB), Data Transform, or another Data Page.</div></div>

<div class="qa-block"><div class="question">Q: Savable Data Page?</div>
<div class="answer">Editable Data Page with <strong>Save Plan</strong> (Database/Activity) to persist changes. Used in Constellation for inline CRUD on Data Types.</div></div>
</div>

<!-- CH 10-11 -->
<div class="chapter" id="ch10">
<h2>Chapter 10: Data Transforms</h2>
<div class="easy-box"><strong>In simple words:</strong> A Data Transform is a recipe for moving data from A to B — copy name here, calculate total there, add a row to a list. No loops, no drama, just clean mapping.</div>
<h3>All DT Actions</h3>
<p>Set · Update Page · Append and Map to · Remove · When / Otherwise · For Each Page In · Apply Data Transform · Sort · Exit Data Transform</p>
<div class="qa-block"><div class="question">Q: DT vs Activity?</div>
<div class="answer">Always prefer <strong>Data Transform</strong> for mapping/simple logic. Use <strong>Activity</strong> only for complex iteration, integration orchestration, or legacy maintenance.</div></div>
</div>

<div class="chapter" id="ch11">
<h2>Chapter 11: Activities</h2>
<h3>Key Methods</h3>
<table>
<tr><th>Method</th><th>Purpose</th></tr>
<tr><td>Property-Set</td><td>Set property value</td></tr>
<tr><td>Call</td><td>Invoke sub-activity</td></tr>
<tr><td>Apply-DataTransform</td><td>Run DT</td></tr>
<tr><td>Obj-Open / Obj-Save / Obj-Delete</td><td>Persistence</td></tr>
<tr><td>Page-New / Page-Remove / Page-Copy</td><td>Clipboard management</td></tr>
<tr><td>RDB-List / RDB-Open</td><td>Direct SQL (avoid if possible)</td></tr>
<tr><td>Connect-REST</td><td>Call REST connector</td></tr>
<tr><td>Queue-For-Agent</td><td>Async processing</td></tr>
</table>
<div class="warning"><strong>Guardrail:</strong> Activities are procedural and being phased out. Say "DT first, Activity only when necessary."</div>
</div>

<!-- CH 12 -->
<div class="chapter" id="ch12">
<h2>Chapter 12: Decision Rules</h2>
{d("16-decision-rules-map", "Decision Rule Selection Flowchart")}
<div class="qa-block"><div class="question">Q: Decision Table vs Tree?</div>
<div class="answer"><strong>Table</strong> — grid of AND/OR conditions → outcomes; best for combinatorial logic. <strong>Tree</strong> — sequential if-else hierarchy; best for nested decisions.</div></div>
<div class="qa-block"><div class="question">Q: What is a Decision Strategy?</div>
<div class="answer">Component of <strong>Customer Decision Hub (CDH)</strong>. Combines Propositions, Filtering, Prioritization, and Arbitration for Next-Best-Action across channels.</div></div>
</div>

<!-- CH 13 -->
<div class="chapter" id="ch13">
<h2>Chapter 13: Declare Rules</h2>
{d("10-declare-expression", "Declare Expression — Forward Chaining")}
<table>
<tr><th>Rule</th><th>Fires When</th><th>Purpose</th></tr>
<tr><td>Declare Expression</td><td>Source property changes</td><td>Computed property (forward chaining)</td></tr>
<tr><td>Declare Constraint</td><td>Property set/save</td><td>Validation constraint</td></tr>
<tr><td>Declare OnChange</td><td>Property value changes</td><td>Trigger DT/Activity</td></tr>
<tr><td>Declare Trigger</td><td>Data instance committed</td><td>Post-save processing on Data- class</td></tr>
<tr><td>Declare Index</td><td>Instance saved</td><td>Maintain search index</td></tr>
</table>
</div>

<!-- CH 14 -->
<div class="chapter" id="ch14">
<h2>Chapter 14: Validation Rules</h2>
{d("19-validation-flow", "Validation Flow — Edit Validate → Validate → Constraint → Save")}
<table>
<tr><th>Rule</th><th>When</th><th>Where</th></tr>
<tr><td>Validate</td><td>Server-side on commit</td><td>Flow, Activity, DT</td></tr>
<tr><td>Edit Validate</td><td>Client + server</td><td>Property control, section</td></tr>
<tr><td>Declare Constraint</td><td>Property change</td><td>Declarative, any time</td></tr>
</table>
</div>

<!-- CH 15 -->
<div class="chapter" id="ch15">
<h2>Chapter 15: UI — Traditional &amp; Constellation</h2>
{d("17-constellation-architecture", "Constellation Center-Out UI Architecture")}
<table>
<tr><th>Traditional</th><th>Constellation (Modern)</th></tr>
<tr><td>Section</td><td>View</td></tr>
<tr><td>Harness</td><td>Full Page / Form</td></tr>
<tr><td>Portal</td><td>Shell + Theme</td></tr>
<tr><td>Dynamic Layout</td><td>Cosmos React components</td></tr>
<tr><td>Skin</td><td>Theme (design tokens)</td></tr>
</table>
<div class="qa-block"><div class="question">Q: Why Constellation?</div>
<div class="answer">Responsive, omnichannel, React-based, faster development, no heavy harness customization, better performance, channel-agnostic via DX API.</div></div>
</div>

<!-- CH 16 -->
<div class="chapter" id="ch16">
<h2>Chapter 16: SLAs &amp; Urgency</h2>
{d("08-sla-timeline", "SLA Timeline — Goal → Deadline → Passed Deadline")}
<div class="qa-block"><div class="question">Q: Assignment SLA vs Case SLA?</div>
<div class="answer"><strong>Assignment SLA</strong> — per task. <strong>Stage/Case SLA</strong> — per stage or overall case duration.</div></div>
</div>

<!-- CH 17 -->
<div class="chapter" id="ch17">
<h2>Chapter 17: Integration &amp; Data Types</h2>
{d("05-rest-integration", "Sequence: REST Integration via Connect-REST")}
<table>
<tr><th>Rule</th><th>Direction</th></tr>
<tr><td>Connect-REST / SOAP / SQL / Kafka / MQ</td><td>Outbound</td></tr>
<tr><td>Service-REST / SOAP / Kafka</td><td>Inbound</td></tr>
</table>
<div class="qa-block"><div class="question">Q: What is a Data Type?</div>
<div class="answer">Pega-managed <code>Data-</code> class with auto-generated CRUD UI, REST API, and storage. Modern way to manage master/reference data.</div></div>
<div class="qa-block"><div class="question">Q: Authentication options?</div>
<div class="answer">Basic Auth, OAuth 2.0, JWT, API Key, Custom (Authentication Service rule). Outbound uses Authentication Profile.</div></div>
</div>

<!-- CH 18 -->
<div class="chapter" id="ch18">
<h2>Chapter 18: Security Model</h2>
{d("06-security-model", "Security Chain — Operator to Privilege")}
<div class="qa-block"><div class="question">Q: What is ABAC?</div>
<div class="answer"><strong>Attribute-Based Access Control</strong> — access based on property values (region, department). Implemented via Access When rules on cases, properties, flow actions.</div></div>
</div>

<!-- CH 19 -->
<div class="chapter" id="ch19">
<h2>Chapter 19: Agents, Queues &amp; Job Schedulers</h2>
{d("14-agent-processing", "Sequence: Queue-For-Agent Processing")}
<table>
<tr><th></th><th>Agent</th><th>Job Scheduler</th></tr>
<tr><td>Best for</td><td>High-volume async queues</td><td>Scheduled tasks</td></tr>
<tr><td>Modern preference</td><td>Legacy for new work</td><td>Preferred for new dev</td></tr>
</table>
</div>

<!-- CH 20-22 -->
<div class="chapter" id="ch20">
<h2>Chapter 20: Reporting</h2>
<div class="easy-box"><strong>In simple words:</strong> Report Definition is a saved SQL query in Pega. Use it for dashboards, manager reports, and as a Data Page source. Always prefer it over writing raw SQL in activities.</div>
<p><strong>Report Definition</strong> replaces Summary View. Uses SQL via association rules for joins. Optimize with indexes, limit columns, avoid functions on indexed WHERE columns.</p>
<div class="qa-block"><div class="question">Q: How to join two classes in a report?</div>
<div class="answer">Create an <strong>Association</strong> rule linking the two classes, then use it in the Report Definition join tab. Example: join Work- case to Data- Customer on CustomerID.</div></div>
<div class="qa-block"><div class="question">Q: Report Definition vs Data Page?</div>
<div class="answer"><strong>Report Definition</strong> = query engine (SQL). <strong>Data Page</strong> = smart layer on top (can use Report Def as source + caching + parameters). Use Data Page in UI; Report Def for analytics.</div></div>
</div>

<div class="chapter" id="ch21">
<h2>Chapter 21: Testing Strategy</h2>
{d("21-testing-strategy", "Testing Strategy — Unit vs Scenario vs CI Pipeline")}
<p><strong>Unit Test Case</strong> — individual rules (DT, Activity, Decision). <strong>Scenario Test</strong> — end-to-end case lifecycle (UI automation). Use dedicated <strong>Test Application</strong> and test ruleset.</p>
<div class="qa-block"><div class="question">Q: How to run tests in CI?</div>
<div class="answer">Export test cases in RAP, import to QA via Deployment Manager pipeline, execute PegaUnits + scenario tests as pipeline stage gate before production promotion.</div></div>
</div>

<div class="chapter" id="ch22">
<h2>Chapter 22: Performance, PAL &amp; Guardrails</h2>
{d("23-performance-debug", "Performance Debugging Decision Flowchart")}
<h3>Performance Tools</h3>
<p>PAL · Tracer · Clipboard Inspector · DB Trace · Rule Inspector</p>
<h3>Complete Guardrails List</h3>
<ol>
<li>Max 5 flow actions per assignment</li>
<li>Prefer Data Transforms over Activities</li>
<li>Limit ~200 properties per class</li>
<li>Use Data Pages, not repeated DB calls</li>
<li>No looping Activities on large datasets</li>
<li>Use Declare Index, not RDB-List in loops</li>
<li>Don't store large blobs in clipboard</li>
<li>Prefer Report Definition over RDB-List</li>
<li>Use pagination for large lists</li>
<li>Avoid custom Java when OOTB works</li>
<li>Use dynamic layouts, not freeform</li>
<li>Limit cascade of sub-activities</li>
<li>Keep clipboard under 2MB per request</li>
<li>PAL: alert if DB ops &gt; 50 or clipboard &gt; 2MB</li>
</ol>
<div class="qa-block"><div class="question">Q: N+1 query problem?</div>
<div class="answer">Loop calling Obj-Open/Data Page per row = N+1 DB calls. Fix: batch Data Page, Report Def with join, paginated load.</div></div>
</div>

<!-- CH 23 -->
<div class="chapter" id="ch23">
<h2>Chapter 23: DevOps &amp; Deployment</h2>
{d("09-deployment-pipeline", "DevOps Deployment Pipeline")}
<p><strong>RAP</strong> = Ruleset Archive Package. <strong>Product Rule</strong> defines contents. <strong>Deployment Manager</strong> orchestrates pipelines. <strong>Git Repository</strong> for version control. <strong>Skim</strong> removes unreferenced rules before packaging.</p>
</div>

<!-- CH 24-27 -->
<div class="chapter" id="ch24">
<h2>Chapter 24: Email, Documents &amp; Correspondence</h2>
<div class="easy-box"><strong>In simple words:</strong> Correspondence rules are email templates. Flows use "Send Email" shape to notify customers. Inbound email can even create new cases automatically.</div>
<p><strong>Correspondence rule</strong> — email templates. <strong>Send Email Smart Shape</strong> in flows. <strong>Email Account</strong> — SMTP config. <strong>Inbound email</strong> — Service Email creates/updates cases. <strong>Document generation</strong> — HTML/PDF templates attached via correspondence.</p>
<div class="qa-block"><div class="question">Q: How to send email from a flow?</div>
<div class="answer">Add <strong>Send Email</strong> smart shape → select Correspondence rule → map properties to template placeholders → configure Email Account for SMTP.</div></div>
</div>

<div class="chapter" id="ch25">
<h2>Chapter 25: Advanced — CDH, RPA, Data Flow, AI</h2>
<div class="easy-box"><strong>In simple words:</strong> CDH = "show the right offer to the right customer." RPA = "let a robot click in old desktop apps." Data Flow = "process millions of rows." GenAI = "Pega helps write emails and summarize cases."</div>
<p><strong>CDH</strong> — Next-Best-Action via Strategies. <strong>RPA</strong> — Robot Studio automates desktop apps. <strong>Data Flow</strong> — streaming/batch pipeline (Kafka). <strong>Prediction Studio</strong> — ML models. <strong>GenAI</strong> — case summarization, email drafting, Socrates chat.</p>
<div class="qa-block"><div class="question">Q: What is Next-Best-Action?</div>
<div class="answer">Pega analyzes customer data + AI models to decide the <strong>single best action</strong> to take (offer, message, retention). Used in marketing, sales, and service across channels.</div></div>
</div>

<div class="chapter" id="ch26">
<h2>Chapter 26: Controls, Field Values &amp; Localization</h2>
{d("22-feature-toggle", "Feature Toggle — Runtime Feature Switching")}
<p><strong>Field Value</strong> — key-value pairs for dropdowns. <strong>Localization</strong> — locale-specific labels via Field Value rules. <strong>Feature Toggle</strong> — runtime feature on/off without deployment. Controls: pxDropdown, pxAutoComplete, pxDateTime, pxTextInput.</p>
</div>

<div class="chapter" id="ch27">
<h2>Chapter 27: Object Layer &amp; Persistence</h2>
{d("20-object-persistence", "Object Persistence — Obj-Open / Obj-Save / Obj-Delete")}
<p><strong>Obj-Open</strong> — read from DB. <strong>Obj-Save</strong> — write to DB. <strong>Obj-Delete</strong> — remove. <strong>Obj-Open-By-Handle</strong> — open by pzInsKey. <strong>pxCommitDateTime</strong> — last DB commit. <strong>pzInsKey</strong> — unique instance key.</p>
<div class="qa-block"><div class="question">Q: Obj-Save vs Commit?</div>
<div class="answer"><strong>Obj-Save</strong> writes instance to DB. In flows, the engine auto-commits on assignment submit. In activities, may need <strong>Commit</strong> method for transaction control.</div></div>
</div>

{build_top50_chapter()}

<!-- CH 29 RAPID FIRE -->
<div class="chapter" id="ch29">
<h2>Chapter 29: 200 Rapid-Fire Questions</h2>
<div class="flirt-box">200 questions. Zero escape. You survive this chapter, you survive any panel.</div>
<div class="cheat"><ol>
<li>BPM? → Business Process Management</li>
<li>Case class prefix? → Work-</li>
<li>Default flow? → pyDefault</li>
<li>Case creator property? → pxCreateOperator</li>
<li>Case status? → pyStatusWork</li>
<li>Assignment urgency? → pxUrgencyAssign</li>
<li>Last update time? → pxUpdateDateTime</li>
<li>Rule base class? → Rule-</li>
<li>Ruleset version format? → MM-mm-nn</li>
<li>FUA? → Full Rule Assembly cache</li>
<li>Work pool? → Class group</li>
<li>Commit time? → pxCommitDateTime</li>
<li>Assignment class? → Assign-</li>
<li>Current flow? → pyFlowName</li>
<li>Step page? → pyStepPage</li>
<li>Current stage label? → pxCurrentStageLabel</li>
<li>Resolve? → Complete assignment</li>
<li>Spin-off? → Create child case</li>
<li>Cover case? → Parent of related cases</li>
<li>Cover key? → pxCoverInsKey</li>
<li>DCO? → Direct Capture of Objectives</li>
<li>Pega Express? → Rapid delivery methodology</li>
<li>Guardrails score? → Application health %</li>
<li>PAL DB warning? → &gt;50 operations</li>
<li>Clipboard warning? → &gt;2MB</li>
<li>DB ops counter? → pxRDBIO</li>
<li>Field Value? → Dropdown key-value</li>
<li>Validate rule? → Server validation</li>
<li>Edit Validate? → Client+server validation</li>
<li>Constraint? → Declare Constraint</li>
<li>Route to? → pxRouteTo</li>
<li>WorkBasket? → Team queue</li>
<li>Org unit? → pxOrgUnit</li>
<li>Division? → pxDivision</li>
<li>Application name? → pxApplication</li>
<li>Process name? → pxProcessName</li>
<li>Task name? → pxTaskName</li>
<li>Constellation? → Modern React UI</li>
<li>Cosmos? → Design system</li>
<li>DX API? → Digital Experience API</li>
<li>pxAPI? → Pega REST layer</li>
<li>Instance key? → pzInsKey</li>
<li>Object class? → pxObjClass</li>
<li>Open by handle? → Obj-Open-By-Handle</li>
<li>Linked page ref? → pxLinkedRefTo</li>
<li>Access role rule? → Rule-Access-Role-Obj</li>
<li>Access When? → Rule-Access-When</li>
<li>Thread name? → pxThreadName</li>
<li>Page list index? → pxSubscript</li>
<li>Results page? → pxResults</li>
<li>RDB-List? → SQL list in activity</li>
<li>Obj-Sort? → Sort page list</li>
<li>Obj-Filter? → Filter page list</li>
<li>Forward chaining? → Auto recalc declares</li>
<li>Data Page params? → pxDPParameters</li>
<li>SLA queue class? → System-Queue-ServiceLevel</li>
<li>Core ruleset? → Pega-Engine</li>
<li>Process ruleset? → Pega-ProCom</li>
<li>Root class? → @baseclass</li>
<li>Withdrawn? → Deprecated rule</li>
<li>Final rule? → Cannot override</li>
<li>Blocked? → Excluded from resolution</li>
<li>Available? → Active rule</li>
<li>Not Available? → Saved but inactive</li>
<li>Current stage? → pxCurrentStage</li>
<li>Sub-status? → pxSubStatus</li>
<li>Save time? → pxSaveDateTime</li>
<li>Update operator? → pxUpdateOperator</li>
<li>Case links? → pyCaseLinks</li>
<li>Work parties? → pyWorkParties</li>
<li>Party role? → pxPartyRole</li>
<li>MapValue use? → 1:1 lookup mapping</li>
<li>Scorecard use? → Weighted scoring</li>
<li>Strategy use? → CDH decisioning</li>
<li>Split-Join? → Parallel processing</li>
<li>Split-ForEach? → Loop page list in flow</li>
<li>Utility shape? → Automated no-assignment step</li>
<li>Subprocess? → Call another flow</li>
<li>Wait types? → Timer, case dependency, event</li>
<li>Reload once? → Data page load mode</li>
<li>Node scope cache? → Shared per cluster node</li>
<li>Save Plan? → Persist editable data page</li>
<li>Authentication Profile? → Outbound auth config</li>
<li>Service Package? → Groups inbound services</li>
<li>Product rule? → Defines RAP contents</li>
<li>Skim? → Remove unreferenced rules</li>
<li>Branch merge? → Combine branch to target</li>
<li>Scenario test? → E2E UI automation</li>
<li>Unit test? → Single rule test</li>
<li>Tracer? → Real-time rule execution trace</li>
<li>PAL? → Performance Analyzer</li>
<li>Declare Index? → Search index maintenance</li>
<li>Declare Trigger? → On commit of Data- instance</li>
<li>Declare OnChange? → On property change</li>
<li>Proposition? → CDH offer/action</li>
<li>Adaptive model? → Self-learning ML</li>
<li>Text analyzer? → NLP in Prediction Studio</li>
<li>Robotic automation? → Desktop app automation</li>
<li>Job Scheduler vs Agent? → Scheduled vs queue polling</li>
<li>Queue-For-Agent? → Defer to agent queue</li>
<li>Association rule? → Join classes in reports</li>
<li>Report Definition? → Modern SQL report rule</li>
<li>Summary View? → Legacy (use Report Def)</li>
<li>Harness types? → New, Perform, Review, Confirm</li>
<li>Local flow action? → Same screen action</li>
<li>Connector flow action? → Navigates to new screen</li>
<li>Dynamic layout? → Responsive flex layout</li>
<li>Freeform layout? → Legacy absolute positioning</li>
<li>Skin rule? → Application look and feel</li>
<li>Portal? → Application shell</li>
<li>Work group? → Group of operators</li>
<li>Access group? → App + roles + portal</li>
<li>Privilege? → Atomic permission</li>
<li>Role? → Collection of privileges</li>
<li>ABAC? → Attribute-based access control</li>
<li>Property security? → Read/write restrictions</li>
<li>Circumstance date? → Time-based rule variant</li>
<li>Circumstance template? → Property-based variant</li>
<li>Directed inheritance? → Explicit parent class</li>
<li>Pattern inheritance? → Namespace hierarchy</li>
<li>Class group table? → pc_work (default)</li>
<li>Data type REST? → Auto-generated CRUD API</li>
<li>Connect-Kafka? → Outbound event streaming</li>
<li>Data Flow? → Batch/stream processing pipeline</li>
<li>Data Set? → Source/sink for data flows</li>
<li>Feature toggle? → Runtime on/off switch</li>
<li>Localization? → Locale-specific labels</li>
<li>Multi-tenancy? → Logical tenant isolation</li>
<li>Repository? → Git integration for rules</li>
<li>Deployment pipeline? → Dev→QA→Prod automation</li>
<li>Guardrail: flow actions? → Max 5 per assignment</li>
<li>Guardrail: activities? → Avoid; use DT</li>
<li>Guardrail: properties? → ~200 per class</li>
<li>pyWorkPage? → Primary case data page</li>
<li>pxRequestor? → Operator session context</li>
<li>pxThread? → Session thread with assignments</li>
<li>param page? → Activity/DT parameters</li>
<li>Step page? → Flow shape page context</li>
<li>Page-Copy? → Copy clipboard page</li>
<li>Page-Merge? → Merge two pages</li>
<li>Property-Map? → Map between pages</li>
<li>Show-Page? → Display harness</li>
<li>Log-Message? → Write to log</li>
<li>Rule resolution cache? → FUA</li>
<li>Application rule? → Defines app stack</li>
<li>Built-on application? → Parent app inheritance</li>
<li>Instance handle? → pxInsHandle</li>
<li>Operator ID page? → OperatorID</li>
<li>Workbasket vs worklist? → Team pool vs personal</li>
<li>Goal interval? → SLA first threshold</li>
<li>Deadline interval? → SLA must-complete</li>
<li>Passed deadline? → SLA overdue actions</li>
<li>SLA agent? → Pega-ProCom:ServiceLevelEvents</li>
<li>Urgency initial? → Default 10</li>
<li>Urgency max? → Typically 100</li>
<li>GenAI Socrates? → AI assistant in App Studio</li>
<li>Center-out? → Design once, deploy everywhere</li>
<li>Pega Infinity? → Unified 8.x+ platform</li>
<li>App Studio persona? → Business developer UX</li>
<li>Admin Studio? → System administration</li>
<li>Prediction Studio? → ML model management</li>
<li>DCR? → Direct Capture Requirements</li>
<li>View (Constellation)? → Replaces Section</li>
<li>Widget? → Reusable UI component</li>
<li>Theme? → Constellation design tokens</li>
<li>Editable data page? → Supports save plan</li>
<li>Read-only data page? → Lookup/reference</li>
<li>List data page? → Returns page list</li>
<li>Singleton data page? → Single object</li>
<li>Stale-while-revalidate? → Return cache, refresh async</li>
<li>HTTP 401 handling? → Auth error in connector</li>
<li>OAuth 2.0? → Token-based auth</li>
<li>JWT? → JSON Web Token auth</li>
<li>Keystore? → Certificate storage</li>
<li>Inbound email service? → Create case from email</li>
<li>Correspondence? → Email/letter template</li>
<li>PDF generation? → HTML template to PDF</li>
<li>AttachAsPDF? → Attach doc to case</li>
<li>RPA robot? → Desktop automation bot</li>
<li>Robot Studio? → Build RPA automations</li>
<li>NBAM? → Next Best Action Marketing</li>
<li>Proposition filter? → Filter offers in strategy</li>
<li>Prioritization? → Rank propositions</li>
<li>Arbitration? → Resolve strategy conflicts</li>
<li>Simulate? → Test decision strategies</li>
<li>Champion-challenger? → A/B test strategies</li>
<li>Text extraction? → NLP from documents</li>
<li>Sentiment analysis? → NLP feature</li>
<li>Entity extraction? → NLP feature</li>
<li>pxAPI case create? → REST case creation</li>
<li>pxUpdateCase? → REST case update</li>
<li>DX API v2? → Constellation API layer</li>
<li>Dynamic system setting? → Config via DSS rule</li>
<li>Declare Expression target? → Computed property</li>
<li>Declare Expression source? → Dependency properties</li>
<li>Auto-populate? → Property triggers DT/Activity</li>
<li>Edit input? → Client-side validation</li>
<li>Constraint message? → Error on violation</li>
<li>When in DT? → Conditional step</li>
<li>For Each Page In? → Loop in DT</li>
<li>Exit DT? → Stop transform execution</li>
<li>Call activity? → Invoke sub-activity</li>
<li>Branch in activity? → Conditional jump to label</li>
<li>Activity allow list? → Security restriction</li>
<li>Restricted activity? → Cannot call from UI</li>
<li>Obj-Delete? → Remove DB instance</li>
<li>History-Work? → Case audit trail</li>
<li>Index-Work? → Search index class</li>
</ol></div>
</div>

<!-- CH 30 MOCK -->
<div class="chapter" id="ch30">
<h2>Chapter 30: Mock Interview Scenarios</h2>
<div class="qa-block"><div class="question">Scenario 1: Design a Loan Application case type.</div>
<div class="answer">Stages: Application → Underwriting → Approval → Fulfillment. Data: Applicant, Income, CreditScore. Integrations: Credit Bureau via Connect-REST + Data Page. Decisions: Decision Table for eligibility. SLAs: 48hr underwriting deadline. Security: Loan Officer vs Underwriter roles.</div></div>
<div class="qa-block"><div class="question">Scenario 2: Production case is slow. How do you debug?</div>
<div class="answer">PAL before/after → Tracer with filters → DB Trace for SQL → Check Data Page load modes → Look for looping activities → Review clipboard size → Check N+1 patterns → Review guardrails compliance.</div></div>
<div class="qa-block"><div class="question">Scenario 3: Migrate traditional UI to Constellation.</div>
<div class="answer">Enable Constellation on case type → Convert Sections to Views → Replace Harnesses with Full Pages → Update Theme → Test DX API → Validate all flow actions → Run scenario tests → Deploy via pipeline.</div></div>
<div class="qa-block"><div class="question">Scenario 4: Implement role-based case access by region.</div>
<div class="answer">Create Access When rules checking <code>.Region = OperatorID.pyRegion</code>. Apply to case type, list views, and flow actions. Configure ABAC on property security for sensitive fields.</div></div>
</div>

<!-- CH 31 FINAL -->
<div class="chapter" id="ch31">
<h2>Chapter 31: Final Checklist &amp; STAR Stories</h2>
<div class="flirt-box">You made it — all 32 chapters, 23 diagrams, Top 50 Q&amp;A, 200 rapid-fire questions. You're not just prepared; you're dangerous. Go get that offer.</div>
<h3>Day-Before Checklist</h3>
<ul>
<li>☑ Draw Rule Resolution flowchart from memory</li>
<li>☑ Draw Case Lifecycle state diagram</li>
<li>☑ Explain Data Page load sequence</li>
<li>☑ Walk through REST integration flow</li>
<li>☑ Recite Security chain</li>
<li>☑ Name all flow shapes</li>
<li>☑ Compare DT vs Activity vs Data Page</li>
<li>☑ Explain Constellation vs Traditional</li>
<li>☑ Describe deployment pipeline</li>
<li>☑ List 10 guardrails</li>
<li>☑ Prepare 3 STAR project stories</li>
</ul>
<div class="teaser">💌 Every concept. Every diagram. Every question. Nothing missed. Now go be brilliant.</div>
<div class="footer-note">Pega Interview Romance Guide — Complete Verified Edition · 32 Chapters · 23 Diagrams · Top 50 + 200 Q&amp;A · CSA/SSA · 3+ Years</div>
</div>

{build_verification_chapter()}
"""
