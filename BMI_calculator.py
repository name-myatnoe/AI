import streamlit as st
st.title("Welcome to BMI Calculator")

weight=st.number_input("Enter weight(in kgs) : ")
height=st.number_input("Enter height(in cms) : ")
try:
    bmi=weight/((height/100)**2)

except:
    st.text("Enter some value of height")

if(st.button('Calculate BMI')):
    st.text(f"Your BMI is : {bmi}")

    if (bmi<16):
        st.error("Extremely UnderWeight")
    elif(bmi>=16 and bmi<18.5):
        st.warning("UnderWeight")
    elif(bmi>=18.5 and bmi<25):
        st.warning("Healthy")
    elif(bmi>=25 and bmi<30):
        st.warning("OverWeight")
    elif(bmi>=30 ):
        st.error("Extremely Overweight")