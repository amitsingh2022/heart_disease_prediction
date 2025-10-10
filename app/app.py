import streamlit as st
import pandas as pd
import joblib
import os

# ------------------------
# Load trained model
# ------------------------
MODEL_PATH = os.path.join("models", "heart_disease_model.pkl")
if os.path.exists(MODEL_PATH):
    model = joblib.load(MODEL_PATH)
else:
    st.error("Model file not found! Please train the model first.")
    st.stop()

st.title("Heart Disease Prediction App🫀")
st.markdown("Provide the following details to predict your risk of heart disease.")

# ------------------------
# User Inputs
# ------------------------
age = st.slider("Age", 1, 120, 40)
sex = st.selectbox("Sex", ['Male', 'Female'])
chest_pain = st.selectbox("Chest Pain Type", ['ATA', 'NAP', 'TA', 'ASY'])
resting_bp = st.number_input("Resting Blood Pressure (mm Hg)", 80, 200, 120)
cholesterol = st.number_input("Cholesterol (mg/dl)", 100, 600, 200)
fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
resting_ecg = st.selectbox("Resting ECG", ['Normal', 'ST', 'LVH'])
max_hr = st.number_input("Maximum Heart Rate Achieved", 60, 220, 150)
exercise_angina = st.selectbox("Exercise Induced Angina", ['Y', 'N'])
oldpeak = st.number_input("Oldpeak (ST depression by exercise)", 0.0, 6.0, 1.0)
st_slope = st.selectbox("Slope of the Peak Exercise ST Segment", ['Up', 'Flat', 'Down'])

# ------------------------
# Prepare input features
# ------------------------
# Columns expected by the model
expected_columns = [
    'Age', 'RestingBP', 'Cholesterol', 'FastingBS', 'MaxHR', 'Oldpeak',
    'Sex_M', 'ChestPainType_ATA', 'ChestPainType_NAP', 'ChestPainType_TA',
    'RestingECG_Normal', 'RestingECG_ST', 'ExerciseAngina_Y',
    'ST_Slope_Flat', 'ST_Slope_Up'
]

# Initialize all columns as 0
input_data = {col: 0 for col in expected_columns}

# Fill numerical features
input_data['Age'] = age
input_data['RestingBP'] = resting_bp
input_data['Cholesterol'] = cholesterol
input_data['FastingBS'] = fasting_bs
input_data['MaxHR'] = max_hr
input_data['Oldpeak'] = oldpeak

# Fill one-hot encoded features
if sex == 'Male':
    input_data['Sex_M'] = 1
if chest_pain == 'ATA':
    input_data['ChestPainType_ATA'] = 1
elif chest_pain == 'NAP':
    input_data['ChestPainType_NAP'] = 1
elif chest_pain == 'TA':
    input_data['ChestPainType_TA'] = 1

if resting_ecg == 'Normal':
    input_data['RestingECG_Normal'] = 1
elif resting_ecg == 'ST':
    input_data['RestingECG_ST'] = 1

if exercise_angina == 'Y':
    input_data['ExerciseAngina_Y'] = 1

if st_slope == 'Flat':
    input_data['ST_Slope_Flat'] = 1
elif st_slope == 'Up':
    input_data['ST_Slope_Up'] = 1

# Convert to DataFrame
input_df = pd.DataFrame([input_data])

# ------------------------
# Prediction
# ------------------------
if st.button("Predict"):
    prediction = model.predict(input_df)[0]

    if prediction == 1:
        st.error("⚠️ The model predicts that you **may have heart disease.** Please consult a healthcare professional.")
    else:
        st.success("✅ The model predicts that you are **unlikely to have heart disease.** Keep maintaining a healthy lifestyle!")
