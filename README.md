# EV Market Share Prediction API

This project is a FastAPI-based web service that predicts the market share of electric vehicles (EVs) based on various factors such as fuel price, EV price, government incentives, and the availability of charging stations.

## Features
- Uses a trained machine learning model (`model.pkl`) for predictions.
- Accepts input values via a REST API endpoint.
- Returns the predicted EV market share as a JSON response.

## Installation

### Prerequisites
Ensure you have the following installed:
- Python 3.7+
- FastAPI
- joblib
- NumPy
- Uvicorn

### Setup
1. Clone this repository:
   ```bash
   git clone <repository_url>
   cd <project_directory>
