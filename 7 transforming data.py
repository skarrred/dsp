# Practical 7: Transforming data

import pandas as pd

# Load data
def load_data(file_path):
    return pd.read_csv(file_path)

# Transform data
def transform_data(df):
    df['Total'] = df['Quantity'] * df['Price']  # Calculate total price
    df['Discounted Price'] = df['Total'] * 0.9  # Apply a 10% discount
    df = df.rename(columns={'Quantity': 'Qty', 'Price': 'Unit Price'})
    return df

if __name__ == "__main__":
    file_path = "data.csv"  # Update with actual file
    df = load_data(file_path)
    transformed_df = transform_data(df)
    print("Transformed Data:")
    print(transformed_df)
