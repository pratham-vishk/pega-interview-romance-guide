"""Low-Level Design framework and problems."""

from content.helpers import bullets, code_block, section, table, tip


SOLID = [
    ("SRP", "Single Responsibility", "One class, one reason to change", "UserService shouldn't send emails AND validate AND persist"),
    ("OCP", "Open/Closed", "Open for extension, closed for modification", "Add new PaymentMethod without changing PaymentProcessor"),
    ("LSP", "Liskov Substitution", "Subtypes must be substitutable", "Square shouldn't break Rectangle setWidth/setHeight contract"),
    ("ISP", "Interface Segregation", "No fat interfaces", "Split Readable/Writable instead of one huge Repository"),
    ("DIP", "Dependency Inversion", "Depend on abstractions", "Inject PaymentGateway interface, not StripeClient"),
]

DESIGN_PATTERNS = [
    ("Strategy", "Swap algorithms at runtime", "PricingStrategy: Regular, Premium, Discount"),
    ("Factory", "Create objects without specifying class", "VehicleFactory.create(type)"),
    ("Abstract Factory", "Families of related objects", "UIFactory: WinButton + WinCheckbox"),
    ("Builder", "Step-by-step complex construction", "HttpRequest.Builder().url().header().build()"),
    ("Observer", "Publish-subscribe", "OrderService notifies Inventory + Notification"),
    ("Decorator", "Add behavior without subclassing", "BufferedInputStream wraps FileInputStream"),
    ("Adapter", "Convert interface", "LegacyPaymentAdapter implements PaymentGateway"),
    ("Facade", "Simplified API over subsystem", "OrderFacade hides inventory + payment + shipping"),
    ("Command", "Encapsulate request as object", "Undo/redo with Command stack"),
    ("State", "Behavior changes with state", "VendingMachine: Idle, HasMoney, Dispensing"),
    ("Singleton", "One instance — often overused", "Prefer DI container scoped bean; hard to test"),
]

LLD_PROBLEMS = [
    "Parking Lot", "Elevator", "Library Management", "Vending Machine", "Splitwise",
    "Tic-Tac-Toe", "Chess", "Cab Booking", "Logger", "Rate Limiter",
]


def _lld_problem_skeleton(name: str) -> str:
    return f"""
<div class="pattern-card">
<h3>{name}</h3>
<h4>Requirements → Entities</h4>
<p>Clarify: actors, core use cases, scale (single machine vs distributed), concurrency needs.</p>
<h4>Key Entities & Interfaces</h4>
<ul>
<li>Define nouns: Vehicle, Spot, Ticket, Payment (example for Parking Lot)</li>
<li>Interfaces for extensibility: PricingStrategy, Notifier, Storage</li>
</ul>
<h4>Design Patterns</h4>
<p>Strategy (pricing), Factory (vehicle types), Observer (notifications), Singleton only if justified.</p>
<h4>Concurrency</h4>
<p>synchronized / ReentrantLock on shared spot map; consider ConcurrentHashMap for spot registry.</p>
<h4>Java Skeleton</h4>
{code_block(f'''// {name} — interview skeleton
interface Repository<T, ID> {{
    Optional<T> findById(ID id);
    void save(T entity);
}}

enum Status {{ ACTIVE, INACTIVE }}

class Service {{
    private final Repository<?, ?> repo;
    Service(Repository<?, ?> repo) {{ this.repo = repo; }}
    // core methods
}}''')}
<h4>Extensibility</h4>
<p>New vehicle types, pricing rules, or payment methods via new implementations — not modifying core.</p>
<h4>Interview Follow-up</h4>
<p>How would you scale to multiple floors/buildings? How handle concurrent booking conflicts?</p>
</div>"""


def build_lld_section() -> str:
    solid_rows = [(p[0], f"{p[1]}: {p[2]} — {p[3]}") for p in SOLID]
    body = "<h3>SOLID Principles</h3>" + table(["Principle", "Explanation"], solid_rows)
    body += "<h3>Core OOP Concepts</h3>" + bullets([
        "Composition over inheritance — favor has-a over is-a",
        "Interfaces for contracts; abstract classes for shared state",
        "Encapsulation — private fields, public behavior",
        "Dependency Injection — constructor injection preferred",
        "Immutability — final fields, unmodifiable collections where possible",
    ])
    body += "<h3>Design Patterns</h3>"
    for name, problem, example in DESIGN_PATTERNS:
        body += f"""
<div class="pattern-card">
<h4>{name}</h4>
<p><strong>Problem:</strong> {problem}</p>
<p><strong>Bad design:</strong> Giant if-else or god class</p>
<p><strong>Better:</strong> {example}</p>
<p><strong>Interview Q:</strong> When would you NOT use {name}?</p>
</div>"""
    body += "<h3>LLD Problems — Full Framework</h3>"
    for prob in LLD_PROBLEMS:
        body += _lld_problem_skeleton(prob)
    body += tip("Google L4 LLD: clear class diagram, SOLID, extensibility, basic concurrency. L5: deeper trade-offs, multi-tenant, observability.")
    return section("lld", "Low-Level Design (LLD)", body)
