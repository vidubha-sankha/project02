import utils.http_session
import utils.transport
import utils.session
import pandas as pd

df = pd.read_csv("outputs/predictions.csv")

# CLV calculation
df["CLV"] = df["MonthlyCharges"] * df["tenure"]

# Segmentation
def segment(row):
    if row['CLV'] > 3000 and row['Churn_Prob'] > 0.7:
        return "High Value - At Risk"
    elif row['CLV'] > 3000:
        return "High Value Loyal"
    elif row['Churn_Prob'] > 0.7:
        return "Low Value At Risk"
    else:
        return "Low Value Stable"

df['Segment'] = df.apply(segment, axis=1)

df.to_csv("data/processed/customer_churn_clv_project.csv", index=False)

print("CLV & segmentation completed!")