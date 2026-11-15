"""
Section 7 — The Complete Project Pipeline: Stage-by-Stage generator.
"""

def get_section7_html(pipeline_svg, threshold_chart_base64):
    return f'''
<div class="page-break"></div>
<h1 id="section-7"><span class="section-number">7</span> THE COMPLETE PROJECT PIPELINE: STAGE BY STAGE</h1>

<h2 id="sec-7-0">7.0 Execution Pipeline Overview</h2>
<p>
  The MerchantShield AI operational pipeline executes as a continuous, nine-stage sequence from the initial bootstrapping of the server environment through request ingestion, feature generation, inference, explainability, policy decisioning, audit logging, and response synthesis.
</p>

<div class="diagram-container">
  {pipeline_svg}
  <div class="diagram-caption">Figure 7.1: The Nine-Stage MerchantShield AI Execution Pipeline.</div>
</div>

<!-- ========================================================================= -->
<!-- STAGE 1 -->
<!-- ========================================================================= -->
<div class="stage-card" id="sec-7-1">
  <div class="stage-header">STAGE 1 — System Bootstrapping &amp; Model Loading</div>
  <div class="stage-body">
    <div class="stage-field">
      <div class="stage-field-label">1. Purpose</div>
      <div class="stage-field-content">
        Loads the pre-trained, frozen LightGBM model artifact, parses its associated evaluation metadata, constructs the in-memory SHAP TreeExplainer, and establishes the SQLite audit database connection once at server startup. Eliminates expensive per-request disk I/O and tree parsing overhead during live transaction scoring.
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">2. Trigger</div>
      <div class="stage-field-content">
        Triggered when Uvicorn initializes the FastAPI process (<code>python -m uvicorn backend.main:app</code>) via the asynchronous <code>lifespan</code> context manager.
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">3. Input</div>
      <div class="stage-field-content">
        Path strings defined in <code>backend/config/settings.py</code>:
        <ul>
          <li><code>MODEL_PATH = "ml/models/candidate_lgbm_v1.pkl"</code> (Binary joblib serialization)</li>
          <li><code>MODEL_METADATA_PATH = "ml/models/lgbm_v1_metadata.json"</code> (JSON metadata file)</li>
          <li><code>AUDIT_DB_URL = "sqlite:///backend/data/audit.db"</code> (SQLite connection URI)</li>
        </ul>
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">4. Processing</div>
      <div class="stage-field-content">
        <ol>
          <li>Validates existence of <code>candidate_lgbm_v1.pkl</code> and loads the LightGBM classifier into memory using <code>joblib.load()</code>.</li>
          <li>Validates that the unpickled object exposes a callable <code>predict_proba</code> method.</li>
          <li>Loads and parses <code>lgbm_v1_metadata.json</code>, verifying the presence of <code>selected_threshold: 0.40</code> and validation metrics.</li>
          <li>Initializes a warm <code>shap.TreeExplainer(model)</code> instance pre-indexed against the LightGBM tree structures.</li>
          <li>Wraps model, explainer, and metadata into a singleton <code>ModelBundle</code> attached to <code>app.state.model_bundle</code>.</li>
          <li>Instantiates <code>AuditStore</code>, creates the <code>audit_log</code> table if missing, and executes idempotent SQLite schema migrations.</li>
        </ol>
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">5. Respective Files</div>
      <div class="stage-field-content">
        <ul>
          <li><code>backend/main.py</code> (lines 32–54, <code>lifespan()</code>)</li>
          <li><code>backend/services/model_loader.py</code> (lines 25–65, <code>load_model_bundle()</code> and <code>ModelBundle</code>)</li>
          <li><code>backend/services/audit_service.py</code> (lines 65–77, <code>AuditStore.__init__()</code>)</li>
        </ul>
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">6. Detailed Code Explanation</div>
      <div class="stage-field-content">
        In <code>backend/services/model_loader.py</code>:
<pre><code><span class="kw">def</span> <span class="fn">load_model_bundle</span>(model_path: str, metadata_path: str) -&gt; ModelBundle:
    <span class="kw">if not</span> os.path.exists(model_path):
        <span class="kw">raise</span> ModelUnavailableError(f<span class="str">"Model artifact not found at {{model_path}}"</span>)
    <span class="kw">try</span>:
        model = joblib.load(model_path)
    <span class="kw">except</span> Exception <span class="kw">as</span> e:
        <span class="kw">raise</span> ModelUnavailableError(f<span class="str">"Model artifact corrupt: {{e}}"</span>) <span class="kw">from</span> e

    <span class="kw">if not</span> hasattr(model, <span class="str">"predict_proba"</span>):
        <span class="kw">raise</span> ModelUnavailableError(<span class="str">"Loaded object does not look like a classifier"</span>)

    <span class="kw">with</span> open(metadata_path) <span class="kw">as</span> f:
        metadata = json.load(f)

    explainer = RiskExplainer(model)  <span class="cm"># Inits shap.TreeExplainer</span>
    <span class="kw">return</span> ModelBundle(model=model, explainer=explainer, metadata=metadata, model_path=model_path)</code></pre>
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">7. Output</div>
      <div class="stage-field-content">
        <code>app.state.model_bundle</code> containing ready-to-serve in-memory models and <code>app.state.audit_store</code> connected to the local database.
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">8. Next Stage</div>
      <div class="stage-field-content">
        The application enters the listening state on port 8000, ready for Stage 2 (Request Reception).
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">9. Failure Cases</div>
      <div class="stage-field-content">
        If the pickle is missing or corrupt, <code>ModelUnavailableError</code> is caught in <code>lifespan()</code>. The process <em>does not crash</em>; it sets <code>app.state.model_bundle = None</code>. The <code>/health</code> endpoint serves <code>status: "degraded", model_loaded: false</code>, allowing monitoring tools to detect the degradation, while scoring endpoints reject requests with HTTP 503 Service Unavailable.
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">10. Conceptual Lesson</div>
      <div class="stage-field-content">
        <strong>Fail-Open Liveness vs. Fail-Closed Traffic:</strong> Server processes should not abruptly crash when optional dependencies or model files fail to load. By coming up degraded, the service maintains network liveness, reports its internal state via telemetry endpoints, and prevents orchestrator cascading restart storms.
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">11. Stage Recap</div>
      <div class="stage-field-content">
        Initializes in-memory model, explainer, and database singletons exactly once, ensuring sub-50ms inference without per-request disk initialization.
      </div>
    </div>
  </div>
</div>

<!-- ========================================================================= -->
<!-- STAGE 2 -->
<!-- ========================================================================= -->
<div class="stage-card" id="sec-7-2">
  <div class="stage-header">STAGE 2 — Request Reception &amp; Strict Shape Validation</div>
  <div class="stage-body">
    <div class="stage-field">
      <div class="stage-field-label">1. Purpose</div>
      <div class="stage-field-content">
        Intercepts incoming HTTP POST requests, deserializes the JSON body, and validates data types, non-blank constraints, and temporal chronological integrity. Prevents corrupt data or future-leakage payloads from reaching the machine learning pipeline.
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">2. Trigger</div>
      <div class="stage-field-content">
        Triggered when an external client (checkout page or React dashboard) submits an HTTP POST request to <code>/risk/evaluate</code>, <code>/risk/score</code>, or <code>/risk/explain</code>.
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">3. Input</div>
      <div class="stage-field-content">
        Raw JSON payload matching the <code>RiskRequest</code> structure:
<pre><code>{{
  "transaction": {{
    "transaction_id": "txn_live_test_001",
    "customer_id": "cust_00042",
    "merchant_id": "merch_0099",
    "merchant_category": "electronics",
    "timestamp": "2026-05-20T10:05:00Z",
    "amount": 45000.0,
    "device_id": "dev_BRAND_NEW",
    "geo_region": "region_19",
    "payment_method": "card",
    "status": "success",
    "account_created": "2025-01-01T00:00:00Z"
  }},
  "prior_transactions": [ /* Array of 0 to 500 prior transactions */ ],
  "source": "manual"
}}</code></pre>
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">4. Processing</div>
      <div class="stage-field-content">
        <ol>
          <li>FastAPI checks router mapping and verifies that the model bundle is loaded (throws HTTP 503 if <code>bundle is None</code>).</li>
          <li>Pydantic validates fields: <code>amount &gt; 0</code> and <code>amount &le; 10,000,000</code>; string fields non-empty and trimmed.</li>
          <li>Asserts <code>account_created &le; timestamp</code> (a user cannot execute a purchase before their account existed).</li>
          <li>Iterates through <code>prior_transactions</code>, verifying:
            <ul>
              <li><code>prior.customer_id == transaction.customer_id</code> (history belongs to the same user).</li>
              <li><code>prior.timestamp &lt; transaction.timestamp</code> (strictly before current event; prevents future leakage).</li>
              <li><code>prior.transaction_id != transaction.transaction_id</code> (a transaction cannot be its own prior history).</li>
            </ul>
          </li>
        </ol>
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">5. Respective Files</div>
      <div class="stage-field-content">
        <ul>
          <li><code>backend/api/routes.py</code> (lines 100–103, <code>risk_evaluate()</code>)</li>
          <li><code>backend/schemas/transaction.py</code> (lines 20–53, <code>TransactionInput</code>; lines 55–101, <code>RiskRequest</code>)</li>
        </ul>
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">6. Detailed Code Explanation</div>
      <div class="stage-field-content">
        Pydantic executes the <code>_account_created_not_after_transaction</code> model validator and then verifies prior history boundaries:
<pre><code><span class="cm"># backend/schemas/transaction.py</span>
<span class="kw">if</span> prior.timestamp &gt;= txn.timestamp:
    <span class="kw">raise</span> ValueError(
        f<span class="str">"prior_transactions[{{i}}].timestamp ({{prior.timestamp}}) is not strictly "</span>
        f<span class="str">"before transaction.timestamp ({{txn.timestamp}}) -- feeding same-or-future "</span>
        f<span class="str">"transactions as 'prior' context would leak information."</span>
    )</code></pre>
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">7. Output</div>
      <div class="stage-field-content">
        A strongly-typed, fully validated <code>RiskRequest</code> Python object instance.
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">8. Next Stage</div>
      <div class="stage-field-content">
        Passed to <code>backend/services/risk_service.py</code> for Stage 3 (Feature Engineering).
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">9. Failure Cases</div>
      <div class="stage-field-content">
        If validation fails, <code>validation_exception_handler()</code> in <code>main.py</code> intercepts the <code>RequestValidationError</code>, sanitizes the error list, and returns a clean HTTP 422 Unprocessable Entity response:
<pre><code>{{"error": "validation_error", "detail": "transaction.amount: Input should be greater than 0"}}</code></pre>
        No Python stack trace is ever leaked to the client.
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">10. Conceptual Lesson</div>
      <div class="stage-field-content">
        <strong>Defensive Boundary Parsing:</strong> Never permit raw dictionary input to penetrate business logic. Validating types, shapes, and domain rules at the outermost network perimeter protects inner statistical engines from undefined behavior.
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">11. Stage Recap</div>
      <div class="stage-field-content">
        Enforces strict request typing, positive amounts, and chronological integrity, rejecting corrupt data with HTTP 422 before feature execution.
      </div>
    </div>
  </div>
</div>

<!-- ========================================================================= -->
<!-- STAGE 3 -->
<!-- ========================================================================= -->
<div class="stage-card" id="sec-7-3">
  <div class="stage-header">STAGE 3 — Leakage-Safe Feature Engineering</div>
  <div class="stage-body">
    <div class="stage-field">
      <div class="stage-field-label">1. Purpose</div>
      <div class="stage-field-content">
        Transforms the raw transaction record and its historical sequence into a single 15-dimensional numeric feature vector. Ensures that all behavioral and velocity features are computed strictly from events preceding the current transaction timestamp.
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">2. Trigger</div>
      <div class="stage-field-content">
        Invoked by <code>risk_service._build_feature_row(request)</code> when processing scoring requests.
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">3. Input</div>
      <div class="stage-field-content">
        A combined raw DataFrame containing the prior history rows concatenated with the current transaction row:
<pre><code>all_txns = list(request.prior_transactions) + [request.transaction]
raw_df = pd.DataFrame([t.model_dump() for t in all_txns])</code></pre>
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">4. Processing</div>
      <div class="stage-field-content">
        Executes the exact, unmodified <code>build_features()</code> function from <code>ml/features/build_features.py</code>:
        <ol>
          <li>Sorts rows chronologically by <code>timestamp</code> for the customer.</li>
          <li>Computes running cumulative sums and squared sums shifted by one index (<code>[:-1]</code>).</li>
          <li>Calculates <code>prior_mean</code>, <code>prior_std</code>, <code>amount_zscore</code>, and <code>amount_vs_avg_ratio</code>.</li>
          <li>Calculates <code>time_since_prev_txn_min</code> (using sentinel <code>99999.0</code> for first transactions).</li>
          <li>Executes two-pointer sliding windows to count prior events within 5-minute, 30-minute, and 60-minute windows.</li>
          <li>Maintains historical sets to flag <code>new_device_flag</code> and <code>new_geo_flag</code> (defaulting to 0 for initial transactions).</li>
          <li>Calculates <code>failed_ratio_trailing10</code> across the preceding 10 transactions.</li>
          <li>Extracts cyclical calendar features: <code>hour_of_day</code>, <code>is_night</code> (hours 0–4), and <code>day_of_week</code>.</li>
        </ol>
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">5. Respective Files</div>
      <div class="stage-field-content">
        <ul>
          <li><code>backend/services/risk_service.py</code> (lines 162–199, <code>_build_feature_row()</code>)</li>
          <li><code>ml/features/build_features.py</code> (lines 25–142, <code>build_features()</code> and <code>FEATURE_COLUMNS</code>)</li>
        </ul>
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">6. Detailed Code Explanation</div>
      <div class="stage-field-content">
        Extracts the single row corresponding to the transaction being scored:
<pre><code><span class="cm"># backend/services/risk_service.py</span>
features_df = build_features(raw_df)
match = features_df[features_df[<span class="str">"transaction_id"</span>] == request.transaction.transaction_id]
<span class="kw">if</span> len(match) != <span class="num">1</span>:
    <span class="kw">raise</span> FeatureGenerationError(f<span class="str">"Expected exactly 1 row for transaction, got {{len(match)}}"</span>)
row = match.iloc[<span class="num">0</span>]</code></pre>
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">7. Output</div>
      <div class="stage-field-content">
        A single <code>pandas.Series</code> (<code>row</code>) containing the 15 numeric values corresponding to <code>FEATURE_COLUMNS</code>.
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">8. Next Stage</div>
      <div class="stage-field-content">
        Passed to Stage 4 (Feature Bounds Checking &amp; V2 Hardening).
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">9. Failure Cases</div>
      <div class="stage-field-content">
        If pandas throws an unexpected grouping or type error, <code>FeatureGenerationError</code> is raised and translated by the route handler into an HTTP 422 error.
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">10. Conceptual Lesson</div>
      <div class="stage-field-content">
        <strong>Temporal Invariance in Time-Series Features:</strong> A feature engineering function must be mathematically incapable of peeking ahead. By enforcing shifting logic in cumulative sums, offline backtesting and live online inference execute under identical mathematical guarantees.
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">11. Stage Recap</div>
      <div class="stage-field-content">
        Extracts 15 strictly-prior behavioral and velocity features without future leakage, matching offline training logic exactly.
      </div>
    </div>
  </div>
</div>

<!-- ========================================================================= -->
<!-- STAGE 4 -->
<!-- ========================================================================= -->
<div class="stage-card" id="sec-7-4">
  <div class="stage-header">STAGE 4 — Feature Bounds Checking &amp; V2 Hardening</div>
  <div class="stage-body">
    <div class="stage-field">
      <div class="stage-field-label">1. Purpose</div>
      <div class="stage-field-content">
        V2 defensive sanity checking: verifies that engineered features fall within defensible physical domain bounds before being fed into the gradient-boosted decision trees. Catches pathological inputs that could cause out-of-distribution model instability.
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">2. Trigger</div>
      <div class="stage-field-content">
        Called within <code>_build_feature_row()</code> via <code>_validate_engineered_features(row)</code> prior to returning the feature series.
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">3. Input</div>
      <div class="stage-field-content">
        The engineered feature <code>pandas.Series</code> generated in Stage 3.
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">4. Processing</div>
      <div class="stage-field-content">
        Evaluates physical domain boundaries:
        <ul>
          <li><code>velocity_60min &le; 1000</code> (normal rate is ~1 txn/min; &gt;1000 txns in an hour indicates malformed history).</li>
          <li><code>velocity_30min &le; 500</code> and <code>velocity_5min &le; 100</code>.</li>
          <li><code>prior_txn_count &le; 100,000</code>.</li>
          <li><code>np.isfinite(amount_zscore)</code> (checks strictly for NaN/Inf; allows legitimately extreme z-scores like 20+).</li>
          <li><code>time_since_prev_txn_min &le; 100,000</code> (sentinel 99999.0 + buffer).</li>
        </ul>
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">5. Respective Files</div>
      <div class="stage-field-content">
        <code>backend/services/risk_service.py</code> (lines 39–92, <code>_validate_engineered_features()</code>)
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">6. Detailed Code Explanation</div>
      <div class="stage-field-content">
<pre><code><span class="cm"># backend/services/risk_service.py</span>
<span class="kw">if</span> row.get(<span class="str">"velocity_60min"</span>, <span class="num">0</span>) &gt; <span class="num">1000</span>:
    <span class="kw">raise</span> FeatureGenerationError(
        f<span class="str">"Feature velocity_60min={{row['velocity_60min']}} exceeds sanity bound (1000). "</span>
        f<span class="str">"Suggests malformed transaction history (e.g. identical timestamps)."</span>
    )
<span class="kw">if not</span> np.isfinite(row.get(<span class="str">"amount_zscore"</span>, <span class="num">0</span>)):
    <span class="kw">raise</span> FeatureGenerationError(<span class="str">"Feature amount_zscore is non-finite (NaN or Inf)."</span>)</code></pre>
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">7. Output</div>
      <div class="stage-field-content">
        Execution completes silently if valid; returns control to caller.
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">8. Next Stage</div>
      <div class="stage-field-content">
        Proceeds to Stage 5 (LightGBM Model Inference).
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">9. Failure Cases</div>
      <div class="stage-field-content">
        Raises <code>FeatureGenerationError</code>, which routes to an HTTP 422 response detailing the exact sanity boundary breach.
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">10. Conceptual Lesson</div>
      <div class="stage-field-content">
        <strong>Domain Bound Invariants:</strong> Tree-based models are step-function estimators that cannot extrapolate outside their training support. Guarding input feature distributions prevents erratic leaf routing under pathological input conditions.
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">11. Stage Recap</div>
      <div class="stage-field-content">
        Validates engineered features against physical domain bounds (velocity caps, finite z-scores) before model scoring.
      </div>
    </div>
  </div>
</div>

<!-- ========================================================================= -->
<!-- STAGE 5 -->
<!-- ========================================================================= -->
<div class="stage-card" id="sec-7-5">
  <div class="stage-header">STAGE 5 — LightGBM Model Inference &amp; Output Hardening</div>
  <div class="stage-body">
    <div class="stage-field">
      <div class="stage-field-label">1. Purpose</div>
      <div class="stage-field-content">
        Executes gradient-boosted decision tree inference to estimate the fraud probability P(fraud) &isin; [0.0, 1.0]. Hardens the output against non-finite values (NaN/Inf) and out-of-range floats before downstream consumption.
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">2. Trigger</div>
      <div class="stage-field-content">
        Invoked by <code>risk_service.evaluate_full()</code> (or <code>score_only()</code>).
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">3. Input</div>
      <div class="stage-field-content">
        A 1&times;15 numeric <code>pandas.DataFrame</code> (<code>X</code>) extracted from <code>row[FEATURE_COLUMNS]</code>.
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">4. Processing</div>
      <div class="stage-field-content">
        <ol>
          <li>Calls <code>bundle.model.predict_proba(X)</code> on the frozen LightGBM artifact.</li>
          <li>Extracts positive class probability at column index 1: <code>raw_prob = float(proba[0, 1])</code>.</li>
          <li>Executes V2 hardening validation via <code>_validate_model_probability(raw_prob)</code>:
            <ul>
              <li>Checks <code>math.isnan(p)</code>.</li>
              <li>Checks <code>math.isinf(p)</code>.</li>
              <li>Checks <code>0.0 &le; p &le; 1.0</code>.</li>
            </ul>
          </li>
          <li>Calculates informational 0–100 risk score and category via <code>score_transaction(probability)</code>.</li>
        </ol>
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">5. Respective Files</div>
      <div class="stage-field-content">
        <ul>
          <li><code>backend/services/risk_service.py</code> (lines 133–160, <code>_validate_model_probability()</code>; lines 282–285)</li>
          <li><code>ml/evaluation/risk_scoring.py</code> (lines 30–51, <code>score_transaction()</code>)</li>
        </ul>
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">6. Detailed Code Explanation</div>
      <div class="stage-field-content">
<pre><code><span class="cm"># backend/services/risk_service.py</span>
X = pd.DataFrame([row[FEATURE_COLUMNS].astype(float).values], columns=FEATURE_COLUMNS)
raw_probability = float(bundle.model.predict_proba(X)[<span class="num">0</span>, <span class="num">1</span>])
probability = _validate_model_probability(raw_probability)</code></pre>
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">7. Output</div>
      <div class="stage-field-content">
        Validated float <code>probability</code> (e.g., <code>0.9997</code>) and informational dictionary <code>{{risk_score: 100, risk_category: "CRITICAL"}}</code>.
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">8. Next Stage</div>
      <div class="stage-field-content">
        Control bifurcates into two independent branches: Stage 6 (SHAP Explainability) and Stage 7 (Policy Evaluation).
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">9. Failure Cases</div>
      <div class="stage-field-content">
        If the model outputs NaN or Inf, <code>ModelOutputError</code> is raised, returning HTTP 422 to prevent corrupt probabilities from reaching financial policy.
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">10. Conceptual Lesson</div>
      <div class="stage-field-content">
        <strong>Trust Boundaries at Model Interfaces:</strong> Never assume a machine learning model's numerical outputs are guaranteed to be well-formed floats. Hardware errors, corrupt tree weights, or unexpected inputs can emit NaNs; verifying outputs protects downstream systems.
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">11. Stage Recap</div>
      <div class="stage-field-content">
        Generates raw fraud probability via LightGBM inference and validates finiteness before policy consumption.
      </div>
    </div>
  </div>
</div>

<!-- ========================================================================= -->
<!-- STAGE 6 -->
<!-- ========================================================================= -->
<div class="stage-card" id="sec-7-6">
  <div class="stage-header">STAGE 6 — Grounded SHAP Explainability &amp; Additivity Verification</div>
  <div class="stage-body">
    <div class="stage-field">
      <div class="stage-field-label">1. Purpose</div>
      <div class="stage-field-content">
        Decomposes the model's raw prediction into exact per-feature Shapley contributions, verifies mathematical additivity, filters history-dependent features for cold-start scenarios, and generates human-readable narratives.
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">2. Trigger</div>
      <div class="stage-field-content">
        Called via <code>bundle.explainer.explain(row)</code> and <code>build_explanation_text()</code> in <code>risk_service.py</code>.
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">3. Input</div>
      <div class="stage-field-content">
        The engineered <code>pandas.Series</code> (<code>row</code>), the frozen decision threshold (<code>0.40</code>), and <code>is_cold_start</code> boolean flag.
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">4. Processing</div>
      <div class="stage-field-content">
        <ol>
          <li>Computes Shapley values using <code>shap.TreeExplainer</code> in margin (log-odds) space.</li>
          <li>Extracts <code>base_value</code> and feature contribution array <code>sv</code>.</li>
          <li><strong>Verifies Additivity:</strong> Reconstructs probability:
            <pre><code>margin = base_value + np.sum(sv)
reconstructed_prob = 1.0 / (1.0 + np.exp(-margin))
additivity_ok = abs(reconstructed_prob - raw_prob) &lt; 1e-4</code></pre>
          </li>
          <li>Sorts contributions by absolute magnitude (<code>abs(shap_value)</code>).</li>
          <li><strong>Cold-Start Filtering:</strong> If <code>prior_txn_count == 0</code>, filters out history-dependent features (rolling averages, z-scores) from the top reasons pool.</li>
          <li>Formats grounded explanation sentences using deterministic templates in <code>ml/evaluation/explainability.py</code>.</li>
        </ol>
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">5. Respective Files</div>
      <div class="stage-field-content">
        <code>ml/evaluation/explainability.py</code> (lines 84–170, <code>RiskExplainer.explain()</code>; lines 182–245, <code>build_explanation_text()</code>; lines 247–270, <code>humanize_contribution()</code>)
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">6. Detailed Code Explanation</div>
      <div class="stage-field-content">
        Grounding template execution without hallucination:
<pre><code><span class="cm"># ml/evaluation/explainability.py</span>
_TEMPLATES = {{
    <span class="str">"amount_vs_avg_ratio"</span>: <span class="kw">lambda</span> v, s: (
        f<span class="str">"Transaction amount is {{v:.1f}}x the customer's historical average amount, "</span>
        f<span class="str">"which {{_direction_word(s)}} risk"</span>
    ),
    <span class="str">"new_device_flag"</span>: <span class="kw">lambda</span> v, s: (
        <span class="str">"Device has not been seen previously for this customer, which increased risk"</span> <span class="kw">if</span> v == <span class="num">1</span>
        <span class="kw">else</span> <span class="str">"Device has been used previously by this customer, which decreased risk"</span>
    ),
}}</code></pre>
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">7. Output</div>
      <div class="stage-field-content">
        Structured dictionary containing:
        <ul>
          <li><code>additivity_check_passed: true</code></li>
          <li><code>header: "Why this transaction was flagged:"</code></li>
          <li><code>reasons: [ "Transaction amount is 85.7x historical average...", ... ]</code></li>
          <li><code>contributions: [ {{ feature, value, shap_value, direction, magnitude }}, ... ]</code></li>
        </ul>
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">8. Next Stage</div>
      <div class="stage-field-content">
        Attached alongside the decision record for Stage 8 (Audit Persistence) and Stage 9 (Response Delivery).
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">9. Failure Cases</div>
      <div class="stage-field-content">
        If SHAP fails due to memory exhaustion or version mismatch, the exception is caught in <code>evaluate_full()</code>. <strong>The risk decision is preserved</strong>, and the response marks <code>explanation_available: false</code> with <code>explanation_header: "Explanation generation failed"</code>.
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">10. Conceptual Lesson</div>
      <div class="stage-field-content">
        <strong>Mathematical Additivity &amp; Grounding:</strong> Shapley values satisfy the efficiency property—contributions sum to the difference between prediction and expected value. Verifying additivity mathematically proves that the explanation truthfully represents the model.
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">11. Stage Recap</div>
      <div class="stage-field-content">
        Computes grounded feature attributions with additivity verification, providing audit transparency without influencing the action.
      </div>
    </div>
  </div>
</div>

<!-- ========================================================================= -->
<!-- STAGE 7 -->
<!-- ========================================================================= -->
<div class="stage-card" id="sec-7-7">
  <div class="stage-header">STAGE 7 — Deterministic Policy Evaluation &amp; Action Bounding</div>
  <div class="stage-body">
    <div class="stage-field">
      <div class="stage-field-label">1. Purpose</div>
      <div class="stage-field-content">
        Converts the raw fraud probability and transaction amount into a bounded, deterministic operational action recommendation using a transparent five-rule priority cascade.
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">2. Trigger</div>
      <div class="stage-field-content">
        Invoked by <code>make_decision()</code> in <code>ml/evaluation/decision_engine.py</code>.
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">3. Input</div>
      <div class="stage-field-content">
        <code>transaction_id: str</code>, <code>model_probability: float</code>, <code>amount: float</code>.
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">4. Processing</div>
      <div class="stage-field-content">
        <ol>
          <li>Re-validates probability (numeric, non-bool, in [0, 1]) and amount (numeric, non-negative).</li>
          <li>Calls <code>evaluate_policy(probability, amount)</code>:
            <ul>
              <li>Checks Rule 1: <code>probability &ge; 0.80</code> &rarr; <code>CRITICAL_BLOCK</code> (<code>BLOCK</code>).</li>
              <li>Checks Rule 2: <code>probability &ge; 0.40</code> &rarr; <code>HIGH_STEP_UP</code> (<code>STEP_UP_VERIFICATION</code>).</li>
              <li>Checks Rule 3: <code>probability &ge; 0.15</code> and <code>amount &ge; 25,000</code> &rarr; <code>MEDIUM_AMOUNT_ESCALATION</code> (<code>STEP_UP_VERIFICATION</code>).</li>
              <li>Checks Rule 4: <code>probability &ge; 0.15</code> &rarr; <code>MEDIUM_MONITOR</code> (<code>ALLOW_WITH_MONITORING</code>).</li>
              <li>Checks Rule 5: Catch-all &rarr; <code>LOW_ALLOW</code> (<code>ALLOW</code>).</li>
            </ul>
          </li>
          <li>Asserts that the produced action is a member of <code>ALLOWED_ACTIONS</code>.</li>
          <li>Packages results into an immutable <code>DecisionRecord</code>.</li>
        </ol>
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">5. Respective Files</div>
      <div class="stage-field-content">
        <ul>
          <li><code>ml/evaluation/policy.py</code> (lines 101–120, <code>evaluate_policy()</code>)</li>
          <li><code>ml/evaluation/decision_engine.py</code> (lines 82–123, <code>make_decision()</code> and <code>DecisionRecord</code>)</li>
        </ul>
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">6. Detailed Code Explanation</div>
      <div class="stage-field-content">
<pre><code><span class="cm"># ml/evaluation/policy.py</span>
<span class="kw">def</span> <span class="fn">evaluate_policy</span>(probability: float, amount: float) -&gt; PolicyRule:
    <span class="kw">for</span> rule <span class="kw">in</span> POLICY_RULES:
        <span class="kw">if</span> rule.condition(probability, amount):
            <span class="kw">if</span> rule.action <span class="kw">not in</span> ALLOWED_ACTIONS:
                <span class="kw">raise</span> RuntimeError(f<span class="str">"Unrecognized action '{{rule.action}}'"</span>)
            <span class="kw">return</span> rule
    <span class="kw">raise</span> RuntimeError(<span class="str">"No policy rule matched. Failing safe."</span>)</code></pre>
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">7. Output</div>
      <div class="stage-field-content">
        An immutable <code>DecisionRecord</code> dataclass instance containing action, rule ID, justification, and timestamp.
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">8. Next Stage</div>
      <div class="stage-field-content">
        Passed to Stage 8 (Audit Persistence).
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">9. Failure Cases</div>
      <div class="stage-field-content">
        If an unrecognized action is produced or no rule matches, a <code>RuntimeError</code> is thrown rather than returning an undefined state, causing the API to return a sanitized HTTP 500.
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">10. Conceptual Lesson</div>
      <div class="stage-field-content">
        <strong>The Separation of Decision and Presentation:</strong> A risk score (0–100) is for human eyes; policy rules must evaluate calibrated probabilities directly. This prevents presentation tweaks from silently mutating financial actions.
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">11. Stage Recap</div>
      <div class="stage-field-content">
        Translates probability and amount into a bounded, auditable operational action via a 5-rule deterministic priority table.
      </div>
    </div>
  </div>
</div>

<!-- ========================================================================= -->
<!-- STAGE 8 -->
<!-- ========================================================================= -->
<div class="stage-card" id="sec-7-8">
  <div class="stage-header">STAGE 8 — Fail-Safe Audit Trail Persistence</div>
  <div class="stage-body">
    <div class="stage-field">
      <div class="stage-field-label">1. Purpose</div>
      <div class="stage-field-content">
        Durably commits the exact decision facts, policy rule, and serialized SHAP reasons to the SQLite audit database while enforcing failure isolation to protect transaction scoring availability.
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">2. Trigger</div>
      <div class="stage-field-content">
        Invoked by the route handler in <code>backend/api/routes.py</code> immediately after <code>evaluate_full()</code> returns.
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">3. Input</div>
      <div class="stage-field-content">
        <code>request_id</code>, <code>decision</code> (DecisionRecord), <code>top_reasons</code> (list of strings), <code>source</code> tag (<code>"demo"</code> | <code>"manual"</code>), and <code>prior_txn_count</code>.
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">4. Processing</div>
      <div class="stage-field-content">
        <ol>
          <li>Opens a SQLAlchemy session bound to <code>sqlite:///backend/data/audit.db</code>.</li>
          <li>Constructs an <code>AuditLogEntry</code> record mapping decision fields.</li>
          <li>Serializes top reasons into JSON format (<code>json.dumps(top_reasons)</code>).</li>
          <li>Executes <code>session.add(entry)</code> and commits the transaction.</li>
          <li>Traps any database I/O exception, executes rollback, and catches <code>AuditPersistenceError</code>.</li>
        </ol>
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">5. Respective Files</div>
      <div class="stage-field-content">
        <ul>
          <li><code>backend/services/audit_service.py</code> (lines 78–110, <code>record_decision()</code>; lines 40–59, <code>AuditLogEntry</code>)</li>
          <li><code>backend/api/routes.py</code> (lines 117–130)</li>
        </ul>
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">6. Detailed Code Explanation</div>
      <div class="stage-field-content">
        Failure isolation pattern in <code>routes.py</code>:
<pre><code><span class="cm"># backend/api/routes.py</span>
audit_persisted = <span class="num">False</span>
audit_error = <span class="num">None</span>
<span class="kw">if</span> audit_store <span class="kw">is not</span> <span class="num">None</span>:
    <span class="kw">try</span>:
        audit_store.record_decision(
            request_id, decision, decision.model_explanation,
            source=payload.source, prior_txn_count=prior_txn_count
        )
        audit_persisted = <span class="num">True</span>
    <span class="kw">except</span> AuditPersistenceError <span class="kw">as</span> e:
        audit_error = str(e)</code></pre>
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">7. Output</div>
      <div class="stage-field-content">
        A durable new row in the SQLite database and boolean flag <code>audit_persisted</code>.
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">8. Next Stage</div>
      <div class="stage-field-content">
        Proceeds to Stage 9 (Response Synthesis &amp; Client Delivery).
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">9. Failure Cases</div>
      <div class="stage-field-content">
        If the disk is read-only or locked, <code>audit_store</code> logs the error and sets <code>audit_persisted = False</code>. The API proceeds without dropping the scoring result.
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">10. Conceptual Lesson</div>
      <div class="stage-field-content">
        <strong>Auxiliary Service Failure Isolation:</strong> Non-critical side-effects (such as telemetry, analytics, or audit logging) must never sit on the critical path in a manner that blocks core revenue operations when they experience transient faults.
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">11. Stage Recap</div>
      <div class="stage-field-content">
        Persists decision facts and serialized SHAP narratives to SQLite without PII, isolated from scoring availability.
      </div>
    </div>
  </div>
</div>

<!-- ========================================================================= -->
<!-- STAGE 9 -->
<!-- ========================================================================= -->
<div class="stage-card" id="sec-7-9">
  <div class="stage-header">STAGE 9 — Response Synthesis &amp; Client Delivery</div>
  <div class="stage-body">
    <div class="stage-field">
      <div class="stage-field-label">1. Purpose</div>
      <div class="stage-field-content">
        Assembles decision records, SHAP reasons, signal quality ratings, and audit persistence status into a strongly-typed Pydantic response, returning HTTP 200 JSON to the client.
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">2. Trigger</div>
      <div class="stage-field-content">
        Concluding return statement in <code>backend/api/routes.py::risk_evaluate()</code>.
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">3. Input</div>
      <div class="stage-field-content">
        The assembled results from Stages 5, 6, 7, and 8.
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">4. Processing</div>
      <div class="stage-field-content">
        <ol>
          <li>Calculates historical context quality via <code>_calculate_signal_quality(prior_txn_count)</code>.</li>
          <li>Instantiates <code>RiskEvaluateResponse</code> with exact typed fields.</li>
          <li>Serializes model into JSON and returns HTTP 200.</li>
          <li>The React dashboard receives the response, updates state, and renders the verbatim action badge.</li>
        </ol>
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">5. Respective Files</div>
      <div class="stage-field-content">
        <ul>
          <li><code>backend/api/routes.py</code> (lines 147–170)</li>
          <li><code>backend/schemas/response.py</code> (lines 48–68, <code>RiskEvaluateResponse</code>)</li>
          <li><code>frontend/src/App.jsx</code> (lines 73–105, <code>handleEvaluate()</code>)</li>
        </ul>
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">6. Detailed Code Explanation</div>
      <div class="stage-field-content">
<pre><code><span class="cm"># backend/api/routes.py</span>
signal_quality = risk_service._calculate_signal_quality(prior_txn_count)
<span class="kw">return</span> RiskEvaluateResponse(
    request_id=request_id,
    transaction_id=decision.transaction_id,
    model_version=decision.model_version,
    fraud_probability=decision.fraud_probability,
    threshold=decision.threshold,
    risk_score=decision.risk_score,
    risk_category=decision.risk_category,
    action=decision.action,
    policy_rule_id=decision.policy_rule_id,
    policy_reason=decision.policy_reason,
    explanation_header=explanation_header,
    reasons=reasons,
    explanation_available=explanation_available,
    cold_start_context=cold_start_context,
    timestamp=decision.timestamp,
    signal_quality=signal_quality,
    prior_transaction_count=prior_txn_count,
    audit_persisted=audit_persisted,
    audit_error=audit_error,
)</code></pre>
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">7. Output</div>
      <div class="stage-field-content">
        JSON response delivered to client over HTTP; rendered in React UI.
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">8. Next Stage</div>
      <div class="stage-field-content">
        Transaction evaluation complete. System waits for next request.
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">9. Failure Cases</div>
      <div class="stage-field-content">
        If network disconnection occurs, the React client catches the fetch error and displays an <code>ErrorBanner</code> without crashing the browser view.
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">10. Conceptual Lesson</div>
      <div class="stage-field-content">
        <strong>Strict Schema Contracts:</strong> A front-end dashboard should never guess backend state or parse unstructured strings. Strongly typed JSON schemas guarantee long-term system stability and cross-team velocity.
      </div>
    </div>
    <div class="stage-field">
      <div class="stage-field-label">11. Stage Recap</div>
      <div class="stage-field-content">
        Synthesizes the complete decision, SHAP attributions, signal quality ratings, and audit status into a typed JSON contract delivered to the client.
      </div>
    </div>
  </div>
</div>

<h2 id="sec-7-10">7.10 Complete Worked End-to-End Execution Trace</h2>
<p>
  To observe how these nine stages collaborate in practice, the table below documents an exact, unedited trace of transaction <code>demo_txn_critical</code> evaluated against the frozen production model:
</p>

<table>
  <thead>
    <tr>
      <th>Pipeline Stage</th>
      <th>Component &amp; Function</th>
      <th>State &amp; Intermediate Values</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Stage 1: Bootstrapping</strong></td>
      <td><code>model_loader.py::load_model_bundle()</code></td>
      <td>Loaded <code>candidate_lgbm_v1.pkl</code> (num_leaves=31, scale_pos_weight=73.2); SQLite connection established.</td>
    </tr>
    <tr>
      <td><strong>Stage 2: Validation</strong></td>
      <td><code>transaction.py::RiskRequest</code></td>
      <td><code>amount = 45000.0</code>; <code>customer_id = "demo_cust_critical"</code>; 8 prior transactions verified (<code>timestamp &lt; current</code>).</td>
    </tr>
    <tr>
      <td><strong>Stage 3: Features</strong></td>
      <td><code>build_features.py::build_features()</code></td>
      <td><code>amount_zscore = 22.4</code>; <code>amount_vs_avg_ratio = 85.7</code>; <code>new_device_flag = 1</code>; <code>new_geo_flag = 1</code>; <code>velocity_60min = 1</code>.</td>
    </tr>
    <tr>
      <td><strong>Stage 4: Bounds Check</strong></td>
      <td><code>risk_service.py::_validate_engineered_features()</code></td>
      <td>Velocity check passed (<code>1 &le; 1000</code>); finite check passed (<code>np.isfinite(22.4) == True</code>).</td>
    </tr>
    <tr>
      <td><strong>Stage 5: Inference</strong></td>
      <td><code>candidate_lgbm_v1.pkl::predict_proba()</code></td>
      <td>Raw margin = +7.82; P(fraud) = 1 / (1 + e<sup>-7.82</sup>) = <strong>0.9997</strong>; Risk Score = <strong>100</strong> (CRITICAL).</td>
    </tr>
    <tr>
      <td><strong>Stage 6: Explainability</strong></td>
      <td><code>explainability.py::explain()</code></td>
      <td><code>base_value = -3.84</code>; &Sigma; shap = +11.66; Reconstructed prob = 0.9997; Additivity check: <strong>PASSED</strong> (|&Delta;| &lt; 0.0001).</td>
    </tr>
    <tr>
      <td><strong>Stage 7: Policy</strong></td>
      <td><code>policy.py::evaluate_policy(0.9997, 45000)</code></td>
      <td>Rule 1 matched: 0.9997 &ge; 0.80; <code>policy_rule_id = "CRITICAL_BLOCK"</code>; Action = <code><b>BLOCK</b></code>.</td>
    </tr>
    <tr>
      <td><strong>Stage 8: Audit</strong></td>
      <td><code>audit_service.py::record_decision()</code></td>
      <td>Row written to <code>backend/data/audit.db</code>; <code>audit_persisted = True</code>; PII omitted.</td>
    </tr>
    <tr>
      <td><strong>Stage 9: Delivery</strong></td>
      <td><code>routes.py &rarr; App.jsx</code></td>
      <td>HTTP 200 returned in 34ms; React dashboard renders Crimson <code>BLOCK</code> badge and SHAP contribution bars.</td>
    </tr>
  </tbody>
</table>

<h3>Validation Set Threshold Analysis Chart</h3>
<p>
  Figure 7.2 displays the actual matplotlib output from Phase 5 (<code>ml/models/threshold_analysis_chart.png</code>), showing precision, recall, F1-score, and total expected rupee cost across the validation threshold sweep:
</p>

<div class="diagram-container">
  <img src="data:image/png;base64,{threshold_chart_base64}" alt="Validation Set Threshold Analysis Plot" style="max-width: 850px;"/>
  <div class="diagram-caption">Figure 7.2: Precision, Recall, F1, and Expected Cost vs. Decision Threshold on the Held-Out Validation Partition (ml/models/threshold_analysis_chart.png). Notice the cost minimum at threshold 0.40.</div>
</div>
'''
