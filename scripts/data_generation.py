import pandas as pd
import numpy as np

np.random.seed(42)

n = 1000

df = pd.DataFrame({
    "customerID": ["C" + str(i) for i in range(1, n+1)],
    "tenure": np.random.randint(1, 60, n),
    "MonthlyCharges": np.random.randint(20, 150, n),
})

df["TotalCharges"] = df["tenure"] * df["MonthlyCharges"]

# Churn logic
df["Churn"] = np.where(
    (df["tenure"] < 12) & (df["MonthlyCharges"] > 80), 1, 0
)

df.to_csv("../data/raw/telco_raw.csv", index=False)

print("Raw dataset created!")