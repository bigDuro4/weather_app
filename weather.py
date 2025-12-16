import requests

api_key= 'd1a2f55240545f1ebb628d31445fff77'

user_input = input ("Enter Your City!:")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

weather= weather_data.json()['weather'][0]['main']
temp= weather_data.json()['main']['temp']

print(f"The weather shows {weather}")
print(f"The temperature is {temp}")
