from flask import Flask,request,json
from flask_sqlalchemy import SQLAlchemy
import os
from config import CONFIRMATION_TOKEN, TOKEN
from vk_bot import vk_api

app = Flask(__name__)

from vk_bot.messenger import message_validators,message_handlers

@app.route('/', methods=['GET', 'POST'])
def webhook():
    data = json.loads(request.data)
    return data


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
