import streamlit as st
import pandas as pd
import time

st.set_page_config(page_title="🚀 Future Sales Predictor", layout="centered")

# Custom CSS
st.markdown("""
<style>
body {
    background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
}
.stApp {
    background: transparent;
}
.big-title {
    font-size: 48px;
    font-weight: bold;
    color: #ffffff;
    text-align: center;
    margin-bottom: 10px;
}
.glass-box {
    background: rgba(255, 255, 255, 0.08);
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.18);
    color: white;
}
.stButton > button {
    background: linear-gradient(135deg, #ff416c, #ff4b2b);
    color: white;
    font-weight: bold;
    border-radius: 10px;
    padding: 10px 24px;
    transition: 0.3s;
}
.stButton > button:hover {
    transform: scale(1.05);
    box-shadow: 0px 0px 15px #ff4b2b;
}
</style>
""", unsafe_allow_html=True)

# 💥 TITLE
st.markdown('<div class="big-title">📊 Future Sales Predictor 🔮</div>', unsafe_allow_html=True)
st.write("")

# 🗂️ Upload Section
with st.container():
    st.markdown('<div class="glass-box">', unsafe_allow_html=True)
    st.subheader("🗂️ Step 1: Upload Your Sales CSV File")
    uploaded_file = st.file_uploader("Choose your .csv file", type="csv")

    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.success("✅ File uploaded successfully!")
        st.dataframe(df.head())
    else:
        st.info("Please upload a file to proceed.")
    st.markdown('</div>', unsafe_allow_html=True)

# 🚀 Prediction Section
st.write("")
with st.container():
    st.markdown('<div class="glass-box">', unsafe_allow_html=True)
    st.subheader("🤖 Step 2: Predict Future Sales")

    if uploaded_file:
        if st.button("🚀 Run Prediction"):
            with st.spinner("AI is predicting... please wait... 🧠"):
                time.sleep(2)  # Simulated delay

                # 🔮 Dummy Prediction Logic
                df["Predicted_Sales"] = df.iloc[:, -1] * 1.25  # Just for demo

                st.success("🎯 Prediction Completed!")
                st.dataframe(df.head())

                # 📥 Download
                csv = df.to_csv(index=False).encode('utf-8')
                st.download_button("📥 Download Results", csv, "predicted_sales.csv", "text/csv")
    else:
        st.warning("⚠️ Please upload a file first.")
    st.markdown('</div>', unsafe_allow_html=True)