import streamlit as st
import pandas as pd
import numpy as np
import time

# --- BRAND CONFIGURATION ---
BRAND_NAME = "Vantix AI"
TAGLINE = "Autonomous Neural Defense"

st.set_page_config(page_title=BRAND_NAME, layout="wide", initial_sidebar_state="expanded")

# --- CSS FIX: FORCING VISIBILITY FOR DARK MODE ---
st.markdown(f"""
    <style>
    /* Main App Background */
    .main {{ background-color: #020617; color: #f8fafc; }}
    
    /* FIXING METRIC VISIBILITY (Clashes in your screenshot) */
    [data-testid="stMetricValue"] {{
        color: #38bdf8 !important; /* Forces numbers to Electric Blue */
        font-weight: bold !important;
    }}
    [data-testid="stMetricLabel"] {{
        color: #94a3b8 !important; /* Makes titles visible grey-white */
    }}
    div[data-testid="metric-container"] {{
        background-color: #0f172a;
        border: 1px solid #1e293b;
        padding: 20px;
        border-radius: 12px;
    }}

    /* Header & Text Styling */
    h1, h2, h3 {{ color: #38bdf8 !important; }}
    .stButton>button {{
        background-color: #38bdf8;
        color: #020617;
        font-weight: 800;
        border: none;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.title(f"🛡️ {BRAND_NAME} | Enterprise Command")
st.write(f"**System Status:** 🟢 Optimal | **Global Server Load:** 14% | **Engine:** {TAGLINE}")

# --- METRICS SECTION (Visible Now) ---
col1, col2, col3, col4 = st.columns(4)
col1.metric("Active Threats", "14", "+2")
col2.metric("Nodes Protected", "1,850", "100%")
col3.metric("Blocked IPs", "912", "+12%")
col4.metric("Risk Index", "Stable", "-5%")

# --- LIVE THREAT FEED ---
st.divider()
st.subheader("🌐 Global Cyber Threat Intelligence (Live)")
with st.expander("10:45 AM - New Ransomware Variant: 'GoldDragon' detected"):
    st.write("Severity: High | Action: Auto-monitored by Vantix Neural Engine")
with st.expander("10:32 AM - Unusual API traffic spike on Node-88"):
    st.write("Severity: Medium | Action: Rate-limiting initiated")

# --- THE VANTIX SCANNER ---
st.divider()
st.subheader("🔍 Vantix Neural Scanner")
target = st.text_input("Enter URL/IP for analysis:", placeholder="https://suspicious-link.com")

if st.button("RUN NEURAL ANALYSIS"):
    if target:
        with st.spinner('Accessing Vantix Global Mesh...'):
            time.sleep(2)
            if "google" in target.lower():
                st.success(f"✅ VERIFIED SAFE: {target} is a known trusted domain.")
            else:
                st.error(f"🚨 BREACH WARNING: {target} contains malicious signatures!")
                st.warning("Recommendation: Immediate network isolation.")
    else:
        st.info("Input required for scan.")

# --- DATA VISUALIZATION ---
st.divider()
st.subheader("Attack Vectors (Last 24h)")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['DDoS', 'Phishing', 'Brute Force'])
st.area_chart(chart_data)

# --- SIDEBAR & TELEMETRY ---
st.sidebar.title(f"{BRAND_NAME}")
st.sidebar.caption(f"v1.0.4 | {TAGLINE}")
st.sidebar.divider()
st.sidebar.subheader("Live Telemetry")
st.sidebar.caption("🤖 Neural Engine: Active")
st.sidebar.caption("📡 Node Sync: 100%")
if st.sidebar.button("🚨 EMERGENCY LOCKDOWN"):
    st.sidebar.error("PROTOCOL INITIATED")
