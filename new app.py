import streamlit as st
import pandas as pd
import numpy as np
import time
import requests
from PIL import Image
from datetime import datetime

# --- BRAND CONFIGURATION ---
BRAND_NAME = "Vantix"
TAGLINE = "Autonomous Neural Defense"

st.set_page_config(page_title=f"{BRAND_NAME} | Command Center", layout="wide", initial_sidebar_state="expanded")

# --- AUTHENTICATION & SECRETS ---
# This pulls your API key from .streamlit/secrets.toml (local) or Cloud Secrets (web)
try:
    ABUSE_API_KEY = st.secrets["ABUSE_API_KEY"]
except:
    ABUSE_API_KEY = None

# --- INITIALIZE SESSION STATE ---
if 'heartbeat_data' not in st.session_state:
    st.session_state.heartbeat_data = pd.DataFrame(np.random.randn(20, 1), columns=['Neural Load'])

# --- SIDEBAR: LOGO, STATUS & DEFENSE TOGGLE ---
with st.sidebar:
    try:
        logo = Image.open("vantix.png")
        st.image(logo, use_container_width=True)
    except:
        st.title(f"🛡️ {BRAND_NAME}")
    
    st.caption(f"Enterprise Security | v1.3.0")
    st.divider()

    st.subheader("🛡️ Defense Protocol")
    defense_mode = st.toggle("ACTIVE NEURAL DEFENSE", value=False)
    
    primary_color = "#dc2626" if defense_mode else "#2563eb" 
    bg_color = "#fef2f2" if defense_mode else "#f0f9ff"      
    
    if defense_mode:
        st.warning("NEURAL SHIELD: ENGAGED")
    else:
        st.info("SYSTEM STATUS: MONITORING")

    st.divider()
    st.subheader("System Health")
    health_icon = "🔴" if defense_mode else "✅"
    st.write(f"{health_icon} Neural Mesh: {'OVERDRIVE' if defense_mode else 'ONLINE'}")
    st.write("✅ All Nodes Active")

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
    div[data-testid="metric-container"] {{
        background-color: {bg_color} !important;
        border: 2px solid {primary_color} !important;
        padding: 15px !important;
        border-radius: 10px !important;
    }}
    [data-testid="stMetricValue"] {{ color: {primary_color} !important; }}
    
    .stButton>button {{
        background-color: {primary_color} !important;
        color: white !important;
        border-radius: 6px !important;
        border: none !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- MAIN DASHBOARD ---
status_suffix = " | DEFENSE ACTIVE" if defense_mode else " | Command Center"
st.title(f"🛡️ {BRAND_NAME}{status_suffix}")

# --- METRICS SECTION ---
col1, col2, col3, col4 = st.columns(4)
col1.metric("Active Threats", "0" if defense_mode else "14", "-100%" if defense_mode else "+2")
col2.metric("Nodes Protected", "1,850", "100%")
col3.metric("Blocked IPs", "1,402" if defense_mode else "912", "+490" if defense_mode else "+12%")
col4.metric("Risk Index", "SECURED" if defense_mode else "Stable", "-100%" if defense_mode else "-5%")

# --- GLOBAL THREAT MAP ---
st.divider()
st.subheader("🌐 Global Threat Intelligence Mesh")
map_data = pd.DataFrame(
    np.random.randn(50, 2) / [10, 20] + [25, 10], 
    columns=['lat', 'lon']
)
st.map(map_data, color=primary_color, size=25)

# --- TOOLS SECTION ---
st.divider()
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("🔍 Neural IP Scanner (LIVE)")
    target_ip = st.text_input("Enter IP Address for Deep Analysis:", placeholder="e.g., 8.8.8.8")
    
    if st.button("EXECUTE NEURAL SCAN"):
        if not ABUSE_API_KEY:
            st.error("API Key missing. Add ABUSE_API_KEY to secrets.")
        elif target_ip:
            with st.spinner(f'Vantix is interrogating global nodes for {target_ip}...'):
                url = 'https://api.abuseipdb.com/api/v2/check'
                params = {'ipAddress': target_ip, 'maxAgeInDays': '90'}
                headers = {'Accept': 'application/json', 'Key': ABUSE_API_KEY}
                
                try:
                    response = requests.get(url, headers=headers, params=params)
                    if response.status_code == 200:
                        data = response.json()['data']
                        score = data['abuseConfidenceScore']
                        
                        st.divider()
                        if score > 75:
                            st.error(f"🚨 CRITICAL RISK: {score}% Confidence")
                        elif score > 20:
                            st.warning(f"⚠️ SUSPICIOUS: {score}% Confidence")
                        else:
                            st.success(f"✅ SECURE: {score}% Confidence")
                        
                        # Detailed Data Table
                        st.table(pd.DataFrame({
                            "Attribute": ["Country", "Usage", "Reports", "Domain"],
                            "Intelligence": [data['countryName'], data['usageType'], data['totalReports'], data['domain']]
                        }))
                    else:
                        st.error("Neural Link Rejected: Invalid IP format or API error.")
                except Exception as e:
                    st.error("Connection Interrupted.")
        else:
            st.info("Neural input required.")

with col_right:
    st.subheader("🧠 Neural Heartbeat (Live Pulse)")
    new_val = np.random.randn(1, 1)
    st.session_state.heartbeat_data = pd.concat([st.session_state.heartbeat_data, pd.DataFrame(new_val, columns=['Neural Load'])], ignore_index=True).iloc[-20:]
    st.line_chart(st.session_state.heartbeat_data, color=primary_color)
    if st.button("🔄 REFRESH PULSE"):
        st.rerun()

# --- AUDIT LOGS ---
st.divider()
st.subheader("📑 Recent Activity Logs")
audit_data = pd.DataFrame([
    {"Timestamp": datetime.now().strftime('%H:%M:%S'), "Event": "Neural Mesh Handshake", "Status": "PASS"},
    {"Timestamp": "13:42:10", "Event": "Scanner Query Executed", "Status": "COMPLETED"},
    {"Timestamp": "13:30:55", "Event": "System Optimization", "Status": "SUCCESS"},
])
st.table(audit_data)

# --- EXPORT ---
csv = audit_data.to_csv(index=False).encode('utf-8')
st.download_button("📩 DOWNLOAD SECURITY REPORT", data=csv, file_name=f"Vantix_Report_{datetime.now().strftime('%Y%m%d')}.csv")
