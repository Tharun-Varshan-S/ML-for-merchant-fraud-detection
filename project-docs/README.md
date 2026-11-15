# MerchantShield AI — Project Understanding & Technical Learning Book

This directory contains the complete source code, vector diagrams, build scripts, and validation suite for generating the **Claude-Level Project Understanding and Technical Learning Book** for `merchantshield-ai` (Track 02: AI Risk Manager, Razorpay AI Buildathon 2026).

---

## 📚 Deliverable Overview

- **Final PDF**: [`project-docs/output/Project_Understanding_Book.pdf`](output/Project_Understanding_Book.pdf)
  - **Format**: A4 Portrait, Print-optimized CSS Paged Media.
  - **Length**: 46 Pages (~16,400 words, 126,600 characters).
  - **Visuals**: 5 vector SVG architectural diagrams, 1 empirical Matplotlib threshold analysis chart, 18 deep-dive code walkthroughs, 9 pipeline stages, and real-world Bangalore saree boutique case study.
- **Editable Source**: [`project-docs/source/`](source/)
  - `styles.css`: Typography, grid layout, callout styling, table formatting, and page-break rules.
  - `cover_and_toc.py`: Monograph cover page and complete hyperlinked Table of Contents.
  - `section1_executive_summary.py`: High-level summary, executive table, architecture diagram.
  - `section2_problem_statement.py`: Industry problem, 3 systemic failures, conventional vs. proposed table.
  - `section3_normal_friend.py`: "Varnam Silks" real-world Bangalore merchant narrative, 7-step walkthrough, analogy-to-code mapping.
  - `section4_tech_stack.py`: 10-category master technology inventory, runtime justification (LightGBM, SHAP, FastAPI, Pydantic v2, SQLite, React 19).
  - `section5_codebase_exploration.py`: Directory tree, module responsibilities, complete file reference table, 17 code deep dives, dependency map.
  - `section6_architecture_and_design.py`: 4-tier conceptual architecture, SQLite audit schema, PII omission rationale, 6 REST API endpoints, 5-rule policy engine, data flow sequence.
  - `section7_pipeline_stage_by_stage.py`: 9 execution stages documented using the exact 11-part template, complete numerical worked trace (`demo_txn_critical`), embedded empirical threshold chart.
  - `section8_final_summary_and_mastery.py`: End-to-end flow recap, key components, verified capabilities vs. prototype limitations, 10 self-test questions & grounded answers, 3-tier pitch (30s, 2m, 10m), glossary & checklist.
- **Diagrams**: [`project-docs/diagrams/`](diagrams/)
  - `architecture.svg` / `architecture.mmd`: High-level 4-tier system architecture.
  - `pipeline.svg` / `pipeline.mmd`: 9-stage transaction risk evaluation pipeline.
  - `decision_policy.svg` / `decision_policy.mmd`: 5-tier deterministic policy decision tree.
  - `database_schema.svg` / `database_schema.mmd`: SQLite audit log entity relationship diagram.
  - `data_flow.svg` / `data_flow.mmd`: Sequence diagram showing synchronous evaluate flow.
  - `generate_svgs.py`: Standalone script to compile all vector diagrams.
- **Scripts**: [`project-docs/scripts/`](scripts/)
  - `generate_book.py`: Assembles HTML from modular sections, inlines vector SVGs and base64 charts, and invokes Google Chrome Headless to compile the 46-page PDF.
  - `validate_pdf.py`: Automated Phase 7 validation script testing PDF existence, page count, word count, section headers, grounded code symbols, absence of placeholders, and rendering representative pages to PNG.

---

## 🛠️ Prerequisites & Environment

To regenerate the documentation and PDF, the following tools are required:

1. **Python 3.10+** (Standard Library only; no extra pip packages required for generation or validation):
   ```bash
   python3 --version
   ```
2. **Google Chrome / Chromium** (used for high-fidelity CSS Paged Media rendering):
   ```bash
   google-chrome --version
   # or
   which google-chrome || which chromium-browser || which chromium
   ```
3. **Poppler Utilities** (optional, used by `validate_pdf.py` for text extraction and page rendering):
   ```bash
   pdftotext -v
   pdftoppm -v
   ```

---

## 🚀 How to Regenerate the Book

### 1. (Optional) Rebuild the Vector Diagrams
If you make changes to the diagram definitions in `project-docs/diagrams/generate_svgs.py`:
```bash
python3 project-docs/diagrams/generate_svgs.py
```
This will regenerate all `.svg` and `.mmd` files in `project-docs/diagrams/`.

### 2. Compile Unified HTML and Render PDF
Run the primary build script from the repository root:
```bash
python3 project-docs/scripts/generate_book.py
```
**What this does**:
1. Imports all 8 modular Python sections and `cover_and_toc.py`.
2. Inlines all 5 standalone SVGs from `project-docs/diagrams/` directly into the DOM (ensuring razor-sharp vector graphics with zero external font/network dependencies).
3. Reads and base64-encodes the empirical threshold analysis chart (`ml/models/threshold_analysis_chart.png`).
4. Generates `project-docs/source/Project_Understanding_Book.html` (~430 KB).
5. Invokes Google Chrome in headless mode (`--headless=new --print-to-pdf-no-header`) with background graphics enabled to produce `project-docs/output/Project_Understanding_Book.pdf`.

### 3. Run the Automated Phase 7 Validation Suite
Verify document integrity, section presence, symbol verification, and page rendering:
```bash
python3 project-docs/scripts/validate_pdf.py
```
**Validation Checks**:
- ✅ Confirms PDF file existence and size (>2 MB).
- ✅ Extracts text via `pdftotext` and counts pages (46 pages, ~16,400 words).
- ✅ Asserts exact presence of all 8 Section headers.
- ✅ Asserts presence of 18 grounded codebase symbols (`candidate_lgbm_v1.pkl`, `DECISION_THRESHOLD`, `CRITICAL_BLOCK`, `TreeExplainer`, `_validate_engineered_features`, `IEEE-CIS`, `Varnam Silks`, etc.).
- ✅ Scans for unresolved placeholders (`TODO`, `FIXME`, `[TBD]`).
- ✅ Renders representative pages (Cover, TOC, Section 1 Architecture, Section 4 Tech Stack, Section 6 DB Schema, Section 7 Stage 5 Matplotlib Chart, Section 8 Mastery) to PNG in `project-docs/output/validation_pages/`.

---

## 📖 Chapter & Section Map

| Chapter | Title | Key Contents |
|---|---|---|
| **Front** | Title & Table of Contents | Monograph metadata, executive badges, complete hyperlinked TOC |
| **Section 1** | Executive Summary | One-line mission, 2-minute pitch, core capabilities, architecture overview, executive summary table |
| **Section 2** | Problem Statement | Indian digital payments context, 3 systemic failures (asymmetry, rule brittleness, black-box friction), conventional vs proposed comparison table |
| **Section 3** | Normal Friend Explanation | "Varnam Silks" Bangalore silk saree boutique story (Ananya & Vikram), 7-step narrative walkthrough, real-world to codebase mapping table |
| **Section 4** | Tech Stack & Rationale | 10-category master technology inventory, runtime justification (LightGBM, SHAP, FastAPI, Pydantic v2, SQLite, React 19) |
| **Section 5** | Codebase Exploration | Full repository tree, directory responsibilities, comprehensive file-by-file reference table, 17 code deep dives, dependency map |
| **Section 6** | Architecture, DB & API Design | 4-tier conceptual architecture, SQLite audit schema & privacy PII omission rationale, 6 OpenAPI REST endpoints, 5-rule policy engine, data flow sequence diagram |
| **Section 7** | The Complete Pipeline (Stage-by-Stage) | 9 execution stages documented with 11-part template, end-to-end worked numerical trace (`demo_txn_critical`), embedded empirical threshold chart |
| **Section 8** | Final Summary & Project Mastery | 10-step lifecycle recap, key components, verified capabilities vs. prototype limitations, 10 self-test questions & grounded answers, 3-tier pitch (30s, 2m, 10m), glossary & revision checklist |

---

## 🛡️ Groundedness & Engineering Honesty

In accordance with strict technical book writing standards, all claims in this document are strictly grounded in the repository's verified source code:
- **Model Distribution Shift**: The book explicitly documents the verified test finding where the synthetic baseline model achieved ROC-AUC 0.443 on the real IEEE-CIS dataset due to feature distribution mismatch, whereas retraining the feature engineering methodology on IEEE-CIS achieved ROC-AUC 0.771 and 79.8% recall (`ml/evaluate_ieee.py`).
- **Synchronous Velocity Calculation**: Documents that transaction velocity is calculated via in-memory sliding windows in the request payload (`prior_transactions`) rather than an external distributed Redis cluster.
- **Zero Hallucinations**: No external cloud services (AWS, GCP, Kafka, Kubernetes) or fabricated third-party competitors are claimed. The project is faithfully analyzed as a self-contained, enterprise-grade prototype designed for local and containerized evaluation.
