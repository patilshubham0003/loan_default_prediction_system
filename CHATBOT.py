from google import genai
import streamlit as st
import os
import streamlit as st
from dotenv import load_dotenv
load_dotenv()

def chatbot():

    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:
         api_key = st.secrets["GOOGLE_API_KEY"]
    
    client = genai.Client(api_key=api_key)

    st.divider()
    st.divider()

    st.title("💰 Loan Default Prediction Chatbot")

    question = st.text_input("Ask about Loan Default features:")

    if st.button("Ask"):

        prompt = f"""
        You are a chatbot for a Loan Default Prediction System.

        Project features:
        Age, Income, LoanAmount, CreditScore, MonthsEmployed,
        NumCreditLines, InterestRate, LoanTerm, DTIRatio,
        Education, EmploymentType, MaritalStatus, HasMortgage,
        HasDependents, LoanPurpose, HasCoSigner, Default.

        Rules:
        - Only answer questions about these features.
        - Explain in simple language.
        - Answer in maximum 3 lines.
        - For unrelated questions, say:
        "I am sorry, I can only tell you about Loan Default Prediction System features."

        User question:
        {question}
        """

        try:
            with st.spinner("Thinking..."):
                interaction = client.interactions.create(
                    model="gemini-3.8-flash",
                    input=prompt
            )

            st.write(interaction.output_text)

        except Exception as e:
            st.error(f"to many questions ask after some time")