import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()

longtitude = data["iss_position"]["longtitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longtitude, latitude)

print(iss_position)
print(response, data)

