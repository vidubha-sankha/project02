import pandas as pd

df = pd.read_csv("data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv")

# Check nulls
print(df.isnull().sum())

# Clean TotalCharges - replace spaces with 0
df["TotalCharges"] = df["TotalCharges"].replace(' ', '0')

# Remove nulls
df = df.dropna()

# Ensure correct types
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors='coerce').fillna(0)

df.to_csv("data/processed/customer_cleaned.csv", index=False)

print("Data cleaned!")