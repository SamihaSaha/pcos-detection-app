import streamlit as st
import pandas as pd
import joblib

model = joblib.load("pcos_model.pkl")
features = joblib.load("feature_names.pkl")

st.set_page_config(page_title="PCOS Detection", layout="centered")

st.title("PCOS Risk Detection System")
st.write("Fill basic health details to check PCOS risk.")

with st.form("pcos_form"):

    age = st.slider("Age", 15, 45, 25)
    bmi = st.slider("BMI", 15.0, 40.0, 22.0)
    cycle = st.slider("Menstrual Cycle Length (days)", 20, 45, 28)

    amh = st.number_input("AMH Level")
    fsh = st.number_input("FSH Level")
    lh = st.number_input("LH Level")

    fol_l = st.number_input("Left Ovary Follicle Count")
    fol_r = st.number_input("Right Ovary Follicle Count")

    fast_food = st.selectbox("Frequent Fast Food Consumption?", ["No", "Yes"])

    submit = st.form_submit_button("Check PCOS Risk")

if submit:
    fast_food = 1 if fast_food == "Yes" else 0

    input_data = [[age, bmi, cycle, amh, fsh, lh, fol_l, fol_r, fast_food]]

    df_input = pd.DataFrame(input_data, columns=features)

    prediction = model.predict(df_input)[0]

    if prediction == 1:
        st.error("⚠ High Risk of PCOS Detected")
    else:
        st.success("✅ Low Risk of PCOS")
