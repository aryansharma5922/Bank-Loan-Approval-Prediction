import streamlit as st
import pandas as pd
import pickle

st.title("Bank Loan Approval Prediction")
with open("loan_model.pkl", "rb") as file:
    model = pickle.load(file)
st.subheader("Enter Applicant Details")
ApplicantIncome = st.number_input("Applicant Income")
CoapplicantIncome = st.number_input("Coapplicant Income")
LoanAmount = st.number_input("Loan Amount")
Loan_Amount_Term = st.number_input("Loan Amount Term")
Credit_History = st.selectbox("Credit History", [0.0, 1.0])
Gender = st.selectbox("Gender", ["Male", "Female"])
Married = st.selectbox("Married", ["Yes", "No"])
Dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
Education = st.selectbox("Education", ["Graduate", "Not Graduate"])
Self_Employed = st.selectbox("Self Employed", ["Yes", "No"])
Property_Area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])
input_data = pd.DataFrame({
    'ApplicantIncome': [ApplicantIncome],
    'CoapplicantIncome': [CoapplicantIncome],
    'LoanAmount': [LoanAmount],
    'Loan_Amount_Term': [Loan_Amount_Term],
    'Credit_History': [Credit_History],
    'Gender_Male': [1 if Gender == "Male" else 0],
    'Married_Yes': [1 if Married == "Yes" else 0],
    'Dependents_1': [1 if Dependents == "1" else 0],
    'Dependents_2': [1 if Dependents == "2" else 0],
    'Dependents_3+': [1 if Dependents == "3+" else 0],
    'Education_Not Graduate': [1 if Education == "Not Graduate" else 0],
    'Self_Employed_Yes': [1 if Self_Employed == "Yes" else 0],
    'Property_Area_Semiurban': [1 if Property_Area == "Semiurban" else 0],
    'Property_Area_Urban': [1 if Property_Area == "Urban" else 0]
})
if st.button("Predict Loan Approval"):
    prediction = model.predict(input_data)

    if prediction[0]:
        st.success("Loan Approved ✅")
    else:
        st.error("Loan Not Approved ❌")