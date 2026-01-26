import sys
import pytest
from PyQt5.QtWidgets import QApplication
import main

# Needed for PyQt widgets in tests
app = QApplication(sys.argv)


def test_kelvin_to_fahrenheit():
    window = main.WeatherApp()

    assert round(window.kelvin_to_fahrenheit(273.15), 1) == 32.0  # freezing
    assert round(window.kelvin_to_fahrenheit(300.15), 1) == 80.6  # warm day
    assert round(window.kelvin_to_fahrenheit(255.37), 1) == 0.0   # 0°F


def test_get_weather_emoji():
    window = main.WeatherApp()

    assert window.get_weather_emoji(800) == "🌞"
    assert window.get_weather_emoji(500) == "🌧️"
    assert window.get_weather_emoji(600) == "☃️"
    assert window.get_weather_emoji(200) == "⛈️"
    assert window.get_weather_emoji(999) == "❓"
