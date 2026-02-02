import streamlit as st
import pandas as pd
import numpy as np
import time
from PIL import Image

# --- BRAND CONFIGURATION ---
BRAND_NAME = "Vantix AI"
TAGLINE = "Autonomous Neural Defense"

st.set_page_config(page_title=BRAND_NAME, layout="wide", initial_sidebar_state="expanded")

# --- CUSTOM CSS: HIGH-CONTRAST CYBER THEME ---
st.markdown(f"""
    <style>
    /* Force Deep Navy Background */
    .stApp {{
        background-color: #020617;
    }}
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] {{
        background-color: #0f172a !important;
        border-right: 1px solid #1e293b;
    }}

    /* GLOWING METRIC CARDS */
    div[data-testid="metric-container"] {{
        background-color: #1e293b !important;
        border: 1px solid #38bdf8 !important;
        padding: 20px !important;
        border-radius: 15px !important;
        box-shadow: 0 4px 15px rgba(56, 189, 248, 0.1);
    }}
    
    /* Metric Text Visibility */
    [data-testid="stMetricValue"] {{
        color: #38bdf8 !important;
        font-family: 'Courier New', monospace;
    }}
    [data-testid="stMetricLabel"] {{
        color: #f8fafc !important;
        font-weight: bold !important;
    }}

    /* Main Text Visibility */
    h1, h2, h3, p, span {{
        color: #f8fafc !important;
    }}
    
    /* Input & Button Styling */
    .stTextInput>div>div>input {{
        background-color: #0f172a !important;
        color: white !important;
        border: 1px solid #38bdf8 !important;
    }}
    .stButton>button {{
        background-color: #38bdf8 !important;
        color: #020617 !important;
        font-weight: bold !important;
        width: 100%;
        border-radius: 10px;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR: LOGO & STATUS ---
try:
    logo = Image.open("vantix.png")
    st.sidebar.image(logo, use_container_width=True)
except:
    st.sidebar.header(f"🛡️ {BRAND_NAME}")

st.sidebar.caption(f"v1.0.6 | {TAGLINE}")
st.sidebar.divider()
st.sidebar.subheader("📡 System Telemetry")
st.sidebar.info("🤖 Neural Engine: ACTIVE")
st.sidebar.info("🌐 Global Mesh: SYNCED")

if st.sidebar.button("🚨 EMERGENCY LOCKDOWN"):
    st.sidebar.error("CRITICAL: LOCKDOWN INITIATED")

# --- MAIN DASHBOARD ---
st.title(f"🛡️ {BRAND_NAME} | Command Center")
st.write(f"**Enterprise Security Protocol:** {TAGLINE}")

# --- METRIC GRID ---
col1, col2, col3, col4 = st.columns(4)
col1.metric("Active Threats", "14", "+2")
col2.metric("Nodes Protected", "1,850", "100%")
col3.metric("Blocked IPs", "912", "+12%")
col4.metric("Risk Index", "Stable", "-5%")

# --- NEURAL SCANNER ---
st.divider()
st.subheader("🔍 Vantix Neural Scanner")
target = st.text_input("Enter URL or IP for Deep Analysis:", placeholder="https://threat-check.io")

if st.button("EXECUTE NEURAL SCAN"):
    if target:
        with st.spinner('Scouring Global Threat Mesh...'):
            time.sleep(2)
            if "google" in target.lower() or "apple" in target.lower():
                st.success(f"✅ VERIFIED SAFE: {target}")
            else:
                st.error(f"🚨 BREACH DETECTED: {target} flagged as MALICIOUS.")
    else:
        st.warning("Please enter a valid target.")

# --- DATA VISUALIZATION ---
st.divider()
st.subheader("📊 Network Traffic Analysis")
chart_data = pd.DataFrame(np.random.randn(20, 2), columns=['Inbound Scans', 'Outbound Blocks'])
st.area_chart(chart_data)
