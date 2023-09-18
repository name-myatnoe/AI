import streamlit as st
import joblib

st.title('Will you like to predict whether you have diabetes or not?')
diabetes_LR_Model = joblib.load("diabetes_model.pkl")

image = './diabetes.jpg'
st.image(image, caption='Image from https://www.health.harvard.edu/blog/good-news-for-those-with-type-2-diabetes-healthy-lifestyle-matters-2020021718827')
name = st.text_input('Enter your name', '')

if name:
    st.success(f" Hi {name}! This prediction is about the diabetes. For prediction, Please provide your information if applicable.")

    gender = st.radio('Choose your Your Gender: ', ("Male", "Female"))
    age = st.number_input('Enter your age ( 2.0~80.0 ): ', min_value=2, max_value=80, value=2, step=1)
    c_hypertension = st.radio('Do you have hypertension: ', ("Yes", "No"))

    if c_hypertension == "Yes":
        hypertension = 1
    else:
        hypertension = 1

    c_heart_disease = st.radio('Do you have heart_disease: ', ("Yes", "No"))

    if c_heart_disease == "Yes":
        heart_disease = 1
    else:
        heart_disease = 1


    bmi = st.number_input('Enter your bmi level ( 15.0~63.0 ): ', min_value=15, max_value=63, value=15, step=1)
    HbA1c_level = st.number_input('Enter your HbA1c_level ( 3.0~9.0 ): ', min_value=3, max_value=9, value=3, step=1)
    blood_glucose_level = st.number_input('Enter your blood_glucose_level ( 80.0~300.0): ', min_value=80, max_value=300, value=80, step=1)

    data = [age, hypertension, heart_disease, bmi, HbA1c_level, blood_glucose_level]
    result = diabetes_LR_Model.predict([data])
    predict_btn = st.button("Predict")

    if predict_btn:
        if result > 0.5:
            st.success(f"Based on the available data, {name}! You have diabetes")
        else:
            st.success(f"Based on the available data, {name}! You don't have diabetes")