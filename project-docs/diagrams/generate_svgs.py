#!/usr/bin/env python3
"""
Generate crisp, publication-grade SVG diagrams for the MerchantShield AI Project Understanding Book.
"""

import os

DIAGRAMS_DIR = os.path.dirname(os.path.abspath(__file__))

def create_architecture_svg():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 680" width="100%" height="100%" style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; background: #ffffff;">
  <defs>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#0f172a" flood-opacity="0.08"/>
    </filter>
    <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#475569"/>
    </marker>
    <marker id="arrow-primary" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#2563eb"/>
    </marker>
    <marker id="arrow-emerald" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#059669"/>
    </marker>
  </defs>

  <!-- Title & Subtitle -->
  <text x="500" y="32" text-anchor="middle" font-size="20" font-weight="700" fill="#0f172a">MerchantShield AI — High-Level System Architecture</text>
  <text x="500" y="52" text-anchor="middle" font-size="12" fill="#64748b">Decoupled ML probability estimation, grounded SHAP explainability, and deterministic policy governance</text>

  <!-- Tier 1: Client / Presentation Tier -->
  <rect x="40" y="80" width="920" height="90" rx="12" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="4 4"/>
  <text x="60" y="104" font-size="12" font-weight="700" fill="#475569" letter-spacing="1">TIER 1: CLIENT &amp; PRESENTATION (REACT 19 / VITE)</text>
  
  <rect x="60" y="115" width="410" height="42" rx="6" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5" filter="url(#shadow)"/>
  <text x="265" y="141" text-anchor="middle" font-size="13" font-weight="600" fill="#1e40af">React Dashboard UI (frontend/src/App.jsx)</text>

  <rect x="530" y="115" width="410" height="42" rx="6" fill="#f0fdf4" stroke="#22c55e" stroke-width="1.5" filter="url(#shadow)"/>
  <text x="735" y="141" text-anchor="middle" font-size="13" font-weight="600" fill="#166534">Sample Scenarios &amp; Manual Drafts (sampleScenarios.js)</text>

  <!-- Flow 1 to 2 -->
  <line x1="265" y1="157" x2="265" y2="200" stroke="#2563eb" stroke-width="2" marker-end="url(#arrow-primary)"/>
  <text x="275" y="184" font-size="11" font-weight="600" fill="#2563eb">HTTP POST /risk/evaluate (JSON)</text>

  <line x1="735" y1="200" x2="735" y2="157" stroke="#2563eb" stroke-width="2" marker-end="url(#arrow-primary)"/>
  <text x="745" y="184" font-size="11" font-weight="600" fill="#2563eb">HTTP 200 Structured Response</text>

  <!-- Tier 2: API Gateway & Validation -->
  <rect x="40" y="202" width="920" height="95" rx="12" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
  <text x="60" y="226" font-size="12" font-weight="700" fill="#475569" letter-spacing="1">TIER 2: API GATEWAY &amp; VALIDATION (FASTAPI / PYDANTIC V2)</text>

  <rect x="60" y="238" width="410" height="45" rx="6" fill="#ffffff" stroke="#0284c7" stroke-width="1.5" filter="url(#shadow)"/>
  <text x="265" y="258" text-anchor="middle" font-size="13" font-weight="600" fill="#0369a1">FastAPI Routers (backend/api/routes.py)</text>
  <text x="265" y="274" text-anchor="middle" font-size="11" fill="#64748b">/health, /model/info, /risk/score, /risk/explain, /risk/evaluate</text>

  <rect x="530" y="238" width="410" height="45" rx="6" fill="#ffffff" stroke="#0284c7" stroke-width="1.5" filter="url(#shadow)"/>
  <text x="735" y="258" text-anchor="middle" font-size="13" font-weight="600" fill="#0369a1">Schema Validation (backend/schemas/transaction.py)</text>
  <text x="735" y="274" text-anchor="middle" font-size="11" fill="#64748b">RiskRequest: Validates chronological timestamps &amp; customer match</text>

  <!-- Flow 2 to 3 -->
  <line x1="500" y1="297" x2="500" y2="330" stroke="#475569" stroke-width="2" marker-end="url(#arrow)"/>
  <text x="510" y="318" font-size="11" font-weight="600" fill="#475569">Validated Payload Passed to Service</text>

  <!-- Tier 3: Core Service Orchestration & ML Intelligence -->
  <rect x="40" y="332" width="920" height="195" rx="12" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
  <text x="60" y="356" font-size="12" font-weight="700" fill="#475569" letter-spacing="1">TIER 3: ORCHESTRATION &amp; ML INTELLIGENCE</text>

  <!-- Service Controller -->
  <rect x="60" y="368" width="880" height="34" rx="6" fill="#f1f5f9" stroke="#64748b" stroke-width="1.5"/>
  <text x="500" y="390" text-anchor="middle" font-size="12" font-weight="700" fill="#334155">backend/services/risk_service.py — Orchestrates Data Preparation &amp; Execution Pipeline</text>

  <!-- 4 Sub-boxes of Tier 3 -->
  <rect x="60" y="414" width="205" height="98" rx="6" fill="#ffffff" stroke="#059669" stroke-width="1.5" filter="url(#shadow)"/>
  <text x="162" y="435" text-anchor="middle" font-size="12" font-weight="700" fill="#065f46">Feature Engineering</text>
  <text x="162" y="452" text-anchor="middle" font-size="11" fill="#047857">ml/features/build_features.py</text>
  <text x="162" y="475" text-anchor="middle" font-size="10" fill="#334155">• 15 strictly-prior features</text>
  <text x="162" y="492" text-anchor="middle" font-size="10" fill="#334155">• Expanding running stats</text>
  <text x="162" y="504" text-anchor="middle" font-size="10" fill="#64748b">Leakage-safe (no future data)</text>

  <rect x="285" y="414" width="205" height="98" rx="6" fill="#ffffff" stroke="#d97706" stroke-width="1.5" filter="url(#shadow)"/>
  <text x="387" y="435" text-anchor="middle" font-size="12" font-weight="700" fill="#92400e">LightGBM Classifier</text>
  <text x="387" y="452" text-anchor="middle" font-size="11" fill="#b45309">candidate_lgbm_v1.pkl</text>
  <text x="387" y="475" text-anchor="middle" font-size="10" fill="#334155">• Frozen model artifact</text>
  <text x="387" y="492" text-anchor="middle" font-size="10" fill="#334155">• Output: raw P(fraud)</text>
  <text x="387" y="504" text-anchor="middle" font-size="10" fill="#64748b">Hardened: NaN/Inf/[0,1] check</text>

  <rect x="510" y="414" width="205" height="98" rx="6" fill="#ffffff" stroke="#7c3aed" stroke-width="1.5" filter="url(#shadow)"/>
  <text x="612" y="435" text-anchor="middle" font-size="12" font-weight="700" fill="#5b21b6">SHAP TreeExplainer</text>
  <text x="612" y="452" text-anchor="middle" font-size="11" fill="#6d28d9">ml/evaluation/explainability.py</text>
  <text x="612" y="475" text-anchor="middle" font-size="10" fill="#334155">• Grounded contributions</text>
  <text x="612" y="492" text-anchor="middle" font-size="10" fill="#334155">• Additivity verified (&lt;1e-4)</text>
  <text x="612" y="504" text-anchor="middle" font-size="10" fill="#64748b">Informational (never sets action)</text>

  <rect x="735" y="414" width="205" height="98" rx="6" fill="#ffffff" stroke="#0891b2" stroke-width="1.5" filter="url(#shadow)"/>
  <text x="837" y="435" text-anchor="middle" font-size="12" font-weight="700" fill="#155e75">Risk Scoring Display</text>
  <text x="837" y="452" text-anchor="middle" font-size="11" fill="#0e7490">ml/evaluation/risk_scoring.py</text>
  <text x="837" y="475" text-anchor="middle" font-size="10" fill="#334155">• Linear 0-100 risk score</text>
  <text x="837" y="492" text-anchor="middle" font-size="10" fill="#334155">• Tiers: LOW, MED, HIGH, CRIT</text>
  <text x="837" y="504" text-anchor="middle" font-size="10" fill="#64748b">Decoupled from action policy</text>

  <!-- Flow 3 to 4 -->
  <line x1="387" y1="512" x2="387" y2="550" stroke="#475569" stroke-width="2" marker-end="url(#arrow)"/>
  <text x="280" y="536" font-size="11" font-weight="600" fill="#0f172a">P(fraud), Amount</text>

  <line x1="612" y1="512" x2="612" y2="550" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="3 3" marker-end="url(#arrow)"/>
  <text x="620" y="536" font-size="10" fill="#64748b">Explanation Narrative (Audit Only)</text>

  <!-- Tier 4: Governance & Audit -->
  <rect x="40" y="552" width="920" height="105" rx="12" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
  <text x="60" y="576" font-size="12" font-weight="700" fill="#475569" letter-spacing="1">TIER 4: GOVERNANCE, POLICY &amp; AUDIT TRAIL</text>

  <rect x="60" y="588" width="410" height="52" rx="6" fill="#fff1f2" stroke="#e11d48" stroke-width="1.5" filter="url(#shadow)"/>
  <text x="265" y="609" text-anchor="middle" font-size="13" font-weight="700" fill="#9f1239">Deterministic Policy Engine (policy.py &amp; decision_engine.py)</text>
  <text x="265" y="627" text-anchor="middle" font-size="11" fill="#be123c">5-rule cascade: BLOCK, STEP_UP, MONITOR, ALLOW | Bound to cost threshold 0.40</text>

  <!-- Flow policy to audit -->
  <line x1="470" y1="614" x2="530" y2="614" stroke="#e11d48" stroke-width="2" marker-end="url(#arrow)"/>
  <text x="500" y="606" text-anchor="middle" font-size="10" font-weight="600" fill="#e11d48">Record</text>

  <rect x="530" y="588" width="410" height="52" rx="6" fill="#f8fafc" stroke="#475569" stroke-width="1.5" filter="url(#shadow)"/>
  <text x="735" y="609" text-anchor="middle" font-size="13" font-weight="700" fill="#1e293b">SQLite Audit Store (backend/services/audit_service.py)</text>
  <text x="735" y="627" text-anchor="middle" font-size="11" fill="#475569">Table audit_log: Persists decision facts &amp; SHAP text | Omits PII | Isolated error handling</text>

</svg>'''
    with open(os.path.join(DIAGRAMS_DIR, "architecture.svg"), "w") as f:
        f.write(svg)
    print("Created architecture.svg")


def create_pipeline_svg():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 700" width="100%" height="100%" style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; background: #ffffff;">
  <defs>
    <filter id="shadow2" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="2" stdDeviation="4" flood-color="#0f172a" flood-opacity="0.08"/>
    </filter>
    <marker id="arrow2" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#0284c7"/>
    </marker>
  </defs>

  <!-- Title -->
  <text x="500" y="32" text-anchor="middle" font-size="20" font-weight="700" fill="#0f172a">MerchantShield AI — 9-Stage Execution Pipeline</text>
  <text x="500" y="52" text-anchor="middle" font-size="12" fill="#64748b">End-to-end execution flow from application startup to final client delivery</text>

  <!-- Grid of 9 stages (3 rows of 3 stages) -->

  <!-- STAGE 1 -->
  <rect x="50" y="80" width="270" height="150" rx="8" fill="#f8fafc" stroke="#0284c7" stroke-width="1.5" filter="url(#shadow2)"/>
  <rect x="50" y="80" width="270" height="28" rx="8" fill="#0284c7"/>
  <text x="185" y="99" text-anchor="middle" font-size="12" font-weight="700" fill="#ffffff">STAGE 1: System Bootstrapping</text>
  <text x="65" y="125" font-size="11" font-weight="600" fill="#0f172a">File: backend/main.py lifespan</text>
  <text x="65" y="145" font-size="10.5" fill="#334155">• Loads candidate_lgbm_v1.pkl</text>
  <text x="65" y="163" font-size="10.5" fill="#334155">• Inits SHAP TreeExplainer</text>
  <text x="65" y="181" font-size="10.5" fill="#334155">• Inits SQLite AuditStore &amp; migrates</text>
  <text x="65" y="202" font-size="10" font-weight="600" fill="#0369a1">Graceful degradation: 503 on model failure</text>

  <!-- Arrow 1 to 2 -->
  <line x1="320" y1="155" x2="365" y2="155" stroke="#0284c7" stroke-width="2" marker-end="url(#arrow2)"/>

  <!-- STAGE 2 -->
  <rect x="365" y="80" width="270" height="150" rx="8" fill="#f8fafc" stroke="#0284c7" stroke-width="1.5" filter="url(#shadow2)"/>
  <rect x="365" y="80" width="270" height="28" rx="8" fill="#0284c7"/>
  <text x="500" y="99" text-anchor="middle" font-size="12" font-weight="700" fill="#ffffff">STAGE 2: Request Reception &amp; Validation</text>
  <text x="380" y="125" font-size="11" font-weight="600" fill="#0f172a">File: backend/schemas/transaction.py</text>
  <text x="380" y="145" font-size="10.5" fill="#334155">• Validates types, IDs, amounts &gt; 0</text>
  <text x="380" y="163" font-size="10.5" fill="#334155">• Checks prior transactions customer match</text>
  <text x="380" y="181" font-size="10.5" fill="#334155">• Strict timestamp check: prior &lt; current</text>
  <text x="380" y="202" font-size="10" font-weight="600" fill="#dc2626">Fails fast with HTTP 422 on shape error</text>

  <!-- Arrow 2 to 3 -->
  <line x1="635" y1="155" x2="680" y2="155" stroke="#0284c7" stroke-width="2" marker-end="url(#arrow2)"/>

  <!-- STAGE 3 -->
  <rect x="680" y="80" width="270" height="150" rx="8" fill="#f8fafc" stroke="#059669" stroke-width="1.5" filter="url(#shadow2)"/>
  <rect x="680" y="80" width="270" height="28" rx="8" fill="#059669"/>
  <text x="815" y="99" text-anchor="middle" font-size="12" font-weight="700" fill="#ffffff">STAGE 3: Feature Engineering</text>
  <text x="695" y="125" font-size="11" font-weight="600" fill="#0f172a">File: ml/features/build_features.py</text>
  <text x="695" y="145" font-size="10.5" fill="#334155">• 15 strictly-prior features computed</text>
  <text x="695" y="163" font-size="10.5" fill="#334155">• Velocity in 5m, 30m, 60m windows</text>
  <text x="695" y="181" font-size="10.5" fill="#334155">• Expanding mean/std &amp; amount z-score</text>
  <text x="695" y="202" font-size="10" font-weight="600" fill="#047857">Leakage-safe: Zero future data peek</text>

  <!-- Arrow 3 to 4 (Downwards) -->
  <path d="M 815 230 L 815 260 L 815 280" fill="none" stroke="#0284c7" stroke-width="2" marker-end="url(#arrow2)"/>

  <!-- STAGE 4 -->
  <rect x="680" y="285" width="270" height="150" rx="8" fill="#f8fafc" stroke="#d97706" stroke-width="1.5" filter="url(#shadow2)"/>
  <rect x="680" y="285" width="270" height="28" rx="8" fill="#d97706"/>
  <text x="815" y="304" text-anchor="middle" font-size="12" font-weight="700" fill="#ffffff">STAGE 4: Feature Bounds Checking</text>
  <text x="695" y="330" font-size="11" font-weight="600" fill="#0f172a">File: backend/services/risk_service.py</text>
  <text x="695" y="350" font-size="10.5" fill="#334155">• _validate_engineered_features()</text>
  <text x="695" y="368" font-size="10.5" fill="#334155">• Velocity caps (60m&lt;1000, 30m&lt;500)</text>
  <text x="695" y="386" font-size="10.5" fill="#334155">• Finite amount_zscore check (no NaN/Inf)</text>
  <text x="695" y="407" font-size="10" font-weight="600" fill="#b45309">V2 Hardening: Blocks pathological input</text>

  <!-- Arrow 4 to 5 (Leftwards) -->
  <line x1="680" y1="360" x2="635" y2="360" stroke="#0284c7" stroke-width="2" marker-end="url(#arrow2)"/>

  <!-- STAGE 5 -->
  <rect x="365" y="285" width="270" height="150" rx="8" fill="#f8fafc" stroke="#d97706" stroke-width="1.5" filter="url(#shadow2)"/>
  <rect x="365" y="285" width="270" height="28" rx="8" fill="#d97706"/>
  <text x="500" y="304" text-anchor="middle" font-size="12" font-weight="700" fill="#ffffff">STAGE 5: LightGBM Inference</text>
  <text x="380" y="330" font-size="11" font-weight="600" fill="#0f172a">File: candidate_lgbm_v1.pkl</text>
  <text x="380" y="350" font-size="10.5" fill="#334155">• predict_proba(X) on 15 features</text>
  <text x="380" y="368" font-size="10.5" fill="#334155">• Output validation: _validate_model_probability</text>
  <text x="380" y="386" font-size="10.5" fill="#334155">• Asserts finite float in [0.0, 1.0]</text>
  <text x="380" y="407" font-size="10" font-weight="600" fill="#b45309">V2 Hardening: No NaN / Inf propagation</text>

  <!-- Arrow 5 to 6 (Leftwards) -->
  <line x1="365" y1="360" x2="320" y2="360" stroke="#0284c7" stroke-width="2" marker-end="url(#arrow2)"/>

  <!-- STAGE 6 -->
  <rect x="50" y="285" width="270" height="150" rx="8" fill="#f8fafc" stroke="#7c3aed" stroke-width="1.5" filter="url(#shadow2)"/>
  <rect x="50" y="285" width="270" height="28" rx="8" fill="#7c3aed"/>
  <text x="185" y="304" text-anchor="middle" font-size="12" font-weight="700" fill="#ffffff">STAGE 6: Grounded SHAP Explanation</text>
  <text x="65" y="330" font-size="11" font-weight="600" fill="#0f172a">File: ml/evaluation/explainability.py</text>
  <text x="65" y="350" font-size="10.5" fill="#334155">• TreeExplainer calculates Shapley values</text>
  <text x="65" y="368" font-size="10.5" fill="#334155">• Mathematical additivity check (|&Delta;|&lt;1e-4)</text>
  <text x="65" y="386" font-size="10.5" fill="#334155">• Grounded natural language narratives</text>
  <text x="65" y="407" font-size="10" font-weight="600" fill="#6d28d9">Cold-start awareness: excludes 0-history stats</text>

  <!-- Arrow 6 to 7 (Downwards) -->
  <path d="M 185 435 L 185 465 L 185 485" fill="none" stroke="#0284c7" stroke-width="2" marker-end="url(#arrow2)"/>

  <!-- STAGE 7 -->
  <rect x="50" y="490" width="270" height="150" rx="8" fill="#f8fafc" stroke="#e11d48" stroke-width="1.5" filter="url(#shadow2)"/>
  <rect x="50" y="490" width="270" height="28" rx="8" fill="#e11d48"/>
  <text x="185" y="509" text-anchor="middle" font-size="12" font-weight="700" fill="#ffffff">STAGE 7: Deterministic Policy Evaluation</text>
  <text x="65" y="535" font-size="11" font-weight="600" fill="#0f172a">File: ml/evaluation/policy.py</text>
  <text x="65" y="555" font-size="10.5" fill="#334155">• 5-rule ordered table (first match wins)</text>
  <text x="65" y="573" font-size="10.5" fill="#334155">• CRITICAL_BLOCK (p&ge;0.80) &rarr; BLOCK</text>
  <text x="65" y="591" font-size="10.5" fill="#334155">• HIGH_STEP_UP (p&ge;0.40) &rarr; STEP_UP</text>
  <text x="65" y="612" font-size="10" font-weight="600" fill="#be123c">SHAP structurally isolated from action</text>

  <!-- Arrow 7 to 8 (Rightwards) -->
  <line x1="320" y1="565" x2="365" y2="565" stroke="#0284c7" stroke-width="2" marker-end="url(#arrow2)"/>

  <!-- STAGE 8 -->
  <rect x="365" y="490" width="270" height="150" rx="8" fill="#f8fafc" stroke="#475569" stroke-width="1.5" filter="url(#shadow2)"/>
  <rect x="365" y="490" width="270" height="28" rx="8" fill="#475569"/>
  <text x="500" y="509" text-anchor="middle" font-size="12" font-weight="700" fill="#ffffff">STAGE 8: Audit Persistence</text>
  <text x="380" y="535" font-size="11" font-weight="600" fill="#0f172a">File: backend/services/audit_service.py</text>
  <text x="380" y="555" font-size="10.5" fill="#334155">• Writes DecisionRecord to SQLite</text>
  <text x="380" y="573" font-size="10.5" fill="#334155">• Separates decision facts &amp; SHAP text</text>
  <text x="380" y="591" font-size="10.5" fill="#334155">• Zero PII stored (no customer/device/geo)</text>
  <text x="380" y="612" font-size="10" font-weight="600" fill="#334155">Failure isolation: Never drops risk decision</text>

  <!-- Arrow 8 to 9 (Rightwards) -->
  <line x1="635" y1="565" x2="680" y2="565" stroke="#0284c7" stroke-width="2" marker-end="url(#arrow2)"/>

  <!-- STAGE 9 -->
  <rect x="680" y="490" width="270" height="150" rx="8" fill="#f8fafc" stroke="#0284c7" stroke-width="1.5" filter="url(#shadow2)"/>
  <rect x="680" y="490" width="270" height="28" rx="8" fill="#0284c7"/>
  <text x="815" y="509" text-anchor="middle" font-size="12" font-weight="700" fill="#ffffff">STAGE 9: Response Assembly &amp; UI</text>
  <text x="695" y="535" font-size="11" font-weight="600" fill="#0f172a">File: RiskEvaluateResponse &amp; App.jsx</text>
  <text x="695" y="555" font-size="10.5" fill="#334155">• Bundles probability, action, rule ID</text>
  <text x="695" y="573" font-size="10.5" fill="#334155">• Includes signal_quality &amp; cold_start</text>
  <text x="695" y="591" font-size="10.5" fill="#334155">• Frontend renders verbatim action badge</text>
  <text x="695" y="612" font-size="10" font-weight="600" fill="#0369a1">Auditable delivery: Clean JSON contract</text>

</svg>'''
    with open(os.path.join(DIAGRAMS_DIR, "pipeline.svg"), "w") as f:
        f.write(svg)
    print("Created pipeline.svg")


def create_decision_policy_svg():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 520" width="100%" height="100%" style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; background: #ffffff;">
  <defs>
    <filter id="shadow3" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="2" stdDeviation="4" flood-color="#0f172a" flood-opacity="0.08"/>
    </filter>
    <marker id="arrow3" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#475569"/>
    </marker>
    <marker id="arrow-red" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#dc2626"/>
    </marker>
    <marker id="arrow-green" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#16a34a"/>
    </marker>
  </defs>

  <!-- Title -->
  <text x="450" y="32" text-anchor="middle" font-size="18" font-weight="700" fill="#0f172a">The 5-Rule Deterministic Policy Cascade (First Match Wins)</text>
  <text x="450" y="52" text-anchor="middle" font-size="12" fill="#64748b">Source of truth: ml/evaluation/policy.py — Evaluated on (probability, amount) only</text>

  <!-- Start Node -->
  <rect x="50" y="80" width="160" height="40" rx="20" fill="#0f172a" filter="url(#shadow3)"/>
  <text x="130" y="105" text-anchor="middle" font-size="13" font-weight="700" fill="#ffffff">evaluate_policy(p, amt)</text>

  <!-- Rule 1: CRITICAL_BLOCK -->
  <line x1="130" y1="120" x2="130" y2="150" stroke="#475569" stroke-width="2" marker-end="url(#arrow3)"/>
  <rect x="50" y="150" width="160" height="50" rx="8" fill="#ffffff" stroke="#e11d48" stroke-width="2" filter="url(#shadow3)"/>
  <text x="130" y="172" text-anchor="middle" font-size="12" font-weight="700" fill="#9f1239">Rule 1: CRITICAL</text>
  <text x="130" y="190" text-anchor="middle" font-size="12" font-weight="600" fill="#0f172a">p &ge; 0.80 ?</text>

  <line x1="210" y1="175" x2="480" y2="175" stroke="#dc2626" stroke-width="2" marker-end="url(#arrow-red)"/>
  <text x="320" y="168" text-anchor="middle" font-size="11" font-weight="700" fill="#dc2626">YES (Val Precision 94.1%)</text>
  <rect x="480" y="152" width="370" height="46" rx="6" fill="#fef2f2" stroke="#dc2626" stroke-width="1.5"/>
  <text x="495" y="173" font-size="12" font-weight="700" fill="#991b1b">ACTION: BLOCK</text>
  <text x="495" y="189" font-size="10.5" fill="#7f1d1d">Rule ID: CRITICAL_BLOCK | Outright hold for human review</text>

  <!-- Rule 2: HIGH_STEP_UP -->
  <line x1="130" y1="200" x2="130" y2="230" stroke="#475569" stroke-width="2" marker-end="url(#arrow3)"/>
  <text x="140" y="218" font-size="10" font-weight="600" fill="#64748b">NO</text>
  <rect x="50" y="230" width="160" height="50" rx="8" fill="#ffffff" stroke="#d97706" stroke-width="2" filter="url(#shadow3)"/>
  <text x="130" y="252" text-anchor="middle" font-size="12" font-weight="700" fill="#92400e">Rule 2: HIGH</text>
  <text x="130" y="270" text-anchor="middle" font-size="12" font-weight="600" fill="#0f172a">p &ge; 0.40 ?</text>

  <line x1="210" y1="255" x2="480" y2="255" stroke="#d97706" stroke-width="2" marker-end="url(#arrow3)"/>
  <text x="320" y="248" text-anchor="middle" font-size="11" font-weight="700" fill="#d97706">YES (Frozen Decision Threshold)</text>
  <rect x="480" y="232" width="370" height="46" rx="6" fill="#fffbeb" stroke="#d97706" stroke-width="1.5"/>
  <text x="495" y="253" font-size="12" font-weight="700" fill="#92400e">ACTION: STEP_UP_VERIFICATION</text>
  <text x="495" y="269" font-size="10.5" fill="#78350f">Rule ID: HIGH_STEP_UP | Cost-optimal threshold operating point</text>

  <!-- Rule 3: MEDIUM_AMOUNT_ESCALATION -->
  <line x1="130" y1="280" x2="130" y2="310" stroke="#475569" stroke-width="2" marker-end="url(#arrow3)"/>
  <text x="140" y="298" font-size="10" font-weight="600" fill="#64748b">NO</text>
  <rect x="50" y="310" width="160" height="50" rx="8" fill="#ffffff" stroke="#f59e0b" stroke-width="2" filter="url(#shadow3)"/>
  <text x="130" y="330" text-anchor="middle" font-size="11" font-weight="700" fill="#b45309">Rule 3: ESCALATION</text>
  <text x="130" y="348" text-anchor="middle" font-size="11" font-weight="600" fill="#0f172a">p &ge; 0.15 &amp; amt &ge; ₹25k?</text>

  <line x1="210" y1="335" x2="480" y2="335" stroke="#d97706" stroke-width="2" marker-end="url(#arrow3)"/>
  <text x="320" y="328" text-anchor="middle" font-size="11" font-weight="700" fill="#d97706">YES (High Financial Exposure)</text>
  <rect x="480" y="312" width="370" height="46" rx="6" fill="#fffbeb" stroke="#f59e0b" stroke-width="1.5"/>
  <text x="495" y="333" font-size="12" font-weight="700" fill="#92400e">ACTION: STEP_UP_VERIFICATION</text>
  <text x="495" y="349" font-size="10.5" fill="#78350f">Rule ID: MEDIUM_AMOUNT_ESCALATION | High loss downside check</text>

  <!-- Rule 4: MEDIUM_MONITOR -->
  <line x1="130" y1="360" x2="130" y2="390" stroke="#475569" stroke-width="2" marker-end="url(#arrow3)"/>
  <text x="140" y="378" font-size="10" font-weight="600" fill="#64748b">NO</text>
  <rect x="50" y="390" width="160" height="50" rx="8" fill="#ffffff" stroke="#0284c7" stroke-width="2" filter="url(#shadow3)"/>
  <text x="130" y="412" text-anchor="middle" font-size="12" font-weight="700" fill="#0369a1">Rule 4: MEDIUM</text>
  <text x="130" y="430" text-anchor="middle" font-size="12" font-weight="600" fill="#0f172a">p &ge; 0.15 ?</text>

  <line x1="210" y1="415" x2="480" y2="415" stroke="#0284c7" stroke-width="2" marker-end="url(#arrow3)"/>
  <text x="320" y="408" text-anchor="middle" font-size="11" font-weight="700" fill="#0284c7">YES (Elevated Risk Above Floor)</text>
  <rect x="480" y="392" width="370" height="46" rx="6" fill="#f0f9ff" stroke="#0284c7" stroke-width="1.5"/>
  <text x="495" y="413" font-size="12" font-weight="700" fill="#0369a1">ACTION: ALLOW_WITH_MONITORING</text>
  <text x="495" y="429" font-size="10.5" fill="#0c4a6e">Rule ID: MEDIUM_MONITOR | Allowed with passive observation flag</text>

  <!-- Rule 5: LOW_ALLOW -->
  <line x1="130" y1="440" x2="130" y2="470" stroke="#475569" stroke-width="2" marker-end="url(#arrow3)"/>
  <text x="140" y="458" font-size="10" font-weight="600" fill="#64748b">NO (p &lt; 0.15)</text>
  <rect x="50" y="470" width="160" height="40" rx="8" fill="#f0fdf4" stroke="#16a34a" stroke-width="2" filter="url(#shadow3)"/>
  <text x="130" y="495" text-anchor="middle" font-size="12" font-weight="700" fill="#15803d">Rule 5: LOW (Catch-all)</text>

  <line x1="210" y1="490" x2="480" y2="490" stroke="#16a34a" stroke-width="2" marker-end="url(#arrow-green)"/>
  <text x="320" y="483" text-anchor="middle" font-size="11" font-weight="700" fill="#16a34a">Catch-all Default</text>
  <rect x="480" y="468" width="370" height="44" rx="6" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.5"/>
  <text x="495" y="488" font-size="12" font-weight="700" fill="#15803d">ACTION: ALLOW</text>
  <text x="495" y="504" font-size="10.5" fill="#14532d">Rule ID: LOW_ALLOW | Zero friction, transaction permitted</text>

</svg>'''
    with open(os.path.join(DIAGRAMS_DIR, "decision_policy.svg"), "w") as f:
        f.write(svg)
    print("Created decision_policy.svg")


def create_database_schema_svg():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 620" width="100%" height="100%" style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; background: #ffffff;">
  <defs>
    <filter id="shadow4" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="3" stdDeviation="5" flood-color="#0f172a" flood-opacity="0.08"/>
    </filter>
  </defs>

  <!-- Title -->
  <text x="400" y="32" text-anchor="middle" font-size="18" font-weight="700" fill="#0f172a">SQLite Audit Log Entity Design (backend/data/audit.db)</text>
  <text x="400" y="52" text-anchor="middle" font-size="12" fill="#64748b">Defensive governance storage: Durably preserves WHAT &amp; WHY while strictly omitting customer PII</text>

  <!-- Table Container -->
  <rect x="60" y="80" width="680" height="510" rx="10" fill="#ffffff" stroke="#475569" stroke-width="2" filter="url(#shadow4)"/>
  
  <!-- Table Header -->
  <rect x="60" y="80" width="680" height="42" rx="10" fill="#1e293b"/>
  <text x="85" y="106" font-size="15" font-weight="700" fill="#f8fafc">TABLE: audit_log</text>
  <text x="715" y="106" text-anchor="end" font-size="12" fill="#94a3b8">SQLAlchemy Model: AuditLogEntry</text>

  <!-- Column Header Row -->
  <rect x="60" y="122" width="680" height="30" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1"/>
  <text x="85" y="142" font-size="11" font-weight="700" fill="#475569">COLUMN NAME</text>
  <text x="270" y="142" font-size="11" font-weight="700" fill="#475569">SQL TYPE</text>
  <text x="410" y="142" font-size="11" font-weight="700" fill="#475569">INDEX / NULL</text>
  <text x="540" y="142" font-size="11" font-weight="700" fill="#475569">GOVERNANCE PURPOSE</text>

  <!-- Rows -->
  <!-- 1. id -->
  <text x="85" y="172" font-size="12" font-weight="700" fill="#0f172a">id</text>
  <text x="270" y="172" font-size="12" fill="#334155">INTEGER</text>
  <text x="410" y="172" font-size="11" font-weight="600" fill="#0284c7">PRIMARY KEY</text>
  <text x="540" y="172" font-size="11" fill="#64748b">Auto-increment row ID</text>
  <line x1="60" y1="184" x2="740" y2="184" stroke="#f1f5f9" stroke-width="1"/>

  <!-- 2. request_id -->
  <text x="85" y="202" font-size="12" font-weight="600" fill="#0f172a">request_id</text>
  <text x="270" y="202" font-size="12" fill="#334155">VARCHAR(64)</text>
  <text x="410" y="202" font-size="11" font-weight="600" fill="#475569">INDEXED, NOT NULL</text>
  <text x="540" y="202" font-size="11" fill="#64748b">UUID4 API transaction trace ID</text>
  <line x1="60" y1="214" x2="740" y2="214" stroke="#f1f5f9" stroke-width="1"/>

  <!-- 3. transaction_id -->
  <text x="85" y="232" font-size="12" font-weight="600" fill="#0f172a">transaction_id</text>
  <text x="270" y="232" font-size="12" fill="#334155">VARCHAR(64)</text>
  <text x="410" y="232" font-size="11" font-weight="600" fill="#475569">INDEXED, NOT NULL</text>
  <text x="540" y="232" font-size="11" fill="#64748b">Merchant transaction identifier</text>
  <line x1="60" y1="244" x2="740" y2="244" stroke="#f1f5f9" stroke-width="1"/>

  <!-- 4. model_version -->
  <text x="85" y="262" font-size="12" font-weight="600" fill="#0f172a">model_version</text>
  <text x="270" y="262" font-size="12" fill="#334155">VARCHAR(32)</text>
  <text x="410" y="262" font-size="11" fill="#64748b">NOT NULL</text>
  <text x="540" y="262" font-size="11" fill="#64748b">Frozen model identifier ("lgbm_v1")</text>
  <line x1="60" y1="274" x2="740" y2="274" stroke="#f1f5f9" stroke-width="1"/>

  <!-- 5. fraud_probability -->
  <text x="85" y="292" font-size="12" font-weight="600" fill="#0f172a">fraud_probability</text>
  <text x="270" y="292" font-size="12" fill="#334155">FLOAT</text>
  <text x="410" y="292" font-size="11" fill="#64748b">NOT NULL</text>
  <text x="540" y="292" font-size="11" fill="#64748b">Raw predicted probability [0.0 - 1.0]</text>
  <line x1="60" y1="304" x2="740" y2="304" stroke="#f1f5f9" stroke-width="1"/>

  <!-- 6. threshold -->
  <text x="85" y="322" font-size="12" font-weight="600" fill="#0f172a">threshold</text>
  <text x="270" y="322" font-size="12" fill="#334155">FLOAT</text>
  <text x="410" y="322" font-size="11" fill="#64748b">NOT NULL</text>
  <text x="540" y="322" font-size="11" fill="#64748b">Cost-optimal boundary (0.40)</text>
  <line x1="60" y1="334" x2="740" y2="334" stroke="#f1f5f9" stroke-width="1"/>

  <!-- 7. risk_score & category -->
  <text x="85" y="352" font-size="12" font-weight="600" fill="#0f172a">risk_score / category</text>
  <text x="270" y="352" font-size="12" fill="#334155">INTEGER / VARCHAR</text>
  <text x="410" y="352" font-size="11" fill="#64748b">NOT NULL</text>
  <text x="540" y="352" font-size="11" fill="#64748b">0-100 score + LOW/MED/HIGH/CRIT</text>
  <line x1="60" y1="364" x2="740" y2="364" stroke="#f1f5f9" stroke-width="1"/>

  <!-- 8. action -->
  <text x="85" y="382" font-size="12" font-weight="700" fill="#dc2626">action</text>
  <text x="270" y="382" font-size="12" fill="#334155">VARCHAR(32)</text>
  <text x="410" y="382" font-size="11" fill="#64748b">NOT NULL</text>
  <text x="540" y="382" font-size="11" font-weight="600" fill="#dc2626">ALLOW / STEP_UP / BLOCK</text>
  <line x1="60" y1="394" x2="740" y2="394" stroke="#f1f5f9" stroke-width="1"/>

  <!-- 9. policy_rule_id & reason -->
  <text x="85" y="412" font-size="12" font-weight="600" fill="#0f172a">policy_rule_id / reason</text>
  <text x="270" y="412" font-size="12" fill="#334155">VARCHAR / TEXT</text>
  <text x="410" y="412" font-size="11" fill="#64748b">NOT NULL</text>
  <text x="540" y="412" font-size="11" fill="#64748b">Exact rule triggered &amp; rationale text</text>
  <line x1="60" y1="424" x2="740" y2="424" stroke="#f1f5f9" stroke-width="1"/>

  <!-- 10. top_reasons_json -->
  <text x="85" y="442" font-size="12" font-weight="700" fill="#7c3aed">top_reasons_json</text>
  <text x="270" y="442" font-size="12" fill="#334155">TEXT</text>
  <text x="410" y="442" font-size="11" fill="#64748b">NULLABLE</text>
  <text x="540" y="442" font-size="11" font-weight="600" fill="#7c3aed">Separated SHAP explanation JSON</text>
  <line x1="60" y1="454" x2="740" y2="454" stroke="#f1f5f9" stroke-width="1"/>

  <!-- 11. source & prior_txn_count -->
  <text x="85" y="472" font-size="12" font-weight="600" fill="#0f172a">source / prior_txn_count</text>
  <text x="270" y="472" font-size="12" fill="#334155">VARCHAR / INTEGER</text>
  <text x="410" y="472" font-size="11" fill="#64748b">NOT NULL</text>
  <text x="540" y="472" font-size="11" fill="#64748b">Origin ("demo"|"manual") &amp; V2 context</text>
  <line x1="60" y1="484" x2="740" y2="484" stroke="#f1f5f9" stroke-width="1"/>

  <!-- 12. created_at -->
  <text x="85" y="502" font-size="12" font-weight="600" fill="#0f172a">created_at</text>
  <text x="270" y="502" font-size="12" fill="#334155">DATETIME</text>
  <text x="410" y="502" font-size="11" fill="#64748b">NOT NULL</text>
  <text x="540" y="502" font-size="11" fill="#64748b">Record persistence timestamp (UTC)</text>
  <line x1="60" y1="514" x2="740" y2="514" stroke="#cbd5e1" stroke-width="1"/>

  <!-- Footer Annotation -->
  <rect x="60" y="525" width="680" height="65" fill="#f8fafc"/>
  <text x="85" y="546" font-size="11" font-weight="700" fill="#b91c1c">DELIBERATELY OMITTED FROM AUDIT STORAGE:</text>
  <text x="85" y="564" font-size="10.5" fill="#475569">• customer_id, device_id, geo_region, payment_method, merchant_id, account_created</text>
  <text x="85" y="580" font-size="10" fill="#64748b">Rationale: Audit trail's purpose is to prove what the RISK SYSTEM decided and why, avoiding merchant PII duplication.</text>

</svg>'''
    with open(os.path.join(DIAGRAMS_DIR, "database_schema.svg"), "w") as f:
        f.write(svg)
    print("Created database_schema.svg")


def create_data_flow_svg():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 640" width="100%" height="100%" style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; background: #ffffff;">
  <defs>
    <filter id="shadow5" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="2" stdDeviation="4" flood-color="#0f172a" flood-opacity="0.08"/>
    </filter>
    <marker id="arrow-flow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#0284c7"/>
    </marker>
    <marker id="arrow-green-flow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#16a34a"/>
    </marker>
  </defs>

  <!-- Title -->
  <text x="460" y="32" text-anchor="middle" font-size="18" font-weight="700" fill="#0f172a">MerchantShield AI — End-to-End Sequence &amp; Data Flow</text>
  <text x="460" y="52" text-anchor="middle" font-size="12" fill="#64748b">Step-by-step transaction evaluation showing exact component interactions and isolation boundaries</text>

  <!-- Lifeline Columns -->
  <!-- Col 1: Client (React) -->
  <line x1="80" y1="80" x2="80" y2="600" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="4 4"/>
  <rect x="25" y="80" width="110" height="34" rx="6" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>
  <text x="80" y="102" text-anchor="middle" font-size="12" font-weight="700" fill="#1d4ed8">React UI</text>

  <!-- Col 2: FastAPI -->
  <line x1="230" y1="80" x2="230" y2="600" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="4 4"/>
  <rect x="175" y="80" width="110" height="34" rx="6" fill="#f0f9ff" stroke="#0284c7" stroke-width="1.5"/>
  <text x="230" y="102" text-anchor="middle" font-size="12" font-weight="700" fill="#0369a1">FastAPI</text>

  <!-- Col 3: Risk Service -->
  <line x1="390" y1="80" x2="390" y2="600" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="4 4"/>
  <rect x="330" y="80" width="120" height="34" rx="6" fill="#f8fafc" stroke="#475569" stroke-width="1.5"/>
  <text x="390" y="102" text-anchor="middle" font-size="12" font-weight="700" fill="#334155">Risk Service</text>

  <!-- Col 4: ML & Features -->
  <line x1="550" y1="80" x2="550" y2="600" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="4 4"/>
  <rect x="495" y="80" width="110" height="34" rx="6" fill="#fefce8" stroke="#ca8a04" stroke-width="1.5"/>
  <text x="550" y="102" text-anchor="middle" font-size="12" font-weight="700" fill="#854d0e">Features / ML</text>

  <!-- Col 5: Policy & Decision -->
  <line x1="700" y1="80" x2="700" y2="600" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="4 4"/>
  <rect x="645" y="80" width="110" height="34" rx="6" fill="#fff1f2" stroke="#e11d48" stroke-width="1.5"/>
  <text x="700" y="102" text-anchor="middle" font-size="12" font-weight="700" fill="#9f1239">Policy Engine</text>

  <!-- Col 6: SQLite DB -->
  <line x1="840" y1="80" x2="840" y2="600" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="4 4"/>
  <rect x="785" y="80" width="110" height="34" rx="6" fill="#f8fafc" stroke="#64748b" stroke-width="1.5"/>
  <text x="840" y="102" text-anchor="middle" font-size="12" font-weight="700" fill="#1e293b">SQLite Audit</text>

  <!-- Sequence Step 1 -->
  <line x1="80" y1="140" x2="230" y2="140" stroke="#0284c7" stroke-width="2" marker-end="url(#arrow-flow)"/>
  <text x="155" y="132" text-anchor="middle" font-size="10.5" font-weight="600" fill="#0284c7">1. POST /risk/evaluate</text>

  <!-- Sequence Step 2 -->
  <line x1="230" y1="180" x2="390" y2="180" stroke="#0284c7" stroke-width="2" marker-end="url(#arrow-flow)"/>
  <text x="310" y="172" text-anchor="middle" font-size="10.5" font-weight="600" fill="#0284c7">2. evaluate_full(bundle, req)</text>

  <!-- Sequence Step 3 -->
  <line x1="390" y1="220" x2="550" y2="220" stroke="#0284c7" stroke-width="2" marker-end="url(#arrow-flow)"/>
  <text x="470" y="212" text-anchor="middle" font-size="10.5" font-weight="600" fill="#0284c7">3. build_features(df)</text>

  <line x1="550" y1="250" x2="390" y2="250" stroke="#64748b" stroke-width="1.5" stroke-dasharray="3 3" marker-end="url(#arrow-flow)"/>
  <text x="470" y="244" text-anchor="middle" font-size="10" fill="#64748b">15 feature series (row)</text>

  <!-- Sequence Step 4 -->
  <line x1="390" y1="285" x2="550" y2="285" stroke="#ca8a04" stroke-width="2" marker-end="url(#arrow-flow)"/>
  <text x="470" y="277" text-anchor="middle" font-size="10.5" font-weight="600" fill="#854d0e">4. predict_proba(X)</text>

  <line x1="550" y1="315" x2="390" y2="315" stroke="#ca8a04" stroke-width="1.5" stroke-dasharray="3 3" marker-end="url(#arrow-flow)"/>
  <text x="470" y="309" text-anchor="middle" font-size="10" fill="#854d0e">P(fraud) = 0.9997</text>

  <!-- Sequence Step 5 (Decision happens BEFORE SHAP) -->
  <line x1="390" y1="355" x2="700" y2="355" stroke="#e11d48" stroke-width="2" marker-end="url(#arrow-flow)"/>
  <text x="545" y="347" text-anchor="middle" font-size="10.5" font-weight="700" fill="#be123c">5. evaluate_policy(0.9997, 45000)</text>

  <line x1="700" y1="385" x2="390" y2="385" stroke="#e11d48" stroke-width="1.5" stroke-dasharray="3 3" marker-end="url(#arrow-flow)"/>
  <text x="545" y="379" text-anchor="middle" font-size="10" font-weight="600" fill="#be123c">DecisionRecord: ACTION=BLOCK, Rule=CRITICAL_BLOCK</text>

  <!-- Sequence Step 6 (SHAP explanation attempted) -->
  <line x1="390" y1="425" x2="550" y2="425" stroke="#7c3aed" stroke-width="2" marker-end="url(#arrow-flow)"/>
  <text x="470" y="417" text-anchor="middle" font-size="10.5" font-weight="600" fill="#6d28d9">6. explainer.explain(row)</text>

  <line x1="550" y1="455" x2="390" y2="455" stroke="#7c3aed" stroke-width="1.5" stroke-dasharray="3 3" marker-end="url(#arrow-flow)"/>
  <text x="470" y="449" text-anchor="middle" font-size="10" fill="#6d28d9">SHAP values + grounded reasons</text>

  <!-- Sequence Step 7: Return to API -->
  <line x1="390" y1="485" x2="230" y2="485" stroke="#64748b" stroke-width="1.5" stroke-dasharray="3 3" marker-end="url(#arrow-flow)"/>
  <text x="310" y="477" text-anchor="middle" font-size="10" fill="#334155">Decision + Explanation tuple</text>

  <!-- Sequence Step 8: Isolated Audit Write -->
  <line x1="230" y1="515" x2="840" y2="515" stroke="#475569" stroke-width="2" marker-end="url(#arrow-flow)"/>
  <text x="535" y="507" text-anchor="middle" font-size="10.5" font-weight="600" fill="#334155">8. audit_store.record_decision() [Isolated try/except]</text>

  <line x1="840" y1="545" x2="230" y2="545" stroke="#16a34a" stroke-width="1.5" stroke-dasharray="3 3" marker-end="url(#arrow-green-flow)"/>
  <text x="535" y="539" text-anchor="middle" font-size="10" font-weight="600" fill="#15803d">Audit persisted: true (or false with warning)</text>

  <!-- Sequence Step 9: Final HTTP Response -->
  <line x1="230" y1="580" x2="80" y2="580" stroke="#16a34a" stroke-width="2" marker-end="url(#arrow-green-flow)"/>
  <text x="155" y="572" text-anchor="middle" font-size="10.5" font-weight="700" fill="#15803d">9. HTTP 200 (RiskEvaluateResponse)</text>

</svg>'''
    with open(os.path.join(DIAGRAMS_DIR, "data_flow.svg"), "w") as f:
        f.write(svg)
    print("Created data_flow.svg")


if __name__ == "__main__":
    create_architecture_svg()
    create_pipeline_svg()
    create_decision_policy_svg()
    create_database_schema_svg()
    create_data_flow_svg()
    print("All diagrams generated successfully!")
