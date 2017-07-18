import urllib.request
import json


def fetch_weather(weather_key, city):
    url = 'https://api.apixu.com/v1/current.json?key=%s&q=%s' % (weather_key, city)
    site = urllib.request.urlopen(url)
    return site.read()
