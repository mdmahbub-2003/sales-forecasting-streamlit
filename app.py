import streamlit as st
import pandas as pd
import time

# Page config
st.set_page_config(
    page_title="🔥 AI Sales Predictor",
    page_icon="📈",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for tadhakta-badhakta look
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Orbitron', sans-serif;
        background: radial-gradient(ellipse at center, #0f0c29 0%, #302b63 50%, #24243e 100%) !important;
        color: #00ffe7;
    }

    .stApp {
        animation: pulseGlow 5s infinite;
    }

    @keyframes pulseGlow {
        0% { box-shadow: 0 0 10px #00ffe7; }
        50% { box-shadow: 0 0 30px #00ffe7; }
        100% { box-shadow: 0 0 10px #00ffe7; }
    }

    .main-title {
        text-align: center;
        font-size: 3em;
        color: #00ffe7;
        text-shadow: 0 0 10px #00ffe7;
        margin-bottom: 30px;
    }

    .footer {
        text-align: center;
        font-size: 0.9em;
        color: #aaa;
        margin-top: 50px;
    }

    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="main-title">⚡ AI Sales Predictor</div>', unsafe_allow_html=True)

# Upload Section
uploaded_file = st.file_uploader("📤 Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    with st.spinner('🚀 Predicting future sales...'):
        time.sleep(2)  # Simulating prediction delay

        df = pd.read_csv(uploaded_file)
        st.success("✅ File uploaded successfully!")

        st.subheader("📊 Preview of Uploaded Data")
        st.dataframe(df.head())

        # Dummy prediction (replace with real model)
        st.subheader("📈 Predicted Sales")
        df['Predicted_Sales'] = df.iloc[:, -1].apply(lambda x: round(x * 1.2, 2))  # Dummy multiplier
        st.dataframe(df[['Predicted_Sales']])

# Footer
st.markdown('<div class="footer">Made with ❤️ by Mudassir Inam</div>', unsafe_allow_html=True)
