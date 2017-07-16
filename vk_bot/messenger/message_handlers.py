from vk_bot.server import db
from vk_bot import vk_api

def add_mem_group_handler(user_info, token, vk_response):
    group_name = vk_response.split()[2]
    group_id = vk_response.split()[3]
    db.session.add(group_name)
    db.session.add(group_id)
    db.session.commit() 


def delete_mem_group_handler(user_info, token):
    pass


def post_memes_handler(user_info, token):
    pass


def post_memes_from_handler(user_info, token):
    pass


def add_news_group_handler(user_info, token):
    pass


def delete_news_group_handler(user_info, token):
    pass


def post_news_handler(user_info, token):
    pass


def post_news_from_handler(user_info, token):
    pass


def parse_possible_photos_handler(user_info, token):
    pass


def imitate_newsfeed_handler(user_info, token):
    pass


def parse_hidden_info_handler(user_info, token):
    pass


def post_weater(user_info, token):
    pass