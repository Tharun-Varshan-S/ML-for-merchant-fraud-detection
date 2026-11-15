"""
Section 2 — Problem Statement generator.
"""

def get_section2_html():
    return '''
<div class="page-break"></div>
<h1 id="section-2"><span class="section-number">2</span> PROBLEM STATEMENT</h1>

<h2 id="sec-2-1">2.1 The Existing Situation: Fraud Detection in Practice</h2>
<p>
  In contemporary electronic commerce and digital payments, merchant enterprises face a relentless operational challenge: discerning legitimate consumer transactions from unauthorized or fraudulent activity in real time. Before modern intelligent risk platforms exist, organizations typically rely on one of two extremes:
</p>
<ol>
  <li><strong>Static Rule Engines:</strong> Primitive "if-then" heuristic rules defined by risk committees (e.g., <em>"flag any transaction exceeding ₹10,000"</em> or <em>"block any payment originating from a new device at night"</em>). While transparent and fast, static rules are brittle, incapable of learning nuanced customer behaviors, easily circumvented by organized fraud rings, and notorious for generating massive false-positive rates that insult loyal customers.</li>
  <li><strong>Opaque Monolithic ML Classifiers:</strong> Second-generation systems employ black-box statistical algorithms (random forests, neural networks, or gradient-boosted trees) that output a raw score between 0.0 and 1.0. However, these systems are almost universally deployed with naive defaults (such as a 0.50 classification cutoff) and lack transparent operational interpretation.</li>
</ol>
<p>
  When a fraudulent transaction bypasses these systems, the merchant suffers a <strong>chargeback</strong>: the true cardholder discovers the unauthorized charge, contacts their issuing bank, and claws back the funds. The merchant loses the merchandise shipped, loses the transaction revenue, incurs a punitive bank chargeback fee (typically ₹1,000 to ₹2,500 per incident), and risks being terminated by payment aggregators if their monthly chargeback ratio breaches 1.0%. Conversely, when a legitimate customer is wrongly declined due to an aggressive heuristic rule (a <strong>false positive</strong>), the customer experiences embarrassment, abandons their cart, and often migrates permanently to a competing platform.
</p>

<h2 id="sec-2-2">2.2 The Three Fundamental Failures of Conventional Systems</h2>
<p>
  As documented in the repository's core problem analysis, fraud detection systems frequently collapse under rigorous architectural and operational scrutiny due to three compounding systemic failures:
</p>

<h3>Failure 1: Meaningless Metric Reporting Under Extreme Class Imbalance</h3>
<p>
  In real-world payment streams, fraudulent transactions account for a tiny fraction of total volume—typically between 1.0% and 3.5%. Under this extreme class imbalance, traditional machine learning metrics such as raw classification accuracy or standard ROC-AUC become dangerously misleading.
</p>
<p>
  Consider an evaluation dataset containing 100,000 transactions where 1,500 are fraudulent (1.5% fraud prevalence). A trivial, degenerate classifier that predicts <code>legitimate</code> for every single transaction achieves an impressive <strong>98.5% accuracy</strong>, yet it allows ₹10,000,000 in fraud losses and catches zero criminal activity. Similarly, ROC-AUC evaluates the true positive rate against the false positive rate across all negative samples; because the pool of legitimate transactions is vast (98,500), tens of thousands of false alarms barely register on the ROC curve, yielding an deceptively high ROC-AUC (e.g., 0.95) even when nine out of ten flagged transactions are completely innocent customers.
</p>

<h3>Failure 2: The Arbitrary 0.50 Threshold Without Economic Justification</h3>
<p>
  Standard machine learning textbooks and off-the-shelf library defaults (such as <code>scikit-learn</code>'s <code>predict()</code>) apply a symmetric probability threshold of <code>p &ge; 0.50</code> to convert a probability into a binary decision. In financial risk management, this default is economically irrational.
</p>
<p>
  Fraud risk is inherently <strong>asymmetric in cost</strong>:
</p>
<ul>
  <li><strong>The Cost of a False Positive (FP):</strong> Wrongly challenging or declining a legitimate customer incurs an operational cost (customer service inquiries, manual verification labor, and customer goodwill friction). In MerchantShield's model, this is modeled as an assumed flat operational expense of ₹50 per occurrence.</li>
  <li><strong>The Cost of a False Negative (FN):</strong> Permitting a fraudulent transaction causes direct financial loss. The merchant is liable for the stolen amount and chargeback penalties. In MerchantShield's cost model, this is formulated as a configurable fraction (e.g., 50% to 100%) of the actual transaction amount. On a ₹50,000 purchase, a false negative costs ₹25,000 to ₹50,000—between 500 and 1,000 times greater than the cost of a false positive.</li>
</ul>
<p>
  Under asymmetric costs, the economically optimal threshold is almost never 0.50. Setting the threshold arbitrarily high (e.g., to maximize the harmonic F1-score at 0.80) yields high precision but misses millions in mid-range fraud, resulting in a 38% higher total financial cost to the merchant.
</p>

<h3>Failure 3: The Black-Box Explanatory Deficit</h3>
<p>
  When a traditional machine learning model outputs a risk score of 0.72, it provides zero actionable reasoning. A merchant risk analyst looking at the dashboard cannot answer:
</p>
<ul>
  <li><em>"Did the score jump because the customer is in a new city?"</em></li>
  <li><em>"Is it because they placed five orders in the last ten minutes?"</em></li>
  <li><em>"Or is it simply because they purchased an expensive television?"</em></li>
</ul>
<p>
  Without grounded explainability, human reviewers cannot distinguish a true fraud ring attack from a loyal customer traveling on vacation. Furthermore, emerging data protection regulations and consumer credit acts strictly require financial institutions to explain adverse actions taken against consumers.
</p>

<h2 id="sec-2-3">2.3 The Problem MerchantShield AI Solves</h2>
<p>
  MerchantShield AI was architected from the ground up to solve these three compounding failures in a unified, auditable software platform. The central objective of the project is to provide a <strong>calibrated, economically rational, and human-explainable decisioning layer</strong> that sits between raw payment telemetry and business action.
</p>
<p>
  Specifically, MerchantShield AI guarantees:
</p>
<ol>
  <li><strong>Precision-Recall &amp; Cost-Driven Evaluation:</strong> Performance is reported exclusively using Precision-Recall Area Under the Curve (PR-AUC), precision, recall, and total expected financial cost, measured strictly on held-out chronological test sets.</li>
  <li><strong>Cost-Optimal Operating Threshold Selection:</strong> Rather than assuming 0.50, the platform sweeps thresholds across a dedicated validation split against a rigorous financial cost objective:
  <pre><code>Total Expected Cost = (Count(FP) &times; Cost_FP) + &Sigma; (Amount_FN &times; Fraction_FN)</code></pre>
  The operating cutoff is frozen at the exact mathematical minimum (0.40) subject to a hard operational requirement of &ge;80% fraud recall.</li>
  <li><strong>Mathematically Grounded Explainability:</strong> Every scored transaction receives an attribution breakdown derived from exact tree-based Shapley values, verified by a mathematical additivity check on every API call.</li>
  <li><strong>Deterministic, Auditable Action Policy:</strong> A transparent five-rule cascade maps validated probabilities into four bounded operational recommendations (<code>ALLOW</code>, <code>ALLOW_WITH_MONITORING</code>, <code>STEP_UP_VERIFICATION</code>, <code>BLOCK</code>).</li>
</ol>

<h2 id="sec-2-4">2.4 Scope Boundaries: What Is In Scope vs. Deliberately Out of Scope</h2>
<p>
  To maintain engineering clarity and avoid architectural overreach, the repository establishes explicit functional boundaries:
</p>
<table>
  <thead>
    <tr>
      <th>Dimension</th>
      <th>Strictly In Scope (Implemented &amp; Verified)</th>
      <th>Deliberately Out of Scope (Prototype Boundaries)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Data Engineering</strong></td>
      <td>15 strictly-prior behavioral features computed across historical customer sequences.</td>
      <td>Live streaming Kafka/Flink infrastructure; real-time graph database queries.</td>
    </tr>
    <tr>
      <td><strong>Model Lifecycle</strong></td>
      <td>Chronological data partitioning; baseline vs. candidate benchmarking; frozen LightGBM artifact.</td>
      <td>Autonomous online retraining; dynamic real-time model hyperparameter updates.</td>
    </tr>
    <tr>
      <td><strong>Operational Decisioning</strong></td>
      <td>Transparent 5-rule policy table returning bounded operational recommendations.</td>
      <td>Irreversible financial actions; automated fund freezing; executing direct payment gateway refund APIs.</td>
    </tr>
    <tr>
      <td><strong>Explainability</strong></td>
      <td>SHAP TreeExplainer with additivity verification (1e-4) and grounded template generation.</td>
      <td>Unconstrained Large Language Model (LLM) narrative generation or conversational chat agents.</td>
    </tr>
    <tr>
      <td><strong>Persistence &amp; Audit</strong></td>
      <td>Local SQLite database capturing full decision facts, rule IDs, and SHAP narratives.</td>
      <td>Distributed enterprise SIEM integration; replication across multi-region PostgreSQL clusters.</td>
    </tr>
    <tr>
      <td><strong>Security &amp; Auth</strong></td>
      <td>Pydantic input shape validation; sanitization of non-finite inputs; zero PII persistence.</td>
      <td>OAuth2/OIDC user authentication; RBAC roles; TLS termination (assumed handled by reverse proxy).</td>
    </tr>
  </tbody>
</table>

<h2 id="sec-2-5">2.5 Conventional Approach vs. MerchantShield AI Architecture</h2>
<p>
  The following comparative matrix illustrates how MerchantShield AI replaces conventional industry practices with defensible software engineering patterns:
</p>
<table>
  <thead>
    <tr>
      <th>System Dimension</th>
      <th>Conventional Fraud Detection Approach</th>
      <th>MerchantShield AI Implementation Pattern</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Performance Reporting</strong></td>
      <td>Reports raw accuracy (e.g. "99% accurate") on imbalanced data, hiding severe false negative leakage.</td>
      <td>Reports <strong>PR-AUC, Precision, Recall, and Expected Rupee Cost</strong> on held-out chronological test partitions.</td>
    </tr>
    <tr>
      <td><strong>Threshold Selection</strong></td>
      <td>Defaults arbitrarily to <code>0.50</code>, or picks the F1-maximizing point (0.80) which ignores asymmetric cost.</td>
      <td><strong>Cost-Minimizing Validation Sweep:</strong> Threshold 0.40 selected mathematically to minimize FP/FN losses subject to &ge;80% recall.</td>
    </tr>
    <tr>
      <td><strong>Feature Engineering</strong></td>
      <td>Random cross-validation shuffles data, leaking future customer transactions into past feature averages.</td>
      <td><strong>Chronological Separation:</strong> All 15 features depend strictly on prior events (<code>timestamp &lt; current</code>), proven by automated leakage tests.</td>
    </tr>
    <tr>
      <td><strong>Decision Authority</strong></td>
      <td>The ML model directly triggers automated blocks, or an opaque score bucket drives arbitrary friction.</td>
      <td><strong>Decoupled Deterministic Policy:</strong> A 5-rule ordered table determines bounded action. SHAP cannot alter the action.</td>
    </tr>
    <tr>
      <td><strong>Reason Transparency</strong></td>
      <td>Black-box score output or hallucinated LLM explanations disconnected from mathematical model weights.</td>
      <td><strong>Grounded SHAP Attribution:</strong> Exact Shapley values verified on every call: <code>base_value + &Sigma;shap &approx; predict_proba</code>.</td>
    </tr>
    <tr>
      <td><strong>Audit Compliance</strong></td>
      <td>Transformed feature vectors or raw merchant PII dumped into unstructured application logs.</td>
      <td><strong>Governance-First Audit Store:</strong> Persists exact decision facts and SHAP text while strictly omitting customer PII.</td>
    </tr>
    <tr>
      <td><strong>Cold-Start Behavior</strong></td>
      <td>New customers produce unpredictable outlier z-scores or crash rolling window aggregations.</td>
      <td><strong>Explicit Cold-Start Guardrails:</strong> Sentinel defaults, history-dependent feature filtering, and transparent <code>signal_quality</code> grading.</td>
    </tr>
  </tbody>
</table>
'''
