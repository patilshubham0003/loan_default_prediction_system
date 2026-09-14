import joblib 

le_HasMortgage = joblib.load("./encoders/le_HasMortgage.pkl")

le_HasDependents = joblib.load("./encoders/le_HasDependents.pkl")

le_HasCoSigner = joblib.load("./encoders/le_HasCoSigner.pkl")

ohe_education = joblib.load("./encoders/ohe_education.pkl")

ohe_MaritalStatus = joblib.load("./encoders/ohe_MaritalStatus.pkl")

ohe_EmploymentType = joblib.load("./encoders/ohe_EmploymentType.pkl")

ohe_LoanPurpose = joblib.load("./encoders/ohe_LoanPurpose.pkl")


