import streamlit as st
import pandas as pd
import time

st.set_page_config(
    page_title="Future Sales Predictor 🚀",
    page_icon="📊",
    layout="centered",
)

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #1f1c2c, #928dab);
        color: white;
        padding: 20px;
        border-radius: 20px;
    }
    h1, h2, h3, p {
        color: white;
    }
    .stButton > button {
        background: linear-gradient(135deg, #ff416c, #ff4b2b);
        color: white;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px 20px;
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# ------------------------------
st.title("📊 Future Sales Predictor")
st.markdown("### Upload your CSV and predict future sales with AI 🔮")
st.markdown("---")

# SECTION 1 – File Upload
st.header("🗂️ Step 1: Upload CSV File")
uploaded_file = st.file_uploader("Upload your sales data file (.csv)", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("✅ File uploaded successfully!")
    st.dataframe(df.head())
else:
    st.info("👆 Please upload a CSV file to proceed.")

# SECTION 2 – Predict Button
st.markdown("---")
st.header("🤖 Step 2: Predict Sales")

if uploaded_file:
    if st.button("🚀 Run Prediction"):
        with st.spinner("Predicting... please wait ⏳"):
            time.sleep(2)  # simulate processing

            # Dummy prediction logic (replace with real ML model)
            df['Predicted_Sales'] = df.iloc[:, -1] * 1.1  # example logic

            st.success("🎯 Prediction Complete!")
            st.dataframe(df.head())

            # Download option
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button("📥 Download Predictions", data=csv, file_name="predicted_sales.csv", mime='text/csv')
else:
    st.warning("⚠️ Upload a file first to enable prediction.")