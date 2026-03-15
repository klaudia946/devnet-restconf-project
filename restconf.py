import requests
import json

# URL przykładowego API
url = "https://jsonplaceholder.typicode.com/posts"

# nagłówki HTTP
headers = {
    "Content-Type": "application/json"
}

# dane które wysyłamy
data = {
    "title": "Network Automation",
    "body": "Creating interface configuration using API",
    "userId": 1
}

# konwersja do JSON
payload = json.dumps(data)

print("Sending API request...")

# wysłanie zapytania POST
response = requests.post(url, headers=headers, data=payload)

print("Status code:", response.status_code)

# sprawdzamy czy request się udał
if response.status_code == 201:
    print("Request successful!")
else:
    print("Request failed")

# pokazujemy odpowiedź serwera
print("Response from server:")
print(response.text)
