import requests
from datetime import datetime

MY_LAT = 51.507351
MY_LONG = -0.127758

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
#
# data = response.json()
#
# longitude = response.json()["iss_position"]["longitude"]
#
# latitude = response.json()["iss_position"]["latitude"]
#
#
# iss_position = (longitude,latitude)
#
# print(iss_position)

parameters = {
    "lat" : MY_LAT,
    "lng" : MY_LONG,
    "formatted" : 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
time_now = datetime.now()

print(sunrise)
print(time_now.hour)