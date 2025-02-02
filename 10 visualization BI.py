# Practical 10: Data visualization using Power BI

# Note: Power BI visualizations are created using the Power BI interface.
# Below is a Python script to export data for visualization in Power BI.

import pandas as pd

# Load data
def load_data(file_path):
    return pd.read_csv(file_path)

if __name__ == "__main__":
    file_path = "data.csv"  # Update with actual file
    df = load_data(file_path)
    df.to_csv("powerbi_data.csv", index=False)
    print("Data exported for Power BI visualization.")
