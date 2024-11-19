import os
import requests

api_key = os.getenv("API_KEY")
if not api_key:
    print("Error: No API key found. Please set the API_KEY environment variable.")
    exit(1)

city = "Croydon"
url = f"http://api.openweathermap.org/data/2.5/onecall/timemachine?lat=-26.2041&lon=28.0473&dt=1631026800&appid={api_key}"

response = requests.get(url)
data = response.json()
print(data)