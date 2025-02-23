import requests
from api_key import api_key

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = api_key
LATITUDE = 49.783699
LONGITUDE = 22.768030

parameters = {
    "lat" : LATITUDE,
    "lon": LONGITUDE,
    "appid" : API_KEY,
    "cnt" : 4
}

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()

weather_data = response.json()

weather_list = weather_data["list"]

will_rain = False

for _ in weather_list:
    if weather_list[0]["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella")
else:
    print("No need to take umbrella")
