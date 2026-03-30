import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import pickle

data = pd.DataFrame({
    'applicant_income': [2500, 4000, 3000, 5000, 3500, 4500, 6000, 3200, 7000, 8000],
    'credit_score': [650, 700, 680, 720, 690, 710, 740, 675, 760, 800],
    'loan_amount': [100000, 200000, 150000, 250000, 180000, 220000, 300000, 160000, 350000, 400000],
    'loan_term_months': [120, 240, 180, 360, 180, 240, 360, 180, 300, 360],
    'num_dependents': [0, 1, 2, 0, 1, 2, 0, 1, 0, 0],
    'loan_approved': [0, 1, 1, 1, 0, 1, 1, 0, 1, 1]
})

X = data[['applicant_income', 'credit_score', 'loan_amount', 'loan_term_months', 'num_dependents']]
y = data['loan_approved']

# 🔥 IMPORTANT FIX
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LogisticRegression())
])

pipeline.fit(X, y)

pickle.dump(pipeline, open('loan_model.pkl', 'wb'))

print("Model fixed & saved!")