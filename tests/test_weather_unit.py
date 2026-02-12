import sys
import pytest
from PyQt5.QtWidgets import QApplication
import weather

# Needed for PyQt widgets in tests
app = QApplication(sys.argv)



def test_get_weather_emoji():
    window = weather.WeatherApp()

    assert window.get_weather_emoji(800) == "🌞"
    assert window.get_weather_emoji(500) == "🌧️"
    assert window.get_weather_emoji(600) == "☃️"
    assert window.get_weather_emoji(200) == "⛈️"
    assert window.get_weather_emoji(999) == "❓"
