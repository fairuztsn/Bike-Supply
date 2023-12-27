from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify

import joblib
import os

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data = {
        "Hour": int(request.form["hour"]),
        "Holiday": True if request.form["holiday"] == "true" else False,
        'Temperature(°C)': float(request.form["temperature"]),
        'Humidity(%)': float(request.form["humidity"]),
        'Wind speed (m/s)': float(request.form["wind_speed"]),
        'Visibility (10m)': float(request.form["visibility"]),
        'Dew point temperature(°C)': float(request.form["dew_point_temperature"]),
        'Solar Radiation (MJ/m2)': float(request.form["solar_radiation"]),
        'Rainfall(mm)': float(request.form["rainfall"]),
        'Snowfall (cm)': float(request.form["snowfall"])
    }

    data["Holiday"] = int(data["Holiday"])

    lgb_model = joblib.load(os.path.join("models", "lgb_model.joblib"))
    rf_model = joblib.load(os.path.join("models", "rf_model.joblib"))
    gb_model = joblib.load(os.path.join("models", "gb_model.joblib"))
    
    data_to_predict = [list(data.values())]

    prediction = {
        "LGB": lgb_model.predict(data_to_predict)[0],
        "RF": rf_model.predict(data_to_predict)[0],
        "GB": gb_model.predict(data_to_predict)[0]
    }
    
    return render_template("result.html", data=prediction)

@app.route('/')
def main():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
