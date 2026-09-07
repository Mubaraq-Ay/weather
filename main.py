import requests

user_location = input('Enter a city: ')

url = f"https://geocoding-api.open-meteo.com/v1/search?name={user_location}"

response = requests.get(url)

data = response.json()
print(data['results'][0])
print(data.keys())
# print(f'Time: {data["hourly"]["time"][0]}')
# print(f'Temperature: {data["hourly"]["temperature_2m"][0]}°C')