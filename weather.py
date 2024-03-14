import requests


def get_weather(city_name, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

    response = requests.get(url)
    weather_data = response.json()

    if weather_data["cod"] != 404:
        main_data = weather_data["main"]
        current_temperature = main_data["temp"]
        current_pressure = main_data["pressure"]
        current_humidity = main_data["humidity"]
        weather_description = weather_data["weather"][0]["description"]
        return {
            "Temperature": current_temperature,
            "Pressure": current_pressure,
            "Humidity": current_humidity,
            "Description": weather_description
        }
    else:
        return "City Not Found"


# Example usage
api_key = "7e6ca0b8d067429e944a212d20946f9a"  # Replace with your API key
city_name = "Berlin"  # Replace with your city
weather_info = get_weather(city_name, api_key)
print(weather_info)
