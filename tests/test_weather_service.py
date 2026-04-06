import pytest
from src.weather_service import WeatherService

def test_celsius_to_fahrenheit():
    # Caso 0°C
    assert WeatherService.celsius_to_fahrenheit(0) == 32
    # Caso 100°C
    assert WeatherService.celsius_to_fahrenheit(100) == 212
    # Caso -40°C = -40°F
    assert WeatherService.celsius_to_fahrenheit(-40) == -40

def test_kmh_to_ms():
    # Caso 3.6 km/h = 1 m/s
    assert round(WeatherService.kmh_to_ms(3.6), 2) == 1.0
    # Caso 0 km/h
    assert WeatherService.kmh_to_ms(0) == 0
    # Caso 36 km/h = 10 m/s
    assert round(WeatherService.kmh_to_ms(36), 2) == 10.0

def test_format_weather_summary():
    mock_data = {
        "latitude": 39.47,
        "longitude": -0.38,
        "current_weather": {
            "temperature": 20,
            "windspeed": 10
        }
    }
    summary = WeatherService.format_weather_summary(mock_data)
    
    assert summary["temperature"]["celsius"] == 20
    assert summary["temperature"]["fahrenheit"] == 68.0
    assert summary["wind_speed"]["kmh"] == 10
    assert summary["wind_speed"]["ms"] == 2.78
    assert summary["metadata"]["latitude"] == 39.47
    assert summary["metadata"]["longitude"] == -0.38
    assert "datetime" in summary["metadata"]
