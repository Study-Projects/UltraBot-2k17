import urllib.request


def fetch_weather(weather_key, city):
    url = 'https://api.apixu.com/v1/current.json?key=%s&q=%s', (weather_key, city)
    with urllib.request.urlopen(url) as site:
        data = site.read()
        return data
