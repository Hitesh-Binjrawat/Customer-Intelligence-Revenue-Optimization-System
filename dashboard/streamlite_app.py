import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from src.decision_engine import predict_customer

st.set_page_config(page_title="Customer Intelligence Sysytem")

st.title("Customer Intelligence Dasboard")

# Inputs
recency = st.slider("Recency (days)", 0, 365, 30)
frequency = st.slider("Frequency", 1, 20, 5)
monetary = st.slider("Monetary Value", 0, 5000, 500)

# Button
if st.button("Predict"):
    result = predict_customer(recency, frequency, monetary)

    st.subheader("Results")

    st.write(f"**Churn Probability:** {result['churn_probability']:.2f}")
    st.write(f"**Segment:** {result['segment']}")
    st.write(f"**Recommended Action:** {result['action']}")