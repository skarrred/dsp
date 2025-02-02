# Practical 5m: Write a Python program to generate payroll from the given data

import pandas as pd

# Load payroll data
def load_data(file_path):
    return pd.read_csv(file_path)

# Generate payroll
def generate_payroll(df):
    df['Net Salary'] = df['Basic Pay'] + df['Allowances'] - df['Deductions']
    return df[['Employee ID', 'Name', 'Net Salary']]

if __name__ == "__main__":
    file_path = "payroll_data.csv"  # Update with actual file
    df = load_data(file_path)
    payroll_df = generate_payroll(df)
    print("Generated Payroll:")
    print(payroll_df)
