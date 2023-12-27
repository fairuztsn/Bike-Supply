import joblib
import os

def predict():
    # Load the trained model
    model = joblib.load(os.path.join("models", "lgb_model.joblib"))

    # Define the input features
    features = ["Hour", "Holiday", 'Temperature(°C)', 'Humidity(%)',
                'Wind speed (m/s)', 'Visibility (10m)', 'Dew point temperature(°C)',
                'Solar Radiation (MJ/m2)', 'Rainfall(mm)', 'Snowfall (cm)']

    # Input data for prediction
    data = [
        15,  # Hour
        True,  # Holiday
        20,  # Temperature(°C)
        10,  # Humidity(%)
        10,  # Wind speed (m/s)
        10,  # Visibility (10m)
        10,  # Dew point temperature(°C)
        10,  # Solar Radiation (MJ/m2)
        10,  # Rainfall(mm)
        10   # Snowfall (cm)
    ]
    input_data = dict(zip(features, data))
    input_data["Holiday"] = int(input_data["Holiday"])
    input_array = [input_data[feature] for feature in features]
    input_array = [input_array]
    prediction = model.predict(input_array)
    print("Predicted value:", prediction[0])