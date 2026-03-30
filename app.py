from flask import Flask, request, jsonify
import pickle
import os

app = Flask(__name__)
model = pickle.load(open('loan_model.pkl', 'rb'))

@app.route('/')
def home():
    return 'Loan Approval Prediction API running'

@app.route('/predict', methods=["POST"])
def predict():
    data = request.json
    features = [[
        data['applicant_income'], 
        data['credit_score'], 
        data['loan_amount'], 
        data['loan_term_months'], 
        data['num_dependents']
    ]]
    
    prediction = model.predict(features)[0]
    return jsonify({'loan_approval_prediction': int(prediction)})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)