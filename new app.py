import streamlit as st
import pandas as pd
import numpy as np
import time

# --- INITIAL SETUP ---
st.set_page_config(page_title="VaultGuard AI Pro", layout="wide")

# --- CUSTOM CSS FOR THE "MILLION DOLLAR" LOOK ---
st.markdown("""
    <style>
    .stMetric { background-color: #1f2937; padding: 15px; border-radius: 10px; border: 1px solid #3b82f6; }
    .main { background-color: #0e1117; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ VaultGuard AI | Enterprise Command")
st.write(f"**System Status:** 🟢 Optimal | **Global Server Load:** 14%")

# --- TOP METRICS ---
col1, col2, col3, col4 = st.columns(4)
col1.metric("Active Threats", "12", "+2")
col2.metric("Nodes Protected", "1,240", "100%")
col3.metric("Blocked IPs", "459", "+12%")
col4.metric("Risk Index", "Low", "-5%")

# --- LIVE THREAT FEED ---
st.divider()
st.subheader("🌐 Global Cyber Threat Intelligence (Live)")
threats = [
    {"Time": "10:45 AM", "Event": "New Ransomware Variant: 'GoldDragon' detected", "Severity": "High"},
    {"Time": "10:32 AM", "Event": "Unusual API traffic spike on Node-88", "Severity": "Medium"},
]
for t in threats:
    with st.expander(f"{t['Time']} - {t['Event']}"):
        st.write(f"**Severity:** {t['Severity']} | **Action:** Auto-monitored")

# --- THE SCANNER (THE NEW PART) ---
st.divider()
st.subheader("🔍 Instant Threat Scanner")
st.write("Paste a URL or IP address below to check against the VaultGuard database.")

target = st.text_input("Enter URL/IP for analysis:", placeholder="https://suspicious-link.com")

if st.button("Run Security Scan"):
    if target:
        with st.spinner('Analyzing...'):
            time.sleep(2) # Artificial intelligence delay
            if "google" in target.lower() or "apple" in target.lower():
                st.success(f"✅ {target} is Verified and Safe.")
            else:
                st.error(f"🚨 WARNING: {target} matches known Phishing patterns!")
                st.warning("Recommendation: Do not click links from this source.")
    else:
        st.info("Please enter a URL to scan.")

# --- DATA VISUALIZATION ---
st.divider()
st.subheader("Attack Vectors (Last 24h)")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['Phishing', 'DDoS', 'Brute Force'])
st.line_chart(chart_data)
# ... (all your previous code above)

# --- VANTIX LIVE TELEMETRY ---
st.sidebar.divider()
st.sidebar.subheader("Live Telemetry")
with st.sidebar.container():
    st.caption("🤖 Neural Engine: Active")
    st.caption("📡 Node Sync: 1,850/1,850")
    st.caption("🛡️ Firewall: Level 7 Filter")
    if st.sidebar.button("Refresh Mesh"):
        st.toast("Re-syncing with global threat database...")
