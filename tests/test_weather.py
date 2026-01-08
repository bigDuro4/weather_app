import os
import pytest

# IMPORTANT: adjust import if his file name differs
from weather import WeatherApp

from PyQt5.QtWidgets import QApplication


@pytest.fixture(scope="session")
def qapp():
    """Ensure a QApplication exists for PyQt widgets."""
    app = QApplication.instance()
    if app is None:
        app = QApplication([])
    return app


def test_get_weather_emoji_mapping(qapp):
    w = WeatherApp()

    assert w.get_weather_emoji(200) == "⛈️"   # thunderstorm range
    assert w.get_weather_emoji(800) == "🌞"   # clear
    assert w.get_weather_emoji(804) == "⛅"   # clouds
    assert w.get_weather_emoji(9999) == "❓"  # unknown


def test_display_weather_sets_labels(qapp):
    w = WeatherApp()

    # Kelvin example: 273.15K = 0C = 32F
    data = {
        "main": {"temp": 273.15},
        "weather": [{"description": "overcast clouds", "id": 804}],
    }

    w.display_weather(data)

    assert w.temperature_label.text() == "32"
    assert w.emoji_label.text() == "⛅"
    assert w.description_label.text() == "overcast clouds"


def test_get_weather_handles_missing_api_key_gracefully(qapp, monkeypatch):
    """
    This test is easiest AFTER he adds a missing-key check.
    Right now, the code will call the API with 'appid=None'.
    Recommend he adds:

        if not api_key:
            self.display_error("Missing OPENWEATHER_API_KEY")
            return

    Then this test will pass.
    """
    w = WeatherApp()
    w.city_input.setText("New York")

    monkeypatch.delenv("OPENWEATHER_API_KEY", raising=False)

    # After he adds the missing-key guard, calling get_weather should display this message.
    w.get_weather()
    assert "Missing OPENWEATHER_API_KEY" in w.temperature_label.text()