import requests

url = "http://127.0.0.1:5000/recommend"
payload = {
    "soil_type": "loamy",
    "rainfall_level": "medium",
    "region": "Nairobi"
}
headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)
print("Status Code:", response.status_code)
print("Response Body:", response.text)
