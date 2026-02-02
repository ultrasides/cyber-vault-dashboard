import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="VaultGuard AI", layout="wide")

st.title("🛡️ VaultGuard AI: Enterprise Security Command")

# Sidebar Stats
st.sidebar.header("System Status")
st.sidebar.success("Firewall: ACTIVE")
st.sidebar.warning("Threat Level: MODERATE")

# Main Dashboard
col1, col2, col3 = st.columns(3)
col1.metric("Active Threats", "12", "+2")
col2.metric("Nodes Protected", "1,240", "100%")
col3.metric("Blocked IPs", "459", "+12%")

st.subheader("Recent Security Events")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['DDoS', 'Phishing', 'Malware'])
st.area_chart(chart_data)

st.info("System performing within normal parameters. No critical breaches detected in the last 24h.")
