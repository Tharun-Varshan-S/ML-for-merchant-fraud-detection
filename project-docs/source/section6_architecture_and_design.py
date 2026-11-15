"""
Section 6 — Architecture, Database Design, and API Design generator.
"""

def get_section6_html(decision_policy_svg, database_schema_svg, data_flow_svg):
    return f'''
<div class="page-break"></div>
<h1 id="section-6"><span class="section-number">6</span> ARCHITECTURE, DATABASE DESIGN, AND API DESIGN</h1>

<h2 id="sec-6-1">6.1 Conceptual Architecture &amp; Component Responsibilities</h2>
<p>
  MerchantShield AI operates on a modern, four-tier architecture designed to maintain strict boundaries between statistical estimation, display presentation, operational governance, and client rendering.
</p>
<p>
  The system components and their isolated responsibilities are:
</p>
<ul>
  <li><strong>Presentation Tier (React 19 / Vite):</strong> Renders the web dashboard. Consumes the backend API purely via asynchronous JSON HTTP requests. It contains no business logic, no policy rules, and zero Python dependencies.</li>
  <li><strong>API &amp; Validation Gateway (FastAPI / Pydantic v2):</strong> Enforces strict structural boundaries on incoming requests. Validates data types, rejects negative amounts or blank strings, and guarantees that historical context transactions belong to the same customer and possess timestamps strictly prior to the current transaction.</li>
  <li><strong>Feature Engineering &amp; ML Intelligence (NumPy / LightGBM / SHAP):</strong> Marshals raw transaction event streams into 15 strictly-prior behavioral features, executes gradient-boosted tree inference using a frozen model artifact (<code>candidate_lgbm_v1.pkl</code>), and decomposes model log-odds into exact Shapley values.</li>
  <li><strong>Governance &amp; Policy Tier (Decision Engine / SQLite):</strong> Evaluates an ordered five-rule cascade to map <code>(probability, amount)</code> to bounded action recommendations, recording the immutable decision facts into an isolated SQLite audit log.</li>
</ul>

<h2 id="sec-6-2">6.2 Database &amp; Storage Design: The SQLite Audit Store</h2>
<p>
  MerchantShield AI utilizes a single, serverless SQLite relational database (<code>backend/data/audit.db</code>) managed through SQLAlchemy 2.0 ORM.
</p>

<div class="diagram-container">
  {database_schema_svg}
  <div class="diagram-caption">Figure 6.1: SQLite Database Entity Design (audit_log table) with Explicit Privacy and Governance Separation.</div>
</div>

<h3>Schema Specification: The <code>audit_log</code> Table</h3>
<table>
  <thead>
    <tr>
      <th>Column Name</th>
      <th>SQL Type</th>
      <th>Nullability / Index</th>
      <th>Description &amp; Governance Rationale</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>id</code></td>
      <td><code>INTEGER</code></td>
      <td>PRIMARY KEY, AUTOINCREMENT</td>
      <td>Unique autoincrementing record sequence identifier.</td>
    </tr>
    <tr>
      <td><code>request_id</code></td>
      <td><code>VARCHAR(64)</code></td>
      <td>NOT NULL, INDEXED</td>
      <td>UUID4 generated per API call, allowing distributed log tracing across systems.</td>
    </tr>
    <tr>
      <td><code>transaction_id</code></td>
      <td><code>VARCHAR(64)</code></td>
      <td>NOT NULL, INDEXED</td>
      <td>Merchant transaction identifier being audited. Fast lookup index.</td>
    </tr>
    <tr>
      <td><code>model_version</code></td>
      <td><code>VARCHAR(32)</code></td>
      <td>NOT NULL</td>
      <td>Identifies the model artifact used (e.g., <code>"lgbm_v1"</code>), ensuring model version reproducibility.</td>
    </tr>
    <tr>
      <td><code>fraud_probability</code></td>
      <td><code>FLOAT</code></td>
      <td>NOT NULL</td>
      <td>Raw predicted probability <code>[0.0, 1.0]</code> from the LightGBM model.</td>
    </tr>
    <tr>
      <td><code>threshold</code></td>
      <td><code>FLOAT</code></td>
      <td>NOT NULL</td>
      <td>The cost-optimal decision threshold in effect at decision time (<code>0.40</code>).</td>
    </tr>
    <tr>
      <td><code>risk_score</code></td>
      <td><code>INTEGER</code></td>
      <td>NOT NULL</td>
      <td>Continuous 0–100 risk score generated for human readability.</td>
    </tr>
    <tr>
      <td><code>risk_category</code></td>
      <td><code>VARCHAR(16)</code></td>
      <td>NOT NULL</td>
      <td>Human tier: <code>LOW</code>, <code>MEDIUM</code>, <code>HIGH</code>, or <code>CRITICAL</code>.</td>
    </tr>
    <tr>
      <td><code>action</code></td>
      <td><code>VARCHAR(32)</code></td>
      <td>NOT NULL</td>
      <td>The bounded action recommended: <code>ALLOW</code>, <code>ALLOW_WITH_MONITORING</code>, <code>STEP_UP_VERIFICATION</code>, <code>BLOCK</code>.</td>
    </tr>
    <tr>
      <td><code>policy_rule_id</code></td>
      <td><code>VARCHAR(64)</code></td>
      <td>NOT NULL</td>
      <td>The exact policy rule that fired (e.g., <code>"CRITICAL_BLOCK"</code> or <code>"HIGH_STEP_UP"</code>).</td>
    </tr>
    <tr>
      <td><code>policy_reason</code></td>
      <td><code>TEXT</code></td>
      <td>NOT NULL</td>
      <td>Verbatim business rationale for the triggered rule, ensuring regulatory auditability.</td>
    </tr>
    <tr>
      <td><code>decision_timestamp</code></td>
      <td><code>VARCHAR(64)</code></td>
      <td>NOT NULL</td>
      <td>ISO-8601 timestamp of the decision computation.</td>
    </tr>
    <tr>
      <td><code>top_reasons_json</code></td>
      <td><code>TEXT</code></td>
      <td>NULLABLE</td>
      <td>Serialized JSON array of grounded SHAP explanation strings.</td>
    </tr>
    <tr>
      <td><code>source</code></td>
      <td><code>VARCHAR(16)</code></td>
      <td>NOT NULL, DEFAULT 'manual'</td>
      <td>Request origin: <code>"demo"</code> for dashboard scenarios or <code>"manual"</code> for API callers.</td>
    </tr>
    <tr>
      <td><code>prior_transaction_count</code></td>
      <td><code>INTEGER</code></td>
      <td>NOT NULL, DEFAULT 0</td>
      <td>V2: Contextual count of prior transactions supplied for behavioral analysis.</td>
    </tr>
    <tr>
      <td><code>created_at</code></td>
      <td><code>DATETIME</code></td>
      <td>NOT NULL</td>
      <td>Database record insertion timestamp (UTC).</td>
    </tr>
  </tbody>
</table>

<h3>Governance Principles: Decision Facts vs. Explanations &amp; PII Omission</h3>
<p>
  The storage design embodies two vital privacy and governance invariants:
</p>
<ol>
  <li><strong>Separation of Durable Decision Facts from Derived Narratives:</strong> The hard facts that govern the transaction (probability, rule ID, threshold, action) are stored in discrete, indexed columns. The human-readable narrative is stored alongside in <code>top_reasons_json</code> as explanatory context. This prevents UI narrative updates from ever mutating underlying audit facts.</li>
  <li><strong>Strict Omission of Customer PII:</strong> The database intentionally stores <em>no</em> customer primary account numbers (PAN), customer names, device fingerprints, or geographic regions. The audit trail's sole responsibility is to prove what the <em>risk decisioning system</em> evaluated and recommended, avoiding unnecessary duplication of sensitive customer data outside core merchant ledgers.</li>
  <li><strong>V2 Idempotent Schema Migration:</strong> In existing deployments where <code>audit_log</code> was created under V1, SQLAlchemy's standard <code>create_all()</code> does not alter existing tables. In <code>backend/services/audit_service.py</code>, the <code>_migrate_add_prior_transaction_count_if_needed()</code> method executes an idempotent raw SQL check:
  <pre><code>cursor.execute("PRAGMA table_info(audit_log)")
columns = {{row[1] for row in cursor.fetchall()}}
if "prior_transaction_count" not in columns:
    cursor.execute("ALTER TABLE audit_log ADD COLUMN prior_transaction_count INTEGER DEFAULT 0")</code></pre>
  This guarantees seamless in-place schema upgrades without downtime or data loss.</li>
</ol>

<h2 id="sec-6-3">6.3 API &amp; Interface Design: The Six Endpoints</h2>
<p>
  MerchantShield AI exposes six documented REST endpoints via FastAPI:
</p>

<table>
  <thead>
    <tr>
      <th>HTTP Method</th>
      <th>Route Path</th>
      <th>Operation Purpose</th>
      <th>Key Request Parameters</th>
      <th>Success Response Model</th>
      <th>Audit Persistence</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>GET</code></td>
      <td><code>/health</code></td>
      <td>Liveness and readiness check; reports model load status.</td>
      <td>None</td>
      <td><code>HealthResponse</code></td>
      <td>No</td>
    </tr>
    <tr>
      <td><code>GET</code></td>
      <td><code>/model/info</code></td>
      <td>Static frozen model metadata, threshold, and metrics.</td>
      <td>None</td>
      <td><code>ModelInfoResponse</code></td>
      <td>No</td>
    </tr>
    <tr>
      <td><code>POST</code></td>
      <td><code>/risk/score</code></td>
      <td>Lightweight scoring: probability and 0–100 score only.</td>
      <td><code>RiskRequest</code> body</td>
      <td><code>RiskScoreResponse</code></td>
      <td>No</td>
    </tr>
    <tr>
      <td><code>POST</code></td>
      <td><code>/risk/explain</code></td>
      <td>Inference plus full SHAP feature contributions and reasons.</td>
      <td><code>RiskRequest</code> body</td>
      <td><code>RiskExplainResponse</code></td>
      <td>No</td>
    </tr>
    <tr>
      <td><code>POST</code></td>
      <td><code>/risk/evaluate</code></td>
      <td><strong>Full Pipeline:</strong> Score + Explain + 5-Rule Decision + Audit.</td>
      <td><code>RiskRequest</code> body</td>
      <td><code>RiskEvaluateResponse</code></td>
      <td><strong>Yes</strong></td>
    </tr>
    <tr>
      <td><code>GET</code></td>
      <td><code>/audit-log</code></td>
      <td>Retrieves recent persisted decision records (default 50).</td>
      <td><code>limit: int = 50</code></td>
      <td><code>List[AuditEntry]</code></td>
      <td>No (Read-only)</td>
    </tr>
  </tbody>
</table>

<h3>Endpoint Isolation &amp; Failure Recovery Rationale</h3>
<p>
  Why does the system provide three separate POST endpoints?
</p>
<ul>
  <li><code>/risk/score</code> and <code>/risk/explain</code> are explicitly designed for interactive exploration, high-throughput batch simulation, and what-if analysis. They <strong>never write to the audit log</strong>, ensuring test simulations do not pollute legal compliance records.</li>
  <li><code>/risk/evaluate</code> is the single authoritative entry point for operational decisions. It executes the full decision engine and attempts an audit write.</li>
</ul>

<div class="callout callout-warning">
  <div class="callout-title">The Audit-Write Failure Isolation Pattern</div>
  In production, high-throughput disk write locks or full storage partitions could cause SQLite to throw an operational exception. Under a naive implementation, this exception would cause <code>/risk/evaluate</code> to return an HTTP 500 Internal Server Error, leaving the merchant payment gateway blind and forcing the merchant to either drop the sale or let unvetted fraud pass through!
  <br/><br/>
  MerchantShield AI handles this through <strong>Audit Isolation</strong> in <code>backend/api/routes.py</code>:
  <pre><code>audit_persisted = False
audit_error = None
if audit_store is not None:
    try:
        audit_store.record_decision(...)
        audit_persisted = True
    except AuditPersistenceError as e:
        audit_error = str(e)</code></pre>
  If audit persistence fails, the API <em>still returns the valid HTTP 200 risk decision</em> (with <code>audit_persisted: false</code> and <code>audit_error</code> populated). The merchant receives their fraud decision, and the audit write failure is surfaced as an operational warning rather than crashing the transaction.
</div>

<h2 id="sec-6-4">6.4 Architectural Trade-Offs, Invariants &amp; Decoupling</h2>

<div class="diagram-container">
  {decision_policy_svg}
  <div class="diagram-caption">Figure 6.2: The Five-Rule Deterministic Policy Decision Cascade (Source: ml/evaluation/policy.py).</div>
</div>

<h3>The 5-Rule Policy Cascade (First Match Wins)</h3>
<p>
  The decision engine implements a strict priority ladder. In <code>ml/evaluation/policy.py</code>, rules fire in order:
</p>
<ol>
  <li><strong><code>CRITICAL_BLOCK</code> (<code>p &ge; 0.80</code>):</strong> Recommends <code>BLOCK</code>. At 0.80 probability, validation precision is 94.1%—the model is overwhelmingly confident that the transaction is criminal.</li>
  <li><strong><code>HIGH_STEP_UP</code> (<code>p &ge; 0.40</code>):</strong> Recommends <code>STEP_UP_VERIFICATION</code>. This operates at the cost-optimal decision threshold (0.40). It catches 88.2% of fraud while subjecting borderline transactions to low-friction verification (e.g., SMS OTP or biometric challenge) rather than an outright decline.</li>
  <li><strong><code>MEDIUM_AMOUNT_ESCALATION</code> (<code>p &ge; 0.15</code> AND <code>amount &ge; ₹25,000</code>):</strong> Recommends <code>STEP_UP_VERIFICATION</code>. Even though model probability is moderate, the high transaction value creates severe financial downside if fraudulent, warranting step-up friction.</li>
  <li><strong><code>MEDIUM_MONITOR</code> (<code>p &ge; 0.15</code>):</strong> Recommends <code>ALLOW_WITH_MONITORING</code>. Elevated risk above baseline, but low enough that customer checkout friction is unwarranted.</li>
  <li><strong><code>LOW_ALLOW</code> (Catch-all):</strong> Recommends <code>ALLOW</code>. Clean transaction with minimal risk signals; permitted with zero friction.</li>
</ol>

<h2 id="sec-6-5">6.5 End-to-End Sequence &amp; Data Flow</h2>
<p>
  The sequence diagram below traces the end-to-end lifecycle of an incoming transaction request through the system:
</p>

<div class="diagram-container">
  {data_flow_svg}
  <div class="diagram-caption">Figure 6.3: MerchantShield AI End-to-End Sequence and Data Flow Diagram.</div>
</div>
'''
