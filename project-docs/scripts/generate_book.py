#!/usr/bin/env python3
"""
MerchantShield AI — Project Understanding Book PDF Generator.
Compiles all chapters, inlines vector SVG diagrams, base64-encodes charts,
and prints a publication-grade PDF using headless Chrome.
"""

import os
import sys
import base64
import subprocess

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DOCS_DIR = os.path.dirname(SCRIPT_DIR)
WORKSPACE_ROOT = os.path.dirname(PROJECT_DOCS_DIR)
SOURCE_DIR = os.path.join(PROJECT_DOCS_DIR, "source")
DIAGRAMS_DIR = os.path.join(PROJECT_DOCS_DIR, "diagrams")
OUTPUT_DIR = os.path.join(PROJECT_DOCS_DIR, "output")

sys.path.insert(0, SOURCE_DIR)

from cover_and_toc import get_cover_html, get_toc_html
from section1_executive_summary import get_section1_html
from section2_problem_statement import get_section2_html
from section3_normal_friend import get_section3_html
from section4_tech_stack import get_section4_html
from section5_codebase_exploration import get_section5_html
from section6_architecture_and_design import get_section6_html
from section7_pipeline_stage_by_stage import get_section7_html
from section8_final_summary_and_mastery import get_section8_html


def read_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


def read_base64_image(filepath):
    with open(filepath, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


def main():
    print("=" * 70)
    print("Compiling MerchantShield AI Technical Learning Book")
    print("=" * 70)

    # 1. Read Stylesheet
    css_content = read_file(os.path.join(SOURCE_DIR, "styles.css"))

    # 2. Read SVGs
    arch_svg = read_file(os.path.join(DIAGRAMS_DIR, "architecture.svg"))
    pipe_svg = read_file(os.path.join(DIAGRAMS_DIR, "pipeline.svg"))
    policy_svg = read_file(os.path.join(DIAGRAMS_DIR, "decision_policy.svg"))
    db_svg = read_file(os.path.join(DIAGRAMS_DIR, "database_schema.svg"))
    flow_svg = read_file(os.path.join(DIAGRAMS_DIR, "data_flow.svg"))

    # 3. Read Matplotlib Chart Image (Base64)
    chart_path = os.path.join(WORKSPACE_ROOT, "ml", "models", "threshold_analysis_chart.png")
    chart_b64 = read_base64_image(chart_path)

    # 4. Assemble HTML Chapters
    html_parts = [
        "<!DOCTYPE html>",
        "<html lang='en'>",
        "<head>",
        "  <meta charset='UTF-8'>",
        "  <title>MerchantShield AI — Project Understanding and Technical Learning Book</title>",
        f"  <style>\n{css_content}\n  </style>",
        "</head>",
        "<body>",
        get_cover_html(),
        get_toc_html(),
        get_section1_html(arch_svg),
        get_section2_html(),
        get_section3_html(),
        get_section4_html(),
        get_section5_html(),
        get_section6_html(policy_svg, db_svg, flow_svg),
        get_section7_html(pipe_svg, chart_b64),
        get_section8_html(),
        "</body>",
        "</html>"
    ]

    full_html = "\n".join(html_parts)
    html_out_path = os.path.join(SOURCE_DIR, "Project_Understanding_Book.html")
    with open(html_out_path, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"Generated unified HTML: {html_out_path} ({len(full_html):,} bytes)")

    # 5. Render PDF using Headless Chrome
    pdf_out_path = os.path.join(OUTPUT_DIR, "Project_Understanding_Book.pdf")
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print("Launching Google Chrome to render PDF...")
    chrome_cmd = [
        "google-chrome",
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--allow-file-access-from-files",
        "--print-to-pdf-no-header",
        f"--print-to-pdf={pdf_out_path}",
        html_out_path,
    ]

    result = subprocess.run(chrome_cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error executing Chrome: {result.stderr}")
        sys.exit(1)

    if not os.path.exists(pdf_out_path):
        print("PDF generation failed: Output file does not exist!")
        sys.exit(1)

    pdf_size = os.path.getsize(pdf_out_path)
    print(f"Successfully generated PDF: {pdf_out_path}")
    print(f"File size: {pdf_size:,} bytes ({pdf_size / (1024*1024):.2f} MB)")
    print("=" * 70)


if __name__ == "__main__":
    main()
