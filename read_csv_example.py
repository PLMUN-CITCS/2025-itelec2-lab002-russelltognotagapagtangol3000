import pandas as pd

# Load the cleaned CSV file
file_path = "E:\\python\\cleaned_customer_data.csv"
df = pd.read_csv(file_path)
print(df.head())  # Display the first few rows
