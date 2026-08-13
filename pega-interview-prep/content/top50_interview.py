"""Top 50 most-asked Pega interview questions with easy-language answers."""


def build_top50_chapter() -> str:
    return """
<div class="chapter" id="ch-top50">
<h2>Chapter 28: Top 50 Most-Asked Interview Questions (Easy Answers)</h2>
<div class="flirt-box">These 50 show up again and again. Read them twice. Smile once. Ace every time.</div>

<div class="qa-block"><div class="question">1. What is Pega in simple words?</div>
<div class="answer"><strong>Easy answer:</strong> Pega is a platform where you build business apps using <em>rules</em> instead of writing lots of Java code. You design cases (like loan applications), workflows, screens, and integrations — and Pega runs it all.</div></div>

<div class="qa-block"><div class="question">2. What is a Case / Work Object?</div>
<div class="answer"><strong>Easy answer:</strong> A <strong>case</strong> is one business request — one loan, one claim, one ticket. It has data, stages, tasks, and a final outcome (completed or cancelled). "Work object" is the older technical name for the same thing.</div></div>

<div class="qa-block"><div class="question">3. What is Rule Resolution?</div>
<div class="answer"><strong>Easy answer:</strong> When Pega needs a rule, it doesn't guess — it follows steps to find the <strong>best matching rule</strong> based on class, name, ruleset version, and circumstance. Like finding the right key for the right lock.</div></div>

<div class="qa-block"><div class="question">4. Explain the 10 steps of Rule Resolution briefly.</div>
<div class="answer">Start with class → match rule type and name → filter by application rulesets → remove unavailable/blocked → pick most specific class → pick highest ruleset version → apply circumstance → check availability → return one winner → cache it (FUA).</div></div>

<div class="qa-block"><div class="question">5. What is a Ruleset?</div>
<div class="answer"><strong>Easy answer:</strong> A <strong>ruleset</strong> is a versioned folder of related rules — like <code>MyApp:01-01-01</code>. Your application stacks multiple rulesets in order.</div></div>

<div class="qa-block"><div class="question">6. What is difference between Pattern and Directed inheritance?</div>
<div class="answer"><strong>Easy answer:</strong> <strong>Pattern</strong> = automatic parent from class name hierarchy. <strong>Directed</strong> = you manually pick a parent class from another branch to reuse rules without copying.</div></div>

<div class="qa-block"><div class="question">7. What is a Data Page and why use it?</div>
<div class="answer"><strong>Easy answer:</strong> A Data Page is a <strong>smart data fetcher</strong>. You call it like <code>D_Customer</code> and Pega loads data from DB, REST, or report — with caching so you don't hit the database 100 times.</div></div>

<div class="qa-block"><div class="question">8. Data Transform vs Activity — which to use?</div>
<div class="answer"><strong>Easy answer:</strong> Use <strong>Data Transform</strong> for copying/mapping data (99% of cases). Use <strong>Activity</strong> only for complex loops, legacy code, or special integration steps. Interviewers want to hear "DT first."</div></div>

<div class="qa-block"><div class="question">9. What is the clipboard?</div>
<div class="answer"><strong>Easy answer:</strong> The clipboard is Pega's <strong>working memory</strong> during a request. It holds pages like <code>pyWorkPage</code> (case data), <code>pxRequestor</code> (logged-in user), and <code>pxThread</code> (open tasks).</div></div>

<div class="qa-block"><div class="question">10. What is pyWorkPage?</div>
<div class="answer"><strong>Easy answer:</strong> The main page holding <strong>current case data</strong> — customer name, status, amounts, everything about that case.</div></div>

<div class="qa-block"><div class="question">11. Page List vs Page Group?</div>
<div class="answer"><strong>Easy answer:</strong> <strong>Page List</strong> = ordered list (1, 2, 3…) like shopping cart items. <strong>Page Group</strong> = named map ("home", "office") like labeled folders.</div></div>

<div class="qa-block"><div class="question">12. What is a Flow vs Flow Action?</div>
<div class="answer"><strong>Easy answer:</strong> <strong>Flow</strong> = behind-the-scenes process (automation). <strong>Flow Action</strong> = button user clicks ("Submit", "Approve") with a screen attached.</div></div>

<div class="qa-block"><div class="question">13. What are Stages in a Case Type?</div>
<div class="answer"><strong>Easy answer:</strong> Stages are the <strong>big chapters</strong> of a case — e.g., Application → Review → Approval → Done. Each stage has processes and tasks inside it.</div></div>

<div class="qa-block"><div class="question">14. What is an Assignment?</div>
<div class="answer"><strong>Easy answer:</strong> A <strong>task waiting for someone</strong> (or a system) to act — "Review this loan", "Approve claim". Shows up in worklist or workbasket.</div></div>

<div class="qa-block"><div class="question">15. Worklist vs Workbasket?</div>
<div class="answer"><strong>Easy answer:</strong> <strong>Worklist</strong> = your personal to-do list. <strong>Workbasket</strong> = team's shared tray — anyone in the team can pick tasks.</div></div>

<div class="qa-block"><div class="question">16. What is SLA?</div>
<div class="answer"><strong>Easy answer:</strong> SLA = <strong>time promise</strong>. Goal = "please finish by", Deadline = "must finish by", Passed Deadline = "you're late — escalate!"</div></div>

<div class="qa-block"><div class="question">17. What is Urgency?</div>
<div class="answer"><strong>Easy answer:</strong> A number (10–100) that says <strong>how important</strong> a task is. Goes up as SLA deadline gets closer. Higher urgency tasks appear on top.</div></div>

<div class="qa-block"><div class="question">18. What is a When rule?</div>
<div class="answer"><strong>Easy answer:</strong> A simple <strong>yes/no question</strong> — "Is amount &gt; 10000?" Returns true or false. Used in flows, validations, and data transforms.</div></div>

<div class="qa-block"><div class="question">19. Decision Table vs Decision Tree?</div>
<div class="answer"><strong>Easy answer:</strong> <strong>Table</strong> = spreadsheet of conditions → results (great for many combinations). <strong>Tree</strong> = flowchart of if-else (great for step-by-step logic).</div></div>

<div class="qa-block"><div class="question">20. What is Declare Expression?</div>
<div class="answer"><strong>Easy answer:</strong> Auto-calculated field. You change First Name or Last Name → Full Name updates automatically. No manual code needed.</div></div>

<div class="qa-block"><div class="question">21. What is Connect-REST?</div>
<div class="answer"><strong>Easy answer:</strong> Pega <strong>calling an external API</strong> (outbound). You configure URL, method, request/response mapping.</div></div>

<div class="qa-block"><div class="question">22. What is Service-REST?</div>
<div class="answer"><strong>Easy answer:</strong> External system <strong>calling Pega</strong> (inbound). Pega exposes a REST URL that others can hit.</div></div>

<div class="qa-block"><div class="question">23. What is an Access Group?</div>
<div class="answer"><strong>Easy answer:</strong> Defines <strong>what a user can access</strong> — which app, portal, roles, and case types. Like a job profile package.</div></div>

<div class="qa-block"><div class="question">24. Role vs Privilege?</div>
<div class="answer"><strong>Easy answer:</strong> <strong>Privilege</strong> = one permission ("can create case"). <strong>Role</strong> = bundle of privileges ("Loan Officer" role has many privileges).</div></div>

<div class="qa-block"><div class="question">25. What is Constellation?</div>
<div class="answer"><strong>Easy answer:</strong> Pega's <strong>modern UI</strong> built with React. Faster, mobile-friendly, replaces old Section/Harness approach. Future of Pega UI.</div></div>

<div class="qa-block"><div class="question">26. Section vs Harness?</div>
<div class="answer"><strong>Easy answer:</strong> <strong>Section</strong> = one UI block (form fields). <strong>Harness</strong> = full screen made by combining sections (like assembling LEGO pieces into a page).</div></div>

<div class="qa-block"><div class="question">27. What is a Report Definition?</div>
<div class="answer"><strong>Easy answer:</strong> A rule that <strong>queries the database</strong> and returns rows — used in reports, dropdowns, and Data Page sources.</div></div>

<div class="qa-block"><div class="question">28. What is an Agent?</div>
<div class="answer"><strong>Easy answer:</strong> A <strong>background worker</strong> that runs on a schedule — processes queues, sends escalations, handles bulk work while users sleep.</div></div>

<div class="qa-block"><div class="question">29. Agent vs Job Scheduler?</div>
<div class="answer"><strong>Easy answer:</strong> Both run background jobs. <strong>Job Scheduler</strong> is newer and preferred for scheduled tasks. <strong>Agent</strong> is older, used for queue processing.</div></div>

<div class="qa-block"><div class="question">30. What is RAP?</div>
<div class="answer"><strong>Easy answer:</strong> <strong>Ruleset Archive Package</strong> — a zip of rules you export from Dev and import to QA/Prod. Like shipping your code in a box.</div></div>

<div class="qa-block"><div class="question">31. What is a branch in Pega?</div>
<div class="answer"><strong>Easy answer:</strong> A <strong>separate workspace</strong> for your feature so you don't break others' work. Merge when done — like Git branches.</div></div>

<div class="qa-block"><div class="question">32. What is PAL?</div>
<div class="answer"><strong>Easy answer:</strong> <strong>Performance Analyzer</strong> — shows how many DB calls happened, clipboard size, and time taken. Your first tool when something is slow.</div></div>

<div class="qa-block"><div class="question">33. What is Tracer?</div>
<div class="answer"><strong>Easy answer:</strong> Shows <strong>step-by-step</strong> which rules ran, in what order, with what data. Like a movie replay of your request.</div></div>

<div class="qa-block"><div class="question">34. What are Guardrails?</div>
<div class="answer"><strong>Easy answer:</strong> Pega's <strong>best practice rules</strong> — don't use too many activities, limit flow actions, avoid huge clipboard. Following them = healthy app.</div></div>

<div class="qa-block"><div class="question">35. What is N+1 problem?</div>
<div class="answer"><strong>Easy answer:</strong> Loop of 100 rows where each row triggers a DB call = 101 calls. Fix: load all data in <strong>one batch</strong> via Data Page or Report Definition with join.</div></div>

<div class="qa-block"><div class="question">36. What is circumstance?</div>
<div class="answer"><strong>Easy answer:</strong> A <strong>special version</strong> of a rule for certain date or condition — e.g., different tax rule for US vs UK without duplicating everything.</div></div>

<div class="qa-block"><div class="question">37. What is a child case?</div>
<div class="answer"><strong>Easy answer:</strong> A <strong>separate sub-case</strong> linked to parent — e.g., main loan case spawns "Document Verification" child case with its own workflow.</div></div>

<div class="qa-block"><div class="question">38. What is a Wait shape?</div>
<div class="answer"><strong>Easy answer:</strong> Puts the flow <strong>on pause</strong> until timer expires or something external happens (email received, child case done).</div></div>

<div class="qa-block"><div class="question">39. What is Split-Join?</div>
<div class="answer"><strong>Easy answer:</strong> Run <strong>multiple tasks in parallel</strong>, then wait for all to finish before continuing. Like sending 3 approvals at once.</div></div>

<div class="qa-block"><div class="question">40. What is a Data Type?</div>
<div class="answer"><strong>Easy answer:</strong> Pega's way to store <strong>reference data</strong> (countries, products) with built-in CRUD screens and REST API — no custom DB code needed.</div></div>

<div class="qa-block"><div class="question">41. Validate vs Edit Validate?</div>
<div class="answer"><strong>Easy answer:</strong> <strong>Edit Validate</strong> checks on screen (fast feedback). <strong>Validate</strong> checks on server when saving (final gatekeeper).</div></div>

<div class="qa-block"><div class="question">42. What is ABAC?</div>
<div class="answer"><strong>Easy answer:</strong> Security based on <strong>data values</strong> — "You can only see cases in your region." Done with Access When rules.</div></div>

<div class="qa-block"><div class="question">43. What is Deployment Manager?</div>
<div class="answer"><strong>Easy answer:</strong> Pega's tool to <strong>move apps</strong> Dev → QA → Prod with pipelines, approvals, and tests — like CI/CD for Pega.</div></div>

<div class="qa-block"><div class="question">44. How do you unit test a Data Transform?</div>
<div class="answer"><strong>Easy answer:</strong> Right-click DT → Create Test Case → set input page, expected output → run from Test Cases landing page or CI pipeline.</div></div>

<div class="qa-block"><div class="question">45. What is pxRequestor?</div>
<div class="answer"><strong>Easy answer:</strong> Page with <strong>logged-in user info</strong> — name, roles, access group, locale. Available everywhere in the session.</div></div>

<div class="qa-block"><div class="question">46. What is pzInsKey?</div>
<div class="answer"><strong>Easy answer:</strong> The <strong>unique ID</strong> of any instance in Pega — like a primary key. Used to open exact record with Obj-Open-By-Handle.</div></div>

<div class="qa-block"><div class="question">47. What is difference between App Studio and Dev Studio?</div>
<div class="answer"><strong>Easy answer:</strong> <strong>App Studio</strong> = simpler, guided, for business users. <strong>Dev Studio</strong> = full power for developers — all rule types, tracer, PAL, advanced config.</div></div>

<div class="qa-block"><div class="question">48. What is your day-to-day as a Pega developer?</div>
<div class="answer"><strong>Sample answer:</strong> Design case types, build flows, create Data Pages/DTs, configure integrations, fix bugs with Tracer/PAL, write unit tests, merge branches, deploy via RAP/pipeline, follow guardrails.</div></div>

<div class="qa-block"><div class="question">49. Tell me about a challenging bug you fixed.</div>
<div class="answer"><strong>STAR tip:</strong> Situation: slow case. Task: find root cause. Action: PAL showed 200 DB ops, Tracer found looping activity calling Obj-Open per row. Result: replaced with batch Data Page, reduced to 3 DB ops, 80% faster.</div></div>

<div class="qa-block"><div class="question">50. Why should we hire you as a Pega developer?</div>
<div class="answer"><strong>Sample answer:</strong> "I have 3+ years building case types end-to-end, I follow guardrails, I prefer declarative rules (DT, Data Pages) over activities, I've done integrations and deployments, and I can explain complex concepts simply to business teams."</div></div>
</div>
"""


def build_verification_chapter() -> str:
    return """
<div class="chapter" id="ch-verify">
<h2>Chapter 32: Topic Verification — Everything Covered ✅</h2>
<div class="flirt-box">I promised nothing would be missed. Here's proof — every row is in this PDF with explanation, diagram, and/or interview Q&amp;A.</div>

<table>
<tr><th>Topic Area</th><th>Covered In</th><th>Diagram?</th><th>Common Q&amp;A?</th></tr>
<tr><td>Platform &amp; Architecture</td><td>Ch 1</td><td>—</td><td>✅</td></tr>
<tr><td>Class Hierarchy</td><td>Ch 2</td><td>✅ Fig 07</td><td>✅</td></tr>
<tr><td>Rule Resolution</td><td>Ch 3</td><td>✅ Fig 01</td><td>✅ Top 50 #3-4</td></tr>
<tr><td>Application Stack</td><td>Ch 4</td><td>✅ Fig 13</td><td>✅</td></tr>
<tr><td>Case Management</td><td>Ch 5</td><td>✅ Fig 02, 15</td><td>✅ Top 50 #2,13</td></tr>
<tr><td>Flows &amp; Flow Actions</td><td>Ch 6</td><td>✅ Fig 03, 18</td><td>✅ Top 50 #12</td></tr>
<tr><td>Assignments &amp; Routing</td><td>Ch 7</td><td>✅ Fig 11</td><td>✅ Top 50 #14-15</td></tr>
<tr><td>Clipboard &amp; Data Model</td><td>Ch 8</td><td>✅ Fig 12</td><td>✅ Top 50 #9-11</td></tr>
<tr><td>Data Pages</td><td>Ch 9</td><td>✅ Fig 04</td><td>✅ Top 50 #7</td></tr>
<tr><td>Data Transforms</td><td>Ch 10</td><td>—</td><td>✅ Top 50 #8</td></tr>
<tr><td>Activities</td><td>Ch 11</td><td>—</td><td>✅ Top 50 #8</td></tr>
<tr><td>Decision Rules</td><td>Ch 12</td><td>✅ Fig 16</td><td>✅ Top 50 #18-19</td></tr>
<tr><td>Declare Rules</td><td>Ch 13</td><td>✅ Fig 10</td><td>✅ Top 50 #20</td></tr>
<tr><td>Validation</td><td>Ch 14</td><td>✅ Fig 19</td><td>✅ Top 50 #41</td></tr>
<tr><td>UI &amp; Constellation</td><td>Ch 15</td><td>✅ Fig 17</td><td>✅ Top 50 #25-26</td></tr>
<tr><td>SLAs &amp; Urgency</td><td>Ch 16</td><td>✅ Fig 08</td><td>✅ Top 50 #16-17</td></tr>
<tr><td>Integration</td><td>Ch 17</td><td>✅ Fig 05</td><td>✅ Top 50 #21-22,40</td></tr>
<tr><td>Security</td><td>Ch 18</td><td>✅ Fig 06</td><td>✅ Top 50 #23-24,42</td></tr>
<tr><td>Agents &amp; Schedulers</td><td>Ch 19</td><td>✅ Fig 14</td><td>✅ Top 50 #28-29</td></tr>
<tr><td>Reporting</td><td>Ch 20</td><td>—</td><td>✅ Top 50 #27</td></tr>
<tr><td>Testing</td><td>Ch 21</td><td>✅ Fig 21</td><td>✅ Top 50 #44</td></tr>
<tr><td>Performance</td><td>Ch 22</td><td>✅ Fig 23</td><td>✅ Top 50 #32-35</td></tr>
<tr><td>DevOps</td><td>Ch 23</td><td>✅ Fig 09</td><td>✅ Top 50 #30-31,43</td></tr>
<tr><td>Email &amp; Documents</td><td>Ch 24</td><td>—</td><td>✅ Rapid Fire</td></tr>
<tr><td>CDH / RPA / AI</td><td>Ch 25</td><td>—</td><td>✅ Rapid Fire</td></tr>
<tr><td>Controls &amp; Localization</td><td>Ch 26</td><td>✅ Fig 22</td><td>✅ Rapid Fire</td></tr>
<tr><td>Object Persistence</td><td>Ch 27</td><td>✅ Fig 20</td><td>✅ Top 50 #46</td></tr>
<tr><td>Top 50 Interview Q&amp;A</td><td>Ch 28</td><td>—</td><td>✅ Full answers</td></tr>
<tr><td>200 Rapid-Fire</td><td>Ch 29</td><td>—</td><td>✅</td></tr>
<tr><td>Mock Scenarios</td><td>Ch 30</td><td>—</td><td>✅</td></tr>
<tr><td>Final Checklist</td><td>Ch 31</td><td>—</td><td>✅</td></tr>
</table>

<div class="tip"><strong>Verified:</strong> 75+ topics · 23 diagrams · 50 detailed Q&amp;A · 200 rapid-fire · 4 mock scenarios · 30+ chapters. You are interview-ready.</div>
</div>
"""
