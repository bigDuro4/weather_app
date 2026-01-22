# Weather App (PyQt5 + OpenWeather)

## Overview

A simple PyQt5 desktop weather application that lets users enter a city and view:

- Temperature (°F)
- Weather description
- A matching weather emoji

Data is fetched from the OpenWeather API.

## Demo 
Go to Openweather.org> Sign in> My Api Keys> Generate


## Prerequisites

- Python 3.10+ (or your version)
- An OpenWeather API key

## Installation

### 1) Clone the repo

```bash
git clone https://github.com/bigDuro4/weather_app.git
cd weather_app
```
### 2) Retreive API Key
- Go to openweathermap.org
  <img width="2164" height="562" alt="image" src="https://github.com/user-attachments/assets/ec450b05-00e0-4fd7-b5e4-2056f3f3e810" />
- Create an account
- Once you sign in go to API Keys and create
  <img width="2171" height="678" alt="image" src="https://github.com/user-attachments/assets/eac173da-1278-475c-a5d6-3729198e1af7" />
- You can then use this in your dotenv file 



### 3) Create & activate a virtual environment

```bash
python -m venv .venv
# mac/linux
source .venv/bin/activate
# windows
.venv\Scripts\activate
```

### 3) Install dependencies

```bash
pip install -r requirements.txt
```

## Create a .env file in the project root and store the key:

```bash
OPENWEATHER_API_KEY=your_key_here
```

## Run the app

```bash
python weather.py
```

## Run tests

```bash
pytest -q
```

#### or run pytest as a module

```bash
python -m pytest
```

## Project Structure (Configure the way you prefer. You can follow this example)

```bash
weather_app/
  weather.py
  requirements.txt
  tests/
    test_weather.py
```
