import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle

# Dummy data (simplified loan data)
data = {
    'Gender': [1, 0, 1, 1],
    'Married': [1, 0, 1, 1],
    'Education': [0, 1, 0, 0],
    'ApplicantIncome': [5000, 3000, 7000, 4000],
    'LoanAmount': [150, 100, 200, 120],
    'Credit_History': [1, 0, 1, 1],
    'Loan_Status': [1, 0, 1, 1]
}
df = pd.DataFrame(data)

X = df.drop("Loan_Status", axis=1)
y = df["Loan_Status"]

model = LogisticRegression()
model.fit(X, y)

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
