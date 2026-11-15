"""
Section 8 — Final Summary and Project Mastery generator.
"""

def get_section8_html():
    return '''
<div class="page-break"></div>
<h1 id="section-8"><span class="section-number">8</span> FINAL SUMMARY AND PROJECT MASTERY</h1>

<h2 id="sec-8-1">8.1 The Project in One Complete Narrative</h2>
<p>
  <strong>MerchantShield AI</strong> is an explainable, defensive transaction-risk decisioning system developed for the Razorpay AI Buildathon 2026. The platform bridges the dangerous gap between statistical machine learning models and operational business action by cleanly decoupling three fundamental concerns:
</p>
<ol>
  <li><strong>Statistical Probability Estimation:</strong> A frozen LightGBM classifier estimates <code>P(fraud) &in; [0.0, 1.0]</code> from 15 strictly-prior behavioral features computed across customer transaction sequences without future leakage.</li>
  <li><strong>Mathematical Explainability:</strong> A SHAP TreeExplainer decomposes the model's raw margin output into exact feature attributions, verifying additivity (<code>base + &Sigma;shap &approx; predict_proba</code>) on every evaluation.</li>
  <li><strong>Deterministic Policy Governance:</strong> A transparent five-rule priority cascade maps <code>(probability, amount)</code> to bounded action recommendations (<code>ALLOW</code>, <code>ALLOW_WITH_MONITORING</code>, <code>STEP_UP_VERIFICATION</code>, <code>BLOCK</code>) using a cost-minimized threshold (0.40) rather than an arbitrary 0.50 cutoff.</li>
</ol>
<p>
  The system packages these capabilities into a high-performance FastAPI backend, a governance-first SQLite audit store that omits customer PII, and an interactive React 19 dashboard speaking pure HTTP/JSON.
</p>

<h2 id="sec-8-2">8.2 Complete Flow Recap (10-Step Numbered Sequence)</h2>
<ol>
  <li><strong>Server Startup:</strong> Uvicorn launches FastAPI; the <code>lifespan</code> manager loads <code>candidate_lgbm_v1.pkl</code>, initializes <code>shap.TreeExplainer</code>, and connects the SQLite audit database.</li>
  <li><strong>Request Ingestion:</strong> A client submits an HTTP POST to <code>/risk/evaluate</code> containing current transaction details and optional prior customer history.</li>
  <li><strong>Shape &amp; Chronology Validation:</strong> Pydantic validates field constraints and asserts that all prior transaction timestamps are strictly before the current transaction.</li>
  <li><strong>Feature Transformation:</strong> <code>build_features()</code> computes 15 leakage-safe behavioral features (rolling means, amount z-scores, velocity counts, device/geo novelty).</li>
  <li><strong>V2 Bounds Hardening:</strong> <code>_validate_engineered_features()</code> checks that velocity counts and z-scores fall within defensible domain limits.</li>
  <li><strong>LightGBM Inference:</strong> The frozen model outputs raw probability, verified to be a finite float in <code>[0.0, 1.0]</code>.</li>
  <li><strong>Decision Engine Execution:</strong> <code>evaluate_policy(probability, amount)</code> checks the 5-rule cascade and produces a bounded action recommendation independently of SHAP.</li>
  <li><strong>SHAP Attributions:</strong> <code>TreeExplainer</code> computes feature contributions and verifies additivity within 1e-4 tolerance, generating grounded text narratives.</li>
  <li><strong>Isolated Audit Persistence:</strong> Decision facts and serialized SHAP reasons are saved to SQLite without customer PII; audit write failures are trapped and isolated.</li>
  <li><strong>Client Delivery:</strong> A strongly-typed <code>RiskEvaluateResponse</code> is returned over HTTP 200, rendering verbatim action badges and SHAP bars in the React dashboard.</li>
</ol>

<h2 id="sec-8-3">8.3 Key Architectural Components to Remember</h2>
<ul>
  <li><code>DECISION_THRESHOLD = 0.40</code>: The operating boundary chosen by sweeping validation thresholds against an asymmetric cost function subject to &ge;80% recall.</li>
  <li><code>CRITICAL_MIN = 0.80</code>: The policy threshold where validation precision reaches 94.1%, warranting an outright <code>BLOCK</code> recommendation.</li>
  <li><code>LARGE_AMOUNT_CUTOFF = 25,000.0</code>: Policy escalation cutoff that subjects mid-probability purchases to <code>STEP_UP_VERIFICATION</code> due to high loss downside.</li>
  <li><code>ml/features/build_features.py</code>: The single source of truth for the 15 behavioral features.</li>
  <li><code>ml/evaluation/policy.py</code>: The single source of truth for the 5-rule deterministic policy table.</li>
  <li><code>backend/services/audit_service.py</code>: The privacy-conscious audit persistence engine with idempotent SQLite schema migrations.</li>
</ul>

<h2 id="sec-8-4">8.4 Verified Strengths vs. Explicit Prototype Limitations</h2>
<table>
  <thead>
    <tr>
      <th>Verified Strengths (Measured Facts)</th>
      <th>Prototype Limitations &amp; Boundary Realities</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Leakage-Free Features:</strong> Proven by dedicated tests verifying strictly-prior historical computation on 213,000 transactions.</td>
      <td><strong>Synthetic Training Data:</strong> The production model was trained on generator-controlled synthetic data; no live bank data was claimed.</td>
    </tr>
    <tr>
      <td><strong>Asymmetric Cost Optimization:</strong> Selected threshold (0.40) reduces test-set fraud loss to ₹41,377 vs ₹110,582 for baseline.</td>
      <td><strong>External Transfer Discrepancy:</strong> Frozen synthetic model failed on IEEE-CIS (ROC-AUC 0.443) due to z-score domain shift; retraining required.</td>
    </tr>
    <tr>
      <td><strong>Mathematical Grounding:</strong> SHAP additivity verified on every call (1e-4 tolerance); no free-text LLM hallucination.</td>
      <td><strong>No Live Customer DB:</strong> Callers must supply prior transaction history in the request payload; no live transaction lookups exist.</td>
    </tr>
    <tr>
      <td><strong>Decoupled Governance:</strong> SHAP explanations are structurally isolated from action logic; score buckets do not drive policy.</td>
      <td><strong>Policy Label Monitoring:</strong> <code>ALLOW_WITH_MONITORING</code> is an auditable label; no background polling daemon exists.</td>
    </tr>
    <tr>
      <td><strong>Defensive V2 Hardening:</strong> Feature bounds validation, model probability checks, and SQLite column migrations.</td>
      <td><strong>No Authentication:</strong> API and dashboard contain no user login or RBAC permissions (designed as an internal microservice).</td>
    </tr>
  </tbody>
</table>

<h2 id="sec-8-5">8.5 Self-Testing Examination &amp; Grounded Answers</h2>

<h3>Q1: Why is reporting raw classification accuracy dangerous in fraud detection?</h3>
<p>
  <strong>Answer:</strong> Because fraud prevalence is extremely low (1–3%). A trivial model predicting 100% legitimate achieves 98.5% accuracy while catching zero fraud. Metrics must report PR-AUC, precision, recall, and total financial cost.
</p>

<h3>Q2: Why was the operating threshold set to 0.40 rather than the default 0.50 or the F1-maximum 0.80?</h3>
<p>
  <strong>Answer:</strong> Fraud losses are asymmetric: false negatives (stolen merchandise) cost orders of magnitude more than false positives (₹50 operational check). Sweeping thresholds on validation data against the cost model identified 0.40 as the exact mathematical minimum cost subject to maintaining &ge;80% recall. The F1-maximum (0.80) weights precision and recall equally, which misses mid-range fraud and increases total costs by ~38%.
</p>

<h3>Q3: How does MerchantShield AI prove that its feature engineering has zero data leakage?</h3>
<p>
  <strong>Answer:</strong> In <code>ml/features/build_features.py</code>, cumulative sums are shifted by one index (<code>np.cumsum(...)[:-1]</code>) so that row <code>i</code> only observes rows <code>0</code> through <code>i-1</code>. Automated tests in <code>tests/test_no_leakage.py</code> verify that feature values match the historical sequence exactly when re-computed incrementally.
</p>

<h3>Q4: Why are SHAP explanations structurally prevented from influencing the decision engine's action?</h3>
<p>
  <strong>Answer:</strong> SHAP explains the model's internal reasoning, which can exhibit feature correlation or credit-splitting. Financial actions require hard, auditable guarantees. The function signature of <code>evaluate_policy(probability, amount)</code> physically cannot receive SHAP explanations, ensuring an explanation bug can never silently alter an operational action.
</p>

<h3>Q5: Why does a transaction with probability 0.25 show as risk category "LOW" while receiving an action of "ALLOW_WITH_MONITORING"?</h3>
<p>
  <strong>Answer:</strong> Because the 0–100 risk score buckets (0–30 is LOW) are informational presentation tools for human cognitive ergonomics, whereas the action policy enforces a 0.15 floor for elevated monitoring. Decoupling display buckets from action rules ensures presentation adjustments never accidentally alter financial actions.
</p>

<h3>Q6: What happened during Experiment A when the frozen synthetic model was tested on real IEEE-CIS data?</h3>
<p>
  <strong>Answer:</strong> The frozen model failed with an inverted ROC-AUC of 0.443. The root cause was domain distribution shift: on IEEE-CIS data, cards with thousands of prior transactions produced extreme z-scores that the synthetic model had never encountered during training, inverting the probability ranking.
</p>

<h3>Q7: How did Phase 15 improve fraud detection on real IEEE-CIS chargeback data?</h3>
<p>
  <strong>Answer:</strong> Phase 15 introduced the <code>card_product_share</code> feature (fraction of a card's prior transactions in the current product category). This emerged as the 3rd most important feature by gain, reducing false positives by 17.7% and expected cost by 17.0%, elevating test ROC-AUC to 0.771.
</p>

<h3>Q8: What is the Audit-Write Failure Isolation pattern in <code>backend/api/routes.py</code>?</h3>
<p>
  <strong>Answer:</strong> If an operational error prevents SQLite from persisting the audit record, the exception is caught and logged. The API still returns the valid HTTP 200 risk decision with <code>audit_persisted: false</code>, ensuring ancillary logging failures never block checkout transactions.
</p>

<h3>Q9: How does the system handle "cold-start" transactions where a customer has zero prior history?</h3>
<p>
  <strong>Answer:</strong> Neutral sentinel values are assigned (<code>time_since_prev_txn_min = 99999.0</code>, z-scores = 0.0), history-dependent features are filtered out of the SHAP narrative, and the API returns <code>signal_quality: {{ level: "MINIMAL" }}</code> to transparently alert analysts.
</p>

<h3>Q10: Why are customer IDs and device IDs omitted from the SQLite audit log table?</h3>
<p>
  <strong>Answer:</strong> To adhere to privacy-by-design standards. The audit log exists solely to prove what the risk decisioning system evaluated and why, avoiding the unnecessary and legally hazardous duplication of merchant customer PII.
</p>

<h2 id="sec-8-6">8.6 How to Explain This Project to Another Engineer</h2>

<h3>The 30-Second Elevator Pitch</h3>
<p>
  <em>"MerchantShield AI is an end-to-end explainable transaction-risk decisioning platform built for the Razorpay AI Buildathon. Instead of naively thresholding a black-box model at 0.50, it decouples statistical estimation, presentation scoring, and business governance. It estimates fraud probability using a frozen LightGBM model over 15 strictly-prior behavioral features, verifies exact mathematical additivity on every prediction using SHAP TreeExplainer, and maps the probability to bounded actions—like step-up verification or blocking—using a cost-optimized threshold of 0.40 and a deterministic 5-rule policy table."</em>
</p>

<h3>The 2-Minute Architectural Overview</h3>
<p>
  <em>"Most fraud ML projects fail in production because they mix up classification with decisioning. A model predicting 0.45 doesn't tell you whether to block a card—that depends on false-positive friction costs, the transaction amount, and compliance policy.</em>
</p>
<p>
  <em>MerchantShield solves this with four decoupled tiers: First, a FastAPI gateway validates incoming payloads and ensures historical context is strictly prior in time. Second, a leakage-safe NumPy pipeline extracts 15 behavioral signals like velocity windows and expanding amount z-scores. Third, a frozen LightGBM classifier estimates fraud probability, which is immediately decomposed by a SHAP TreeExplainer that verifies mathematical additivity on every call. Fourth, a deterministic five-rule policy cascade maps probability and amount to an operational recommendation—ALLOW, ALLOW_WITH_MONITORING, STEP_UP_VERIFICATION, or BLOCK. Everything is committed to a PII-free SQLite audit log with isolated error handling and served to a React 19 dashboard speaking pure HTTP/JSON. The entire system is covered by 269 automated tests."</em>
</p>

<h3>The 10-Minute Deep Technical Walkthrough</h3>
<p>
  When presenting the codebase in an architectural interview or deep-dive code review:
</p>
<ol>
  <li><strong>Start at <code>backend/config/settings.py</code> and <code>ml/evaluation/policy.py</code>:</strong> Point out that settings files define paths and constants, but deliberately contain zero policy numbers. Policy numbers live strictly in <code>policy.py</code>.</li>
  <li><strong>Walk through <code>ml/features/build_features.py</code>:</strong> Show the cumulative sum indexing (<code>cumsum[:-1]</code>) and two-pointer velocity loops. Emphasize how <code>tests/test_no_leakage.py</code> proves temporal invariance.</li>
  <li><strong>Explain <code>ml/training/train_candidates.py</code> and the Early Stopping Bug:</strong> Share the discovery of the LightGBM <code>scale_pos_weight</code> logloss veto and how switching to <code>first_metric_only=True</code> on AUC fixed convergence.</li>
  <li><strong>Review <code>ml/evaluation/threshold_analysis.py</code> and Cost Formulation:</strong> Explain why the operating threshold is 0.40 (cost-optimal) rather than 0.80 (F1-maximum), citing asymmetric false negative losses.</li>
  <li><strong>Demonstrate <code>ml/evaluation/explainability.py</code>:</strong> Show how the margin sum reconstructs probability through the sigmoid function, proving exact SHAP grounding.</li>
  <li><strong>Examine <code>backend/api/routes.py</code> and <code>services/audit_service.py</code>:</strong> Highlight the audit failure isolation pattern and idempotent SQLite column migration for V2 deployments.</li>
  <li><strong>Discuss the External Validation Track (IEEE-CIS):</strong> Explain the honest failure of Experiment A (frozen transfer) due to z-score distribution shift, and the success of Experiment B (retrained transfer achieving 0.771 ROC-AUC and 79.8% recall with <code>card_product_share</code>).</li>
</ol>

<h2 id="sec-8-7">8.7 Engineering Glossary &amp; Final Revision Checklist</h2>

<h3>Technical Glossary</h3>
<ul>
  <li><strong>Class Imbalance:</strong> An extreme disparity between positive (fraud) and negative (legitimate) examples, invalidating raw accuracy.</li>
  <li><strong>Temporal Data Leakage:</strong> An error where information from future events inadvertently contaminates feature calculations for past transactions.</li>
  <li><strong>Operating Threshold:</strong> The mathematical probability cutoff above which an alert or friction action is triggered.</li>
  <li><strong>Asymmetric Cost Function:</strong> A loss formulation where false negatives and false positives carry unequal financial weights.</li>
  <li><strong>Shapley Value:</strong> A game-theoretic measure calculating the fair marginal contribution of each feature to a model's prediction.</li>
  <li><strong>Additivity Property:</strong> The mathematical requirement that the base expected value plus the sum of all feature attributions equals the model's prediction.</li>
  <li><strong>Bounded Action:</strong> An operational recommendation that is reversible and non-destructive, avoiding automated unilateral financial transfers.</li>
  <li><strong>Signal Quality:</strong> An operational rating (MINIMAL to ESTABLISHED) indicating the volume of historical context available for behavioral inference.</li>
</ul>

<h3>Final Revision Checklist for Engineers</h3>
<ul>
  <li>[x] Understand the 3-tier decoupling (ML probability &rarr; 0–100 display score &rarr; 5-rule policy action).</li>
  <li>[x] Explain why 0.40 was chosen instead of 0.50 using the asymmetric financial cost model.</li>
  <li>[x] Articulate how shifting cumulative sums prevents data leakage in <code>build_features.py</code>.</li>
  <li>[x] Describe how <code>shap.TreeExplainer</code> verifies additivity within 1e-4 tolerance.</li>
  <li>[x] Explain why the audit log omits customer PII and how audit write failure isolation works.</li>
  <li>[x] Understand why the frozen model failed on IEEE-CIS while the retrained methodology succeeded.</li>
  <li>[x] Verify that all 269 automated tests pass and that CI runs cleanly.</li>
</ul>
'''
