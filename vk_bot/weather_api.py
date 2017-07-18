import urllib.request
import json


def fetch_weather(weather_key, city):
    url = 'https://api.apixu.com/v1/current.json?key=%s&q=%s', (weather_key, city)
    with urllib.request.urlopen(url) as opened_url:
        data = json.loads(opened_url.read().decode())
        return data
    return
