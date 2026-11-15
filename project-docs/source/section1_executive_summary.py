"""
Section 1 — Executive Summary generator.
"""

def get_section1_html(architecture_svg):
    return f'''
<div class="page-break"></div>
<h1 id="section-1"><span class="section-number">1</span> EXECUTIVE SUMMARY</h1>

<h2 id="sec-1-1">1.1 Project Overview &amp; Core Mission</h2>
<p>
  <strong>MerchantShield AI</strong> is an end-to-end, defensive transaction-risk decisioning platform engineered for electronic commerce merchants and digital payment service providers. Developed for the <em>Razorpay AI Buildathon 2026 (Track 02 — AI Risk Manager)</em>, the system solves a fundamental, systemic failure in modern payment security: the conflation of raw machine learning statistical classification with operational decision-making. 
</p>
<p>
  In a single evaluation cycle, MerchantShield AI ingests an incoming payment transaction along with its customer's prior transaction history, computes 15 strictly-prior behavioral features without future temporal leakage, estimates the probability of fraud using a frozen LightGBM gradient-boosted decision tree classifier (<code>candidate_lgbm_v1.pkl</code>), mathematically validates and decomposes that estimate using grounded Shapley Additive exPlanations (SHAP), and maps the probability to a bounded, auditable operational recommendation (<code>ALLOW</code>, <code>ALLOW_WITH_MONITORING</code>, <code>STEP_UP_VERIFICATION</code>, or <code>BLOCK</code>) using a transparent five-rule deterministic policy table. Crucially, the system is strictly advisory: it never executes irreversible financial side effects such as freezing bank accounts, moving funds, or issuing unilateral chargebacks.
</p>

<div class="callout callout-note">
  <div class="callout-title">Core Architectural Axiom: The Three-Tier Separation of Concerns</div>
  MerchantShield AI enforces a structural, architectural decoupling between three distinct operational concerns:
  <ol style="margin-top: 4px; margin-bottom: 2px;">
    <li><strong>The Statistical Estimator:</strong> A machine learning model estimates the objective probability of fraud: <code>P(fraud) &in; [0.0, 1.0]</code>. It does not decide what to do.</li>
    <li><strong>The Human Presentation Layer:</strong> A deterministic function maps the continuous probability to a 0–100 risk score and categorical tier (<code>LOW</code>, <code>MEDIUM</code>, <code>HIGH</code>, <code>CRITICAL</code>) solely for human cognitive ergonomics.</li>
    <li><strong>The Governance Policy Engine:</strong> An independent, deterministic rule cascade evaluates <code>(probability, amount)</code> against an asymmetric economic cost threshold (0.40) to select a bounded operational action.</li>
  </ol>
  Because these tiers are strictly decoupled, modifying display buckets can never silently alter financial actions, and bugs in explanatory text can never alter transaction disposition.
</div>

<h2 id="sec-1-2">1.2 Target Users &amp; Integrating Systems</h2>
<p>
  MerchantShield AI is designed to integrate into two distinct operational environments:
</p>
<ul>
  <li><strong>Payment Gateways &amp; Merchant Acquirers (e.g., Razorpay, Stripe, Adyen):</strong> Placed inline within the pre-authorization or post-authorization payment routing pipeline. The gateway supplies the transaction context and receives a bounded risk recommendation in sub-50 milliseconds.</li>
  <li><strong>Merchant Risk Operations Teams &amp; Fraud Analysts:</strong> Interacting through the dedicated React 19 dashboard, fraud analysts investigate high-risk transactions, review grounded SHAP attribution bars explaining exactly why an alert fired, verify historical velocity, and inspect an immutable SQLite audit trail.</li>
</ul>

<h2 id="sec-1-3">1.3 Real-World Problem &amp; Core Capabilities</h2>
<p>
  Conventional fraud detection models routinely fail rigorous production scrutiny for three compounding reasons:
</p>
<ol>
  <li><strong>Deceptive Metric Reporting on Imbalanced Classes:</strong> At real-world fraud rates (1% to 3.5%), reporting standard classification "accuracy" is completely meaningless (a naive model predicting 100% legitimate achieves 98.5% accuracy while catching 0% of fraud).</li>
  <li><strong>The Arbitrary 0.5 Threshold Flaw:</strong> Defaulting to a 0.50 classification cutoff ignores the severe economic asymmetry between the cost of a false positive (customer checkout friction, support tickets, lost lifetime value) and the cost of a false negative (chargeback fees, stolen merchandise, merchant penalties).</li>
  <li><strong>The Black-Box Explanatory Deficit:</strong> Complex ensemble models or neural networks cannot explain to a human compliance officer or merchant why a transaction was halted, leading to regulatory vulnerability and merchant distrust.</li>
</ol>
<p>
  MerchantShield AI addresses all three problems simultaneously through verified capabilities:
</p>
<ul>
  <li><strong>Leakage-Safe Feature Pipeline:</strong> All 15 behavioral signals (velocity windows, amount z-scores, rolling failure rates, device novelty) are computed strictly from events prior to the current transaction timestamp, proven by a 213,000-row leakage verification test suite.</li>
  <li><strong>Cost-Driven Threshold Optimization:</strong> Operating threshold (0.40) was selected by sweeping thresholds against an explicit financial cost model (₹50 flat FP cost; 0.5 &times; amount FN cost) on a held-out validation set, subject to an operational floor of &ge;80% fraud recall.</li>
  <li><strong>Grounded SHAP Explainability with Additivity Verification:</strong> Per-transaction feature contributions derived from <code>shap.TreeExplainer</code> verify mathematical additivity (<code>base_value + &Sigma;shap &approx; predict_proba</code> within 1e-4) on every API invocation.</li>
  <li><strong>V2 Production Hardening:</strong> Defensive model validation rejects non-finite probabilities (NaN/Inf) and out-of-range floats, while feature bounds checking guards against pathological input spikes. Historical signal quality grading (<code>MINIMAL</code>, <code>LIMITED</code>, <code>MODERATE</code>, <code>ESTABLISHED</code>) transparently communicates context sufficiency.</li>
</ul>

<h2 id="sec-1-4">1.4 High-Level Architecture &amp; Key Technologies</h2>
<p>
  The system consists of a modern, containerized client-server architecture built on Python 3.13 and React 19:
</p>

<div class="diagram-container">
  {architecture_svg}
  <div class="diagram-caption">Figure 1.1: MerchantShield AI High-Level Architecture — Tiered Client, API Gateway, ML Intelligence, and Governance Layers.</div>
</div>

<p>
  The technical foundation comprises:
</p>
<ul>
  <li><strong>Machine Learning &amp; Math:</strong> Python 3.13, NumPy 2.4, pandas 3.0, scikit-learn 1.8, LightGBM 4.7, SHAP 0.52, and SciPy 1.17.</li>
  <li><strong>Backend API &amp; Services:</strong> FastAPI 0.141, Pydantic v2.13, Uvicorn 0.52, SQLAlchemy 2.0, and SQLite 3.</li>
  <li><strong>Frontend Client:</strong> React 19.2, Vite 8.2, and Vanilla CSS Tokens (no heavy CSS framework dependencies).</li>
  <li><strong>Testing &amp; DevOps:</strong> pytest 9.1, HTTPX 0.28, multi-stage Docker (Node 22 + Python 3.13), and GitHub Actions CI.</li>
</ul>

<h2 id="sec-1-5">1.5 System Boundaries, Inputs &amp; Outputs</h2>
<p>
  MerchantShield AI operates under strictly enforced boundaries:
</p>
<ul>
  <li><strong>Inputs:</strong> The API accepts a <code>RiskRequest</code> containing the target <code>TransactionInput</code> (transaction ID, customer ID, merchant ID, amount, timestamp, device ID, geographic region, payment method, status, account creation time) and an optional list of <code>prior_transactions</code> for that same customer.</li>
  <li><strong>Outputs:</strong> A strongly-typed <code>RiskEvaluateResponse</code> containing the transaction ID, model version (<code>lgbm_v1</code>), raw fraud probability, frozen threshold (0.40), 0–100 risk score, categorical tier, recommended operational action, triggering policy rule ID, human-readable policy reason, grounded SHAP explanation header and reasons, signal quality rating, and audit persistence confirmation.</li>
  <li><strong>Boundaries:</strong> MerchantShield AI does not manage bank transfers, does not capture funds, does not store cardholder primary account numbers (PAN), and does not persist customer PII in its audit log.</li>
</ul>

<h2 id="sec-1-6">1.6 Implementation Status &amp; Limitations</h2>
<p>
  To maintain complete scientific and architectural integrity, the repository explicitly distinguishes verified implementations from prototype constraints:
</p>
<ul>
  <li><strong>Fully Implemented and Verified:</strong> The feature engineering pipeline, chronological split utility, LightGBM training, cost-optimized threshold analysis, SHAP explainer with additivity checking, deterministic 5-rule policy engine, FastAPI REST API, SQLite audit persistence with idempotent schema migration, React 19 dashboard, and 269 automated unit/hardening tests.</li>
  <li><strong>External Real-Data Validation (Phases 14–17):</strong> Methodology was evaluated on 590,540 real-world e-commerce transactions from the IEEE-CIS dataset (Vesta chargebacks). The frozen synthetic model failed to transfer (ROC-AUC 0.443) due to distribution shift in customer z-scores, but retraining with MerchantShield's feature engineering achieved <strong>ROC-AUC 0.771</strong> and <strong>79.8% fraud recall</strong> at an expected cost of 2,469,531 cost units on the held-out test split.</li>
  <li><strong>Prototype Limitations:</strong> Production model was trained on generator-controlled synthetic data (~213k transactions, 1.5% fraud). The prototype does not include a live customer transaction database (callers must provide historical context), has no authentication layer, and <code>ALLOW_WITH_MONITORING</code> is an auditable policy label without an autonomous background polling daemon.</li>
</ul>

<h2 id="sec-1-7">1.7 Executive Summary Master Reference Table</h2>
<table>
  <thead>
    <tr>
      <th>Dimension</th>
      <th>System Specification / Implementation Reality</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Project Name &amp; Track</strong></td>
      <td>MerchantShield AI — Razorpay AI Buildathon 2026 (Track 02: AI Risk Manager)</td>
    </tr>
    <tr>
      <td><strong>Core Architecture</strong></td>
      <td>Decoupled 3-Tier: LightGBM Classifier &rarr; SHAP Explainer &rarr; 5-Rule Deterministic Policy Cascade</td>
    </tr>
    <tr>
      <td><strong>Primary Model Artifact</strong></td>
      <td><code>ml/models/candidate_lgbm_v1.pkl</code> (LightGBM, max_depth=6, num_leaves=31, scale_pos_weight=73.2)</td>
    </tr>
    <tr>
      <td><strong>Selected Decision Threshold</strong></td>
      <td><strong>0.40</strong> (Chosen on validation set to minimize expected cost subject to Recall &ge; 80%)</td>
    </tr>
    <tr>
      <td><strong>Test Set Performance (Synthetic)</strong></td>
      <td>Precision: <strong>78.5%</strong> | Recall: <strong>88.2%</strong> | F1: <strong>0.830</strong> | PR-AUC: <strong>0.901</strong> | Est. Cost: <strong>₹41,377</strong></td>
    </tr>
    <tr>
      <td><strong>External Held-Out Test (IEEE-CIS)</strong></td>
      <td>ROC-AUC: <strong>0.771</strong> | Recall: <strong>79.8%</strong> (3,243 / 4,064 frauds caught) | Selected Threshold: 0.35</td>
    </tr>
    <tr>
      <td><strong>Action Catalog</strong></td>
      <td><code>ALLOW</code>, <code>ALLOW_WITH_MONITORING</code>, <code>STEP_UP_VERIFICATION</code>, <code>BLOCK</code> (Purely advisory recommendations)</td>
    </tr>
    <tr>
      <td><strong>Feature Engineering</strong></td>
      <td>15 strictly-prior features computed across customer historical sequences (Leakage verified)</td>
    </tr>
    <tr>
      <td><strong>Explainability Engine</strong></td>
      <td>TreeExplainer with per-request additivity check (<code>|base + &Sigma;shap - prob| &lt; 1e-4</code>) + Grounded templates</td>
    </tr>
    <tr>
      <td><strong>Persistence &amp; Audit</strong></td>
      <td>SQLite (<code>backend/data/audit.db</code>) via SQLAlchemy 2.0; stores decision facts; omits customer PII</td>
    </tr>
    <tr>
      <td><strong>Frontend Dashboard</strong></td>
      <td>React 19, Vite 8, pure CSS design tokens; consumes HTTP/JSON only (zero Python backend imports)</td>
    </tr>
    <tr>
      <td><strong>Test Suite Coverage</strong></td>
      <td>269 passing automated unit/property tests covering leakage, policy boundaries, SHAP additivity &amp; V2 hardening</td>
    </tr>
  </tbody>
</table>
'''
