import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

# ── Color Palette Definitions (Exact match from tokens.css & App.css) ─────────
COLOR_BG            = RGBColor(0xF0, 0xF2, 0xF5)  # #f0f2f5 Main page canvas
COLOR_SURFACE       = RGBColor(0xFF, 0xFF, 0xFF)  # #ffffff Card background
COLOR_SURFACE_SUNKEN= RGBColor(0xF5, 0xF7, 0xFA)  # #f5f7fa Secondary surface
COLOR_SURFACE_INSET = RGBColor(0xEE, 0xF0, 0xF4)  # #eef0f4 Inset surface
COLOR_HEADER_BG     = RGBColor(0x0F, 0x16, 0x24)  # #0f1624 Dark shell / header

COLOR_TEXT_PRIMARY  = RGBColor(0x0F, 0x16, 0x24)  # #0f1624 Obsidian text
COLOR_TEXT_SECONDARY= RGBColor(0x4A, 0x55, 0x68)  # #4a5568 Slate text
COLOR_TEXT_TERTIARY = RGBColor(0x84, 0x92, 0xA6)  # #8492a6 Muted text
COLOR_TEXT_WHITE    = RGBColor(0xFF, 0xFF, 0xFF)  # #ffffff Inverse text

COLOR_BORDER        = RGBColor(0xDD, 0xE1, 0xEA)  # #dde1ea Base border
COLOR_BORDER_STRONG = RGBColor(0xC4, 0xCA, 0xD6)  # #c4cad6 Strong border
COLOR_BORDER_SUBTLE = RGBColor(0xE8, 0xEA, 0xEF)  # #e8eaef Subtle border

COLOR_ACCENT        = RGBColor(0x25, 0x63, 0xEB)  # #2563eb Primary blue
COLOR_ACCENT_STRONG = RGBColor(0x1D, 0x4E, 0xD8)  # #1d4ed8 Dark blue
COLOR_ACCENT_SOFT   = RGBColor(0xDB, 0xEA, 0xFE)  # #dbeafe Light blue
COLOR_ACCENT_MUTED  = RGBColor(0xEF, 0xF6, 0xFF)  # #eff6ff Blue tint

COLOR_RISK_LOW      = RGBColor(0x16, 0xA3, 0x4A)  # #16a34a Green
COLOR_RISK_LOW_BG   = RGBColor(0xF0, 0xFD, 0xF4)  # #f0fdf4
COLOR_RISK_LOW_BRD  = RGBColor(0xBB, 0xF7, 0xD0)  # #bbf7d0

COLOR_RISK_MED      = RGBColor(0xD9, 0x77, 0x06)  # #d97706 Amber
COLOR_RISK_MED_BG   = RGBColor(0xFF, 0xFB, 0xEB)  # #fffbeb
COLOR_RISK_MED_BRD  = RGBColor(0xFD, 0xE6, 0x8A)  # #fde68a

COLOR_RISK_HIGH     = RGBColor(0xEA, 0x58, 0x0C)  # #ea580c Orange
COLOR_RISK_HIGH_BG  = RGBColor(0xFF, 0xF7, 0xED)  # #fff7ed
COLOR_RISK_HIGH_BRD = RGBColor(0xFE, 0xD7, 0xAA)  # #fed7aa

COLOR_RISK_CRIT     = RGBColor(0xDC, 0x26, 0x26)  # #dc2626 Red
COLOR_RISK_CRIT_BG  = RGBColor(0xFE, 0xF2, 0xF2)  # #fef2f2
COLOR_RISK_CRIT_BRD = RGBColor(0xFE, 0xCA, 0xCA)  # #fecaca

COLOR_STATUS_OK     = RGBColor(0x4A, 0xDE, 0x80)  # #4ade80 Live OK dot

FONT_UI = "Inter"
FONT_MONO = "Consolas"

SCREENSHOTS_DIR = "MerchantShield_AI_Presentation/screenshots"
ASSETS_DIR = "MerchantShield_AI_Presentation/presentation_assets"

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
blank_layout = prs.slide_layouts[6]

def set_slide_background(slide, color):
    bg_shape = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5)
    )
    bg_shape.fill.solid()
    bg_shape.fill.fore_color.rgb = color
    bg_shape.line.fill.background()
    return bg_shape

def add_header(slide, category_text, title_text, subtitle_text):
    # Category Pill
    pill = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(0.32), Inches(3.4), Inches(0.26)
    )
    pill.fill.solid()
    pill.fill.fore_color.rgb = COLOR_ACCENT_SOFT
    pill.line.color.rgb = COLOR_ACCENT
    pill.line.width = Pt(1)
    tf_p = pill.text_frame
    tf_p.word_wrap = True
    tf_p.margin_left = tf_p.margin_right = tf_p.margin_top = tf_p.margin_bottom = 0
    p_p = tf_p.paragraphs[0]
    p_p.alignment = PP_ALIGN.CENTER
    r_p = p_p.add_run()
    r_p.text = category_text.upper()
    r_p.font.name = FONT_UI
    r_p.font.size = Pt(9)
    r_p.font.bold = True
    r_p.font.color.rgb = COLOR_ACCENT_STRONG

    # Right Live Status Badge
    rt_pill = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, Inches(9.2), Inches(0.32), Inches(3.533), Inches(0.26)
    )
    rt_pill.fill.solid()
    rt_pill.fill.fore_color.rgb = COLOR_SURFACE
    rt_pill.line.color.rgb = COLOR_BORDER
    rt_pill.line.width = Pt(1)
    tf_rt = rt_pill.text_frame
    tf_rt.word_wrap = True
    tf_rt.margin_left = tf_rt.margin_right = tf_rt.margin_top = tf_rt.margin_bottom = 0
    p_rt = tf_rt.paragraphs[0]
    p_rt.alignment = PP_ALIGN.CENTER
    r_rt = p_rt.add_run()
    r_rt.text = "● LIVE SYSTEM: http://localhost:8000"
    r_rt.font.name = FONT_MONO
    r_rt.font.size = Pt(8.5)
    r_rt.font.bold = True
    r_rt.font.color.rgb = COLOR_ACCENT_STRONG

    # Title & Subtitle Box
    tb = slide.shapes.add_textbox(Inches(0.6), Inches(0.62), Inches(12.133), Inches(0.70))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    
    p1 = tf.paragraphs[0]
    r1 = p1.add_run()
    r1.text = title_text
    r1.font.name = FONT_UI
    r1.font.size = Pt(19)
    r1.font.bold = True
    r1.font.color.rgb = COLOR_TEXT_PRIMARY

    p2 = tf.add_paragraph()
    r2 = p2.add_run()
    r2.text = subtitle_text
    r2.font.name = FONT_UI
    r2.font.size = Pt(10)
    r2.font.color.rgb = COLOR_TEXT_SECONDARY

    # Header divider rule
    line = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, Inches(0.6), Inches(1.36), Inches(12.133), Inches(0.015)
    )
    line.fill.solid()
    line.fill.fore_color.rgb = COLOR_BORDER
    line.line.fill.background()

def add_footer(slide, slide_num, total=10):
    line = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, Inches(0.6), Inches(7.05), Inches(12.133), Inches(0.015)
    )
    line.fill.solid()
    line.fill.fore_color.rgb = COLOR_BORDER
    line.line.fill.background()

    tb_l = slide.shapes.add_textbox(Inches(0.6), Inches(7.10), Inches(8.5), Inches(0.3))
    tf_l = tb_l.text_frame
    tf_l.word_wrap = True
    tf_l.margin_left = tf_l.margin_right = tf_l.margin_top = tf_l.margin_bottom = 0
    p_l = tf_l.paragraphs[0]
    r_l = p_l.add_run()
    r_l.text = "MerchantShield AI — Explainable Transaction Risk Decisioning System  |  SECE ML Engineering Project"
    r_l.font.name = FONT_UI
    r_l.font.size = Pt(8.5)
    r_l.font.color.rgb = COLOR_TEXT_TERTIARY

    tb_r = slide.shapes.add_textbox(Inches(10.0), Inches(7.10), Inches(2.733), Inches(0.3))
    tf_r = tb_r.text_frame
    tf_r.word_wrap = True
    tf_r.margin_left = tf_r.margin_right = tf_r.margin_top = tf_r.margin_bottom = 0
    p_r = tf_r.paragraphs[0]
    p_r.alignment = PP_ALIGN.RIGHT
    r_r = p_r.add_run()
    r_r.text = f"Slide {slide_num} of {total}"
    r_r.font.name = FONT_MONO
    r_r.font.size = Pt(8.5)
    r_r.font.bold = True
    r_r.font.color.rgb = COLOR_TEXT_PRIMARY

def add_card(slide, left, top, width, height, bg_color=COLOR_SURFACE, border_color=COLOR_BORDER):
    card = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height
    )
    card.fill.solid()
    card.fill.fore_color.rgb = bg_color
    card.line.color.rgb = border_color
    card.line.width = Pt(1)
    return card

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 1 – TITLE SLIDE (Dark Shell Theme #0F1624)
# ══════════════════════════════════════════════════════════════════════════════
print("Generating Slide 1: Title Slide...")
s1 = prs.slides.add_slide(blank_layout)
set_slide_background(s1, COLOR_HEADER_BG)

# Title Left Container
tb1_badge = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.75), Inches(4.5), Inches(0.32))
tb1_badge.fill.solid()
tb1_badge.fill.fore_color.rgb = RGBColor(0x1E, 0x29, 0x3B)
tb1_badge.line.color.rgb = RGBColor(0x3B, 0x82, 0xF6)
tb1_badge.line.width = Pt(1)
tf1_b = tb1_badge.text_frame
p1_b = tf1_b.paragraphs[0]
p1_b.alignment = PP_ALIGN.CENTER
r1_b = p1_b.add_run()
r1_b.text = "ENGINEERING PROJECT & SYSTEM ARCHITECTURE AUDIT"
r1_b.font.name = FONT_UI
r1_b.font.size = Pt(9)
r1_b.font.bold = True
r1_b.font.color.rgb = RGBColor(0x60, 0xA5, 0xFA)

# Main Title Box
tb1 = s1.shapes.add_textbox(Inches(0.8), Inches(1.2), Inches(6.0), Inches(2.2))
tf1 = tb1.text_frame
tf1.word_wrap = True
tf1.margin_left = tf1.margin_right = tf1.margin_top = tf1.margin_bottom = 0

p_t1 = tf1.paragraphs[0]
r_t1 = p_t1.add_run()
r_t1.text = "MERCHANTSHIELD "
r_t1.font.name = FONT_UI
r_t1.font.size = Pt(36)
r_t1.font.bold = True
r_t1.font.color.rgb = COLOR_TEXT_WHITE

r_t1_ai = p_t1.add_run()
r_t1_ai.text = "AI"
r_t1_ai.font.name = FONT_UI
r_t1_ai.font.size = Pt(36)
r_t1_ai.font.bold = True
r_t1_ai.font.color.rgb = RGBColor(0x3B, 0x82, 0xF6)

p_t2 = tf1.add_paragraph()
r_t2 = p_t2.add_run()
r_t2.text = "Intelligent Merchant Risk Detection and Decision Support System"
r_t2.font.name = FONT_UI
r_t2.font.size = Pt(14)
r_t2.font.bold = True
r_t2.font.color.rgb = RGBColor(0x93, 0xC5, 0xFD)

p_t3 = tf1.add_paragraph()
p_t3.space_before = Pt(8)
r_t3 = p_t3.add_run()
r_t3.text = "An end-to-end explainable transaction-risk decisioning system that bridges machine learning fraud probability estimation with a transparent, rule-based operational policy."
r_t3.font.name = FONT_UI
r_t3.font.size = Pt(10.5)
r_t3.font.color.rgb = RGBColor(0x94, 0xA3, 0xB8)

# 3 System Highlight Mini Cards
metrics_data = [
    ("ML CLASSIFIER", "LightGBM v1", "Frozen artifact @ 0.40 threshold"),
    ("EVALUATION RIGOR", "78.5% Prec | 88.2% Rec", "Held-out test set | ₹41.4K cost"),
    ("DECISION ENGINE", "5-Rule Policy", "Deterministic & auditable actions")
]
for idx, (m_lbl, m_val, m_sub) in enumerate(metrics_data):
    cx = Inches(0.8 + idx * 2.05)
    cy = Inches(3.65)
    c_card = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, cy, Inches(1.95), Inches(1.05))
    c_card.fill.solid()
    c_card.fill.fore_color.rgb = RGBColor(0x16, 0x20, 0x32)
    c_card.line.color.rgb = RGBColor(0x33, 0x41, 0x55)
    c_card.line.width = Pt(1)
    
    tb_m = s1.shapes.add_textbox(cx + Inches(0.1), cy + Inches(0.1), Inches(1.75), Inches(0.85))
    tf_m = tb_m.text_frame
    tf_m.word_wrap = True
    tf_m.margin_left = tf_m.margin_right = tf_m.margin_top = tf_m.margin_bottom = 0
    
    p_ml = tf_m.paragraphs[0]
    r_ml = p_ml.add_run()
    r_ml.text = m_lbl
    r_ml.font.name = FONT_UI
    r_ml.font.size = Pt(8)
    r_ml.font.bold = True
    r_ml.font.color.rgb = RGBColor(0x60, 0xA5, 0xFA)
    
    p_mv = tf_m.add_paragraph()
    r_mv = p_mv.add_run()
    r_mv.text = m_val
    r_mv.font.name = FONT_MONO
    r_mv.font.size = Pt(11)
    r_mv.font.bold = True
    r_mv.font.color.rgb = COLOR_TEXT_WHITE
    
    p_ms = tf_m.add_paragraph()
    r_ms = p_ms.add_run()
    r_ms.text = m_sub
    r_ms.font.name = FONT_UI
    r_ms.font.size = Pt(7.5)
    r_ms.font.color.rgb = RGBColor(0x94, 0xA3, 0xB8)

# Academic & Institutional Metadata Box
meta_card = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(4.95), Inches(6.05), Inches(1.8))
meta_card.fill.solid()
meta_card.fill.fore_color.rgb = RGBColor(0x13, 0x1C, 0x2D)
meta_card.line.color.rgb = RGBColor(0x28, 0x35, 0x4B)
meta_card.line.width = Pt(1)

tb_meta = s1.shapes.add_textbox(Inches(1.0), Inches(5.1), Inches(5.65), Inches(1.5))
tf_meta = tb_meta.text_frame
tf_meta.word_wrap = True
tf_meta.margin_left = tf_meta.margin_right = tf_meta.margin_top = tf_meta.margin_bottom = 0

rows_meta = [
    ("Target Track:", "Razorpay AI Buildathon 2026 — Track 02 (AI Risk Manager)"),
    ("Institution:", "Sri Eshwar College of Engineering (SECE)"),
    ("Department:", "Department of Computer Science and Engineering / AI & ML"),
    ("Course / Scope:", "B.E. 3rd Year / 5th Semester — Machine Learning Project"),
    ("Architecture:", "Decoupled LightGBM + Grounded TreeSHAP + 5-Rule Deterministic Policy")
]
for i, (k, v) in enumerate(rows_meta):
    p_row = tf_meta.paragraphs[0] if i == 0 else tf_meta.add_paragraph()
    p_row.space_before = Pt(2) if i > 0 else Pt(0)
    r_k = p_row.add_run()
    r_k.text = f"{k:<16} "
    r_k.font.name = FONT_MONO
    r_k.font.size = Pt(8.5)
    r_k.font.bold = True
    r_k.font.color.rgb = RGBColor(0x60, 0xA5, 0xFA)
    
    r_v = p_row.add_run()
    r_v.text = v
    r_v.font.name = FONT_UI
    r_v.font.size = Pt(8.5)
    r_v.font.color.rgb = RGBColor(0xCB, 0xD5, 0xE1)

# Right Side: Browser Mockup Card featuring Dashboard Overview
dash_frame = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.1), Inches(0.75), Inches(5.45), Inches(3.6))
dash_frame.fill.solid()
dash_frame.fill.fore_color.rgb = RGBColor(0x1E, 0x29, 0x3B)
dash_frame.line.color.rgb = RGBColor(0x3B, 0x82, 0xF6)
dash_frame.line.width = Pt(1.5)

# Browser Title Bar
tb_bar = s1.shapes.add_textbox(Inches(7.3), Inches(0.85), Inches(5.05), Inches(0.28))
tf_bar = tb_bar.text_frame
p_bar = tf_bar.paragraphs[0]
r_bar_dot = p_bar.add_run()
r_bar_dot.text = "● ● ●  "
r_bar_dot.font.size = Pt(9)
r_bar_dot.font.color.rgb = RGBColor(0x94, 0xA3, 0xB8)
r_bar_url = p_bar.add_run()
r_bar_url.text = "http://localhost:8000 — Live Application Dashboard"
r_bar_url.font.name = FONT_MONO
r_bar_url.font.size = Pt(8.5)
r_bar_url.font.color.rgb = RGBColor(0x60, 0xA5, 0xFA)

# Insert Hero Clean Screenshot inside frame (Aspect-Ratio Preserved)
s1.shapes.add_picture(
    os.path.join(SCREENSHOTS_DIR, "critical_block_full_panel.png"),
    Inches(7.22), Inches(1.18), Inches(5.21), Inches(2.9)
)

# Underneath Browser: Model & Policy Live Summary Card
info_frame = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.1), Inches(4.55), Inches(5.45), Inches(2.2))
info_frame.fill.solid()
info_frame.fill.fore_color.rgb = RGBColor(0x13, 0x1C, 0x2D)
info_frame.line.color.rgb = RGBColor(0x33, 0x41, 0x55)
info_frame.line.width = Pt(1)

# Insert Model Info Crop inside info_frame
s1.shapes.add_picture(
    os.path.join(SCREENSHOTS_DIR, "model_info_panel_crop.png"),
    Inches(7.22), Inches(4.65), Inches(5.21), Inches(1.95)
)

print("Slide 1 generated successfully.")

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 2 – PROJECT OVERVIEW
# ══════════════════════════════════════════════════════════════════════════════
print("Generating Slide 2: Project Overview...")
s2 = prs.slides.add_slide(blank_layout)
set_slide_background(s2, COLOR_BG)
add_header(s2, "Project Overview & Core Mission", "MerchantShield AI: End-to-End Explainable Decisioning", "Bridging statistical fraud probability estimation and bounded operational policy governance")
add_footer(s2, 2)

col_w = Inches(3.85)
col_h = Inches(4.35)
col_y = Inches(1.55)

# Col 1: System Definition & Core Mission
add_card(s2, Inches(0.6), col_y, col_w, col_h)
s2.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.6), col_y, col_w, Inches(0.08)).fill.solid()
s2.shapes[-1].fill.fore_color.rgb = COLOR_ACCENT
s2.shapes[-1].line.fill.background()

tb_c1 = s2.shapes.add_textbox(Inches(0.8), col_y + Inches(0.18), col_w - Inches(0.4), col_h - Inches(0.3))
tf_c1 = tb_c1.text_frame
tf_c1.word_wrap = True

p_c1_h = tf_c1.paragraphs[0]
r_c1_h = p_c1_h.add_run()
r_c1_h.text = "WHAT IS MERCHANTSHIELD AI?"
r_c1_h.font.name = FONT_UI
r_c1_h.font.size = Pt(11)
r_c1_h.font.bold = True
r_c1_h.font.color.rgb = COLOR_TEXT_PRIMARY

items_c1 = [
    ("Core Identity:", "An end-to-end explainable transaction-risk decisioning system designed for payment processors and merchants."),
    ("Real-Time Assessment:", "Evaluates incoming payment transactions and customer history in real time, calculating calibrated fraud probabilities."),
    ("Decoupled Architecture:", "Separates statistical estimation (LightGBM) from display risk scoring (0-100) and deterministic action policy."),
    ("Non-Custodial Advisory:", "Recommends bounded operational actions; never executes irreversible monetary movements or arbitrary account bans.")
]
for title, desc in items_c1:
    p = tf_c1.add_paragraph()
    p.space_before = Pt(8)
    r_t = p.add_run()
    r_t.text = title + " "
    r_t.font.name = FONT_UI
    r_t.font.size = Pt(9.5)
    r_t.font.bold = True
    r_t.font.color.rgb = COLOR_ACCENT_STRONG
    
    r_d = p.add_run()
    r_d.text = desc
    r_d.font.name = FONT_UI
    r_d.font.size = Pt(9.5)
    r_d.font.color.rgb = COLOR_TEXT_SECONDARY

# Col 2: The Trilemma Addressed
add_card(s2, Inches(4.74), col_y, col_w, col_h)
s2.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(4.74), col_y, col_w, Inches(0.08)).fill.solid()
s2.shapes[-1].fill.fore_color.rgb = COLOR_RISK_MED
s2.shapes[-1].line.fill.background()

tb_c2 = s2.shapes.add_textbox(Inches(4.94), col_y + Inches(0.18), col_w - Inches(0.4), col_h - Inches(0.3))
tf_c2 = tb_c2.text_frame
tf_c2.word_wrap = True

p_c2_h = tf_c2.paragraphs[0]
r_c2_h = p_c2_h.add_run()
r_c2_h.text = "THE FRAUD DETECTION TRILEMMA"
r_c2_h.font.name = FONT_UI
r_c2_h.font.size = Pt(11)
r_c2_h.font.bold = True
r_c2_h.font.color.rgb = COLOR_TEXT_PRIMARY

items_c2 = [
    ("1. Class Imbalance Trap:", "At 1–3% fraud rates, reporting raw accuracy is meaningless. A naive model that classifies 100% as legitimate achieves 98.5% accuracy while failing completely."),
    ("2. Arbitrary Thresholding:", "Default 0.50 cutoffs ignore financial economics. A false positive costs customer friction (~₹50); a false negative costs stolen funds (0.5 × amount)."),
    ("3. Black-Box Opacity:", "Standard ML models cannot explain decisions to human reviewers or compliance auditors, creating legal and operational liabilities."),
    ("4. The Decisioning Gap:", "A probability of 0.45 does not answer 'what should we do?'. Production systems require bounded, deterministic action rules.")
]
for title, desc in items_c2:
    p = tf_c2.add_paragraph()
    p.space_before = Pt(7)
    r_t = p.add_run()
    r_t.text = title + " "
    r_t.font.name = FONT_UI
    r_t.font.size = Pt(9.5)
    r_t.font.bold = True
    r_t.font.color.rgb = COLOR_RISK_MED
    
    r_d = p.add_run()
    r_d.text = desc
    r_d.font.name = FONT_UI
    r_d.font.size = Pt(9.5)
    r_d.font.color.rgb = COLOR_TEXT_SECONDARY

# Col 3: Bounded Actions & Four Tiers
add_card(s2, Inches(8.88), col_y, col_w, col_h)
s2.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(8.88), col_y, col_w, Inches(0.08)).fill.solid()
s2.shapes[-1].fill.fore_color.rgb = COLOR_RISK_LOW
s2.shapes[-1].line.fill.background()

tb_c3 = s2.shapes.add_textbox(Inches(9.08), col_y + Inches(0.18), col_w - Inches(0.4), col_h - Inches(0.3))
tf_c3 = tb_c3.text_frame
tf_c3.word_wrap = True

p_c3_h = tf_c3.paragraphs[0]
r_c3_h = p_c3_h.add_run()
r_c3_h.text = "FOUR BOUNDED OPERATIONAL ACTIONS"
r_c3_h.font.name = FONT_UI
r_c3_h.font.size = Pt(11)
r_c3_h.font.bold = True
r_c3_h.font.color.rgb = COLOR_TEXT_PRIMARY

actions_data = [
    ("ALLOW", COLOR_RISK_LOW, "Routine low-friction checkout (prob < 0.15). No additional customer friction warranted."),
    ("ALLOW_WITH_MONITORING", COLOR_RISK_MED, "Medium-risk tier (prob 0.15–0.39). Transaction approved; flagged for asynchronous telemetry."),
    ("STEP_UP_VERIFICATION", COLOR_RISK_HIGH, "High-risk tier (prob ≥ 0.40) or large amount escalation (prob ≥ 0.15 & amount ≥ ₹25K). 2FA/OTP challenged."),
    ("BLOCK", COLOR_RISK_CRIT, "Critical-risk tier (prob ≥ 0.80). Precision is high enough that transaction is prevented.")
]
for act_name, act_col, act_desc in actions_data:
    p = tf_c3.add_paragraph()
    p.space_before = Pt(6)
    r_a = p.add_run()
    r_a.text = act_name + "\n"
    r_a.font.name = FONT_MONO
    r_a.font.size = Pt(9.5)
    r_a.font.bold = True
    r_a.font.color.rgb = act_col
    
    r_d = p.add_run()
    r_d.text = act_desc
    r_d.font.name = FONT_UI
    r_d.font.size = Pt(9)
    r_d.font.color.rgb = COLOR_TEXT_SECONDARY

# Bottom Callout Banner
bot_card = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(6.05), Inches(12.133), Inches(0.85))
bot_card.fill.solid()
bot_card.fill.fore_color.rgb = COLOR_SURFACE_SUNKEN
bot_card.line.color.rgb = COLOR_BORDER
bot_card.line.width = Pt(1)

tb_bot = s2.shapes.add_textbox(Inches(0.8), Inches(6.12), Inches(11.733), Inches(0.7))
tf_bot = tb_bot.text_frame
tf_bot.word_wrap = True
p_b1 = tf_bot.paragraphs[0]
r_b1 = p_b1.add_run()
r_b1.text = "CORE ARCHITECTURAL PRINCIPLE: "
r_b1.font.name = FONT_UI
r_b1.font.size = Pt(9.5)
r_b1.font.bold = True
r_b1.font.color.rgb = COLOR_ACCENT

r_b2 = p_b1.add_run()
r_b2.text = "Strict separation of concerns. Changing how risk is displayed (0–100 score) can never silently change what operational action is taken. Similarly, SHAP explanations cannot alter decisions, ensuring complete determinism and legal defensibility."
r_b2.font.name = FONT_UI
r_b2.font.size = Pt(9.5)
r_b2.font.color.rgb = COLOR_TEXT_PRIMARY

print("Slide 2 generated successfully.")

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 3 – PROBLEM STATEMENT
# ══════════════════════════════════════════════════════════════════════════════
print("Generating Slide 3: Problem Statement...")
s3 = prs.slides.add_slide(blank_layout)
set_slide_background(s3, COLOR_BG)
add_header(s3, "Problem Analysis & Industry Gaps", "Problem Statement: Challenges in Merchant Risk Assessment", "Analyzing structural failure modes in traditional fraud detection pipelines")
add_footer(s3, 3)

grid_w = Inches(3.45)
grid_h = Inches(2.45)

prob_cards = [
    ("1. Class Imbalance Fallacy", COLOR_RISK_CRIT, [
        "In production transaction streams, fraud prevalence is typically 1.0% – 3.0%.",
        "Reporting standard classification accuracy creates dangerous false confidence.",
        "A dummy model predicting 100% legitimate transactions achieves 98.5% accuracy while suffering 100% fraud losses."
    ]),
    ("2. Cost-Agnostic Thresholding", COLOR_RISK_HIGH, [
        "Default classification threshold of 0.50 assumes symmetric error costs.",
        "In merchant reality: False Positive cost (₹50 customer friction) is heavily asymmetric to False Negative cost (0.50 × amount stolen).",
        "A fixed 0.50 cutoff drastically inflates expected financial loss."
    ]),
    ("3. The Black-Box Compliance Void", COLOR_RISK_MED, [
        "Complex ensembles or deep models output raw scalar probabilities without explanation.",
        "Human review teams and compliance officers cannot justify why a legitimate merchant was blocked.",
        "Generates customer churn, regulatory penalties, and unexplainable dispute losses."
    ]),
    ("4. Coupling Prediction with Action", COLOR_ACCENT, [
        "Directly linking raw ML scores to account freezing causes catastrophic false blocks.",
        "Without an independent, deterministic policy layer, model updates cause unpredictable business disruptions.",
        "Audit logs lack exact decision provenance and feature state snapshots."
    ])
]

for idx, (p_title, p_col, p_points) in enumerate(prob_cards):
    gx = Inches(0.6 + (idx % 2) * 3.6)
    gy = Inches(1.55 + (idx // 2) * 2.65)
    add_card(s3, gx, gy, grid_w, grid_h)
    
    s3.shapes.add_shape(MSO_SHAPE.RECTANGLE, gx, gy, Inches(0.08), grid_h).fill.solid()
    s3.shapes[-1].fill.fore_color.rgb = p_col
    s3.shapes[-1].line.fill.background()
    
    tb_p = s3.shapes.add_textbox(gx + Inches(0.18), gy + Inches(0.12), grid_w - Inches(0.28), grid_h - Inches(0.2))
    tf_p = tb_p.text_frame
    tf_p.word_wrap = True
    
    p_ph = tf_p.paragraphs[0]
    r_ph = p_ph.add_run()
    r_ph.text = p_title
    r_ph.font.name = FONT_UI
    r_ph.font.size = Pt(10.5)
    r_ph.font.bold = True
    r_ph.font.color.rgb = COLOR_TEXT_PRIMARY
    
    for pt in p_points:
        p_pt = tf_p.add_paragraph()
        p_pt.space_before = Pt(4)
        r_b = p_pt.add_run()
        r_b.text = "• "
        r_b.font.color.rgb = p_col
        r_b.font.bold = True
        
        r_txt = p_pt.add_run()
        r_txt.text = pt
        r_txt.font.name = FONT_UI
        r_txt.font.size = Pt(8.5)
        r_txt.font.color.rgb = COLOR_TEXT_SECONDARY

# Right Side: Comparison Table (Adjusted to prevent any text clipping)
add_card(s3, Inches(7.95), Inches(1.55), Inches(4.78), Inches(5.1))
tb_cmp = s3.shapes.add_textbox(Inches(8.15), Inches(1.68), Inches(4.38), Inches(4.85))
tf_cmp = tb_cmp.text_frame
tf_cmp.word_wrap = True

p_ch = tf_cmp.paragraphs[0]
r_ch = p_ch.add_run()
r_ch.text = "INDUSTRY NORM VS. MERCHANTSHIELD AI"
r_ch.font.name = FONT_UI
r_ch.font.size = Pt(11)
r_ch.font.bold = True
r_ch.font.color.rgb = COLOR_TEXT_PRIMARY

comp_items = [
    ("Optimization Metric", "Raw Accuracy / ROC-AUC alone", "Asymmetric cost function subject to recall ≥ 80%"),
    ("Decision Threshold", "Arbitrary default 0.50 cutoff", "Cost-minimized threshold (0.40) swept on validation"),
    ("Feature Pipeline", "Global look-ahead leakage", "Strictly-prior window calculations verified via tests"),
    ("Explainability", "Opaque output / templates", "Grounded TreeSHAP with mathematical runtime check"),
    ("Operational Action", "Unbounded account freezes", "Deterministic 5-rule ordered table (advisory only)"),
    ("Audit Traceability", "Opaque logs / lost context", "PII-safe SQLite audit trail storing full decision context")
]

for dim, norm, ms in comp_items:
    p_d = tf_cmp.add_paragraph()
    p_d.space_before = Pt(5)
    
    r_dim = p_d.add_run()
    r_dim.text = f"{dim.upper()}\n"
    r_dim.font.name = FONT_MONO
    r_dim.font.size = Pt(8)
    r_dim.font.bold = True
    r_dim.font.color.rgb = COLOR_ACCENT
    
    r_n = p_d.add_run()
    r_n.text = f"✕ Traditional: {norm}\n"
    r_n.font.name = FONT_UI
    r_n.font.size = Pt(7.8)
    r_n.font.color.rgb = COLOR_RISK_CRIT
    
    r_m = p_d.add_run()
    r_m.text = f"✓ MerchantShield: {ms}"
    r_m.font.name = FONT_UI
    r_m.font.size = Pt(7.8)
    r_m.font.color.rgb = COLOR_RISK_LOW

print("Slide 3 generated successfully.")

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 4 – PROPOSED SYSTEM WORKFLOW
# ══════════════════════════════════════════════════════════════════════════════
print("Generating Slide 4: Proposed System Workflow...")
s4 = prs.slides.add_slide(blank_layout)
set_slide_background(s4, COLOR_BG)
add_header(s4, "System Implementation & Workflow", "Proposed System: End-to-End Decisioning Pipeline", "Verified execution flow matching the production codebase implementation")
add_footer(s4, 4)

stages_data = [
    ("Stage 1", "INGESTION & VALIDATION", COLOR_ACCENT, [
        "FastAPI payload ingestion",
        "Pydantic strict schema",
        "V2 pathological bounds check",
        "Graceful 422 on bad data"
    ]),
    ("Stage 2", "LEAKAGE-SAFE FEATURES", COLOR_ACCENT_STRONG, [
        "15 behavioral features",
        "Strictly-prior window filter",
        "Velocity (5m, 30m, 60m)",
        "Amount z-score & novelty"
    ]),
    ("Stage 3", "LIGHTGBM INFERENCE", RGBColor(0x02, 0x84, 0xC7), [
        "Frozen lgbm_v1 artifact",
        "Evaluates 15-feature vector",
        "Output: P(Fraud) in [0, 1]",
        "Hardened sanity checks"
    ]),
    ("Stage 4", "DUAL-TRACK EVALUATION", RGBColor(0x7C, 0x3A, 0xED), [
        "Track A: Risk Score (0-100)",
        "Tier: LOW/MED/HIGH/CRIT",
        "Track B: SHAP TreeExplainer",
        "Additivity check verified"
    ]),
    ("Stage 5", "POLICY ENGINE", COLOR_RISK_HIGH, [
        "5-rule ordered table",
        "First matching rule wins",
        "Evaluates (prob, amt) only",
        "Bounded action produced"
    ]),
    ("Stage 6", "DELIVERY & AUDIT", COLOR_RISK_LOW, [
        "Structured JSON response",
        "React Vite live dashboard",
        "SQLite audit.db logging",
        "PII-safe decision record"
    ])
]

card_w = Inches(1.88)
card_h = Inches(2.9)
card_y = Inches(1.6)

for idx, (stg_num, stg_name, stg_col, stg_bullets) in enumerate(stages_data):
    cx = Inches(0.6 + idx * 2.05)
    add_card(s4, cx, card_y, card_w, card_h)
    
    s4.shapes.add_shape(MSO_SHAPE.RECTANGLE, cx, card_y, card_w, Inches(0.06)).fill.solid()
    s4.shapes[-1].fill.fore_color.rgb = stg_col
    s4.shapes[-1].line.fill.background()
    
    tb_s = s4.shapes.add_textbox(cx + Inches(0.08), card_y + Inches(0.1), card_w - Inches(0.16), card_h - Inches(0.15))
    tf_s = tb_s.text_frame
    tf_s.word_wrap = True
    
    p_num = tf_s.paragraphs[0]
    r_num = p_num.add_run()
    r_num.text = stg_num
    r_num.font.name = FONT_MONO
    r_num.font.size = Pt(8)
    r_num.font.bold = True
    r_num.font.color.rgb = stg_col
    
    p_name = tf_s.add_paragraph()
    r_name = p_name.add_run()
    r_name.text = stg_name
    r_name.font.name = FONT_UI
    r_name.font.size = Pt(9)
    r_name.font.bold = True
    r_name.font.color.rgb = COLOR_TEXT_PRIMARY
    
    for b in stg_bullets:
        p_b = tf_s.add_paragraph()
        p_b.space_before = Pt(4)
        r_dot = p_b.add_run()
        r_dot.text = "• "
        r_dot.font.color.rgb = stg_col
        r_dot.font.bold = True
        
        r_bt = p_b.add_run()
        r_bt.text = b
        r_bt.font.name = FONT_UI
        r_bt.font.size = Pt(7.8)
        r_bt.font.color.rgb = COLOR_TEXT_SECONDARY

    if idx < 5:
        arrow_x = cx + card_w + Inches(0.02)
        arrow_y = card_y + Inches(1.35)
        tb_arr = s4.shapes.add_textbox(arrow_x, arrow_y, Inches(0.15), Inches(0.3))
        p_arr = tb_arr.text_frame.paragraphs[0]
        r_arr = p_arr.add_run()
        r_arr.text = "→"
        r_arr.font.name = FONT_UI
        r_arr.font.size = Pt(14)
        r_arr.font.bold = True
        r_arr.font.color.rgb = COLOR_TEXT_TERTIARY

# Bottom 2 Deep Dive Cards
bb_w = Inches(5.95)
bb_h = Inches(1.95)
bb_y = Inches(4.75)

# Left Deep Dive: Leakage-Safe Feature Pipeline
add_card(s4, Inches(0.6), bb_y, bb_w, bb_h)
tb_lf = s4.shapes.add_textbox(Inches(0.8), bb_y + Inches(0.15), bb_w - Inches(0.4), bb_h - Inches(0.3))
tf_lf = tb_lf.text_frame
tf_lf.word_wrap = True

p_lf_h = tf_lf.paragraphs[0]
r_lf_h = p_lf_h.add_run()
r_lf_h.text = "LEAKAGE-SAFE FEATURE PIPELINE (build_features.py)"
r_lf_h.font.name = FONT_UI
r_lf_h.font.size = Pt(10.5)
r_lf_h.font.bold = True
r_lf_h.font.color.rgb = COLOR_ACCENT

lf_points = [
    "Strictly-Prior Enforcement: Velocity (5m, 30m, 60m) and amount z-scores are computed strictly from transactions occurring prior to current timestamp (t < t_current).",
    "Leakage Regression Testing: Dedicated test suite (tests/test_no_leakage.py) validates zero look-ahead bias across customer histories.",
    "Engineered Signals: Velocity counts, amount z-score vs. historical mean, device novelty flag, geo novelty flag, failure ratio trailing 10, account age, and night-time indicator."
]
for pt in lf_points:
    p = tf_lf.add_paragraph()
    p.space_before = Pt(3)
    r_pt = p.add_run()
    r_pt.text = "• " + pt
    r_pt.font.name = FONT_UI
    r_pt.font.size = Pt(8.5)
    r_pt.font.color.rgb = COLOR_TEXT_SECONDARY

# Right Deep Dive: Decoupled Decisioning Rationale
add_card(s4, Inches(6.78), bb_y, bb_w, bb_h)
tb_df = s4.shapes.add_textbox(Inches(6.98), bb_y + Inches(0.15), bb_w - Inches(0.4), bb_h - Inches(0.3))
tf_df = tb_df.text_frame
tf_df.word_wrap = True

p_df_h = tf_df.paragraphs[0]
r_df_h = p_df_h.add_run()
r_df_h.text = "DECOUPLED DECISION GOVERNANCE (decision_engine.py)"
r_df_h.font.name = FONT_UI
r_df_h.font.size = Pt(10.5)
r_df_h.font.bold = True
r_df_h.font.color.rgb = COLOR_RISK_HIGH

df_points = [
    "Independent Actioning: The policy function signature `evaluate_policy(probability, amount)` accepts only probability and amount. SHAP explanations cannot alter the action.",
    "Additivity Integrity: On every evaluation call, TreeSHAP mathematically verifies that `base_value + Σ(shap_values) ≈ predict_proba` within a tight tolerance (< 0.0001).",
    "Failure Isolation: If SHAP calculation or audit persistence fails, the decision is still returned to ensure low latency and zero transaction drops."
]
for pt in df_points:
    p = tf_df.add_paragraph()
    p.space_before = Pt(3)
    r_pt = p.add_run()
    r_pt.text = "• " + pt
    r_pt.font.name = FONT_UI
    r_pt.font.size = Pt(8.5)
    r_pt.font.color.rgb = COLOR_TEXT_SECONDARY

print("Slide 4 generated successfully.")

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 5 – SYSTEM ARCHITECTURE & TECHNOLOGIES
# ══════════════════════════════════════════════════════════════════════════════
print("Generating Slide 5: System Architecture & Technologies...")
s5 = prs.slides.add_slide(blank_layout)
set_slide_background(s5, COLOR_BG)
add_header(s5, "Architecture & Technology Stack", "System Architecture & Verified Technologies", "Multi-tier production architecture with verified components and zero framework bloat")
add_footer(s5, 5)

# Left Column: Layered Architecture Diagram (Shapes)
arch_w = Inches(5.5)
arch_h = Inches(5.1)
add_card(s5, Inches(0.6), Inches(1.55), arch_w, arch_h)

tb_at = s5.shapes.add_textbox(Inches(0.8), Inches(1.7), arch_w - Inches(0.4), Inches(0.35))
p_at = tb_at.text_frame.paragraphs[0]
r_at = p_at.add_run()
r_at.text = "MULTI-TIER ARCHITECTURAL TOPOLOGY"
r_at.font.name = FONT_UI
r_at.font.size = Pt(11)
r_at.font.bold = True
r_at.font.color.rgb = COLOR_TEXT_PRIMARY

layers_info = [
    ("PRESENTATION LAYER (React 19 / Vite)", [
        "Vite SPA frontend, Pure CSS Design Tokens (tokens.css)",
        "Zero heavyweight UI frameworks (no MUI/Tailwind bloat)",
        "Communicates exclusively via HTTP/JSON REST endpoints"
    ], COLOR_ACCENT_SOFT, COLOR_ACCENT_STRONG),
    ("API GATEWAY & VALIDATION LAYER (FastAPI)", [
        "FastAPI asynchronous web framework with Uvicorn ASGI",
        "Pydantic V2 schema validation and pathological bound checks",
        "Structured error handling: 422 (validation), 503 (degraded)"
    ], COLOR_SURFACE_SUNKEN, COLOR_ACCENT),
    ("ML INFERENCE & EXPLAINABILITY (LightGBM + SHAP)", [
        "Frozen LightGBM classifier artifact (ml/models/candidate_lgbm_v1.pkl)",
        "TreeSHAP explainability engine with runtime additivity check",
        "Metadata-configured threshold (0.40) and validation metrics"
    ], COLOR_SURFACE_SUNKEN, RGBColor(0x02, 0x84, 0xC7)),
    ("DECISION ENGINE & AUDIT STORE (Policy + SQLite)", [
        "Deterministic 5-rule ordered table (ALLOW to BLOCK)",
        "SQLAlchemy ORM + SQLite persistent storage (backend/data/audit.db)",
        "PII-safe audit logging with idempotent schema migrations"
    ], COLOR_SURFACE_SUNKEN, COLOR_RISK_LOW)
]

for idx, (lyr_title, lyr_desc, lyr_bg, lyr_col) in enumerate(layers_info):
    ly_top = Inches(2.15 + idx * 1.1)
    l_card = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), ly_top, arch_w - Inches(0.4), Inches(0.95))
    l_card.fill.solid()
    l_card.fill.fore_color.rgb = lyr_bg
    l_card.line.color.rgb = COLOR_BORDER
    l_card.line.width = Pt(1)
    
    s5.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), ly_top, Inches(0.06), Inches(0.95)).fill.solid()
    s5.shapes[-1].fill.fore_color.rgb = lyr_col
    s5.shapes[-1].line.fill.background()
    
    tb_l = s5.shapes.add_textbox(Inches(0.95), ly_top + Inches(0.06), arch_w - Inches(0.65), Inches(0.85))
    tf_l = tb_l.text_frame
    tf_l.word_wrap = True
    
    p_lh = tf_l.paragraphs[0]
    r_lh = p_lh.add_run()
    r_lh.text = lyr_title
    r_lh.font.name = FONT_UI
    r_lh.font.size = Pt(8.5)
    r_lh.font.bold = True
    r_lh.font.color.rgb = lyr_col
    
    for d in lyr_desc:
        p_d = tf_l.add_paragraph()
        r_d = p_d.add_run()
        r_d.text = "• " + d
        r_d.font.name = FONT_UI
        r_d.font.size = Pt(7.5)
        r_d.font.color.rgb = COLOR_TEXT_SECONDARY

# Right Column: Native Table for Verified Technology Stack
tech_w = Inches(6.45)
add_card(s5, Inches(6.3), Inches(1.55), tech_w, arch_h)

tb_tt = s5.shapes.add_textbox(Inches(6.5), Inches(1.7), tech_w - Inches(0.4), Inches(0.35))
p_tt = tb_tt.text_frame.paragraphs[0]
r_tt = p_tt.add_run()
r_tt.text = "VERIFIED TECHNOLOGY STACK & DEPENDENCY INVENTORY"
r_tt.font.name = FONT_UI
r_tt.font.size = Pt(11)
r_tt.font.bold = True
r_tt.font.color.rgb = COLOR_TEXT_PRIMARY

# Create Native PowerPoint Table for Technologies
table_tech_shape = s5.shapes.add_table(10, 3, Inches(6.5), Inches(2.1), tech_w - Inches(0.4), Inches(4.3))
tbl_t = table_tech_shape.table
tbl_t.columns[0].width = Inches(1.8)
tbl_t.columns[1].width = Inches(1.8)
tbl_t.columns[2].width = Inches(2.45)

tech_table_data = [
    ("LAYER", "TECHNOLOGY", "IMPLEMENTATION ROLE"),
    ("Frontend UI", "React 19, Vite", "SPA dashboard, CSS tokens, SVG gauges"),
    ("Backend API", "FastAPI, Uvicorn", "Async REST endpoints, OpenAPI at /docs"),
    ("Validation", "Pydantic V2", "Strict schemas, pathological bounds check"),
    ("Feature Engine", "pandas, NumPy", "Strictly-prior velocity windows, z-scores"),
    ("ML Classifier", "LightGBM (lgbm_v1)", "Frozen artifact @ 0.40 cost threshold"),
    ("Explainability", "SHAP TreeExplainer", "Additive attributions with runtime checks"),
    ("Decision Engine", "Python Rule Engine", "Deterministic 5-rule table (ALLOW-BLOCK)"),
    ("Audit Store", "SQLite, SQLAlchemy", "PII-safe persistence, schema migration"),
    ("Containerization", "Docker, Compose", "Multi-stage Node 22 + Python 3.13 slim")
]

for row_idx, row in enumerate(tech_table_data):
    for col_idx, cell_value in enumerate(row):
        cell = tbl_t.cell(row_idx, col_idx)
        cell.margin_left = cell.margin_right = cell.margin_top = cell.margin_bottom = Inches(0.04)
        p = cell.text_frame.paragraphs[0]
        r = p.add_run()
        r.text = cell_value
        if row_idx == 0:
            cell.fill.solid()
            cell.fill.fore_color.rgb = COLOR_HEADER_BG
            r.font.name = FONT_UI
            r.font.size = Pt(8.5)
            r.font.bold = True
            r.font.color.rgb = COLOR_TEXT_WHITE
        else:
            cell.fill.solid()
            cell.fill.fore_color.rgb = COLOR_SURFACE_SUNKEN if row_idx % 2 == 1 else COLOR_SURFACE
            r.font.name = FONT_UI if col_idx != 0 else FONT_MONO
            r.font.size = Pt(7.8)
            r.font.color.rgb = COLOR_ACCENT_STRONG if col_idx == 0 else COLOR_TEXT_PRIMARY

print("Slide 5 generated successfully.")

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 6 – USER INTERFACE SHOWCASE
# ══════════════════════════════════════════════════════════════════════════════
print("Generating Slide 6: User Interface Showcase...")
s6 = prs.slides.add_slide(blank_layout)
set_slide_background(s6, COLOR_BG)
add_header(s6, "User Interface & Experience", "MerchantShield AI User Interface & Investigation Workspace", "Real screenshots from the live application showing scenarios, risk ring, and verbatim actions")
add_footer(s6, 6)

# Main Large Screenshot Container (Left)
main_shot_w = Inches(7.5)
main_shot_h = Inches(5.1)
add_card(s6, Inches(0.6), Inches(1.55), main_shot_w, main_shot_h)

tb_ms = s6.shapes.add_textbox(Inches(0.8), Inches(1.68), main_shot_w - Inches(0.4), Inches(0.3))
p_ms = tb_ms.text_frame.paragraphs[0]
r_ms = p_ms.add_run()
r_ms.text = "PRIMARY INVESTIGATION DASHBOARD — LIVE EVALUATION"
r_ms.font.name = FONT_UI
r_ms.font.size = Pt(9.5)
r_ms.font.bold = True
r_ms.font.color.rgb = COLOR_TEXT_PRIMARY

s6.shapes.add_picture(
    os.path.join(SCREENSHOTS_DIR, "critical_block_full_panel.png"),
    Inches(0.8), Inches(2.05), Inches(7.1), Inches(4.35)
)

# Right Top Screenshot: Low Risk Scenario
right_w = Inches(4.45)
right_h = Inches(2.45)
add_card(s6, Inches(8.3), Inches(1.55), right_w, right_h)

tb_r1 = s6.shapes.add_textbox(Inches(8.45), Inches(1.65), right_w - Inches(0.3), Inches(0.25))
p_r1 = tb_r1.text_frame.paragraphs[0]
r_r1 = p_r1.add_run()
r_r1.text = "LOW RISK TIER — ALLOW ACTION (PROB: 0.0001)"
r_r1.font.name = FONT_UI
r_r1.font.size = Pt(8.5)
r_r1.font.bold = True
r_r1.font.color.rgb = COLOR_RISK_LOW

s6.shapes.add_picture(
    os.path.join(SCREENSHOTS_DIR, "low_risk_clean.png"),
    Inches(8.45), Inches(1.95), Inches(4.15), Inches(1.95)
)

# Right Bottom Screenshot: High Risk Step-Up Scenario
add_card(s6, Inches(8.3), Inches(4.2), right_w, right_h)

tb_r2 = s6.shapes.add_textbox(Inches(8.45), Inches(4.3), right_w - Inches(0.3), Inches(0.25))
p_r2 = tb_r2.text_frame.paragraphs[0]
r_r2 = p_r2.add_run()
r_r2.text = "HIGH RISK TIER — STEP_UP_VERIFICATION"
r_r2.font.name = FONT_UI
r_r2.font.size = Pt(8.5)
r_r2.font.bold = True
r_r2.font.color.rgb = COLOR_RISK_HIGH

s6.shapes.add_picture(
    os.path.join(SCREENSHOTS_DIR, "high_risk_clean.png"),
    Inches(8.45), Inches(4.6), Inches(4.15), Inches(1.95)
)

print("Slide 6 generated successfully.")

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 7 – DECISION ENGINE & EXPLAINABILITY
# ══════════════════════════════════════════════════════════════════════════════
print("Generating Slide 7: Decision Engine & Explainability...")
s7 = prs.slides.add_slide(blank_layout)
set_slide_background(s7, COLOR_BG)
add_header(s7, "Decision Policy & XAI", "Deterministic Decision Engine & Grounded Explainability", "Transparent 5-rule operational policy paired with mathematically verified TreeSHAP attributions")
add_footer(s7, 7)

# Left Column: 5-Rule Deterministic Policy Table
de_w = Inches(5.8)
de_h = Inches(5.1)
add_card(s7, Inches(0.6), Inches(1.55), de_w, de_h)

tb_de = s7.shapes.add_textbox(Inches(0.8), Inches(1.7), de_w - Inches(0.4), Inches(0.4))
p_de = tb_de.text_frame.paragraphs[0]
r_de = p_de.add_run()
r_de.text = "5-RULE DETERMINISTIC POLICY TABLE (decision_engine.py)"
r_de.font.name = FONT_UI
r_de.font.size = Pt(11)
r_de.font.bold = True
r_de.font.color.rgb = COLOR_TEXT_PRIMARY

rules_info = [
    ("RULE 1: CRITICAL_BLOCK", "probability ≥ 0.80", "BLOCK", COLOR_RISK_CRIT, 
     "Fraud probability is at or above critical threshold; high precision prevents false blocks."),
    ("RULE 2: HIGH_STEP_UP", "probability ≥ 0.40", "STEP_UP_VERIFICATION", COLOR_RISK_HIGH,
     "Fraud probability exceeds cost-minimized threshold (0.40); step-up 2FA challenge triggered."),
    ("RULE 3: MEDIUM_AMOUNT_ESCALATION", "probability ≥ 0.15 and amount ≥ ₹25,000", "STEP_UP_VERIFICATION", COLOR_RISK_HIGH,
     "Elevated risk combined with large transaction exposure escalates to step-up verification."),
    ("RULE 4: MEDIUM_MONITOR", "probability ≥ 0.15", "ALLOW_WITH_MONITORING", COLOR_RISK_MED,
     "Borderline transaction allowed through with background telemetry flag; zero customer friction."),
    ("RULE 5: LOW_ALLOW (Default Catch-All)", "All other transactions", "ALLOW", COLOR_RISK_LOW,
     "Low fraud probability (< 0.15); seamless approval with zero customer friction.")
]

for idx, (r_name, r_cond, r_act, r_col, r_reason) in enumerate(rules_info):
    ry = Inches(2.15 + idx * 0.88)
    rc_card = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), ry, de_w - Inches(0.4), Inches(0.82))
    rc_card.fill.solid()
    rc_card.fill.fore_color.rgb = COLOR_SURFACE_SUNKEN
    rc_card.line.color.rgb = COLOR_BORDER
    rc_card.line.width = Pt(1)
    
    s7.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), ry, Inches(0.06), Inches(0.82)).fill.solid()
    s7.shapes[-1].fill.fore_color.rgb = r_col
    s7.shapes[-1].line.fill.background()
    
    tb_rc = s7.shapes.add_textbox(Inches(0.95), ry + Inches(0.04), de_w - Inches(0.65), Inches(0.74))
    tf_rc = tb_rc.text_frame
    tf_rc.word_wrap = True
    
    p_rh = tf_rc.paragraphs[0]
    r_rn = p_rh.add_run()
    r_rn.text = r_name + "  "
    r_rn.font.name = FONT_MONO
    r_rn.font.size = Pt(8.5)
    r_rn.font.bold = True
    r_rn.font.color.rgb = COLOR_TEXT_PRIMARY
    
    r_ra = p_rh.add_run()
    r_ra.text = f"→ {r_act}"
    r_ra.font.name = FONT_MONO
    r_ra.font.size = Pt(8.5)
    r_ra.font.bold = True
    r_ra.font.color.rgb = r_col
    
    p_rc = tf_rc.add_paragraph()
    r_rc = p_rc.add_run()
    r_rc.text = f"Condition: {r_cond} | {r_reason}"
    r_rc.font.name = FONT_UI
    r_rc.font.size = Pt(7.5)
    r_rc.font.color.rgb = COLOR_TEXT_SECONDARY

# Right Column: Grounded SHAP & Additivity Screenshot
xai_w = Inches(6.15)
add_card(s7, Inches(6.6), Inches(1.55), xai_w, de_h)

tb_xt = s7.shapes.add_textbox(Inches(6.8), Inches(1.7), xai_w - Inches(0.4), Inches(0.4))
p_xt = tb_xt.text_frame.paragraphs[0]
r_xt = p_xt.add_run()
r_xt.text = "GROUNDED SHAP EXPLAINABILITY (explainability.py)"
r_xt.font.name = FONT_UI
r_xt.font.size = Pt(11)
r_xt.font.bold = True
r_xt.font.color.rgb = COLOR_ACCENT

# Insert SHAP Screenshot
s7.shapes.add_picture(
    os.path.join(SCREENSHOTS_DIR, "shap_clean.png"),
    Inches(6.8), Inches(2.1), Inches(5.75), Inches(2.65)
)

# Text Box Explaining SHAP Details Below Screenshot
tb_xb = s7.shapes.add_textbox(Inches(6.8), Inches(4.85), Inches(5.75), Inches(1.65))
tf_xb = tb_xb.text_frame
tf_xb.word_wrap = True

xai_features = [
    ("Mathematical Additivity Check:", "Every API call verifies |base_value + Σ(shap_values) - predict_proba| < 0.0001. If violated, explanation is flagged invalid."),
    ("Grounded Natural Language:", "Reasons are dynamically constructed from (feature, value, shap_value) triples (e.g. 'Amount is 83.7x customer historical average')."),
    ("Correct Contextual Framing:", "Differentiates 'Why this was flagged' vs. 'Why this was NOT flagged' based on whether probability crosses the 0.40 threshold."),
    ("Architectural Decoupling:", "SHAP calculations run asynchronously or in parallel; policy evaluation never consumes SHAP output, preventing feedback corruption.")
]

for idx, (title, desc) in enumerate(xai_features):
    p_xf = tf_xb.paragraphs[0] if idx == 0 else tf_xb.add_paragraph()
    p_xf.space_before = Pt(2.5) if idx > 0 else Pt(0)
    
    r_xt = p_xf.add_run()
    r_xt.text = title + " "
    r_xt.font.name = FONT_UI
    r_xt.font.size = Pt(8)
    r_xt.font.bold = True
    r_xt.font.color.rgb = COLOR_ACCENT_STRONG
    
    r_xd = p_xf.add_run()
    r_xd.text = desc
    r_xd.font.name = FONT_UI
    r_xd.font.size = Pt(8)
    r_xd.font.color.rgb = COLOR_TEXT_SECONDARY

print("Slide 7 generated successfully.")

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 8 – EXPERIMENTS, VALIDATION & MODEL RESULTS
# ══════════════════════════════════════════════════════════════════════════════
print("Generating Slide 8: Experiments, Validation & Model Results...")
s8 = prs.slides.add_slide(blank_layout)
set_slide_background(s8, COLOR_BG)
add_header(s8, "Empirical Validation & Results", "Model Evaluation & Experimental Validation", "Held-out test set performance, cost-sensitive threshold optimization, and external IEEE-CIS validation")
add_footer(s8, 8)

res_w = Inches(6.8)
res_h = Inches(5.1)
add_card(s8, Inches(0.6), Inches(1.55), res_w, res_h)

tb_rh = s8.shapes.add_textbox(Inches(0.8), Inches(1.68), res_w - Inches(0.4), Inches(0.35))
p_rh = tb_rh.text_frame.paragraphs[0]
r_rh = p_rh.add_run()
r_rh.text = "HELD-OUT TEST SET EVALUATION (Days 50–59 | 21,300 Txns)"
r_rh.font.name = FONT_UI
r_rh.font.size = Pt(11)
r_rh.font.bold = True
r_rh.font.color.rgb = COLOR_TEXT_PRIMARY

# Native Table for Model Evaluation
table_res_shape = s8.shapes.add_table(4, 8, Inches(0.8), Inches(2.05), res_w - Inches(0.4), Inches(1.5))
tbl_r = table_res_shape.table
tbl_r.columns[0].width = Inches(1.8)
tbl_r.columns[1].width = Inches(0.65)
tbl_r.columns[2].width = Inches(0.65)
tbl_r.columns[3].width = Inches(0.65)
tbl_r.columns[4].width = Inches(0.65)
tbl_r.columns[5].width = Inches(0.55)
tbl_r.columns[6].width = Inches(0.55)
tbl_r.columns[7].width = Inches(0.9)

eval_table_data = [
    ("MODEL", "PREC", "REC", "F1", "PR-AUC", "FP", "FN", "EST. COST"),
    ("Logistic Regression", "0.448", "0.825", "0.581", "0.739", "730", "126", "₹110,582"),
    ("Random Forest", "0.746", "0.868", "0.802", "0.883", "213", "95", "₹68,479"),
    ("LightGBM (Selected)", "0.785", "0.882", "0.830", "0.901", "174", "85", "₹41,377")
]

for row_idx, row in enumerate(eval_table_data):
    for col_idx, cell_value in enumerate(row):
        cell = tbl_r.cell(row_idx, col_idx)
        cell.margin_left = cell.margin_right = cell.margin_top = cell.margin_bottom = Inches(0.03)
        p = cell.text_frame.paragraphs[0]
        r = p.add_run()
        r.text = cell_value
        if row_idx == 0:
            cell.fill.solid()
            cell.fill.fore_color.rgb = COLOR_HEADER_BG
            r.font.name = FONT_UI
            r.font.size = Pt(8)
            r.font.bold = True
            r.font.color.rgb = COLOR_TEXT_WHITE
        elif row_idx == 3:  # Selected LightGBM
            cell.fill.solid()
            cell.fill.fore_color.rgb = COLOR_ACCENT_SOFT
            r.font.name = FONT_MONO if col_idx != 0 else FONT_UI
            r.font.size = Pt(8)
            r.font.bold = True
            r.font.color.rgb = COLOR_ACCENT_STRONG
        else:
            cell.fill.solid()
            cell.fill.fore_color.rgb = COLOR_SURFACE_SUNKEN if row_idx % 2 == 1 else COLOR_SURFACE
            r.font.name = FONT_MONO if col_idx != 0 else FONT_UI
            r.font.size = Pt(7.8)
            r.font.color.rgb = COLOR_TEXT_PRIMARY

# Key Empirical Takeaways Below Table
tb_tkw = s8.shapes.add_textbox(Inches(0.8), Inches(3.65), res_w - Inches(0.4), Inches(2.85))
tf_tkw = tb_tkw.text_frame
tf_tkw.word_wrap = True

tkw_items = [
    ("Asymmetric Cost Optimization:", "Selected threshold 0.40 minimizes total cost (FP: ₹50 review cost; FN: 0.5 × txn amount) subject to recall ≥ 80%. Not the naive 0.50 cutoff, nor the F1-maximizing 0.80 (which costs 38% more)."),
    ("Superior Loss Reduction:", "Selected LightGBM model reduced total business cost from ₹110,582 (baseline) to ₹41,377 — a 62.6% reduction in operational and fraud losses."),
    ("Chronological Data Hygiene:", "60-day dataset (213K txns, 2.2K customers) chronologically split into Train (days 0–39), Validation (days 40–49), and Test (days 50–59), preventing velocity leakage.")
]
for title, desc in tkw_items:
    p = tf_tkw.add_paragraph()
    p.space_before = Pt(3.5)
    r_t = p.add_run()
    r_t.text = title + " "
    r_t.font.name = FONT_UI
    r_t.font.size = Pt(8.5)
    r_t.font.bold = True
    r_t.font.color.rgb = COLOR_TEXT_PRIMARY
    
    r_d = p.add_run()
    r_d.text = desc
    r_d.font.name = FONT_UI
    r_d.font.size = Pt(8)
    r_d.font.color.rgb = COLOR_TEXT_SECONDARY

# Right Column: Threshold Analysis Chart & External Validation
ext_w = Inches(5.15)
add_card(s8, Inches(7.6), Inches(1.55), ext_w, res_h)

tb_eh = s8.shapes.add_textbox(Inches(7.8), Inches(1.68), ext_w - Inches(0.4), Inches(0.35))
p_eh = tb_eh.text_frame.paragraphs[0]
r_eh = p_eh.add_run()
r_eh.text = "VALIDATION THRESHOLD SWEEP & IEEE-CIS"
r_eh.font.name = FONT_UI
r_eh.font.size = Pt(11)
r_eh.font.bold = True
r_eh.font.color.rgb = COLOR_TEXT_PRIMARY

# Insert Real Threshold Analysis Chart
s8.shapes.add_picture(
    os.path.join(SCREENSHOTS_DIR, "10-threshold-analysis.png"),
    Inches(7.8), Inches(2.05), Inches(4.75), Inches(2.1)
)

# External Validation Takeaways Below Chart
tb_ext = s8.shapes.add_textbox(Inches(7.8), Inches(4.25), ext_w - Inches(0.4), Inches(2.3))
tf_ext = tb_ext.text_frame
tf_ext.word_wrap = True

p_ext_t = tf_ext.paragraphs[0]
r_ext_t = p_ext_t.add_run()
r_ext_t.text = "HONEST EXTERNAL VALIDATION (IEEE-CIS CHARGEBACKS)"
r_ext_t.font.name = FONT_UI
r_ext_t.font.size = Pt(9)
r_ext_t.font.bold = True
r_ext_t.font.color.rgb = COLOR_RISK_MED

ext_points = [
    ("Experiment A (Frozen Model):", "ROC-AUC 0.443. Distribution shift and card velocity scale differences inverted the ranking; proving frozen synthetic models cannot transfer directly to real data."),
    ("Experiment B (Retrained Pipeline):", "ROC-AUC 0.771, PR-AUC 0.128, caught 79.8% of frauds (3,243 / 4,064). Proves our feature engineering methodology transfers strongly to real e-commerce data."),
    ("Phase 15 Feature Discovery:", "Adding `card_product_share` reduced false positives by 17.7% and lowered total expected cost by 17.0%.")
]
for title, desc in ext_points:
    p = tf_ext.add_paragraph()
    p.space_before = Pt(2.5)
    r_t = p.add_run()
    r_t.text = title + " "
    r_t.font.name = FONT_UI
    r_t.font.size = Pt(7.8)
    r_t.font.bold = True
    r_t.font.color.rgb = COLOR_TEXT_PRIMARY
    
    r_d = p.add_run()
    r_d.text = desc
    r_d.font.name = FONT_UI
    r_d.font.size = Pt(7.8)
    r_d.font.color.rgb = COLOR_TEXT_SECONDARY

print("Slide 8 generated successfully.")

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 9 – AUDIT TRAIL, API & DEPLOYMENT
# ══════════════════════════════════════════════════════════════════════════════
print("Generating Slide 9: Audit Trail, API & Deployment...")
s9 = prs.slides.add_slide(blank_layout)
set_slide_background(s9, COLOR_BG)
add_header(s9, "Operations & Production Engineering", "Audit Trail, REST API Contract & Docker Deployment", "Immutable decision persistence, production REST contracts, and multi-stage containerization")
add_footer(s9, 9)

col9_w = Inches(3.85)
col9_h = Inches(5.1)

# Col 1: Immutable Audit Trail
add_card(s9, Inches(0.6), Inches(1.55), col9_w, col9_h)
tb_a1 = s9.shapes.add_textbox(Inches(0.75), Inches(1.7), col9_w - Inches(0.3), Inches(0.35))
p_a1 = tb_a1.text_frame.paragraphs[0]
r_a1 = p_a1.add_run()
r_a1.text = "1. IMMUTABLE AUDIT TRAIL"
r_a1.font.name = FONT_UI
r_a1.font.size = Pt(10.5)
r_a1.font.bold = True
r_a1.font.color.rgb = COLOR_ACCENT

# Insert Audit Trail Screenshot
s9.shapes.add_picture(
    os.path.join(SCREENSHOTS_DIR, "audit_clean.png"),
    Inches(0.75), Inches(2.1), col9_w - Inches(0.3), Inches(1.85)
)

tb_a1_txt = s9.shapes.add_textbox(Inches(0.75), Inches(4.05), col9_w - Inches(0.3), Inches(2.5))
tf_a1_txt = tb_a1_txt.text_frame
tf_a1_txt.word_wrap = True

audit_pts = [
    ("Privacy-Safe Schema:", "Persists transaction_id, model_version, fraud_probability, threshold, risk_score, action, policy_rule, policy_reason, top_reasons, timestamp, source (demo/manual)."),
    ("PII Protection:", "Deliberately excludes customer ID, device ID, and geo location to avoid copying sensitive merchant data into audit storage."),
    ("Non-Blocking Persistence:", "If database writes fail, API still returns the risk decision with audit_persisted=false rather than dropping customer transactions.")
]
for idx, (t, d) in enumerate(audit_pts):
    p = tf_a1_txt.paragraphs[0] if idx == 0 else tf_a1_txt.add_paragraph()
    p.space_before = Pt(3) if idx > 0 else Pt(0)
    r_t = p.add_run()
    r_t.text = t + " "
    r_t.font.name = FONT_UI
    r_t.font.size = Pt(8)
    r_t.font.bold = True
    r_t.font.color.rgb = COLOR_TEXT_PRIMARY
    
    r_d = p.add_run()
    r_d.text = d
    r_d.font.name = FONT_UI
    r_d.font.size = Pt(8)
    r_d.font.color.rgb = COLOR_TEXT_SECONDARY

# Col 2: Production REST API Contract
add_card(s9, Inches(4.74), Inches(1.55), col9_w, col9_h)
tb_a2 = s9.shapes.add_textbox(Inches(4.89), Inches(1.7), col9_w - Inches(0.3), Inches(0.35))
p_a2 = tb_a2.text_frame.paragraphs[0]
r_a2 = p_a2.add_run()
r_a2.text = "2. REST API CONTRACT (/docs)"
r_a2.font.name = FONT_UI
r_a2.font.size = Pt(10.5)
r_a2.font.bold = True
r_a2.font.color.rgb = COLOR_ACCENT

# Insert API Docs Screenshot
s9.shapes.add_picture(
    os.path.join(SCREENSHOTS_DIR, "api_docs_clean.png"),
    Inches(4.89), Inches(2.1), col9_w - Inches(0.3), Inches(1.85)
)

tb_a2_txt = s9.shapes.add_textbox(Inches(4.89), Inches(4.05), col9_w - Inches(0.3), Inches(2.5))
tf_a2_txt = tb_a2_txt.text_frame
tf_a2_txt.word_wrap = True

api_endpoints = [
    ("GET /health", "Liveness & readiness probe; reports model loaded status."),
    ("GET /model/info", "Frozen metadata, decision threshold, test metrics."),
    ("POST /risk/score", "Fast probability + 0-100 score (no audit write)."),
    ("POST /risk/explain", "Probability + SHAP explanations (no audit write)."),
    ("POST /risk/evaluate", "Complete pipeline: score + explain + decide + audit."),
    ("GET /audit-log", "Returns recent persisted decision records (limit 50).")
]
for idx, (ep, purp) in enumerate(api_endpoints):
    p = tf_a2_txt.paragraphs[0] if idx == 0 else tf_a2_txt.add_paragraph()
    p.space_before = Pt(2.5) if idx > 0 else Pt(0)
    r_ep = p.add_run()
    r_ep.text = ep + " "
    r_ep.font.name = FONT_MONO
    r_ep.font.size = Pt(8)
    r_ep.font.bold = True
    r_ep.font.color.rgb = COLOR_ACCENT_STRONG
    
    r_p = p.add_run()
    r_p.text = "→ " + purp
    r_p.font.name = FONT_UI
    r_p.font.size = Pt(7.8)
    r_p.font.color.rgb = COLOR_TEXT_SECONDARY

# Col 3: Docker Deployment & Resilience
add_card(s9, Inches(8.88), Inches(1.55), col9_w, col9_h)
tb_a3 = s9.shapes.add_textbox(Inches(9.03), Inches(1.7), col9_w - Inches(0.3), Inches(0.35))
p_a3 = tb_a3.text_frame.paragraphs[0]
r_a3 = p_a3.add_run()
r_a3.text = "3. CONTAINERIZED DEPLOYMENT"
r_a3.font.name = FONT_UI
r_a3.font.size = Pt(10.5)
r_a3.font.bold = True
r_a3.font.color.rgb = COLOR_ACCENT

# Code / Config box inside Col 3
box_dck = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(9.03), Inches(2.1), col9_w - Inches(0.3), Inches(1.85))
box_dck.fill.solid()
box_dck.fill.fore_color.rgb = COLOR_HEADER_BG
box_dck.line.color.rgb = COLOR_BORDER
box_dck.line.width = Pt(1)

tb_code = s9.shapes.add_textbox(Inches(9.15), Inches(2.15), col9_w - Inches(0.55), Inches(1.75))
tf_code = tb_code.text_frame
tf_code.word_wrap = True

code_lines = [
    "# Multi-Stage Dockerfile",
    "FROM node:22-slim AS fe-build",
    "RUN npm run build",
    "",
    "FROM python:3.13-slim",
    "COPY --from=fe-build /frontend/dist",
    "RUN pip install -r requirements.txt",
    "CMD [\"uvicorn\", \"backend.main:app\",",
    "     \"--host\", \"0.0.0.0\", \"--port\", \"8000\"]"
]
for idx, line in enumerate(code_lines):
    p_c = tf_code.paragraphs[0] if idx == 0 else tf_code.add_paragraph()
    r_c = p_c.add_run()
    r_c.text = line
    r_c.font.name = FONT_MONO
    r_c.font.size = Pt(7.5)
    r_c.font.color.rgb = RGBColor(0x60, 0xA5, 0xFA) if line.startswith("#") else RGBColor(0x94, 0xA3, 0xB8)

tb_a3_txt = s9.shapes.add_textbox(Inches(9.03), Inches(4.05), col9_w - Inches(0.3), Inches(2.5))
tf_a3_txt = tb_a3_txt.text_frame
tf_a3_txt.word_wrap = True

dck_pts = [
    ("Multi-Stage Optimization:", "Node 22-slim builds static frontend; Python 3.13-slim serves unified app, reducing container attack surface."),
    ("State Persistence:", "Named volume `audit_data` mounted at `/app/backend/data/` ensures SQLite decisions persist across container restarts."),
    ("Graceful Degradation:", "If model fails to load, API starts in degraded mode with 503 on /model/info and degraded /health status instead of crashing.")
]
for idx, (t, d) in enumerate(dck_pts):
    p = tf_a3_txt.paragraphs[0] if idx == 0 else tf_a3_txt.add_paragraph()
    p.space_before = Pt(3) if idx > 0 else Pt(0)
    r_t = p.add_run()
    r_t.text = t + " "
    r_t.font.name = FONT_UI
    r_t.font.size = Pt(8)
    r_t.font.bold = True
    r_t.font.color.rgb = COLOR_TEXT_PRIMARY
    
    r_d = p.add_run()
    r_d.text = d
    r_d.font.name = FONT_UI
    r_d.font.size = Pt(8)
    r_d.font.color.rgb = COLOR_TEXT_SECONDARY

print("Slide 9 generated successfully.")

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 10 – CONCLUSION & FUTURE SCOPE
# ══════════════════════════════════════════════════════════════════════════════
print("Generating Slide 10: Conclusion & Future Scope...")
s10 = prs.slides.add_slide(blank_layout)
set_slide_background(s10, COLOR_BG)
add_header(s10, "Summary & Future Roadmap", "Conclusion, Technical Contributions & Future Scope", "Distinguishing completed prototype capabilities from enterprise production enhancements")
add_footer(s10, 10)

col10_w = Inches(5.8)
col10_h = Inches(4.0)
add_card(s10, Inches(0.6), Inches(1.55), col10_w, col10_h)

tb_c10 = s10.shapes.add_textbox(Inches(0.8), Inches(1.7), col10_w - Inches(0.4), Inches(0.35))
p_c10 = tb_c10.text_frame.paragraphs[0]
r_c10 = p_c10.add_run()
r_c10.text = "CORE IMPLEMENTED CONTRIBUTIONS"
r_c10.font.name = FONT_UI
r_c10.font.size = Pt(11)
r_c10.font.bold = True
r_c10.font.color.rgb = COLOR_RISK_LOW

contribs = [
    ("Decoupled 3-Tier Architecture:", "Clean separation of LightGBM statistical estimation, 0–100 risk score display, and deterministic 5-rule policy governance."),
    ("Leakage-Safe Feature Engineering:", "15 behavioral features calculated strictly from prior timestamps, verified by rigorous regression testing."),
    ("Asymmetric Cost Optimization:", "Cost-minimizing threshold (0.40) reduces operational losses by 62.6% compared to standard baseline cutoffs."),
    ("Mathematically Grounded Explainability:", "Real-time TreeSHAP attributions with strict mathematical runtime additivity verification (|base + Σshap - proba| < 0.0001)."),
    ("Production-Ready Full Stack Application:", "High-performance FastAPI REST backend, React 19 / Vite interactive dashboard, SQLite audit logging, and multi-stage Docker packaging.")
]

tb_cnt = s10.shapes.add_textbox(Inches(0.8), Inches(2.1), col10_w - Inches(0.4), Inches(3.3))
tf_cnt = tb_cnt.text_frame
tf_cnt.word_wrap = True

for idx, (t, d) in enumerate(contribs):
    p = tf_cnt.paragraphs[0] if idx == 0 else tf_cnt.add_paragraph()
    p.space_before = Pt(4) if idx > 0 else Pt(0)
    r_t = p.add_run()
    r_t.text = t + " "
    r_t.font.name = FONT_UI
    r_t.font.size = Pt(8.5)
    r_t.font.bold = True
    r_t.font.color.rgb = COLOR_TEXT_PRIMARY
    
    r_d = p.add_run()
    r_d.text = d
    r_d.font.name = FONT_UI
    r_d.font.size = Pt(8.5)
    r_d.font.color.rgb = COLOR_TEXT_SECONDARY

# Right Column: Future Roadmap (Distinct from Implemented)
add_card(s10, Inches(6.6), Inches(1.55), col10_w, col10_h)

tb_r10 = s10.shapes.add_textbox(Inches(6.8), Inches(1.7), col10_w - Inches(0.4), Inches(0.35))
p_r10 = tb_r10.text_frame.paragraphs[0]
r_r10 = p_r10.add_run()
r_r10.text = "FUTURE SCOPE & ENTERPRISE ROADMAP"
r_r10.font.name = FONT_UI
r_r10.font.size = Pt(11)
r_r10.font.bold = True
r_r10.font.color.rgb = COLOR_ACCENT

roadmap = [
    ("Graph-Based Syndicate Detection:", "Incorporate graph neural networks (GNNs) or community detection algorithms to identify coordinated merchant fraud rings across shared device fingerprints."),
    ("Streaming Event Ingestion:", "Migrate from synchronous REST to asynchronous streaming architecture using Apache Kafka or RabbitMQ for sub-10ms transaction throughput."),
    ("Automated Drift Monitoring & Recalibration:", "Implement Population Stability Index (PSI) and concept drift detection to automatically trigger model retraining when fraud patterns evolve."),
    ("Distributed Ledger Audit Persistence:", "Upgrade SQLite to an immutable distributed database (e.g., PostgreSQL with write-ahead logs or cryptographic hash chaining) for financial compliance.")
]

tb_rdm = s10.shapes.add_textbox(Inches(6.8), Inches(2.1), col10_w - Inches(0.4), Inches(3.3))
tf_rdm = tb_rdm.text_frame
tf_rdm.word_wrap = True

for idx, (t, d) in enumerate(roadmap):
    p = tf_rdm.paragraphs[0] if idx == 0 else tf_rdm.add_paragraph()
    p.space_before = Pt(4.5) if idx > 0 else Pt(0)
    r_t = p.add_run()
    r_t.text = t + " "
    r_t.font.name = FONT_UI
    r_t.font.size = Pt(8.5)
    r_t.font.bold = True
    r_t.font.color.rgb = COLOR_TEXT_PRIMARY
    
    r_d = p.add_run()
    r_d.text = d
    r_d.font.name = FONT_UI
    r_d.font.size = Pt(8.5)
    r_d.font.color.rgb = COLOR_TEXT_SECONDARY

# Bottom Closing Banner
close_card = s10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(5.7), Inches(12.133), Inches(1.15))
close_card.fill.solid()
close_card.fill.fore_color.rgb = COLOR_HEADER_BG
close_card.line.color.rgb = COLOR_ACCENT
close_card.line.width = Pt(1.5)

tb_cls = s10.shapes.add_textbox(Inches(0.8), Inches(5.78), Inches(11.733), Inches(0.95))
tf_cls = tb_cls.text_frame
tf_cls.word_wrap = True

p_thx = tf_cls.paragraphs[0]
p_thx.alignment = PP_ALIGN.CENTER
r_thx = p_thx.add_run()
r_thx.text = "THANK YOU"
r_thx.font.name = FONT_UI
r_thx.font.size = Pt(22)
r_thx.font.bold = True
r_thx.font.color.rgb = COLOR_TEXT_WHITE

p_sub = tf_cls.add_paragraph()
p_sub.alignment = PP_ALIGN.CENTER
p_sub.space_before = Pt(2)
r_sub = p_sub.add_run()
r_sub.text = "MerchantShield AI — Intelligent Merchant Risk Detection and Decision Support System\nSri Eshwar College of Engineering  |  SECE ML Engineering  |  Razorpay AI Buildathon 2026"
r_sub.font.name = FONT_UI
r_sub.font.size = Pt(9.5)
r_sub.font.color.rgb = RGBColor(0x94, 0xA3, 0xB8)

print("Slide 10 generated successfully.")

# ══════════════════════════════════════════════════════════════════════════════
# SAVE PRESENTATION
# ══════════════════════════════════════════════════════════════════════════════
output_pptx = "MerchantShield_AI_Presentation/MerchantShield_AI_Presentation.pptx"
prs.save(output_pptx)
print(f"Presentation successfully saved to: {output_pptx}")
print(f"Total slides created: {len(prs.slides)}")
