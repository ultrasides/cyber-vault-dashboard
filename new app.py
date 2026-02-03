import streamlit as st
import pandas as pd
import numpy as np
import time
from PIL import Image

# --- BRAND CONFIGURATION ---
BRAND_NAME = "Vantix"
TAGLINE = "Autonomous Neural Defense"

st.set_page_config(page_title=BRAND_NAME, layout="wide", initial_sidebar_state="expanded")

# --- LIGHT THEME CSS ---
st.markdown(f"""
    <style>
    /* 1. Background to White */
    .stApp {{
        background-color: #ffffff !important;
    }}
    
    /* 2. Headings to Black */
    h1, h2, h3, h4, h5, h6, [data-testid="stHeader"] {{
        color: #000000 !important;
        font-family: 'Inter', sans-serif;
        font-weight: 800 !important;
    }}

    /* 3. Text to Blue */
    p, span, label, div, .stMarkdown {{
        color: #1e40af !important; /* Deep Royal Blue */
    }}

    /* Sidebar Styling (Slight Grey for contrast) */
    section[data-testid="stSidebar"] {{
        background-color: #f8fafc !important;
        border-right: 1px solid #e2e8f0;
    }}

    /* Metric Boxes (Light Blue Border) */
    div[data-testid="metric-container"] {{
        background-color: #f0f9ff !important;
        border: 2px solid #3b82f6 !important;
        padding: 15px !important;
        border-radius: 10px !important;
    }}
    
    /* Metric Values (Keep them distinct) */
    [data-testid="stMetricValue"] {{
        color: #1d4ed8 !important;
    }}

    /* Buttons (Solid Blue) */
    .stButton>button {{
        background-color: #2563eb !important;
        color: white !important;
        border-radius: 6px !important;
        border: none !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR: LOGO, STATUS & LIVE FEED ---
with st.sidebar:
    try:
        logo = Image.open("vantix.png")
        st.image(logo, use_container_width=True)
    except:
        st.title(f"🛡️ {BRAND_NAME}")
    
    st.caption(f"Enterprise Security | v1.2.0")
    st.divider()
    
    st.subheader("System Health")
    st.write("✅ All Nodes Active")
    st.write("✅ Neural Mesh: Online")

    st.divider()
    st.subheader("📡 Live Intelligence")
    st.caption("Updated: Feb 3, 2026")
    # Real-time news snippets
    st.markdown("**[URGENT]** FCC warns of telecom ransomware")
    st.markdown("**[NEW]** AI-based browser exploits detected")
    st.markdown("**[GLOBAL]** MS begins NTLM phase-out")
    
    st.divider()
    if st.button("🚨 EMERGENCY LOCKDOWN"):
        st.error("LOCKDOWN INITIATED")

# --- MAIN DASHBOARD ---
st.title(f"🛡️ {BRAND_NAME} | Command Center")
st.write(f"Official Security Dashboard for {BRAND_NAME} Neural Systems.")

# --- METRICS SECTION ---
col1, col2, col3, col4 = st.columns(4)
col1.metric("Active Threats", "14", "+2")
col2.metric("Nodes Protected", "1,850", "100%")
col3.metric("Blocked IPs", "912", "+12%")
col4.metric("Risk Index", "Stable", "-5%")

# --- GLOBAL THREAT MAP ---
st.divider()
st.subheader("🌐 Global Threat Intelligence Mesh")
# Generate random coordinates for visual effect
map_data = pd.DataFrame(
    np.random.randn(50, 2) / [10, 20] + [25, 10], 
    columns=['lat', 'lon']
)
st.map(map_data, color="#1e40af", size=25)
st.caption("📍 Blue indicators represent high-risk IP origins currently being mitigated by Vantix.")

# --- NEURAL SCANNER ---
st.divider()
st.subheader("🔍 Security Scanner")
target = st.text_input("Analyze URL or IP Address:", placeholder="e.g., example.com")

if st.button("RUN ANALYSIS"):
    if target:
        with st.spinner('Scanning...'):
            time.sleep(1.5)
            if "google" in target.lower():
                st.success(f"✅ VERIFIED: {target} is safe.")
            else:
                st.error(f"🚨 ALERT: Potential threat found on {target}.")
    else:
        st.info("Input required.")

# --- DATA VISUALIZATION ---
st.divider()
st.subheader("📊 Traffic Distribution")
chart_data = pd.DataFrame(np.random.randn(20, 2), columns=['Inbound', 'Outbound'])
st.line_chart(chart_data)
# --- DATA VISUALIZATION ---
st.divider()
st.subheader("📊 Traffic Distribution")
chart_data = pd.DataFrame(np.random.randn(20, 2), columns=['Inbound', 'Outbound'])
st.line_chart(chart_data)
