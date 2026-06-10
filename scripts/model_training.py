import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("data/processed/customer_cleaned.csv")

X = df[['tenure', 'MonthlyCharges']]
y = df['Churn']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LogisticRegression()
model.fit(X_train, y_train)

df['Churn_Prob'] = model.predict_proba(X)[:,1]

df.to_csv("outputs/predictions.csv", index=False)

print("Model trained & predictions saved!")