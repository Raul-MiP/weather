from fastapi import FastAPI, HTTPException
from src.weather_service import WeatherService

app = FastAPI(title="Weather Wrapper API")

@app.get("/api/v1/weather-summary")
async def get_weather_summary():
    try:
        raw_data = await WeatherService.get_weather_data()
        summary = WeatherService.format_weather_summary(raw_data)
        return summary
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
