import streamlit as st
import joblib
import pandas as pd

st.set_page_config(page_title="Salary Prediction App", page_icon="💼", layout="centered")

model = joblib.load("salary_model.pkl")

st.title("Salary Prediction App")
st.write("Fill in your profile below to get a predicted salary.")

with st.form("salary_form"):
    col1, col2 = st.columns(2)

    with col1:
        years_exp = st.number_input("Years of Experience", min_value=0.0, max_value=45.0, step=0.5)
        education_level = st.selectbox("Education Level", ["Diploma", "Bachelor's", "Master's", "PhD"])
        skill_level = st.slider("Overall Skill Level (1 = beginner, 10 = expert)", 1, 10, 5)
        communication_score = st.slider("Communication Skills (1 = weak, 10 = excellent)", 1, 10, 5)

    with col2:
        num_languages = st.number_input("Languages Known (spoken)", min_value=0, max_value=15, step=1, value=2)
        num_programming_languages = st.number_input("Languages Known (programming)", min_value=0, max_value=15, step=1, value=2)
        num_tech = st.number_input("Technologies/Frameworks Known", min_value=0, max_value=30, step=1, value=3)
        num_tools = st.number_input("Tools Known (Git, Docker, AWS, etc.)", min_value=0, max_value=25, step=1, value=2)
        num_projects = st.number_input("Projects Completed", min_value=0, max_value=100, step=1, value=3)

    submitted = st.form_submit_button("Predict Salary")

if submitted:
    input_df = pd.DataFrame([{
        "years_experience": years_exp,
        "education_level": education_level,
        "skill_level": skill_level,
        "communication_score": communication_score,
        "num_languages": num_languages,
        "num_tech": num_tech,
        "num_tools": num_tools,
        "num_projects": num_projects,
    }])

    prediction = model.predict(input_df)[0]
    st.success(f"Predicted Salary: ₹{prediction:,.2f}")

    with st.expander("See the profile used for this prediction"):
        st.dataframe(input_df, use_container_width=True)

