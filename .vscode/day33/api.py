import requests

parameters = {
    "city": "Bangalore"
}

response = requests.get(
    "https://api.example.com/weather",
    params=parameters
)

print(response.url)