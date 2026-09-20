import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.set_page_config(page_title="Healthcare Readmission Analytics", page_icon="🏥", layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv("data/healthcare_readmission.csv")

@st.cache_resource
def load_model():
    return joblib.load("models/readmission_xgboost.joblib")

df = load_data()
model = load_model()

st.title("🏥 Hospital Readmission Risk Prediction")
st.caption("Synthetic educational dataset — not for clinical decision-making.")

a,b,c,d = st.columns(4)
a.metric("Patients", f"{len(df):,}")
b.metric("30-Day Readmission", f"{df.readmitted_30_days.mean()*100:.1f}%")
c.metric("Average Stay", f"{df.length_of_stay.mean():.1f} days")
d.metric("Previous Admissions", f"{df.previous_admissions.mean():.1f}")

st.divider()
left,right = st.columns(2)
with left:
    st.subheader("Readmission by Diagnosis")
    st.bar_chart(df.groupby("diagnosis")["readmitted_30_days"].mean().sort_values(ascending=False))
with right:
    st.subheader("Readmission by Admission Type")
    st.bar_chart(df.groupby("admission_type")["readmitted_30_days"].mean().sort_values(ascending=False))

st.divider()
st.header("Patient Readmission Risk Prediction")

c1,c2,c3 = st.columns(3)
with c1:
    age = st.number_input("Age", 18, 90, 55)
    gender = st.selectbox("Gender", ["Female","Male"])
    admission_type = st.selectbox("Admission Type", ["Emergency","Urgent","Elective"])
    diagnosis = st.selectbox("Diagnosis", ["Diabetes","Heart Disease","Respiratory","Kidney Disease","Hypertension","Other"])
with c2:
    length_of_stay = st.number_input("Length of Stay (days)", 1, 30, 5)
    previous_admissions = st.number_input("Previous Admissions", 0, 10, 1)
    emergency_visits = st.number_input("Emergency Visits", 0, 8, 1)
    medication_count = st.number_input("Medication Count", 1, 25, 7)
with c3:
    diagnosis_count = st.number_input("Diagnosis Count", 1, 8, 2)
    lab_tests = st.number_input("Lab Tests", 2, 35, 10)
    days_since_last_admission = st.number_input("Days Since Last Admission", 5, 730, 180)
    discharge = st.selectbox("Discharge Disposition", ["Home","Skilled Nursing Facility","Home Health","Rehabilitation"])

if st.button("Predict Readmission Risk", type="primary"):
    patient = pd.DataFrame([{
        "age": age, "gender": gender, "admission_type": admission_type,
        "diagnosis": diagnosis, "length_of_stay": length_of_stay,
        "previous_admissions": previous_admissions,
        "emergency_visits": emergency_visits,
        "medication_count": medication_count,
        "diagnosis_count": diagnosis_count,
        "lab_tests": lab_tests,
        "days_since_last_admission": days_since_last_admission,
        "discharge_disposition": discharge,
        "age_group": ("18-29" if age < 30 else "30-44" if age < 45 else "45-59" if age < 60 else "60-74" if age < 75 else "75-90")
    }])
    risk = float(model.predict_proba(patient)[0,1])
    st.subheader(f"Estimated 30-Day Readmission Risk: {risk*100:.1f}%")
    if risk >= .60:
        st.error("High-risk category")
    elif risk >= .30:
        st.warning("Moderate-risk category")
    else:
        st.success("Low-risk category")
    st.info("This prediction is a machine-learning demonstration using synthetic data and must not be used for clinical decisions.")
