
# ==============================================================================================
# ==================== 04-09-2026 ==========================================================================

import requests
import os
from dotenv import load_dotenv
load_dotenv()

def get_weather(city,state,country):
    
    location = f"{city},{state},{country}"
    
    url="https://api.openweathermap.org/data/2.5/weather"
    
    params = {
        "q": location,
        "appid":os.getenv("GEMINI_API_KEY"),
        "units":"metric"
    }


    try:
        response = requests.get(url,params=params)
        data = response.json()
        
        if response.status_code != 200:
            return{
                "error":data.get("message","unable to fetch Weather details")
            }

        weather_info = {
            "city": data["name"],
            "country":data["sys"]["country"],
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
        return{
            "error":str(e)
        }

if __name__ == "__main__":
    result = get_weather(
        city="Chennai",state="Tamilnadu",country="India"
    )
    
    print(result)


# ==============================================================================================


# import requests
# import os
# from dotenv import load_dotenv
# load_dotenv()


# def get_weather(city,state,country):
    
#     location = f"{city},{state},{country}"
    
#     url = "https://api.openweathermap.org/data/2.5/weather"
    
#     params = {
#         "q":location,
#         "appid":os.getenv("WEATHER_API_KEY"),
#         "units":"metric"
#     }
    
#     try:
#         response = requests.get(url,params=params)
#         data = response.json()
        
#         print(data,'data-------------11111111')
        
#         if response.status_code != 200:
#             return {
#                 "error": data.get("message", "Unable to fetch Weather")
#             }
        
#         weather_info = {
#             "city": data["name"],
#             "country": data["sys"]["country"],
#             "temperature": data["main"]["temp"],
#             "feels_like": data["main"]["feels_like"],
#             "humidity": data["main"]["humidity"],
#             "pressure": data["main"]["pressure"],
#             "weather": data["weather"][0]["main"],
#             "description": data["weather"][0]["description"],
#             "wind_speed": data["wind"]["speed"]
            
#         }
#         return weather_info
#     except Exception as e:
#         return {
#             "error": str(e)
#         }

# if __name__ == "__main__":
#     result = get_weather(
#         city="Chennai",
#         state="Tamil Nadu",
#         country="IN"
#     )
    
#     print(result)


