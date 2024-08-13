import pickle
import streamlit as st

# Numpy -->  1.26.4
# Pandas -->  2.1.4
# Sklearn -->  1.3.2

# loading the saved model
credit_model = pickle.load(open("C:/Users/91863/OneDrive/Desktop/Nptel/CodeAlpha/CreditScoreModel/credit_score_model.sav", 'rb'))

# Credit score prediction page
# creating a title
st.title("Credit Score Prediction using Machine Learning")

st.markdown(
    """
    <style>
    text_input {
        font-size: 10px !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# taking the input from the user
# columns for input fields --> means input field in one row
# making 4 columns for rows 
col1, col2, col3, col4 = st.columns(4)
with col1:
    Annual_Income = st.text_input("Annual Income")
with col2:
    Monthly_Inhand_Salary = st.text_input("Monthly In-hand Salary")
with col3:
    Num_Bank_Accounts = st.text_input("Number of bank accounts")
with col4:
    Num_Credit_Cards = st.text_input("Number of Credit Cards")

with col1:
    Interest_Rate = st.text_input("Interest Rate")
with col2:
    Num_of_Loan = st.text_input("Number of Loans")
with col3:
    Outstanding_Debt = st.text_input("Outstanding Debt")
with col4:
    Monthly_Balance = st.text_input("Monthly_Balance")

with col1:
    Delay_from_due_date = st.text_input("Delay from due date")
with col2:
    Num_of_Delayed_Payment = st.text_input('No. of delayed payment')
     

# code for prediction
score_result = ""

# creating the button for the result of prediction
if st.button("Check Credit Score"):
    # credit score prediction model using here check the credit score of the persom --> Standard, Good, Poor
    # giving a list of list to tell that we are predicting for the single data point
    cs_prediction = credit_model.predict(
        [[Annual_Income, Monthly_Inhand_Salary, Num_Bank_Accounts, Num_Credit_Cards, Interest_Rate, Num_of_Loan,
          Delay_from_due_date, Num_of_Delayed_Payment, Outstanding_Debt, Monthly_Balance]])
    
    # 1 --> Poor
    # 0 --> Good
    # 2 --> Standard

    if cs_prediction[0] == 1:
        score_result = "Poor Credit Score"
    elif cs_prediction[0] == 2:
        score_result = "Standard Credit Score"
    else:
        score_result = "Good Credit Score"

    st.success(score_result)
