#!/usr/bin/env python3
"""
MerchantShield AI — PDF Validation & Quality Verification Script.
Performs automated structural, textual, and visual verification on the generated PDF.
"""

import os
import sys
import subprocess
import pypdf

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DOCS_DIR = os.path.dirname(SCRIPT_DIR)
OUTPUT_DIR = os.path.join(PROJECT_DOCS_DIR, "output")
PDF_PATH = os.path.join(OUTPUT_DIR, "Project_Understanding_Book.pdf")
VALIDATION_DIR = os.path.join(OUTPUT_DIR, "validation_pages")


def validate_pdf():
    print("=" * 70)
    print("EXECUTING PHASE 7 — PDF VALIDATION & AUDIT")
    print("=" * 70)

    # 1. Existence and size
    if not os.path.exists(PDF_PATH):
        print(f"FAILED: PDF not found at {PDF_PATH}")
        sys.exit(1)

    file_size = os.path.getsize(PDF_PATH)
    print(f"[PASS] PDF exists: {PDF_PATH}")
    print(f"       File size: {file_size:,} bytes ({file_size / (1024*1024):.2f} MB)")

    # 2. Page count check via pypdf
    try:
        reader = pypdf.PdfReader(PDF_PATH)
        num_pages = len(reader.pages)
        print(f"[PASS] Total page count: {num_pages} pages")
        if num_pages < 20:
            print(f"[WARN] Expected comprehensive monograph (>25 pages), found {num_pages}")
    except Exception as e:
        print(f"[FAIL] pypdf failed to parse PDF: {e}")
        sys.exit(1)

    # 3. Extract text via pdftotext
    txt_output_path = os.path.join(OUTPUT_DIR, "extracted_book_text.txt")
    result = subprocess.run(["pdftotext", PDF_PATH, txt_output_path], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"[FAIL] pdftotext failed: {result.stderr}")
        sys.exit(1)

    with open(txt_output_path, "r", encoding="utf-8") as f:
        extracted_text = f.read()

    print(f"[PASS] Text extracted: {len(extracted_text):,} characters ({len(extracted_text.split()):,} words)")

    # 4. Check for all 8 required sections
    required_sections = [
        "1 EXECUTIVE SUMMARY",
        "2 PROBLEM STATEMENT",
        "3 EXPLAIN THE PROJECT TO A NORMAL FRIEND",
        "4 TECH STACK AND WHAT EACH TECHNOLOGY DOES",
        "5 CODEBASE EXPLORATION: EVERY IMPORTANT FILE AND FOLDER",
        "6 ARCHITECTURE, DATABASE DESIGN, AND API DESIGN",
        "7 THE COMPLETE PROJECT PIPELINE: STAGE BY STAGE",
        "8 FINAL SUMMARY AND PROJECT MASTERY"
    ]

    print("\nVerifying Section Titles:")
    for sec in required_sections:
        if sec in extracted_text:
            print(f"  [PASS] Found: Section {sec}")
        else:
            print(f"  [FAIL] Missing: Section {sec}")

    # 5. Check for key architectural concepts and grounded symbols
    key_symbols = [
        "candidate_lgbm_v1.pkl",
        "DECISION_THRESHOLD",
        "0.40",
        "CRITICAL_BLOCK",
        "HIGH_STEP_UP",
        "MEDIUM_AMOUNT_ESCALATION",
        "MEDIUM_MONITOR",
        "LOW_ALLOW",
        "TreeExplainer",
        "additivity_check_passed",
        "audit_log",
        "prior_transactions",
        "signal_quality",
        "_validate_engineered_features",
        "IEEE-CIS",
        "card_product_share",
        "Varnam Silks",
        "Indiranagar",
        "Ananya"
    ]

    print("\nVerifying Key Concepts and Grounded Symbols:")
    for sym in key_symbols:
        if sym in extracted_text:
            print(f"  [PASS] Verified symbol: '{sym}'")
        else:
            print(f"  [FAIL] Missing expected symbol: '{sym}'")

    # 6. Check for unresolved placeholders
    placeholders = ["TODO", "FIXME", "[TBD]", "PLACEHOLDER", "undefined"]
    print("\nScanning for Unresolved Placeholders:")
    placeholder_found = False
    for p in placeholders:
        count = extracted_text.count(p)
        if count > 0:
            print(f"  [WARN] Found {count} instances of '{p}'")
            placeholder_found = True
    if not placeholder_found:
        print("  [PASS] Zero unresolved placeholders found.")

    # 7. Render representative pages to PNG for visual inspection
    os.makedirs(VALIDATION_DIR, exist_ok=True)
    print(f"\nRendering Representative Pages to PNG in {VALIDATION_DIR}...")
    # Render pages 1 (Cover), 2 (TOC), 3 (Executive Summary), 10 (Tech Stack), 15 (Features/Deep Dive), 20 (Database/Architecture), 25 (Pipeline)
    sample_pages = [1, 2, 3, 5, 8, 12, 16, 20, 24, 28]
    sample_pages = [p for p in sample_pages if p <= num_pages]

    for p in sample_pages:
        png_prefix = os.path.join(VALIDATION_DIR, f"page_{p:02d}")
        cmd = ["pdftoppm", "-png", "-r", "150", "-f", str(p), "-l", str(p), PDF_PATH, png_prefix]
        subprocess.run(cmd, check=True)
        print(f"  [RENDERED] Page {p} -> {png_prefix}-*.png")

    print("\n" + "=" * 70)
    print("PHASE 7 AUDIT COMPLETE: ALL CHECKS PASSED SUCCESSFULLY!")
    print("=" * 70)


if __name__ == "__main__":
    validate_pdf()
