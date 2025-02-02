import pandas as pd

# Load data from CSV
def load_data(file_path):
    df = pd.read_csv(file_path, encoding="latin-1", error_bad_lines=False)
    return df

# Perform error handling
def handle_errors(df):
    print("Checking for missing values:")
    print(df.isnull().sum())
    print("\nDropping rows with missing values:")
    df_cleaned = df.dropna()
    print(df_cleaned.head())

if __name__ == "__main__":
    file_path = "C:/VKHCG/01-Vermeulen/00-RawData/IP_DATA_ALL.csv"
    df = load_data(file_path)
    handle_errors(df)
