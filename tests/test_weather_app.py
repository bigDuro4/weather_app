import sys
import pytest
from unittest.mock import patch
from PyQt5.QtWidgets import QApplication

import main  # your weather app file


# Needed so PyQt can run in test mode
app = QApplication(sys.argv)


# Fake OpenWeather API response
mock_weather_response = {
    "cod": 200,
    "main": {"temp": 300.15},  # Kelvin
    "weather": [
        {"description": "clear sky", "id": 800}
    ]
}


@patch("main.requests.get")
def test_get_weather_updates_ui(mock_get):
    """Integration test: API call + parsing + UI update"""

    # Mock API response
    mock_get.return_value.json.return_value = mock_weather_response
    mock_get.return_value.raise_for_status = lambda: None

    window = main.WeatherApp()
    window.city_input.setText("London")

    # Call the method directly (simulates button click)
    window.get_weather()

    # 300.15K → 80.6°F → rounds to 81
    assert window.temperature_label.text() == "81"
    assert window.description_label.text() == "clear sky"
    assert window.emoji_label.text() == "🌞"
