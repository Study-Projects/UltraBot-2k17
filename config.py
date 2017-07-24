import os

#testing db
basedir = os.path.abspath(os.path.dirname(__file__))

#vk comunity tokens
TOKEN = os.environ.get('TOKEN')
CONFIRMATION_TOKEN = os.environ.get('CONFIRMATION_TOKEN')
BOT_GROUP_ID = os.environ.get('BOT_GROUP_ID')

#vk user tokens
APP_ID = os.environ.get('APP_ID')
LOGIN = os.environ.get('LOGIN')
PASSWORD = os.environ.get('PASSWORD')

#weather token
WEATHER_KEY = os.environ.get('WEATHER_KEY')
