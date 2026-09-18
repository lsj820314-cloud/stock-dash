from __future__ import annotations

import html
import streamlit as st


NAV_ITEMS = [
    ("홈", "⌂"),
    ("내 종목", "▥"),
    ("계좌 연결", "▣"),
    ("교육자료", "◫"),
    ("설정", "⚙"),
]


def apply_theme():
    st.markdown(
        """
<style>
:root {
  --bg: #F4F7FC;
  --surface: #FFFFFF;
  --surface-soft: #F8FAFF;
  --line: #E5EAF2;
  --line-strong: #D8E0EC;
  --text: #15213B;
  --muted: #71809A;
  --blue: #2563EB;
  --blue-2: #4F8CFF;
  --blue-soft: #EAF2FF;
  --green: #0A9B72;
  --green-soft: #EAF9F3;
  --red: #E5484D;
  --shadow: 0 12px 32px rgba(37, 70, 125, .07);
}
html, body, [class*="css"] {
  font-family: Pretendard, "Noto Sans KR", "Apple SD Gothic Neo", sans-serif;
}
.stApp {
  background: linear-gradient(180deg, #F7F9FD 0%, #F3F6FB 100%);
  color: var(--text);
}
.block-container {
  max-width: 1540px;
  padding-top: 1.25rem;
  padding-bottom: 4rem;
}
header[data-testid="stHeader"] {
  background: rgba(247,249,253,.86);
  backdrop-filter: blur(12px);
}
section[data-testid="stSidebar"] {
  background: #FFFFFF;
  border-right: 1px solid var(--line);
  box-shadow: 10px 0 30px rgba(37,70,125,.025);
}
section[data-testid="stSidebar"] > div {
  padding-top: 1rem;
}
[data-testid="stSidebar"] .stRadio > label {
  display: none;
}
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] {
  gap: .35rem;
}
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label {
  border-radius: 13px;
  padding: .68rem .72rem;
  transition: all .16s ease;
  color: #52627C;
}
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:hover {
  background: #F4F7FC;
}
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:has(input:checked) {
  background: var(--blue-soft);
  color: #1D4ED8;
  font-weight: 800;
  box-shadow: inset 3px 0 #3B82F6;
}
h1, h2, h3, h4 {
  color: var(--text);
  letter-spacing: -.035em;
}
h1 { font-weight: 850; }
h2, h3 { font-weight: 780; }
p, li { line-height: 1.62; }
[data-testid="stCaptionContainer"] {
  color: var(--muted);
}
[data-testid="stMetric"] {
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 18px;
  padding: 18px 20px;
  box-shadow: var(--shadow);
  min-height: 118px;
}
[data-testid="stMetricLabel"] {
  color: #60708A;
  font-weight: 700;
}
[data-testid="stMetricValue"] {
  color: #17233E;
  font-weight: 850;
  letter-spacing: -.03em;
}
[data-testid="stMetricDelta"] {
  font-weight: 700;
}
[data-testid="stVerticalBlockBorderWrapper"] {
  border-color: var(--line) !important;
  border-radius: 18px !important;
  background: var(--surface);
  box-shadow: var(--shadow);
}
[data-testid="stExpander"] {
  background: #FFFFFF;
  border: 1px solid var(--line) !important;
  border-radius: 14px !important;
}
.stButton > button, .stFormSubmitButton > button {
  border-radius: 12px;
  min-height: 2.75rem;
  font-weight: 750;
  border-color: #DDE5F0;
}
.stButton > button[kind="primary"], .stFormSubmitButton > button[kind="primary"] {
  background: linear-gradient(135deg, #2563EB, #4F8CFF);
  border-color: #2563EB;
  color: white;
  box-shadow: 0 8px 18px rgba(37,99,235,.18);
}
.stTextInput input, .stTextArea textarea, .stSelectbox div[data-baseweb="select"] > div {
  border-radius: 12px !important;
  background: #FFFFFF;
  border-color: #DFE6F0 !important;
}
.stTabs [data-baseweb="tab-list"] {
  gap: 7px;
  background: #EEF3FA;
  padding: 5px;
  border-radius: 13px;
}
.stTabs [data-baseweb="tab"] {
  border-radius: 10px;
  padding: 8px 13px;
  font-weight: 700;
}
.stTabs [aria-selected="true"] {
  background: #FFFFFF !important;
  color: #2563EB !important;
  box-shadow: 0 3px 10px rgba(30,64,175,.08);
}
.stDataFrame {
  border: 1px solid var(--line);
  border-radius: 15px;
  overflow: hidden;
  background: #FFFFFF;
}
.planx-brand {
  display:flex; align-items:center; gap:11px; margin: 3px 0 24px 0;
}
.planx-brand-mark {
  width:39px; height:39px; border-radius:12px;
  display:flex; align-items:center; justify-content:center;
  background:linear-gradient(145deg,#2563EB,#60A5FA);
  color:white; font-size:21px; font-weight:900;
  box-shadow:0 8px 20px rgba(37,99,235,.2);
}
.planx-brand-title {
  font-size:18px; line-height:1.15; font-weight:850; letter-spacing:-.04em;
  color:#17233E;
}
.planx-brand-sub {
  font-size:10.5px; color:#8A98AD; margin-top:3px;
}
.planx-hero {
  background: linear-gradient(135deg, #FFFFFF 0%, #FBFDFF 58%, #EEF5FF 100%);
  border: 1px solid #E1E8F2;
  border-radius: 22px;
  padding: 25px 28px;
  margin-bottom: 18px;
  box-shadow: var(--shadow);
  position: relative;
  overflow: hidden;
}
.planx-hero:after {
  content:"";
  position:absolute; right:-70px; top:-90px;
  width:240px; height:240px; border-radius:50%;
  background:radial-gradient(circle, rgba(79,140,255,.14), rgba(79,140,255,0) 68%);
}
.planx-eyebrow {
  color:#2563EB; font-size:11px; font-weight:850; letter-spacing:.12em;
  text-transform:uppercase; margin-bottom:7px;
}
.planx-hero h1 {
  margin:0; font-size:32px; line-height:1.18; position:relative; z-index:1;
}
.planx-hero p {
  margin:9px 0 0; color:#6E7F98; font-size:14px; max-width:800px; position:relative; z-index:1;
}
.planx-card {
  background:#FFFFFF;
  border:1px solid #E4EAF3;
  border-radius:18px;
  padding:18px 19px;
  min-height:120px;
  box-shadow:var(--shadow);
}
.planx-card-title {
  font-size:12px; color:#70809A; margin-bottom:8px; font-weight:750;
}
.planx-card-value {
  font-size:24px; color:#17233E; font-weight:850; letter-spacing:-.035em;
  font-variant-numeric:tabular-nums;
}
.planx-card-note {
  margin-top:8px; font-size:11.5px; color:#94A1B4;
}
.planx-empty {
  background: #FFFFFF;
  border:1px dashed #C8D4E5;
  border-radius:16px;
  padding:22px;
  color:#6E7F98;
}
.planx-source {
  display:inline-flex; align-items:center; gap:5px;
  color:#64748B; background:#F8FAFC; border:1px solid #E2E8F0;
  padding:4px 8px; border-radius:999px; font-size:10px;
}
.planx-status-ok { color:#047857; background:#ECFDF5; border-color:#A7F3D0; }
.planx-status-wait { color:#92400E; background:#FFFBEB; border-color:#FDE68A; }
.planx-status-bad { color:#B91C1C; background:#FEF2F2; border-color:#FECACA; }
.dashboard-panel-title {
  font-size:16px; font-weight:850; color:#17233E; margin-bottom:4px;
}
.dashboard-panel-sub {
  font-size:12px; color:#8795AA; margin-bottom:12px;
}
.dashboard-insight {
  border:1px solid #E7ECF4;
  border-radius:13px;
  padding:12px 13px;
  background:#FBFDFF;
  margin-bottom:9px;
}
.dashboard-insight strong { color:#17233E; }
.dashboard-insight span { color:#64748B; font-size:12px; }
hr { border-color:#E6EAF0 !important; }
@media (max-width: 900px) {
  .block-container { padding-left:1rem; padding-right:1rem; }
  .planx-hero { padding:21px 20px; }
  .planx-hero h1 { font-size:27px; }
}
</style>
""",
        unsafe_allow_html=True,
    )


def brand():
    st.markdown(
        """
<div class="planx-brand">
  <div class="planx-brand-mark">↗</div>
  <div>
    <div class="planx-brand-title">내 주식 대시보드</div>
    <div class="planx-brand-sub">오늘도, 더 나은 투자를 위해</div>
  </div>
</div>
""",
        unsafe_allow_html=True,
    )


def hero(title: str, subtitle: str, eyebrow: str = "MY STOCK DASHBOARD"):
    st.markdown(
        f"""
<div class="planx-hero">
  <div class="planx-eyebrow">{html.escape(eyebrow)}</div>
  <h1>{html.escape(title)}</h1>
  <p>{html.escape(subtitle)}</p>
</div>
""",
        unsafe_allow_html=True,
    )


def card(title: str, value: str, note: str = "", status: str = ""):
    status_html = f'<div class="planx-card-note">{html.escape(status)}</div>' if status else ""
    st.markdown(
        f"""
<div class="planx-card">
  <div class="planx-card-title">{html.escape(title)}</div>
  <div class="planx-card-value">{html.escape(value)}</div>
  <div class="planx-card-note">{html.escape(note)}</div>
  {status_html}
</div>
""",
        unsafe_allow_html=True,
    )


def empty_state(title: str, message: str):
    st.markdown(
        f"""
<div class="planx-empty">
  <strong style="color:#334155">{html.escape(title)}</strong><br>
  <span>{html.escape(message)}</span>
</div>
""",
        unsafe_allow_html=True,
    )


def source_badge(label: str, state: str = "wait"):
    cls = {"ok": "planx-status-ok", "bad": "planx-status-bad"}.get(state, "planx-status-wait")
    st.markdown(
        f'<span class="planx-source {cls}">{html.escape(label)}</span>',
        unsafe_allow_html=True,
    )
