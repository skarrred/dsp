# Practical 8: Organizing data

import pandas as pd

# Load data
def load_data(file_path):
    return pd.read_csv(file_path)

# Organize data
def organize_data(df):
    df = df.sort_values(by=['Category', 'Date'])  # Sort by category and date
    df = df.fillna(method='ffill')  # Fill missing values with forward fill
    return df

if __name__ == "__main__":
    file_path = "data.csv"  # Update with actual file
    df = load_data(file_path)
    organized_df = organize_data(df)
    print("Organized Data:")
    print(organized_df)
