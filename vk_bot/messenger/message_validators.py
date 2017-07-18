def is_add_mem_group_command(messaging_event):
    validators = ['Добавь мемогруппу']
    return validate(validators, messaging_event)


def is_delete_mem_group_command(messaging_event):
    validators = ['Удали мемогруппу']
    return validate(validators, messaging_event)


def is_post_memes_command(messaging_event):
    validators = ['Пришли свежие мемы']
    return validate(validators, messaging_event)


def is_post_memes_from_command(messaging_event):
    validators = ['Пришли мемы из']
    return validate(validators, messaging_event)


def is_add_news_group_command(messaging_event):
    validators = ['Добавь новостигруппу']
    return validate(validators, messaging_event)


def is_delete_news_group_command(messaging_event):
    validators = ['Удали новостигруппу']
    return validate(validators, messaging_event)


def is_post_news_command(messaging_event):
    validators = ['Пришли свежие новости']
    return validate(validators, messaging_event)


def is_post_news_from_command(messaging_event):
    validators = ['Пришли новости из']
    return validate(validators, messaging_event)


def is_parse_possible_photos_command(messaging_event):
    validators = ['Найди фото']
    return validate(validators, messaging_event)


def is_imitate_newsfeed_command(messaging_event):
    validators = ['Имитируй']
    return validate(validators, messaging_event)


def is_parse_hidden_info_command(messaging_event):
    validators = ['Найди инфо']
    return validate(validators, messaging_event)


def is_post_weather_command(messaging_event):
    validators = ['Погода']
    return validate(validators, messaging_event)


def validate(validators, messaging_event):
    for validator in validators:
        if validator in messaging_event:
            return True
    return False
