import streamlit as st
import pandas as pd
import joblib

# Load model and encoders
model = joblib.load("sales_forecasting_model.pkl")
le_product = joblib.load("le_product.pkl")
le_category = joblib.load("le_category.pkl")
le_region = joblib.load("le_region.pkl")

st.set_page_config(page_title="Sales Forecasting App", layout="centered")
st.title("📈 Sales Revenue Forecasting")
st.write("Enter the product details below to predict sales revenue.")

# User Inputs
product = st.selectbox("Select Product ID", le_product.classes_)
category = st.selectbox("Select Product Category", le_category.classes_)
region = st.selectbox("Select Region", le_region.classes_)

# Date Inputs (for month & day)
date = st.date_input("Select Date")

# Feature Engineering from date
month = date.month
day = date.day

# Encode categorical features
encoded_product = le_product.transform([product])[0]
encoded_category = le_category.transform([category])[0]
encoded_region = le_region.transform([region])[0]

# Combine into single input DataFrame
input_data = pd.DataFrame([{
    "Product_ID": encoded_product,
    "Category": encoded_category,
    "Region": encoded_region,
    "Month": month,
    "Day": day
}])

# Predict Button
if st.button("Predict Sales Revenue"):
    prediction = model.predict(input_data)[0]
    st.success(f"💰 Predicted Sales Revenue: ${prediction:,.2f}")
