import os

import requests


def get_weather(city, country):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': f'{city},{country}',
        'appid': os.getenv("WEATHER_API_KEY"),
        'units': 'metric',
    }
    response = requests.get(base_url, params=params)
    return response.json()
