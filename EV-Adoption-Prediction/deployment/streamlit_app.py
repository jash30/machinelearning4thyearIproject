 import streamlit as st  
import requests  

# Title  
st.title("EV Market Share Prediction")  
st.write("Enter the details below to predict EV adoption trends.")  

# User Inputs  
fuel_price = st.number_input("Fuel Price (per liter/gallon)", min_value=0.0, value=3.5)  
ev_price = st.number_input("EV Price (average)", min_value=0.0, value=40000.0)  
gov_incentives = st.number_input("Government Incentives ($)", min_value=0.0, value=5000.0)  
charging_stations = st.number_input("Number of Charging Stations", min_value=0, value=10000)  

# API Call Button  
if st.button("Predict EV Market Share"):  
    input_data = {  
        "fuel_price": fuel_price,  
        "ev_price": ev_price,  
        "gov_incentives": gov_incentives,  
        "charging_stations": charging_stations  
    }  
    
    # Call FastAPI  
    response = requests.post("http://127.0.0.1:8000/predict", json=input_data)  

    if response.status_code == 200:  
        result = response.json()  
        st.success(f"Predicted EV Market Share: {result['Predicted EV Market Share (%)']:.2f}%")  
    else:  
        st.error("Error: Unable to get prediction. Make sure the API is running.")  

