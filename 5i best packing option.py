# Practical 5i: Write a Python program to delete the best packing option to ship in container from the given data

import pandas as pd

# Load data
def load_data(file_path):
    return pd.read_csv(file_path)

# Delete the best packing option
def delete_best_packing_option(df):
    best_option_index = df['Efficiency'].idxmax()
    df = df.drop(best_option_index)
    return df

if __name__ == "__main__":
    file_path = "packing_options.csv"  # Update with actual file
    df = load_data(file_path)
    updated_df = delete_best_packing_option(df)
    print("Updated Packing Options:")
    print(updated_df)
