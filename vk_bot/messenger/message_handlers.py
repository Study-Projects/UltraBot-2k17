from vk_bot import vk_group_api, vk_user_api, weather_api
from vk_bot.server import db
from vk_bot.models.groups import User, Mems_group, News_group
from config import WEATHER_KEY

def add_mem_group_handler(user_info, TOKEN, vk_response):
    if User.query.filter_by(user_id=str(user_info)).first() is None:
        user_id = User(user_id=str(user_info))
        db.session.add(user_id)
    else:
        user_id = User.query.filter_by(user_id=str(user_info)).first()
    group_name = vk_response.split()[2]
    group_id = vk_response.split()[3]
    mems_group = Mems_group(group_name=group_name, group_id=group_id, owner=user_id)
    db.session.add(mems_group)
    db.session.commit()
    message = "Группа добавлена" 
    return vk_group_api.send_message(user_info, TOKEN, message) 


def delete_mem_group_handler(user_info, TOKEN, vk_response):
    deleted_group = vk_response.split()[2]
    user_data = User.query.filter_by(user_id=str(user_info)).first()
    if user_data is None:
        message = "Чтобы пользоваться новостными функциями бота, добавьте новостигруппу или мемогруппу"
        return vk_group_api.send_message(user_info, TOKEN, message)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    if not user_data.mems_groups.all():
        message = "Список групп пуст"
        return vk_group_api.send_message(user_info, TOKEN, message)
    for users_group in user_data.mems_groups.all():
        if users_group.group_name == deleted_group:
            db.session.delete(users_group)
            db.session.commit()
            message = "Группа удалена"
            return vk_group_api.send_message(user_info, TOKEN, message)
    message = "Такой группы нет"
    return vk_group_api.send_message(user_info, TOKEN, message)
    

def post_memes_handler(user_info, TOKEN, vk_response):
    user_data = User.query.filter_by(user_id=str(user_info)).first()
    if user_data is None:
        message = "Чтобы пользоваться новостными функциями бота, добавьте новостигруппу или мемогруппу"
        return vk_group_api.send_message(user_info, TOKEN, message)
    if not user_data.mems_groups.all():
        message = "Список групп пуст"
        return vk_group_api.send_message(user_info, TOKEN, message)
    for users_group in user_data.mems_groups.all():
        group_number_id = vk_group_api.get_group_info(str(users_group.group_id)[15:])
        post_id = vk_user_api.parse_posts(group_number_id)
        message = 'https://vk.com/wall-%s_%s' % (group_number_id, post_id)
        vk_group_api.send_message(user_info, TOKEN, message) 


def post_memes_from_handler(user_info, TOKEN, vk_response):
    post_desirable_group = vk_response.split()[3]
    user_data = User.query.filter_by(user_id=str(user_info)).first()
    if user_data is None:
        message = "Чтобы пользоваться новостными функциями бота, добавьте новостигруппу или мемогруппу"
        return vk_group_api.send_message(user_info, TOKEN, message)
    if not user_data.mems_groups.all():
        message = "Список групп пуст"
        return vk_group_api.send_message(user_info, TOKEN, message)
    for users_group in user_data.mems_groups.all():
        if users_group.group_name == post_desirable_group:
            group_number_id = vk_group_api.get_group_info(str(users_group.group_id)[15:])
            post_id = vk_user_api.parse_posts(group_number_id)
            message = 'https://vk.com/wall-%s_%s' % (group_number_id, post_id)
            vk_group_api.send_message(user_info, TOKEN, message) 


def post_list_of_memes_groups_handler(user_info, TOKEN, vk_response):
    user_data = User.query.filter_by(user_id=str(user_info)).first()
    if user_data is None:
        message = "Чтобы пользоваться новостными функциями бота, добавьте новостигруппу или мемогруппу"
        return vk_group_api.send_message(user_info, TOKEN, message)
    if not user_data.mems_groups.all():
        message = "Список групп пуст"
        return vk_group_api.send_message(user_info, TOKEN, message)
    for users_group in user_data.mems_groups.all():
        vk_group_api.send_message(user_info, TOKEN, users_group.group_name)


def add_news_group_handler(user_info, token):
    pass


def delete_news_group_handler(user_info, token):
    pass


def post_news_handler(user_info, token):
    pass


def post_news_from_handler(user_info, token):
    pass


def post_list_of_news_groups_handler(user_info, TOKEN, vk_response):
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

