# Practical 9: Generating data

import numpy as np
import pandas as pd

# Generate random data
def generate_data(rows=100):
    np.random.seed(42)
    data = {
        'ID': range(1, rows+1),
        'Value': np.random.randint(1, 100, rows),
        'Category': np.random.choice(['A', 'B', 'C'], rows)
    }
    return pd.DataFrame(data)

if __name__ == "__main__":
    df = generate_data()
    df.to_csv("generated_data.csv", index=False)
    print("Generated Data:")
    print(df.head())
