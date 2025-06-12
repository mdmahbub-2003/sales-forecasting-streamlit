import streamlit as st
import pandas as pd
import joblib

# Load model and encoders
model = joblib.load("sales_forecasting_model.pkl")
le_product = joblib.load("le_product.pkl")
le_category = joblib.load("le_category.pkl")
le_region = joblib.load("le_region.pkl")

# Load your training dataset to reference default values
data = pd.read_csv("data/cloud_sales_forecasting_3lakh.csv")
data['Date'] = pd.to_datetime(data['Date'], format='%d-%m-%Y')
data['Month'] = data['Date'].dt.month
data['Day'] = data['Date'].dt.day

st.set_page_config(page_title="Sales Forecasting App", layout="centered")
st.title("📈 Sales Revenue Forecasting")
st.write("Enter product details to predict revenue. The app will auto-fill the rest.")

# User Inputs
product = st.selectbox("Select Product ID", le_product.classes_)
category = st.selectbox("Select Product Category", le_category.classes_)
region = st.selectbox("Select Region", le_region.classes_)
date = st.date_input("Select Date")
month = date.month
day = date.day

# Encode user input
encoded_product = le_product.transform([product])[0]
encoded_category = le_category.transform([category])[0]
encoded_region = le_region.transform([region])[0]

# Filter dataset to auto-fill missing inputs
filtered = data[
    (data["Product_ID"] == product) &
    (data["Category"] == category) &
    (data["Region"] == region) &
    (data["Month"] == month) &
    (data["Day"] == day)
]

if filtered.empty:
    # fallback: take average values from whole dataset
    default_row = data[["Cloud_Cost ($)", "Ad_Spend ($)", "Website_Visits", "Units_Sold"]].mean()
else:
    default_row = filtered.iloc[0][["Cloud_Cost ($)", "Ad_Spend ($)", "Website_Visits", "Units_Sold"]]

# Build full input for prediction
input_data = pd.DataFrame([{
    "Product_ID": encoded_product,
    "Category": encoded_category,
    "Region": encoded_region,
    "Cloud_Cost ($)": default_row["Cloud_Cost ($)"],
    "Ad_Spend ($)": default_row["Ad_Spend ($)"],
    "Website_Visits": default_row["Website_Visits"],
    "Units_Sold": default_row["Units_Sold"],
    "Month": month,
    "Day": day
}])

# Predict
if st.button("Predict Sales Revenue"):
    prediction = model.predict(input_data)[0]
    st.success(f"💰 Predicted Sales Revenue: ${prediction:,.2f}")
