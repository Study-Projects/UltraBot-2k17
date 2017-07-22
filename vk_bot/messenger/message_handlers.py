from vk_bot import vk_group_api, vk_user_api, weather_api
from vk_bot.server import db
from vk_bot.models.groups import User, Mems_group, News_group
from config import WEATHER_KEY

def add_group_handler(user_info, TOKEN, vk_response):
    user_id = User.query.filter_by(user_id=str(user_info)).first()
    if user_id is None:
        user_id = User(user_id=str(user_info))
        db.session.add(user_id)
    group_type = vk_response.split()[1]
    group_name = vk_response.split()[2]
    group_id = vk_response.split()[3]
    if group_type == "мемогруппу":
        for users_group in user_id.mems_groups.all():
            if users_group.group_name == group_name:
                message = "Эта группа уже добавлена"
                return vk_group_api.send_message(user_info, TOKEN, message)
        mems_group = Mems_group(group_name=group_name, group_id=group_id, owner=user_id)
        db.session.add(mems_group)
        db.session.commit()
    elif group_type == "новостигруппу":
        for users_group in user_id.news_groups.all():
            if users_group.group_name == group_name:
                message = "Эта группа уже добавлена"
                return vk_group_api.send_message(user_info, TOKEN, message)
        news_group = News_group(group_name=group_name, group_id=group_id, owner=user_id)
        db.session.add(news_group)
        db.session.commit()
    message = "Группа добавлена" 
    return vk_group_api.send_message(user_info, TOKEN, message) 


def delete_group_handler(user_info, TOKEN, vk_response):
    deleted_group = vk_response.split()[2]
    user_data = User.query.filter_by(user_id=str(user_info)).first()
    if user_data is None:
        message = "Чтобы пользоваться новостными функциями бота, добавьте новостигруппу или мемогруппу"
        return vk_group_api.send_message(user_info, TOKEN, message)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    deleted_group_type = vk_response.split()[1]
    if deleted_group_type == "мемогруппу":
        users_groups = user_data.mems_groups.all()
    elif deleted_group_type == "новостигруппу":
        users_groups = user_data.news_groups.all()
    if not users_groups:
        message = "Список групп пуст"
        return vk_group_api.send_message(user_info, TOKEN, message)
    for users_group in users_groups:
        if users_group.group_name == deleted_group:
            db.session.delete(users_group)
            db.session.commit()
            message = "Группа удалена"
            return vk_group_api.send_message(user_info, TOKEN, message)
    message = "Такой группы нет"
    return vk_group_api.send_message(user_info, TOKEN, message)


def post_handler(user_info, TOKEN, vk_response):
    post_type = vk_response.split()[2]
    user_data = User.query.filter_by(user_id=str(user_info)).first()
    if user_data is None:
        message = "Чтобы пользоваться новостными функциями бота, добавьте новостигруппу или мемогруппу"
        return vk_group_api.send_message(user_info, TOKEN, message)
    if post_type == "мемы":
        users_groups = user_data.mems_groups.all()
    elif post_type == "новости":
        users_groups = user_data.news_groups.all()
    if not users_groups:
        message = "Список групп пуст"
        return vk_group_api.send_message(user_info, TOKEN, message)
    for users_group in users_groups:
        group_number_id = vk_group_api.get_group_info(str(users_group.group_id)[15:])
        post_text, post_attachments = vk_user_api.parse_posts(group_number_id)
        vk_group_api.send_message(user_info, TOKEN, post_text, post_attachments)


def post_from_handler(user_info, TOKEN, vk_response):
    post_desirable_type = vk_response.split()[1]
    post_desirable_group = vk_response.split()[3]
    user_data = User.query.filter_by(user_id=str(user_info)).first()
    if user_data is None:
        message = "Чтобы пользоваться новостными функциями бота, добавьте новостигруппу или мемогруппу"
        return vk_group_api.send_message(user_info, TOKEN, message)
    if post_desirable_type == "мемы":
        users_groups = user_data.mems_groups.all()
    elif post_desirable_type == "новости":
        users_groups = user_data.news_groups.all()
    if not users_groups:
        message = "Список групп пуст"
        return vk_group_api.send_message(user_info, TOKEN, message)
    for users_group in users_groups:
        if users_group.group_name == post_desirable_group:
            group_number_id = vk_group_api.get_group_info(str(users_group.group_id)[15:])
            post_text, post_attachments = vk_user_api.parse_posts(group_number_id)
            vk_group_api.send_message(user_info, TOKEN, post_text, post_attachments)


def post_list_of_groups_handler(user_info, TOKEN, vk_response):
    desirable_list_group = vk_response.split()[2]
    user_data = User.query.filter_by(user_id=str(user_info)).first()
    if user_data is None:
        message = "Чтобы пользоваться новостными функциями бота, добавьте новостигруппу или мемогруппу"
        return vk_group_api.send_message(user_info, TOKEN, message)
    if desirable_list_group == "мемогрупп":
        users_groups = user_data.mems_groups.all()
    elif desirable_list_group == "новостигрупп":
        users_groups = user_data.news_groups.all()
    if not users_groups:
        message = "Список групп пуст"
        return vk_group_api.send_message(user_info, TOKEN, message)
    for users_group in users_groups:
        vk_group_api.send_message(user_info, TOKEN, users_group.group_name)


def delete_news_group_handler(user_info, TOKEN, vk_response):
    pass


def post_news_handler(user_info, TOKEN, vk_response):
    pass


def post_news_from_handler(user_info, TOKEN, vk_response):
    pass


def post_list_of_news_groups_handler(user_info, TOKEN, vk_response):
    pass


def parse_possible_photos_handler(user_info, TOKEN, vk_response):
    pass


def imitate_newsfeed_handler(user_info, TOKEN, vk_response):
    pass


def parse_hidden_info_handler(user_info, TOKEN, vk_response):
    pass


def post_weather_handler(user_info, TOKEN, vk_response):
    city = vk_response.split()[-1]
    weather_info = weather_api.fetch_weather(WEATHER_KEY, city)
    return vk_group_api.send_message(user_info, TOKEN, weather_info)


def default_handler(user_info, TOKEN, vk_response):
    message = 'Я тебя не понял. Возможно, ты опечатался.'
    return vk_group_api.send_message(user_info, TOKEN, message)

