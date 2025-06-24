# This script fetches and displays current weather information for a given city using the OpenWeatherMap API.
# It retrieves temperature, humidity, and weather conditions, and handles API errors gracefully.
# Requires the 'requests' library and a valid OpenWeatherMap API key.
# Usage: Run the script and enter a city name when prompted.
# Example: python weather_script.py
# Author: [Your Name]
# Date: 2025-06-24
#
# API documentation: https://openweathermap.org/current
#
# Note: Replace the API_KEY variable with your own key if needed.

# Fetch weather data from OpenWeatherMap API
import requests

def get_weather(city_name, api_key):
    """Fetch weather data for a given city from OpenWeatherMap API."""
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        main = data.get('main', {})
        weather = data.get('weather', [{}])[0]
        temp = main.get('temp')
        humidity = main.get('humidity')
        description = weather.get('description')
        print(f"Weather in {city_name}:")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {description}")
    else:
        print(f"Failed to get weather data for {city_name}. Error: {response.status_code}")

if __name__ == "__main__":
    API_KEY = "9e6caf64838051aa53274d6c93d0ab01"
    city = input("Enter city name: ")
    get_weather(city, API_KEY)
