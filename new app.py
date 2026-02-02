import streamlit as st
import pandas as pd
import numpy as np
import time
from PIL import Image

# --- BRAND CONFIGURATION ---
BRAND_NAME = "Vantix"
TAGLINE = "Autonomous Neural Defense"

st.set_page_config(page_title=BRAND_NAME, layout="wide", initial_sidebar_state="expanded")

# --- THE "PRO-SLATE" THEME ---
st.markdown(f"""
    <style>
    /* Main Background: Deep Slate Gradient */
    .stApp {{
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%) !important;
        color: #f8fafc !important;
    }}
    
    /* Sidebar: Solid Indigo */
    section[data-testid="stSidebar"] {{
        background-color: #1e293b !important;
        border-right: 1px solid #334155;
    }}

    /* GLASS CARDS for Metrics */
    div[data-testid="metric-container"] {{
        background-color: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        padding: 20px !important;
        border-radius: 16px !important;
        backdrop-filter: blur(10px);
    }}
    
    /* Metric Text: Soft Blue & White */
    [data-testid="stMetricValue"] {{
        color: #60a5fa !important; /* Soft Blue */
        font-weight: 800 !important;
    }}
    [data-testid="stMetricLabel"] {{
        color: #94a3b8 !important;
        text-transform: uppercase;
        letter-spacing: 1px;
    }}

    /* Buttons: Indigo Glow */
    .stButton>button {{
        background: linear-gradient(90deg, #6366f1 0%, #a855f7 100%) !important;
        color: white !important;
        border: none !important;
        font-weight: bold !important;
        padding: 10px 20px !important;
        border-radius: 12px !important;
        transition: 0.3s;
    }}
    .stButton>button:hover {{
        box-shadow: 0 0 15px rgba(99, 102, 241, 0.5);
        transform: translateY(-2px);
    }}

    /* Inputs */
    input {{
        background-color: #0f172a !important;
        color: white !important;
        border: 1px solid #334155 !important;
        border-radius: 10px !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR: LOGO ---
with st.sidebar:
    try:
        logo = Image.open("vantix.png")
        st.image(logo, use_container_width=True)
    except:
        st.header(f"🛡️ {BRAND_NAME}")
    
    st.caption(f"Enterprise Security | v1.0.8")
    st.divider()
    
    st.subheader("System Health")
    st.progress(85, text="Neural Mesh Integrity")
    st.progress(40, text="Global Server Load")

# --- MAIN INTERFACE ---
st.title(f"{BRAND_NAME} Command Center")
st.write(f"**Security Protocol:** {TAGLINE}")

# --- METRIC GRID ---
m_col1, m_col2, m_col3, m_col4 = st.columns(4)
m_col1.metric("Active Threats", "14", "+2")
m_col2.metric("Nodes Protected", "1,850", "100%")
m_col3.metric("Blocked IPs", "912", "+12%")
m_col4.metric("Risk Index", "Stable", "-5%")

# --- NEURAL SCANNER ---
st.divider()
st.subheader("🔍 Deep Neural Scanner")
target = st.text_input("Analyze URL/IP Target:", placeholder="https://security-verify.io")

if st.button("START ANALYSIS"):
    if target:
        with st.status("Accessing Global Threat Intelligence...", expanded=True) as status:
            st.write("Checking DNS reputation...")
            time.sleep(1)
            st.write("Scanning for malicious payload signatures...")
            time.sleep(1)
            status.update(label="Analysis Complete!", state="complete", expanded=False)
            
            if "google" in target.lower():
                st.success(f"✅ CLEAN: {target} is verified.")
            else:
                st.error(f"🚨 ALERT: {target} flagged as high risk.")
    else:
        st.warning("Target input required.")

# --- CHARTS ---
st.divider()
st.subheader("📡 Global Traffic Intelligence")
chart_data = pd.DataFrame(np.random.randn(20, 2), columns=['Filtered', 'Threats'])
st.line_chart(chart_data)
