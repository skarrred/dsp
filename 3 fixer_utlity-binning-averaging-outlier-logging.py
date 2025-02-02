#fixer utitlity
import string
import datetime as dt

def remove_spaces(text):
    return text.strip()

def remove_nonprintable(text):
    printable = set(string.printable)
    return ''.join(filter(lambda x: x in printable, text))

def reformat_date(date_str):
    date_obj = dt.datetime.strptime(date_str, '%Y-%m-%d')
    return date_obj.strftime('%d %B %Y')

if __name__ == "__main__":
    sample_text = "  Data Science with spaces  "
    sample_bad_chars = "Data\x00Science with\x02 funny characters"
    sample_date = "2025-02-01"

    print("Fixed Text:", remove_spaces(sample_text))
    print("Fixed Characters:", remove_nonprintable(sample_bad_chars))
    print("Reformatted Date:", reformat_date(sample_date))



#binning
import pandas as pd
import numpy as np

def data_binning(data, bins):
    labels = [f'Bin_{i+1}' for i in range(len(bins)-1)]
    data['Binned'] = pd.cut(data['value'], bins=bins, labels=labels)
    return data

if __name__ == "__main__":
    df = pd.DataFrame({'value': [5, 15, 25, 35, 45]})
    bins = [0, 10, 20, 30, 40, 50]
    print("Binned Data:")
    print(data_binning(df, bins))




#averaging
import pandas as pd

def averaging_data(data):
    return data.groupby('category').mean().reset_index()

if __name__ == "__main__":
    df = pd.DataFrame({'category': ['A', 'B', 'A', 'B'], 'value': [10, 20, 15, 25]})
    print("Averaged Data:")
    print(averaging_data(df))




#outlier detection
import pandas as pd

def detect_outliers(data):
    q1 = data['value'].quantile(0.25)
    q3 = data['value'].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    return data[(data['value'] < lower_bound) | (data['value'] > upper_bound)]

if __name__ == "__main__":
    df = pd.DataFrame({'value': [10, 20, 15, 25, 100, -5]})
    print("Outliers:")
    print(detect_outliers(df))




#logging data
import pandas as pd

def log_data(data, log_file):
    with open(log_file, 'w') as f:
        f.write(data.to_string())
    print(f"Data logged to {log_file}")

if __name__ == "__main__":
    df = pd.DataFrame({'category': ['A', 'B', 'A', 'B'], 'value': [10, 20, 15, 25]})
    log_data(df, "data_log.txt")
