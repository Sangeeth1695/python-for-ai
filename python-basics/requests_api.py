import requests

# We need coordinates to get weather data
latitude = 48.85  # Paris latitude
longitude = 2.35  # Paris longitude

# Build the API URL with our parameters
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

# Make the request
response = requests.get(url)
data = response.json()

print(data)
type(data)

data["latitude"]
data.keys()

for key in data.keys():
    print(f"{key}: {data[key]}")


def get_weather(latitude, longitude):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"
    response = requests.get(url)
    data = response.json()
    return data["current"]["temperature_2m"]


paris_temp = get_weather(48.85, 2.35)
london_temp = get_weather(51.50, -0.12)
tokyo_temp = get_weather(35.68, 139.69)

print(f"Paris: {paris_temp} degree Celsius")
print(f"London: {london_temp} degree Celsius")
print(f"Tokyo: {tokyo_temp} degree Celsius")
