import requests

url = "http://127.0.0.1:5000/predict"

data = {
    "age": 55,
    "trestbps": 140,
    "chol": 250,
    "fbs": 0,
    "thalach": 150,
    "exang": 0,
    "oldpeak": 1.2,
    "sex_num": 1,
    "dataset_num": 1,
    "cp_num": 0,
    "restecg_num": 1,
    "slope_num": 2
}

response = requests.post(url, json=data)

print(response.json())
