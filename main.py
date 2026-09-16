import requests

user_location = input('Enter a city: ')

url = f"https://geocoding-api.open-meteo.com/v1/search?name={user_location}"

response = requests.get(url)

data = response.json()
longitude = data['results'][0]['longitude']
latitude = data['results'][0]['latitude']

forecast_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m"
forecast_response = requests.get(forecast_url)

forecast_data = forecast_response.json()
time = forecast_data['hourly']['time'][0]
temperature = forecast_data['hourly']['temperature_2m'][0]

print(f"""
    Today's weather
    -----------------
    Location: {user_location}
    Time:   {time}
    Temperature: {temperature}°C
""")