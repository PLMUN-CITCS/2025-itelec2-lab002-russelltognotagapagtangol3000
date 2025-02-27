import pandas as pd

# Load data
df = pd.read_csv("data.csv")

# 1. Fill missing values
df["Age"].fillna(df["Age"].mean(), inplace=True)  # Fill missing age with the average
df["Purchase_Amount"].fillna(df["Purchase_Amount"].median(), inplace=True)  # Median for amount
df["Purchase_Date"].fillna("01/01/2024", inplace=True)  # Placeholder for missing date
df["Category"].fillna("Unknown", inplace=True)  # Fill category with placeholder

# 2. Standardize purchase dates
df["Purchase_Date"] = pd.to_datetime(df["Purchase_Date"], errors="coerce").dt.strftime("%d/%m/%Y")

# 3. Handle duplicates
df.drop_duplicates(inplace=True)

# Save cleaned data
df.to_csv("cleaned_data.csv", index=False)
print("Data cleaned and saved as 'cleaned_data.csv'")
