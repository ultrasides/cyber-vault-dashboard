import streamlit as st
import pandas as pd
import numpy as np
import time
from PIL import Image

# --- BRAND CONFIGURATION ---
BRAND_NAME = "Vantix"
TAGLINE = "Autonomous Neural Defense"

st.set_page_config(page_title=BRAND_NAME, layout="wide", initial_sidebar_state="expanded")

# --- THE "ENTERPRISE BLUE" THEME ---
st.markdown(f"""
    <style>
    /* Background: Professional Slate Blue */
    .stApp {{
        background-color: #1e293b !important;
        color: #f1f5f9 !important;
    }}
    
    /* Sidebar: Deep Cobalt */
    section[data-testid="stSidebar"] {{
        background-color: #0f172a !important;
        border-right: 2px solid #3b82f6;
    }}

    /* METRIC CARDS: High-Contrast "Frost" Style */
    div[data-testid="metric-container"] {{
        background-color: #334155 !important;
        border: 1px solid #64748b !important;
        padding: 20px !important;
        border-radius: 12px !important;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }}
    
    /* Metric Text: Bright White & Cobalt */
    [data-testid="stMetricValue"] {{
        color: #60a5fa !important;
        font-weight: 800 !important;
        font-family: 'Inter', sans-serif;
    }}
    [data-testid="stMetricLabel"] {{
        color: #cbd5e1 !important;
        font-weight: 500 !important;
    }}

    /* Buttons: Solid Cobalt Blue */
    .stButton>button {{
        background-color: #2563eb !important;
        color: white !important;
        font-weight: bold !important;
        border-radius: 8px !important;
        border: none !important;
        height: 3em !important;
        transition: 0.3s;
    }}
    .stButton>button:hover {{
        background-color: #1d4ed8 !important;
        box-shadow: 0 0 10px rgba(37, 99, 235, 0.4);
    }}

    /* Input Fields */
    input {{
        background-color: #0f172a !important;
        color: white !important;
        border: 1px solid #475569 !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR: LOGO & SYSTEM VITALITY ---
with st.sidebar:
    try:
        # Tries to load your logo
        logo = Image.open("vantix.png")
        st.image(logo, use_container_width=True)
    except:
        st.title(f"🛡️ {BRAND_NAME}")
    
    st.caption(f"v1.1.0 | {TAGLINE}")
    st.divider()
    
    st.subheader("📡 Global Mesh Status")
    st.success("🤖 Neural Engine: ACTIVE")
    st.info("🌐 Network Nodes: 1,850")
    st.warning("⚠️ Latency: 42ms (Elevated)")
    
    if st.button("🚨 EMERGENCY LOCKDOWN"):
        st.error("SYSTEM FROZEN")

# --- MAIN DASHBOARD ---
st.title(f"🛡️ {BRAND_NAME} | Corporate Command")
st.write(f"**Enterprise Security Protocol:** {TAGLINE}")

# --- METRICS SECTION ---
m_col1, m_col2, m_col3, m_col4 = st.columns(4)
m_col1.metric("Active Threats", "12", "+1")
m_col2.metric("Uptime", "99.98%", "Stable")
m_col3.metric("Blocked IPs", "1,042", "+45")
m_col4.metric("Threat Level", "LOW", "-2%")

# --- NEURAL SCANNER ---
st.divider()
st.subheader("🔍 Vantix Neural Analysis")
target = st.text_input("Enter URL or IP for Security Audit:", placeholder="security-audit.vantix.ai")

if st.button("EXECUTE SECURITY SCAN"):
    if target:
        with st.spinner('Syncing with Vantix Intelligence Mesh...'):
            time.sleep(2)
            if "google" in target.lower():
                st.success(f"✅ VERIFIED SAFE: {target}")
            else:
                st.error(f"🚨 THREAT DETECTED: {target} flagged as MALICIOUS.")
    else:
        st.info("Input required for audit.")

# --- DATA VISUALIZATION ---
st.divider()
st.subheader("📊 Traffic Distribution (24h)")
# Creating a dummy dataframe for the chart
chart_data = pd.DataFrame(
    np.random.randint(10, 100, size=(20, 3)),
    columns=['Firewall Blocks', 'Neural Analysis', 'Filtered']
)
st.area_chart(chart_data)
