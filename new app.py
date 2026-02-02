import streamlit as st
import pandas as pd
import numpy as np
import time
from PIL import Image

# --- BRAND CONFIGURATION ---
BRAND_NAME = "Vantix AI"
TAGLINE = "Autonomous Neural Defense"

st.set_page_config(page_title=BRAND_NAME, layout="wide", initial_sidebar_state="expanded")

# --- FORCE DARK THEME & VISIBILITY CSS ---
st.markdown(f"""
    <style>
    /* Force Dark Background for the whole app */
    .stApp {{
        background-color: #020617;
    }}
    
    /* Sidebar styling */
    section[data-testid="stSidebar"] {{
        background-color: #0f172a !important;
    }}

    /* Metric Box Visibility Fix */
    div[data-testid="metric-container"] {{
        background-color: #1e293b;
        border: 1px solid #38bdf8;
        padding: 15px;
        border-radius: 10px;
        color: white !important;
    }}
    [data-testid="stMetricValue"] {{
        color: #38bdf8 !important;
    }}
    [data-testid="stMetricLabel"] {{
        color: #f8fafc !important;
    }}

    /* Text Colors */
    h1, h2, h3, p, span {{
        color: #f8fafc !important;
    }}
    
    /* Button Styling */
    .stButton>button {{
        background-color: #38bdf8;
        color: #020617;
        font-weight: bold;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR: LOGO & TELEMETRY ---
try:
    logo = Image.open("vantix.png")
    st.sidebar.image(logo, use_container_width=True)
except:
    st.sidebar.title(f"🛡️ {BRAND_NAME}")

st.sidebar.caption(f"v1.0.5 | {TAGLINE}")
st.sidebar.divider()
st.sidebar.subheader("Live Telemetry")
st.sidebar.caption("🤖 Neural Engine: Active")
st.sidebar.caption("📡 Node Sync: 100%")

if st.sidebar.button("🚨 EMERGENCY LOCKDOWN"):
    st.sidebar.error("PROTOCOL INITIATED")

# --- MAIN INTERFACE ---
st.title(f"🛡️ {BRAND_NAME} | Enterprise Command")
st.write(f"**System Status:** 🟢 Optimal | **Global Load:** 14%")

# --- METRICS SECTION ---
col1, col2, col3, col4 = st.columns(4)
col1.metric("Active Threats", "14", "+2")
col2.metric("Nodes Protected", "1,850", "100%")
col3.metric("Blocked IPs", "912", "+12%")
col4.metric("Risk Index", "Stable", "-5%")

# --- THE SCANNER ---
st.divider()
st.subheader("🔍 Vantix Neural Scanner")
target = st.text_input("Enter URL/IP for analysis:", placeholder="https://suspicious-link.com")

if st.button("RUN NEURAL ANALYSIS"):
    if target:
        with st.spinner('Accessing Vantix Global Mesh...'):
            time.sleep(2)
            if "google" in target.lower():
                st.success(f"✅ VERIFIED SAFE: {target}")
            else:
                st.error(f"🚨 BREACH WARNING: Malicious signatures detected!")
    else:
        st.info("Input required for scan.")

# --- DATA VISUALIZATION ---
st.divider()
st.subheader("Attack Vectors (Last 24h)")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['DDoS', 'Phishing', 'Brute Force'])
st.area_chart(chart_data)
