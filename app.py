import joblib 
import pandas as pd
import numpy as np
import streamlit as st
from CHATBOT import chatbot
from Print_feature import print_feature

# encoders
from encoders.encoders import (le_HasMortgage,le_HasDependents,le_HasCoSigner,ohe_education,ohe_MaritalStatus,ohe_EmploymentType,ohe_LoanPurpose)

st.set_page_config(
    page_title="Loan Default Prediction System",
    page_icon="💰"
)


#title
st.title("💰 Loan Default Prediction System")



#inputs

age = st.number_input(
    "Age(18 - 70)",
    min_value=18,
    max_value=70,
    value=30,
    step=1
)

income = st.number_input(
    "Income",
    min_value=0,
    max_value=10000000,
    value=50000,
    step=1000
)

loan_amount = st.number_input(
    "Loan Amount (₹)",
    min_value=0,
    value=100000,
    step=5000
)

credit_score = st.number_input(
    "Credit Score",
    min_value=200,
    max_value=850,
    value=650,
    step=1
)

months_employed = st.number_input(
    "Months Employed",
    min_value=0,
    max_value=200,
    value=60,
    step=1
)

num_credit_lines = st.number_input(
    "Number of Credit Lines",
    min_value=0,
    max_value=5,
    value=5,
    step=1
)

interest_rate = st.number_input(
    "Interest Rate (%)",
    min_value=0.0,
    max_value=30.0,
    value=10.0,
    step=0.1
)

loan_term = st.number_input(
    "Loan Term (Months)",
    min_value=1,
    max_value=60,
    value=51,
    step=1
)

dti_ratio = st.number_input(
    "DTI Ratio (%)",
    min_value=0.0,
    max_value=1.0,
    value=0.3,
    step=0.1
)

has_mortgage = st.selectbox(
    "Has Mortgage?",
    ["Yes", "No"]
)

has_dependents = st.selectbox(
    "Has Dependents?",
    ["Yes", "No"]
)

has_cosigner = st.selectbox(
    "Has Co-Signer?",
    ["Yes", "No"]
)

education = st.selectbox(
    "Education",
    ["Bachelor's", "Master's", "High School", "PhD"]
)

marital_status = st.selectbox(
    "Marital Status",
    ["Divorced", "Married", "Single"]
)

employment_type = st.selectbox(
    "Employment Type",
    ['Full-time', 'Unemployed', 'Self-employed', 'Part-time']
)

loan_purpose = st.selectbox(
    "Loan Purpose",
    ['Other', 'Auto', 'Business', 'Home', 'Education']
)







# model transform

numerical_Arr = np.array([age,income,loan_amount,credit_score,months_employed,num_credit_lines,interest_rate,loan_term,dti_ratio])

le_HasMortgage_Arr = le_HasMortgage.transform([has_mortgage])

le_HasDependents_Arr = le_HasDependents.transform([has_dependents])

le_HasCoSigner__Arr = le_HasCoSigner.transform([has_cosigner])

ohe_education_Arr = ohe_education.transform([[education]]).toarray()

ohe_MaritalStatus_Arr = ohe_MaritalStatus.transform([[marital_status]]).toarray()

ohe_EmploymentType_Arr = ohe_EmploymentType.transform([[employment_type]]).toarray()

ohe_LoanPurpose_Arr = ohe_LoanPurpose.transform([[loan_purpose]]).toarray()

np.set_printoptions(suppress=True)

ALL_INPUTS = np.concatenate((numerical_Arr,le_HasMortgage_Arr,le_HasDependents_Arr,le_HasCoSigner__Arr,ohe_education_Arr[0],ohe_MaritalStatus_Arr[0],ohe_EmploymentType_Arr[0],ohe_LoanPurpose_Arr[0]))



# output model

loan_default_model = joblib.load("loan_default_model.pkl")
output = None

if st.button("Predict Loan Default"):
    prediction = loan_default_model.predict([ALL_INPUTS])
    output=prediction[0]

    if prediction[0] == 1:
        st.error("Loan Default")
    else:
        st.success("Loan Approved")

  
#print
print_feature(
    age,
    income,
    loan_amount,
    credit_score,
    months_employed,
    num_credit_lines,
    interest_rate,
    loan_term,
    dti_ratio,
    has_mortgage,
    has_dependents,
    has_cosigner,
    education,
    marital_status,
    employment_type,
    loan_purpose,
    output
)

#chatbot
chatbot()







