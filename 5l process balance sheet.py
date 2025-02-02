# Practical 5l: Write a Python program to process the balance sheet to ensure the only good data is processing

import pandas as pd

# Load balance sheet data
def load_data(file_path):
    return pd.read_csv(file_path)

# Process balance sheet to remove invalid data
def process_balance_sheet(df):
    df = df.dropna()
    df = df[df['Amount'] >= 0]  # Ensuring no negative amounts
    return df

if __name__ == "__main__":
    file_path = "balance_sheet.csv"  # Update with actual file
    df = load_data(file_path)
    processed_df = process_balance_sheet(df)
    print("Processed Balance Sheet:")
    print(processed_df)
