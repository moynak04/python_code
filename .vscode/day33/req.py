import requests

response = requests.get("https://api.example.com/data")

try:
    response.raise_for_status()

    data = response.json()

    print(data)

except requests.exceptions.HTTPError:
    print("HTTP error occurred!")

except requests.exceptions.ConnectionError:
    print("Connection error occurred!")

except requests.exceptions.JSONDecodeError:
    print("The response was not valid JSON!")