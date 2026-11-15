"""
Cover and Table of Contents generator for MerchantShield AI Technical Book.
"""

def get_cover_html():
    return '''
<div class="cover-page">
  <div>
    <div class="cover-badge">ENGINEERING MONOGRAPH &amp; ARCHITECTURE AUDIT</div>
    <div class="cover-title">MerchantShield <span>AI</span></div>
    <div class="cover-subtitle">
      A Claude-Level Project Understanding &amp; Technical Learning Book: From Business Intent and Asymmetric Risk Economics to Leakage-Safe Feature Engineering and Deterministic Policy Governance.
    </div>
    <div class="cover-divider"></div>
  </div>

  <div class="cover-meta-grid">
    <div class="cover-meta-item">
      <div class="cover-meta-label">Target Track</div>
      <div class="cover-meta-value">Razorpay AI Buildathon 2026 — Track 02 (AI Risk Manager)</div>
    </div>
    <div class="cover-meta-item">
      <div class="cover-meta-label">System Architecture</div>
      <div class="cover-meta-value">Decoupled ML Estimator + Grounded SHAP + 5-Rule Deterministic Policy</div>
    </div>
    <div class="cover-meta-item">
      <div class="cover-meta-label">Primary Artifact</div>
      <div class="cover-meta-value">Frozen LightGBM Classifier (lgbm_v1) @ Cost-Min Threshold 0.40</div>
    </div>
    <div class="cover-meta-item">
      <div class="cover-meta-label">Evaluation Rigor</div>
      <div class="cover-meta-value">Chronological Split + IEEE-CIS External Real Chargeback Validation</div>
    </div>
    <div class="cover-meta-item">
      <div class="cover-meta-label">Codebase Version</div>
      <div class="cover-meta-value">v1.0.0 (V2 Hardened: Sanity Bounds, Signal Quality, Migrations)</div>
    </div>
    <div class="cover-meta-item">
      <div class="cover-meta-label">Document Date</div>
      <div class="cover-meta-value">October 2026 | Technical Monograph Edition</div>
    </div>
  </div>

  <div class="cover-footer">
    <span>Principal Software Architect &amp; Technical Systems Auditor</span>
    <span>Production Architecture &amp; Codebase Learning Reference</span>
  </div>
</div>
'''

def get_toc_html():
    return '''
<div class="page-break"></div>

<div class="toc-container">
  <div class="toc-title">TABLE OF CONTENTS</div>
  <ul class="toc-list">
    <li class="toc-item toc-item-major">
      <a href="#section-1"><span class="section-number">1</span> EXECUTIVE SUMMARY</a>
      <span>Section 1</span>
    </li>
    <ul class="toc-sublist">
      <li class="toc-subitem"><a href="#sec-1-1">1.1 Project Overview &amp; Core Mission</a></li>
      <li class="toc-subitem"><a href="#sec-1-2">1.2 Target Users &amp; Integrating Systems</a></li>
      <li class="toc-subitem"><a href="#sec-1-3">1.3 Real-World Problem &amp; Core Capabilities</a></li>
      <li class="toc-subitem"><a href="#sec-1-4">1.4 High-Level Architecture &amp; Key Technologies</a></li>
      <li class="toc-subitem"><a href="#sec-1-5">1.5 System Boundaries, Inputs &amp; Outputs</a></li>
      <li class="toc-subitem"><a href="#sec-1-6">1.6 Implementation Status &amp; Limitations</a></li>
      <li class="toc-subitem"><a href="#sec-1-7">1.7 Executive Summary Master Reference Table</a></li>
    </ul>

    <li class="toc-item toc-item-major">
      <a href="#section-2"><span class="section-number">2</span> PROBLEM STATEMENT</a>
      <span>Section 2</span>
    </li>
    <ul class="toc-sublist">
      <li class="toc-subitem"><a href="#sec-2-1">2.1 The Existing Situation: Why Fraud Detection Fails in Practice</a></li>
      <li class="toc-subitem"><a href="#sec-2-2">2.2 The Three Fundamental Failures of Conventional Systems</a></li>
      <li class="toc-subitem"><a href="#sec-2-3">2.3 The Problem MerchantShield AI Solves</a></li>
      <li class="toc-subitem"><a href="#sec-2-4">2.4 Scope Boundaries: What Is In Scope vs. Deliberately Out of Scope</a></li>
      <li class="toc-subitem"><a href="#sec-2-5">2.5 Conventional Approach vs. MerchantShield AI Architecture</a></li>
    </ul>

    <li class="toc-item toc-item-major">
      <a href="#section-3"><span class="section-number">3</span> EXPLAIN THE PROJECT TO A NORMAL FRIEND</a>
      <span>Section 3</span>
    </li>
    <ul class="toc-sublist">
      <li class="toc-subitem"><a href="#sec-3-1">3.1 A Familiar Real-World Situation: Ananya's Handcrafted Silk Boutique</a></li>
      <li class="toc-subitem"><a href="#sec-3-2">3.2 The Nightmare Without MerchantShield: The Chargeback Trap</a></li>
      <li class="toc-subitem"><a href="#sec-3-3">3.3 Introducing MerchantShield AI: The Invisible Risk Manager</a></li>
      <li class="toc-subitem"><a href="#sec-3-4">3.4 The Complete Transaction Journey: Step-by-Step</a></li>
      <li class="toc-subitem"><a href="#sec-3-5">3.5 Mapping Everyday Concepts to Real Code Components</a></li>
    </ul>

    <li class="toc-item toc-item-major">
      <a href="#section-4"><span class="section-number">4</span> TECH STACK AND WHAT EACH TECHNOLOGY DOES</a>
      <span>Section 4</span>
    </li>
    <ul class="toc-sublist">
      <li class="toc-subitem"><a href="#sec-4-1">4.1 Master Technology Inventory &amp; Architecture Map</a></li>
      <li class="toc-subitem"><a href="#sec-4-2">4.2 Python Ecosystem &amp; Machine Learning Libraries</a></li>
      <li class="toc-subitem"><a href="#sec-4-3">4.3 LightGBM &amp; SHAP: The Dual Reasoning Engine</a></li>
      <li class="toc-subitem"><a href="#sec-4-4">4.4 Backend API Stack: FastAPI, Pydantic v2 &amp; Uvicorn</a></li>
      <li class="toc-subitem"><a href="#sec-4-5">4.5 Persistence &amp; Governance: SQLAlchemy &amp; SQLite</a></li>
      <li class="toc-subitem"><a href="#sec-4-6">4.6 Frontend Architecture: React 19, Vite &amp; Vanilla CSS</a></li>
      <li class="toc-subitem"><a href="#sec-4-7">4.7 Verification &amp; DevOps: pytest &amp; Multi-Stage Docker</a></li>
      <li class="toc-subitem"><a href="#sec-4-8">4.8 Dependency Classification: Direct, Indirect &amp; Tooling</a></li>
    </ul>

    <li class="toc-item toc-item-major">
      <a href="#section-5"><span class="section-number">5</span> CODEBASE EXPLORATION: EVERY IMPORTANT FILE AND FOLDER</a>
      <span>Section 5</span>
    </li>
    <ul class="toc-sublist">
      <li class="toc-subitem"><a href="#sec-5-1">5.1 Complete Repository Directory Tree</a></li>
      <li class="toc-subitem"><a href="#sec-5-2">5.2 Folder-by-Folder Structural Overview</a></li>
      <li class="toc-subitem"><a href="#sec-5-3">5.3 File-by-File Technical Reference Inventory</a></li>
      <li class="toc-subitem"><a href="#sec-5-4">5.4 Critical File Deep Dives &amp; Code Walkthroughs</a></li>
      <li class="toc-subitem"><a href="#sec-5-5">5.5 File Dependency &amp; Runtime Execution Graph</a></li>
    </ul>

    <li class="toc-item toc-item-major">
      <a href="#section-6"><span class="section-number">6</span> ARCHITECTURE, DATABASE DESIGN, AND API DESIGN</a>
      <span>Section 6</span>
    </li>
    <ul class="toc-sublist">
      <li class="toc-subitem"><a href="#sec-6-1">6.1 Conceptual Architecture &amp; Component Responsibilities</a></li>
      <li class="toc-subitem"><a href="#sec-6-2">6.2 Database &amp; Storage Design: The SQLite Audit Store</a></li>
      <li class="toc-subitem"><a href="#sec-6-3">6.3 API &amp; Interface Design: The Six Endpoints</a></li>
      <li class="toc-subitem"><a href="#sec-6-4">6.4 Architectural Trade-Offs, Invariants &amp; Decoupling</a></li>
      <li class="toc-subitem"><a href="#sec-6-5">6.5 End-to-End Sequence &amp; Data Flow</a></li>
    </ul>

    <li class="toc-item toc-item-major">
      <a href="#section-7"><span class="section-number">7</span> THE COMPLETE PROJECT PIPELINE: STAGE BY STAGE</a>
      <span>Section 7</span>
    </li>
    <ul class="toc-sublist">
      <li class="toc-subitem"><a href="#sec-7-0">7.0 Execution Pipeline Overview</a></li>
      <li class="toc-subitem"><a href="#sec-7-1">Stage 1: System Bootstrapping &amp; Model Loading</a></li>
      <li class="toc-subitem"><a href="#sec-7-2">Stage 2: Request Reception &amp; Strict Shape Validation</a></li>
      <li class="toc-subitem"><a href="#sec-7-3">Stage 3: Leakage-Safe Feature Engineering</a></li>
      <li class="toc-subitem"><a href="#sec-7-4">Stage 4: Feature Bounds Checking &amp; V2 Hardening</a></li>
      <li class="toc-subitem"><a href="#sec-7-5">Stage 5: LightGBM Model Inference &amp; Output Hardening</a></li>
      <li class="toc-subitem"><a href="#sec-7-6">Stage 6: Grounded SHAP Explainability &amp; Additivity Verification</a></li>
      <li class="toc-subitem"><a href="#sec-7-7">Stage 7: Deterministic Policy Evaluation &amp; Action Bounding</a></li>
      <li class="toc-subitem"><a href="#sec-7-8">Stage 8: Fail-Safe Audit Trail Persistence</a></li>
      <li class="toc-subitem"><a href="#sec-7-9">Stage 9: Response Synthesis &amp; Client Delivery</a></li>
      <li class="toc-subitem"><a href="#sec-7-10">7.10 Complete Worked Execution Trace</a></li>
    </ul>

    <li class="toc-item toc-item-major">
      <a href="#section-8"><span class="section-number">8</span> FINAL SUMMARY AND PROJECT MASTERY</a>
      <span>Section 8</span>
    </li>
    <ul class="toc-sublist">
      <li class="toc-subitem"><a href="#sec-8-1">8.1 The Project in One Complete Narrative</a></li>
      <li class="toc-subitem"><a href="#sec-8-2">8.2 Complete Flow Recap (10-Step Numbered Sequence)</a></li>
      <li class="toc-subitem"><a href="#sec-8-3">8.3 Key Architectural Components to Remember</a></li>
      <li class="toc-subitem"><a href="#sec-8-4">8.4 Verified Strengths vs. Explicit Prototype Limitations</a></li>
      <li class="toc-subitem"><a href="#sec-8-5">8.5 Self-Testing Examination &amp; Grounded Answers</a></li>
      <li class="toc-subitem"><a href="#sec-8-6">8.6 How to Explain This Project to Another Engineer</a></li>
      <li class="toc-subitem"><a href="#sec-8-7">8.7 Engineering Glossary &amp; Final Revision Checklist</a></li>
    </ul>
  </ul>
</div>
'''
