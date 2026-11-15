"""
Section 4 — Tech Stack and Technology Deep Dives generator.
"""

def get_section4_html():
    return '''
<div class="page-break"></div>
<h1 id="section-4"><span class="section-number">4</span> TECH STACK AND WHAT EACH TECHNOLOGY DOES</h1>

<h2 id="sec-4-1">4.1 Master Technology Inventory &amp; Architecture Map</h2>
<p>
  Every technology in MerchantShield AI was selected based on strict requirements of mathematical precision, execution determinism, and minimal operational overhead. The table below inventories every verified dependency across the backend, machine learning, frontend, and DevOps layers:
</p>

<table>
  <thead>
    <tr>
      <th>Technology / Tool</th>
      <th>Verified Version</th>
      <th>Architectural Category</th>
      <th>Primary Role in Repository</th>
      <th>Interacting Components</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Python</strong></td>
      <td><code>3.13</code> (3.11+ req)</td>
      <td>Core Runtime</td>
      <td>Powers the entire backend API, ML training pipelines, feature engineering, and test suites.</td>
      <td>Interprets all backend and ML source code; hosts Uvicorn and pytest.</td>
    </tr>
    <tr>
      <td><strong>NumPy</strong></td>
      <td><code>2.4.4</code></td>
      <td>Scientific Computing</td>
      <td>High-performance vectorized array operations; rolling sums; cumulative variance computations.</td>
      <td><code>ml/features/build_features.py</code>; fed by pandas series; consumed by LightGBM.</td>
    </tr>
    <tr>
      <td><strong>pandas</strong></td>
      <td><code>3.0.2</code></td>
      <td>Data Manipulation</td>
      <td>Dataframe structures for transaction event logs; chronological sorting; customer groupbys.</td>
      <td><code>ml/data/</code>, <code>ml/features/</code>, and <code>backend/services/risk_service.py</code>.</td>
    </tr>
    <tr>
      <td><strong>scikit-learn</strong></td>
      <td><code>1.8.0</code></td>
      <td>Machine Learning Toolkit</td>
      <td>Baseline Logistic Regression; StandardScaler; PR-AUC and ROC-AUC evaluation metrics.</td>
      <td><code>ml/training/train_baseline.py</code> and candidate model benchmarking.</td>
    </tr>
    <tr>
      <td><strong>LightGBM</strong></td>
      <td><code>4.7.0</code></td>
      <td>Gradient Boosted Trees</td>
      <td>The primary production model (<code>candidate_lgbm_v1.pkl</code>); fast, leaf-wise tree inference.</td>
      <td>Trained in <code>ml/training/train_candidates.py</code>; loaded via joblib in <code>model_loader.py</code>.</td>
    </tr>
    <tr>
      <td><strong>SHAP</strong></td>
      <td><code>0.52.0</code></td>
      <td>Model Explainability</td>
      <td><code>TreeExplainer</code> computing exact, grounded Shapley values in log-odds margin space.</td>
      <td><code>ml/evaluation/explainability.py</code>; wraps LightGBM model; supplies API payload.</td>
    </tr>
    <tr>
      <td><strong>SciPy</strong></td>
      <td><code>1.17.1</code></td>
      <td>Advanced Mathematics</td>
      <td>Statistical distribution utilities and mathematical verification algorithms.</td>
      <td>Underpins scikit-learn metrics and model evaluation functions.</td>
    </tr>
    <tr>
      <td><strong>FastAPI</strong></td>
      <td><code>0.141.1</code></td>
      <td>Asynchronous Web API</td>
      <td>High-speed RESTful API gateway; dependency injection; automatic OpenAPI/Swagger generation.</td>
      <td><code>backend/main.py</code> and <code>backend/api/routes.py</code>; orchestrates services.</td>
    </tr>
    <tr>
      <td><strong>Pydantic</strong></td>
      <td><code>2.13.4</code> (v2)</td>
      <td>Data Validation &amp; Typing</td>
      <td>Strict request/response schema validation; field type coercion; chronological validation.</td>
      <td><code>backend/schemas/transaction.py</code> and <code>backend/schemas/response.py</code>.</td>
    </tr>
    <tr>
      <td><strong>SQLAlchemy</strong></td>
      <td><code>2.0.52</code></td>
      <td>ORM &amp; Database Layer</td>
      <td>Object-Relational Mapping for audit log records; schema creation; declarative base models.</td>
      <td><code>backend/services/audit_service.py</code>; communicates with SQLite database.</td>
    </tr>
    <tr>
      <td><strong>SQLite</strong></td>
      <td><code>3.x</code> (embedded)</td>
      <td>Relational Persistence</td>
      <td>Zero-configuration, serverless, single-file relational database for audit trails.</td>
      <td>Stores <code>backend/data/audit.db</code>; managed through SQLAlchemy sessions.</td>
    </tr>
    <tr>
      <td><strong>Uvicorn</strong></td>
      <td><code>0.52.4</code></td>
      <td>ASGI Web Server</td>
      <td>Lightning-fast ASGI web server hosting the FastAPI application process.</td>
      <td>Entry point for <code>python -m uvicorn backend.main:app</code>.</td>
    </tr>
    <tr>
      <td><strong>React</strong></td>
      <td><code>19.2.8</code></td>
      <td>Frontend UI Framework</td>
      <td>Single-page dashboard; dynamic scenario loading; reactive audit log tables and charts.</td>
      <td><code>frontend/src/App.jsx</code> and component hierarchy in <code>frontend/src/components/</code>.</td>
    </tr>
    <tr>
      <td><strong>Vite</strong></td>
      <td><code>8.2.0</code></td>
      <td>Frontend Tooling</td>
      <td>Ultra-fast development server with Hot Module Replacement; production ES bundle builder.</td>
      <td>Compiles React source into <code>frontend/dist/</code> for same-origin backend serving.</td>
    </tr>
    <tr>
      <td><strong>pytest</strong></td>
      <td><code>9.1.1</code></td>
      <td>Testing Framework</td>
      <td>Executes 269 automated test cases across leakage, explainability, policy, and API boundaries.</td>
      <td><code>tests/conftest.py</code> and test modules in <code>tests/</code>.</td>
    </tr>
    <tr>
      <td><strong>HTTPX</strong></td>
      <td><code>0.28.1</code></td>
      <td>HTTP Client Library</td>
      <td>Underpins FastAPI's <code>TestClient</code> for end-to-end API integration and error-path tests.</td>
      <td>Used in <code>tests/test_api.py</code> to test REST endpoints without starting a live port.</td>
    </tr>
    <tr>
      <td><strong>Docker</strong></td>
      <td>Multi-stage</td>
      <td>Containerization</td>
      <td>Container build bundling Node 22 (frontend builder) and Python 3.13-slim (runtime).</td>
      <td>Defined in <code>Dockerfile</code> and orchestrated via <code>docker-compose.yml</code>.</td>
    </tr>
  </tbody>
</table>

<h2 id="sec-4-2">4.2 Python Ecosystem &amp; Machine Learning Libraries</h2>

<h3>Python 3.13: Modern Asynchronous &amp; Typed Foundation</h3>
<p>
  MerchantShield AI utilizes Python 3.13 as its primary programming environment. Python was chosen because it represents the undisputed center of gravity for modern data science, statistical modeling, and scientific machine learning, while providing robust asynchronous web frameworks. The codebase adheres strictly to modern Python typing conventions (using <code>dataclasses</code>, <code>typing.Optional</code>, <code>typing.Literal</code>, and Pydantic models), ensuring static verification and maintainability.
</p>

<h3>NumPy 2.4.4 &amp; pandas 3.0.2: Leakage-Safe Behavioral Mathematics</h3>
<p>
  The feature engineering engine in <code>ml/features/build_features.py</code> is built upon NumPy and pandas. While pandas handles high-level customer partitioning via <code>groupby("customer_id")</code>, raw NumPy arrays are used to calculate rolling statistics without incurring pandas indexing overhead. Specifically:
</p>
<ul>
  <li><code>np.cumsum()</code> and squared cumulative sums are concatenated with a leading <code>0.0</code> and sliced with <code>[:-1]</code> to compute running means and running standard deviations strictly on transactions <em>prior</em> to the current row index.</li>
  <li><code>np.divide(..., where=prior_count &gt; 0)</code> ensures division-by-zero errors are mathematically trapped, outputting safe <code>0.0</code> defaults for first-time customers.</li>
  <li>Vectorized timestamp integer arrays (<code>datetime64[s]</code>) compute trailing 5-minute, 30-minute, and 60-minute transaction velocities via pointer-sliding two-pointer loops in $O(N)$ time per customer.</li>
</ul>

<h3>scikit-learn 1.8.0: Benchmarking &amp; Metric Verification</h3>
<p>
  <code>scikit-learn</code> provides the foundation for the baseline model (<code>LogisticRegression</code> paired with <code>StandardScaler</code> in <code>ml/training/train_baseline.py</code>) and all rigorous evaluation metrics across the project:
</p>
<ul>
  <li><code>precision_recall_curve</code> and <code>average_precision_score</code> compute PR-AUC, the canonical metric for class-imbalanced fraud detection.</li>
  <li><code>confusion_matrix(..., labels=[0, 1])</code> extracts exact True Positive, False Positive, True Negative, and False Negative counts for feeding the asymmetric financial cost model.</li>
</ul>

<h2 id="sec-4-3">4.3 LightGBM &amp; SHAP: The Dual Reasoning Engine</h2>

<h3>LightGBM 4.7.0: High-Speed, Leaf-Wise Gradient Boosting</h3>
<p>
  <code>LightGBM</code> was selected over Random Forest and Deep Neural Networks as the primary production classifier (<code>ml/models/candidate_lgbm_v1.pkl</code>). LightGBM utilizes histogram-based algorithms and leaf-wise (best-first) tree growth rather than depth-wise growth, resulting in superior accuracy on non-linear tabular data with significantly faster training and inference times (under 5 milliseconds for a batch of 1,000 transactions).
</p>
<div class="callout callout-important">
  <div class="callout-title">The Early Stopping Metric Bug &amp; Its Fix (Phase 4 Engineering Record)</div>
  During candidate model training, an insidious machine learning bug was uncovered: using <code>eval_metric="average_precision"</code> for early stopping caused LightGBM to prematurely halt training after iteration 1, resulting in probabilities capped near 0.35 and 0% recall.
  <br/><br/>
  <strong>Root Cause Analysis:</strong> LightGBM's binary objective automatically evaluates <code>binary_logloss</code> alongside any custom metric. Under severe class imbalance (~1.5% fraud), our high <code>scale_pos_weight=73.2</code> artificially inflates predicted-positive confidence, causing <code>binary_logloss</code> to deteriorate immediately—even while PR-AUC is rapidly climbing. By default, LightGBM requires all metrics to improve, so logloss vetoed training.
  <br/><br/>
  <strong>The Fix:</strong> Configured <code>eval_metric="auc"</code> with <code>callbacks=[lgb.early_stopping(stopping_rounds=50, first_metric_only=True)]</code>. This decoupled early stopping from secondary metrics, allowing boosting to converge naturally at its optimum.
</div>

<h3>SHAP 0.52.0: Exact Shapley Attributions with Additivity Checks</h3>
<p>
  Rather than relying on sampling approximations (such as KernelSHAP or LIME), MerchantShield AI deploys <code>shap.TreeExplainer</code>. TreeExplainer leverages the tree structure of LightGBM to calculate exact Shapley values in polynomial time $O(TLD^2)$.
</p>
<p>
  In <code>ml/evaluation/explainability.py</code>, SHAP decomposes the model's raw margin (log-odds) output:
</p>
<pre><code>margin = base_value + &Sigma; shap_values[i]
P(fraud) = 1.0 / (1.0 + exp(-margin))</code></pre>
<p>
  Every single call to <code>RiskExplainer.explain()</code> mathematically reconstructs the probability and asserts:
</p>
<pre><code>abs(reconstructed_prob - raw_prob) &lt; 1e-4</code></pre>
<p>
  If this additivity check fails, the system immediately flags <code>additivity_check_passed=false</code>, preventing corrupt or mismatched model explanations from reaching compliance audits.
</p>

<h2 id="sec-4-4">4.4 Backend API Stack: FastAPI, Pydantic v2 &amp; Uvicorn</h2>
<p>
  The backend service is powered by <strong>FastAPI 0.141.1</strong> and <strong>Pydantic 2.13.4</strong> running on the <strong>Uvicorn ASGI server</strong>:
</p>
<ul>
  <li><strong>Lifespan Management:</strong> In <code>backend/main.py</code>, an <code>@asynccontextmanager</code> lifespan loads the frozen LightGBM model, warms up the SHAP TreeExplainer, and connects the SQLite audit store exactly once during application startup. If the model artifact is missing, the service starts in a degraded state so <code>/health</code> can report the issue rather than crashing the operating system process.</li>
  <li><strong>Strict Pydantic Validation:</strong> In <code>backend/schemas/transaction.py</code>, custom validators enforce that transaction amounts are positive (<code>gt=0</code>), identifiers are non-empty strings, payment methods match permitted enums, and all <code>prior_transactions</code> have timestamps strictly before the transaction being evaluated.</li>
  <li><strong>Exception Sanitization:</strong> Global handlers in <code>main.py</code> intercept validation errors and unhandled exceptions, converting internal Python tracebacks into sanitized, structured JSON error bodies (status 422 and 500) to prevent internal system leakage.</li>
</ul>

<h2 id="sec-4-5">4.5 Persistence &amp; Governance: SQLAlchemy &amp; SQLite</h2>
<p>
  The governance tier utilizes <strong>SQLAlchemy 2.0</strong> with a local <strong>SQLite 3</strong> embedded database (<code>backend/data/audit.db</code>):
</p>
<ul>
  <li><strong>Single-File, Serverless Architecture:</strong> Ideal for self-contained buildathon evaluation and edge deployments without external database daemon dependencies.</li>
  <li><strong>Deliberate PII Omission:</strong> To adhere to privacy-by-design standards, the audit table intentionally omits <code>customer_id</code>, <code>device_id</code>, and <code>geo_region</code>. It persists only the decision facts (transaction ID, probability, threshold, risk score, action, rule ID, and SHAP top reasons).</li>
  <li><strong>V2 Idempotent Schema Migration:</strong> In <code>backend/services/audit_service.py</code>, the <code>_migrate_add_prior_transaction_count_if_needed()</code> method executes a raw SQLite PRAGMA check on startup to dynamically add the <code>prior_transaction_count</code> column to pre-existing databases without requiring alembic or dropping data.</li>
</ul>

<h2 id="sec-4-6">4.6 Frontend Architecture: React 19, Vite &amp; Vanilla CSS</h2>
<p>
  The analyst dashboard is built with <strong>React 19.2</strong> and bundled using <strong>Vite 8.2</strong>:
</p>
<ul>
  <li><strong>Strict Decoupling:</strong> The frontend contains zero Python imports and zero duplicated business logic. It interacts with the backend strictly via standard HTTP/JSON fetch calls in <code>frontend/src/api/client.js</code>.</li>
  <li><strong>Design System Tokens:</strong> Styled using Vanilla CSS tokens (<code>frontend/src/styles/tokens.css</code> and <code>App.css</code>). Avoiding bulky CSS frameworks (like Tailwind or Bootstrap) guarantees zero dependency bloat, pristine load speeds, and full design flexibility.</li>
  <li><strong>Dual-Call Pattern:</strong> When evaluating a transaction, the frontend executes <code>Promise.all([api.evaluateTransaction(), api.explainTransaction()])</code> to simultaneously fetch the authoritative decision record and the full per-feature SHAP contribution bars for rendering.</li>
</ul>

<h2 id="sec-4-7">4.7 Verification &amp; DevOps: pytest &amp; Multi-Stage Docker</h2>
<ul>
  <li><strong>Automated Testing:</strong> <code>pytest 9.1</code> executes 269 automated tests covering leakage proof, decision policy boundary conditions, SHAP mathematical additivity, API failure recovery, and V2 hardening.</li>
  <li><strong>Multi-Stage Containerization:</strong> The project's <code>Dockerfile</code> uses a multi-stage pattern: Stage 1 builds the React frontend using <code>node:22-slim</code>; Stage 2 copies the compiled static assets into a <code>python:3.13-slim</code> environment, installs Python wheels, pre-generates the synthetic dataset, and serves both frontend and API from a unified single container origin.</li>
</ul>
'''
