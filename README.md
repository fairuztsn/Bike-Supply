# Bike Supply (KR) 🚴‍♂️

This project predicts bike supply based on various factors. The features used for prediction include:

- **Hour**
- **Holiday**
- **Temperature (°C)**
- **Humidity (%)**
- **Wind speed (m/s)**
- **Visibility (10m)**
- **Dew point temperature (°C)**
- **Solar Radiation (MJ/m2)**
- **Rainfall (mm)**
- **Snowfall (cm)**

## Getting Started 🏁

These instructions will help you set up and run the project on your local machine.

### Prerequisites 🛠️

Make sure you have the following installed on your machine:

- **Python** (version 3.12.x)
- **pip** (package installer for Python)
- **Git**

### Clone the Repository 📥

```bash
git clone https://github.com/fairuztsn/Bike-Supply.git
cd Bike-Supply

```

### Create a Python Virtual Environment 🌐
It's good practice to use a virtual environment to manage dependencies. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

If you're using Windows:
```bash
./venv/Scripts/activate
```
### Install Dependencies 📦
Install the required Python packages:

```bash
pip install -r requirements.txt
```
### Run the Jupyter Notebook 📓
Start the Jupyter notebook to interact with the project:

```bash
jupyter notebook
```

Navigate to the notebooks directory and open the main notebook.

### Execute the Run Script 🏃‍♀️
After running the notebook, you might have some additional steps or scripts to execute. If so, run the provided script:

```bash
./run
```
This script runs flask app.
