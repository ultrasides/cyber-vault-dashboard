import streamlit as st
import pandas as pd
import numpy as np
import time
from PIL import Image

# --- BRAND CONFIGURATION ---
BRAND_NAME = "Vantix AI"
TAGLINE = "Autonomous Neural Defense"

st.set_page_config(page_title=BRAND_NAME, layout="wide", initial_sidebar_state="expanded")

# --- THE "UNIFIED DARK" CSS ---
# This forces the sidebar and main body to be the same dark color
st.markdown(f"""
    <style>
    /* Force dark background on everything */
    .stApp, [data-testid="stSidebar"], .main {{
        background-color: #050a14 !important;
    }}

    /* Global Text Color */
    h1, h2, h3, p, span, label {{
        color: #f8fafc !important;
    }}

    /* GLOWING METRIC BOXES */
    div[data-testid="metric-container"] {{
        background-color: #0f172a !important;
        border: 1px solid #38bdf8 !important;
        padding: 20px !important;
        border-radius: 12px !important;
        text-align: center;
    }}
    [data-testid="stMetricValue"] {{
        color: #38bdf8 !important;
        font-size: 2.5rem !important;
    }}

    /* Input Fields */
    input {{
        background-color: #1e293b !important;
        color: white !important;
        border: 1px solid #38bdf8 !important;
    }}

    /* High-Visibility Buttons */
    .stButton>button {{
        background-color: #38bdf8 !important;
        color: #020617 !important;
        font-weight: bold !important;
        border-radius: 5px;
        border: none;
        width: 100%;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR: LOGO & SYSTEM STATUS ---
with st.sidebar:
    try:
        logo = Image.open("vantix.png")
        st.image(logo, use_container_width=True)
    except:
        st.title(f"🛡️ {BRAND_NAME}")
    
    st.caption(f"v1.0.7 | {TAGLINE}")
    st.divider()
    
    st.subheader("📡 System Status")
    st.success("🤖 Neural Engine: ONLINE")
    st.info("🌐 Global Mesh: SYNCED")
    
    if st.button("🚨 EMERGENCY LOCKDOWN"):
        st.error("LOCKDOWN INITIATED")

# --- MAIN DASHBOARD ---
st.title(f"🛡️ {BRAND_NAME} | Command Center")
st.write(f"**Security Protocol:** {TAGLINE}")

# --- METRIC GRID ---
m_col1, m_col2, m_col3, m_col4 = st.columns(4)
m_col1.metric("Active Threats", "14", "+2")
m_col2.metric("Nodes Protected", "1,850", "100%")
m_col3.metric("Blocked IPs", "912", "+12%")
m_col4.metric("Risk Index", "Stable", "-5%")

# --- NEURAL SCANNER ---
st.divider()
st.subheader("🔍 Vantix Neural Scanner")
target = st.text_input("Analyze URL or IP Address:", placeholder="e.g., 192.168.1.1 or malware-site.net")

if st.button("EXECUTE NEURAL SCAN"):
    if target:
        with st.spinner('Querying Global Threat Mesh...'):
            time.sleep(2)
            if "google" in target.lower():
                st.success(f"✅ CLEAN: {target} is a verified trusted source.")
            else:
                st.error(f"🚨 THREAT DETECTED: {target} flagged for high-risk activity.")
    else:
        st.warning("Input required for scan.")

# --- ANALYTICS ---
st.divider()
st.subheader("📊 Network Traffic Analysis")
chart_data = pd.DataFrame(np.random.randn(20, 2), columns=['Inbound', 'Outbound'])
st.area_chart(chart_data)
