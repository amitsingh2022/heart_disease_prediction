import streamlit as st
import pandas as pd
import joblib 

model = joblib.load("KNN_heart.pkl")
scaler = joblib.load("scaler.pkl")
expected_columns = joblib.load("columns.pkl")


st.title("Heart Disease Prediction🫀🩺")
st.markdown("Provide the following details to predict the likelihood of heart disease.")

age = st.slider("Age", 1, 120, 40)
sex = st.selectbox("SEX",['Male','Female'])
chest_pain = st.selectbox("Chest Pain Type", ['ATA', 'NAP', 'TA', 'ASY'])
resting_bp = st.number_input("Resting Blood Pressure (in mm Hg)", 80,200,120)
cholesterol = st.number_input("Cholesterol (in mg/dl)", 100,600,200)
fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0,1])
resting_ecg = st.selectbox("Resting ECG", ['Normal', 'ST', 'LVH'])
max_hr = st.number_input("Maximum Heart Rate Achieved", 60,220,150)
exercise_angina = st.selectbox("Exercise Induced Angina", ['Y','N'])
oldpeak = st.number_input("Oldpeak (ST depression induced by exercise)", 0.0,6.0,1.0)
st_slope = st.selectbox("Slope of the peak exercise ST segment", ['Up', 'Flat', 'Down'])


if st.button("Predict"):
    raw_data = {
        'age':age,
        'RestingBP':resting_bp,
        'Cholesterol':cholesterol,
        'FastingBS':fasting_bs,
        'MaxHR':max_hr,
        'Oldpeak':oldpeak,
        'ST_Slope'+ st_slope:1,
        'Sex' +sex:1,
        'ChestPainType'+ chest_pain:1,
        'RestingECG'+ resting_ecg:1,
        'ExerciseAngina'+ exercise_angina:1
    }

    input_df = pd.DataFrame([raw_data])

    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    input_df = input_df[expected_columns]

    scaled_data = scaler.transform(input_df)
    prediction = model.predict(scaled_data)[0]

    if prediction == 1:
        st.error("The model predicts that you may have heart disease. Please consult a healthcare professional for a comprehensive evaluation.")
    else:
        st.success("The model predicts that you are unlikely to have heart disease. However, maintain a healthy lifestyle and regular check-ups.")