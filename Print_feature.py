import streamlit as st

def print_feature(
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
):
    feature_text = f""""
        LOAN DEFAULT PREDICTION SYSTEM
        ==============================

        Project Input Features:

        1. Age
        value: {age}

        2. Income
        value: {income}

        3. Loan Amount
        value: {loan_amount}

        4. Credit Score
        value: {credit_score}

        5. Months Employed
        value: {months_employed}

        6. Number of Credit Lines
        value: {num_credit_lines}

        7. Interest Rate
        value: {interest_rate}

        8. Loan Term
        value: {loan_term}

        9. DTI Ratio
        value: {dti_ratio}

        10. Has Mortgage?
            Yes/No: {has_mortgage}

        11. Has Dependents?
            Yes/No: {has_dependents}

        12. Has Co-Signer?
            Yes/No: {has_cosigner}

        13. Education
            value: {education}

        14. Marital Status
            value: {marital_status}

        15. Employment Type
            value: {employment_type}

        16. Loan Purpose
            value: {loan_purpose}
            
        17. output
            value: {output}    
        """
    st.download_button(
    label="📄 Get Feature TXT",
    data=feature_text,
    file_name="loan_default_features.txt",
    mime="text/plain"
    )