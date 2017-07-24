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
    if is_memes_group(group_type):
        added_groups = user_id.mems_groups.all()
        group_to_add = Mems_group(group_name=group_name, group_id=group_id, owner=user_id)
    elif is_news_group(group_type):
        added_groups = user_id.news_groups.all()
        group_to_add = News_group(group_name=group_name, group_id=group_id, owner=user_id)
    else:
        message = "Не понял тип группы"
        return vk_group_api.send_message(user_info, TOKEN, message)
    for users_group in added_groups:
        if users_group.group_name == group_name:
            message = "Эта группа уже добавлена"
            return vk_group_api.send_message(user_info, TOKEN, message)
    db.session.add(group_to_add)
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
    if is_memes_group(deleted_group_type):
        users_groups = user_data.mems_groups.all()
    elif is_news_group(deleted_group_type):
        users_groups = user_data.news_groups.all()
    else:
        message = "Не понял тип группы"
        return vk_group_api.send_message(user_info, TOKEN, message)
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
    else:
        message = "Не понял тип поста"
        return vk_group_api.send_message(user_info, TOKEN, message)
    if not users_groups:
        message = "Список групп пуст"
        return vk_group_api.send_message(user_info, TOKEN, message)
    for users_group in users_groups:
        group_number_id = vk_group_api.get_group_info(str(users_group.group_id)[15:])
        posts_to_send = vk_user_api.parse_posts(group_number_id)
        for post_text, post_attachments in posts_to_send:
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
    else:
        message = "Не понял тип поста"
        return vk_group_api.send_message(user_info, TOKEN, message)
    if not users_groups:
        message = "Список групп пуст"
        return vk_group_api.send_message(user_info, TOKEN, message)
    for users_group in users_groups:
        if users_group.group_name == post_desirable_group:
            group_number_id = vk_group_api.get_group_info(str(users_group.group_id)[15:])
            posts_to_send = vk_user_api.parse_posts(group_number_id)
            for post_text, post_attachments in posts_to_send:
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
    else:
        message = "Не понял тип поста"
        return vk_group_api.send_message(user_info, TOKEN, message)
    if not users_groups:
        message = "Список групп пуст"
        return vk_group_api.send_message(user_info, TOKEN, message)
    for users_group in users_groups:
        vk_group_api.send_message(user_info, TOKEN, users_group.group_name)


def delete_all_groups_handler(user_info, TOKEN, vk_response):
    user_data = User.query.filter_by(user_id=str(user_info)).first()
    if user_data is None:
        message = "Чтобы пользоваться новостными функциями бота, добавьте новостигруппу или мемогруппу"
        return vk_group_api.send_message(user_info, TOKEN, message)
    deleted_group_type = vk_response.split()[-1]
    if is_memes_group(deleted_group_type):
        users_groups = user_data.mems_groups.all()
    elif is_news_group(deleted_group_type):
        users_groups = user_data.news_groups.all()
    else:
        message = "Не понял тип групп"
        return vk_group_api.send_message(user_info, TOKEN, message)
    if not users_groups:
        message = "Список групп пуст"
        return vk_group_api.send_message(user_info, TOKEN, message)
    for users_group in users_groups:
        db.session.delete(users_group)
        db.session.commit()
    message = "Группы удалены"
    return vk_group_api.send_message(user_info, TOKEN, message)


def help_handler(user_info, TOKEN, vk_response):
    message = """Добавь (мемо/новости)группу <название группы> <ссылка>
    Удали (мемо/новости)группу <название группы>
    Удали все (мемо/новости)группы
    Пришли свежие (мемы/новости)
    Пришли (мемы/новости) из <название группы>
    Пришли список (мемо/новости)групп
    Погода <город>"""
    return vk_group_api.send_message(user_info, TOKEN, message)


def parse_possible_photos_handler(user_info, TOKEN, vk_response):
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


def is_memes_group(group_type):
    return 'мемогруп' in group_type


def is_news_group(group_type):
    return 'новостигруп' in group_type