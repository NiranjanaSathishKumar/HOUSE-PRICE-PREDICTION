import joblib
import numpy as np

model = joblib.load("indian_house_model.pkl")

def predict_price(features):
    features_array = np.array(features).reshape(1, -1)
    prediction = model.predict(features_array)[0]
    return prediction  # price in lakhs
