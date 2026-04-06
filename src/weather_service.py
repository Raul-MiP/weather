import httpx
from datetime import datetime

class WeatherService:
    @staticmethod
    def celsius_to_fahrenheit(celsius: float) -> float:
        """Convierte grados Celsius a Fahrenheit."""
        return (celsius * 9/5) + 32

    @staticmethod
    def kmh_to_ms(kmh: float) -> float:
        """Convierte km/h a m/s."""
        return kmh / 3.6

    @staticmethod
    async def get_weather_data() -> dict:
        """Obtiene datos de la API de Open-Meteo."""
        url = "https://api.open-meteo.com/v1/forecast?latitude=39.47&longitude=-0.38&current_weather=true"
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            if response.status_code != 200:
                raise Exception("Error al consultar el servicio meteorológico externo.")
            return response.json()

    @classmethod
    def format_weather_summary(cls, data: dict) -> dict:
        """Formatea la respuesta según los requisitos."""
        current_weather = data.get("current_weather", {})
        temp_c = current_weather.get("temperature")
        wind_kmh = current_weather.get("windspeed")
        
        return {
            "temperature": {
                "celsius": temp_c,
                "fahrenheit": round(cls.celsius_to_fahrenheit(temp_c), 2)
            },
            "wind_speed": {
                "kmh": wind_kmh,
                "ms": round(cls.kmh_to_ms(wind_kmh), 2)
            },
            "metadata": {
                "datetime": datetime.now().isoformat(),
                "latitude": data.get("latitude"),
                "longitude": data.get("longitude")
            }
        }
