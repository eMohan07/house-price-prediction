import streamlit as st
import pandas as pd

from src.predict import predict_price
from src.utils import validate_house

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠",
    layout="centered"
)

st.title("🏠 House Price Prediction")

st.write("Enter the house details below.")

# -----------------------------
# Cities
# -----------------------------
from src.constants import CITIES

# -----------------------------
# Input Section
# -----------------------------
col1, col2 = st.columns(2)

with col1:

    bedrooms = st.number_input(
    "Bedrooms",
    min_value=0,
    max_value=9,
    value=3,
    step=1
)

    bathrooms = st.number_input(
    "Bathrooms",
    min_value=0.0,
    max_value=8.0,
    value=2.0,
    step=0.5
)

    sqft_living = st.number_input(
    "Living Area (sqft)",
    min_value=370,
    max_value=13540,
    value=2000,
    step=1
)  

    sqft_lot = st.number_input(
    "Lot Area (sqft)",
    min_value=638,
    max_value=1074218,
    value=5000,
    step=1
)

    floors = st.number_input(
    "Floors",
    min_value=1.0,
    max_value=3.5,
    value=1.0,
    step=0.5
)

    waterfront_option = st.selectbox(
        "Waterfront",
        ["No", "Yes"]
    )

with col2:

    view = st.selectbox(
        "View Rating",
        [0, 1, 2, 3, 4]
    )

    condition = st.selectbox(
        "Condition",
        [1, 2, 3, 4, 5]
    )

    sqft_above = st.number_input(
    "Above Ground Area",
    min_value=0,
    value=1500,
    step=1
)

    sqft_basement = st.number_input(
    "Basement Area",
    min_value=0,
    value=500,
    step=1
)

    yr_built = st.number_input(
    "Year Built",
    min_value=1900,
    max_value=2050,
    value=2000,
    step=1
)

    renovated = st.selectbox(
    "Renovated",
    ["No", "Yes"]
)

if renovated == "Yes":
    yr_renovated = st.number_input(
        "Renovation Year",
        min_value=1900,
        max_value=2050,
        value=2000,
        step=1
    )
else:
    yr_renovated = 0

    city = st.selectbox(
    "City",
    sorted(CITIES)
)

waterfront = 1 if waterfront_option == "Yes" else 0

# -----------------------------
# Prediction
# -----------------------------
if st.button("Predict House Price"):

    if not validate_house(
        sqft_living,
        sqft_above,
        sqft_basement
    ):
        st.error(
            "Above Ground Area + Basement Area cannot exceed Living Area."
        )
        st.stop()

    input_df = pd.DataFrame({
        "bedrooms": [bedrooms],
        "bathrooms": [bathrooms],
        "sqft_living": [sqft_living],
        "sqft_lot": [sqft_lot],
        "floors": [floors],
        "waterfront": [waterfront],
        "view": [view],
        "condition": [condition],
        "sqft_above": [sqft_above],
        "sqft_basement": [sqft_basement],
        "yr_built": [yr_built],
        "yr_renovated": [yr_renovated],
        "city": [city]
    })

    prediction = predict_price(input_df)    

    st.success("✅ Prediction completed successfully!")

    st.metric(
    label="🏠 Estimated House Price",
    value=f"${prediction:,}"
)
    st.subheader("Property Details")
    st.table(input_df)

st.divider()

st.caption("Model : Linear Regression")
st.caption("Framework : Scikit-learn Pipeline")
st.caption("Frontend : Streamlit")
