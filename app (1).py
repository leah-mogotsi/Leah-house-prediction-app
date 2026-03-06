""
import streamlit as st
import joblib
import numpy as np

model = joblib.load("house_model.pkl")

st.set_page_config(page_title="House Price Predictor", page_icon="🏠", layout="centered")

st.title("🏠 House Price Prediction App")
st.write("Enter the house details below to estimate the price.")

st.divider()

st.subheader("📊 Property Details")

col1, col2 = st.columns(2)

with col1:
    area = st.number_input("Area (sq ft)", min_value=0)
    bedrooms = st.number_input("Bedrooms", min_value=0)
    bathrooms = st.number_input("Bathrooms", min_value=0)

with col2:
    stories = st.number_input("Stories", min_value=0)
    parking = st.number_input("Parking Spaces", min_value=0)

st.divider()

st.subheader("🏡 Additional Features")

col3, col4 = st.columns(2)

with col3:
    mainroad = st.selectbox("Main Road Access", ["yes", "no"])
    guestroom = st.selectbox("Guest Room", ["yes", "no"])

with col4:
    basement = st.selectbox("Basement", ["yes", "no"])
    airconditioning = st.selectbox("Air Conditioning", ["yes", "no"])

st.divider()

if st.button("🔮 Predict Price"):

    features = np.array([[area, bedrooms, bathrooms, stories,
                          1 if mainroad=="yes" else 0,
                          1 if guestroom=="yes" else 0,
                          1 if basement=="yes" else 0,
                          0,
                          1 if airconditioning=="yes" else 0,
                          parking,
                          0,
                          1]])

    prediction = model.predict(features)

    st.success(f"💰 Estimated House Price: {prediction[0]:,.2f}")
    