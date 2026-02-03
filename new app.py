import streamlit as st
import pandas as pd
import numpy as np
import time
from PIL import Image
from datetime import datetime

# --- BRAND CONFIGURATION ---
BRAND_NAME = "Vantix"
TAGLINE = "Autonomous Neural Defense"

st.set_page_config(page_title=f"{BRAND_NAME} | Command Center", layout="wide", initial_sidebar_state="expanded")

# --- SIDEBAR: LOGO, STATUS & DEFENSE TOGGLE ---
with st.sidebar:
    try:
        logo = Image.open("vantix.png")
        st.image(logo, use_container_width=True)
    except:
        st.title(f"🛡️ {BRAND_NAME}")
    
    st.caption(f"Enterprise Security | v1.2.5")
    st.divider()

    # DEFENSE PROTOCOL TOGGLE
    st.subheader("🛡️ Defense Protocol")
    defense_mode = st.toggle("ACTIVE NEURAL DEFENSE", value=False)
    
    # Dynamic Styling Variables
    primary_color = "#dc2626" if defense_mode else "#2563eb" # Red vs Blue
    bg_color = "#fef2f2" if defense_mode else "#f0f9ff"      # Light Red vs Light Blue
    
    if defense_mode:
        st.warning("NEURAL SHIELD: ENGAGED")
    else:
        st.info("SYSTEM STATUS: MONITORING")

    st.divider()
    st.subheader("System Health")
    st.write("✅ All Nodes Active")
    st.write("✅ Neural Mesh: Online")

    st.divider()
    st.subheader("📡 Live Intelligence")
    st.caption(f"Updated: {datetime.now().strftime('%b %d, %Y')}")
    st.markdown("**[URGENT]** FCC warns of telecom ransomware")
    st.markdown("**[NEW]** AI-based browser exploits detected")
    
    st.divider()
    if st.button("🚨 EMERGENCY LOCKDOWN"):
        st.error("LOCKDOWN INITIATED")

# --- DYNAMIC THEME CSS ---
st.markdown(f"""
    <style>
    .stApp {{ background-color: #ffffff !important; }}
    h1, h2, h3, h4, h5, h6, [data-testid="stHeader"] {{
        color: #000000 !important;
        font-family: 'Inter', sans-serif;
        font-weight: 800 !important;
    }}
    p, span, label, div, .stMarkdown {{ color: #1e40af !important; }}
    section[data-testid="stSidebar"] {{
        background-color: #f8fafc !important;
        border-right: 1px solid #e2e8f0;
    }}
    /* Metric Boxes dynamic update */
    div[data-testid="metric-container"] {{
        background-color: {bg_color} !important;
        border: 2px solid {primary_color} !important;
        padding: 15px !important;
        border-radius: 10px !important;
    }}
    [data-testid="stMetricValue"] {{ color: {primary_color} !important; }}
    
    /* Dynamic Button color */
    .stButton>button {{
        background-color: {primary_color} !important;
        color: white !important;
        border-radius: 6px !important;
        border: none !important;
        width: 100%;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- MAIN DASHBOARD ---
status_suffix = " | DEFENSE ACTIVE" if defense_mode else " | Command Center"
st.title(f"🛡️ {BRAND_NAME}{status_suffix}")
st.write(f"Official Security Dashboard for {BRAND_NAME} Neural Systems.")

# --- METRICS SECTION ---
# Values slightly "spike" when defense mode is on for realism
col1, col2, col3, col4 = st.columns(4)
col1.metric("Active Threats", "14" if not defense_mode else "0", "+2" if not defense_mode else "-14")
col2.metric("Nodes Protected", "1,850", "100%")
col3.metric("Blocked IPs", "912", "+12%")
col4.metric("Risk Index", "Stable" if not defense_mode else "SECURED", "-5%")

# --- GLOBAL THREAT MAP ---
st.divider()
st.subheader("🌐 Global Threat Intelligence Mesh")
map_data = pd.DataFrame(
    np.random.randn(50, 2) / [10, 20] + [25, 10], 
    columns=['lat', 'lon']
)
# Map dots turn red in defense mode
map_color = "#dc2626" if defense_mode else "#1e40af"
st.map(map_data, color=map_color, size=25)

# --- TOOLS SECTION ---
st.divider()
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("🔍 Security Scanner")
    target = st.text_input("Analyze URL or IP Address:", placeholder="e.g., example.com")
    if st.button("RUN ANALYSIS"):
        if target:
            with st.spinner('Scanning...'):
                time.sleep(1.5)
                st.success(f"Analysis complete for {target}.")
        else:
            st.info("Input required.")

with col_right:
    st.subheader("📊 Traffic Analysis")
    chart_data = pd.DataFrame(np.random.randn(20, 2), columns=['Inbound', 'Outbound'])
    st.area_chart(chart_data, color=primary_color)

# --- AUDIT LOGS ---
st.divider()
st.subheader("📑 Recent Activity Logs")
audit_data = pd.DataFrame([
    {"Timestamp": "13:45:02", "Event": "Neural Mesh Handshake", "Status": "PASS"},
    {"Timestamp": "13:42:10", "Event": "Active Defense Toggle", "Status": "MANUAL_ON" if defense_mode else "MONITORING"},
    {"Timestamp": "13:30:55", "Event": "System Optimization", "Status": "SUCCESS"},
])
st.table(audit_data)

# --- REPORT EXPORT ---
st.divider()
@st.cache_data
def convert_df_to_csv(df):
    return df.to_csv(index=False).encode('utf-8')

csv_report = convert_df_to_csv(audit_data)
st.download_button(
    label="📩 DOWNLOAD SECURITY REPORT",
    data=csv_report,
    file_name=f"Vantix_Report_{datetime.now().strftime('%Y%m%d')}.csv",
    mime="text/csv",
)
