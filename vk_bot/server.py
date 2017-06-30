from flask import Flask
import os
from config import CONFIRMATION_TOKEN
from vk_bot.messenger import message_validators,message_handlers

app = Flask(__name__)


@app.route('/', methods=['POST'])
def webhook():
    messaging_event = ''
    message_processors = [
        (
            message_validators.is_add_mem_group_command(messaging_event),
            message_handlers.add_mem_group_handler()
        ),
        (
            message_validators.is_delete_mem_group_command(messaging_event),
            message_handlers.delete_mem_group_handler()
        ),
        (
            message_validators.is_post_memes_command(messaging_event),
            message_handlers.post_memes_handler()
        ),
        (
            message_validators.is_post_memes_from_command(messaging_event),
            message_handlers.post_memes_from_handler()
        ),
        (
            message_validators.is_add_news_group_command(messaging_event),
            message_handlers.add_mem_group_handler()
        ),
        (
            message_validators.is_delete_news_group_command(messaging_event),
            message_handlers.delete_news_group_handler()
        ),
        (
            message_validators.is_post_news_command(messaging_event),
            message_handlers.post_news_handler()
        ),
        (
            message_validators.is_post_news_from_command(messaging_event),
            message_handlers.post_news_from_handler()
        ),
        (
            message_validators.is_parse_possible_photos_command(messaging_event),
            message_handlers.parse_possible_photos_handler()
        ),
        (
            message_validators.is_imitate_newsfeed_command(messaging_event),
            message_handlers.imitate_newsfeed_handler()
        ),
        (
            message_validators.is_parse_hidden_info_command(messaging_event),
            message_handlers.parse_hidden_info_handler()
        )
    ]
    for message_validator, message_handler in message_processors:
        if message_validator(messaging_event):
            message_handler()
    return CONFIRMATION_TOKEN


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
