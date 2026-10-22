



# ==============================================================================================
# ==================== 04-09-2026 ==========================================================================

def tools():
    return [ 
        {
            "name":"get_weather_data",
            "description":"Fetch current weather data for a given location",
            "parameters":{
                "type": "object",
                "properties": {
                    "city" : {"type": "string", "description": "City name"},
                    "state": {"type": "string", "description": "State name or State Code"},
                    "country": {"type": "string", "description": "Country code in ISO 3166-1 alpha-2 format (Example: IN, US)"}
                    
                },
                "required":["city","state","country"],
            }
        }
            
    ]







# ==============================================================================================





# def tools():
    return [
        {
            "name":"get_weather_data",
            "description": "Fetch current weather data for a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string", "description": "City name"},
                    "state": {
                        "type": "string",
                        "description": "State name or state code",
                    },
                    "country": {
                        "type": "string",
                        "description": "Country code in ISO 3166-1 alpha-2 format (Example: IN, US)",
                    },
                },
                "required": ["city","state", "country"],
            },
        }
    ]
    
    
    
    
    
    
    
    