from vk_bot import vk_group_api, vk_user_api, weather_api
from vk_bot.server import db
from vk_bot.models.groups import Mems
from config import WEATHER_KEY

def add_mem_group_handler(user_info, TOKEN, vk_response):
    group_name = vk_response.split()[2]
    group_id = vk_response.split()[3]
    db.session.add(Mems(group_name, group_id))
    db.session.commit()
    message = "Группа добавлена" 
    return vk_group_api.send_message(user_info, TOKEN, message) 


def delete_mem_group_handler(user_info, TOKEN, vk_response):
    group = Mems.query.filter_by(group_name=vk_response.split()[2]).first()
    if group is None:
        message = "Такой группы нет"
        return vk_group_api.send_message(user_info, TOKEN, message)
    db.session.delete(group)
    db.session.commit()
    message = "Группа удалена"
    return vk_group_api.send_message(user_info, TOKEN, message)

    
def post_memes_handler(user_info, TOKEN, vk_response):
    groups_letter_id = Mems.query.order_by(Mems.group_id)
    for group_letter_id in groups_letter_id:
        group_number_id = vk_group_api.get_group_info(str(group_letter_id)[16:-1])
        post_id = vk_user_api.parse_posts(group_number_id)
        message = 'https://vk.com/wall-%s_%s' % (group_number_id, post_id)
        vk_group_api.send_message(user_info, TOKEN, message) 


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


def post_weather_handler(user_info, TOKEN, vk_response):
    city = vk_response.split()[-1]
    weather_info = weather_api.fetch_weather(WEATHER_KEY, city)
    return vk_group_api.send_message(user_info, TOKEN, weather_info)
