import streamlit as st
import joblib
import numpy as np


model = joblib.load("salary_model.pkl")


st.title("💼 Salary Prediction App")
st.write("Enter years of experience to predict salary")


years_exp = st.number_input("Years of Experience:", min_value=0.0, step=0.1)

if st.button("Predict Salary"):
    prediction = model.predict(np.array([[years_exp]]))
    st.success(f"Predicted Salary: ₹{prediction[0]:,.2f}")
