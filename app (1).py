""
import streamlit as st
import joblib
import numpy as np

model = joblib.load("house_model.pkl")

st.set_page_config(page_title="House Price Predictor", page_icon="🏠", layout="centered")

# General CSS for Streamlit app
st.markdown("""
<style>
/* Fade background image slightly */
.stApp {
    background-image: url("https://images.unsplash.com/photo-1600585154340-be6161a56a0c");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    filter: brightness(0.9); /* 60% brightness for fade effect */
}

/* Make main content container slightly transparent */
.block-container{
    background-color: rgba(0, 0, 0, 0.3); /* darker and transparent */
    padding: 2rem;
    border-radius: 15px;
}

/* Button styling */
div.stButton > button {
    background-color: #2E86C1;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 18px;
}

/* Slider text color */
.css-1aumxhk input[type=range]::-webkit-slider-thumb {
    background-color: white !important;
}
.css-1aumxhk .css-1vv3m87 {
    color: white !important;
}

/* General text color and main body font size */
h1, h2, h3, p, label, .stTextInput, .stSelectbox {
    color: white !important;
    font-size: 18px; /* Increase main body text size */
}

/* Predicted price box styling */
.stAlert {
    background-color: black !important;
    color: white !important;
    font-size: 20px !important;
}
</style>
""", unsafe_allow_html=True)

st.title("🏠 House Price Prediction App")
st.write("Enter the house details below to estimate the price.")

st.divider()

st.subheader("📊 Property Details")
col1, col2 = st.columns(2)
with col1:
    area = st.slider("Area (sq ft)", 500, 10000, 2000)
    bedrooms = st.slider("Bedrooms", 1, 10, 3)
    bathrooms = st.slider("Bathrooms", 1, 5, 2)
with col2:
    stories = st.slider("Stories", 1, 4, 2)
    parking = st.slider("Parking Spaces", 0, 5, 1)

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
    st.success(f"💰 Estimated House Price: P {prediction[0]:,.2f}")