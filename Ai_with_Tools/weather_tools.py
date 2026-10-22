import requests
import os
from dotenv import load_dotenv
load_dotenv()

def get_weather(city, state, country):
    """
    Fetch live weather data using OpenWeather API.

    Args:
        city (str): City name
        state (str): State name/code
        country (str): Country code (Example: IN, US)
        api_key (str): OpenWeather API key

    Returns:
        dict: Weather details
    """

    # Create location query
    location = f"{city},{state},{country}"

    # OpenWeather API URL
    url = "https://api.openweathermap.org/data/2.5/weather"

    # Parameters
    params = {
        "q": location,
        "appid": os.getenv("WEATHER_API_KEY"),
        "units": "metric"  # Celsius
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        # Check for errors
        if response.status_code != 200:
            return {
                "error": data.get("message", "Unable to fetch weather")
            }

        # Extract useful information
        weather_info = {
            "city": data["name"],
            "country": data["sys"]["country"],
            "temperature": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "humidity": data["main"]["humidity"],
            "pressure": data["main"]["pressure"],
            "weather": data["weather"][0]["main"],
            "description": data["weather"][0]["description"],
            "wind_speed": data["wind"]["speed"]
        }

        return weather_info

    except Exception as e:
        return {
            "error": str(e)
        }


# Example Usage
# API_KEY = "YOUR_OPENWEATHER_API_KEY"

if __name__ == "__main__":
    
    result = get_weather(
        city="Chennai",
        state="Tamil Nadu",
        country="IN"
    )

    print(result)
    