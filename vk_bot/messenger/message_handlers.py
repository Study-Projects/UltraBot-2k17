from vk_bot.models import base
from vk_bot import vk_api
from vk_bot.models import groups

def add_mem_group_handler(user_info, token, vk_response):
    group_name = vk_response.split()[2]
    group_id = vk_response.split()[3]
    base.db.session.add(groups.Mems(group_name, group_id))
    base.db.session.commit()
    return vk_api.send_message(user_info, token, "Group added") 


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