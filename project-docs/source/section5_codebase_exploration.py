"""
Section 5 — Codebase Exploration generator.
"""

def get_section5_html():
    return '''
<div class="page-break"></div>
<h1 id="section-5"><span class="section-number">5</span> CODEBASE EXPLORATION: EVERY IMPORTANT FILE AND FOLDER</h1>

<h2 id="sec-5-1">5.1 Complete Repository Directory Tree</h2>
<p>
  The MerchantShield AI repository is organized into distinct, decoupled domains covering backend APIs, machine learning pipelines, evaluation modules, external datasets, frontend UI, automated tests, and documentation:
</p>

<pre><code>merchantshield-ai/
├── .github/workflows/
│   └── ci.yml                       # GitHub Actions: multi-job CI (Python 3.13 + Node 22)
├── backend/                         # FastAPI Application &amp; Services
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes.py                # 6 API route handlers (/health, /risk/evaluate, etc.)
│   ├── config/
│   │   ├── __init__.py
│   │   └── settings.py              # Path constants, titles, versions (no policy rules)
│   ├── data/
│   │   └── audit.db                 # SQLite database file (created on runtime)
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── response.py              # Pydantic response models (Health, RiskEvaluate, etc.)
│   │   └── transaction.py           # Pydantic request models (RiskRequest, TransactionInput)
│   ├── services/
│   │   ├── __init__.py
│   │   ├── audit_service.py         # SQLAlchemy AuditStore with idempotent schema migration
│   │   ├── model_loader.py          # One-time startup model &amp; explainer artifact loader
│   │   └── risk_service.py          # Pipeline orchestrator &amp; V2 hardening bounds checker
│   ├── __init__.py
│   └── main.py                      # FastAPI lifespan, CORS, error handlers, static mount
├── docs/                            # Comprehensive System Architecture &amp; Experiment Reports
│   ├── api.md                       # Complete API contract and error specification
│   ├── decision_engine.md           # Rationale for rule-based decisioning &amp; boundary tests
│   ├── explainability.md            # SHAP TreeExplainer mathematics &amp; grounding rules
│   ├── external_validation_ieee_cis.md # IEEE-CIS dataset provenance &amp; Experiment A/B results
│   ├── frontend.md                  # Dashboard decoupling &amp; scenario verification
│   ├── phase15_card_product_experiment.md # Ablation study for card_product_share feature
│   ├── phase17_razorpay_real_data_validation.md # Canonical held-out real data evaluation
│   └── README.md                    # Documentation index and review order
├── frontend/                        # React 19 / Vite Single-Page Dashboard
│   ├── src/
│   │   ├── api/
│   │   │   └── client.js            # Fetch API client (zero backend Python dependencies)
│   │   ├── components/
│   │   │   ├── AuditLogTable.jsx    # Real-time tabular display of persisted decisions
│   │   │   ├── ErrorBanner.jsx      # Clean error notification banner
│   │   │   ├── ExplanationPanel.jsx # SHAP grounded reasons &amp; contribution bar charts
│   │   │   ├── ModelInfoPanel.jsx   # Frozen threshold &amp; test set metrics viewer
│   │   │   ├── RiskResultCard.jsx   # Action badge (BLOCK/ALLOW) &amp; 0-100 score gauge
│   │   │   ├── StatusBar.jsx        # API liveness &amp; model load readiness indicator
│   │   │   └── TransactionForm.jsx  # Scenario selector &amp; manual transaction editor
│   │   ├── data/
│   │   │   └── sampleScenarios.js   # 4 demo scenarios (LOW, MEDIUM, HIGH, CRITICAL)
│   │   ├── styles/
│   │   │   ├── App.css              # Dashboard layout, cards, and responsive styles
│   │   │   └── tokens.css           # Vanilla CSS custom properties (colors, typography)
│   │   ├── utils/
│   │   │   └── presentation.js      # Color mappers and human-readable formatting
│   │   ├── App.jsx                  # Root React component orchestrating dashboard state
│   │   └── main.jsx                 # React DOM mount point
│   ├── index.html                   # HTML5 template
│   ├── package.json                 # Node dependencies (React 19, Vite, Oxlint)
│   └── vite.config.js               # Vite build and proxy configuration
├── ml/                              # Machine Learning Research, Training &amp; Evaluation
│   ├── data/
│   │   └── generate_synthetic.py    # Synthetic generator (~213k txns, 2,200 users, 1.5% fraud)
│   ├── evaluation/
│   │   ├── cost_model.py            # Asymmetric FP/FN financial loss objective formulation
│   │   ├── decision_engine.py       # make_decision() and DecisionRecord dataclass
│   │   ├── demo_decision.py         # Verification demo of policy decision outputs
│   │   ├── demo_explain.py          # Verification demo of SHAP explainability outputs
│   │   ├── explainability.py        # RiskExplainer (TreeExplainer + additivity check)
│   │   ├── policy.py                # 5-rule deterministic policy table &amp; boundary logic
│   │   ├── risk_scoring.py          # Continuous probability to 0-100 score &amp; tier mapping
│   │   └── threshold_analysis.py    # Cost-minimizing validation threshold sweep
│   ├── external/                    # External Real-World Validation Track (IEEE-CIS)
│   │   └── ieee/
│   │       ├── card_product_features.py # Phase 15 card_product_share feature extractor
│   │       ├── experiment_a_frozen.py   # Evaluates frozen synthetic model on IEEE-CIS
│   │       ├── experiment_b_retrain.py  # Retrains LightGBM on IEEE-CIS training split
│   │       ├── ieee_adapter.py          # Maps raw IEEE-CIS columns to MerchantShield schema
│   │       ├── ieee_features.py         # Leakage-safe feature extraction for IEEE-CIS
│   │       ├── ieee_split.py            # Chronological 182-day train/val/test splitter
│   │       └── razorpay_validation.py   # Phase 17 canonical held-out real data evaluation
│   ├── features/
│   │   └── build_features.py        # 15 strictly-prior features computed on event logs
│   ├── models/
│   │   ├── baseline_logreg_v1.pkl   # Fitted Logistic Regression baseline artifact
│   │   ├── candidate_lgbm_v1.pkl    # Frozen LightGBM production model artifact
│   │   ├── candidate_rf_v1.pkl      # Fitted Random Forest candidate artifact
│   │   ├── lgbm_v1_metadata.json    # Committed metadata (threshold, val/test metrics)
│   │   ├── threshold_analysis_chart.png # Validation precision/recall/cost sweep plot
│   │   └── threshold_sweep_validation.csv # CSV log of threshold sweep metrics
│   └── training/
│       ├── train_baseline.py        # Trains baseline Logistic Regression &amp; chronological_split
│       └── train_candidates.py      # Benchmarks RF &amp; LightGBM candidates vs baseline
├── screenshots/
│   └── README.md                    # Capture guide for UI screenshots (none fabricated)
├── tests/                           # 269 Automated pytest Test Cases
│   ├── conftest.py                  # Pytest fixtures (sample payloads, mock models)
│   ├── test_api.py                  # API contract, status codes, audit isolation tests
│   ├── test_card_product_features.py # 35 unit tests verifying card_product_share
│   ├── test_decision_engine.py      # 51 tests: policy branches, boundaries, fail-safes
│   ├── test_explainability.py       # SHAP additivity checks, grounding &amp; determinism
│   ├── test_ieee_external.py        # IEEE-CIS adapter, prohibited columns, leakage tests
│   ├── test_no_leakage.py           # Validates strictly-prior feature logic on 213k rows
│   ├── test_phase17_validation.py   # Phase 17 pipeline contract &amp; threshold selection tests
│   └── test_v2_hardening.py         # Feature bounds, probability validation &amp; migration tests
├── CONTRIBUTING.md                  # Developer guidelines &amp; ML integrity rules
├── docker-compose.yml               # Multi-container orchestration (FastAPI + Audit volume)
├── Dockerfile                       # Multi-stage production container build definition
├── README.md                        # Master repository documentation &amp; project summary
└── requirements.txt                 # Pinned Python dependencies (NumPy, LightGBM, etc.)
</code></pre>

<h2 id="sec-5-2">5.2 Folder-by-Folder Structural Overview</h2>
<ul>
  <li><strong><code>backend/</code>:</strong> Encapsulates the application server. Divided into <code>api/</code> (REST endpoint declarations), <code>schemas/</code> (strict Pydantic contracts), <code>config/</code> (global constants and project paths), and <code>services/</code> (business logic, model artifact caching, and persistence).</li>
  <li><strong><code>ml/</code>:</strong> Contains all machine learning research, data synthesis, feature engineering, and model training code. Divided into <code>data/</code> (raw transaction generator), <code>features/</code> (feature transformation), <code>training/</code> (model training scripts), <code>evaluation/</code> (cost models, threshold sweep, decision engine, explainability), <code>models/</code> (frozen binary artifacts and serialized JSON metadata), and <code>external/</code> (IEEE-CIS research track).</li>
  <li><strong><code>frontend/</code>:</strong> Houses the React 19 single-page application. Features a modular component hierarchy (<code>components/</code>), static scenario definitions (<code>data/</code>), and zero-dependency Vanilla CSS tokens (<code>styles/</code>).</li>
  <li><strong><code>docs/</code>:</strong> Comprehensive technical monographs, API contracts, architectural design decisions, and external validation experiment reports.</li>
  <li><strong><code>tests/</code>:</strong> Robust test suite comprising 269 automated test cases covering every mathematical invariant, boundary condition, API status code, and defensive failure path.</li>
</ul>

<h2 id="sec-5-3">5.3 File-by-File Technical Reference Inventory</h2>
<table>
  <thead>
    <tr>
      <th>Relative File Path</th>
      <th>Primary Responsibility &amp; Key Definitions</th>
      <th>Inputs &amp; Outputs</th>
      <th>Pipeline Participation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>backend/main.py</code></td>
      <td>FastAPI application entry point; <code>lifespan</code> context manager; global error handlers; static asset mounting.</td>
      <td>In: App config; Out: Running ASGI application process.</td>
      <td>Stage 1 (Bootstrapping) &amp; Stage 9 (Delivery)</td>
    </tr>
    <tr>
      <td><code>backend/config/settings.py</code></td>
      <td>Centralizes file paths, API title, version, and SQLite DB URL. Deliberately omits policy numbers.</td>
      <td>In: Environment; Out: Path and service constants.</td>
      <td>Global configuration across all backend modules.</td>
    </tr>
    <tr>
      <td><code>backend/api/routes.py</code></td>
      <td>Implements 6 REST routes: <code>/health</code>, <code>/model/info</code>, <code>/risk/score</code>, <code>/risk/explain</code>, <code>/risk/evaluate</code>, <code>/audit-log</code>.</td>
      <td>In: <code>RiskRequest</code>; Out: Strongly typed Pydantic responses.</td>
      <td>Stage 2 (Request) &amp; Stage 9 (Response)</td>
    </tr>
    <tr>
      <td><code>backend/schemas/transaction.py</code></td>
      <td>Declares <code>TransactionInput</code> and <code>RiskRequest</code>. Validates positive amounts, non-blank strings, and strictly-prior timestamps.</td>
      <td>In: Raw JSON body; Out: Validated Python Pydantic objects.</td>
      <td>Stage 2: Request Validation</td>
    </tr>
    <tr>
      <td><code>backend/schemas/response.py</code></td>
      <td>Defines response models: <code>HealthResponse</code>, <code>ModelInfoResponse</code>, <code>RiskScoreResponse</code>, <code>RiskEvaluateResponse</code>.</td>
      <td>In: Service results; Out: Validated JSON schemas.</td>
      <td>Stage 9: Response Assembly</td>
    </tr>
    <tr>
      <td><code>backend/services/risk_service.py</code></td>
      <td>Wires feature engineering, model inference, V2 bounds checking, SHAP explainability, and policy evaluation.</td>
      <td>In: <code>ModelBundle</code>, <code>RiskRequest</code>; Out: Decision &amp; explanation tuple.</td>
      <td>Stages 3, 4, 5, 6, and 7 orchestration.</td>
    </tr>
    <tr>
      <td><code>backend/services/model_loader.py</code></td>
      <td>Loads <code>candidate_lgbm_v1.pkl</code> and constructs <code>RiskExplainer</code> once at startup. Defines <code>ModelBundle</code>.</td>
      <td>In: Pickle/JSON paths; Out: In-memory cached <code>ModelBundle</code>.</td>
      <td>Stage 1: System Bootstrapping</td>
    </tr>
    <tr>
      <td><code>backend/services/audit_service.py</code></td>
      <td>SQLAlchemy <code>AuditStore</code>; records decisions; executes idempotent V2 SQLite column migrations; omits PII.</td>
      <td>In: <code>DecisionRecord</code>, reasons; Out: Persisted SQLite rows.</td>
      <td>Stage 8: Audit Persistence</td>
    </tr>
    <tr>
      <td><code>ml/features/build_features.py</code></td>
      <td>Computes 15 strictly-prior behavioral features (velocity, z-scores, device/geo novelty) without leakage.</td>
      <td>In: Raw transaction DataFrame; Out: 15-feature DataFrame.</td>
      <td>Stage 3: Feature Engineering</td>
    </tr>
    <tr>
      <td><code>ml/evaluation/policy.py</code></td>
      <td>Declares <code>DECISION_THRESHOLD=0.40</code>, <code>CRITICAL_MIN=0.80</code>, and <code>POLICY_RULES</code> (5-rule ordered table).</td>
      <td>In: <code>(probability, amount)</code>; Out: Triggered <code>PolicyRule</code>.</td>
      <td>Stage 7: Policy Evaluation</td>
    </tr>
    <tr>
      <td><code>ml/evaluation/decision_engine.py</code></td>
      <td>Encapsulates <code>make_decision()</code> and <code>DecisionRecord</code>. Enforces structural isolation of SHAP explanations.</td>
      <td>In: Probability, amount, ID; Out: Immutable <code>DecisionRecord</code>.</td>
      <td>Stage 7: Decision Engine</td>
    </tr>
    <tr>
      <td><code>ml/evaluation/explainability.py</code></td>
      <td><code>RiskExplainer</code> wraps <code>shap.TreeExplainer</code>; checks mathematical additivity; formats grounded narrative text.</td>
      <td>In: Feature Series; Out: Contributions &amp; grounded reasons.</td>
      <td>Stage 6: Explainability Layer</td>
    </tr>
    <tr>
      <td><code>ml/evaluation/risk_scoring.py</code></td>
      <td>Deterministic mapping of probability to 0–100 integer score and categorical tier (LOW/MED/HIGH/CRIT).</td>
      <td>In: Float probability; Out: Score &amp; category dict.</td>
      <td>Informational display across Stages 5–9.</td>
    </tr>
    <tr>
      <td><code>ml/evaluation/cost_model.py</code></td>
      <td>Formulates expected cost: <code>(FP &times; 50) + &Sigma;(FN &times; 0.5 &times; amount)</code>.</td>
      <td>In: True/pred arrays, amounts; Out: Expected rupee cost breakdown.</td>
      <td>Used in training and validation threshold analysis.</td>
    </tr>
    <tr>
      <td><code>ml/evaluation/threshold_analysis.py</code></td>
      <td>Sweeps validation thresholds (0.05 to 0.95); selects 0.40 as cost minimum subject to &ge;80% recall.</td>
      <td>In: Validation probabilities; Out: Frozen threshold &amp; chart.</td>
      <td>Threshold selection &amp; model governance.</td>
    </tr>
    <tr>
      <td><code>ml/external/ieee/razorpay_validation.py</code></td>
      <td>Canonical Phase 17 held-out real data evaluation on IEEE-CIS chargeback dataset.</td>
      <td>In: IEEE-CIS CSVs; Out: Precision/Recall/Cost on test split.</td>
      <td>External real-data validation track.</td>
    </tr>
    <tr>
      <td><code>frontend/src/App.jsx</code></td>
      <td>Root React component managing liveness status, scenario loading, dual endpoint calls, and UI state.</td>
      <td>In: User interaction; Out: Rendered DOM elements.</td>
      <td>Client Presentation Tier.</td>
    </tr>
  </tbody>
</table>

<h2 id="sec-5-4">5.4 Critical File Deep Dives &amp; Code Walkthroughs</h2>

<h3>5.4.1 <code>backend/main.py</code>: Lifespan &amp; Degradation Handling</h3>
<p>
  The main entry point manages the lifecycle of the FastAPI process. The <code>lifespan</code> context manager initializes expensive objects exactly once:
</p>
<pre><code><span class="cm"># backend/main.py (lines 32-50)</span>
<span class="kw">@asynccontextmanager</span>
<span class="kw">async def</span> <span class="fn">lifespan</span>(app: FastAPI):
    <span class="kw">try</span>:
        app.state.model_bundle = load_model_bundle(settings.MODEL_PATH, settings.MODEL_METADATA_PATH)
        logger.info(f<span class="str">"Model loaded from {{settings.MODEL_PATH}}"</span>)
    <span class="kw">except</span> ModelUnavailableError <span class="kw">as</span> e:
        <span class="cm"># Do not crash the process -- come up degraded so /health reports it clearly</span>
        logger.error(f<span class="str">"MODEL FAILED TO LOAD: {{e}}"</span>)
        app.state.model_bundle = <span class="num">None</span>

    <span class="kw">try</span>:
        app.state.audit_store = AuditStore(settings.AUDIT_DB_URL, settings.AUDIT_DB_DIR)
        logger.info(f<span class="str">"Audit store ready at {{settings.AUDIT_DB_PATH}}"</span>)
    <span class="kw">except</span> Exception <span class="kw">as</span> e:
        logger.error(f<span class="str">"AUDIT STORE FAILED TO INITIALIZE: {{e}}"</span>)
        app.state.audit_store = <span class="num">None</span>
    <span class="kw">yield</span></code></pre>
<p>
  <strong>Architectural Rationale:</strong> Rather than allowing an unhandled exception to crash the Python container during startup (which results in opaque Docker crash loops), attaching <code>model_bundle = None</code> allows the HTTP process to start. Orchestration systems (Kubernetes, AWS ECS) can query <code>/health</code>, receive <code>status: "degraded", model_loaded: false</code>, and handle alerting gracefully, while <code>/risk/evaluate</code> returns an explicit HTTP 503 Service Unavailable.
</p>

<h3>5.4.2 <code>backend/schemas/transaction.py</code>: Strict Prior History Validation</h3>
<p>
  Pydantic model validators guarantee that callers cannot accidentally pass corrupt data or future transactions as historical context:
</p>
<pre><code><span class="cm"># backend/schemas/transaction.py (lines 78-100)</span>
<span class="kw">@model_validator</span>(mode=<span class="str">"after"</span>)
<span class="kw">def</span> <span class="fn">_prior_transactions_must_be_valid_context</span>(self):
    txn = self.transaction
    <span class="kw">for</span> i, prior <span class="kw">in</span> enumerate(self.prior_transactions):
        <span class="kw">if</span> prior.customer_id != txn.customer_id:
            <span class="kw">raise</span> ValueError(
                f<span class="str">"prior_transactions[{{i}}].customer_id does not match transaction.customer_id"</span>
            )
        <span class="kw">if</span> prior.timestamp &gt;= txn.timestamp:
            <span class="kw">raise</span> ValueError(
                f<span class="str">"prior_transactions[{{i}}].timestamp ({{prior.timestamp}}) is not strictly "</span>
                f<span class="str">"before transaction.timestamp ({{txn.timestamp}}) -- leaks future data!"</span>
            )
        <span class="kw">if</span> prior.transaction_id == txn.transaction_id:
            <span class="kw">raise</span> ValueError(f<span class="str">"Transaction cannot be its own prior context."</span>)
    <span class="kw">return</span> self</code></pre>
<p>
  <strong>Architectural Rationale:</strong> If a payment gateway mistakenly included the transaction currently being evaluated inside the <code>prior_transactions</code> array, the rolling velocity and z-score calculations would double-count the transaction and leak its existence into its own baseline. This validator rejects such requests with HTTP 422 before the feature pipeline executes.
</p>

<h3>5.4.3 <code>ml/features/build_features.py</code>: Strictly-Prior Vectorized Statistics</h3>
<p>
  To prevent data leakage, cumulative sums are shifted by one index so that a transaction at index <code>i</code> only sees transactions <code>0</code> through <code>i-1</code>:
</p>
<pre><code><span class="cm"># ml/features/build_features.py (lines 36-48)</span>
prior_count = np.arange(n)  <span class="cm"># 0 for first transaction</span>
amounts = g[<span class="str">"amount"</span>].values

<span class="cm"># expanding mean/std computed strictly on values BEFORE current index</span>
cum_sum = np.concatenate(([<span class="num">0.0</span>], np.cumsum(amounts)[:-<span class="num">1</span>]))
cum_sum_sq = np.concatenate(([<span class="num">0.0</span>], np.cumsum(amounts ** <span class="num">2</span>)[:-<span class="num">1</span>]))

prior_mean = np.divide(cum_sum, prior_count, out=np.zeros(n), where=prior_count &gt; <span class="num">0</span>)
prior_var = np.divide(cum_sum_sq, prior_count, out=np.zeros(n), where=prior_count &gt; <span class="num">0</span>) - prior_mean ** <span class="num">2</span>
prior_var = np.clip(prior_var, a_min=<span class="num">0</span>, a_max=<span class="num">None</span>)
prior_std = np.sqrt(prior_var)

<span class="cm"># Require at least 3 prior transactions before computing statistical z-score</span>
amount_zscore = np.where(
    prior_count &gt;= <span class="num">3</span>,
    (amounts - prior_mean) / np.where(prior_std &gt; <span class="num">1e-6</span>, prior_std, <span class="num">1.0</span>),
    <span class="num">0.0</span>
)</code></pre>
<p>
  <strong>Architectural Rationale:</strong> The z-score quantifies how anomalous the current purchase amount is relative to the customer's typical spending. Requiring <code>prior_count &gt;= 3</code> avoids calculating volatile standard deviations on sample sizes of one or two purchases, outputting a safe neutral <code>0.0</code> until an established pattern emerges.
</p>

<h3>5.4.4 <code>ml/evaluation/policy.py</code>: The 5-Rule Cascade</h3>
<p>
  The policy engine evaluates rules in strict order, with the first match determining the action:
</p>
<pre><code><span class="cm"># ml/evaluation/policy.py (lines 50-98)</span>
POLICY_RULES = [
    PolicyRule(
        rule_id=<span class="str">"CRITICAL_BLOCK"</span>,
        action=<span class="str">"BLOCK"</span>,
        reason=<span class="str">"Fraud probability &gt;= 0.80 where validation precision is 94.1%."</span>,
        condition=<span class="kw">lambda</span> p, amt: p &gt;= CRITICAL_MIN,  <span class="cm"># 0.80</span>
    ),
    PolicyRule(
        rule_id=<span class="str">"HIGH_STEP_UP"</span>,
        action=<span class="str">"STEP_UP_VERIFICATION"</span>,
        reason=<span class="str">"Fraud probability &gt;= 0.40 (cost-optimal decision threshold)."</span>,
        condition=<span class="kw">lambda</span> p, amt: p &gt;= DECISION_THRESHOLD,  <span class="cm"># 0.40</span>
    ),
    PolicyRule(
        rule_id=<span class="str">"MEDIUM_AMOUNT_ESCALATION"</span>,
        action=<span class="str">"STEP_UP_VERIFICATION"</span>,
        reason=<span class="str">"Probability elevated (&gt;=0.15) and amount &gt;= Rs25,000."</span>,
        condition=<span class="kw">lambda</span> p, amt: p &gt;= LOW_MAX <span class="kw">and</span> amt &gt;= LARGE_AMOUNT_CUTOFF,
    ),
    PolicyRule(
        rule_id=<span class="str">"MEDIUM_MONITOR"</span>,
        action=<span class="str">"ALLOW_WITH_MONITORING"</span>,
        reason=<span class="str">"Probability elevated (&gt;=0.15) but below decision threshold."</span>,
        condition=<span class="kw">lambda</span> p, amt: p &gt;= LOW_MAX,
    ),
    PolicyRule(
        rule_id=<span class="str">"LOW_ALLOW"</span>,
        action=<span class="str">"ALLOW"</span>,
        reason=<span class="str">"Fraud probability &lt; 0.15; zero friction warranted."</span>,
        condition=<span class="kw">lambda</span> p, amt: <span class="num">True</span>,  <span class="cm"># catch-all</span>
    ),
]</code></pre>
<p>
  <strong>Architectural Rationale:</strong> The signature of <code>evaluate_policy(probability: float, amount: float)</code> is structurally incapable of accepting SHAP explanations. This ensures that SHAP explanations can never subtly alter transaction decisions, guaranteeing auditable compliance.
</p>

<h3>5.4.5 <code>backend/services/risk_service.py</code>: V2 Production Hardening</h3>
<p>
  In V2, defensive guardrails intercept inputs and model outputs before downstream consumers are invoked:
</p>
<pre><code><span class="cm"># backend/services/risk_service.py (lines 133-159)</span>
<span class="kw">def</span> <span class="fn">_validate_model_probability</span>(probability: float) -&gt; float:
    <span class="kw">if</span> math.isnan(probability):
        <span class="kw">raise</span> ModelOutputError(<span class="str">"Model produced NaN probability; prediction invalid."</span>)
    <span class="kw">if</span> math.isinf(probability):
        <span class="kw">raise</span> ModelOutputError(f<span class="str">"Model produced infinite probability ({{probability}})."</span>)
    <span class="kw">if not</span> (<span class="num">0.0</span> &lt;= probability &lt;= <span class="num">1.0</span>):
        <span class="kw">raise</span> ModelOutputError(f<span class="str">"Probability out of range ({{probability}}); must be in [0, 1]."</span>)
    <span class="kw">return</span> probability</code></pre>
<p>
  Similarly, <code>_validate_engineered_features()</code> checks that <code>velocity_60min &lt;= 1000</code> and <code>amount_zscore</code> is finite, catching corrupt data (such as 500 identical synthetic transactions submitted in a single millisecond) before LightGBM performs out-of-distribution inference.
</p>

<h2 id="sec-5-5">5.5 File Dependency &amp; Runtime Execution Graph</h2>
<table>
  <thead>
    <tr>
      <th>Origin Module</th>
      <th>Import Dependencies (Static)</th>
      <th>Runtime Call Relationship (Dynamic)</th>
      <th>Data Transferred</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>backend/main.py</code></td>
      <td><code>settings</code>, <code>model_loader</code>, <code>audit_service</code>, <code>routes</code></td>
      <td>Executes <code>load_model_bundle()</code> and initializes <code>AuditStore</code>.</td>
      <td>Instantiates <code>app.state.model_bundle</code> and <code>audit_store</code>.</td>
    </tr>
    <tr>
      <td><code>backend/api/routes.py</code></td>
      <td><code>schemas</code>, <code>risk_service</code>, <code>audit_service</code>, <code>decision_engine</code></td>
      <td>Calls <code>risk_service.evaluate_full()</code> and <code>audit_store.record_decision()</code>.</td>
      <td>Transfers validated <code>RiskRequest</code>; returns <code>RiskEvaluateResponse</code>.</td>
    </tr>
    <tr>
      <td><code>backend/services/risk_service.py</code></td>
      <td><code>build_features</code>, <code>explainability</code>, <code>decision_engine</code>, <code>policy</code></td>
      <td>Calls <code>build_features()</code>, <code>predict_proba()</code>, <code>make_decision()</code>, <code>explain()</code>.</td>
      <td>Marshals raw dicts &rarr; DataFrame &rarr; float probability &rarr; <code>DecisionRecord</code>.</td>
    </tr>
    <tr>
      <td><code>ml/evaluation/decision_engine.py</code></td>
      <td><code>policy</code>, <code>risk_scoring</code></td>
      <td>Calls <code>score_transaction(prob)</code> and <code>evaluate_policy(prob, amt)</code>.</td>
      <td>Packages pure numeric outputs into an immutable <code>DecisionRecord</code>.</td>
    </tr>
    <tr>
      <td><code>backend/services/audit_service.py</code></td>
      <td><code>sqlalchemy</code>, <code>json</code>, <code>sqlite3</code></td>
      <td>Executes SQLite PRAGMA table info; inserts <code>AuditLogEntry</code> into <code>audit.db</code>.</td>
      <td>Persists decision facts and serialized JSON SHAP strings.</td>
    </tr>
  </tbody>
</table>
'''
