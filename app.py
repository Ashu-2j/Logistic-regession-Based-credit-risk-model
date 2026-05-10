import streamlit as st
import pandas as pd
import joblib
import numpy as np

# 1. THE BRAIN: Load your saved model
model = joblib.load('midland_model.pkl')

# 2. THE MENU: Create the website header
st.title("Midland Microfin: Credit Decision Tool")
st.write("Fill in the borrower's details to check for risk.")

# 3. THE QUESTIONS: Create input fields (Layman: The Sliders and Boxes)
st.sidebar.header("Borrower Details")
principal = st.sidebar.number_input("Loan Amount (Principal)", value=1000)
terms = st.sidebar.selectbox("Loan Term (Days)", [7, 15, 30])
age = st.sidebar.slider("Age of Borrower", 18, 70, 30)
gender = st.sidebar.radio("Gender", ["male", "female"])
education = st.sidebar.selectbox("Education Level", 
                                 ["High School or Below", "college", "Bechalor", "Master or Above"])

# 4. PREPARATION: Convert text to numbers (matching your training code)
gender_n = 0 if gender == "male" else 1
edu_map = {'High School or Below': 1, 'college': 2, 'Bechalor': 3, 'Master or Above': 4}
education_n = edu_map[education]

# 5. THE DECISION: Run the model when the button is clicked
if st.button("Calculate Risk Score"):
    # Arrange inputs exactly like your training data
    input_data = np.array([[principal, terms, age, gender_n, education_n]])
    
    # Get the prediction
    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)[0][1] # Probability of Default

    # Show the result to the user
    if prediction[0] == 0:
        st.success(f"APPROVED: This borrower is low risk (Risk: {probability:.2%})")
    else:
        st.error(f"REJECTED: High risk of default detected (Risk: {probability:.2%})")