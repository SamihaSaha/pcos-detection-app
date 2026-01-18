🩺 PCOS Detection System using Machine Learning & Explainable AI

This project is a web-based healthcare application that predicts the risk of Polycystic Ovary Syndrome (PCOS) using machine learning models trained on hormonal, physical, and lifestyle parameters. The system also focuses on model transparency and usability.

🚀 Features

PCOS risk prediction using Machine Learning

XGBoost classification model

SHAP-based Explainable AI (in training phase)

User-friendly Streamlit web interface

Real-time prediction

Online deployment using Streamlit Cloud

📊 Dataset

The dataset was obtained from Kaggle and contains:

Hormonal parameters (AMH, FSH, LH, TSH, etc.)

Physical parameters (BMI, weight, height)

Reproductive health indicators (cycle length, follicle count)

Lifestyle factors

Target label: PCOS (Y/N)

🧠 Machine Learning Model

Algorithm: XGBoost Classifier

Task: Binary Classification (PCOS / No PCOS)

Evaluation Metrics:

Accuracy

Precision

Recall

F1-score

🔍 Explainable AI

SHAP (SHapley Additive Explanations) was used during model training to:

Identify most influential features

Explain individual predictions

Improve model transparency for healthcare applications

🌐 Web Application

The Streamlit web application allows users to:

Enter medical parameters

Get instant PCOS risk prediction

View results in a clear and simple format

🛠 Tech Stack

Python

Pandas

Scikit-learn

XGBoost

SHAP

Streamlit

Joblib

📁 Project Structure
pcos-detection-app/
│
├── app.py
├── pcos_model.pkl
├── feature_names.pkl
├── requirements.txt
├── README.md

▶️ How to Run Locally

Clone the repository

Install dependencies

python -m pip install -r requirements.txt


Run the app

python -m streamlit run app.py

🌍 Online Deployment

The application is deployed using Streamlit Cloud and connected with GitHub for continuous deployment.

📌 Use Case

This system can assist:

Healthcare students

Medical research projects

Early awareness of PCOS risk

Academic machine learning demonstrations

📄 Future Enhancements

PCOS risk percentage score

SHAP visualization inside UI

Medical recommendation system

Mobile-friendly UI

👩‍💻 Author

Samiha Saha
Machine Learning & Healthcare Analytics Project

⚠️ Disclaimer

This system is for educational and research purposes only and should not be used as a substitute for professional medical diagnosis.
