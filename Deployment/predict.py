import streamlit as st
import pandas as pd
import numpy as np
import pickle
import json


# load model

# Import model
with open('model_final.pkl', 'rb') as file_1:
    model = pickle.load(file_1)



def run():
    st.title('StreamThis Customer Data Prediction')
    st.image('https://media.licdn.com/dms/image/D4E12AQHfSDwg_APJ-Q/article-cover_image-shrink_600_2000/0/1690878573150?e=2147483647&v=beta&t=Ko0_4eU6f3eic4B3D2MB2B-Ixfbq6-Ydm2XGThJ3b9I', width=500, caption='Churn Customer')


    st.sidebar.title('Input Data in the Form Provided to Predict')
    st.sidebar.title('About this page')
    st.sidebar.write('This is page for predicting customers StreamThis likelihood to Churn')

    # Membuat form untuk input data
    st.write("Input Data for Prediction:")


    # Form input data
    with st.form(key = 'customer'):
        CustomerID = st.text_input('CustomerID')
        Age = st.number_input('Age', min_value=10, max_value=100)
        Gender = st.selectbox('Gender', ['Male', 'Female'])
        Tenure = st.number_input('Tenure', max_value=30)
        Usage_Frequency = st.number_input('Usage Frequency', max_value=200)
        Total_Spend = st.number_input('Total Spend', max_value=5000)
        Last_Interaction = st.slider('Last Interaction', min_value=1, max_value=30)
        Support_Calls = st.slider('Support Calls', min_value=0, max_value=30)
        Payment_Delay = st.slider('Payment Delay', min_value=0, max_value=30)
        Subscription_Type = st.selectbox('Subscription Type', ['Basic', 'Standard', 'Premium'])
        Contract_Length = st.selectbox('Contract Length', ['Monthly', 'Quarterly', 'Annual'])
        

        #Submit button
        submit_button = st.form_submit_button(label = 'Predict')
    if submit_button:
        Customer = {
        'CustomerID': CustomerID,
        'Age': Age,
        'Gender': Gender,
        'Tenure': Tenure,
        'Usage Frequency': Usage_Frequency,
        'Support Calls': Support_Calls,
        'Payment Delay': Payment_Delay,
        'Subscription Type': Subscription_Type,
        'Contract Length': Contract_Length,
        'Total Spend': Total_Spend,
        'Last Interaction': Last_Interaction}

        df = pd.DataFrame([Customer])

        st.write("## Data Summary")
        st.dataframe(df)

 
        # predict
        prediction = model.predict(df)

        st.write("## Data Prediction")
        st.write(f'### Prediction for Customer ID {df["CustomerID"][0]} is {int(prediction[0])}')

        if int(prediction[0]) == 1:
            st.write(f'### Customer ID {df["CustomerID"][0]} will Churn')
            st.write(f'### Go approach this customers and crete promo to prevent this customer in churning')
        else:
            st.write(f'### Customer ID {df["CustomerID"][0]} will not Churn')
            st.write(f'### No immidiate action required')