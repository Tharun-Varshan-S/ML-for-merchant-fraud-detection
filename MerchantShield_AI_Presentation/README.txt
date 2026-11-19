================================================================================
MERCHANTSHIELD AI - TECHNICAL PRESENTATION PACKAGE
================================================================================

PROJECT:         MerchantShield AI
SUBTITLE:        Intelligent Merchant Risk Detection and Decision Support System
TARGET TRACK:    Razorpay AI Buildathon 2026 — Track 02 (AI Risk Manager)
INSTITUTION:     Sri Eshwar College of Engineering (SECE)
DEPARTMENT:      Department of Computer Science and Engineering / AI & ML
DELIVERABLE:     Professional 10-Slide Editable PowerPoint Presentation (.pptx)
LIVE SERVICE:    http://localhost:8000 | FastAPI Swagger Docs: http://localhost:8000/docs

--------------------------------------------------------------------------------
1. DIRECTORY STRUCTURE
--------------------------------------------------------------------------------
MerchantShield_AI_Presentation/
│
├── MerchantShield_AI_Presentation.pptx   [Primary Deliverable: 10 Widescreen 16:9 Slides]
├── MerchantShield_AI_Presentation.pdf    [Reference PDF Export for Cross-Platform Viewing]
│
├── screenshots/                          [Genuine Application Screenshots from Live App]
│   ├── dashboard.png                     (Live app overview on port 8000)
│   ├── merchant_interface.png            (Transaction evaluation form & scenario selector)
│   ├── explainability.png                (SHAP grounded explanation panel with contribution bars)
│   ├── audit_trail.png                   (Recent persisted decision table)
│   ├── api_docs.png                      (Interactive FastAPI Swagger UI at /docs)
│   ├── model_info.png                    (Frozen model metadata and test metrics panel)
│   ├── threshold_analysis.png            (Matplotlib validation cost and threshold sweep)
│   ├── critical_block_full_panel.png     (Clean viewport crop of CRITICAL_BLOCK scenario)
│   ├── low_risk_clean.png                (Clean viewport crop of LOW_ALLOW scenario)
│   ├── high_risk_clean.png               (Clean viewport crop of HIGH_STEP_UP scenario)
│   ├── shap_clean.png                    (Cropped grounded SHAP contribution breakdown)
│   └── audit_clean.png                   (Cropped SQLite audit log table)
│
├── presentation_assets/                  [Design System & Architecture Assets]
│   ├── ui_color_palette.txt              (Extracted HEX values matching tokens.css & App.css)
│   ├── architecture_diagram.png          (Full system architecture diagram)
│   ├── workflow_diagram.png              (7-stage end-to-end data pipeline)
│   ├── decision_policy_diagram.png       (5-rule deterministic policy state machine)
│   └── data_flow_diagram.png             (Component data flow diagram)
│
├── slide_previews/                       [High-Resolution 150 DPI Renderings of Slides 1-10]
│   ├── slide-01.png                      (Slide 1: Title Slide — Dark Shell Theme)
│   ├── slide-02.png                      (Slide 2: Project Overview & Core Mission)
│   ├── slide-03.png                      (Slide 3: Problem Statement & Industry Gaps)
│   ├── slide-04.png                      (Slide 4: Proposed System Workflow)
│   ├── slide-05.png                      (Slide 5: System Architecture & Technologies)
│   ├── slide-06.png                      (Slide 6: MerchantShield AI User Interface Showcase)
│   ├── slide-07.png                      (Slide 7: Decision Engine & Grounded Explainability)
│   ├── slide-08.png                      (Slide 8: Experimental Validation & Model Results)
│   ├── slide-09.png                      (Slide 9: Audit Trail, REST API & Docker Deployment)
│   └── slide-10.png                      (Slide 10: Conclusion, Technical Contributions & Roadmap)
│
└── README.txt                            [This documentation file]

--------------------------------------------------------------------------------
2. EXACT DESIGN SYSTEM & COLOR PALETTE
--------------------------------------------------------------------------------
Directly extracted from frontend/src/styles/tokens.css & App.css:

- Page Background:           #F0F2F5  (--bg)
- Dark Shell Header:         #0F1624  (--text-primary, used for app header & Slide 1)
- Card / Panel Surface:      #FFFFFF  (--surface, --surface-raised)
- Sunken Secondary Surface:  #F5F7FA  (--surface-sunken: header trims, tiles, table headers)
- Inset Surface:             #EEF0F4  (--surface-inset: tags, input tracks)
- Base Border:               #DDE1EA  (--border)
- Strong Border:             #C4CAD6  (--border-strong)
- Subtle Border:             #E8EAEF  (--border-subtle)

Brand Accents:
- Primary Brand Accent:      #2563EB  (--accent, Royal Blue)
- Accent Strong:             #1D4ED8  (--accent-strong)
- Accent Soft:               #DBEAFE  (--accent-soft, Pill background)
- Accent Muted:              #EFF6FF  (--accent-muted)

Risk Tiers & Operational Actions:
- LOW / ALLOW:               #16A34A  (Green, --risk-low)
- MEDIUM / MONITOR:          #D97706  (Amber, --risk-medium)
- HIGH / STEP_UP:            #EA580C  (Orange, --risk-high)
- CRITICAL / BLOCK:          #DC2626  (Crimson Red, --risk-critical)
- Live Operational Status:   #4ADE80  (Status dot green)

--------------------------------------------------------------------------------
3. SLIDE BREAKDOWN & VERIFIED METRICS
--------------------------------------------------------------------------------

SLIDE 1: TITLE SLIDE
- Dark Shell Theme (#0F1624) matching the live app header.
- Main title: MERCHANTSHIELD AI.
- Subtitle: Intelligent Merchant Risk Detection and Decision Support System.
- Embedded high-res browser mockup of the live application running on localhost:8000.
- Summary card featuring live model metadata: LightGBM v1 @ 0.40 threshold.
- Institutional & academic accreditation: Sri Eshwar College of Engineering (SECE).

SLIDE 2: PROJECT OVERVIEW
- Core Definition: End-to-end explainable transaction-risk decisioning system.
- Three foundational pillars: Leakage-Safe Feature Engineering, Grounded SHAP, and Independent Policy Governance.
- The Fraud Detection Trilemma: Extreme class imbalance (1.5%), arbitrary 0.50 thresholding, and black-box opacity.
- Four Bounded Actions: ALLOW, ALLOW_WITH_MONITORING, STEP_UP_VERIFICATION, and BLOCK.

SLIDE 3: PROBLEM STATEMENT
- 4 Critical Industry Vulnerabilities: Class Imbalance Fallacy, Cost-Agnostic Thresholding, Black-Box Compliance Void, and Prediction-Action Coupling.
- Structured Comparative Table: Industry Norm vs. MerchantShield AI approach across 6 key engineering dimensions.

SLIDE 4: PROPOSED SYSTEM WORKFLOW
- 6-Stage End-to-End Pipeline: Ingestion & Pydantic Validation -> Leakage-Safe Feature Engineering (15 features) -> LightGBM Inference Engine -> Dual-Track Evaluation (Risk Score & SHAP) -> 5-Rule Deterministic Policy -> Delivery & SQLite Audit Persistence.
- Deep dives on strictly-prior leakage regression tests and architectural decoupling.

SLIDE 5: SYSTEM ARCHITECTURE & TECHNOLOGIES
- Multi-tier topology diagram: Presentation (React 19/Vite), API Gateway (FastAPI/Uvicorn), Inference/XAI (LightGBM/SHAP), Decision/Audit (Policy Engine/SQLite).
- Native PowerPoint Table listing verified technologies, versions, and architectural responsibilities.

SLIDE 6: MERCHANTSHIELD AI USER INTERFACE
- Showcase of the genuine running user interface:
  * Primary Dashboard: Critical Block scenario with 99.9% probability, Score 100, and CRITICAL_BLOCK policy rule.
  * Supporting Visual 1: Routine Repeat Purchase (LOW tier, 0.0001 probability, ALLOW action).
  * Supporting Visual 2: New Device & Unfamiliar Region (HIGH tier, STEP_UP_VERIFICATION action).

SLIDE 7: DECISION ENGINE & GROUNDED EXPLAINABILITY
- 5-Rule Ordered Deterministic Policy Table: CRITICAL_BLOCK (prob >= 0.80), HIGH_STEP_UP (prob >= 0.40), MEDIUM_AMOUNT_ESCALATION (prob >= 0.15 & amt >= 25k), MEDIUM_MONITOR (prob >= 0.15), LOW_ALLOW (catch-all).
- SHAP TreeExplainer attributions with runtime additivity check (|base + sum(SHAP) - proba| < 0.0001).
- Screenshot of the real diverging horizontal contribution bars.

SLIDE 8: EXPERIMENTS, VALIDATION & MODEL RESULTS
- Comprehensive Held-Out Test Set Performance Table (Days 50-59 | 21,300 Transactions):
  * Logistic Regression (Baseline): Prec 0.448 | Rec 0.825 | F1 0.581 | PR-AUC 0.739 | FP 730 | FN 126 | Cost Rs 110,582
  * Random Forest Candidate:        Prec 0.746 | Rec 0.868 | F1 0.802 | PR-AUC 0.883 | FP 213 | FN 95  | Cost Rs 68,479
  * LightGBM Candidate (Selected):  Prec 0.785 | Rec 0.882 | F1 0.830 | PR-AUC 0.901 | FP 174 | FN 85  | Cost Rs 41,377
- Cost Function: FP = Rs 50 review cost; FN = 0.50 * transaction amount.
- 62.6% total business cost reduction compared to baseline.
- Honest External Validation (IEEE-CIS Real Data):
  * Frozen Model: ROC-AUC 0.443 (proves synthetic models cannot transfer directly).
  * Retrained Methodology: ROC-AUC 0.771, PR-AUC 0.128, caught 79.8% of real chargebacks (3,243 of 4,064).
  * Phase 15 Feature: card_product_share reduced false positives by 17.7% and total cost by 17.0%.
- Real matplotlib validation curve embedded.

SLIDE 9: AUDIT TRAIL, REST API & DOCKER DEPLOYMENT
- Immutable Audit Logging: SQLite persistence via SQLAlchemy (audit.db) storing full decision context while strictly omitting customer PII, device IDs, and geo strings.
- REST API Contract: Documented endpoints GET /health, GET /model/info, POST /risk/score, POST /risk/explain, POST /risk/evaluate, GET /audit-log.
- Containerization: Multi-stage Dockerfile (Node 22-slim builder -> Python 3.13-slim runtime) with Docker Compose and persistent audit_data volume.

SLIDE 10: CONCLUSION & FUTURE SCOPE
- Summary of core implemented achievements across the 5 pillars.
- Explicit demarcation of Future Scope: Graph-based syndicate detection, Apache Kafka streaming, automated drift monitoring (PSI), and distributed ledger persistence.
- Closing THANK YOU banner with SECE engineering institutional branding.

--------------------------------------------------------------------------------
4. VERIFICATION & QUALITY AUDIT
--------------------------------------------------------------------------------
- Slide Count: Exactly 10 slides.
- Aspect Ratio: 16:9 Widescreen (13.333 inches x 7.500 inches).
- Visual Fidelity: All shapes, panels, badges, tables, and typography match the real UI tokens.
- Native Shapes & Tables: Editable PowerPoint native shapes and tables used throughout.
- Screenshots: Genuine high-DPI screenshots captured directly from http://localhost:8000.
================================================================================
