"""Complete interview-ready chapter content — full explanations, cheat sheets, Q&A."""

from content.helpers import simple, flirt_ex, cheat, qa, section, bullets, chapter_wrap


def build_all_full_chapters(d) -> str:
    """d is lambda key, caption for diagram images."""
    parts = [
        ch01_platform(d), ch02_classes(d), ch03_rules(d), ch04_rulesets(d),
        ch05_cases(d), ch06_flows(d), ch07_assignments(d), ch08_clipboard(d),
        ch09_datapages(d), ch10_dt(d), ch11_activities(d), ch12_decisions(d),
        ch13_declares(d), ch14_validation(d), ch15_ui(d), ch16_sla(d),
        ch17_integration(d), ch18_security(d), ch19_agents(d), ch20_reporting(d),
        ch21_testing(d), ch22_performance(d), ch23_devops(d), ch24_email(d),
        ch25_advanced(d), ch26_controls(d), ch27_persistence(d),
        master_cheat_sheet(),
    ]
    return "\n".join(parts)


def ch01_platform(d):
    body = f"""
{simple("Pega is a platform where you build business applications using <strong>rules</strong> instead of writing thousands of lines of Java. Think of it like configuring a smart factory — you define what happens (cases, flows, screens), and Pega runs it for you.")}
{section("What is Pega really?", "<p>Pega combines <strong>BPM</strong> (Business Process Management), <strong>CRM</strong>, and <strong>Case Management</strong> in one platform. Companies use it for loan processing, insurance claims, customer service, healthcare — anything with a workflow and data.</p>")}
{section("6 Architecture Layers — Know These Cold", """
<table><tr><th>Layer</th><th>What It Does</th><th>Rules You Must Know</th></tr>
<tr><td>Presentation</td><td>Screens users see</td><td>Section, Harness, View, Portal</td></tr>
<tr><td>Case/Process</td><td>Workflow engine</td><td>Case Type, Flow, Flow Action, Stage</td></tr>
<tr><td>Decision</td><td>Business logic IF/ELSE</td><td>When, Decision Table, MapValue</td></tr>
<tr><td>Data</td><td>Fetch & transform data</td><td>Data Page, Data Transform, Report Def</td></tr>
<tr><td>Integration</td><td>Talk to external systems</td><td>Connect-REST, Service-REST</td></tr>
<tr><td>Security</td><td>Who can do what</td><td>Access Group, Role, Privilege</td></tr></table>""")}
{flirt_ex("Imagine you're building a dating app for loan applications 💕 — the <strong>Case Type</strong> is the profile, <strong>Stages</strong> are 'Matched → Chatting → Meeting → Together', and <strong>Flows</strong> move each couple (case) through the journey. Pega is that app — but for business.")}
{cheat("Platform Basics", [
    ("BPM", "Managing business processes digitally"),
    ("Case", "One business request (one loan, one claim)"),
    ("Rule", "A configurable building block (not Java code)"),
    ("Low-code", "Build with clicks + config, minimal coding"),
    ("App Studio", "Simple UI for business developers"),
    ("Dev Studio", "Full power for technical developers"),
    ("Center-Out", "Design once, deploy to web/mobile/API"),
    ("Pega Infinity", "Modern unified platform (8.x+)"),
])}
{qa("What is Pega and why do companies use it?", "Pega lets enterprises build complex workflow apps fast using declarative rules. Benefits: case management built-in, change rules without recompiling, guardrails for quality, omnichannel via Constellation.")}
{qa("Difference between App Studio and Dev Studio?", "<strong>App Studio</strong> = guided, persona-based, low-code for BAs and junior devs. <strong>Dev Studio</strong> = full rule forms, Tracer, PAL, all rule types for senior developers.")}
{qa("What is Center-Out architecture?", "Build data, logic, and UI once at the center. Expose through any channel — web portal, mobile app, REST API. No duplicate logic per channel.")}
{qa("Pega Cloud vs On-Prem?", "<strong>Cloud</strong> = Pega hosts, patches, scales. <strong>On-Prem</strong> = you manage servers. Same platform features.")}
{qa("What is Pega Express?", "Rapid delivery approach: workshops → MVP in weeks → iterate. Uses templates and guardrails.")}
{qa("Name the 4 Studios in Pega.", "App Studio, Dev Studio, Admin Studio (system config), Prediction Studio (ML/AI models).")}
"""
    return chapter_wrap(1, "Platform & Architecture — Complete Guide", None, body, 0)


def ch02_classes(d):
    body = f"""
{simple("Classes in Pega are like <strong>folders in a family tree</strong>. Every rule and every data object belongs to a class. Child classes inherit rules from parents — so you never copy-paste.")}
{d("07-class-hierarchy", "Class Hierarchy — Work-, Data-, Rule- branches")}
{section("Class Prefixes — Memorize These", """
<table><tr><th>Prefix</th><th>Stores What</th><th>Example</th></tr>
<tr><td>Work-</td><td>Case instances</td><td>Work-Cover-LoanApp</td></tr>
<tr><td>Data-</td><td>Reference/master data</td><td>Data-Customer</td></tr>
<tr><td>Rule-</td><td>All rules</td><td>Rule-Obj-Activity</td></tr>
<tr><td>Assign-</td><td>Tasks/assignments</td><td>Assign-Worklist</td></tr>
<tr><td>History-</td><td>Audit trail</td><td>History-Work</td></tr>
<tr><td>Index-</td><td>Search indexes</td><td>Index-Work</td></tr></table>""")}
{flirt_ex("Think of <code>Work-Cover-LoanApp</code> as your type — and <code>Work-Cover-</code> as your family name. You inherit everything from the family without rewriting it. That's Pattern inheritance, babe.")}
{cheat("Class Hierarchy", [
    ("Abstract class", "Cannot create instances — for inheritance only"),
    ("Concrete class", "Can create and save instances"),
    ("Pattern inheritance", "Auto parent from namespace (Work-Cover-LoanApp → Work-Cover-)"),
    ("Directed inheritance", "Manual parent pick from another branch"),
    ("Class Group", "Groups case types in one DB table (work pool)"),
    ("Work Pool", "Same as Class Group — which cases an operator sees"),
])}
{qa("Pattern vs Directed inheritance?", "<strong>Pattern</strong> = automatic from class name hierarchy. <strong>Directed</strong> = you explicitly pick a parent class outside your namespace to reuse rules.")}
{qa("Abstract vs Concrete?", "Abstract = blueprint only, no instances. Concrete = real objects saved to DB.")}
{qa("What is a Class Group?", "Groups related case types under one table (pc_work). Set in Application rule and Access Group.")}
{qa("Why not duplicate rules across classes?", "Use inheritance! Guardrail violation. Extend parent class instead.")}
{qa("What is @baseclass?", "Root of entire class hierarchy. Everything inherits from here.")}
"""
    return chapter_wrap(2, "Class Hierarchy & Inheritance — Complete Guide", None, body, 1)


def ch03_rules(d):
    body = f"""
{simple("When Pega needs a rule, it runs <strong>Rule Resolution</strong> — a 10-step search to find the ONE correct rule version. Interviewers LOVE asking this. Learn the flowchart below like a love song.")}
{d("01-rule-resolution", "Rule Resolution — Full 10-Step Flowchart with Labels")}
{section("10 Steps Explained Simply", bullets([
    "<strong>Step 1:</strong> Start with the class of the calling rule",
    "<strong>Step 2:</strong> Find rules matching type + name (e.g., Data Transform 'MapCustomer')",
    "<strong>Step 3:</strong> Filter by application's ruleset stack",
    "<strong>Step 4:</strong> Remove 'Not Available' rules",
    "<strong>Step 5:</strong> Remove 'Blocked' rules",
    "<strong>Step 6:</strong> Pick most specific class (nearest match wins)",
    "<strong>Step 7:</strong> Pick highest ruleset version",
    "<strong>Step 8:</strong> Apply circumstance (date or property-based variant)",
    "<strong>Step 9:</strong> Check availability one more time",
    "<strong>Step 10:</strong> Return winner and cache in FUA",
]))}
{section("Rule Availability States", """
<table><tr><th>State</th><th>Meaning</th></tr>
<tr><td>Available</td><td>Active — used in resolution</td></tr>
<tr><td>Not Available</td><td>Saved but ignored</td></tr>
<tr><td>Blocked</td><td>Forcefully excluded</td></tr>
<tr><td>Final</td><td>Cannot be overridden by child</td></tr>
<tr><td>Withdrawn</td><td>Deprecated forever</td></tr></table>""")}
{flirt_ex("Rule Resolution is like finding the right person in a crowded room — class is the venue, ruleset is the guest list, circumstance is 'only if they're wearing blue'. Pega always finds your match.")}
{cheat("Rule Resolution", [
    ("Circumstance (date)", "Rule variant effective between two dates"),
    ("Circumstance (template)", "Rule variant when property = value"),
    ("FUA", "Cached compiled rule — fast on 2nd call"),
    ("Duplicate rule", "Two rules same specificity — fix this!"),
    ("Ruleset", "Versioned container: MyApp:01-01-01"),
])}
{qa("Explain Rule Resolution in interview?", "Walk through 10 steps. Mention class specificity, ruleset version, circumstance, FUA cache. Draw the flowchart if whiteboard available.")}
{qa("What is circumstance?", "A variant of a rule for specific date or property condition. E.g., different tax rule for US vs UK.")}
{qa("What is FUA?", "Full Rule Assembly — compiled cached rule. First call slow, then cached until rule changes.")}
{qa("What happens with duplicate rules?", "Warning in logs. Should be fixed — indicates design problem.")}
{qa("List 5 rule types in Process category.", "Case Type, Flow, Flow Action, Stage, Process.")}
{qa("Blocked vs Not Available?", "Not Available = saved but inactive. Blocked = explicitly excluded from resolution.")}
"""
    return chapter_wrap(3, "Rules & Rule Resolution — Complete Guide", None, body, 2)


def ch04_rulesets(d):
    body = f"""
{simple("A <strong>ruleset</strong> is a versioned bag of rules — like <code>MyBankApp:01-02-03</code>. Your Application rule stacks rulesets in order. Higher version wins when two rules match.")}
{d("13-application-stack", "Application Stack — How Rulesets Layer")}
{cheat("Rulesets & Application", [
    ("Version format", "MM-mm-nn (Major-minor-patch)"),
    ("Application rule", "Lists all rulesets in resolution order"),
    ("Built-on application", "Inherit from parent app (e.g., PegaRULES)"),
    ("Branch", "Parallel dev stream — like Git branch"),
    ("Merge", "Combine branch changes to target ruleset"),
    ("Ruleset versioning", "01-01-01 → 01-01-02 for patches"),
])}
{qa("What is a ruleset version format?", "MM-mm-nn. Example: MyApp:01-02-03.")}
{qa("What is built-on application?", "Your app inherits rulesets from parent. Platform → Framework → Your App.")}
{qa("Why use branches?", "Parallel development without conflicts. Merge when feature is ready.")}
{qa("What is an Application rule?", "Defines app name, ruleset stack, class structure, access.")}
{qa("How to version rules?", "Lock ruleset, create new version (01-01-02), save changes to new version.")}
"""
    return chapter_wrap(4, "Application Stack & Rulesets — Complete Guide", None, body, 3)


def ch05_cases(d):
    body = f"""
{simple("A <strong>Case</strong> is one business story — one loan application, one insurance claim. It has data, stages, tasks, and ends as Completed or Cancelled. This is the HEART of Pega.")}
{d("15-case-type-anatomy", "Case Type — Full Anatomy Mind Map")}
{d("02-case-lifecycle", "Case Lifecycle — New → Open → Resolved")}
{d("25-case-creation", "Sequence: How a Case Gets Created")}
{flirt_ex("A loan case is a love story 💕 — <strong>Stage 1:</strong> First application (nervous excitement). <strong>Stage 2:</strong> Underwriting (getting serious). <strong>Stage 3:</strong> Approval (commitment!). <strong>Resolved:</strong> Happily ever after… or cancelled if it wasn't meant to be.")}
{cheat("Case Management", [
    ("Case Type", "Blueprint for a business process"),
    ("Stage", "Big lifecycle phase (Application, Review, Done)"),
    ("Process", "Workflow inside a stage"),
    ("pyStatusWork", "Current case status property"),
    ("Child case", "Separate linked case with own lifecycle"),
    ("Cover case", "Parent holding multiple sub-cases"),
    ("Spin-off", "Create child case mid-flow"),
    ("Wait shape", "Pause until timer/event/child resolves"),
])}
{qa("What is a Case Type?", "Blueprint defining data model, stages, processes, UI, security for one business process.")}
{qa("Parent vs Child vs Cover case?", "Child = linked separate case. Cover = container parent. Spin-off = create child from parent flow.")}
{qa("Case statuses?", "New, Open, Pending-..., Resolved-Completed, Resolved-Cancelled.")}
{qa("Case-wide vs Stage actions?", "Case-wide = available everywhere (Transfer). Stage = only in that stage (Submit).")}
{qa("What is pyDefault flow?", "Primary flow run when case enters a process/stage.")}
{qa("How is Case ID generated?", "Via Case ID rule — can include prefix, date, sequence.")}
"""
    return chapter_wrap(5, "Case Management & Lifecycle — Complete Guide", None, body, 4)


def ch06_flows(d):
    body = f"""
{simple("A <strong>Flow</strong> is the backstage automation — shapes connected together. Users don't see flows directly; they see <strong>Flow Actions</strong> (buttons like Submit, Approve).")}
{d("03-flow-shapes", "All Flow Shapes — Assignment, Decision, Utility, Wait, Split-Join")}
{d("18-save-case-sequence", "Sequence: User Submits → Data Saved → Flow Advances")}
{cheat("Flows & Flow Actions", [
    ("Assignment shape", "Creates human task"),
    ("Utility shape", "Automation — no user task"),
    ("Decision shape", "Branches on When rule"),
    ("Subprocess", "Calls another flow"),
    ("Wait", "Pauses for timer/event"),
    ("Split-Join", "Parallel branches then merge"),
    ("Split-ForEach", "Loop over page list items"),
    ("Flow Action", "User button with UI screen"),
    ("Local FA", "Stays on same screen"),
    ("Connector FA", "Navigates to new screen"),
])}
{qa("Flow vs Flow Action?", "Flow = backend process. Flow Action = user-facing button with screen.")}
{qa("All flow shapes?", "Assignment, Decision, Utility, Subprocess, Wait, Split-Join, Split-ForEach, Notify.")}
{qa("What does Utility shape do?", "Runs DT/Activity automatically without creating assignment.")}
{qa("Split-Join use case?", "Send 3 approvals in parallel, wait for all, then continue.")}
{qa("Split-ForEach use case?", "Process each item in an order list separately.")}
{qa("What is pyFlowName?", "Property holding current flow name on assignment.")}
"""
    return chapter_wrap(6, "Flows, Processes & Flow Actions — Complete Guide", None, body, 5)


def ch07_assignments(d):
    body = f"""
{simple("An <strong>Assignment</strong> is a task waiting for someone — 'Review this loan', 'Approve claim'. It lands in a worklist, workbasket, or work queue.")}
{d("11-assignment-routing", "Assignment Routing — How Tasks Get to People")}
{flirt_ex("Worklist is your personal DMs. Workbasket is the group chat everyone can pick from. Work Queue is 'slide into specific someone's inbox.' Pega routes like a thoughtful matchmaker.")}
{cheat("Assignments", [
    ("Worklist", "Personal queue for one operator"),
    ("Workbasket", "Shared team pool"),
    ("Work Queue", "Named queue — dynamic routing"),
    ("pxUrgencyAssign", "Assignment urgency property"),
    ("Urgency", "10-100, higher = more priority"),
    ("Router activity", "Custom routing logic"),
])}
{qa("Worklist vs Workbasket?", "Worklist = personal. Workbasket = team shared pool.")}
{qa("What is urgency?", "Numeric priority 10-100. Increases as SLA deadline nears.")}
{qa("How to route to specific team?", "Configure WorkBasket or Work Queue on assignment shape.")}
{qa("What is pxRouteTo?", "Property for routing destination.")}
"""
    return chapter_wrap(7, "Assignments & Routing — Complete Guide", None, body, 6)


def ch08_clipboard(d):
    body = f"""
{simple("The <strong>clipboard</strong> is Pega's short-term memory during a request. It holds pages of data — case info, user info, parameters. Gone when request ends (unless saved to DB).")}
{d("12-clipboard-structure", "Clipboard — pyWorkPage, pxThread, pxRequestor")}
{d("26-property-types", "All Property Types — Text, Page, Page List, Page Group")}
{flirt_ex("pyWorkPage is the case's diary — everything about THIS loan. pxRequestor is YOUR ID card. pxThread is your to-do list for this session. Know these three and you're already impressive.")}
{cheat("Clipboard & Properties", [
    ("pyWorkPage", "Current case data page"),
    ("pxRequestor", "Logged-in user info"),
    ("pxThread", "Session thread with open assignments"),
    ("param", "Parameter page for passing args"),
    ("Page List", "Ordered list — .Items(1), .Items(2)"),
    ("Page Group", "Keyed map — .Docs('ID1')"),
    ("Embedded page", "Stored inside parent"),
    ("Linked page", "Reference via pxLinkedRefTo"),
    ("pzInsKey", "Unique instance key"),
])}
{qa("What is pyWorkPage?", "Primary page with all current case data.")}
{qa("Page List vs Page Group?", "List = integer index, ordered. Group = string key, unordered.")}
{qa("pxRequestor vs pxThread?", "Requestor = user session. Thread = open work in session.")}
{qa("What is pzInsKey?", "Unique DB key for any instance. Use with Obj-Open-By-Handle.")}
{qa("Embedded vs Linked page?", "Embedded = inside parent. Linked = separate page reference.")}
"""
    return chapter_wrap(8, "Clipboard & Data Model — Complete Guide", None, body, 7)


def ch09_datapages(d):
    body = f"""
{simple("A <strong>Data Page</strong> is your data butler. Say <code>D_Customer[ID:123]</code> and Pega fetches, caches, and delivers. No manual DB code needed.")}
{d("04-data-page-load", "Sequence: Data Page Load with Cache Check")}
{flirt_ex("Calling a Data Page 50 times without cache is like texting 'hey' 50 times — exhausting. Data Pages cache smartly so Pega only fetches when needed. That's maturity.")}
{cheat("Data Pages", [
    ("Read-only DP", "Lookup/reference data"),
    ("Editable DP", "Can modify + Save Plan"),
    ("List DP", "Returns multiple rows"),
    ("Singleton DP", "Returns one object"),
    ("Reload per interaction", "Fresh every request"),
    ("Reload once per requestor", "Cache per user session"),
    ("Node scope", "Shared across cluster node"),
    ("Parameters", "D_Page[param:value] affects cache key"),
    ("Sources", "Report Def, Activity, REST, Lookup, DT"),
])}
{qa("Why use Data Page over Activity?", "Declarative, cacheable, guardrail-friendly, reusable everywhere.")}
{qa("Data Page load modes?", "Per interaction, per requestor, time-based, access group, node.")}
{qa("What is Save Plan?", "How editable Data Page persists changes back to DB.")}
{qa("Data Page vs Report Definition?", "Report Def = SQL query. Data Page = smart layer with cache + parameters.")}
{qa("How to pass parameters?", "Define on DP rule. Call as D_Customer[CustomerID:123].")}
"""
    return chapter_wrap(9, "Data Pages — Complete Guide", None, body, 8)


def ch10_dt(d):
    body = f"""
{simple("A <strong>Data Transform</strong> copies and maps data — set this field, calculate that total, add row to list. Always prefer DT over Activity for mapping.")}
{d("24-data-transform-flow", "Data Transform — Step-by-Step Flow")}
{cheat("Data Transform Actions", [
    ("Set", "Assign value to property"),
    ("Update Page", "Run DT on embedded page"),
    ("Append and Map to", "Add to page list"),
    ("Remove", "Delete list entry"),
    ("When / Otherwise", "Conditional steps"),
    ("For Each Page In", "Loop page list"),
    ("Apply Data Transform", "Call another DT"),
    ("Exit", "Stop DT execution"),
])}
{qa("DT vs Activity — when which?", "DT for mapping/simple logic ALWAYS first. Activity only for complex loops, legacy, integration orchestration.")}
{qa("How to call DT from flow?", "Configure on flow shape, flow action, or call from another DT.")}
{qa("What is Auto-populate?", "Property auto-runs DT when referenced.")}
{qa("Can DT call REST?", "Not directly — use Data Page with REST source, then map in DT.")}
"""
    return chapter_wrap(10, "Data Transforms — Complete Guide", None, body, 9)


def ch11_activities(d):
    body = f"""
{simple("Activities are <strong>old-school procedural code</strong> in Pega. Still needed for legacy and edge cases, but interviewers want to hear you prefer Data Transforms.")}
{cheat("Activity Methods", [
    ("Property-Set", "Set property value"),
    ("Call", "Invoke sub-activity"),
    ("Apply-DataTransform", "Run DT"),
    ("Obj-Open / Obj-Save", "Read/write DB"),
    ("Page-New / Page-Copy", "Clipboard pages"),
    ("RDB-List", "SQL query — avoid in loops!"),
    ("Connect-REST", "Call REST connector"),
    ("Queue-For-Agent", "Defer to background"),
    ("Branch", "Jump to labeled step"),
])}
{qa("Why are activities phased out?", "Procedural, hard to maintain, bypass guardrails, allow infinite loops.")}
{qa("Activity security?", "Allow list + Privilege on activity rule.")}
{qa("Call vs Branch?", "Call = sub-activity. Branch = jump within same activity.")}
{qa("When MUST you use activity?", "Legacy maintenance, complex iteration, Queue-For-Agent, some integrations.")}
"""
    return chapter_wrap(11, "Activities — Complete Guide", None, body, 10)


def ch12_decisions(d):
    body = f"""
{simple("Decision rules answer questions — yes/no, lookup tables, scoring. Pick the right type and interviewers know you're senior material.")}
{d("16-decision-rules-map", "Which Decision Rule to Use — Selection Flowchart")}
{cheat("Decision Rules", [
    ("When", "Single true/false condition"),
    ("Decision Table", "Grid of conditions → results"),
    ("Decision Tree", "Hierarchical if-else"),
    ("MapValue", "One input → one output lookup"),
    ("Scorecard", "Weighted scoring model"),
    ("Strategy", "CDH / Next-Best-Action"),
])}
{qa("When vs Decision Table?", "When = one condition. Table = many combinations in grid.")}
{qa("MapValue example?", "Map status code 'A' → 'Approved', 'R' → 'Rejected'.")}
{qa("What is Scorecard?", "Weighted conditions → total score → rating (e.g., credit risk).")}
{qa("What is Decision Strategy?", "CDH component combining propositions, filters, AI for NBA.")}
"""
    return chapter_wrap(12, "Decision Rules — Complete Guide", None, body, 11)


def ch13_declares(d):
    body = f"""
{simple("Declare rules compute things <strong>automatically</strong> — change FirstName, FullName updates itself. No manual code. That's forward chaining.")}
{d("10-declare-expression", "Declare Expression — Forward Chaining Flow")}
{cheat("Declare Rules", [
    ("Declare Expression", "Auto-compute property from sources"),
    ("Declare Constraint", "Validation on property change"),
    ("Declare OnChange", "Trigger DT/Activity when property changes"),
    ("Declare Trigger", "Fire on save of Data- instance"),
    ("Declare Index", "Maintain search index on save"),
])}
{qa("Declare Expression example?", ".FullName = .FirstName + ' ' + .LastName — auto updates.")}
{qa("OnChange vs Trigger?", "OnChange = clipboard property change. Trigger = on DB commit of Data class.")}
{qa("What is forward chaining?", "Pega tracks dependencies and recalculates automatically.")}
"""
    return chapter_wrap(13, "Declare Rules — Complete Guide", None, body, 12)


def ch14_validation(d):
    body = f"""
{simple("Validation keeps bad data out — like standards in a relationship. Three types work together: screen check, server check, and always-on constraints.")}
{d("19-validation-flow", "Validation Flow — Edit Validate → Validate → Constraint")}
{qa("Validate vs Edit Validate?", "Edit Validate = client+server on field. Validate = server on commit.")}
{qa("Declare Constraint?", "Always enforced when property set — declarative validation.")}
{qa("Where to use Validate rule?", "On flow submit, activity commit, data transform.")}
"""
    return chapter_wrap(14, "Validation Rules — Complete Guide", None, body, 13)


def ch15_ui(d):
    body = f"""
{simple("UI is what users see. <strong>Traditional</strong> = Section + Harness. <strong>Constellation</strong> = modern React Views. Know both — interviews ask.")}
{d("17-constellation-architecture", "Constellation — Center-Out UI Architecture")}
{cheat("UI Layer", [
    ("Section", "UI building block (traditional)"),
    ("Harness", "Full screen from sections"),
    ("View", "Constellation UI unit (replaces Section)"),
    ("Portal", "App shell / navigation"),
    ("Dynamic Layout", "Responsive flex layout — USE THIS"),
    ("Freeform Layout", "Legacy absolute — AVOID"),
    ("Cosmos", "Design system for Constellation"),
    ("DX API", "API layer for Constellation frontends"),
])}
{qa("Section vs Harness?", "Section = fragment. Harness = complete screen.")}
{qa("Why Constellation?", "React-based, responsive, mobile-ready, faster dev, omnichannel.")}
{qa("Constellation vs Traditional?", "Views replace Sections. Theme replaces Skin. Full pages replace Harnesses.")}
"""
    return chapter_wrap(15, "UI & Constellation — Complete Guide", None, body, 14)


def ch16_sla(d):
    body = f"""
{simple("SLA = time promises. <strong>Goal</strong> = please finish by. <strong>Deadline</strong> = must finish by. <strong>Passed Deadline</strong> = you're late — escalate!")}
{d("08-sla-timeline", "SLA Timeline — Goal → Deadline → Passed Deadline")}
{qa("Assignment SLA vs Case SLA?", "Assignment = per task. Case/Stage SLA = overall duration.")}
{qa("What is urgency?", "Priority number increasing as SLA approaches.")}
{qa("SLA agent?", "Pega-ProCom:ServiceLevelEvents — processes SLA events.")}
{qa("What happens at deadline?", "Escalation actions: notify, reassign, update priority.")}
"""
    return chapter_wrap(16, "SLAs & Urgency — Complete Guide", None, body, 15)


def ch17_integration(d):
    body = f"""
{simple("Integration = Pega talking to other systems. <strong>Connect</strong> = Pega calls out. <strong>Service</strong> = others call Pega.")}
{d("05-rest-integration", "Sequence: REST Integration via Connect-REST")}
{d("28-integration-overview", "Integration Overview — Connect vs Service")}
{cheat("Integration", [
    ("Connect-REST", "Outbound REST call"),
    ("Service-REST", "Inbound REST endpoint"),
    ("Connect-SOAP", "Outbound SOAP"),
    ("Connect-Kafka", "Event streaming out"),
    ("Auth Profile", "Credentials for outbound calls"),
    ("Service Package", "Groups inbound services"),
    ("Data Type", "Pega-managed CRUD + auto REST API"),
    ("Error handling", "Map HTTP codes to error pages"),
])}
{qa("Connect vs Service?", "Connect = outbound. Service = inbound.")}
{qa("How to handle REST errors?", "Error handlers on connector, fallback Data Page, log integration.")}
{qa("Authentication options?", "Basic, OAuth 2.0, JWT, API Key, Custom.")}
{qa("What is Data Type?", "Managed Data- class with UI, storage, REST API auto-generated.")}
"""
    return chapter_wrap(17, "Integration & Data Types — Complete Guide", None, body, 16)


def ch18_security(d):
    body = f"""
{simple("Security chain: <strong>Operator → Access Group → Roles → Privileges → Access When</strong>. Memorize this line. Say it in interview. Watch them nod.")}
{d("06-security-model", "Security Model — Full Chain Diagram")}
{d("27-access-check-flow", "Access Check Flow — Privilege + Access When")}
{cheat("Security", [
    ("Access Group", "App + Portal + Roles + Work Pool"),
    ("Role", "Bundle of privileges (job function)"),
    ("Privilege", "Single permission (atomic)"),
    ("Access When", "Condition-based access (ABAC)"),
    ("ABAC", "Access based on property values"),
    ("Property security", "Read/write restrictions per property"),
])}
{qa("Role vs Privilege?", "Privilege = one permission. Role = collection of privileges.")}
{qa("What is ABAC?", "Attribute-Based Access Control — e.g., only see cases in your region.")}
{qa("How to restrict flow action?", "Access When rule on flow action + privilege.")}
"""
    return chapter_wrap(18, "Security Model — Complete Guide", None, body, 17)


def ch19_agents(d):
    body = f"""
{simple("Agents and Job Schedulers run work in the background — SLAs, bulk processing, emails. Job Scheduler is preferred for new development.")}
{d("14-agent-processing", "Sequence: Queue-For-Agent Background Processing")}
{qa("Agent vs Job Scheduler?", "Agent = queue polling (legacy). Job Scheduler = scheduled tasks (modern).")}
{qa("Queue-For-Agent?", "Defer work to agent queue for async processing.")}
{qa("How to troubleshoot stopped agent?", "Admin Studio → Agents → check enabled, logs, queue.")}
"""
    return chapter_wrap(19, "Agents & Job Schedulers — Complete Guide", None, body, 18)


def ch20_reporting(d):
    body = f"""
{simple("Report Definitions query the database — for dashboards, manager reports, and Data Page sources. Always prefer over raw SQL in activities.")}
{qa("Report Definition vs Summary View?", "Summary View is legacy. Always say Report Definition.")}
{qa("How to join classes in report?", "Create Association rule, use in report join tab.")}
{qa("How to optimize slow report?", "Indexes, limit columns, avoid functions on indexed WHERE columns.")}
"""
    return chapter_wrap(20, "Reporting — Complete Guide", None, body, 19)


def ch21_testing(d):
    body = f"""
{simple("Test your rules! Unit tests for individual rules. Scenario tests for full case lifecycle. Interviewers love hearing you write tests.")}
{d("21-testing-strategy", "Testing Strategy — Unit vs Scenario vs CI")}
{qa("How to unit test a DT?", "Right-click → Create Test Case → input/output pages → assert.")}
{qa("Scenario test?", "End-to-end UI automation of case lifecycle.")}
{qa("Test Application?", "Isolated app stack for running tests safely.")}
"""
    return chapter_wrap(21, "Testing Strategy — Complete Guide", None, body, 20)


def ch22_performance(d):
    body = f"""
{simple("Slow case? Open PAL first. Then Tracer. Then fix. This is your debugging love language.")}
{d("23-performance-debug", "Performance Debugging — Step-by-Step Flowchart")}
{cheat("Performance & Guardrails", [
    ("PAL", "Performance Analyzer — DB ops, clipboard size"),
    ("Tracer", "Step-by-step rule execution trace"),
    ("N+1 problem", "Loop calling DB per row — use batch DP"),
    ("Max flow actions", "5 per assignment (guardrail)"),
    ("Prefer DT over Activity", "Always say this in interview"),
    ("Clipboard limit", "~2MB per request"),
    ("DB ops warning", "PAL alerts if >50 operations"),
])}
{qa("How to debug slow case?", "PAL → Tracer → DB Trace → check DP load modes → find looping activities.")}
{qa("What is N+1?", "100 rows × 1 DB call each = 101 calls. Fix with batch Data Page.")}
{qa("Top 5 guardrails?", "DT over Activity, max 5 FAs, use Data Pages, no loop activities, limit properties.")}
"""
    return chapter_wrap(22, "Performance & Guardrails — Complete Guide", None, body, 21)


def ch23_devops(d):
    body = f"""
{simple("Moving code Dev → QA → Prod: branches, merge, RAP package, Deployment Manager pipeline. Like moving in together — needs planning.")}
{d("09-deployment-pipeline", "DevOps Pipeline — Branch → RAP → QA → Prod")}
{cheat("DevOps", [
    ("RAP", "Ruleset Archive Package — export zip"),
    ("Product rule", "Defines what goes in RAP"),
    ("Branch", "Parallel development stream"),
    ("Merge", "Combine branch to target"),
    ("Skim", "Remove unreferenced rules before export"),
    ("Deployment Manager", "CI/CD for Pega"),
    ("Git Repository", "Version control for rules"),
])}
{qa("What is RAP?", "Export package of rules for deployment to another environment.")}
{qa("Branch vs ruleset version?", "Branch = parallel stream. Version = sequential 01-01-01 → 01-01-02.")}
{qa("What is skim?", "Removes rules not referenced by application — smaller RAP.")}
"""
    return chapter_wrap(23, "DevOps & Deployment — Complete Guide", None, body, 22)


def ch24_email(d):
    body = f"""
{simple("Send emails from flows using Correspondence rules. Receive emails via Service Email to create/update cases.")}
{qa("How to send email from flow?", "Send Email smart shape + Correspondence rule + Email Account.")}
{qa("Inbound email?", "Service Email rule creates or updates cases from incoming email.")}
{qa("Document generation?", "HTML/PDF templates via Correspondence, attach to case.")}
"""
    return chapter_wrap(24, "Email, Documents & Correspondence — Complete Guide", None, body, 23)


def ch25_advanced(d):
    body = f"""
{simple("Advanced topics for SSA interviews — CDH for marketing, RPA for desktop apps, Data Flows for big data, GenAI for smart assistance.")}
{cheat("Advanced Topics", [
    ("CDH", "Customer Decision Hub — Next-Best-Action"),
    ("RPA", "Robot Studio — desktop automation"),
    ("Data Flow", "Batch/stream processing pipeline"),
    ("Prediction Studio", "ML model management"),
    ("GenAI / Socrates", "AI assistant in App Studio"),
    ("Proposition", "Offer/action in CDH strategy"),
    ("Adaptive Model", "Self-learning ML in Pega"),
])}
{qa("What is Next-Best-Action?", "AI-driven decision to show best offer/action to customer.")}
{qa("RPA in Pega?", "Automate legacy desktop apps via robots in case flows.")}
{qa("Data Flow use case?", "Process millions of records from Kafka or DB in batch/stream.")}
"""
    return chapter_wrap(25, "Advanced — CDH, RPA, AI — Complete Guide", None, body, 24)


def ch26_controls(d):
    body = f"""
{simple("Field Values power dropdowns. Feature Toggles switch features on/off without deployment. Localization makes labels multi-language.")}
{d("22-feature-toggle", "Feature Toggle — Runtime Switching")}
{qa("What is Field Value?", "Key-value pairs for dropdown options.")}
{qa("Feature Toggle?", "Runtime on/off for features without new deployment.")}
{qa("Localization?", "Locale-specific labels via Field Value rules.")}
"""
    return chapter_wrap(26, "Controls, Field Values & Localization — Complete Guide", None, body, 0)


def ch27_persistence(d):
    body = f"""
{simple("Obj-Open reads from DB. Obj-Save writes. pzInsKey is the unique ID. These are how Pega persists data.")}
{d("20-object-persistence", "Object Layer — Obj-Open / Obj-Save / Obj-Delete")}
{qa("Obj-Open vs Obj-Save?", "Open = read from DB. Save = write to DB.")}
{qa("What is pzInsKey?", "Unique instance identifier — primary key.")}
{qa("pxCommitDateTime?", "Timestamp of last DB commit.")}
"""
    return chapter_wrap(27, "Object Layer & Persistence — Complete Guide", None, body, 1)


def master_cheat_sheet():
    return """
<div class="chapter" id="master-cheat">
<h2>🏆 Master Interview Cheat Sheet — Print This Page</h2>
<div class="flirt-box">You made it through every chapter. This page is your weapon. Read it the morning of your interview. Then go be unforgettable.</div>
<table>
<tr><th>Topic</th><th>One-Line Answer</th></tr>
<tr><td>Rule Resolution</td><td>10 steps: class → name → ruleset → availability → specificity → circumstance → cache FUA</td></tr>
<tr><td>Data Page</td><td>Smart cached data fetcher — prefer over activity</td></tr>
<tr><td>Data Transform</td><td>Map/copy data — always prefer over activity</td></tr>
<tr><td>Flow vs Flow Action</td><td>Flow = backend. Flow Action = user button</td></tr>
<tr><td>Worklist vs Basket</td><td>Personal vs team shared queue</td></tr>
<tr><td>Page List vs Group</td><td>Integer index vs string key</td></tr>
<tr><td>When vs Dec Table</td><td>One condition vs grid of conditions</td></tr>
<tr><td>Declare Expression</td><td>Auto-computed property (forward chaining)</td></tr>
<tr><td>Connect vs Service</td><td>Outbound vs inbound integration</td></tr>
<tr><td>Access Group chain</td><td>Operator → AG → Role → Privilege → Access When</td></tr>
<tr><td>SLA intervals</td><td>Goal → Deadline → Passed Deadline</td></tr>
<tr><td>Constellation</td><td>Modern React UI — Views replace Sections</td></tr>
<tr><td>PAL</td><td>First tool when case is slow</td></tr>
<tr><td>RAP</td><td>Rule export package for deployment</td></tr>
<tr><td>Guardrail #1</td><td>Prefer DT over Activity</td></tr>
<tr><td>pyWorkPage</td><td>Current case data</td></tr>
<tr><td>pxRequestor</td><td>Logged-in user context</td></tr>
<tr><td>pzInsKey</td><td>Unique instance key</td></tr>
<tr><td>N+1 problem</td><td>Loop DB calls — fix with batch DP</td></tr>
<tr><td>Branch</td><td>Parallel dev stream — merge when done</td></tr>
</table>
</div>"""
