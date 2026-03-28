import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.predictor import predict_salary

st.set_page_config(page_title="Salary Prediction Model", layout="wide")

st.title("Salary Prediction Model")
st.write("Enter your details to estimate your salary.")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Enter Employee Details")

    experience = st.number_input(
        "Years of Experience", min_value=0, max_value=50, value=5
    )

    education = st.selectbox(
        "Education Level",
        ["Bachelor's", "Master's", "PhD"]
    )

    job_role = st.selectbox(
        "Job Role",
        ["Analyst", "Data Scientist", "Engineer", "Manager"]
    )

    location = st.selectbox(
        "Location",
        ["Pune", "Bangalore", "Mumbai", "Delhi"]
    )

    skills = st.number_input(
        "Skills Count", min_value=1, max_value=20, value=5
    )

    predict_btn = st.button("Predict Salary")

with col2:
    st.subheader("Predicted Salary")

    if predict_btn:
        salary = predict_salary(
            experience,
            education,
            job_role,
            location,
            skills
        )

        st.success("✅ Best Model Used: Ridge Regression")
        st.markdown(f"## ₹{salary:,.0f}")