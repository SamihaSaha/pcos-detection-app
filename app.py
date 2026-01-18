import streamlit as st
import pandas as pd
import joblib

model = joblib.load("pcos_model.pkl")
features = joblib.load("feature_names.pkl")

st.title("PCOS Detection System")

input_data = []

for col in features:
    value = st.number_input(col)
    input_data.append(value)

if st.button("Predict PCOS"):
    df_input = pd.DataFrame([input_data], columns=features)
    prediction = model.predict(df_input)[0]

    if prediction == 1:
        st.error("PCOS Detected")
    else:
        st.success("No PCOS Detected")
