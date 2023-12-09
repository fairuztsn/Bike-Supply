import plotly.express as px
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import os

def histogram_of_normalized_df(df, features):
    # Tentukan jumlah baris dan kolom pada subplot sesuai dengan jumlah fitur
    num_rows = len(features) // 2
    num_cols = 2

    # Buat subplot
    fig, axes = plt.subplots(num_rows, num_cols, figsize=(15, 15))
    fig.tight_layout(pad=5.0)  # Menambahkan jarak antar subplot

    # Perulangan untuk membuat histogram untuk setiap fitur
    for i, feature in enumerate(features):
        row = i // num_cols
        col = i % num_cols

        # Buat histogram 1D
        axes[row, col].hist(df[feature], bins=30, color='skyblue', edgecolor='black')
        axes[row, col].set_title(f'Histogram of {feature}')
        axes[row, col].set_xlabel(feature)
        axes[row, col].set_ylabel('Frequency')

    # Tampilkan plot
    plt.show()

def normalize_df(df, features):
    return (df[features] - df[features].mean()) / df[features].std()

def remove_outliers_from_normalized_df(df, threshold=3):
    z_scores = np.abs(df)
    df_no_outliers = df[(z_scores < threshold).all(axis=1)]
    return df_no_outliers

if __name__ == "__main__":
    df = pd.read_csv(os.path.join(os.getcwd(), "data", "filtered_data.csv"))

features = ['Temperature(°C)', 'Humidity(%)','Wind speed (m/s)', 'Visibility (10m)', 'Dew point temperature(°C)', 'Solar Radiation (MJ/m2)', 'Rainfall(mm)','Snowfall (cm)']

df_normalized = normalize_df(df, features)
df[features] = remove_outliers_from_normalized_df(df_normalized[features])

df = df.dropna()

# Pisahkan data menjadi fitur (X) dan target (y)
X = df[features] #.values.reshape(-1, 1)
y = df[["Rented Bike Count"]] #.values.reshape(-1,1)

# Bagi data menjadi set pelatihan dan pengujian
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=44)

# Inisialisasi model regresi linear
model = LinearRegression()

# Latih model pada set pelatihan
model.fit(X_train, y_train)

def flatten(l):
    return [item for sublist in l for item in sublist]

predicted = flatten(model.predict(X_test))
expected = flatten(y_test.values)

import plotly.express as px

# Put data to plot in dataframe
df_plot = pd.DataFrame({'expected':expected, 'predicted':predicted})

# Make scatter plot from data
fig = px.scatter(
    df_plot, 
    x='expected', 
    y='predicted',
    title='Predicted vs. Actual Values')

# Add straight line indicating perfect model
fig.add_shape(type="line",
    x0=0, y0=0, x1=50, y1=50,
    line=dict(
        color="Red",
        width=4,
        dash="dot",
    )
)

# Show figure
fig.show()
