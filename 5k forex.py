# Practical 5k: Write a Python program to create simple forex trading planner from the given data

import pandas as pd

# Load forex data
def load_data(file_path):
    return pd.read_csv(file_path)

# Basic trading strategy
def simple_trading_strategy(df):
    df['Signal'] = df['Close'].diff().apply(lambda x: 'Buy' if x > 0 else 'Sell')
    return df

if __name__ == "__main__":
    file_path = "forex_data.csv"  # Update with actual file
    df = load_data(file_path)
    trading_plan = simple_trading_strategy(df)
    print("Forex Trading Plan:")
    print(trading_plan[['Date', 'Close', 'Signal']])
