import streamlit as st
import pandas as pd
import joblib

model = joblib.load("pcos_modelnew.pkl")
features = joblib.load("features_names.pkl")

st.set_page_config(page_title="PCOS Detection System", layout="centered")

st.title("🩺 PCOS Risk Detection System")
st.write("Fill the details below to check PCOS risk. This tool is for educational purposes only.")

st.markdown("---")

input_data = []

with st.form("pcos_form"):

    st.subheader("Basic Information")

    age = st.slider("Age (years)", 15, 45, 25)
    bmi = st.slider("BMI (Body Mass Index)", 15.0, 40.0, 22.0)
    cycle = st.slider("Menstrual Cycle Length (days)", 20, 45, 28)

    st.markdown("---")
    st.subheader("Hormonal & Medical Parameters")

    amh = st.number_input("AMH Level", help="Anti-Mullerian Hormone: reflects ovarian reserve.")
    fsh = st.number_input("FSH Level", help="Follicle Stimulating Hormone: regulates egg development.")
    lh = st.number_input("LH Level", help="Luteinizing Hormone: triggers ovulation.")
    tsh = st.number_input("TSH Level", help="Thyroid Stimulating Hormone: affects metabolism and cycles.")

    st.markdown("---")
    st.subheader("Ovary Details")

    fol_l = st.number_input("Left Ovary Follicle Count", help="Number of follicles in left ovary.")
    fol_r = st.number_input("Right Ovary Follicle Count", help="Number of follicles in right ovary.")

    st.markdown("---")
    st.subheader("Lifestyle")

    fast_food = st.selectbox("Frequent Fast Food Consumption?", ["No", "Yes"],
                             help="Regular fast food intake can influence hormonal imbalance.")

    submit = st.form_submit_button("Check PCOS Risk")

if submit:

    fast_food = 1 if fast_food == "Yes" else 0

    input_data = [
        age, bmi, cycle,
        amh, fsh, lh, tsh,
        fol_l, fol_r,
        fast_food
    ]

    df_input = pd.DataFrame([input_data], columns=features)

    prediction = model.predict(df_input)[0]

    st.markdown("---")

    if prediction == 1:
        st.error("⚠ High Risk of PCOS Detected")
        st.write("Please consult a healthcare professional for proper diagnosis.")
    else:
        st.success("✅ Low Risk of PCOS Detected")
        st.write("Your parameters indicate a lower risk of PCOS.")
