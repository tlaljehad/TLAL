
from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# تحميل النموذج المدرب
model = joblib.load('heart_disease_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    input_data = pd.DataFrame([data])
    prediction = model.predict(input_data)
    result = int(prediction[0])
    return jsonify({'prediction': result})

if __name__ == '__main__':
    app.run(debug=True)
