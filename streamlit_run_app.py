import streamlit as st
from predict import predict_price

st.set_page_config(page_title="House Price Predictor", layout="centered")
st.title("House Price Prediction")

st.markdown("**Enter house details:**")

location = st.selectbox("📍 Location (City Type)", ["Tier-3", "Tier-2", "Tier-1", "Metro"])
location_encoded = ["Tier-3", "Tier-2", "Tier-1", "Metro"].index(location)

size = st.number_input("📐 Size (in square feet)", min_value=100, max_value=10000, step=50)
bedrooms = st.number_input("🛏 Bedrooms", min_value=1, max_value=10, step=1)
bathrooms = st.number_input("🛁 Bathrooms", min_value=1, max_value=5, step=1)
parking = st.number_input("🚗 Parking Spaces", min_value=0, max_value=3, step=1)
furnishing = st.selectbox("🪑 Furnishing Status", ["Unfurnished", "Semi-Furnished", "Fully-Furnished"])
furnishing_encoded = ["Unfurnished", "Semi-Furnished", "Fully-Furnished"].index(furnishing)

if st.button("Predict House Price"):
    inputs = [location_encoded, size, bedrooms, bathrooms, parking, furnishing_encoded]
    predicted_price_lakhs = predict_price(inputs)
    price_inr = predicted_price_lakhs * 1_00_000
    st.success(f"🏡 Estimated Price: ₹ {price_inr:,.2f}")
