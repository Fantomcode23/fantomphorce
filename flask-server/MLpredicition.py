import numpy as np
import joblib

rf_regressor = joblib.load('newpicklefile1.pkl')
recommend_list = []

def preprocess_data(distance, mileage, v_type):
    v_type_4 = 1 if v_type == 4 else 0
    sample = np.array([[mileage, distance, v_type_4]])
    return sample

def generate_recommendations(count, distance, mileage, v_type):
    sample = preprocess_data(distance, mileage, v_type)
    prediction = rf_regressor.predict(sample)[0]

    perturbation = (distance) + (10 / mileage)
    adjusted_prediction = prediction + perturbation
    
    recommend_list.append((adjusted_prediction, count))

recommend_list.sort()
for prediction, count in recommend_list:
    print(f"Route {count}:\tCO2 Emissions Prediction: {prediction:.2f} g/km")
