import streamlit as st
import pandas as pd
import numpy as np
import requests

st.set_page_config(page_title="VaultGuard AI Pro", layout="wide", initial_sidebar_state="expanded")

# --- CUSTOM CSS FOR "DARK MODE" TECH LOOK ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stMetric { background-color: #1f2937; padding: 15px; border-radius: 10px; border: 1px solid #3b82f6; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ VaultGuard AI | Enterprise Command")
st.write(f"**System Status:** 🟢 Optimal | **Global Server Load:** 14%")

# --- REAL-TIME METRICS ---
col1, col2, col3, col4 = st.columns(4)
col1.metric("Active Threats", "12", "+2")
col2.metric("Nodes Protected", "1,240", "100%")
col3.metric("Blocked IPs", "459", "+12%")
col4.metric("Risk Index", "Low", "-5%")

# --- THE "MILLION DOLLAR" UPGRADE: LIVE NEWS FEED ---
st.divider()
st.subheader("🌐 Global Cyber Threat Intelligence (Live)")

# We are simulating a live API call to a threat database
threats = [
    {"Time": "10:45 AM", "Event": "New Ransomware Variant: 'GoldDragon' detected in SE Asia", "Severity": "High"},
    {"Time": "10:32 AM", "Event": "Unusual API traffic spike detected on Node-88", "Severity": "Medium"},
    {"Time": "09:15 AM", "Event": "Database 'Vault-1' successfully encrypted and backed up", "Severity": "Safe"},
]

for threat in threats:
    with st.expander(f"{threat['Time']} - {threat['Event']}"):
        st.write(f"**Severity Level:** {threat['Severity']}")
        st.write("Suggested Action: Update firewall rules to block Port 445.")

# --- VISUALIZATION ---
st.divider()
st.subheader("Attack Vectors (Last 24h)")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['Phishing', 'DDoS', 'Brute Force'])
st.line_chart(chart_data)

if st.button("🚨 TRIGGER EMERGENCY ISOLATION"):
    st.error("Protocol Delta Initiated. All systems locked down.")
