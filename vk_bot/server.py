from flask import Flask,request,json
from flask_sqlalchemy import SQLAlchemy
import os
from config import CONFIRMATION_TOKEN, TOKEN
from vk_bot import vk_group_api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

from vk_bot.messenger import message_validators,message_handlers

@app.route('/', methods=['GET', 'POST'])
def webhook():
    data = json.loads(request.data)
    if data['type'] == 'confirmation':
        return CONFIRMATION_TOKEN
    elif data['type'] == 'message_new':
        user_info = data['object']['user_id']
        vk_response = data['object']['body'].capitalize()
        message_processors = [
            (
                message_validators.is_add_mem_group_command,
                message_handlers.add_mem_group_handler
            ),
            (
                message_validators.is_delete_mem_group_command,
                message_handlers.delete_mem_group_handler
            ),
            (
                message_validators.is_post_memes_command,
                message_handlers.post_memes_handler
            ),
            (
                message_validators.is_post_memes_from_command,
                message_handlers.post_memes_from_handler
            ),
            (
                message_validators.is_post_list_of_memes_group_command,
                message_handlers.post_list_of_memes_groups_handler
            ),
            (
                message_validators.is_add_news_group_command,
                message_handlers.add_mem_group_handler
            ),
            (
                message_validators.is_delete_news_group_command,
                message_handlers.delete_news_group_handler
            ),
            (
                message_validators.is_post_news_command,
                message_handlers.post_news_handler
            ),
            (
                message_validators.is_post_news_from_command,
                message_handlers.post_news_from_handler
            ),
            (
                message_validators.is_post_list_of_news_group_command,
                message_handlers.is_post_list_of_news_group_handler                                                                                                                                                                                                                                                         
            ),
            (
                message_validators.is_parse_possible_photos_command,
                message_handlers.parse_possible_photos_handler
            ),
            (
                message_validators.is_imitate_newsfeed_command,
                message_handlers.imitate_newsfeed_handler
            ),
            (
                message_validators.is_parse_hidden_info_command,
                message_handlers.parse_hidden_info_handler
            ),
            (
                message_validators.is_post_weather_command,
                message_handlers.post_weather_handler
            )
        ]
        for message_validator, message_handler in message_processors:
            if message_validator(vk_response):
                message_handler(user_info, TOKEN, vk_response)
        return 'ok'


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
