import streamlit as st
import requests

st.title("Loan Approval Predictor")

applicant_income = st.slider("Applicant Income ($)", 1000, 10000, 4000)
credit_score = st.slider("Credit Score", 300, 850, 700)
loan_amount = st.slider("Loan Amount ($)", 50000, 500000, 200000)
loan_term_months = st.slider("Loan Term (Months)", 60, 360, 180)
num_dependents = st.slider("Number of Dependents", 0, 5, 1)

if st.button("Predict Loan Approval"):
    url = "http://127.0.0.1:5000/predict"   
    data = {
        "applicant_income": applicant_income,
        "credit_score": credit_score,
        "loan_amount": loan_amount,
        "loan_term_months": loan_term_months,
        "num_dependents": num_dependents
    }
    response = requests.post(url, json=data)
    result = response.json()
    
    if result['loan_approval_prediction'] == 1:
        st.success("Loan Approved ✅")
    else:
        st.error("Loan Not Approved ❌")