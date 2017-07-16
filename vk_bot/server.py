from flask import Flask,request,json
from flask_sqlalchemy import SQLAlchemy
import os
from config import CONFIRMATION_TOKEN, TOKEN
from vk_bot import vk_api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

from vk_bot.messenger import message_validators,message_handlers

@app.route('/', methods=['GET', 'POST'])
def webhook():
    data = json.loads(request.data)
    if data['type'] == 'message_new':
        vk_api.send_message("177940474", TOKEN, data)
    return 'ok'


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
