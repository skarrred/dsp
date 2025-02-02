# Practical 5d: Write a Python/R program to pick the content for Billboards from the given data

import pandas as pd

# Load data
def load_data(file_path):
    return pd.read_csv(file_path)

# Select top advertisements based on ranking
def select_billboard_content(df, top_n=5):
    return df.nlargest(top_n, 'Score')

if __name__ == "__main__":
    file_path = "billboard_data.csv"  # Update with actual file
    df = load_data(file_path)
    top_ads = select_billboard_content(df)
    print(top_ads)
