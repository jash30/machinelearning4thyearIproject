 from fastapi import FastAPI  
import joblib  
import numpy as np  

# Load trained model  
model = joblib.load("../src/model.pkl")  

# Initialize FastAPI  
app = FastAPI()  

@app.post("/predict")  
def predict(fuel_price: float, ev_price: float, gov_incentives: float, charging_stations: float):  
    # Prepare input data  
    features = np.array([[fuel_price, ev_price, gov_incentives, charging_stations]])  
    prediction = model.predict(features)[0]  

    return {"Predicted EV Market Share (%)": prediction}  

if __name__ == "__main__":  
    import uvicorn  
    uvicorn.run(app, host="0.0.0.0", port=8000)  

