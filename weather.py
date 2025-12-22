from dotenv import load_dotenv
import requests
import os

load_dotenv()

city = os.getenv("CITY")

#if not city:
   # city = input("Enter your city: ")

api_key = os.getenv("OPENWEATHER_API_KEY")

if not api_key:
    print("API key not found. Check your .env file.")
    exit()

url = "https://api.openweathermap.org/data/2.5/weather"
params = {
    "q": city,
    "units": "imperial",
    "appid": api_key
}

weather_data = requests.get(url, params=params)
data = weather_data.json()

# Always inspect failures
if weather_data.status_code != 200:
    print("Error:", data.get("message", "Unknown error"))
    exit()

weather = data["weather"][0]["main"]
temp = data["main"]["temp"]

print(f"The weather shows {weather}")
print(f"The temperature is {temp}°F")
