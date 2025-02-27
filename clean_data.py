import pandas as pd

try:
    df = pd.read_csv("data.csv", on_bad_lines='skip')
    print("Dataset loaded successfully.")
    print(df.head())
except Exception as e:
    print(f"Error reading the file: {e}")
