
from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd

app = Flask(__name__)

# تحميل النموذج
model = joblib.load('heart_disease_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form.to_dict()
    input_data = pd.DataFrame([data])
    input_data = input_data.astype(float)
    prediction = model.predict(input_data)
    result = 'مصاب بمرض القلب' if prediction[0] == 1 else 'سليم'
    return render_template('index.html', prediction_text=f'النتيجة: {result}')

if __name__ == '__main__':
    app.run(debug=True)
