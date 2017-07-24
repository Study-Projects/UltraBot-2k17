import urllib.request
import json


def fetch_weather(weather_key, city):
    url = 'https://api.apixu.com/v1/current.json?key=%s&q=%s' % (weather_key, city)
    site = urllib.request.urlopen(url)
    weather = json.loads(site.read().decode("utf-8"))
    current_weather = weather["current"]
    last_updated = current_weather["last_updated"]
    temp = current_weather["temp_c"]
    text = current_weather["condition"]["text"]
    wind = current_weather["wind_kph"]
    cloud = current_weather["cloud"]
    feelslike = current_weather["feelslike_c"]
    text_weather = """
    Погода проверялась: %s
    На улице %s
    Температура: %s
    Чувствуется: %s
    Облачность: %s
    Ветер: %s
    """ % (last_updated, text, temp, feelslike, cloud, wind)
    return text_weather