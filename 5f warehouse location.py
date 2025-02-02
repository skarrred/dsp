# Practical 5f: Write a Python/R program to plan the location of a warehouse from the given data

import pandas as pd
import numpy as np

# Load data
def load_data(file_path):
    return pd.read_csv(file_path)

# Find central location
def find_central_warehouse(df):
    mean_lat = np.mean(df['Latitude'])
    mean_long = np.mean(df['Longitude'])
    return mean_lat, mean_long

if __name__ == "__main__":
    file_path = "warehouse_data.csv"  # Update with actual file
    df = load_data(file_path)
    lat, long = find_central_warehouse(df)
    print(f"Optimal warehouse location: Latitude {lat}, Longitude {long}")
